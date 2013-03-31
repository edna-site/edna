# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__="Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


import os.path
import time
import sys
import json
import traceback
import shutil
import socket

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString
from XSDataCommon import  XSDataInteger, XSDataTime, XSDataFloat

from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataResCutoff
from XSDataAutoproc import XSDataMinimalXdsIn
from XSDataAutoproc import XSDataXdsGenerateInput
from XSDataAutoproc import XSDataXdsOutputFile
from XSDataAutoproc import XSDataXscaleInput
from XSDataAutoproc import XSDataXscaleInputFile
from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataAutoprocImport

edFactoryPlugin.loadModule('XSDataWaitFilev1_0')
from XSDataWaitFilev1_0 import XSDataInputWaitFile

edFactoryPlugin.loadModule('XSDataISPyBv1_4')
# plugin input/output
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc

# what actually goes inside
from XSDataISPyBv1_4 import AutoProcContainer, AutoProc, AutoProcScalingContainer
from XSDataISPyBv1_4 import AutoProcScaling, AutoProcScalingStatistics
from XSDataISPyBv1_4 import AutoProcIntegrationContainer, AutoProcIntegration
from XSDataISPyBv1_4 import AutoProcProgramContainer, AutoProcProgram
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import Image
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc

# status updates
from XSDataISPyBv1_4 import AutoProcStatus
from XSDataISPyBv1_4 import  XSDataInputStoreAutoProcStatus

from xdscfgparser import parse_xds_file, dump_xds_file

import autoproclog
autoproclog.LOG_SERVER='rnice655:5000'

WAIT_FOR_FRAME_TIMEOUT=240 #max uses 50*5

# We used to go through the results directory and add all files to the
# ispyb upload. Now some files should not be uploaded, so we'll
# discriminate by extension for now
ISPYB_UPLOAD_EXTENSIONS=['.lp', '.mtz', '.log', '.inp']

class EDPluginControlAutoproc(EDPluginControl):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataAutoprocInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoproc.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")

        # save the root path (where the initial xds.inp is) for later use
        self.root_dir = os.path.abspath(os.path.dirname(self.dataInput.input_file.path.value))

        # at least check for the xds input file existence before
        # trying to start anything even if the first xds run does it
        # anyway
        if not os.path.isfile(self.dataInput.input_file.path.value):
            EDVerbose.ERROR('the specified input file does not exist')
            self.setFailure()
            # setFailure does not prevent preProcess/process/etc from running
            raise Exception('EDNA FAILURE')
        else:
            # copy it to our dir and modify our input
            newpath = os.path.join(self.getWorkingDirectory(),
                                   os.path.basename(self.dataInput.input_file.path.value))
            shutil.copyfile(self.dataInput.input_file.path.value,
                            newpath)
            self.dataInput.input_file.path = XSDataString(newpath)

    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG('EDPluginControlAutoproc.preProcess starting')
        self.DEBUG('failure state is currently {0}'.format(self.isFailure()))

        # for info to send to the autoproc stats server
        self.custom_stats = dict(creation_time=time.time(),
                                 processing_type='edna fastproc',
                                 datacollect_id=self.dataInput.data_collection_id.value,
                                 comments='running on {0}'.format(socket.gethostname()))


        data_in = self.dataInput
        xds_in = XSDataMinimalXdsIn()
        xds_in.input_file = data_in.input_file.path
        xds_in.spacegroup = data_in.spacegroup
        xds_in.unit_cell = data_in.unit_cell

        self.log_file_path = os.path.join(self.root_dir, 'stats.json')
        self.DEBUG('will log timing information to {0}'.format(self.log_file_path))
        self.stats = dict()

        # Get the image prefix from the directory name
        # XXX: This is horrible
        try:
            self.image_prefix = '_'.join(os.path.basename(self.root_dir).split('_')[1:-1])
        except Exception:
            self.image_prefix = ''

        self.results_dir = os.path.join(self.root_dir, 'results', 'fast_processing')
        try:
            os.makedirs(self.results_dir)
        except OSError: # it most likely exists
            pass

        # Copy the vanilla XDS input file to the results dir
        infile_dest = os.path.join(self.results_dir, self.image_prefix + '_input_XDS.INP')
        shutil.copy(self.dataInput.input_file.path.value,
                    infile_dest)

        # Ensure the autoproc ids directory is there
        self.autoproc_ids_dir = os.path.join(self.results_dir, 'fastproc_integration_ids')
        try:
            os.makedirs(self.autoproc_ids_dir)
        except OSError: # it's there
            pass


        # we'll need the low res limit later on
        lowres = data_in.low_resolution_limit
        if lowres is not None:
            self.low_resolution_limit = lowres.value
        else:
            self.low_resolution_limit = 50

        res_override = data_in.res_override
        if res_override is not None:
            self.res_override = res_override.value
        else:
            # XXX: default to 0?
            self.res_override = None

        # check the number of images (must be > 8) and get the first
        # image name to wait for. Also modify the XDS.INP file to
        # reflect these values, if specified
        conf = parse_xds_file(data_in.input_file.path.value)


        # Make the [XY]-GEO_CORR paths absolute
        if 'X-GEO_CORR=' in conf:
            xgeo = os.path.abspath(os.path.join(self.root_dir,
                                                conf['X-GEO_CORR='][0]))
            if not os.path.exists(xgeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(xgeo))
                del conf['X-GEO_CORR=']
            else:
                conf['X-GEO_CORR='] = xgeo

        if 'Y-GEO_CORR=' in conf:
            ygeo = os.path.abspath(os.path.join(self.root_dir,
                                                conf['Y-GEO_CORR='][0]))
            if not os.path.exists(ygeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(ygeo))
                del conf['Y-GEO_CORR=']
            else:
                conf['Y-GEO_CORR='] = ygeo

        dump_xds_file(data_in.input_file.path.value, conf)

        resrange = conf.get('INCLUDE_RESOLUTION_RANGE=')

        if resrange is not None:
            if self.low_resolution_limit is not None:
                resrange[0] = self.low_resolution_limit
            if self.res_override is not None:
                resrange[1] = self.res_override
            conf['INCLUDE_RESOLUTION_RANGE='] = resrange
            dump_xds_file(data_in.input_file.path.value, conf)


        data_range = conf.get('DATA_RANGE=')
        # we'll need that for the very last part ( file import )
        self.data_range = data_range
        if data_range is not None:
            start_image = data_range[0]
            end_image = data_range[1]
            if end_image - start_image < 8:
                self.ERROR('there are fewer than 8 images, aborting')
                self.setFailure()
                return

        template = conf['NAME_TEMPLATE_OF_DATA_FRAMES='][0]
        self.DEBUG('template for images is {0}'.format(template))
        # fix the path if it's not absolute
        if not os.path.isabs(template):
            self.DEBUG('file template {0} is not absolute'.format(template))
            base_dir = os.path.abspath(os.path.dirname(data_in.input_file.path.value))
            template = os.path.normpath(os.path.join(self.root_dir, template))
            conf['NAME_TEMPLATE_OF_DATA_FRAMES=']=template
            self.DEBUG('file template fixed to {0}'.format(template))
            self.DEBUG('dumping back the file to {0}'.format(data_in.input_file.path.value))
            dump_xds_file(data_in.input_file.path.value, conf)

        first_image = _template_to_image(template, start_image)


        self.wait_file = self.loadPlugin('EDPluginWaitFile')
        waitfileinput = XSDataInputWaitFile()
        waitfileinput.expectedFile = XSDataFile()
        waitfileinput.expectedFile.path = XSDataString(first_image)
        waitfileinput.expectedSize = XSDataInteger(0) # we do not care
        timeout = XSDataTime()
        global WAIT_FOR_FRAME_TIMEOUT
        timeout.value = WAIT_FOR_FRAME_TIMEOUT
        waitfileinput.timeOut = timeout
        self.wait_file.dataInput = waitfileinput

        self.xds_first = self.loadPlugin("EDPluginControlRunXdsFastProc")
        self.xds_first.dataInput = xds_in

        self.generate = self.loadPlugin("EDPluginXDSGenerate")

        self.first_res_cutoff = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_anom = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_noanom = self.loadPlugin("EDPluginResCutoff")

        self.parse_xds_anom = self.loadPlugin("EDPluginParseXdsOutput")
        self.parse_xds_noanom = self.loadPlugin("EDPluginParseXdsOutput")

        self.xscale_generate = self.loadPlugin("EDPluginControlXscaleGenerate")

        self.store_autoproc_anom = self.loadPlugin('EDPluginISPyBStoreAutoProcv1_4')
        self.store_autoproc_noanom = self.loadPlugin('EDPluginISPyBStoreAutoProcv1_4')

        self.file_conversion = self.loadPlugin('EDPluginControlAutoprocImport')

        self.DEBUG('EDPluginControlAutoproc.preProcess finished')

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlAutoproc.process starting')

        process_start = time.time()


        # get our two integration IDs
        try:
            self.integration_id_noanom = create_integration_id(self.dataInput.data_collection_id.value)
        except Exception, e:
            EDVerbose.ERROR('could not get integration ID: \n{0}'.format(traceback.format_exc(e)))
            self.integration_id_noanom = None

        try:
            self.integration_id_anom = create_integration_id(self.dataInput.data_collection_id.value)
        except Exception, e:
            EDVerbose.ERROR('could not get integration ID: \n{0}'.format(traceback.format_exc(e)))
            self.integration_id_anom = None

        # wait for the first frame
        t0=time.time()
        self.wait_file.executeSynchronous()
        if self.wait_file.isFailure():
            self.ERROR('error waiting for the first image file to appear')
            self.setFailure()
            return
        EDVerbose.screen('first frame appeared on time')
        self.stats['wait_file'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        # first XDS plugin run with supplied XDS file
        EDVerbose.screen('STARTING XDS run...')

        t0=time.time()
        self.xds_first.executeSynchronous()

        self.stats['first_xds'] = time.time()-t0
        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)
        self.custom_stats['xds_runtime']=self.stats['first_xds']

        log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                     'Indexing', 'Launched', 'first xds run')

        if self.xds_first.isFailure():
            EDVerbose.ERROR('first XDS run failed')
            self.setFailure()
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Failed',
                         'first xds run failed after {0}s'.format(self.stats['first_xds']))
            return
        else:
            EDVerbose.screen('FINISHED first XDS run')
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Successful',
                         'first xds run finished after {0}s'.format(self.stats['first_xds']))
        EDVerbose.screen('FINISHED first XDS run')


        # use the cell dimensions and spacegroup from XDS to create a
        # file in the results directory
        filename = '_'.join([str(self.xds_first.dataOutput.sg_number.value),
                             str(self.xds_first.dataOutput.cell_a.value),
                             str(self.xds_first.dataOutput.cell_b.value),
                             str(self.xds_first.dataOutput.cell_c.value),
                             str(self.xds_first.dataOutput.cell_alpha.value),
                             str(self.xds_first.dataOutput.cell_beta.value),
                             str(self.xds_first.dataOutput.cell_gamma.value)])
        try:
            os.mknod(os.path.join(self.results_dir, filename), 0755)
        except OSError: #file exists
            pass

        # Copy the XDS.INP file that was used for the successful run
        # to the results directory
        tmppath = os.path.join(self.results_dir, self.image_prefix + '_successful_XDS.INP')
        shutil.copy(os.path.join(self.xds_first.dataOutput.xds_run_directory.value, 'XDS.INP'),
                    tmppath)

        # Copy the INTEGRATE.LP file as well
        integrate_path = os.path.join(self.results_dir, self.image_prefix + '_INTEGRATE.LP')
        try:
            shutil.copy(os.path.join(self.xds_first.dataOutput.xds_run_directory.value,
                                     'INTEGRATE.LP'),
                        integrate_path)
        except (IOError, OSError):
            EDVerbose.ERROR('failed to copy INTEGRATE.LP file ({0}) to the results dir'.format(integrate_path))


        log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                     'Indexing', 'Launched', 'start of res cutoff')

        # apply the first res cutoff with the res extracted from the first XDS run
        EDVerbose.screen('STARTING first resolution cutoff')
        t0=time.time()
        xdsresult = self.xds_first.dataOutput

        # for the custom stats
        self.custom_stats['overall_i_over_sigma']=xdsresult.total_completeness.outer_isig.value
        self.custom_stats['overall_r_value']=xdsresult.total_completeness.outer_rfactor.value
        self.custom_stats['inner_i_over_sigma']=xdsresult.completeness_entries[0].outer_isig.value
        self.custom_stats['inner_r_value']=xdsresult.completeness_entries[0].outer_rfactor.value
        self.custom_stats['outer_i_over_sigma']=xdsresult.completeness_entries[-1].outer_isig.value
        self.custom_stats['outer_r_value']=xdsresult.completeness_entries[-1].outer_rfactor.value


        res_cutoff_in = XSDataResCutoff()
        res_cutoff_in.xds_res = xdsresult
        res_cutoff_in.completeness_entries = xdsresult.completeness_entries
        res_cutoff_in.detector_max_res = self.dataInput.detector_max_res

        #XXX: remove from the data model as it is just pass-through?
        res_cutoff_in.total_completeness = xdsresult.total_completeness
        res_cutoff_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.first_res_cutoff.dataInput = res_cutoff_in
        self.first_res_cutoff.executeSynchronous()

        self.stats['first_res_cutoff'] = time.time()-t0

        if self.first_res_cutoff.isFailure():
            EDVerbose.ERROR("res cutoff failed")
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Failed',
                         'res cutoff failed in {0}s'.format(self.stats['first_res_cutoff']))
            self.setFailure()
            return
        else:
            EDVerbose.screen('FINISHED first resolution cutoff')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Indexing',
                         'Successful',
                         'res cutoff finished in {0}s'.format(self.stats['first_res_cutoff']))


        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        resolution = self.first_res_cutoff.dataOutput.res

        # for the generate w/ and w/out anom we have to specify where
        # the first XDS plugin run took place
        xds_run_directory = os.path.abspath(self.xds_first.dataOutput.xds_run_directory.value)
        EDVerbose.screen("the xds run took place in {0}".format(xds_run_directory))
        generate_input = XSDataXdsGenerateInput()
        generate_input.resolution = resolution
        generate_input.previous_run_dir = XSDataString(xds_run_directory)
        self.generate.dataInput = generate_input

        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of anom/noanom generation')

        self.DEBUG('STARTING anom/noanom generation')
        t0=time.time()
        self.generate.executeSynchronous()
        self.stats['anom/noanom_generation'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        self.DEBUG('FINISHED anom/noanom generation')

        if self.generate.isFailure():
            EDVerbose.ERROR('generating w/ and w/out anom failed')
            self.setFailure()
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Failed',
                         'anom/noanom generation failed in {0}s'.format(self.stats['anom/noanom_generation']))
            return
        else:
            EDVerbose.screen('generating w/ and w/out anom finished')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Successful',
                         'anom/noanom generation finished in {0}s'.format(self.stats['anom/noanom_generation']))

        # we can now use the xds output parser on the two correct.lp
        # files, w/ and w/out anom
        parse_anom_input = XSDataXdsOutputFile()
        parse_anom_input.correct_lp = XSDataFile()
        parse_anom_input.correct_lp.path = self.generate.dataOutput.correct_lp_anom

        # this one is the same as the first XDS run since they share
        # the same directory
        gxparm_file_anom = XSDataFile()
        gxparm_file_anom.path = self.generate.dataOutput.gxparm
        parse_anom_input.gxparm = gxparm_file_anom

        self.parse_xds_anom.dataInput = parse_anom_input

        self.parse_xds_anom.executeSynchronous()

        if self.parse_xds_anom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # now the other one w/out anom
        parse_noanom_input = XSDataXdsOutputFile()
        parse_noanom_input.correct_lp = XSDataFile()
        parse_noanom_input.correct_lp.path = self.generate.dataOutput.correct_lp_no_anom

        gxparm_file_noanom = XSDataFile()
        gxparm_file_noanom.path = self.generate.dataOutput.gxparm
        parse_noanom_input.gxparm = gxparm_file_noanom

        self.parse_xds_noanom.dataInput = parse_noanom_input
        self.parse_xds_noanom.executeSynchronous()

        if self.parse_xds_noanom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # we now can apply the res cutoff on the anom and no anom
        # outputs. Note that this is not done in parallel, like the
        # xds parsing


        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of anom/noanom resolution cutoffs')

        # XXX completeness_cutoff/res_override and isig_cutoff still
        # missing
        res_cutoff_anom_in = XSDataResCutoff()
        res_cutoff_anom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_anom_in.xds_res = self.parse_xds_anom.dataOutput
        res_cutoff_anom_in.completeness_entries = self.parse_xds_anom.dataOutput.completeness_entries
        res_cutoff_anom_in.total_completeness = self.parse_xds_anom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_anom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_anom_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_anom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_anom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_anom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_anom.dataInput = res_cutoff_anom_in

        self.DEBUG('STARTING anom res cutoff')
        t0=time.time()
        self.res_cutoff_anom.executeSynchronous()
        self.stats['res_cutoff_anom'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.res_cutoff_anom.isFailure():
            EDVerbose.ERROR('res cutoff for anom data failed')
            self.setFailure()
            log_to_ispyb(self.integration_id_anom,
                         'Scaling',
                         'Failed',
                         'anom resolution cutoffs failed in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_anom']))
            return
        else:
            self.screen('FINISHED anom res cutoff')
            log_to_ispyb(self.integration_id_anom,
                         'Scaling',
                         'Successful',
                         'anom resolution cutoffs finished in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_anom']))

        self.DEBUG('FINISHED anom res cutoff')

        # same for non anom
        res_cutoff_noanom_in = XSDataResCutoff()
        res_cutoff_noanom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_noanom_in.xds_res = self.parse_xds_noanom.dataOutput
        res_cutoff_noanom_in.completeness_entries = self.parse_xds_noanom.dataOutput.completeness_entries
        res_cutoff_noanom_in.total_completeness = self.parse_xds_noanom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_noanom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_noanom_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_noanom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_noanom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_noanom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_noanom.dataInput = res_cutoff_noanom_in

        self.DEBUG('STARTING noanom res cutoff')
        t0=time.time()
        self.res_cutoff_noanom.executeSynchronous()
        self.stats['res_cutoff_noanom'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.res_cutoff_noanom.isFailure():
            EDVerbose.ERROR('res cutoff for non anom data failed')
            self.setFailure()
            log_to_ispyb(self.integration_id_noanom,
                         'Scaling',
                         'Failed',
                         'noanom resolution cutoffs failed in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_noanom']))
            return
        else:
            self.screen('FINISHED noanom res cutoff')
            log_to_ispyb(self.integration_id_noanom,
                         'Scaling',
                         'Successful',
                         'noanom resolution cutoffs finished in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_noanom']))



        # now we just have to run XScale to generate w/ and w/out
        # anom, merged and unmerged

        # We use another control plugin for that to isolate the whole thing
        xscale_generate_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path_anom = self.generate.dataOutput.hkl_anom
        input_file.path_noanom = self.generate.dataOutput.hkl_no_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_generate_in.xds_files = [input_file]
        xscale_generate_in.unit_cell_constants = self.parse_xds_anom.dataOutput.unit_cell_constants
        xscale_generate_in.sg_number = self.parse_xds_anom.dataOutput.sg_number
        xscale_generate_in.bins = self.res_cutoff_anom.dataOutput.bins


        self.xscale_generate.dataInput = xscale_generate_in
        self.DEBUG('STARTING xscale generation')
        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of xscale generation')

        t0=time.time()
        self.xscale_generate.executeSynchronous()
        self.stats['xscale_generate']=time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.xscale_generate.isFailure():
            EDVerbose.ERROR('xscale generation failed')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Failed',
                         'xscale generation failed in {0}s'.format(self.stats['xscale_generate']))
            return
        else:
            EDVerbose.screen('xscale anom/merge generation finished')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Successful',
                         'xscale generation finished in {0}s'.format(self.stats['xscale_generate']))

        # Copy the generated files to the results dir
        attrs = ['lp_anom_merged', 'lp_noanom_merged',
                 'lp_anom_unmerged', 'lp_noanom_unmerged']
        xscale_logs = [getattr(self.xscale_generate.dataOutput, attr)
                       for attr in attrs]
        xscale_logs = [log.value for log in xscale_logs if log is not None]
        for log in xscale_logs:
            target = os.path.join(self.results_dir,
                                  '_'.join([self.image_prefix, os.path.basename(log)]))
            try:
                shutil.copyfile(log, target)
            except IOError:
                self.ERROR('Could not copy {0} to {1}'.format(log, target))



        import_in = XSDataAutoprocImport()
        import_in.input_anom = self.xscale_generate.dataOutput.hkl_anom_unmerged
        import_in.input_noanom = self.xscale_generate.dataOutput.hkl_noanom_unmerged
        import_in.dataCollectionID = self.dataInput.data_collection_id
        import_in.start_image = XSDataInteger(self.data_range[0])
        import_in.end_image = XSDataInteger(self.data_range[1])

        # XXX: is this the right place to get the res from?
        import_in.res = self.res_cutoff_anom.dataOutput.res

        # XXX: This is optional but seems required by aimless
        import_in.nres = self.dataInput.nres

        import_in.output_directory = XSDataString(self.results_dir)

        try:
            import_in.image_prefix = XSDataString(self.image_prefix)
        except:
            self.DEBUG('could not determine image prefix from directory "{0}"'.format(self.root_dir))

        self.file_conversion.dataInput = import_in

        t0 = time.time()
        self.file_conversion.executeSynchronous()
        self.stats['autoproc_import']=time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.file_conversion.isFailure():
            EDVerbose.ERROR("file import failed")


        self.custom_stats['total_time']=time.time() - process_start
        try:
            autoproclog.log(**self.custom_stats)
        except Exception, e:
            EDVerbose.screen('could not logs stats to custom log server')
            EDVerbose.screen(traceback.format_exc())


    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

        #Now that we have executed the whole thing we need to create
        #the suitable ISPyB plugin input and serialize it to the file
        #we've been given as input
        output = AutoProcContainer()

        # AutoProc attr
        autoproc = AutoProc()

        xdsout = self.xds_first.dataOutput
        if xdsout.sg_number is not None: # and it should not
            autoproc.spaceGroup = SPACE_GROUP_NAMES[xdsout.sg_number.value]
        autoproc.refinedCell_a = xdsout.cell_a.value
        autoproc.refinedCell_b = xdsout.cell_b.value
        autoproc.refinedCell_c = xdsout.cell_c.value
        autoproc.refinedCell_alpha = xdsout.cell_alpha.value
        autoproc.refinedCell_beta = xdsout.cell_beta.value
        autoproc.refinedCell_gamma = xdsout.cell_gamma.value

        output.AutoProc = autoproc

        # scaling container and all the things that go in
        scaling_container_noanom = AutoProcScalingContainer()
        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        scaling_container_noanom.AutoProcScaling = scaling

        # NOANOM PATH
        xscale_stats_noanom = self.xscale_generate.dataOutput.stats_noanom_merged
        inner_stats_noanom = xscale_stats_noanom.completeness_entries[0]
        outer_stats_noanom = xscale_stats_noanom.completeness_entries[-1]

        # use the previous shell's res as low res, if available
        prev_res = self.low_resolution_limit
        try:
            prev_res = xscale_stats_noanom.completeness_entries[-2].outer_res.value
        except IndexError:
            pass
        total_stats_noanom = xscale_stats_noanom.total_completeness

        stats = _create_scaling_stats(inner_stats_noanom, 'innerShell',
                                      self.low_resolution_limit, False)
        overall_low = stats.resolutionLimitLow
        scaling_container_noanom.AutoProcScalingStatistics.append(stats)

        stats = _create_scaling_stats(outer_stats_noanom, 'outerShell',
                                      prev_res, False)
        overall_high = stats.resolutionLimitHigh
        scaling_container_noanom.AutoProcScalingStatistics.append(stats)
        stats = _create_scaling_stats(total_stats_noanom, 'overall',
                                      self.low_resolution_limit, False)
        stats.resolutionLimitLow = overall_low
        stats.resolutionLimitHigh = overall_high
        scaling_container_noanom.AutoProcScalingStatistics.append(stats)

        integration_container_noanom = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.data_collection_id.value
        integration_container_noanom.Image = image

        integration_noanom = AutoProcIntegration()
        if self.integration_id_noanom is not None:
            integration_noanom.autoProcIntegrationId = self.integration_id_noanom
        crystal_stats =  self.parse_xds_noanom.dataOutput
        integration_noanom.cell_a = crystal_stats.cell_a.value
        integration_noanom.cell_b = crystal_stats.cell_b.value
        integration_noanom.cell_c = crystal_stats.cell_c.value
        integration_noanom.cell_alpha = crystal_stats.cell_alpha.value
        integration_noanom.cell_beta = crystal_stats.cell_beta.value
        integration_noanom.cell_gamma = crystal_stats.cell_gamma.value
        integration_noanom.anomalous = 0

        # done with the integration
        integration_container_noanom.AutoProcIntegration = integration_noanom
        scaling_container_noanom.AutoProcIntegrationContainer = integration_container_noanom

        # ANOM PATH
        scaling_container_anom = AutoProcScalingContainer()
        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        scaling_container_anom.AutoProcScaling = scaling

        xscale_stats_anom = self.xscale_generate.dataOutput.stats_anom_merged
        inner_stats_anom = xscale_stats_anom.completeness_entries[0]
        outer_stats_anom = xscale_stats_anom.completeness_entries[-1]

        # use the previous shell's res as low res if available
        prev_res = self.low_resolution_limit
        try:
            prev_res = xscale_stats_anom.completeness_entries[-2].outer_res.value
        except IndexError:
            pass
        total_stats_anom = xscale_stats_anom.total_completeness

        stats = _create_scaling_stats(inner_stats_anom, 'innerShell',
                                      self.low_resolution_limit, True)
        overall_low = stats.resolutionLimitLow
        scaling_container_anom.AutoProcScalingStatistics.append(stats)

        stats = _create_scaling_stats(outer_stats_anom, 'outerShell',
                                      prev_res, True)
        overall_high = stats.resolutionLimitHigh
        scaling_container_anom.AutoProcScalingStatistics.append(stats)
        stats = _create_scaling_stats(total_stats_anom, 'overall',
                                      self.low_resolution_limit, True)
        stats.resolutionLimitLow = overall_low
        stats.resolutionLimitHigh = overall_high
        scaling_container_anom.AutoProcScalingStatistics.append(stats)


        integration_container_anom = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.data_collection_id.value
        integration_container_anom.Image = image

        integration_anom = AutoProcIntegration()
        crystal_stats =  self.parse_xds_anom.dataOutput
        if self.integration_id_anom is not None:
            integration_anom.autoProcIntegrationId = self.integration_id_anom
        integration_anom.cell_a = crystal_stats.cell_a.value
        integration_anom.cell_b = crystal_stats.cell_b.value
        integration_anom.cell_c = crystal_stats.cell_c.value
        integration_anom.cell_alpha = crystal_stats.cell_alpha.value
        integration_anom.cell_beta = crystal_stats.cell_beta.value
        integration_anom.cell_gamma = crystal_stats.cell_gamma.value
        integration_anom.anomalous = 1

        # done with the integration
        integration_container_anom.AutoProcIntegration = integration_anom
        scaling_container_anom.AutoProcIntegrationContainer = integration_container_anom


        # ------ NO ANOM / ANOM end



        program_container = AutoProcProgramContainer()
        program_container.AutoProcProgram = AutoProcProgram()
        program_container.AutoProcProgram.processingCommandLine = ' '.join(sys.argv)
        program_container.AutoProcProgram.processingPrograms = 'edna-fastproc'

        # now for the generated files. There's some magic to do with
        # their paths to determine where to put them on pyarch
        pyarch_path = None
        # Note: the path is in the form /data/whatever

        # remove the edna-autoproc-import suffix
        original_files_dir = self.file_conversion.dataInput.output_directory.value
        #files_dir, _ = os.path.split(original_files_dir)
        files_dir = original_files_dir

        # the whole transformation is fragile!
        if files_dir.startswith('/data/visitor'):
            # We might get empty elements at the head/tail of the list
            tokens = [elem for elem in files_dir.split(os.path.sep)
                      if len(elem) > 0]
            pyarch_path = os.path.join('/data/pyarch',
                                       tokens[3], tokens[2],
                                       *tokens[4:])
        else:
            # We might get empty elements at the head/tail of the list
            tokens = [elem for elem in files_dir.split(os.path.sep)
                      if len(elem) > 0]
            if tokens[2] == 'inhouse':
                pyarch_path = os.path.join('/data/pyarch', tokens[1],
                                           *tokens[3:])
        if pyarch_path is not None:
            pyarch_path = pyarch_path.replace('PROCESSED_DATA', 'RAW_DATA')
            try:
                os.makedirs(pyarch_path)
            except OSError:
                # dir already exists, may happen when testing
                EDVerbose.screen('Target directory on pyarch ({0}) already exists, ignoring'.format(pyarch_path))

            file_list = []
            # we can now copy the files to this dir
            for f in os.listdir(original_files_dir):
                current = os.path.join(original_files_dir, f)
                if not os.path.isfile(current):
                    continue
                if not os.path.splitext(current)[1].lower() in ISPYB_UPLOAD_EXTENSIONS:
                    continue
                new_path = os.path.join(pyarch_path, f)
                file_list.append(new_path)
                shutil.copyfile(current,
                                new_path)
            # now add those to the ispyb upload
            for path in file_list:
                dirname, filename = os.path.split(path)
                attach = AutoProcProgramAttachment()
                attach.fileType = "Result"
                attach.fileName = filename
                attach.filePath = dirname
                program_container.AutoProcProgramAttachment.append(attach)


        program_container.AutoProcProgram.processingStatus = True
        output.AutoProcProgramContainer = program_container

        # first with anom

        output.AutoProcScalingContainer = scaling_container_anom

        ispyb_input = XSDataInputStoreAutoProc()
        ispyb_input.AutoProcContainer = output


        with open(self.dataInput.output_file.path.value, 'w') as f:
            f.write(ispyb_input.marshal())

        # store results in ispyb
        self.store_autoproc_anom.dataInput = ispyb_input
        t0=time.time()
        self.store_autoproc_anom.executeSynchronous()
        self.stats['ispyb_upload'] = time.time() - t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.store_autoproc_anom.isFailure():
            self.ERROR('could not send results to ispyb')
        else:
            # store the autoproc ID as a filename in the
            # fastproc_integration_ids directory
            os.mknod(os.path.join(self.autoproc_ids_dir, str(self.integration_id_anom)), 0755)
        # then noanom stats

        output.AutoProcScalingContainer = scaling_container_noanom

        ispyb_input = XSDataInputStoreAutoProc()
        ispyb_input.AutoProcContainer = output


        with open(self.dataInput.output_file.path.value, 'w') as f:
            f.write(ispyb_input.marshal())

        # store results in ispyb
        self.store_autoproc_noanom.dataInput = ispyb_input
        t0=time.time()
        self.store_autoproc_noanom.executeSynchronous()
        self.stats['ispyb_upload'] = time.time() - t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.store_autoproc_noanom.isFailure():
            self.ERROR('could not send results to ispyb')
        else:
            # store the autoproc id
            os.mknod(os.path.join(self.autoproc_ids_dir, str(self.integration_id_noanom)), 0755)

# Proxy since the API changed and we can now log to several ids
def log_to_ispyb(integration_id, step, status, comments=""):
    if type(integration_id) is list:
        for item in integration_id:
            log_to_ispyb_impl(item, step, status, comments)
    else:
        log_to_ispyb_impl(integration_id, step, status, comments)

def log_to_ispyb_impl(integration_id, step, status, comments=""):
    # hack in the event we could not create an integration ID
    if integration_id is None:
        EDVerbose.ERROR('could not log to ispyb: no integration id')
        return
    autoproc_status = edFactoryPlugin.loadPlugin('EDPluginISPyBStoreAutoProcStatusv1_4')
    status_input = XSDataInputStoreAutoProcStatus()
    status_input.autoProcIntegrationId = integration_id
    status_data = AutoProcStatus()
    status_data.step = step
    status_data.status = status
    status_data.comments = comments
    status_input.AutoProcStatus = status_data

    autoproc_status.dataInput = status_input

    autoproc_status.executeSynchronous()

def create_integration_id(datacollect_id):
    autoproc_status = edFactoryPlugin.loadPlugin('EDPluginISPyBStoreAutoProcStatusv1_4')
    status_input = XSDataInputStoreAutoProcStatus()
    status_input.dataCollectionId = datacollect_id

    # needed even if we only want to get an integration ID?
    status_data = AutoProcStatus()
    status_data.step = "Indexing"
    status_data.status = "Launched"
    status_data.comments = "Getting integration ID"
    status_input.AutoProcStatus = status_data

    autoproc_status.dataInput = status_input
    # get our autoproc status id
    autoproc_status.executeSynchronous()
    return autoproc_status.dataOutput.autoProcIntegrationId

def _create_scaling_stats(xscale_stats, stats_type, lowres, anom):
    stats = AutoProcScalingStatistics()
    stats.scalingStatisticsType = stats_type
    stats.resolutionLimitLow = lowres
    if stats_type != 'overall':
        stats.resolutionLimitHigh = xscale_stats.outer_res.value
    stats.meanIOverSigI = xscale_stats.outer_isig.value
    stats.completeness = xscale_stats.outer_complete.value
    stats.multiplicity = xscale_stats.multiplicity.value
    # The ispyb plugin DOES NOT convert to the right data types. This
    # happens to be an integer on the ispyb side
    stats.nTotalObservations = int(xscale_stats.outer_observed.value)
    stats.rMerge = xscale_stats.outer_rfactor.value
    stats.anomalous = anom

    return stats



# copy/pasted from another plugin
def _template_to_image(fmt, num):
    # for simplicity we will assume the template to contain only one
    # sequence of '?' characters. max's code uses a regexp so this
    # further restrict the possible templates.
    start = fmt.find('?')
    end = fmt.rfind('?')
    if start == -1 or end == -1:
        # the caller test for the file existence and an empty path
        # does not exist
        return ''
    prefix = fmt[:start]
    suffix = fmt[end+1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + '{0:0' + str(length) + 'd}' + suffix

    return fmt_string.format(num)


# taken straight from max's code
SPACE_GROUP_NAMES = {
    1: ' P 1 ',
    2: ' P -1 ',
    3: ' P 1 2 1 ',
    4: ' P 1 21 1 ',
    5: ' C 1 2 1 ',
    6: ' P 1 m 1 ',
    7: ' P 1 c 1 ',
    8: ' C 1 m 1 ',
    9: ' C 1 c 1 ',
    10: ' P 1 2/m 1 ',
    11: ' P 1 21/m 1 ',
    12: ' C 1 2/m 1 ',
    13: ' P 1 2/c 1 ',
    14: ' P 1 21/c 1 ',
    15: ' C 1 2/c 1 ',
    16: ' P 2 2 2 ',
    17: ' P 2 2 21 ',
    18: ' P 21 21 2 ',
    19: ' P 21 21 21 ',
    20: ' C 2 2 21 ',
    21: ' C 2 2 2 ',
    22: ' F 2 2 2 ',
    23: ' I 2 2 2 ',
    24: ' I 21 21 21 ',
    25: ' P m m 2 ',
    26: ' P m c 21 ',
    27: ' P c c 2 ',
    28: ' P m a 2 ',
    29: ' P c a 21 ',
    30: ' P n c 2 ',
    31: ' P m n 21 ',
    32: ' P b a 2 ',
    33: ' P n a 21 ',
    34: ' P n n 2 ',
    35: ' C m m 2 ',
    36: ' C m c 21 ',
    37: ' C c c 2 ',
    38: ' A m m 2 ',
    39: ' A b m 2 ',
    40: ' A m a 2 ',
    41: ' A b a 2 ',
    42: ' F m m 2 ',
    43: ' F d d 2 ',
    44: ' I m m 2 ',
    45: ' I b a 2 ',
    46: ' I m a 2 ',
    47: ' P m m m ',
    48: ' P n n n ',
    49: ' P c c m ',
    50: ' P b a n ',
    51: ' P m m a1 ',
    52: ' P n n a1 ',
    53: ' P m n a1 ',
    54: ' P c c a1 ',
    55: ' P b a m1 ',
    56: ' P c c n1 ',
    57: ' P b c m1 ',
    58: ' P n n m1 ',
    59: ' P m m n1 ',
    60: ' P b c n1 ',
    61: ' P b c a1 ',
    62: ' P n m a1 ',
    63: ' C m c m1 ',
    64: ' C m c a1 ',
    65: ' C m m m ',
    66: ' C c c m ',
    67: ' C m m a ',
    68: ' C c c a ',
    69: ' F m m m ',
    70: ' F d d d ',
    71: ' I m m m ',
    72: ' I b a m ',
    73: ' I b c a1 ',
    74: ' I m m a1 ',
    75: ' P 4 ',
    76: ' P 41 ',
    77: ' P 42 ',
    78: ' P 43 ',
    79: ' I 4 ',
    80: ' I 41 ',
    81: ' P -4 ',
    82: ' I -4 ',
    83: ' P 4/m ',
    84: ' P 42/m ',
    85: ' P 4/n ',
    86: ' P 42/n ',
    87: ' I 4/m ',
    88: ' I 41/a ',
    89: ' P 4 2 2 ',
    90: ' P 4 21 2 ',
    91: ' P 41 2 2 ',
    92: ' P 41 21 2 ',
    93: ' P 42 2 2 ',
    94: ' P 42 21 2 ',
    95: ' P 43 2 2 ',
    96: ' P 43 21 2 ',
    97: ' I 4 2 2 ',
    98: ' I 41 2 2 ',
    99: ' P 4 m m ',
    100: ' P 4 b m ',
    101: ' P 42 c m ',
    102: ' P 42 n m ',
    103: ' P 4 c c ',
    104: ' P 4 n c ',
    105: ' P 42 m c ',
    106: ' P 42 b c ',
    107: ' I 4 m m ',
    108: ' I 4 c m ',
    109: ' I 41 m d ',
    110: ' I 41 c d ',
    111: ' P -4 2 m ',
    112: ' P -4 2 c ',
    113: ' P -4 21 m ',
    114: ' P -4 21 c ',
    115: ' P -4 m 2 ',
    116: ' P -4 c 2 ',
    117: ' P -4 b 2 ',
    118: ' P -4 n 2 ',
    119: ' I -4 m 2 ',
    120: ' I -4 c 2 ',
    121: ' I -4 2 m ',
    122: ' I -4 2 d ',
    123: ' P 4/m m m ',
    124: ' P 4/m c c ',
    125: ' P 4/n b m ',
    126: ' P 4/n n c ',
    127: ' P 4/m b m1 ',
    128: ' P 4/m n c1 ',
    129: ' P 4/n m m1 ',
    130: ' P 4/n c c1 ',
    131: ' P 42/m m c ',
    132: ' P 42/m c m ',
    133: ' P 42/n b c ',
    134: ' P 42/n n m ',
    135: ' P 42/m b c ',
    136: ' P 42/m n m ',
    137: ' P 42/n m c ',
    138: ' P 42/n c m ',
    139: ' I 4/m m m ',
    140: ' I 4/m c m ',
    141: ' I 41/a m d ',
    142: ' I 41/a c d ',
    143: ' P 3 ',
    144: ' P 31 ',
    145: ' P 32 ',
    146: ' H 3 ',
    147: ' P -3 ',
    148: ' H -3 ',
    149: ' P 3 1 2 ',
    150: ' P 3 2 1 ',
    151: ' P 31 1 2 ',
    152: ' P 31 2 1 ',
    153: ' P 32 1 2 ',
    154: ' P 32 2 1 ',
    155: ' H 3 2 ',
    156: ' P 3 m 1 ',
    157: ' P 3 1 m ',
    158: ' P 3 c 1 ',
    159: ' P 3 1 c ',
    160: ' H 3 m ',
    161: ' H 3 c ',
    162: ' P -3 1 m ',
    163: ' P -3 1 c ',
    164: ' P -3 m 1 ',
    165: ' P -3 c 1 ',
    166: ' H -3 m ',
    167: ' H -3 c ',
    168: ' P 6 ',
    169: ' P 61 ',
    170: ' P 65 ',
    171: ' P 62 ',
    172: ' P 64 ',
    173: ' P 63 ',
    174: ' P -6 ',
    175: ' P 6/m ',
    176: ' P 63/m ',
    177: ' P 6 2 2 ',
    178: ' P 61 2 2 ',
    179: ' P 65 2 2 ',
    180: ' P 62 2 2 ',
    181: ' P 64 2 2 ',
    182: ' P 63 2 2 ',
    183: ' P 6 m m ',
    184: ' P 6 c c ',
    185: ' P 63 c m ',
    186: ' P 63 m c ',
    187: ' P -6 m 2 ',
    188: ' P -6 c 2 ',
    189: ' P -6 2 m ',
    190: ' P -6 2 c ',
    191: ' P 6/m m m ',
    192: ' P 6/m c c ',
    193: ' P 63/m c m ',
    194: ' P 63/m m c ',
    195: ' P 2 3 ',
    196: ' F 2 3 ',
    197: ' I 2 3 ',
    198: ' P 21 3 ',
    199: ' I 21 3 ',
    200: ' P m -3 ',
    201: ' P n -3 ',
    202: ' F m -3 ',
    203: ' F d -3 ',
    204: ' I m -3 ',
    205: ' P a -31 ',
    206: ' I a -31 ',
    207: ' P 4 3 2 ',
    208: ' P 42 3 2 ',
    209: ' F 4 3 2 ',
    210: ' F 41 3 2 ',
    211: ' I 4 3 2 ',
    212: ' P 43 3 2 ',
    213: ' P 41 3 2 ',
    214: ' I 41 3 2 ',
    215: ' P -4 3 m ',
    216: ' F -4 3 m ',
    217: ' I -4 3 m ',
    218: ' P -4 3 n ',
    219: ' F -4 3 c ',
    220: ' I -4 3 d ',
    221: ' P m -3 m ',
    222: ' P n -3 n ',
    223: ' P m -3 n1 ',
    224: ' P n -3 m1 ',
    225: ' F m -3 m ',
    226: ' F m -3 c ',
    227: ' F d -3 m1 ',
    228: ' F d -3 c1 ',
    229: ' I m -3 m ',
    230: ' I a -3 d1 ',
}

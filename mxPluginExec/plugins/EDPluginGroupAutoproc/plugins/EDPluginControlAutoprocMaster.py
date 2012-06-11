# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:        <author>
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

__author__="<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"


import os.path
import os
from tempfile import mkstemp

from EDConfiguration import EDConfiguration
from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString, XSDataInteger

from XSDataAutoproc import XSDataAutoprocInput

from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc


edFactoryPlugin.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile

from xdscfgparser import parse_xds_file, dump_xds_file

class EDPluginControlAutoprocMaster(EDPluginControl):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataAutoprocInput)

    def configure(self):
        conf = self.getConfiguration()
        output_path = EDConfiguration.getStringParamValue(conf, 'outputPath')
        if output_path is None:
            EDVerbose.ERROR('no output dir for ISPyB data specified, exiting')
            self.setFailure()
            return
        if not os.path.exists(output_path):
            EDVerbose.ERROR('the ISPyB output dir does not exist, exiting')
            self.setFailure()
            return
        if output_path[-1] != '/':
            # mkstemp is picky about that
            output_path += '/'
        fd, path = mkstemp(prefix=output_path, suffix='.xml')
        os.close(fd)
        self.output_file = path

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        input_file = self.dataInput.input_file
        if input_file is None:
            EDVerbose.ERROR('no xds input file given, giving up')
            self.setFailure()
            return

        input_file = input_file.value
        if not os.path.exists(input_file):
            EDVerbose.ERROR('the specified input file does not seem to exist,'
                            ' giving up')
            self.setFailure()
            return



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoprocMaster.preProcess")

        # instantiate the plugins
        self.wait_input_files = self.loadPlugin("EDPluginWaitFile")
        self.run_autoproc = self.loadPlugin("EDPluginExecAutoprocOnOar")
        self.ispyb_upload = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4")

        # we need to "fix" the input file so the SPOT_RANGE gets set
        # to a sensible value
        input_file = self.dataInput.input_file.value
        cfg = parse_xds_file(input_file)
        data_range = cfg.get("DATA_RANGE=", None)
        if data_range is None:
            # max's code exits shortly after if there's no data range
            self.ERROR('DATA_RANGE not specified in the XDS.INP file, exiting')
            self.setFailure()
            return
        image_start, image_end = data_range
        template = cfg["NAME_TEMPLATE_OF_DATA_FILES="]

        #that's the image we'll wait for
        self.first_image = _template_to_image(template, image_start)

        spot_range = _spot_range(cfg)
        if len(spot_range) != 0:
            cfg['SPOT_RANGE='] = spot_range

        #SECONDS is also set to 20
        cfg['SECONDS='] = 20
        dump_xds_file(input_file, cfg)

        wait_file_in = XSDataInputWaitFile()
        filepath = XSDataFile()
        filepath.path = XSDataString(self.first_image)
        wait_file_in.expectedFile = filepath
        wait_file_in.timeOut = XSDataInteger(240) # max uses 250
        self.wait_input_files.dataInput = wait_file_in


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoprocMaster.process")

        self.wait_input_files.executeSynchronous()
        if self.wait_input_files.isFailure() or self.wait_input_files.dataOutput.timedOut.value:
            EDVerbose.ERROR('waiting for the first file to appear failed/timed out')
            self.setFailure()
            return

        # first file's here

        # the autoproc proper takes a subclass of our data model, with
        # only an added path to serialize its output to
        # XXX: maybe move that stuff to preprocess?
        autoproc_input = XSDataAutoprocInput()
        autoproc_input.input_file = self.dataInput.input_file
        autoproc_input.completeness_cutoff = self.dataInput.completeness_cutoff
        autoproc_input.res_override = self.dataInput.res_override
        autoproc_input.isig_cutoff = self.dataInput.isig_cutoff
        autoproc_input.data_collection_id = self.dataInput.data_collection_id
        output_file = XSDataFile()
        output_file.path = XSDataString(self.output_path)
        autoproc_input.output_file = output_file

        self.run_autoproc.dataInput = autoproc_input
        self.run_autoproc.executeSynchronous()

        if self.run_autoproc.isFailure():
            # TODO: maybe distinguish between timeout and "other"
            # failures
            EDVerbose.ERROR('autoproc completed Unsuccessfully on the cluster')
            self.setFailure()
            return

        # try to parse the output from the plugin, which sould be in the right format already
        try:
            autoproc_output = XSDataInputStoreAutoProc.parseFile(self.output_path)
        except Exception:
            # maybe output more details?
            # err = sys.exc_info()[1]
            EDVerbose.ERROR('could not parse the output file {0}'.format(self.output_path))
            self.setFailure()
            return

        self.ispyb_upload.dataInput = autoproc_output
        self.ispyb_upload.executeSynchronous()
        if self.ispyb_upload.isFailure():
            EDVerbose.ERROR('upload to ispyb failed. data still in {0}'.format(self.output_path))
            self.setFailure()
            return


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoprocMaster.postProcess")


# for the original see xdsproc.pl::spot_range(). Determine a suitable
# value for the SPOT_RANGE XDS input file
def _spot_range(cfg):
    """straight port of max's code. we will return a list of strings
    in the format "START END" or an empty list in case anything goes
    wrong."""

    # Why did I make that parameter a list...
    template = cfg['NAME_TEMPLATE_OF_DATA_FRAMES='][0]
    osc_range = cfg['OSCILLATION_RANGE=']
    data_range = cfg['DATA_RANGE=']

    startimage = data_range[0]

    # reuse more or less the same variable names
    eranges = [[90, 85, 80, 75, 70, 65, 60],
               [45, 40, 35, 30, 25, 20, 15]]
    res = list()
    for range_ in eranges:
        for angle in range_:
            imnumber = int(startimage+(angle//osc_range))
            filename = _template_to_image(template, imnumber)
            if os.path.exists(filename):
                startno = imnumber-10
                if startno < 0:
                    continue #try the next angle
                else:
                    res.append("{0} {1}".format(startno, imnumber))
                    break # next erange
            else:
                EDVerbose.DEBUG('file {0} does not exist'.format(filename))
    return res

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

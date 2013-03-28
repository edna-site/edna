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

import sys
import os.path
import shutil

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile, XSDataString

from XSDataAutoproc  import XSDataMinimalXdsIn, XSDataXdsOutputFile, XSDataRange

from xdscfgparser import parse_xds_file

class EDPluginControlRunXdsFastProc( EDPluginControl ):
    """
    Run XDS up to three times, extending the SPOT_RANGE after each
    failure.
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataMinimalXdsIn)
        self.controlled_plugin_name = 'EDPluginExecMinimalXds'
        self.first_run = None
        self.second_run = None
        self.third_run = None

        # to hold a ref to the successful plugin
        self.successful_run = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlRunXdsFastProc.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlRunXdsFastProc.preProcess")
        # Load the execution plugin
        self.first_run = self.loadPlugin(self.controlled_plugin_name)

        cfg = parse_xds_file(self.dataInput.input_file.value)
        spot_range = cfg.get('SPOT_RANGE=')
        if spot_range is None:
            self.ERROR('no SPOT_RANGE parameter')
            self.setFailure()
        else:
            self.spot_range = spot_range

        # we will use this value to constrain the upper bound of
        # spot_range so it does not get past the last image number, so
        # we use a default value that cannot be a constraint in case
        # we cannot find it in the xds input file
        self.end_image_no = sys.maxint

        data_range = cfg.get('DATA_RANGE=')
        if data_range is not None:
            self.end_image_no = data_range[1]

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlRunXdsFastProc.process")
        # First run is vanilla without any modification
        params = XSDataMinimalXdsIn()
        params.input_file = self.dataInput.input_file
        params.spacegroup = self.dataInput.spacegroup
        params.unit_cell = self.dataInput.unit_cell
        self.first_run.dataInput = params
        self.first_run.executeSynchronous()

        EDVerbose.DEBUG('first run completed...')

        if self.first_run.dataOutput is not None and self.first_run.dataOutput.succeeded.value:
            EDVerbose.DEBUG('... and it worked')
            self.successful_run = self.first_run
        else:
            EDVerbose.DEBUG('... and it failed')


        if not self.successful_run:
            self.second_run = self.loadPlugin(self.controlled_plugin_name)
            self.DEBUG('retrying with increased SPOT_RANGE')
            self.DEBUG('copying previously generated files to the new plugin dir')
            copy_xds_files(self.first_run.getWorkingDirectory(),
                           self.second_run.getWorkingDirectory())
            params = XSDataMinimalXdsIn()
            params.input_file = self.dataInput.input_file
            params.job = XSDataString('DEFPIX INTEGRATE CORRECT')
            params.spacegroup = self.dataInput.spacegroup
            params.unit_cell = self.dataInput.unit_cell

            # increase all the spot ranges end by 20, constrained to
            # the data range upper limit
            spot_range = list()
            for srange in self.spot_range:
                range_begin = srange[0]
                range_end = srange[1] + 20
                if range_end > self.end_image_no:
                    self.DEBUG('End of range {0} would be past the last image {1}'.format(range_end,
                                                                                          self.end_image_no))
                    range_end = self.end_image_no
                self.DEBUG('Changing spot range {0} to [{1} {2}]'.format(srange, range_begin, range_end))
                r = XSDataRange(begin=range_begin, end=range_end)
                spot_range.append(r)

            params.spot_range = spot_range

            self.second_run.dataInput = params
            self.second_run.executeSynchronous()

            EDVerbose.DEBUG('second run completed')
            if self.second_run.dataOutput is not None and self.second_run.dataOutput.succeeded.value:
                EDVerbose.DEBUG('... and it worked')
                self.successful_run = self.second_run
            else:
                EDVerbose.DEBUG('... and it failed')


        if not self.successful_run:
            self.third_run = self.loadPlugin(self.controlled_plugin_name)
            self.DEBUG('retrying with increased SPOT_RANGE')
            self.DEBUG('copying previously generated files to the new plugin dir')
            copy_xds_files(self.second_run.getWorkingDirectory(),
                           self.third_run.getWorkingDirectory())
            params = XSDataMinimalXdsIn()
            params.input_file = self.dataInput.input_file
            params.job = XSDataString('DEFPIX INTEGRATE CORRECT')
            params.spacegroup = self.dataInput.spacegroup
            params.unit_cell = self.dataInput.unit_cell
            spot_range = list()
            for srange in self.spot_range:
                range_begin = srange[0]
                range_end = srange[1] + 40
                if range_end > self.end_image_no:
                    self.DEBUG('End of range {0} would be past the last image {1}'.format(range_end,
                                                                                          self.end_image_no))
                    range_end = self.end_image_no
                self.DEBUG('Changing spot range {0} to [{1} {2}]'.format(srange, range_begin, range_end))
                r = XSDataRange(begin=range_begin, end=range_end)
                spot_range.append(r)

            params.spot_range = spot_range

            self.third_run.dataInput = params
            self.third_run.executeSynchronous()

            EDVerbose.DEBUG('third run completed')
            if self.third_run.dataOutput is not None and self.third_run.dataOutput.succeeded.value:
                EDVerbose.DEBUG('... and it worked')
                self.successful_run = self.third_run
            else:
                EDVerbose.DEBUG('... and it failed')

        if not self.successful_run:
        # all runs failed so bail out ...
            self.setFailure()
        else:
            # use the xds parser plugin to parse the xds output file...
            parser = self.loadPlugin("EDPluginParseXdsOutput")
            wd = self.successful_run.getWorkingDirectory()
            parser_input = XSDataXdsOutputFile()
            correct_lp_path = XSDataFile()
            correct_lp_path.path = XSDataString(os.path.join(wd, 'CORRECT.LP'))
            parser_input.correct_lp = correct_lp_path
            gxparm_path = os.path.join(wd, 'GXPARM.XDS')
            if os.path.isfile(gxparm_path):
                gxparm = XSDataFile()
                gxparm.path = XSDataString(os.path.join(wd, 'GXPARM.XDS'))
                parser_input.gxparm = gxparm

            parser.dataInput = parser_input
            parser.executeSynchronous()

            if parser.isFailure():
                # that should not happen
                self.setFailure()
                return
            self.dataOutput = parser.dataOutput

    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlRunXdsFastProc.postProcess")
        # XXX: maybe move the XDS output parsing there?

def copy_xds_files(source_dir, dest_dir):
    # those files are generated by the first steps of XDS. When we try
    # a re-run with JOB= DEFPIX INTEGRATE CORRECT we need them to be
    # available in the current directory
    FILES = [ 'X-CORRECTIONS.cbf',
              'Y-CORRECTIONS.cbf',
              'BKGINIT.cbf',
              'XPARM.XDS',
              'BLANK.cbf',
              'GAIN.cbf',
              'REMOVE.HKL'
              ]
    for f in FILES:
        try:
            shutil.copyfile(os.path.join(source_dir, f),
                            os.path.join(dest_dir, f))
        except IOError:
            #file not found
            pass

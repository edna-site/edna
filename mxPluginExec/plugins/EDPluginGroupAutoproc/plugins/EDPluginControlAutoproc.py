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

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString

from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataResCutoff
from XSDataAutoproc import XSDataMinimalXdsIn
from XSDataAutoproc import XSDataXdsGenerateInput
from XSDataAutoproc import XSDataXdsOutputFile
from XSDataAutoproc import XSDataXscaleInput
from XSDataAutoproc import XSDataXscaleInputFile


class EDPluginControlAutoproc( EDPluginControl ):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataMinimalXdsIn)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoproc.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")

    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoproc.preProcess")

        self.xds_first = self.loadPlugin("EDPluginControlRunXds")
        self.generate = self.loadPlugin("EDPluginXDSGenerate")

        self.first_res_cutoff = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_anom = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_noanom = self.loadPlugin("EDPluginResCutoff")

        self.parse_xds_anom = self.loadPlugin("EDPluginParseXdsOutput")
        self.parse_xds_noanom = self.loadPlugin("EDPluginParseXdsOutput")

        self.xscale_anom = self.loadPlugin("EDPluginControlXscaleGenerate")
        self.xscale_noanom = self.loadPlugin("EDPluginControlXscaleGenerate")

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoproc.process")

        # first XDS plugin run with supplied XDS file
        EDVerbose.INFO("First XDS run...")
        self.xds_first.executeSynchronous()
        if self.xds_first.isFailure():
            EDVerbose.ERROR('first XDS run failed')
            self.setFailure(True)
            return
        EDVerbose.INFO("First XDS run successfully completed")

        # apply the first res cutoff with the res extracted from the first XDS run
        EDVerbose.INFO("First resolution cutoff")
        xdsresult = self.xds_first.dataOutput
        res_cutoff_in = XSDataResCutoff()
        res_cutoff_in.xds_res = xdsresult
        self.first_res_cutoff.dataInput = res_cutoff_in
        self.first_res_cutoff.executeSynchronous()
        if self.first_res_cutoff.isFailure():
            EDVerbose.ERROR("res cutoff failed")
            self.setFailure()
            return
        EDVerbose.INFO("First resolution cutoff successfully completed")
        resolution = self.first_res_cutoff.dataOutput.res

        # for the generate w/ and w/out anom we have to specify where
        # the first XDS plugin run took place
        xds_run_path = os.path.abspath(self.xds_first.getWorkingDirectory())
        generate_input = XSDataXdsGenerateInput()
        generate_input.resolution = res
        generate_input.previous_run_dir = XSDataString(xds_run_path)
        self.generate.dataInput = generate_input

        self.generate.executeSynchronous()

        if self.generate.isFailure():
            EDVerbose.ERROR('generating w/ and w/out anom failed')
            self.setFailure()
            return

        # we can now use the xds output parser on the two correct.lp
        # files, w/ and w/out anom
        parse_anom_input = XSDataXdsOutputFile()
        parse_anom_input.correct_lp = XSDataPath()
        parse_anom_input.correct_lp.path = self.generate.dataOutput.correct_lp_anom

        self.parse_xds_anom.dataInput = parse_anom_input
        self.parse_xds_anom.executeSynchronous()

        if self.parse_xds_anom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # now the other one w/out anom
        parse_noanom_input = XSDataXdsOutputFile()
        parse_noanom_input.correct_lp = XSDataPath()
        parse_noanom_input.correct_lp.path = self.generate.dataOutput.correct_lp_no_anom

        self.parse_xds_noanom.dataInput = parse_noanom_input
        self.parse_xds_noanom.executeSynchronous()

        if self.parse_xds_noanom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # we now can apply the res cutoff on the anom and no anom
        # outputs. Note that this is not done in parallel, like the
        # xds parsing

        # XXX completeness_cutoff/res_override and isig_cutoff still
        # missing
        res_cutoff_anom_in = XSDataResCutoff()
        res_cutoff_anom_in.xds_res = self.parse_xds_anom.dataOutput
        self.res_cutoff_anom.dataInput = res_cutoff_anom_in

        self.res_cutoff_anom.executeSynchronous()
        if self.res_cutoff_anom.isFailure():
            EDVerbose.ERROR('res cutoff for anom data failed')
            self.setFailure()
            return

        # same for non anom
        res_cutoff_noanom_in = XSDataResCutoff()
        res_cutoff_noanom_in.xds_res = self.parse_xds_noanom.dataOutput
        self.res_cutoff_noanom.dataInput = res_cutoff_noanom_in

        self.res_cutoff_noanom.executeSynchronous()
        if self.res_cutoff_noanom.isFailure():
            EDVerbose.ERROR('res cutoff for anom data failed')
            self.setFailure()
            return

        # now we just have to run XScale to generate w/ and w/out
        # anom, merged and unmerged

        # We use another control plugin for that to isolate the whole thing

        xscale_anom_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path = self.generate.dataOuput.hkl_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_anom_in.xds_files = [input_file]
        xscale_anom_in.unit_cell_constants = self.parse_xds_anom.dataOutput.unit_cell_constants
        xscale_anom_in.sg_number = self.parse_xds_anom.dataOutput.sg_number
        xscale_anom_in.bins = self.res_cutoff_anom.bins

        self.xscale_anom.dataInput = xscale_anom_in
        self.xscale_anom.executeSynchronous()

        if self.xscale_anom.isFailure():
            EDVerbose.ERROR('xscale anom/merge generation failed')
            self.setFailure()
            return

        # same for non anom code path
        xscale_noanom_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path = self.generate.dataOuput.hkl_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_noanom_in.xds_files = [input_file]
        xscale_noanom_in.unit_cell_constants = self.parse_xds_noanom.dataOutput.unit_cell_constants
        xscale_noanom_in.sg_number = self.parse_xds_noanom.dataOutput.sg_number
        xscale_noanom_in.bins = self.res_cutoff_noanom.bins

        self.xscale_noanom.dataInput = xscale_noanom_in
        self.xscale_noanom.executeSynchronous()

        if self.xscale_noanom.isFailure():
            EDVerbose.ERROR('xscale anom/merge generation failed')
            self.setFailure()
            return



    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

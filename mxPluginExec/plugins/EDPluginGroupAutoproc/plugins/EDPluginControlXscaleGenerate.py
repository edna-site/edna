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


from EDPluginControl import EDPluginControl

from XSDataCommon import XSDataBoolean

# we reuse the vanilla xscale input and will just ignore the friedel's
# law and merge boolean parameters
from XSDataAutoproc import XSDataXscaleInput, XSDataXscaleGeneratedFiles

class EDPluginControlXscaleGenerate(EDPluginControl):
    """
    Uses the XScale plugin to generate merged and unmerged and w/ and w/out anom
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataXscaleInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlXscaleGenerate.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlXscaleGenerate.preProcess")
        # Load the execution plugin
        self.xscale_anom_merged  = self.loadPlugin("EDPluginExecXscale")
        anom_merged_in = XSDataXscaleInput.copyViaDict()
        anom_merged_in.friedels_law = XSDataBoolean(True)
        anom_merged_in.merge = XSDataBoolean(True)
        self.xscale_anom_merged.dataInput = anom_merged_in
        self.xscale_anom_merged.connectSUCCESS(self.xscale_success)
        self.xscale_anom_merged.connectFAILURE(self.xscale_failure)


        self.xscale_anom_unmerged  = self.loadPlugin("EDPluginExecXscale")
        anom_unmerged_in = XSDataXscaleInput.copyViaDict()
        anom_unmerged_in.friedels_law = XSDataBoolean(True)
        anom_unmerged_in.merge = XSDataBoolean(False)
        self.xscale_anom_unmerged.dataInput = anom_unmerged_in
        self.xscale_anom_unmerged.connectSUCCESS(self.xscale_success)
        self.xscale_anom_unmerged.connectFAILURE(self.xscale_failure)

        self.xscale_noanom_merged  = self.loadPlugin("EDPluginExecXscale")
        noanom_merged_in = XSDataXscaleInput.copyViaDict()
        noanom_merged_in.friedels_law = XSDataBoolean(False)
        noanom_merged_in.merge = XSDataBoolean(True)
        self.xscale_noanom_merged.dataInput = noanom_merged_in
        self.xscale_noanom_merged.connectSUCCESS(self.xscale_success)
        self.xscale_noanom_merged.connectFAILURE(self.xscale_failure)

        self.xscale_noanom_unmerged  = self.loadPlugin("EDPluginExecXscale")
        noanom_unmerged_in = XSDataXscaleInput.copyViaDict()
        noanom_unmerged_in.friedels_law = XSDataBoolean(False)
        noanom_unmerged_in.merge = XSDataBoolean(False)
        self.xscale_noanom_unmerged.dataInput = noanom_unmerged_in
        self.xscale_noanom_unmerged.connectSUCCESS(self.xscale_success)
        self.xscale_noanom_unmerged.connectFAILURE(self.xscale_failure)

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlXscaleGenerate.process")

        # start all plugins
        for p in self.getListOfLoadedPlugin():
            p.execute()


    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlXscaleGenerate.postProcess")

        self.synchronizePlugins()

        out = XSDataXscaleGeneratedFiles()

        if not self.isFailure():
            out.anom_merged = self.xscale_anom_merged.dataOutput.output_file
            out.noanom_merged = self.xscale_noanom_merged.dataOutput.output_file
            out.anom_unmerged = self.xscale_anom_unmerged.dataOutput.output_file
            out.noanom_unmerged = self.xscale_noanom_unmerged.dataOutput.output_file
        self.dataOutput = out



    def xscale_success(self, plugin):
        EDVerbose.DEBUG('{!r} succeeded'.format(plugin))
        return

    def xscale_failure(self, plugin):
        EDVerbose.ERROR('{!r} failed'.format(plugin))
        self.setFailure()

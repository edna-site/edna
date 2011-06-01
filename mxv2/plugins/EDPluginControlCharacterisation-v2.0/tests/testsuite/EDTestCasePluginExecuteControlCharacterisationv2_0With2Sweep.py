#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


import os

from EDAssert                            import EDAssert

from EDTestCasePluginExecuteControlCharacterisationv2_0 import EDTestCasePluginExecuteControlCharacterisationv2_0




class EDTestCasePluginExecuteControlCharacterisationv2_0With2Sweep(EDTestCasePluginExecuteControlCharacterisationv2_0):
    """
    Bug#97: BEST two sweep strategy:
    Please download the following images under tests/data/images to perform this test
    /data/bugzilla/bug-97/ref-thermo1_1_001.img
    /data/bugzilla/bug-97/ref-thermo1_1_002.img
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecuteControlCharacterisationv2_0.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv2_0With2Sweep",)

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference_2_sweep.xml") , "mxv1InputCharacterisation")



    def preProcess(self):
        EDTestCasePluginExecuteControlCharacterisationv2_0.preProcess(self)
        self.loadTestImage([ "ref-thermo1_1_001.img", "ref-thermo1_1_002.img" ])


    def testExecute(self):
        EDTestCasePluginExecuteControlCharacterisationv2_0.testExecute(self)

        plugin = self.getPlugin()

        xsDataCharacterisation = plugin.getDataOutput()
        xsDataCollectionPlanList = xsDataCharacterisation.getStrategyResult().getCollectionPlan()

        EDAssert.equal(2, len(xsDataCollectionPlanList), "Length of xsDataCollectionPlanList should be 2")

        strRankingResolutionInitial = xsDataCollectionPlanList[1].getStrategySummary().getResolutionReasoning().getValue()
        EDAssert.equal("Resolution limit is set by the initial image resolution", strRankingResolutionInitial)

        #Ric: to avoid error:
        strRankingResolutionLow = xsDataCollectionPlanList[0].getStrategySummary().getResolutionReasoning().getValue()
        if (plugin.m_strPluginStrategyName == "EDPluginControlStrategyv1_1"):
            EDAssert.equal("Low-resolution pass, no overloads", strRankingResolutionLow, "(Low-resolution pass, no overloads)")
        elif (plugin.m_strPluginStrategyName == "EDPluginControlStrategyv1_2"):
            EDAssert.equal("Low-resolution pass, no overloads and full completeness", strRankingResolutionLow, "(Low-resolution pass, no overloads and full completeness)")




    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv2_0With2Sweep = EDTestCasePluginExecuteControlCharacterisationv2_0With2Sweep("EDTestCasePluginExecuteControlCharacterisationv2_0With2Sweep")
    edTestCasePluginExecuteControlCharacterisationv2_0With2Sweep.execute()

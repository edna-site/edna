#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlCharacterisationv1_1With2Sweep.py 1509 2010-05-11 07:17:48Z svensson $"
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlCharacterisationv1_2 import EDTestCasePluginExecuteControlCharacterisationv1_2




class EDTestCasePluginExecuteControlCharacterisationv1_2With2Sweep(EDTestCasePluginExecuteControlCharacterisationv1_2):
    """
    Bug#97: BEST two sweep strategy:
    Please download the following images under tests/data/images to perform this test
    /data/bugzilla/bug-97/ref-thermo1_1_001.img
    /data/bugzilla/bug-97/ref-thermo1_1_002.img
    """

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv1_2.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv1_2With2Sweep")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference_2_sweep.xml"))
        self.setNoExpectedWarningMessages(2)


    def preProcess(self):
        EDTestCasePluginExecuteControlCharacterisationv1_2.preProcess(self)
        self.loadTestImage([ "ref-thermo1_1_001.img", "ref-thermo1_1_002.img" ])


    def testExecute(self):
        EDTestCasePluginExecuteControlCharacterisationv1_2.testExecute(self)

        plugin = self.getPlugin()

        xsDataCharacterisation = plugin.getDataOutput()
        xsDataCollectionPlanList = xsDataCharacterisation.getStrategyResult().getCollectionPlan()

        EDAssert.equal(2, len(xsDataCollectionPlanList))

        strRankingResolutionInitial = xsDataCollectionPlanList[1].getStrategySummary().getResolutionReasoning().getValue()
        EDAssert.equal("Resolution limit is set by the initial image resolution", strRankingResolutionInitial)

        #Ric: to avoid error:
        strRankingResolutionLow = xsDataCollectionPlanList[0].getStrategySummary().getResolutionReasoning().getValue()
        if (plugin.getPluginStrategyName == "EDPluginControlStrategyv1_2"):
            EDAssert.equal("Low-resolution pass, no overloads", strRankingResolutionLow)
        elif (plugin.getPluginStrategyName == "EDPluginControlStrategyv1_2"):
            EDAssert.equal("Low-resolution pass, no overloads and full completeness", strRankingResolutionLow)




    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv1_2With2Sweep = EDTestCasePluginExecuteControlCharacterisationv1_2With2Sweep("EDTestCasePluginExecuteControlCharacterisationv1_2With2Sweep")
    edTestCasePluginExecuteControlCharacterisationv1_2With2Sweep.execute()

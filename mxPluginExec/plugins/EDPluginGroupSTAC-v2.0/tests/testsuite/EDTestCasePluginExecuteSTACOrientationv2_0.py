#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

import os


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath



class EDTestCasePluginExecuteSTACOrientationv2_0(EDTestCasePluginExecute):

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginSTACOrientationv2_0")

        edStringPluginTestDataHome = self.getPluginTestsDataHome()
        self.m_edStringExecutionTestDataInputHome = os.path.join(edStringPluginTestDataHome, "executionTestInput")
        self.m_edStringExecutionTestDataResultHome = os.path.join(edStringPluginTestDataHome, "executionTestResult")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.m_edStringExecutionTestDataInputHome, "EDPluginSTACOrientationv2_0_dataInputKappaStrategyOption_reference.xml"), "KappaStrategyOption")
        self.setDataInputFile(os.path.join(self.m_edStringExecutionTestDataInputHome, "EDPluginSTACOrientationv2_0_dataInputBest_reference.xml"), "inputBest")
        self.setDataInputFile(os.path.join(self.m_edStringExecutionTestDataInputHome, "EDPluginSTACOrientationv2_0_dataInputDataCollection_reference.xml"), "dataCollection")
        self.setDataInputFile(os.path.join(self.m_edStringExecutionTestDataInputHome, "EDPluginSTACOrientationv2_0_dataInputIndexingResult_reference.xml"), "indexingResult")
        self.__pyStrBCMDEFReference = os.path.join(self.m_edStringExecutionTestDataInputHome, "BCM.dat")

        self.setReferenceDataOutputFile(os.path.join(self.m_edStringExecutionTestDataResultHome, "EDPluginSTACOrientationv2_0_dataOutput_reference.xml"))
        #self.m_edObtainedOutputDataFile = self.getPluginName() + "_dataOutput.xml"
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        edPluginSTACOrientation = self.getPlugin()
        edPluginSTACOrientation.setBCMDEF(self.__pyStrBCMDEFReference)
        #self.loadTestImage( [ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ] )


    def testExecute(self):
        self.run()





    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteSTACOrientationv2_0 = EDTestCasePluginExecuteSTACOrientationv2_0("EDTestCasePluginExecuteSTACOrientationv2_0")
    edTestCasePluginExecuteSTACOrientationv2_0.execute()

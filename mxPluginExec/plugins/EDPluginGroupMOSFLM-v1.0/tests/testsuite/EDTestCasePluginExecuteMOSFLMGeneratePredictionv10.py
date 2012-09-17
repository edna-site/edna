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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"


import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute



class EDTestCasePluginExecuteMOSFLMGeneratePredictionv10(EDTestCasePluginExecute):

    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginMOSFLMGeneratePredictionv10")

        pyStrPluginTestDataHome = self.getPluginTestsDataHome()
        self.strExecutionTestDataInputHome = os.path.join(pyStrPluginTestDataHome, "executionTestInput")
        self.strExecutionTestDataResultHome = os.path.join(pyStrPluginTestDataHome, "executionTestResult")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.strExecutionTestDataInputHome, "XSDataMOSFLMInputGeneratePrediction_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.strExecutionTestDataResultHome, "XSDataMOSFLMOutputGeneratePrediction_reference.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()

        # Checks the expected result
        strObtainedOutput = self.readAndParseFile(self.m_edObtainedOutputDataFile)
        from XSDataMOSFLMv10 import XSDataMOSFLMOutputGeneratePrediction
        xsDataMOSFLMOutputGeneratePrediction = XSDataMOSFLMOutputGeneratePrediction.parseString(strObtainedOutput)
        strImagePath = xsDataMOSFLMOutputGeneratePrediction.getPredictionImage().getPath().getValue()
        bImageExists = os.path.exists(strImagePath)
        EDAssert.strAlmostEqual(True, bImageExists, "(Test if the image with prediction exists)")




    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteMOSFLMGeneratePredictionv10 = EDTestCasePluginExecuteMOSFLMGeneratePredictionv10("EDTestCasePluginExecuteMOSFLMGeneratePredictionv10")
    edTestCasePluginExecuteMOSFLMGeneratePredictionv10.execute()

#
#    Project: EDNA MXv1
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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteControlIndexingv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataIndexingInput_reference.xml"))
        self.strReferenceDataOutputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataIndexingResult_reference.xml")



    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile(self.strReferenceDataOutputFile)
        # Check that all the paths in the prediction results actaully exists
        from XSDataMXv1 import XSDataIndexingResult
        xsDataIndexingResultObtained = plugin.getDataOutput()
        xsDataIndexingResultExpected = XSDataIndexingResult.parseString(strExpectedOutput)
        xsDataGeneratePredictionResult = xsDataIndexingResultObtained.getPredictionResult()
        for predictionImage in xsDataGeneratePredictionResult.getPredictionImage():
            strImagePath = predictionImage.getPath().getValue()
            bImageExists = os.path.exists(strImagePath)
            EDAssert.equal(True, bImageExists)
        # Check that we found the right space group
        xsDataIndexingSolutionSelectedObtained = xsDataIndexingResultObtained.getSelectedSolution()
        xsDataIndexingSolutionSelectedExpected = xsDataIndexingResultExpected.getSelectedSolution()

        xsDataCrystalObtained = xsDataIndexingSolutionSelectedObtained.getCrystal()
        xsDataCrystalExpected = xsDataIndexingSolutionSelectedExpected.getCrystal()

        xsDataSpaceGroupObtained = xsDataCrystalObtained.getSpaceGroup()
        xsDataSpaceGroupExpected = xsDataCrystalExpected.getSpaceGroup()

        strSpacegroupNameObtained = xsDataSpaceGroupObtained.getName().getValue()
        strSpacegroupNameExpected = xsDataSpaceGroupExpected.getName().getValue()

        EDAssert.equal(strSpacegroupNameExpected, strSpacegroupNameObtained)




    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlIndexingv10 = EDTestCasePluginExecuteControlIndexingv10("EDTestCasePluginExecuteControlIndexingv10")
    edTestCasePluginExecuteControlIndexingv10.execute()

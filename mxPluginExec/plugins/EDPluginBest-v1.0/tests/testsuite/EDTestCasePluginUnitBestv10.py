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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "deprecated"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsFile import EDUtilsFile

class EDTestCasePluginUnitBestv10(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBestv10")
        self.strDataPath = self.getPluginTestsDataHome()

        self.strObtainedInputFile = "XSDataInputBestv10.xml"
        self.strObtainedInputFile2 = "XSDataInputBestv10FromObject_02.xml"
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataBestv10Input_reference.xml")
        self.strReferenceInputFile2 = os.path.join(self.strDataPath, "XSDataBestv10Input_reference_02.xml")

        self.strReferenceScriptLogFileName = os.path.join(self.strDataPath, "EDPluginBestv10.log")




    def testConfigureOK(self):
        edPluginBest = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.strDataPath, "XSConfiguration.xml"))
        edPluginBest.setConfiguration(xsPluginItemGood01)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()
        EDAssert.equal("/bin/bash", edPluginBest.getScriptShell())
        EDAssert.equal("cat", edPluginBest.getScriptExecutable())
        EDAssert.equal("/opt/pxsoft/ccp4-6.0.2/include/ccp4.setup-bash.orig", edPluginBest.getSetupCCP4())
        EDAssert.equal("Version of Best to be tested", edPluginBest.getStringVersion())
        #EDAssert.equal(600, edPluginMessage.getTimeOut())
        EDAssert.equal("/home/sweet/home", edPluginBest.getBestHome())
        EDAssert.equal("export besthome=/home/sweet/home", edPluginBest.getCommandBestHome())
        self.cleanUp(edPluginBest)


    def testSetDataModelInput(self):
        """
        """
        edPluginBest = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.strDataPath, "XSConfiguration.xml"))
        edPluginBest.setConfiguration(xsPluginItemGood01)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()

        from XSDataBestv10 import XSDataBestInput
        xsDataBestInput = XSDataBestInput()

        from XSDataCommon import XSDataAbsorbedDoseRate
        from XSDataCommon import XSDataFloat
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataTime
        from XSDataCommon import XSDataFile
        from XSDataCommon import XSDataSpeed
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataAngle

        xsDataBestInput.setCrystalAbsorbedDoseRate(XSDataAbsorbedDoseRate(0.22E+06))
        xsDataBestInput.setCrystalShape(XSDataFloat(1))
        xsDataBestInput.setCrystalSusceptibility(XSDataFloat(1.5))
        xsDataBestInput.setDetectorType(XSDataString("q210-2x"))
        xsDataBestInput.setBeamExposureTime(XSDataTime(1))
        xsDataBestInput.setBeamMaxExposureTime(XSDataTime(10000))
        xsDataBestInput.setBeamMinExposureTime(XSDataTime(0.1))
        xsDataBestInput.setGoniostatMinRotationWidth(XSDataAngle(0.1))
        xsDataBestInput.setGoniostatMaxRotationSpeed(XSDataSpeed(10))
        xsDataBestInput.setAimedResolution(XSDataFloat(2))
        xsDataBestInput.setAimedRedundancy(XSDataFloat(6.5))
        xsDataBestInput.setAimedCompleteness(XSDataFloat(0.9))
        xsDataBestInput.setAimedIOverSigma(XSDataFloat(3))
        xsDataBestInput.setComplexity(XSDataString("min"))
        fileDirectory = edPluginBest.getWorkingDirectory()

        bestFileContentDat = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.dat"))
        xsDataBestInput.setBestFileContentDat(XSDataString(bestFileContentDat))

        bestFileContentPar = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.par"))
        xsDataBestInput.setBestFileContentPar(XSDataString(bestFileContentPar))

        bestFileContentHKL = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile1.hkl"))
        listBestFileContentHKL = []
        listBestFileContentHKL.append(XSDataString(bestFileContentHKL))
        xsDataBestInput.setBestFileContentHKL(listBestFileContentHKL)

        xsDataBestInput.outputFile(self.strObtainedInputFile)

        strExpectedInput = self.readAndParseFile (self.strReferenceInputFile)
        strObtainedInput = self.readAndParseFile (self.strObtainedInputFile)

        xsDataInputExpected = XSDataBestInput.parseString(strExpectedInput)
        xsDataInputObtained = XSDataBestInput.parseString(strObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())

        self.cleanUp(edPluginBest)


##############################################################################

    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataModelInput)




if __name__ == '__main__':

    edTestCasePluginUnitBestv10 = EDTestCasePluginUnitBestv10("EDTestCasePluginUnitBestv10")
    edTestCasePluginUnitBestv10.execute()


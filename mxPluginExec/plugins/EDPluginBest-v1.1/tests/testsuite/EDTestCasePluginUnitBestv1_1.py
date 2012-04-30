#
#    Project: mxPluginExec
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

import os

from EDAssert                            import EDAssert
from EDUtilsFile                         import EDUtilsFile
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath


class EDTestCasePluginUnitBestv1_1(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):

        EDTestCasePluginUnit.__init__(self, "EDPluginBestv1_1")
        self.strDataPath = self.getPluginTestsDataHome()

        self.strObtainedInputFile = "XSDataInputBest_test.xml"
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataInputBest_reference.xml")
        self.strReferenceResultFile = os.path.join(self.strDataPath, "XSDataResultBest_reference.xml")

        self.strReferenceScriptLogFileName = os.path.join(self.strDataPath, "EDPluginBestv1_1.log")


    def testConfigureOK(self):
        edPluginBest = self.createPlugin()
        strConfigPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        xsPluginItemGood01 = self.getPluginConfiguration(strConfigPath)
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

        from XSDataBestv1_1 import XSDataInputBest
        xsDataInputBest = XSDataInputBest()

        from XSDataCommon import XSDataAbsorbedDoseRate
        from XSDataCommon import XSDataDouble
        from XSDataCommon import XSDataTime
        from XSDataCommon import XSDataSpeed
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataAngle
        from XSDataCommon import XSDataBoolean

        xsDataInputBest.setCrystalAbsorbedDoseRate(XSDataAbsorbedDoseRate(0.22E+06))
        xsDataInputBest.setCrystalShape(XSDataDouble(1))
        xsDataInputBest.setCrystalSusceptibility(XSDataDouble(1.5))
        xsDataInputBest.setDetectorType(XSDataString("q210-2x"))
        xsDataInputBest.setBeamExposureTime(XSDataTime(1))
        xsDataInputBest.setBeamMaxExposureTime(XSDataTime(10000))
        xsDataInputBest.setBeamMinExposureTime(XSDataTime(0.1))
        xsDataInputBest.setGoniostatMinRotationWidth(XSDataAngle(0.1))
        xsDataInputBest.setGoniostatMaxRotationSpeed(XSDataSpeed(10))
        xsDataInputBest.setAimedResolution(XSDataDouble(2))
        xsDataInputBest.setAimedRedundancy(XSDataDouble(6.5))
        xsDataInputBest.setAimedCompleteness(XSDataDouble(0.9))
        xsDataInputBest.setAimedIOverSigma(XSDataDouble(3))
        xsDataInputBest.setComplexity(XSDataString("min"))
        xsDataInputBest.setAnomalousData(XSDataBoolean(True))

        bestFileContentDat = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.dat"))
        xsDataInputBest.setBestFileContentDat(XSDataString(bestFileContentDat))

        bestFileContentPar = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.par"))
        xsDataInputBest.setBestFileContentPar(XSDataString(bestFileContentPar))

        bestFileContentHKL = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile1.hkl"))
        listBestFileContentHKL = []
        listBestFileContentHKL.append(XSDataString(bestFileContentHKL))
        xsDataInputBest.setBestFileContentHKL(listBestFileContentHKL)

        xsDataInputBest.outputFile(self.strObtainedInputFile)

        strExpectedInput = self.readAndParseFile (self.strReferenceInputFile)
        strObtainedInput = self.readAndParseFile (self.strObtainedInputFile)

        xsDataInputExpected = XSDataInputBest.parseString(strExpectedInput)
        xsDataInputObtained = XSDataInputBest.parseString(strObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())
        os.remove(self.strObtainedInputFile)

        self.cleanUp(edPluginBest)


    def testGenerateExecutiveSummary(self):
        strInputBest = self.readAndParseFile (self.strReferenceInputFile)
        strResultBest = self.readAndParseFile (self.strReferenceResultFile)

        from XSDataBestv1_1 import XSDataInputBest
        from XSDataBestv1_1 import XSDataResultBest

        xsDataInputBest = XSDataInputBest.parseString(strInputBest)
        xsDataResultBest = XSDataResultBest.parseString(strResultBest)
        edPluginBest = self.createPlugin()
        edPluginBest.setDataInput(xsDataInputBest)
        edPluginBest.setDataOutput(xsDataResultBest)
        edPluginBest.generateExecutiveSummary(edPluginBest)


    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataModelInput)
        self.addTestMethod(self.testGenerateExecutiveSummary)




if __name__ == '__main__':

    edTestCasePluginUnitBestv1_1 = EDTestCasePluginUnitBestv1_1("EDTestCasePluginUnitBestv1_1")
    edTestCasePluginUnitBestv1_1.execute()


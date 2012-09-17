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
__status__ = "production"

import os


from EDUtilsPath                         import EDUtilsPath
from EDAssert                            import EDAssert
from EDUtilsFile                         import EDUtilsFile
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath


class EDTestCasePluginUnitBestv1_2(EDTestCasePluginUnit):

    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBestv1_2")
        self.m_pyStrDataPath = self.getPluginTestsDataHome()

        self.m_edObtainedInputFile = "XSDataInputBest_test.xml"
        self.m_edReferenceInputFile = os.path.join(self.m_pyStrDataPath, "XSDataInputBest_reference.xml")
        self.m_edReferenceResultFile = os.path.join(self.m_pyStrDataPath, "XSDataResultBest_reference.xml")

        self.m_edReferenceScriptLogFileName = os.path.join(self.m_pyStrDataPath, "EDPluginBestv1_2.log")


    def testConfigureOK(self):
        edPluginBest = self.createPlugin()
        pyStrConfigPath = os.path.join(self.m_pyStrDataPath, "XSConfiguration.xml")
        xsPluginItemGood01 = self.getPluginConfiguration(pyStrConfigPath)
        edPluginBest.setConfiguration(xsPluginItemGood01)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()
        EDAssert.equal("/bin/bash", edPluginBest.getScriptShell())
        EDAssert.equal("cat", edPluginBest.getScriptExecutable())
        EDAssert.equal("/opt/pxsoft/ccp4-6.0.2/include/ccp4.setup-bash.orig", edPluginBest.getSetupCCP4())
        EDAssert.equal("Version of Best to be tested", edPluginBest.getStringVersion())
        EDAssert.equal(600, edPluginBest.getTimeOut())
        EDAssert.equal("/home/sweet/home", edPluginBest.getBestHome())
        EDAssert.equal("export besthome=/home/sweet/home", edPluginBest.getCommandBestHome())
        self.cleanUp(edPluginBest)


    def testSetDataModelInput(self):
        edPluginBest = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.m_pyStrDataPath, "XSConfiguration.xml"))
        edPluginBest.setConfiguration(xsPluginItemGood01)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()

        from XSDataBestv1_2 import XSDataInputBest
        xsDataInputBest = XSDataInputBest()

        from XSDataCommon import XSDataAbsorbedDoseRate
        from XSDataCommon import XSDataDouble
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataTime
        from XSDataCommon import XSDataFile
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
        xsDataInputBest.setAnomalousData(XSDataBoolean(False))
        fileDirectory = edPluginBest.getWorkingDirectory()

        bestFileContentDat = EDUtilsFile.readFile(os.path.join(self.m_pyStrDataPath, "bestfile.dat"))
        xsDataInputBest.setBestFileContentDat(XSDataString(bestFileContentDat))

        bestFileContentPar = EDUtilsFile.readFile(os.path.join(self.m_pyStrDataPath, "bestfile.par"))
        xsDataInputBest.setBestFileContentPar(XSDataString(bestFileContentPar))

        bestFileContentHKL = EDUtilsFile.readFile(os.path.join(self.m_pyStrDataPath, "bestfile1.hkl"))
        xsDataInputBest.addBestFileContentHKL(XSDataString(bestFileContentHKL))

        xsDataInputBest.exportToFile(self.m_edObtainedInputFile)

        pyStrExpectedInput = self.readAndParseFile (self.m_edReferenceInputFile)
        pyStrObtainedInput = self.readAndParseFile (self.m_edObtainedInputFile)

        xsDataInputExpected = XSDataInputBest.parseString(pyStrExpectedInput)
        xsDataInputObtained = XSDataInputBest.parseString(pyStrObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())
        EDUtilsFile.deleteFile(self.m_edObtainedInputFile)

        self.cleanUp(edPluginBest)


    def testGenerateExecutiveSummary(self):
        pyStrInputBest = self.readAndParseFile (self.m_edReferenceInputFile)
        pyStrResultBest = self.readAndParseFile (self.m_edReferenceResultFile)

        from XSDataBestv1_2 import XSDataInputBest
        from XSDataBestv1_2 import XSDataResultBest

        xsDataInputBest = XSDataInputBest.parseString(pyStrInputBest)
        xsDataResultBest = XSDataResultBest.parseString(pyStrResultBest)
        edPluginBest = self.createPlugin()
        edPluginBest.setDataInput(xsDataInputBest)
        edPluginBest.setDataOutput(xsDataResultBest)
        edPluginBest.generateExecutiveSummary(edPluginBest)


    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataModelInput)
        #self.addTestMethod(self.testGenerateExecutiveSummary)



if __name__ == '__main__':

    edTestCasePluginUnitBestv1_2 = EDTestCasePluginUnitBestv1_2("EDTestCasePluginUnitBestv1_2")
    edTestCasePluginUnitBestv1_2.execute()


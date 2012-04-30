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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit


class EDTestCasePluginUnitRaddosev10(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginRaddosev10")

        self.strDataPath = self.getPluginTestsDataHome()
        self.strObtainedInputFile = "XSDataInputRaddosev10.xml"
        self.strObtainedInputFile2 = "XSDataInputRaddosev10FromObject_02.xml"
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataRaddosev10Input_reference.xml")
        self.strReferenceInputFile2 = os.path.join(self.strDataPath, "XSDataRaddosev10Input_reference_02.xml")

        self.strReferenceScriptLogFileName = os.path.join(self.strDataPath, "EDPluginRaddosev10.log")
        self.strReferenceScriptLogFileNamev2 = os.path.join(self.strDataPath, "EDPluginRaddosev10_Raddosev2.log")




    def testConfigureOK(self):
        edPluginRaddose = self.createPlugin()
        edStringConfigurationFile = os.path.join(self.strDataPath, "XSConfiguration.xml")
        xsPluginItemGood01 = self.getPluginConfiguration(edStringConfigurationFile)
        edPluginRaddose.setConfiguration(xsPluginItemGood01)
        edPluginRaddose.setScriptExecutable("cat")
        edPluginRaddose.configure()
        EDAssert.equal("/bin/bash", edPluginRaddose.getScriptShell())
        EDAssert.equal("cat", edPluginRaddose.getScriptExecutable())
        EDAssert.equal("/opt/pxsoft/ccp4-6.0.2/include/ccp4.setup-bash.orig", edPluginRaddose.getSetupCCP4())
        EDAssert.equal("Verion of Raddose to be tested", edPluginRaddose.getStringVersion())
        #EDAssert.equal(600, edPluginMessage.getTimeOut())

        self.cleanUp(edPluginRaddose)


    def testSetDataModelInput(self):
        # Crystal         
        from XSDataRaddosev10 import XSDataRaddoseInput
        xsDataRaddoseInput = XSDataRaddoseInput()

        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataFloat
        from XSDataCommon import XSDataAngle
        from XSDataCommon import XSDataLength
        from XSDataCommon import XSDataSize
        from XSDataCommon import XSDataInteger
        from XSDataRaddosev10 import XSDataCell
        from XSDataRaddosev10 import XSDataAtom
        from XSDataRaddosev10 import XSDataAtomicComposition

        xsDataAtomSulfur = XSDataAtom()
        xsDataAtomSulfur.setNumberOf(XSDataFloat(4))
        xsDataAtomSulfur.setSymbol(XSDataString("S"))
        xsDataAtomSelenium = XSDataAtom()
        xsDataAtomSelenium.setNumberOf(XSDataFloat(4))
        xsDataAtomSelenium.setSymbol(XSDataString("Se"))

        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomicComposition.addAtom(xsDataAtomSulfur)
        xsDataAtomicComposition.addAtom(xsDataAtomSelenium)
        xsDataRaddoseInput.setCrystalPATM(xsDataAtomicComposition)
        xsDataRaddoseInput.setCrystalNRES(XSDataInteger(295))
        xsDataRaddoseInput.setCrystalNMON(XSDataInteger(8))
        xsDataCell = XSDataCell(angle_alpha = XSDataAngle(90.0),
                                angle_beta =  XSDataAngle(90.0),
                                angle_gamma =  XSDataAngle(90.0),
                                length_a = XSDataLength(78.9),
                                length_b = XSDataLength(95.162),
                                length_c = XSDataLength(104.087))

        xsDataSizeCrystal = XSDataSize(XSDataLength(0.1),
                                        XSDataLength(0.1),
                                        XSDataLength(0.1))

        xsDataRaddoseInput.setCrystalCell(xsDataCell)
        xsDataRaddoseInput.setCrystalSize(xsDataSizeCrystal)

        # Beam
        from XSDataCommon import XSDataFlux
        from XSDataCommon import XSDataWavelength
        from XSDataCommon import XSDataTime

        xsDataSize = XSDataSize(x = XSDataLength(0.1),
                                y = XSDataLength(0.1))

        xsDataRaddoseInput.setBeamSize(xsDataSize)
        xsDataRaddoseInput.setBeamFlux(XSDataFlux(1e+12))
        xsDataRaddoseInput.setBeamWavelength(XSDataWavelength(2.41))
        xsDataRaddoseInput.setBeamExposureTime(XSDataTime(1))

        xsDataRaddoseInput.setNumberOfImages(XSDataInteger(1))

        xsDataRaddoseInput.exportToFile(self.strObtainedInputFile)

        strExpectedInput = self.readAndParseFile (self.strReferenceInputFile)
        strObtainedInput = self.readAndParseFile (self.strObtainedInputFile)

        xsDataRaddoseInputExpected = XSDataRaddoseInput.parseString(strExpectedInput)
        xsDataRaddoseInputObtained = XSDataRaddoseInput.parseString(strObtainedInput)

        EDAssert.equal(xsDataRaddoseInputExpected.marshal(), xsDataRaddoseInputObtained.marshal())


    def testSetDataInput(self):

        from XSDataRaddosev10 import XSDataRaddoseInput
        edPluginRaddose = self.createPlugin()

        strXMLInputData = self.readAndParseFile (self.strReferenceInputFile)
        edPluginRaddose.setDataInput(strXMLInputData)
        edPluginRaddose.setScriptExecutable("cat")
        edPluginRaddose.preProcess()

        xsDataInput = edPluginRaddose.getDataInput()
        xsDataInput.exportToFile("XSDataInputRaddosev10FromObject.xml")
        strExpectedInput = self.readAndParseFile(self.strReferenceInputFile)
        strObtainedInput = self.readAndParseFile("XSDataInputRaddosev10FromObject.xml")

        xsDataRaddoseInputExpected = XSDataRaddoseInput.parseString(strExpectedInput)
        xsDataRaddoseInputObtained = XSDataRaddoseInput.parseString(strObtainedInput)

        EDAssert.equal(xsDataRaddoseInputExpected.marshal(), xsDataRaddoseInputObtained.marshal())

        EDAssert.equal("CELL 78.9 95.162 104.087 90.0 90.0 90.0", edPluginRaddose.getCommandCrystalCell())

        EDAssert.equal("NRES 295", edPluginRaddose.getCommandCrystalNRES())
        EDAssert.equal("NMON 8", edPluginRaddose.getCommandCrystalNMON())
        EDAssert.equal(None, edPluginRaddose.getCommandCrystalNDNA())
        EDAssert.equal(None, edPluginRaddose.getCommandCrystalNRNA())
        EDAssert.equal("S", xsDataInput.getCrystalPATM().getAtom()[0].getSymbol().getValue())
        EDAssert.equal(4, xsDataInput.getCrystalPATM().getAtom()[0].getNumberOf().getValue())
        EDAssert.equal("Se", xsDataInput.getCrystalPATM().getAtom()[1].getSymbol().getValue())
        EDAssert.equal(4, xsDataInput.getCrystalPATM().getAtom()[1].getNumberOf().getValue())
        EDAssert.equal("PATM S 4.0 Se 4.0", edPluginRaddose.getCommandCrystalPATM())
        EDAssert.equal(None, xsDataInput.getCrystalSATM())
        EDAssert.equal(None, edPluginRaddose.getCommandCrystalSATM())
        EDAssert.equal("CRYSTAL 0.1 0.1 0.1", edPluginRaddose.getCommandCrystalSize())

        EDAssert.equal("BEAM 0.1 0.1", edPluginRaddose.getCommandBeamSize())
        EDAssert.equal("PHOSEC 1e+12", edPluginRaddose.getCommandBeamFlux())
        EDAssert.equal("WAVELENGTH 2.41", edPluginRaddose.getCommandBeamWavelength())

        EDAssert.equal("EXPOSURE 1.0", edPluginRaddose.getCommandExposureTime())
        EDAssert.equal("IMAGES 1", edPluginRaddose.getCommandImages())

        self.cleanUp(edPluginRaddose)


    def testDictionnaryResults(self):

        # Tests with Raddose v? (old version, no Raddose version management...)
        edPluginRaddose = self.createPlugin()
        expectedDictionnaryv1 = {}
        expectedDictionnaryv1["Dose in Grays"] = "0.22E+06"
        expectedDictionnaryv1["Total absorbed dose (Gy)"] = None
        expectedDictionnaryv1["Solvent Content (%)"] = "59.2"
        obtainedDictionnaryv1 = edPluginRaddose.analyseScriptLogFileName(self.strReferenceScriptLogFileName)
        EDAssert.equal(expectedDictionnaryv1, obtainedDictionnaryv1)

        # Tests with Raddose v2
        edPluginRaddose = self.createPlugin()
        expectedDictionnaryv2 = {}
        expectedDictionnaryv2["Dose in Grays"] = None
        expectedDictionnaryv2["Total absorbed dose (Gy)"] = "0.223E+06"
        expectedDictionnaryv2["Solvent Content (%)"] = "59.2"
        obtainedDictionnaryv2 = edPluginRaddose.analyseScriptLogFileName(self.strReferenceScriptLogFileNamev2)
        EDAssert.equal(expectedDictionnaryv2, obtainedDictionnaryv2)





    def process(self):
        """
        """
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataModelInput)
        self.addTestMethod(self.testSetDataInput)
        self.addTestMethod(self.testDictionnaryResults)



if __name__ == '__main__':

    edTestCasePluginUnitRaddosev10 = EDTestCasePluginUnitRaddosev10("EDTestCasePluginUnitRaddosev10")
    edTestCasePluginUnitRaddosev10.execute()


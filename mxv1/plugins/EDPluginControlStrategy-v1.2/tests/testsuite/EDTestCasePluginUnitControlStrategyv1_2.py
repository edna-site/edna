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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDVerbose                           import EDVerbose
from EDUtilsFile                         import EDUtilsFile
from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest

from XSDataCommon import XSDataFlux
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger

from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataStructure
from XSDataMXv1 import XSDataChain
from XSDataMXv1 import XSDataAtom
from XSDataMXv1 import XSDataLigand
from XSDataMXv1 import XSDataSampleCrystalMM
from XSDataMXv1 import XSDataChemicalCompositionMM
from XSDataMXv1 import XSDataAtomicComposition
from XSDataMXv1 import XSDataSolvent
from XSDataMXv1 import XSDataCell
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataBeam
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataGoniostat

class EDTestCasePluginUnitControlStrategyv1_2(EDTestCasePluginUnit):

    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlStrategyv1_2", "EDPluginControlStrategy-v1.1", _pyStrTestName)
        self.strDataPath = self.getPluginTestsDataHome()
        self.strObtainedInputFile = "XSDataInputStrategyv1_2.xml"
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataInputStrategy_unitTest.xml")


    def testConfigureOK(self):
        edPluginStrategy = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.strDataPath, "XSConfiguration_ESRF.xml"))
        edPluginStrategy.setConfiguration(xsPluginItemGood01)
        edPluginStrategy.configure()
        EDAssert.equal("/opt/pxsoft/ccp4-6.0.2/lib/data", edPluginStrategy.getSymopHome())


    def testSetDataModelInput(self):
        edPluginStrategy = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.strDataPath, "XSConfiguration_ESRF.xml"))
        edPluginStrategy.setConfiguration(xsPluginItemGood01)
        edPluginStrategy.configure()

        from XSDataMXv1 import XSDataStrategyInput
        xsDataStrategy = XSDataStrategyInput()

        # Beam

        xsExperimentalCondition = XSDataExperimentalCondition()

        xsBeam = XSDataBeam()
        xsBeam.setFlux(XSDataFlux(1e+12))
        xsBeam.setWavelength(XSDataWavelength(2.41))
        xsBeam.setSize(XSDataSize(x=XSDataLength(0.1), y=XSDataLength(0.1)))
        xsBeam.setExposureTime(XSDataTime(1))

        xsExperimentalCondition.setBeam(xsBeam)

        # Detector and Exposure Time

        xsDataDetector = XSDataDetector()
        xsDataDetector.setType(XSDataString("q210-2x"))
        xsExperimentalCondition.setDetector(xsDataDetector)

        xsDataGoniostat = XSDataGoniostat()
        xsDataGoniostat.setRotationAxis(XSDataString("phi"))
        xsExperimentalCondition.setGoniostat(xsDataGoniostat)

        xsDataStrategy.setExperimentalCondition(xsExperimentalCondition)


        # Best Files
        bestFileContentDat = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.dat"))
        xsDataStrategy.setBestFileContentDat(XSDataString(bestFileContentDat))
        bestFileContentPar = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.par"))
        xsDataStrategy.setBestFileContentPar(XSDataString(bestFileContentPar))
        bestFileContentHKL = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile1.hkl"))
        xsDataStrategy.addBestFileContentHKL(XSDataString(bestFileContentHKL))

        # Crystal

        xsDataSampleCrystalMM = XSDataSampleCrystalMM()
        xsDataStructure = XSDataStructure()
        xsDataComposition = XSDataChemicalCompositionMM()

        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfCopies(XSDataDouble(2))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtom1 = XSDataAtom()
        xsDataAtom1.setSymbol(XSDataString("Se"))
        xsDataAtom1.setNumberOf(XSDataDouble(4))
        xsDataAtomicComposition.addAtom(xsDataAtom1)

        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)
        xsDataChain.setNumberOfMonomers(XSDataDouble(100))
        xsDataStructure.addChain(xsDataChain)

        xsDataChain2 = XSDataChain()
        xsDataChain2.setType(XSDataString("rna"))
        xsDataChain2.setNumberOfCopies(XSDataDouble(1))
        xsDataChain2.setNumberOfMonomers(XSDataDouble(60))
        xsDataStructure.addChain(xsDataChain2)

        xsDataLigand = XSDataLigand()
        xsDataLigand.setNumberOfCopies(XSDataDouble(2))
        xsDataLigand.setNumberOfLightAtoms(XSDataDouble(42))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtom2 = XSDataAtom()
        xsDataAtom2.setSymbol(XSDataString("Fe"))
        xsDataAtom2.setNumberOf(XSDataDouble(1))
        xsDataAtomicComposition.addAtom(xsDataAtom2)
        xsDataLigand.setHeavyAtoms(xsDataAtomicComposition)
        xsDataStructure.addLigand(xsDataLigand)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataDouble(0.25))

        xsDataSolvent = XSDataSolvent()
        xsDataAtomicComposition = XSDataAtomicComposition()

        xsDataAtom3 = XSDataAtom()
        xsDataAtom3.setSymbol(XSDataString("Na"))
        xsDataAtom3.setConcentration(XSDataDouble(1000))
        xsDataAtom4 = XSDataAtom()
        xsDataAtom4.setSymbol(XSDataString("Cl"))
        xsDataAtom4.setConcentration(XSDataDouble(1000))

        xsDataAtomicComposition.addAtom(xsDataAtom3)
        xsDataAtomicComposition.addAtom(xsDataAtom4)
        xsDataSolvent.setAtoms(xsDataAtomicComposition)

        xsDataComposition.setStructure(xsDataStructure)
        xsDataComposition.setSolvent(xsDataSolvent)
        xsDataSampleCrystalMM.setChemicalComposition(xsDataComposition)

        xsDataSampleCrystalMM.setSize(XSDataSize(XSDataLength(0.1), XSDataLength(0.1), XSDataLength(0.1)))

        xsDataCrystal = XSDataCrystal()
        xsDataCell = XSDataCell(angle_alpha=XSDataAngle(90.0),
                                angle_beta=XSDataAngle(90.0),
                                angle_gamma=XSDataAngle(90.0),
                                length_a=XSDataLength(78.9),
                                length_b=XSDataLength(95.162),
                                length_c=XSDataLength(104.087))
        xsDataCrystal.setCell(xsDataCell)

        xsDataSpaceGroup = XSDataSpaceGroup()
        xsDataSpaceGroup.setITNumber(XSDataInteger(16))
        xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)

        xsDataSampleCrystalMM.setSusceptibility(XSDataDouble(1.5))

        xsDataStrategy.setCrystalRefined(xsDataCrystal)

        xsDataStrategy.setSample(xsDataSampleCrystalMM)

        xsDataStrategy.exportToFile(self.strObtainedInputFile)

        pyStrExpectedInput = self.readAndParseFile (self.strReferenceInputFile)
        pyStrObtainedInput = self.readAndParseFile (self.strObtainedInputFile)

        xsDataInputExpected = XSDataStrategyInput.parseString(pyStrExpectedInput)
        xsDataInputObtained = XSDataStrategyInput.parseString(pyStrObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())


    def testDefaultChemicalComposition(self):
        edPluginStrategy = self.createPlugin()

        xsDataSampleCrystalMM = XSDataSampleCrystalMM()
        xsDataCrystal = XSDataCrystal()
        xsDataCell = XSDataCell(XSDataAngle(90.0),
                                 XSDataAngle(90.0),
                                 XSDataAngle(90.0),
                                 XSDataLength(78.9),
                                 XSDataLength(95.162),
                                 XSDataLength(104.087))
        xsDataCrystal.setCell(xsDataCell)
        xsDataSampleCrystalMM.setCrystal(xsDataCrystal)
        inumOperators = 4

        xsDataSample2 = edPluginStrategy.getDefaultChemicalComposition(xsDataSampleCrystalMM, inumOperators)
        pyStrChainType = xsDataSample2.getStructure().getChain()[0].getType()
        EDAssert.equal("protein", pyStrChainType.getValue())


    def testUpdateChemicalCompositionWithNativeSulfurAtom(self):

        edPluginStrategy = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.strDataPath, "XSConfiguration_ESRF.xml"))
        edPluginStrategy.setConfiguration(xsPluginItemGood01)
        edPluginStrategy.configure()

        xsDataStructure = XSDataStructure()
        xsDataComposition = XSDataChemicalCompositionMM()
        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfCopies(XSDataDouble(2))
        xsDataChain.setNumberOfMonomers(XSDataDouble(60))
        xsDataStructure.addChain(xsDataChain)
        xsDataComposition.setStructure(xsDataStructure)
        updatedChemicalComposition = edPluginStrategy.updateChemicalComposition(xsDataComposition)
        EDAssert.equal(3, updatedChemicalComposition.getStructure().getChain()[0].getHeavyAtoms().getAtom()[0].getNumberOf().getValue())
        EDAssert.equal("S", updatedChemicalComposition.getStructure().getChain()[0].getHeavyAtoms().getAtom()[0].getSymbol().getValue())

        xsDataStructure = XSDataStructure()
        xsDataComposition = XSDataChemicalCompositionMM()
        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfCopies(XSDataDouble(2))
        xsDataChain.setNumberOfMonomers(XSDataDouble(60))
        xsDataAtom1 = XSDataAtom()
        xsDataAtom1.setSymbol(XSDataString("Se"))
        xsDataAtom1.setNumberOf(XSDataDouble(4))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomicComposition.addAtom(xsDataAtom1)
        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)
        xsDataStructure.addChain(xsDataChain)
        xsDataComposition.setStructure(xsDataStructure)
        updatedChemicalComposition = edPluginStrategy.updateChemicalComposition(xsDataComposition)
        heavyAtoms = updatedChemicalComposition.getStructure().getChain()[0].getHeavyAtoms().getAtom()
        for heavyAtom in heavyAtoms:
            EDVerbose.unitTest(heavyAtom.getSymbol().getValue() + " : " + str(heavyAtom.getNumberOf().getValue()))
            if(heavyAtom.getSymbol().getValue() == "S"):
                EDAssert.equal(3, heavyAtom.getNumberOf().getValue())


    def testGenerateStrategyShortSummary(self):
        edPluginStrategy = self.createPlugin()
        strReferenceOutputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultStrategy_2_sweep.xml")
        strXML = self.readAndParseFile(strReferenceOutputFile)
        xsDataStrategyResult = XSDataResultStrategy.parseString(strXML)
        edPluginStrategy.generateStrategyShortSummary(xsDataStrategyResult)
        for strLine in edPluginStrategy.getDataOutput("strategyShortSummary")[0].getValue().split("\n"):
            EDVerbose.unitTest(strLine)


    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataModelInput)
        self.addTestMethod(self.testDefaultChemicalComposition)
        self.addTestMethod(self.testUpdateChemicalCompositionWithNativeSulfurAtom)
        self.addTestMethod(self.testGenerateStrategyShortSummary)




if __name__ == '__main__':

    edTestCasePluginUnitControlStrategyv1_2 = EDTestCasePluginUnitControlStrategyv1_2("EDTestCasePluginUnitControlStrategyv1_2")
    edTestCasePluginUnitControlStrategyv1_2.execute()


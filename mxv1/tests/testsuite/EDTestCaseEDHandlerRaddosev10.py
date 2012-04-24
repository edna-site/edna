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


from EDTestCase                      import EDTestCase
from EDAssert                        import EDAssert
from EDUtilsPath                     import EDUtilsPath
from EDUtilsTest                     import EDUtilsTest
from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDTestCaseEDHandlerRaddosev10(EDTestCase):


    def __init__(self, _pyStrTestName=None):
        EDTestCase.__init__(self, _pyStrTestName)
        strKernelDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerRaddosev10"
        self.strDataPath = EDUtilsPath.mergePath(strKernelDataHome, strDataDir)
        self.strReferenceInputFile2 = EDUtilsPath.mergePath(self.strDataPath, "XSDataRaddosev10Input_reference_02.xml")
        self.strObtainedInputFile2 = "XSDataInputRaddosev10FromObject_02.xml"


    def testGetXSDataRaddoseInput(self):
        """
        """
        from XSDataCommon import XSDataLength
        from XSDataCommon import XSDataWavelength
        from XSDataCommon import XSDataFlux
        from XSDataCommon import XSDataSize
        from XSDataCommon import XSDataDouble
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataAngle
        from XSDataCommon import XSDataTime
        from XSDataCommon import XSDataInteger

        from XSDataMXv1   import XSDataBeam
        from XSDataMXv1   import XSDataStructure
        from XSDataMXv1   import XSDataChain
        from XSDataMXv1   import XSDataAtom
        from XSDataMXv1   import XSDataLigand
        from XSDataMXv1   import XSDataCrystal
        from XSDataMXv1   import XSDataSpaceGroup
        from XSDataMXv1   import XSDataSampleCrystalMM
        from XSDataMXv1   import XSDataChemicalCompositionMM
        from XSDataMXv1   import XSDataAtomicComposition
        from XSDataMXv1   import XSDataSolvent
        from XSDataMXv1   import XSDataCell

        from EDHandlerXSDataRaddosev10 import EDHandlerXSDataRaddosev10

        EDFactoryPluginStatic.loadModule("XSDataRaddosev10")
        from XSDataRaddosev10 import XSDataRaddoseInput

        xsDataBeam = XSDataBeam()
        xsDataBeam.setSize(XSDataSize(x=XSDataLength(0.1), y=XSDataLength(0.1)))
        xsDataBeam.setWavelength(XSDataWavelength(2.41))
        xsDataBeam.setFlux(XSDataFlux(1e+12))

        xsDataSample = XSDataSampleCrystalMM()
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
        xsDataAtom2 = XSDataAtom()
        xsDataAtom2.setSymbol(XSDataString("S"))
        xsDataAtom2.setNumberOf(XSDataDouble(5))
        xsDataAtomicComposition.addAtom(xsDataAtom2)
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
        xsDataAtom3 = XSDataAtom()
        xsDataAtom3.setSymbol(XSDataString("Fe"))
        xsDataAtom3.setNumberOf(XSDataDouble(1))
        xsDataAtomicComposition.addAtom(xsDataAtom3)
        xsDataLigand.setHeavyAtoms(xsDataAtomicComposition)
        xsDataStructure.addLigand(xsDataLigand)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataDouble(0.25))

        xsDataSolvent = XSDataSolvent()
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomNa = XSDataAtom()
        xsDataAtomNa.setSymbol(XSDataString("Na"))
        xsDataAtomNa.setConcentration(XSDataDouble(1000))
        xsDataAtomicComposition.addAtom(xsDataAtomNa)
        xsDataAtomCl = XSDataAtom()
        xsDataAtomCl.setSymbol(XSDataString("Cl"))
        xsDataAtomCl.setConcentration(XSDataDouble(1000))
        xsDataAtomicComposition.addAtom(xsDataAtomCl)
        xsDataSolvent.setAtoms(xsDataAtomicComposition)

        xsDataComposition.setStructure(xsDataStructure)
        xsDataComposition.setSolvent(xsDataSolvent)
        xsDataSample.setChemicalComposition(xsDataComposition)

        xsDataSample.setSize(XSDataSize(XSDataLength(0.1), XSDataLength(0.1), XSDataLength(0.1)))
        xsDataCell = XSDataCell(angle_alpha=XSDataAngle(90.0),
                                angle_beta=XSDataAngle(90.0),
                                angle_gamma=XSDataAngle(90.0),
                                length_a=XSDataLength(78.9),
                                length_b=XSDataLength(95.162),
                                length_c=XSDataLength(104.087))

        xsDataCrystal = XSDataCrystal()
        xsDataSpaceGroup = XSDataSpaceGroup()

        xsDataCrystal.setCell(xsDataCell)

        xsDataSpaceGroup.setITNumber(XSDataInteger(16))
        xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)

        xsDataSample.setCrystal(xsDataCrystal)

        iNumSymOperators = 4


        xsDataRaddosev01Input = EDHandlerXSDataRaddosev10().getXSDataRaddoseInput(xsDataBeam,
                                                                                      xsDataSample,
                                                                                      iNumSymOperators)


        xsDataRaddosev01Input.exportToFile(self.strObtainedInputFile2)
        strExpectedInput = EDUtilsTest.readAndParseFile (self.strReferenceInputFile2)
        strObtainedInput = EDUtilsTest.readAndParseFile (self.strObtainedInputFile2)

        xsDataInputExpected = XSDataRaddoseInput.parseString(strExpectedInput)
        xsDataInputObtained = XSDataRaddoseInput.parseString(strObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())


    def testMergeAtomicComposition(self):
        from XSDataRaddosev10 import XSDataAtomicComposition
        from XSDataRaddosev10 import XSDataAtom
        from XSDataCommon import XSDataDouble
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataInteger

        xsDataAtomicComposition1 = XSDataAtomicComposition()
        xsDataAtom1 = XSDataAtom()
        xsDataAtom1.setSymbol(XSDataString("S"))
        xsDataAtom1.setNumberOf(XSDataDouble(4))
        xsDataAtomicComposition1.addAtom(xsDataAtom1)

        xsDataAtom2 = XSDataAtom()
        xsDataAtom2.setSymbol(XSDataString("Se"))
        xsDataAtom2.setNumberOf(XSDataDouble(3))
        xsDataAtomicComposition1.addAtom(xsDataAtom2)

        xsDataAtomicComposition2 = XSDataAtomicComposition()
        xsDataAtom3 = XSDataAtom()
        xsDataAtom3.setSymbol(XSDataString("S"))
        xsDataAtom3.setNumberOf(XSDataDouble(1))
        xsDataAtomicComposition2.addAtom(xsDataAtom3)

        xsDataAtom4 = XSDataAtom()
        xsDataAtom4.setSymbol(XSDataString("Fe"))
        xsDataAtom4.setNumberOf(XSDataDouble(5))
        xsDataAtomicComposition2.addAtom(xsDataAtom4)

        from EDHandlerXSDataRaddosev10 import EDHandlerXSDataRaddosev10
        xsDataMergedAtomicComposition = EDHandlerXSDataRaddosev10().mergeAtomicComposition(xsDataAtomicComposition1,
                                                                                           xsDataAtomicComposition2)

        EDAssert.equal(3, len(xsDataMergedAtomicComposition.getAtom()))

        for atom in xsDataMergedAtomicComposition.getAtom():
            if(atom.getSymbol().getValue() == "S"):
                EDAssert.equal(5, atom.getNumberOf().getValue())
            if(atom.getSymbol().getValue() == "Se"):
                EDAssert.equal(3, atom.getNumberOf().getValue())
            if(atom.getSymbol().getValue() == "Fe"):
                EDAssert.equal(5, atom.getNumberOf().getValue())

        xsDataMergedAtomicComposition = EDHandlerXSDataRaddosev10().mergeAtomicComposition(XSDataAtomicComposition(),
                                                                                           xsDataAtomicComposition2)
        EDAssert.equal(2, len(xsDataMergedAtomicComposition.getAtom()))
        for atom in xsDataMergedAtomicComposition.getAtom():
            if(atom.getSymbol().getValue() == "S"):
                EDAssert.equal(1, atom.getNumberOf().getValue())
            if(atom.getSymbol().getValue() == "Fe"):
                EDAssert.equal(5, atom.getNumberOf().getValue())



    def process(self):
        self.addTestMethod(self.testGetXSDataRaddoseInput)
        self.addTestMethod(self.testMergeAtomicComposition)



if __name__ == '__main__':

    edTestCaseEDHandlerRaddosev10 = EDTestCaseEDHandlerRaddosev10("EDTestCaseEDHandlerRaddosev10")
    edTestCaseEDHandlerRaddosev10.execute()


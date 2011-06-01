#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Marie-Francoise Incardona (incardon@esrf.fr)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCasePluginUnit                import EDTestCasePluginUnit


class EDTestCasePluginUnitCCP4iv1_1(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlCCP4iv1_1", "EDPluginGroupInterface-v1.1", _edStringTestName)
        self.strDataPath = self.getPluginTestsDataHome()
        self.strXSDataGenerateTemplateFile = os.path.join(self.getPluginTestsDataHome(), "XSDataGenerateTemplate.xml")
        self.edObtainedInputFile = "XSDataInputCCP4i.xml"


    def testSetDataModelInput(self):
        from XSDataCCP4iv1_1 import XSDataInputCCP4i
        xsDataInputCCP4i = XSDataInputCCP4i()

        # Beam
        from XSDataCommon import XSDataFlux
        from XSDataCommon import XSDataSize
        from XSDataCommon import XSDataLength
        from XSDataCommon import XSDataFloat

        from XSDataMXv1 import XSDataBeam
        from XSDataMXv1 import XSDataExperimentalCondition

        xsExperimentalCondition = XSDataExperimentalCondition()

        xsBeam = XSDataBeam()
        xsBeam.setFlux(XSDataFlux(1e+12))
        xsBeam.setSize(XSDataSize(XSDataLength(0.1), XSDataLength(0.1)))
        xsBeam.setMinExposureTimePerImage(XSDataFloat(0.1))
        xsExperimentalCondition.setBeam(xsBeam)

        # Goniostat
        from XSDataCommon import XSDataSpeed
        from XSDataCommon import XSDataAngle

        from XSDataMXv1 import XSDataGoniostat

        xsDataGoniostat = XSDataGoniostat()
        xsDataGoniostat.setMaxOscillationSpeed(XSDataSpeed(0.2))
        xsDataGoniostat.setMinOscillationWidth(XSDataAngle(0.1))
        xsExperimentalCondition.setGoniostat(xsDataGoniostat)
        xsDataInputCCP4i.setExperimentalCondition(xsExperimentalCondition)

        # Sample
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataFloat
        from XSDataCommon import XSDataString

        from XSDataMXv1 import XSDataStructure
        from XSDataMXv1 import XSDataChain
        from XSDataMXv1 import XSDataAtom
        from XSDataMXv1 import XSDataLigand
        from XSDataMXv1 import XSDataSampleCrystalMM
        from XSDataMXv1 import XSDataChemicalCompositionMM
        from XSDataMXv1 import XSDataAtomicComposition
        from XSDataMXv1 import XSDataSolvent

        xsDataSampleCrystalMM = XSDataSampleCrystalMM()
        xsDataStructure = XSDataStructure()
        xsDataComposition = XSDataChemicalCompositionMM()

        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfCopies(XSDataFloat(2))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtom1 = XSDataAtom()
        xsDataAtom1.setSymbol(XSDataString("Se"))
        xsDataAtom1.setNumberOf(XSDataFloat(4))
        xsDataAtomicComposition.addAtom(xsDataAtom1)

        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)
        xsDataChain.setNumberOfMonomers(XSDataFloat(100))
        xsDataStructure.addChain(xsDataChain)

        xsDataChain2 = XSDataChain()
        xsDataChain2.setType(XSDataString("rna"))
        xsDataChain2.setNumberOfCopies(XSDataFloat(1))
        xsDataChain2.setNumberOfMonomers(XSDataFloat(60))
        xsDataStructure.addChain(xsDataChain2)

        xsDataLigand = XSDataLigand()
        xsDataLigand.setNumberOfCopies(XSDataFloat(2))
        xsDataLigand.setNumberOfLightAtoms(XSDataFloat(42))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtom2 = XSDataAtom()
        xsDataAtom2.setSymbol(XSDataString("Fe"))
        xsDataAtom2.setNumberOf(XSDataFloat(1))
        xsDataAtomicComposition.addAtom(xsDataAtom2)
        xsDataLigand.setHeavyAtoms(xsDataAtomicComposition)
        xsDataStructure.addLigand(xsDataLigand)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataFloat(0.25))

        xsDataSolvent = XSDataSolvent()
        xsDataAtomicComposition = XSDataAtomicComposition()

        xsDataAtom3 = XSDataAtom()
        xsDataAtom3.setSymbol(XSDataString("Na"))
        xsDataAtom3.setConcentration(XSDataFloat(1000))
        xsDataAtom4 = XSDataAtom()
        xsDataAtom4.setSymbol(XSDataString("Cl"))
        xsDataAtom4.setConcentration(XSDataFloat(1000))

        xsDataAtomicComposition.addAtom(xsDataAtom3)
        xsDataAtomicComposition.addAtom(xsDataAtom4)
        xsDataSolvent.setAtoms(xsDataAtomicComposition)

        xsDataComposition.setStructure(xsDataStructure)
        xsDataComposition.setSolvent(xsDataSolvent)
        xsDataSampleCrystalMM.setChemicalComposition(xsDataComposition)

        xsDataSampleCrystalMM.setSize(XSDataSize(XSDataLength(0.2), XSDataLength(0.2), XSDataLength(0.2)))
        xsDataSampleCrystalMM.setSusceptibility(XSDataFloat(1.5))
        xsDataSampleCrystalMM.setShape(XSDataFloat(2))

        xsDataInputCCP4i.setSample(xsDataSampleCrystalMM)

        from XSDataMXv1 import XSDataDiffractionPlan

        xsDataDiffractionPlan = XSDataDiffractionPlan()

        xsDataDiffractionPlan.setAimedCompleteness(XSDataFloat(95.5))
        xsDataDiffractionPlan.setAimedIOverSigmaAtHighestResolution(XSDataFloat(2.5))
        xsDataDiffractionPlan.setAimedMultiplicity(XSDataFloat(95.5))
        xsDataDiffractionPlan.setAimedResolution(XSDataFloat(3))
        xsDataDiffractionPlan.setComplexity(XSDataString("full"))
        xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString("P222"))
        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataFloat(10000))

        xsDataInputCCP4i.setDiffractionPlan(xsDataDiffractionPlan)

        from XSDataCommon import XSDataFile

        listInputDataFile = []
        xsDataFile = XSDataFile(XSDataString(self.strXSDataGenerateTemplateFile))
        listInputDataFile.append(xsDataFile)
        xsDataInputCCP4i.setDataFile(listInputDataFile)



    def process(self):
        self.addTestMethod(self.testSetDataModelInput)



if __name__ == '__main__':

    edTestCasePluginUnitCCP4iv1_1 = EDTestCasePluginUnitCCP4iv1_1("EDTestCasePluginUnitCCP4iv1_1")
    edTestCasePluginUnitCCP4iv1_1.execute()


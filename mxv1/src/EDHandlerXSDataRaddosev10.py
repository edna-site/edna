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

from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon        import XSDataDouble
from XSDataCommon        import XSDataString
from XSDataCommon        import XSDataTime
from XSDataCommon        import XSDataInteger

EDFactoryPluginStatic.loadModule("XSDataRaddosev10")
from XSDataRaddosev10    import XSDataAtomicComposition
from XSDataRaddosev10    import XSDataAtom
from XSDataRaddosev10    import XSDataRaddoseInput
from XSDataRaddosev10    import XSDataAtom
from XSDataRaddosev10    import XSDataAtomicComposition


class EDHandlerXSDataRaddosev10:


    def getXSDataRaddoseInput(self, _xsDataBeam, _xsDataSample, _inumOperators, _iNumberOfImages):



        xsDataRaddoseInput = XSDataRaddoseInput()

        # Beam        
        xsDataRaddoseInput.setBeamSize(_xsDataBeam.getSize())
        xsDataRaddoseInput.setBeamFlux(_xsDataBeam.getFlux())
        xsDataRaddoseInput.setBeamWavelength(_xsDataBeam.getWavelength())

        xsDataRaddoseInput.setBeamExposureTime(_xsDataBeam.getExposureTime())
        xsDataRaddoseInput.setNumberOfImages(XSDataInteger(_iNumberOfImages))
        xsDataRaddoseInput.setCrystalCell(_xsDataSample.getCrystal().getCell())

        xsDataRaddoseInput.setCrystalSize(_xsDataSample.getSize())

        xsDataComposition = _xsDataSample.getChemicalComposition()

        xsDataSolvent = xsDataComposition.getSolvent()
        if(xsDataSolvent is not None):
            xsDataRaddoseInput.setCrystalSATM(xsDataSolvent.getAtoms())

        xsDataStructure = xsDataComposition.getStructure()
        if(xsDataStructure is not None):
            xsDataChains = xsDataStructure.getChain()

            totalNRESInStructure = 0
            totalNDNAInStructure = 0
            totalNRNAInStructure = 0
            totalPATM = XSDataAtomicComposition()

            for chain in xsDataChains:
                # heavy atoms of each chain to be added in the PATM
                xsDataAtomicCompositionHeavyAtoms = chain.getHeavyAtoms()
                if (xsDataAtomicCompositionHeavyAtoms is not None):
                    iterator = 1
                    while iterator <= chain.getNumberOfCopies().getValue():
                        totalPATM = self.mergeAtomicComposition(totalPATM, xsDataAtomicCompositionHeavyAtoms)
                        iterator = iterator + 1

                type = chain.getType().getValue()
                numberOfMonomers = chain.getNumberOfMonomers().getValue() * chain.getNumberOfCopies().getValue()

                if (type == "protein"):
                    totalNRESInStructure = totalNRESInStructure + numberOfMonomers
                elif(type == "dna"):
                    totalNDNAInStructure = totalNDNAInStructure + numberOfMonomers
                elif(type == "rna"):
                    totalNRNAInStructure = totalNRNAInStructure + numberOfMonomers

            xsDataLigands = xsDataStructure.getLigand()
            for ligand in xsDataLigands:

                # Light atoms to be added to the NRES
                nres = ligand.getNumberOfLightAtoms().getValue() * ligand.getNumberOfCopies().getValue() / 7.85
                totalNRESInStructure = totalNRESInStructure + nres

                # Heavy atoms to be added to the PATM
                if (ligand.getHeavyAtoms() is not None):
                    iterator = 1
                    while iterator <= ligand.getNumberOfCopies().getValue():
                        totalPATM = self.mergeAtomicComposition(totalPATM, ligand.getHeavyAtoms())
                        iterator = iterator + 1

            if(totalNRESInStructure != 0):
                xsDataRaddoseInput.setCrystalNRES(XSDataInteger(int(round(totalNRESInStructure))))
            if(totalNDNAInStructure != 0):
                xsDataRaddoseInput.setCrystalNDNA(XSDataInteger(int(totalNDNAInStructure)))
            if(totalNRNAInStructure != 0):
                xsDataRaddoseInput.setCrystalNRNA(XSDataInteger(int(totalNRNAInStructure)))
            if(len(totalPATM.getAtom()) != 0):
                xsDataRaddoseInput.setCrystalPATM(totalPATM)

            xsDataNumberNumStructInAU = xsDataStructure.getNumberOfCopiesInAsymmetricUnit()
            xsDataNumberNumStructInUC = int(xsDataNumberNumStructInAU.getValue() * _inumOperators)
            xsDataRaddoseInput.setCrystalNMON(XSDataInteger(xsDataNumberNumStructInUC))

        return xsDataRaddoseInput


    def mergeAtomicComposition(self, _xsDataAtomicComposition1, _xsDataAtomicComposition2):

        EDFactoryPluginStatic.loadModule("XSDataRaddosev10")

        mergedAtomicComposition = XSDataAtomicComposition()
        dictionary = {}

        for atom in _xsDataAtomicComposition2.getAtom():
            dictionary[atom.getSymbol().getValue()] = atom.getNumberOf().getValue()

        for atom1 in _xsDataAtomicComposition1.getAtom():
            symbol = atom1.getSymbol().getValue()
            if (self.exists(symbol, _xsDataAtomicComposition2) == True):
                mergedAtom = XSDataAtom()
                mergedAtom.setNumberOf(XSDataDouble(atom1.getNumberOf().getValue() + dictionary[symbol]))
                mergedAtom.setSymbol(XSDataString(symbol))
                mergedAtomicComposition.addAtom(mergedAtom)
            else:
                mergedAtomicComposition.addAtom(atom1)

        for atom2 in _xsDataAtomicComposition2.getAtom():
            symbol = atom2.getSymbol().getValue()
            if (self.exists(symbol, _xsDataAtomicComposition1) == False):
                mergedAtomicComposition.addAtom(atom2)

        return mergedAtomicComposition


    def exists(self, _strSymbol, _xsDataAtomicComposition):
        bExists = False

        for atom in _xsDataAtomicComposition.getAtom():
            if (atom.getSymbol().getValue() == _strSymbol):
                bExists = True
                break

        return bExists




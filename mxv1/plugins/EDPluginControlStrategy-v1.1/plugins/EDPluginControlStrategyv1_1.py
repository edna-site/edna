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
import math

from EDVerbose import EDVerbose
from EDPluginControl                   import EDPluginControl
from EDMessage                         import EDMessage
from EDConfiguration                   import EDConfiguration
from EDUtilsSymmetry                   import EDUtilsSymmetry

from XSDataCommon                      import XSDataString
from XSDataCommon                      import XSDataFloat

from XSDataMXv1                        import XSDataInputStrategy
from XSDataMXv1                        import XSDataSampleCrystalMM
from XSDataMXv1                        import XSDataAtom
from XSDataMXv1                        import XSDataAtomicComposition
from XSDataMXv1                        import XSDataChain
from XSDataMXv1                        import XSDataStructure
from XSDataMXv1                        import XSDataSolvent
from XSDataMXv1                        import XSDataChemicalCompositionMM


class EDPluginControlStrategyv1_1(EDPluginControl):
    """
    The Plugin that controls the strategy step
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputStrategy)

        self.__strPluginRaddoseName = "EDPluginRaddosev10"
        self.__edPluginRaddose = None
        self.__edHandlerXSDataRaddose = None

        self.__strPluginBestName = "EDPluginBestv1_1"
        self.__edPluginBest = None
        self.__edHandlerXSDataBest = None

        self.__strCONF_SYMOP_HOME = "symopHome"
        # Default value for the location of the symop table
        self.__strSymopHome = "/opt/pxsoft/ccp4-6.0.2/lib/data"

        self.__xsDataSampleCopy = None

        # For default chemical composition
        self.__fAverageAminoAcidVolume = 135.49
        self.__fAverageCrystalSolventContent = 0.47
        self.__fAverageSulfurContentPerAminoacid = 0.05
        self.__fAverageSulfurConcentration = 314


    def setSymopHome(self, _strSymopHome):
        self.__strSymopHome = _strSymopHome


    def getSymopHome(self):
        return self.__strSymopHome


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.preProcess...")
        self.__edPluginRaddose = None

        xsDataSampleCrystalMM = self.getDataInput().getSample()

        if(xsDataSampleCrystalMM is None):
            self.__xsDataSampleCopy = XSDataSampleCrystalMM()

        else:
            strXmlStringDataSample = xsDataSampleCrystalMM.marshal()
            self.__xsDataSampleCopy = XSDataSampleCrystalMM.parseString(strXmlStringDataSample)

        xsDataCrystal = self.getDataInput().getCrystalRefined()
        if(xsDataCrystal is not None):
            self.__xsDataSampleCopy.setCrystal(xsDataCrystal)

        # Raddose is enabled only if the beam flux is set
        if(self.getDataInput().getExperimentalCondition().getBeam().getFlux() is None):
            pyStrWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_1.preProcess', self.__strPluginRaddoseName, "Beam Flux not set")
            EDVerbose.warning(pyStrWarningMessage)
            self.addWarningMessage(pyStrWarningMessage)

        else:
            self.__edPluginRaddose = self.loadPlugin(self.__strPluginRaddoseName)

            if (self.__edPluginRaddose is not None):
                EDVerbose.DEBUG("EDPluginControlStrategyv1_1.preProcess: " + self.__strPluginRaddoseName + " Found... setting Data Input")

                strFileSymop = os.path.join(self.getSymopHome(), "symop.lib")

                xsDataStringSpaceGroup = self.getDataInput().getDiffractionPlan().getForcedSpaceGroup()
                # Space Group has been forced
                # Prepare chemical composition calculation with the forced Space Group (Space Group Name)
                strNumOperators = None
                strSpaceGroup = None
                if(xsDataStringSpaceGroup is not None):
                    strSpaceGroup = xsDataStringSpaceGroup.getValue().upper()
                    EDVerbose.DEBUG("EDPluginControlStrategyv1_1.preProcess: Forced Space Group Found: " + strSpaceGroup)
                    try:
                        strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroup, strFileSymop)
                    except Exception, detail:
                        pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_1.preProcess', "Problem to calculate Number of symmetry operators", detail)
                        EDVerbose.error(pyStrErrorMessage)
                        self.addErrorMessage(pyStrErrorMessage)
                        self.setFailure()
                # Space Group has NOT been forced
                else:
                    xsDataStringSpaceGroup = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getName()
                    if (xsDataStringSpaceGroup is not None):
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group Name)
                        strSpaceGroupName = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getName().getValue()
                        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.preProcess: Space Group IT Name found by indexing: " + strSpaceGroupName)
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroupName, strFileSymop)
                        except Exception, detail:
                            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_1.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(pyStrErrorMessage)
                            self.addErrorMessage(pyStrErrorMessage)
                            self.setFailure()
                    else:
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group IT number)
                        iSpaceGroupITNumber = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getITNumber().getValue()
                        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.preProcess: Space Group IT Number Found by indexing: " + str(iSpaceGroupITNumber))
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupITNumber(str(iSpaceGroupITNumber), strFileSymop)
                        except Exception, detail:
                            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_1.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(pyStrErrorMessage)
                            self.addErrorMessage(pyStrErrorMessage)
                            self.setFailure()

                if(strNumOperators is not None):
                    iNumOperators = int(strNumOperators)
                else:
                    pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_1.preProcess', "No symmetry operators found for Space Group: ", strSpaceGroup)
                    EDVerbose.error(pyStrErrorMessage)
                    self.addErrorMessage(pyStrErrorMessage)
                    self.setFailure()

                if not self.isFailure():
                    xsDataChemicalComposition = self.__xsDataSampleCopy.getChemicalComposition()

                    if(xsDataChemicalComposition is None):
                        # create a default chemical composition and assign it to the sample
                        xsDataDefaultChemicalComposition = self.getDefaultChemicalComposition(self.__xsDataSampleCopy, iNumOperators)
                        self.__xsDataSampleCopy.setChemicalComposition(xsDataDefaultChemicalComposition)
                    else:
                        # Check for Sulfur atoms, if none, add native sulfur atoms
                        xsDataUpdatedChemicalComposition = self.updateChemicalComposition(xsDataChemicalComposition)
                        self.__xsDataSampleCopy.setChemicalComposition(xsDataUpdatedChemicalComposition)

                    # create Data Input for Raddose
                    from EDHandlerXSDataRaddosev10 import EDHandlerXSDataRaddosev10
                    self.__edHandlerXSDataRaddose = EDHandlerXSDataRaddosev10()
                    xsDataBeam = self.getDataInput().getExperimentalCondition().getBeam()

                    xsDataRaddoseInput = None

                    try:
                        xsDataRaddoseInput = self.__edHandlerXSDataRaddose.getXSDataRaddoseInput(xsDataBeam, self.__xsDataSampleCopy, iNumOperators)

                    except Exception, detail:
                        pyStrWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_1.preProcess', self.__strPluginRaddoseName, self.__edHandlerXSDataRaddose.getClassName() + ": " + detail)
                        EDVerbose.warning(pyStrWarningMessage)
                        self.addWarningMessage(pyStrWarningMessage)

                    if(xsDataRaddoseInput is not None):
                        self.__edPluginRaddose.setDataInput(xsDataRaddoseInput)
                        self.__edPluginRaddose.setBaseDirectory(self.getWorkingDirectory())
                        self.__edPluginRaddose.setBaseName(self.__strPluginRaddoseName)

                        # More checks?
    #                    try:
    #                        self.__edPluginRaddose.setDataInput( xsDataRaddoseInput )
    #                        self.__edPluginRaddose.setBaseDirectory( self.getWorkingDirectory() )
    #                        self.__edPluginRaddose.setBaseName( self.__strPluginRaddoseName )
    #                        
    #                    except Exception, detail:
    #                        pyStrWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_1.preProcess', self.__strPluginRaddoseName, str( detail ) )
    #                        EDVerbose.warning( pyStrWarningMessage )
    #                        self.addWarningMessage( pyStrWarningMessage )

            else:
                pyStrErrorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlStrategyv1_1.preProcess', self.__strPluginRaddoseName)
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                self.setFailure()

        if not self.isFailure():
            self.__edPluginBest = self.loadPlugin(self.__strPluginBestName)
            if (self.__edPluginBest is None):
                pyStrErrorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlStrategyv1_1.preProcess', self.__strPluginBestName)
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            else:
                self.__edPluginBest.setBaseDirectory(self.getWorkingDirectory())
                self.__edPluginBest.setBaseName(self.__strPluginBestName)


    def configure(self):
        """
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.configure")
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            pyStrWarningMessage = EDMessage.WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 % ('EDPluginControlStrategyv1_1.configure', self.getPluginName())
            EDVerbose.warning(pyStrWarningMessage)
            self.addWarningMessage(pyStrWarningMessage)
        else:
            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, self.__strCONF_SYMOP_HOME)
            if(strSymopHome == None):
                pyStrWarningMessage = EDMessage.WARNING_NO_PARAM_CONFIGURATION_ITEM_FOUND_03 % ('EDPluginControlStrategyv1_1.configure', self.__strCONF_SYMOP_HOME, self.getPluginName())
                EDVerbose.warning(pyStrWarningMessage)
                self.addWarningMessage(pyStrWarningMessage)
            else:
                strSymopHomeNorm = os.path.normpath(strSymopHome)
                self.setSymopHome(strSymopHomeNorm)


    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.process...")

        # In case Beam Flux has not been set, The plugin Raddose has not been created, so it could be None
        # and it won't be launched in this case
        if(self.__edPluginRaddose is not None):
            self.connectProcess(self.__edPluginRaddose.executeSynchronous)
            self.__edPluginRaddose.connectSUCCESS(self.doRaddoseToBestTransition)
            self.__edPluginRaddose.connectFAILURE(self.doFailureActionRaddose)
        else:
            # The plugin Best should not be None as this has been checked in the preProcess method... Double check it anyway
            if(self.__edPluginBest is not None):
                self.connectProcess(self.executeBest)

        # Launches Best anyway whether Raddose has been launched or not
        # The plugin Best should not be None as this has been checked in the preProcess method... Double check it anyway
        if(self.__edPluginBest is not None):
            self.__edPluginBest.connectSUCCESS(self.doSuccessActionBest)
            self.__edPluginBest.connectFAILURE(self.doFailureActionBest)


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.postProcess...")

        xsDataResultBest = self.__edPluginBest.getDataOutput()
        xsDataResultStrategy = None

        if(xsDataResultBest is not None):
            xsDataResultStrategy = self.__edHandlerXSDataBest.getXSDataResultStrategy(xsDataResultBest, self.getDataInput().getExperimentalCondition(), self.__xsDataSampleCopy)

        self.setDataOutput(xsDataResultStrategy)


    def doRaddoseToBestTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.doRaddoseToBestTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlStrategyv1_1.doRaddoseToBestTransition")

        xsDataRaddoseOutput = self.__edPluginRaddose.getDataOutput()

        # update the strategy data with the data coming from Raddose
        self.__xsDataSampleCopy.setAbsorbedDoseRate(xsDataRaddoseOutput.getAbsorbedDoseRate())

        # Call the Best Translator layer
        from EDHandlerXSDataBestv1_1    import EDHandlerXSDataBestv1_1
        self.__edHandlerXSDataBest = EDHandlerXSDataBestv1_1()

        xsDataInputBest = self.__edHandlerXSDataBest.getXSDataInputBest(self.getDataInput().getExperimentalCondition().getBeam(),
                                                                             self.__xsDataSampleCopy,
                                                                             self.getDataInput().getExperimentalCondition().getDetector(),
                                                                             self.getDataInput().getExperimentalCondition().getGoniostat(),
                                                                             self.getDataInput().getDiffractionPlan(),
                                                                             self.getDataInput().getBestFileContentDat(),
                                                                             self.getDataInput().getBestFileContentPar(),
                                                                             self.getDataInput().getBestFileContentHKL())

        self.__edPluginBest.setDataInput(xsDataInputBest)
        self.__edPluginBest.executeSynchronous()


    def doFailureActionRaddose(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.doFailureActionRaddose")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlStrategyv1_1.doFailureActionRaddose")
        pyStrWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_1.doFailureActionRaddose', self.__strPluginRaddoseName, "Raddose failure")
        EDVerbose.warning(pyStrWarningMessage)
        self.addWarningMessage(pyStrWarningMessage)
        self.executeBest(self)


    def executeBest(self, _edPlugin):
        # Call the Best Translator layer

        from EDHandlerXSDataBestv1_1    import EDHandlerXSDataBestv1_1
        self.__edHandlerXSDataBest = EDHandlerXSDataBestv1_1()
        xsDataInputBest = self.__edHandlerXSDataBest.getXSDataInputBest(self.getDataInput().getExperimentalCondition().getBeam(),
                                                                         self.__xsDataSampleCopy,
                                                                         self.getDataInput().getExperimentalCondition().getDetector(),
                                                                         self.getDataInput().getExperimentalCondition().getGoniostat(),
                                                                         self.getDataInput().getDiffractionPlan(),
                                                                         self.getDataInput().getBestFileContentDat(),
                                                                         self.getDataInput().getBestFileContentPar(),
                                                                         self.getDataInput().getBestFileContentHKL())
        self.__edPluginBest.setDataInput(xsDataInputBest)
        self.__edPluginBest.executeSynchronous()


    def doSuccessActionBest(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.doSuccessActionBest")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlStrategyv1_1.doSuccessActionBest")


    def doFailureActionBest(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.doFailureActionBest")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlStrategyv1_1.doFailureActionBest")


    def getDefaultChemicalComposition(self, _xsDataSample, _inumOperators):
        """
        """
        xsDataCell = _xsDataSample.getCrystal().getCell()
        a = xsDataCell.getLength_a().getValue()
        b = xsDataCell.getLength_b().getValue()
        c = xsDataCell.getLength_c().getValue()
        alpha = math.radians(xsDataCell.getAngle_alpha().getValue())
        beta = math.radians(xsDataCell.getAngle_beta().getValue())
        gamma = math.radians(xsDataCell.getAngle_gamma().getValue())

        fUnitCellVolume = a * b * c * (math.sqrt(1 - math.cos(alpha) * math.cos(alpha) - math.cos(beta) * math.cos(beta) - math.cos(gamma) * math.cos(gamma) + 2 * math.cos(alpha) * math.cos(beta) * math.cos(gamma)))
        fPolymerVolume = fUnitCellVolume * (1 - self.__fAverageCrystalSolventContent)
        fNumberOfMonomersPerUnitCell = fPolymerVolume / self.__fAverageAminoAcidVolume
        fNumberOfMonomersPerAsymmetricUnit = fNumberOfMonomersPerUnitCell / _inumOperators
        iNumberOfSulfurAtom = int(round(fNumberOfMonomersPerAsymmetricUnit * self.__fAverageSulfurContentPerAminoacid))

        xsDataAtom = XSDataAtom()
        xsDataAtom.setSymbol(XSDataString("S"))
        xsDataAtom.setNumberOf(XSDataFloat(iNumberOfSulfurAtom))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomicComposition.addAtom(xsDataAtom)

        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfMonomers(XSDataFloat(round(fNumberOfMonomersPerAsymmetricUnit)))
        xsDataChain.setNumberOfCopies(XSDataFloat(1))
        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)

        xsDataStructure = XSDataStructure()
        xsDataStructure.addChain(xsDataChain)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataFloat(1))

        xsDataAtomSolvent = XSDataAtom()
        xsDataAtomSolvent.setSymbol(XSDataString("S"))
        xsDataAtomSolvent.setConcentration(XSDataFloat(self.__fAverageSulfurConcentration))
        xsDataAtomicCompositionSolvent = XSDataAtomicComposition()
        xsDataAtomicCompositionSolvent.addAtom(xsDataAtomSolvent)
        xsDataSolvent = XSDataSolvent()
        xsDataSolvent.setAtoms(xsDataAtomicCompositionSolvent)

        xsDataChemicalCompositionMM = XSDataChemicalCompositionMM()
        xsDataChemicalCompositionMM.setSolvent(xsDataSolvent)
        xsDataChemicalCompositionMM.setStructure(xsDataStructure)

        return xsDataChemicalCompositionMM

    def updateChemicalComposition(self, _xsDataChemicalComposition):
        """
        """
        xsDataChemicalComposition = _xsDataChemicalComposition

        for chain in xsDataChemicalComposition.getStructure().getChain():
            if(chain.getType().getValue() == "protein"):
                bSulfurExists = False
                xsDataAtomicCompositionHeavyAtoms = chain.getHeavyAtoms()
                if(xsDataAtomicCompositionHeavyAtoms is None):
                    xsDataAtomicCompositionHeavyAtoms = XSDataAtomicComposition()
                else:
                    for heavyAtom in xsDataAtomicCompositionHeavyAtoms.getAtom():
                        if(heavyAtom.getSymbol().getValue() == "S" or heavyAtom.getSymbol().getValue() == "s"):
                            bSulfurExists = True

                # all protein chains should contain sulfur atom as a percentage of the number
                # of amino acids. Add them if the user did not input them.
                if(bSulfurExists == False):
                    iNumberOfSulfurAtom = int(round(chain.getNumberOfMonomers().getValue() * 0.05))
                    xsDataSulfurAtom = XSDataAtom()
                    xsDataSulfurAtom.setSymbol(XSDataString("S"))
                    xsDataSulfurAtom.setNumberOf(XSDataFloat(iNumberOfSulfurAtom))
                    xsDataAtomicCompositionHeavyAtoms.addAtom(xsDataSulfurAtom)
                    chain.setHeavyAtoms(xsDataAtomicCompositionHeavyAtoms)

        return xsDataChemicalComposition


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_1.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of Strategy:")
        self.addErrorWarningMessagesToExecutiveSummary()

        xsDataResultStrategy = self.getDataOutput()

        if (self.__edPluginRaddose is not None):
            if (self.__edPluginRaddose.getDataOutput() is not None):
                self.appendExecutiveSummary(self.__edPluginRaddose, "Raddose : ")
                self.addExecutiveSummaryLine("")
                self.addExecutiveSummaryLine("Calculations assuming polymer crystal with:")
                self.addExecutiveSummaryLine("------------------------------------------")
                self.addExecutiveSummaryLine("")

                xsDataStructure = xsDataResultStrategy.getCollectionPlan()[0].getCollectionStrategy().getSample().getChemicalComposition().getStructure()

                self.addExecutiveSummaryLine("Number of structure copies in asymmetric unit: %.2f" % xsDataStructure.getNumberOfCopiesInAsymmetricUnit().getValue())
                self.addExecutiveSummaryLine("")

                chains = xsDataStructure.getChain()
                self.addExecutiveSummaryLine("Chains:")
                for chain in chains:
                    strChainType = chain.getType().getValue()
                    self.addExecutiveSummaryLine("    Type                           : %s" % strChainType)
                    if(strChainType == "protein"):
                        self.addExecutiveSummaryLine("    Number of residues             : %.2f" % chain.getNumberOfMonomers().getValue())
                    elif(strChainType == "dna" or strChainType == "rna"):
                        self.addExecutiveSummaryLine("    Number of nucleotides          : %.2f" % chain.getNumberOfMonomers().getValue())
                    strHeavyAtomsChain = "    Number of heavy atoms          :"
                    if(chain.getHeavyAtoms() is not None):
                        heavyAtomsChain = chain.getHeavyAtoms().getAtom()
                        for heavyAtomChain in heavyAtomsChain:
                            strHeavyAtomsChain = strHeavyAtomsChain + " %s=%d" % (heavyAtomChain.getSymbol().getValue(), heavyAtomChain.getNumberOf().getValue())
                    else:
                        strHeavyAtomsChain = strHeavyAtomsChain + " No heavy atoms"
                    self.addExecutiveSummaryLine(strHeavyAtomsChain)

                    self.addExecutiveSummaryLine("    Number of copies in structure  : %.2f" % chain.getNumberOfCopies().getValue())
                    self.addExecutiveSummaryLine("")

                ligands = xsDataStructure.getLigand()
                if(len(ligands) != 0):
                    self.addExecutiveSummaryLine("Ligands:")

                for ligand in ligands:
                    self.addExecutiveSummaryLine("    Number of light atoms          : %.2f" % ligand.getNumberOfLightAtoms().getValue())
                    strHeavyAtomsLigand = "    Number of heavy atoms          :"
                    if(ligand.getHeavyAtoms() is not None):
                        heavyAtomsLigand = ligand.getHeavyAtoms().getAtom()
                        for heavyAtomLigand in heavyAtomsLigand:
                            strHeavyAtomsLigand = strHeavyAtomsLigand + " %s=%d" % (heavyAtomLigand.getSymbol().getValue(), heavyAtomLigand.getNumberOf().getValue())
                    else:
                        strHeavyAtomsChain = strHeavyAtomsChain + " No heavy atoms"
                    self.addExecutiveSummaryLine(strHeavyAtomsLigand)
                    self.addExecutiveSummaryLine("    Number of copies in structure  : %.2f" % chain.getNumberOfCopies().getValue())
                    self.addExecutiveSummaryLine("")


        if (self.__edPluginBest is not None):
            if (self.__edPluginBest.getDataOutput() is not None):
                self.appendExecutiveSummary(self.__edPluginBest, "Best : ")
                self.addExecutiveSummaryLine("")


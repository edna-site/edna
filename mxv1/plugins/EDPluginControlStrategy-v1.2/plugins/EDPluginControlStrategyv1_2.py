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

from EDVerbose                         import EDVerbose

from EDPluginControl                   import EDPluginControl
from EDMessage                         import EDMessage
from EDConfiguration                   import EDConfiguration
from EDUtilsSymmetry                   import EDUtilsSymmetry

from XSDataCommon                      import XSDataString
from XSDataCommon                      import XSDataDouble

from XSDataMXv1                        import XSDataInputStrategy
from XSDataMXv1                        import XSDataResultStrategy
from XSDataMXv1                        import XSDataSampleCrystalMM
from XSDataMXv1                        import XSDataAtom
from XSDataMXv1                        import XSDataAtomicComposition
from XSDataMXv1                        import XSDataChain
from XSDataMXv1                        import XSDataStructure
from XSDataMXv1                        import XSDataSolvent
from XSDataMXv1                        import XSDataChemicalCompositionMM


class EDPluginControlStrategyv1_2(EDPluginControl):
    """
    The Plugin that controls the strategy step
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputStrategy)

        self.__strPluginRaddoseName = "EDPluginRaddosev10"
        self.__edPluginRaddose = None
        self.__edHandlerXSDataRaddose = None

        self.__strPluginBestName = "EDPluginBestv1_2"
        self.__edPluginBest = None
        self.__edHandlerXSDataBest = None

        self.__strCONF_SYMOP_HOME = "symopHome"
        # Default value for the location of the symop table
        self.__strSymopHome = None

        self.__xsDataSampleCopy = None

        # For default chemical composition
        self.__fAverageAminoAcidVolume = 135.49
        self.__fAverageCrystalSolventContent = 0.47
        self.__fAverageSulfurContentPerAminoacid = 0.05
        self.__fAverageSulfurConcentration = 314

        # This varaible determines if Raddose should be executed or not
        self.__bEstimateRadiationDamage = None


    def setSymopHome(self, _strSymopHome):
        self.__strSymopHome = _strSymopHome


    def getSymopHome(self):
        return self.__strSymopHome


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.preProcess...")
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

        # Load the Best plugin
        self.__edPluginBest = self.loadPlugin(self.__strPluginBestName)
        self.__edPluginBest.setBaseDirectory(self.getWorkingDirectory())
        self.__edPluginBest.setBaseName(self.__strPluginBestName)

        # Check if radiation damage estimation is required or not in the diffraction plan
        xsDataDiffractionPlan = self.getDataInput().getDiffractionPlan()
        if xsDataDiffractionPlan is not None:
            if xsDataDiffractionPlan.getEstimateRadiationDamage():
                if xsDataDiffractionPlan.getEstimateRadiationDamage().getValue():
                    # Yes, is requested
                    self.__bEstimateRadiationDamage = True
                else:
                    # No, is explicitly not requested
                    self.__bEstimateRadiationDamage = False
            elif xsDataDiffractionPlan.getStrategyOption() is not None:
                if xsDataDiffractionPlan.getStrategyOption().getValue().find("-DamPar") != -1:
                    # The "-DamPar" option requires estimation of radiation damage
                    self.__bEstimateRadiationDamage = True

        # Check if we know what to do with radiation damage
        if self.__bEstimateRadiationDamage is None:
            # "Force" the estimation of radiation damage if the flux is present
            if self.getDataInput().getExperimentalCondition().getBeam().getFlux() is None:
                strWarningMessage = "EDPluginControlStrategyv1_2: Missing flux input - cannot estimate radiation damage."
                EDVerbose.WARNING(strWarningMessage)
                self.addWarningMessage(strWarningMessage)
                self.__bEstimateRadiationDamage = False
            else:
                self.__bEstimateRadiationDamage = True


        if self.__bEstimateRadiationDamage:
            if self.getDataInput().getExperimentalCondition().getBeam().getFlux() is None:
                strErrorMessage = "EDPluginControlStrategyv1_2: Missing flux input. Cannot estimate radiation damage"
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()

        if not self.isFailure():

            self.__edPluginRaddose = self.loadPlugin(self.__strPluginRaddoseName)

            if (self.__edPluginRaddose is not None):
                EDVerbose.DEBUG("EDPluginControlStrategyv1_2.preProcess: " + self.__strPluginRaddoseName + " Found... setting Data Input")

                strFileSymop = os.path.join(self.getSymopHome(), "symop.lib")

                xsDataStringSpaceGroup = self.getDataInput().getDiffractionPlan().getForcedSpaceGroup()
                # Space Group has been forced
                # Prepare chemical composition calculation with the forced Space Group (Space Group Name)
                if(xsDataStringSpaceGroup is not None):
                    strSpaceGroup = xsDataStringSpaceGroup.getValue().upper()
                    EDVerbose.DEBUG("EDPluginControlStrategyv1_2.preProcess: Forced Space Group Found: " + strSpaceGroup)
                    try:
                        strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroup, strFileSymop)
                    except Exception, detail:
                        strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_2.preProcess', "Problem to calculate Number of symmetry operators", detail)
                        EDVerbose.error(strErrorMessage)
                        self.addErrorMessage(strErrorMessage)
                        raise RuntimeError, strErrorMessage
                # Space Group has NOT been forced
                else:
                    xsDataStringSpaceGroup = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getName()
                    if (xsDataStringSpaceGroup is not None):
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group Name)
                        strSpaceGroupName = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getName().getValue()
                        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.preProcess: Space Group IT Name found by indexing: " + strSpaceGroupName)
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroupName, strFileSymop)
                        except Exception, detail:
                            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_2.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(strErrorMessage)
                            self.addErrorMessage(strErrorMessage)
                            raise RuntimeError, strErrorMessage
                    else:
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group IT number)
                        iSpaceGroupITNumber = self.__xsDataSampleCopy.getCrystal().getSpaceGroup().getITNumber().getValue()
                        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.preProcess: Space Group IT Number Found by indexing: %d" % iSpaceGroupITNumber)
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupITNumber(str(iSpaceGroupITNumber), strFileSymop)
                        except Exception, detail:
                            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_2.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(strErrorMessage)
                            self.addErrorMessage(strErrorMessage)
                            raise RuntimeError, strErrorMessage

                if (strNumOperators is not None):
                    iNumOperators = int(strNumOperators)
                else:
                    strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlStrategyv1_2.preProcess', "No symmetry operators found for Space Group: ", strNumOperators)
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    raise RuntimeError, strErrorMessage

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

                xsDataRaddoseInput = self.__edHandlerXSDataRaddose.getXSDataRaddoseInput(xsDataBeam, self.__xsDataSampleCopy, iNumOperators)
                if xsDataRaddoseInput is not None:
                    self.__edPluginRaddose.setDataInput(xsDataRaddoseInput)
                    self.__edPluginRaddose.setBaseDirectory(self.getWorkingDirectory())
                    self.__edPluginRaddose.setBaseName(self.__strPluginRaddoseName)



    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.configure")
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            strWarningMessage = EDMessage.WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 % ('EDPluginControlStrategyv1_2.configure', self.getPluginName())
            EDVerbose.warning(strWarningMessage)
            self.addWarningMessage(strWarningMessage)
        else:
            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, self.__strCONF_SYMOP_HOME)
            if(strSymopHome == None):
                strWarningMessage = EDMessage.WARNING_NO_PARAM_CONFIGURATION_ITEM_FOUND_03 % ('EDPluginControlStrategyv1_2.configure', self.__strCONF_SYMOP_HOME, self.getPluginName())
                EDVerbose.warning(strWarningMessage)
                self.addWarningMessage(strWarningMessage)
            else:
                self.setSymopHome(strSymopHome)


    def process(self, _edObject=None):
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.process...")
        self.__edPluginBest.connectSUCCESS(self.doSuccessActionBest)
        self.__edPluginBest.connectFAILURE(self.doFailureActionBest)
        if self.__bEstimateRadiationDamage:
            self.__edPluginRaddose.connectSUCCESS(self.doRaddoseToBestTransition)
            self.__edPluginRaddose.connectFAILURE(self.doFailureActionRaddose)
            self.__edPluginRaddose.executeSynchronous()
        else:
            self.executeBest()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.postProcess...")

        xsDataResultBest = self.__edPluginBest.getDataOutput()
        # TODO
        # Temporary! Otherwise fails Model from -bonly is different
        xsDataResultStrategy = None
        if(xsDataResultBest is not None and self.getDataInput().getDiffractionPlan().getStrategyOption() is not None):
            if (self.getDataInput().getDiffractionPlan().getStrategyOption().getValue() != "-Bonly"):
                xsDataResultStrategy = self.__edHandlerXSDataBest.getXSDataResultStrategy(xsDataResultBest, self.getDataInput().getExperimentalCondition(), self.__xsDataSampleCopy)
        else:
            xsDataResultStrategy = self.__edHandlerXSDataBest.getXSDataResultStrategy(xsDataResultBest, self.getDataInput().getExperimentalCondition(), self.__xsDataSampleCopy)

        self.setDataOutput(xsDataResultStrategy)
        self.generateStrategyShortSummary(xsDataResultStrategy)

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.finallyProcess")
        if not self.hasDataOutput():
            self.setDataOutput(XSDataResultStrategy())


    def doRaddoseToBestTransition(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.doRaddoseToBestTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlStrategyv1_2.doRaddoseToBestTransition")

        xsDataRaddoseOutput = self.__edPluginRaddose.getDataOutput()

        # update the strategy data with the data coming from Raddose
        self.__xsDataSampleCopy.setAbsorbedDoseRate(xsDataRaddoseOutput.getAbsorbedDoseRate())

        # Call the Best Translator layer
        from EDHandlerXSDataBestv1_2    import EDHandlerXSDataBestv1_2
        self.__edHandlerXSDataBest = EDHandlerXSDataBestv1_2()

        xsDataInputStrategyCopy = XSDataInputStrategy.parseString(self.getDataInput().marshal())
        xsDataInputStrategyCopy.setSample(self.__xsDataSampleCopy)

        xsDataInputBest = self.__edHandlerXSDataBest.getXSDataInputBest(xsDataInputStrategyCopy)

        self.__edPluginBest.setDataInput(xsDataInputBest)
        self.__edPluginBest.executeSynchronous()


    def doFailureActionRaddose(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.doFailureActionRaddose")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlStrategyv1_2.doFailureActionRaddose")
        strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_2.doFailureActionRaddose', self.__strPluginRaddoseName, "Raddose failure")
        EDVerbose.warning(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        self.executeBest(self)


    def executeBest(self, _edPlugin=None):
        # Call the Best Translator layer

        from EDHandlerXSDataBestv1_2    import EDHandlerXSDataBestv1_2
        self.__edHandlerXSDataBest = EDHandlerXSDataBestv1_2()
        xsDataInputStrategyCopy = XSDataInputStrategy.parseString(self.getDataInput().marshal())
        xsDataInputStrategyCopy.setSample(self.__xsDataSampleCopy)
        xsDataInputBest = self.__edHandlerXSDataBest.getXSDataInputBest(xsDataInputStrategyCopy)
        self.__edPluginBest.setDataInput(xsDataInputBest)
        self.__edPluginBest.executeSynchronous()


    def doSuccessActionBest(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.doSuccessActionBest")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlStrategyv1_2.doSuccessActionBest")


    def doFailureActionBest(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.doFailureActionBest")
        self.retrieveFailureMessages(_edPlugin, "BEST failure:")
        self.generateExecutiveSummary(self)
        self.setFailure()


    def getDefaultChemicalComposition(self, _xsDataSample, _inumOperators):
        xsDataCell = _xsDataSample.getCrystal().getCell()
        a = xsDataCell.getLength_a().getValue()
        b = xsDataCell.getLength_b().getValue()
        c = xsDataCell.getLength_c().getValue()
        alpha = math.radians(xsDataCell.getAngle_alpha().getValue())
        beta = math.radians(xsDataCell.getAngle_beta().getValue())
        gamma = math.radians(xsDataCell.getAngle_gamma().getValue())

        fUnitCellVolume = a * b * c * (math.sqrt(1 - math.cos(alpha) * math.cos(alpha) - \
                                                 math.cos(beta) * math.cos(beta) - \
                                                 math.cos(gamma) * math.cos(gamma) + \
                                                 2 * math.cos(alpha) * math.cos(beta) * math.cos(gamma)))
        fPolymerVolume = fUnitCellVolume * (1 - self.__fAverageCrystalSolventContent)
        fNumberOfMonomersPerUnitCell = fPolymerVolume / self.__fAverageAminoAcidVolume
        fNumberOfMonomersPerAsymmetricUnit = fNumberOfMonomersPerUnitCell / _inumOperators
        iNumberOfSulfurAtom = int(round(fNumberOfMonomersPerAsymmetricUnit * self.__fAverageSulfurContentPerAminoacid))

        xsDataAtom = XSDataAtom()
        xsDataAtom.setSymbol(XSDataString("S"))
        xsDataAtom.setNumberOf(XSDataDouble(iNumberOfSulfurAtom))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomicComposition.addAtom(xsDataAtom)

        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfMonomers(XSDataDouble(round(fNumberOfMonomersPerAsymmetricUnit)))
        xsDataChain.setNumberOfCopies(XSDataDouble(1))
        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)

        xsDataStructure = XSDataStructure()
        xsDataStructure.addChain(xsDataChain)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataDouble(1))

        xsDataAtomSolvent = XSDataAtom()
        xsDataAtomSolvent.setSymbol(XSDataString("S"))
        xsDataAtomSolvent.setConcentration(XSDataDouble(self.__fAverageSulfurConcentration))
        xsDataAtomicCompositionSolvent = XSDataAtomicComposition()
        xsDataAtomicCompositionSolvent.addAtom(xsDataAtomSolvent)
        xsDataSolvent = XSDataSolvent()
        xsDataSolvent.setAtoms(xsDataAtomicCompositionSolvent)

        xsDataChemicalCompositionMM = XSDataChemicalCompositionMM()
        xsDataChemicalCompositionMM.setSolvent(xsDataSolvent)
        xsDataChemicalCompositionMM.setStructure(xsDataStructure)

        return xsDataChemicalCompositionMM

    def updateChemicalComposition(self, _xsDataChemicalComposition):
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
                    xsDataSulfurAtom.setNumberOf(XSDataDouble(iNumberOfSulfurAtom))
                    xsDataAtomicCompositionHeavyAtoms.addAtom(xsDataSulfurAtom)
                    chain.setHeavyAtoms(xsDataAtomicCompositionHeavyAtoms)

        return xsDataChemicalComposition


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlStrategyv1_2.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of Strategy:")
        self.addErrorWarningMessagesToExecutiveSummary()

        xsDataResultStrategy = self.getDataOutput()

        if (self.__edPluginRaddose is not None):
            if (self.__edPluginRaddose.getDataOutput() is not None):

                self.addExecutiveSummaryLine("")
                self.appendExecutiveSummary(self.__edPluginRaddose, "Raddose : ")

            if (xsDataResultStrategy is not None):
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


    def generateStrategyShortSummary(self, _xsDataResultStrategy):
        """
        Generates a short summary of the BEST strategy
        """
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.generateIntegrationShortSummary")
        strStrategyShortSummary = ""
        iTotalNoImages = 0
        fTotalExposureTime = 0.0
        xsDataDiffractionPlan = None
        if self.getDataInput():
            if self.getDataInput().getDiffractionPlan():
                xsDataDiffractionPlan = self.getDataInput().getDiffractionPlan()
        if self.__bEstimateRadiationDamage:
            strStrategyShortSummary += "Strategy: Radiation damage estimated"
            if self.__edPluginRaddose.getDataOutput().getTimeToReachHendersonLimit():
                strStrategyShortSummary += ", time to reach Henderson limit: %.1f s\n" % self.__edPluginRaddose.getDataOutput().getTimeToReachHendersonLimit().getValue()
            else:
                strStrategyShortSummary += "\n"

        else:
            strStrategyShortSummary += "Strategy: No radiation damage estimation"
            if xsDataDiffractionPlan:
                if xsDataDiffractionPlan.getMaxExposureTimePerDataCollection():
                    strStrategyShortSummary += ", max exposure time per data collection: %.1f s\n" % xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue()
                else:
                    strStrategyShortSummary += "\n"
            else:
                strStrategyShortSummary += "\n"
        if xsDataDiffractionPlan:
            strStrategyShortSummary += "Strategy: Options: "
            listStrategyOptions = []
            if xsDataDiffractionPlan.getAnomalousData():
                if xsDataDiffractionPlan.getAnomalousData().getValue():
                    listStrategyOptions.append("anomalous data")
            if xsDataDiffractionPlan.getAimedCompleteness():
                listStrategyOptions.append("aimed completeness = %.1f" % xsDataDiffractionPlan.getAimedCompleteness().getValue())
            if xsDataDiffractionPlan.getAimedMultiplicity():
                listStrategyOptions.append("aimed multiplicity = %d" % xsDataDiffractionPlan.getAimedMultiplicity().getValue())
            if xsDataDiffractionPlan.getAimedResolution():
                listStrategyOptions.append("aimed resolution = %.2f A" % xsDataDiffractionPlan.getAimedResolution().getValue())
            if xsDataDiffractionPlan.getComplexity():
                listStrategyOptions.append("complexity = %s" % xsDataDiffractionPlan.getComplexity().getValue())
            if xsDataDiffractionPlan.getStrategyOption():
                listStrategyOptions.append("extra strategy option(s) = %s" % xsDataDiffractionPlan.getStrategyOption().getValue())
            if listStrategyOptions != []:
                for strStrategyOption in listStrategyOptions[:-1]:
                    strStrategyShortSummary += strStrategyOption + ", "
                strStrategyShortSummary += listStrategyOptions[-1]
            strStrategyShortSummary += "\n"
        fResolutionMax = None
        for xsDataCollectionPlan in _xsDataResultStrategy.getCollectionPlan():
            iNoCollectionPlan = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
            strStrategyShortSummary += "Strategy: Collection plan %d" % iNoCollectionPlan
            xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
            if xsDataStrategySummary.getResolutionReasoning() != None:
                strResolutionResoning = xsDataStrategySummary.getResolutionReasoning().getValue()
                strStrategyShortSummary += ": %s\n" % strResolutionResoning
            else:
                strStrategyShortSummary += "\n"
            xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
            fRankingResolution = xsDataStrategySummary.getRankingResolution().getValue()
            strStrategyShortSummary += "Strategy: Ranking resolution: %.2f [A]\n" % fRankingResolution
            for xsDataSubWedge in xsDataCollectionStrategy.getSubWedge():
                iWedgeNo = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
                strStrategyShortSummary += "Strategy: wedge %d: " % iWedgeNo
                xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                fResolution = xsDataStrategySummary.getResolution().getValue()
                if (fResolutionMax is None) or (fResolution < fResolutionMax):
                    fResolutionMax = fResolution
                strStrategyShortSummary += "resolution %.2f [A], " % fResolution
                xsDataStringAction = xsDataSubWedge.getAction()
                if xsDataStringAction is not None:
                    strStrategyShortSummary += "%s, " % xsDataStringAction.getValue()
                iSubWedgeNo = xsDataSubWedge.getSubWedgeNumber().getValue()
                strStrategyShortSummary += "sub wedge %d: " % iSubWedgeNo
                xsDataExperimentalCondition = xsDataSubWedge.getExperimentalCondition()
                xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()
                fRotationStart = xsDataGoniostat.getRotationAxisStart().getValue()
                strStrategyShortSummary += "start %.2f, " % fRotationStart
                fRange = xsDataGoniostat.getOscillationWidth().getValue()
                fRotationEnd = xsDataGoniostat.getRotationAxisEnd().getValue()
                iNoImages = int((fRotationEnd - fRotationStart) / fRange + 0.1)
                strStrategyShortSummary += "images %d, " % iNoImages
                strStrategyShortSummary += "width %.2f, " % fRange
                xsDataBeam = xsDataExperimentalCondition.getBeam()
                fExpTime = xsDataBeam.getExposureTime().getValue()
                strStrategyShortSummary += "time %.2f [s], " % fExpTime
                fTransmission = xsDataBeam.getTransmission().getValue()
                strStrategyShortSummary += "transmission %.2f\n" % fTransmission
                iTotalNoImages += iNoImages
                fTotalExposureTime += fExpTime * iNoImages
            strStrategyShortSummary += "Strategy: total no images %d, total exposure time %.1f [s]\n" % \
                                    (iTotalNoImages, fTotalExposureTime)
        if (fRankingResolution < fResolutionMax) and (abs(fRankingResolution - fResolutionMax) > 0.1):
            strStrategyShortSummary += "\n"
            strStrategyShortSummary += "OBS! "*20 + "\n"
            strStrategyShortSummary += "\n"
            strStrategyShortSummary += "BEST has calculated that it should be possible to collect data to %.2f A from this sample.\n" % fRankingResolution
            strStrategyShortSummary += "If you want to calculate a new strategy for data collection to this resolution you\n"
            strStrategyShortSummary += "must first recollect reference images at this resolution.\n"
            strStrategyShortSummary += "\n"
            strStrategyShortSummary += "OBS! "*20 + "\n"
            strStrategyShortSummary += "\n"
        
        self.setDataOutput(XSDataString(strStrategyShortSummary), "strategyShortSummary")

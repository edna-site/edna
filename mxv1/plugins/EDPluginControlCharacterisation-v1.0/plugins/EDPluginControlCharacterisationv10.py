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

from EDVerbose import EDVerbose

from EDPluginControl import EDPluginControl
from EDConfiguration import EDConfiguration
from EDMessage       import EDMessage

from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataCharacterisation
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataStrategyInput


class EDPluginControlCharacterisationv10(EDPluginControl):
    """
    The Plugin that controls the whole characterisation.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataCollection)
        self.__strPluginIndexingName = "EDPluginControlIndexingv10"
        self.__edPluginIndexing = None
        self.__strPluginIntegrationName = "EDPluginControlIntegrationv10"
        self.__edPluginIntegration = None
        self.__strPluginStrategyName = "EDPluginControlStrategyv10"
        self.__edPluginStrategy = None
        self.__xsDataCharacterisation = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDiffractionPlan(), "diffractionPlan")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.preProcess...")

        self.__edPluginIndexing = self.loadPlugin(self.__strPluginIndexingName   , "Indexing")
        self.__edPluginIntegration = self.loadPlugin(self.__strPluginIntegrationName, "Integration")
        self.__edPluginStrategy = self.loadPlugin(self.__strPluginStrategyName   , "Strategy")

        if (self.__edPluginIndexing is not None):
            EDVerbose.DEBUG("EDPluginControlCharacterisationv10.preProcess: " + self.__strPluginIndexingName + " Found... setting Data Input")
            # create Data Input for indexing
            xsDataCollection = self.getDataInput()
            xsDataSample = xsDataCollection.getSample()
            xsDataSubWedgeList = xsDataCollection.getSubWedge()
            xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()

            xsDataIndexingInput = XSDataIndexingInput()
            xsDataIndexingInput.setDataCollection(xsDataCollection)
            xsDataIndexingInput.setExperimentalCondition(xsDataExperimentalCondition)

            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
            xsDataStringForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup()
            if (xsDataStringForcedSpaceGroup is not None):
                xsDataCrystal = XSDataCrystal()
                xsDataSpaceGroup = XSDataSpaceGroup()
                xsDataSpaceGroup.setName(xsDataStringForcedSpaceGroup)
                xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)
                xsDataIndexingInput.setCrystal(xsDataCrystal)

            self.__edPluginIndexing.setDataInput(xsDataIndexingInput)

            # Populate characterisation object
            self.__xsDataCharacterisation = XSDataCharacterisation()
            self.__xsDataCharacterisation.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))



    def process(self, _edObject=None):
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.process")
        self.connectProcess(self.__edPluginIndexing.executeSynchronous)
        self.__edPluginIndexing.connectSUCCESS(self.doIndexingToIntegrationTransition)
        self.__edPluginIndexing.connectFAILURE(self.doFailureActionIndexing)
        self.__edPluginIntegration.connectSUCCESS(self.doIntegrationToStrategyTransition)
        self.__edPluginIntegration.connectFAILURE(self.doFailureActionIntegration)
        self.__edPluginStrategy.connectFAILURE(self.doFailureActionStrategy)
        self.__edPluginStrategy.connectSUCCESS(self.doSuccessActionStrategy)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.postProcess")
        if (self.__xsDataCharacterisation is not None):
            self.setDataOutput(self.__xsDataCharacterisation)


    def doIndexingToIntegrationTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doIndexingToIntegrationTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv10.doIntegrationToStrategyTransition")
        xsDataIndexingResult = self.__edPluginIndexing.getDataOutput()
        self.__xsDataCharacterisation.setIndexingResult(xsDataIndexingResult)
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self.__xsDataCharacterisation.getDataCollection())
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined())
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self.__edPluginIntegration.setDataInput(xsDataIntegrationInput)
        self.__edPluginIntegration.executeSynchronous()


    def doIntegrationToStrategyTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doIntegrationToStrategyTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv10.doIntegrationToStrategyTransition")

        xsDataIntegrationOutput = self.__edPluginIntegration.getDataOutput()
        self.__xsDataCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        #EDVerbose.DEBUG( self.__xsDataExperimentCharacterisation.marshal() )
        xsDataStrategyInput = XSDataStrategyInput()

        xsDataSolutionSelected = self.__xsDataCharacterisation.getIndexingResult().getSelectedSolution()

        xsDataStrategyInput.setCrystalRefined(xsDataSolutionSelected.getCrystal())
        xsDataStrategyInput.setSample(self.__xsDataCharacterisation.getDataCollection().getSample())

        xsDataIntegrationSubWedgeResultList = xsDataIntegrationOutput.getIntegrationSubWedgeResult()

        xsDataStrategyInput.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
        xsDataStrategyInput.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
        xsDataStrategyInput.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())

        for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
            xsDataStrategyInput.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())

        xsDataStrategyInput.setDiffractionPlan(self.__xsDataCharacterisation.getDataCollection().getDiffractionPlan())

        #print xsDataStrategyInput.marshal()
        self.__edPluginStrategy.setDataInput(xsDataStrategyInput)
        self.__edPluginStrategy.executeSynchronous()



    def doFailureActionIndexing(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doFailureActionIndexing")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv10.doFailureActionIndexing")


    def doFailureActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doFailureActionIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv10.doFailureActionIntegration")


    def doFailureActionStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doFailureActionStrategy")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv10.doFailureActionStrategy")


    def doSuccessActionStrategy(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.doSuccessActionStrategy")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv10.doSuccessActionStrategy")
        xsDataStrategyResult = self.__edPluginStrategy.getDataOutput()
        self.__xsDataCharacterisation.setStrategyResult(xsDataStrategyResult)


    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv01.configure")
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            strWarningMessage = EDMessage.WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 % ('EDPluginControlCharacterisationv01.configure', self.getPluginName())
            EDVerbose.DEBUG(strWarningMessage)
        else:
            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, "KAPPA")
            if(strSymopHome == None or strSymopHome != "ON"):
                self.__strPluginStrategyName = "EDPluginControlStrategyv10"
            else:
                self.__strPluginStrategyName = "EDPluginControlKappaStrategyv10"

            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, "POINTLESS")
            if(strSymopHome == None or strSymopHome != "ON"):
                self.__strPluginIntegrationName = "EDPluginControlIntegrationv10"
            else:
                self.__strPluginIntegrationName = "EDPluginControlIntegrationPointlessv10"



    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of characterisation:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()
        xsDataCollection = self.getDataInput()
        xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
        self.addExecutiveSummaryLine("Diffraction plan:")
        if (xsDataDiffractionPlan.getComplexity() is not None):
            self.addExecutiveSummaryLine("BEST complexity                       : %s" % xsDataDiffractionPlan.getComplexity().getValue())
        if (xsDataDiffractionPlan.getAimedCompleteness() is not None):
            self.addExecutiveSummaryLine("Aimed completeness                    : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getAimedCompleteness().getValue()))
        if (xsDataDiffractionPlan.getRequiredCompleteness() is not None):
            self.addExecutiveSummaryLine("Required completeness                 : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getRequiredCompleteness().getValue()))
        if (xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is not None):
            self.addExecutiveSummaryLine("Aimed I/sigma at highest resolution   : %6.1f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue())
        if (xsDataDiffractionPlan.getAimedResolution() is not None):
            self.addExecutiveSummaryLine("Aimed resolution                      : %6.1f [A]" % xsDataDiffractionPlan.getAimedResolution().getValue())
        if (xsDataDiffractionPlan.getRequiredResolution() is not None):
            self.addExecutiveSummaryLine("Required resolution                   : %6.1f [A]" % xsDataDiffractionPlan.getRequiredResolution().getValue())
        if (xsDataDiffractionPlan.getAimedMultiplicity() is not None):
            self.addExecutiveSummaryLine("Aimed multiplicity                    : %6.1f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue())
        if (xsDataDiffractionPlan.getRequiredMultiplicity() is not None):
            self.addExecutiveSummaryLine("Required multiplicity                 : %6.1f" % xsDataDiffractionPlan.getRequiredMultiplicity().getValue())
        if (xsDataDiffractionPlan.getForcedSpaceGroup() is not None):
            self.addExecutiveSummaryLine("Forced space group                    : %6s" % xsDataDiffractionPlan.getForcedSpaceGroup().getValue())
        if (xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is not None):
            self.addExecutiveSummaryLine("Max exposure time per data collection : %6.1f [s]" % xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue())
        self.addExecutiveSummarySeparator()
        if (self.__edPluginIndexing is not None):
            self.appendExecutiveSummary(self.__edPluginIndexing, "Indexing : ")
        if (self.__edPluginIntegration is not None):
            self.appendExecutiveSummary(self.__edPluginIntegration, "Integration : ")
        if (self.__edPluginStrategy is not None):
            self.appendExecutiveSummary(self.__edPluginStrategy, "Strategy : ")



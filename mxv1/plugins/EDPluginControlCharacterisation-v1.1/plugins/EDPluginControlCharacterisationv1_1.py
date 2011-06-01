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


from EDVerbose       import EDVerbose
from EDPluginControl import EDPluginControl
from EDConfiguration import EDConfiguration
from EDMessage       import EDMessage
from EDUtilsFile     import EDUtilsFile

from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataInputStrategy


class EDPluginControlCharacterisationv1_1(EDPluginControl):
    """
    The Plugin that controls the whole characterisation.
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisation)
        self.__strPluginIndexingName = "EDPluginControlIndexingv10"
        self.__edPluginIndexing = None
        self.__strPluginIntegrationName = "EDPluginControlIntegrationv10"
        self.__edPluginIntegration = None
        self.__strPluginStrategyName = "EDPluginControlStrategyv1_1"
        self.__edPluginStrategy = None
        self.__xsDataResultCharacterisation = None
        self.__strPluginKappaStrategyName = "EDPluginControlKappaStrategyv1_1"
        self.__strPluginIntegrationPointlessName = "EDPluginControlIntegrationPointlessv10"


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan(), "diffractionPlan")


    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.configure")
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration is None):
            EDVerbose.DEBUG("No plugin configuration found for EDPluginControlCharacterisationv1_1.")
        else:
            if (self.getControlledPluginName("indexingPlugin") is not None):
                self.__strPluginIndexingName = self.getControlledPluginName("indexingPlugin")
            if (self.getControlledPluginName("integrationPlugin") is not None):
                self.__strPluginIntegrationName = self.getControlledPluginName("integrationPlugin")
            if (self.getControlledPluginName("strategyPlugin") is not None):
                self.__strPluginStrategyName = self.getControlledPluginName("strategyPlugin")
            if (self.getControlledPluginName("kappaStrategyPlugin") is not None):
                self.__strPluginKappaStrategyName = self.getControlledPluginName("kappaStrategyPlugin")
            if (self.getControlledPluginName("integrationPointlessPlugin") is not None):
                self.__strPluginIntegrationPoitlessName = self.getControlledPluginName("integrationPointlessPlugin")

            pyStrKappa = EDConfiguration.getStringParamValue(pluginConfiguration, "KAPPA")
            if(pyStrKappa == "ON"):
                self.__strPluginStrategyName = self.__strPluginKappaStrategyName

            pyStrPointless = EDConfiguration.getStringParamValue(pluginConfiguration, "POINTLESS")
            if(pyStrPointless == "ON"):
                self.__strPluginIntegrationName = self.__strPluginIntegrationPointlessName



    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.preProcess...")

        self.__edPluginIndexing = self.loadPlugin(self.__strPluginIndexingName   , "Indexing")
        self.__edPluginIntegration = self.loadPlugin(self.__strPluginIntegrationName, "Integration")
        self.__edPluginStrategy = self.loadPlugin(self.__strPluginStrategyName   , "Strategy")

        if (self.__edPluginIndexing is not None):
            EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.preProcess: " + self.__strPluginIndexingName + " Found... setting Data Input")
            # create Data Input for indexing
            xsDataInputStrategy = self.getDataInput()
            xsDataCollection = xsDataInputStrategy.getDataCollection()
            xsDataSample = xsDataCollection.getSample()
            xsDataSubWedgeList = xsDataCollection.getSubWedge()
            if ((xsDataSubWedgeList is None) or (xsDataSubWedgeList == [])):
            	strError = "EDPluginControlCharacterisationv1_1.preProcess: No subwedges in input data."
            	EDVerbose.ERROR(strError)
                self.setFailure()
            else:
                xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()

                # Fix for bug 431: if the flux is zero raise an error
                xsDataDoubleFlux = xsDataExperimentalCondition.getBeam().getFlux()
                if (xsDataDoubleFlux is not None):
                    if (xsDataDoubleFlux.getValue() < 0.1):
                        pyStrErrorMessage = "EDPluginControlCharacterisationv1_1.preProcess ERROR: Input flux is negative or close to zero. Execution of characterisation aborted."
                        EDVerbose.ERROR(pyStrErrorMessage)
                        self.addErrorMessage(pyStrErrorMessage)
                        self.setFailure()

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
                self.__xsDataResultCharacterisation = XSDataResultCharacterisation()
                self.__xsDataResultCharacterisation.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))



    def process(self, _edObject=None):
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.process")
        self.connectProcess(self.__edPluginIndexing.executeSynchronous)
        self.__edPluginIndexing.connectSUCCESS(self.doIndexingToIntegrationTransition)
        self.__edPluginIndexing.connectFAILURE(self.doFailureActionIndexing)
        self.__edPluginIntegration.connectSUCCESS(self.doIntegrationToStrategyTransition)
        self.__edPluginIntegration.connectFAILURE(self.doFailureActionIntegration)
        self.__edPluginStrategy.connectFAILURE(self.doFailureActionStrategy)
        self.__edPluginStrategy.connectSUCCESS(self.doSuccessActionStrategy)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.postProcess")
        if (self.__xsDataResultCharacterisation is not None):
            self.setDataOutput(self.__xsDataResultCharacterisation)


    def doIndexingToIntegrationTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doIndexingToIntegrationTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doIntegrationToStrategyTransition")
        xsDataIndexingResult = self.__edPluginIndexing.getDataOutput()
        self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self.__xsDataResultCharacterisation.getDataCollection())
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined())
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self.__edPluginIntegration.setDataInput(xsDataIntegrationInput)
        self.__edPluginIntegration.executeSynchronous()


    def doIntegrationToStrategyTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doIntegrationToStrategyTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doIntegrationToStrategyTransition")

        xsDataIntegrationOutput = self.__edPluginIntegration.getDataOutput()
        self.__xsDataResultCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        #EDVerbose.DEBUG( self.__xsDataExperimentCharacterisation.marshal() )
        xsDataInputStrategy = XSDataInputStrategy()

        xsDataSolutionSelected = self.__xsDataResultCharacterisation.getIndexingResult().getSelectedSolution()

        xsDataInputStrategy.setCrystalRefined(xsDataSolutionSelected.getCrystal())
        xsDataInputStrategy.setSample(self.__xsDataResultCharacterisation.getDataCollection().getSample())

        xsDataIntegrationSubWedgeResultList = xsDataIntegrationOutput.getIntegrationSubWedgeResult()

        xsDataInputStrategy.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
        xsDataInputStrategy.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
        xsDataInputStrategy.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())

        for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
            xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())

        xsDataInputStrategy.setDiffractionPlan(self.__xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())

        #print xsDataInputStrategy.marshal()
        self.__edPluginStrategy.setDataInput(xsDataInputStrategy)
        self.__edPluginStrategy.executeSynchronous()



    def doFailureActionIndexing(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doFailureActionIndexing")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doFailureActionIndexing")
        # If indexing fails all processing should stop
        self.generateExecutiveSummary(self)
        self.setFailure()


    def doFailureActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doFailureActionIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doFailureActionIntegration")


    def doFailureActionStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doFailureActionStrategy")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doFailureActionStrategy")


    def doSuccessActionStrategy(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.doSuccessActionStrategy")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doSuccessActionStrategy")
        xsDataResultStrategy = self.__edPluginStrategy.getDataOutput()
        self.__xsDataResultCharacterisation.setStrategyResult(xsDataResultStrategy)







    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_1.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of characterisation:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()
        xsDataInputStrategy = self.getDataInput()
        xsDataCollection = xsDataInputStrategy.getDataCollection()
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


    def getPluginStrategyName(self):
        return self.__strPluginStrategyName

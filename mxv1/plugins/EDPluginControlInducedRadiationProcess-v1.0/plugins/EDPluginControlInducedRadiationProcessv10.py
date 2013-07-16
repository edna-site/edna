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
#                            Ricardo Leal
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

__authors__ = [ "Ricardo Leal", "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "ricardo.leal@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDVerbose       import EDVerbose
from EDPluginControl import EDPluginControl

from XSDataMXv1 import XSDataInputInducedRadiationProcess
from XSDataMXv1 import XSDataInputStrategy


class EDPluginControlInducedRadiationProcessv10(EDPluginControl):
    """
    The Plugin that controls the whole characterisation.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputInducedRadiationProcess)
        self.__strPluginIntegrationName = "EDPluginControlIntegrationv10"
        self.__edPluginIntegration = None
        self.__strPluginStrategyName = "EDPluginControlStrategyv1_2"
        self.__edPluginStrategy = None
        self.__xsDataResultCharacterisation = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getIndexingResult(), "indexingResult")
        self.checkMandatoryParameters(self.getDataInput().getStrategyResult(), "strategyResult")
        # Stategy option mandatory (dampar or bonly!)
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan().getStrategyOption(), "strategyOption")

    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        if (self.getControlledPluginName("integrationPlugin") is not None):
            self.__strPluginIntegrationName = self.getControlledPluginName("integrationPlugin")
        if (self.getControlledPluginName("strategyPlugin") is not None):
            self.__strPluginStrategyName = self.getControlledPluginName("strategyPlugin")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.preProcess...")

        # TODO, if it's Bonly no Indexation needed! Get matrix from reference
        #xsDataStringStrategyOption = self.getDataInput().getDataCollection().getDiffractionPlan().getStrategyOption()
        #pyStrStrategyOption = xsDataStringStrategyOption.getValue()
        #if ( pyStrStrategyOption != "-Bonly" ):
        #    self.__edPluginIndexing    = self.loadPlugin( self.__strPluginIndexingName   , "Indexing" )

        self.__edPluginIntegration = self.loadPlugin(self.__strPluginIntegrationName, "Integration")
        self.__edPluginStrategy = self.loadPlugin(self.__strPluginStrategyName   , "Strategy")

#        if ( self.__edPluginIndexing is not None ):
#            EDVerbose.DEBUG( "EDPluginControlInducedRadiationProcessv10.preProcess: " + self.__strPluginIndexingName + " Found... setting Data Input")
#            # create Data Input for indexing
#            xsDataInputStrategy = self.getDataInput()
#            xsDataCollection   = xsDataInputStrategy.getDataCollection()
#            xsDataSample       = xsDataCollection.getSample()
#            xsDataSubWedgeList = xsDataCollection.getSubWedge()
#            xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()
#            
#            xsDataIndexingInput = XSDataIndexingInput()
#            xsDataIndexingInput.setDataCollection( xsDataCollection )
#            xsDataIndexingInput.setExperimentalCondition( xsDataExperimentalCondition )
#            
#            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
#            xsDataStringForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup()
#            if ( xsDataStringForcedSpaceGroup is not None ):
#                xsDataCrystal = XSDataCrystal()
#                xsDataSpaceGroup = XSDataSpaceGroup()
#                xsDataSpaceGroup.setName( xsDataStringForcedSpaceGroup )
#                xsDataCrystal.setSpaceGroup( xsDataSpaceGroup )
#                xsDataIndexingInput.setCrystal( xsDataCrystal )
#            
#            self.__edPluginIndexing.setDataInput( xsDataIndexingInput )
#            
#            # Populate characterisation object
#            self.__xsDataResultCharacterisation = XSDataResultCharacterisation()
#            self.__xsDataResultCharacterisation.setDataCollection( XSDataCollection.parseString( xsDataCollection.marshal() ) )



    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.process")
        self.connectProcess(self.__edPluginIntegration.executeSynchronous)
#        self.__edPluginIndexing.connectSUCCESS( self.doIndexingToIntegrationTransition )
#        self.__edPluginIndexing.connectFAILURE( self.doFailureActionIndexing )
        self.__edPluginIntegration.connectSUCCESS(self.doIntegrationToStrategyTransition)
        self.__edPluginIntegration.connectFAILURE(self.doFailureActionIntegration)
        self.__edPluginStrategy.connectFAILURE(self.doFailureActionStrategy)
        self.__edPluginStrategy.connectSUCCESS(self.doSuccessActionStrategy)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.postProcess")
        if (self.__xsDataResultCharacterisation is not None):
            self.setDataOutput(self.__xsDataResultCharacterisation)


#    def doIndexingToIntegrationTransition(self, _edPlugin=None):
#        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doIndexingToIntegrationTransition")
#        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doIntegrationToStrategyTransition")
#        xsDataIndexingResult = self.__edPluginIndexing.getDataOutput()
#        self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
#        xsDataIntegrationInput = XSDataIntegrationInput()
#        xsDataIntegrationInput.setDataCollection(self.__xsDataResultCharacterisation.getDataCollection())
#        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined())
#        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
#        self.__edPluginIntegration.setDataInput(xsDataIntegrationInput)
#        self.__edPluginIntegration.executeSynchronous()


    def doIntegrationToStrategyTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doIntegrationToStrategyTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doIntegrationToStrategyTransition")

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
        xsDataInputStrategy.setDataCollection(self.getDataInput().getDataCollection())
        for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
            xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())

        xsDataInputStrategy.setDiffractionPlan(self.__xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())

        #print xsDataInputStrategy.marshal()
        self.__edPluginStrategy.setDataInput(xsDataInputStrategy)
        self.__edPluginStrategy.executeSynchronous()



    def doFailureActionIndexing(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doFailureActionIndexing")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doFailureActionIndexing")


    def doFailureActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doFailureActionIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doFailureActionIntegration")


    def doFailureActionStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doFailureActionStrategy")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doFailureActionStrategy")


    def doSuccessActionStrategy(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.doSuccessActionStrategy")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlInducedRadiationProcessv10.doSuccessActionStrategy")
        xsDataResultStrategy = self.__edPluginStrategy.getDataOutput()
        self.__xsDataResultCharacterisation.setStrategyResult(xsDataResultStrategy)


#    def configure(self):
#        EDPluginControl.configure(self)
#        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.configure")
#        pluginConfiguration = self.getConfiguration()
#
#        if(pluginConfiguration == None):
#            warningMessage = EDMessage.WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 % ('EDPluginControlCharacterisationv01.configure', self.getPluginName())
#            EDVerbose.warning(warningMessage)
#            self.addWarningMessage(warningMessage)
#        else:
#            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, "KAPPA")
#            if(strSymopHome == None or strSymopHome != "ON"):
#                #self.__strPluginStrategyName = "EDPluginControlStrategyv10"
#                self.__strPluginStrategyName = self.__strPluginStrategyName
#            else:
#                self.__strPluginStrategyName = "EDPluginControlKappaStrategyv1_1"
#
#            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, "POINTLESS")
#            if(strSymopHome == None or strSymopHome != "ON"):
#                self.__strPluginIntegrationName = "EDPluginControlIntegrationv10"
#            else:
#                self.__strPluginIntegrationName = "EDPluginControlIntegrationPointlessv10"




    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlInducedRadiationProcessv10.generateExecutiveSummary")
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
        #if (self.__edPluginIndexing is not None):
        #    self.appendExecutiveSummary(self.__edPluginIndexing, "Indexing : ")
        if (self.__edPluginIntegration is not None):
            self.appendExecutiveSummary(self.__edPluginIntegration, "Integration : ")
        if (self.__edPluginStrategy is not None):
            self.appendExecutiveSummary(self.__edPluginStrategy, "Strategy : ")


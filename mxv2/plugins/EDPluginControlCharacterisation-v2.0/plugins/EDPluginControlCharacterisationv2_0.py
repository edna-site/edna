#
#    Project: EDNA MXv2
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


from EDVerbose       import EDVerbose
from EDFactoryPluginStatic   import EDFactoryPluginStatic
from EDPluginControl import EDPluginControl
from EDConfiguration import EDConfiguration
from EDMessage       import EDMessage

EDFactoryPluginStatic.loadModule("XSDataMXv1")

from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataResultCharacterisation

from XSDataMXv2 import XSDataInputCharacterisationv2_0
from XSDataMXv2 import XSDataResultCharacterisationv2_0

class EDPluginControlCharacterisationv2_0(EDPluginControl):
    """
    The Plugin that controls the whole characterisation: Indexing-Integration-(Kappa)Strategy    
    Indexing-Integration is the same as mxv1 characterisation.
    KappaStrategy:
    Preferred Strategy is given at the initial orientation, but if KAPPA features are enabled,
    strategies are calculated to some alignments.
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        #self.setXSDataInputClass( XSDataInputCharacterisation )
        #self.setXSDataInputClass(EDList)
        #self.strPluginIndexingName = "EDPluginControlIndexingv2_0"
        self.strPluginIndexingName = "EDPluginControlIndexingv10"
        self.edPluginIndexing = None
        self.strPluginIntegrationName = "EDPluginControlIntegrationv10"
        self.edPluginIntegration = None
        self.strPluginStrategyName = "EDPluginControlKappaStrategyv2_0"
        self.edPluginStrategy = None
        self.xsDataResultCharacterisationv2_0 = None
        self.xsDataResultCharacterisation = None
        self.xsDataInputStrategy = None

        self.setXSDataInputClass(XSDataInputCharacterisationv2_0)
        
        EDFactoryPluginStatic.loadModule("XSDataMXv1")
        import XSDataMXv1
        self.setXSDataInputClass(XSDataMXv1.XSDataInputCharacterisation, "mxv1InputCharacterisation")
        EDFactoryPluginStatic.loadModule("XSDataMXv2")
        import XSDataMXv2
        self.setXSDataInputClass(XSDataMXv2.XSDataCollection, "mxv2DataCollection")


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.checkParameters")
        # Check for mxv1InputCharacterisation:
        if self.hasDataInput():
            if self.hasDataInput("mxv1InputCharacterisation") or self.hasDataInput("mxv2DataCollection"):
                EDVerbose.WARNING("Ambiguous input! Both XSDataInputCharacterisatiov2_0 input, and mxv1InputCharacterisation or mxv2DataCollection input(s), are given")
            self.setDataInput(self.getDataInput().getMxv1InputCharacterisation().marshal(), "mxv1InputCharacterisation")
            self.setDataInput(self.getDataInput().getMxv2DataCollection().marshal(), "mxv2DataCollection")
        # Check for mxv1InputCharacterisation
        self.checkMandatoryParameters(self.getDataInput("mxv1InputCharacterisation"), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput("mxv1InputCharacterisation")[0].getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput("mxv1InputCharacterisation")[0].getDataCollection().getDiffractionPlan(), "diffractionPlan")



    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.preProcess...")

        self.edPluginIndexing = self.loadPlugin(self.strPluginIndexingName   , "Indexing")
        self.edPluginIntegration = self.loadPlugin(self.strPluginIntegrationName, "Integration")
        self.edPluginStrategy = self.loadPlugin(self.strPluginStrategyName   , "Strategy")

        if (self.edPluginIndexing is not None):
            EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.preProcess: " + self.strPluginIndexingName + " Found... setting Data Input")
            # create Data Input for indexing
            xsDataInputStrategy = self.getDataInput("mxv1InputCharacterisation")[0]
            xsDataCollection = xsDataInputStrategy.getDataCollection()
            #xsDataSample = xsDataCollection.getSample()
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

            self.edPluginIndexing.setDataInput(xsDataIndexingInput)

            # Populate characterisation object
            self.xsDataResultCharacterisationv2_0 = XSDataResultCharacterisationv2_0()
            self.xsDataResultCharacterisation = XSDataResultCharacterisation()
            self.xsDataResultCharacterisationv2_0.setMxv1ResultCharacterisation(self.xsDataResultCharacterisation)
            self.xsDataResultCharacterisation.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))



    def process(self, _edObject=None):
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.process")
        self.connectProcess(self.edPluginIndexing.executeSynchronous)
        self.edPluginIndexing.connectSUCCESS(self.doIndexingToIntegrationTransition)
        self.edPluginIndexing.connectFAILURE(self.doFailureActionIndexing)
        self.edPluginIntegration.connectSUCCESS(self.doIntegrationToStrategyTransition)
        self.edPluginIntegration.connectFAILURE(self.doFailureActionIntegration)
        self.edPluginStrategy.connectFAILURE(self.doFailureActionStrategy)
        self.edPluginStrategy.connectSUCCESS(self.doSuccessActionStrategy)


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.postProcess")
        if (self.xsDataResultCharacterisationv2_0 is not None):
            self.setDataOutput(self.xsDataResultCharacterisationv2_0)


    def doIndexingToIntegrationTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doIndexingToIntegrationTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doIntegrationToStrategyTransition")
        xsDataIndexingResult = self.edPluginIndexing.getDataOutput()
        self.xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
        from XSDataMXv1 import XSDataIntegrationInput
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self.xsDataResultCharacterisation.getDataCollection())
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined())
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self.edPluginIntegration.setDataInput(xsDataIntegrationInput)
        self.edPluginIntegration.executeSynchronous()


    def doIntegrationToStrategyTransition(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doIntegrationToStrategyTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doIntegrationToStrategyTransition")

        xsDataIntegrationOutput = self.edPluginIntegration.getDataOutput()
        self.xsDataResultCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        #EDVerbose.DEBUG( self.xsDataExperimentCharacterisation.marshal() )
        from XSDataMXv1 import XSDataInputStrategy
        xsDataInputStrategyOLD = XSDataInputStrategy()

        xsDataSolutionSelected = self.xsDataResultCharacterisation.getIndexingResult().getSelectedSolution()

        xsDataInputStrategyOLD.setCrystalRefined(xsDataSolutionSelected.getCrystal())
        xsDataInputStrategyOLD.setSample(self.xsDataResultCharacterisation.getDataCollection().getSample())

        xsDataIntegrationSubWedgeResultList = xsDataIntegrationOutput.getIntegrationSubWedgeResult()

        xsDataInputStrategyOLD.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
        xsDataInputStrategyOLD.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
        xsDataInputStrategyOLD.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())

        for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
            xsDataInputStrategyOLD.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())

        xsDataInputStrategyOLD.setDiffractionPlan(self.xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())
        xsDataInputStrategyOLD.setXdsBackgroundImage(self.xsDataResultCharacterisation.getXdsBackgroundImage())

        #print xsDataInputStrategy.marshal()
        self.edPluginStrategy.setDataInput(xsDataInputStrategyOLD, "mxv1InputStrategy")
        if self.hasDataInput("mxv2DataCollection"):
            self.edPluginStrategy.setDataInput(self.getDataInput("mxv2DataCollection")[0], "mxv2DataCollection")
        self.edPluginStrategy.setDataInput(self.xsDataResultCharacterisation.getIndexingResult(), "mxv1IndexingResult")

#            xsDataInputStrategy= EDList()
#            xsDataInputStrategy.add(xsDataInputStrategyOLD)
#            xsDataInputStrategy.add(self.getDataInput()[1])
#            xsDataInputStrategy.add(self.xsDataResultCharacterisationv2_0.getIndexingResult())
#            self.edPluginStrategy.setDataInput( xsDataInputStrategy )
        self.edPluginStrategy.executeSynchronous()



    def doFailureActionIndexing(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doFailureActionIndexing")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionIndexing")


    def doFailureActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doFailureActionIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionIntegration")


    def doFailureActionStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doFailureActionStrategy")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionStrategy")


    def doSuccessActionStrategy(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.doSuccessActionStrategy")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doSuccessActionStrategy")
        xsDataResultStrategy = self.edPluginStrategy.getDataOutput()
        self.xsDataResultCharacterisation.setStrategyResult(xsDataResultStrategy)


    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.configure")
        pluginConfiguration = self.getConfiguration()

        self.strPluginStrategyName = "EDPluginControlKappaStrategyv2_0"
        if(pluginConfiguration != None):
            strKappaOn = EDConfiguration.getStringParamValue(pluginConfiguration, "KAPPA")
#            if(strKappaOn == None or strKappaOn != "ON"):
#                #self.strPluginStrategyName = "EDPluginControlStrategyv10"
#                #self.strPluginStrategyName = "EDPluginControlStrategyv2_0"
#                self.strPluginStrategyName = "EDPluginControlKappaStrategyv2_0"
#            else:
#                self.strPluginStrategyName = "EDPluginControlKappaStrategyv2_0"

            strPointlessOn = EDConfiguration.getStringParamValue(pluginConfiguration, "POINTLESS")
            if(strPointlessOn == None or strPointlessOn != "True"):
                self.strPluginIntegrationName = "EDPluginControlIntegrationv10"
            else:
                self.strPluginIntegrationName = "EDPluginControlIntegrationPointlessv10"




    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv2_0.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of characterisation:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()
        xsDataInputStrategy = self.getDataInput("mxv1InputCharacterisation")[0]
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
        if (self.edPluginIndexing is not None):
            self.appendExecutiveSummary(self.edPluginIndexing, "Indexing : ")
        if (self.edPluginIntegration is not None):
            self.appendExecutiveSummary(self.edPluginIntegration, "Integration : ")
        if (self.edPluginStrategy is not None):
            self.appendExecutiveSummary(self.edPluginStrategy, "Strategy : ")


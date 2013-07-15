#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson
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

from XSDataCommon import XSDataString

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataGeneratePredictionInput
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataInputStrategy

class EDPluginControlCharacterisationv1_2(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisation)
        self.__strPluginControlIndexingIndicators = "EDPluginControlIndexingIndicatorsv10"
        self.__strPluginControlIndexingLabelit = "EDPluginControlIndexingLabelitv10"
        self.__strPluginExecEvaluationIndexing = "EDPluginExecEvaluationIndexingv10"
        self.__strPluginControlGeneratePrediction = "EDPluginControlGeneratePredictionv10"
        self.__strPluginControlIntegration = "EDPluginControlIntegrationv10"
        self.__strPluginControlStrategy = "EDPluginControlStrategyv1_2"
        self.__edPluginControlIndexingIndicators = None
        self.__edPluginControlIndexingLabelit = None
        self.__edPluginExecEvaluationIndexingMOSFLM = None
        self.__edPluginExecEvaluationIndexingLABELIT = None
        self.__edPluginControlGeneratePrediction = None
        self.__edPluginControlIntegration = None
        self.__edPluginControlStrategy = None
        self.__xsDataCollection = None
        self.__xsDataResultCharacterisation = None
        self.__xsDataIndexingResultMOSFLM = None
        self.__xsDataCrystal = None
        self.__strCharacterisationShortSummary = ""
        self.__strStatusMessage = ""
        self.__bDoStrategyCalculation = True



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan(), "diffractionPlan")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.preProcess")
        # Load the plugins
        self.__edPluginControlIndexingIndicators = self.loadPlugin(self.__strPluginControlIndexingIndicators, \
                                                                   "Indexing")
        self.__edPluginControlIndexingLabelit = self.loadPlugin(self.__strPluginControlIndexingLabelit, \
                                                                   "IndexingLabelit")
        self.__edPluginExecEvaluationIndexingMOSFLM = self.loadPlugin(self.__strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionMOSFLM")
        self.__edPluginExecEvaluationIndexingLABELIT = self.loadPlugin(self.__strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionLABELIT")
        self.__edPluginControlGeneratePrediction = self.loadPlugin(self.__strPluginControlGeneratePrediction, \
                                                                   "GeneratePrediction")
        self.__edPluginControlIntegration = self.loadPlugin(self.__strPluginControlIntegration, \
                                                            "Integration")
        self.__edPluginControlStrategy = self.loadPlugin(self.__strPluginControlStrategy, \
                                                         "Strategy")
        if (self.__edPluginControlIndexingIndicators is not None):
            EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.preProcess: " + self.__strPluginControlIndexingIndicators + " Found... setting Data Input")
            # create Data Input for indexing
            xsDataInputCharacterisation = self.getDataInput()
            self.__xsDataCollection = xsDataInputCharacterisation.getDataCollection()
            xsDataCrystal = None
            xsDataSubWedgeList = self.__xsDataCollection.getSubWedge()
            if ((xsDataSubWedgeList is None) or (xsDataSubWedgeList == [])):
                strError = "EDPluginControlCharacterisationv1_2.preProcess: No subwedges in input data."
                EDVerbose.ERROR(strError)
                self.setFailure()
            else:
                xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()

                # Fix for bug 431: if the flux is zero raise an error
                xsDataDoubleFlux = xsDataExperimentalCondition.getBeam().getFlux()
                if (xsDataDoubleFlux is not None):
                    if (xsDataDoubleFlux.getValue() < 0.1):
                        strErrorMessage = "Input flux is negative or close to zero. Execution of characterisation aborted."
                        EDVerbose.ERROR(strErrorMessage)
                        self.addErrorMessage("EDPluginControlCharacterisationv1_2.preProcess ERROR: " + strErrorMessage)
                        #self.addComment(strErrorMessage)
                        self.setFailure()

                xsDataDiffractionPlan = self.__xsDataCollection.getDiffractionPlan()
                xsDataStringForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup()
                if (xsDataStringForcedSpaceGroup is not None):
                    self.__xsDataCrystal = XSDataCrystal()
                    xsDataSpaceGroup = XSDataSpaceGroup()
                    xsDataSpaceGroup.setName(xsDataStringForcedSpaceGroup)
                    self.__xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)

                self.__edPluginControlIndexingIndicators.setDataInput(self.__xsDataCollection, "dataCollection")
                if self.__xsDataCrystal is not None:
                    self.__edPluginControlIndexingIndicators.setDataInput(self.__xsDataCrystal, "crystal")

                # Populate characterisation object
                self.__xsDataResultCharacterisation = XSDataResultCharacterisation()
                self.__xsDataResultCharacterisation.setDataCollection(XSDataCollection.parseString(self.__xsDataCollection.marshal()))


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.process")
        self.__edPluginControlIndexingIndicators.connectSUCCESS(self.doSuccessIndexingIndicators)
        self.__edPluginControlIndexingIndicators.connectFAILURE(self.doFailureIndexingIndicators)
        self.__edPluginControlIndexingLabelit.connectSUCCESS(self.doSuccessIndexingLabelit)
        self.__edPluginControlIndexingLabelit.connectFAILURE(self.doFailureIndexingLabelit)
        self.__edPluginExecEvaluationIndexingMOSFLM.connectSUCCESS(self.doSuccessEvaluationIndexingMOSFLM)
        self.__edPluginExecEvaluationIndexingMOSFLM.connectFAILURE(self.doFailureEvaluationIndexingMOSFLM)
        self.__edPluginExecEvaluationIndexingLABELIT.connectSUCCESS(self.doSuccessEvaluationIndexingLABELIT)
        self.__edPluginExecEvaluationIndexingLABELIT.connectFAILURE(self.doFailureEvaluationIndexingLABELIT)
        self.__edPluginControlGeneratePrediction.connectSUCCESS(self.doSuccessGeneratePrediction)
        self.__edPluginControlGeneratePrediction.connectFAILURE(self.doFailureGeneratePrediction)
        self.__edPluginControlIntegration.connectSUCCESS(self.doSuccessIntegration)
        self.__edPluginControlIntegration.connectFAILURE(self.doFailureIntegration)
        self.__edPluginControlStrategy.connectSUCCESS(self.doSuccessStrategy)
        self.__edPluginControlStrategy.connectFAILURE(self.doFailureStrategy)
        self.__edPluginControlIndexingIndicators.executeSynchronous()


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.finallyProcess")
        if self.__edPluginControlGeneratePrediction.isRunning():
            self.__edPluginControlGeneratePrediction.synchronize()
        if self.__strStatusMessage != None:
            self.setDataOutput(XSDataString(self.__strStatusMessage), "statusMessage")
            self.__xsDataResultCharacterisation.setStatusMessage(XSDataString(self.__strStatusMessage))
        if self.__strCharacterisationShortSummary != None:
            self.setDataOutput(XSDataString(self.__strCharacterisationShortSummary), "shortSummary")
            self.__xsDataResultCharacterisation.setShortSummary(XSDataString(self.__strCharacterisationShortSummary))
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)


    def doSuccessIndexingIndicators(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessIndexingIndicators")
        #self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessIndexingIndicators")
        if self.__edPluginControlIndexingIndicators.hasDataOutput("indexingResult"):
            xsDataIndexingResult = self.__edPluginControlIndexingIndicators.getDataOutput("indexingResult")[0]
            #self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            self.__edPluginExecEvaluationIndexingMOSFLM.setDataInput(xsDataIndexingResult, "indexingResult")
        if self.__edPluginControlIndexingIndicators.hasDataOutput("imageQualityIndicators"):
            listXSDataImageQualityIndicators = self.__edPluginControlIndexingIndicators.getDataOutput("imageQualityIndicators")
            for xsDataImageQualityIndicators in listXSDataImageQualityIndicators:
                self.__xsDataResultCharacterisation.addImageQualityIndicators(xsDataImageQualityIndicators)
                self.__edPluginExecEvaluationIndexingMOSFLM.setDataInput(xsDataImageQualityIndicators, "imageQualityIndicators")
        if self.__edPluginControlIndexingIndicators.hasDataOutput("indicatorsShortSummary"):
            self.__strCharacterisationShortSummary += self.__edPluginControlIndexingIndicators.getDataOutput("indicatorsShortSummary")[0].getValue()
        self.__edPluginExecEvaluationIndexingMOSFLM.executeSynchronous()


    def doFailureIndexingIndicators(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureIndexingIndicators")
        strErrorMessage = "Execution of Indexing and Indicators plugin failed. Execution of characterisation aborted."
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)
        self.setFailure()
        if self.__strStatusMessage != None:
            self.setDataOutput(XSDataString(self.__strStatusMessage), "statusMessage")
            self.writeDataOutput()


#    def doSuccessIndexingLabelit(self, _edPlugin=None):
#        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessIndexingLabelit")
#        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessIndexingLabelit")
#        # Retrieve the indexing result
#        xsDataIndexingResult = self.__edPluginControlIndexingLabelit.getDataOutput()
#        self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
#        if self.__edPluginControlIndexingLabelit.hasDataOutput("indexingShortSummary"):
#            self.__strCharacterisationShortSummary += self.__edPluginControlIndexingLabelit.getDataOutput("indexingShortSummary")[0].getValue()
#        # Then start the integration of the reference images
#        self.indexingToIntegration()


    def doSuccessIndexingLabelit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessIndexingLabelit")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessIndexingLabelit")
        if self.__edPluginControlIndexingLabelit.hasDataOutput("indexingShortSummary"):
            self.__strCharacterisationShortSummary += self.__edPluginControlIndexingLabelit.getDataOutput("indexingShortSummary")[0].getValue()
        # Check the indexing results
        xsDataIndexingResult = self.__edPluginControlIndexingLabelit.getDataOutput()
        self.__edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataIndexingResult, "indexingResult")
        xsDataImageQualityIndicators = self.__xsDataResultCharacterisation.getImageQualityIndicators()[0]
        self.__edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataImageQualityIndicators, "imageQualityIndicators")
        self.__edPluginExecEvaluationIndexingLABELIT.executeSynchronous()


    def doFailureIndexingLabelit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureIndexingLabelit")
        self.addStatusMessage("Labelit: Indexing FAILURE.")
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)
        if self.__xsDataIndexingResultMOSFLM == None:
            strErrorMessage = "Execution of indexing with both MOSFLM and Labelit failed. Execution of characterisation aborted."
            EDVerbose.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.generateExecutiveSummary(self)
            self.setFailure()
            if self.__strStatusMessage != None:
                self.setDataOutput(XSDataString(self.__strStatusMessage), "statusMessage")
                self.writeDataOutput()
        else:
            # Use the MOSFLM indexing results - even if it's P1
            self.__xsDataResultCharacterisation.setIndexingResult(self.__xsDataIndexingResultMOSFLM)
            xsDataCollection = self.__xsDataResultCharacterisation.getDataCollection()
            xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
            xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
            xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(self.__xsDataIndexingResultMOSFLM.getSelectedSolution().marshal()))
            self.__edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
            if self.__edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                self.__strCharacterisationShortSummary += self.__edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
            # Start the generation of prediction images - we synchronize in the post-process
            self.__edPluginControlGeneratePrediction.execute()
            # Then start the integration of the reference images
            self.indexingToIntegration()



    def doSuccessEvaluationIndexingMOSFLM(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessEvaluationIndexingMOSFLM")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessEvaluationIndexing")
        # Retrieve status messages (if any)
        if self.__edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageImageQualityIndicators"):
            self.addStatusMessage(self.__edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageImageQualityIndicators")[0].getValue())
        if self.__edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageIndexing"):
            self.addStatusMessage("MOSFLM: " + self.__edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexWithLabelit = False
        bIndexingSuccess = self.__edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            xsDataIndexingResult = self.__edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingResult")[0]
            self.__xsDataIndexingResultMOSFLM = xsDataIndexingResult
            # Check if space group is P1 - if yes run Labelit indexing
            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
            xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
            strSpaceGroupName = xsDataSpaceGroup.getName().getValue().upper()
            # Check if MOSFLM has indexed in P1
            if strSpaceGroupName == "P1":
                # Check if the user maybe asked for P1!
                bIndexWithLabelit = True
                if self.__xsDataCollection.getDiffractionPlan() is not None:
                    if self.__xsDataCollection.getDiffractionPlan().getForcedSpaceGroup() is not None:
                        if self.__xsDataCollection.getDiffractionPlan().getForcedSpaceGroup().getValue().upper() == "P1":
                            EDVerbose.screen("P1 space forced by diffraction plan")
                            bIndexWithLabelit = False
            if bIndexWithLabelit:
                EDVerbose.screen("P1 space group choosed - reindexing with Labelit")
            else:
                EDVerbose.screen("MOSFLM indexing successful!")
                if self.__edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                    self.__strCharacterisationShortSummary += self.__edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
                # Generate prediction images
                xsDataCollection = self.__xsDataResultCharacterisation.getDataCollection()
                self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
                xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
                xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
                xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataIndexingResult.getSelectedSolution().marshal()))
                self.__edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
                # Start the generation of prediction images - we synchronize in the post-process
                self.__edPluginControlGeneratePrediction.execute()
                # Then start the integration of the reference images
                self.indexingToIntegration()
        else:
            EDVerbose.screen("Indexing with MOSFLM failed!")
            bIndexWithLabelit = True
        if bIndexWithLabelit:
            # Execute Labelit indexing
            EDVerbose.screen("Now trying to index with Labelit - please be patient...")
            xsDataIndexingInput = XSDataIndexingInput()
            xsDataSubWedgeList = self.__xsDataCollection.getSubWedge()
            xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()
            xsDataIndexingInput.setDataCollection(self.__xsDataCollection)
            xsDataIndexingInput.setExperimentalCondition(xsDataExperimentalCondition)
            if self.__xsDataCrystal != None:
                xsDataIndexingInput.setCrystal(self.__xsDataCrystal)
            self.__edPluginControlIndexingLabelit.setDataInput(xsDataIndexingInput)
            self.__edPluginControlIndexingLabelit.executeSynchronous()


    def doSuccessEvaluationIndexingLABELIT(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessEvaluationIndexingLABELIT")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessEvaluationIndexingLABELIT")
        # Retrieve status messages (if any)
        if self.__edPluginExecEvaluationIndexingLABELIT.hasDataOutput("statusMessageIndexing"):
            self.addStatusMessage("Labelit: " + self.__edPluginExecEvaluationIndexingLABELIT.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexingSuccess = self.__edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            xsDataIndexingResult = self.__edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingResult")[0]
            self.__xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            # Then start the integration of the reference images
            self.indexingToIntegration()
        else:
            EDVerbose.screen("Indexing with LABELIT failed!")
            self.setFailure()


    def indexingToIntegration(self, _edPlugin=None):
        # Integrate the reference images 
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self.__xsDataResultCharacterisation.getDataCollection())
        xsDataIndexingResult = self.__xsDataResultCharacterisation.getIndexingResult()
        xsDataExperimentalConditionRefinded = xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined()
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataExperimentalConditionRefinded)
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self.__edPluginControlIntegration.setDataInput(xsDataIntegrationInput)
        self.__edPluginControlIntegration.executeSynchronous()


    def doFailureEvaluationIndexingMOSFLM(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureEvaluationIndexing")
        strWarningMessage = "Execution of indexing evaluation plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)


    def doFailureEvaluationIndexingLABELIT(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureEvaluationIndexing")
        strWarningMessage = "Execution of indexing evaluation plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)


    def doSuccessGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessGeneratePrediction")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessGeneratePrediction")
        xsDataGeneratePredictionResult = _edPlugin.getDataOutput()
        xsDataIndexingResult = self.__xsDataResultCharacterisation.getIndexingResult()
        xsDataIndexingResult.setPredictionResult(xsDataGeneratePredictionResult)


    def doFailureGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureGeneratePrediction")
        strWarningMessage = "Execution of generate prediction plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)
        #self.addComment("warning: no prediction images")


    def doSuccessIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_2.doSuccessIntegration")
        self.addStatusMessage("Integration successful.")
        xsDataIntegrationOutput = self.__edPluginControlIntegration.getDataOutput()
        self.__xsDataResultCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        # Integration short summary
        if self.__edPluginControlIntegration.hasDataOutput("integrationShortSummary"):
            self.__strCharacterisationShortSummary += self.__edPluginControlIntegration.getDataOutput("integrationShortSummary")[0].getValue()
        #EDVerbose.DEBUG( self.__xsDataExperimentCharacterisation.marshal() )
        if self.__bDoStrategyCalculation:
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
            self.__edPluginControlStrategy.setDataInput(xsDataInputStrategy)
            self.__edPluginControlStrategy.executeSynchronous()



    def doFailureIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureIntegration")
        strErrorMessage = "Execution of integration plugin failed."
        self.addStatusMessage("Integration FAILURE.")
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        #self.addComment("integration failure")
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)
        self.generateExecutiveSummary(self)
        self.setFailure()
        if self.__strStatusMessage != None:
            self.setDataOutput(XSDataString(self.__strStatusMessage), "statusMessage")
            self.writeDataOutput()


    def doSuccessStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doSuccessStrategy")
        self.retrieveSuccessMessages(self.__edPluginControlStrategy, "EDPluginControlCharacterisationv1_2.doSuccessStrategy")
        xsDataStrategyResult = self.__edPluginControlStrategy.getDataOutput()
        self.__xsDataResultCharacterisation.setStrategyResult(xsDataStrategyResult)
        if self.__edPluginControlStrategy.hasDataOutput("strategyShortSummary"):
            self.__strCharacterisationShortSummary += self.__edPluginControlStrategy.getDataOutput("strategyShortSummary")[0].getValue()
        self.addStatusMessage("Strategy calculation successful.")


    def doFailureStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.doFailureStrategy")
        strErrorMessage = "Execution of strategy plugin failed."
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        if self.__xsDataResultCharacterisation is not None:
            self.setDataOutput(self.__xsDataResultCharacterisation)
        self.addStatusMessage("Strategy calculation FAILURE.")
        self.generateExecutiveSummary(self)
        if self.__strStatusMessage != None:
            self.setDataOutput(XSDataString(self.__strStatusMessage), "statusMessage")
            self.writeDataOutput()
        self.setFailure()


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_2.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of characterisation:")
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
        if self.__edPluginControlIndexingIndicators is not None:
            self.appendExecutiveSummary(self.__edPluginControlIndexingIndicators, "")
        if self.__edPluginControlIndexingLabelit is not None:
            self.appendExecutiveSummary(self.__edPluginControlIndexingLabelit, "")
        if self.__edPluginControlIntegration is not None:
            self.appendExecutiveSummary(self.__edPluginControlIntegration, "")
        if self.__edPluginControlStrategy is not None:
            self.appendExecutiveSummary(self.__edPluginControlStrategy, "")
        self.addExecutiveSummarySeparator()
        if self.__strCharacterisationShortSummary is not None:
            self.addExecutiveSummaryLine("Characterisation short summary:")
            self.addExecutiveSummaryLine("")
            if self.__strStatusMessage != None:
                for strLine in self.__strStatusMessage.split(". "):
                    if strLine.endswith("."):
                        self.addExecutiveSummaryLine(strLine)
                    else:
                        self.addExecutiveSummaryLine(strLine+".")
            self.addExecutiveSummaryLine("")
            for strLine in self.__strCharacterisationShortSummary.split("\n"):
                if strLine != "\n":
                    self.addExecutiveSummaryLine(strLine)
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation error and warning messages: ")
        self.addExecutiveSummarySeparator()


    def getPluginStrategyName(self):
        return self.__strPluginControlStrategy


    def addStatusMessage(self, _strStatusMessage):
        if self.__strStatusMessage != "":
            self.__strStatusMessage += " "
        self.__strStatusMessage += _strStatusMessage

        
    def doStrategyCalculation(self, _bValue):
        self.__bDoStrategyCalculation = _bValue

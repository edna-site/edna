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
from XSDataMXv1 import XSDataInputControlXDSGenerateBackgroundImage

class EDPluginControlCharacterisationv1_3(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisation)
        self._strPluginControlIndexingIndicators = "EDPluginControlIndexingIndicatorsv10"
        self._strPluginControlIndexingLabelit = "EDPluginControlIndexingLabelitv10"
        self._strPluginExecEvaluationIndexing = "EDPluginExecEvaluationIndexingv10"
        self._strPluginControlGeneratePrediction = "EDPluginControlGeneratePredictionv10"
        self._strPluginControlIntegration = "EDPluginControlIntegrationv10"
        self._strPluginControlXDSGenerateBackgroundImage = "EDPluginControlXDSGenerateBackgroundImagev1_0"
        self._strPluginControlStrategy = "EDPluginControlStrategyv1_2"
        self._edPluginControlIndexingIndicators = None
        self._edPluginControlIndexingLabelit = None
        self._edPluginExecEvaluationIndexingMOSFLM = None
        self._edPluginExecEvaluationIndexingLABELIT = None
        self._edPluginControlGeneratePrediction = None
        self._edPluginControlIntegration = None
        self._edPluginControlXDSGenerateBackgroundImage = None
        self._edPluginControlStrategy = None
        self._xsDataCollection = None
        self._xsDataResultCharacterisation = None
        self._xsDataIndexingResultMOSFLM = None
        self._xsDataCrystal = None
        self._strCharacterisationShortSummary = ""
        self._strStatusMessage = ""
        self._xsDataFileXdsBackgroundImage = None
        self._bDoStrategyCalculation = True


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan(), "diffractionPlan")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.preProcess")
        # Load the plugins
        self._edPluginControlIndexingIndicators = self.loadPlugin(self._strPluginControlIndexingIndicators, \
                                                                   "Indexing")
        self._edPluginControlIndexingLabelit = self.loadPlugin(self._strPluginControlIndexingLabelit, \
                                                                   "IndexingLabelit")
        self._edPluginExecEvaluationIndexingMOSFLM = self.loadPlugin(self._strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionMOSFLM")
        self._edPluginExecEvaluationIndexingLABELIT = self.loadPlugin(self._strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionLABELIT")
        self._edPluginControlGeneratePrediction = self.loadPlugin(self._strPluginControlGeneratePrediction, \
                                                                   "GeneratePrediction")
        self._edPluginControlIntegration = self.loadPlugin(self._strPluginControlIntegration, \
                                                            "Integration")
        self._edPluginControlXDSGenerateBackgroundImage = self.loadPlugin(self._strPluginControlXDSGenerateBackgroundImage, \
                                                            "ControlXDSGenerateBackgroundImage")
        self._edPluginControlStrategy = self.loadPlugin(self._strPluginControlStrategy, \
                                                         "Strategy")
        if (self._edPluginControlIndexingIndicators is not None):
            EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.preProcess: " + self._strPluginControlIndexingIndicators + " Found... setting Data Input")
            # create Data Input for indexing
            xsDataInputCharacterisation = self.getDataInput()
            self._xsDataCollection = xsDataInputCharacterisation.getDataCollection()
            xsDataCrystal = None
            xsDataSubWedgeList = self._xsDataCollection.getSubWedge()
            if ((xsDataSubWedgeList is None) or (xsDataSubWedgeList == [])):
                strError = "EDPluginControlCharacterisationv1_3.preProcess: No subwedges in input data."
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
                        self.addErrorMessage("EDPluginControlCharacterisationv1_3.preProcess ERROR: " + strErrorMessage)
                        #self.addComment(strErrorMessage)
                        self.setFailure()

                xsDataDiffractionPlan = self._xsDataCollection.getDiffractionPlan()
                xsDataStringForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup()
                if (xsDataStringForcedSpaceGroup is not None):
                    self._xsDataCrystal = XSDataCrystal()
                    xsDataSpaceGroup = XSDataSpaceGroup()
                    xsDataSpaceGroup.setName(xsDataStringForcedSpaceGroup)
                    self._xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)

                self._edPluginControlIndexingIndicators.setDataInput(self._xsDataCollection, "dataCollection")
                if self._xsDataCrystal is not None:
                    self._edPluginControlIndexingIndicators.setDataInput(self._xsDataCrystal, "crystal")

                # Populate characterisation object
                self._xsDataResultCharacterisation = XSDataResultCharacterisation()
                self._xsDataResultCharacterisation.setDataCollection(XSDataCollection.parseString(self._xsDataCollection.marshal()))


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.process")
        self._edPluginControlIndexingIndicators.connectSUCCESS(self.doSuccessIndexingIndicators)
        self._edPluginControlIndexingIndicators.connectFAILURE(self.doFailureIndexingIndicators)
        self._edPluginControlIndexingLabelit.connectSUCCESS(self.doSuccessIndexingLabelit)
        self._edPluginControlIndexingLabelit.connectFAILURE(self.doFailureIndexingLabelit)
        self._edPluginExecEvaluationIndexingMOSFLM.connectSUCCESS(self.doSuccessEvaluationIndexingMOSFLM)
        self._edPluginExecEvaluationIndexingMOSFLM.connectFAILURE(self.doFailureEvaluationIndexingMOSFLM)
        self._edPluginExecEvaluationIndexingLABELIT.connectSUCCESS(self.doSuccessEvaluationIndexingLABELIT)
        self._edPluginExecEvaluationIndexingLABELIT.connectFAILURE(self.doFailureEvaluationIndexingLABELIT)
        self._edPluginControlGeneratePrediction.connectSUCCESS(self.doSuccessGeneratePrediction)
        self._edPluginControlGeneratePrediction.connectFAILURE(self.doFailureGeneratePrediction)
        self._edPluginControlIntegration.connectSUCCESS(self.doSuccessIntegration)
        self._edPluginControlIntegration.connectFAILURE(self.doFailureIntegration)
        self._edPluginControlXDSGenerateBackgroundImage.connectSUCCESS(self.doSuccessXDSGenerateBackgroundImage)
        self._edPluginControlXDSGenerateBackgroundImage.connectFAILURE(self.doFailureXDSGenerateBackgroundImage)
        self._edPluginControlStrategy.connectSUCCESS(self.doSuccessStrategy)
        self._edPluginControlStrategy.connectFAILURE(self.doFailureStrategy)
        self.executePluginSynchronous(self._edPluginControlIndexingIndicators)


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.finallyProcess")
        if self._edPluginControlGeneratePrediction.isRunning():
            self._edPluginControlGeneratePrediction.synchronize()
        if self._strStatusMessage != None:
            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
            self._xsDataResultCharacterisation.setStatusMessage(XSDataString(self._strStatusMessage))
        if self._strCharacterisationShortSummary != None:
            self.setDataOutput(XSDataString(self._strCharacterisationShortSummary), "shortSummary")
            self._xsDataResultCharacterisation.setShortSummary(XSDataString(self._strCharacterisationShortSummary))
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)


    def doSuccessIndexingIndicators(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessIndexingIndicators")
        #self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessIndexingIndicators")
        if self._edPluginControlIndexingIndicators.hasDataOutput("indexingResult"):
            xsDataIndexingResult = self._edPluginControlIndexingIndicators.getDataOutput("indexingResult")[0]
            #self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            self._edPluginExecEvaluationIndexingMOSFLM.setDataInput(xsDataIndexingResult, "indexingResult")
        if self._edPluginControlIndexingIndicators.hasDataOutput("imageQualityIndicators"):
            listXSDataImageQualityIndicators = self._edPluginControlIndexingIndicators.getDataOutput("imageQualityIndicators")
            for xsDataImageQualityIndicators in listXSDataImageQualityIndicators:
                self._xsDataResultCharacterisation.addImageQualityIndicators(xsDataImageQualityIndicators)
                self._edPluginExecEvaluationIndexingMOSFLM.setDataInput(xsDataImageQualityIndicators, "imageQualityIndicators")
        if self._edPluginControlIndexingIndicators.hasDataOutput("indicatorsShortSummary"):
            self._strCharacterisationShortSummary += self._edPluginControlIndexingIndicators.getDataOutput("indicatorsShortSummary")[0].getValue()
        self.executePluginSynchronous(self._edPluginExecEvaluationIndexingMOSFLM)


    def doFailureIndexingIndicators(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureIndexingIndicators")
        strErrorMessage = "Execution of Indexing and Indicators plugin failed. Execution of characterisation aborted."
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        self.setFailure()
        if self._strStatusMessage != None:
            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
            self.writeDataOutput()


#    def doSuccessIndexingLabelit(self, _edPlugin=None):
#        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessIndexingLabelit")
#        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessIndexingLabelit")
#        # Retrieve the indexing result
#        xsDataIndexingResult = self._edPluginControlIndexingLabelit.getDataOutput()
#        self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
#        if self._edPluginControlIndexingLabelit.hasDataOutput("indexingShortSummary"):
#            self._strCharacterisationShortSummary += self._edPluginControlIndexingLabelit.getDataOutput("indexingShortSummary")[0].getValue()
#        # Then start the integration of the reference images
#        self.indexingToIntegration()


    def doSuccessIndexingLabelit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessIndexingLabelit")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessIndexingLabelit")
        if self._edPluginControlIndexingLabelit.hasDataOutput("indexingShortSummary"):
            self._strCharacterisationShortSummary += self._edPluginControlIndexingLabelit.getDataOutput("indexingShortSummary")[0].getValue()
        # Check the indexing results
        xsDataIndexingResult = self._edPluginControlIndexingLabelit.getDataOutput()
        self._edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataIndexingResult, "indexingResult")
        xsDataImageQualityIndicators = self._xsDataResultCharacterisation.getImageQualityIndicators()[0]
        self._edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataImageQualityIndicators, "imageQualityIndicators")
        self.executePluginSynchronous(self._edPluginExecEvaluationIndexingLABELIT)


    def doFailureIndexingLabelit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureIndexingLabelit")
        self.addStatusMessage("Labelit: Indexing FAILURE.")
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        if self._xsDataIndexingResultMOSFLM == None:
            strErrorMessage = "Execution of indexing with both MOSFLM and Labelit failed. Execution of characterisation aborted."
            EDVerbose.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.generateExecutiveSummary(self)
            self.setFailure()
            if self._strStatusMessage != None:
                self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
                self.writeDataOutput()
        else:
            # Use the MOSFLM indexing results - even if it's P1
            self._xsDataResultCharacterisation.setIndexingResult(self._xsDataIndexingResultMOSFLM)
            xsDataCollection = self._xsDataResultCharacterisation.getDataCollection()
            xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
            xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
            xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(self._xsDataIndexingResultMOSFLM.getSelectedSolution().marshal()))
            self._edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
            if self._edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                self._strCharacterisationShortSummary += self._edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
            # Start the generation of prediction images - we synchronize in the post-process
            self._edPluginControlGeneratePrediction.execute()
            # Then start the integration of the reference images
            self.indexingToIntegration()



    def doSuccessEvaluationIndexingMOSFLM(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessEvaluationIndexingMOSFLM")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessEvaluationIndexing")
        # Retrieve status messages (if any)
        if self._edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageImageQualityIndicators"):
            self.addStatusMessage(self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageImageQualityIndicators")[0].getValue())
        if self._edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageIndexing"):
            self.addStatusMessage("MOSFLM: " + self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexWithLabelit = False
        bIndexingSuccess = self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            xsDataIndexingResult = self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingResult")[0]
            self._xsDataIndexingResultMOSFLM = xsDataIndexingResult
            # Check if space group is P1 - if yes run Labelit indexing
            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
            xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
            strSpaceGroupName = xsDataSpaceGroup.getName().getValue().upper()
            # Check if MOSFLM has indexed in P1
            if strSpaceGroupName == "P1":
                # Check if the user maybe asked for P1!
                bIndexWithLabelit = True
                if self._xsDataCollection.getDiffractionPlan() is not None:
                    if self._xsDataCollection.getDiffractionPlan().getForcedSpaceGroup() is not None:
                        if self._xsDataCollection.getDiffractionPlan().getForcedSpaceGroup().getValue().upper() == "P1":
                            EDVerbose.screen("P1 space forced by diffraction plan")
                            bIndexWithLabelit = False
            if bIndexWithLabelit:
                EDVerbose.screen("P1 space group choosed - reindexing with Labelit")
            else:
                EDVerbose.screen("MOSFLM indexing successful!")
                if self._edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                    self._strCharacterisationShortSummary += self._edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
                # Generate prediction images
                xsDataCollection = self._xsDataResultCharacterisation.getDataCollection()
                self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
                xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
                xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
                xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataIndexingResult.getSelectedSolution().marshal()))
                self._edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
                # Start the generation of prediction images - we synchronize in the post-process
                self._edPluginControlGeneratePrediction.execute()
                # Then start the integration of the reference images
                self.indexingToIntegration()
        else:
            EDVerbose.screen("Indexing with MOSFLM failed!")
            bIndexWithLabelit = True
        if bIndexWithLabelit:
            # Execute Labelit indexing
            EDVerbose.screen("Now trying to index with Labelit - please be patient...")
            xsDataIndexingInput = XSDataIndexingInput()
            xsDataSubWedgeList = self._xsDataCollection.getSubWedge()
            xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()
            xsDataIndexingInput.setDataCollection(self._xsDataCollection)
            xsDataIndexingInput.setExperimentalCondition(xsDataExperimentalCondition)
            if self._xsDataCrystal != None:
                xsDataIndexingInput.setCrystal(self._xsDataCrystal)
            self._edPluginControlIndexingLabelit.setDataInput(xsDataIndexingInput)
            self.executePluginSynchronous(self._edPluginControlIndexingLabelit)


    def doSuccessEvaluationIndexingLABELIT(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessEvaluationIndexingLABELIT")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessEvaluationIndexingLABELIT")
        # Retrieve status messages (if any)
        if self._edPluginExecEvaluationIndexingLABELIT.hasDataOutput("statusMessageIndexing"):
            self.addStatusMessage("Labelit: " + self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexingSuccess = self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            xsDataIndexingResult = self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingResult")[0]
            self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            # Then start the integration of the reference images
            self.indexingToIntegration()
        else:
            EDVerbose.screen("Indexing with LABELIT failed!")
            self.setFailure()


    def indexingToIntegration(self, _edPlugin=None):
        # Create the XDS background image
        xsDataInputControlXDSGenerateBackgroundImage = XSDataInputControlXDSGenerateBackgroundImage()
        xsDataInputControlXDSGenerateBackgroundImage.setDataCollection(self._xsDataCollection)
        self._edPluginControlXDSGenerateBackgroundImage.setDataInput(xsDataInputControlXDSGenerateBackgroundImage)
        self._edPluginControlXDSGenerateBackgroundImage.execute()
        # Integrate the reference images 
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self._xsDataResultCharacterisation.getDataCollection())
        xsDataIndexingResult = self._xsDataResultCharacterisation.getIndexingResult()
        xsDataExperimentalConditionRefinded = xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined()
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataExperimentalConditionRefinded)
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self._edPluginControlIntegration.setDataInput(xsDataIntegrationInput)
        self.executePluginSynchronous(self._edPluginControlIntegration)


    def doFailureEvaluationIndexingMOSFLM(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureEvaluationIndexing")
        strWarningMessage = "Execution of indexing evaluation plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)


    def doFailureEvaluationIndexingLABELIT(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureEvaluationIndexing")
        strWarningMessage = "Execution of indexing evaluation plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)


    def doSuccessGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessGeneratePrediction")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessGeneratePrediction")
        xsDataGeneratePredictionResult = _edPlugin.getDataOutput()
        xsDataIndexingResult = self._xsDataResultCharacterisation.getIndexingResult()
        xsDataIndexingResult.setPredictionResult(xsDataGeneratePredictionResult)


    def doFailureGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureGeneratePrediction")
        strWarningMessage = "Execution of generate prediction plugin failed."
        EDVerbose.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        #self.addComment("warning: no prediction images")


    def doSuccessIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessIntegration")
        # Wait for XDS plugin if necessary
        self._edPluginControlXDSGenerateBackgroundImage.synchronize()
        self.addStatusMessage("Integration successful.")
        xsDataIntegrationOutput = self._edPluginControlIntegration.getDataOutput()
        self._xsDataResultCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        # Integration short summary
        if self._edPluginControlIntegration.hasDataOutput("integrationShortSummary"):
            self._strCharacterisationShortSummary += self._edPluginControlIntegration.getDataOutput("integrationShortSummary")[0].getValue()
        #EDVerbose.DEBUG( self._xsDataExperimentCharacterisation.marshal() )
        if self._bDoStrategyCalculation:
            xsDataInputStrategy = XSDataInputStrategy()
            xsDataSolutionSelected = self._xsDataResultCharacterisation.getIndexingResult().getSelectedSolution()
            xsDataInputStrategy.setCrystalRefined(xsDataSolutionSelected.getCrystal())
            xsDataInputStrategy.setSample(self._xsDataResultCharacterisation.getDataCollection().getSample())
            xsDataIntegrationSubWedgeResultList = xsDataIntegrationOutput.getIntegrationSubWedgeResult()
            xsDataInputStrategy.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
            xsDataInputStrategy.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
            xsDataInputStrategy.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())
            xsDataInputStrategy.setXdsBackgroundImage(self._xsDataFileXdsBackgroundImage)
            for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
                xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())
            xsDataInputStrategy.setDiffractionPlan(self._xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())
            self._edPluginControlStrategy.setDataInput(xsDataInputStrategy)
            self.executePluginSynchronous(self._edPluginControlStrategy)



    def doFailureIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureIntegration")
        strErrorMessage = "Execution of integration plugin failed."
        self.addStatusMessage("Integration FAILURE.")
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        #self.addComment("integration failure")
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        self.generateExecutiveSummary(self)
        self.setFailure()
        if self._strStatusMessage != None:
            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
            self.writeDataOutput()


    def doSuccessXDSGenerateBackgroundImage(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessXDSGenerateBackgroundImage")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_3.doSuccessXDSGenerateBackgroundImage")
        self._xsDataFileXdsBackgroundImage = self._edPluginControlXDSGenerateBackgroundImage.getDataOutput().getXdsBackgroundImage()


    def doFailureXDSGenerateBackgroundImage(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureXDSGenerateBackgroundImage")


    def doSuccessStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doSuccessStrategy")
        self.retrieveSuccessMessages(self._edPluginControlStrategy, "EDPluginControlCharacterisationv1_3.doSuccessStrategy")
        xsDataStrategyResult = self._edPluginControlStrategy.getDataOutput()
        self._xsDataResultCharacterisation.setStrategyResult(xsDataStrategyResult)
        if self._edPluginControlStrategy.hasDataOutput("strategyShortSummary"):
            self._strCharacterisationShortSummary += self._edPluginControlStrategy.getDataOutput("strategyShortSummary")[0].getValue()
        self.addStatusMessage("Strategy calculation successful.")


    def doFailureStrategy(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.doFailureStrategy")
        strErrorMessage = "Execution of strategy plugin failed."
        EDVerbose.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        self.addStatusMessage("Strategy calculation FAILURE.")
        self.generateExecutiveSummary(self)
        if self._strStatusMessage != None:
            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
            self.writeDataOutput()
        self.setFailure()


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlCharacterisationv1_3.generateExecutiveSummary")
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
        if self._edPluginControlIndexingIndicators is not None:
            self.appendExecutiveSummary(self._edPluginControlIndexingIndicators, "")
        if self._edPluginControlIndexingLabelit is not None:
            self.appendExecutiveSummary(self._edPluginControlIndexingLabelit, "")
        if self._edPluginControlIntegration is not None:
            self.appendExecutiveSummary(self._edPluginControlIntegration, "")
        if self._edPluginControlStrategy is not None:
            self.appendExecutiveSummary(self._edPluginControlStrategy, "")
        self.addExecutiveSummarySeparator()
        if self._strCharacterisationShortSummary is not None:
            self.addExecutiveSummaryLine("Characterisation short summary:")
            self.addExecutiveSummaryLine("")
            if self._strStatusMessage != None:
                for strLine in self._strStatusMessage.split(". "):
                    if strLine.endswith("."):
                        self.addExecutiveSummaryLine(strLine)
                    else:
                        self.addExecutiveSummaryLine(strLine + ".")
            self.addExecutiveSummaryLine("")
            for strLine in self._strCharacterisationShortSummary.split("\n"):
                if strLine != "\n":
                    self.addExecutiveSummaryLine(strLine)
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation error and warning messages: ")
        self.addExecutiveSummarySeparator()


    def getPluginStrategyName(self):
        return self._strPluginControlStrategy


    def addStatusMessage(self, _strStatusMessage):
        if self._strStatusMessage != "":
            self._strStatusMessage += " "
        self._strStatusMessage += _strStatusMessage
        
    def doStrategyCalculation(self, _bValue):
        self._bDoStrategyCalculation = _bValue

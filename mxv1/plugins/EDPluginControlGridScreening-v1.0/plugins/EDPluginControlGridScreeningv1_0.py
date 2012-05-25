#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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

import os

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger


from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataInputStrategy
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataInputControlImageQualityIndicators



from XSDataGridScreeningv1_0 import XSDataInputGridScreening
from XSDataGridScreeningv1_0 import XSDataResultGridScreening
from XSDataGridScreeningv1_0 import XSDataGridScreeningFileNameParameters
from XSDataGridScreeningv1_0 import XSDataGridScreeningResultIntegration

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_3")
from XSDataISPyBv1_3 import XSDataInputStoreImageQualityIndicators
from XSDataISPyBv1_3 import XSDataISPyBImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataInputMtz2Various


class EDPluginControlGridScreeningv1_0(EDPluginControl):
    """
    This plugin is a "light-weight" characterisation to be used for processing
    images from grid scans.
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputGridScreening)
        self.strControlReadImageHeaderPluginName = "EDPluginControlReadImageHeaderv10"
        self.edPluginControlReadImageHeader = None
        self.strControlledIndicatorsPluginName = "EDPluginControlImageQualityIndicatorsv1_1"
        self.edPluginControlIndicators = None
        self.strISPyBStoreImageQualityIndicatorsPluginName = "EDPluginISPyBStoreImageQualityIndicatorsv1_3"
        self.edPluginISPyBStoreImageQualityIndicators = None
        self.strIndexingMOSFLMPluginName = "EDPluginMOSFLMIndexingv10"
        self.edPluginMOSFLMIndexing = None
        self.strPluginControlIntegration = "EDPluginControlIntegrationv10"
        self.edPluginControlIntegration = None
        self.strPluginControlStrategy = "EDPluginControlStrategyv1_2"
        self.edPluginControlStrategy = None
        self.strPluginExecMtz2Various = "EDPluginExecMtz2Variousv1_0"
        self.edPluginExecMtz2Various = None
        self.strImageFile = None
        self.xsDataIndexingResultMOSFLM = None
        self.xsDataCrystal = None
        self.strCharacterisationShortSummary = ""
        self.strStatusMessage = ""
        self.xsDataDiffractionPlan = None 
        self.xsDataCollection = None
        self.xsDataIndexingResult = None
        self.xsDataStrategyResult = None
        self.xsDataImageQualityIndicators = None
        self.bStoreImageQualityIndicatorsInISPyB = False
        self.bDoOnlyImageQualityIndicators = False
        self.bDoOnlyIntegrationWithXMLOutput = False
        self.iImageQualityIndicatorsId = None
        self.xsDataGridScreeningResultIntegration = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlGridScreeningv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getImageFile(), "imageFile")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlGridScreeningv1_0.preProcess")
        # Load the plugins
        self.edPluginControlReadImageHeader = self.loadPlugin(self.strControlReadImageHeaderPluginName, \
                                                                   "ReadImageHeader")
        self.edPluginControlIndicators = self.loadPlugin(self.strControlledIndicatorsPluginName, \
                                                                   "ControlIndicators")
        self.edPluginMOSFLMIndexing = self.loadPlugin(self.strIndexingMOSFLMPluginName, \
                                                                   "IndexingMOSFLM")
        self.edPluginControlIntegration = self.loadPlugin(self.strPluginControlIntegration, \
                                                            "Integration")
        self.edPluginControlStrategy = self.loadPlugin(self.strPluginControlStrategy, \
                                                         "Strategy")
        self.edPluginExecMtz2Various = self.loadPlugin(self.strPluginExecMtz2Various, \
                                                         "Mtz2Various")
        # Input data
        self.strImageFile = self.getDataInput().getImageFile().getPath().getValue()
        self.xsDataGridScreeningFileNameParameters = self.getFileNameParameters(self.strImageFile)
        self.xsDataDiffractionPlan = self.getDataInput().getDiffractionPlan()
        if self.xsDataDiffractionPlan is None:
            self.xsDataDiffractionPlan = XSDataDiffractionPlan()
        if self.xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is None:
            # Default max esposure time: 10000s
            self.xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(10000))
        self.xsDataDiffractionPlan.setEstimateRadiationDamage(XSDataBoolean(False))
        # Image quality indicators
        if self.getDataInput().getStoreImageQualityIndicatorsInISPyB():
            self.bStoreImageQualityIndicatorsInISPyB = self.getDataInput().getStoreImageQualityIndicatorsInISPyB().getValue()
        if self.getDataInput().getDoOnlyImageQualityIndicators():
            self.bDoOnlyImageQualityIndicators = self.getDataInput().getDoOnlyImageQualityIndicators().getValue()
        if self.getDataInput().getDoOnlyIntegrationWithXMLOutput():
            self.bDoOnlyIntegrationWithXMLOutput = self.getDataInput().getDoOnlyIntegrationWithXMLOutput().getValue()
        if self.bStoreImageQualityIndicatorsInISPyB:
            self.edPluginISPyBStoreImageQualityIndicators = self.loadPlugin(self.strISPyBStoreImageQualityIndicatorsPluginName, \
                                                         "ISPyBStoreImageQualityIndicators")
        


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlGridScreeningv1_0.process")
        xsDataInputReadImageHeader = XSDataInputReadImageHeader()
        xsDataInputReadImageHeader.setImage(image=XSDataFile(path=XSDataString(self.strImageFile)))
        self.edPluginControlReadImageHeader.setDataInput(xsDataInputReadImageHeader)
        self.edPluginControlReadImageHeader.connectSUCCESS(self.doSuccessReadImageHeader)
        self.edPluginControlReadImageHeader.connectFAILURE(self.doFailureReadImageHeader)
        self.executePluginSynchronous(self.edPluginControlReadImageHeader)


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        self.DEBUG("EDPluginControlGridScreeningv1_0.finallyProcess")
        # Synchronise if necessary
        if self.edPluginISPyBStoreImageQualityIndicators is not None:
            self.edPluginISPyBStoreImageQualityIndicators.synchronize()
        # Build up the output object
        strComment = ""
        xsDataResultGridScreening = XSDataResultGridScreening()
        if self.xsDataGridScreeningFileNameParameters is not None:
            xsDataResultGridScreening.setFileNameParameters(self.xsDataGridScreeningFileNameParameters)
        if self.xsDataImageQualityIndicators is None:
            strComment = "No image quality indicators"
        else:
            xsDataResultGridScreening.setImageQualityIndicators(self.xsDataImageQualityIndicators)
            if self.xsDataImageQualityIndicators.getIceRings().getValue() > 1:
                strComment = "Ice rings detected"
        if self.xsDataIndexingResult is None:
            if strComment == "":
                strComment = "No indexing result"
            else:
                strComment += ", no indexing result"
        else:
            xsDataSelectedSolution = self.xsDataIndexingResult.getSelectedSolution()
            xsDataResultGridScreening.setMosaicity(xsDataSelectedSolution.getCrystal().getMosaicity())
            if self.xsDataStrategyResult is None:
                if strComment == "":
                    strComment = "No strategy result"
                else:
                    strComment += ", no strategy result"
            else:
                xsDataCollectionPlan = self.xsDataStrategyResult.getCollectionPlan()[0]
                xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                xsDataResultGridScreening.setRankingResolution(xsDataStrategySummary.getRankingResolution())
        xsDataResultGridScreening.setResultIntegration(self.xsDataGridScreeningResultIntegration)
        xsDataResultGridScreening.setComment(XSDataString(strComment))
        if self.iImageQualityIndicatorsId is not None:
            xsDataResultGridScreening.setImageQualityIndicatorsId(XSDataInteger(self.iImageQualityIndicatorsId))
        #print xsDataResultGridScreening.marshal()
        self.setDataOutput(xsDataResultGridScreening)



    def doSuccessReadImageHeader(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessReadImageHeader")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doSuccessReadImageHeader")
        xsDataResultReadImageHeader = self.edPluginControlReadImageHeader.getDataOutput()
        if xsDataResultReadImageHeader is not None:
            xsDataSubWedge = xsDataResultReadImageHeader.getSubWedge()
            self.xsDataCollection = XSDataCollection()
            self.xsDataCollection.addSubWedge(xsDataSubWedge)
            self.xsDataCollection.setDiffractionPlan(self.xsDataDiffractionPlan)
            if not self.bDoOnlyIntegrationWithXMLOutput:
                xsDataInputControlImageQualityIndicators = XSDataInputControlImageQualityIndicators()
                xsDataInputControlImageQualityIndicators.addImage(XSDataImage(path=XSDataString(self.strImageFile)))
                self.edPluginControlIndicators.setDataInput(xsDataInputControlImageQualityIndicators)
                self.edPluginControlIndicators.connectSUCCESS(self.doSuccessIndicators)
                self.edPluginControlIndicators.connectFAILURE(self.doFailureIndicators)
                self.executePluginSynchronous(self.edPluginControlIndicators)
            else:
                xsDataIndexingInput = XSDataIndexingInput()
                xsDataIndexingInput.setDataCollection(self.xsDataCollection)
                from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
                xsDataMOSFLMIndexingInput = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(xsDataIndexingInput)
                self.edPluginMOSFLMIndexing.connectSUCCESS(self.doSuccessIndexingMOSFLM)
                self.edPluginMOSFLMIndexing.connectFAILURE(self.doFailureIndexingMOSFLM)
                self.edPluginMOSFLMIndexing.setDataInput(xsDataMOSFLMIndexingInput)
                self.edPluginMOSFLMIndexing.executeSynchronous()


    def doFailureReadImageHeader(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureReadImageHeader")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doSuccessReadImageHeader")
    
    
    
    def doSuccessIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessIndicators")
        #self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doSuccessIndexingIndicators")
        if self.edPluginControlIndicators.hasDataOutput():
            self.xsDataImageQualityIndicators = self.edPluginControlIndicators.getDataOutput().getImageQualityIndicators()[0]
            # Store results in ISPyB if requested
            if self.bStoreImageQualityIndicatorsInISPyB:
                xsDataInputStoreImageQualityIndicators = XSDataInputStoreImageQualityIndicators()
                xsDataISPyBImageQualityIndicators = XSDataISPyBImageQualityIndicators.parseString(self.xsDataImageQualityIndicators.marshal())
                xsDataInputStoreImageQualityIndicators.setImageQualityIndicators(xsDataISPyBImageQualityIndicators)
                self.edPluginISPyBStoreImageQualityIndicators.setDataInput(xsDataInputStoreImageQualityIndicators)
                self.edPluginISPyBStoreImageQualityIndicators.connectSUCCESS(self.doSuccessISPyBStoreImageQualityIndicators)
                self.edPluginISPyBStoreImageQualityIndicators.connectFAILURE(self.doFailureISPyBStoreImageQualityIndicators)
                self.edPluginISPyBStoreImageQualityIndicators.execute()
            # Continue only if requested
            if not self.bDoOnlyImageQualityIndicators:
                xsDataIndexingInput = XSDataIndexingInput()
                xsDataIndexingInput.setDataCollection(self.xsDataCollection)
                from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
                xsDataMOSFLMIndexingInput = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(xsDataIndexingInput)
                self.edPluginMOSFLMIndexing.connectSUCCESS(self.doSuccessIndexingMOSFLM)
                self.edPluginMOSFLMIndexing.connectFAILURE(self.doFailureIndexingMOSFLM)
                self.edPluginMOSFLMIndexing.setDataInput(xsDataMOSFLMIndexingInput)
                self.edPluginMOSFLMIndexing.executeSynchronous()


    def doFailureIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureIndicators")
        strErrorMessage = "Execution of Indexing and Indicators plugin failed. Execution of characterisation aborted."
        self.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)


    def doSuccessISPyBStoreImageQualityIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessISPyBStoreImageQualityIndicators")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doSuccessISPyBStoreImageQualityIndicators")
        self.iImageQualityIndicatorsId = self.edPluginISPyBStoreImageQualityIndicators.getDataOutput().getImageQualityIndicatorsId().getValue()
        if self.iImageQualityIndicatorsId is None:
            self.WARNING("Image quality indicators result not stored in ISPyB!")

    def doFailureISPyBStoreImageQualityIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureISPyBStoreImageQualityIndicators")
        strErrorMessage = "Execution of store ISPyB image quality indicators plugin failed."
        self.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)



    def doSuccessIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessIndexingMOSFLM")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doIntegrationToStrategyTransition")
        xsDataMOSFLMIndexingOutput = self.edPluginMOSFLMIndexing.getDataOutput()
        xsDataExperimentalConditionRefined = None
        if self.hasDataInput("refinedExperimentalCondition"):
            xsDataExperimentalConditionRefined = self.getDataInput("refinedExperimentalCondition")[0]
        else:
            # Use the experimental condition from the xsDataCollection
            xsDataExperimentalConditionRefined = self.xsDataCollection.getSubWedge()[0].getExperimentalCondition()
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        self.xsDataIndexingResult = EDHandlerXSDataMOSFLMv10.generateXSDataIndexingResult(xsDataMOSFLMIndexingOutput, xsDataExperimentalConditionRefined)
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self.xsDataCollection)
        xsDataIntegrationInput.setExperimentalConditionRefined(self.xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined())
        xsDataIntegrationInput.setSelectedIndexingSolution(self.xsDataIndexingResult.getSelectedSolution())
        self.edPluginControlIntegration.connectSUCCESS(self.doSuccessIntegration)
        self.edPluginControlIntegration.connectFAILURE(self.doFailureIntegration)
        self.edPluginControlIntegration.setDataInput(xsDataIntegrationInput)
        self.executePluginSynchronous(self.edPluginControlIntegration)


    def doFailureIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureActionIndexing")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv1_1.doFailureActionIndexing")


    def doSuccessIntegration(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGridScreeningv1_0.doSuccessIntegration")
        self.addStatusMessage("Integration successful.")
        self.xsDataIntegrationOutput = self.edPluginControlIntegration.getDataOutput()
        # Integration short summary
        if self.edPluginControlIntegration.hasDataOutput("integrationShortSummary"):
            self.strCharacterisationShortSummary += self.edPluginControlIntegration.getDataOutput("integrationShortSummary")[0].getValue()
        #self.DEBUG( self.xsDataExperimentCharacterisation.marshal() )
        if self.bDoOnlyIntegrationWithXMLOutput:
            # Run mtz2various
            xsDataInputMtz2Various = XSDataInputMtz2Various()
            xsDataInputMtz2Various.setMtzfile(self.edPluginControlIntegration.getDataOutput().getIntegrationSubWedgeResult()[0].getGeneratedMTZFile())
            xsDataInputMtz2Various.addLabin(XSDataString("I=I"))
            xsDataInputMtz2Various.addLabin(XSDataString("SIGI=SIGI"))
            xsDataInputMtz2Various.setOutput(XSDataString("USER '(3I4,2F10.1)'"))
            self.edPluginExecMtz2Various.setDataInput(xsDataInputMtz2Various)
            self.edPluginExecMtz2Various.executeSynchronous()
            strHklFilePath = self.edPluginExecMtz2Various.getDataOutput().getHklfile().getPath().getValue()
            strIntegration = EDUtilsFile.readFile(strHklFilePath)
            # Output the result in XML format
            self.xsDataGridScreeningResultIntegration = XSDataGridScreeningResultIntegration()
            self.xsDataGridScreeningResultIntegration.setFileName(os.path.basename(self.strImageFile))
            self.xsDataGridScreeningResultIntegration.setFileDirectory(os.path.dirname(self.strImageFile))
            self.xsDataGridScreeningResultIntegration.setIntegratedData(strIntegration)
        else:
            # We continue with the strategy calculation
            xsDataInputStrategy = XSDataInputStrategy()
            xsDataSolutionSelected = self.xsDataIndexingResult.getSelectedSolution()
            xsDataInputStrategy.setCrystalRefined(xsDataSolutionSelected.getCrystal())
            xsDataInputStrategy.setSample(self.xsDataCollection.getSample())
            xsDataIntegrationSubWedgeResultList = self.xsDataIntegrationOutput.getIntegrationSubWedgeResult()
            xsDataInputStrategy.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
            xsDataInputStrategy.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
            xsDataInputStrategy.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())
            for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
                xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())
            xsDataInputStrategy.setDiffractionPlan(self.xsDataDiffractionPlan)
            self.edPluginControlStrategy.connectSUCCESS(self.doSuccessStrategy)
            self.edPluginControlStrategy.connectFAILURE(self.doFailureStrategy)
            self.edPluginControlStrategy.setDataInput(xsDataInputStrategy)
            self.executePluginSynchronous(self.edPluginControlStrategy)



    def doFailureIntegration(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureIntegration")
        strErrorMessage = "Execution of integration plugin failed."
        self.addStatusMessage("Integration FAILURE.")
        self.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)


    def doSuccessStrategy(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doSuccessStrategy")
        self.retrieveSuccessMessages(self.edPluginControlStrategy, "EDPluginControlGridScreeningv1_0.doSuccessStrategy")
        self.xsDataStrategyResult = self.edPluginControlStrategy.getDataOutput()


    def doFailureStrategy(self, _edPlugin=None):
        self.DEBUG("EDPluginControlGridScreeningv1_0.doFailureStrategy")
        self.retrieveFailureMessages(self.edPluginControlStrategy, "EDPluginControlGridScreeningv1_0.doFailureStrategy")
        strErrorMessage = "Execution of strategy plugin failed."
        self.ERROR(strErrorMessage)
        self.addErrorMessage(strErrorMessage)

#    def generateExecutiveSummary(self, _edPlugin):
#        """
#        Generates a summary of the execution of the plugin.
#        """
#        self.DEBUG("EDPluginControlGridScreeningv1_0.generateExecutiveSummary")
#        self.addExecutiveSummaryLine("Summary of characterisation:")
#        xsDataInputStrategy = self.getDataInput()
#        xsDataCollection = xsDataInputStrategy.getDataCollection()
#        xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
#        self.addExecutiveSummaryLine("Diffraction plan:")
#        if (xsDataDiffractionPlan.getComplexity() is not None):
#            self.addExecutiveSummaryLine("BEST complexity                       : %s" % xsDataDiffractionPlan.getComplexity().getValue())
#        if (xsDataDiffractionPlan.getAimedCompleteness() is not None):
#            self.addExecutiveSummaryLine("Aimed completeness                    : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getAimedCompleteness().getValue()))
#        if (xsDataDiffractionPlan.getRequiredCompleteness() is not None):
#            self.addExecutiveSummaryLine("Required completeness                 : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getRequiredCompleteness().getValue()))
#        if (xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is not None):
#            self.addExecutiveSummaryLine("Aimed I/sigma at highest resolution   : %6.1f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue())
#        if (xsDataDiffractionPlan.getAimedResolution() is not None):
#            self.addExecutiveSummaryLine("Aimed resolution                      : %6.1f [A]" % xsDataDiffractionPlan.getAimedResolution().getValue())
#        if (xsDataDiffractionPlan.getRequiredResolution() is not None):
#            self.addExecutiveSummaryLine("Required resolution                   : %6.1f [A]" % xsDataDiffractionPlan.getRequiredResolution().getValue())
#        if (xsDataDiffractionPlan.getAimedMultiplicity() is not None):
#            self.addExecutiveSummaryLine("Aimed multiplicity                    : %6.1f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue())
#        if (xsDataDiffractionPlan.getRequiredMultiplicity() is not None):
#            self.addExecutiveSummaryLine("Required multiplicity                 : %6.1f" % xsDataDiffractionPlan.getRequiredMultiplicity().getValue())
#        if (xsDataDiffractionPlan.getForcedSpaceGroup() is not None):
#            self.addExecutiveSummaryLine("Forced space group                    : %6s" % xsDataDiffractionPlan.getForcedSpaceGroup().getValue())
#        if (xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is not None):
#            self.addExecutiveSummaryLine("Max exposure time per data collection : %6.1f [s]" % xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue())
#        self.addExecutiveSummarySeparator()
#        if self.edPluginControlIndexingIndicators is not None:
#            self.appendExecutiveSummary(self.edPluginControlIndexingIndicators, "")
#        if self.edPluginControlIndexingLabelit is not None:
#            self.appendExecutiveSummary(self.edPluginControlIndexingLabelit, "")
#        if self.edPluginControlIntegration is not None:
#            self.appendExecutiveSummary(self.edPluginControlIntegration, "")
#        if self.edPluginControlStrategy is not None:
#            self.appendExecutiveSummary(self.edPluginControlStrategy, "")
#        self.addExecutiveSummarySeparator()
#        if self.strCharacterisationShortSummary is not None:
#            self.addExecutiveSummaryLine("Characterisation short summary:")
#            self.addExecutiveSummaryLine("")
#            if self.strStatusMessage != None:
#                for strLine in self.strStatusMessage.split(". "):
#                    if strLine.endswith("."):
#                        self.addExecutiveSummaryLine(strLine)
#                    else:
#                        self.addExecutiveSummaryLine(strLine + ".")
#            self.addExecutiveSummaryLine("")
#            for strLine in self.strCharacterisationShortSummary.split("\n"):
#                if strLine != "\n":
#                    self.addExecutiveSummaryLine(strLine)
#        self.addErrorWarningMessagesToExecutiveSummary("Characterisation error and warning messages: ")
#        self.addExecutiveSummarySeparator()



    def addStatusMessage(self, _strStatusMessage):
        if self.strStatusMessage != "":
            self.strStatusMessage += " "
        self.strStatusMessage += _strStatusMessage


    def getFileNameParameters(self, _strFileName):
        """Method for extracting the rotation start angle, the two motor positions and the grid scan image no from the file name"""
        # Typical file name: mesh_0_21.676_-0.051_22_001.mccd
        listParts = os.path.basename(_strFileName).split("_")
        xsDataGridScreeningFileNameParameters = XSDataGridScreeningFileNameParameters()
        try:
            strScanId1 = listParts[1]
            xsDataGridScreeningFileNameParameters.setScanId1(XSDataString(strScanId1))
            strMotorPosition1 = listParts[2]
            xsDataGridScreeningFileNameParameters.setMotorPosition1(XSDataString(strMotorPosition1))
            strMotorPosition2 = listParts[3]
            xsDataGridScreeningFileNameParameters.setMotorPosition2(XSDataString(strMotorPosition2))
            strScanId2 = listParts[4]
            xsDataGridScreeningFileNameParameters.setScanId2(XSDataString(strScanId2))
        except:
            xsDataGridScreeningFileNameParameters = None
        return xsDataGridScreeningFileNameParameters
        
            
            
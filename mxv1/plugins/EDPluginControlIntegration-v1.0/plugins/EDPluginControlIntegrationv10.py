#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
Control plugin for MOSFLM integration.
"""

from EDVerbose import EDVerbose

from EDActionCluster import EDActionCluster

from EDPluginControl  import EDPluginControl
from EDMessage        import EDMessage
from EDConfiguration  import EDConfiguration

from XSDataCommon import XSPluginItem
from XSDataCommon import XSDataString

from XSDataMXv1 import XSDataInteger
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIntegrationResult


class EDPluginControlIntegrationv10(EDPluginControl):
    """
    The Plugin that controls the MOSFLM integration.
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataIntegrationInput)
        self.__strPluginIntegrationName = "EDPluginMOSFLMIntegrationv10"
        self.__edPluginIntegrationList = []
        self.__iNoSubwedges = None
        self.__strCONF_CONTROL_INTEGRATION_MAX_RMS = "maxRMSSpotDeviation"
        self.__fMaxRMSSpotDeviation = None
        self.__xsDataExperimentalConditionRefined = None
        self.__xsDataIntegrationResult = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getSelectedIndexingSolution(), "selectedIndexingSolution")


    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            EDVerbose.DEBUG("EDPluginControlIntegrationv10.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()
        strMaxRMSSpotDeviation = self.getStringConfigurationParameterValue(self.__strCONF_CONTROL_INTEGRATION_MAX_RMS)
        if(strMaxRMSSpotDeviation == None):
            EDVerbose.DEBUG("EDPluginControlIntegrationv10.configure: No configuration parameter found for: " + self.__strCONF_CONTROL_INTEGRATION_MAX_RMS + ", no default value.")
        else:
            self.setMaxRMSSpotDeviation(float(strMaxRMSSpotDeviation))


    def setMaxRMSSpotDeviation(self, _fMaxRMSSpotDeviation):
        self.__fMaxRMSSpotDeviation = _fMaxRMSSpotDeviation

    def getMaxRMSSpotDeviation(self):
        return self.__fMaxRMSSpotDeviation


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.preProcess...")

        xsDataIntegrationInput = self.getDataInput()
        xsDataSelectedIndexingSolution = xsDataIntegrationInput.getSelectedIndexingSolution()
        self.__xsDataExperimentalConditionRefined = xsDataIntegrationInput.getExperimentalConditionRefined()
        # To be changed (see bug #40)
        if (self.__xsDataExperimentalConditionRefined is None):
            self.__xsDataExperimentalConditionRefined = xsDataSelectedIndexingSolution.getExperimentalConditionRefined()
        xsDataCollection = xsDataIntegrationInput.getDataCollection()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()

        self.__edPluginIntegrationList = []

        iIndex = 0
        for xsDataSubWedge in xsDataSubWedgeList:
            iSubWedgeNumber = iIndex
            if (xsDataSubWedge.getSubWedgeNumber() is not None):
                # Use the incoming subwedge number if it exists
                iSubWedgeNumber = xsDataSubWedge.getSubWedgeNumber().getValue()

            edPluginIntegration = self.loadPlugin(self.__strPluginIntegrationName)

            if (not edPluginIntegration is None):
                iIndex += 1
                xsDataIntegrationInputSubWedge = XSDataIntegrationInput()
                xsDataIntegrationInputSubWedge.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataSelectedIndexingSolution.marshal()))
                xsDataIntegrationInputSubWedge.setExperimentalConditionRefined(XSDataExperimentalCondition.parseString(self.__xsDataExperimentalConditionRefined.marshal()))
                xsDataCollection = XSDataCollection()
                xsDataCollection.addSubWedge(xsDataSubWedge)
                xsDataIntegrationInputSubWedge.setDataCollection(xsDataCollection)
                try:
                    from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
                    xsDataMOSFLMInputIntegration = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIntegration(xsDataIntegrationInputSubWedge)
                    edPluginIntegration.setDataInput(xsDataMOSFLMInputIntegration)
                    edPluginIntegration.setBaseName("%s-%02d" % (self.__strPluginIntegrationName, iIndex))
                    edPluginIntegration.connectSUCCESS(self.doSuccessActionIntegration)
                    edPluginIntegration.connectFAILURE(self.doFailureActionIntegration)
                    # Here we store the sub wedge number for use in the results
                    self.__edPluginIntegrationList.append([iSubWedgeNumber, edPluginIntegration])
                except Exception, strErrorMessage:
                    self.addErrorMessage(strErrorMessage)
                    EDVerbose.ERROR(strErrorMessage)
                    self.setFailure()
            else:
                strErrorMessage = "EDPluginControlIntegrationv10.preProcess: could not load plugin %s" % self.__strPluginIntegrationName
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()


    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.process")
        for (iSubWedgeNumber, edPluginIntegration) in self.__edPluginIntegrationList:
            self.addPluginToActionCluster(edPluginIntegration)
        self.executeActionCluster()
        self.synchronizeActionCluster()
        if self.isFailure():
            self.generateExecutiveSummary(self)



    def doSuccessActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.doSuccessActionIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlIntegrationv10.doSuccessActionIntegration")


    def doFailureActionIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.doFailureActionIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlIntegrationv10.doFailureActionIntegration")
        self.setFailure()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.postProcess")
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        for (iSubWedgeNumber, edPluginIntegration) in self.__edPluginIntegrationList:
            xsDataMOSFLMOutputIntegration = edPluginIntegration.getDataOutput()
            if (xsDataMOSFLMOutputIntegration is None):
                strError = "MOSFLM integration error : no integration results obtained."
                self.addExecutiveSummaryLine(strError)
                EDVerbose.ERROR(strError)
                self.setFailure()
            else:
                xsDataIntegrationSubWedgeResult = None
                try:
                    xsDataIntegrationSubWedgeResult = EDHandlerXSDataMOSFLMv10.generateXSDataIntegrationSubWedgeResult(xsDataMOSFLMOutputIntegration, self.__xsDataExperimentalConditionRefined)
                except Exception, strErrorMessage:
                    self.addErrorMessage(strErrorMessage)
                    EDVerbose.ERROR(strErrorMessage)
                    self.setFailure()
                if (xsDataIntegrationSubWedgeResult is None):
                    strError = "MOSFLM integration error : no integration results obtained."
                    self.addExecutiveSummaryLine(strError)
                    EDVerbose.ERROR(strError)
                    self.setFailure()
                else:
                    xsDataIntegrationSubWedgeResult.setSubWedgeNumber(XSDataInteger(iSubWedgeNumber))
                    xsDataStatisticsIntegration = xsDataIntegrationSubWedgeResult.getStatistics()
                    fRMSSpotDeviation = xsDataStatisticsIntegration.getRMSSpotDeviation().getValue()
                    if (self.__fMaxRMSSpotDeviation is not None):
                        if (self.__fMaxRMSSpotDeviation < fRMSSpotDeviation):
                            iImageStart = edPluginIntegration.getDataInput().getImageStart().getValue()
                            iImageEnd = edPluginIntegration.getDataInput().getImageEnd().getValue()
                            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlIntegrationv10.postProcess", \
                                                                               "MOSFLM Integration : RMS spot deviation (%.3f [mm]) larger than max value from configuration (%.3f [mm]) for images %d to %d" % \
                                                                               (fRMSSpotDeviation, self.__fMaxRMSSpotDeviation, iImageStart, iImageEnd))
                            EDVerbose.error(errorMessage)
                            self.addErrorMessage(errorMessage)
                    if (xsDataIntegrationSubWedgeResult is not None):
                        if (self.__xsDataIntegrationResult is None):
                            self.__xsDataIntegrationResult = XSDataIntegrationResult()
                        self.__xsDataIntegrationResult.addIntegrationSubWedgeResult(xsDataIntegrationSubWedgeResult)
        self.setDataOutput(self.__xsDataIntegrationResult)
        self.generateIntegrationShortSummary(self.__xsDataIntegrationResult)


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of integration:")
        self.addErrorWarningMessagesToExecutiveSummary("Integration warning/error messages:")
        for (iSubWedgeNumber, edPluginIntegration) in self.__edPluginIntegrationList:
            if (edPluginIntegration is not None):
                if (edPluginIntegration.getDataOutput() is not None):
                    self.appendExecutiveSummary(edPluginIntegration, "MOSFLM : ")


    def generateIntegrationShortSummary(self, _xsDataIntegrationResult):
        """
        Generates a short summary of the MOSFLM integration(s)
        """
        EDVerbose.DEBUG("EDPluginControlIntegrationv10.generateIntegrationShortSummary")
        strIntegrationShortSummary = ""
        for xsDataIntegrationSubWedgeResult in _xsDataIntegrationResult.getIntegrationSubWedgeResult():
            iSubWedgeNumber = xsDataIntegrationSubWedgeResult.getSubWedgeNumber().getValue()
            strIntegrationShortSummary += "Integration: %d " % iSubWedgeNumber
            xsDataStatisticsIntegration = xsDataIntegrationSubWedgeResult.getStatistics()
            iNoFull = xsDataStatisticsIntegration.getNumberOfFullyRecordedReflections().getValue()
            strIntegrationShortSummary += "no full: %d, " % iNoFull
            iNoPartial = xsDataStatisticsIntegration.getNumberOfPartialReflections().getValue()
            strIntegrationShortSummary += "part: %d, " % iNoPartial
            iNoBad = xsDataStatisticsIntegration.getNumberOfBadReflections().getValue()
            iNoNegative = xsDataStatisticsIntegration.getNumberOfNegativeReflections().getValue()
            iNoOverlapped = xsDataStatisticsIntegration.getNumberOfOverlappedReflections().getValue()
            strIntegrationShortSummary += "bad/neg/ovrlp: %d, " % (iNoBad + iNoNegative + iNoOverlapped)
            fRMSSpotDeviation = xsDataStatisticsIntegration.getRMSSpotDeviation().getValue()
            strIntegrationShortSummary += "RMS dev: %.3f [mm], " % fRMSSpotDeviation
            fIOverSigmaOverall = xsDataStatisticsIntegration.getIOverSigmaOverall().getValue()
            strIntegrationShortSummary += "I/sigma overall %.1f " % fIOverSigmaOverall
            fIOverSigmaAtHighestResolution = xsDataStatisticsIntegration.getIOverSigmaAtHighestResolution().getValue()
            strIntegrationShortSummary += "at highest res %.1f" % fIOverSigmaAtHighestResolution
            strIntegrationShortSummary += "\n"
        for strLine in strIntegrationShortSummary.split("\n"):
            EDVerbose.screen(strLine)
        self.setDataOutput(XSDataString(strIntegrationShortSummary), "integrationShortSummary")


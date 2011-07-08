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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDPluginControl import EDPluginControl
from EDMessage       import EDMessage

from XSDataCommon import XSDataImage
from XSDataCommon import XSDataString

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataGeneratePredictionInput
from XSDataMXv1 import XSDataIndexingSolutionSelected


class EDPluginControlIndexingv10(EDPluginControl):
    """
    The plugin which controls the indexing execution plugins.
    
    Note that this plugin is not controlling the execution plugins directly,
    it is using separate specialised plugins which controls e.g. MOSFLM indexing,
    which are derived from this plugin class.
    
    This plugin accepts several sub-wedges with one or several images each.
    The indexing is performed on all images together.
    One image with prediction is generated for each input image.
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataIndexingInput)
        self.strPluginIndexingName = "EDPluginControlIndexingMOSFLMv10"
        #self.strPluginIndexingName = "EDPluginControlIndexingLabelitv10"
        #self.strPluginIndexingName = "EDPluginControlIndexingParallelv10"
        self.edPluginIndexing = None
        self.strPluginGeneratePredictionName = "EDPluginControlGeneratePredictionv10"
        self.edPluginGeneratePrediction = None
        self.xsDataIndexingOutput = None
        self.xsDataExperimentalCondition = None
        self.xsDataIndexingResult = None
        self.xsDataCollection = None
        self.bGeneratePredictionImage = False
        self.strPluginIndexingExecutiveSummaryName = None



    def configure(self):
        """
        Gets the EDPluginControl parameters from the configuration file and stores them in class member attributes.
        """
        EDPluginControl.configure(self)
        if (self.getControlledPluginName("indexingPlugin") is not None):
            self.strPluginIndexingName = self.getControlledPluginName("indexingPlugin")
        if (self.getControlledPluginName("generatePredictionPlugin") is not None):
            self.strPluginGeneratePredictionName = self.getControlledPluginName("generatePredictionPlugin")

    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        self.verboseDebug("EDPluginControlIndexingv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingv10.preProcess...")
        if (self.strPluginIndexingName is not None):
            # Load the indexing plugin and generate input data
            self.verboseDebug("EDPluginControlIndexingv10.preProcess : loading plugin %s" % self.strPluginIndexingName)
            self.edPluginIndexing = self.loadPlugin(self.strPluginIndexingName)
            self.loadPluginIndexingInputData()
            xsDataIndexingInput = self.getDataInput()
            # Save the data collection and the experimental condition for constructing the indexing results
            self.xsDataExperimentalCondition = xsDataIndexingInput.getExperimentalCondition()
            self.xsDataCollection = xsDataIndexingInput.getDataCollection()
        # Load the generate prediction plugin
        self.edPluginGeneratePrediction = self.loadPlugin(self.strPluginGeneratePredictionName)


    def loadPluginIndexingInputData(self):
        """
        This method is supposed to be overriden by the specific control indexing
        plugins in order to set their specific data input.
        """
        self.verboseDebug("EDPluginControlIndexingv10.loadPluginIndexingInputData...")
        self.edPluginIndexing.setDataInput(self.getDataInput())


    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingv10.process")
        if (self.edPluginIndexing is not None):
            self.edPluginIndexing.connectSUCCESS(self.doSuccessActionIndexing)
            self.edPluginIndexing.connectFAILURE(self.doFailureActionIndexing)
            self.connectProcess(self.edPluginIndexing.executeSynchronous)
        self.edPluginGeneratePrediction.connectSUCCESS(self.doSuccessActionGeneratePrediction)
        self.edPluginGeneratePrediction.connectFAILURE(self.doFailureActionGeneratePrediction)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingv10.postProcess")
        self.setDataOutput(self.xsDataIndexingResult)


    def doSuccessActionIndexing(self, _edPlugin=None):
        self.verboseDebug("EDPluginControlIndexingv10.doSuccessActionIndexing")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlIndexingv10.doSuccessActionIndexing")
        # Retrieve the output from the plugin
        self.xsDataIndexingResult = self.getDataIndexingResult(_edPlugin)
        self.generateShortSummary()
        # Add the list of images to the results
        xsDataListImage = self.generateImageList(self.xsDataCollection)
        self.xsDataIndexingResult.setImage(xsDataListImage)
        if (self.bGeneratePredictionImage):
            # Generate prediction images
            xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
            xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(self.xsDataCollection.marshal()))
            xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(self.xsDataIndexingResult.getSelectedSolution().marshal()))
            self.edPluginGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
            self.edPluginGeneratePrediction.executeSynchronous()


    def getDataIndexingResult(self, _edPlugin):
        """
        This method retrieves the indexing results from a MOSFLM indexing plugin.
        """
        self.verboseDebug("EDPluginControlIndexingv10.getDataIndexingResult")
        return _edPlugin.getDataOutput()


    def doFailureActionIndexing(self, _edPlugin=None):
        self.verboseDebug("EDPluginControlIndexingv10.doFailureActionIndexing")
        self.screen("Execution of " + self.strPluginIndexingName + "  failed.")
        self.screen("Please inspect the log file for further information.")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlIndexingv10.doFailureActionIndexing")
        self.generateExecutiveSummary(self)
        self.setFailure()



    def generatePredictionImageList(self, _edPluginGeneratePrediction, _xsDataCollection, _xsDataIndexingResult):
        """
        Generate a list containing the prediction images
        """
        self.verboseDebug("EDPluginControlIndexingv10.generatePredictionImageList")
        xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
        xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(_xsDataCollection.marshal()))
        xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(_xsDataIndexingResult.getSelectedSolution().marshal()))
        _edPluginGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
        _edPluginGeneratePrediction.executeSynchronous()



    def doSuccessActionGeneratePrediction(self, _edPlugin):
        """
        Executed if the generate prediction plugin terminated correctly.
        """
        self.verboseDebug("EDPluginControlIndexingv10.doSuccessActionGeneratePrediction")
        xsDataImageList = None
        if _edPlugin.isFailure():
            # Translate all error messages to warning messages
            for errorMessage in _edPlugin.getListOfErrorMessages():
                warningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ("EDPluginControlIndexingv10.generatePredictionImageList", \
                                                                            self.strPluginGeneratePredictionName, \
                                                                            errorMessage)
                self.warning(warningMessage)
                self.addWarningMessages([ warningMessage ])
        else:
            self.retrieveSuccessMessages(_edPlugin, "EDPluginControlIndexingv10.doSuccessActionGeneratePrediction")
            xsDataGeneratePredictionResult = _edPlugin.getDataOutput()
            self.xsDataIndexingResult.setPredictionResult(xsDataGeneratePredictionResult)


    def doFailureActionGeneratePrediction(self, _edPlugin):
        """
        Executed if the generate prediction plugin did not terminate correctly.
        """
        self.verboseDebug("EDPluginControlIndexingv10.doFailureActionGeneratePrediction")
        strWarningMessage = "Cannot generate prediction pattern"
        self.warning(strWarningMessage)
        self.addWarningMessages([ strWarningMessage ])




    def generateImageList(self, _xsDataCollection):
        """
        Make a list of all images in the subwedges
        """
        self.verboseDebug("EDPluginControlIndexingv10.generateImageList")
        listImage = None
        if (_xsDataCollection is not None):
            listImage = []
            xsDataSubWedgeList = _xsDataCollection.getSubWedge()
            for xsDataSubWedge in xsDataSubWedgeList:
                xsDataImageList = xsDataSubWedge.getImage()
                for xsDataImage in xsDataImageList:
                    listImage.append(XSDataImage.parseString(xsDataImage.marshal()))
        return listImage



    def generateShortSummary(self, _edPlugin=None):
        """
        Generates a very short summary of the indexing
        """
        strIndexingShortSummary = ""
        # Check if forced space group requested.
        xsDataIndexingInput = self.getDataInput()
        xsDataCrystal = xsDataIndexingInput.getCrystal()
        if xsDataCrystal is not None:
            if xsDataCrystal.getSpaceGroup() is not None:
                strForcedSpaceGroup = xsDataCrystal.getSpaceGroup().getName().getValue().upper()
                strIndexingShortSummary += "Forced space group: %s\n" % strForcedSpaceGroup
        if not self.isFailure() and self.xsDataIndexingResult is not None:
            # Indexing solution
            xsDataSelectedSolution = self.xsDataIndexingResult.getSelectedSolution()
            xsDataCrystal = xsDataSelectedSolution.getCrystal()
            # Refined cell parameters
            xsDataCell = xsDataCrystal.getCell()
            fA = xsDataCell.getLength_a().getValue()
            fB = xsDataCell.getLength_b().getValue()
            fC = xsDataCell.getLength_c().getValue()
            fAlpha = xsDataCell.getAngle_alpha().getValue()
            fBeta = xsDataCell.getAngle_beta().getValue()
            fGamma = xsDataCell.getAngle_gamma().getValue()
            # Estimated mosaicity
            fEstimatedMosaicity = xsDataCrystal.getMosaicity().getValue()
            # Space group
            strSpaceGroup = xsDataCrystal.getSpaceGroup().getName().getValue()
            # Spot deviation
            xsDataStatisticsIndexing = xsDataSelectedSolution.getStatistics()
            fSpotDeviationPositional = xsDataStatisticsIndexing.getSpotDeviationPositional().getValue()
            strIndexingShortSummary += "Indexing: laue/space group %s, mosaicity %.2f [degree], " % (strSpaceGroup, fEstimatedMosaicity)
            strIndexingShortSummary += "RMS dev pos %.2f [mm]" % fSpotDeviationPositional
            if xsDataStatisticsIndexing.getSpotDeviationAngular() is not None:
                fSpotDeviationAngular = xsDataStatisticsIndexing.getSpotDeviationAngular().getValue()
                strIndexingShortSummary += " ang %.2f [degree]" % fSpotDeviationAngular
            strIndexingShortSummary += "\n"
            strIndexingShortSummary += "Indexing: refined Cell %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f\n" % (fA, fB, fC, fAlpha, fBeta, fGamma)
        else:
            strIndexingShortSummary += "Indexing failed."
        self.screen("Control indexing short summary:")
        for strLine in strIndexingShortSummary.split("\n"):
            self.screen(strLine)
        self.setDataOutput(XSDataString(strIndexingShortSummary), "indexingShortSummary")




    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.verboseDebug("EDPluginControlIndexingv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of indexing with %s :" % self.strPluginIndexingName)
        self.addErrorWarningMessagesToExecutiveSummary("Indexing failure! Error messages: ")
        if (self.edPluginIndexing is not None):
            if (self.strPluginIndexingExecutiveSummaryName is not None):
                self.appendExecutiveSummary(self.edPluginIndexing, self.strPluginIndexingExecutiveSummaryName + " : ")
            else:
                self.appendExecutiveSummary(self.edPluginIndexing)
        if (self.edPluginGeneratePrediction is not None):
            self.appendExecutiveSummary(self.edPluginGeneratePrediction, "Prediction : ")


    def setPluginIndexingName(self, _strPluginIndexingName):
        self.strPluginIndexingName = _strPluginIndexingName


    def setPluginIndexingExecutiveSummaryName(self, _strPluginIndexingExecutiveSummaryName):
        self.strPluginIndexingExecutiveSummaryName = _strPluginIndexingExecutiveSummaryName


    def setGeneratePredictionImage(self, _bGeneratePredictionImage):
        self.bGeneratePredictionImage = _bGeneratePredictionImage


    def getPluginIndexing(self):
        return self.edPluginIndexing


    def getExperimentalCondition(self):
        return self.xsDataExperimentalCondition

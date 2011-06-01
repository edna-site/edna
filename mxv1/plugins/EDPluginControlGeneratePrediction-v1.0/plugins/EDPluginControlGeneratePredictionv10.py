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
from EDActionCluster import EDActionCluster
from EDPluginControl import EDPluginControl
from EDMessage       import EDMessage

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataImage

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataGeneratePredictionInput
from XSDataMXv1 import XSDataGeneratePredictionResult
from XSDataMXv1 import XSDataExperimentalCondition


class EDPluginControlGeneratePredictionv10(EDPluginControl):
    """
    The Plugin that control the plugin that generates the prediction.
    If several images are available the execution of the plugin which generates
    the prediction is performed in parallel.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.__strPluginGeneratePredictionName = "EDPluginMOSFLMGeneratePredictionv10"
        #self.m_strPluginGeneratePredictionName = "EDPluginMOSFLMv01GeneratePrediction"
        self.__listPluginGeneratePrediction = []
        self.__dNoSubwedges = None
        self.__xsDataGeneratePredictionResult = None
        self.setXSDataInputClass(XSDataGeneratePredictionInput)


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getSelectedIndexingSolution(), "selectedIndexingSolution")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.preProcess...")

        xsDataGeneratePredictionInput = self.getDataInput()

        xsDataSelectedIndexingSolution = xsDataGeneratePredictionInput.getSelectedIndexingSolution()
        xsDataExperimentalConditionRefined = xsDataSelectedIndexingSolution.getExperimentalConditionRefined()
        xsDataCollection = xsDataGeneratePredictionInput.getDataCollection()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()

        # List containing instances of all the generate prediction plugins
        self.__listPluginGeneratePrediction = []

        # Loop through all subwedges
        iIndex = 0
        for xsDataSubWedge in xsDataSubWedgeList:

            xsDataImageList = xsDataSubWedge.getImage()
            # First find the lowest image number
            iLowestImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                if (iLowestImageNumber is None):
                    iLowestImageNumber = iImageNumber
                elif (iImageNumber < iLowestImageNumber):
                    iLowestImageNumber = iImageNumber
            # Then loop through all images in a sub wedge
            for xsDataImage in xsDataImageList:
                iIndex += 1
                edPluginGeneratePrediction = self.loadPlugin(self.__strPluginGeneratePredictionName,
                                                              "%s-%02d" % (self.__strPluginGeneratePredictionName, iIndex))
                xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
                xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataSelectedIndexingSolution.marshal()))
                xsDataCollectionNew = XSDataCollection()
                xsDataSubWedgeNew = XSDataSubWedge()
                xsDataSubWedgeNew.addImage(XSDataImage.parseString(xsDataImage.marshal()))
                xsDataSubWedgeNew.setExperimentalCondition(XSDataExperimentalCondition.parseString(xsDataSubWedge.getExperimentalCondition().marshal()))
                # We must modify the rotationOscillationStart for the new subwedge
                xsDataGoniostatNew = xsDataSubWedgeNew.getExperimentalCondition().getGoniostat()
                fGoniostatRotationAxisStart = xsDataGoniostatNew.getRotationAxisStart().getValue()
                fGonioStatOscillationRange = xsDataGoniostatNew.getOscillationWidth().getValue()
                iImageNumber = xsDataImage.getNumber().getValue()
                fGoniostatRotationAxisStartNew = fGoniostatRotationAxisStart + (iImageNumber - iLowestImageNumber) * fGonioStatOscillationRange
                xsDataGoniostatNew.setRotationAxisStart(XSDataAngle(fGoniostatRotationAxisStartNew))
                # 
                xsDataCollectionNew.addSubWedge(xsDataSubWedgeNew)
                xsDataGeneratePredictionInput.setDataCollection(xsDataCollectionNew)
                from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
                xsDataMOSFLMInputGeneratePrediction = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputGeneratePrediction(xsDataGeneratePredictionInput)
                edPluginGeneratePrediction.setDataInput(xsDataMOSFLMInputGeneratePrediction)
                self.__listPluginGeneratePrediction.append(edPluginGeneratePrediction)



    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.process")
        # Prepare the action cluster
        for edPluginGeneratePrediction in self.__listPluginGeneratePrediction:
            edPluginGeneratePrediction.connectSUCCESS(self.doSuccessGeneratePrediction)
            edPluginGeneratePrediction.connectFAILURE(self.doFailureGeneratePrediction)
            self.addPluginToActionCluster(edPluginGeneratePrediction)
        # Launch the cluster
        self.executeActionCluster()
        self.synchronizeActionCluster()


    def doSuccessGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.doSuccessGeneratePrediction")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlGeneratePredictionv10.doSuccessGeneratePrediction")
        if (self.__xsDataGeneratePredictionResult is None):
            self.__xsDataGeneratePredictionResult = XSDataGeneratePredictionResult()
        xsDataMOSFLMOutputGeneratePrediction = _edPlugin.getDataOutput()
        xsDataImage = xsDataMOSFLMOutputGeneratePrediction.getPredictionImage()
        self.__xsDataGeneratePredictionResult.addPredictionImage(XSDataImage.parseString(xsDataImage.marshal()))


    def doFailureGeneratePrediction(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.doFailureGeneratePrediction")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlGeneratePredictionv10.doFailureGeneratePrediction")


    def postProcess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.postProcess")
        self.setDataOutput(self.__xsDataGeneratePredictionResult)


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlGeneratePredictionv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of generation of image(s) with prediction:")
        self.addErrorWarningMessagesToExecutiveSummary("Generation of prediction failure! Error messages: ")
        xsDataGeneratePredictionResult = self.getDataOutput()
        if (xsDataGeneratePredictionResult is not None):
            for predictionImage in xsDataGeneratePredictionResult.getPredictionImage():
                self.addExecutiveSummaryLine("Path to prediction image number %d : %s" % \
                                             (predictionImage.getNumber().getValue(), predictionImage.getPath().getValue()))

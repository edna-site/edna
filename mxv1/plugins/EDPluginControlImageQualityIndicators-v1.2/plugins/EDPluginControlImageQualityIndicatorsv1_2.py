#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose import EDVerbose
from EDUtilsParallel import EDUtilsParallel

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput

from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10

EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile

EDFactoryPluginStatic.loadModule("XSDataLabelitv1_1")
from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataISPyBImageQualityIndicators
from XSDataISPyBv1_4 import XSDataInputStoreListOfImageQualityIndicators


class EDPluginControlImageQualityIndicatorsv1_2(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.strPluginWaitFileName = "EDPluginWaitFile"
        self.strPluginName = "EDPluginDistlSignalStrengthv1_1"
        self.strPluginNameThinClient = "EDPluginDistlSignalStrengthThinClientv1_1"
        self.strISPyBPluginName = "EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4"
        self.strIndexingMOSFLMPluginName = "EDPluginMOSFLMIndexingv10"
        self.edPluginMOSFLMIndexing = None
        self.strPluginReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.edPluginReadImageHeader = None
        self.setXSDataInputClass(XSDataInputControlImageQualityIndicators)
        self.listPluginExecImageQualityIndicator = []
        self.xsDataResultControlImageQualityIndicators = None
        self.edPluginWaitFile = None
        # Default time out for wait file
        self.fWaitFileTimeOut = 30 #s
        # Flag for using the thin client
        self.bUseThinClient = True
        self.edPluginISPyB = None
        self.listPluginMOSFLM = []
        

    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "Image")


    def configure(self, _edPlugin = None):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.configure")
        self.fWaitFileTimeOut = float(self.config.get("waitFileTimeOut", self.fWaitFileTimeOut))

    

    def process(self, _edPlugin=None):
        """
        Executes the execution plugins
        """
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.process")
        EDUtilsParallel.initializeNbThread()
        # Check if we should do indexing:
        bDoIndexing = False
        if self.dataInput.doIndexing is not None:
            if self.dataInput.doIndexing.value:
                 bDoIndexing = True
        # Loop through all the incoming reference images
        listXSDataImage = self.dataInput.image
        xsDataInputWaitFile = XSDataInputWaitFile()
        self.xsDataResultControlImageQualityIndicators = XSDataResultControlImageQualityIndicators()
        listPlugin = []
        for xsDataImage in listXSDataImage:
            if not os.path.exists(xsDataImage.path.value):
                self.screen("Waiting for image %s" % xsDataImage.path.value)
                self.edPluginWaitFile = self.loadPlugin(self.strPluginWaitFileName)
                xsDataInputWaitFile.expectedFile = XSDataFile(xsDataImage.path)
                xsDataInputWaitFile.setExpectedSize(XSDataInteger(100000))
                xsDataInputWaitFile.setTimeOut(XSDataTime(self.fWaitFileTimeOut))
                self.DEBUG("Wait file timeOut set to %f" % self.fWaitFileTimeOut)
                self.edPluginWaitFile.setDataInput(xsDataInputWaitFile)
                self.edPluginWaitFile.executeSynchronous()
            if not os.path.exists(xsDataImage.path.value):
                strError = "Time-out while waiting for image %s" % xsDataImage.path.value
                self.error(strError)
                self.addErrorMessage(strError)
                self.setFailure()
            else:
                if self.bUseThinClient:
                    strPluginName = self.strPluginNameThinClient
                else:
                    strPluginName = self.strPluginName
                edPluginPluginExecImageQualityIndicator = self.loadPlugin(strPluginName)
                listPlugin.append(edPluginPluginExecImageQualityIndicator)
                self.listPluginExecImageQualityIndicator.append(edPluginPluginExecImageQualityIndicator)
                xsDataInputDistlSignalStrength = XSDataInputDistlSignalStrength()
                xsDataInputDistlSignalStrength.setReferenceImage(xsDataImage)
                edPluginPluginExecImageQualityIndicator.setDataInput(xsDataInputDistlSignalStrength)
                edPluginPluginExecImageQualityIndicator.execute()
        listIndexing = []
        # Synchronize all image quality indicator plugins and upload to ISPyB
        xsDataInputStoreListOfImageQualityIndicators = XSDataInputStoreListOfImageQualityIndicators()
        for edPluginPluginExecImageQualityIndicator in listPlugin:
            edPluginPluginExecImageQualityIndicator.synchronize()
            xsDataImageQualityIndicators = XSDataImageQualityIndicators.parseString( \
                                             edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators.marshal())
            self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(xsDataImageQualityIndicators)
            xsDataISPyBImageQualityIndicators = \
                XSDataISPyBImageQualityIndicators.parseString(xsDataImageQualityIndicators.marshal())
            xsDataInputStoreListOfImageQualityIndicators.addImageQualityIndicators(xsDataISPyBImageQualityIndicators)
#        print xsDataInputStoreListOfImageQualityIndicators.marshal()
        self.edPluginISPyB = self.loadPlugin(self.strISPyBPluginName)
        self.edPluginISPyB.dataInput = xsDataInputStoreListOfImageQualityIndicators
        self.edPluginISPyB.execute()
        #
        if bDoIndexing:
            # Find the 5 most intensive images (TIS):
            listImage = []
            listSorted = sorted(self.xsDataResultControlImageQualityIndicators.imageQualityIndicators,
                                key=lambda imageQualityIndicators: imageQualityIndicators.totalIntegratedSignal.value)
            for xsDataResultControlImageQualityIndicator in listSorted[-5:]:
                if xsDataResultControlImageQualityIndicator.goodBraggCandidates.value > 30:
                    xsDataInputReadImageHeader = XSDataInputReadImageHeader()
                    xsDataInputReadImageHeader.image = XSDataFile(xsDataResultControlImageQualityIndicator.image.path)
                    self.edPluginReadImageHeader = self.loadPlugin(self.strPluginReadImageHeaderName)
                    self.edPluginReadImageHeader.dataInput = xsDataInputReadImageHeader
                    self.edPluginReadImageHeader.executeSynchronous()
                    xsDataResultReadImageHeader = self.edPluginReadImageHeader.dataOutput
                    if xsDataResultReadImageHeader is not None:
                        xsDataSubWedge = xsDataResultReadImageHeader.subWedge
                        self.xsDataCollection = XSDataCollection()
                        self.xsDataCollection.addSubWedge(xsDataSubWedge)
                        xsDataIndexingInput = XSDataIndexingInput()
                        xsDataIndexingInput.setDataCollection(self.xsDataCollection)
                        xsDataMOSFLMIndexingInput = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(xsDataIndexingInput)
                        edPluginMOSFLMIndexing = self.loadPlugin(self.strIndexingMOSFLMPluginName)
                        self.listPluginMOSFLM.append([edPluginMOSFLMIndexing, xsDataResultControlImageQualityIndicator])
                        edPluginMOSFLMIndexing.setDataInput(xsDataMOSFLMIndexingInput)
                        edPluginMOSFLMIndexing.execute()
            for tupleMOSFLM in self.listPluginMOSFLM:
                edPluginMOSFLMIndexing = tupleMOSFLM[0]
                xsDataResultControlImageQualityIndicator = tupleMOSFLM[1]
                edPluginMOSFLMIndexing.synchronize()
                if not edPluginMOSFLMIndexing.isFailure():
                    xsDataMOSFLMOutput = edPluginMOSFLMIndexing.dataOutput
                    xsDataIndexingResult = EDHandlerXSDataMOSFLMv10.generateXSDataIndexingResult(xsDataMOSFLMOutput)
                    selectedSolution = xsDataIndexingResult.selectedSolution
                    if selectedSolution is not None:
                        xsDataResultControlImageQualityIndicator.selectedIndexingSolution = selectedSolution

#                print xsDataIndexingResult.marshal()
#                xsDataResultISPyB = edPluginISPyB.dataOutput
#                if xsDataResultISPyB is not None:
                #print xsDataResultISPyB.marshal()
            
        

    def finallyProcess(self, _edPlugin= None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        # Synchronize ISPyB plugin
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.finallyProcess")
        self.edPluginISPyB.synchronize()
        listId = []
        for xsDataInteger in self.edPluginISPyB.dataOutput.imageQualityIndicatorsId:
            listId.append(xsDataInteger.value)
        EDVerbose.DEBUG("ISPyB imageQualityIndicatorIds = %r" % listId) 
        self.setDataOutput(self.xsDataResultControlImageQualityIndicators)



    def generateExecutiveSummary(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.strPluginName)
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Distl.signal_strength : ", _bAddSeparator=False)

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

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile

EDFactoryPluginStatic.loadModule("XSDataLabelitv1_1")
from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataISPyBImageQualityIndicators
from XSDataISPyBv1_4 import XSDataInputStoreImageQualityIndicators


class EDPluginControlImageQualityIndicatorsv1_2(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.strPluginWaitFileName = "EDPluginWaitFile"
        self.strPluginName = "EDPluginDistlSignalStrengthv1_1"
        self.strPluginNameThinClient = "EDPluginDistlSignalStrengthThinClientv1_1"
        self.strISPyBPluginName = "EDPluginISPyBStoreImageQualityIndicatorsv1_4"
        self.setXSDataInputClass(XSDataInputControlImageQualityIndicators)
        self.listPluginExecImageQualityIndicator = []
        self.xsDataResultControlImageQualityIndicators = None
        self.edPluginWaitFile = None
        # Default time out for wait file
        self.fWaitFileTimeOut = 30 #s
        # Flag for using the thin client
        self.bUseThinClient = True
        

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
        for edPluginPluginExecImageQualityIndicator in listPlugin:
            edPluginPluginExecImageQualityIndicator.synchronize()
            xsDataImageQualityIndicators = \
                edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators
            self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(
                XSDataImageQualityIndicators.parseString(xsDataImageQualityIndicators.marshal()))
            # Upload to ISPyB
            xsDataInputStoreImageQualityIndicators = XSDataInputStoreImageQualityIndicators()
            xsDataISPyBImageQualityIndicators = \
                XSDataISPyBImageQualityIndicators.parseString(
                    xsDataImageQualityIndicators.marshal())
            xsDataInputStoreImageQualityIndicators.imageQualityIndicators = \
                xsDataISPyBImageQualityIndicators
            #print xsDataInputStoreImageQualityIndicators.marshal()
            edPluginISPyB = self.loadPlugin(self.strISPyBPluginName)
            edPluginISPyB.dataInput = xsDataInputStoreImageQualityIndicators
            edPluginISPyB.executeSynchronous()
#                xsDataResultISPyB = edPluginISPyB.dataOutput
#                if xsDataResultISPyB is not None:
                    #print xsDataResultISPyB.marshal()
        

    def finallyProcess(self, _edPlugin= None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.finallyProcess")
        self.setDataOutput(self.xsDataResultControlImageQualityIndicators)



    def generateExecutiveSummary(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.strPluginName)
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Distl.signal_strength : ", _bAddSeparator=False)

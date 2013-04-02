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

from EDVerbose import EDVerbose

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDConfiguration import EDConfiguration
from EDActionCluster import EDActionCluster


from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitMultiFile

EDFactoryPluginStatic.loadModule("XSDataLabelitv1_1")
from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength


class EDPluginControlImageQualityIndicatorsv1_2(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.strPluginExecWaitMultiFileName = "EDPluginWaitMultiFile"
        self.strPluginExecImageQualityIndicatorName = "EDPluginDistlSignalStrengthv1_1"
        self.strPluginExecImageQualityIndicatorNameThinClient = "EDPluginDistlSignalStrengthThinClientv1_1"
        self.setXSDataInputClass(XSDataInputControlImageQualityIndicators)
        self.listPluginExecImageQualityIndicator = None
        self.xsDataResultControlImageQualityIndicators = None
        self.edPluginWaitMultiFile = None
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

    
    def preProcess(self, _edPlugin=None):
        """
        Prepares the execution plugin
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.preProcess...")
        # Loop through all the incoming reference images
        self.edPluginWaitMultiFile = self.loadPlugin(self.strPluginExecWaitMultiFileName)
        listXSDataImage = self.getDataInput().getImage()
        xsDataInputWaitMultiFile = XSDataInputWaitMultiFile()
        for xsDataImage in listXSDataImage:
            xsDataInputWaitMultiFile.addExpectedFile(XSDataFile(xsDataImage.getPath()))
        xsDataInputWaitMultiFile.setExpectedSize(XSDataInteger(100000))
        xsDataInputWaitMultiFile.setTimeOut(XSDataTime(self.fWaitFileTimeOut))
        self.DEBUG("Wait file timeOut set to %f" % self.fWaitFileTimeOut)
        self.edPluginWaitMultiFile.setDataInput(xsDataInputWaitMultiFile)
        self.xsDataResultControlImageQualityIndicators = XSDataResultControlImageQualityIndicators()



    def process(self, _edPlugin=None):
        """
        Executes the execution plugins
        """
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.process")
        self.edPluginWaitMultiFile.connectSUCCESS(self.doSuccessWaitMultiFile)
        self.edPluginWaitMultiFile.connectFAILURE(self.doFailureWaitMultiFile)
        self.executePluginSynchronous(self.edPluginWaitMultiFile)


    def finallyProcess(self, _edPlugin= None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.finallyProcess")
        self.setDataOutput(self.xsDataResultControlImageQualityIndicators)


    def doSuccessWaitMultiFile(self, _edPlugin):
        """
        The file has appeared on the disk 
        """
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.doSuccessWaitMultiFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doSuccessWaitMultiFile")
        # Check if we should use the thin client
        if self.bUseThinClient:
            self.runExecPluginImageQualityIndicatorsThinClient()
        else:
            self.runExecPluginImageQualityIndicators()
        
        
    def runExecPluginImageQualityIndicatorsThinClient(self, _edPlugin=None):
        """Runs the thin client of the image quality indicator exec plugin"""
        self.executeImageQualityIndicatorActionCluster(self.strPluginExecImageQualityIndicatorNameThinClient, \
                                                       self.doSuccessActionCluster, \
                                                       self.runExecPluginImageQualityIndicators)
        
        
    def runExecPluginImageQualityIndicators(self, _edPlugin=None):
        """Runs the image quality indicator exec plugin locally"""
        self.executeImageQualityIndicatorActionCluster(self.strPluginExecImageQualityIndicatorName, \
                                                       self.doSuccessActionCluster, \
                                                       self.doFailureActionCluster)

        
    def executeImageQualityIndicatorActionCluster(self, _strPluginName, _pyMethodSuccess, _pyMethodFailure):
        # List containing instances of all the exeuction plugins
        self.listPluginExecImageQualityIndicator = []
        listXSDataImage = self.getDataInput().getImage()
        for (iIndex, xsDataImage) in enumerate(listXSDataImage):
            edPluginPluginExecImageQualityIndicator = self.loadPlugin(_strPluginName, \
                                                                      "%s-%d" % (_strPluginName, iIndex + 1))
            xsDataInputDistlSignalStrength = XSDataInputDistlSignalStrength()
            xsDataInputDistlSignalStrength.setReferenceImage(xsDataImage)
            edPluginPluginExecImageQualityIndicator.setDataInput(xsDataInputDistlSignalStrength)
            self.listPluginExecImageQualityIndicator.append(edPluginPluginExecImageQualityIndicator)
        # Prepare the action cluster
        edActionCluster = EDActionCluster()
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            edActionCluster.addAction(edPluginPluginExecImageQualityIndicator)
        edActionCluster.connectSUCCESS(_pyMethodSuccess)
        edActionCluster.connectFAILURE(_pyMethodFailure)
        # Launch the cluster
        edActionCluster.executeSynchronous()


    def doFailureWaitMultiFile(self, _edPlugin):
        """
        The file has not appeared on the disk 
        """
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.doFailureWaitMultiFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doFailureWaitMultiFile")
        self.ERROR("Timeout when waiting for images")
        self.setFailure()

    
    def doSuccessActionCluster(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.doSuccessActionCluster")
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            xsDataImageQualityIndicators = edPluginPluginExecImageQualityIndicator.getDataOutput().getImageQualityIndicators()
            self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(XSDataImageQualityIndicators.parseString(xsDataImageQualityIndicators.marshal()))


    def doFailureActionCluster(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.doFailureGeneratePrediction")
        #self.retrieveFailureMessages(_edPlugin, "EDPluginControlImageQualityIndicatorsv1_2.doFailureExecPlugin")


    def generateExecutiveSummary(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_2.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.strPluginExecImageQualityIndicatorName)
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Distl.signal_strength : ", _bAddSeparator=False)

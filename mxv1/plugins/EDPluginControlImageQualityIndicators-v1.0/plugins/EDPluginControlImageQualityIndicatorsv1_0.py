#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
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

from XSDataCommon import XSDataImage

from XSDataMXv1 import XSDataImageQualityIndicators

class EDPluginControlImageQualityIndicatorsv1_0(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.__strPluginExecImageQualityIndicatorName = "EDPluginLabelitDistlv1_1"
        self.setXSDataInputClass(XSDataImage, "referenceImage")
        self.__listPluginExecImageQualityIndicator = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput("referenceImage"), "referenceImage")


    def preProcess(self, _edObject=None):
        """
        Prepares the execution plugin
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.preProcess...")
        # List containing instances of all the exeuction plugins
        self.__listPluginExecImageQualityIndicator = []
        # Loop through all the incoming reference images
        listXSDataImage = self.getDataInput("referenceImage")
        for (iIndex, xsDataImage) in enumerate(listXSDataImage):
            edPluginPluginExecImageQualityIndicator = self.loadPlugin(self.__strPluginExecImageQualityIndicatorName, \
                                                                      "%s-%d" % (self.__strPluginExecImageQualityIndicatorName, iIndex + 1))
            edPluginPluginExecImageQualityIndicator.setDataInput(str(xsDataImage.marshal()), "referenceImage")
            self.__listPluginExecImageQualityIndicator.append(edPluginPluginExecImageQualityIndicator)


    def process(self, _edObject=None):
        """
        Executes the execution plugins
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.process")
        # Prepare the action cluster
        for edPluginPluginExecImageQualityIndicator in self.__listPluginExecImageQualityIndicator:
            edPluginPluginExecImageQualityIndicator.connectSUCCESS(self.doSuccessExecPlugin)
            edPluginPluginExecImageQualityIndicator.connectFAILURE(self.doFailureExecPlugin)
            self.addPluginToActionCluster(edPluginPluginExecImageQualityIndicator)
        # Launch the cluster
        self.executeActionCluster()
        self.synchronizeActionCluster()


    def doSuccessExecPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.doSuccessExecPlugin")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlImageQualityIndicatorsv1_0.doSuccessExecPlugin")
        xsDataImageQualityIndicators = _edPlugin.getDataOutput("imageQualityIndicators")[0]
        self.synchronizeOn()
        self.setDataOutput(XSDataImageQualityIndicators.parseString(xsDataImageQualityIndicators.marshal()), \
                           "imageQualityIndicators")
        self.synchronizeOff()


    def doFailureExecPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.doFailureGeneratePrediction")
        #self.retrieveFailureMessages(_edPlugin, "EDPluginControlImageQualityIndicatorsv1_0.doFailureExecPlugin")


    def generateExecutiveSummary(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlImageQualityIndicatorsv1_0.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.__strPluginExecImageQualityIndicatorName)
        for edPluginPluginExecImageQualityIndicator in self.__listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Labelit.distl : ", _bAddSeparator=False)

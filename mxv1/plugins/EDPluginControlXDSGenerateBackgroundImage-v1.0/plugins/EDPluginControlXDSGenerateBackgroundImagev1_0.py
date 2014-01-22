#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:        Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl

from XSDataMXv1 import XSDataInputControlXDSGenerateBackgroundImage
from XSDataMXv1 import XSDataResultControlXDSGenerateBackgroundImage

from EDHandlerXSDataXDSv1_0 import EDHandlerXSDataXDSv1_0


class EDPluginControlXDSGenerateBackgroundImagev1_0(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlXDSGenerateBackgroundImage)
        self.__strXDSGenerateBackgroundImagePluginName = "EDPluginXDSGenerateBackgroundImagev1_0"
        self.__edPluginXDSGenerateBackgroundImage = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.preProcess")
        # Input data
        xsDataCollection = self.getDataInput().getDataCollection()
        xsDataInputXDS = EDHandlerXSDataXDSv1_0.generateXSDataInputXDS(xsDataCollection)
        # Load the execution plugin
        self.__edPluginXDSGenerateBackgroundImage = self.loadPlugin(self.__strXDSGenerateBackgroundImagePluginName)
        self.__edPluginXDSGenerateBackgroundImage.setDataInput(xsDataInputXDS)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.process")
        self.__edPluginXDSGenerateBackgroundImage.connectSUCCESS(self.doSuccessExecTemplate)
        self.__edPluginXDSGenerateBackgroundImage.connectFAILURE(self.doFailureExecTemplate)
        self.executePluginSynchronous(self.__edPluginXDSGenerateBackgroundImage)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.postProcess")
        # Create some output data
        # xsDataResult = XSDataResultControlXDSGenerateBackgroundImage()
        # self.setDataOutput(xsDataResult)


    def doSuccessExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlXDSGenerateBackgroundImagev1_0.doSuccessExecTemplate")
        xsDataResultXDSGenerateBackgroundImage = self.__edPluginXDSGenerateBackgroundImage.getDataOutput()
        xsDataResultControlXDSGenerateBackgroundImage = EDHandlerXSDataXDSv1_0.generateXSDataResultXDSGenerateBackgroundImage(xsDataResultXDSGenerateBackgroundImage)
        self.setDataOutput(xsDataResultControlXDSGenerateBackgroundImage)


    def doFailureExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXDSGenerateBackgroundImagev1_0.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlXDSGenerateBackgroundImagev1_0.doFailureExecTemplate")

# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF
#
#    Principal author:        Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011 ESRF"


from EDPluginControl import EDPluginControl
from XSDataEdnaSaxs import XSDataInputAutoSub
from XSDataEdnaSaxs import XSDataResultAutoSub

class EDPluginAutoSub(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputAutoSub)
        self.__strControlledPluginName = "<controledPluginName>"
        self.__edPluginExecTemplate = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginAutoSub.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginAutoSub.preProcess")
        # Load the execution plugin
        self.__edPluginExecTemplate = self.loadPlugin(self.__strControlledPluginName)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginAutoSub.process")
        self.__edPluginExecTemplate.connectSUCCESS(self.doSuccessExecTemplate)
        self.__edPluginExecTemplate.connectFAILURE(self.doFailureExecTemplate)
        self.__edPluginExecTemplate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginAutoSub.postProcess")
        # Create some output data
        xsDataResult = XSDataResultAutoSub()
        self.setDataOutput(xsDataResult)


    def doSuccessExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSub.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginAutoSub.doSuccessExecTemplate")


    def doFailureExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSub.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginAutoSub.doFailureExecTemplate")

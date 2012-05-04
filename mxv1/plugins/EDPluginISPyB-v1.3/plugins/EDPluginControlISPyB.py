# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDPluginControl import EDPluginControl
from XSDataMXv1 import XSDataInputControlISPyB
from XSDataMXv1 import XSDataResultControlISPyB

class EDPluginControlISPyB( EDPluginControl ):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """
    

    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlISPyB)
        self.__strControlledPluginName = "EDPluginToDrivev10"
        self.__edPluginExecTemplate = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlISPyB.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlISPyB.preProcess")
        # Load the execution plugin
        self.__edPluginExecTemplate = self.loadPlugin(self.__strControlledPluginName) 

        
    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlISPyB.process")
        self.__edPluginExecTemplate.connectSUCCESS(self.doSuccessExecTemplate)
        self.__edPluginExecTemplate.connectFAILURE(self.doFailureExecTemplate)
        self.__edPluginExecTemplate.executeSynchronous()

    
    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlISPyB.postProcess")
        # Create some output data
        xsDataResult = XSDataResultControlISPyB()
        self.setDataOutput(xsDataResult)
    

    def doSuccessExecTemplate(self,  _edPlugin = None):
        self.DEBUG("EDPluginControlISPyB.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlISPyB.doSuccessExecTemplate")


    def doFailureExecTemplate(self,  _edPlugin = None):
        self.DEBUG("EDPluginControlISPyB.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlISPyB.doFailureExecTemplate")

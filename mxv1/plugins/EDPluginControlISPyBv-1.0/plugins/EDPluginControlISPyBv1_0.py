#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDVerbose       import EDVerbose
from EDPluginControl import EDPluginControl
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataInputControlISPyB
from XSDataMXv1 import XSDataResultControlISPyB

class EDPluginControlISPyBv1_0(EDPluginControl):
    """
    This plugin controls the ISPyB execution plugin.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlISPyB)
        self.setXSDataInputClass(XSDataString, "shortComments")
        self.setXSDataInputClass(XSDataString, "comments")
        self.setXSDataInputClass(XSDataString, "statusMessage")
        self.__strPluginExecISPyBName = "EDPluginISPyBv1_1"
        self.__edPluginExecISPyB = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getCharacterisationResult(), "characterisationResult")


    def preProcess(self, _edObject=None):
        """
        Loads the ISPyB execution plugin and prepares the input data
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.preProcess...")
        self.__edPluginExecISPyB = self.loadPlugin(self.__strPluginExecISPyBName)
        from EDHandlerXSDataISPyBv1_1 import EDHandlerXSDataISPyBv1_1
	strStatusMessage = None
	if self.hasDataInput("statusMessage"):
	    strStatusMessage = self.getDataInput("statusMessage")[0].getValue()
        xsDataInputISPyB = EDHandlerXSDataISPyBv1_1.generateXSDataInputISPyB(self.getDataInput(), strStatusMessage)
        self.__edPluginExecISPyB.setDataInput(xsDataInputISPyB)


    def process(self, _edObject=None):
        """
        Executes the ISPyB execution plugin
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.process")
        if (self.__edPluginExecISPyB is not None):
            self.__edPluginExecISPyB.connectSUCCESS(self.doSuccessExecuteISPyBPlugin)
            self.__edPluginExecISPyB.connectFAILURE(self.doFailureExecuteISPyBPlugin)
            self.__edPluginExecISPyB.executeSynchronous()


    def doSuccessExecuteISPyBPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.doSuccessExecuteISPyBPlugin")
        self.retrieveSuccessMessages(self.__edPluginExecISPyB, "EDPluginControlISPyBv1_0.doSuccessExecuteISPyBPlugin")


    def doFailureExecuteISPyBPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.doFailureExecuteISPyBPlugin")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlISPyBv1_0.doFailureExecuteISPyBPlugin")
        self.setFailure()


    def postProcess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_0.postProcess")
        # For the moment just an empty result object
        xsDataResultControlISPyB = XSDataResultControlISPyB()
        self.setDataOutput(xsDataResultControlISPyB)



#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr)
#                            Karl Levik (karl.levik@diamond.ac.uk)
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
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from XSDataMXv1         import XSDataInputControlISPyB
from XSDataMXv1         import XSDataResultControlISPyB
from XSDataCommon       import XSDataString

from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

class EDPluginControlISPyBv1_4(EDPluginControl):
    """
    This plugin controls the ISPyB v1.4 execution plugin.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlISPyB)
        self.setXSDataInputClass(XSDataString, "shortComments")
        self.setXSDataInputClass(XSDataString, "comments")
        self.setXSDataInputClass(XSDataString, "statusMessage")
        self.edStringPluginExecISPyBName = "EDPluginISPyBStoreScreeningv1_4"
        self.edPluginExecISPyB = None
        self.strShortComments = None
        self.strComments = None
        self.strStatusMessage = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getCharacterisationResult(), "characterisationResult")


    def preProcess(self, _edObject=None):
        """
        Loads the ISPyB execution plugin and prepares the input data
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.preProcess...")

        if (self.hasDataInput("shortComments")):
            self.strShortComments = self.getDataInput("shortComments")[0].getValue()
        if (self.hasDataInput("comments")):
            self.strComments = self.getDataInput("comments")[0].getValue()
        if (self.hasDataInput("statusMessage")):
            self.strStatusMessage = self.getDataInput("statusMessage")[0].getValue()

        self.edPluginExecISPyB = self.loadPlugin(self.edStringPluginExecISPyBName)
        try:
            xsDataInputISPyBStoreScreening = EDHandlerXSDataISPyBv1_4.generateXSDataInputISPyBStoreScreening(self.getDataInput(), 
                                                                                                             self.strStatusMessage, \
                                                                                                             self.strShortComments, \
                                                                                                             self.strComments)
        except Exception, error:
            raise
            # This exception handling needs to be rethought, see bug #43.
            errorMessage = "EDPluginControlISPyBv1_4.preProcess: Unexpected error in ISPyB handler: %r" % error
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage
        self.edPluginExecISPyB.setDataInput(xsDataInputISPyBStoreScreening)


    def process(self, _edObject=None):
        """
        Executes the ISPyB execution plugin
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.process")
        if (self.edPluginExecISPyB is not None):
            self.edPluginExecISPyB.connectSUCCESS(self.doSuccessExecISPyB)
            self.edPluginExecISPyB.connectFAILURE(self.doFailureExecISPyB)
            self.edPluginExecISPyB.executeSynchronous()


    def doSuccessExecISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.doSuccessExecISPyB")
        self.retrieveSuccessMessages(self.edPluginExecISPyB, "EDPluginControlISPyBv1_4.doSuccessExecISPyB")


    def doFailureExecISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.doFailureExecISPyB")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlISPyBv1_4.doFailureExecISPyB")


    def postProcess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlISPyBv1_4.postProcess")
        # For the moment just an empty result object
        xsDataResultControlISPyB = XSDataResultControlISPyB()
        if self.edPluginExecISPyB.hasDataOutput():
            xsDataResultControlISPyB.screeningId = self.edPluginExecISPyB.dataOutput.screeningId
        self.setDataOutput(xsDataResultControlISPyB)



# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF Grenoble
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
__copyright__ = "2011, ESRF Grenoble"


from EDPluginControl import EDPluginControl
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsSingleSamplev1_0, XSDataResultBioSaxsSingleSamplev1_0

class EDPluginControlSingleSamplev1_0(EDPluginControl):
    """
    Plugin that does the processing a sample: (1 protein at 1 concentration)
    
    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(None)
        self.__strControlledPluginName = "EDPluginControlBioSaxsSmartMergev1_0"
        self.__edPluginExecTemplate = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlSingleSamplev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlSingleSamplev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginExecTemplate = self.loadPlugin(self.__strControlledPluginName)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlSingleSamplev1_0.process")
        self.__edPluginExecTemplate.connectSUCCESS(self.doSuccessExecTemplate)
        self.__edPluginExecTemplate.connectFAILURE(self.doFailureExecTemplate)
        self.__edPluginExecTemplate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlSingleSamplev1_0.postProcess")
        # Create some output data
        xsDataResult = None()
        self.setDataOutput(xsDataResult)


    def doSuccessExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doSuccessExecTemplate")


    def doFailureExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doFailureExecTemplate")

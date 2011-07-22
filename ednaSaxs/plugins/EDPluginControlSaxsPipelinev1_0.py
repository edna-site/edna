# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Thomas Boeglin
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

__author__ = "Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDPluginControl import EDPluginControl
from XSDataEdnaSaxs import XSDataInputSaxsPipeline, XSDataResultSaxsPipeline, XSDataInputAutoRg
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule('XSDataBioSaxsv1_0')
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsReduceFileSeriev1_0


class EDPluginControlSaxsPipelinev1_0(EDPluginControl):
    """
    Execute saxs reduce file serie and pipes it to autoRg.
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsPipeline)
        self.__strControlledPluginReduce = "EDPluginBioSaxsReduceFileSeriev1_0"
        self.__strControlledPluginAutoRg = "EDPluginExecAutoRgv1_0"
        self.__edPluginExecAutoRg = None
        self.__edPluginBioSaxsReduce = None
        self.inputautorg = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginBioSaxsReduce = self.loadPlugin(self.__strControlledPluginReduce)
        self.__edPluginExecAutoRg = self.loadPlugin(self.__strControlledPluginAutoRg)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.process")
        input = XSDataInputBioSaxsReduceFileSeriev1_0.parseString(self.dataInput.marshal())
        self.__edPluginBioSaxsReduce.setDataInput(input)
        self.__edPluginBioSaxsReduce.connectSUCCESS(self.doSuccessReduce)
        self.__edPluginBioSaxsReduce.connectFAILURE(self.doFailureReduce)
        self.__edPluginBioSaxsReduce.executeSynchronous()

        if self.inputautorg is None:
            return
        self.__edPluginExecAutoRg.setDataInput(self.inputautorg)
        self.__edPluginExecAutoRg.connectSUCCESS(self.doSuccessAutoRg)
        self.__edPluginExecAutoRg.connectFAILURE(self.doFailureAutoRg)
        self.__edPluginExecAutoRg.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSaxsPipeline()
        self.setDataOutput(xsDataResult)


    def doSuccessReduce(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.doSuccessReduce")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSaxsPipelinev1_0.doSuccessReduce")
        self.inputautorg = XSDataInputAutoRg(inputCurve=[_edPlugin.dataOutput.mergedCurve])
        self.inputautorg.sample = self.dataInput.sample


    def doFailureReduce(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.doFailureReduce")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSaxsPipelinev1_0.doFailureReduce")
        self.setFailure()

    def doSuccessAutoRg(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.doSuccessAutoRg")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSaxsPipelinev1_0.doSuccessAutoRg")


    def doFailureAutoRg(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsPipelinev1_0.doFailureAutoRg")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSaxsPipelinev1_0.doFailureAutoRg")
        self.setFailure()

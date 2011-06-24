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
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsReduceFileSeriev1_0, XSDataResultBioSaxsReduceFileSeriev1_0, \
    XSDataInputBioSaxsProcessOneFilev1_0, XSDataInputBioSaxsSmartMergev1_0

class EDPluginControlBioSaxsReduceFileSeriev1_0(EDPluginControl):
    """
    Control plugin that does: 
    
    * n times processOneFile
    * synchronize plugins
    * smart merge at the end
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsReduceFileSeriev1_0)
        self.__strControlledPluginName = "EDPluginControlBioSaxsSmartMergev1_0"
        self.__edPluginExecSmartMerge = None

        self.lstCurves = [] #list of 1D curves produced by the data reduction 


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.preProcess")
        # Load the execution plugin



    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.process")





        self.synchronizePlugins()
        xsdMerge = XSDataInputBioSaxsSmartMergev1_0()
        xsdMerge.absoluteSimilarity = self.dataInput.absoluteSimilarity
        xsdMerge.relativeSimilarity = self.dataInput.relativeSimilarity
        self.__edPluginExecSmartMerge = self.loadPlugin(self.__strControlledPluginName)
        self.__edPluginExecSmartMerge.connectSUCCESS(self.doSuccessExecSmartMerge)
        self.__edPluginExecSmartMerge.connectFAILURE(self.doFailureExecSmartMerge)
        self.__edPluginExecSmartMerge.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsReduceFileSeriev1_0()
        self.setDataOutput(xsDataResult)




    def doSuccessExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.doSuccessExecProcessOneFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsReduceFileSeriev1_0.doSuccessExecProcessOneFile")
        self.synchronizeOn()
        curve = _edPlugin.dataOutput.outputCurve
#        TODO
        self.lstCurves.append(object)
        self.synchronizeOff()

    def doFailureExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.doFailureExecProcessOneFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsReduceFileSeriev1_0.doFailureExecProcessOneFile")


    def doSuccessExecSmartMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.doSuccessExecSmartMerge")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsReduceFileSeriev1_0.doSuccessExecSmartMerge")


    def doFailureExecSmartMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsReduceFileSeriev1_0.doFailureExecSmartMerge")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsReduceFileSeriev1_0.doFailureExecSmartMerge")

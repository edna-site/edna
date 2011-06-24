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
from XSDataCommon import XSDataStatus, XSDataString

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF Grenoble"

import os
from EDPluginControl import EDPluginControl
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsSingleSamplev1_0, XSDataResultBioSaxsSingleSamplev1_0

class EDPluginBioSaxsSingleSamplev1_0(EDPluginControl):
    """
    Plugin that does the processing a sample: 
    - 1 protein 
    - 1 concentration
    - 2+ serie of buffer files: each file is individually reduced to 1D data
    - 1+ serie of sample files: each file is individually reduced to 1D data
    
    * Each serie is merged using smart merge
    * All buffer are averages (regardless to radiation damage)
    * All Samples are averages (they are at the same concentration) 
    * buffer is subtracted from sample to obtain the final result
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsSingleSamplev1_0)
        self.__strControlledMerge = "EDPluginBioSaxsSmartMergev1_0"
        self.__strControlledProcessOneFile = "EDPluginBioSaxsProcessOneFilev1_0"
        self.__edPluginMerge = None

        self.strDirectory1D = None
        self.strDirectory2D = None
        self.strDirectoryMisc = None
        self.bufferSeries = [] #list of list of files
        self.sampleSeries = [] #list of list of files
        self.strExecutiveSummary = ""

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlSingleSamplev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.directory1D, "No target Directory for 1D curves provided")
        self.checkMandatoryParameters(self.dataInput.directory2D , "No target Directory for 2D curves provided")
        self.checkMandatoryParameters(self.dataInput.directoryMisc , "No target Directory for Misc data provided")
        self.checkMandatoryParameters(self.dataInput.bufferSeries, "No background file-serie provided")
        self.checkMandatoryParameters(self.dataInput.sampleSeries, "No sample data file-series provided")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlSingleSamplev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginMerge = self.loadPlugin(self.__strControlledMerge)
        self.strDirectory1D = self.dataInput.direcory1D.path.value
        self.strDirectory2D = self.dataInput.direcory2D.path.value
        self.strDirectoryMisc = self.dataInput.direcoryMisc.path.value
        self.bufferSeries = [ [j.path.value for j in i ] for i in  self.dataInput.bufferSeries]
        self.sampleSeries = [ [j.path.value for j in i ] for i in  self.dataInput.sampleSeries]

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
        xsDataResult = XSDataResultBioSaxsSingleSamplev1_0()
        xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(self.strExecutiveSummary))
        self.setDataOutput(xsDataResult)


    def doSuccessExecSubtract(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doSuccessExecSubtract")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doSuccessExecSubtract")


    def doFailureExecSubtract(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doFailureExecSubtract")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doFailureExecSubtract")


    def doSuccessExecMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doSuccessExecMerge")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doSuccessExecMerge")


    def doFailureExecMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doFailureExecMerge")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doFailureExecMerge")


    def doSuccessExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doSuccessExecProcessOneFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doSuccessExecProcessOneFile")


    def doFailureExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSingleSamplev1_0.doFailureExecProcessOneFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSingleSamplev1_0.doFailureExecProcessOneFile")

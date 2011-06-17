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
from EDFactoryPluginStatic import EDFactoryPluginStatic
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsSmartMergev1_0
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsSmartMergev1_0
EDFactoryPluginStatic.loadModule("XSDataAtsas.py")
from XSDataAtsas import XSDataInputDatcmp
from XSDataAtsas import XSDataInputDataver
from XSDataCommon import XSDatadouble, XSDataFile, XSDataString

class EDPluginControlBioSaxsSmartMergev1_0(EDPluginControl):
    """
    This plugin takes a set of input data files (1D SAXS) measure
    their differences (versus previous and versus first) and merge those which are equivalent
    
    Controled plugins:
#     - Execplugin/Accumulator
     - Execplugin/Atsas/DatCmp
     - Execplugin/Atsas/DatAver
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(None)

        self.__strControlledPluginDataver = "EDPluginExecDataverv1_0"
        self.__strControlledPluginDatcmp = "EDPluginExecDatcmpv1_0"
        self.__strControlledPluginName = "EDPluginExecTemplate"
        self.__edPluginExecTemplate = None
        self.__edPluginExecDatcmp = None
        self.__edPluginExecDataver = None
        self.setXSDataInputClass(XSDataInputBioSaxsSmartMergev1_0)
        self.__strControlledPluginDatCmp = ""
        self.__edPluginExecDatCmp = None
        self.lstInput = []
        self.absoluteSimilarity = None
        self.relativeSimilarity = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().inputFile, "Input curve list is empty")
        self.checkMandatoryParameters(self.getDataInput().mergedFile, "Output curve filename  is empty")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginExecTemplate = self.loadPlugin(self.__strControlledPluginName)
        if self.getDataInput().absoluteSimilarity is not None:
            self.absoluteSimilarity = self.getDataInput().absoluteSimilarity.value
        if self.getDataInput().relativeSimilarity is not None:
            self.absoluteSimilarity = self.getDataInput().relativeSimilarity.value
        self.lstInput = self.getDataInput().inputFile

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.process")
        lstFile = []
        if (self.absoluteSimilarity is None) and (self.relativeSimilarity is None):
            lstFile = self.lstInput
        else:
            if self.absoluteSimilarity is None :
            lstFile

        if len(lstFile) > 1:
            self.__edPluginExecDataver = self.loadPlugin(self.__strControlledPluginDataver)
            xsd = XSDataInputDataver(outputCurve=self.getDataInput().mergedFile,
                                    inputCurve=lstFile)
            self.__edPluginExecDataver.setDataInput(xsd)
            self.__edPluginExecDataver.connectSUCCESS(self.doSuccessExecDataver)
            self.__edPluginExecDataver.connectFAILURE(self.doFailureExecDataver)
            self.__edPluginExecDataver.executeSynchronous()
        else:
            shutil.copy_file(lstFile[0].path.value, self.getDataInput().mergedFile.path.value)

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsSmartMergev1_0()
        xsDataResult.mergedFile = self.getDataInput().mergedFile
        self.setDataOutput(xsDataResult)

    def doSuccessExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecDataver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecDataver")


    def doFailureExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doFailureExecDataver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doFailureExecDataver")

    def doSuccessExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecDatcmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecDatcmp")


    def doFailureExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doFailureExecDatcmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doFailureExecDatcmp")

    def doSuccessExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doSuccessExecTemplate")


    def doFailureExecTemplate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsSmartMergev1_0.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsSmartMergev1_0.doFailureExecTemplate")

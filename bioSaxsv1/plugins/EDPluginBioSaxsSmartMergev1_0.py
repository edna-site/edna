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
EDFactoryPluginStatic.loadModule("XSDataAtsas")
from XSDataAtsas import XSDataInputDatcmp
from XSDataAtsas import XSDataInputDataver
from XSDataCommon import XSDataDouble, XSDataFile, XSDataString

class EDPluginBioSaxsSmartMergev1_0(EDPluginControl):
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
        self.__strControlledPluginDataver = "EDPluginExecDataverv1_0"
        self.__strControlledPluginDatcmp = "EDPluginExecDatcmpv1_0"
        self.__edPluginExecDatcmp = None
        self.__edPluginExecDataver = None
        self.setXSDataInputClass(XSDataInputBioSaxsSmartMergev1_0)
        self.__edPluginExecDatCmp = None
        self.lstInput = []
        self.lstXsdInput = []
        self.absoluteSimilarity = None
        self.relativeSimilarity = None
        self.dictSimilarities = {} #key: 2-tuple of images, similarities


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().inputFile, "Input curve list is empty")
        self.checkMandatoryParameters(self.getDataInput().mergedCurve, "Output curve filename  is empty")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.preProcess")
        # Load the execution plugin
        if self.getDataInput().absoluteSimilarity is not None:
            self.absoluteSimilarity = self.getDataInput().absoluteSimilarity.value
        if self.getDataInput().relativeSimilarity is not None:
            self.relativeSimilarity = self.getDataInput().relativeSimilarity.value
        self.lstInput = self.getDataInput().inputFile
        self.lstStrInput = [i.path.value for i in self.lstInput]


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.process")
        if len(self.lstInput) == 1:
            shutil.copy_file(self.lstInput[0].path.value, self.getDataInput().mergedCurve.path.value)
        else:
            lstFile = []
            if (self.absoluteSimilarity is None) and (self.relativeSimilarity is None):
                lstFile = self.lstInput
            else:
                if self.absoluteSimilarity is not None :
                    for oneFile in self.lstInput[1:]:
                        edPluginExecAbsoluteSimilarity = self.loadPlugin(self.__strControlledPluginDatcmp)
                        xsd = XSDataInputDatcmp(inputCurve=[self.lstInput[0], oneFile])
                        edPluginExecAbsoluteSimilarity.setDataInput(xsd)
                        edPluginExecAbsoluteSimilarity.connectFAILURE(self.doFailureExecDatcmp)
                        edPluginExecAbsoluteSimilarity.connectSUCCESS(self.doSuccessExecDatcmp)
                        edPluginExecAbsoluteSimilarity.execute()
                if (self.relativeSimilarity is not None) and (len(self.lstInput) > 2):
                    for idx, oneFile in enumerate(self.lstInput[2:]):
                        edPluginExecRelativeSimilarity = self.loadPlugin(self.__strControlledPluginDatcmp)
                        xsd = XSDataInputDatcmp(inputCurve=[self.lstInput[idx + 1], oneFile])
                        edPluginExecRelativeSimilarity.setDataInput(xsd)
                        edPluginExecRelativeSimilarity.connectFAILURE(self.doFailureExecDatcmp)
                        edPluginExecRelativeSimilarity.connectSUCCESS(self.doSuccessExecDatcmp)
                        edPluginExecRelativeSimilarity.execute()
            self.synchronizePlugins()

            for idx, oneFile in enumerate(self.lstInput):
                if idx == 0:
                    lstFile.append(oneFile)
                elif (self.absoluteSimilarity is not None) and (self.absoluteSimilarity is not None):
                    if (self.dictSimilarities[(0, idx)] >= self.absoluteSimilarity) and (self.dictSimilarities[(idx - 1, idx)] >= self.relativeSimilarity):
                        lstFile.append(oneFile)
                    else:
                        break
                elif (self.absoluteSimilarity is not None) :
                    if (self.dictSimilarities[(0, idx)] >= self.absoluteSimilarity):
                        lstFile.append(oneFile)
                    else:
                        break
                elif (self.relativeSimilarity is not None) :
                    if (self.dictSimilarities[(idx - 1, idx)] >= self.relativeSimilarity):
                        lstFile.append(oneFile)
                    else:
                        break
                else:
                    lstFile.append(oneFile)

            self.__edPluginExecDataver = self.loadPlugin(self.__strControlledPluginDataver)
            xsd = XSDataInputDataver(outputCurve=self.getDataInput().mergedCurve,
                                    inputCurve=lstFile)
            self.__edPluginExecDataver.setDataInput(xsd)
            self.__edPluginExecDataver.connectSUCCESS(self.doSuccessExecDataver)
            self.__edPluginExecDataver.connectFAILURE(self.doFailureExecDataver)
            self.__edPluginExecDataver.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsSmartMergev1_0()
        xsDataResult.mergedCurve = self.getDataInput().mergedCurve
        self.setDataOutput(xsDataResult)


    def doSuccessExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.doSuccessExecDataver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_0.doSuccessExecDataver")



    def doFailureExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.doFailureExecDataver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_0.doFailureExecDataver")


    def doSuccessExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.doSuccessExecDatcmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_0.doSuccessExecDatcmp")
        self.synchronizeOn()
        xsdIn = _edPlugin.getDataInput()
        xsdOut = _edPlugin.getDataOutput()
        self.dictSimilarities[tuple([self.lstStrInput.index(i.path.value) for i in xsdIn.inputCurve])] = xsdOut.fidelity.value
        self.synchronizeOff()

    def doFailureExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_0.doFailureExecDatcmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_0.doFailureExecDatcmp")



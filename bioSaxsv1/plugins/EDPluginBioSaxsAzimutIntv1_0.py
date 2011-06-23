# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:    Jérôme Kieffer
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
__copyright__ = "ESRF"

from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataString
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsAzimutIntv1_0, XSDataResultBioSaxsAzimutIntv1_0, \
                               XSDataInputBioSaxsAsciiExportv1_0, XSDataResultBioSaxsAsciiExportv1_0, \
                               XSDataInputBioSaxsMetadatav1_0, XSDataResultBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataSaxsv1_0         import XSDataInputSaxsAddv1_0, XSDataInputSaxsAnglev1_0



class EDPluginBioSaxsAzimutIntv1_0(EDPluginControl):
    """
    Control for Bio Saxs azimuthal integration: 
    * wait for normalized file to arrive  (EDPluginWaitFile) 
    * retrieve and update metadata (EDPluginBioSaxsMetadatav1_1)
    * apply mask (EDPluginSaxsAddv1_0)
    * Write metadata (EDPluginBioSaxsMetadatav1_1)
    * integrate (EDPluginSaxsAnglev1_0)
    * export as spec-file (EDPluginAsciiExportv1_0)    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAzimutIntv1_0)
        self.__strControlledPluginWaitFile = "EDPluginWaitFile"
        self.__strControlledPluginSaxsAdd = "EDPluginExecSaxsAddv1_0"
        self.__strControlledPluginSaxsAngle = "EDPluginExecSaxsAnglev1_0"
        self.__strControlledPluginAsciiExport = "EDPluginBioSaxsAsciiExportv1_0"
        self.__strControlledPluginSaxsGetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__strControlledPluginSaxsSetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginWaitFile = None
        self.__edPluginSaxsAdd = None
        self.__edPluginSaxsAngle = None
        self.__edPluginAsciiExport = None
        self.__edPluginSaxsGetMetadata = None
        self.__edPluginSaxsSetMetadata = None

        self.xsdMetadata = None

        self.normalizedImage = None
        self.integratedImage = None
        self.integratedCurve = None
        self.normalizationFactor = None
        self.correctedImage = None

        self.strProcessLog = ""
        self.xsdResult = XSDataResultBioSaxsAzimutIntv1_0()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getNormalizedImage(), "Missing normalizedImage")
        self.checkMandatoryParameters(self.getDataInput().getNormalizedImageSize(), "Missing normalizedImageSize")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedImage(), "Missing integratedImage")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedCurve(), "Missing integratedCurve")
        self.checkMandatoryParameters(self.getDataInput().getCorrectedImage(), "Missing correctedImage")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.preProcess")
        # Load the execution plugins
        self.__edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
        self.__edPluginSaxsAdd = self.loadPlugin(self.__strControlledPluginSaxsAdd)
        self.__edPluginSaxsAngle = self.loadPlugin(self.__strControlledPluginSaxsAngle)
        self.__edPluginAsciiExport = self.loadPlugin(self.__strControlledPluginAsciiExport)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.__edPluginSaxsSetMetadata = self.loadPlugin(self.__strControlledPluginSaxsSetMetadata)

        self.normalizedImage = self.getDataInput().getNormalizedImage().getPath().getValue()
        self.correctedImage = self.getDataInput().getCorrectedImage().getPath().getValue()
        self.integratedImage = self.getDataInput().getIntegratedImage().getPath().getValue()
        self.integratedCurve = self.getDataInput().getIntegratedCurve().getPath().getValue()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.process")
        xsdiWaitFile = XSDataInputWaitFile()
        xsdiWaitFile.setExpectedFile(self.getDataInput().getNormalizedImage())
        xsdiWaitFile.setExpectedSize(self.getDataInput().getNormalizedImageSize())
        self.__edPluginWaitFile.setDataInput(xsdiWaitFile)
        self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        if not self.isFailure():
            self.__edPluginWaitFile.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSuccessGetMetadata)
            self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
            self.__edPluginSaxsGetMetadata.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsAdd.connectSUCCESS(self.doSuccessSaxsAdd)
            self.__edPluginSaxsAdd.connectFAILURE(self.doFailureSaxsAdd)
            self.__edPluginSaxsAdd.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsSetMetadata.connectSUCCESS(self.doSuccessSetMetadata)
            self.__edPluginSaxsSetMetadata.connectFAILURE(self.doFailureSetMetadata)
            self.__edPluginSaxsSetMetadata.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsAngle.connectSUCCESS(self.doSuccessSaxsAngle)
            self.__edPluginSaxsAngle.connectFAILURE(self.doFailureSaxsAngle)
            self.__edPluginSaxsAngle.executeSynchronous()
        if not self.isFailure():
            self.__edPluginAsciiExport.connectSUCCESS(self.doSuccessAsciiExport)
            self.__edPluginAsciiExport.connectFAILURE(self.doFailureAsciiExport)
            self.__edPluginAsciiExport.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.postProcess")

        #remove the terminal carriage return
        if self.strProcessLog.endswith("\n"):
           self.strProcessLog = self.strProcessLog[:-1]
        # Create some output data
        self.xsdResult.setProcessLog(XSDataString(self.strProcessLog))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("Comment generated ...\n" + self.strProcessLog)


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessWaitFile")

        self.strProcessLog += "Retrieve metadata from file %s\n" % (self.normalizedImage)
        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.getDataInput().getNormalizedImage())
        xsdiMetadata.setSampleConcentration(self.getDataInput().getSampleConcentration())
        xsdiMetadata.setSampleComments(self.getDataInput().getSampleComments())
        xsdiMetadata.setSampleCode(self.getDataInput().getSampleCode())
        xsdiMetadata.setDetector(self.getDataInput().getDetector())
        xsdiMetadata.setDetectorDistance(self.getDataInput().getDetectorDistance())
        xsdiMetadata.setPixelSize_1(self.getDataInput().getPixelSize_1())
        xsdiMetadata.setPixelSize_2(self.getDataInput().getPixelSize_2())
        xsdiMetadata.setBeamCenter_1(self.getDataInput().getBeamCenter_1())
        xsdiMetadata.setBeamCenter_2(self.getDataInput().getBeamCenter_2())
        xsdiMetadata.setWavelength(self.getDataInput().getWavelength())
        xsdiMetadata.setMachineCurrent(self.getDataInput().getMachineCurrent())
        xsdiMetadata.setMaskFile(self.getDataInput().getMaskFile())
        xsdiMetadata.setNormalizationFactor(self.getDataInput().getNormalizationFactor())
        self.__edPluginSaxsGetMetadata.setDataInput(xsdiMetadata)


    def doFailureWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureWaitFile")
        self.strProcessLog += "Timeout in waiting for file '%s'\n" % (self.normalizedImage)
        self.setFailure()


    def doSuccessGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessGetMetadata")
        self.strProcessLog += "Correcting EDF image '%s' with mask file\n" % (self.normalizedImage)
        self.xsdMetadata = _edPlugin.getDataOutput()
        xsdiSaxsAdd = XSDataInputSaxsAddv1_0()
        xsdiSaxsAdd.setInputImage([self.getDataInput().getNormalizedImage(), self.xsdMetadata.getMaskFile()])
        xsdiSaxsAdd.setOutputImage(self.getDataInput().getCorrectedImage())
        xsdiSaxsAdd.setOptions(XSDataString('+pass  -omod n '))
        self.__edPluginSaxsAdd.setDataInput(xsdiSaxsAdd)


    def doFailureGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureGetMetadata")
        self.strProcessLog += "Failure in GetMetadata retrival from '%s'\n" % (self.normalizedImage)
        self.setFailure()


    def doSuccessSaxsAdd(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessSaxsAdd")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessSaxsAdd")
        self.xsdResult.setCorrectedImage(self.getDataInput().getCorrectedImage())
        self.strProcessLog += "Appending metadata to Corrected EDF image '%s'.\n" % (self.correctedImage)

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.getDataInput().getCorrectedImage())
        xsdiMetadata.setOutputImage(self.getDataInput().getCorrectedImage())
        xsdiMetadata.setSampleConcentration(self.xsdMetadata.getSampleConcentration())
        xsdiMetadata.setSampleComments(self.xsdMetadata.getSampleComments())
        xsdiMetadata.setSampleCode(self.xsdMetadata.getSampleCode())
        xsdiMetadata.setDetector(self.xsdMetadata.getDetector())
        xsdiMetadata.setDetectorDistance(self.xsdMetadata.getDetectorDistance())
        xsdiMetadata.setPixelSize_1(self.xsdMetadata.getPixelSize_1())
        xsdiMetadata.setPixelSize_2(self.xsdMetadata.getPixelSize_2())
        xsdiMetadata.setBeamCenter_1(self.xsdMetadata.getBeamCenter_1())
        xsdiMetadata.setBeamCenter_2(self.xsdMetadata.getBeamCenter_2())
        xsdiMetadata.setWavelength(self.xsdMetadata.getWavelength())
        xsdiMetadata.setMachineCurrent(self.xsdMetadata.getMachineCurrent())
        xsdiMetadata.setMaskFile(self.xsdMetadata.getMaskFile())
        xsdiMetadata.setNormalizationFactor(self.xsdMetadata.getNormalizationFactor())
        self.__edPluginSaxsSetMetadata.setDataInput(xsdiMetadata)


    def doFailureSaxsAdd(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAdd")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAdd")
        self.strProcessLog += "Error during the call to saxs_add, unable to produce '%s'\n" % (self.correctedImage)
        self.setFailure()


    def doSuccessSetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessSetMetadata")
        self.xsdMetadata = _edPlugin.getDataOutput()
        self.strProcessLog += "Azimuthal integration of Corrected EDF image '%s'.\n" % (self.correctedImage)
        xsdiSaxsAngle = XSDataInputSaxsAnglev1_0()
        xsdiSaxsAngle.setInputDataFile(self.getDataInput().getCorrectedImage())
        xsdiSaxsAngle.setRegroupedDataFile(self.getDataInput().getIntegratedImage())
        xsdiSaxsAngle.setOptions(XSDataString('+pass -omod n -rsys normal -da 360_deg -odim = 1'))
        self.__edPluginSaxsAngle.setDataInput(xsdiSaxsAngle)


    def doFailureSetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureSetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureSetMetadata")
        self.strProcessLog += "Failure in appending metadata to '%s'\n" % (self.correctedImage)
        self.setFailure()


    def doSuccessSaxsAngle(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessSaxsAngle")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessSaxsAngle")
        self.xsdResult.setIntegratedImage(self.getDataInput().getIntegratedImage())
        self.strProcessLog += "Conversion to spec-like file of '%s'\n" % (self.integratedImage)
        xsdiAsciiExport = XSDataInputBioSaxsAsciiExportv1_0()
        xsdiAsciiExport.setIntegratedImage(self.getDataInput().getIntegratedImage())
        xsdiAsciiExport.setIntegratedCurve(self.getDataInput().getIntegratedCurve())
        self.__edPluginAsciiExport.setDataInput(xsdiAsciiExport)


    def doFailureSaxsAngle(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAngle")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAngle")
        self.strProcessLog += "Error during integration with saxs_angle on '%s'\n" % (self.integratedImage)
        self.setFailure()


    def doSuccessAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessAsciiExport")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessAsciiExport")
        self.xsdResult.setIntegratedCurve(self.getDataInput().getIntegratedCurve())
        self.strProcessLog += _edPlugin.getDataOutput().getProcessLog().getValue()


    def doFailureAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureAsciiExport")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureAsciiExport")
        self.strProcessLog += _edPlugin.getDataOutput().getProcessLog().getValue()
        self.setFailure()

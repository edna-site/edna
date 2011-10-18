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
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20111013"
__status__ = "deprecated"

from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataString, XSDataStatus, XSDataFile
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
        self.sample = None
        self.exprimentSetup = None
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
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.normalizedImage, "Missing normalizedImage")
        self.checkMandatoryParameters(self.dataInput.getNormalizedImageSize(), "Missing normalizedImageSize")
        self.checkMandatoryParameters(self.dataInput.getIntegratedImage(), "Missing integratedImage")
        self.checkMandatoryParameters(self.dataInput.getIntegratedCurve(), "Missing integratedCurve")
        self.checkMandatoryParameters(self.dataInput.getCorrectedImage(), "Missing correctedImage")
        self.checkMandatoryParameters(self.dataInput.sample, "Missing sample description")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "Missing experiment setup")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.preProcess")
        self.sample = self.dataInput.sample
        self.exprimentSetup = self.dataInput.experimentSetup
        # Load the execution plugins

        self.__edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
        self.__edPluginSaxsAdd = self.loadPlugin(self.__strControlledPluginSaxsAdd)
        self.__edPluginSaxsAngle = self.loadPlugin(self.__strControlledPluginSaxsAngle)
        self.__edPluginAsciiExport = self.loadPlugin(self.__strControlledPluginAsciiExport)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.__edPluginSaxsSetMetadata = self.loadPlugin(self.__strControlledPluginSaxsSetMetadata)

        self.normalizedImage = self.dataInput.normalizedImage.getPath().value
        self.correctedImage = self.dataInput.getCorrectedImage().getPath().value
        self.integratedImage = self.dataInput.getIntegratedImage().getPath().value
        self.integratedCurve = self.dataInput.getIntegratedCurve().getPath().value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.process")
        xsdiWaitFile = XSDataInputWaitFile(expectedFile=XSDataFile(self.dataInput.normalizedImage.path),
                                           expectedSize=self.dataInput.normalizedImageSize)
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
        self.xsdResult.setStatus(XSDataStatus(executiveSummary=XSDataString(self.strProcessLog)))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("Comment generated ...\n" + self.strProcessLog)


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessWaitFile")

        self.strProcessLog += "Retrieve metadata from file %s\n" % (self.normalizedImage)
        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.dataInput.normalizedImage)
        xsdiMetadata.setConcentration(self.sample.concentration)
        xsdiMetadata.setComments(self.sample.comments)
        xsdiMetadata.setCode(self.sample.code)
        xsdiMetadata.setDetector(self.exprimentSetup.getDetector())
        xsdiMetadata.setDetectorDistance(self.exprimentSetup.detectorDistance)
        xsdiMetadata.setPixelSize_1(self.exprimentSetup.pixelSize_1)
        xsdiMetadata.setPixelSize_2(self.exprimentSetup.pixelSize_2)
        xsdiMetadata.setBeamCenter_1(self.exprimentSetup.beamCenter_1)
        xsdiMetadata.setBeamCenter_2(self.exprimentSetup.beamCenter_2)
        xsdiMetadata.setWavelength(self.exprimentSetup.wavelength)
        xsdiMetadata.setMachineCurrent(self.exprimentSetup.machineCurrent)
        xsdiMetadata.setMaskFile(self.exprimentSetup.maskFile)
        xsdiMetadata.setNormalizationFactor(self.exprimentSetup.normalizationFactor)
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
        xsdiSaxsAdd.setInputImage([self.dataInput.normalizedImage, self.xsdMetadata.maskFile])
        xsdiSaxsAdd.setOutputImage(self.dataInput.getCorrectedImage())
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
        self.xsdResult.setCorrectedImage(self.dataInput.getCorrectedImage())
        self.strProcessLog += "Appending metadata to Corrected EDF image '%s'.\n" % (self.correctedImage)

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.dataInput.getCorrectedImage())
        xsdiMetadata.setOutputImage(self.dataInput.getCorrectedImage())
        xsdiMetadata.setConcentration(self.xsdMetadata.concentration)
        xsdiMetadata.setComments(self.xsdMetadata.comments)
        xsdiMetadata.setCode(self.xsdMetadata.code)
        xsdiMetadata.setDetector(self.xsdMetadata.getDetector())
        xsdiMetadata.setDetectorDistance(self.xsdMetadata.detectorDistance)
        xsdiMetadata.setPixelSize_1(self.xsdMetadata.pixelSize_1)
        xsdiMetadata.setPixelSize_2(self.xsdMetadata.pixelSize_2)
        xsdiMetadata.setBeamCenter_1(self.xsdMetadata.beamCenter_1)
        xsdiMetadata.setBeamCenter_2(self.xsdMetadata.beamCenter_2)
        xsdiMetadata.setWavelength(self.xsdMetadata.wavelength)
        xsdiMetadata.setMachineCurrent(self.xsdMetadata.machineCurrent)
        xsdiMetadata.setMaskFile(self.xsdMetadata.maskFile)
        xsdiMetadata.setNormalizationFactor(self.xsdMetadata.normalizationFactor)
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
        xsdiSaxsAngle.setInputDataFile(self.dataInput.getCorrectedImage())
        xsdiSaxsAngle.setRegroupedDataFile(self.dataInput.getIntegratedImage())
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
        self.xsdResult.setIntegratedImage(self.dataInput.getIntegratedImage())
        self.strProcessLog += "Conversion to spec-like file of '%s'\n" % (self.integratedImage)
        xsdiAsciiExport = XSDataInputBioSaxsAsciiExportv1_0()
        xsdiAsciiExport.setIntegratedImage(self.dataInput.getIntegratedImage())
        xsdiAsciiExport.setIntegratedCurve(self.dataInput.getIntegratedCurve())
        self.__edPluginAsciiExport.setDataInput(xsdiAsciiExport)


    def doFailureSaxsAngle(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAngle")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureSaxsAngle")
        self.strProcessLog += "Error during integration with saxs_angle on '%s'\n" % (self.integratedImage)
        self.setFailure()


    def doSuccessAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doSuccessAsciiExport")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doSuccessAsciiExport")
        self.xsdResult.setIntegratedCurve(self.dataInput.getIntegratedCurve())
        self.strProcessLog += _edPlugin.getDataOutput().getProcessLog().value


    def doFailureAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureAsciiExport")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureAsciiExport")
        self.strProcessLog += _edPlugin.getDataOutput().getProcessLog().value
        self.setFailure()

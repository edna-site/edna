#
#coding: utf8
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

import os, sys, shutil
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon       import XSDataString, XSDataBoolean, XSDataImage, \
                            XSDataDouble, XSDataFile, XSDataTime
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsAveragev1_0, XSDataResultBioSaxsAveragev1_0, \
                            XSDataInputBioSaxsAsciiExportv1_0, \
                            XSDataInputBioSaxsMetadatav1_0, XSDataResultBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitMultiFile
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataSaxsv1_0     import XSDataInputSaxsMacv1_0

class EDPluginBioSaxsAveragev1_0(EDPluginControl):
    """
    Control for Bio Saxs Averaging of spectra in : 
    * wait for azimuthally integrated files to arrive  (EDPluginWaitMultiFile) 
    * sum & divide spectra (EDPluginSaxsMCv1_0)
    * export as spec-file (EDPluginBioSaxsAsciiExportv1_0)    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAveragev1_0)
        self.__strControlledPluginWaitMultiFile = "EDPluginWaitMultiFile"
        self.__strControlledPluginSaxsMac = "EDPluginExecSaxsMacv1_0"
        self.__strControlledPluginAsciiExport = "EDPluginBioSaxsAsciiExportv1_0"
        self.__strControlledPluginSaxsGetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__strControlledPluginSaxsSetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginWaitMultiFile = None
        self.__edPluginSaxsMac = None
        self.__edPluginAsciiExport = None
        self.__edPluginSaxsGetMetadata = None
        self.__edPluginSaxsSetMetadata = None

        self.xsdMetadata = None

        self.averagedImage = None
        self.integratedImages = []
        self.averagedCurve = None
        self.normalizationFactor = None
        self.correctedImage = None
        self.concentration = None
        self.comments = None
        self.code = None

        self.strLogFile = None
        self.strProcessLog = ""
        self.xsdResult = XSDataResultBioSaxsAveragev1_0()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.getIntegratedImage(), "Missing IntegratedImage")
        self.checkMandatoryParameters(self.dataInput.getIntegratedImageSize(), "Missing IntegratedImageSize")
        self.checkMandatoryParameters(self.dataInput.getAveragedImage(), "Missing AveragedImage")
        self.checkMandatoryParameters(self.dataInput.getAveragedCurve(), "Missing AveragedCurve")
        self.checkMandatoryParameters(self.dataInput.getLogFile(), "Missing log File")



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.preProcess")
        # Load the execution plugins
        self.__edPluginWaitMultiFile = self.loadPlugin(self.__strControlledPluginWaitMultiFile)
        self.__edPluginSaxsMac = self.loadPlugin(self.__strControlledPluginSaxsMac)
        self.__edPluginAsciiExport = self.loadPlugin(self.__strControlledPluginAsciiExport)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.__edPluginSaxsSetMetadata = self.loadPlugin(self.__strControlledPluginSaxsSetMetadata)

        self.integratedImages = [ oneImage.getPath().value for oneImage in self.dataInput.getIntegratedImage()]

        self.averagedImage = self.dataInput.getAveragedImage().getPath().value
        self.averagedCurve = self.dataInput.getAveragedCurve().getPath().value
        self.strLogFile = self.dataInput.getLogFile().getPath().value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.process")


        xsdiWaitMultiFile = XSDataInputWaitMultiFile(expectedFile=[XSDataFile(i.path) for i in self.dataInput.integratedImage],
                                                     expectedSize=self.dataInput.integratedImageSize,
                                                     timeOut=XSDataTime(30))
        self.__edPluginWaitMultiFile.setDataInput(xsdiWaitMultiFile)
        self.__edPluginWaitMultiFile.connectSUCCESS(self.doSuccessWaitMultiFile)
        self.__edPluginWaitMultiFile.connectFAILURE(self.doFailureWaitMultiFile)
        self.__edPluginWaitMultiFile.executeSynchronous ()

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.postProcess")

        #remove the terminal carriage return
        if self.strProcessLog.endswith("\n"):
           self.strProcessLog = self.strProcessLog[:-1]
        # Create some output data
        self.xsdResult.setProcessLog(XSDataString(self.strProcessLog))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("Comment generated ...\n" + self.strProcessLog)


    def doSuccessWaitMultiFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doSuccessWaitMultiFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doSuccessWaitMultiFile")

        self.strProcessLog += "Retrieve metadata from file %s\n" % (self.integratedImages[0])
        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.dataInput.getIntegratedImage()[0])
        xsdiMetadata.setConcentration(self.dataInput.concentration)
        xsdiMetadata.setComments(self.dataInput.comments)
        xsdiMetadata.setCode(self.dataInput.code)
        xsdiMetadata.setDetector(self.dataInput.getDetector())
        xsdiMetadata.setDetectorDistance(self.dataInput.detectorDistance)
        xsdiMetadata.setPixelSize_1(self.dataInput.pixelSize_1)
        xsdiMetadata.setPixelSize_2(self.dataInput.pixelSize_2)
        xsdiMetadata.setBeamCenter_1(self.dataInput.beamCenter_1)
        xsdiMetadata.setBeamCenter_2(self.dataInput.beamCenter_2)
        xsdiMetadata.setWavelength(self.dataInput.wavelength)
        xsdiMetadata.setMachineCurrent(self.dataInput.machineCurrent)
        xsdiMetadata.setMaskFile(self.dataInput.maskFile)
        xsdiMetadata.setNormalizationFactor(self.dataInput.normalizationFactor)
        self.__edPluginSaxsGetMetadata.setDataInput(xsdiMetadata)
        self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSucessGetMetadata)
        self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
        self.__edPluginSaxsGetMetadata.executeSynchronous()


    def doFailureWaitMultiFile(self, _edPlugin=None):
        self.synchronizeOn()
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureWaitMultiFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureWaitMultiFile")
        self.strProcessLog += "Timeout in waiting for file '%s'\n" % (_edPlugin.dataInput.getExpectedFile().getPath().value)
        EDVerbose.DEBUG("XSDataResult from EDPluginWaitMultiFile that failed: \n%s" % _edPlugin.getDataOutput().marshal())
        self.synchronizeOff()
        self.setFailure()


    def doSucessGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doSuccessGetMetadata")
#        self.strProcessLog += "Averaging EDF images to '%s'\n" % (self.averagedImage)
        self.xsdMetadata = _edPlugin.getDataOutput()

        xsdSaxsMac = XSDataInputSaxsMacv1_0()
        prefix = os.path.commonprefix(self.integratedImages)
        listFilesReversed = []
        for oneFile in self.integratedImages:
            revLst = list(oneFile)
            revLst.reverse()
            listFilesReversed.append("".join(revLst))
        revLst = list(os.path.commonprefix(listFilesReversed))
        revLst.reverse()
        suffix = "".join(revLst)
        lenSuffix = len(suffix)
        lenPrefix = len(prefix)
        maxdif = 0
        maxInt = 0
        miniInt = sys.maxint
        for oneFile in self.integratedImages:
            lenOneFile = len(oneFile)
            if lenOneFile - lenSuffix - lenPrefix > maxdif:
                maxdif = lenOneFile - lenSuffix - lenPrefix
            try:
                val = int(oneFile[lenPrefix:-lenSuffix])
            except Exception:
                val = None
                pass
            if val is not None:
                if val < miniInt:
                    miniInt = val
                if val > maxInt:
                    maxInt = val
        strImages = prefix + """%""" * maxdif + suffix + ",%i,%i" % (miniInt, maxInt)
        self.strProcessLog += "Averaging images '%s' to %s\n" % (strImages, self.averagedImage)
        EDVerbose.DEBUG("Averaging '%s'\n" % (strImages))
        xsdImage = XSDataImage()
        xsdImage.setPath(XSDataString(strImages))
        xsdiSaxsMac = XSDataInputSaxsMacv1_0()
        xsdiSaxsMac.setInputImage(xsdImage)
        xsdiSaxsMac.setOutputImage(self.dataInput.getAveragedImage())
        xsdiSaxsMac.setOptions(XSDataString("+pass -omod n +var -add %d" % len(self.integratedImages)))
        xsdiSaxsMac.setMultConst(XSDataDouble(1.0 / len(self.integratedImages)))
        self.__edPluginSaxsMac.setDataInput(xsdiSaxsMac)
        self.__edPluginSaxsMac.connectSUCCESS(self.doSuccessSaxsMac)
        self.__edPluginSaxsMac.connectFAILURE(self.doFailureSaxsMac)
        self.__edPluginSaxsMac.executeSynchronous()

    def doFailureGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureGetMetadata")
        self.strProcessLog += "Failure in GetMetadata retrival from '%s'\n" % (self.integratedImages[0])
        self.setFailure()




    def doSuccessSaxsMac(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doSuccessSaxsMac")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doSuccessSaxsMac")
        strEdnaLogFile = os.path.join(_edPlugin.getWorkingDirectory(), _edPlugin.getScriptLogFileName())
        EDVerbose.DEBUG("ExecPlugin log file is in: %s" % strEdnaLogFile)
        if os.path.isfile(strEdnaLogFile):
            shutil.copy(strEdnaLogFile, self.strLogFile)
            xsLogFile = XSDataFile()
            xsLogFile.setPath(XSDataString(self.strLogFile))
            self.xsdResult.setLogFile(xsLogFile)

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.dataInput.getAveragedImage())
        xsdiMetadata.setOutputImage(self.dataInput.getAveragedImage())
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
        self.__edPluginSaxsSetMetadata.connectSUCCESS(self.doSuccessSetMetadata)
        self.__edPluginSaxsSetMetadata.connectFAILURE(self.doFailureSetMetadata)
        self.__edPluginSaxsSetMetadata.executeSynchronous()



    def doFailureSaxsMac(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureSaxsMac")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureSaxsMac")
        self.strProcessLog += "Error during averaging of images with saxs_angle on '%s'\n" % (self.averagedImage)
        self.setFailure()

    def doSuccessSetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doSuccessSetMetadata")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doSuccessSetMetadata")

        self.xsdResult.setAveragedImage(self.dataInput.getAveragedImage())
        self.strProcessLog += "Conversion to 3-column ascii file: '%s'\n" % (self.averagedCurve)
        xsdiAsciiExport = XSDataInputBioSaxsAsciiExportv1_0()
        xsdiAsciiExport.setIntegratedImage(self.dataInput.getAveragedImage())
        xsdiAsciiExport.setIntegratedCurve(self.dataInput.getAveragedCurve())
        self.__edPluginAsciiExport.setDataInput(xsdiAsciiExport)
        self.__edPluginAsciiExport.connectSUCCESS(self.doSuccessAsciiExport)
        self.__edPluginAsciiExport.connectFAILURE(self.doFailureAsciiExport)
        self.__edPluginAsciiExport.executeSynchronous()


    def doFailureSetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureSetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureSetMetadata")
        self.strProcessLog += "Failure in appending metadata to '%s'\n" % (self.averagedImage)
        self.setFailure()


    def doSuccessAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doSuccessAsciiExport")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doSuccessAsciiExport")
        self.xsdResult.setAveragedCurve(self.dataInput.getAveragedCurve())
#        self.strProcessLog += "Successful Execution of EDPlugin BioSaxs Average v1_0"

    def doFailureAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureAsciiExport")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureAsciiExport")
        self.strProcessLog += "Error during the call of saxs_curves for the production of '%s'\n" % (self.averagedCurve)
        self.setFailure()


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
    XSDataFloat, XSDataFile
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
        self.averagedSpectrum = None
        self.normalizationFactor = None
        self.correctedImage = None
        self.sampleConcentration = None
        self.sampleComments = None
        self.sampleCode = None

        self.strLogFile = None
        self.strProcessLog = ""
        self.xsdResult = XSDataResultBioSaxsAveragev1_0()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedImage(), "Missing IntegratedImage")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedImageSize(), "Missing IntegratedImageSize")
        self.checkMandatoryParameters(self.getDataInput().getAveragedImage(), "Missing AveragedImage")
        self.checkMandatoryParameters(self.getDataInput().getAveragedSpectrum(), "Missing AveragedSpectrum")
        self.checkMandatoryParameters(self.getDataInput().getLogFile(), "Missing log File")



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.preProcess")
        # Load the execution plugins
        self.__edPluginWaitMultiFile = self.loadPlugin(self.__strControlledPluginWaitMultiFile)
        self.__edPluginSaxsMac = self.loadPlugin(self.__strControlledPluginSaxsMac)
        self.__edPluginAsciiExport = self.loadPlugin(self.__strControlledPluginAsciiExport)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.__edPluginSaxsSetMetadata = self.loadPlugin(self.__strControlledPluginSaxsSetMetadata)

        self.integratedImages = [ oneImage.getPath().getValue() for oneImage in self.getDataInput().getIntegratedImage()]

        self.averagedImage = self.getDataInput().getAveragedImage().getPath().getValue()
        self.averagedSpectrum = self.getDataInput().getAveragedSpectrum().getPath().getValue()
        self.strLogFile = self.getDataInput().getLogFile().getPath().getValue()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.process")


        xsdiWaitMultiFile = XSDataInputWaitMultiFile()
        xsdiWaitMultiFile.setExpectedFile(self.getDataInput().getIntegratedImage())
        xsdiWaitMultiFile.setExpectedSize(self.getDataInput().getIntegratedImageSize())
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
        xsdiMetadata.setInputImage(self.getDataInput().getIntegratedImage()[0])
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
        self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSucessGetMetadata)
        self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
        self.__edPluginSaxsGetMetadata.executeSynchronous()


    def doFailureWaitMultiFile(self, _edPlugin=None):
        self.synchronizeOn()
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureWaitMultiFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureWaitMultiFile")
        self.strProcessLog += "Timeout in waiting for file '%s'\n" % (_edPlugin.getDataInput().getExpectedFile().getPath().getValue())
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
            except:
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
        xsdiSaxsMac.setOutputImage(self.getDataInput().getAveragedImage())
        xsdiSaxsMac.setOptions(XSDataString("+pass -omod n +var -add %d" % len(self.integratedImages)))
        xsdiSaxsMac.setMultConst(XSDataFloat(1.0 / len(self.integratedImages)))
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
        xsdiMetadata.setInputImage(self.getDataInput().getAveragedImage())
        xsdiMetadata.setOutputImage(self.getDataInput().getAveragedImage())
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

        self.xsdResult.setAveragedImage(self.getDataInput().getAveragedImage())
        self.strProcessLog += "Conversion to 3-column ascii file: '%s'\n" % (self.averagedSpectrum)
        xsdiAsciiExport = XSDataInputBioSaxsAsciiExportv1_0()
        xsdiAsciiExport.setIntegratedImage(self.getDataInput().getAveragedImage())
        xsdiAsciiExport.setIntegratedSpectrum(self.getDataInput().getAveragedSpectrum())
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
        self.xsdResult.setAveragedSpectrum(self.getDataInput().getAveragedSpectrum())
#        self.strProcessLog += "Successful Execution of EDPlugin BioSaxs Average v1_0"

    def doFailureAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAveragev1_0.doFailureAsciiExport")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAveragev1_0.doFailureAsciiExport")
        self.strProcessLog += "Error during the call of saxs_curves for the production of '%s'\n" % (self.averagedSpectrum)
        self.setFailure()


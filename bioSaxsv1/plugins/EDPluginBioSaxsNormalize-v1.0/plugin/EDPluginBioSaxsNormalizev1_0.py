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
#    Principal author:       Jérôme Kieffer (kieffer@esrf.fr) 
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
import shutil

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import shutil, os
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from XSDataCommon       import XSDataInteger, XSDataDouble, XSDataImage, XSDataFile, XSDataString
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsNormalizev1_0, XSDataResultBioSaxsNormalizev1_0, XSDataInputBioSaxsMetadatav1_0, XSDataResultBioSaxsMetadatav1_0
from EDFactoryPluginStatic      import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataSaxsv1_0     import XSDataInputSaxsMacv1_0


class EDPluginBioSaxsNormalizev1_0(EDPluginControl):
    """
    Wait for the file to appear then 
    do the normalization of the raw data by ring current and BeamStopDiode 
    Finally append all metadata to the file (in post-processing).
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsNormalizev1_0)
        self.__strPluginNameSaxsMac = "EDPluginExecSaxsMacv1_0"
        self.__edPluginExecSaxsMac = None
        self.__strPluginNameWaitFile = "EDPluginWaitFile"
        self.__edPluginExecWaitFile = None
        self.__strPluginNameMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginExecMetadata = None


        self.strLogFile = None
        self.strRawImage = None
        self.strRawImageSize = None
        self.strNormalizedImage = None
        self.strProcessLog = "" #comments to be returned

        self.detector = None
        self.detectorDistance = None
        self.pixelSize_1 = None
        self.pixelSize_2 = None
        self.beamCenter_1 = None
        self.beamCenter_2 = None
        self.beamStopDiode = None
        self.wavelength = None
        self.maskFile = None
        self.normalizationFactor = None
        self.machineCurrent = None
        self.sampleComments = None

        self.xsdInput = None
        self.xsdResult = XSDataResultBioSaxsNormalizev1_0()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.checkParameters")
        self.xsdInput = self.getDataInput()
        self.checkMandatoryParameters(self.xsdInput, "Data Input is None")
        self.checkMandatoryParameters(self.xsdInput.getRawImage(), "Raw File is None")
        self.checkMandatoryParameters(self.xsdInput.getLogFile(), "Output Log File is None")
        self.checkMandatoryParameters(self.xsdInput.getNormalizedImage(), "Normalized File is None")
        self.checkMandatoryParameters(self.xsdInput.getRawImageSize(), "No size given for expected Raw File")
        self.checkMandatoryParameters(self.xsdInput.getBeamStopDiode(), "No beam stop diod signal given")
        self.checkMandatoryParameters(self.xsdInput.getNormalizationFactor(), "No Normalization factor provided")
        self.checkMandatoryParameters(self.xsdInput.getMachineCurrent(), "No Machine current provided")
        self.checkMandatoryParameters(self.xsdInput.getMaskFile(), "No mask file provided")
        self.checkMandatoryParameters(self.xsdInput.getDetectorDistance(), "No detector distance provided")
        self.checkMandatoryParameters(self.xsdInput.getWavelength(), "No Wavelength provided")
        self.checkMandatoryParameters(self.xsdInput.getPixelSize_1(), "No Pixel size X provided")
        self.checkMandatoryParameters(self.xsdInput.getPixelSize_2(), "No Pixel size Y provided")
        self.checkMandatoryParameters(self.xsdInput.getBeamCenter_1(), "No beam center X provided")
        self.checkMandatoryParameters(self.xsdInput.getBeamCenter_2(), "No BeamCenter Y Provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.preProcess")
        self.strLogFile = self.xsdInput.getLogFile().getPath().getValue()
        self.strRawImage = self.xsdInput.getRawImage().getPath().getValue()
        self.strNormalizedImage = self.xsdInput.getNormalizedImage().getPath().getValue()
        self.strRawImageSize = self.xsdInput.getRawImageSize().getValue()
        self.beamStopDiode = self.xsdInput.getBeamStopDiode().getValue()
        self.normalizationFactor = self.xsdInput.getNormalizationFactor().getValue()
        self.machineCurrent = self.xsdInput.getMachineCurrent().getValue()
        self.maskFile = self.xsdInput.getMaskFile().getPath().getValue()
        self.detectorDistance = self.xsdInput.getDetectorDistance().getValue()
        self.waveLength = self.xsdInput.getWavelength().getValue()
        self.pixelSize_1 = self.xsdInput.getPixelSize_1().getValue()
        self.pixelSize_2 = self.xsdInput.getPixelSize_2().getValue()
        self.beamCenter_1 = self.xsdInput.getBeamCenter_1().getValue()
        self.beamCenter_2 = self.xsdInput.getBeamCenter_2().getValue()

        if self.xsdInput.getSampleComments() is not None:
            self.sampleComments = self.xsdInput.getSampleComments().getValue()

        # Load the execution plugin
        self.__edPluginExecWaitFile = self.loadPlugin(self.__strPluginNameWaitFile)
        self.__edPluginExecSaxsMac = self.loadPlugin(self.__strPluginNameSaxsMac)
        self.__edPluginExecMetadata = self.loadPlugin(self.__strPluginNameMetadata)

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.process")
        xsdiWaitFile = XSDataInputWaitFile()
        xsdiWaitFile.setExpectedFile(self.xsdInput.getRawImage())
        xsdiWaitFile.setExpectedSize(self.xsdInput.getRawImageSize())
        self.__edPluginExecWaitFile.setDataInput(xsdiWaitFile)

        self.__edPluginExecWaitFile.connectSUCCESS(self.doSuccessExecWaitFile)
        self.__edPluginExecWaitFile.connectFAILURE(self.doFailureExecWaitFile)
        self.__edPluginExecWaitFile.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.postProcess")
        #remove the terminal carriage return
        if self.strProcessLog.endswith("\n"):
           self.strProcessLog = self.strProcessLog[:-1]
        # Create some output data
        self.xsdResult.setProcessLog(XSDataString(self.strProcessLog))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("Comment generated ...\n" + self.strProcessLog)


    def doSuccessExecWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecWaitFile")

        self.strProcessLog += "Normalizing EDF frame '%s' -> '%s'\n" % (self.strRawImage, self.strNormalizedImage)

        xsdiSaxsMac = XSDataInputSaxsMacv1_0()
        xsdiSaxsMac.setInputImage(self.xsdInput.getRawImage())
        xsdiSaxsMac.setOutputImage(self.xsdInput.getNormalizedImage())
        xsdiSaxsMac.setMultConst(XSDataDouble(self.normalizationFactor / self.beamStopDiode))
        xsdiSaxsMac.setAddConst(XSDataDouble(0))
        if self.sampleComments is not None:
            title = ' -otit \"%s\" ' % self.sampleComments
        else:
            title = ""
        saxsMacOptions = '+var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 %s  -i1dis \"%s\" -i1wvl %s -i1pix %s %s -i1cen %s %s -ofac %s' % \
        (title, self.detectorDistance, self.waveLength, self.pixelSize_1, self.pixelSize_2, self.beamCenter_1, self.beamCenter_2, self.normalizationFactor / self.beamStopDiode)
        xsdiSaxsMac.setOptions(XSDataString(saxsMacOptions))
        self.__edPluginExecSaxsMac.setDataInput(xsdiSaxsMac)
        self.__edPluginExecSaxsMac.connectSUCCESS(self.doSuccessExecSaxsMac)
        self.__edPluginExecSaxsMac.connectFAILURE(self.doFailureExecSaxsMac)
        self.__edPluginExecSaxsMac.executeSynchronous()


    def doFailureExecWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecWaitFile")
        self.strProcessLog += "Timeout in waiting for file '%s'.\n" % (self.strRawImage)
        self.setFailure()

    def doSuccessExecSaxsMac(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecSaxsMac")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecSaxsMac")
        strEdnaLogFile = os.path.join(self.__edPluginExecSaxsMac.getWorkingDirectory(), self.__edPluginExecSaxsMac.getScriptLogFileName())
        EDVerbose.DEBUG("ExecPlugin log file is in: %s" % strEdnaLogFile)
        if os.path.isfile(self.strNormalizedImage) and EDVerbose.isVerboseDebug():
            shutil.copy(self.strNormalizedImage, self.strNormalizedImage + ".bak")
        if os.path.isfile(strEdnaLogFile):
            shutil.copy(strEdnaLogFile, self.strLogFile)
            xsLogFile = XSDataFile()
            xsLogFile.setPath(XSDataString(self.strLogFile))
            self.xsdResult.setLogFile(xsLogFile)

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.xsdInput.getNormalizedImage())
        xsdiMetadata.setOutputImage(self.xsdInput.getNormalizedImage())
        xsdiMetadata.setBeamStopDiode(self.xsdInput.getBeamStopDiode())
        xsdiMetadata.setNormalizationFactor(self.xsdInput.getNormalizationFactor())
        xsdiMetadata.setDetector(self.xsdInput.getDetector())
        xsdiMetadata.setMachineCurrent(self.xsdInput.getMachineCurrent())
        xsdiMetadata.setMaskFile(self.xsdInput.getMaskFile())
        xsdiMetadata.setDetectorDistance(self.xsdInput.getDetectorDistance())
        xsdiMetadata.setWavelength(self.xsdInput.getWavelength())
        xsdiMetadata.setPixelSize_1(self.xsdInput.getPixelSize_1())
        xsdiMetadata.setPixelSize_2(self.xsdInput.getPixelSize_2())
        xsdiMetadata.setBeamCenter_1(self.xsdInput.getBeamCenter_1())
        xsdiMetadata.setBeamCenter_2(self.xsdInput.getBeamCenter_2())

        xsdiMetadata.setSampleConcentration(self.xsdInput.getSampleConcentration())
        xsdiMetadata.setSampleComments(self.xsdInput.getSampleComments())
        xsdiMetadata.setSampleCode(self.xsdInput.getSampleCode())

        self.__edPluginExecMetadata.setDataInput(xsdiMetadata)
        self.__edPluginExecMetadata.connectSUCCESS(self.doSuccessExecMetadata)
        self.__edPluginExecMetadata.connectFAILURE(self.doFailureExecMetadata)
        self.__edPluginExecMetadata.executeSynchronous()




    def doFailureExecSaxsMac(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecSaxsMac")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecSaxsMac")
        strEdnaLogFile = self.__edPluginExecSaxsMac.getScriptLogFileName()
        if os.path.isfile(strEdnaLogFile):
            shutil.copy(strEdnaLogFile, self.strLogFile)
            xsLogFile = XSDataFile()
            xsLogFile.setPath(XSDataString(self.strLogFile))
            self.xsdResult.setLogFile(xsLogFile)

        self.strProcessLog += "Normalization failure during execution of saxs_mac.\n"
        self.setFailure()


    def doSuccessExecMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecMetadata")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecMetadata")
        if os.path.isfile(self.strNormalizedImage):
            xsNormFile = XSDataImage()
            xsNormFile.setPath(XSDataString(self.strNormalizedImage))
            self.xsdResult.setNormalizedImage(xsNormFile)


    def doFailureExecMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecMetadata")
        self.strProcessLog += "Metadata addition failure.\n"
        self.setFailure()



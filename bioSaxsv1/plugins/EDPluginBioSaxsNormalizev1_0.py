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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

__status__ = "deprecated"

import os, shutil
from EDPluginControl    import EDPluginControl
from XSDataCommon       import XSDataDouble, XSDataImage, XSDataFile, XSDataString, XSDataStatus, XSDataTime
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsNormalizev1_0, XSDataResultBioSaxsNormalizev1_0, \
                                XSDataInputBioSaxsMetadatav1_0
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
    __strPluginNameSaxsMac = "EDPluginExecSaxsMacv1_0"
    __strPluginNameWaitFile = "EDPluginWaitFile"
    __strPluginNameMetadata = "EDPluginBioSaxsMetadatav1_0"
    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsNormalizev1_0)

        self.__edPluginExecSaxsMac = None
        self.__edPluginExecWaitFile = None
        self.__edPluginExecMetadata = None


        self.strLogFile = None
        self.strRawImage = None
        self.strRawImageSize = None
        self.strNormalizedImage = None
        self.lstProcessLog = [] #comments to be returned

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
        self.comments = None

        self.xsdInput = None
        self.xsdResult = XSDataResultBioSaxsNormalizev1_0()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.checkParameters")
        self.xsdInput = self.dataInput
        self.checkMandatoryParameters(self.xsdInput, "Data Input is None")
        self.checkMandatoryParameters(self.xsdInput.rawImage, "Raw File is None")
        #self.checkMandatoryParameters(self.xsdInput.logFile, "Output Log File is None")
        self.checkMandatoryParameters(self.xsdInput.experimentSetup, "No experiment setup")
        self.checkMandatoryParameters(self.xsdInput.sample, "No sample description")
#        self.checkMandatoryParameters(self.xsdInput.normalizedImage, "Normalized File is None")
#        self.checkMandatoryParameters(self.xsdInput.rawImageSize, "No size given for expected Raw File")
#        self.checkMandatoryParameters(self.xsdInput.beamStopDiode, "No beam stop diod signal given")
#        self.checkMandatoryParameters(self.xsdInput.normalizationFactor, "No Normalization factor provided")
#        self.checkMandatoryParameters(self.xsdInput.machineCurrent, "No Machine current provided")
#        self.checkMandatoryParameters(self.xsdInput.maskFile, "No mask file provided")
#        self.checkMandatoryParameters(self.xsdInput.detectorDistance, "No detector distance provided")
#        self.checkMandatoryParameters(self.xsdInput.wavelength, "No Wavelength provided")
#        self.checkMandatoryParameters(self.xsdInput.pixelSize_1, "No Pixel size X provided")
#        self.checkMandatoryParameters(self.xsdInput.pixelSize_2, "No Pixel size Y provided")
#        self.checkMandatoryParameters(self.xsdInput.beamCenter_1, "No beam center X provided")
#        self.checkMandatoryParameters(self.xsdInput.beamCenter_2, "No BeamCenter Y Provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.preProcess")
        self.strLogFile = self.xsdInput.getLogFile().getPath().value
        self.strRawImage = self.xsdInput.getRawImage().getPath().value
        self.strNormalizedImage = self.xsdInput.normalizedImage.getPath().value
        self.strRawImageSize = self.xsdInput.getRawImageSize().value
        self.beamStopDiode = self.xsdInput.experimentSetup.beamStopDiode.value
        self.normalizationFactor = self.xsdInput.experimentSetup.normalizationFactor.value
        self.machineCurrent = self.xsdInput.experimentSetup.machineCurrent.value
        self.maskFile = self.xsdInput.experimentSetup.maskFile.getPath().value
        self.detectorDistance = self.xsdInput.experimentSetup.detectorDistance.value
        self.waveLength = self.xsdInput.experimentSetup.wavelength.value
        self.pixelSize_1 = self.xsdInput.experimentSetup.pixelSize_1.value
        self.pixelSize_2 = self.xsdInput.experimentSetup.pixelSize_2.value
        self.beamCenter_1 = self.xsdInput.experimentSetup.beamCenter_1.value
        self.beamCenter_2 = self.xsdInput.experimentSetup.beamCenter_2.value

        if self.xsdInput.sample.comments is not None:
            self.comments = self.xsdInput.sample.comments.value

        # Load the execution plugin
        self.__edPluginExecWaitFile = self.loadPlugin(self.__strPluginNameWaitFile)
        self.__edPluginExecSaxsMac = self.loadPlugin(self.__strPluginNameSaxsMac)
        self.__edPluginExecMetadata = self.loadPlugin(self.__strPluginNameMetadata)

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.process")
        xsdiWaitFile = XSDataInputWaitFile(expectedFile=XSDataFile(self.xsdInput.rawImage.path),
                                           expectedSize=self.xsdInput.rawImageSize,
                                           timeOut=XSDataTime(30))
        self.__edPluginExecWaitFile.setDataInput(xsdiWaitFile)

        self.__edPluginExecWaitFile.connectSUCCESS(self.doSuccessExecWaitFile)
        self.__edPluginExecWaitFile.connectFAILURE(self.doFailureExecWaitFile)
        self.__edPluginExecWaitFile.executeSynchronous()


        if self.isFailure():
            return
        self.__edPluginExecSaxsMac.connectSUCCESS(self.doSuccessExecSaxsMac)
        self.__edPluginExecSaxsMac.connectFAILURE(self.doFailureExecSaxsMac)
        self.__edPluginExecSaxsMac.executeSynchronous()

        if self.isFailure():
            return

        self.__edPluginExecMetadata.connectSUCCESS(self.doSuccessExecMetadata)
        self.__edPluginExecMetadata.connectFAILURE(self.doFailureExecMetadata)
        self.__edPluginExecMetadata.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.postProcess")
        # Create some output data
        self.xsdResult.status = XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstProcessLog)))
        self.setDataOutput(self.xsdResult)


    def doSuccessExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecWaitFile")

        self.lstProcessLog.append("Normalizing EDF frame '%s' -> '%s'" % (self.strRawImage, self.strNormalizedImage))

        xsdiSaxsMac = XSDataInputSaxsMacv1_0()
        xsdiSaxsMac.setInputImage(self.xsdInput.getRawImage())
        xsdiSaxsMac.setOutputImage(self.xsdInput.normalizedImage)
        xsdiSaxsMac.setMultConst(XSDataDouble(self.normalizationFactor / self.beamStopDiode))
        xsdiSaxsMac.setAddConst(XSDataDouble(0))
        if self.comments is not None:
            title = ' -otit \"%s\" ' % self.comments
        else:
            title = ""
        saxsMacOptions = '+var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 %s  -i1dis \"%s\" -i1wvl %s -i1pix %s %s -i1cen %s %s -ofac %s' % \
        (title, self.detectorDistance, self.waveLength, self.pixelSize_1, self.pixelSize_2, self.beamCenter_1, self.beamCenter_2, self.normalizationFactor / self.beamStopDiode)
        xsdiSaxsMac.setOptions(XSDataString(saxsMacOptions))
        self.__edPluginExecSaxsMac.setDataInput(xsdiSaxsMac)


    def doFailureExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecWaitFile")
        self.lstProcessLog.append("Timeout in waiting for file '%s'." % (self.strRawImage))
        self.setFailure()

    def doSuccessExecSaxsMac(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecSaxsMac")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecSaxsMac")
        strEdnaLogFile = os.path.join(self.__edPluginExecSaxsMac.getWorkingDirectory(), self.__edPluginExecSaxsMac.getScriptLogFileName())
        self.DEBUG("ExecPlugin log file is in: %s" % strEdnaLogFile)
        if os.path.isfile(self.strNormalizedImage) and self.isVerboseDebug():
            shutil.copy(self.strNormalizedImage, self.strNormalizedImage + ".bak")
        if os.path.isfile(strEdnaLogFile):
            shutil.copy(strEdnaLogFile, self.strLogFile)
            xsLogFile = XSDataFile()
            xsLogFile.setPath(XSDataString(self.strLogFile))
            self.xsdResult.setLogFile(xsLogFile)

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.xsdInput.normalizedImage)
        xsdiMetadata.setOutputImage(self.xsdInput.normalizedImage)
        xsdiMetadata.setBeamStopDiode(self.xsdInput.experimentSetup.beamStopDiode)
        xsdiMetadata.setNormalizationFactor(self.xsdInput.experimentSetup.normalizationFactor)
        xsdiMetadata.setDetector(self.xsdInput.experimentSetup.getDetector())
        xsdiMetadata.setMachineCurrent(self.xsdInput.experimentSetup.machineCurrent)
        xsdiMetadata.setMaskFile(self.xsdInput.experimentSetup.maskFile)
        xsdiMetadata.setDetectorDistance(self.xsdInput.experimentSetup.detectorDistance)
        xsdiMetadata.setWavelength(self.xsdInput.experimentSetup.wavelength)
        xsdiMetadata.setPixelSize_1(self.xsdInput.experimentSetup.pixelSize_1)
        xsdiMetadata.setPixelSize_2(self.xsdInput.experimentSetup.pixelSize_2)
        xsdiMetadata.setBeamCenter_1(self.xsdInput.experimentSetup.beamCenter_1)
        xsdiMetadata.setBeamCenter_2(self.xsdInput.experimentSetup.beamCenter_2)

        xsdiMetadata.setConcentration(self.xsdInput.sample.concentration)
        xsdiMetadata.setComments(self.xsdInput.sample.comments)
        xsdiMetadata.setCode(self.xsdInput.sample.code)

        self.__edPluginExecMetadata.setDataInput(xsdiMetadata)




    def doFailureExecSaxsMac(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecSaxsMac")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecSaxsMac")
        strEdnaLogFile = self.__edPluginExecSaxsMac.getScriptLogFileName()
        if os.path.isfile(strEdnaLogFile):
            shutil.copy(strEdnaLogFile, self.strLogFile)
            xsLogFile = XSDataFile()
            xsLogFile.setPath(XSDataString(self.strLogFile))
            self.xsdResult.setLogFile(xsLogFile)

        self.lstProcessLog.append("Normalization failure during execution of saxs_mac.")
        self.setFailure()


    def doSuccessExecMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doSuccessExecMetadata")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doSuccessExecMetadata")
        if os.path.isfile(self.strNormalizedImage):
            xsNormFile = XSDataImage()
            xsNormFile.setPath(XSDataString(self.strNormalizedImage))
            self.xsdResult.setNormalizedImage(xsNormFile)


    def doFailureExecMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_0.doFailureExecMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_0.doFailureExecMetadata")
        self.lstProcessLog.append("Metadata addition failure.")
        self.setFailure()



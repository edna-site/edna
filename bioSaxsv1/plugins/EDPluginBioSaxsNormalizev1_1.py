# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jérôme Kieffer (jerome.kieffer@esrf.eu) 
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
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20110919"
__status__ = "production"

import os, threading
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from XSDataCommon           import XSDataImage, XSDataString, XSDataStatus, XSDataFile, XSDataTime
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsNormalizev1_0, XSDataResultBioSaxsNormalizev1_0
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPath            import EDUtilsPath
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataCommon           import XSPluginItem
from EDConfiguration        import EDConfiguration

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
if fabio is None:
    strErr = """Error in loading numpy, PIL, fabio ,
    Please re-run the test suite for EDTestSuitePluginBioSaxsNormalizev1_1
    to ensure that all modules are compiled for you computer as they don't seem to be installed"""
    EDVerbose.ERROR(strErr)
    raise ImportError(strErr)



class EDPluginBioSaxsNormalizev1_1(EDPluginControl):
    """
    Wait for the file to appear then apply mask ;  
    do the normalization of the raw data by ring current and BeamStopDiode 
    and finally append all metadata to the file EDF.
    
    All "processing" are done with Numpy, Input/Output is handled by Fabio
    """
    __maskfiles = {} #key=filename, value=numpy.ndarray
    __semaphore = threading.Semaphore()
    CONF_DUMMY_PIXEL_VALUE = "DummyPixelValue"

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsNormalizev1_0)
        self.__strPluginNameWaitFile = "EDPluginWaitFile"
        self.__edPluginExecWaitFile = None

        self.dummy = None
        self.strLogFile = None
        self.strRawImage = None
        self.strRawImageSize = None
        self.strNormalizedImage = None
        self.lstProcessLog = [] #comments to be returned

        self.xsdInput = None
        self.sample = None
        self.experimentSetup = None
        self.xsdResult = XSDataResultBioSaxsNormalizev1_0()
        self.dictOutputHeader = {}

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.checkParameters")
        self.xsdInput = self.dataInput
        self.checkMandatoryParameters(self.xsdInput, "Data Input is None")
        self.checkMandatoryParameters(self.xsdInput.rawImage, "Raw File is None")
        self.checkMandatoryParameters(self.xsdInput.normalizedImage, "No normalized output image provided")
        self.checkMandatoryParameters(self.xsdInput.sample, "No sample provided")
        self.checkMandatoryParameters(self.xsdInput.experimentSetup, "No experiment setup provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.preProcess")
        self.sample = self.xsdInput.sample
        self.experimentSetup = self.xsdInput.experimentSetup
#        self.strLogFile = self.xsdInput.getLogFile().path.value
        self.strRawImage = self.xsdInput.rawImage.path.value
        self.strNormalizedImage = self.xsdInput.normalizedImage.path.value
        outDir = os.path.dirname(self.strNormalizedImage)
        if not os.path.exists(outDir):
            os.mkdir(outDir)
        self.strRawImageSize = self.xsdInput.getRawImageSize().value
        self.dictOutputHeader["DiodeCurr"] = self.experimentSetup.beamStopDiode.value
        self.dictOutputHeader["Normalization"] = self.experimentSetup.normalizationFactor.value
        self.dictOutputHeader["MachCurr"] = self.experimentSetup.machineCurrent.value
        self.dictOutputHeader["Mask"] = str(self.experimentSetup.maskFile.path.value)
        self.dictOutputHeader["SampleDistance"] = self.experimentSetup.detectorDistance.value
        self.dictOutputHeader["WaveLength"] = self.experimentSetup.wavelength.value
        self.dictOutputHeader["PSize_1"] = self.experimentSetup.pixelSize_1.value
        self.dictOutputHeader["PSize_2"] = self.experimentSetup.pixelSize_2.value
        self.dictOutputHeader["Center_1"] = self.experimentSetup.beamCenter_1.value
        self.dictOutputHeader["Center_2"] = self.experimentSetup.beamCenter_2.value
        if self.experimentSetup.storageTemperature is not None:
            self.dictOutputHeader["storageTemperature"] = self.experimentSetup.storageTemperature.value
        if self.experimentSetup.exposureTemperature is not None:
            self.dictOutputHeader["exposureTemperature"] = self.experimentSetup.exposureTemperature.value
        if self.experimentSetup.exposureTime is not None:
            self.dictOutputHeader["exposureTime"] = self.experimentSetup.exposureTime.value
        if self.experimentSetup.frameNumber is not None:
            self.dictOutputHeader["frameNumber"] = self.experimentSetup.frameNumber.value
        if self.experimentSetup.frameMax is not None:
            self.dictOutputHeader["frameMax"] = self.experimentSetup.frameMax.value

        if self.sample.comments is not None:
            self.dictOutputHeader["Comments"] = str(self.sample.comments.value)
            self.dictOutputHeader["title"] = str(self.sample.comments.value)

        if self.sample.concentration is not None:
            self.dictOutputHeader["Concentration"] = str(self.sample.concentration.value)
        if self.sample.code is not None:
            self.dictOutputHeader["Code"] = str(self.sample.code.value)

        # Load the execution plugin
        self.__edPluginExecWaitFile = self.loadPlugin(self.__strPluginNameWaitFile)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.process")
        xsdiWaitFile = XSDataInputWaitFile(expectedFile=XSDataFile(self.xsdInput.rawImage.path),
                                           expectedSize=self.xsdInput.rawImageSize,
                                           timeOut=XSDataTime(value=30))
        self.__edPluginExecWaitFile.setDataInput(xsdiWaitFile)
        self.__edPluginExecWaitFile.connectSUCCESS(self.doSuccessExecWaitFile)
        self.__edPluginExecWaitFile.connectFAILURE(self.doFailureExecWaitFile)
        self.__edPluginExecWaitFile.executeSynchronous()
        if self.isFailure():
            return
#        Small Numpy processing:
        fabIn = fabio.open(self.strRawImage)
        if "time_of_day" in fabIn.header:
            self.dictOutputHeader["time_of_day"] = fabIn.header["time_of_day"]
        if "Mask" in self.dictOutputHeader:
            mask = self.getMask(self.dictOutputHeader["Mask"])
            npaMaskedData = numpy.ma.masked_array(fabIn.data.astype("float32"),
                                                  ((fabIn.data < 0) + (mask[:fabIn.dim2, :fabIn.dim1 ] < 0)))
        else:
            npaMaskedData = numpy.ma.masked_array(fabIn.data.astype("float32"), (fabIn.data < 0))
        scale = self.dictOutputHeader["Normalization"] / self.dictOutputHeader["DiodeCurr"]
        self.dictOutputHeader["Dummy"] = str(self.dummy)
        self.dictOutputHeader["DDummy"] = "0.1"
        self.dictOutputHeader["EDF_DataBlockID"] = "1.Image.Psd"
        header_keys = self.dictOutputHeader.keys()
        header_keys.sort()
        fabioOut = fabio.edfimage.edfimage(header=self.dictOutputHeader, header_keys=header_keys,
                             data=numpy.ma.filled(npaMaskedData * scale, float(self.dummy)))
        fabioOut.appendFrame(header={"Dummy": str(self.dummy), "DDummy":"0.1", "EDF_DataBlockID":"1.Image.Error"},
                              data=(numpy.ma.filled(npaMaskedData * (scale ** 2), float(self.dummy))))
        fabioOut.write(self.strNormalizedImage)
        self.lstProcessLog.append("Normalized image by factor %.3f " % (scale))


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.postProcess")

        if os.path.isfile(self.strNormalizedImage):
            xsNormFile = XSDataImage()
            xsNormFile.setPath(XSDataString(self.strNormalizedImage))
            self.xsdResult.setNormalizedImage(xsNormFile)
        self.xsdResult.status = XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstProcessLog)))
        # Create some output data
        self.setDataOutput(self.xsdResult)


    def doSuccessExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.doSuccessExecWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_1.doSuccessExecWaitFile")
        xsdOut = _edPlugin.getDataOutput()
        if (xsdOut.timedOut is not None) and (xsdOut.timedOut.value):
            strErr = "Timeout (%s s) in waiting for file %s" % (_edPlugin.getTimeOut(), self.strRawImage)
            self.ERROR(strErr)
            self.lstProcessLog.append(strErr)
            self.setFailure()
        else:
            self.log("EDPluginBioSaxsNormalizev1_1.WaitFile took %.3fs" % self.getRunTime())
            self.lstProcessLog.append("Normalizing EDF frame '%s' -> '%s'" % (self.strRawImage, self.strNormalizedImage))


    def doFailureExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.doFailureExecWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_1.doFailureExecWaitFile")
        self.lstProcessLog.append("Timeout in waiting for file '%s'.\n" % (self.strRawImage))
        self.setFailure()


    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters:
         - DummyPixelValue: the value to be assigned to dummy pixels.
        """
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            self.warning("EDPluginBioSaxsNormalizev1_1.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()
        self.dummy = EDConfiguration.getStringParamValue(xsPluginItem, self.CONF_DUMMY_PIXEL_VALUE)
        if self.dummy is None:
            strMessage = 'EDPluginBioSaxsNormalizev1_1.configure: %s Configuration parameter missing: \
%s, defaulting to "-1"' % (self.getBaseName(), self.CONF_DUMMY_PIXEL_VALUE)
            self.WARNING(strMessage)
            self.addErrorWarningMessagesToExecutiveSummary(strMessage)
            self.dummy = -1

    @classmethod
    def getMask(cls, _strFilename):
        """
        Retrieve the data from a file, featuring caching.
        
        @param _strFilename: name of the file
        @return: numpy ndarray
        
        /!\ This is a class method (for the cache part)
        """
        if _strFilename not in cls.__maskfiles:
            cls.__semaphore.acquire()
            maskFile = fabio.open(_strFilename)
            cls.__maskfiles[_strFilename] = maskFile.data
            cls.__semaphore.release()
        return cls.__maskfiles[_strFilename]

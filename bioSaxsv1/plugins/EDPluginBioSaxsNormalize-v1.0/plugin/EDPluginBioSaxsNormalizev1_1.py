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
import shutil, threading

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import shutil, os
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from XSDataCommon           import XSDataInteger, XSDataFloat, XSDataImage, XSDataFile, XSDataString
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsNormalizev1_0, XSDataResultBioSaxsNormalizev1_0
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataCommon           import XSPluginItem
from EDConfiguration        import EDConfiguration

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)

try:
    import numpy, Image, fabio
    from fabio.openimage import openimage
    from  fabio.edfimage import edfimage, Frame
except ImportError:
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
        self.xsdResult = XSDataResultBioSaxsNormalizev1_0()
        self.dictOutputHeader = {}

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.checkParameters")
        self.xsdInput = self.getDataInput()
        self.checkMandatoryParameters(self.xsdInput, "Data Input is None")
        self.checkMandatoryParameters(self.xsdInput.getRawImage(), "Raw File is None")
        self.checkMandatoryParameters(self.xsdInput.getLogFile(), "Output Log File is None")
        self.checkMandatoryParameters(self.xsdInput.getNormalizedImage(), "Normalized File is None")
        self.checkMandatoryParameters(self.xsdInput.getRawImageSize(), "No size given for expected Raw File")
        self.checkMandatoryParameters(self.xsdInput.getBeamStopDiode(), "No beam stop diode signal given")
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
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.preProcess")
        self.strLogFile = self.xsdInput.getLogFile().getPath().getValue()
        self.strRawImage = self.xsdInput.getRawImage().getPath().getValue()
        self.strNormalizedImage = self.xsdInput.getNormalizedImage().getPath().getValue()
        self.strRawImageSize = self.xsdInput.getRawImageSize().getValue()
        self.dictOutputHeader["DiodeCurr"] = self.xsdInput.getBeamStopDiode().getValue()
        self.dictOutputHeader["Normalization"] = self.xsdInput.getNormalizationFactor().getValue()
        self.dictOutputHeader["MachCurr"] = self.xsdInput.getMachineCurrent().getValue()
        self.dictOutputHeader["Mask"] = str(self.xsdInput.getMaskFile().getPath().getValue())
        self.dictOutputHeader["SampleDistance"] = self.xsdInput.getDetectorDistance().getValue()
        self.dictOutputHeader["WaveLength"] = self.xsdInput.getWavelength().getValue()
        self.dictOutputHeader["PSize_1"] = self.xsdInput.getPixelSize_1().getValue()
        self.dictOutputHeader["PSize_2"] = self.xsdInput.getPixelSize_2().getValue()
        self.dictOutputHeader["Center_1"] = self.xsdInput.getBeamCenter_1().getValue()
        self.dictOutputHeader["Center_2"] = self.xsdInput.getBeamCenter_2().getValue()

        if self.xsdInput.getSampleComments() is not None:
            self.dictOutputHeader["Comments"] = str(self.xsdInput.getSampleComments().getValue())
            self.dictOutputHeader["title"] = str(self.xsdInput.getSampleComments().getValue())
        if self.xsdInput.getSampleCode() is not None:
            self.dictOutputHeader["Code"] = str(self.xsdInput.getSampleCode().getValue())

        # Load the execution plugin
        self.__edPluginExecWaitFile = self.loadPlugin(self.__strPluginNameWaitFile)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.process")
        xsdiWaitFile = XSDataInputWaitFile()
        xsdiWaitFile.setExpectedFile(self.xsdInput.getRawImage())
        xsdiWaitFile.setExpectedSize(self.xsdInput.getRawImageSize())
        self.__edPluginExecWaitFile.setDataInput(xsdiWaitFile)

        self.__edPluginExecWaitFile.connectSUCCESS(self.doSuccessExecWaitFile)
        self.__edPluginExecWaitFile.connectFAILURE(self.doFailureExecWaitFile)
        self.__edPluginExecWaitFile.executeSynchronous()

#        Small Numpy processing:
        fabIn = openimage(self.strRawImage)
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
        fabioOut = edfimage(header=self.dictOutputHeader, header_keys=header_keys,
                             data=numpy.ma.filled(npaMaskedData * scale, float(self.dummy)))
        frameVariance = Frame(header={"Dummy": str(self.dummy), "DDummy":"0.1", "EDF_DataBlockID":"1.Image.Error"},
                              data=(numpy.ma.filled(npaMaskedData * (scale ** 2), float(self.dummy))))
        fabioOut.frames.append(frameVariance)
        fabioOut.write(self.strNormalizedImage)
        self.lstProcessLog.append("Normalized image by factor %.3f " % (scale))


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.postProcess")
        if os.path.isfile(self.strNormalizedImage):
            xsNormFile = XSDataImage()
            xsNormFile.setPath(XSDataString(self.strNormalizedImage))
            self.xsdResult.setNormalizedImage(xsNormFile)

        strProcessLog = os.linesep.join(self.lstProcessLog)
        # Create some output data
        self.xsdResult.setProcessLog(XSDataString(strProcessLog))
        self.setDataOutput(self.xsdResult)
        self.DEBUG("Comment generated ...\n%s" % strProcessLog)


    def doSuccessExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.doSuccessExecWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_1.doSuccessExecWaitFile")

        self.lstProcessLog.append("Normalizing EDF frame '%s' -> '%s'" % (self.strRawImage, self.strNormalizedImage))


    def doFailureExecWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsNormalizev1_1.doFailureExecWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsNormalizev1_1.doFailureExecWaitFile")
        self.lstProcessLog += "Timeout in waiting for file '%s'.\n" % (self.strRawImage)
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


    def getMask(cls, _strFilename):
        """
        Retrieve the data from a file, featuring caching.
        
        @param _strFilename: name of the file
        @return: numpy ndarray
        
        /!\ This is a class method (for the cache part)
        """
        if _strFilename not in cls.__maskfiles:
            cls.__semaphore.acquire()
            maskFile = openimage(_strFilename)
            cls.__maskfiles[_strFilename] = maskFile.data
            cls.__semaphore.release()
        return cls.__maskfiles[_strFilename]

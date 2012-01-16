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
__date__ = "20111018"
__status__ = "production"


import os
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPlatform        import EDUtilsPlatform
from EDUtilsPath            import EDUtilsPath
from XSDataCommon           import XSDataString, XSDataStatus, XSDataTime, XSDataFile
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsAzimutIntv1_0, XSDataResultBioSaxsAzimutIntv1_0, \
                                XSDataInputBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataSaxsv1_0         import XSDataInputSaxsAnglev1_0
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)


class EDPluginBioSaxsAzimutIntv1_2(EDPluginControl):
    """
    Control for Bio Saxs azimuthal integration; suppose the mask is already applied by BioSaxsNormalizev1.1 : 
    * wait for normalized file to arrive  (EDPluginWaitFile) 
    * retrieve and update metadata (EDPluginBioSaxsMetadatav1_0)
    * integrate (EDPluginSaxsAnglev1_0)
    * export as 3-column ascii-file is done here to allow more precise header      
    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAzimutIntv1_0)
        self.__strControlledPluginWaitFile = "EDPluginWaitFile"
        self.__strControlledPluginSaxsAngle = "EDPluginExecSaxsAnglev1_0"
#        self.__strControlledPluginAsciiExport = "EDPluginBioSaxsAsciiExportv1_1"
        self.__strControlledPluginSaxsGetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginWaitFile = None
        self.__edPluginSaxsAdd = None
        self.__edPluginSaxsAngle = None
#        self.__edPluginAsciiExport = None
        self.__edPluginSaxsGetMetadata = None
        self.__edPluginSaxsSetMetadata = None

        self.xsdMetadata = None
        self.sample = None
        self.experimentSetup = None
        self.normalizedImage = None
        self.integratedImage = None
        self.integratedCurve = None
        self.normalizationFactor = None

        self.lstProcessLog = []

        self.xsdResult = XSDataResultBioSaxsAzimutIntv1_0()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.normalizedImage, "Missing normalizedImage")
        self.checkMandatoryParameters(self.dataInput.normalizedImageSize, "Missing normalizedImageSize")
        self.checkMandatoryParameters(self.dataInput.integratedImage, "Missing integratedImage")
        self.checkMandatoryParameters(self.dataInput.integratedCurve, "Missing integratedCurve")
        self.checkMandatoryParameters(self.dataInput.sample, "Missing a sample description")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "Missing an experiment setup")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.preProcess")
        # Load the execution plugins
        self.sample = self.dataInput.sample
        self.experimentSetup = self.dataInput.experimentSetup
        self.__edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
        self.__edPluginSaxsAngle = self.loadPlugin(self.__strControlledPluginSaxsAngle)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.normalizedImage = self.dataInput.normalizedImage.path.value
        self.integratedImage = self.dataInput.integratedImage.path.value
        self.integratedCurve = self.dataInput.integratedCurve.path.value
        curveDir = os.path.dirname(self.integratedCurve)
        if not os.path.isdir(curveDir):
            os.mkdir(curveDir)
        integDir = os.path.dirname(self.integratedImage)
        if not os.path.isdir(integDir):
            os.mkdir(integDir)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.process")
        xsdiWaitFile = XSDataInputWaitFile(expectedFile=XSDataFile(self.dataInput.normalizedImage.path),
                                           expectedSize=self.dataInput.normalizedImageSize,
                                           timeOut=XSDataTime(30))
        self.__edPluginWaitFile.setDataInput(xsdiWaitFile)
        self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        self.__edPluginWaitFile.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSuccessGetMetadata)
            self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
            self.__edPluginSaxsGetMetadata.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsAngle.connectSUCCESS(self.doSuccessSaxsAngle)
            self.__edPluginSaxsAngle.connectFAILURE(self.doFailureSaxsAngle)
            self.__edPluginSaxsAngle.executeSynchronous()
        if not self.isFailure():
            self.write3ColumnAscii(self.integratedImage, self.integratedCurve)
            self.lstProcessLog.append("Conversion to ascii: '%s' --> '%s'" % (self.integratedImage, self.integratedCurve))
            self.xsdResult.setIntegratedCurve(self.dataInput.integratedCurve)

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.postProcess")

        # Create some output data
        strLog = os.linesep.join(self.lstProcessLog)
        self.xsdResult.status = XSDataStatus(executiveSummary=XSDataString(strLog))
        self.setDataOutput(self.xsdResult)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.postProces: Comments generated: " + os.linesep + strLog)


    def doSuccessWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_2.doSuccessWaitFile")

        self.lstProcessLog.append("Retrieve metadata from file %s" % (self.normalizedImage))
        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.inputImage = self.dataInput.normalizedImage
        xsdiMetadata.concentration = self.sample.concentration
        xsdiMetadata.comments = self.sample.comments
        xsdiMetadata.code = self.sample.code
        xsdiMetadata.detector = self.experimentSetup.detector
        xsdiMetadata.detectorDistance = self.experimentSetup.detectorDistance
        xsdiMetadata.pixelSize_1 = self.experimentSetup.pixelSize_1
        xsdiMetadata.pixelSize_2 = self.experimentSetup.pixelSize_2
        xsdiMetadata.beamCenter_1 = self.experimentSetup.beamCenter_1
        xsdiMetadata.beamCenter_2 = self.experimentSetup.beamCenter_2
        xsdiMetadata.wavelength = self.experimentSetup.wavelength
        xsdiMetadata.machineCurrent = self.experimentSetup.machineCurrent
        xsdiMetadata.maskFile = self.experimentSetup.maskFile
        xsdiMetadata.normalizationFactor = self.experimentSetup.normalizationFactor
        xsdiMetadata.beamStopDiode = self.experimentSetup.beamStopDiode
        self.__edPluginSaxsGetMetadata.setDataInput(xsdiMetadata)


    def doFailureWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_2.doFailureWaitFile")
        self.lstProcessLog.append("Timeout in waiting for file '%s'" % (self.normalizedImage))
        self.setFailure()


    def doSuccessGetMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doSuccessGetMetadata")
        if _edPlugin is not None:
            self.xsdMetadata = _edPlugin.getDataOutput()

            self.sample = self.xsdMetadata.sample
            self.experimentSetup = self.xsdMetadata.experimentSetup

            self.lstProcessLog.append("Azimuthal integration of Corrected+Masked EDF image '%s'." % (self.normalizedImage))
            xsdiSaxsAngle = XSDataInputSaxsAnglev1_0()
            xsdiSaxsAngle.setInputDataFile(self.dataInput.normalizedImage)
            # XSDataFile(XSDataString(self.normalizedImage)))
            xsdiSaxsAngle.setRegroupedDataFile(self.dataInput.getIntegratedImage())
            xsdiSaxsAngle.setOptions(XSDataString('+pass -omod n -rsys normal -da 360_deg -odim = 1'))
            self.__edPluginSaxsAngle.setDataInput(xsdiSaxsAngle)


    def doFailureGetMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_2.doFailureGetMetadata")
        self.lstProcessLog.append("Failure in GetMetadata retrieval from '%s'" % (self.normalizedImage))
        self.setFailure()


    def doSuccessSaxsAngle(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doSuccessSaxsAngle")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_2.doSuccessSaxsAngle")
        self.xsdResult.setIntegratedImage(self.dataInput.getIntegratedImage())


    def doFailureSaxsAngle(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_2.doFailureSaxsAngle")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_2.doFailureSaxsAngle")
        self.lstProcessLog.append("Error during integration with saxs_angle on '%s'" % (self.integratedImage))
        self.setFailure()


    def write3ColumnAscii(self, inputImage, outputCurve, hdr="#", linesep=os.linesep):
        """
        @param inputImage: name of the EDF 1-D image generated by saxs_angle
        @param outputCurve: name of the 3-column ascii file to be written
        @param hdr: header mark, usually '#'
        
         
Adam Round explicitelly asked for (email from Date: Tue, 04 Oct 2011 15:22:29 +0200) :
Modification from: 
        
# BSA buffer 
# Sample c= 0.0 mg/ml (these two lines are required for current DOS pipeline and can be cleaned up once we use EDNA to get to ab-initio models)
# 
# Sample environment:
# Detector = Pilatus 1M
# PixelSize_1 = 0.000172 
# PixelSize_2 = 6.283185 (I think it could avoid confusion if we give teh actual pixel size as 0.000172 for X and Y and not to give the integrated sizes. Also could there also be a modification for PixelSize_1 as on the diagonal wont it be the hypotenuse (0.000243)? and thus will be on average a bit bigger than 0.000172)
#
# title = BSA buffer 
# Frame 7 of 10
# Time per frame (s) = 10
# SampleDistance = 2.43 
# WaveLength = 9.31e-11 
# Normalization = 0.0004885 
# History-1 = saxs_angle +pass -omod n -rsys normal -da 360_deg -odim = 1 /data/id14eh3/inhouse/saxs_pilatus/Adam/EDNAtests/2d/dumdum_008_07.edf/data/id14eh3/inhouse/saxs_pilatus/Adam/EDNAtests/misc/dumdum_008_07.ang 
# DiodeCurr = 0.0001592934 
# MachCurr = 163.3938 
# Mask = /data/id14eh3/archive/CALIBRATION/MASK/Pcon_01Jun_msk.edf 
# SaxsDataVersion = 2.40 
#  
# N 3 
# L q*nm  I_BSA buffer  stddev 
# 
# Sample Information:
# Storage Temperature (degrees C): 4
# Measurement Temperature (degrees C): 10
# Concentration: 0.0
# Code: BSA
s-vector Intensity Error
s-vector Intensity Error
s-vector Intensity Error
s-vector Intensity Error
        """
        hdr = str(hdr)
        fabiofile = fabio.open(inputImage)
        npaSignal = fabiofile.data[0, :]
        npaStd = numpy.sqrt(fabiofile.next().data[0, :])
        fDistance = float(fabiofile.header["SampleDistance"])
        fPixelSize = float(fabiofile.header["PSize_1"])
        iOffset = int(fabiofile.header["Offset_1"])
        fWavelength = float(fabiofile.header["WaveLength"])
        fDummy = float(fabiofile.header["Dummy"])
        fDeltaDummy = float(fabiofile.header["DDummy"])
        npaQ = 4e-9 * numpy.pi / fWavelength * \
                    numpy.sin(numpy.arctan((numpy.arange(fabiofile.dim1) + 0.5 + iOffset) * fPixelSize / fDistance) / 2)
        headers = []
        if self.sample.comments is not None:
            headers.append(hdr + " " + self.sample.comments.value)
        else:
            headers.append(hdr)
        if self.sample.concentration is not None:
            headers.append(hdr + " Sample c= %s mg/ml" % self.sample.concentration.value)
        else:
            headers.append(hdr + " Sample c= -1  mg/ml")
        headers += [hdr,
                   hdr + " Sample environment:"]
        if self.experimentSetup.detector is not None:
            headers.append(hdr + " Detector = %s" % self.experimentSetup.detector.value)
        if self.experimentSetup.pixelSize_1 is not None:
            headers.append(hdr + " PixelSize_1 = %s" % self.experimentSetup.pixelSize_1.value)
        else:
            headers.append(hdr + " PixelSize_1 = %s" % fPixelSize)
        if self.experimentSetup.pixelSize_2 is not None:
            headers.append(hdr + " PixelSize_2 = %s" % self.experimentSetup.pixelSize_2.value)
        headers.append(hdr)
        if self.sample.comments is not None:
            headers.append(hdr + " title = %s" % self.sample.comments.value)
        if (self.experimentSetup.frameNumber is not None) and\
           (self.experimentSetup.frameMax is not None):
            headers.append(hdr + " Frame %s of %s" % (self.experimentSetup.frameNumber.value, self.experimentSetup.frameMax.value))
        if self.experimentSetup.exposureTime is not None:
            headers.append(hdr + " Time per frame (s) = %s" % self.experimentSetup.exposureTime.value)
        if self.experimentSetup.detectorDistance is not None:
            headers.append(hdr + " SampleDistance = %s" % fDistance)
        if self.experimentSetup.wavelength is not None:
            headers.append(hdr + " WaveLength = %s" % fWavelength)
        if self.experimentSetup.normalizationFactor is not None:
            headers.append(hdr + " Normalization = %s" % self.experimentSetup.normalizationFactor.value)
        history = [key for key in fabiofile.header if key.startswith("History")]
        history.sort()
        for key in  history:
            headers.append(hdr + " " + key + " = " + fabiofile.header[key])
        if self.experimentSetup.beamStopDiode is not None:
            headers.append(hdr + " DiodeCurr = %s" % self.experimentSetup.beamStopDiode.value)
        if self.experimentSetup.machineCurrent is not None:
            headers.append(hdr + " MachCurr = %s" % self.experimentSetup.machineCurrent.value)
        if self.experimentSetup.maskFile is not None:
            headers.append(hdr + " Mask = %s" % self.experimentSetup.maskFile.path.value)
        if "SaxsDataVersion" in fabiofile.header:
            headers.append(hdr + " SaxsDataVersion = %s" % fabiofile.header["SaxsDataVersion"])
        headers.append(hdr)
        headers.append(hdr + " N 3")
        if self.sample.comments is not None:
            headers.append(hdr + " L q*nm  I_%s  stddev" % self.sample.comments.value)
        else:
            headers.append(hdr + " L q*nm  I_  stddev")
        headers.append(hdr)
        headers.append(hdr + " Sample Information:")
        if self.experimentSetup.storageTemperature is not None:
            headers.append(hdr + " Storage Temperature (degrees C): %s" % self.experimentSetup.storageTemperature.value)
        if self.experimentSetup.exposureTemperature is not None:
            headers.append(hdr + " Measurement Temperature (degrees C): %s" % self.experimentSetup.exposureTemperature.value)

        if self.sample.concentration is not None:
            headers.append(hdr + " Concentration: %s" % self.sample.concentration.value)
        else:
            headers.append(hdr + " Concentration: -1")
        if self.sample.code is not None:
            headers.append(hdr + " Code: %s" % self.sample.code.value)
        else:
            headers.append(hdr + " Code: ")

        with open(outputCurve, "w") as f:
            f.writelines(linesep.join(headers))
            f.write(linesep)
            for q, I, std in zip(npaQ, npaSignal, npaStd):
                if abs(I - fDummy) > fDeltaDummy:
                    f.write("%14.6e %14.6e %14.6e%s" % (q, I, std, linesep))
            f.flush()

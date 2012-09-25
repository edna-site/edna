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
__date__ = "20120824"
__status__ = "development"

import os
from EDUtilsArray           import EDUtilsArray
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPlatform        import EDUtilsPlatform
from EDUtilsPath            import EDUtilsPath
from XSDataCommon           import XSDataString, XSDataStatus, XSDataTime, XSDataFile, XSDataAngle, \
                                    XSDataDouble, XSDataInteger
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsAzimutIntv1_0, XSDataResultBioSaxsAzimutIntv1_0, \
                                XSDataInputBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataPyFAIv1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataPyFAIv1_0        import XSDataInputPyFAI, XSDataDetector, XSDataGeometryFit2D
from EDUtilsParallel        import EDUtilsParallel
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
import pyFAI

class EDPluginBioSaxsAzimutIntv1_3(EDPluginControl):
    """
    Control for Bio Saxs azimuthal integration; suppose the mask is already applied by BioSaxsNormalizev1.1 :
    * wait for normalized file to arrive  (EDPluginWaitFile)
    * retrieve and update metadata (EDPluginBioSaxsMetadatav1_0)
    * integrate (directly vi pyFAI)
    * export as 3-column ascii-file is done here to allow more precise header
    Changelog since v1.2: use PyFAI instead of saxs_angle from Peter Boesecke
    """
    cpWaitFile = "EDPluginWaitFile"
    cpGetMetadata = "EDPluginBioSaxsMetadatav1_1"
    integrator = pyFAI.AzimuthalIntegrator()
    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAzimutIntv1_0)
        self.__edPluginWaitFile = None
        self.__edPluginMetadata = None
        self.xsdMetadata = None
        self.sample = None
        self.experimentSetup = None
        self.normalizedImage = None
        self.integratedCurve = None
        self.normalizationFactor = None

        self.lstProcessLog = []
        self.npaOut = None
        self.xsdResult = XSDataResultBioSaxsAzimutIntv1_0()
        self.dummy = -1
        self.delta_dummy = 0.1
        self .integrator_config = {}

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.normalizedImage, "Missing normalizedImage")
        self.checkMandatoryParameters(self.dataInput.normalizedImageSize, "Missing normalizedImageSize")
        self.checkMandatoryParameters(self.dataInput.integratedCurve, "Missing integratedCurve")
        self.checkMandatoryParameters(self.dataInput.sample, "Missing a sample description")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "Missing an experiment setup")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.preProcess")
        # Load the execution plugins
        self.sample = self.dataInput.sample
        self.experimentSetup = self.dataInput.experimentSetup
        self.__edPluginWaitFile = self.loadPlugin(self.cpWaitFile)
        self.__edPluginMetadata = self.loadPlugin(self.cpGetMetadata)
        self.normalizedImage = self.dataInput.normalizedImage.path.value
        self.integratedCurve = self.dataInput.integratedCurve.path.value
        curveDir = os.path.dirname(self.integratedCurve)
        if not os.path.isdir(curveDir):
            try:
                os.mkdir(curveDir)
            except OSError:
                pass



    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.process")
        self.__edPluginWaitFile.dataInput = XSDataInputWaitFile(expectedFile=XSDataFile(self.dataInput.normalizedImage.path),
                                           expectedSize=self.dataInput.normalizedImageSize,
                                           timeOut=XSDataTime(30))
        self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        self.__edPluginWaitFile.executeSynchronous()
        if self.isFailure():
            return
        self.__edPluginMetadata.connectSUCCESS(self.doSuccessGetMetadata)
        self.__edPluginMetadata.connectFAILURE(self.doFailureGetMetadata)
        self.__edPluginMetadata.executeSynchronous()
        if self.isFailure():
            return
        if not self.isFailure():
            q, I, std = self.integrate()
            self.write3ColumnAscii(q, I, std, self.integratedCurve)
#            self.lstProcessLog.append("Conversion to ascii --> '%s'" % (self.integratedCurve))
            self.xsdResult.setIntegratedCurve(self.dataInput.integratedCurve)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.postProcess")

        # Create some output data
        strLog = os.linesep.join(self.lstProcessLog)
        self.xsdResult.status = XSDataStatus(executiveSummary=XSDataString(strLog))
        self.xsdResult.sample = self.sample
        self.xsdResult.experimentSetup = self.experimentSetup

        self.setDataOutput(self.xsdResult)
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.postProces: Comments generated: " + os.linesep + strLog)


    def doSuccessWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_3.doSuccessWaitFile")

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
        self.__edPluginMetadata.dataInput = xsdiMetadata


    def doFailureWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_3.doFailureWaitFile")
        self.lstProcessLog.append("Timeout in waiting for file '%s'" % (self.normalizedImage))
        self.setFailure()


    def doSuccessGetMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.doSuccessGetMetadata")
        if _edPlugin is not None:
            self.xsdMetadata = _edPlugin.dataOutput
            self.sample = self.xsdMetadata.sample
            self.experimentSetup = self.xsdMetadata.experimentSetup

            self.lstProcessLog.append("Azimuthal integration of Corrected+Masked EDF image -->'%s'." % (self.integratedCurve))
            self .integrator_config = {'dist': self.experimentSetup.detectorDistance.value,
                            'pixel1': self.experimentSetup.pixelSize_2.value, # flip X,Y
                            'pixel2': self.experimentSetup.pixelSize_1.value, # flip X,Y
                            'poni1': self.experimentSetup.beamCenter_2.value * self.experimentSetup.pixelSize_2.value,
                            'poni2': self.experimentSetup.beamCenter_1.value * self.experimentSetup.pixelSize_1.value,
                            'rot1': 0.0,
                            'rot2': 0.0,
                            'rot3': 0.0,
                            'splineFile': None}
#
#            detector = XSDataDetector(name=XSDataString(self.experimentSetup.detector.value.capitalize().replace(" ", "")),
#                                      pixelSizeX=self.xsdMetadata.pixelSize_1,
#                                      pixelSizeY=self.xsdMetadata.pixelSize_2,
#                                      )
#            geometry = XSDataGeometryFit2D(detector=detector,
#                                           distance=self.experimentSetup.detectorDistance,
#                                           beamCentreInPixelsX=self.xsdMetadata.beamCenter_1,
#                                           beamCentreInPixelsY=self.xsdMetadata.beamCenter_2,
#                                           tiltRotation=XSDataAngle(0.0),
#                                           angleOfTilt=XSDataAngle(0.0))
#            self.__edPluginPyFAI.dataInput = XSDataInputPyFAI(input=self.dataInput.normalizedImage,
#                                             dummy=XSDataDouble(self.dummy),
#                                             deltaDummy=XSDataDouble(self.delta_dummy),
#                                             geometryFit2D=geometry,
#                                             nbPt=XSDataInteger(500),
#                                             wavelength=self.experimentSetup.wavelength,
#                                             saxsWaxs=XSDataString("saxs"))


    def doFailureGetMetadata(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsAzimutIntv1_3.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_3.doFailureGetMetadata")
        self.lstProcessLog.append("Failure in GetMetadata retrieval from '%s'" % (self.normalizedImage))
        self.setFailure()


    def integrate(self):
        if (self.integrator.getPyFAI() != self.integrator_config) or \
           (self.integrator.wavelength != self.experimentSetup.wavelength.value):
            self.screen("Resetting PyFAI integrator")
            self.integrator.setPyFAI(**self.integrator_config)
            self.integrator.wavelength = self.experimentSetup.wavelength.value
        with EDUtilsParallel.getSemaphoreNbThreads():
            img = fabio.open(self.normalizedImage)
            variance = img.next()
            q, I, std = self.integrator.saxs(data=img.data, nbPt=max(img.dim1, img.dim2),
                                       correctSolidAngle=True,
                                       variance=variance.data,
                                       dummy= -2, delta_dummy=1.1,
                                       method="splitBBox")
        return q, I, std
    def write3ColumnAscii(self, npaQ, npaI, npaStd=None, outputCurve="output.dat", hdr="#", linesep=os.linesep):
        """
        @param npaQ,npaI,npaStd: 3x 1d numpy array containing Scattering vector, Intensity and deviation
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
            headers.append(hdr + " SampleDistance = %s" % self.experimentSetup.detectorDistance.value)
        if self.experimentSetup.wavelength is not None:
            headers.append(hdr + " WaveLength = %s" % self.experimentSetup.wavelength.value)
        if self.experimentSetup.normalizationFactor is not None:
            headers.append(hdr + " Normalization = %s" % self.experimentSetup.normalizationFactor.value)
        if self.experimentSetup.beamStopDiode is not None:
            headers.append(hdr + " DiodeCurr = %s" % self.experimentSetup.beamStopDiode.value)
        if self.experimentSetup.machineCurrent is not None:
            headers.append(hdr + " MachCurr = %s" % self.experimentSetup.machineCurrent.value)
        if self.experimentSetup.maskFile is not None:
            headers.append(hdr + " Mask = %s" % self.experimentSetup.maskFile.path.value)
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
            if npaStd is None:
                data = ["%14.6e %14.6e " % (q, I)
                        for q, I in zip(npaQ, npaI)
                        if abs(I - self.dummy) > self.delta_dummy]
            else:
                data = ["%14.6e %14.6e %14.6e" % (q, I, std)
                        for q, I, std in zip(npaQ, npaI, npaStd)
                        if abs(I - self.dummy) > self.delta_dummy]
            data.append("")
            f.writelines(linesep.join(data))
            f.flush()

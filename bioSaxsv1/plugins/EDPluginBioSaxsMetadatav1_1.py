# coding:utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Jérôme Kieffer
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

"""
Retrieves and update metadata taken from EDF files, and optionally save them
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20111014"
__status = "production"

import os, shutil

from EDVerbose                  import EDVerbose
from EDPluginExec               import EDPluginExec
from EDUtilsBioSaxs             import EDUtilsBioSaxs
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDUtilsPath                import EDUtilsPath
from XSDataCommon               import XSDataString, XSDataImage, \
                         XSDataDouble, XSDataLength, XSDataWavelength, \
                         XSDataTime, XSDataInteger, XSDataTime
from XSDataBioSaxsv1_0          import XSDataInputBioSaxsMetadatav1_0, \
                                     XSDataResultBioSaxsMetadatav1_0, \
                                     XSDataBioSaxsExperimentSetup, \
                                     XSDataBioSaxsSample
from EDUtilsPlatform            import EDUtilsPlatform

architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)

if fabio is None:
    EDVerbose.ERROR("Unable to import Fabio: Please re-run the tests EDTestSuiteBioSaxs")


class EDPluginBioSaxsMetadatav1_1(EDPluginExec):
    """
    Plugin for reading, updating and writing Metadata. 
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)

        self.setXSDataInputClass(XSDataInputBioSaxsMetadatav1_0)
        self.xsdInputData = None
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
        self.storageTemperature = None
        self.exposureTemperature = None
        self.exposureTime = None
        self.frameNumber = None
        self.frameMax = None
        self.timeOfFrame = None
        #
        self.code = None
        self.comments = None
        self.concentration = None
        self.strInputImage = None
        self.strOutputImage = None
        self.fabioedf = fabio.edfimage.edfimage()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.xsdInputData = self.dataInput
        self.checkMandatoryParameters(self.xsdInputData.getInputImage(), "No input Image given !")


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_1.preProcess")
        self.strInputImage = self.xsdInputData.getInputImage().getPath().value
        if self.xsdInputData.getDetector() is not None:
            self.detector = self.xsdInputData.getDetector().value
        if self.xsdInputData.detectorDistance is not None:
            self.detectorDistance = self.xsdInputData.detectorDistance.value
        if self.xsdInputData.beamCenter_1 is not None:
            self.beamCenter_1 = self.xsdInputData.beamCenter_1.value
        if self.xsdInputData.pixelSize_1 is not None:
            self.pixelSize_1 = self.xsdInputData.pixelSize_1.value
        if self.xsdInputData.beamCenter_2 is not None:
            self.beamCenter_2 = self.xsdInputData.beamCenter_2.value
        if self.xsdInputData.pixelSize_2 is not None:
            self.pixelSize_2 = self.xsdInputData.pixelSize_2.value
        if self.xsdInputData.beamStopDiode is not None:
            self.beamStopDiode = self.xsdInputData.beamStopDiode.value
        if self.xsdInputData.storageTemperature is not None:
            self.storageTemperature = self.xsdInputData.storageTemperature.value
        if    self.xsdInputData.exposureTemperature is not None:
            self.exposureTemperature = self.xsdInputData.exposureTemperature.value
        if    self.xsdInputData.exposureTime is not None:
            self.exposureTime = self.xsdInputData.exposureTemperature.value
        if    self.xsdInputData.frameNumber is not None:
            self.frameNumber = self.xsdInputData.exposureTemperature.value
        if    self.xsdInputData.frameMax is not None:
            self.frameMax = self.xsdInputData.exposureTemperature.value
        if self.xsdInputData.code is not None:
            self.code = self.xsdInputData.code.value
        if self.xsdInputData.comments is not None:
            self.comments = self.xsdInputData.comments.value
        if self.xsdInputData.concentration is not None:
            self.concentration = self.xsdInputData.concentration.value
        if self.xsdInputData.machineCurrent is not None:
            self.machineCurrent = self.xsdInputData.machineCurrent.value
        if self.xsdInputData.wavelength is not None:
            self.wavelength = self.xsdInputData.wavelength.value
        if self.xsdInputData.normalizationFactor is not None:
            self.normalizationFactor = self.xsdInputData.normalizationFactor.value
        if self.xsdInputData.maskFile is not None:
            self.maskFile = self.xsdInputData.maskFile.getPath().value
        if self.xsdInputData.getOutputImage() is not None:
            self.strOutputImage = self.xsdInputData.getOutputImage().getPath().value


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_1.process")
        if not os.path.isfile(self.strInputImage):
            EDVerbose.WARNING("The given input file does not exist !!!")
            header = {}
        else:
            self.fabioedf = fabio.open(self.strInputImage)
            if not isinstance(self.fabioedf, fabio.edfimage.edfimage):
                self.fabioedf = fabio.edfimage.edfimage(data=self.fabioedf.data, header=self.fabioedf.header)
            header = self.fabioedf.header
            for key in EDUtilsBioSaxs.TRANSLATION:
                if self.__getattribute__(key) is None:
                    if EDUtilsBioSaxs.TRANSLATION[key] in header:
                        if key in EDUtilsBioSaxs.FLOAT_KEYS:
                            self.__setattr__(key, float(header[EDUtilsBioSaxs.TRANSLATION[key]]))
                        elif key in EDUtilsBioSaxs.INT_KEYS:
                            self.__setattr__(key, int(header[EDUtilsBioSaxs.TRANSLATION[key]]))
                        else:
                            self.__setattr__(key, header[EDUtilsBioSaxs.TRANSLATION[key]])

        if self.strOutputImage is not None:
            if os.path.abspath(self.strOutputImage) != os.path.abspath(self.strInputImage):
                shutil.copy(self.strInputImage, self.strOutputImage)
            keyToUpgrade = []
            for key in EDUtilsBioSaxs.TRANSLATION:
                if self.__getattribute__(key) is not None:
                    if EDUtilsBioSaxs.TRANSLATION[key] not in header:
                        keyToUpgrade.append(key)
                    else:
                        if key in EDUtilsBioSaxs.FLOAT_KEYS:
                            oneHeader = float(header[EDUtilsBioSaxs.TRANSLATION[key]])
                        elif key in EDUtilsBioSaxs.INT_KEYS:
                            oneHeader = int(header[EDUtilsBioSaxs.TRANSLATION[key]])
                        else:
                            oneHeader = header[EDUtilsBioSaxs.TRANSLATION[key]]
                        oneValue = self.__getattribute__(key)
                        EDVerbose.DEBUG("key: %s value_header=%s(%s) value_extra=%s(%s)" % (key, oneHeader, oneHeader.__class__, self.__getattribute__(key), self.__getattribute__(key).__class__))
                        if oneHeader != oneValue:
                            keyToUpgrade.append(key)
            if keyToUpgrade:
                for key in keyToUpgrade:
                    self.fabioedf.header_keys.append(EDUtilsBioSaxs.TRANSLATION[key])
                    self.fabioedf.header[EDUtilsBioSaxs.TRANSLATION[key]] = str(self.__getattribute__(key))
                self.fabioedf.write(self.strOutputImage)


    def postProcess(self, _edObject=None):
        """
complex type XSDataBioSaxsExperimentSetup extends XSData{
    detector : XSDataString optional
    detectorDistance : XSDataLength optional
    pixelSize_1 : XSDataLength optional
    pixelSize_2 : XSDataLength optional
    beamCenter_1 : XSDataDouble optional
    beamCenter_2 : XSDataDouble optional
    beamStopDiode : XSDataDouble optional
    wavelength : XSDataWavelength optional
    machineCurrent : XSDataDouble optional
    maskFile : XSDataImage optional
    normalizationFactor : XSDataDouble optional
    storageTemperature: XSDataDouble optional
    exposureTemperature: XSDataDouble optional
    exposureTime: XSDataTime optional
    frameNumber: XSDataInteger optional
    frameMax: XSDataInteger optional
}

complex type XSDataBioSaxsSample extends XSData {
    concentration : XSDataDouble optional
    comments : XSDataString optional
    code : XSDataString optional
    temperature: XSDataDouble optional
"""

        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_1.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsMetadatav1_0()
        xsdSample = XSDataBioSaxsSample()
        xsdExperiment = XSDataBioSaxsExperimentSetup()
        if self.strOutputImage is not None:
            xsdImage = XSDataImage()
            xsdImage.setPath(XSDataString(self.strOutputImage))
            xsDataResult.setOutputImage(xsdImage)
        if self.detector is not None:
            xsdExperiment.detector = xsDataResult.detector = XSDataString(self.detector)
        if self.detectorDistance is not None:
            xsdExperiment.detectorDistance = xsDataResult.detectorDistance = XSDataLength(self.detectorDistance)
        if self.pixelSize_1 is not None:
            xsDataResult.pixelSize_1 = XSDataLength(self.pixelSize_1)
            xsdExperiment.pixelSize_1 = xsDataResult.pixelSize_1
        if self.pixelSize_2 is not None:
            xsDataResult.pixelSize_2 = XSDataLength(self.pixelSize_2)
            xsdExperiment.pixelSize_2 = xsDataResult.pixelSize_2
        if self.beamCenter_1 is not None:
            xsDataResult.beamCenter_1 = XSDataDouble(self.beamCenter_1)
            xsdExperiment.beamCenter_1 = xsDataResult.beamCenter_1
        if self.beamCenter_2 is not None:
            xsDataResult.beamCenter_2 = XSDataDouble(self.beamCenter_2)
            xsdExperiment.beamCenter_2 = xsDataResult.beamCenter_2
        if self.beamStopDiode is not None:
            xsdExperiment.beamStopDiode = xsDataResult.beamStopDiode = XSDataDouble(self.beamStopDiode)
        if self.wavelength is not None:
            xsdExperiment.wavelength = xsDataResult.wavelength = XSDataWavelength(self.wavelength)
        if self.maskFile is not None:
            xsdFile = XSDataImage()
            xsdFile.setPath(XSDataString(self.maskFile))
            xsdExperiment.maskFile = xsDataResult.maskFile = xsdFile
        if self.normalizationFactor is not None:
            xsdExperiment.normalizationFactor = xsDataResult.normalizationFactor = XSDataDouble(self.normalizationFactor)
        if self.machineCurrent is not None:
            xsdExperiment.machineCurrent = xsDataResult.machineCurrent = XSDataDouble(self.machineCurrent)
        if self.storageTemperature is not None:
            xsdExperiment.storageTemperature = xsDataResult.storageTemperature = XSDataDouble(self.storageTemperature)
        if self.exposureTemperature is not None:
            xsdExperiment.exposureTemperature = xsDataResult.exposureTemperature = XSDataDouble(self.exposureTemperature)
        if self.exposureTime is not None:
            xsdExperiment.exposureTime = xsDataResult.exposureTime = XSDataTime(self.exposureTime)
        if self.frameNumber is not None:
            xsdExperiment.frameNumber = xsDataResult.frameNumber = XSDataInteger(self.frameNumber)
        if self.frameMax is not None:
            xsdExperiment.frameMax = xsDataResult.frameMax = XSDataInteger(self.frameMax)
        if self.timeOfFrame is not None:
            xsdExperiment.timeOfFrame = xsDataResult.timeOfFrame = XSDataTime(self.timeOfFrame)
        if self.code is not None:
            xsdSample.code = xsDataResult.code = XSDataString(self.code)
        if self.comments is not None:
            xsdSample.comments = xsDataResult.comments = XSDataString(self.comments)
        if self.concentration is not None:
            xsdSample.concentration = xsDataResult.concentration = XSDataDouble(self.concentration)

        xsDataResult.sample = xsdSample
        xsDataResult.experimentSetup = xsdExperiment
        self.setDataOutput(xsDataResult)



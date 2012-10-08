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
__status__ = "deprecated"

import os, shutil
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDUtilsBioSaxs     import EDUtilsBioSaxs
from EDUtilsPath        import EDUtilsPath
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon       import XSDataString, XSDataImage, XSDataDouble, XSDataLength, \
    XSDataWavelength
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsMetadatav1_0, XSDataResultBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataSaxsv1_0             import XSDataInputSaxsAddMetadatav1_0
from EDUtilsPlatform   import EDUtilsPlatform

architecture = EDUtilsPlatform.architecture
edfFilePath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "EdfFile", architecture)
EdfFileMod = EDFactoryPluginStatic.preImport("EdfFile", edfFilePath)
if EdfFileMod is None:
    EDVerbose.ERROR("Unable to import EdfFile: Please re-run the tests EDTestSuiteBioSaxs")
else:
    from EdfFile import EdfFile


class EDPluginBioSaxsMetadatav1_0(EDPluginControl):
    """
    Plugin for reading, updating and writing Metadata. 
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.__strControlledPluginMetadata = "EDPluginExecSaxsAddMetadatav1_0"

        self.setXSDataInputClass(XSDataInputBioSaxsMetadatav1_0)
        self.xsdInputData = None
        self.__bSaxsMetadataFailed = False
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


        self.code = None
        self.comments = None
        self.concentration = None

        self.strInputImage = None
        self.strOutputImage = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.xsdInputData = self.dataInput
        self.checkMandatoryParameters(self.xsdInputData.getInputImage(), "No input Image given !")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.preProcess")
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
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.process")
        if not os.path.isfile(self.strInputImage):
            EDVerbose.WARNING("The given input file does not exist !!!")
            header = {}
        else:
            header = EdfFile(self.strInputImage).GetHeader(0)
            for key in EDUtilsBioSaxs.TRANSLATION:
                if key in dir(self) and  self.__getattribute__(key) is None:
                    if EDUtilsBioSaxs.TRANSLATION[key] in header:
                        if key in EDUtilsBioSaxs.FLOAT_KEYS:
                            setattr(self, key, float(header[EDUtilsBioSaxs.TRANSLATION[key]]))
                        else:
                            setattr(self, key, header[EDUtilsBioSaxs.TRANSLATION[key]])
        if self.strOutputImage is not None:
            if os.path.abspath(self.strOutputImage) != os.path.abspath(self.strInputImage):
                shutil.copy(self.strInputImage, self.strOutputImage)
            keyToUpgrade = []
            for key in EDUtilsBioSaxs.TRANSLATION:
                if key in dir(self) and  self.__getattribute__(key) is None:
                    if EDUtilsBioSaxs.TRANSLATION[key] not in header:
                        keyToUpgrade.append(key)
                    else:

                        if key in EDUtilsBioSaxs.FLOAT_KEYS:
                            oneHeader = float(header[EDUtilsBioSaxs.TRANSLATION[key]])
                        else:
                            oneHeader = header[EDUtilsBioSaxs.TRANSLATION[key]]
                        oneValue = eval("self.%s" % key)
                        EDVerbose.DEBUG("key: %s value_header=%s(%s) value_extra=%s(%s)" % (key, oneHeader, oneHeader.__class__, eval("self.%s" % key), eval("self.%s" % key).__class__))
                        if oneHeader != oneValue:
                            keyToUpgrade.append(key)
            for key in keyToUpgrade:
                if not self.__bSaxsMetadataFailed:
                    xsdi = XSDataInputSaxsAddMetadatav1_0()
                    xsdi.setInputImage(self.xsdInputData.getOutputImage())
                    xsdi.setKey(XSDataString(EDUtilsBioSaxs.TRANSLATION[key]))
                    xsdi.setValue(XSDataString("%s" % eval("self.%s" % key)))
                    edPlugin = self.loadPlugin(self.__strControlledPluginMetadata)
                    edPlugin.setDataInput(xsdi)
                    edPlugin.connectSUCCESS(self.doSuccessMetadata)
                    edPlugin.connectFAILURE(self.doFailureMetadata)
                    edPlugin.executeSynchronous ()

            if self.__bSaxsMetadataFailed:
                EDVerbose.screen("EDPluginBioSaxsMetadatav1_0.process: writeMetadata using EdfFile ")
                edf = EdfFile(self.strOutputImage)
                headers = [edf.GetHeader(i) for i in xrange(edf.GetNumImages())]
                data = [edf.GetData(i) for i in xrange(edf.GetNumImages())]
                del edf
                for key in EDUtilsBioSaxs.TRANSLATION:
                    if key in dir(self) and  self.__getattribute__(key) is None:
                        header[EDUtilsBioSaxs.TRANSLATION[key]] = eval("self.%s" % key)

                edf = EdfFile(self.strOutputImage)
                if len(data) == 1:
                    edf.WriteImage(header, data[0], Append=0)
                elif len(data) > 1:
                    edf.WriteImage(header, data[0], Append=0)
                    for datum in data[1:]:
                        edf.WriteImage({}, datum, Append=1)
                else:
                    EDVerbose.WARNING("There are not data in %s !!!" % self.strInputImage)





    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsMetadatav1_0()
        if self.strOutputImage is not None:
            xsdImage = XSDataImage()
            xsdImage.setPath(XSDataString(self.strOutputImage))
            xsDataResult.setOutputImage(xsdImage)
        if self.detector is not None:
#            EDVerbose.DEBUG("Detector=%s" % self.detector)
            xsDataResult.setDetector(XSDataString(self.detector))
        if self.detectorDistance is not None:
#            EDVerbose.DEBUG("DetectorDistance %s(%s)" % (self.detectorDistance, self.detectorDistance.__class__))
            xsDataResult.setDetectorDistance(XSDataLength(self.detectorDistance))
        if self.pixelSize_1 is not None:
#            EDVerbose.DEBUG("pixelSize_1  %s(%s)" % (self.pixelSize_1, self.pixelSize_1.__class__))
            xsDataResult.setPixelSize_1(XSDataLength(self.pixelSize_1))
        if self.pixelSize_2 is not None:
#            EDVerbose.DEBUG("pixelSize_2  %s(%s)" % (self.pixelSize_2, self.pixelSize_2.__class__))
            xsDataResult.setPixelSize_2(XSDataLength(self.pixelSize_2))
        if self.beamCenter_1 is not None:
#            EDVerbose.DEBUG("beamCenter_1  %s(%s)" % (self.beamCenter_1, self.beamCenter_1.__class__))
            xsDataResult.setBeamCenter_1(XSDataDouble(self.beamCenter_1))
        if self.beamCenter_2 is not None:
#            EDVerbose.DEBUG("beamCenter_2  %s(%s)" % (self.beamCenter_2, self.beamCenter_2.__class__))
            xsDataResult.setBeamCenter_2(XSDataDouble(self.beamCenter_2))
        if self.beamStopDiode is not None:
#            EDVerbose.DEBUG("beamStopDiode  %s(%s)" % (self.beamStopDiode, self.beamStopDiode.__class__))
            xsDataResult.setBeamStopDiode(XSDataDouble(self.beamStopDiode))
        if self.wavelength is not None:
            xsDataResult.setWavelength(XSDataWavelength(self.wavelength))
        if self.maskFile is not None:
            xsdFile = XSDataImage()
            xsdFile.setPath(XSDataString(self.maskFile))
            xsDataResult.setMaskFile(xsdFile)
        if self.normalizationFactor is not None:
            xsDataResult.setNormalizationFactor(XSDataDouble(self.normalizationFactor))
        if self.machineCurrent is not None:
            xsDataResult.setMachineCurrent(XSDataDouble(self.machineCurrent))
        if self.code is not None:
            xsDataResult.setCode(XSDataString(self.code))
        if self.comments is not None:
            xsDataResult.setComments(XSDataString(self.comments))
        if self.concentration is not None:
            xsDataResult.setConcentration(XSDataDouble(self.concentration))
        EDVerbose.DEBUG("xsDataResult=%s" % xsDataResult.marshal())
        self.setDataOutput(xsDataResult)

    def doSuccessMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.doSuccessSaxsMetadata")
    def doFailureMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsMetadatav1_0.doFailureSaxsMetadata with: \n%s" % _edPlugin.dataInput.marshal())
        self.__bSaxsMetadataFailed = True
#        self.setFailure()


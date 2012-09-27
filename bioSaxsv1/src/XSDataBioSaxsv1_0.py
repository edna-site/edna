#!/usr/bin/env python

#
# Generated Thu Sep 27 11:01::24 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataEdnaSaxs": "ednaSaxs/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataEdnaSaxs import XSDataAutoRg
    from XSDataEdnaSaxs import XSDataGnom
    from XSDataCommon import XSDataDoubleWithUnit
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
    from XSDataCommon import XSDataWavelength
except ImportError as error:
    if strEdnaHome is not None:
        for strXsdName in dictLocation:
            strXsdModule = strXsdName + ".py"
            strRootdir = os.path.dirname(os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName])))
            for strRoot, listDirs, listFiles in os.walk(strRootdir):
                if strXsdModule in listFiles:
                    sys.path.append(strRoot)
    else:
        raise error
from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataEdnaSaxs import XSDataAutoRg
from XSDataEdnaSaxs import XSDataGnom
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength




#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith('3'):
    unicode = str
    from io import StringIO
else:
    from StringIO import StringIO


def showIndent(outfile, level):
    for idx in range(level):
        outfile.write(unicode('    '))


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    #if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
    #    print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer(object):
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:     # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write(unicode('<%s>%s</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write(unicode('<%s>%d</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write(unicode('<%s>%f</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write(unicode('<%s>%g</%s>' % (self.name, self.value, self.name)))

#
# Data representation classes.
#



class XSDataBioSaxsExperimentSetup(XSData):
    def __init__(self, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSData.__init__(self,)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detector' is not XSDataString but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detectorDistance' is not XSDataLength but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_1' is not XSDataLength but %s" % self._pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_2' is not XSDataLength but %s" % self._pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_1' is not XSDataDouble but %s" % self._beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_2' is not XSDataDouble but %s" % self._beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamStopDiode' is not XSDataDouble but %s" % self._beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'machineCurrent' is not XSDataDouble but %s" % self._machineCurrent.__class__.__name__
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'maskFile' is not XSDataImage but %s" % self._maskFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'normalizationFactor' is not XSDataDouble but %s" % self._normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'storageTemperature' is not XSDataDouble but %s" % self._storageTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'exposureTemperature' is not XSDataDouble but %s" % self._exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'exposureTime' is not XSDataTime but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'frameNumber' is not XSDataInteger but %s" % self._frameNumber.__class__.__name__
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'frameMax' is not XSDataInteger but %s" % self._frameMax.__class__.__name__
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'timeOfFrame' is not XSDataTime but %s" % self._timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setDetector argument is not XSDataString but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setDetectorDistance argument is not XSDataLength but %s" % detectorDistance.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_1 argument is not XSDataLength but %s" % pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_1(self): self._pixelSize_1 = None
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_2 argument is not XSDataLength but %s" % pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_2(self): self._pixelSize_2 = None
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_1 argument is not XSDataDouble but %s" % beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_1(self): self._beamCenter_1 = None
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_2 argument is not XSDataDouble but %s" % beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_2(self): self._beamCenter_2 = None
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamStopDiode argument is not XSDataDouble but %s" % beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
    def delBeamStopDiode(self): self._beamStopDiode = None
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setMachineCurrent argument is not XSDataDouble but %s" % machineCurrent.__class__.__name__
            raise BaseException(strMessage)
    def delMachineCurrent(self): self._machineCurrent = None
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setMaskFile argument is not XSDataImage but %s" % maskFile.__class__.__name__
            raise BaseException(strMessage)
    def delMaskFile(self): self._maskFile = None
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setNormalizationFactor argument is not XSDataDouble but %s" % normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizationFactor(self): self._normalizationFactor = None
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setStorageTemperature argument is not XSDataDouble but %s" % storageTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delStorageTemperature(self): self._storageTemperature = None
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setExposureTemperature argument is not XSDataDouble but %s" % exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTemperature(self): self._exposureTemperature = None
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setExposureTime argument is not XSDataTime but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setFrameNumber argument is not XSDataInteger but %s" % frameNumber.__class__.__name__
            raise BaseException(strMessage)
    def delFrameNumber(self): self._frameNumber = None
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setFrameMax argument is not XSDataInteger but %s" % frameMax.__class__.__name__
            raise BaseException(strMessage)
    def delFrameMax(self): self._frameMax = None
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self): return self._timeOfFrame
    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setTimeOfFrame argument is not XSDataTime but %s" % timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    def delTimeOfFrame(self): self._timeOfFrame = None
    timeOfFrame = property(getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame")
    def export(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_='detectorDistance')
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_='machineCurrent')
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_='maskFile')
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_='storageTemperature')
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_='frameNumber')
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_='frameMax')
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_='timeOfFrame')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_1':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_2':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamStopDiode':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineCurrent':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maskFile':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizationFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'storageTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameMax':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeOfFrame':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataBioSaxsExperimentSetup")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataBioSaxsExperimentSetup')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataBioSaxsExperimentSetup is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataBioSaxsExperimentSetup.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataBioSaxsExperimentSetup")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataBioSaxsExperimentSetup


class XSDataBioSaxsSample(XSData):
    def __init__(self, code=None, comments=None, concentration=None):
        XSData.__init__(self,)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s" % self._concentration.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'code' is not XSDataString but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'concentration' attribute
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setConcentration argument is not XSDataDouble but %s" % concentration.__class__.__name__
            raise BaseException(strMessage)
    def delConcentration(self): self._concentration = None
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setCode argument is not XSDataString but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='XSDataBioSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBioSaxsSample'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataBioSaxsSample')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataBioSaxsSample")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataBioSaxsSample


class XSDataFileSeries(XSData):
    def __init__(self, files=None):
        XSData.__init__(self,)
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataFileSeries constructor argument 'files' is not list but %s" % self._files.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'files' attribute
    def getFiles(self): return self._files
    def setFiles(self, files):
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataFileSeries.setFiles argument is not list but %s" % files.__class__.__name__
            raise BaseException(strMessage)
    def delFiles(self): self._files = None
    files = property(getFiles, setFiles, delFiles, "Property for files")
    def addFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._files.append(value)
        else:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataFileSeries.insertFiles argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataFileSeries.insertFiles argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._files[index] = value
        else:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataFileSeries'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataFileSeries'):
        XSData.exportChildren(self, outfile, level, name_)
        for files_ in self.getFiles():
            files_.export(outfile, level, name_='files')
        if self.getFiles() == []:
            warnEmptyAttribute("files", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'files':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.files.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataFileSeries")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataFileSeries')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataFileSeries is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataFileSeries.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataFileSeries")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataFileSeries


class XSDataInputBioSaxsAsciiExportv1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None):
        XSDataInput.__init__(self, configuration)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'integratedImage' is not XSDataImage but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setIntegratedImage argument is not XSDataImage but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def export(self, outfile, level, name_='XSDataInputBioSaxsAsciiExportv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAsciiExportv1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_='integratedImage')
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsAsciiExportv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAsciiExportv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsAsciiExportv1_0


class XSDataInputBioSaxsAzimutIntv1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, correctedImage=None, integratedCurve=None, integratedImage=None, normalizedImageSize=None, normalizedImage=None):
        XSDataInput.__init__(self, configuration)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'normalizedImage' is not XSDataImage but %s" % self._normalizedImage.__class__.__name__
            raise BaseException(strMessage)
        if normalizedImageSize is None:
            self._normalizedImageSize = None
        elif normalizedImageSize.__class__.__name__ == "XSDataInteger":
            self._normalizedImageSize = normalizedImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'normalizedImageSize' is not XSDataInteger but %s" % self._normalizedImageSize.__class__.__name__
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'integratedImage' is not XSDataImage but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'correctedImage' is not XSDataImage but %s" % self._correctedImage.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setNormalizedImage argument is not XSDataImage but %s" % normalizedImage.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImage(self): self._normalizedImage = None
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    # Methods and properties for the 'normalizedImageSize' attribute
    def getNormalizedImageSize(self): return self._normalizedImageSize
    def setNormalizedImageSize(self, normalizedImageSize):
        if normalizedImageSize is None:
            self._normalizedImageSize = None
        elif normalizedImageSize.__class__.__name__ == "XSDataInteger":
            self._normalizedImageSize = normalizedImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setNormalizedImageSize argument is not XSDataInteger but %s" % normalizedImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImageSize(self): self._normalizedImageSize = None
    normalizedImageSize = property(getNormalizedImageSize, setNormalizedImageSize, delNormalizedImageSize, "Property for normalizedImageSize")
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setIntegratedImage argument is not XSDataImage but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'correctedImage' attribute
    def getCorrectedImage(self): return self._correctedImage
    def setCorrectedImage(self, correctedImage):
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setCorrectedImage argument is not XSDataImage but %s" % correctedImage.__class__.__name__
            raise BaseException(strMessage)
    def delCorrectedImage(self): self._correctedImage = None
    correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def export(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_='normalizedImage')
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._normalizedImageSize is not None:
            self.normalizedImageSize.export(outfile, level, name_='normalizedImageSize')
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_='integratedImage')
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._correctedImage is not None:
            self.correctedImage.export(outfile, level, name_='correctedImage')
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNormalizedImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correctedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setCorrectedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsAzimutIntv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAzimutIntv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsAzimutIntv1_0


class XSDataInputBioSaxsNormalizev1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, rawImageSize=None, normalizedImage=None, logFile=None, rawImage=None):
        XSDataInput.__init__(self, configuration)
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'rawImage' is not XSDataImage but %s" % self._rawImage.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s" % self._normalizedImage.__class__.__name__
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s" % self._rawImageSize.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'rawImage' attribute
    def getRawImage(self): return self._rawImage
    def setRawImage(self, rawImage):
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setRawImage argument is not XSDataImage but %s" % rawImage.__class__.__name__
            raise BaseException(strMessage)
    def delRawImage(self): self._rawImage = None
    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setNormalizedImage argument is not XSDataImage but %s" % normalizedImage.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImage(self): self._normalizedImage = None
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setRawImageSize argument is not XSDataInteger but %s" % rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delRawImageSize(self): self._rawImageSize = None
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsNormalizev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def export(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rawImage is not None:
            self.rawImage.export(outfile, level, name_='rawImage')
        else:
            warnEmptyAttribute("rawImage", "XSDataImage")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_='normalizedImage')
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_='rawImageSize')
        else:
            warnEmptyAttribute("rawImageSize", "XSDataInteger")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setRawImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsNormalizev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsNormalizev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsNormalizev1_0


class XSDataInputBioSaxsProcessOneFilev1_0(XSDataInput):
    """Plugin that runs subsequently Normalize and Azimuthal integration"""
    def __init__(self, configuration=None, frameId=None, runId=None, integratedCurve=None, integratedImage=None, normalizedImage=None, logFile=None, rawImageSize=None, experimentSetup=None, sample=None, rawImage=None):
        XSDataInput.__init__(self, configuration)
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'rawImage' is not XSDataImage but %s" % self._rawImage.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s" % self._rawImageSize.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s" % self._normalizedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'integratedImage' is not XSDataImage but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'runId' is not XSDataString but %s" % self._runId.__class__.__name__
            raise BaseException(strMessage)
        if frameId is None:
            self._frameId = None
        elif frameId.__class__.__name__ == "XSDataInteger":
            self._frameId = frameId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'frameId' is not XSDataInteger but %s" % self._frameId.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'rawImage' attribute
    def getRawImage(self): return self._rawImage
    def setRawImage(self, rawImage):
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRawImage argument is not XSDataImage but %s" % rawImage.__class__.__name__
            raise BaseException(strMessage)
    def delRawImage(self): self._rawImage = None
    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRawImageSize argument is not XSDataInteger but %s" % rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delRawImageSize(self): self._rawImageSize = None
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setNormalizedImage argument is not XSDataImage but %s" % normalizedImage.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImage(self): self._normalizedImage = None
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setIntegratedImage argument is not XSDataImage but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'runId' attribute
    def getRunId(self): return self._runId
    def setRunId(self, runId):
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRunId argument is not XSDataString but %s" % runId.__class__.__name__
            raise BaseException(strMessage)
    def delRunId(self): self._runId = None
    runId = property(getRunId, setRunId, delRunId, "Property for runId")
    # Methods and properties for the 'frameId' attribute
    def getFrameId(self): return self._frameId
    def setFrameId(self, frameId):
        if frameId is None:
            self._frameId = None
        elif frameId.__class__.__name__ == "XSDataInteger":
            self._frameId = frameId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setFrameId argument is not XSDataInteger but %s" % frameId.__class__.__name__
            raise BaseException(strMessage)
    def delFrameId(self): self._frameId = None
    frameId = property(getFrameId, setFrameId, delFrameId, "Property for frameId")
    def export(self, outfile, level, name_='XSDataInputBioSaxsProcessOneFilev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsProcessOneFilev1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rawImage is not None:
            self.rawImage.export(outfile, level, name_='rawImage')
        else:
            warnEmptyAttribute("rawImage", "XSDataImage")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_='rawImageSize')
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_='normalizedImage')
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_='integratedImage')
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        if self._runId is not None:
            self.runId.export(outfile, level, name_='runId')
        if self._frameId is not None:
            self.frameId.export(outfile, level, name_='frameId')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setRawImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'runId':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRunId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameId(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsProcessOneFilev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsProcessOneFilev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsProcessOneFilev1_0


class XSDataInputBioSaxsReduceFileSeriev1_0(XSDataInput):
    """Run ProcessOneFile on each file of a time time serie  """
    def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
        XSDataInput.__init__(self, configuration)
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'fileSerie' is not XSDataFileSeries but %s" % self._fileSerie.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directory1D' is not XSDataFile but %s" % self._directory1D.__class__.__name__
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directory2D' is not XSDataFile but %s" % self._directory2D.__class__.__name__
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s" % self._directoryMisc.__class__.__name__
            raise BaseException(strMessage)
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'forceReprocess' is not XSDataBoolean but %s" % self._forceReprocess.__class__.__name__
            raise BaseException(strMessage)
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'absoluteFidelity' is not XSDataDouble but %s" % self._absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'relativeFidelity' is not XSDataDouble but %s" % self._relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s" % self._rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fileSerie' attribute
    def getFileSerie(self): return self._fileSerie
    def setFileSerie(self, fileSerie):
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setFileSerie argument is not XSDataFileSeries but %s" % fileSerie.__class__.__name__
            raise BaseException(strMessage)
    def delFileSerie(self): self._fileSerie = None
    fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectory1D argument is not XSDataFile but %s" % directory1D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory1D(self): self._directory1D = None
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectory2D argument is not XSDataFile but %s" % directory2D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory2D(self): self._directory2D = None
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectoryMisc argument is not XSDataFile but %s" % directoryMisc.__class__.__name__
            raise BaseException(strMessage)
    def delDirectoryMisc(self): self._directoryMisc = None
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    # Methods and properties for the 'forceReprocess' attribute
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setForceReprocess argument is not XSDataBoolean but %s" % forceReprocess.__class__.__name__
            raise BaseException(strMessage)
    def delForceReprocess(self): self._forceReprocess = None
    forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
    # Methods and properties for the 'absoluteFidelity' attribute
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setAbsoluteFidelity argument is not XSDataDouble but %s" % absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    # Methods and properties for the 'relativeFidelity' attribute
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setRelativeFidelity argument is not XSDataDouble but %s" % relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delRelativeFidelity(self): self._relativeFidelity = None
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setRawImageSize argument is not XSDataInteger but %s" % rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delRawImageSize(self): self._rawImageSize = None
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    def export(self, outfile, level, name_='XSDataInputBioSaxsReduceFileSeriev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsReduceFileSeriev1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._fileSerie is not None:
            self.fileSerie.export(outfile, level, name_='fileSerie')
        else:
            warnEmptyAttribute("fileSerie", "XSDataFileSeries")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_='directory1D')
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_='directory2D')
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_='directoryMisc')
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
        if self._forceReprocess is not None:
            self.forceReprocess.export(outfile, level, name_='forceReprocess')
        if self._absoluteFidelity is not None:
            self.absoluteFidelity.export(outfile, level, name_='absoluteFidelity')
        if self._relativeFidelity is not None:
            self.relativeFidelity.export(outfile, level, name_='relativeFidelity')
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_='rawImageSize')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileSerie':
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.setFileSerie(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory1D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory2D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directoryMisc':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forceReprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setForceReprocess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'absoluteFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAbsoluteFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'relativeFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRelativeFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsReduceFileSeriev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsReduceFileSeriev1_0


class XSDataInputBioSaxsSample(XSDataInput):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None):
        XSDataInput.__init__(self, configuration)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s" % self._concentration.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample constructor argument 'code' is not XSDataString but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'concentration' attribute
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample.setConcentration argument is not XSDataDouble but %s" % concentration.__class__.__name__
            raise BaseException(strMessage)
    def delConcentration(self): self._concentration = None
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSample.setCode argument is not XSDataString but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='XSDataInputBioSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSample'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsSample')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSample")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsSample


class XSDataInputBioSaxsSmartMergev1_0(XSDataInput):
    def __init__(self, configuration=None, bufferCurves=None, runId=None, subtractedCurve=None, mergedCurve=None, sample=None, relativeFidelity=None, absoluteFidelity=None, inputCurves=None):
        XSDataInput.__init__(self, configuration)
        if inputCurves is None:
            self._inputCurves = []
        elif inputCurves.__class__.__name__ == "list":
            self._inputCurves = inputCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'inputCurves' is not list but %s" % self._inputCurves.__class__.__name__
            raise BaseException(strMessage)
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'absoluteFidelity' is not XSDataDouble but %s" % self._absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'relativeFidelity' is not XSDataDouble but %s" % self._relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s" % self._mergedCurve.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'runId' is not XSDataString but %s" % self._runId.__class__.__name__
            raise BaseException(strMessage)
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'bufferCurves' is not list but %s" % self._bufferCurves.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputCurves' attribute
    def getInputCurves(self): return self._inputCurves
    def setInputCurves(self, inputCurves):
        if inputCurves is None:
            self._inputCurves = []
        elif inputCurves.__class__.__name__ == "list":
            self._inputCurves = inputCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setInputCurves argument is not list but %s" % inputCurves.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurves(self): self._inputCurves = None
    inputCurves = property(getInputCurves, setInputCurves, delInputCurves, "Property for inputCurves")
    def addInputCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurves.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertInputCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertInputCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertInputCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurves[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'absoluteFidelity' attribute
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setAbsoluteFidelity argument is not XSDataDouble but %s" % absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    # Methods and properties for the 'relativeFidelity' attribute
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setRelativeFidelity argument is not XSDataDouble but %s" % relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delRelativeFidelity(self): self._relativeFidelity = None
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setMergedCurve argument is not XSDataFile but %s" % mergedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delMergedCurve(self): self._mergedCurve = None
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'runId' attribute
    def getRunId(self): return self._runId
    def setRunId(self, runId):
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setRunId argument is not XSDataString but %s" % runId.__class__.__name__
            raise BaseException(strMessage)
    def delRunId(self): self._runId = None
    runId = property(getRunId, setRunId, delRunId, "Property for runId")
    # Methods and properties for the 'bufferCurves' attribute
    def getBufferCurves(self): return self._bufferCurves
    def setBufferCurves(self, bufferCurves):
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.setBufferCurves argument is not list but %s" % bufferCurves.__class__.__name__
            raise BaseException(strMessage)
    def delBufferCurves(self): self._bufferCurves = None
    bufferCurves = property(getBufferCurves, setBufferCurves, delBufferCurves, "Property for bufferCurves")
    def addBufferCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBufferCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertBufferCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertBufferCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurves_ in self.getInputCurves():
            inputCurves_.export(outfile, level, name_='inputCurves')
        if self.getInputCurves() == []:
            warnEmptyAttribute("inputCurves", "XSDataFile")
        if self._absoluteFidelity is not None:
            self.absoluteFidelity.export(outfile, level, name_='absoluteFidelity')
        if self._relativeFidelity is not None:
            self.relativeFidelity.export(outfile, level, name_='relativeFidelity')
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_='mergedCurve')
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        if self._runId is not None:
            self.runId.export(outfile, level, name_='runId')
        for bufferCurves_ in self.getBufferCurves():
            bufferCurves_.export(outfile, level, name_='bufferCurves')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurves':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'absoluteFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAbsoluteFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'relativeFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRelativeFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mergedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'runId':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRunId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bufferCurves':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.bufferCurves.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsSmartMergev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSmartMergev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsSmartMergev1_0


class XSDataInputBioSaxsSubtractv1_0(XSDataInput):
    """Runs sequentially subtraction of buffer and SaxsAnalysis"""
    def __init__(self, configuration=None, gnomFile=None, subtractedCurve=None, sample=None, bufferCurves=None, sampleCurve=None):
        XSDataInput.__init__(self, configuration)
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'sampleCurve' is not XSDataFile but %s" % self._sampleCurve.__class__.__name__
            raise BaseException(strMessage)
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'bufferCurves' is not list but %s" % self._bufferCurves.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sampleCurve' attribute
    def getSampleCurve(self): return self._sampleCurve
    def setSampleCurve(self, sampleCurve):
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.setSampleCurve argument is not XSDataFile but %s" % sampleCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSampleCurve(self): self._sampleCurve = None
    sampleCurve = property(getSampleCurve, setSampleCurve, delSampleCurve, "Property for sampleCurve")
    # Methods and properties for the 'bufferCurves' attribute
    def getBufferCurves(self): return self._bufferCurves
    def setBufferCurves(self, bufferCurves):
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.setBufferCurves argument is not list but %s" % bufferCurves.__class__.__name__
            raise BaseException(strMessage)
    def delBufferCurves(self): self._bufferCurves = None
    bufferCurves = property(getBufferCurves, setBufferCurves, delBufferCurves, "Property for bufferCurves")
    def addBufferCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBufferCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.insertBufferCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.insertBufferCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    def export(self, outfile, level, name_='XSDataInputBioSaxsSubtractv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSubtractv1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sampleCurve is not None:
            self.sampleCurve.export(outfile, level, name_='sampleCurve')
        else:
            warnEmptyAttribute("sampleCurve", "XSDataFile")
        for bufferCurves_ in self.getBufferCurves():
            bufferCurves_.export(outfile, level, name_='bufferCurves')
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sampleCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSampleCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bufferCurves':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.bufferCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsSubtractv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSubtractv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsSubtractv1_0


class XSDataInputBioSaxsToSASv1_0(XSDataInput):
    """This is just a wrapper for the SAS downstream pipeline"""
    def __init__(self, configuration=None, destinationDirectory=None, qMax=None, lastPoint=None, firstPoint=None, subtractedCurve=None):
        XSDataInput.__init__(self, configuration)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if firstPoint is None:
            self._firstPoint = None
        elif firstPoint.__class__.__name__ == "XSDataInteger":
            self._firstPoint = firstPoint
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'firstPoint' is not XSDataInteger but %s" % self._firstPoint.__class__.__name__
            raise BaseException(strMessage)
        if lastPoint is None:
            self._lastPoint = None
        elif lastPoint.__class__.__name__ == "XSDataInteger":
            self._lastPoint = lastPoint
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'lastPoint' is not XSDataInteger but %s" % self._lastPoint.__class__.__name__
            raise BaseException(strMessage)
        if qMax is None:
            self._qMax = None
        elif qMax.__class__.__name__ == "XSDataDouble":
            self._qMax = qMax
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'qMax' is not XSDataDouble but %s" % self._qMax.__class__.__name__
            raise BaseException(strMessage)
        if destinationDirectory is None:
            self._destinationDirectory = None
        elif destinationDirectory.__class__.__name__ == "XSDataFile":
            self._destinationDirectory = destinationDirectory
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'destinationDirectory' is not XSDataFile but %s" % self._destinationDirectory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'firstPoint' attribute
    def getFirstPoint(self): return self._firstPoint
    def setFirstPoint(self, firstPoint):
        if firstPoint is None:
            self._firstPoint = None
        elif firstPoint.__class__.__name__ == "XSDataInteger":
            self._firstPoint = firstPoint
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0.setFirstPoint argument is not XSDataInteger but %s" % firstPoint.__class__.__name__
            raise BaseException(strMessage)
    def delFirstPoint(self): self._firstPoint = None
    firstPoint = property(getFirstPoint, setFirstPoint, delFirstPoint, "Property for firstPoint")
    # Methods and properties for the 'lastPoint' attribute
    def getLastPoint(self): return self._lastPoint
    def setLastPoint(self, lastPoint):
        if lastPoint is None:
            self._lastPoint = None
        elif lastPoint.__class__.__name__ == "XSDataInteger":
            self._lastPoint = lastPoint
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0.setLastPoint argument is not XSDataInteger but %s" % lastPoint.__class__.__name__
            raise BaseException(strMessage)
    def delLastPoint(self): self._lastPoint = None
    lastPoint = property(getLastPoint, setLastPoint, delLastPoint, "Property for lastPoint")
    # Methods and properties for the 'qMax' attribute
    def getQMax(self): return self._qMax
    def setQMax(self, qMax):
        if qMax is None:
            self._qMax = None
        elif qMax.__class__.__name__ == "XSDataDouble":
            self._qMax = qMax
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0.setQMax argument is not XSDataDouble but %s" % qMax.__class__.__name__
            raise BaseException(strMessage)
    def delQMax(self): self._qMax = None
    qMax = property(getQMax, setQMax, delQMax, "Property for qMax")
    # Methods and properties for the 'destinationDirectory' attribute
    def getDestinationDirectory(self): return self._destinationDirectory
    def setDestinationDirectory(self, destinationDirectory):
        if destinationDirectory is None:
            self._destinationDirectory = None
        elif destinationDirectory.__class__.__name__ == "XSDataFile":
            self._destinationDirectory = destinationDirectory
        else:
            strMessage = "ERROR! XSDataInputBioSaxsToSASv1_0.setDestinationDirectory argument is not XSDataFile but %s" % destinationDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delDestinationDirectory(self): self._destinationDirectory = None
    destinationDirectory = property(getDestinationDirectory, setDestinationDirectory, delDestinationDirectory, "Property for destinationDirectory")
    def export(self, outfile, level, name_='XSDataInputBioSaxsToSASv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsToSASv1_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        else:
            warnEmptyAttribute("subtractedCurve", "XSDataFile")
        if self._firstPoint is not None:
            self.firstPoint.export(outfile, level, name_='firstPoint')
        if self._lastPoint is not None:
            self.lastPoint.export(outfile, level, name_='lastPoint')
        if self._qMax is not None:
            self.qMax.export(outfile, level, name_='qMax')
        if self._destinationDirectory is not None:
            self.destinationDirectory.export(outfile, level, name_='destinationDirectory')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstPoint':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFirstPoint(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lastPoint':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLastPoint(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'qMax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setQMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'destinationDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDestinationDirectory(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsToSASv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsToSASv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsToSASv1_0


class XSDataResultBioSaxsAsciiExportv1_0(XSDataResult):
    def __init__(self, status=None, processLog=None, integratedCurve=None):
        XSDataResult.__init__(self, status)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAsciiExportv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAsciiExportv1_0 constructor argument 'processLog' is not XSDataString but %s" % self._processLog.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAsciiExportv1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAsciiExportv1_0.setProcessLog argument is not XSDataString but %s" % processLog.__class__.__name__
            raise BaseException(strMessage)
    def delProcessLog(self): self._processLog = None
    processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
    def export(self, outfile, level, name_='XSDataResultBioSaxsAsciiExportv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAsciiExportv1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_='processLog')
        else:
            warnEmptyAttribute("processLog", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processLog':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsAsciiExportv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAsciiExportv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsAsciiExportv1_0


class XSDataResultBioSaxsAveragev1_0(XSDataResult):
    def __init__(self, status=None, logFile=None, processLog=None, averagedCurve=None, averagedImage=None):
        XSDataResult.__init__(self, status)
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'averagedImage' is not XSDataImage but %s" % self._averagedImage.__class__.__name__
            raise BaseException(strMessage)
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'averagedCurve' is not XSDataFile but %s" % self._averagedCurve.__class__.__name__
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'processLog' is not XSDataString but %s" % self._processLog.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'averagedImage' attribute
    def getAveragedImage(self): return self._averagedImage
    def setAveragedImage(self, averagedImage):
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0.setAveragedImage argument is not XSDataImage but %s" % averagedImage.__class__.__name__
            raise BaseException(strMessage)
    def delAveragedImage(self): self._averagedImage = None
    averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
    # Methods and properties for the 'averagedCurve' attribute
    def getAveragedCurve(self): return self._averagedCurve
    def setAveragedCurve(self, averagedCurve):
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0.setAveragedCurve argument is not XSDataFile but %s" % averagedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delAveragedCurve(self): self._averagedCurve = None
    averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0.setProcessLog argument is not XSDataString but %s" % processLog.__class__.__name__
            raise BaseException(strMessage)
    def delProcessLog(self): self._processLog = None
    processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAveragev1_0.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def export(self, outfile, level, name_='XSDataResultBioSaxsAveragev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAveragev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._averagedImage is not None:
            self.averagedImage.export(outfile, level, name_='averagedImage')
        else:
            warnEmptyAttribute("averagedImage", "XSDataImage")
        if self._averagedCurve is not None:
            self.averagedCurve.export(outfile, level, name_='averagedCurve')
        else:
            warnEmptyAttribute("averagedCurve", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_='processLog')
        else:
            warnEmptyAttribute("processLog", "XSDataString")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averagedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setAveragedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averagedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAveragedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processLog':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsAveragev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAveragev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsAveragev1_0


class XSDataResultBioSaxsAzimutIntv1_0(XSDataResult):
    def __init__(self, status=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None, correctedImage=None):
        XSDataResult.__init__(self, status)
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'correctedImage' is not XSDataImage but %s" % self._correctedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'integratedImage' is not XSDataImage but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'correctedImage' attribute
    def getCorrectedImage(self): return self._correctedImage
    def setCorrectedImage(self, correctedImage):
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setCorrectedImage argument is not XSDataImage but %s" % correctedImage.__class__.__name__
            raise BaseException(strMessage)
    def delCorrectedImage(self): self._correctedImage = None
    correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setIntegratedImage argument is not XSDataImage but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def export(self, outfile, level, name_='XSDataResultBioSaxsAzimutIntv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAzimutIntv1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._correctedImage is not None:
            self.correctedImage.export(outfile, level, name_='correctedImage')
        else:
            warnEmptyAttribute("correctedImage", "XSDataImage")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_='integratedImage')
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correctedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setCorrectedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsAzimutIntv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAzimutIntv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsAzimutIntv1_0


class XSDataResultBioSaxsNormalizev1_0(XSDataResult):
    def __init__(self, status=None, processLog=None, logFile=None, normalizedImage=None):
        XSDataResult.__init__(self, status)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s" % self._normalizedImage.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'processLog' is not XSDataString but %s" % self._processLog.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0.setNormalizedImage argument is not XSDataImage but %s" % normalizedImage.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImage(self): self._normalizedImage = None
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = "ERROR! XSDataResultBioSaxsNormalizev1_0.setProcessLog argument is not XSDataString but %s" % processLog.__class__.__name__
            raise BaseException(strMessage)
    def delProcessLog(self): self._processLog = None
    processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
    def export(self, outfile, level, name_='XSDataResultBioSaxsNormalizev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsNormalizev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_='normalizedImage')
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_='processLog')
        else:
            warnEmptyAttribute("processLog", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processLog':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsNormalizev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsNormalizev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsNormalizev1_0


class XSDataResultBioSaxsProcessOneFilev1_0(XSDataResult):
    def __init__(self, status=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None, normalizedImage=None):
        XSDataResult.__init__(self, status)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s" % self._normalizedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'integratedImage' is not XSDataImage but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'integratedCurve' is not XSDataFile but %s" % self._integratedCurve.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setNormalizedImage argument is not XSDataImage but %s" % normalizedImage.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizedImage(self): self._normalizedImage = None
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setIntegratedImage argument is not XSDataImage but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setIntegratedCurve argument is not XSDataFile but %s" % integratedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedCurve(self): self._integratedCurve = None
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def export(self, outfile, level, name_='XSDataResultBioSaxsProcessOneFilev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsProcessOneFilev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_='normalizedImage')
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_='integratedImage')
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsProcessOneFilev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsProcessOneFilev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsProcessOneFilev1_0


class XSDataResultBioSaxsReduceFileSeriev1_0(XSDataResult):
    def __init__(self, status=None, directoryMisc=None, directory2D=None, directory1D=None, mergedCurve=None):
        XSDataResult.__init__(self, status)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s" % self._mergedCurve.__class__.__name__
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directory1D' is not XSDataFile but %s" % self._directory1D.__class__.__name__
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directory2D' is not XSDataFile but %s" % self._directory2D.__class__.__name__
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s" % self._directoryMisc.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setMergedCurve argument is not XSDataFile but %s" % mergedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delMergedCurve(self): self._mergedCurve = None
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectory1D argument is not XSDataFile but %s" % directory1D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory1D(self): self._directory1D = None
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectory2D argument is not XSDataFile but %s" % directory2D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory2D(self): self._directory2D = None
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectoryMisc argument is not XSDataFile but %s" % directoryMisc.__class__.__name__
            raise BaseException(strMessage)
    def delDirectoryMisc(self): self._directoryMisc = None
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    def export(self, outfile, level, name_='XSDataResultBioSaxsReduceFileSeriev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsReduceFileSeriev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_='mergedCurve')
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_='directory1D')
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_='directory2D')
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_='directoryMisc')
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mergedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory1D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory2D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directoryMisc':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsReduceFileSeriev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsReduceFileSeriev1_0


class XSDataResultBioSaxsSample(XSDataResult):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, status=None, code=None, comments=None, concentration=None):
        XSDataResult.__init__(self, status)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s" % self._concentration.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample constructor argument 'code' is not XSDataString but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'concentration' attribute
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample.setConcentration argument is not XSDataDouble but %s" % concentration.__class__.__name__
            raise BaseException(strMessage)
    def delConcentration(self): self._concentration = None
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSample.setCode argument is not XSDataString but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='XSDataResultBioSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSample'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsSample')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSample")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsSample


class XSDataResultBioSaxsSingleSamplev1_0(XSDataResult):
    """Class for precessing a single sample (at 1 single concentration)"""
    def __init__(self, status=None, directory2D=None, directory1D=None, outputCurve=None):
        XSDataResult.__init__(self, status)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'outputCurve' is not XSDataFile but %s" % self._outputCurve.__class__.__name__
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'directory1D' is not XSDataFile but %s" % self._directory1D.__class__.__name__
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'directory2D' is not XSDataFile but %s" % self._directory2D.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setOutputCurve argument is not XSDataFile but %s" % outputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCurve(self): self._outputCurve = None
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setDirectory1D argument is not XSDataFile but %s" % directory1D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory1D(self): self._directory1D = None
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setDirectory2D argument is not XSDataFile but %s" % directory2D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory2D(self): self._directory2D = None
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    def export(self, outfile, level, name_='XSDataResultBioSaxsSingleSamplev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSingleSamplev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_='directory1D')
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_='directory2D')
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory1D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory2D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsSingleSamplev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSingleSamplev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsSingleSamplev1_0


class XSDataResultBioSaxsSmartMergev1_0(XSDataResult):
    def __init__(self, status=None, subtractedCurve=None, volume=None, gnom=None, autoRg=None, mergedCurve=None):
        XSDataResult.__init__(self, status)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s" % self._mergedCurve.__class__.__name__
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0.setMergedCurve argument is not XSDataFile but %s" % mergedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delMergedCurve(self): self._mergedCurve = None
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSmartMergev1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def export(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_='mergedCurve')
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mergedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsSmartMergev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSmartMergev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsSmartMergev1_0


class XSDataResultBioSaxsSubtractv1_0(XSDataResult):
    def __init__(self, status=None, volume=None, gnom=None, autorg=None, subtractedCurve=None):
        XSDataResult.__init__(self, status)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if autorg is None:
            self._autorg = None
        elif autorg.__class__.__name__ == "XSDataAutoRg":
            self._autorg = autorg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'autorg' is not XSDataAutoRg but %s" % self._autorg.__class__.__name__
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'autorg' attribute
    def getAutorg(self): return self._autorg
    def setAutorg(self, autorg):
        if autorg is None:
            self._autorg = None
        elif autorg.__class__.__name__ == "XSDataAutoRg":
            self._autorg = autorg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0.setAutorg argument is not XSDataAutoRg but %s" % autorg.__class__.__name__
            raise BaseException(strMessage)
    def delAutorg(self): self._autorg = None
    autorg = property(getAutorg, setAutorg, delAutorg, "Property for autorg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSubtractv1_0.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def export(self, outfile, level, name_='XSDataResultBioSaxsSubtractv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSubtractv1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        else:
            warnEmptyAttribute("subtractedCurve", "XSDataFile")
        if self._autorg is not None:
            self.autorg.export(outfile, level, name_='autorg')
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autorg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutorg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsSubtractv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSubtractv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsSubtractv1_0


class XSDataResultBioSaxsToSASv1_0(XSDataResult):
    def __init__(self, status=None, htmlPage=None):
        XSDataResult.__init__(self, status)
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsToSASv1_0 constructor argument 'htmlPage' is not XSDataFile but %s" % self._htmlPage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'htmlPage' attribute
    def getHtmlPage(self): return self._htmlPage
    def setHtmlPage(self, htmlPage):
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsToSASv1_0.setHtmlPage argument is not XSDataFile but %s" % htmlPage.__class__.__name__
            raise BaseException(strMessage)
    def delHtmlPage(self): self._htmlPage = None
    htmlPage = property(getHtmlPage, setHtmlPage, delHtmlPage, "Property for htmlPage")
    def export(self, outfile, level, name_='XSDataResultBioSaxsToSASv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsToSASv1_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._htmlPage is not None:
            self.htmlPage.export(outfile, level, name_='htmlPage')
        else:
            warnEmptyAttribute("htmlPage", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'htmlPage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHtmlPage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsToSASv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsToSASv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsToSASv1_0


class XSDataInputBioSaxsHPLCv1_0(XSDataInputBioSaxsProcessOneFilev1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""
    def __init__(self, configuration=None, frameId=None, runId=None, integratedCurve=None, integratedImage=None, normalizedImage=None, logFile=None, rawImageSize=None, experimentSetup=None, sample=None, rawImage=None, hplcFile=None, gnomFile=None, subtractedCurve=None, bufferCurve=None):
        XSDataInputBioSaxsProcessOneFilev1_0.__init__(self, configuration, frameId, runId, integratedCurve, integratedImage, normalizedImage, logFile, rawImageSize, experimentSetup, sample, rawImage)
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'bufferCurve' is not XSDataFile but %s" % self._bufferCurve.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'hplcFile' is not XSDataFile but %s" % self._hplcFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bufferCurve' attribute
    def getBufferCurve(self): return self._bufferCurve
    def setBufferCurve(self, bufferCurve):
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0.setBufferCurve argument is not XSDataFile but %s" % bufferCurve.__class__.__name__
            raise BaseException(strMessage)
    def delBufferCurve(self): self._bufferCurve = None
    bufferCurve = property(getBufferCurve, setBufferCurve, delBufferCurve, "Property for bufferCurve")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'hplcFile' attribute
    def getHplcFile(self): return self._hplcFile
    def setHplcFile(self, hplcFile):
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsHPLCv1_0.setHplcFile argument is not XSDataFile but %s" % hplcFile.__class__.__name__
            raise BaseException(strMessage)
    def delHplcFile(self): self._hplcFile = None
    hplcFile = property(getHplcFile, setHplcFile, delHplcFile, "Property for hplcFile")
    def export(self, outfile, level, name_='XSDataInputBioSaxsHPLCv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsHPLCv1_0'):
        XSDataInputBioSaxsProcessOneFilev1_0.exportChildren(self, outfile, level, name_)
        if self._bufferCurve is not None:
            self.bufferCurve.export(outfile, level, name_='bufferCurve')
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        if self._hplcFile is not None:
            self.hplcFile.export(outfile, level, name_='hplcFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bufferCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBufferCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hplcFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcFile(obj_)
        XSDataInputBioSaxsProcessOneFilev1_0.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsHPLCv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsHPLCv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsHPLCv1_0


class XSDataInputBioSaxsSampleExperiment(XSDataInputBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSDataInputBioSaxsSample.__init__(self, configuration, code, comments, concentration)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'detector' is not XSDataString but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'detectorDistance' is not XSDataLength but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'pixelSize_1' is not XSDataLength but %s" % self._pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'pixelSize_2' is not XSDataLength but %s" % self._pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamCenter_1' is not XSDataDouble but %s" % self._beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamCenter_2' is not XSDataDouble but %s" % self._beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamStopDiode' is not XSDataDouble but %s" % self._beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'machineCurrent' is not XSDataDouble but %s" % self._machineCurrent.__class__.__name__
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'maskFile' is not XSDataImage but %s" % self._maskFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'normalizationFactor' is not XSDataDouble but %s" % self._normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'storageTemperature' is not XSDataDouble but %s" % self._storageTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'exposureTemperature' is not XSDataDouble but %s" % self._exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'exposureTime' is not XSDataTime but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'frameNumber' is not XSDataInteger but %s" % self._frameNumber.__class__.__name__
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'frameMax' is not XSDataInteger but %s" % self._frameMax.__class__.__name__
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'timeOfFrame' is not XSDataTime but %s" % self._timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setDetector argument is not XSDataString but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setDetectorDistance argument is not XSDataLength but %s" % detectorDistance.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setPixelSize_1 argument is not XSDataLength but %s" % pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_1(self): self._pixelSize_1 = None
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setPixelSize_2 argument is not XSDataLength but %s" % pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_2(self): self._pixelSize_2 = None
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamCenter_1 argument is not XSDataDouble but %s" % beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_1(self): self._beamCenter_1 = None
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamCenter_2 argument is not XSDataDouble but %s" % beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_2(self): self._beamCenter_2 = None
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamStopDiode argument is not XSDataDouble but %s" % beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
    def delBeamStopDiode(self): self._beamStopDiode = None
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setMachineCurrent argument is not XSDataDouble but %s" % machineCurrent.__class__.__name__
            raise BaseException(strMessage)
    def delMachineCurrent(self): self._machineCurrent = None
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setMaskFile argument is not XSDataImage but %s" % maskFile.__class__.__name__
            raise BaseException(strMessage)
    def delMaskFile(self): self._maskFile = None
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setNormalizationFactor argument is not XSDataDouble but %s" % normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizationFactor(self): self._normalizationFactor = None
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setStorageTemperature argument is not XSDataDouble but %s" % storageTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delStorageTemperature(self): self._storageTemperature = None
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setExposureTemperature argument is not XSDataDouble but %s" % exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTemperature(self): self._exposureTemperature = None
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setExposureTime argument is not XSDataTime but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setFrameNumber argument is not XSDataInteger but %s" % frameNumber.__class__.__name__
            raise BaseException(strMessage)
    def delFrameNumber(self): self._frameNumber = None
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setFrameMax argument is not XSDataInteger but %s" % frameMax.__class__.__name__
            raise BaseException(strMessage)
    def delFrameMax(self): self._frameMax = None
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self): return self._timeOfFrame
    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSampleExperiment.setTimeOfFrame argument is not XSDataTime but %s" % timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    def delTimeOfFrame(self): self._timeOfFrame = None
    timeOfFrame = property(getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame")
    def export(self, outfile, level, name_='XSDataInputBioSaxsSampleExperiment'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSampleExperiment'):
        XSDataInputBioSaxsSample.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_='detectorDistance')
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_='machineCurrent')
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_='maskFile')
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_='storageTemperature')
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_='frameNumber')
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_='frameMax')
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_='timeOfFrame')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_1':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_2':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamStopDiode':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineCurrent':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maskFile':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizationFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'storageTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameMax':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeOfFrame':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSDataInputBioSaxsSample.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsSampleExperiment')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSampleExperiment.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsSampleExperiment


class XSDataResultBioSaxsHPLCv1_0(XSDataResultBioSaxsProcessOneFilev1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""
    def __init__(self, status=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None, normalizedImage=None, hplcImage=None, mergedCurves=None, hplcFile=None, volume=None, gnom=None, autoRg=None, subtractedCurve=None, bufferCurve=None):
        XSDataResultBioSaxsProcessOneFilev1_0.__init__(self, status, experimentSetup, sample, integratedCurve, integratedImage, normalizedImage)
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'bufferCurve' is not XSDataFile but %s" % self._bufferCurve.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'hplcFile' is not XSDataFile but %s" % self._hplcFile.__class__.__name__
            raise BaseException(strMessage)
        if mergedCurves is None:
            self._mergedCurves = []
        elif mergedCurves.__class__.__name__ == "list":
            self._mergedCurves = mergedCurves
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'mergedCurves' is not list but %s" % self._mergedCurves.__class__.__name__
            raise BaseException(strMessage)
        if hplcImage is None:
            self._hplcImage = None
        elif hplcImage.__class__.__name__ == "XSDataFile":
            self._hplcImage = hplcImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'hplcImage' is not XSDataFile but %s" % self._hplcImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bufferCurve' attribute
    def getBufferCurve(self): return self._bufferCurve
    def setBufferCurve(self, bufferCurve):
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setBufferCurve argument is not XSDataFile but %s" % bufferCurve.__class__.__name__
            raise BaseException(strMessage)
    def delBufferCurve(self): self._bufferCurve = None
    bufferCurve = property(getBufferCurve, setBufferCurve, delBufferCurve, "Property for bufferCurve")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'hplcFile' attribute
    def getHplcFile(self): return self._hplcFile
    def setHplcFile(self, hplcFile):
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setHplcFile argument is not XSDataFile but %s" % hplcFile.__class__.__name__
            raise BaseException(strMessage)
    def delHplcFile(self): self._hplcFile = None
    hplcFile = property(getHplcFile, setHplcFile, delHplcFile, "Property for hplcFile")
    # Methods and properties for the 'mergedCurves' attribute
    def getMergedCurves(self): return self._mergedCurves
    def setMergedCurves(self, mergedCurves):
        if mergedCurves is None:
            self._mergedCurves = []
        elif mergedCurves.__class__.__name__ == "list":
            self._mergedCurves = mergedCurves
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setMergedCurves argument is not list but %s" % mergedCurves.__class__.__name__
            raise BaseException(strMessage)
    def delMergedCurves(self): self._mergedCurves = None
    mergedCurves = property(getMergedCurves, setMergedCurves, delMergedCurves, "Property for mergedCurves")
    def addMergedCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._mergedCurves.append(value)
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertMergedCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.insertMergedCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.insertMergedCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._mergedCurves[index] = value
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hplcImage' attribute
    def getHplcImage(self): return self._hplcImage
    def setHplcImage(self, hplcImage):
        if hplcImage is None:
            self._hplcImage = None
        elif hplcImage.__class__.__name__ == "XSDataFile":
            self._hplcImage = hplcImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.setHplcImage argument is not XSDataFile but %s" % hplcImage.__class__.__name__
            raise BaseException(strMessage)
    def delHplcImage(self): self._hplcImage = None
    hplcImage = property(getHplcImage, setHplcImage, delHplcImage, "Property for hplcImage")
    def export(self, outfile, level, name_='XSDataResultBioSaxsHPLCv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsHPLCv1_0'):
        XSDataResultBioSaxsProcessOneFilev1_0.exportChildren(self, outfile, level, name_)
        if self._bufferCurve is not None:
            self.bufferCurve.export(outfile, level, name_='bufferCurve')
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        if self._hplcFile is not None:
            self.hplcFile.export(outfile, level, name_='hplcFile')
        for mergedCurves_ in self.getMergedCurves():
            mergedCurves_.export(outfile, level, name_='mergedCurves')
        if self._hplcImage is not None:
            self.hplcImage.export(outfile, level, name_='hplcImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bufferCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBufferCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hplcFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mergedCurves':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.mergedCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hplcImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcImage(obj_)
        XSDataResultBioSaxsProcessOneFilev1_0.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsHPLCv1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsHPLCv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsHPLCv1_0


class XSDataResultBioSaxsSampleExperiment(XSDataResultBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, status=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSDataResultBioSaxsSample.__init__(self, status, code, comments, concentration)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'detector' is not XSDataString but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'detectorDistance' is not XSDataLength but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'pixelSize_1' is not XSDataLength but %s" % self._pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'pixelSize_2' is not XSDataLength but %s" % self._pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamCenter_1' is not XSDataDouble but %s" % self._beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamCenter_2' is not XSDataDouble but %s" % self._beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamStopDiode' is not XSDataDouble but %s" % self._beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'machineCurrent' is not XSDataDouble but %s" % self._machineCurrent.__class__.__name__
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'maskFile' is not XSDataImage but %s" % self._maskFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'normalizationFactor' is not XSDataDouble but %s" % self._normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'storageTemperature' is not XSDataDouble but %s" % self._storageTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'exposureTemperature' is not XSDataDouble but %s" % self._exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'exposureTime' is not XSDataTime but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'frameNumber' is not XSDataInteger but %s" % self._frameNumber.__class__.__name__
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'frameMax' is not XSDataInteger but %s" % self._frameMax.__class__.__name__
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'timeOfFrame' is not XSDataTime but %s" % self._timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setDetector argument is not XSDataString but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setDetectorDistance argument is not XSDataLength but %s" % detectorDistance.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setPixelSize_1 argument is not XSDataLength but %s" % pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_1(self): self._pixelSize_1 = None
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setPixelSize_2 argument is not XSDataLength but %s" % pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_2(self): self._pixelSize_2 = None
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamCenter_1 argument is not XSDataDouble but %s" % beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_1(self): self._beamCenter_1 = None
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamCenter_2 argument is not XSDataDouble but %s" % beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_2(self): self._beamCenter_2 = None
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamStopDiode argument is not XSDataDouble but %s" % beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
    def delBeamStopDiode(self): self._beamStopDiode = None
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setMachineCurrent argument is not XSDataDouble but %s" % machineCurrent.__class__.__name__
            raise BaseException(strMessage)
    def delMachineCurrent(self): self._machineCurrent = None
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setMaskFile argument is not XSDataImage but %s" % maskFile.__class__.__name__
            raise BaseException(strMessage)
    def delMaskFile(self): self._maskFile = None
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setNormalizationFactor argument is not XSDataDouble but %s" % normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizationFactor(self): self._normalizationFactor = None
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setStorageTemperature argument is not XSDataDouble but %s" % storageTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delStorageTemperature(self): self._storageTemperature = None
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setExposureTemperature argument is not XSDataDouble but %s" % exposureTemperature.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTemperature(self): self._exposureTemperature = None
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setExposureTime argument is not XSDataTime but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setFrameNumber argument is not XSDataInteger but %s" % frameNumber.__class__.__name__
            raise BaseException(strMessage)
    def delFrameNumber(self): self._frameNumber = None
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setFrameMax argument is not XSDataInteger but %s" % frameMax.__class__.__name__
            raise BaseException(strMessage)
    def delFrameMax(self): self._frameMax = None
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self): return self._timeOfFrame
    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = "ERROR! XSDataResultBioSaxsSampleExperiment.setTimeOfFrame argument is not XSDataTime but %s" % timeOfFrame.__class__.__name__
            raise BaseException(strMessage)
    def delTimeOfFrame(self): self._timeOfFrame = None
    timeOfFrame = property(getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame")
    def export(self, outfile, level, name_='XSDataResultBioSaxsSampleExperiment'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSampleExperiment'):
        XSDataResultBioSaxsSample.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_='detectorDistance')
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_='machineCurrent')
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_='maskFile')
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_='storageTemperature')
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_='frameNumber')
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_='frameMax')
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_='timeOfFrame')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_1':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_2':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamStopDiode':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineCurrent':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maskFile':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizationFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'storageTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTemperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'frameMax':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeOfFrame':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSDataResultBioSaxsSample.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsSampleExperiment')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSampleExperiment.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsSampleExperiment


class XSDataInputBioSaxsAveragev1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, logFile=None, averagedCurve=None, averagedImage=None, integratedImageSize=None, integratedImage=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, timeOfFrame, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
        if integratedImage is None:
            self._integratedImage = []
        elif integratedImage.__class__.__name__ == "list":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'integratedImage' is not list but %s" % self._integratedImage.__class__.__name__
            raise BaseException(strMessage)
        if integratedImageSize is None:
            self._integratedImageSize = None
        elif integratedImageSize.__class__.__name__ == "XSDataInteger":
            self._integratedImageSize = integratedImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'integratedImageSize' is not XSDataInteger but %s" % self._integratedImageSize.__class__.__name__
            raise BaseException(strMessage)
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'averagedImage' is not XSDataImage but %s" % self._averagedImage.__class__.__name__
            raise BaseException(strMessage)
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'averagedCurve' is not XSDataFile but %s" % self._averagedCurve.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = []
        elif integratedImage.__class__.__name__ == "list":
            self._integratedImage = integratedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.setIntegratedImage argument is not list but %s" % integratedImage.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImage(self): self._integratedImage = None
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def addIntegratedImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataImage":
            self._integratedImage.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is not XSDataImage but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertIntegratedImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.insertIntegratedImage argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.insertIntegratedImage argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataImage":
            self._integratedImage[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is not XSDataImage but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'integratedImageSize' attribute
    def getIntegratedImageSize(self): return self._integratedImageSize
    def setIntegratedImageSize(self, integratedImageSize):
        if integratedImageSize is None:
            self._integratedImageSize = None
        elif integratedImageSize.__class__.__name__ == "XSDataInteger":
            self._integratedImageSize = integratedImageSize
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.setIntegratedImageSize argument is not XSDataInteger but %s" % integratedImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delIntegratedImageSize(self): self._integratedImageSize = None
    integratedImageSize = property(getIntegratedImageSize, setIntegratedImageSize, delIntegratedImageSize, "Property for integratedImageSize")
    # Methods and properties for the 'averagedImage' attribute
    def getAveragedImage(self): return self._averagedImage
    def setAveragedImage(self, averagedImage):
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.setAveragedImage argument is not XSDataImage but %s" % averagedImage.__class__.__name__
            raise BaseException(strMessage)
    def delAveragedImage(self): self._averagedImage = None
    averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
    # Methods and properties for the 'averagedCurve' attribute
    def getAveragedCurve(self): return self._averagedCurve
    def setAveragedCurve(self, averagedCurve):
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.setAveragedCurve argument is not XSDataFile but %s" % averagedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delAveragedCurve(self): self._averagedCurve = None
    averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def export(self, outfile, level, name_='XSDataInputBioSaxsAveragev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAveragev1_0'):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        for integratedImage_ in self.getIntegratedImage():
            integratedImage_.export(outfile, level, name_='integratedImage')
        if self.getIntegratedImage() == []:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedImageSize is not None:
            self.integratedImageSize.export(outfile, level, name_='integratedImageSize')
        else:
            warnEmptyAttribute("integratedImageSize", "XSDataInteger")
        if self._averagedImage is not None:
            self.averagedImage.export(outfile, level, name_='averagedImage')
        else:
            warnEmptyAttribute("averagedImage", "XSDataImage")
        if self._averagedCurve is not None:
            self.averagedCurve.export(outfile, level, name_='averagedCurve')
        else:
            warnEmptyAttribute("averagedCurve", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.integratedImage.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integratedImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIntegratedImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averagedImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setAveragedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averagedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAveragedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsAveragev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAveragev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsAveragev1_0


class XSDataInputBioSaxsMetadatav1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, inputImage=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, timeOfFrame, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
        if inputImage is None:
            self._inputImage = None
        elif inputImage.__class__.__name__ == "XSDataImage":
            self._inputImage = inputImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsMetadatav1_0 constructor argument 'inputImage' is not XSDataImage but %s" % self._inputImage.__class__.__name__
            raise BaseException(strMessage)
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsMetadatav1_0 constructor argument 'outputImage' is not XSDataImage but %s" % self._outputImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputImage' attribute
    def getInputImage(self): return self._inputImage
    def setInputImage(self, inputImage):
        if inputImage is None:
            self._inputImage = None
        elif inputImage.__class__.__name__ == "XSDataImage":
            self._inputImage = inputImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsMetadatav1_0.setInputImage argument is not XSDataImage but %s" % inputImage.__class__.__name__
            raise BaseException(strMessage)
    def delInputImage(self): self._inputImage = None
    inputImage = property(getInputImage, setInputImage, delInputImage, "Property for inputImage")
    # Methods and properties for the 'outputImage' attribute
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = "ERROR! XSDataInputBioSaxsMetadatav1_0.setOutputImage argument is not XSDataImage but %s" % outputImage.__class__.__name__
            raise BaseException(strMessage)
    def delOutputImage(self): self._outputImage = None
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def export(self, outfile, level, name_='XSDataInputBioSaxsMetadatav1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsMetadatav1_0'):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._inputImage is not None:
            self.inputImage.export(outfile, level, name_='inputImage')
        else:
            warnEmptyAttribute("inputImage", "XSDataImage")
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setInputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsMetadatav1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsMetadatav1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsMetadatav1_0


class XSDataInputBioSaxsSingleSamplev1_0(XSDataInputBioSaxsSampleExperiment):
    """Class for precessing a single sample (at 1 single concentration)"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, forceReprocess=None, sampleSeries=None, bufferSeries=None, directoryMisc=None, directory2D=None, directory1D=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, timeOfFrame, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directory1D' is not XSDataFile but %s" % self._directory1D.__class__.__name__
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directory2D' is not XSDataFile but %s" % self._directory2D.__class__.__name__
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s" % self._directoryMisc.__class__.__name__
            raise BaseException(strMessage)
        if bufferSeries is None:
            self._bufferSeries = []
        elif bufferSeries.__class__.__name__ == "list":
            self._bufferSeries = bufferSeries
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'bufferSeries' is not list but %s" % self._bufferSeries.__class__.__name__
            raise BaseException(strMessage)
        if sampleSeries is None:
            self._sampleSeries = []
        elif sampleSeries.__class__.__name__ == "list":
            self._sampleSeries = sampleSeries
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'sampleSeries' is not list but %s" % self._sampleSeries.__class__.__name__
            raise BaseException(strMessage)
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'forceReprocess' is not XSDataBoolean but %s" % self._forceReprocess.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectory1D argument is not XSDataFile but %s" % directory1D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory1D(self): self._directory1D = None
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectory2D argument is not XSDataFile but %s" % directory2D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory2D(self): self._directory2D = None
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectoryMisc argument is not XSDataFile but %s" % directoryMisc.__class__.__name__
            raise BaseException(strMessage)
    def delDirectoryMisc(self): self._directoryMisc = None
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    # Methods and properties for the 'bufferSeries' attribute
    def getBufferSeries(self): return self._bufferSeries
    def setBufferSeries(self, bufferSeries):
        if bufferSeries is None:
            self._bufferSeries = []
        elif bufferSeries.__class__.__name__ == "list":
            self._bufferSeries = bufferSeries
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setBufferSeries argument is not list but %s" % bufferSeries.__class__.__name__
            raise BaseException(strMessage)
    def delBufferSeries(self): self._bufferSeries = None
    bufferSeries = property(getBufferSeries, setBufferSeries, delBufferSeries, "Property for bufferSeries")
    def addBufferSeries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._bufferSeries.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is not XSDataFileSeries but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBufferSeries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertBufferSeries argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertBufferSeries argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._bufferSeries[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is not XSDataFileSeries but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sampleSeries' attribute
    def getSampleSeries(self): return self._sampleSeries
    def setSampleSeries(self, sampleSeries):
        if sampleSeries is None:
            self._sampleSeries = []
        elif sampleSeries.__class__.__name__ == "list":
            self._sampleSeries = sampleSeries
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setSampleSeries argument is not list but %s" % sampleSeries.__class__.__name__
            raise BaseException(strMessage)
    def delSampleSeries(self): self._sampleSeries = None
    sampleSeries = property(getSampleSeries, setSampleSeries, delSampleSeries, "Property for sampleSeries")
    def addSampleSeries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._sampleSeries.append(value)
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is not XSDataFileSeries but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSampleSeries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertSampleSeries argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertSampleSeries argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._sampleSeries[index] = value
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is not XSDataFileSeries but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'forceReprocess' attribute
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setForceReprocess argument is not XSDataBoolean but %s" % forceReprocess.__class__.__name__
            raise BaseException(strMessage)
    def delForceReprocess(self): self._forceReprocess = None
    forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
    def export(self, outfile, level, name_='XSDataInputBioSaxsSingleSamplev1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSingleSamplev1_0'):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_='directory1D')
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_='directory2D')
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_='directoryMisc')
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
        for bufferSeries_ in self.getBufferSeries():
            bufferSeries_.export(outfile, level, name_='bufferSeries')
        if self.getBufferSeries() == []:
            warnEmptyAttribute("bufferSeries", "XSDataFileSeries")
        for sampleSeries_ in self.getSampleSeries():
            sampleSeries_.export(outfile, level, name_='sampleSeries')
        if self.getSampleSeries() == []:
            warnEmptyAttribute("sampleSeries", "XSDataFileSeries")
        if self._forceReprocess is not None:
            self.forceReprocess.export(outfile, level, name_='forceReprocess')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory1D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory2D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directoryMisc':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bufferSeries':
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.bufferSeries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sampleSeries':
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.sampleSeries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forceReprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setForceReprocess(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataInputBioSaxsSingleSamplev1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSingleSamplev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataInputBioSaxsSingleSamplev1_0


class XSDataResultBioSaxsMetadatav1_0(XSDataResultBioSaxsSampleExperiment):
    def __init__(self, status=None, code=None, comments=None, concentration=None, timeOfFrame=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, experimentSetup=None, sample=None):
        XSDataResultBioSaxsSampleExperiment.__init__(self, status, code, comments, concentration, timeOfFrame, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'outputImage' is not XSDataImage but %s" % self._outputImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    # Methods and properties for the 'outputImage' attribute
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = "ERROR! XSDataResultBioSaxsMetadatav1_0.setOutputImage argument is not XSDataImage but %s" % outputImage.__class__.__name__
            raise BaseException(strMessage)
    def delOutputImage(self): self._outputImage = None
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def export(self, outfile, level, name_='XSDataResultBioSaxsMetadatav1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsMetadatav1_0'):
        XSDataResultBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataResultBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export(outfile, 0, name_='XSDataResultBioSaxsMetadatav1_0')
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsMetadatav1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0")
        oStreamString.close()
        return rootObj
    parseString = staticmethod(parseString)
    #Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod(parseFile)
# end class XSDataResultBioSaxsMetadatav1_0



# End of data representation classes.



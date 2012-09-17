#!/usr/bin/env python

#
# Generated Fri Sep 7 03:07::46 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataEdnaSaxs": "ednaSaxs/datamodel", \
 "XSDataEdnaSaxs": "ednaSaxs/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
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


def checkType(_strClassName, _strMethodName, _value, _strExpectedType):
    if _value != None:
        if _strExpectedType not in (_value.__class__.__name__,)+(_value.__class__.__bases__):
            if (_value.__class__.__name__ == "unicode") and (_strExpectedType == "str"):
                # Accept unicode as expected str
                return
            elif (_value.__class__.__name__ == "int") and (_strExpectedType in ["float", "double"]):
                # Accept int as expected double or float
                return
            else:
                strMessage = "ERROR! %s.%s argument is not %s but %s" % (_strClassName, _strMethodName, _strExpectedType, _value.__class__.__name__)
                print(strMessage)


def warnEmptyAttribute(_strName, _strTypeName):
    if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
        print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

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
    def __init__(self, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", detector, "XSDataString")
        self._detector = detector
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", maskFile, "XSDataImage")
        self._maskFile = maskFile
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
        checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        checkType("XSDataBioSaxsExperimentSetup", "setDetector", detector, "XSDataString")
        self._detector = detector
    def delDetector(self): self._detector = None
    # Properties
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        checkType("XSDataBioSaxsExperimentSetup", "setDetectorDistance", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
    def delDetectorDistance(self): self._detectorDistance = None
    # Properties
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        checkType("XSDataBioSaxsExperimentSetup", "setPixelSize_1", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
    def delPixelSize_1(self): self._pixelSize_1 = None
    # Properties
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        checkType("XSDataBioSaxsExperimentSetup", "setPixelSize_2", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
    def delPixelSize_2(self): self._pixelSize_2 = None
    # Properties
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
    def delBeamCenter_1(self): self._beamCenter_1 = None
    # Properties
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
    def delBeamCenter_2(self): self._beamCenter_2 = None
    # Properties
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        checkType("XSDataBioSaxsExperimentSetup", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
    def delBeamStopDiode(self): self._beamStopDiode = None
    # Properties
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        checkType("XSDataBioSaxsExperimentSetup", "setWavelength", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
    def delWavelength(self): self._wavelength = None
    # Properties
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        checkType("XSDataBioSaxsExperimentSetup", "setMachineCurrent", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
    def delMachineCurrent(self): self._machineCurrent = None
    # Properties
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        checkType("XSDataBioSaxsExperimentSetup", "setMaskFile", maskFile, "XSDataImage")
        self._maskFile = maskFile
    def delMaskFile(self): self._maskFile = None
    # Properties
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        checkType("XSDataBioSaxsExperimentSetup", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
    def delNormalizationFactor(self): self._normalizationFactor = None
    # Properties
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        checkType("XSDataBioSaxsExperimentSetup", "setStorageTemperature", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
    def delStorageTemperature(self): self._storageTemperature = None
    # Properties
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        checkType("XSDataBioSaxsExperimentSetup", "setExposureTemperature", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
    def delExposureTemperature(self): self._exposureTemperature = None
    # Properties
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        checkType("XSDataBioSaxsExperimentSetup", "setExposureTime", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
    def delExposureTime(self): self._exposureTime = None
    # Properties
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        checkType("XSDataBioSaxsExperimentSetup", "setFrameNumber", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
    def delFrameNumber(self): self._frameNumber = None
    # Properties
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        checkType("XSDataBioSaxsExperimentSetup", "setFrameMax", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def delFrameMax(self): self._frameMax = None
    # Properties
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
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
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBioSaxsExperimentSetup' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBioSaxsExperimentSetup is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBioSaxsExperimentSetup.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsExperimentSetup

class XSDataBioSaxsSample(XSData):
    def __init__(self, code=None, comments=None, concentration=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", concentration, "XSDataDouble")
        self._concentration = concentration
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", comments, "XSDataString")
        self._comments = comments
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", code, "XSDataString")
        self._code = code
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        checkType("XSDataBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
        self._concentration = concentration
    def delConcentration(self): self._concentration = None
    # Properties
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    def getComments(self): return self._comments
    def setComments(self, comments):
        checkType("XSDataBioSaxsSample", "setComments", comments, "XSDataString")
        self._comments = comments
    def delComments(self): self._comments = None
    # Properties
    comments = property(getComments, setComments, delComments, "Property for comments")
    def getCode(self): return self._code
    def setCode(self, code):
        checkType("XSDataBioSaxsSample", "setCode", code, "XSDataString")
        self._code = code
    def delCode(self): self._code = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBioSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsSample

class XSDataFileSeries(XSData):
    def __init__(self, files=None):
        XSData.__init__(self, )
    
    
        if files is None:
            self._files = []
        else:
            checkType("XSDataFileSeries", "Constructor of XSDataFileSeries", files, "list")
            self._files = files
    def getFiles(self): return self._files
    def setFiles(self, files):
        checkType("XSDataFileSeries", "setFiles", files, "list")
        self._files = files
    def delFiles(self): self._files = None
    # Properties
    files = property(getFiles, setFiles, delFiles, "Property for files")
    def addFiles(self, value):
        checkType("XSDataFileSeries", "setFiles", value, "XSDataFile")
        self._files.append(value)
    def insertFiles(self, index, value):
        checkType("XSDataFileSeries", "setFiles", value, "XSDataFile")
        self._files[index] = value
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataFileSeries" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataFileSeries' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataFileSeries is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataFileSeries.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataFileSeries" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataFileSeries

class XSDataInputBioSaxsAsciiExportv1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputBioSaxsAsciiExportv1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsAsciiExportv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsAsciiExportv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAsciiExportv1_0

class XSDataInputBioSaxsAzimutIntv1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, correctedImage=None, integratedCurve=None, integratedImage=None, normalizedImageSize=None, normalizedImage=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", normalizedImageSize, "XSDataInteger")
        self._normalizedImageSize = normalizedImageSize
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", correctedImage, "XSDataImage")
        self._correctedImage = correctedImage
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
    def delNormalizedImage(self): self._normalizedImage = None
    # Properties
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    def getNormalizedImageSize(self): return self._normalizedImageSize
    def setNormalizedImageSize(self, normalizedImageSize):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setNormalizedImageSize", normalizedImageSize, "XSDataInteger")
        self._normalizedImageSize = normalizedImageSize
    def delNormalizedImageSize(self): self._normalizedImageSize = None
    # Properties
    normalizedImageSize = property(getNormalizedImageSize, setNormalizedImageSize, delNormalizedImageSize, "Property for normalizedImageSize")
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    def getCorrectedImage(self): return self._correctedImage
    def setCorrectedImage(self, correctedImage):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setCorrectedImage", correctedImage, "XSDataImage")
        self._correctedImage = correctedImage
    def delCorrectedImage(self): self._correctedImage = None
    # Properties
    correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputBioSaxsAzimutIntv1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
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
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsAzimutIntv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsAzimutIntv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAzimutIntv1_0

class XSDataInputBioSaxsNormalizev1_0(XSDataInput):
    def __init__(self, configuration=None, experimentSetup=None, sample=None, rawImageSize=None, normalizedImage=None, logFile=None, rawImage=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", rawImage, "XSDataImage")
        self._rawImage = rawImage
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def getRawImage(self): return self._rawImage
    def setRawImage(self, rawImage):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setRawImage", rawImage, "XSDataImage")
        self._rawImage = rawImage
    def delRawImage(self): self._rawImage = None
    # Properties
    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
    def delNormalizedImage(self): self._normalizedImage = None
    # Properties
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def delRawImageSize(self): self._rawImageSize = None
    # Properties
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputBioSaxsNormalizev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsNormalizev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsNormalizev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsNormalizev1_0

class XSDataInputBioSaxsProcessOneFilev1_0(XSDataInput):
    """Plugin that runs subsequently Normalize and Azimuthal integration"""
    def __init__(self, configuration=None, integratedCurve=None, integratedImage=None, normalizedImage=None, logFile=None, rawImageSize=None, experimentSetup=None, sample=None, rawImage=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", rawImage, "XSDataImage")
        self._rawImage = rawImage
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def getRawImage(self): return self._rawImage
    def setRawImage(self, rawImage):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setRawImage", rawImage, "XSDataImage")
        self._rawImage = rawImage
    def delRawImage(self): self._rawImage = None
    # Properties
    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def delRawImageSize(self): self._rawImageSize = None
    # Properties
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
    def delNormalizedImage(self): self._normalizedImage = None
    # Properties
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setIntegratedImage", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
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
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsProcessOneFilev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsProcessOneFilev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsProcessOneFilev1_0

class XSDataInputBioSaxsReduceFileSeriev1_0(XSDataInput):
    """Run ProcessOneFile on each file of a time time serie  """
    def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", fileSerie, "XSDataFileSeries")
        self._fileSerie = fileSerie
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directory1D, "XSDataFile")
        self._directory1D = directory1D
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directory2D, "XSDataFile")
        self._directory2D = directory2D
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def getFileSerie(self): return self._fileSerie
    def setFileSerie(self, fileSerie):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setFileSerie", fileSerie, "XSDataFileSeries")
        self._fileSerie = fileSerie
    def delFileSerie(self): self._fileSerie = None
    # Properties
    fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectory1D", directory1D, "XSDataFile")
        self._directory1D = directory1D
    def delDirectory1D(self): self._directory1D = None
    # Properties
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectory2D", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def delDirectory2D(self): self._directory2D = None
    # Properties
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
    def delDirectoryMisc(self): self._directoryMisc = None
    # Properties
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setForceReprocess", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
    def delForceReprocess(self): self._forceReprocess = None
    # Properties
    forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    # Properties
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
    def delRelativeFidelity(self): self._relativeFidelity = None
    # Properties
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def delRawImageSize(self): self._rawImageSize = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsReduceFileSeriev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsReduceFileSeriev1_0

class XSDataInputBioSaxsSample(XSDataInput):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", concentration, "XSDataDouble")
        self._concentration = concentration
        checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", comments, "XSDataString")
        self._comments = comments
        checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", code, "XSDataString")
        self._code = code
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        checkType("XSDataInputBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
        self._concentration = concentration
    def delConcentration(self): self._concentration = None
    # Properties
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    def getComments(self): return self._comments
    def setComments(self, comments):
        checkType("XSDataInputBioSaxsSample", "setComments", comments, "XSDataString")
        self._comments = comments
    def delComments(self): self._comments = None
    # Properties
    comments = property(getComments, setComments, delComments, "Property for comments")
    def getCode(self): return self._code
    def setCode(self, code):
        checkType("XSDataInputBioSaxsSample", "setCode", code, "XSDataString")
        self._code = code
    def delCode(self): self._code = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSample

class XSDataInputBioSaxsSmartMergev1_0(XSDataInput):
    def __init__(self, configuration=None, subtractedCurve=None, mergedCurve=None, sample=None, relativeFidelity=None, absoluteFidelity=None, inputCurves=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputCurves is None:
            self._inputCurves = []
        else:
            checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", inputCurves, "list")
            self._inputCurves = inputCurves
        checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
        checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
        checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
        checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def getInputCurves(self): return self._inputCurves
    def setInputCurves(self, inputCurves):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", inputCurves, "list")
        self._inputCurves = inputCurves
    def delInputCurves(self): self._inputCurves = None
    # Properties
    inputCurves = property(getInputCurves, setInputCurves, delInputCurves, "Property for inputCurves")
    def addInputCurves(self, value):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", value, "XSDataFile")
        self._inputCurves.append(value)
    def insertInputCurves(self, index, value):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", value, "XSDataFile")
        self._inputCurves[index] = value
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    # Properties
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
    def delRelativeFidelity(self): self._relativeFidelity = None
    # Properties
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
    def delMergedCurve(self): self._mergedCurve = None
    # Properties
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataInputBioSaxsSmartMergev1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
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
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsSmartMergev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsSmartMergev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSmartMergev1_0

class XSDataInputBioSaxsSubtractv1_0(XSDataInput):
    """Runs sequentially subtraction of buffer and SaxsAnalysis"""
    def __init__(self, configuration=None, gnomFile=None, subtractedCurve=None, sample=None, bufferCurves=None, sampleCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsSubtractv1_0", "Constructor of XSDataInputBioSaxsSubtractv1_0", sampleCurve, "XSDataFile")
        self._sampleCurve = sampleCurve
        if bufferCurves is None:
            self._bufferCurves = []
        else:
            checkType("XSDataInputBioSaxsSubtractv1_0", "Constructor of XSDataInputBioSaxsSubtractv1_0", bufferCurves, "list")
            self._bufferCurves = bufferCurves
        checkType("XSDataInputBioSaxsSubtractv1_0", "Constructor of XSDataInputBioSaxsSubtractv1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputBioSaxsSubtractv1_0", "Constructor of XSDataInputBioSaxsSubtractv1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
        checkType("XSDataInputBioSaxsSubtractv1_0", "Constructor of XSDataInputBioSaxsSubtractv1_0", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def getSampleCurve(self): return self._sampleCurve
    def setSampleCurve(self, sampleCurve):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setSampleCurve", sampleCurve, "XSDataFile")
        self._sampleCurve = sampleCurve
    def delSampleCurve(self): self._sampleCurve = None
    # Properties
    sampleCurve = property(getSampleCurve, setSampleCurve, delSampleCurve, "Property for sampleCurve")
    def getBufferCurves(self): return self._bufferCurves
    def setBufferCurves(self, bufferCurves):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setBufferCurves", bufferCurves, "list")
        self._bufferCurves = bufferCurves
    def delBufferCurves(self): self._bufferCurves = None
    # Properties
    bufferCurves = property(getBufferCurves, setBufferCurves, delBufferCurves, "Property for bufferCurves")
    def addBufferCurves(self, value):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setBufferCurves", value, "XSDataFile")
        self._bufferCurves.append(value)
    def insertBufferCurves(self, index, value):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setBufferCurves", value, "XSDataFile")
        self._bufferCurves[index] = value
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        checkType("XSDataInputBioSaxsSubtractv1_0", "setGnomFile", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def delGnomFile(self): self._gnomFile = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsSubtractv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsSubtractv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSubtractv1_0

class XSDataInputBioSaxsToSASv1_0(XSDataInput):
    """This is just a wrapper for the SAS downstream pipeline"""
    def __init__(self, configuration=None, destinationDirectory=None, qMax=None, lastPoint=None, firstPoint=None, subtractedCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputBioSaxsToSASv1_0", "Constructor of XSDataInputBioSaxsToSASv1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
        checkType("XSDataInputBioSaxsToSASv1_0", "Constructor of XSDataInputBioSaxsToSASv1_0", firstPoint, "XSDataInteger")
        self._firstPoint = firstPoint
        checkType("XSDataInputBioSaxsToSASv1_0", "Constructor of XSDataInputBioSaxsToSASv1_0", lastPoint, "XSDataInteger")
        self._lastPoint = lastPoint
        checkType("XSDataInputBioSaxsToSASv1_0", "Constructor of XSDataInputBioSaxsToSASv1_0", qMax, "XSDataDouble")
        self._qMax = qMax
        checkType("XSDataInputBioSaxsToSASv1_0", "Constructor of XSDataInputBioSaxsToSASv1_0", destinationDirectory, "XSDataFile")
        self._destinationDirectory = destinationDirectory
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataInputBioSaxsToSASv1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def getFirstPoint(self): return self._firstPoint
    def setFirstPoint(self, firstPoint):
        checkType("XSDataInputBioSaxsToSASv1_0", "setFirstPoint", firstPoint, "XSDataInteger")
        self._firstPoint = firstPoint
    def delFirstPoint(self): self._firstPoint = None
    # Properties
    firstPoint = property(getFirstPoint, setFirstPoint, delFirstPoint, "Property for firstPoint")
    def getLastPoint(self): return self._lastPoint
    def setLastPoint(self, lastPoint):
        checkType("XSDataInputBioSaxsToSASv1_0", "setLastPoint", lastPoint, "XSDataInteger")
        self._lastPoint = lastPoint
    def delLastPoint(self): self._lastPoint = None
    # Properties
    lastPoint = property(getLastPoint, setLastPoint, delLastPoint, "Property for lastPoint")
    def getQMax(self): return self._qMax
    def setQMax(self, qMax):
        checkType("XSDataInputBioSaxsToSASv1_0", "setQMax", qMax, "XSDataDouble")
        self._qMax = qMax
    def delQMax(self): self._qMax = None
    # Properties
    qMax = property(getQMax, setQMax, delQMax, "Property for qMax")
    def getDestinationDirectory(self): return self._destinationDirectory
    def setDestinationDirectory(self, destinationDirectory):
        checkType("XSDataInputBioSaxsToSASv1_0", "setDestinationDirectory", destinationDirectory, "XSDataFile")
        self._destinationDirectory = destinationDirectory
    def delDestinationDirectory(self): self._destinationDirectory = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsToSASv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsToSASv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsToSASv1_0

class XSDataResultBioSaxsAsciiExportv1_0(XSDataResult):
    def __init__(self, status=None, processLog=None, integratedCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsAsciiExportv1_0", "Constructor of XSDataResultBioSaxsAsciiExportv1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
        checkType("XSDataResultBioSaxsAsciiExportv1_0", "Constructor of XSDataResultBioSaxsAsciiExportv1_0", processLog, "XSDataString")
        self._processLog = processLog
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataResultBioSaxsAsciiExportv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        checkType("XSDataResultBioSaxsAsciiExportv1_0", "setProcessLog", processLog, "XSDataString")
        self._processLog = processLog
    def delProcessLog(self): self._processLog = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsAsciiExportv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsAsciiExportv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAsciiExportv1_0

class XSDataResultBioSaxsAveragev1_0(XSDataResult):
    def __init__(self, status=None, logFile=None, processLog=None, averagedCurve=None, averagedImage=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", averagedImage, "XSDataImage")
        self._averagedImage = averagedImage
        checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", averagedCurve, "XSDataFile")
        self._averagedCurve = averagedCurve
        checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", processLog, "XSDataString")
        self._processLog = processLog
        checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", logFile, "XSDataFile")
        self._logFile = logFile
    def getAveragedImage(self): return self._averagedImage
    def setAveragedImage(self, averagedImage):
        checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedImage", averagedImage, "XSDataImage")
        self._averagedImage = averagedImage
    def delAveragedImage(self): self._averagedImage = None
    # Properties
    averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
    def getAveragedCurve(self): return self._averagedCurve
    def setAveragedCurve(self, averagedCurve):
        checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedCurve", averagedCurve, "XSDataFile")
        self._averagedCurve = averagedCurve
    def delAveragedCurve(self): self._averagedCurve = None
    # Properties
    averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        checkType("XSDataResultBioSaxsAveragev1_0", "setProcessLog", processLog, "XSDataString")
        self._processLog = processLog
    def delProcessLog(self): self._processLog = None
    # Properties
    processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataResultBioSaxsAveragev1_0", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsAveragev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsAveragev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAveragev1_0

class XSDataResultBioSaxsAzimutIntv1_0(XSDataResult):
    def __init__(self, status=None, integratedCurve=None, integratedImage=None, correctedImage=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", correctedImage, "XSDataImage")
        self._correctedImage = correctedImage
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def getCorrectedImage(self): return self._correctedImage
    def setCorrectedImage(self, correctedImage):
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "setCorrectedImage", correctedImage, "XSDataImage")
        self._correctedImage = correctedImage
    def delCorrectedImage(self): self._correctedImage = None
    # Properties
    correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataResultBioSaxsAzimutIntv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsAzimutIntv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsAzimutIntv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAzimutIntv1_0

class XSDataResultBioSaxsNormalizev1_0(XSDataResult):
    def __init__(self, status=None, processLog=None, logFile=None, normalizedImage=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
        checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", processLog, "XSDataString")
        self._processLog = processLog
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        checkType("XSDataResultBioSaxsNormalizev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
    def delNormalizedImage(self): self._normalizedImage = None
    # Properties
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataResultBioSaxsNormalizev1_0", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getProcessLog(self): return self._processLog
    def setProcessLog(self, processLog):
        checkType("XSDataResultBioSaxsNormalizev1_0", "setProcessLog", processLog, "XSDataString")
        self._processLog = processLog
    def delProcessLog(self): self._processLog = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsNormalizev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsNormalizev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsNormalizev1_0

class XSDataResultBioSaxsProcessOneFilev1_0(XSDataResult):
    def __init__(self, status=None, integratedCurve=None, integratedImage=None, normalizedImage=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def getNormalizedImage(self): return self._normalizedImage
    def setNormalizedImage(self, normalizedImage):
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
        self._normalizedImage = normalizedImage
    def delNormalizedImage(self): self._normalizedImage = None
    # Properties
    normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setIntegratedImage", integratedImage, "XSDataImage")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
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
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsProcessOneFilev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsProcessOneFilev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsProcessOneFilev1_0

class XSDataResultBioSaxsReduceFileSeriev1_0(XSDataResult):
    def __init__(self, status=None, directoryMisc=None, directory2D=None, directory1D=None, mergedCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directory1D, "XSDataFile")
        self._directory1D = directory1D
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directory2D, "XSDataFile")
        self._directory2D = directory2D
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
    def delMergedCurve(self): self._mergedCurve = None
    # Properties
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectory1D", directory1D, "XSDataFile")
        self._directory1D = directory1D
    def delDirectory1D(self): self._directory1D = None
    # Properties
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectory2D", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def delDirectory2D(self): self._directory2D = None
    # Properties
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
    def delDirectoryMisc(self): self._directoryMisc = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsReduceFileSeriev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsReduceFileSeriev1_0

class XSDataResultBioSaxsSample(XSDataResult):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, status=None, code=None, comments=None, concentration=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", concentration, "XSDataDouble")
        self._concentration = concentration
        checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", comments, "XSDataString")
        self._comments = comments
        checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", code, "XSDataString")
        self._code = code
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        checkType("XSDataResultBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
        self._concentration = concentration
    def delConcentration(self): self._concentration = None
    # Properties
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    def getComments(self): return self._comments
    def setComments(self, comments):
        checkType("XSDataResultBioSaxsSample", "setComments", comments, "XSDataString")
        self._comments = comments
    def delComments(self): self._comments = None
    # Properties
    comments = property(getComments, setComments, delComments, "Property for comments")
    def getCode(self): return self._code
    def setCode(self, code):
        checkType("XSDataResultBioSaxsSample", "setCode", code, "XSDataString")
        self._code = code
    def delCode(self): self._code = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSample

class XSDataResultBioSaxsSingleSamplev1_0(XSDataResult):
    """Class for precessing a single sample (at 1 single concentration)"""
    def __init__(self, status=None, directory2D=None, directory1D=None, outputCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", directory1D, "XSDataFile")
        self._directory1D = directory1D
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "setOutputCurve", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def delOutputCurve(self): self._outputCurve = None
    # Properties
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "setDirectory1D", directory1D, "XSDataFile")
        self._directory1D = directory1D
    def delDirectory1D(self): self._directory1D = None
    # Properties
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        checkType("XSDataResultBioSaxsSingleSamplev1_0", "setDirectory2D", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def delDirectory2D(self): self._directory2D = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsSingleSamplev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsSingleSamplev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSingleSamplev1_0

class XSDataResultBioSaxsSmartMergev1_0(XSDataResult):
    def __init__(self, status=None, subtractedCurve=None, volume=None, gnom=None, autoRg=None, mergedCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
        checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
        checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", gnom, "XSDataGnom")
        self._gnom = gnom
        checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", volume, "XSDataDoubleWithUnit")
        self._volume = volume
        checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def getMergedCurve(self): return self._mergedCurve
    def setMergedCurve(self, mergedCurve):
        checkType("XSDataResultBioSaxsSmartMergev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
        self._mergedCurve = mergedCurve
    def delMergedCurve(self): self._mergedCurve = None
    # Properties
    mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        checkType("XSDataResultBioSaxsSmartMergev1_0", "setAutoRg", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
    def delAutoRg(self): self._autoRg = None
    # Properties
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        checkType("XSDataResultBioSaxsSmartMergev1_0", "setGnom", gnom, "XSDataGnom")
        self._gnom = gnom
    def delGnom(self): self._gnom = None
    # Properties
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        checkType("XSDataResultBioSaxsSmartMergev1_0", "setVolume", volume, "XSDataDoubleWithUnit")
        self._volume = volume
    def delVolume(self): self._volume = None
    # Properties
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataResultBioSaxsSmartMergev1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsSmartMergev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsSmartMergev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSmartMergev1_0

class XSDataResultBioSaxsSubtractv1_0(XSDataResult):
    def __init__(self, status=None, subtractedCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsSubtractv1_0", "Constructor of XSDataResultBioSaxsSubtractv1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataResultBioSaxsSubtractv1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsSubtractv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsSubtractv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSubtractv1_0

class XSDataResultBioSaxsToSASv1_0(XSDataResult):
    def __init__(self, status=None, htmlPage=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultBioSaxsToSASv1_0", "Constructor of XSDataResultBioSaxsToSASv1_0", htmlPage, "XSDataFile")
        self._htmlPage = htmlPage
    def getHtmlPage(self): return self._htmlPage
    def setHtmlPage(self, htmlPage):
        checkType("XSDataResultBioSaxsToSASv1_0", "setHtmlPage", htmlPage, "XSDataFile")
        self._htmlPage = htmlPage
    def delHtmlPage(self): self._htmlPage = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsToSASv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsToSASv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsToSASv1_0

class XSDataInputBioSaxsHPLCv1_0(XSDataInputBioSaxsProcessOneFilev1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""
    def __init__(self, configuration=None, integratedCurve=None, integratedImage=None, normalizedImage=None, logFile=None, rawImageSize=None, experimentSetup=None, sample=None, rawImage=None, gnomFile=None, subtractedCurve=None, bufferCurve=None):
        XSDataInputBioSaxsProcessOneFilev1_0.__init__(self, configuration, integratedCurve, integratedImage, normalizedImage, logFile, rawImageSize, experimentSetup, sample, rawImage)
    
    
        checkType("XSDataInputBioSaxsHPLCv1_0", "Constructor of XSDataInputBioSaxsHPLCv1_0", bufferCurve, "XSDataFile")
        self._bufferCurve = bufferCurve
        checkType("XSDataInputBioSaxsHPLCv1_0", "Constructor of XSDataInputBioSaxsHPLCv1_0", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
        checkType("XSDataInputBioSaxsHPLCv1_0", "Constructor of XSDataInputBioSaxsHPLCv1_0", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def getBufferCurve(self): return self._bufferCurve
    def setBufferCurve(self, bufferCurve):
        checkType("XSDataInputBioSaxsHPLCv1_0", "setBufferCurve", bufferCurve, "XSDataFile")
        self._bufferCurve = bufferCurve
    def delBufferCurve(self): self._bufferCurve = None
    # Properties
    bufferCurve = property(getBufferCurve, setBufferCurve, delBufferCurve, "Property for bufferCurve")
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataInputBioSaxsHPLCv1_0", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        checkType("XSDataInputBioSaxsHPLCv1_0", "setGnomFile", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def delGnomFile(self): self._gnomFile = None
    # Properties
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
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
        XSDataInputBioSaxsProcessOneFilev1_0.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsHPLCv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsHPLCv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsHPLCv1_0

class XSDataInputBioSaxsSampleExperiment(XSDataInputBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSDataInputBioSaxsSample.__init__(self, configuration, code, comments, concentration)
    
    
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", detector, "XSDataString")
        self._detector = detector
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", maskFile, "XSDataImage")
        self._maskFile = maskFile
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
        checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        checkType("XSDataInputBioSaxsSampleExperiment", "setDetector", detector, "XSDataString")
        self._detector = detector
    def delDetector(self): self._detector = None
    # Properties
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        checkType("XSDataInputBioSaxsSampleExperiment", "setDetectorDistance", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
    def delDetectorDistance(self): self._detectorDistance = None
    # Properties
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        checkType("XSDataInputBioSaxsSampleExperiment", "setPixelSize_1", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
    def delPixelSize_1(self): self._pixelSize_1 = None
    # Properties
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        checkType("XSDataInputBioSaxsSampleExperiment", "setPixelSize_2", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
    def delPixelSize_2(self): self._pixelSize_2 = None
    # Properties
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        checkType("XSDataInputBioSaxsSampleExperiment", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
    def delBeamCenter_1(self): self._beamCenter_1 = None
    # Properties
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        checkType("XSDataInputBioSaxsSampleExperiment", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
    def delBeamCenter_2(self): self._beamCenter_2 = None
    # Properties
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        checkType("XSDataInputBioSaxsSampleExperiment", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
    def delBeamStopDiode(self): self._beamStopDiode = None
    # Properties
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        checkType("XSDataInputBioSaxsSampleExperiment", "setWavelength", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
    def delWavelength(self): self._wavelength = None
    # Properties
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        checkType("XSDataInputBioSaxsSampleExperiment", "setMachineCurrent", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
    def delMachineCurrent(self): self._machineCurrent = None
    # Properties
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        checkType("XSDataInputBioSaxsSampleExperiment", "setMaskFile", maskFile, "XSDataImage")
        self._maskFile = maskFile
    def delMaskFile(self): self._maskFile = None
    # Properties
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        checkType("XSDataInputBioSaxsSampleExperiment", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
    def delNormalizationFactor(self): self._normalizationFactor = None
    # Properties
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        checkType("XSDataInputBioSaxsSampleExperiment", "setStorageTemperature", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
    def delStorageTemperature(self): self._storageTemperature = None
    # Properties
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        checkType("XSDataInputBioSaxsSampleExperiment", "setExposureTemperature", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
    def delExposureTemperature(self): self._exposureTemperature = None
    # Properties
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        checkType("XSDataInputBioSaxsSampleExperiment", "setExposureTime", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
    def delExposureTime(self): self._exposureTime = None
    # Properties
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        checkType("XSDataInputBioSaxsSampleExperiment", "setFrameNumber", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
    def delFrameNumber(self): self._frameNumber = None
    # Properties
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        checkType("XSDataInputBioSaxsSampleExperiment", "setFrameMax", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def delFrameMax(self): self._frameMax = None
    # Properties
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
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
        XSDataInputBioSaxsSample.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsSampleExperiment' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsSampleExperiment.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSampleExperiment

class XSDataResultBioSaxsHPLCv1_0(XSDataResultBioSaxsSubtractv1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""
    def __init__(self, status=None, subtractedCurve=None, integratedCurve=None):
        XSDataResultBioSaxsSubtractv1_0.__init__(self, status, subtractedCurve)
    
    
        checkType("XSDataResultBioSaxsHPLCv1_0", "Constructor of XSDataResultBioSaxsHPLCv1_0", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def getIntegratedCurve(self): return self._integratedCurve
    def setIntegratedCurve(self, integratedCurve):
        checkType("XSDataResultBioSaxsHPLCv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
        self._integratedCurve = integratedCurve
    def delIntegratedCurve(self): self._integratedCurve = None
    # Properties
    integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
    def export(self, outfile, level, name_='XSDataResultBioSaxsHPLCv1_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsHPLCv1_0'):
        XSDataResultBioSaxsSubtractv1_0.exportChildren(self, outfile, level, name_)
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_='integratedCurve')
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
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
        XSDataResultBioSaxsSubtractv1_0.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsHPLCv1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsHPLCv1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsHPLCv1_0

class XSDataResultBioSaxsSampleExperiment(XSDataResultBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""
    def __init__(self, status=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSDataResultBioSaxsSample.__init__(self, status, code, comments, concentration)
    
    
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", detector, "XSDataString")
        self._detector = detector
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", maskFile, "XSDataImage")
        self._maskFile = maskFile
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
        checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        checkType("XSDataResultBioSaxsSampleExperiment", "setDetector", detector, "XSDataString")
        self._detector = detector
    def delDetector(self): self._detector = None
    # Properties
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        checkType("XSDataResultBioSaxsSampleExperiment", "setDetectorDistance", detectorDistance, "XSDataLength")
        self._detectorDistance = detectorDistance
    def delDetectorDistance(self): self._detectorDistance = None
    # Properties
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        checkType("XSDataResultBioSaxsSampleExperiment", "setPixelSize_1", pixelSize_1, "XSDataLength")
        self._pixelSize_1 = pixelSize_1
    def delPixelSize_1(self): self._pixelSize_1 = None
    # Properties
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        checkType("XSDataResultBioSaxsSampleExperiment", "setPixelSize_2", pixelSize_2, "XSDataLength")
        self._pixelSize_2 = pixelSize_2
    def delPixelSize_2(self): self._pixelSize_2 = None
    # Properties
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        checkType("XSDataResultBioSaxsSampleExperiment", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
        self._beamCenter_1 = beamCenter_1
    def delBeamCenter_1(self): self._beamCenter_1 = None
    # Properties
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        checkType("XSDataResultBioSaxsSampleExperiment", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
        self._beamCenter_2 = beamCenter_2
    def delBeamCenter_2(self): self._beamCenter_2 = None
    # Properties
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        checkType("XSDataResultBioSaxsSampleExperiment", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
        self._beamStopDiode = beamStopDiode
    def delBeamStopDiode(self): self._beamStopDiode = None
    # Properties
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        checkType("XSDataResultBioSaxsSampleExperiment", "setWavelength", wavelength, "XSDataWavelength")
        self._wavelength = wavelength
    def delWavelength(self): self._wavelength = None
    # Properties
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        checkType("XSDataResultBioSaxsSampleExperiment", "setMachineCurrent", machineCurrent, "XSDataDouble")
        self._machineCurrent = machineCurrent
    def delMachineCurrent(self): self._machineCurrent = None
    # Properties
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        checkType("XSDataResultBioSaxsSampleExperiment", "setMaskFile", maskFile, "XSDataImage")
        self._maskFile = maskFile
    def delMaskFile(self): self._maskFile = None
    # Properties
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        checkType("XSDataResultBioSaxsSampleExperiment", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
        self._normalizationFactor = normalizationFactor
    def delNormalizationFactor(self): self._normalizationFactor = None
    # Properties
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    def getStorageTemperature(self): return self._storageTemperature
    def setStorageTemperature(self, storageTemperature):
        checkType("XSDataResultBioSaxsSampleExperiment", "setStorageTemperature", storageTemperature, "XSDataDouble")
        self._storageTemperature = storageTemperature
    def delStorageTemperature(self): self._storageTemperature = None
    # Properties
    storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
    def getExposureTemperature(self): return self._exposureTemperature
    def setExposureTemperature(self, exposureTemperature):
        checkType("XSDataResultBioSaxsSampleExperiment", "setExposureTemperature", exposureTemperature, "XSDataDouble")
        self._exposureTemperature = exposureTemperature
    def delExposureTemperature(self): self._exposureTemperature = None
    # Properties
    exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        checkType("XSDataResultBioSaxsSampleExperiment", "setExposureTime", exposureTime, "XSDataTime")
        self._exposureTime = exposureTime
    def delExposureTime(self): self._exposureTime = None
    # Properties
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    def getFrameNumber(self): return self._frameNumber
    def setFrameNumber(self, frameNumber):
        checkType("XSDataResultBioSaxsSampleExperiment", "setFrameNumber", frameNumber, "XSDataInteger")
        self._frameNumber = frameNumber
    def delFrameNumber(self): self._frameNumber = None
    # Properties
    frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
    def getFrameMax(self): return self._frameMax
    def setFrameMax(self, frameMax):
        checkType("XSDataResultBioSaxsSampleExperiment", "setFrameMax", frameMax, "XSDataInteger")
        self._frameMax = frameMax
    def delFrameMax(self): self._frameMax = None
    # Properties
    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
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
        XSDataResultBioSaxsSample.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsSampleExperiment' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsSampleExperiment.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSampleExperiment

class XSDataInputBioSaxsAveragev1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, logFile=None, averagedCurve=None, averagedImage=None, integratedImageSize=None, integratedImage=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
    
    
        if integratedImage is None:
            self._integratedImage = []
        else:
            checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", integratedImage, "list")
            self._integratedImage = integratedImage
        checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", integratedImageSize, "XSDataInteger")
        self._integratedImageSize = integratedImageSize
        checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", averagedImage, "XSDataImage")
        self._averagedImage = averagedImage
        checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", averagedCurve, "XSDataFile")
        self._averagedCurve = averagedCurve
        checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", logFile, "XSDataFile")
        self._logFile = logFile
    def getIntegratedImage(self): return self._integratedImage
    def setIntegratedImage(self, integratedImage):
        checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", integratedImage, "list")
        self._integratedImage = integratedImage
    def delIntegratedImage(self): self._integratedImage = None
    # Properties
    integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
    def addIntegratedImage(self, value):
        checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", value, "XSDataImage")
        self._integratedImage.append(value)
    def insertIntegratedImage(self, index, value):
        checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", value, "XSDataImage")
        self._integratedImage[index] = value
    def getIntegratedImageSize(self): return self._integratedImageSize
    def setIntegratedImageSize(self, integratedImageSize):
        checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImageSize", integratedImageSize, "XSDataInteger")
        self._integratedImageSize = integratedImageSize
    def delIntegratedImageSize(self): self._integratedImageSize = None
    # Properties
    integratedImageSize = property(getIntegratedImageSize, setIntegratedImageSize, delIntegratedImageSize, "Property for integratedImageSize")
    def getAveragedImage(self): return self._averagedImage
    def setAveragedImage(self, averagedImage):
        checkType("XSDataInputBioSaxsAveragev1_0", "setAveragedImage", averagedImage, "XSDataImage")
        self._averagedImage = averagedImage
    def delAveragedImage(self): self._averagedImage = None
    # Properties
    averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
    def getAveragedCurve(self): return self._averagedCurve
    def setAveragedCurve(self, averagedCurve):
        checkType("XSDataInputBioSaxsAveragev1_0", "setAveragedCurve", averagedCurve, "XSDataFile")
        self._averagedCurve = averagedCurve
    def delAveragedCurve(self): self._averagedCurve = None
    # Properties
    averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataInputBioSaxsAveragev1_0", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsAveragev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsAveragev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAveragev1_0

class XSDataInputBioSaxsMetadatav1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, inputImage=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
    
    
        checkType("XSDataInputBioSaxsMetadatav1_0", "Constructor of XSDataInputBioSaxsMetadatav1_0", inputImage, "XSDataImage")
        self._inputImage = inputImage
        checkType("XSDataInputBioSaxsMetadatav1_0", "Constructor of XSDataInputBioSaxsMetadatav1_0", outputImage, "XSDataImage")
        self._outputImage = outputImage
    def getInputImage(self): return self._inputImage
    def setInputImage(self, inputImage):
        checkType("XSDataInputBioSaxsMetadatav1_0", "setInputImage", inputImage, "XSDataImage")
        self._inputImage = inputImage
    def delInputImage(self): self._inputImage = None
    # Properties
    inputImage = property(getInputImage, setInputImage, delInputImage, "Property for inputImage")
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataInputBioSaxsMetadatav1_0", "setOutputImage", outputImage, "XSDataImage")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsMetadatav1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsMetadatav1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsMetadatav1_0

class XSDataInputBioSaxsSingleSamplev1_0(XSDataInputBioSaxsSampleExperiment):
    """Class for precessing a single sample (at 1 single concentration)"""
    def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, forceReprocess=None, sampleSeries=None, bufferSeries=None, directoryMisc=None, directory2D=None, directory1D=None):
        XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
    
    
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directory1D, "XSDataFile")
        self._directory1D = directory1D
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directory2D, "XSDataFile")
        self._directory2D = directory2D
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
        if bufferSeries is None:
            self._bufferSeries = []
        else:
            checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", bufferSeries, "list")
            self._bufferSeries = bufferSeries
        if sampleSeries is None:
            self._sampleSeries = []
        else:
            checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", sampleSeries, "list")
            self._sampleSeries = sampleSeries
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectory1D", directory1D, "XSDataFile")
        self._directory1D = directory1D
    def delDirectory1D(self): self._directory1D = None
    # Properties
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectory2D", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def delDirectory2D(self): self._directory2D = None
    # Properties
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
    def delDirectoryMisc(self): self._directoryMisc = None
    # Properties
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    def getBufferSeries(self): return self._bufferSeries
    def setBufferSeries(self, bufferSeries):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", bufferSeries, "list")
        self._bufferSeries = bufferSeries
    def delBufferSeries(self): self._bufferSeries = None
    # Properties
    bufferSeries = property(getBufferSeries, setBufferSeries, delBufferSeries, "Property for bufferSeries")
    def addBufferSeries(self, value):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", value, "XSDataFileSeries")
        self._bufferSeries.append(value)
    def insertBufferSeries(self, index, value):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", value, "XSDataFileSeries")
        self._bufferSeries[index] = value
    def getSampleSeries(self): return self._sampleSeries
    def setSampleSeries(self, sampleSeries):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", sampleSeries, "list")
        self._sampleSeries = sampleSeries
    def delSampleSeries(self): self._sampleSeries = None
    # Properties
    sampleSeries = property(getSampleSeries, setSampleSeries, delSampleSeries, "Property for sampleSeries")
    def addSampleSeries(self, value):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", value, "XSDataFileSeries")
        self._sampleSeries.append(value)
    def insertSampleSeries(self, index, value):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", value, "XSDataFileSeries")
        self._sampleSeries[index] = value
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        checkType("XSDataInputBioSaxsSingleSamplev1_0", "setForceReprocess", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
    def delForceReprocess(self): self._forceReprocess = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBioSaxsSingleSamplev1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBioSaxsSingleSamplev1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSingleSamplev1_0

class XSDataResultBioSaxsMetadatav1_0(XSDataResultBioSaxsSampleExperiment):
    def __init__(self, status=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, experimentSetup=None, sample=None):
        XSDataResultBioSaxsSampleExperiment.__init__(self, status, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
    
    
        checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
        checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", outputImage, "XSDataImage")
        self._outputImage = outputImage
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataResultBioSaxsMetadatav1_0", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataResultBioSaxsMetadatav1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataResultBioSaxsMetadatav1_0", "setOutputImage", outputImage, "XSDataImage")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBioSaxsMetadatav1_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBioSaxsMetadatav1_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsMetadatav1_0



# End of data representation classes.



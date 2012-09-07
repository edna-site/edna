#!/usr/bin/env python

#
# Generated Fri Sep 7 02:23::26 2012 by EDGenerateDS.
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
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataRotation
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataVectorDouble
    from XSDataCommon import XSDataDoubleWithUnit
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
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
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataRotation
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
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


class XSDataAutoRg(XSData):
    def __init__(self, isagregated=None, quality=None, lastPointUsed=None, firstPointUsed=None, i0Stdev=None, i0=None, rgStdev=None, rg=None, filename=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", filename, "XSDataFile")
        self._filename = filename
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", rg, "XSDataLength")
        self._rg = rg
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", rgStdev, "XSDataLength")
        self._rgStdev = rgStdev
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", i0, "XSDataDouble")
        self._i0 = i0
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", i0Stdev, "XSDataDouble")
        self._i0Stdev = i0Stdev
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", firstPointUsed, "XSDataInteger")
        self._firstPointUsed = firstPointUsed
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", lastPointUsed, "XSDataInteger")
        self._lastPointUsed = lastPointUsed
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", quality, "XSDataDouble")
        self._quality = quality
        checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", isagregated, "XSDataBoolean")
        self._isagregated = isagregated
    def getFilename(self): return self._filename
    def setFilename(self, filename):
        checkType("XSDataAutoRg", "setFilename", filename, "XSDataFile")
        self._filename = filename
    def delFilename(self): self._filename = None
    # Properties
    filename = property(getFilename, setFilename, delFilename, "Property for filename")
    def getRg(self): return self._rg
    def setRg(self, rg):
        checkType("XSDataAutoRg", "setRg", rg, "XSDataLength")
        self._rg = rg
    def delRg(self): self._rg = None
    # Properties
    rg = property(getRg, setRg, delRg, "Property for rg")
    def getRgStdev(self): return self._rgStdev
    def setRgStdev(self, rgStdev):
        checkType("XSDataAutoRg", "setRgStdev", rgStdev, "XSDataLength")
        self._rgStdev = rgStdev
    def delRgStdev(self): self._rgStdev = None
    # Properties
    rgStdev = property(getRgStdev, setRgStdev, delRgStdev, "Property for rgStdev")
    def getI0(self): return self._i0
    def setI0(self, i0):
        checkType("XSDataAutoRg", "setI0", i0, "XSDataDouble")
        self._i0 = i0
    def delI0(self): self._i0 = None
    # Properties
    i0 = property(getI0, setI0, delI0, "Property for i0")
    def getI0Stdev(self): return self._i0Stdev
    def setI0Stdev(self, i0Stdev):
        checkType("XSDataAutoRg", "setI0Stdev", i0Stdev, "XSDataDouble")
        self._i0Stdev = i0Stdev
    def delI0Stdev(self): self._i0Stdev = None
    # Properties
    i0Stdev = property(getI0Stdev, setI0Stdev, delI0Stdev, "Property for i0Stdev")
    def getFirstPointUsed(self): return self._firstPointUsed
    def setFirstPointUsed(self, firstPointUsed):
        checkType("XSDataAutoRg", "setFirstPointUsed", firstPointUsed, "XSDataInteger")
        self._firstPointUsed = firstPointUsed
    def delFirstPointUsed(self): self._firstPointUsed = None
    # Properties
    firstPointUsed = property(getFirstPointUsed, setFirstPointUsed, delFirstPointUsed, "Property for firstPointUsed")
    def getLastPointUsed(self): return self._lastPointUsed
    def setLastPointUsed(self, lastPointUsed):
        checkType("XSDataAutoRg", "setLastPointUsed", lastPointUsed, "XSDataInteger")
        self._lastPointUsed = lastPointUsed
    def delLastPointUsed(self): self._lastPointUsed = None
    # Properties
    lastPointUsed = property(getLastPointUsed, setLastPointUsed, delLastPointUsed, "Property for lastPointUsed")
    def getQuality(self): return self._quality
    def setQuality(self, quality):
        checkType("XSDataAutoRg", "setQuality", quality, "XSDataDouble")
        self._quality = quality
    def delQuality(self): self._quality = None
    # Properties
    quality = property(getQuality, setQuality, delQuality, "Property for quality")
    def getIsagregated(self): return self._isagregated
    def setIsagregated(self, isagregated):
        checkType("XSDataAutoRg", "setIsagregated", isagregated, "XSDataBoolean")
        self._isagregated = isagregated
    def delIsagregated(self): self._isagregated = None
    # Properties
    isagregated = property(getIsagregated, setIsagregated, delIsagregated, "Property for isagregated")
    def export(self, outfile, level, name_='XSDataAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoRg'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._filename is not None:
            self.filename.export(outfile, level, name_='filename')
        else:
            warnEmptyAttribute("filename", "XSDataFile")
        if self._rg is not None:
            self.rg.export(outfile, level, name_='rg')
        else:
            warnEmptyAttribute("rg", "XSDataLength")
        if self._rgStdev is not None:
            self.rgStdev.export(outfile, level, name_='rgStdev')
        else:
            warnEmptyAttribute("rgStdev", "XSDataLength")
        if self._i0 is not None:
            self.i0.export(outfile, level, name_='i0')
        else:
            warnEmptyAttribute("i0", "XSDataDouble")
        if self._i0Stdev is not None:
            self.i0Stdev.export(outfile, level, name_='i0Stdev')
        else:
            warnEmptyAttribute("i0Stdev", "XSDataDouble")
        if self._firstPointUsed is not None:
            self.firstPointUsed.export(outfile, level, name_='firstPointUsed')
        else:
            warnEmptyAttribute("firstPointUsed", "XSDataInteger")
        if self._lastPointUsed is not None:
            self.lastPointUsed.export(outfile, level, name_='lastPointUsed')
        else:
            warnEmptyAttribute("lastPointUsed", "XSDataInteger")
        if self._quality is not None:
            self.quality.export(outfile, level, name_='quality')
        else:
            warnEmptyAttribute("quality", "XSDataDouble")
        if self._isagregated is not None:
            self.isagregated.export(outfile, level, name_='isagregated')
        else:
            warnEmptyAttribute("isagregated", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filename':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFilename(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rg':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgStdev':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgStdev(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i0':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setI0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i0Stdev':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setI0Stdev(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstPointUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFirstPointUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lastPointUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLastPointUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'quality':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isagregated':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setIsagregated(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoRg

class XSDataBioSaxsExperimentSetup(XSData):
    def __init__(self, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
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
    def __init__(self, temperature=None, code=None, comments=None, concentration=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", concentration, "XSDataDouble")
        self._concentration = concentration
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", comments, "XSDataString")
        self._comments = comments
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", code, "XSDataString")
        self._code = code
        checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", temperature, "XSDataDouble")
        self._temperature = temperature
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
    def getTemperature(self): return self._temperature
    def setTemperature(self, temperature):
        checkType("XSDataBioSaxsSample", "setTemperature", temperature, "XSDataDouble")
        self._temperature = temperature
    def delTemperature(self): self._temperature = None
    # Properties
    temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
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
        if self._temperature is not None:
            self.temperature.export(outfile, level, name_='temperature')
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'temperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTemperature(obj_)
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

class XSDataConfigGnom(XSData):
    def __init__(self, nextjob=None, rad56=None, coef=None, nreal=None, alpha=None, spot2=None, spot1=None, lw2=None, aw2=None, lh2=None, ah2=None, lw1=None, aw1=None, lh1=None, ah1=None, fwhm2=None, fwhm1=None, idet=None, deviat=None, kernel=None, lzrmax=None, lzrmin=None, rmax=None, rmin=None, jobtyp=None, lkern=None, ploerr=None, evaerr=None, plores=None, plonp=None, iscale=None, output=None, nskip2=None, nskip1=None, input2=None, input1=None, expert=None, forfac=None, printer=None):
        XSData.__init__(self, )
    
    
        if printer is None:
            self._printer = []
        else:
            checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", printer, "list")
            self._printer = printer
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", forfac, "XSDataFile")
        self._forfac = forfac
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", expert, "XSDataFile")
        self._expert = expert
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", input1, "XSDataFile")
        self._input1 = input1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", input2, "XSDataFile")
        self._input2 = input2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nskip1, "XSDataInteger")
        self._nskip1 = nskip1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nskip2, "XSDataInteger")
        self._nskip2 = nskip2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", output, "XSDataFile")
        self._output = output
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", iscale, "XSDataInteger")
        self._iscale = iscale
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", plonp, "XSDataBoolean")
        self._plonp = plonp
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", plores, "XSDataBoolean")
        self._plores = plores
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", evaerr, "XSDataBoolean")
        self._evaerr = evaerr
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ploerr, "XSDataBoolean")
        self._ploerr = ploerr
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lkern, "XSDataBoolean")
        self._lkern = lkern
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", jobtyp, "XSDataInteger")
        self._jobtyp = jobtyp
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rmin, "XSDataDouble")
        self._rmin = rmin
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rmax, "XSDataDouble")
        self._rmax = rmax
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lzrmin, "XSDataBoolean")
        self._lzrmin = lzrmin
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lzrmax, "XSDataBoolean")
        self._lzrmax = lzrmax
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", kernel, "XSDataFile")
        self._kernel = kernel
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", deviat, "XSDataDouble")
        self._deviat = deviat
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", idet, "XSDataInteger")
        self._idet = idet
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", fwhm1, "XSDataDouble")
        self._fwhm1 = fwhm1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", fwhm2, "XSDataDouble")
        self._fwhm2 = fwhm2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ah1, "XSDataDouble")
        self._ah1 = ah1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lh1, "XSDataDouble")
        self._lh1 = lh1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", aw1, "XSDataDouble")
        self._aw1 = aw1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lw1, "XSDataDouble")
        self._lw1 = lw1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ah2, "XSDataDouble")
        self._ah2 = ah2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lh2, "XSDataDouble")
        self._lh2 = lh2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", aw2, "XSDataDouble")
        self._aw2 = aw2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lw2, "XSDataDouble")
        self._lw2 = lw2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", spot1, "XSDataFile")
        self._spot1 = spot1
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", spot2, "XSDataFile")
        self._spot2 = spot2
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", alpha, "XSDataDouble")
        self._alpha = alpha
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nreal, "XSDataInteger")
        self._nreal = nreal
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", coef, "XSDataDouble")
        self._coef = coef
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rad56, "XSDataDouble")
        self._rad56 = rad56
        checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nextjob, "XSDataBoolean")
        self._nextjob = nextjob
    def getPrinter(self): return self._printer
    def setPrinter(self, printer):
        checkType("XSDataConfigGnom", "setPrinter", printer, "list")
        self._printer = printer
    def delPrinter(self): self._printer = None
    # Properties
    printer = property(getPrinter, setPrinter, delPrinter, "Property for printer")
    def addPrinter(self, value):
        checkType("XSDataConfigGnom", "setPrinter", value, "XSDataString")
        self._printer.append(value)
    def insertPrinter(self, index, value):
        checkType("XSDataConfigGnom", "setPrinter", value, "XSDataString")
        self._printer[index] = value
    def getForfac(self): return self._forfac
    def setForfac(self, forfac):
        checkType("XSDataConfigGnom", "setForfac", forfac, "XSDataFile")
        self._forfac = forfac
    def delForfac(self): self._forfac = None
    # Properties
    forfac = property(getForfac, setForfac, delForfac, "Property for forfac")
    def getExpert(self): return self._expert
    def setExpert(self, expert):
        checkType("XSDataConfigGnom", "setExpert", expert, "XSDataFile")
        self._expert = expert
    def delExpert(self): self._expert = None
    # Properties
    expert = property(getExpert, setExpert, delExpert, "Property for expert")
    def getInput1(self): return self._input1
    def setInput1(self, input1):
        checkType("XSDataConfigGnom", "setInput1", input1, "XSDataFile")
        self._input1 = input1
    def delInput1(self): self._input1 = None
    # Properties
    input1 = property(getInput1, setInput1, delInput1, "Property for input1")
    def getInput2(self): return self._input2
    def setInput2(self, input2):
        checkType("XSDataConfigGnom", "setInput2", input2, "XSDataFile")
        self._input2 = input2
    def delInput2(self): self._input2 = None
    # Properties
    input2 = property(getInput2, setInput2, delInput2, "Property for input2")
    def getNskip1(self): return self._nskip1
    def setNskip1(self, nskip1):
        checkType("XSDataConfigGnom", "setNskip1", nskip1, "XSDataInteger")
        self._nskip1 = nskip1
    def delNskip1(self): self._nskip1 = None
    # Properties
    nskip1 = property(getNskip1, setNskip1, delNskip1, "Property for nskip1")
    def getNskip2(self): return self._nskip2
    def setNskip2(self, nskip2):
        checkType("XSDataConfigGnom", "setNskip2", nskip2, "XSDataInteger")
        self._nskip2 = nskip2
    def delNskip2(self): self._nskip2 = None
    # Properties
    nskip2 = property(getNskip2, setNskip2, delNskip2, "Property for nskip2")
    def getOutput(self): return self._output
    def setOutput(self, output):
        checkType("XSDataConfigGnom", "setOutput", output, "XSDataFile")
        self._output = output
    def delOutput(self): self._output = None
    # Properties
    output = property(getOutput, setOutput, delOutput, "Property for output")
    def getIscale(self): return self._iscale
    def setIscale(self, iscale):
        checkType("XSDataConfigGnom", "setIscale", iscale, "XSDataInteger")
        self._iscale = iscale
    def delIscale(self): self._iscale = None
    # Properties
    iscale = property(getIscale, setIscale, delIscale, "Property for iscale")
    def getPlonp(self): return self._plonp
    def setPlonp(self, plonp):
        checkType("XSDataConfigGnom", "setPlonp", plonp, "XSDataBoolean")
        self._plonp = plonp
    def delPlonp(self): self._plonp = None
    # Properties
    plonp = property(getPlonp, setPlonp, delPlonp, "Property for plonp")
    def getPlores(self): return self._plores
    def setPlores(self, plores):
        checkType("XSDataConfigGnom", "setPlores", plores, "XSDataBoolean")
        self._plores = plores
    def delPlores(self): self._plores = None
    # Properties
    plores = property(getPlores, setPlores, delPlores, "Property for plores")
    def getEvaerr(self): return self._evaerr
    def setEvaerr(self, evaerr):
        checkType("XSDataConfigGnom", "setEvaerr", evaerr, "XSDataBoolean")
        self._evaerr = evaerr
    def delEvaerr(self): self._evaerr = None
    # Properties
    evaerr = property(getEvaerr, setEvaerr, delEvaerr, "Property for evaerr")
    def getPloerr(self): return self._ploerr
    def setPloerr(self, ploerr):
        checkType("XSDataConfigGnom", "setPloerr", ploerr, "XSDataBoolean")
        self._ploerr = ploerr
    def delPloerr(self): self._ploerr = None
    # Properties
    ploerr = property(getPloerr, setPloerr, delPloerr, "Property for ploerr")
    def getLkern(self): return self._lkern
    def setLkern(self, lkern):
        checkType("XSDataConfigGnom", "setLkern", lkern, "XSDataBoolean")
        self._lkern = lkern
    def delLkern(self): self._lkern = None
    # Properties
    lkern = property(getLkern, setLkern, delLkern, "Property for lkern")
    def getJobtyp(self): return self._jobtyp
    def setJobtyp(self, jobtyp):
        checkType("XSDataConfigGnom", "setJobtyp", jobtyp, "XSDataInteger")
        self._jobtyp = jobtyp
    def delJobtyp(self): self._jobtyp = None
    # Properties
    jobtyp = property(getJobtyp, setJobtyp, delJobtyp, "Property for jobtyp")
    def getRmin(self): return self._rmin
    def setRmin(self, rmin):
        checkType("XSDataConfigGnom", "setRmin", rmin, "XSDataDouble")
        self._rmin = rmin
    def delRmin(self): self._rmin = None
    # Properties
    rmin = property(getRmin, setRmin, delRmin, "Property for rmin")
    def getRmax(self): return self._rmax
    def setRmax(self, rmax):
        checkType("XSDataConfigGnom", "setRmax", rmax, "XSDataDouble")
        self._rmax = rmax
    def delRmax(self): self._rmax = None
    # Properties
    rmax = property(getRmax, setRmax, delRmax, "Property for rmax")
    def getLzrmin(self): return self._lzrmin
    def setLzrmin(self, lzrmin):
        checkType("XSDataConfigGnom", "setLzrmin", lzrmin, "XSDataBoolean")
        self._lzrmin = lzrmin
    def delLzrmin(self): self._lzrmin = None
    # Properties
    lzrmin = property(getLzrmin, setLzrmin, delLzrmin, "Property for lzrmin")
    def getLzrmax(self): return self._lzrmax
    def setLzrmax(self, lzrmax):
        checkType("XSDataConfigGnom", "setLzrmax", lzrmax, "XSDataBoolean")
        self._lzrmax = lzrmax
    def delLzrmax(self): self._lzrmax = None
    # Properties
    lzrmax = property(getLzrmax, setLzrmax, delLzrmax, "Property for lzrmax")
    def getKernel(self): return self._kernel
    def setKernel(self, kernel):
        checkType("XSDataConfigGnom", "setKernel", kernel, "XSDataFile")
        self._kernel = kernel
    def delKernel(self): self._kernel = None
    # Properties
    kernel = property(getKernel, setKernel, delKernel, "Property for kernel")
    def getDeviat(self): return self._deviat
    def setDeviat(self, deviat):
        checkType("XSDataConfigGnom", "setDeviat", deviat, "XSDataDouble")
        self._deviat = deviat
    def delDeviat(self): self._deviat = None
    # Properties
    deviat = property(getDeviat, setDeviat, delDeviat, "Property for deviat")
    def getIdet(self): return self._idet
    def setIdet(self, idet):
        checkType("XSDataConfigGnom", "setIdet", idet, "XSDataInteger")
        self._idet = idet
    def delIdet(self): self._idet = None
    # Properties
    idet = property(getIdet, setIdet, delIdet, "Property for idet")
    def getFwhm1(self): return self._fwhm1
    def setFwhm1(self, fwhm1):
        checkType("XSDataConfigGnom", "setFwhm1", fwhm1, "XSDataDouble")
        self._fwhm1 = fwhm1
    def delFwhm1(self): self._fwhm1 = None
    # Properties
    fwhm1 = property(getFwhm1, setFwhm1, delFwhm1, "Property for fwhm1")
    def getFwhm2(self): return self._fwhm2
    def setFwhm2(self, fwhm2):
        checkType("XSDataConfigGnom", "setFwhm2", fwhm2, "XSDataDouble")
        self._fwhm2 = fwhm2
    def delFwhm2(self): self._fwhm2 = None
    # Properties
    fwhm2 = property(getFwhm2, setFwhm2, delFwhm2, "Property for fwhm2")
    def getAh1(self): return self._ah1
    def setAh1(self, ah1):
        checkType("XSDataConfigGnom", "setAh1", ah1, "XSDataDouble")
        self._ah1 = ah1
    def delAh1(self): self._ah1 = None
    # Properties
    ah1 = property(getAh1, setAh1, delAh1, "Property for ah1")
    def getLh1(self): return self._lh1
    def setLh1(self, lh1):
        checkType("XSDataConfigGnom", "setLh1", lh1, "XSDataDouble")
        self._lh1 = lh1
    def delLh1(self): self._lh1 = None
    # Properties
    lh1 = property(getLh1, setLh1, delLh1, "Property for lh1")
    def getAw1(self): return self._aw1
    def setAw1(self, aw1):
        checkType("XSDataConfigGnom", "setAw1", aw1, "XSDataDouble")
        self._aw1 = aw1
    def delAw1(self): self._aw1 = None
    # Properties
    aw1 = property(getAw1, setAw1, delAw1, "Property for aw1")
    def getLw1(self): return self._lw1
    def setLw1(self, lw1):
        checkType("XSDataConfigGnom", "setLw1", lw1, "XSDataDouble")
        self._lw1 = lw1
    def delLw1(self): self._lw1 = None
    # Properties
    lw1 = property(getLw1, setLw1, delLw1, "Property for lw1")
    def getAh2(self): return self._ah2
    def setAh2(self, ah2):
        checkType("XSDataConfigGnom", "setAh2", ah2, "XSDataDouble")
        self._ah2 = ah2
    def delAh2(self): self._ah2 = None
    # Properties
    ah2 = property(getAh2, setAh2, delAh2, "Property for ah2")
    def getLh2(self): return self._lh2
    def setLh2(self, lh2):
        checkType("XSDataConfigGnom", "setLh2", lh2, "XSDataDouble")
        self._lh2 = lh2
    def delLh2(self): self._lh2 = None
    # Properties
    lh2 = property(getLh2, setLh2, delLh2, "Property for lh2")
    def getAw2(self): return self._aw2
    def setAw2(self, aw2):
        checkType("XSDataConfigGnom", "setAw2", aw2, "XSDataDouble")
        self._aw2 = aw2
    def delAw2(self): self._aw2 = None
    # Properties
    aw2 = property(getAw2, setAw2, delAw2, "Property for aw2")
    def getLw2(self): return self._lw2
    def setLw2(self, lw2):
        checkType("XSDataConfigGnom", "setLw2", lw2, "XSDataDouble")
        self._lw2 = lw2
    def delLw2(self): self._lw2 = None
    # Properties
    lw2 = property(getLw2, setLw2, delLw2, "Property for lw2")
    def getSpot1(self): return self._spot1
    def setSpot1(self, spot1):
        checkType("XSDataConfigGnom", "setSpot1", spot1, "XSDataFile")
        self._spot1 = spot1
    def delSpot1(self): self._spot1 = None
    # Properties
    spot1 = property(getSpot1, setSpot1, delSpot1, "Property for spot1")
    def getSpot2(self): return self._spot2
    def setSpot2(self, spot2):
        checkType("XSDataConfigGnom", "setSpot2", spot2, "XSDataFile")
        self._spot2 = spot2
    def delSpot2(self): self._spot2 = None
    # Properties
    spot2 = property(getSpot2, setSpot2, delSpot2, "Property for spot2")
    def getAlpha(self): return self._alpha
    def setAlpha(self, alpha):
        checkType("XSDataConfigGnom", "setAlpha", alpha, "XSDataDouble")
        self._alpha = alpha
    def delAlpha(self): self._alpha = None
    # Properties
    alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
    def getNreal(self): return self._nreal
    def setNreal(self, nreal):
        checkType("XSDataConfigGnom", "setNreal", nreal, "XSDataInteger")
        self._nreal = nreal
    def delNreal(self): self._nreal = None
    # Properties
    nreal = property(getNreal, setNreal, delNreal, "Property for nreal")
    def getCoef(self): return self._coef
    def setCoef(self, coef):
        checkType("XSDataConfigGnom", "setCoef", coef, "XSDataDouble")
        self._coef = coef
    def delCoef(self): self._coef = None
    # Properties
    coef = property(getCoef, setCoef, delCoef, "Property for coef")
    def getRad56(self): return self._rad56
    def setRad56(self, rad56):
        checkType("XSDataConfigGnom", "setRad56", rad56, "XSDataDouble")
        self._rad56 = rad56
    def delRad56(self): self._rad56 = None
    # Properties
    rad56 = property(getRad56, setRad56, delRad56, "Property for rad56")
    def getNextjob(self): return self._nextjob
    def setNextjob(self, nextjob):
        checkType("XSDataConfigGnom", "setNextjob", nextjob, "XSDataBoolean")
        self._nextjob = nextjob
    def delNextjob(self): self._nextjob = None
    # Properties
    nextjob = property(getNextjob, setNextjob, delNextjob, "Property for nextjob")
    def export(self, outfile, level, name_='XSDataConfigGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataConfigGnom'):
        XSData.exportChildren(self, outfile, level, name_)
        for printer_ in self.getPrinter():
            printer_.export(outfile, level, name_='printer')
        if self._forfac is not None:
            self.forfac.export(outfile, level, name_='forfac')
        if self._expert is not None:
            self.expert.export(outfile, level, name_='expert')
        if self._input1 is not None:
            self.input1.export(outfile, level, name_='input1')
        else:
            warnEmptyAttribute("input1", "XSDataFile")
        if self._input2 is not None:
            self.input2.export(outfile, level, name_='input2')
        if self._nskip1 is not None:
            self.nskip1.export(outfile, level, name_='nskip1')
        if self._nskip2 is not None:
            self.nskip2.export(outfile, level, name_='nskip2')
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
        if self._iscale is not None:
            self.iscale.export(outfile, level, name_='iscale')
        if self._plonp is not None:
            self.plonp.export(outfile, level, name_='plonp')
        else:
            warnEmptyAttribute("plonp", "XSDataBoolean")
        if self._plores is not None:
            self.plores.export(outfile, level, name_='plores')
        else:
            warnEmptyAttribute("plores", "XSDataBoolean")
        if self._evaerr is not None:
            self.evaerr.export(outfile, level, name_='evaerr')
        if self._ploerr is not None:
            self.ploerr.export(outfile, level, name_='ploerr')
        else:
            warnEmptyAttribute("ploerr", "XSDataBoolean")
        if self._lkern is not None:
            self.lkern.export(outfile, level, name_='lkern')
        if self._jobtyp is not None:
            self.jobtyp.export(outfile, level, name_='jobtyp')
        if self._rmin is not None:
            self.rmin.export(outfile, level, name_='rmin')
        if self._rmax is not None:
            self.rmax.export(outfile, level, name_='rmax')
        if self._lzrmin is not None:
            self.lzrmin.export(outfile, level, name_='lzrmin')
        if self._lzrmax is not None:
            self.lzrmax.export(outfile, level, name_='lzrmax')
        if self._kernel is not None:
            self.kernel.export(outfile, level, name_='kernel')
        if self._deviat is not None:
            self.deviat.export(outfile, level, name_='deviat')
        else:
            warnEmptyAttribute("deviat", "XSDataDouble")
        if self._idet is not None:
            self.idet.export(outfile, level, name_='idet')
        if self._fwhm1 is not None:
            self.fwhm1.export(outfile, level, name_='fwhm1')
        if self._fwhm2 is not None:
            self.fwhm2.export(outfile, level, name_='fwhm2')
        if self._ah1 is not None:
            self.ah1.export(outfile, level, name_='ah1')
        if self._lh1 is not None:
            self.lh1.export(outfile, level, name_='lh1')
        if self._aw1 is not None:
            self.aw1.export(outfile, level, name_='aw1')
        if self._lw1 is not None:
            self.lw1.export(outfile, level, name_='lw1')
        if self._ah2 is not None:
            self.ah2.export(outfile, level, name_='ah2')
        if self._lh2 is not None:
            self.lh2.export(outfile, level, name_='lh2')
        if self._aw2 is not None:
            self.aw2.export(outfile, level, name_='aw2')
        if self._lw2 is not None:
            self.lw2.export(outfile, level, name_='lw2')
        if self._spot1 is not None:
            self.spot1.export(outfile, level, name_='spot1')
        if self._spot2 is not None:
            self.spot2.export(outfile, level, name_='spot2')
        if self._alpha is not None:
            self.alpha.export(outfile, level, name_='alpha')
        else:
            warnEmptyAttribute("alpha", "XSDataDouble")
        if self._nreal is not None:
            self.nreal.export(outfile, level, name_='nreal')
        else:
            warnEmptyAttribute("nreal", "XSDataInteger")
        if self._coef is not None:
            self.coef.export(outfile, level, name_='coef')
        if self._rad56 is not None:
            self.rad56.export(outfile, level, name_='rad56')
        if self._nextjob is not None:
            self.nextjob.export(outfile, level, name_='nextjob')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'printer':
            obj_ = XSDataString()
            obj_.build(child_)
            self.printer.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forfac':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForfac(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expert':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setExpert(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input1':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input2':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip1':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNskip1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip2':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNskip2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iscale':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIscale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plonp':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPlonp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plores':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPlores(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'evaerr':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setEvaerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ploerr':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPloerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lkern':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLkern(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jobtyp':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setJobtyp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmin':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmin':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLzrmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmax':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLzrmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kernel':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setKernel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deviat':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDeviat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'idet':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIdet(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFwhm1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFwhm2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot1':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSpot1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot2':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSpot2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'alpha':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAlpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nreal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNreal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coef':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCoef(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rad56':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRad56(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nextjob':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setNextjob(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataConfigGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataConfigGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataConfigGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataConfigGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataConfigGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataConfigGnom

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

class XSDataGnom(XSData):
    def __init__(self, total=None, dmax=None, rgGnom=None, rgGuinier=None, gnomFile=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataGnom", "Constructor of XSDataGnom", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
        checkType("XSDataGnom", "Constructor of XSDataGnom", rgGuinier, "XSDataLength")
        self._rgGuinier = rgGuinier
        checkType("XSDataGnom", "Constructor of XSDataGnom", rgGnom, "XSDataLength")
        self._rgGnom = rgGnom
        checkType("XSDataGnom", "Constructor of XSDataGnom", dmax, "XSDataLength")
        self._dmax = dmax
        checkType("XSDataGnom", "Constructor of XSDataGnom", total, "XSDataDouble")
        self._total = total
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        checkType("XSDataGnom", "setGnomFile", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def delGnomFile(self): self._gnomFile = None
    # Properties
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    def getRgGuinier(self): return self._rgGuinier
    def setRgGuinier(self, rgGuinier):
        checkType("XSDataGnom", "setRgGuinier", rgGuinier, "XSDataLength")
        self._rgGuinier = rgGuinier
    def delRgGuinier(self): self._rgGuinier = None
    # Properties
    rgGuinier = property(getRgGuinier, setRgGuinier, delRgGuinier, "Property for rgGuinier")
    def getRgGnom(self): return self._rgGnom
    def setRgGnom(self, rgGnom):
        checkType("XSDataGnom", "setRgGnom", rgGnom, "XSDataLength")
        self._rgGnom = rgGnom
    def delRgGnom(self): self._rgGnom = None
    # Properties
    rgGnom = property(getRgGnom, setRgGnom, delRgGnom, "Property for rgGnom")
    def getDmax(self): return self._dmax
    def setDmax(self, dmax):
        checkType("XSDataGnom", "setDmax", dmax, "XSDataLength")
        self._dmax = dmax
    def delDmax(self): self._dmax = None
    # Properties
    dmax = property(getDmax, setDmax, delDmax, "Property for dmax")
    def getTotal(self): return self._total
    def setTotal(self, total):
        checkType("XSDataGnom", "setTotal", total, "XSDataDouble")
        self._total = total
    def delTotal(self): self._total = None
    # Properties
    total = property(getTotal, setTotal, delTotal, "Property for total")
    def export(self, outfile, level, name_='XSDataGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataGnom'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        else:
            warnEmptyAttribute("gnomFile", "XSDataFile")
        if self._rgGuinier is not None:
            self.rgGuinier.export(outfile, level, name_='rgGuinier')
        else:
            warnEmptyAttribute("rgGuinier", "XSDataLength")
        if self._rgGnom is not None:
            self.rgGnom.export(outfile, level, name_='rgGnom')
        else:
            warnEmptyAttribute("rgGnom", "XSDataLength")
        if self._dmax is not None:
            self.dmax.export(outfile, level, name_='dmax')
        else:
            warnEmptyAttribute("dmax", "XSDataLength")
        if self._total is not None:
            self.total.export(outfile, level, name_='total')
        else:
            warnEmptyAttribute("total", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgGuinier':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgGuinier(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgGnom':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dmax':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotal(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataGnom

class XSDataSaxsSample(XSData):
    """Everything describing the sample"""
    def __init__(self, code=None, comment=None, name=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", name, "XSDataString")
        self._name = name
        checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", comment, "XSDataString")
        self._comment = comment
        checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", code, "XSDataString")
        self._code = code
    def getName(self): return self._name
    def setName(self, name):
        checkType("XSDataSaxsSample", "setName", name, "XSDataString")
        self._name = name
    def delName(self): self._name = None
    # Properties
    name = property(getName, setName, delName, "Property for name")
    def getComment(self): return self._comment
    def setComment(self, comment):
        checkType("XSDataSaxsSample", "setComment", comment, "XSDataString")
        self._comment = comment
    def delComment(self): self._comment = None
    # Properties
    comment = property(getComment, setComment, delComment, "Property for comment")
    def getCode(self): return self._code
    def setCode(self, code):
        checkType("XSDataSaxsSample", "setCode", code, "XSDataString")
        self._code = code
    def delCode(self): self._code = None
    # Properties
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='XSDataSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSaxsSample'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        if self._comment is not None:
            self.comment.export(outfile, level, name_='comment')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComment(obj_)
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
        self.export( oStreamString, 0, name_="XSDataSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSaxsSample

class XSDataSaxsSeries(XSData):
    """Basical"""
    def __init__(self, concentration=None, curve=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataSaxsSeries", "Constructor of XSDataSaxsSeries", curve, "XSDataFile")
        self._curve = curve
        checkType("XSDataSaxsSeries", "Constructor of XSDataSaxsSeries", concentration, "XSDataDouble")
        self._concentration = concentration
    def getCurve(self): return self._curve
    def setCurve(self, curve):
        checkType("XSDataSaxsSeries", "setCurve", curve, "XSDataFile")
        self._curve = curve
    def delCurve(self): self._curve = None
    # Properties
    curve = property(getCurve, setCurve, delCurve, "Property for curve")
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        checkType("XSDataSaxsSeries", "setConcentration", concentration, "XSDataDouble")
        self._concentration = concentration
    def delConcentration(self): self._concentration = None
    # Properties
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    def export(self, outfile, level, name_='XSDataSaxsSeries'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSaxsSeries'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._curve is not None:
            self.curve.export(outfile, level, name_='curve')
        else:
            warnEmptyAttribute("curve", "XSDataFile")
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'curve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSaxsSeries" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSaxsSeries' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSaxsSeries is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSaxsSeries.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSaxsSeries" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSeries()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSaxsSeries

class XSDataInputAutoRg(XSDataInput):
    def __init__(self, configuration=None, maxSminRg=None, maxSmaxRg=None, minIntervalLength=None, inputCurve=None, sample=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", sample, "XSDataSaxsSample")
        self._sample = sample
        if inputCurve is None:
            self._inputCurve = []
        else:
            checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", inputCurve, "list")
            self._inputCurve = inputCurve
        checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", minIntervalLength, "XSDataInteger")
        self._minIntervalLength = minIntervalLength
        checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", maxSmaxRg, "XSDataDouble")
        self._maxSmaxRg = maxSmaxRg
        checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", maxSminRg, "XSDataDouble")
        self._maxSminRg = maxSminRg
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputAutoRg", "setSample", sample, "XSDataSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        checkType("XSDataInputAutoRg", "setInputCurve", inputCurve, "list")
        self._inputCurve = inputCurve
    def delInputCurve(self): self._inputCurve = None
    # Properties
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        checkType("XSDataInputAutoRg", "setInputCurve", value, "XSDataFile")
        self._inputCurve.append(value)
    def insertInputCurve(self, index, value):
        checkType("XSDataInputAutoRg", "setInputCurve", value, "XSDataFile")
        self._inputCurve[index] = value
    def getMinIntervalLength(self): return self._minIntervalLength
    def setMinIntervalLength(self, minIntervalLength):
        checkType("XSDataInputAutoRg", "setMinIntervalLength", minIntervalLength, "XSDataInteger")
        self._minIntervalLength = minIntervalLength
    def delMinIntervalLength(self): self._minIntervalLength = None
    # Properties
    minIntervalLength = property(getMinIntervalLength, setMinIntervalLength, delMinIntervalLength, "Property for minIntervalLength")
    def getMaxSmaxRg(self): return self._maxSmaxRg
    def setMaxSmaxRg(self, maxSmaxRg):
        checkType("XSDataInputAutoRg", "setMaxSmaxRg", maxSmaxRg, "XSDataDouble")
        self._maxSmaxRg = maxSmaxRg
    def delMaxSmaxRg(self): self._maxSmaxRg = None
    # Properties
    maxSmaxRg = property(getMaxSmaxRg, setMaxSmaxRg, delMaxSmaxRg, "Property for maxSmaxRg")
    def getMaxSminRg(self): return self._maxSminRg
    def setMaxSminRg(self, maxSminRg):
        checkType("XSDataInputAutoRg", "setMaxSminRg", maxSminRg, "XSDataDouble")
        self._maxSminRg = maxSminRg
    def delMaxSminRg(self): self._maxSminRg = None
    # Properties
    maxSminRg = property(getMaxSminRg, setMaxSminRg, delMaxSminRg, "Property for maxSminRg")
    def export(self, outfile, level, name_='XSDataInputAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputAutoRg'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._minIntervalLength is not None:
            self.minIntervalLength.export(outfile, level, name_='minIntervalLength')
        if self._maxSmaxRg is not None:
            self.maxSmaxRg.export(outfile, level, name_='maxSmaxRg')
        if self._maxSminRg is not None:
            self.maxSminRg.export(outfile, level, name_='maxSminRg')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minIntervalLength':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMinIntervalLength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxSmaxRg':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxSmaxRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxSminRg':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxSminRg(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputAutoRg

class XSDataInputAutoSub(XSDataInput):
    """Autosub works by default in sampleCurve directory """
    def __init__(self, configuration=None, subtractedCurve=None, sampleCurve=None, buffers=None):
        XSDataInput.__init__(self, configuration)
    
    
        if buffers is None:
            self._buffers = []
        else:
            checkType("XSDataInputAutoSub", "Constructor of XSDataInputAutoSub", buffers, "list")
            self._buffers = buffers
        checkType("XSDataInputAutoSub", "Constructor of XSDataInputAutoSub", sampleCurve, "XSDataFile")
        self._sampleCurve = sampleCurve
        checkType("XSDataInputAutoSub", "Constructor of XSDataInputAutoSub", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def getBuffers(self): return self._buffers
    def setBuffers(self, buffers):
        checkType("XSDataInputAutoSub", "setBuffers", buffers, "list")
        self._buffers = buffers
    def delBuffers(self): self._buffers = None
    # Properties
    buffers = property(getBuffers, setBuffers, delBuffers, "Property for buffers")
    def addBuffers(self, value):
        checkType("XSDataInputAutoSub", "setBuffers", value, "XSDataFile")
        self._buffers.append(value)
    def insertBuffers(self, index, value):
        checkType("XSDataInputAutoSub", "setBuffers", value, "XSDataFile")
        self._buffers[index] = value
    def getSampleCurve(self): return self._sampleCurve
    def setSampleCurve(self, sampleCurve):
        checkType("XSDataInputAutoSub", "setSampleCurve", sampleCurve, "XSDataFile")
        self._sampleCurve = sampleCurve
    def delSampleCurve(self): self._sampleCurve = None
    # Properties
    sampleCurve = property(getSampleCurve, setSampleCurve, delSampleCurve, "Property for sampleCurve")
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataInputAutoSub", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def export(self, outfile, level, name_='XSDataInputAutoSub'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputAutoSub'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for buffers_ in self.getBuffers():
            buffers_.export(outfile, level, name_='buffers')
        if self.getBuffers() == []:
            warnEmptyAttribute("buffers", "XSDataFile")
        if self._sampleCurve is not None:
            self.sampleCurve.export(outfile, level, name_='sampleCurve')
        else:
            warnEmptyAttribute("sampleCurve", "XSDataFile")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'buffers':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.buffers.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sampleCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSampleCurve(obj_)
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
        self.export( oStreamString, 0, name_="XSDataInputAutoSub" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputAutoSub' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputAutoSub is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputAutoSub.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoSub()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputAutoSub" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoSub()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputAutoSub

class XSDataInputDamaver(XSDataInput):
    def __init__(self, configuration=None, automatic=None, symmetry=None, pdbInputFiles=None):
        XSDataInput.__init__(self, configuration)
    
    
        if pdbInputFiles is None:
            self._pdbInputFiles = []
        else:
            checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", pdbInputFiles, "list")
            self._pdbInputFiles = pdbInputFiles
        checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", symmetry, "XSDataString")
        self._symmetry = symmetry
        checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", automatic, "XSDataBoolean")
        self._automatic = automatic
    def getPdbInputFiles(self): return self._pdbInputFiles
    def setPdbInputFiles(self, pdbInputFiles):
        checkType("XSDataInputDamaver", "setPdbInputFiles", pdbInputFiles, "list")
        self._pdbInputFiles = pdbInputFiles
    def delPdbInputFiles(self): self._pdbInputFiles = None
    # Properties
    pdbInputFiles = property(getPdbInputFiles, setPdbInputFiles, delPdbInputFiles, "Property for pdbInputFiles")
    def addPdbInputFiles(self, value):
        checkType("XSDataInputDamaver", "setPdbInputFiles", value, "XSDataFile")
        self._pdbInputFiles.append(value)
    def insertPdbInputFiles(self, index, value):
        checkType("XSDataInputDamaver", "setPdbInputFiles", value, "XSDataFile")
        self._pdbInputFiles[index] = value
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        checkType("XSDataInputDamaver", "setSymmetry", symmetry, "XSDataString")
        self._symmetry = symmetry
    def delSymmetry(self): self._symmetry = None
    # Properties
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    def getAutomatic(self): return self._automatic
    def setAutomatic(self, automatic):
        checkType("XSDataInputDamaver", "setAutomatic", automatic, "XSDataBoolean")
        self._automatic = automatic
    def delAutomatic(self): self._automatic = None
    # Properties
    automatic = property(getAutomatic, setAutomatic, delAutomatic, "Property for automatic")
    def export(self, outfile, level, name_='XSDataInputDamaver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamaver'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for pdbInputFiles_ in self.getPdbInputFiles():
            pdbInputFiles_.export(outfile, level, name_='pdbInputFiles')
        if self.getPdbInputFiles() == []:
            warnEmptyAttribute("pdbInputFiles", "XSDataFile")
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self._automatic is not None:
            self.automatic.export(outfile, level, name_='automatic')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbInputFiles':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.pdbInputFiles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'automatic':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAutomatic(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamaver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamaver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamaver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamaver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamaver

class XSDataInputDamfilt(XSDataInput):
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDamfilt", "Constructor of XSDataInputDamfilt", inputPdbFile, "XSDataFile")
        self._inputPdbFile = inputPdbFile
    def getInputPdbFile(self): return self._inputPdbFile
    def setInputPdbFile(self, inputPdbFile):
        checkType("XSDataInputDamfilt", "setInputPdbFile", inputPdbFile, "XSDataFile")
        self._inputPdbFile = inputPdbFile
    def delInputPdbFile(self): self._inputPdbFile = None
    # Properties
    inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
    def export(self, outfile, level, name_='XSDataInputDamfilt'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamfilt'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputPdbFile is not None:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        else:
            warnEmptyAttribute("inputPdbFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamfilt' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamfilt is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamfilt.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamfilt" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamfilt

class XSDataInputDammif(XSDataInput):
    def __init__(self, configuration=None, constant=None, chained=None, mode=None, symmetry=None, unit=None, gnomOutputFile=None, expectedParticleShape=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", expectedParticleShape, "XSDataInteger")
        self._expectedParticleShape = expectedParticleShape
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", gnomOutputFile, "XSDataFile")
        self._gnomOutputFile = gnomOutputFile
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", unit, "XSDataString")
        self._unit = unit
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", symmetry, "XSDataString")
        self._symmetry = symmetry
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", mode, "XSDataString")
        self._mode = mode
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", chained, "XSDataBoolean")
        self._chained = chained
        checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", constant, "XSDataDouble")
        self._constant = constant
    def getExpectedParticleShape(self): return self._expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape):
        checkType("XSDataInputDammif", "setExpectedParticleShape", expectedParticleShape, "XSDataInteger")
        self._expectedParticleShape = expectedParticleShape
    def delExpectedParticleShape(self): self._expectedParticleShape = None
    # Properties
    expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
    def getGnomOutputFile(self): return self._gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile):
        checkType("XSDataInputDammif", "setGnomOutputFile", gnomOutputFile, "XSDataFile")
        self._gnomOutputFile = gnomOutputFile
    def delGnomOutputFile(self): self._gnomOutputFile = None
    # Properties
    gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
    def getUnit(self): return self._unit
    def setUnit(self, unit):
        checkType("XSDataInputDammif", "setUnit", unit, "XSDataString")
        self._unit = unit
    def delUnit(self): self._unit = None
    # Properties
    unit = property(getUnit, setUnit, delUnit, "Property for unit")
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        checkType("XSDataInputDammif", "setSymmetry", symmetry, "XSDataString")
        self._symmetry = symmetry
    def delSymmetry(self): self._symmetry = None
    # Properties
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    def getMode(self): return self._mode
    def setMode(self, mode):
        checkType("XSDataInputDammif", "setMode", mode, "XSDataString")
        self._mode = mode
    def delMode(self): self._mode = None
    # Properties
    mode = property(getMode, setMode, delMode, "Property for mode")
    def getChained(self): return self._chained
    def setChained(self, chained):
        checkType("XSDataInputDammif", "setChained", chained, "XSDataBoolean")
        self._chained = chained
    def delChained(self): self._chained = None
    # Properties
    chained = property(getChained, setChained, delChained, "Property for chained")
    def getConstant(self): return self._constant
    def setConstant(self, constant):
        checkType("XSDataInputDammif", "setConstant", constant, "XSDataDouble")
        self._constant = constant
    def delConstant(self): self._constant = None
    # Properties
    constant = property(getConstant, setConstant, delConstant, "Property for constant")
    def export(self, outfile, level, name_='XSDataInputDammif'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDammif'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._expectedParticleShape is not None:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        else:
            warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
        if self._gnomOutputFile is not None:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        else:
            warnEmptyAttribute("gnomOutputFile", "XSDataFile")
        if self._unit is not None:
            self.unit.export(outfile, level, name_='unit')
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        else:
            warnEmptyAttribute("symmetry", "XSDataString")
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
        if self._chained is not None:
            self.chained.export(outfile, level, name_='chained')
        if self._constant is not None:
            self.constant.export(outfile, level, name_='constant')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chained':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setChained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'constant':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConstant(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDammif' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDammif is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDammif.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDammif" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDammif

class XSDataInputDammin(XSDataInput):
    def __init__(self, configuration=None, mode=None, symmetry=None, pdbInputFile=None, initialDummyAtomModel=None, gnomOutputFile=None, expectedParticleShape=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", expectedParticleShape, "XSDataInteger")
        self._expectedParticleShape = expectedParticleShape
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", gnomOutputFile, "XSDataFile")
        self._gnomOutputFile = gnomOutputFile
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", initialDummyAtomModel, "XSDataInteger")
        self._initialDummyAtomModel = initialDummyAtomModel
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", pdbInputFile, "XSDataFile")
        self._pdbInputFile = pdbInputFile
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", symmetry, "XSDataString")
        self._symmetry = symmetry
        checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", mode, "XSDataString")
        self._mode = mode
    def getExpectedParticleShape(self): return self._expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape):
        checkType("XSDataInputDammin", "setExpectedParticleShape", expectedParticleShape, "XSDataInteger")
        self._expectedParticleShape = expectedParticleShape
    def delExpectedParticleShape(self): self._expectedParticleShape = None
    # Properties
    expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
    def getGnomOutputFile(self): return self._gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile):
        checkType("XSDataInputDammin", "setGnomOutputFile", gnomOutputFile, "XSDataFile")
        self._gnomOutputFile = gnomOutputFile
    def delGnomOutputFile(self): self._gnomOutputFile = None
    # Properties
    gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
    def getInitialDummyAtomModel(self): return self._initialDummyAtomModel
    def setInitialDummyAtomModel(self, initialDummyAtomModel):
        checkType("XSDataInputDammin", "setInitialDummyAtomModel", initialDummyAtomModel, "XSDataInteger")
        self._initialDummyAtomModel = initialDummyAtomModel
    def delInitialDummyAtomModel(self): self._initialDummyAtomModel = None
    # Properties
    initialDummyAtomModel = property(getInitialDummyAtomModel, setInitialDummyAtomModel, delInitialDummyAtomModel, "Property for initialDummyAtomModel")
    def getPdbInputFile(self): return self._pdbInputFile
    def setPdbInputFile(self, pdbInputFile):
        checkType("XSDataInputDammin", "setPdbInputFile", pdbInputFile, "XSDataFile")
        self._pdbInputFile = pdbInputFile
    def delPdbInputFile(self): self._pdbInputFile = None
    # Properties
    pdbInputFile = property(getPdbInputFile, setPdbInputFile, delPdbInputFile, "Property for pdbInputFile")
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        checkType("XSDataInputDammin", "setSymmetry", symmetry, "XSDataString")
        self._symmetry = symmetry
    def delSymmetry(self): self._symmetry = None
    # Properties
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    def getMode(self): return self._mode
    def setMode(self, mode):
        checkType("XSDataInputDammin", "setMode", mode, "XSDataString")
        self._mode = mode
    def delMode(self): self._mode = None
    # Properties
    mode = property(getMode, setMode, delMode, "Property for mode")
    def export(self, outfile, level, name_='XSDataInputDammin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDammin'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._expectedParticleShape is not None:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        else:
            warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
        if self._gnomOutputFile is not None:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        else:
            warnEmptyAttribute("gnomOutputFile", "XSDataFile")
        if self._initialDummyAtomModel is not None:
            self.initialDummyAtomModel.export(outfile, level, name_='initialDummyAtomModel')
        else:
            warnEmptyAttribute("initialDummyAtomModel", "XSDataInteger")
        if self._pdbInputFile is not None:
            self.pdbInputFile.export(outfile, level, name_='pdbInputFile')
        else:
            warnEmptyAttribute("pdbInputFile", "XSDataFile")
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        else:
            warnEmptyAttribute("symmetry", "XSDataString")
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialDummyAtomModel':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setInitialDummyAtomModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbInputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbInputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDammin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDammin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDammin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDammin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDammin

class XSDataInputDamstart(XSDataInput):
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDamstart", "Constructor of XSDataInputDamstart", inputPdbFile, "XSDataFile")
        self._inputPdbFile = inputPdbFile
    def getInputPdbFile(self): return self._inputPdbFile
    def setInputPdbFile(self, inputPdbFile):
        checkType("XSDataInputDamstart", "setInputPdbFile", inputPdbFile, "XSDataFile")
        self._inputPdbFile = inputPdbFile
    def delInputPdbFile(self): self._inputPdbFile = None
    # Properties
    inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
    def export(self, outfile, level, name_='XSDataInputDamstart'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamstart'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputPdbFile is not None:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        else:
            warnEmptyAttribute("inputPdbFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamstart' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamstart is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamstart.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamstart" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamstart

class XSDataInputDatGnom(XSDataInput):
    """Input file can be in 1/nm or 1/A, result will be in the same unit."""
    def __init__(self, configuration=None, output=None, skip=None, rg=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDatGnom", "Constructor of XSDataInputDatGnom", inputCurve, "XSDataFile")
        self._inputCurve = inputCurve
        checkType("XSDataInputDatGnom", "Constructor of XSDataInputDatGnom", rg, "XSDataLength")
        self._rg = rg
        checkType("XSDataInputDatGnom", "Constructor of XSDataInputDatGnom", skip, "XSDataInteger")
        self._skip = skip
        checkType("XSDataInputDatGnom", "Constructor of XSDataInputDatGnom", output, "XSDataFile")
        self._output = output
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        checkType("XSDataInputDatGnom", "setInputCurve", inputCurve, "XSDataFile")
        self._inputCurve = inputCurve
    def delInputCurve(self): self._inputCurve = None
    # Properties
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def getRg(self): return self._rg
    def setRg(self, rg):
        checkType("XSDataInputDatGnom", "setRg", rg, "XSDataLength")
        self._rg = rg
    def delRg(self): self._rg = None
    # Properties
    rg = property(getRg, setRg, delRg, "Property for rg")
    def getSkip(self): return self._skip
    def setSkip(self, skip):
        checkType("XSDataInputDatGnom", "setSkip", skip, "XSDataInteger")
        self._skip = skip
    def delSkip(self): self._skip = None
    # Properties
    skip = property(getSkip, setSkip, delSkip, "Property for skip")
    def getOutput(self): return self._output
    def setOutput(self, output):
        checkType("XSDataInputDatGnom", "setOutput", output, "XSDataFile")
        self._output = output
    def delOutput(self): self._output = None
    # Properties
    output = property(getOutput, setOutput, delOutput, "Property for output")
    def export(self, outfile, level, name_='XSDataInputDatGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatGnom'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputCurve is not None:
            self.inputCurve.export(outfile, level, name_='inputCurve')
        else:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._rg is not None:
            self.rg.export(outfile, level, name_='rg')
        if self._skip is not None:
            self.skip.export(outfile, level, name_='skip')
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rg':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'skip':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSkip(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatGnom

class XSDataInputDatPorod(XSDataInput):
    """Input file can be in 1/nm or 1/A, result will be in the same unit(^3)."""
    def __init__(self, configuration=None, gnomFile=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputDatPorod", "Constructor of XSDataInputDatPorod", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        checkType("XSDataInputDatPorod", "setGnomFile", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def delGnomFile(self): self._gnomFile = None
    # Properties
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    def export(self, outfile, level, name_='XSDataInputDatPorod'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatPorod'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatPorod" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatPorod' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatPorod is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatPorod.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatPorod()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatPorod" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatPorod()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatPorod

class XSDataInputDataver(XSDataInput):
    """dataver averages two or more curves from files"""
    def __init__(self, configuration=None, outputCurve=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputCurve is None:
            self._inputCurve = []
        else:
            checkType("XSDataInputDataver", "Constructor of XSDataInputDataver", inputCurve, "list")
            self._inputCurve = inputCurve
        checkType("XSDataInputDataver", "Constructor of XSDataInputDataver", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        checkType("XSDataInputDataver", "setInputCurve", inputCurve, "list")
        self._inputCurve = inputCurve
    def delInputCurve(self): self._inputCurve = None
    # Properties
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        checkType("XSDataInputDataver", "setInputCurve", value, "XSDataFile")
        self._inputCurve.append(value)
    def insertInputCurve(self, index, value):
        checkType("XSDataInputDataver", "setInputCurve", value, "XSDataFile")
        self._inputCurve[index] = value
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        checkType("XSDataInputDataver", "setOutputCurve", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def delOutputCurve(self): self._outputCurve = None
    # Properties
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataInputDataver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDataver'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDataver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDataver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDataver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDataver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDataver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDataver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDataver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDataver

class XSDataInputDatcmp(XSDataInput):
    """datcmp compares two curves from files
	"""
    def __init__(self, configuration=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputCurve is None:
            self._inputCurve = []
        else:
            checkType("XSDataInputDatcmp", "Constructor of XSDataInputDatcmp", inputCurve, "list")
            self._inputCurve = inputCurve
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        checkType("XSDataInputDatcmp", "setInputCurve", inputCurve, "list")
        self._inputCurve = inputCurve
    def delInputCurve(self): self._inputCurve = None
    # Properties
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
        self._inputCurve.append(value)
    def insertInputCurve(self, index, value):
        checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
        self._inputCurve[index] = value
    def export(self, outfile, level, name_='XSDataInputDatcmp'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatcmp'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatcmp" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatcmp' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatcmp is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatcmp.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatcmp()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatcmp" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatcmp()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatcmp

class XSDataInputDatop(XSDataInput):
    """datop makes an operation on curves"""
    def __init__(self, configuration=None, constant=None, operation=None, outputCurve=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputCurve is None:
            self._inputCurve = []
        else:
            checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", inputCurve, "list")
            self._inputCurve = inputCurve
        checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
        checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", operation, "XSDataString")
        self._operation = operation
        checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", constant, "XSDataDouble")
        self._constant = constant
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        checkType("XSDataInputDatop", "setInputCurve", inputCurve, "list")
        self._inputCurve = inputCurve
    def delInputCurve(self): self._inputCurve = None
    # Properties
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        checkType("XSDataInputDatop", "setInputCurve", value, "XSDataFile")
        self._inputCurve.append(value)
    def insertInputCurve(self, index, value):
        checkType("XSDataInputDatop", "setInputCurve", value, "XSDataFile")
        self._inputCurve[index] = value
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        checkType("XSDataInputDatop", "setOutputCurve", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def delOutputCurve(self): self._outputCurve = None
    # Properties
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def getOperation(self): return self._operation
    def setOperation(self, operation):
        checkType("XSDataInputDatop", "setOperation", operation, "XSDataString")
        self._operation = operation
    def delOperation(self): self._operation = None
    # Properties
    operation = property(getOperation, setOperation, delOperation, "Property for operation")
    def getConstant(self): return self._constant
    def setConstant(self, constant):
        checkType("XSDataInputDatop", "setConstant", constant, "XSDataDouble")
        self._constant = constant
    def delConstant(self): self._constant = None
    # Properties
    constant = property(getConstant, setConstant, delConstant, "Property for constant")
    def export(self, outfile, level, name_='XSDataInputDatop'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatop'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
        if self._operation is not None:
            self.operation.export(outfile, level, name_='operation')
        else:
            warnEmptyAttribute("operation", "XSDataString")
        if self._constant is not None:
            self.constant.export(outfile, level, name_='constant')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOperation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'constant':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConstant(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatop" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatop' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatop is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatop.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatop()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatop" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatop()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatop

class XSDataInputGnom(XSDataInput):
    """Input data can be provided either as a list of doubles, as Arrays or as a filename"""
    def __init__(self, configuration=None, mode=None, angularScale=None, experimentalDataFile=None, experimentalDataStdArray=None, experimentalDataStdDev=None, experimentalDataIArray=None, experimentalDataValues=None, experimentalDataQArray=None, experimentalDataQ=None, rMax=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", rMax, "XSDataDouble")
        self._rMax = rMax
        if experimentalDataQ is None:
            self._experimentalDataQ = []
        else:
            checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataQ, "list")
            self._experimentalDataQ = experimentalDataQ
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataQArray, "XSDataArray")
        self._experimentalDataQArray = experimentalDataQArray
        if experimentalDataValues is None:
            self._experimentalDataValues = []
        else:
            checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataValues, "list")
            self._experimentalDataValues = experimentalDataValues
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataIArray, "XSDataArray")
        self._experimentalDataIArray = experimentalDataIArray
        if experimentalDataStdDev is None:
            self._experimentalDataStdDev = []
        else:
            checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataStdDev, "list")
            self._experimentalDataStdDev = experimentalDataStdDev
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataStdArray, "XSDataArray")
        self._experimentalDataStdArray = experimentalDataStdArray
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataFile, "XSDataFile")
        self._experimentalDataFile = experimentalDataFile
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", angularScale, "XSDataInteger")
        self._angularScale = angularScale
        checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", mode, "XSDataString")
        self._mode = mode
    def getRMax(self): return self._rMax
    def setRMax(self, rMax):
        checkType("XSDataInputGnom", "setRMax", rMax, "XSDataDouble")
        self._rMax = rMax
    def delRMax(self): self._rMax = None
    # Properties
    rMax = property(getRMax, setRMax, delRMax, "Property for rMax")
    def getExperimentalDataQ(self): return self._experimentalDataQ
    def setExperimentalDataQ(self, experimentalDataQ):
        checkType("XSDataInputGnom", "setExperimentalDataQ", experimentalDataQ, "list")
        self._experimentalDataQ = experimentalDataQ
    def delExperimentalDataQ(self): self._experimentalDataQ = None
    # Properties
    experimentalDataQ = property(getExperimentalDataQ, setExperimentalDataQ, delExperimentalDataQ, "Property for experimentalDataQ")
    def addExperimentalDataQ(self, value):
        checkType("XSDataInputGnom", "setExperimentalDataQ", value, "XSDataDouble")
        self._experimentalDataQ.append(value)
    def insertExperimentalDataQ(self, index, value):
        checkType("XSDataInputGnom", "setExperimentalDataQ", value, "XSDataDouble")
        self._experimentalDataQ[index] = value
    def getExperimentalDataQArray(self): return self._experimentalDataQArray
    def setExperimentalDataQArray(self, experimentalDataQArray):
        checkType("XSDataInputGnom", "setExperimentalDataQArray", experimentalDataQArray, "XSDataArray")
        self._experimentalDataQArray = experimentalDataQArray
    def delExperimentalDataQArray(self): self._experimentalDataQArray = None
    # Properties
    experimentalDataQArray = property(getExperimentalDataQArray, setExperimentalDataQArray, delExperimentalDataQArray, "Property for experimentalDataQArray")
    def getExperimentalDataValues(self): return self._experimentalDataValues
    def setExperimentalDataValues(self, experimentalDataValues):
        checkType("XSDataInputGnom", "setExperimentalDataValues", experimentalDataValues, "list")
        self._experimentalDataValues = experimentalDataValues
    def delExperimentalDataValues(self): self._experimentalDataValues = None
    # Properties
    experimentalDataValues = property(getExperimentalDataValues, setExperimentalDataValues, delExperimentalDataValues, "Property for experimentalDataValues")
    def addExperimentalDataValues(self, value):
        checkType("XSDataInputGnom", "setExperimentalDataValues", value, "XSDataDouble")
        self._experimentalDataValues.append(value)
    def insertExperimentalDataValues(self, index, value):
        checkType("XSDataInputGnom", "setExperimentalDataValues", value, "XSDataDouble")
        self._experimentalDataValues[index] = value
    def getExperimentalDataIArray(self): return self._experimentalDataIArray
    def setExperimentalDataIArray(self, experimentalDataIArray):
        checkType("XSDataInputGnom", "setExperimentalDataIArray", experimentalDataIArray, "XSDataArray")
        self._experimentalDataIArray = experimentalDataIArray
    def delExperimentalDataIArray(self): self._experimentalDataIArray = None
    # Properties
    experimentalDataIArray = property(getExperimentalDataIArray, setExperimentalDataIArray, delExperimentalDataIArray, "Property for experimentalDataIArray")
    def getExperimentalDataStdDev(self): return self._experimentalDataStdDev
    def setExperimentalDataStdDev(self, experimentalDataStdDev):
        checkType("XSDataInputGnom", "setExperimentalDataStdDev", experimentalDataStdDev, "list")
        self._experimentalDataStdDev = experimentalDataStdDev
    def delExperimentalDataStdDev(self): self._experimentalDataStdDev = None
    # Properties
    experimentalDataStdDev = property(getExperimentalDataStdDev, setExperimentalDataStdDev, delExperimentalDataStdDev, "Property for experimentalDataStdDev")
    def addExperimentalDataStdDev(self, value):
        checkType("XSDataInputGnom", "setExperimentalDataStdDev", value, "XSDataDouble")
        self._experimentalDataStdDev.append(value)
    def insertExperimentalDataStdDev(self, index, value):
        checkType("XSDataInputGnom", "setExperimentalDataStdDev", value, "XSDataDouble")
        self._experimentalDataStdDev[index] = value
    def getExperimentalDataStdArray(self): return self._experimentalDataStdArray
    def setExperimentalDataStdArray(self, experimentalDataStdArray):
        checkType("XSDataInputGnom", "setExperimentalDataStdArray", experimentalDataStdArray, "XSDataArray")
        self._experimentalDataStdArray = experimentalDataStdArray
    def delExperimentalDataStdArray(self): self._experimentalDataStdArray = None
    # Properties
    experimentalDataStdArray = property(getExperimentalDataStdArray, setExperimentalDataStdArray, delExperimentalDataStdArray, "Property for experimentalDataStdArray")
    def getExperimentalDataFile(self): return self._experimentalDataFile
    def setExperimentalDataFile(self, experimentalDataFile):
        checkType("XSDataInputGnom", "setExperimentalDataFile", experimentalDataFile, "XSDataFile")
        self._experimentalDataFile = experimentalDataFile
    def delExperimentalDataFile(self): self._experimentalDataFile = None
    # Properties
    experimentalDataFile = property(getExperimentalDataFile, setExperimentalDataFile, delExperimentalDataFile, "Property for experimentalDataFile")
    def getAngularScale(self): return self._angularScale
    def setAngularScale(self, angularScale):
        checkType("XSDataInputGnom", "setAngularScale", angularScale, "XSDataInteger")
        self._angularScale = angularScale
    def delAngularScale(self): self._angularScale = None
    # Properties
    angularScale = property(getAngularScale, setAngularScale, delAngularScale, "Property for angularScale")
    def getMode(self): return self._mode
    def setMode(self, mode):
        checkType("XSDataInputGnom", "setMode", mode, "XSDataString")
        self._mode = mode
    def delMode(self): self._mode = None
    # Properties
    mode = property(getMode, setMode, delMode, "Property for mode")
    def export(self, outfile, level, name_='XSDataInputGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputGnom'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rMax is not None:
            self.rMax.export(outfile, level, name_='rMax')
        else:
            warnEmptyAttribute("rMax", "XSDataDouble")
        for experimentalDataQ_ in self.getExperimentalDataQ():
            experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
        if self._experimentalDataQArray is not None:
            self.experimentalDataQArray.export(outfile, level, name_='experimentalDataQArray')
        for experimentalDataValues_ in self.getExperimentalDataValues():
            experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
        if self._experimentalDataIArray is not None:
            self.experimentalDataIArray.export(outfile, level, name_='experimentalDataIArray')
        for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
            experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
        if self._experimentalDataStdArray is not None:
            self.experimentalDataStdArray.export(outfile, level, name_='experimentalDataStdArray')
        if self._experimentalDataFile is not None:
            self.experimentalDataFile.export(outfile, level, name_='experimentalDataFile')
        if self._angularScale is not None:
            self.angularScale.export(outfile, level, name_='angularScale')
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataQ':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataQArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataQArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataValues':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataIArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdDev':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataStdDev.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataStdArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setExperimentalDataFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angularScale':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setAngularScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputGnom

class XSDataInputSaxsAnalysis(XSDataInput):
    """AutoRg -> Gnom -> Prod pipeline"""
    def __init__(self, configuration=None, gnomFile=None, autoRg=None, scatterCurve=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputSaxsAnalysis", "Constructor of XSDataInputSaxsAnalysis", scatterCurve, "XSDataFile")
        self._scatterCurve = scatterCurve
        checkType("XSDataInputSaxsAnalysis", "Constructor of XSDataInputSaxsAnalysis", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
        checkType("XSDataInputSaxsAnalysis", "Constructor of XSDataInputSaxsAnalysis", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def getScatterCurve(self): return self._scatterCurve
    def setScatterCurve(self, scatterCurve):
        checkType("XSDataInputSaxsAnalysis", "setScatterCurve", scatterCurve, "XSDataFile")
        self._scatterCurve = scatterCurve
    def delScatterCurve(self): self._scatterCurve = None
    # Properties
    scatterCurve = property(getScatterCurve, setScatterCurve, delScatterCurve, "Property for scatterCurve")
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        checkType("XSDataInputSaxsAnalysis", "setAutoRg", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
    def delAutoRg(self): self._autoRg = None
    # Properties
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        checkType("XSDataInputSaxsAnalysis", "setGnomFile", gnomFile, "XSDataFile")
        self._gnomFile = gnomFile
    def delGnomFile(self): self._gnomFile = None
    # Properties
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    def export(self, outfile, level, name_='XSDataInputSaxsAnalysis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsAnalysis'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._scatterCurve is not None:
            self.scatterCurve.export(outfile, level, name_='scatterCurve')
        else:
            warnEmptyAttribute("scatterCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatterCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
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
        self.export( oStreamString, 0, name_="XSDataInputSaxsAnalysis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsAnalysis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsAnalysis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsAnalysis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsAnalysis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsAnalysis

class XSDataInputSaxsPipeline(XSDataInput):
    """Run ProcessOneFile on each file of a time time serie until autorg """
    def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", fileSerie, "XSDataFileSeries")
        self._fileSerie = fileSerie
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", sample, "XSDataBioSaxsSample")
        self._sample = sample
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directory1D, "XSDataFile")
        self._directory1D = directory1D
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directory2D, "XSDataFile")
        self._directory2D = directory2D
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
        checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def getFileSerie(self): return self._fileSerie
    def setFileSerie(self, fileSerie):
        checkType("XSDataInputSaxsPipeline", "setFileSerie", fileSerie, "XSDataFileSeries")
        self._fileSerie = fileSerie
    def delFileSerie(self): self._fileSerie = None
    # Properties
    fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
    def getSample(self): return self._sample
    def setSample(self, sample):
        checkType("XSDataInputSaxsPipeline", "setSample", sample, "XSDataBioSaxsSample")
        self._sample = sample
    def delSample(self): self._sample = None
    # Properties
    sample = property(getSample, setSample, delSample, "Property for sample")
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        checkType("XSDataInputSaxsPipeline", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
        self._experimentSetup = experimentSetup
    def delExperimentSetup(self): self._experimentSetup = None
    # Properties
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        checkType("XSDataInputSaxsPipeline", "setDirectory1D", directory1D, "XSDataFile")
        self._directory1D = directory1D
    def delDirectory1D(self): self._directory1D = None
    # Properties
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        checkType("XSDataInputSaxsPipeline", "setDirectory2D", directory2D, "XSDataFile")
        self._directory2D = directory2D
    def delDirectory2D(self): self._directory2D = None
    # Properties
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        checkType("XSDataInputSaxsPipeline", "setDirectoryMisc", directoryMisc, "XSDataFile")
        self._directoryMisc = directoryMisc
    def delDirectoryMisc(self): self._directoryMisc = None
    # Properties
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        checkType("XSDataInputSaxsPipeline", "setForceReprocess", forceReprocess, "XSDataBoolean")
        self._forceReprocess = forceReprocess
    def delForceReprocess(self): self._forceReprocess = None
    # Properties
    forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        checkType("XSDataInputSaxsPipeline", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
        self._absoluteFidelity = absoluteFidelity
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    # Properties
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        checkType("XSDataInputSaxsPipeline", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
        self._relativeFidelity = relativeFidelity
    def delRelativeFidelity(self): self._relativeFidelity = None
    # Properties
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        checkType("XSDataInputSaxsPipeline", "setRawImageSize", rawImageSize, "XSDataInteger")
        self._rawImageSize = rawImageSize
    def delRawImageSize(self): self._rawImageSize = None
    # Properties
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    def export(self, outfile, level, name_='XSDataInputSaxsPipeline'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsPipeline'):
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
        self.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsPipeline' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsPipeline is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsPipeline.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsPipeline()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsPipeline()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsPipeline

class XSDataInputSupcomb(XSDataInput):
    def __init__(self, configuration=None, backbone=None, enantiomorphs=None, superimposeFile=None, templateFile=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", templateFile, "XSDataFile")
        self._templateFile = templateFile
        checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", superimposeFile, "XSDataFile")
        self._superimposeFile = superimposeFile
        checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", enantiomorphs, "XSDataBoolean")
        self._enantiomorphs = enantiomorphs
        checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", backbone, "XSDataBoolean")
        self._backbone = backbone
    def getTemplateFile(self): return self._templateFile
    def setTemplateFile(self, templateFile):
        checkType("XSDataInputSupcomb", "setTemplateFile", templateFile, "XSDataFile")
        self._templateFile = templateFile
    def delTemplateFile(self): self._templateFile = None
    # Properties
    templateFile = property(getTemplateFile, setTemplateFile, delTemplateFile, "Property for templateFile")
    def getSuperimposeFile(self): return self._superimposeFile
    def setSuperimposeFile(self, superimposeFile):
        checkType("XSDataInputSupcomb", "setSuperimposeFile", superimposeFile, "XSDataFile")
        self._superimposeFile = superimposeFile
    def delSuperimposeFile(self): self._superimposeFile = None
    # Properties
    superimposeFile = property(getSuperimposeFile, setSuperimposeFile, delSuperimposeFile, "Property for superimposeFile")
    def getEnantiomorphs(self): return self._enantiomorphs
    def setEnantiomorphs(self, enantiomorphs):
        checkType("XSDataInputSupcomb", "setEnantiomorphs", enantiomorphs, "XSDataBoolean")
        self._enantiomorphs = enantiomorphs
    def delEnantiomorphs(self): self._enantiomorphs = None
    # Properties
    enantiomorphs = property(getEnantiomorphs, setEnantiomorphs, delEnantiomorphs, "Property for enantiomorphs")
    def getBackbone(self): return self._backbone
    def setBackbone(self, backbone):
        checkType("XSDataInputSupcomb", "setBackbone", backbone, "XSDataBoolean")
        self._backbone = backbone
    def delBackbone(self): self._backbone = None
    # Properties
    backbone = property(getBackbone, setBackbone, delBackbone, "Property for backbone")
    def export(self, outfile, level, name_='XSDataInputSupcomb'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSupcomb'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._templateFile is not None:
            self.templateFile.export(outfile, level, name_='templateFile')
        else:
            warnEmptyAttribute("templateFile", "XSDataFile")
        if self._superimposeFile is not None:
            self.superimposeFile.export(outfile, level, name_='superimposeFile')
        else:
            warnEmptyAttribute("superimposeFile", "XSDataFile")
        if self._enantiomorphs is not None:
            self.enantiomorphs.export(outfile, level, name_='enantiomorphs')
        if self._backbone is not None:
            self.backbone.export(outfile, level, name_='backbone')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'templateFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setTemplateFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'superimposeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSuperimposeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enantiomorphs':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setEnantiomorphs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'backbone':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setBackbone(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSupcomb' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSupcomb is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSupcomb.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSupcomb" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSupcomb

class XSDataResultAutoRg(XSDataResult):
    def __init__(self, status=None, autoRgOut=None):
        XSDataResult.__init__(self, status)
    
    
        if autoRgOut is None:
            self._autoRgOut = []
        else:
            checkType("XSDataResultAutoRg", "Constructor of XSDataResultAutoRg", autoRgOut, "list")
            self._autoRgOut = autoRgOut
    def getAutoRgOut(self): return self._autoRgOut
    def setAutoRgOut(self, autoRgOut):
        checkType("XSDataResultAutoRg", "setAutoRgOut", autoRgOut, "list")
        self._autoRgOut = autoRgOut
    def delAutoRgOut(self): self._autoRgOut = None
    # Properties
    autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
    def addAutoRgOut(self, value):
        checkType("XSDataResultAutoRg", "setAutoRgOut", value, "XSDataAutoRg")
        self._autoRgOut.append(value)
    def insertAutoRgOut(self, index, value):
        checkType("XSDataResultAutoRg", "setAutoRgOut", value, "XSDataAutoRg")
        self._autoRgOut[index] = value
    def export(self, outfile, level, name_='XSDataResultAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultAutoRg'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for autoRgOut_ in self.getAutoRgOut():
            autoRgOut_.export(outfile, level, name_='autoRgOut')
        if self.getAutoRgOut() == []:
            warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRgOut':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.autoRgOut.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultAutoRg

class XSDataResultAutoSub(XSDataResult):
    """Result of AutoSub (EDNA implementation) 	"""
    def __init__(self, status=None, autoRg=None, subtractedCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultAutoSub", "Constructor of XSDataResultAutoSub", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
        checkType("XSDataResultAutoSub", "Constructor of XSDataResultAutoSub", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        checkType("XSDataResultAutoSub", "setSubtractedCurve", subtractedCurve, "XSDataFile")
        self._subtractedCurve = subtractedCurve
    def delSubtractedCurve(self): self._subtractedCurve = None
    # Properties
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        checkType("XSDataResultAutoSub", "setAutoRg", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
    def delAutoRg(self): self._autoRg = None
    # Properties
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    def export(self, outfile, level, name_='XSDataResultAutoSub'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultAutoSub'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        else:
            warnEmptyAttribute("subtractedCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        else:
            warnEmptyAttribute("autoRg", "XSDataAutoRg")
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
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultAutoSub" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultAutoSub' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultAutoSub is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultAutoSub.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoSub()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultAutoSub" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoSub()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultAutoSub

class XSDataResultDamaver(XSDataResult):
    def __init__(self, status=None, damstartPdbFile=None, damfilterPdbFile=None, damaverPdbFile=None, variationNSD=None, meanNSD=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", meanNSD, "XSDataDouble")
        self._meanNSD = meanNSD
        checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", variationNSD, "XSDataDouble")
        self._variationNSD = variationNSD
        checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damaverPdbFile, "XSDataFile")
        self._damaverPdbFile = damaverPdbFile
        checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damfilterPdbFile, "XSDataFile")
        self._damfilterPdbFile = damfilterPdbFile
        checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damstartPdbFile, "XSDataFile")
        self._damstartPdbFile = damstartPdbFile
    def getMeanNSD(self): return self._meanNSD
    def setMeanNSD(self, meanNSD):
        checkType("XSDataResultDamaver", "setMeanNSD", meanNSD, "XSDataDouble")
        self._meanNSD = meanNSD
    def delMeanNSD(self): self._meanNSD = None
    # Properties
    meanNSD = property(getMeanNSD, setMeanNSD, delMeanNSD, "Property for meanNSD")
    def getVariationNSD(self): return self._variationNSD
    def setVariationNSD(self, variationNSD):
        checkType("XSDataResultDamaver", "setVariationNSD", variationNSD, "XSDataDouble")
        self._variationNSD = variationNSD
    def delVariationNSD(self): self._variationNSD = None
    # Properties
    variationNSD = property(getVariationNSD, setVariationNSD, delVariationNSD, "Property for variationNSD")
    def getDamaverPdbFile(self): return self._damaverPdbFile
    def setDamaverPdbFile(self, damaverPdbFile):
        checkType("XSDataResultDamaver", "setDamaverPdbFile", damaverPdbFile, "XSDataFile")
        self._damaverPdbFile = damaverPdbFile
    def delDamaverPdbFile(self): self._damaverPdbFile = None
    # Properties
    damaverPdbFile = property(getDamaverPdbFile, setDamaverPdbFile, delDamaverPdbFile, "Property for damaverPdbFile")
    def getDamfilterPdbFile(self): return self._damfilterPdbFile
    def setDamfilterPdbFile(self, damfilterPdbFile):
        checkType("XSDataResultDamaver", "setDamfilterPdbFile", damfilterPdbFile, "XSDataFile")
        self._damfilterPdbFile = damfilterPdbFile
    def delDamfilterPdbFile(self): self._damfilterPdbFile = None
    # Properties
    damfilterPdbFile = property(getDamfilterPdbFile, setDamfilterPdbFile, delDamfilterPdbFile, "Property for damfilterPdbFile")
    def getDamstartPdbFile(self): return self._damstartPdbFile
    def setDamstartPdbFile(self, damstartPdbFile):
        checkType("XSDataResultDamaver", "setDamstartPdbFile", damstartPdbFile, "XSDataFile")
        self._damstartPdbFile = damstartPdbFile
    def delDamstartPdbFile(self): self._damstartPdbFile = None
    # Properties
    damstartPdbFile = property(getDamstartPdbFile, setDamstartPdbFile, delDamstartPdbFile, "Property for damstartPdbFile")
    def export(self, outfile, level, name_='XSDataResultDamaver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamaver'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._meanNSD is not None:
            self.meanNSD.export(outfile, level, name_='meanNSD')
        if self._variationNSD is not None:
            self.variationNSD.export(outfile, level, name_='variationNSD')
        if self._damaverPdbFile is not None:
            self.damaverPdbFile.export(outfile, level, name_='damaverPdbFile')
        if self._damfilterPdbFile is not None:
            self.damfilterPdbFile.export(outfile, level, name_='damfilterPdbFile')
        if self._damstartPdbFile is not None:
            self.damstartPdbFile.export(outfile, level, name_='damstartPdbFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'meanNSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMeanNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'variationNSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setVariationNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damaverPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamaverPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfilterPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamfilterPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamstartPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamaver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamaver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamaver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamaver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamaver

class XSDataResultDamfilt(XSDataResult):
    def __init__(self, status=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDamfilt", "Constructor of XSDataResultDamfilt", outputPdbFile, "XSDataFile")
        self._outputPdbFile = outputPdbFile
    def getOutputPdbFile(self): return self._outputPdbFile
    def setOutputPdbFile(self, outputPdbFile):
        checkType("XSDataResultDamfilt", "setOutputPdbFile", outputPdbFile, "XSDataFile")
        self._outputPdbFile = outputPdbFile
    def delOutputPdbFile(self): self._outputPdbFile = None
    # Properties
    outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
    def export(self, outfile, level, name_='XSDataResultDamfilt'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamfilt'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputPdbFile is not None:
            self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamfilt' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamfilt is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamfilt.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamfilt" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamfilt

class XSDataResultDammif(XSDataResult):
    def __init__(self, status=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", fitFile, "XSDataFile")
        self._fitFile = fitFile
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", rfactor, "XSDataDouble")
        self._rfactor = rfactor
        checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", chiSqrt, "XSDataDouble")
        self._chiSqrt = chiSqrt
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        checkType("XSDataResultDammif", "setFitFile", fitFile, "XSDataFile")
        self._fitFile = fitFile
    def delFitFile(self): self._fitFile = None
    # Properties
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataResultDammif", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        checkType("XSDataResultDammif", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    # Properties
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        checkType("XSDataResultDammif", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
    def delPdbSolventFile(self): self._pdbSolventFile = None
    # Properties
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        checkType("XSDataResultDammif", "setRfactor", rfactor, "XSDataDouble")
        self._rfactor = rfactor
    def delRfactor(self): self._rfactor = None
    # Properties
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    def getChiSqrt(self): return self._chiSqrt
    def setChiSqrt(self, chiSqrt):
        checkType("XSDataResultDammif", "setChiSqrt", chiSqrt, "XSDataDouble")
        self._chiSqrt = chiSqrt
    def delChiSqrt(self): self._chiSqrt = None
    # Properties
    chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
    def export(self, outfile, level, name_='XSDataResultDammif'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDammif'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._chiSqrt is not None:
            self.chiSqrt.export(outfile, level, name_='chiSqrt')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDammif' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDammif is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDammif.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDammif" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDammif

class XSDataResultDammin(XSDataResult):
    def __init__(self, status=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", fitFile, "XSDataFile")
        self._fitFile = fitFile
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", rfactor, "XSDataDouble")
        self._rfactor = rfactor
        checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", chiSqrt, "XSDataDouble")
        self._chiSqrt = chiSqrt
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        checkType("XSDataResultDammin", "setFitFile", fitFile, "XSDataFile")
        self._fitFile = fitFile
    def delFitFile(self): self._fitFile = None
    # Properties
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataResultDammin", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        checkType("XSDataResultDammin", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    # Properties
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        checkType("XSDataResultDammin", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
    def delPdbSolventFile(self): self._pdbSolventFile = None
    # Properties
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        checkType("XSDataResultDammin", "setRfactor", rfactor, "XSDataDouble")
        self._rfactor = rfactor
    def delRfactor(self): self._rfactor = None
    # Properties
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    def getChiSqrt(self): return self._chiSqrt
    def setChiSqrt(self, chiSqrt):
        checkType("XSDataResultDammin", "setChiSqrt", chiSqrt, "XSDataDouble")
        self._chiSqrt = chiSqrt
    def delChiSqrt(self): self._chiSqrt = None
    # Properties
    chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
    def export(self, outfile, level, name_='XSDataResultDammin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDammin'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._chiSqrt is not None:
            self.chiSqrt.export(outfile, level, name_='chiSqrt')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDammin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDammin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDammin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDammin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDammin

class XSDataResultDamstart(XSDataResult):
    def __init__(self, status=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDamstart", "Constructor of XSDataResultDamstart", outputPdbFile, "XSDataFile")
        self._outputPdbFile = outputPdbFile
    def getOutputPdbFile(self): return self._outputPdbFile
    def setOutputPdbFile(self, outputPdbFile):
        checkType("XSDataResultDamstart", "setOutputPdbFile", outputPdbFile, "XSDataFile")
        self._outputPdbFile = outputPdbFile
    def delOutputPdbFile(self): self._outputPdbFile = None
    # Properties
    outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
    def export(self, outfile, level, name_='XSDataResultDamstart'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamstart'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputPdbFile is not None:
            self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamstart' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamstart is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamstart.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamstart" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamstart

class XSDataResultDatGnom(XSDataResult):
    def __init__(self, status=None, gnom=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDatGnom", "Constructor of XSDataResultDatGnom", gnom, "XSDataGnom")
        self._gnom = gnom
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        checkType("XSDataResultDatGnom", "setGnom", gnom, "XSDataGnom")
        self._gnom = gnom
    def delGnom(self): self._gnom = None
    # Properties
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    def export(self, outfile, level, name_='XSDataResultDatGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatGnom'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        else:
            warnEmptyAttribute("gnom", "XSDataGnom")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatGnom

class XSDataResultDatPorod(XSDataResult):
    def __init__(self, status=None, volume=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDatPorod", "Constructor of XSDataResultDatPorod", volume, "XSDataDoubleWithUnit")
        self._volume = volume
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        checkType("XSDataResultDatPorod", "setVolume", volume, "XSDataDoubleWithUnit")
        self._volume = volume
    def delVolume(self): self._volume = None
    # Properties
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def export(self, outfile, level, name_='XSDataResultDatPorod'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatPorod'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataDoubleWithUnit")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatPorod" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatPorod' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatPorod is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatPorod.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatPorod()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatPorod" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatPorod()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatPorod

class XSDataResultDataver(XSDataResult):
    """Result of Dataver 	"""
    def __init__(self, status=None, outputCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDataver", "Constructor of XSDataResultDataver", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        checkType("XSDataResultDataver", "setOutputCurve", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def delOutputCurve(self): self._outputCurve = None
    # Properties
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataResultDataver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDataver'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDataver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDataver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDataver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDataver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDataver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDataver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDataver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDataver

class XSDataResultDatcmp(XSDataResult):
    """Higher chi-values indicate dis-similarities in the input.

	 Fidelity gives the likelihood of the two data sets being identical.
	"""
    def __init__(self, status=None, fidelity=None, chi=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", chi, "XSDataDouble")
        self._chi = chi
        checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", fidelity, "XSDataDouble")
        self._fidelity = fidelity
    def getChi(self): return self._chi
    def setChi(self, chi):
        checkType("XSDataResultDatcmp", "setChi", chi, "XSDataDouble")
        self._chi = chi
    def delChi(self): self._chi = None
    # Properties
    chi = property(getChi, setChi, delChi, "Property for chi")
    def getFidelity(self): return self._fidelity
    def setFidelity(self, fidelity):
        checkType("XSDataResultDatcmp", "setFidelity", fidelity, "XSDataDouble")
        self._fidelity = fidelity
    def delFidelity(self): self._fidelity = None
    # Properties
    fidelity = property(getFidelity, setFidelity, delFidelity, "Property for fidelity")
    def export(self, outfile, level, name_='XSDataResultDatcmp'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatcmp'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._chi is not None:
            self.chi.export(outfile, level, name_='chi')
        else:
            warnEmptyAttribute("chi", "XSDataDouble")
        if self._fidelity is not None:
            self.fidelity.export(outfile, level, name_='fidelity')
        else:
            warnEmptyAttribute("fidelity", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chi':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFidelity(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatcmp" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatcmp' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatcmp is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatcmp.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatcmp()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatcmp" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatcmp()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatcmp

class XSDataResultDatop(XSDataResult):
    """Result of Datop 	"""
    def __init__(self, status=None, outputCurve=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultDatop", "Constructor of XSDataResultDatop", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        checkType("XSDataResultDatop", "setOutputCurve", outputCurve, "XSDataFile")
        self._outputCurve = outputCurve
    def delOutputCurve(self): self._outputCurve = None
    # Properties
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataResultDatop'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatop'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatop" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatop' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatop is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatop.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatop()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatop" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatop()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatop

class XSDataResultGnom(XSDataResult):
    def __init__(self, status=None, radiusOfGyration=None, radiusOfCrossSection=None, arrayErr=None, arrayPr=None, arrayR=None, distributionErr=None, distributionPr=None, distributionR=None, scatteringFitIArray=None, scatteringFitQArray=None, scatteringFitValues=None, scatteringFitQ=None, output=None, fitQuality=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", fitQuality, "XSDataDouble")
        self._fitQuality = fitQuality
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", output, "XSDataFile")
        self._output = output
        if scatteringFitQ is None:
            self._scatteringFitQ = []
        else:
            checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitQ, "list")
            self._scatteringFitQ = scatteringFitQ
        if scatteringFitValues is None:
            self._scatteringFitValues = []
        else:
            checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitValues, "list")
            self._scatteringFitValues = scatteringFitValues
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitQArray, "XSDataArray")
        self._scatteringFitQArray = scatteringFitQArray
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitIArray, "XSDataArray")
        self._scatteringFitIArray = scatteringFitIArray
        if distributionR is None:
            self._distributionR = []
        else:
            checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionR, "list")
            self._distributionR = distributionR
        if distributionPr is None:
            self._distributionPr = []
        else:
            checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionPr, "list")
            self._distributionPr = distributionPr
        if distributionErr is None:
            self._distributionErr = []
        else:
            checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionErr, "list")
            self._distributionErr = distributionErr
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayR, "XSDataArray")
        self._arrayR = arrayR
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayPr, "XSDataArray")
        self._arrayPr = arrayPr
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayErr, "XSDataArray")
        self._arrayErr = arrayErr
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", radiusOfCrossSection, "XSDataDouble")
        self._radiusOfCrossSection = radiusOfCrossSection
        checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", radiusOfGyration, "XSDataDouble")
        self._radiusOfGyration = radiusOfGyration
    def getFitQuality(self): return self._fitQuality
    def setFitQuality(self, fitQuality):
        checkType("XSDataResultGnom", "setFitQuality", fitQuality, "XSDataDouble")
        self._fitQuality = fitQuality
    def delFitQuality(self): self._fitQuality = None
    # Properties
    fitQuality = property(getFitQuality, setFitQuality, delFitQuality, "Property for fitQuality")
    def getOutput(self): return self._output
    def setOutput(self, output):
        checkType("XSDataResultGnom", "setOutput", output, "XSDataFile")
        self._output = output
    def delOutput(self): self._output = None
    # Properties
    output = property(getOutput, setOutput, delOutput, "Property for output")
    def getScatteringFitQ(self): return self._scatteringFitQ
    def setScatteringFitQ(self, scatteringFitQ):
        checkType("XSDataResultGnom", "setScatteringFitQ", scatteringFitQ, "list")
        self._scatteringFitQ = scatteringFitQ
    def delScatteringFitQ(self): self._scatteringFitQ = None
    # Properties
    scatteringFitQ = property(getScatteringFitQ, setScatteringFitQ, delScatteringFitQ, "Property for scatteringFitQ")
    def addScatteringFitQ(self, value):
        checkType("XSDataResultGnom", "setScatteringFitQ", value, "XSDataDouble")
        self._scatteringFitQ.append(value)
    def insertScatteringFitQ(self, index, value):
        checkType("XSDataResultGnom", "setScatteringFitQ", value, "XSDataDouble")
        self._scatteringFitQ[index] = value
    def getScatteringFitValues(self): return self._scatteringFitValues
    def setScatteringFitValues(self, scatteringFitValues):
        checkType("XSDataResultGnom", "setScatteringFitValues", scatteringFitValues, "list")
        self._scatteringFitValues = scatteringFitValues
    def delScatteringFitValues(self): self._scatteringFitValues = None
    # Properties
    scatteringFitValues = property(getScatteringFitValues, setScatteringFitValues, delScatteringFitValues, "Property for scatteringFitValues")
    def addScatteringFitValues(self, value):
        checkType("XSDataResultGnom", "setScatteringFitValues", value, "XSDataDouble")
        self._scatteringFitValues.append(value)
    def insertScatteringFitValues(self, index, value):
        checkType("XSDataResultGnom", "setScatteringFitValues", value, "XSDataDouble")
        self._scatteringFitValues[index] = value
    def getScatteringFitQArray(self): return self._scatteringFitQArray
    def setScatteringFitQArray(self, scatteringFitQArray):
        checkType("XSDataResultGnom", "setScatteringFitQArray", scatteringFitQArray, "XSDataArray")
        self._scatteringFitQArray = scatteringFitQArray
    def delScatteringFitQArray(self): self._scatteringFitQArray = None
    # Properties
    scatteringFitQArray = property(getScatteringFitQArray, setScatteringFitQArray, delScatteringFitQArray, "Property for scatteringFitQArray")
    def getScatteringFitIArray(self): return self._scatteringFitIArray
    def setScatteringFitIArray(self, scatteringFitIArray):
        checkType("XSDataResultGnom", "setScatteringFitIArray", scatteringFitIArray, "XSDataArray")
        self._scatteringFitIArray = scatteringFitIArray
    def delScatteringFitIArray(self): self._scatteringFitIArray = None
    # Properties
    scatteringFitIArray = property(getScatteringFitIArray, setScatteringFitIArray, delScatteringFitIArray, "Property for scatteringFitIArray")
    def getDistributionR(self): return self._distributionR
    def setDistributionR(self, distributionR):
        checkType("XSDataResultGnom", "setDistributionR", distributionR, "list")
        self._distributionR = distributionR
    def delDistributionR(self): self._distributionR = None
    # Properties
    distributionR = property(getDistributionR, setDistributionR, delDistributionR, "Property for distributionR")
    def addDistributionR(self, value):
        checkType("XSDataResultGnom", "setDistributionR", value, "XSDataDouble")
        self._distributionR.append(value)
    def insertDistributionR(self, index, value):
        checkType("XSDataResultGnom", "setDistributionR", value, "XSDataDouble")
        self._distributionR[index] = value
    def getDistributionPr(self): return self._distributionPr
    def setDistributionPr(self, distributionPr):
        checkType("XSDataResultGnom", "setDistributionPr", distributionPr, "list")
        self._distributionPr = distributionPr
    def delDistributionPr(self): self._distributionPr = None
    # Properties
    distributionPr = property(getDistributionPr, setDistributionPr, delDistributionPr, "Property for distributionPr")
    def addDistributionPr(self, value):
        checkType("XSDataResultGnom", "setDistributionPr", value, "XSDataDouble")
        self._distributionPr.append(value)
    def insertDistributionPr(self, index, value):
        checkType("XSDataResultGnom", "setDistributionPr", value, "XSDataDouble")
        self._distributionPr[index] = value
    def getDistributionErr(self): return self._distributionErr
    def setDistributionErr(self, distributionErr):
        checkType("XSDataResultGnom", "setDistributionErr", distributionErr, "list")
        self._distributionErr = distributionErr
    def delDistributionErr(self): self._distributionErr = None
    # Properties
    distributionErr = property(getDistributionErr, setDistributionErr, delDistributionErr, "Property for distributionErr")
    def addDistributionErr(self, value):
        checkType("XSDataResultGnom", "setDistributionErr", value, "XSDataDouble")
        self._distributionErr.append(value)
    def insertDistributionErr(self, index, value):
        checkType("XSDataResultGnom", "setDistributionErr", value, "XSDataDouble")
        self._distributionErr[index] = value
    def getArrayR(self): return self._arrayR
    def setArrayR(self, arrayR):
        checkType("XSDataResultGnom", "setArrayR", arrayR, "XSDataArray")
        self._arrayR = arrayR
    def delArrayR(self): self._arrayR = None
    # Properties
    arrayR = property(getArrayR, setArrayR, delArrayR, "Property for arrayR")
    def getArrayPr(self): return self._arrayPr
    def setArrayPr(self, arrayPr):
        checkType("XSDataResultGnom", "setArrayPr", arrayPr, "XSDataArray")
        self._arrayPr = arrayPr
    def delArrayPr(self): self._arrayPr = None
    # Properties
    arrayPr = property(getArrayPr, setArrayPr, delArrayPr, "Property for arrayPr")
    def getArrayErr(self): return self._arrayErr
    def setArrayErr(self, arrayErr):
        checkType("XSDataResultGnom", "setArrayErr", arrayErr, "XSDataArray")
        self._arrayErr = arrayErr
    def delArrayErr(self): self._arrayErr = None
    # Properties
    arrayErr = property(getArrayErr, setArrayErr, delArrayErr, "Property for arrayErr")
    def getRadiusOfCrossSection(self): return self._radiusOfCrossSection
    def setRadiusOfCrossSection(self, radiusOfCrossSection):
        checkType("XSDataResultGnom", "setRadiusOfCrossSection", radiusOfCrossSection, "XSDataDouble")
        self._radiusOfCrossSection = radiusOfCrossSection
    def delRadiusOfCrossSection(self): self._radiusOfCrossSection = None
    # Properties
    radiusOfCrossSection = property(getRadiusOfCrossSection, setRadiusOfCrossSection, delRadiusOfCrossSection, "Property for radiusOfCrossSection")
    def getRadiusOfGyration(self): return self._radiusOfGyration
    def setRadiusOfGyration(self, radiusOfGyration):
        checkType("XSDataResultGnom", "setRadiusOfGyration", radiusOfGyration, "XSDataDouble")
        self._radiusOfGyration = radiusOfGyration
    def delRadiusOfGyration(self): self._radiusOfGyration = None
    # Properties
    radiusOfGyration = property(getRadiusOfGyration, setRadiusOfGyration, delRadiusOfGyration, "Property for radiusOfGyration")
    def export(self, outfile, level, name_='XSDataResultGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultGnom'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitQuality is not None:
            self.fitQuality.export(outfile, level, name_='fitQuality')
        else:
            warnEmptyAttribute("fitQuality", "XSDataDouble")
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
        else:
            warnEmptyAttribute("output", "XSDataFile")
        for scatteringFitQ_ in self.getScatteringFitQ():
            scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
        for scatteringFitValues_ in self.getScatteringFitValues():
            scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
        if self._scatteringFitQArray is not None:
            self.scatteringFitQArray.export(outfile, level, name_='scatteringFitQArray')
        if self._scatteringFitIArray is not None:
            self.scatteringFitIArray.export(outfile, level, name_='scatteringFitIArray')
        for distributionR_ in self.getDistributionR():
            distributionR_.export(outfile, level, name_='distributionR')
        for distributionPr_ in self.getDistributionPr():
            distributionPr_.export(outfile, level, name_='distributionPr')
        for distributionErr_ in self.getDistributionErr():
            distributionErr_.export(outfile, level, name_='distributionErr')
        if self._arrayR is not None:
            self.arrayR.export(outfile, level, name_='arrayR')
        if self._arrayPr is not None:
            self.arrayPr.export(outfile, level, name_='arrayPr')
        if self._arrayErr is not None:
            self.arrayErr.export(outfile, level, name_='arrayErr')
        if self._radiusOfCrossSection is not None:
            self.radiusOfCrossSection.export(outfile, level, name_='radiusOfCrossSection')
        else:
            warnEmptyAttribute("radiusOfCrossSection", "XSDataDouble")
        if self._radiusOfGyration is not None:
            self.radiusOfGyration.export(outfile, level, name_='radiusOfGyration')
        else:
            warnEmptyAttribute("radiusOfGyration", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitQuality':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFitQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQ':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.scatteringFitQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitValues':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.scatteringFitValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setScatteringFitQArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitIArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setScatteringFitIArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionR':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionR.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionPr':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionPr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionErr':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionErr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayR':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayPr':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayPr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayErr':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayErr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfCrossSection':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiusOfCrossSection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfGyration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiusOfGyration(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultGnom

class XSDataResultSaxsAnalysis(XSDataResult):
    """AutoRg -> Gnom -> Prod pipeline"""
    def __init__(self, status=None, volume=None, gnom=None, autoRg=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultSaxsAnalysis", "Constructor of XSDataResultSaxsAnalysis", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
        checkType("XSDataResultSaxsAnalysis", "Constructor of XSDataResultSaxsAnalysis", gnom, "XSDataGnom")
        self._gnom = gnom
        checkType("XSDataResultSaxsAnalysis", "Constructor of XSDataResultSaxsAnalysis", volume, "XSDataDoubleWithUnit")
        self._volume = volume
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        checkType("XSDataResultSaxsAnalysis", "setAutoRg", autoRg, "XSDataAutoRg")
        self._autoRg = autoRg
    def delAutoRg(self): self._autoRg = None
    # Properties
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        checkType("XSDataResultSaxsAnalysis", "setGnom", gnom, "XSDataGnom")
        self._gnom = gnom
    def delGnom(self): self._gnom = None
    # Properties
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        checkType("XSDataResultSaxsAnalysis", "setVolume", volume, "XSDataDoubleWithUnit")
        self._volume = volume
    def delVolume(self): self._volume = None
    # Properties
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def export(self, outfile, level, name_='XSDataResultSaxsAnalysis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsAnalysis'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        else:
            warnEmptyAttribute("autoRg", "XSDataAutoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        else:
            warnEmptyAttribute("gnom", "XSDataGnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataDoubleWithUnit")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
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
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsAnalysis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsAnalysis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsAnalysis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsAnalysis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsAnalysis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsAnalysis

class XSDataResultSaxsPipeline(XSDataResult):
    def __init__(self, status=None, autoRgOut=None):
        XSDataResult.__init__(self, status)
    
    
        if autoRgOut is None:
            self._autoRgOut = []
        else:
            checkType("XSDataResultSaxsPipeline", "Constructor of XSDataResultSaxsPipeline", autoRgOut, "list")
            self._autoRgOut = autoRgOut
    def getAutoRgOut(self): return self._autoRgOut
    def setAutoRgOut(self, autoRgOut):
        checkType("XSDataResultSaxsPipeline", "setAutoRgOut", autoRgOut, "list")
        self._autoRgOut = autoRgOut
    def delAutoRgOut(self): self._autoRgOut = None
    # Properties
    autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
    def addAutoRgOut(self, value):
        checkType("XSDataResultSaxsPipeline", "setAutoRgOut", value, "XSDataAutoRg")
        self._autoRgOut.append(value)
    def insertAutoRgOut(self, index, value):
        checkType("XSDataResultSaxsPipeline", "setAutoRgOut", value, "XSDataAutoRg")
        self._autoRgOut[index] = value
    def export(self, outfile, level, name_='XSDataResultSaxsPipeline'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsPipeline'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for autoRgOut_ in self.getAutoRgOut():
            autoRgOut_.export(outfile, level, name_='autoRgOut')
        if self.getAutoRgOut() == []:
            warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRgOut':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.autoRgOut.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsPipeline' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsPipeline is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsPipeline.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsPipeline()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsPipeline()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsPipeline

class XSDataResultSupcomb(XSDataResult):
    def __init__(self, status=None, NSD=None, trns=None, rot=None, outputFilename=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", outputFilename, "XSDataFile")
        self._outputFilename = outputFilename
        checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", rot, "XSDataRotation")
        self._rot = rot
        checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", trns, "XSDataVectorDouble")
        self._trns = trns
        checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", NSD, "XSDataDouble")
        self._NSD = NSD
    def getOutputFilename(self): return self._outputFilename
    def setOutputFilename(self, outputFilename):
        checkType("XSDataResultSupcomb", "setOutputFilename", outputFilename, "XSDataFile")
        self._outputFilename = outputFilename
    def delOutputFilename(self): self._outputFilename = None
    # Properties
    outputFilename = property(getOutputFilename, setOutputFilename, delOutputFilename, "Property for outputFilename")
    def getRot(self): return self._rot
    def setRot(self, rot):
        checkType("XSDataResultSupcomb", "setRot", rot, "XSDataRotation")
        self._rot = rot
    def delRot(self): self._rot = None
    # Properties
    rot = property(getRot, setRot, delRot, "Property for rot")
    def getTrns(self): return self._trns
    def setTrns(self, trns):
        checkType("XSDataResultSupcomb", "setTrns", trns, "XSDataVectorDouble")
        self._trns = trns
    def delTrns(self): self._trns = None
    # Properties
    trns = property(getTrns, setTrns, delTrns, "Property for trns")
    def getNSD(self): return self._NSD
    def setNSD(self, NSD):
        checkType("XSDataResultSupcomb", "setNSD", NSD, "XSDataDouble")
        self._NSD = NSD
    def delNSD(self): self._NSD = None
    # Properties
    NSD = property(getNSD, setNSD, delNSD, "Property for NSD")
    def export(self, outfile, level, name_='XSDataResultSupcomb'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSupcomb'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputFilename is not None:
            self.outputFilename.export(outfile, level, name_='outputFilename')
        else:
            warnEmptyAttribute("outputFilename", "XSDataFile")
        if self._rot is not None:
            self.rot.export(outfile, level, name_='rot')
        else:
            warnEmptyAttribute("rot", "XSDataRotation")
        if self._trns is not None:
            self.trns.export(outfile, level, name_='trns')
        else:
            warnEmptyAttribute("trns", "XSDataVectorDouble")
        if self._NSD is not None:
            self.NSD.export(outfile, level, name_='NSD')
        else:
            warnEmptyAttribute("NSD", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputFilename':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputFilename(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rot':
            obj_ = XSDataRotation()
            obj_.build(child_)
            self.setRot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trns':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setTrns(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNSD(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSupcomb' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSupcomb is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSupcomb.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSupcomb" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSupcomb



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Fri Sep 14 06:13::15 2012 by EDGenerateDS.
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
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataImageExt
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
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImageExt




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


class OffsetedImage(XSData):
    """DummyValue is the value for which the data are considered as invalid (0 by default)"""
    def __init__(self, offset=None, file=None, dummyValue=None, deltaDummy=None, array=None):
        XSData.__init__(self, )
    
    
        checkType("OffsetedImage", "Constructor of OffsetedImage", array, "XSDataArray")
        self._array = array
        checkType("OffsetedImage", "Constructor of OffsetedImage", deltaDummy, "XSDataDouble")
        self._deltaDummy = deltaDummy
        checkType("OffsetedImage", "Constructor of OffsetedImage", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
        checkType("OffsetedImage", "Constructor of OffsetedImage", file, "XSDataImageExt")
        self._file = file
        if offset is None:
            self._offset = []
        else:
            checkType("OffsetedImage", "Constructor of OffsetedImage", offset, "list")
            self._offset = offset
    def getArray(self): return self._array
    def setArray(self, array):
        checkType("OffsetedImage", "setArray", array, "XSDataArray")
        self._array = array
    def delArray(self): self._array = None
    # Properties
    array = property(getArray, setArray, delArray, "Property for array")
    def getDeltaDummy(self): return self._deltaDummy
    def setDeltaDummy(self, deltaDummy):
        checkType("OffsetedImage", "setDeltaDummy", deltaDummy, "XSDataDouble")
        self._deltaDummy = deltaDummy
    def delDeltaDummy(self): self._deltaDummy = None
    # Properties
    deltaDummy = property(getDeltaDummy, setDeltaDummy, delDeltaDummy, "Property for deltaDummy")
    def getDummyValue(self): return self._dummyValue
    def setDummyValue(self, dummyValue):
        checkType("OffsetedImage", "setDummyValue", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
    def delDummyValue(self): self._dummyValue = None
    # Properties
    dummyValue = property(getDummyValue, setDummyValue, delDummyValue, "Property for dummyValue")
    def getFile(self): return self._file
    def setFile(self, file):
        checkType("OffsetedImage", "setFile", file, "XSDataImageExt")
        self._file = file
    def delFile(self): self._file = None
    # Properties
    file = property(getFile, setFile, delFile, "Property for file")
    def getOffset(self): return self._offset
    def setOffset(self, offset):
        checkType("OffsetedImage", "setOffset", offset, "list")
        self._offset = offset
    def delOffset(self): self._offset = None
    # Properties
    offset = property(getOffset, setOffset, delOffset, "Property for offset")
    def addOffset(self, value):
        checkType("OffsetedImage", "setOffset", value, "XSDataDouble")
        self._offset.append(value)
    def insertOffset(self, index, value):
        checkType("OffsetedImage", "setOffset", value, "XSDataDouble")
        self._offset[index] = value
    def export(self, outfile, level, name_='OffsetedImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='OffsetedImage'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._array is not None:
            self.array.export(outfile, level, name_='array')
        if self._deltaDummy is not None:
            self.deltaDummy.export(outfile, level, name_='deltaDummy')
        if self._dummyValue is not None:
            self.dummyValue.export(outfile, level, name_='dummyValue')
        if self._file is not None:
            self.file.export(outfile, level, name_='file')
        for offset_ in self.getOffset():
            offset_.export(outfile, level, name_='offset')
        if self.getOffset() == []:
            warnEmptyAttribute("offset", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'array':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deltaDummy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDeltaDummy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dummyValue':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDummyValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'file':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'offset':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.offset.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="OffsetedImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='OffsetedImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class OffsetedImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return OffsetedImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = OffsetedImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="OffsetedImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = OffsetedImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class OffsetedImage

class XSDataInputMeasureOffset(XSDataInput):
    """Input can be given as a pair of 2D arrays or 2 EDF files. 
Measurement is done on the full image by default but borders can be cropped, smoothed, ...
Images must have the same size
"""
    def __init__(self, configuration=None, width=None, sobelFilter=None, smoothBorders=None, index=None, image=None, cropBorders=None, center=None, backgroundSubtraction=None, array=None):
        XSDataInput.__init__(self, configuration)
    
    
        if array is None:
            self._array = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", array, "list")
            self._array = array
        checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", backgroundSubtraction, "XSDataBoolean")
        self._backgroundSubtraction = backgroundSubtraction
        if center is None:
            self._center = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", center, "list")
            self._center = center
        if cropBorders is None:
            self._cropBorders = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", cropBorders, "list")
            self._cropBorders = cropBorders
        if image is None:
            self._image = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", image, "list")
            self._image = image
        if index is None:
            self._index = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", index, "list")
            self._index = index
        if smoothBorders is None:
            self._smoothBorders = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", smoothBorders, "list")
            self._smoothBorders = smoothBorders
        checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", sobelFilter, "XSDataBoolean")
        self._sobelFilter = sobelFilter
        if width is None:
            self._width = []
        else:
            checkType("XSDataInputMeasureOffset", "Constructor of XSDataInputMeasureOffset", width, "list")
            self._width = width
    def getArray(self): return self._array
    def setArray(self, array):
        checkType("XSDataInputMeasureOffset", "setArray", array, "list")
        self._array = array
    def delArray(self): self._array = None
    # Properties
    array = property(getArray, setArray, delArray, "Property for array")
    def addArray(self, value):
        checkType("XSDataInputMeasureOffset", "setArray", value, "XSDataArray")
        self._array.append(value)
    def insertArray(self, index, value):
        checkType("XSDataInputMeasureOffset", "setArray", value, "XSDataArray")
        self._array[index] = value
    def getBackgroundSubtraction(self): return self._backgroundSubtraction
    def setBackgroundSubtraction(self, backgroundSubtraction):
        checkType("XSDataInputMeasureOffset", "setBackgroundSubtraction", backgroundSubtraction, "XSDataBoolean")
        self._backgroundSubtraction = backgroundSubtraction
    def delBackgroundSubtraction(self): self._backgroundSubtraction = None
    # Properties
    backgroundSubtraction = property(getBackgroundSubtraction, setBackgroundSubtraction, delBackgroundSubtraction, "Property for backgroundSubtraction")
    def getCenter(self): return self._center
    def setCenter(self, center):
        checkType("XSDataInputMeasureOffset", "setCenter", center, "list")
        self._center = center
    def delCenter(self): self._center = None
    # Properties
    center = property(getCenter, setCenter, delCenter, "Property for center")
    def addCenter(self, value):
        checkType("XSDataInputMeasureOffset", "setCenter", value, "XSDataInteger")
        self._center.append(value)
    def insertCenter(self, index, value):
        checkType("XSDataInputMeasureOffset", "setCenter", value, "XSDataInteger")
        self._center[index] = value
    def getCropBorders(self): return self._cropBorders
    def setCropBorders(self, cropBorders):
        checkType("XSDataInputMeasureOffset", "setCropBorders", cropBorders, "list")
        self._cropBorders = cropBorders
    def delCropBorders(self): self._cropBorders = None
    # Properties
    cropBorders = property(getCropBorders, setCropBorders, delCropBorders, "Property for cropBorders")
    def addCropBorders(self, value):
        checkType("XSDataInputMeasureOffset", "setCropBorders", value, "XSDataInteger")
        self._cropBorders.append(value)
    def insertCropBorders(self, index, value):
        checkType("XSDataInputMeasureOffset", "setCropBorders", value, "XSDataInteger")
        self._cropBorders[index] = value
    def getImage(self): return self._image
    def setImage(self, image):
        checkType("XSDataInputMeasureOffset", "setImage", image, "list")
        self._image = image
    def delImage(self): self._image = None
    # Properties
    image = property(getImage, setImage, delImage, "Property for image")
    def addImage(self, value):
        checkType("XSDataInputMeasureOffset", "setImage", value, "XSDataImageExt")
        self._image.append(value)
    def insertImage(self, index, value):
        checkType("XSDataInputMeasureOffset", "setImage", value, "XSDataImageExt")
        self._image[index] = value
    def getIndex(self): return self._index
    def setIndex(self, index):
        checkType("XSDataInputMeasureOffset", "setIndex", index, "list")
        self._index = index
    def delIndex(self): self._index = None
    # Properties
    index = property(getIndex, setIndex, delIndex, "Property for index")
    def addIndex(self, value):
        checkType("XSDataInputMeasureOffset", "setIndex", value, "XSDataInteger")
        self._index.append(value)
    def insertIndex(self, index, value):
        checkType("XSDataInputMeasureOffset", "setIndex", value, "XSDataInteger")
        self._index[index] = value
    def getSmoothBorders(self): return self._smoothBorders
    def setSmoothBorders(self, smoothBorders):
        checkType("XSDataInputMeasureOffset", "setSmoothBorders", smoothBorders, "list")
        self._smoothBorders = smoothBorders
    def delSmoothBorders(self): self._smoothBorders = None
    # Properties
    smoothBorders = property(getSmoothBorders, setSmoothBorders, delSmoothBorders, "Property for smoothBorders")
    def addSmoothBorders(self, value):
        checkType("XSDataInputMeasureOffset", "setSmoothBorders", value, "XSDataInteger")
        self._smoothBorders.append(value)
    def insertSmoothBorders(self, index, value):
        checkType("XSDataInputMeasureOffset", "setSmoothBorders", value, "XSDataInteger")
        self._smoothBorders[index] = value
    def getSobelFilter(self): return self._sobelFilter
    def setSobelFilter(self, sobelFilter):
        checkType("XSDataInputMeasureOffset", "setSobelFilter", sobelFilter, "XSDataBoolean")
        self._sobelFilter = sobelFilter
    def delSobelFilter(self): self._sobelFilter = None
    # Properties
    sobelFilter = property(getSobelFilter, setSobelFilter, delSobelFilter, "Property for sobelFilter")
    def getWidth(self): return self._width
    def setWidth(self, width):
        checkType("XSDataInputMeasureOffset", "setWidth", width, "list")
        self._width = width
    def delWidth(self): self._width = None
    # Properties
    width = property(getWidth, setWidth, delWidth, "Property for width")
    def addWidth(self, value):
        checkType("XSDataInputMeasureOffset", "setWidth", value, "XSDataInteger")
        self._width.append(value)
    def insertWidth(self, index, value):
        checkType("XSDataInputMeasureOffset", "setWidth", value, "XSDataInteger")
        self._width[index] = value
    def export(self, outfile, level, name_='XSDataInputMeasureOffset'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputMeasureOffset'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for array_ in self.getArray():
            array_.export(outfile, level, name_='array')
        if self._backgroundSubtraction is not None:
            self.backgroundSubtraction.export(outfile, level, name_='backgroundSubtraction')
        for center_ in self.getCenter():
            center_.export(outfile, level, name_='center')
        for cropBorders_ in self.getCropBorders():
            cropBorders_.export(outfile, level, name_='cropBorders')
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        for index_ in self.getIndex():
            index_.export(outfile, level, name_='index')
        for smoothBorders_ in self.getSmoothBorders():
            smoothBorders_.export(outfile, level, name_='smoothBorders')
        if self._sobelFilter is not None:
            self.sobelFilter.export(outfile, level, name_='sobelFilter')
        for width_ in self.getWidth():
            width_.export(outfile, level, name_='width')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'array':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.array.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'backgroundSubtraction':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setBackgroundSubtraction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'center':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.center.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cropBorders':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.cropBorders.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.image.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'index':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.index.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'smoothBorders':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.smoothBorders.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sobelFilter':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setSobelFilter(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'width':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.width.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputMeasureOffset" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputMeasureOffset' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputMeasureOffset is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputMeasureOffset.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputMeasureOffset()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputMeasureOffset" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputMeasureOffset()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputMeasureOffset

class XSDataInputMeasureOffsetSift(XSDataInput):
    def __init__(self, configuration=None, descriptorFile=None):
        XSDataInput.__init__(self, configuration)
    
    
        if descriptorFile is None:
            self._descriptorFile = []
        else:
            checkType("XSDataInputMeasureOffsetSift", "Constructor of XSDataInputMeasureOffsetSift", descriptorFile, "list")
            self._descriptorFile = descriptorFile
    def getDescriptorFile(self): return self._descriptorFile
    def setDescriptorFile(self, descriptorFile):
        checkType("XSDataInputMeasureOffsetSift", "setDescriptorFile", descriptorFile, "list")
        self._descriptorFile = descriptorFile
    def delDescriptorFile(self): self._descriptorFile = None
    # Properties
    descriptorFile = property(getDescriptorFile, setDescriptorFile, delDescriptorFile, "Property for descriptorFile")
    def addDescriptorFile(self, value):
        checkType("XSDataInputMeasureOffsetSift", "setDescriptorFile", value, "XSDataFile")
        self._descriptorFile.append(value)
    def insertDescriptorFile(self, index, value):
        checkType("XSDataInputMeasureOffsetSift", "setDescriptorFile", value, "XSDataFile")
        self._descriptorFile[index] = value
    def export(self, outfile, level, name_='XSDataInputMeasureOffsetSift'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputMeasureOffsetSift'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for descriptorFile_ in self.getDescriptorFile():
            descriptorFile_.export(outfile, level, name_='descriptorFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'descriptorFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.descriptorFile.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputMeasureOffsetSift" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputMeasureOffsetSift' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputMeasureOffsetSift is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputMeasureOffsetSift.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputMeasureOffsetSift()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputMeasureOffsetSift" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputMeasureOffsetSift()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputMeasureOffsetSift

class XSDataInputShiftImage(XSDataInput):
    def __init__(self, configuration=None, panoFile=None, outputImage=None, offset=None, invertCorrection=None, inputImage=None, inputArray=None, index=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", index, "XSDataInteger")
        self._index = index
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", inputArray, "XSDataArray")
        self._inputArray = inputArray
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", inputImage, "XSDataImageExt")
        self._inputImage = inputImage
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", invertCorrection, "XSDataBoolean")
        self._invertCorrection = invertCorrection
        if offset is None:
            self._offset = []
        else:
            checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", offset, "list")
            self._offset = offset
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
        checkType("XSDataInputShiftImage", "Constructor of XSDataInputShiftImage", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def getIndex(self): return self._index
    def setIndex(self, index):
        checkType("XSDataInputShiftImage", "setIndex", index, "XSDataInteger")
        self._index = index
    def delIndex(self): self._index = None
    # Properties
    index = property(getIndex, setIndex, delIndex, "Property for index")
    def getInputArray(self): return self._inputArray
    def setInputArray(self, inputArray):
        checkType("XSDataInputShiftImage", "setInputArray", inputArray, "XSDataArray")
        self._inputArray = inputArray
    def delInputArray(self): self._inputArray = None
    # Properties
    inputArray = property(getInputArray, setInputArray, delInputArray, "Property for inputArray")
    def getInputImage(self): return self._inputImage
    def setInputImage(self, inputImage):
        checkType("XSDataInputShiftImage", "setInputImage", inputImage, "XSDataImageExt")
        self._inputImage = inputImage
    def delInputImage(self): self._inputImage = None
    # Properties
    inputImage = property(getInputImage, setInputImage, delInputImage, "Property for inputImage")
    def getInvertCorrection(self): return self._invertCorrection
    def setInvertCorrection(self, invertCorrection):
        checkType("XSDataInputShiftImage", "setInvertCorrection", invertCorrection, "XSDataBoolean")
        self._invertCorrection = invertCorrection
    def delInvertCorrection(self): self._invertCorrection = None
    # Properties
    invertCorrection = property(getInvertCorrection, setInvertCorrection, delInvertCorrection, "Property for invertCorrection")
    def getOffset(self): return self._offset
    def setOffset(self, offset):
        checkType("XSDataInputShiftImage", "setOffset", offset, "list")
        self._offset = offset
    def delOffset(self): self._offset = None
    # Properties
    offset = property(getOffset, setOffset, delOffset, "Property for offset")
    def addOffset(self, value):
        checkType("XSDataInputShiftImage", "setOffset", value, "XSDataDouble")
        self._offset.append(value)
    def insertOffset(self, index, value):
        checkType("XSDataInputShiftImage", "setOffset", value, "XSDataDouble")
        self._offset[index] = value
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataInputShiftImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def getPanoFile(self): return self._panoFile
    def setPanoFile(self, panoFile):
        checkType("XSDataInputShiftImage", "setPanoFile", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def delPanoFile(self): self._panoFile = None
    # Properties
    panoFile = property(getPanoFile, setPanoFile, delPanoFile, "Property for panoFile")
    def export(self, outfile, level, name_='XSDataInputShiftImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputShiftImage'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._index is not None:
            self.index.export(outfile, level, name_='index')
        if self._inputArray is not None:
            self.inputArray.export(outfile, level, name_='inputArray')
        if self._inputImage is not None:
            self.inputImage.export(outfile, level, name_='inputImage')
        if self._invertCorrection is not None:
            self.invertCorrection.export(outfile, level, name_='invertCorrection')
        for offset_ in self.getOffset():
            offset_.export(outfile, level, name_='offset')
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
        if self._panoFile is not None:
            self.panoFile.export(outfile, level, name_='panoFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'index':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIndex(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setInputArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setInputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'invertCorrection':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setInvertCorrection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'offset':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.offset.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'panoFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPanoFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputShiftImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputShiftImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputShiftImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputShiftImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputShiftImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputShiftImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputShiftImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputShiftImage

class XSDataInputSiftDescriptor(XSDataInput):
    def __init__(self, configuration=None, image=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputSiftDescriptor", "Constructor of XSDataInputSiftDescriptor", image, "XSDataImageExt")
        self._image = image
    def getImage(self): return self._image
    def setImage(self, image):
        checkType("XSDataInputSiftDescriptor", "setImage", image, "XSDataImageExt")
        self._image = image
    def delImage(self): self._image = None
    # Properties
    image = property(getImage, setImage, delImage, "Property for image")
    def export(self, outfile, level, name_='XSDataInputSiftDescriptor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSiftDescriptor'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataImageExt")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSiftDescriptor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSiftDescriptor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSiftDescriptor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSiftDescriptor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSiftDescriptor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSiftDescriptor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSiftDescriptor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSiftDescriptor

class XSDataInputStitchImage(XSDataInput):
    def __init__(self, configuration=None, mask=None, blending=None, widthROI=None, centerROI=None, deltaDummy=None, dummyValue=None, autoscale=None, outputImage=None, inputImages=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputImages is None:
            self._inputImages = []
        else:
            checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", inputImages, "list")
            self._inputImages = inputImages
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", autoscale, "XSDataBoolean")
        self._autoscale = autoscale
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", deltaDummy, "XSDataDouble")
        self._deltaDummy = deltaDummy
        if centerROI is None:
            self._centerROI = []
        else:
            checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", centerROI, "list")
            self._centerROI = centerROI
        if widthROI is None:
            self._widthROI = []
        else:
            checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", widthROI, "list")
            self._widthROI = widthROI
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", blending, "XSDataString")
        self._blending = blending
        checkType("XSDataInputStitchImage", "Constructor of XSDataInputStitchImage", mask, "XSDataImageExt")
        self._mask = mask
    def getInputImages(self): return self._inputImages
    def setInputImages(self, inputImages):
        checkType("XSDataInputStitchImage", "setInputImages", inputImages, "list")
        self._inputImages = inputImages
    def delInputImages(self): self._inputImages = None
    # Properties
    inputImages = property(getInputImages, setInputImages, delInputImages, "Property for inputImages")
    def addInputImages(self, value):
        checkType("XSDataInputStitchImage", "setInputImages", value, "XSDataImageExt")
        self._inputImages.append(value)
    def insertInputImages(self, index, value):
        checkType("XSDataInputStitchImage", "setInputImages", value, "XSDataImageExt")
        self._inputImages[index] = value
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataInputStitchImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def getAutoscale(self): return self._autoscale
    def setAutoscale(self, autoscale):
        checkType("XSDataInputStitchImage", "setAutoscale", autoscale, "XSDataBoolean")
        self._autoscale = autoscale
    def delAutoscale(self): self._autoscale = None
    # Properties
    autoscale = property(getAutoscale, setAutoscale, delAutoscale, "Property for autoscale")
    def getDummyValue(self): return self._dummyValue
    def setDummyValue(self, dummyValue):
        checkType("XSDataInputStitchImage", "setDummyValue", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
    def delDummyValue(self): self._dummyValue = None
    # Properties
    dummyValue = property(getDummyValue, setDummyValue, delDummyValue, "Property for dummyValue")
    def getDeltaDummy(self): return self._deltaDummy
    def setDeltaDummy(self, deltaDummy):
        checkType("XSDataInputStitchImage", "setDeltaDummy", deltaDummy, "XSDataDouble")
        self._deltaDummy = deltaDummy
    def delDeltaDummy(self): self._deltaDummy = None
    # Properties
    deltaDummy = property(getDeltaDummy, setDeltaDummy, delDeltaDummy, "Property for deltaDummy")
    def getCenterROI(self): return self._centerROI
    def setCenterROI(self, centerROI):
        checkType("XSDataInputStitchImage", "setCenterROI", centerROI, "list")
        self._centerROI = centerROI
    def delCenterROI(self): self._centerROI = None
    # Properties
    centerROI = property(getCenterROI, setCenterROI, delCenterROI, "Property for centerROI")
    def addCenterROI(self, value):
        checkType("XSDataInputStitchImage", "setCenterROI", value, "XSDataInteger")
        self._centerROI.append(value)
    def insertCenterROI(self, index, value):
        checkType("XSDataInputStitchImage", "setCenterROI", value, "XSDataInteger")
        self._centerROI[index] = value
    def getWidthROI(self): return self._widthROI
    def setWidthROI(self, widthROI):
        checkType("XSDataInputStitchImage", "setWidthROI", widthROI, "list")
        self._widthROI = widthROI
    def delWidthROI(self): self._widthROI = None
    # Properties
    widthROI = property(getWidthROI, setWidthROI, delWidthROI, "Property for widthROI")
    def addWidthROI(self, value):
        checkType("XSDataInputStitchImage", "setWidthROI", value, "XSDataInteger")
        self._widthROI.append(value)
    def insertWidthROI(self, index, value):
        checkType("XSDataInputStitchImage", "setWidthROI", value, "XSDataInteger")
        self._widthROI[index] = value
    def getBlending(self): return self._blending
    def setBlending(self, blending):
        checkType("XSDataInputStitchImage", "setBlending", blending, "XSDataString")
        self._blending = blending
    def delBlending(self): self._blending = None
    # Properties
    blending = property(getBlending, setBlending, delBlending, "Property for blending")
    def getMask(self): return self._mask
    def setMask(self, mask):
        checkType("XSDataInputStitchImage", "setMask", mask, "XSDataImageExt")
        self._mask = mask
    def delMask(self): self._mask = None
    # Properties
    mask = property(getMask, setMask, delMask, "Property for mask")
    def export(self, outfile, level, name_='XSDataInputStitchImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStitchImage'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputImages_ in self.getInputImages():
            inputImages_.export(outfile, level, name_='inputImages')
        if self.getInputImages() == []:
            warnEmptyAttribute("inputImages", "XSDataImageExt")
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
        if self._autoscale is not None:
            self.autoscale.export(outfile, level, name_='autoscale')
        if self._dummyValue is not None:
            self.dummyValue.export(outfile, level, name_='dummyValue')
        if self._deltaDummy is not None:
            self.deltaDummy.export(outfile, level, name_='deltaDummy')
        for centerROI_ in self.getCenterROI():
            centerROI_.export(outfile, level, name_='centerROI')
        for widthROI_ in self.getWidthROI():
            widthROI_.export(outfile, level, name_='widthROI')
        if self._blending is not None:
            self.blending.export(outfile, level, name_='blending')
        if self._mask is not None:
            self.mask.export(outfile, level, name_='mask')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputImages':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.inputImages.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoscale':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAutoscale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dummyValue':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDummyValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deltaDummy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDeltaDummy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'centerROI':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.centerROI.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'widthROI':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.widthROI.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blending':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBlending(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mask':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setMask(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStitchImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStitchImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStitchImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStitchImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStitchImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStitchImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStitchImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStitchImage

class XSDataInputStitchOffsetedImage(XSDataInput):
    """Dummy is the value of pixels that are still invalid after stitching.
Blending can be: max, min or mean (default)."""
    def __init__(self, configuration=None, mask=None, blending=None, widthROI=None, centerROI=None, dummyValue=None, autoscale=None, outputImage=None, inputImages=None):
        XSDataInput.__init__(self, configuration)
    
    
        if inputImages is None:
            self._inputImages = []
        else:
            checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", inputImages, "list")
            self._inputImages = inputImages
        checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
        checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", autoscale, "XSDataBoolean")
        self._autoscale = autoscale
        checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
        if centerROI is None:
            self._centerROI = []
        else:
            checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", centerROI, "list")
            self._centerROI = centerROI
        if widthROI is None:
            self._widthROI = []
        else:
            checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", widthROI, "list")
            self._widthROI = widthROI
        checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", blending, "XSDataString")
        self._blending = blending
        checkType("XSDataInputStitchOffsetedImage", "Constructor of XSDataInputStitchOffsetedImage", mask, "XSDataImageExt")
        self._mask = mask
    def getInputImages(self): return self._inputImages
    def setInputImages(self, inputImages):
        checkType("XSDataInputStitchOffsetedImage", "setInputImages", inputImages, "list")
        self._inputImages = inputImages
    def delInputImages(self): self._inputImages = None
    # Properties
    inputImages = property(getInputImages, setInputImages, delInputImages, "Property for inputImages")
    def addInputImages(self, value):
        checkType("XSDataInputStitchOffsetedImage", "setInputImages", value, "OffsetedImage")
        self._inputImages.append(value)
    def insertInputImages(self, index, value):
        checkType("XSDataInputStitchOffsetedImage", "setInputImages", value, "OffsetedImage")
        self._inputImages[index] = value
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataInputStitchOffsetedImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def getAutoscale(self): return self._autoscale
    def setAutoscale(self, autoscale):
        checkType("XSDataInputStitchOffsetedImage", "setAutoscale", autoscale, "XSDataBoolean")
        self._autoscale = autoscale
    def delAutoscale(self): self._autoscale = None
    # Properties
    autoscale = property(getAutoscale, setAutoscale, delAutoscale, "Property for autoscale")
    def getDummyValue(self): return self._dummyValue
    def setDummyValue(self, dummyValue):
        checkType("XSDataInputStitchOffsetedImage", "setDummyValue", dummyValue, "XSDataDouble")
        self._dummyValue = dummyValue
    def delDummyValue(self): self._dummyValue = None
    # Properties
    dummyValue = property(getDummyValue, setDummyValue, delDummyValue, "Property for dummyValue")
    def getCenterROI(self): return self._centerROI
    def setCenterROI(self, centerROI):
        checkType("XSDataInputStitchOffsetedImage", "setCenterROI", centerROI, "list")
        self._centerROI = centerROI
    def delCenterROI(self): self._centerROI = None
    # Properties
    centerROI = property(getCenterROI, setCenterROI, delCenterROI, "Property for centerROI")
    def addCenterROI(self, value):
        checkType("XSDataInputStitchOffsetedImage", "setCenterROI", value, "XSDataInteger")
        self._centerROI.append(value)
    def insertCenterROI(self, index, value):
        checkType("XSDataInputStitchOffsetedImage", "setCenterROI", value, "XSDataInteger")
        self._centerROI[index] = value
    def getWidthROI(self): return self._widthROI
    def setWidthROI(self, widthROI):
        checkType("XSDataInputStitchOffsetedImage", "setWidthROI", widthROI, "list")
        self._widthROI = widthROI
    def delWidthROI(self): self._widthROI = None
    # Properties
    widthROI = property(getWidthROI, setWidthROI, delWidthROI, "Property for widthROI")
    def addWidthROI(self, value):
        checkType("XSDataInputStitchOffsetedImage", "setWidthROI", value, "XSDataInteger")
        self._widthROI.append(value)
    def insertWidthROI(self, index, value):
        checkType("XSDataInputStitchOffsetedImage", "setWidthROI", value, "XSDataInteger")
        self._widthROI[index] = value
    def getBlending(self): return self._blending
    def setBlending(self, blending):
        checkType("XSDataInputStitchOffsetedImage", "setBlending", blending, "XSDataString")
        self._blending = blending
    def delBlending(self): self._blending = None
    # Properties
    blending = property(getBlending, setBlending, delBlending, "Property for blending")
    def getMask(self): return self._mask
    def setMask(self, mask):
        checkType("XSDataInputStitchOffsetedImage", "setMask", mask, "XSDataImageExt")
        self._mask = mask
    def delMask(self): self._mask = None
    # Properties
    mask = property(getMask, setMask, delMask, "Property for mask")
    def export(self, outfile, level, name_='XSDataInputStitchOffsetedImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStitchOffsetedImage'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputImages_ in self.getInputImages():
            inputImages_.export(outfile, level, name_='inputImages')
        if self.getInputImages() == []:
            warnEmptyAttribute("inputImages", "OffsetedImage")
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
        if self._autoscale is not None:
            self.autoscale.export(outfile, level, name_='autoscale')
        if self._dummyValue is not None:
            self.dummyValue.export(outfile, level, name_='dummyValue')
        else:
            warnEmptyAttribute("dummyValue", "XSDataDouble")
        for centerROI_ in self.getCenterROI():
            centerROI_.export(outfile, level, name_='centerROI')
        for widthROI_ in self.getWidthROI():
            widthROI_.export(outfile, level, name_='widthROI')
        if self._blending is not None:
            self.blending.export(outfile, level, name_='blending')
        if self._mask is not None:
            self.mask.export(outfile, level, name_='mask')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputImages':
            obj_ = OffsetedImage()
            obj_.build(child_)
            self.inputImages.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoscale':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAutoscale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dummyValue':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDummyValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'centerROI':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.centerROI.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'widthROI':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.widthROI.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blending':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBlending(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mask':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setMask(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStitchOffsetedImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStitchOffsetedImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStitchOffsetedImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStitchOffsetedImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStitchOffsetedImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStitchOffsetedImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStitchOffsetedImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStitchOffsetedImage

class XSDataResultMeasureOffset(XSDataResult):
    def __init__(self, status=None, panoFile=None, offset=None):
        XSDataResult.__init__(self, status)
    
    
        if offset is None:
            self._offset = []
        else:
            checkType("XSDataResultMeasureOffset", "Constructor of XSDataResultMeasureOffset", offset, "list")
            self._offset = offset
        checkType("XSDataResultMeasureOffset", "Constructor of XSDataResultMeasureOffset", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def getOffset(self): return self._offset
    def setOffset(self, offset):
        checkType("XSDataResultMeasureOffset", "setOffset", offset, "list")
        self._offset = offset
    def delOffset(self): self._offset = None
    # Properties
    offset = property(getOffset, setOffset, delOffset, "Property for offset")
    def addOffset(self, value):
        checkType("XSDataResultMeasureOffset", "setOffset", value, "XSDataDouble")
        self._offset.append(value)
    def insertOffset(self, index, value):
        checkType("XSDataResultMeasureOffset", "setOffset", value, "XSDataDouble")
        self._offset[index] = value
    def getPanoFile(self): return self._panoFile
    def setPanoFile(self, panoFile):
        checkType("XSDataResultMeasureOffset", "setPanoFile", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def delPanoFile(self): self._panoFile = None
    # Properties
    panoFile = property(getPanoFile, setPanoFile, delPanoFile, "Property for panoFile")
    def export(self, outfile, level, name_='XSDataResultMeasureOffset'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultMeasureOffset'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for offset_ in self.getOffset():
            offset_.export(outfile, level, name_='offset')
        if self.getOffset() == []:
            warnEmptyAttribute("offset", "XSDataDouble")
        if self._panoFile is not None:
            self.panoFile.export(outfile, level, name_='panoFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'offset':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.offset.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'panoFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPanoFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultMeasureOffset" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultMeasureOffset' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultMeasureOffset is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultMeasureOffset.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultMeasureOffset()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultMeasureOffset" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultMeasureOffset()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultMeasureOffset

class XSDataResultMeasureOffsetSift(XSDataResult):
    def __init__(self, status=None, panoFile=None, outputArray=None):
        XSDataResult.__init__(self, status)
    
    
        if outputArray is None:
            self._outputArray = []
        else:
            checkType("XSDataResultMeasureOffsetSift", "Constructor of XSDataResultMeasureOffsetSift", outputArray, "list")
            self._outputArray = outputArray
        checkType("XSDataResultMeasureOffsetSift", "Constructor of XSDataResultMeasureOffsetSift", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def getOutputArray(self): return self._outputArray
    def setOutputArray(self, outputArray):
        checkType("XSDataResultMeasureOffsetSift", "setOutputArray", outputArray, "list")
        self._outputArray = outputArray
    def delOutputArray(self): self._outputArray = None
    # Properties
    outputArray = property(getOutputArray, setOutputArray, delOutputArray, "Property for outputArray")
    def addOutputArray(self, value):
        checkType("XSDataResultMeasureOffsetSift", "setOutputArray", value, "XSDataArray")
        self._outputArray.append(value)
    def insertOutputArray(self, index, value):
        checkType("XSDataResultMeasureOffsetSift", "setOutputArray", value, "XSDataArray")
        self._outputArray[index] = value
    def getPanoFile(self): return self._panoFile
    def setPanoFile(self, panoFile):
        checkType("XSDataResultMeasureOffsetSift", "setPanoFile", panoFile, "XSDataFile")
        self._panoFile = panoFile
    def delPanoFile(self): self._panoFile = None
    # Properties
    panoFile = property(getPanoFile, setPanoFile, delPanoFile, "Property for panoFile")
    def export(self, outfile, level, name_='XSDataResultMeasureOffsetSift'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultMeasureOffsetSift'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for outputArray_ in self.getOutputArray():
            outputArray_.export(outfile, level, name_='outputArray')
        if self.getOutputArray() == []:
            warnEmptyAttribute("outputArray", "XSDataArray")
        if self._panoFile is not None:
            self.panoFile.export(outfile, level, name_='panoFile')
        else:
            warnEmptyAttribute("panoFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.outputArray.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'panoFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPanoFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultMeasureOffsetSift" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultMeasureOffsetSift' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultMeasureOffsetSift is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultMeasureOffsetSift.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultMeasureOffsetSift()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultMeasureOffsetSift" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultMeasureOffsetSift()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultMeasureOffsetSift

class XSDataResultShiftImage(XSDataResult):
    """Export as array by default unless an output filename is provided.
Correction can be either a simple global shift or a transformation based on a cubic spline if a panoFile (.pto) is provided.
The correction can be inverted if needed. """
    def __init__(self, status=None, outputImage=None, outputArray=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultShiftImage", "Constructor of XSDataResultShiftImage", outputArray, "XSDataArray")
        self._outputArray = outputArray
        checkType("XSDataResultShiftImage", "Constructor of XSDataResultShiftImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def getOutputArray(self): return self._outputArray
    def setOutputArray(self, outputArray):
        checkType("XSDataResultShiftImage", "setOutputArray", outputArray, "XSDataArray")
        self._outputArray = outputArray
    def delOutputArray(self): self._outputArray = None
    # Properties
    outputArray = property(getOutputArray, setOutputArray, delOutputArray, "Property for outputArray")
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataResultShiftImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def export(self, outfile, level, name_='XSDataResultShiftImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultShiftImage'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputArray is not None:
            self.outputArray.export(outfile, level, name_='outputArray')
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setOutputArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultShiftImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultShiftImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultShiftImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultShiftImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultShiftImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultShiftImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultShiftImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultShiftImage

class XSDataResultSiftDescriptor(XSDataResult):
    def __init__(self, status=None, descriptorFile=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultSiftDescriptor", "Constructor of XSDataResultSiftDescriptor", descriptorFile, "XSDataFile")
        self._descriptorFile = descriptorFile
    def getDescriptorFile(self): return self._descriptorFile
    def setDescriptorFile(self, descriptorFile):
        checkType("XSDataResultSiftDescriptor", "setDescriptorFile", descriptorFile, "XSDataFile")
        self._descriptorFile = descriptorFile
    def delDescriptorFile(self): self._descriptorFile = None
    # Properties
    descriptorFile = property(getDescriptorFile, setDescriptorFile, delDescriptorFile, "Property for descriptorFile")
    def export(self, outfile, level, name_='XSDataResultSiftDescriptor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSiftDescriptor'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._descriptorFile is not None:
            self.descriptorFile.export(outfile, level, name_='descriptorFile')
        else:
            warnEmptyAttribute("descriptorFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'descriptorFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDescriptorFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSiftDescriptor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSiftDescriptor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSiftDescriptor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSiftDescriptor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSiftDescriptor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSiftDescriptor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSiftDescriptor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSiftDescriptor

class XSDataResultStitchImage(XSDataResult):
    def __init__(self, status=None, outputImage=None, outputArray=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultStitchImage", "Constructor of XSDataResultStitchImage", outputArray, "XSDataArray")
        self._outputArray = outputArray
        checkType("XSDataResultStitchImage", "Constructor of XSDataResultStitchImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def getOutputArray(self): return self._outputArray
    def setOutputArray(self, outputArray):
        checkType("XSDataResultStitchImage", "setOutputArray", outputArray, "XSDataArray")
        self._outputArray = outputArray
    def delOutputArray(self): self._outputArray = None
    # Properties
    outputArray = property(getOutputArray, setOutputArray, delOutputArray, "Property for outputArray")
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataResultStitchImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def export(self, outfile, level, name_='XSDataResultStitchImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStitchImage'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputArray is not None:
            self.outputArray.export(outfile, level, name_='outputArray')
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setOutputArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStitchImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStitchImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStitchImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStitchImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStitchImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStitchImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStitchImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStitchImage

class XSDataResultStitchOffsetedImage(XSDataResult):
    def __init__(self, status=None, outputImage=None, outputArray=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResultStitchOffsetedImage", "Constructor of XSDataResultStitchOffsetedImage", outputArray, "XSDataArray")
        self._outputArray = outputArray
        checkType("XSDataResultStitchOffsetedImage", "Constructor of XSDataResultStitchOffsetedImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def getOutputArray(self): return self._outputArray
    def setOutputArray(self, outputArray):
        checkType("XSDataResultStitchOffsetedImage", "setOutputArray", outputArray, "XSDataArray")
        self._outputArray = outputArray
    def delOutputArray(self): self._outputArray = None
    # Properties
    outputArray = property(getOutputArray, setOutputArray, delOutputArray, "Property for outputArray")
    def getOutputImage(self): return self._outputImage
    def setOutputImage(self, outputImage):
        checkType("XSDataResultStitchOffsetedImage", "setOutputImage", outputImage, "XSDataImageExt")
        self._outputImage = outputImage
    def delOutputImage(self): self._outputImage = None
    # Properties
    outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
    def export(self, outfile, level, name_='XSDataResultStitchOffsetedImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStitchOffsetedImage'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputArray is not None:
            self.outputArray.export(outfile, level, name_='outputArray')
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_='outputImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setOutputArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputImage':
            obj_ = XSDataImageExt()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStitchOffsetedImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStitchOffsetedImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStitchOffsetedImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStitchOffsetedImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStitchOffsetedImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStitchOffsetedImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStitchOffsetedImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStitchOffsetedImage



# End of data representation classes.



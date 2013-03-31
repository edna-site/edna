#!/usr/bin/env python

#
# Generated Tue Nov 13 01:33::30 2012 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataFloat
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataMatrixDouble
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataWavelength
    from XSDataCommon import XSDataAngle
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataAngle




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



class XSDataMOSFLMDetector(object):
    def __init__(self, type=None, pixelSizeY=None, pixelSizeX=None, numberPixelY=None, numberPixelX=None):
        if numberPixelX is None:
            self._numberPixelX = None
        elif numberPixelX.__class__.__name__ == "XSDataInteger":
            self._numberPixelX = numberPixelX
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector constructor argument 'numberPixelX' is not XSDataInteger but %s" % self._numberPixelX.__class__.__name__
            raise BaseException(strMessage)
        if numberPixelY is None:
            self._numberPixelY = None
        elif numberPixelY.__class__.__name__ == "XSDataInteger":
            self._numberPixelY = numberPixelY
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector constructor argument 'numberPixelY' is not XSDataInteger but %s" % self._numberPixelY.__class__.__name__
            raise BaseException(strMessage)
        if pixelSizeX is None:
            self._pixelSizeX = None
        elif pixelSizeX.__class__.__name__ == "XSDataLength":
            self._pixelSizeX = pixelSizeX
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector constructor argument 'pixelSizeX' is not XSDataLength but %s" % self._pixelSizeX.__class__.__name__
            raise BaseException(strMessage)
        if pixelSizeY is None:
            self._pixelSizeY = None
        elif pixelSizeY.__class__.__name__ == "XSDataLength":
            self._pixelSizeY = pixelSizeY
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector constructor argument 'pixelSizeY' is not XSDataLength but %s" % self._pixelSizeY.__class__.__name__
            raise BaseException(strMessage)
        if type is None:
            self._type = None
        elif type.__class__.__name__ == "XSDataString":
            self._type = type
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector constructor argument 'type' is not XSDataString but %s" % self._type.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'numberPixelX' attribute
    def getNumberPixelX(self): return self._numberPixelX
    def setNumberPixelX(self, numberPixelX):
        if numberPixelX is None:
            self._numberPixelX = None
        elif numberPixelX.__class__.__name__ == "XSDataInteger":
            self._numberPixelX = numberPixelX
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector.setNumberPixelX argument is not XSDataInteger but %s" % numberPixelX.__class__.__name__
            raise BaseException(strMessage)
    def delNumberPixelX(self): self._numberPixelX = None
    numberPixelX = property(getNumberPixelX, setNumberPixelX, delNumberPixelX, "Property for numberPixelX")
    # Methods and properties for the 'numberPixelY' attribute
    def getNumberPixelY(self): return self._numberPixelY
    def setNumberPixelY(self, numberPixelY):
        if numberPixelY is None:
            self._numberPixelY = None
        elif numberPixelY.__class__.__name__ == "XSDataInteger":
            self._numberPixelY = numberPixelY
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector.setNumberPixelY argument is not XSDataInteger but %s" % numberPixelY.__class__.__name__
            raise BaseException(strMessage)
    def delNumberPixelY(self): self._numberPixelY = None
    numberPixelY = property(getNumberPixelY, setNumberPixelY, delNumberPixelY, "Property for numberPixelY")
    # Methods and properties for the 'pixelSizeX' attribute
    def getPixelSizeX(self): return self._pixelSizeX
    def setPixelSizeX(self, pixelSizeX):
        if pixelSizeX is None:
            self._pixelSizeX = None
        elif pixelSizeX.__class__.__name__ == "XSDataLength":
            self._pixelSizeX = pixelSizeX
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector.setPixelSizeX argument is not XSDataLength but %s" % pixelSizeX.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSizeX(self): self._pixelSizeX = None
    pixelSizeX = property(getPixelSizeX, setPixelSizeX, delPixelSizeX, "Property for pixelSizeX")
    # Methods and properties for the 'pixelSizeY' attribute
    def getPixelSizeY(self): return self._pixelSizeY
    def setPixelSizeY(self, pixelSizeY):
        if pixelSizeY is None:
            self._pixelSizeY = None
        elif pixelSizeY.__class__.__name__ == "XSDataLength":
            self._pixelSizeY = pixelSizeY
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector.setPixelSizeY argument is not XSDataLength but %s" % pixelSizeY.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSizeY(self): self._pixelSizeY = None
    pixelSizeY = property(getPixelSizeY, setPixelSizeY, delPixelSizeY, "Property for pixelSizeY")
    # Methods and properties for the 'type' attribute
    def getType(self): return self._type
    def setType(self, type):
        if type is None:
            self._type = None
        elif type.__class__.__name__ == "XSDataString":
            self._type = type
        else:
            strMessage = "ERROR! XSDataMOSFLMDetector.setType argument is not XSDataString but %s" % type.__class__.__name__
            raise BaseException(strMessage)
    def delType(self): self._type = None
    type = property(getType, setType, delType, "Property for type")
    def export(self, outfile, level, name_='XSDataMOSFLMDetector'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMDetector'):
        pass
        if self._numberPixelX is not None:
            self.numberPixelX.export(outfile, level, name_='numberPixelX')
        else:
            warnEmptyAttribute("numberPixelX", "XSDataInteger")
        if self._numberPixelY is not None:
            self.numberPixelY.export(outfile, level, name_='numberPixelY')
        else:
            warnEmptyAttribute("numberPixelY", "XSDataInteger")
        if self._pixelSizeX is not None:
            self.pixelSizeX.export(outfile, level, name_='pixelSizeX')
        else:
            warnEmptyAttribute("pixelSizeX", "XSDataLength")
        if self._pixelSizeY is not None:
            self.pixelSizeY.export(outfile, level, name_='pixelSizeY')
        else:
            warnEmptyAttribute("pixelSizeY", "XSDataLength")
        if self._type is not None:
            self.type.export(outfile, level, name_='type')
        else:
            warnEmptyAttribute("type", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberPixelX':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberPixelX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberPixelY':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberPixelY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSizeX':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSizeX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSizeY':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSizeY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setType(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMDetector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMDetector' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMDetector is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMDetector.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMDetector()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMDetector" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMDetector()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMDetector


class XSDataCell(XSData):
    def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
        XSData.__init__(self, )
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_alpha' is not XSDataAngle but %s" % self._angle_alpha.__class__.__name__
            raise BaseException(strMessage)
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_beta' is not XSDataAngle but %s" % self._angle_beta.__class__.__name__
            raise BaseException(strMessage)
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_gamma' is not XSDataAngle but %s" % self._angle_gamma.__class__.__name__
            raise BaseException(strMessage)
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_a' is not XSDataLength but %s" % self._length_a.__class__.__name__
            raise BaseException(strMessage)
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_b' is not XSDataLength but %s" % self._length_b.__class__.__name__
            raise BaseException(strMessage)
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_c' is not XSDataLength but %s" % self._length_c.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angle_alpha' attribute
    def getAngle_alpha(self): return self._angle_alpha
    def setAngle_alpha(self, angle_alpha):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell.setAngle_alpha argument is not XSDataAngle but %s" % angle_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_alpha(self): self._angle_alpha = None
    angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
    # Methods and properties for the 'angle_beta' attribute
    def getAngle_beta(self): return self._angle_beta
    def setAngle_beta(self, angle_beta):
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataCell.setAngle_beta argument is not XSDataAngle but %s" % angle_beta.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_beta(self): self._angle_beta = None
    angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
    # Methods and properties for the 'angle_gamma' attribute
    def getAngle_gamma(self): return self._angle_gamma
    def setAngle_gamma(self, angle_gamma):
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataCell.setAngle_gamma argument is not XSDataAngle but %s" % angle_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_gamma(self): self._angle_gamma = None
    angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
    # Methods and properties for the 'length_a' attribute
    def getLength_a(self): return self._length_a
    def setLength_a(self, length_a):
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataCell.setLength_a argument is not XSDataLength but %s" % length_a.__class__.__name__
            raise BaseException(strMessage)
    def delLength_a(self): self._length_a = None
    length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
    # Methods and properties for the 'length_b' attribute
    def getLength_b(self): return self._length_b
    def setLength_b(self, length_b):
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataCell.setLength_b argument is not XSDataLength but %s" % length_b.__class__.__name__
            raise BaseException(strMessage)
    def delLength_b(self): self._length_b = None
    length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
    # Methods and properties for the 'length_c' attribute
    def getLength_c(self): return self._length_c
    def setLength_c(self, length_c):
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataCell.setLength_c argument is not XSDataLength but %s" % length_c.__class__.__name__
            raise BaseException(strMessage)
    def delLength_c(self): self._length_c = None
    length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
    def export(self, outfile, level, name_='XSDataCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataCell'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._angle_alpha is not None:
            self.angle_alpha.export(outfile, level, name_='angle_alpha')
        else:
            warnEmptyAttribute("angle_alpha", "XSDataAngle")
        if self._angle_beta is not None:
            self.angle_beta.export(outfile, level, name_='angle_beta')
        else:
            warnEmptyAttribute("angle_beta", "XSDataAngle")
        if self._angle_gamma is not None:
            self.angle_gamma.export(outfile, level, name_='angle_gamma')
        else:
            warnEmptyAttribute("angle_gamma", "XSDataAngle")
        if self._length_a is not None:
            self.length_a.export(outfile, level, name_='length_a')
        else:
            warnEmptyAttribute("length_a", "XSDataLength")
        if self._length_b is not None:
            self.length_b.export(outfile, level, name_='length_b')
        else:
            warnEmptyAttribute("length_b", "XSDataLength")
        if self._length_c is not None:
            self.length_c.export(outfile, level, name_='length_c')
        else:
            warnEmptyAttribute("length_c", "XSDataLength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_alpha':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_beta':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_gamma':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_a':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_b':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_c':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_c(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataCell


class XSDataMOSFLMBeamPosition(XSData):
    def __init__(self, y=None, x=None):
        XSData.__init__(self, )
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataLength":
            self._x = x
        else:
            strMessage = "ERROR! XSDataMOSFLMBeamPosition constructor argument 'x' is not XSDataLength but %s" % self._x.__class__.__name__
            raise BaseException(strMessage)
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataLength":
            self._y = y
        else:
            strMessage = "ERROR! XSDataMOSFLMBeamPosition constructor argument 'y' is not XSDataLength but %s" % self._y.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'x' attribute
    def getX(self): return self._x
    def setX(self, x):
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataLength":
            self._x = x
        else:
            strMessage = "ERROR! XSDataMOSFLMBeamPosition.setX argument is not XSDataLength but %s" % x.__class__.__name__
            raise BaseException(strMessage)
    def delX(self): self._x = None
    x = property(getX, setX, delX, "Property for x")
    # Methods and properties for the 'y' attribute
    def getY(self): return self._y
    def setY(self, y):
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataLength":
            self._y = y
        else:
            strMessage = "ERROR! XSDataMOSFLMBeamPosition.setY argument is not XSDataLength but %s" % y.__class__.__name__
            raise BaseException(strMessage)
    def delY(self): self._y = None
    y = property(getY, setY, delY, "Property for y")
    def export(self, outfile, level, name_='XSDataMOSFLMBeamPosition'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMBeamPosition'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._x is not None:
            self.x.export(outfile, level, name_='x')
        else:
            warnEmptyAttribute("x", "XSDataLength")
        if self._y is not None:
            self.y.export(outfile, level, name_='y')
        else:
            warnEmptyAttribute("y", "XSDataLength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setY(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMBeamPosition" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMBeamPosition' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMBeamPosition is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMBeamPosition.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMBeamPosition()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMBeamPosition" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMBeamPosition()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMBeamPosition


class XSDataMOSFLMImage(XSData):
    def __init__(self, rotationAxisStart=None, rotationAxisEnd=None, number=None):
        XSData.__init__(self, )
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataMOSFLMImage constructor argument 'number' is not XSDataInteger but %s" % self._number.__class__.__name__
            raise BaseException(strMessage)
        if rotationAxisEnd is None:
            self._rotationAxisEnd = None
        elif rotationAxisEnd.__class__.__name__ == "XSDataAngle":
            self._rotationAxisEnd = rotationAxisEnd
        else:
            strMessage = "ERROR! XSDataMOSFLMImage constructor argument 'rotationAxisEnd' is not XSDataAngle but %s" % self._rotationAxisEnd.__class__.__name__
            raise BaseException(strMessage)
        if rotationAxisStart is None:
            self._rotationAxisStart = None
        elif rotationAxisStart.__class__.__name__ == "XSDataAngle":
            self._rotationAxisStart = rotationAxisStart
        else:
            strMessage = "ERROR! XSDataMOSFLMImage constructor argument 'rotationAxisStart' is not XSDataAngle but %s" % self._rotationAxisStart.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'number' attribute
    def getNumber(self): return self._number
    def setNumber(self, number):
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataMOSFLMImage.setNumber argument is not XSDataInteger but %s" % number.__class__.__name__
            raise BaseException(strMessage)
    def delNumber(self): self._number = None
    number = property(getNumber, setNumber, delNumber, "Property for number")
    # Methods and properties for the 'rotationAxisEnd' attribute
    def getRotationAxisEnd(self): return self._rotationAxisEnd
    def setRotationAxisEnd(self, rotationAxisEnd):
        if rotationAxisEnd is None:
            self._rotationAxisEnd = None
        elif rotationAxisEnd.__class__.__name__ == "XSDataAngle":
            self._rotationAxisEnd = rotationAxisEnd
        else:
            strMessage = "ERROR! XSDataMOSFLMImage.setRotationAxisEnd argument is not XSDataAngle but %s" % rotationAxisEnd.__class__.__name__
            raise BaseException(strMessage)
    def delRotationAxisEnd(self): self._rotationAxisEnd = None
    rotationAxisEnd = property(getRotationAxisEnd, setRotationAxisEnd, delRotationAxisEnd, "Property for rotationAxisEnd")
    # Methods and properties for the 'rotationAxisStart' attribute
    def getRotationAxisStart(self): return self._rotationAxisStart
    def setRotationAxisStart(self, rotationAxisStart):
        if rotationAxisStart is None:
            self._rotationAxisStart = None
        elif rotationAxisStart.__class__.__name__ == "XSDataAngle":
            self._rotationAxisStart = rotationAxisStart
        else:
            strMessage = "ERROR! XSDataMOSFLMImage.setRotationAxisStart argument is not XSDataAngle but %s" % rotationAxisStart.__class__.__name__
            raise BaseException(strMessage)
    def delRotationAxisStart(self): self._rotationAxisStart = None
    rotationAxisStart = property(getRotationAxisStart, setRotationAxisStart, delRotationAxisStart, "Property for rotationAxisStart")
    def export(self, outfile, level, name_='XSDataMOSFLMImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMImage'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._number is not None:
            self.number.export(outfile, level, name_='number')
        else:
            warnEmptyAttribute("number", "XSDataInteger")
        if self._rotationAxisEnd is not None:
            self.rotationAxisEnd.export(outfile, level, name_='rotationAxisEnd')
        else:
            warnEmptyAttribute("rotationAxisEnd", "XSDataAngle")
        if self._rotationAxisStart is not None:
            self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
        else:
            warnEmptyAttribute("rotationAxisStart", "XSDataAngle")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisEnd':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setRotationAxisEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisStart':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setRotationAxisStart(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMImage


class XSDataMOSFLMIndexingSolution(XSData):
    def __init__(self, penalty=None, lattice=None, index=None, cell=None):
        XSData.__init__(self, )
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataCell":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution constructor argument 'cell' is not XSDataCell but %s" % self._cell.__class__.__name__
            raise BaseException(strMessage)
        if index is None:
            self._index = None
        elif index.__class__.__name__ == "XSDataInteger":
            self._index = index
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution constructor argument 'index' is not XSDataInteger but %s" % self._index.__class__.__name__
            raise BaseException(strMessage)
        if lattice is None:
            self._lattice = None
        elif lattice.__class__.__name__ == "XSDataString":
            self._lattice = lattice
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution constructor argument 'lattice' is not XSDataString but %s" % self._lattice.__class__.__name__
            raise BaseException(strMessage)
        if penalty is None:
            self._penalty = None
        elif penalty.__class__.__name__ == "XSDataInteger":
            self._penalty = penalty
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution constructor argument 'penalty' is not XSDataInteger but %s" % self._penalty.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'cell' attribute
    def getCell(self): return self._cell
    def setCell(self, cell):
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataCell":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution.setCell argument is not XSDataCell but %s" % cell.__class__.__name__
            raise BaseException(strMessage)
    def delCell(self): self._cell = None
    cell = property(getCell, setCell, delCell, "Property for cell")
    # Methods and properties for the 'index' attribute
    def getIndex(self): return self._index
    def setIndex(self, index):
        if index is None:
            self._index = None
        elif index.__class__.__name__ == "XSDataInteger":
            self._index = index
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution.setIndex argument is not XSDataInteger but %s" % index.__class__.__name__
            raise BaseException(strMessage)
    def delIndex(self): self._index = None
    index = property(getIndex, setIndex, delIndex, "Property for index")
    # Methods and properties for the 'lattice' attribute
    def getLattice(self): return self._lattice
    def setLattice(self, lattice):
        if lattice is None:
            self._lattice = None
        elif lattice.__class__.__name__ == "XSDataString":
            self._lattice = lattice
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution.setLattice argument is not XSDataString but %s" % lattice.__class__.__name__
            raise BaseException(strMessage)
    def delLattice(self): self._lattice = None
    lattice = property(getLattice, setLattice, delLattice, "Property for lattice")
    # Methods and properties for the 'penalty' attribute
    def getPenalty(self): return self._penalty
    def setPenalty(self, penalty):
        if penalty is None:
            self._penalty = None
        elif penalty.__class__.__name__ == "XSDataInteger":
            self._penalty = penalty
        else:
            strMessage = "ERROR! XSDataMOSFLMIndexingSolution.setPenalty argument is not XSDataInteger but %s" % penalty.__class__.__name__
            raise BaseException(strMessage)
    def delPenalty(self): self._penalty = None
    penalty = property(getPenalty, setPenalty, delPenalty, "Property for penalty")
    def export(self, outfile, level, name_='XSDataMOSFLMIndexingSolution'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMIndexingSolution'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._cell is not None:
            self.cell.export(outfile, level, name_='cell')
        else:
            warnEmptyAttribute("cell", "XSDataCell")
        if self._index is not None:
            self.index.export(outfile, level, name_='index')
        else:
            warnEmptyAttribute("index", "XSDataInteger")
        if self._lattice is not None:
            self.lattice.export(outfile, level, name_='lattice')
        else:
            warnEmptyAttribute("lattice", "XSDataString")
        if self._penalty is not None:
            self.penalty.export(outfile, level, name_='penalty')
        else:
            warnEmptyAttribute("penalty", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell':
            obj_ = XSDataCell()
            obj_.build(child_)
            self.setCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'index':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIndex(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lattice':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'penalty':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setPenalty(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMIndexingSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMIndexingSolution' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMIndexingSolution is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMIndexingSolution.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIndexingSolution()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIndexingSolution" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIndexingSolution()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIndexingSolution


class XSDataMOSFLMIntegrationStatistics(XSData):
    def __init__(self, numberOfReflections=None, averageSigma=None, averageIOverSigma=None, averageIntensity=None):
        XSData.__init__(self, )
        if averageIntensity is None:
            self._averageIntensity = None
        elif averageIntensity.__class__.__name__ == "XSDataFloat":
            self._averageIntensity = averageIntensity
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics constructor argument 'averageIntensity' is not XSDataFloat but %s" % self._averageIntensity.__class__.__name__
            raise BaseException(strMessage)
        if averageIOverSigma is None:
            self._averageIOverSigma = None
        elif averageIOverSigma.__class__.__name__ == "XSDataFloat":
            self._averageIOverSigma = averageIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics constructor argument 'averageIOverSigma' is not XSDataFloat but %s" % self._averageIOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if averageSigma is None:
            self._averageSigma = None
        elif averageSigma.__class__.__name__ == "XSDataFloat":
            self._averageSigma = averageSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics constructor argument 'averageSigma' is not XSDataFloat but %s" % self._averageSigma.__class__.__name__
            raise BaseException(strMessage)
        if numberOfReflections is None:
            self._numberOfReflections = None
        elif numberOfReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfReflections = numberOfReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics constructor argument 'numberOfReflections' is not XSDataInteger but %s" % self._numberOfReflections.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'averageIntensity' attribute
    def getAverageIntensity(self): return self._averageIntensity
    def setAverageIntensity(self, averageIntensity):
        if averageIntensity is None:
            self._averageIntensity = None
        elif averageIntensity.__class__.__name__ == "XSDataFloat":
            self._averageIntensity = averageIntensity
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics.setAverageIntensity argument is not XSDataFloat but %s" % averageIntensity.__class__.__name__
            raise BaseException(strMessage)
    def delAverageIntensity(self): self._averageIntensity = None
    averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
    # Methods and properties for the 'averageIOverSigma' attribute
    def getAverageIOverSigma(self): return self._averageIOverSigma
    def setAverageIOverSigma(self, averageIOverSigma):
        if averageIOverSigma is None:
            self._averageIOverSigma = None
        elif averageIOverSigma.__class__.__name__ == "XSDataFloat":
            self._averageIOverSigma = averageIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics.setAverageIOverSigma argument is not XSDataFloat but %s" % averageIOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delAverageIOverSigma(self): self._averageIOverSigma = None
    averageIOverSigma = property(getAverageIOverSigma, setAverageIOverSigma, delAverageIOverSigma, "Property for averageIOverSigma")
    # Methods and properties for the 'averageSigma' attribute
    def getAverageSigma(self): return self._averageSigma
    def setAverageSigma(self, averageSigma):
        if averageSigma is None:
            self._averageSigma = None
        elif averageSigma.__class__.__name__ == "XSDataFloat":
            self._averageSigma = averageSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics.setAverageSigma argument is not XSDataFloat but %s" % averageSigma.__class__.__name__
            raise BaseException(strMessage)
    def delAverageSigma(self): self._averageSigma = None
    averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
    # Methods and properties for the 'numberOfReflections' attribute
    def getNumberOfReflections(self): return self._numberOfReflections
    def setNumberOfReflections(self, numberOfReflections):
        if numberOfReflections is None:
            self._numberOfReflections = None
        elif numberOfReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfReflections = numberOfReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatistics.setNumberOfReflections argument is not XSDataInteger but %s" % numberOfReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfReflections(self): self._numberOfReflections = None
    numberOfReflections = property(getNumberOfReflections, setNumberOfReflections, delNumberOfReflections, "Property for numberOfReflections")
    def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatistics'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatistics'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._averageIntensity is not None:
            self.averageIntensity.export(outfile, level, name_='averageIntensity')
        else:
            warnEmptyAttribute("averageIntensity", "XSDataFloat")
        if self._averageIOverSigma is not None:
            self.averageIOverSigma.export(outfile, level, name_='averageIOverSigma')
        else:
            warnEmptyAttribute("averageIOverSigma", "XSDataFloat")
        if self._averageSigma is not None:
            self.averageSigma.export(outfile, level, name_='averageSigma')
        else:
            warnEmptyAttribute("averageSigma", "XSDataFloat")
        if self._numberOfReflections is not None:
            self.numberOfReflections.export(outfile, level, name_='numberOfReflections')
        else:
            warnEmptyAttribute("numberOfReflections", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensity':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setAverageIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIOverSigma':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setAverageIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageSigma':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfReflections(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatistics" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatistics' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatistics is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMIntegrationStatistics.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatistics()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatistics" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatistics()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatistics


class XSDataMOSFLMIntegrationStatisticsPerReflectionType(XSData):
    def __init__(self, partials=None, fullyRecorded=None):
        XSData.__init__(self, )
        if fullyRecorded is None:
            self._fullyRecorded = None
        elif fullyRecorded.__class__.__name__ == "XSDataMOSFLMIntegrationStatistics":
            self._fullyRecorded = fullyRecorded
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerReflectionType constructor argument 'fullyRecorded' is not XSDataMOSFLMIntegrationStatistics but %s" % self._fullyRecorded.__class__.__name__
            raise BaseException(strMessage)
        if partials is None:
            self._partials = None
        elif partials.__class__.__name__ == "XSDataMOSFLMIntegrationStatistics":
            self._partials = partials
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerReflectionType constructor argument 'partials' is not XSDataMOSFLMIntegrationStatistics but %s" % self._partials.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fullyRecorded' attribute
    def getFullyRecorded(self): return self._fullyRecorded
    def setFullyRecorded(self, fullyRecorded):
        if fullyRecorded is None:
            self._fullyRecorded = None
        elif fullyRecorded.__class__.__name__ == "XSDataMOSFLMIntegrationStatistics":
            self._fullyRecorded = fullyRecorded
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerReflectionType.setFullyRecorded argument is not XSDataMOSFLMIntegrationStatistics but %s" % fullyRecorded.__class__.__name__
            raise BaseException(strMessage)
    def delFullyRecorded(self): self._fullyRecorded = None
    fullyRecorded = property(getFullyRecorded, setFullyRecorded, delFullyRecorded, "Property for fullyRecorded")
    # Methods and properties for the 'partials' attribute
    def getPartials(self): return self._partials
    def setPartials(self, partials):
        if partials is None:
            self._partials = None
        elif partials.__class__.__name__ == "XSDataMOSFLMIntegrationStatistics":
            self._partials = partials
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerReflectionType.setPartials argument is not XSDataMOSFLMIntegrationStatistics but %s" % partials.__class__.__name__
            raise BaseException(strMessage)
    def delPartials(self): self._partials = None
    partials = property(getPartials, setPartials, delPartials, "Property for partials")
    def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._fullyRecorded is not None:
            self.fullyRecorded.export(outfile, level, name_='fullyRecorded')
        else:
            warnEmptyAttribute("fullyRecorded", "XSDataMOSFLMIntegrationStatistics")
        if self._partials is not None:
            self.partials.export(outfile, level, name_='partials')
        else:
            warnEmptyAttribute("partials", "XSDataMOSFLMIntegrationStatistics")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fullyRecorded':
            obj_ = XSDataMOSFLMIntegrationStatistics()
            obj_.build(child_)
            self.setFullyRecorded(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'partials':
            obj_ = XSDataMOSFLMIntegrationStatistics()
            obj_.build(child_)
            self.setPartials(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerReflectionType" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatisticsPerReflectionType is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMIntegrationStatisticsPerReflectionType.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerReflectionType" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatisticsPerReflectionType


class XSDataMOSFLMIntegrationStatisticsPerResolutionBin(XSData):
    def __init__(self, summation=None, profileFitted=None, minResolution=None, maxResolution=None):
        XSData.__init__(self, )
        if maxResolution is None:
            self._maxResolution = None
        elif maxResolution.__class__.__name__ == "XSDataFloat":
            self._maxResolution = maxResolution
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin constructor argument 'maxResolution' is not XSDataFloat but %s" % self._maxResolution.__class__.__name__
            raise BaseException(strMessage)
        if minResolution is None:
            self._minResolution = None
        elif minResolution.__class__.__name__ == "XSDataFloat":
            self._minResolution = minResolution
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin constructor argument 'minResolution' is not XSDataFloat but %s" % self._minResolution.__class__.__name__
            raise BaseException(strMessage)
        if profileFitted is None:
            self._profileFitted = None
        elif profileFitted.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerReflectionType":
            self._profileFitted = profileFitted
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin constructor argument 'profileFitted' is not XSDataMOSFLMIntegrationStatisticsPerReflectionType but %s" % self._profileFitted.__class__.__name__
            raise BaseException(strMessage)
        if summation is None:
            self._summation = None
        elif summation.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerReflectionType":
            self._summation = summation
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin constructor argument 'summation' is not XSDataMOSFLMIntegrationStatisticsPerReflectionType but %s" % self._summation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'maxResolution' attribute
    def getMaxResolution(self): return self._maxResolution
    def setMaxResolution(self, maxResolution):
        if maxResolution is None:
            self._maxResolution = None
        elif maxResolution.__class__.__name__ == "XSDataFloat":
            self._maxResolution = maxResolution
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin.setMaxResolution argument is not XSDataFloat but %s" % maxResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMaxResolution(self): self._maxResolution = None
    maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
    # Methods and properties for the 'minResolution' attribute
    def getMinResolution(self): return self._minResolution
    def setMinResolution(self, minResolution):
        if minResolution is None:
            self._minResolution = None
        elif minResolution.__class__.__name__ == "XSDataFloat":
            self._minResolution = minResolution
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin.setMinResolution argument is not XSDataFloat but %s" % minResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMinResolution(self): self._minResolution = None
    minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
    # Methods and properties for the 'profileFitted' attribute
    def getProfileFitted(self): return self._profileFitted
    def setProfileFitted(self, profileFitted):
        if profileFitted is None:
            self._profileFitted = None
        elif profileFitted.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerReflectionType":
            self._profileFitted = profileFitted
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin.setProfileFitted argument is not XSDataMOSFLMIntegrationStatisticsPerReflectionType but %s" % profileFitted.__class__.__name__
            raise BaseException(strMessage)
    def delProfileFitted(self): self._profileFitted = None
    profileFitted = property(getProfileFitted, setProfileFitted, delProfileFitted, "Property for profileFitted")
    # Methods and properties for the 'summation' attribute
    def getSummation(self): return self._summation
    def setSummation(self, summation):
        if summation is None:
            self._summation = None
        elif summation.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerReflectionType":
            self._summation = summation
        else:
            strMessage = "ERROR! XSDataMOSFLMIntegrationStatisticsPerResolutionBin.setSummation argument is not XSDataMOSFLMIntegrationStatisticsPerReflectionType but %s" % summation.__class__.__name__
            raise BaseException(strMessage)
    def delSummation(self): self._summation = None
    summation = property(getSummation, setSummation, delSummation, "Property for summation")
    def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._maxResolution is not None:
            self.maxResolution.export(outfile, level, name_='maxResolution')
        if self._minResolution is not None:
            self.minResolution.export(outfile, level, name_='minResolution')
        if self._profileFitted is not None:
            self.profileFitted.export(outfile, level, name_='profileFitted')
        else:
            warnEmptyAttribute("profileFitted", "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
        if self._summation is not None:
            self.summation.export(outfile, level, name_='summation')
        else:
            warnEmptyAttribute("summation", "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxResolution':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setMaxResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minResolution':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setMinResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'profileFitted':
            obj_ = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
            obj_.build(child_)
            self.setProfileFitted(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'summation':
            obj_ = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
            obj_.build(child_)
            self.setSummation(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerResolutionBin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatisticsPerResolutionBin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMIntegrationStatisticsPerResolutionBin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerResolutionBin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatisticsPerResolutionBin


class XSDataMOSFLMMissettingsAngles(XSData):
    def __init__(self, phiz=None, phiy=None, phix=None):
        XSData.__init__(self, )
        if phix is None:
            self._phix = None
        elif phix.__class__.__name__ == "XSDataAngle":
            self._phix = phix
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles constructor argument 'phix' is not XSDataAngle but %s" % self._phix.__class__.__name__
            raise BaseException(strMessage)
        if phiy is None:
            self._phiy = None
        elif phiy.__class__.__name__ == "XSDataAngle":
            self._phiy = phiy
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles constructor argument 'phiy' is not XSDataAngle but %s" % self._phiy.__class__.__name__
            raise BaseException(strMessage)
        if phiz is None:
            self._phiz = None
        elif phiz.__class__.__name__ == "XSDataAngle":
            self._phiz = phiz
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles constructor argument 'phiz' is not XSDataAngle but %s" % self._phiz.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'phix' attribute
    def getPhix(self): return self._phix
    def setPhix(self, phix):
        if phix is None:
            self._phix = None
        elif phix.__class__.__name__ == "XSDataAngle":
            self._phix = phix
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles.setPhix argument is not XSDataAngle but %s" % phix.__class__.__name__
            raise BaseException(strMessage)
    def delPhix(self): self._phix = None
    phix = property(getPhix, setPhix, delPhix, "Property for phix")
    # Methods and properties for the 'phiy' attribute
    def getPhiy(self): return self._phiy
    def setPhiy(self, phiy):
        if phiy is None:
            self._phiy = None
        elif phiy.__class__.__name__ == "XSDataAngle":
            self._phiy = phiy
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles.setPhiy argument is not XSDataAngle but %s" % phiy.__class__.__name__
            raise BaseException(strMessage)
    def delPhiy(self): self._phiy = None
    phiy = property(getPhiy, setPhiy, delPhiy, "Property for phiy")
    # Methods and properties for the 'phiz' attribute
    def getPhiz(self): return self._phiz
    def setPhiz(self, phiz):
        if phiz is None:
            self._phiz = None
        elif phiz.__class__.__name__ == "XSDataAngle":
            self._phiz = phiz
        else:
            strMessage = "ERROR! XSDataMOSFLMMissettingsAngles.setPhiz argument is not XSDataAngle but %s" % phiz.__class__.__name__
            raise BaseException(strMessage)
    def delPhiz(self): self._phiz = None
    phiz = property(getPhiz, setPhiz, delPhiz, "Property for phiz")
    def export(self, outfile, level, name_='XSDataMOSFLMMissettingsAngles'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMMissettingsAngles'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._phix is not None:
            self.phix.export(outfile, level, name_='phix')
        else:
            warnEmptyAttribute("phix", "XSDataAngle")
        if self._phiy is not None:
            self.phiy.export(outfile, level, name_='phiy')
        else:
            warnEmptyAttribute("phiy", "XSDataAngle")
        if self._phiz is not None:
            self.phiz.export(outfile, level, name_='phiz')
        else:
            warnEmptyAttribute("phiz", "XSDataAngle")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phix':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiy':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhiy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiz':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhiz(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMMissettingsAngles" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMMissettingsAngles' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMMissettingsAngles is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMMissettingsAngles.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMMissettingsAngles()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMMissettingsAngles" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMMissettingsAngles()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMMissettingsAngles


class XSDataMOSFLMNewmat(XSData):
    def __init__(self, uMatrix=None, refinedCell=None, missettingAngles=None, aMatrix=None):
        XSData.__init__(self, )
        if aMatrix is None:
            self._aMatrix = None
        elif aMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._aMatrix = aMatrix
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat constructor argument 'aMatrix' is not XSDataMatrixDouble but %s" % self._aMatrix.__class__.__name__
            raise BaseException(strMessage)
        if missettingAngles is None:
            self._missettingAngles = None
        elif missettingAngles.__class__.__name__ == "XSDataMOSFLMMissettingsAngles":
            self._missettingAngles = missettingAngles
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat constructor argument 'missettingAngles' is not XSDataMOSFLMMissettingsAngles but %s" % self._missettingAngles.__class__.__name__
            raise BaseException(strMessage)
        if refinedCell is None:
            self._refinedCell = None
        elif refinedCell.__class__.__name__ == "XSDataCell":
            self._refinedCell = refinedCell
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat constructor argument 'refinedCell' is not XSDataCell but %s" % self._refinedCell.__class__.__name__
            raise BaseException(strMessage)
        if uMatrix is None:
            self._uMatrix = None
        elif uMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._uMatrix = uMatrix
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat constructor argument 'uMatrix' is not XSDataMatrixDouble but %s" % self._uMatrix.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'aMatrix' attribute
    def getAMatrix(self): return self._aMatrix
    def setAMatrix(self, aMatrix):
        if aMatrix is None:
            self._aMatrix = None
        elif aMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._aMatrix = aMatrix
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat.setAMatrix argument is not XSDataMatrixDouble but %s" % aMatrix.__class__.__name__
            raise BaseException(strMessage)
    def delAMatrix(self): self._aMatrix = None
    aMatrix = property(getAMatrix, setAMatrix, delAMatrix, "Property for aMatrix")
    # Methods and properties for the 'missettingAngles' attribute
    def getMissettingAngles(self): return self._missettingAngles
    def setMissettingAngles(self, missettingAngles):
        if missettingAngles is None:
            self._missettingAngles = None
        elif missettingAngles.__class__.__name__ == "XSDataMOSFLMMissettingsAngles":
            self._missettingAngles = missettingAngles
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat.setMissettingAngles argument is not XSDataMOSFLMMissettingsAngles but %s" % missettingAngles.__class__.__name__
            raise BaseException(strMessage)
    def delMissettingAngles(self): self._missettingAngles = None
    missettingAngles = property(getMissettingAngles, setMissettingAngles, delMissettingAngles, "Property for missettingAngles")
    # Methods and properties for the 'refinedCell' attribute
    def getRefinedCell(self): return self._refinedCell
    def setRefinedCell(self, refinedCell):
        if refinedCell is None:
            self._refinedCell = None
        elif refinedCell.__class__.__name__ == "XSDataCell":
            self._refinedCell = refinedCell
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat.setRefinedCell argument is not XSDataCell but %s" % refinedCell.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedCell(self): self._refinedCell = None
    refinedCell = property(getRefinedCell, setRefinedCell, delRefinedCell, "Property for refinedCell")
    # Methods and properties for the 'uMatrix' attribute
    def getUMatrix(self): return self._uMatrix
    def setUMatrix(self, uMatrix):
        if uMatrix is None:
            self._uMatrix = None
        elif uMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._uMatrix = uMatrix
        else:
            strMessage = "ERROR! XSDataMOSFLMNewmat.setUMatrix argument is not XSDataMatrixDouble but %s" % uMatrix.__class__.__name__
            raise BaseException(strMessage)
    def delUMatrix(self): self._uMatrix = None
    uMatrix = property(getUMatrix, setUMatrix, delUMatrix, "Property for uMatrix")
    def export(self, outfile, level, name_='XSDataMOSFLMNewmat'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMNewmat'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._aMatrix is not None:
            self.aMatrix.export(outfile, level, name_='aMatrix')
        else:
            warnEmptyAttribute("aMatrix", "XSDataMatrixDouble")
        if self._missettingAngles is not None:
            self.missettingAngles.export(outfile, level, name_='missettingAngles')
        else:
            warnEmptyAttribute("missettingAngles", "XSDataMOSFLMMissettingsAngles")
        if self._refinedCell is not None:
            self.refinedCell.export(outfile, level, name_='refinedCell')
        else:
            warnEmptyAttribute("refinedCell", "XSDataCell")
        if self._uMatrix is not None:
            self.uMatrix.export(outfile, level, name_='uMatrix')
        else:
            warnEmptyAttribute("uMatrix", "XSDataMatrixDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aMatrix':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setAMatrix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'missettingAngles':
            obj_ = XSDataMOSFLMMissettingsAngles()
            obj_.build(child_)
            self.setMissettingAngles(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell':
            obj_ = XSDataCell()
            obj_.build(child_)
            self.setRefinedCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'uMatrix':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setUMatrix(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMNewmat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMNewmat' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMNewmat is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMNewmat.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMNewmat()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMNewmat" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMNewmat()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMNewmat


class XSDataMOSFLMOutputGeneratePrediction(XSData):
    def __init__(self, pathToLogFile=None, predictionImage=None):
        XSData.__init__(self, )
        if predictionImage is None:
            self._predictionImage = None
        elif predictionImage.__class__.__name__ == "XSDataImage":
            self._predictionImage = predictionImage
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputGeneratePrediction constructor argument 'predictionImage' is not XSDataImage but %s" % self._predictionImage.__class__.__name__
            raise BaseException(strMessage)
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputGeneratePrediction constructor argument 'pathToLogFile' is not XSDataFile but %s" % self._pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'predictionImage' attribute
    def getPredictionImage(self): return self._predictionImage
    def setPredictionImage(self, predictionImage):
        if predictionImage is None:
            self._predictionImage = None
        elif predictionImage.__class__.__name__ == "XSDataImage":
            self._predictionImage = predictionImage
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputGeneratePrediction.setPredictionImage argument is not XSDataImage but %s" % predictionImage.__class__.__name__
            raise BaseException(strMessage)
    def delPredictionImage(self): self._predictionImage = None
    predictionImage = property(getPredictionImage, setPredictionImage, delPredictionImage, "Property for predictionImage")
    # Methods and properties for the 'pathToLogFile' attribute
    def getPathToLogFile(self): return self._pathToLogFile
    def setPathToLogFile(self, pathToLogFile):
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputGeneratePrediction.setPathToLogFile argument is not XSDataFile but %s" % pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToLogFile(self): self._pathToLogFile = None
    pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
    def export(self, outfile, level, name_='XSDataMOSFLMOutputGeneratePrediction'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputGeneratePrediction'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._predictionImage is not None:
            self.predictionImage.export(outfile, level, name_='predictionImage')
        else:
            warnEmptyAttribute("predictionImage", "XSDataImage")
        if self._pathToLogFile is not None:
            self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'predictionImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setPredictionImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToLogFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToLogFile(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMOutputGeneratePrediction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMOutputGeneratePrediction' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMOutputGeneratePrediction is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMOutputGeneratePrediction.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputGeneratePrediction()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputGeneratePrediction" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputGeneratePrediction()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputGeneratePrediction


class XSDataMOSFLMInput(XSDataInput):
    def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None):
        XSDataInput.__init__(self, configuration)
        if beam is None:
            self._beam = None
        elif beam.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._beam = beam
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'beam' is not XSDataMOSFLMBeamPosition but %s" % self._beam.__class__.__name__
            raise BaseException(strMessage)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataMOSFLMDetector":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'detector' is not XSDataMOSFLMDetector but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if directory is None:
            self._directory = None
        elif directory.__class__.__name__ == "XSDataString":
            self._directory = directory
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'directory' is not XSDataString but %s" % self._directory.__class__.__name__
            raise BaseException(strMessage)
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'distance' is not XSDataLength but %s" % self._distance.__class__.__name__
            raise BaseException(strMessage)
        if matrix is None:
            self._matrix = None
        elif matrix.__class__.__name__ == "XSDataMOSFLMNewmat":
            self._matrix = matrix
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'matrix' is not XSDataMOSFLMNewmat but %s" % self._matrix.__class__.__name__
            raise BaseException(strMessage)
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataDouble":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'mosaicity' is not XSDataDouble but %s" % self._mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'symmetry' is not XSDataString but %s" % self._symmetry.__class__.__name__
            raise BaseException(strMessage)
        if template is None:
            self._template = None
        elif template.__class__.__name__ == "XSDataString":
            self._template = template
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'template' is not XSDataString but %s" % self._template.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataMOSFLMInput constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'beam' attribute
    def getBeam(self): return self._beam
    def setBeam(self, beam):
        if beam is None:
            self._beam = None
        elif beam.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._beam = beam
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setBeam argument is not XSDataMOSFLMBeamPosition but %s" % beam.__class__.__name__
            raise BaseException(strMessage)
    def delBeam(self): self._beam = None
    beam = property(getBeam, setBeam, delBeam, "Property for beam")
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataMOSFLMDetector":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setDetector argument is not XSDataMOSFLMDetector but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'directory' attribute
    def getDirectory(self): return self._directory
    def setDirectory(self, directory):
        if directory is None:
            self._directory = None
        elif directory.__class__.__name__ == "XSDataString":
            self._directory = directory
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setDirectory argument is not XSDataString but %s" % directory.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory(self): self._directory = None
    directory = property(getDirectory, setDirectory, delDirectory, "Property for directory")
    # Methods and properties for the 'distance' attribute
    def getDistance(self): return self._distance
    def setDistance(self, distance):
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setDistance argument is not XSDataLength but %s" % distance.__class__.__name__
            raise BaseException(strMessage)
    def delDistance(self): self._distance = None
    distance = property(getDistance, setDistance, delDistance, "Property for distance")
    # Methods and properties for the 'matrix' attribute
    def getMatrix(self): return self._matrix
    def setMatrix(self, matrix):
        if matrix is None:
            self._matrix = None
        elif matrix.__class__.__name__ == "XSDataMOSFLMNewmat":
            self._matrix = matrix
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setMatrix argument is not XSDataMOSFLMNewmat but %s" % matrix.__class__.__name__
            raise BaseException(strMessage)
    def delMatrix(self): self._matrix = None
    matrix = property(getMatrix, setMatrix, delMatrix, "Property for matrix")
    # Methods and properties for the 'mosaicity' attribute
    def getMosaicity(self): return self._mosaicity
    def setMosaicity(self, mosaicity):
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataDouble":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setMosaicity argument is not XSDataDouble but %s" % mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicity(self): self._mosaicity = None
    mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
    # Methods and properties for the 'symmetry' attribute
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setSymmetry argument is not XSDataString but %s" % symmetry.__class__.__name__
            raise BaseException(strMessage)
    def delSymmetry(self): self._symmetry = None
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    # Methods and properties for the 'template' attribute
    def getTemplate(self): return self._template
    def setTemplate(self, template):
        if template is None:
            self._template = None
        elif template.__class__.__name__ == "XSDataString":
            self._template = template
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setTemplate argument is not XSDataString but %s" % template.__class__.__name__
            raise BaseException(strMessage)
    def delTemplate(self): self._template = None
    template = property(getTemplate, setTemplate, delTemplate, "Property for template")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataMOSFLMInput.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    def export(self, outfile, level, name_='XSDataMOSFLMInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._beam is not None:
            self.beam.export(outfile, level, name_='beam')
        else:
            warnEmptyAttribute("beam", "XSDataMOSFLMBeamPosition")
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        else:
            warnEmptyAttribute("detector", "XSDataMOSFLMDetector")
        if self._directory is not None:
            self.directory.export(outfile, level, name_='directory')
        else:
            warnEmptyAttribute("directory", "XSDataString")
        if self._distance is not None:
            self.distance.export(outfile, level, name_='distance')
        else:
            warnEmptyAttribute("distance", "XSDataLength")
        if self._matrix is not None:
            self.matrix.export(outfile, level, name_='matrix')
        if self._mosaicity is not None:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self._template is not None:
            self.template.export(outfile, level, name_='template')
        else:
            warnEmptyAttribute("template", "XSDataString")
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        else:
            warnEmptyAttribute("wavelength", "XSDataWavelength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beam':
            obj_ = XSDataMOSFLMBeamPosition()
            obj_.build(child_)
            self.setBeam(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataMOSFLMDetector()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'matrix':
            obj_ = XSDataMOSFLMNewmat()
            obj_.build(child_)
            self.setMatrix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'template':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setTemplate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInput


class XSDataMOSFLMOutput(XSDataResult):
    def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None):
        XSDataResult.__init__(self, status)
        if refinedBeam is None:
            self._refinedBeam = None
        elif refinedBeam.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._refinedBeam = refinedBeam
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput constructor argument 'refinedBeam' is not XSDataMOSFLMBeamPosition but %s" % self._refinedBeam.__class__.__name__
            raise BaseException(strMessage)
        if refinedDistance is None:
            self._refinedDistance = None
        elif refinedDistance.__class__.__name__ == "XSDataLength":
            self._refinedDistance = refinedDistance
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput constructor argument 'refinedDistance' is not XSDataLength but %s" % self._refinedDistance.__class__.__name__
            raise BaseException(strMessage)
        if refinedNewmat is None:
            self._refinedNewmat = None
        elif refinedNewmat.__class__.__name__ == "XSDataMOSFLMNewmat":
            self._refinedNewmat = refinedNewmat
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput constructor argument 'refinedNewmat' is not XSDataMOSFLMNewmat but %s" % self._refinedNewmat.__class__.__name__
            raise BaseException(strMessage)
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput constructor argument 'pathToLogFile' is not XSDataFile but %s" % self._pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'refinedBeam' attribute
    def getRefinedBeam(self): return self._refinedBeam
    def setRefinedBeam(self, refinedBeam):
        if refinedBeam is None:
            self._refinedBeam = None
        elif refinedBeam.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._refinedBeam = refinedBeam
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput.setRefinedBeam argument is not XSDataMOSFLMBeamPosition but %s" % refinedBeam.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedBeam(self): self._refinedBeam = None
    refinedBeam = property(getRefinedBeam, setRefinedBeam, delRefinedBeam, "Property for refinedBeam")
    # Methods and properties for the 'refinedDistance' attribute
    def getRefinedDistance(self): return self._refinedDistance
    def setRefinedDistance(self, refinedDistance):
        if refinedDistance is None:
            self._refinedDistance = None
        elif refinedDistance.__class__.__name__ == "XSDataLength":
            self._refinedDistance = refinedDistance
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput.setRefinedDistance argument is not XSDataLength but %s" % refinedDistance.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedDistance(self): self._refinedDistance = None
    refinedDistance = property(getRefinedDistance, setRefinedDistance, delRefinedDistance, "Property for refinedDistance")
    # Methods and properties for the 'refinedNewmat' attribute
    def getRefinedNewmat(self): return self._refinedNewmat
    def setRefinedNewmat(self, refinedNewmat):
        if refinedNewmat is None:
            self._refinedNewmat = None
        elif refinedNewmat.__class__.__name__ == "XSDataMOSFLMNewmat":
            self._refinedNewmat = refinedNewmat
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput.setRefinedNewmat argument is not XSDataMOSFLMNewmat but %s" % refinedNewmat.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedNewmat(self): self._refinedNewmat = None
    refinedNewmat = property(getRefinedNewmat, setRefinedNewmat, delRefinedNewmat, "Property for refinedNewmat")
    # Methods and properties for the 'pathToLogFile' attribute
    def getPathToLogFile(self): return self._pathToLogFile
    def setPathToLogFile(self, pathToLogFile):
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutput.setPathToLogFile argument is not XSDataFile but %s" % pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToLogFile(self): self._pathToLogFile = None
    pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
    def export(self, outfile, level, name_='XSDataMOSFLMOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._refinedBeam is not None:
            self.refinedBeam.export(outfile, level, name_='refinedBeam')
        if self._refinedDistance is not None:
            self.refinedDistance.export(outfile, level, name_='refinedDistance')
        if self._refinedNewmat is not None:
            self.refinedNewmat.export(outfile, level, name_='refinedNewmat')
        if self._pathToLogFile is not None:
            self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedBeam':
            obj_ = XSDataMOSFLMBeamPosition()
            obj_.build(child_)
            self.setRefinedBeam(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedDistance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRefinedDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedNewmat':
            obj_ = XSDataMOSFLMNewmat()
            obj_.build(child_)
            self.setRefinedNewmat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToLogFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutput


class XSDataMOSFLMInputGeneratePrediction(XSDataMOSFLMInput):
    def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, image=None):
        XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataMOSFLMImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataMOSFLMInputGeneratePrediction constructor argument 'image' is not XSDataMOSFLMImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataMOSFLMImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataMOSFLMInputGeneratePrediction.setImage argument is not XSDataMOSFLMImage but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def export(self, outfile, level, name_='XSDataMOSFLMInputGeneratePrediction'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputGeneratePrediction'):
        XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataMOSFLMImage")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataMOSFLMImage()
            obj_.build(child_)
            self.setImage(obj_)
        XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMInputGeneratePrediction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMInputGeneratePrediction' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMInputGeneratePrediction is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMInputGeneratePrediction.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputGeneratePrediction()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputGeneratePrediction" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputGeneratePrediction()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputGeneratePrediction


class XSDataMOSFLMInputIndexing(XSDataMOSFLMInput):
    def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, image=None):
        XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing constructor argument 'image' is not list but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.setImage argument is not list but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def addImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.addImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMImage":
            self._image.append(value)
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.addImage argument is not XSDataMOSFLMImage but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.insertImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.insertImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMImage":
            self._image[index] = value
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIndexing.addImage argument is not XSDataMOSFLMImage but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataMOSFLMInputIndexing'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputIndexing'):
        XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getImage() == []:
            warnEmptyAttribute("image", "XSDataMOSFLMImage")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataMOSFLMImage()
            obj_.build(child_)
            self.image.append(obj_)
        XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMInputIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMInputIndexing' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMInputIndexing is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMInputIndexing.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputIndexing()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputIndexing" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputIndexing()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputIndexing


class XSDataMOSFLMInputIntegration(XSDataMOSFLMInput):
    def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, rotationAxisStart=None, oscillationWidth=None, imageStart=None, imageEnd=None):
        XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
        if imageEnd is None:
            self._imageEnd = None
        elif imageEnd.__class__.__name__ == "XSDataInteger":
            self._imageEnd = imageEnd
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration constructor argument 'imageEnd' is not XSDataInteger but %s" % self._imageEnd.__class__.__name__
            raise BaseException(strMessage)
        if imageStart is None:
            self._imageStart = None
        elif imageStart.__class__.__name__ == "XSDataInteger":
            self._imageStart = imageStart
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration constructor argument 'imageStart' is not XSDataInteger but %s" % self._imageStart.__class__.__name__
            raise BaseException(strMessage)
        if oscillationWidth is None:
            self._oscillationWidth = None
        elif oscillationWidth.__class__.__name__ == "XSDataAngle":
            self._oscillationWidth = oscillationWidth
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration constructor argument 'oscillationWidth' is not XSDataAngle but %s" % self._oscillationWidth.__class__.__name__
            raise BaseException(strMessage)
        if rotationAxisStart is None:
            self._rotationAxisStart = None
        elif rotationAxisStart.__class__.__name__ == "XSDataAngle":
            self._rotationAxisStart = rotationAxisStart
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration constructor argument 'rotationAxisStart' is not XSDataAngle but %s" % self._rotationAxisStart.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageEnd' attribute
    def getImageEnd(self): return self._imageEnd
    def setImageEnd(self, imageEnd):
        if imageEnd is None:
            self._imageEnd = None
        elif imageEnd.__class__.__name__ == "XSDataInteger":
            self._imageEnd = imageEnd
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration.setImageEnd argument is not XSDataInteger but %s" % imageEnd.__class__.__name__
            raise BaseException(strMessage)
    def delImageEnd(self): self._imageEnd = None
    imageEnd = property(getImageEnd, setImageEnd, delImageEnd, "Property for imageEnd")
    # Methods and properties for the 'imageStart' attribute
    def getImageStart(self): return self._imageStart
    def setImageStart(self, imageStart):
        if imageStart is None:
            self._imageStart = None
        elif imageStart.__class__.__name__ == "XSDataInteger":
            self._imageStart = imageStart
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration.setImageStart argument is not XSDataInteger but %s" % imageStart.__class__.__name__
            raise BaseException(strMessage)
    def delImageStart(self): self._imageStart = None
    imageStart = property(getImageStart, setImageStart, delImageStart, "Property for imageStart")
    # Methods and properties for the 'oscillationWidth' attribute
    def getOscillationWidth(self): return self._oscillationWidth
    def setOscillationWidth(self, oscillationWidth):
        if oscillationWidth is None:
            self._oscillationWidth = None
        elif oscillationWidth.__class__.__name__ == "XSDataAngle":
            self._oscillationWidth = oscillationWidth
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration.setOscillationWidth argument is not XSDataAngle but %s" % oscillationWidth.__class__.__name__
            raise BaseException(strMessage)
    def delOscillationWidth(self): self._oscillationWidth = None
    oscillationWidth = property(getOscillationWidth, setOscillationWidth, delOscillationWidth, "Property for oscillationWidth")
    # Methods and properties for the 'rotationAxisStart' attribute
    def getRotationAxisStart(self): return self._rotationAxisStart
    def setRotationAxisStart(self, rotationAxisStart):
        if rotationAxisStart is None:
            self._rotationAxisStart = None
        elif rotationAxisStart.__class__.__name__ == "XSDataAngle":
            self._rotationAxisStart = rotationAxisStart
        else:
            strMessage = "ERROR! XSDataMOSFLMInputIntegration.setRotationAxisStart argument is not XSDataAngle but %s" % rotationAxisStart.__class__.__name__
            raise BaseException(strMessage)
    def delRotationAxisStart(self): self._rotationAxisStart = None
    rotationAxisStart = property(getRotationAxisStart, setRotationAxisStart, delRotationAxisStart, "Property for rotationAxisStart")
    def export(self, outfile, level, name_='XSDataMOSFLMInputIntegration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputIntegration'):
        XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
        if self._imageEnd is not None:
            self.imageEnd.export(outfile, level, name_='imageEnd')
        else:
            warnEmptyAttribute("imageEnd", "XSDataInteger")
        if self._imageStart is not None:
            self.imageStart.export(outfile, level, name_='imageStart')
        else:
            warnEmptyAttribute("imageStart", "XSDataInteger")
        if self._oscillationWidth is not None:
            self.oscillationWidth.export(outfile, level, name_='oscillationWidth')
        else:
            warnEmptyAttribute("oscillationWidth", "XSDataAngle")
        if self._rotationAxisStart is not None:
            self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
        else:
            warnEmptyAttribute("rotationAxisStart", "XSDataAngle")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageEnd':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageStart':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationWidth':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOscillationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisStart':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setRotationAxisStart(obj_)
        XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMInputIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMInputIntegration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMInputIntegration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMInputIntegration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputIntegration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputIntegration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputIntegration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputIntegration


class XSDataMOSFLMInputPostRefinement(XSDataMOSFLMInput):
    def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None):
        XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
    def export(self, outfile, level, name_='XSDataMOSFLMInputPostRefinement'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputPostRefinement'):
        XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMInputPostRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMInputPostRefinement' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMInputPostRefinement is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMInputPostRefinement.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputPostRefinement()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputPostRefinement" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMInputPostRefinement()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputPostRefinement


class XSDataMOSFLMOutputIndexing(XSDataMOSFLMOutput):
    def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None, spotsUsed=None, spotsTotal=None, selectedSolutionSpaceGroupNumber=None, selectedSolutionSpaceGroup=None, selectedSolutionNumber=None, possibleSolutions=None, mosaicityEstimation=None, deviationPositional=None, deviationAngular=None, beamShift=None):
        XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
        if beamShift is None:
            self._beamShift = None
        elif beamShift.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._beamShift = beamShift
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'beamShift' is not XSDataMOSFLMBeamPosition but %s" % self._beamShift.__class__.__name__
            raise BaseException(strMessage)
        if deviationAngular is None:
            self._deviationAngular = None
        elif deviationAngular.__class__.__name__ == "XSDataAngle":
            self._deviationAngular = deviationAngular
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'deviationAngular' is not XSDataAngle but %s" % self._deviationAngular.__class__.__name__
            raise BaseException(strMessage)
        if deviationPositional is None:
            self._deviationPositional = None
        elif deviationPositional.__class__.__name__ == "XSDataLength":
            self._deviationPositional = deviationPositional
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'deviationPositional' is not XSDataLength but %s" % self._deviationPositional.__class__.__name__
            raise BaseException(strMessage)
        if mosaicityEstimation is None:
            self._mosaicityEstimation = None
        elif mosaicityEstimation.__class__.__name__ == "XSDataFloat":
            self._mosaicityEstimation = mosaicityEstimation
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'mosaicityEstimation' is not XSDataFloat but %s" % self._mosaicityEstimation.__class__.__name__
            raise BaseException(strMessage)
        if possibleSolutions is None:
            self._possibleSolutions = []
        elif possibleSolutions.__class__.__name__ == "list":
            self._possibleSolutions = possibleSolutions
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'possibleSolutions' is not list but %s" % self._possibleSolutions.__class__.__name__
            raise BaseException(strMessage)
        if selectedSolutionNumber is None:
            self._selectedSolutionNumber = None
        elif selectedSolutionNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionNumber = selectedSolutionNumber
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'selectedSolutionNumber' is not XSDataInteger but %s" % self._selectedSolutionNumber.__class__.__name__
            raise BaseException(strMessage)
        if selectedSolutionSpaceGroup is None:
            self._selectedSolutionSpaceGroup = None
        elif selectedSolutionSpaceGroup.__class__.__name__ == "XSDataString":
            self._selectedSolutionSpaceGroup = selectedSolutionSpaceGroup
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'selectedSolutionSpaceGroup' is not XSDataString but %s" % self._selectedSolutionSpaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if selectedSolutionSpaceGroupNumber is None:
            self._selectedSolutionSpaceGroupNumber = None
        elif selectedSolutionSpaceGroupNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionSpaceGroupNumber = selectedSolutionSpaceGroupNumber
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'selectedSolutionSpaceGroupNumber' is not XSDataInteger but %s" % self._selectedSolutionSpaceGroupNumber.__class__.__name__
            raise BaseException(strMessage)
        if spotsTotal is None:
            self._spotsTotal = None
        elif spotsTotal.__class__.__name__ == "XSDataInteger":
            self._spotsTotal = spotsTotal
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'spotsTotal' is not XSDataInteger but %s" % self._spotsTotal.__class__.__name__
            raise BaseException(strMessage)
        if spotsUsed is None:
            self._spotsUsed = None
        elif spotsUsed.__class__.__name__ == "XSDataInteger":
            self._spotsUsed = spotsUsed
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing constructor argument 'spotsUsed' is not XSDataInteger but %s" % self._spotsUsed.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'beamShift' attribute
    def getBeamShift(self): return self._beamShift
    def setBeamShift(self, beamShift):
        if beamShift is None:
            self._beamShift = None
        elif beamShift.__class__.__name__ == "XSDataMOSFLMBeamPosition":
            self._beamShift = beamShift
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setBeamShift argument is not XSDataMOSFLMBeamPosition but %s" % beamShift.__class__.__name__
            raise BaseException(strMessage)
    def delBeamShift(self): self._beamShift = None
    beamShift = property(getBeamShift, setBeamShift, delBeamShift, "Property for beamShift")
    # Methods and properties for the 'deviationAngular' attribute
    def getDeviationAngular(self): return self._deviationAngular
    def setDeviationAngular(self, deviationAngular):
        if deviationAngular is None:
            self._deviationAngular = None
        elif deviationAngular.__class__.__name__ == "XSDataAngle":
            self._deviationAngular = deviationAngular
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setDeviationAngular argument is not XSDataAngle but %s" % deviationAngular.__class__.__name__
            raise BaseException(strMessage)
    def delDeviationAngular(self): self._deviationAngular = None
    deviationAngular = property(getDeviationAngular, setDeviationAngular, delDeviationAngular, "Property for deviationAngular")
    # Methods and properties for the 'deviationPositional' attribute
    def getDeviationPositional(self): return self._deviationPositional
    def setDeviationPositional(self, deviationPositional):
        if deviationPositional is None:
            self._deviationPositional = None
        elif deviationPositional.__class__.__name__ == "XSDataLength":
            self._deviationPositional = deviationPositional
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setDeviationPositional argument is not XSDataLength but %s" % deviationPositional.__class__.__name__
            raise BaseException(strMessage)
    def delDeviationPositional(self): self._deviationPositional = None
    deviationPositional = property(getDeviationPositional, setDeviationPositional, delDeviationPositional, "Property for deviationPositional")
    # Methods and properties for the 'mosaicityEstimation' attribute
    def getMosaicityEstimation(self): return self._mosaicityEstimation
    def setMosaicityEstimation(self, mosaicityEstimation):
        if mosaicityEstimation is None:
            self._mosaicityEstimation = None
        elif mosaicityEstimation.__class__.__name__ == "XSDataFloat":
            self._mosaicityEstimation = mosaicityEstimation
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setMosaicityEstimation argument is not XSDataFloat but %s" % mosaicityEstimation.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicityEstimation(self): self._mosaicityEstimation = None
    mosaicityEstimation = property(getMosaicityEstimation, setMosaicityEstimation, delMosaicityEstimation, "Property for mosaicityEstimation")
    # Methods and properties for the 'possibleSolutions' attribute
    def getPossibleSolutions(self): return self._possibleSolutions
    def setPossibleSolutions(self, possibleSolutions):
        if possibleSolutions is None:
            self._possibleSolutions = []
        elif possibleSolutions.__class__.__name__ == "list":
            self._possibleSolutions = possibleSolutions
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setPossibleSolutions argument is not list but %s" % possibleSolutions.__class__.__name__
            raise BaseException(strMessage)
    def delPossibleSolutions(self): self._possibleSolutions = None
    possibleSolutions = property(getPossibleSolutions, setPossibleSolutions, delPossibleSolutions, "Property for possibleSolutions")
    def addPossibleSolutions(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.addPossibleSolutions argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMIndexingSolution":
            self._possibleSolutions.append(value)
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.addPossibleSolutions argument is not XSDataMOSFLMIndexingSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPossibleSolutions(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.insertPossibleSolutions argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.insertPossibleSolutions argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMIndexingSolution":
            self._possibleSolutions[index] = value
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.addPossibleSolutions argument is not XSDataMOSFLMIndexingSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'selectedSolutionNumber' attribute
    def getSelectedSolutionNumber(self): return self._selectedSolutionNumber
    def setSelectedSolutionNumber(self, selectedSolutionNumber):
        if selectedSolutionNumber is None:
            self._selectedSolutionNumber = None
        elif selectedSolutionNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionNumber = selectedSolutionNumber
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setSelectedSolutionNumber argument is not XSDataInteger but %s" % selectedSolutionNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSelectedSolutionNumber(self): self._selectedSolutionNumber = None
    selectedSolutionNumber = property(getSelectedSolutionNumber, setSelectedSolutionNumber, delSelectedSolutionNumber, "Property for selectedSolutionNumber")
    # Methods and properties for the 'selectedSolutionSpaceGroup' attribute
    def getSelectedSolutionSpaceGroup(self): return self._selectedSolutionSpaceGroup
    def setSelectedSolutionSpaceGroup(self, selectedSolutionSpaceGroup):
        if selectedSolutionSpaceGroup is None:
            self._selectedSolutionSpaceGroup = None
        elif selectedSolutionSpaceGroup.__class__.__name__ == "XSDataString":
            self._selectedSolutionSpaceGroup = selectedSolutionSpaceGroup
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setSelectedSolutionSpaceGroup argument is not XSDataString but %s" % selectedSolutionSpaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delSelectedSolutionSpaceGroup(self): self._selectedSolutionSpaceGroup = None
    selectedSolutionSpaceGroup = property(getSelectedSolutionSpaceGroup, setSelectedSolutionSpaceGroup, delSelectedSolutionSpaceGroup, "Property for selectedSolutionSpaceGroup")
    # Methods and properties for the 'selectedSolutionSpaceGroupNumber' attribute
    def getSelectedSolutionSpaceGroupNumber(self): return self._selectedSolutionSpaceGroupNumber
    def setSelectedSolutionSpaceGroupNumber(self, selectedSolutionSpaceGroupNumber):
        if selectedSolutionSpaceGroupNumber is None:
            self._selectedSolutionSpaceGroupNumber = None
        elif selectedSolutionSpaceGroupNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionSpaceGroupNumber = selectedSolutionSpaceGroupNumber
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setSelectedSolutionSpaceGroupNumber argument is not XSDataInteger but %s" % selectedSolutionSpaceGroupNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSelectedSolutionSpaceGroupNumber(self): self._selectedSolutionSpaceGroupNumber = None
    selectedSolutionSpaceGroupNumber = property(getSelectedSolutionSpaceGroupNumber, setSelectedSolutionSpaceGroupNumber, delSelectedSolutionSpaceGroupNumber, "Property for selectedSolutionSpaceGroupNumber")
    # Methods and properties for the 'spotsTotal' attribute
    def getSpotsTotal(self): return self._spotsTotal
    def setSpotsTotal(self, spotsTotal):
        if spotsTotal is None:
            self._spotsTotal = None
        elif spotsTotal.__class__.__name__ == "XSDataInteger":
            self._spotsTotal = spotsTotal
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setSpotsTotal argument is not XSDataInteger but %s" % spotsTotal.__class__.__name__
            raise BaseException(strMessage)
    def delSpotsTotal(self): self._spotsTotal = None
    spotsTotal = property(getSpotsTotal, setSpotsTotal, delSpotsTotal, "Property for spotsTotal")
    # Methods and properties for the 'spotsUsed' attribute
    def getSpotsUsed(self): return self._spotsUsed
    def setSpotsUsed(self, spotsUsed):
        if spotsUsed is None:
            self._spotsUsed = None
        elif spotsUsed.__class__.__name__ == "XSDataInteger":
            self._spotsUsed = spotsUsed
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIndexing.setSpotsUsed argument is not XSDataInteger but %s" % spotsUsed.__class__.__name__
            raise BaseException(strMessage)
    def delSpotsUsed(self): self._spotsUsed = None
    spotsUsed = property(getSpotsUsed, setSpotsUsed, delSpotsUsed, "Property for spotsUsed")
    def export(self, outfile, level, name_='XSDataMOSFLMOutputIndexing'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputIndexing'):
        XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
        if self._beamShift is not None:
            self.beamShift.export(outfile, level, name_='beamShift')
        if self._deviationAngular is not None:
            self.deviationAngular.export(outfile, level, name_='deviationAngular')
        if self._deviationPositional is not None:
            self.deviationPositional.export(outfile, level, name_='deviationPositional')
        if self._mosaicityEstimation is not None:
            self.mosaicityEstimation.export(outfile, level, name_='mosaicityEstimation')
        for possibleSolutions_ in self.getPossibleSolutions():
            possibleSolutions_.export(outfile, level, name_='possibleSolutions')
        if self._selectedSolutionNumber is not None:
            self.selectedSolutionNumber.export(outfile, level, name_='selectedSolutionNumber')
        if self._selectedSolutionSpaceGroup is not None:
            self.selectedSolutionSpaceGroup.export(outfile, level, name_='selectedSolutionSpaceGroup')
        if self._selectedSolutionSpaceGroupNumber is not None:
            self.selectedSolutionSpaceGroupNumber.export(outfile, level, name_='selectedSolutionSpaceGroupNumber')
        if self._spotsTotal is not None:
            self.spotsTotal.export(outfile, level, name_='spotsTotal')
        if self._spotsUsed is not None:
            self.spotsUsed.export(outfile, level, name_='spotsUsed')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShift':
            obj_ = XSDataMOSFLMBeamPosition()
            obj_.build(child_)
            self.setBeamShift(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deviationAngular':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setDeviationAngular(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deviationPositional':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDeviationPositional(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityEstimation':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setMosaicityEstimation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possibleSolutions':
            obj_ = XSDataMOSFLMIndexingSolution()
            obj_.build(child_)
            self.possibleSolutions.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedSolutionNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSelectedSolutionNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedSolutionSpaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSelectedSolutionSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedSolutionSpaceGroupNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSelectedSolutionSpaceGroupNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotsTotal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpotsTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotsUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpotsUsed(obj_)
        XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMOutputIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMOutputIndexing' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMOutputIndexing is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMOutputIndexing.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputIndexing()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputIndexing" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputIndexing()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputIndexing


class XSDataMOSFLMOutputIntegration(XSDataMOSFLMOutput):
    def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None, statisticsPerResolutionBin=None, RMSSpotDeviation=None, refinedYScale=None, refinedMosaicity=None, overallStatistics=None, overallIOverSigma=None, numberOfReflectionsGenerated=None, numberOfPartialReflections=None, numberOfOverlappedReflections=None, numberOfNegativeReflections=None, numberOfFullyRecordedReflections=None, numberOfBadReflections=None, highestResolutionIOverSigma=None, generatedMTZFile=None, bestfilePar=None, bestfileHKL=None, bestfileDat=None):
        XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
        if bestfileDat is None:
            self._bestfileDat = None
        elif bestfileDat.__class__.__name__ == "XSDataString":
            self._bestfileDat = bestfileDat
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'bestfileDat' is not XSDataString but %s" % self._bestfileDat.__class__.__name__
            raise BaseException(strMessage)
        if bestfileHKL is None:
            self._bestfileHKL = None
        elif bestfileHKL.__class__.__name__ == "XSDataString":
            self._bestfileHKL = bestfileHKL
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'bestfileHKL' is not XSDataString but %s" % self._bestfileHKL.__class__.__name__
            raise BaseException(strMessage)
        if bestfilePar is None:
            self._bestfilePar = None
        elif bestfilePar.__class__.__name__ == "XSDataString":
            self._bestfilePar = bestfilePar
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'bestfilePar' is not XSDataString but %s" % self._bestfilePar.__class__.__name__
            raise BaseException(strMessage)
        if generatedMTZFile is None:
            self._generatedMTZFile = None
        elif generatedMTZFile.__class__.__name__ == "XSDataFile":
            self._generatedMTZFile = generatedMTZFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'generatedMTZFile' is not XSDataFile but %s" % self._generatedMTZFile.__class__.__name__
            raise BaseException(strMessage)
        if highestResolutionIOverSigma is None:
            self._highestResolutionIOverSigma = None
        elif highestResolutionIOverSigma.__class__.__name__ == "XSDataFloat":
            self._highestResolutionIOverSigma = highestResolutionIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'highestResolutionIOverSigma' is not XSDataFloat but %s" % self._highestResolutionIOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if numberOfBadReflections is None:
            self._numberOfBadReflections = None
        elif numberOfBadReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfBadReflections = numberOfBadReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfBadReflections' is not XSDataInteger but %s" % self._numberOfBadReflections.__class__.__name__
            raise BaseException(strMessage)
        if numberOfFullyRecordedReflections is None:
            self._numberOfFullyRecordedReflections = None
        elif numberOfFullyRecordedReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfFullyRecordedReflections' is not XSDataInteger but %s" % self._numberOfFullyRecordedReflections.__class__.__name__
            raise BaseException(strMessage)
        if numberOfNegativeReflections is None:
            self._numberOfNegativeReflections = None
        elif numberOfNegativeReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfNegativeReflections = numberOfNegativeReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfNegativeReflections' is not XSDataInteger but %s" % self._numberOfNegativeReflections.__class__.__name__
            raise BaseException(strMessage)
        if numberOfOverlappedReflections is None:
            self._numberOfOverlappedReflections = None
        elif numberOfOverlappedReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfOverlappedReflections = numberOfOverlappedReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfOverlappedReflections' is not XSDataInteger but %s" % self._numberOfOverlappedReflections.__class__.__name__
            raise BaseException(strMessage)
        if numberOfPartialReflections is None:
            self._numberOfPartialReflections = None
        elif numberOfPartialReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfPartialReflections = numberOfPartialReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfPartialReflections' is not XSDataInteger but %s" % self._numberOfPartialReflections.__class__.__name__
            raise BaseException(strMessage)
        if numberOfReflectionsGenerated is None:
            self._numberOfReflectionsGenerated = None
        elif numberOfReflectionsGenerated.__class__.__name__ == "XSDataInteger":
            self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'numberOfReflectionsGenerated' is not XSDataInteger but %s" % self._numberOfReflectionsGenerated.__class__.__name__
            raise BaseException(strMessage)
        if overallIOverSigma is None:
            self._overallIOverSigma = None
        elif overallIOverSigma.__class__.__name__ == "XSDataFloat":
            self._overallIOverSigma = overallIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'overallIOverSigma' is not XSDataFloat but %s" % self._overallIOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if overallStatistics is None:
            self._overallStatistics = None
        elif overallStatistics.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerResolutionBin":
            self._overallStatistics = overallStatistics
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'overallStatistics' is not XSDataMOSFLMIntegrationStatisticsPerResolutionBin but %s" % self._overallStatistics.__class__.__name__
            raise BaseException(strMessage)
        if refinedMosaicity is None:
            self._refinedMosaicity = None
        elif refinedMosaicity.__class__.__name__ == "XSDataFloat":
            self._refinedMosaicity = refinedMosaicity
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'refinedMosaicity' is not XSDataFloat but %s" % self._refinedMosaicity.__class__.__name__
            raise BaseException(strMessage)
        if refinedYScale is None:
            self._refinedYScale = None
        elif refinedYScale.__class__.__name__ == "XSDataFloat":
            self._refinedYScale = refinedYScale
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'refinedYScale' is not XSDataFloat but %s" % self._refinedYScale.__class__.__name__
            raise BaseException(strMessage)
        if RMSSpotDeviation is None:
            self._RMSSpotDeviation = None
        elif RMSSpotDeviation.__class__.__name__ == "XSDataLength":
            self._RMSSpotDeviation = RMSSpotDeviation
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'RMSSpotDeviation' is not XSDataLength but %s" % self._RMSSpotDeviation.__class__.__name__
            raise BaseException(strMessage)
        if statisticsPerResolutionBin is None:
            self._statisticsPerResolutionBin = []
        elif statisticsPerResolutionBin.__class__.__name__ == "list":
            self._statisticsPerResolutionBin = statisticsPerResolutionBin
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration constructor argument 'statisticsPerResolutionBin' is not list but %s" % self._statisticsPerResolutionBin.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bestfileDat' attribute
    def getBestfileDat(self): return self._bestfileDat
    def setBestfileDat(self, bestfileDat):
        if bestfileDat is None:
            self._bestfileDat = None
        elif bestfileDat.__class__.__name__ == "XSDataString":
            self._bestfileDat = bestfileDat
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setBestfileDat argument is not XSDataString but %s" % bestfileDat.__class__.__name__
            raise BaseException(strMessage)
    def delBestfileDat(self): self._bestfileDat = None
    bestfileDat = property(getBestfileDat, setBestfileDat, delBestfileDat, "Property for bestfileDat")
    # Methods and properties for the 'bestfileHKL' attribute
    def getBestfileHKL(self): return self._bestfileHKL
    def setBestfileHKL(self, bestfileHKL):
        if bestfileHKL is None:
            self._bestfileHKL = None
        elif bestfileHKL.__class__.__name__ == "XSDataString":
            self._bestfileHKL = bestfileHKL
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setBestfileHKL argument is not XSDataString but %s" % bestfileHKL.__class__.__name__
            raise BaseException(strMessage)
    def delBestfileHKL(self): self._bestfileHKL = None
    bestfileHKL = property(getBestfileHKL, setBestfileHKL, delBestfileHKL, "Property for bestfileHKL")
    # Methods and properties for the 'bestfilePar' attribute
    def getBestfilePar(self): return self._bestfilePar
    def setBestfilePar(self, bestfilePar):
        if bestfilePar is None:
            self._bestfilePar = None
        elif bestfilePar.__class__.__name__ == "XSDataString":
            self._bestfilePar = bestfilePar
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setBestfilePar argument is not XSDataString but %s" % bestfilePar.__class__.__name__
            raise BaseException(strMessage)
    def delBestfilePar(self): self._bestfilePar = None
    bestfilePar = property(getBestfilePar, setBestfilePar, delBestfilePar, "Property for bestfilePar")
    # Methods and properties for the 'generatedMTZFile' attribute
    def getGeneratedMTZFile(self): return self._generatedMTZFile
    def setGeneratedMTZFile(self, generatedMTZFile):
        if generatedMTZFile is None:
            self._generatedMTZFile = None
        elif generatedMTZFile.__class__.__name__ == "XSDataFile":
            self._generatedMTZFile = generatedMTZFile
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setGeneratedMTZFile argument is not XSDataFile but %s" % generatedMTZFile.__class__.__name__
            raise BaseException(strMessage)
    def delGeneratedMTZFile(self): self._generatedMTZFile = None
    generatedMTZFile = property(getGeneratedMTZFile, setGeneratedMTZFile, delGeneratedMTZFile, "Property for generatedMTZFile")
    # Methods and properties for the 'highestResolutionIOverSigma' attribute
    def getHighestResolutionIOverSigma(self): return self._highestResolutionIOverSigma
    def setHighestResolutionIOverSigma(self, highestResolutionIOverSigma):
        if highestResolutionIOverSigma is None:
            self._highestResolutionIOverSigma = None
        elif highestResolutionIOverSigma.__class__.__name__ == "XSDataFloat":
            self._highestResolutionIOverSigma = highestResolutionIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setHighestResolutionIOverSigma argument is not XSDataFloat but %s" % highestResolutionIOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delHighestResolutionIOverSigma(self): self._highestResolutionIOverSigma = None
    highestResolutionIOverSigma = property(getHighestResolutionIOverSigma, setHighestResolutionIOverSigma, delHighestResolutionIOverSigma, "Property for highestResolutionIOverSigma")
    # Methods and properties for the 'numberOfBadReflections' attribute
    def getNumberOfBadReflections(self): return self._numberOfBadReflections
    def setNumberOfBadReflections(self, numberOfBadReflections):
        if numberOfBadReflections is None:
            self._numberOfBadReflections = None
        elif numberOfBadReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfBadReflections = numberOfBadReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfBadReflections argument is not XSDataInteger but %s" % numberOfBadReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfBadReflections(self): self._numberOfBadReflections = None
    numberOfBadReflections = property(getNumberOfBadReflections, setNumberOfBadReflections, delNumberOfBadReflections, "Property for numberOfBadReflections")
    # Methods and properties for the 'numberOfFullyRecordedReflections' attribute
    def getNumberOfFullyRecordedReflections(self): return self._numberOfFullyRecordedReflections
    def setNumberOfFullyRecordedReflections(self, numberOfFullyRecordedReflections):
        if numberOfFullyRecordedReflections is None:
            self._numberOfFullyRecordedReflections = None
        elif numberOfFullyRecordedReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfFullyRecordedReflections argument is not XSDataInteger but %s" % numberOfFullyRecordedReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfFullyRecordedReflections(self): self._numberOfFullyRecordedReflections = None
    numberOfFullyRecordedReflections = property(getNumberOfFullyRecordedReflections, setNumberOfFullyRecordedReflections, delNumberOfFullyRecordedReflections, "Property for numberOfFullyRecordedReflections")
    # Methods and properties for the 'numberOfNegativeReflections' attribute
    def getNumberOfNegativeReflections(self): return self._numberOfNegativeReflections
    def setNumberOfNegativeReflections(self, numberOfNegativeReflections):
        if numberOfNegativeReflections is None:
            self._numberOfNegativeReflections = None
        elif numberOfNegativeReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfNegativeReflections = numberOfNegativeReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfNegativeReflections argument is not XSDataInteger but %s" % numberOfNegativeReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfNegativeReflections(self): self._numberOfNegativeReflections = None
    numberOfNegativeReflections = property(getNumberOfNegativeReflections, setNumberOfNegativeReflections, delNumberOfNegativeReflections, "Property for numberOfNegativeReflections")
    # Methods and properties for the 'numberOfOverlappedReflections' attribute
    def getNumberOfOverlappedReflections(self): return self._numberOfOverlappedReflections
    def setNumberOfOverlappedReflections(self, numberOfOverlappedReflections):
        if numberOfOverlappedReflections is None:
            self._numberOfOverlappedReflections = None
        elif numberOfOverlappedReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfOverlappedReflections = numberOfOverlappedReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfOverlappedReflections argument is not XSDataInteger but %s" % numberOfOverlappedReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfOverlappedReflections(self): self._numberOfOverlappedReflections = None
    numberOfOverlappedReflections = property(getNumberOfOverlappedReflections, setNumberOfOverlappedReflections, delNumberOfOverlappedReflections, "Property for numberOfOverlappedReflections")
    # Methods and properties for the 'numberOfPartialReflections' attribute
    def getNumberOfPartialReflections(self): return self._numberOfPartialReflections
    def setNumberOfPartialReflections(self, numberOfPartialReflections):
        if numberOfPartialReflections is None:
            self._numberOfPartialReflections = None
        elif numberOfPartialReflections.__class__.__name__ == "XSDataInteger":
            self._numberOfPartialReflections = numberOfPartialReflections
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfPartialReflections argument is not XSDataInteger but %s" % numberOfPartialReflections.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfPartialReflections(self): self._numberOfPartialReflections = None
    numberOfPartialReflections = property(getNumberOfPartialReflections, setNumberOfPartialReflections, delNumberOfPartialReflections, "Property for numberOfPartialReflections")
    # Methods and properties for the 'numberOfReflectionsGenerated' attribute
    def getNumberOfReflectionsGenerated(self): return self._numberOfReflectionsGenerated
    def setNumberOfReflectionsGenerated(self, numberOfReflectionsGenerated):
        if numberOfReflectionsGenerated is None:
            self._numberOfReflectionsGenerated = None
        elif numberOfReflectionsGenerated.__class__.__name__ == "XSDataInteger":
            self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setNumberOfReflectionsGenerated argument is not XSDataInteger but %s" % numberOfReflectionsGenerated.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfReflectionsGenerated(self): self._numberOfReflectionsGenerated = None
    numberOfReflectionsGenerated = property(getNumberOfReflectionsGenerated, setNumberOfReflectionsGenerated, delNumberOfReflectionsGenerated, "Property for numberOfReflectionsGenerated")
    # Methods and properties for the 'overallIOverSigma' attribute
    def getOverallIOverSigma(self): return self._overallIOverSigma
    def setOverallIOverSigma(self, overallIOverSigma):
        if overallIOverSigma is None:
            self._overallIOverSigma = None
        elif overallIOverSigma.__class__.__name__ == "XSDataFloat":
            self._overallIOverSigma = overallIOverSigma
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setOverallIOverSigma argument is not XSDataFloat but %s" % overallIOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delOverallIOverSigma(self): self._overallIOverSigma = None
    overallIOverSigma = property(getOverallIOverSigma, setOverallIOverSigma, delOverallIOverSigma, "Property for overallIOverSigma")
    # Methods and properties for the 'overallStatistics' attribute
    def getOverallStatistics(self): return self._overallStatistics
    def setOverallStatistics(self, overallStatistics):
        if overallStatistics is None:
            self._overallStatistics = None
        elif overallStatistics.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerResolutionBin":
            self._overallStatistics = overallStatistics
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setOverallStatistics argument is not XSDataMOSFLMIntegrationStatisticsPerResolutionBin but %s" % overallStatistics.__class__.__name__
            raise BaseException(strMessage)
    def delOverallStatistics(self): self._overallStatistics = None
    overallStatistics = property(getOverallStatistics, setOverallStatistics, delOverallStatistics, "Property for overallStatistics")
    # Methods and properties for the 'refinedMosaicity' attribute
    def getRefinedMosaicity(self): return self._refinedMosaicity
    def setRefinedMosaicity(self, refinedMosaicity):
        if refinedMosaicity is None:
            self._refinedMosaicity = None
        elif refinedMosaicity.__class__.__name__ == "XSDataFloat":
            self._refinedMosaicity = refinedMosaicity
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setRefinedMosaicity argument is not XSDataFloat but %s" % refinedMosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedMosaicity(self): self._refinedMosaicity = None
    refinedMosaicity = property(getRefinedMosaicity, setRefinedMosaicity, delRefinedMosaicity, "Property for refinedMosaicity")
    # Methods and properties for the 'refinedYScale' attribute
    def getRefinedYScale(self): return self._refinedYScale
    def setRefinedYScale(self, refinedYScale):
        if refinedYScale is None:
            self._refinedYScale = None
        elif refinedYScale.__class__.__name__ == "XSDataFloat":
            self._refinedYScale = refinedYScale
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setRefinedYScale argument is not XSDataFloat but %s" % refinedYScale.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedYScale(self): self._refinedYScale = None
    refinedYScale = property(getRefinedYScale, setRefinedYScale, delRefinedYScale, "Property for refinedYScale")
    # Methods and properties for the 'RMSSpotDeviation' attribute
    def getRMSSpotDeviation(self): return self._RMSSpotDeviation
    def setRMSSpotDeviation(self, RMSSpotDeviation):
        if RMSSpotDeviation is None:
            self._RMSSpotDeviation = None
        elif RMSSpotDeviation.__class__.__name__ == "XSDataLength":
            self._RMSSpotDeviation = RMSSpotDeviation
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setRMSSpotDeviation argument is not XSDataLength but %s" % RMSSpotDeviation.__class__.__name__
            raise BaseException(strMessage)
    def delRMSSpotDeviation(self): self._RMSSpotDeviation = None
    RMSSpotDeviation = property(getRMSSpotDeviation, setRMSSpotDeviation, delRMSSpotDeviation, "Property for RMSSpotDeviation")
    # Methods and properties for the 'statisticsPerResolutionBin' attribute
    def getStatisticsPerResolutionBin(self): return self._statisticsPerResolutionBin
    def setStatisticsPerResolutionBin(self, statisticsPerResolutionBin):
        if statisticsPerResolutionBin is None:
            self._statisticsPerResolutionBin = []
        elif statisticsPerResolutionBin.__class__.__name__ == "list":
            self._statisticsPerResolutionBin = statisticsPerResolutionBin
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.setStatisticsPerResolutionBin argument is not list but %s" % statisticsPerResolutionBin.__class__.__name__
            raise BaseException(strMessage)
    def delStatisticsPerResolutionBin(self): self._statisticsPerResolutionBin = None
    statisticsPerResolutionBin = property(getStatisticsPerResolutionBin, setStatisticsPerResolutionBin, delStatisticsPerResolutionBin, "Property for statisticsPerResolutionBin")
    def addStatisticsPerResolutionBin(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.addStatisticsPerResolutionBin argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerResolutionBin":
            self._statisticsPerResolutionBin.append(value)
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.addStatisticsPerResolutionBin argument is not XSDataMOSFLMIntegrationStatisticsPerResolutionBin but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertStatisticsPerResolutionBin(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.insertStatisticsPerResolutionBin argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.insertStatisticsPerResolutionBin argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataMOSFLMIntegrationStatisticsPerResolutionBin":
            self._statisticsPerResolutionBin[index] = value
        else:
            strMessage = "ERROR! XSDataMOSFLMOutputIntegration.addStatisticsPerResolutionBin argument is not XSDataMOSFLMIntegrationStatisticsPerResolutionBin but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataMOSFLMOutputIntegration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputIntegration'):
        XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
        if self._bestfileDat is not None:
            self.bestfileDat.export(outfile, level, name_='bestfileDat')
        else:
            warnEmptyAttribute("bestfileDat", "XSDataString")
        if self._bestfileHKL is not None:
            self.bestfileHKL.export(outfile, level, name_='bestfileHKL')
        if self._bestfilePar is not None:
            self.bestfilePar.export(outfile, level, name_='bestfilePar')
        else:
            warnEmptyAttribute("bestfilePar", "XSDataString")
        if self._generatedMTZFile is not None:
            self.generatedMTZFile.export(outfile, level, name_='generatedMTZFile')
        else:
            warnEmptyAttribute("generatedMTZFile", "XSDataFile")
        if self._highestResolutionIOverSigma is not None:
            self.highestResolutionIOverSigma.export(outfile, level, name_='highestResolutionIOverSigma')
        else:
            warnEmptyAttribute("highestResolutionIOverSigma", "XSDataFloat")
        if self._numberOfBadReflections is not None:
            self.numberOfBadReflections.export(outfile, level, name_='numberOfBadReflections')
        else:
            warnEmptyAttribute("numberOfBadReflections", "XSDataInteger")
        if self._numberOfFullyRecordedReflections is not None:
            self.numberOfFullyRecordedReflections.export(outfile, level, name_='numberOfFullyRecordedReflections')
        else:
            warnEmptyAttribute("numberOfFullyRecordedReflections", "XSDataInteger")
        if self._numberOfNegativeReflections is not None:
            self.numberOfNegativeReflections.export(outfile, level, name_='numberOfNegativeReflections')
        else:
            warnEmptyAttribute("numberOfNegativeReflections", "XSDataInteger")
        if self._numberOfOverlappedReflections is not None:
            self.numberOfOverlappedReflections.export(outfile, level, name_='numberOfOverlappedReflections')
        else:
            warnEmptyAttribute("numberOfOverlappedReflections", "XSDataInteger")
        if self._numberOfPartialReflections is not None:
            self.numberOfPartialReflections.export(outfile, level, name_='numberOfPartialReflections')
        else:
            warnEmptyAttribute("numberOfPartialReflections", "XSDataInteger")
        if self._numberOfReflectionsGenerated is not None:
            self.numberOfReflectionsGenerated.export(outfile, level, name_='numberOfReflectionsGenerated')
        if self._overallIOverSigma is not None:
            self.overallIOverSigma.export(outfile, level, name_='overallIOverSigma')
        else:
            warnEmptyAttribute("overallIOverSigma", "XSDataFloat")
        if self._overallStatistics is not None:
            self.overallStatistics.export(outfile, level, name_='overallStatistics')
        else:
            warnEmptyAttribute("overallStatistics", "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
        if self._refinedMosaicity is not None:
            self.refinedMosaicity.export(outfile, level, name_='refinedMosaicity')
        if self._refinedYScale is not None:
            self.refinedYScale.export(outfile, level, name_='refinedYScale')
        else:
            warnEmptyAttribute("refinedYScale", "XSDataFloat")
        if self._RMSSpotDeviation is not None:
            self.RMSSpotDeviation.export(outfile, level, name_='RMSSpotDeviation')
        else:
            warnEmptyAttribute("RMSSpotDeviation", "XSDataLength")
        for statisticsPerResolutionBin_ in self.getStatisticsPerResolutionBin():
            statisticsPerResolutionBin_.export(outfile, level, name_='statisticsPerResolutionBin')
        if self.getStatisticsPerResolutionBin() == []:
            warnEmptyAttribute("statisticsPerResolutionBin", "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfileDat':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestfileDat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfileHKL':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestfileHKL(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfilePar':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestfilePar(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'generatedMTZFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGeneratedMTZFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'highestResolutionIOverSigma':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setHighestResolutionIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfBadReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfBadReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfFullyRecordedReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfFullyRecordedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfNegativeReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfNegativeReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfOverlappedReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfOverlappedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfPartialReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfPartialReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfReflectionsGenerated':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfReflectionsGenerated(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallIOverSigma':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOverallIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallStatistics':
            obj_ = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
            obj_.build(child_)
            self.setOverallStatistics(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedMosaicity':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRefinedMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedYScale':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRefinedYScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'RMSSpotDeviation':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRMSSpotDeviation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statisticsPerResolutionBin':
            obj_ = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
            obj_.build(child_)
            self.statisticsPerResolutionBin.append(obj_)
        XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMOutputIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMOutputIntegration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMOutputIntegration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMOutputIntegration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputIntegration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputIntegration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputIntegration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputIntegration


class XSDataMOSFLMOutputPostRefinement(XSDataMOSFLMOutput):
    def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None):
        XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
    def export(self, outfile, level, name_='XSDataMOSFLMOutputPostRefinement'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputPostRefinement'):
        XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMOSFLMOutputPostRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMOSFLMOutputPostRefinement' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMOSFLMOutputPostRefinement is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMOSFLMOutputPostRefinement.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputPostRefinement()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputPostRefinement" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMOSFLMOutputPostRefinement()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputPostRefinement



# End of data representation classes.



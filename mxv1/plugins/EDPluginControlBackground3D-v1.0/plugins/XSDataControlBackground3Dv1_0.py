#!/usr/bin/env python

#
# Generated Tue Dec 10 10:15::51 2013 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataResult
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult




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



class XSDataControlImageBackground3D(object):
    def __init__(self, estimate=None, b_cryst=None, b_coef=None, rfactor=None, correlation=None, resolution=None, bfactor=None, scale=None, image=None):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'image' is not XSDataFile but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'scale' is not XSDataDouble but %s" % self._scale.__class__.__name__
            raise BaseException(strMessage)
        if bfactor is None:
            self._bfactor = None
        elif bfactor.__class__.__name__ == "XSDataDouble":
            self._bfactor = bfactor
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'bfactor' is not XSDataDouble but %s" % self._bfactor.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if correlation is None:
            self._correlation = None
        elif correlation.__class__.__name__ == "XSDataDouble":
            self._correlation = correlation
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'correlation' is not XSDataDouble but %s" % self._correlation.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if b_coef is None:
            self._b_coef = None
        elif b_coef.__class__.__name__ == "XSDataDouble":
            self._b_coef = b_coef
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'b_coef' is not XSDataDouble but %s" % self._b_coef.__class__.__name__
            raise BaseException(strMessage)
        if b_cryst is None:
            self._b_cryst = None
        elif b_cryst.__class__.__name__ == "XSDataDouble":
            self._b_cryst = b_cryst
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'b_cryst' is not XSDataDouble but %s" % self._b_cryst.__class__.__name__
            raise BaseException(strMessage)
        if estimate is None:
            self._estimate = None
        elif estimate.__class__.__name__ == "XSDataDouble":
            self._estimate = estimate
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D constructor argument 'estimate' is not XSDataDouble but %s" % self._estimate.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setImage argument is not XSDataFile but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'scale' attribute
    def getScale(self): return self._scale
    def setScale(self, scale):
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setScale argument is not XSDataDouble but %s" % scale.__class__.__name__
            raise BaseException(strMessage)
    def delScale(self): self._scale = None
    scale = property(getScale, setScale, delScale, "Property for scale")
    # Methods and properties for the 'bfactor' attribute
    def getBfactor(self): return self._bfactor
    def setBfactor(self, bfactor):
        if bfactor is None:
            self._bfactor = None
        elif bfactor.__class__.__name__ == "XSDataDouble":
            self._bfactor = bfactor
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setBfactor argument is not XSDataDouble but %s" % bfactor.__class__.__name__
            raise BaseException(strMessage)
    def delBfactor(self): self._bfactor = None
    bfactor = property(getBfactor, setBfactor, delBfactor, "Property for bfactor")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'correlation' attribute
    def getCorrelation(self): return self._correlation
    def setCorrelation(self, correlation):
        if correlation is None:
            self._correlation = None
        elif correlation.__class__.__name__ == "XSDataDouble":
            self._correlation = correlation
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setCorrelation argument is not XSDataDouble but %s" % correlation.__class__.__name__
            raise BaseException(strMessage)
    def delCorrelation(self): self._correlation = None
    correlation = property(getCorrelation, setCorrelation, delCorrelation, "Property for correlation")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'b_coef' attribute
    def getB_coef(self): return self._b_coef
    def setB_coef(self, b_coef):
        if b_coef is None:
            self._b_coef = None
        elif b_coef.__class__.__name__ == "XSDataDouble":
            self._b_coef = b_coef
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setB_coef argument is not XSDataDouble but %s" % b_coef.__class__.__name__
            raise BaseException(strMessage)
    def delB_coef(self): self._b_coef = None
    b_coef = property(getB_coef, setB_coef, delB_coef, "Property for b_coef")
    # Methods and properties for the 'b_cryst' attribute
    def getB_cryst(self): return self._b_cryst
    def setB_cryst(self, b_cryst):
        if b_cryst is None:
            self._b_cryst = None
        elif b_cryst.__class__.__name__ == "XSDataDouble":
            self._b_cryst = b_cryst
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setB_cryst argument is not XSDataDouble but %s" % b_cryst.__class__.__name__
            raise BaseException(strMessage)
    def delB_cryst(self): self._b_cryst = None
    b_cryst = property(getB_cryst, setB_cryst, delB_cryst, "Property for b_cryst")
    # Methods and properties for the 'estimate' attribute
    def getEstimate(self): return self._estimate
    def setEstimate(self, estimate):
        if estimate is None:
            self._estimate = None
        elif estimate.__class__.__name__ == "XSDataDouble":
            self._estimate = estimate
        else:
            strMessage = "ERROR! XSDataControlImageBackground3D.setEstimate argument is not XSDataDouble but %s" % estimate.__class__.__name__
            raise BaseException(strMessage)
    def delEstimate(self): self._estimate = None
    estimate = property(getEstimate, setEstimate, delEstimate, "Property for estimate")
    def export(self, outfile, level, name_='XSDataControlImageBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataControlImageBackground3D'):
        pass
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataFile")
        if self._scale is not None:
            self.scale.export(outfile, level, name_='scale')
        if self._bfactor is not None:
            self.bfactor.export(outfile, level, name_='bfactor')
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        if self._correlation is not None:
            self.correlation.export(outfile, level, name_='correlation')
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._b_coef is not None:
            self.b_coef.export(outfile, level, name_='b_coef')
        else:
            warnEmptyAttribute("b_coef", "XSDataDouble")
        if self._b_cryst is not None:
            self.b_cryst.export(outfile, level, name_='b_cryst')
        else:
            warnEmptyAttribute("b_cryst", "XSDataDouble")
        if self._estimate is not None:
            self.estimate.export(outfile, level, name_='estimate')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scale':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correlation':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCorrelation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b_coef':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setB_coef(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b_cryst':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setB_cryst(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'estimate':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setEstimate(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataControlImageBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataControlImageBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataControlImageBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataControlImageBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataControlImageBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataControlImageBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataControlImageBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataControlImageBackground3D


class XSDataInputControlBackground3D(XSDataInput):
    def __init__(self, configuration=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputControlBackground3D constructor argument 'image' is not list but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputControlBackground3D.setImage argument is not list but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def addImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputControlBackground3D.addImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image.append(value)
        else:
            strMessage = "ERROR! XSDataInputControlBackground3D.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputControlBackground3D.insertImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputControlBackground3D.insertImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image[index] = value
        else:
            strMessage = "ERROR! XSDataInputControlBackground3D.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputControlBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlBackground3D'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getImage() == []:
            warnEmptyAttribute("image", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.image.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlBackground3D


class XSDataResultControlBackground3D(XSDataResult):
    def __init__(self, status=None, imageBackground=None):
        XSDataResult.__init__(self, status)
        if imageBackground is None:
            self._imageBackground = []
        elif imageBackground.__class__.__name__ == "list":
            self._imageBackground = imageBackground
        else:
            strMessage = "ERROR! XSDataResultControlBackground3D constructor argument 'imageBackground' is not list but %s" % self._imageBackground.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageBackground' attribute
    def getImageBackground(self): return self._imageBackground
    def setImageBackground(self, imageBackground):
        if imageBackground is None:
            self._imageBackground = []
        elif imageBackground.__class__.__name__ == "list":
            self._imageBackground = imageBackground
        else:
            strMessage = "ERROR! XSDataResultControlBackground3D.setImageBackground argument is not list but %s" % imageBackground.__class__.__name__
            raise BaseException(strMessage)
    def delImageBackground(self): self._imageBackground = None
    imageBackground = property(getImageBackground, setImageBackground, delImageBackground, "Property for imageBackground")
    def addImageBackground(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultControlBackground3D.addImageBackground argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataControlImageBackground3D":
            self._imageBackground.append(value)
        else:
            strMessage = "ERROR! XSDataResultControlBackground3D.addImageBackground argument is not XSDataControlImageBackground3D but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImageBackground(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultControlBackground3D.insertImageBackground argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultControlBackground3D.insertImageBackground argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataControlImageBackground3D":
            self._imageBackground[index] = value
        else:
            strMessage = "ERROR! XSDataResultControlBackground3D.addImageBackground argument is not XSDataControlImageBackground3D but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultControlBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlBackground3D'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for imageBackground_ in self.getImageBackground():
            imageBackground_.export(outfile, level, name_='imageBackground')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageBackground':
            obj_ = XSDataControlImageBackground3D()
            obj_.build(child_)
            self.imageBackground.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultControlBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlBackground3D



# End of data representation classes.



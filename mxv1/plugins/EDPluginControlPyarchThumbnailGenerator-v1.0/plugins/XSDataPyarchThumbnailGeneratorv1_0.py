#!/usr/bin/env python

#
# Generated Mon Feb 3 03:01::03 2014 by EDGenerateDS.
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
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataTime
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
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataTime




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



class XSDataInputPyarchThumbnailGenerator(XSDataInput):
    def __init__(self, configuration=None, waitForFileTimeOut=None, forcedOutputDirectory=None, diffractionImage=None):
        XSDataInput.__init__(self, configuration)
        if diffractionImage is None:
            self._diffractionImage = None
        elif diffractionImage.__class__.__name__ == "XSDataFile":
            self._diffractionImage = diffractionImage
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator constructor argument 'diffractionImage' is not XSDataFile but %s" % self._diffractionImage.__class__.__name__
            raise BaseException(strMessage)
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator constructor argument 'forcedOutputDirectory' is not XSDataFile but %s" % self._forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
        if waitForFileTimeOut is None:
            self._waitForFileTimeOut = None
        elif waitForFileTimeOut.__class__.__name__ == "XSDataTime":
            self._waitForFileTimeOut = waitForFileTimeOut
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator constructor argument 'waitForFileTimeOut' is not XSDataTime but %s" % self._waitForFileTimeOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'diffractionImage' attribute
    def getDiffractionImage(self): return self._diffractionImage
    def setDiffractionImage(self, diffractionImage):
        if diffractionImage is None:
            self._diffractionImage = None
        elif diffractionImage.__class__.__name__ == "XSDataFile":
            self._diffractionImage = diffractionImage
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator.setDiffractionImage argument is not XSDataFile but %s" % diffractionImage.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionImage(self): self._diffractionImage = None
    diffractionImage = property(getDiffractionImage, setDiffractionImage, delDiffractionImage, "Property for diffractionImage")
    # Methods and properties for the 'forcedOutputDirectory' attribute
    def getForcedOutputDirectory(self): return self._forcedOutputDirectory
    def setForcedOutputDirectory(self, forcedOutputDirectory):
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator.setForcedOutputDirectory argument is not XSDataFile but %s" % forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delForcedOutputDirectory(self): self._forcedOutputDirectory = None
    forcedOutputDirectory = property(getForcedOutputDirectory, setForcedOutputDirectory, delForcedOutputDirectory, "Property for forcedOutputDirectory")
    # Methods and properties for the 'waitForFileTimeOut' attribute
    def getWaitForFileTimeOut(self): return self._waitForFileTimeOut
    def setWaitForFileTimeOut(self, waitForFileTimeOut):
        if waitForFileTimeOut is None:
            self._waitForFileTimeOut = None
        elif waitForFileTimeOut.__class__.__name__ == "XSDataTime":
            self._waitForFileTimeOut = waitForFileTimeOut
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGenerator.setWaitForFileTimeOut argument is not XSDataTime but %s" % waitForFileTimeOut.__class__.__name__
            raise BaseException(strMessage)
    def delWaitForFileTimeOut(self): self._waitForFileTimeOut = None
    waitForFileTimeOut = property(getWaitForFileTimeOut, setWaitForFileTimeOut, delWaitForFileTimeOut, "Property for waitForFileTimeOut")
    def export(self, outfile, level, name_='XSDataInputPyarchThumbnailGenerator'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputPyarchThumbnailGenerator'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._diffractionImage is not None:
            self.diffractionImage.export(outfile, level, name_='diffractionImage')
        else:
            warnEmptyAttribute("diffractionImage", "XSDataFile")
        if self._forcedOutputDirectory is not None:
            self.forcedOutputDirectory.export(outfile, level, name_='forcedOutputDirectory')
        if self._waitForFileTimeOut is not None:
            self.waitForFileTimeOut.export(outfile, level, name_='waitForFileTimeOut')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDiffractionImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedOutputDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForcedOutputDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'waitForFileTimeOut':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setWaitForFileTimeOut(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputPyarchThumbnailGenerator" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputPyarchThumbnailGenerator' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputPyarchThumbnailGenerator is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputPyarchThumbnailGenerator.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputPyarchThumbnailGenerator()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputPyarchThumbnailGenerator" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputPyarchThumbnailGenerator()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputPyarchThumbnailGenerator


class XSDataInputPyarchThumbnailGeneratorParallel(XSDataInput):
    def __init__(self, configuration=None, waitForFileTimeOut=None, forcedOutputDirectory=None, diffractionImage=None):
        XSDataInput.__init__(self, configuration)
        if diffractionImage is None:
            self._diffractionImage = []
        elif diffractionImage.__class__.__name__ == "list":
            self._diffractionImage = diffractionImage
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel constructor argument 'diffractionImage' is not list but %s" % self._diffractionImage.__class__.__name__
            raise BaseException(strMessage)
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel constructor argument 'forcedOutputDirectory' is not XSDataFile but %s" % self._forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
        if waitForFileTimeOut is None:
            self._waitForFileTimeOut = None
        elif waitForFileTimeOut.__class__.__name__ == "XSDataTime":
            self._waitForFileTimeOut = waitForFileTimeOut
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel constructor argument 'waitForFileTimeOut' is not XSDataTime but %s" % self._waitForFileTimeOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'diffractionImage' attribute
    def getDiffractionImage(self): return self._diffractionImage
    def setDiffractionImage(self, diffractionImage):
        if diffractionImage is None:
            self._diffractionImage = []
        elif diffractionImage.__class__.__name__ == "list":
            self._diffractionImage = diffractionImage
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.setDiffractionImage argument is not list but %s" % diffractionImage.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionImage(self): self._diffractionImage = None
    diffractionImage = property(getDiffractionImage, setDiffractionImage, delDiffractionImage, "Property for diffractionImage")
    def addDiffractionImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.addDiffractionImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._diffractionImage.append(value)
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.addDiffractionImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDiffractionImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.insertDiffractionImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.insertDiffractionImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._diffractionImage[index] = value
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.addDiffractionImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'forcedOutputDirectory' attribute
    def getForcedOutputDirectory(self): return self._forcedOutputDirectory
    def setForcedOutputDirectory(self, forcedOutputDirectory):
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.setForcedOutputDirectory argument is not XSDataFile but %s" % forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delForcedOutputDirectory(self): self._forcedOutputDirectory = None
    forcedOutputDirectory = property(getForcedOutputDirectory, setForcedOutputDirectory, delForcedOutputDirectory, "Property for forcedOutputDirectory")
    # Methods and properties for the 'waitForFileTimeOut' attribute
    def getWaitForFileTimeOut(self): return self._waitForFileTimeOut
    def setWaitForFileTimeOut(self, waitForFileTimeOut):
        if waitForFileTimeOut is None:
            self._waitForFileTimeOut = None
        elif waitForFileTimeOut.__class__.__name__ == "XSDataTime":
            self._waitForFileTimeOut = waitForFileTimeOut
        else:
            strMessage = "ERROR! XSDataInputPyarchThumbnailGeneratorParallel.setWaitForFileTimeOut argument is not XSDataTime but %s" % waitForFileTimeOut.__class__.__name__
            raise BaseException(strMessage)
    def delWaitForFileTimeOut(self): self._waitForFileTimeOut = None
    waitForFileTimeOut = property(getWaitForFileTimeOut, setWaitForFileTimeOut, delWaitForFileTimeOut, "Property for waitForFileTimeOut")
    def export(self, outfile, level, name_='XSDataInputPyarchThumbnailGeneratorParallel'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputPyarchThumbnailGeneratorParallel'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for diffractionImage_ in self.getDiffractionImage():
            diffractionImage_.export(outfile, level, name_='diffractionImage')
        if self.getDiffractionImage() == []:
            warnEmptyAttribute("diffractionImage", "XSDataFile")
        if self._forcedOutputDirectory is not None:
            self.forcedOutputDirectory.export(outfile, level, name_='forcedOutputDirectory')
        if self._waitForFileTimeOut is not None:
            self.waitForFileTimeOut.export(outfile, level, name_='waitForFileTimeOut')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.diffractionImage.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedOutputDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForcedOutputDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'waitForFileTimeOut':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setWaitForFileTimeOut(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputPyarchThumbnailGeneratorParallel" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputPyarchThumbnailGeneratorParallel' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputPyarchThumbnailGeneratorParallel is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputPyarchThumbnailGeneratorParallel.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputPyarchThumbnailGeneratorParallel()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputPyarchThumbnailGeneratorParallel" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputPyarchThumbnailGeneratorParallel()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputPyarchThumbnailGeneratorParallel


class XSDataResultPyarchThumbnailGenerator(XSDataResult):
    def __init__(self, status=None, pathToThumbImage=None, pathToJPEGImage=None):
        XSDataResult.__init__(self, status)
        if pathToJPEGImage is None:
            self._pathToJPEGImage = None
        elif pathToJPEGImage.__class__.__name__ == "XSDataFile":
            self._pathToJPEGImage = pathToJPEGImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGenerator constructor argument 'pathToJPEGImage' is not XSDataFile but %s" % self._pathToJPEGImage.__class__.__name__
            raise BaseException(strMessage)
        if pathToThumbImage is None:
            self._pathToThumbImage = None
        elif pathToThumbImage.__class__.__name__ == "XSDataFile":
            self._pathToThumbImage = pathToThumbImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGenerator constructor argument 'pathToThumbImage' is not XSDataFile but %s" % self._pathToThumbImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pathToJPEGImage' attribute
    def getPathToJPEGImage(self): return self._pathToJPEGImage
    def setPathToJPEGImage(self, pathToJPEGImage):
        if pathToJPEGImage is None:
            self._pathToJPEGImage = None
        elif pathToJPEGImage.__class__.__name__ == "XSDataFile":
            self._pathToJPEGImage = pathToJPEGImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGenerator.setPathToJPEGImage argument is not XSDataFile but %s" % pathToJPEGImage.__class__.__name__
            raise BaseException(strMessage)
    def delPathToJPEGImage(self): self._pathToJPEGImage = None
    pathToJPEGImage = property(getPathToJPEGImage, setPathToJPEGImage, delPathToJPEGImage, "Property for pathToJPEGImage")
    # Methods and properties for the 'pathToThumbImage' attribute
    def getPathToThumbImage(self): return self._pathToThumbImage
    def setPathToThumbImage(self, pathToThumbImage):
        if pathToThumbImage is None:
            self._pathToThumbImage = None
        elif pathToThumbImage.__class__.__name__ == "XSDataFile":
            self._pathToThumbImage = pathToThumbImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGenerator.setPathToThumbImage argument is not XSDataFile but %s" % pathToThumbImage.__class__.__name__
            raise BaseException(strMessage)
    def delPathToThumbImage(self): self._pathToThumbImage = None
    pathToThumbImage = property(getPathToThumbImage, setPathToThumbImage, delPathToThumbImage, "Property for pathToThumbImage")
    def export(self, outfile, level, name_='XSDataResultPyarchThumbnailGenerator'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultPyarchThumbnailGenerator'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._pathToJPEGImage is not None:
            self.pathToJPEGImage.export(outfile, level, name_='pathToJPEGImage')
        if self._pathToThumbImage is not None:
            self.pathToThumbImage.export(outfile, level, name_='pathToThumbImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToJPEGImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToJPEGImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToThumbImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToThumbImage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultPyarchThumbnailGenerator" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultPyarchThumbnailGenerator' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultPyarchThumbnailGenerator is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultPyarchThumbnailGenerator.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultPyarchThumbnailGenerator()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultPyarchThumbnailGenerator" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultPyarchThumbnailGenerator()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultPyarchThumbnailGenerator


class XSDataResultPyarchThumbnailGeneratorParallel(XSDataResult):
    def __init__(self, status=None, pathToThumbImage=None, pathToJPEGImage=None):
        XSDataResult.__init__(self, status)
        if pathToJPEGImage is None:
            self._pathToJPEGImage = []
        elif pathToJPEGImage.__class__.__name__ == "list":
            self._pathToJPEGImage = pathToJPEGImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel constructor argument 'pathToJPEGImage' is not list but %s" % self._pathToJPEGImage.__class__.__name__
            raise BaseException(strMessage)
        if pathToThumbImage is None:
            self._pathToThumbImage = []
        elif pathToThumbImage.__class__.__name__ == "list":
            self._pathToThumbImage = pathToThumbImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel constructor argument 'pathToThumbImage' is not list but %s" % self._pathToThumbImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pathToJPEGImage' attribute
    def getPathToJPEGImage(self): return self._pathToJPEGImage
    def setPathToJPEGImage(self, pathToJPEGImage):
        if pathToJPEGImage is None:
            self._pathToJPEGImage = []
        elif pathToJPEGImage.__class__.__name__ == "list":
            self._pathToJPEGImage = pathToJPEGImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.setPathToJPEGImage argument is not list but %s" % pathToJPEGImage.__class__.__name__
            raise BaseException(strMessage)
    def delPathToJPEGImage(self): self._pathToJPEGImage = None
    pathToJPEGImage = property(getPathToJPEGImage, setPathToJPEGImage, delPathToJPEGImage, "Property for pathToJPEGImage")
    def addPathToJPEGImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToJPEGImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pathToJPEGImage.append(value)
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToJPEGImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPathToJPEGImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.insertPathToJPEGImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.insertPathToJPEGImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pathToJPEGImage[index] = value
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToJPEGImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pathToThumbImage' attribute
    def getPathToThumbImage(self): return self._pathToThumbImage
    def setPathToThumbImage(self, pathToThumbImage):
        if pathToThumbImage is None:
            self._pathToThumbImage = []
        elif pathToThumbImage.__class__.__name__ == "list":
            self._pathToThumbImage = pathToThumbImage
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.setPathToThumbImage argument is not list but %s" % pathToThumbImage.__class__.__name__
            raise BaseException(strMessage)
    def delPathToThumbImage(self): self._pathToThumbImage = None
    pathToThumbImage = property(getPathToThumbImage, setPathToThumbImage, delPathToThumbImage, "Property for pathToThumbImage")
    def addPathToThumbImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToThumbImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pathToThumbImage.append(value)
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToThumbImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPathToThumbImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.insertPathToThumbImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.insertPathToThumbImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pathToThumbImage[index] = value
        else:
            strMessage = "ERROR! XSDataResultPyarchThumbnailGeneratorParallel.addPathToThumbImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultPyarchThumbnailGeneratorParallel'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultPyarchThumbnailGeneratorParallel'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for pathToJPEGImage_ in self.getPathToJPEGImage():
            pathToJPEGImage_.export(outfile, level, name_='pathToJPEGImage')
        for pathToThumbImage_ in self.getPathToThumbImage():
            pathToThumbImage_.export(outfile, level, name_='pathToThumbImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToJPEGImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.pathToJPEGImage.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToThumbImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.pathToThumbImage.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultPyarchThumbnailGeneratorParallel" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultPyarchThumbnailGeneratorParallel' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultPyarchThumbnailGeneratorParallel is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultPyarchThumbnailGeneratorParallel.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultPyarchThumbnailGeneratorParallel()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultPyarchThumbnailGeneratorParallel" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultPyarchThumbnailGeneratorParallel()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultPyarchThumbnailGeneratorParallel



# End of data representation classes.



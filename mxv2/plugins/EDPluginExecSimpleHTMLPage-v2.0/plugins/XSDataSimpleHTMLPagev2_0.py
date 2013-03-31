#!/usr/bin/env python

#
# Generated Mon Dec 3 01:45::44 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv2": "mxv2/datamodel", \
}

try:
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataResult
    from XSDataMXv1 import XSDataResultCharacterisation
    from XSDataMXv2 import XSDataResultCharacterisationv2_0
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
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv2 import XSDataResultCharacterisationv2_0




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



class XSDataInputSimpleHTMLPage(XSDataInput):
    def __init__(self, configuration=None, fileGraph=None, characterisationResultv2_0=None, characterisationResult=None):
        XSDataInput.__init__(self, configuration)
        if characterisationResult is None:
            self._characterisationResult = None
        elif characterisationResult.__class__.__name__ == "XSDataResultCharacterisation":
            self._characterisationResult = characterisationResult
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage constructor argument 'characterisationResult' is not XSDataResultCharacterisation but %s" % self._characterisationResult.__class__.__name__
            raise BaseException(strMessage)
        if characterisationResultv2_0 is None:
            self._characterisationResultv2_0 = None
        elif characterisationResultv2_0.__class__.__name__ == "XSDataResultCharacterisationv2_0":
            self._characterisationResultv2_0 = characterisationResultv2_0
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage constructor argument 'characterisationResultv2_0' is not XSDataResultCharacterisationv2_0 but %s" % self._characterisationResultv2_0.__class__.__name__
            raise BaseException(strMessage)
        if fileGraph is None:
            self._fileGraph = []
        elif fileGraph.__class__.__name__ == "list":
            self._fileGraph = fileGraph
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage constructor argument 'fileGraph' is not list but %s" % self._fileGraph.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'characterisationResult' attribute
    def getCharacterisationResult(self): return self._characterisationResult
    def setCharacterisationResult(self, characterisationResult):
        if characterisationResult is None:
            self._characterisationResult = None
        elif characterisationResult.__class__.__name__ == "XSDataResultCharacterisation":
            self._characterisationResult = characterisationResult
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.setCharacterisationResult argument is not XSDataResultCharacterisation but %s" % characterisationResult.__class__.__name__
            raise BaseException(strMessage)
    def delCharacterisationResult(self): self._characterisationResult = None
    characterisationResult = property(getCharacterisationResult, setCharacterisationResult, delCharacterisationResult, "Property for characterisationResult")
    # Methods and properties for the 'characterisationResultv2_0' attribute
    def getCharacterisationResultv2_0(self): return self._characterisationResultv2_0
    def setCharacterisationResultv2_0(self, characterisationResultv2_0):
        if characterisationResultv2_0 is None:
            self._characterisationResultv2_0 = None
        elif characterisationResultv2_0.__class__.__name__ == "XSDataResultCharacterisationv2_0":
            self._characterisationResultv2_0 = characterisationResultv2_0
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.setCharacterisationResultv2_0 argument is not XSDataResultCharacterisationv2_0 but %s" % characterisationResultv2_0.__class__.__name__
            raise BaseException(strMessage)
    def delCharacterisationResultv2_0(self): self._characterisationResultv2_0 = None
    characterisationResultv2_0 = property(getCharacterisationResultv2_0, setCharacterisationResultv2_0, delCharacterisationResultv2_0, "Property for characterisationResultv2_0")
    # Methods and properties for the 'fileGraph' attribute
    def getFileGraph(self): return self._fileGraph
    def setFileGraph(self, fileGraph):
        if fileGraph is None:
            self._fileGraph = []
        elif fileGraph.__class__.__name__ == "list":
            self._fileGraph = fileGraph
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.setFileGraph argument is not list but %s" % fileGraph.__class__.__name__
            raise BaseException(strMessage)
    def delFileGraph(self): self._fileGraph = None
    fileGraph = property(getFileGraph, setFileGraph, delFileGraph, "Property for fileGraph")
    def addFileGraph(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.addFileGraph argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._fileGraph.append(value)
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.addFileGraph argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFileGraph(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.insertFileGraph argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.insertFileGraph argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._fileGraph[index] = value
        else:
            strMessage = "ERROR! XSDataInputSimpleHTMLPage.addFileGraph argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputSimpleHTMLPage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSimpleHTMLPage'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._characterisationResult is not None:
            self.characterisationResult.export(outfile, level, name_='characterisationResult')
        if self._characterisationResultv2_0 is not None:
            self.characterisationResultv2_0.export(outfile, level, name_='characterisationResultv2_0')
        for fileGraph_ in self.getFileGraph():
            fileGraph_.export(outfile, level, name_='fileGraph')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'characterisationResult':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setCharacterisationResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'characterisationResultv2_0':
            obj_ = XSDataResultCharacterisationv2_0()
            obj_.build(child_)
            self.setCharacterisationResultv2_0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileGraph':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.fileGraph.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSimpleHTMLPage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSimpleHTMLPage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSimpleHTMLPage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSimpleHTMLPage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSimpleHTMLPage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSimpleHTMLPage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSimpleHTMLPage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSimpleHTMLPage


class XSDataResultSimpleHTMLPage(XSDataResult):
    def __init__(self, status=None, pathToHTMLDirectory=None, pathToHTMLFile=None):
        XSDataResult.__init__(self, status)
        if pathToHTMLFile is None:
            self._pathToHTMLFile = None
        elif pathToHTMLFile.__class__.__name__ == "XSDataFile":
            self._pathToHTMLFile = pathToHTMLFile
        else:
            strMessage = "ERROR! XSDataResultSimpleHTMLPage constructor argument 'pathToHTMLFile' is not XSDataFile but %s" % self._pathToHTMLFile.__class__.__name__
            raise BaseException(strMessage)
        if pathToHTMLDirectory is None:
            self._pathToHTMLDirectory = None
        elif pathToHTMLDirectory.__class__.__name__ == "XSDataFile":
            self._pathToHTMLDirectory = pathToHTMLDirectory
        else:
            strMessage = "ERROR! XSDataResultSimpleHTMLPage constructor argument 'pathToHTMLDirectory' is not XSDataFile but %s" % self._pathToHTMLDirectory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pathToHTMLFile' attribute
    def getPathToHTMLFile(self): return self._pathToHTMLFile
    def setPathToHTMLFile(self, pathToHTMLFile):
        if pathToHTMLFile is None:
            self._pathToHTMLFile = None
        elif pathToHTMLFile.__class__.__name__ == "XSDataFile":
            self._pathToHTMLFile = pathToHTMLFile
        else:
            strMessage = "ERROR! XSDataResultSimpleHTMLPage.setPathToHTMLFile argument is not XSDataFile but %s" % pathToHTMLFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToHTMLFile(self): self._pathToHTMLFile = None
    pathToHTMLFile = property(getPathToHTMLFile, setPathToHTMLFile, delPathToHTMLFile, "Property for pathToHTMLFile")
    # Methods and properties for the 'pathToHTMLDirectory' attribute
    def getPathToHTMLDirectory(self): return self._pathToHTMLDirectory
    def setPathToHTMLDirectory(self, pathToHTMLDirectory):
        if pathToHTMLDirectory is None:
            self._pathToHTMLDirectory = None
        elif pathToHTMLDirectory.__class__.__name__ == "XSDataFile":
            self._pathToHTMLDirectory = pathToHTMLDirectory
        else:
            strMessage = "ERROR! XSDataResultSimpleHTMLPage.setPathToHTMLDirectory argument is not XSDataFile but %s" % pathToHTMLDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delPathToHTMLDirectory(self): self._pathToHTMLDirectory = None
    pathToHTMLDirectory = property(getPathToHTMLDirectory, setPathToHTMLDirectory, delPathToHTMLDirectory, "Property for pathToHTMLDirectory")
    def export(self, outfile, level, name_='XSDataResultSimpleHTMLPage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSimpleHTMLPage'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._pathToHTMLFile is not None:
            self.pathToHTMLFile.export(outfile, level, name_='pathToHTMLFile')
        else:
            warnEmptyAttribute("pathToHTMLFile", "XSDataFile")
        if self._pathToHTMLDirectory is not None:
            self.pathToHTMLDirectory.export(outfile, level, name_='pathToHTMLDirectory')
        else:
            warnEmptyAttribute("pathToHTMLDirectory", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToHTMLFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToHTMLFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToHTMLDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToHTMLDirectory(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSimpleHTMLPage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSimpleHTMLPage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSimpleHTMLPage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSimpleHTMLPage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSimpleHTMLPage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSimpleHTMLPage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSimpleHTMLPage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSimpleHTMLPage



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Wed May 22 02:22::55 2013 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
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
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
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



class XSDataInputReadDataBM23(XSDataInput):
    def __init__(self, configuration=None, nSkipHeader=None, inputFile=None):
        XSDataInput.__init__(self, configuration)
        if inputFile is None:
            self._inputFile = None
        elif inputFile.__class__.__name__ == "XSDataFile":
            self._inputFile = inputFile
        else:
            strMessage = "ERROR! XSDataInputReadDataBM23 constructor argument 'inputFile' is not XSDataFile but %s" % self._inputFile.__class__.__name__
            raise BaseException(strMessage)
        if nSkipHeader is None:
            self._nSkipHeader = None
        elif nSkipHeader.__class__.__name__ == "XSDataInteger":
            self._nSkipHeader = nSkipHeader
        else:
            strMessage = "ERROR! XSDataInputReadDataBM23 constructor argument 'nSkipHeader' is not XSDataInteger but %s" % self._nSkipHeader.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputFile' attribute
    def getInputFile(self): return self._inputFile
    def setInputFile(self, inputFile):
        if inputFile is None:
            self._inputFile = None
        elif inputFile.__class__.__name__ == "XSDataFile":
            self._inputFile = inputFile
        else:
            strMessage = "ERROR! XSDataInputReadDataBM23.setInputFile argument is not XSDataFile but %s" % inputFile.__class__.__name__
            raise BaseException(strMessage)
    def delInputFile(self): self._inputFile = None
    inputFile = property(getInputFile, setInputFile, delInputFile, "Property for inputFile")
    # Methods and properties for the 'nSkipHeader' attribute
    def getNSkipHeader(self): return self._nSkipHeader
    def setNSkipHeader(self, nSkipHeader):
        if nSkipHeader is None:
            self._nSkipHeader = None
        elif nSkipHeader.__class__.__name__ == "XSDataInteger":
            self._nSkipHeader = nSkipHeader
        else:
            strMessage = "ERROR! XSDataInputReadDataBM23.setNSkipHeader argument is not XSDataInteger but %s" % nSkipHeader.__class__.__name__
            raise BaseException(strMessage)
    def delNSkipHeader(self): self._nSkipHeader = None
    nSkipHeader = property(getNSkipHeader, setNSkipHeader, delNSkipHeader, "Property for nSkipHeader")
    def export(self, outfile, level, name_='XSDataInputReadDataBM23'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputReadDataBM23'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputFile is not None:
            self.inputFile.export(outfile, level, name_='inputFile')
        else:
            warnEmptyAttribute("inputFile", "XSDataFile")
        if self._nSkipHeader is not None:
            self.nSkipHeader.export(outfile, level, name_='nSkipHeader')
        else:
            warnEmptyAttribute("nSkipHeader", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nSkipHeader':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNSkipHeader(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputReadDataBM23" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputReadDataBM23' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputReadDataBM23 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputReadDataBM23.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadDataBM23()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputReadDataBM23" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadDataBM23()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputReadDataBM23


class XSDataResultReadDataBM23(XSDataResult):
    def __init__(self, status=None, dataArray=None, energy=None):
        XSDataResult.__init__(self, status)
        if energy is None:
            self._energy = None
        elif energy.__class__.__name__ == "XSDataArray":
            self._energy = energy
        else:
            strMessage = "ERROR! XSDataResultReadDataBM23 constructor argument 'energy' is not XSDataArray but %s" % self._energy.__class__.__name__
            raise BaseException(strMessage)
        if dataArray is None:
            self._dataArray = None
        elif dataArray.__class__.__name__ == "XSDataArray":
            self._dataArray = dataArray
        else:
            strMessage = "ERROR! XSDataResultReadDataBM23 constructor argument 'dataArray' is not XSDataArray but %s" % self._dataArray.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'energy' attribute
    def getEnergy(self): return self._energy
    def setEnergy(self, energy):
        if energy is None:
            self._energy = None
        elif energy.__class__.__name__ == "XSDataArray":
            self._energy = energy
        else:
            strMessage = "ERROR! XSDataResultReadDataBM23.setEnergy argument is not XSDataArray but %s" % energy.__class__.__name__
            raise BaseException(strMessage)
    def delEnergy(self): self._energy = None
    energy = property(getEnergy, setEnergy, delEnergy, "Property for energy")
    # Methods and properties for the 'dataArray' attribute
    def getDataArray(self): return self._dataArray
    def setDataArray(self, dataArray):
        if dataArray is None:
            self._dataArray = None
        elif dataArray.__class__.__name__ == "XSDataArray":
            self._dataArray = dataArray
        else:
            strMessage = "ERROR! XSDataResultReadDataBM23.setDataArray argument is not XSDataArray but %s" % dataArray.__class__.__name__
            raise BaseException(strMessage)
    def delDataArray(self): self._dataArray = None
    dataArray = property(getDataArray, setDataArray, delDataArray, "Property for dataArray")
    def export(self, outfile, level, name_='XSDataResultReadDataBM23'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultReadDataBM23'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._energy is not None:
            self.energy.export(outfile, level, name_='energy')
        if self._dataArray is not None:
            self.dataArray.export(outfile, level, name_='dataArray')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'energy':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setEnergy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setDataArray(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultReadDataBM23" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultReadDataBM23' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultReadDataBM23 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultReadDataBM23.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadDataBM23()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultReadDataBM23" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadDataBM23()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultReadDataBM23



# End of data representation classes.



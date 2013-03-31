#!/usr/bin/env python

#
# Generated Mon Jan 14 11:03::28 2013 by EDGenerateDS.
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
from XSDataCommon import XSDataArray
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



class XSDataEnergyCalibration(object):
    def __init__(self, d=None, c=None, b=None, a=None):
        if a is None:
            self._a = None
        elif a.__class__.__name__ == "XSDataDouble":
            self._a = a
        else:
            strMessage = "ERROR! XSDataEnergyCalibration constructor argument 'a' is not XSDataDouble but %s" % self._a.__class__.__name__
            raise BaseException(strMessage)
        if b is None:
            self._b = None
        elif b.__class__.__name__ == "XSDataDouble":
            self._b = b
        else:
            strMessage = "ERROR! XSDataEnergyCalibration constructor argument 'b' is not XSDataDouble but %s" % self._b.__class__.__name__
            raise BaseException(strMessage)
        if c is None:
            self._c = None
        elif c.__class__.__name__ == "XSDataDouble":
            self._c = c
        else:
            strMessage = "ERROR! XSDataEnergyCalibration constructor argument 'c' is not XSDataDouble but %s" % self._c.__class__.__name__
            raise BaseException(strMessage)
        if d is None:
            self._d = None
        elif d.__class__.__name__ == "XSDataDouble":
            self._d = d
        else:
            strMessage = "ERROR! XSDataEnergyCalibration constructor argument 'd' is not XSDataDouble but %s" % self._d.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'a' attribute
    def getA(self): return self._a
    def setA(self, a):
        if a is None:
            self._a = None
        elif a.__class__.__name__ == "XSDataDouble":
            self._a = a
        else:
            strMessage = "ERROR! XSDataEnergyCalibration.setA argument is not XSDataDouble but %s" % a.__class__.__name__
            raise BaseException(strMessage)
    def delA(self): self._a = None
    a = property(getA, setA, delA, "Property for a")
    # Methods and properties for the 'b' attribute
    def getB(self): return self._b
    def setB(self, b):
        if b is None:
            self._b = None
        elif b.__class__.__name__ == "XSDataDouble":
            self._b = b
        else:
            strMessage = "ERROR! XSDataEnergyCalibration.setB argument is not XSDataDouble but %s" % b.__class__.__name__
            raise BaseException(strMessage)
    def delB(self): self._b = None
    b = property(getB, setB, delB, "Property for b")
    # Methods and properties for the 'c' attribute
    def getC(self): return self._c
    def setC(self, c):
        if c is None:
            self._c = None
        elif c.__class__.__name__ == "XSDataDouble":
            self._c = c
        else:
            strMessage = "ERROR! XSDataEnergyCalibration.setC argument is not XSDataDouble but %s" % c.__class__.__name__
            raise BaseException(strMessage)
    def delC(self): self._c = None
    c = property(getC, setC, delC, "Property for c")
    # Methods and properties for the 'd' attribute
    def getD(self): return self._d
    def setD(self, d):
        if d is None:
            self._d = None
        elif d.__class__.__name__ == "XSDataDouble":
            self._d = d
        else:
            strMessage = "ERROR! XSDataEnergyCalibration.setD argument is not XSDataDouble but %s" % d.__class__.__name__
            raise BaseException(strMessage)
    def delD(self): self._d = None
    d = property(getD, setD, delD, "Property for d")
    def export(self, outfile, level, name_='XSDataEnergyCalibration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataEnergyCalibration'):
        pass
        if self._a is not None:
            self.a.export(outfile, level, name_='a')
        else:
            warnEmptyAttribute("a", "XSDataDouble")
        if self._b is not None:
            self.b.export(outfile, level, name_='b')
        else:
            warnEmptyAttribute("b", "XSDataDouble")
        if self._c is not None:
            self.c.export(outfile, level, name_='c')
        if self._d is not None:
            self.d.export(outfile, level, name_='d')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'a':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setA(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setB(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'c':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setC(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'd':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setD(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataEnergyCalibration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataEnergyCalibration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataEnergyCalibration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataEnergyCalibration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataEnergyCalibration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataEnergyCalibration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataEnergyCalibration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataEnergyCalibration


class XSDataInputReadDataID24(XSDataInput):
    def __init__(self, configuration=None, energyCalibration=None, inputFile=None):
        XSDataInput.__init__(self, configuration)
        if inputFile is None:
            self._inputFile = None
        elif inputFile.__class__.__name__ == "XSDataFile":
            self._inputFile = inputFile
        else:
            strMessage = "ERROR! XSDataInputReadDataID24 constructor argument 'inputFile' is not XSDataFile but %s" % self._inputFile.__class__.__name__
            raise BaseException(strMessage)
        if energyCalibration is None:
            self._energyCalibration = None
        elif energyCalibration.__class__.__name__ == "XSDataEnergyCalibration":
            self._energyCalibration = energyCalibration
        else:
            strMessage = "ERROR! XSDataInputReadDataID24 constructor argument 'energyCalibration' is not XSDataEnergyCalibration but %s" % self._energyCalibration.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputFile' attribute
    def getInputFile(self): return self._inputFile
    def setInputFile(self, inputFile):
        if inputFile is None:
            self._inputFile = None
        elif inputFile.__class__.__name__ == "XSDataFile":
            self._inputFile = inputFile
        else:
            strMessage = "ERROR! XSDataInputReadDataID24.setInputFile argument is not XSDataFile but %s" % inputFile.__class__.__name__
            raise BaseException(strMessage)
    def delInputFile(self): self._inputFile = None
    inputFile = property(getInputFile, setInputFile, delInputFile, "Property for inputFile")
    # Methods and properties for the 'energyCalibration' attribute
    def getEnergyCalibration(self): return self._energyCalibration
    def setEnergyCalibration(self, energyCalibration):
        if energyCalibration is None:
            self._energyCalibration = None
        elif energyCalibration.__class__.__name__ == "XSDataEnergyCalibration":
            self._energyCalibration = energyCalibration
        else:
            strMessage = "ERROR! XSDataInputReadDataID24.setEnergyCalibration argument is not XSDataEnergyCalibration but %s" % energyCalibration.__class__.__name__
            raise BaseException(strMessage)
    def delEnergyCalibration(self): self._energyCalibration = None
    energyCalibration = property(getEnergyCalibration, setEnergyCalibration, delEnergyCalibration, "Property for energyCalibration")
    def export(self, outfile, level, name_='XSDataInputReadDataID24'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputReadDataID24'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputFile is not None:
            self.inputFile.export(outfile, level, name_='inputFile')
        else:
            warnEmptyAttribute("inputFile", "XSDataFile")
        if self._energyCalibration is not None:
            self.energyCalibration.export(outfile, level, name_='energyCalibration')
        else:
            warnEmptyAttribute("energyCalibration", "XSDataEnergyCalibration")
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
            nodeName_ == 'energyCalibration':
            obj_ = XSDataEnergyCalibration()
            obj_.build(child_)
            self.setEnergyCalibration(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputReadDataID24" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputReadDataID24' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputReadDataID24 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputReadDataID24.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadDataID24()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputReadDataID24" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadDataID24()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputReadDataID24


class XSDataResultReadDataID24(XSDataResult):
    def __init__(self, status=None, dataArray=None, energy=None):
        XSDataResult.__init__(self, status)
        if energy is None:
            self._energy = None
        elif energy.__class__.__name__ == "XSDataArray":
            self._energy = energy
        else:
            strMessage = "ERROR! XSDataResultReadDataID24 constructor argument 'energy' is not XSDataArray but %s" % self._energy.__class__.__name__
            raise BaseException(strMessage)
        if dataArray is None:
            self._dataArray = None
        elif dataArray.__class__.__name__ == "XSDataArray":
            self._dataArray = dataArray
        else:
            strMessage = "ERROR! XSDataResultReadDataID24 constructor argument 'dataArray' is not XSDataArray but %s" % self._dataArray.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'energy' attribute
    def getEnergy(self): return self._energy
    def setEnergy(self, energy):
        if energy is None:
            self._energy = None
        elif energy.__class__.__name__ == "XSDataArray":
            self._energy = energy
        else:
            strMessage = "ERROR! XSDataResultReadDataID24.setEnergy argument is not XSDataArray but %s" % energy.__class__.__name__
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
            strMessage = "ERROR! XSDataResultReadDataID24.setDataArray argument is not XSDataArray but %s" % dataArray.__class__.__name__
            raise BaseException(strMessage)
    def delDataArray(self): self._dataArray = None
    dataArray = property(getDataArray, setDataArray, delDataArray, "Property for dataArray")
    def export(self, outfile, level, name_='XSDataResultReadDataID24'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultReadDataID24'):
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
        self.export( oStreamString, 0, name_="XSDataResultReadDataID24" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultReadDataID24' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultReadDataID24 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultReadDataID24.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadDataID24()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultReadDataID24" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadDataID24()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultReadDataID24



# End of data representation classes.



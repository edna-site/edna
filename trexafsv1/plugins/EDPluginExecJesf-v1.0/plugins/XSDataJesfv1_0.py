#!/usr/bin/env python

#
# Generated Tue Jan 8 11:17::25 2013 by EDGenerateDS.
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
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataDouble
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



class XSDataInputJesf(XSDataInput):
    def __init__(self, configuration=None, data=None):
        XSDataInput.__init__(self, configuration)
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataArray":
            self._data = data
        else:
            strMessage = "ERROR! XSDataInputJesf constructor argument 'data' is not XSDataArray but %s" % self._data.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'data' attribute
    def getData(self): return self._data
    def setData(self, data):
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataArray":
            self._data = data
        else:
            strMessage = "ERROR! XSDataInputJesf.setData argument is not XSDataArray but %s" % data.__class__.__name__
            raise BaseException(strMessage)
    def delData(self): self._data = None
    data = property(getData, setData, delData, "Property for data")
    def export(self, outfile, level, name_='XSDataInputJesf'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputJesf'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._data is not None:
            self.data.export(outfile, level, name_='data')
        else:
            warnEmptyAttribute("data", "XSDataArray")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setData(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputJesf" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputJesf' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputJesf is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputJesf.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputJesf()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputJesf" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputJesf()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputJesf


class XSDataResultJesf(XSDataResult):
    def __init__(self, status=None, fort99=None, fort98=None, fort97=None, fort96=None, fort95=None, fort92=None, ewl=None, hwl=None, jump=None, slope=None, edge=None):
        XSDataResult.__init__(self, status)
        if edge is None:
            self._edge = None
        elif edge.__class__.__name__ == "XSDataDouble":
            self._edge = edge
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'edge' is not XSDataDouble but %s" % self._edge.__class__.__name__
            raise BaseException(strMessage)
        if slope is None:
            self._slope = None
        elif slope.__class__.__name__ == "XSDataDouble":
            self._slope = slope
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'slope' is not XSDataDouble but %s" % self._slope.__class__.__name__
            raise BaseException(strMessage)
        if jump is None:
            self._jump = None
        elif jump.__class__.__name__ == "XSDataDouble":
            self._jump = jump
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'jump' is not XSDataDouble but %s" % self._jump.__class__.__name__
            raise BaseException(strMessage)
        if hwl is None:
            self._hwl = None
        elif hwl.__class__.__name__ == "XSDataDouble":
            self._hwl = hwl
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'hwl' is not XSDataDouble but %s" % self._hwl.__class__.__name__
            raise BaseException(strMessage)
        if ewl is None:
            self._ewl = None
        elif ewl.__class__.__name__ == "XSDataDouble":
            self._ewl = ewl
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'ewl' is not XSDataDouble but %s" % self._ewl.__class__.__name__
            raise BaseException(strMessage)
        if fort92 is None:
            self._fort92 = None
        elif fort92.__class__.__name__ == "XSDataArray":
            self._fort92 = fort92
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort92' is not XSDataArray but %s" % self._fort92.__class__.__name__
            raise BaseException(strMessage)
        if fort95 is None:
            self._fort95 = None
        elif fort95.__class__.__name__ == "XSDataArray":
            self._fort95 = fort95
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort95' is not XSDataArray but %s" % self._fort95.__class__.__name__
            raise BaseException(strMessage)
        if fort96 is None:
            self._fort96 = None
        elif fort96.__class__.__name__ == "XSDataArray":
            self._fort96 = fort96
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort96' is not XSDataArray but %s" % self._fort96.__class__.__name__
            raise BaseException(strMessage)
        if fort97 is None:
            self._fort97 = None
        elif fort97.__class__.__name__ == "XSDataArray":
            self._fort97 = fort97
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort97' is not XSDataArray but %s" % self._fort97.__class__.__name__
            raise BaseException(strMessage)
        if fort98 is None:
            self._fort98 = None
        elif fort98.__class__.__name__ == "XSDataArray":
            self._fort98 = fort98
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort98' is not XSDataArray but %s" % self._fort98.__class__.__name__
            raise BaseException(strMessage)
        if fort99 is None:
            self._fort99 = None
        elif fort99.__class__.__name__ == "XSDataArray":
            self._fort99 = fort99
        else:
            strMessage = "ERROR! XSDataResultJesf constructor argument 'fort99' is not XSDataArray but %s" % self._fort99.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'edge' attribute
    def getEdge(self): return self._edge
    def setEdge(self, edge):
        if edge is None:
            self._edge = None
        elif edge.__class__.__name__ == "XSDataDouble":
            self._edge = edge
        else:
            strMessage = "ERROR! XSDataResultJesf.setEdge argument is not XSDataDouble but %s" % edge.__class__.__name__
            raise BaseException(strMessage)
    def delEdge(self): self._edge = None
    edge = property(getEdge, setEdge, delEdge, "Property for edge")
    # Methods and properties for the 'slope' attribute
    def getSlope(self): return self._slope
    def setSlope(self, slope):
        if slope is None:
            self._slope = None
        elif slope.__class__.__name__ == "XSDataDouble":
            self._slope = slope
        else:
            strMessage = "ERROR! XSDataResultJesf.setSlope argument is not XSDataDouble but %s" % slope.__class__.__name__
            raise BaseException(strMessage)
    def delSlope(self): self._slope = None
    slope = property(getSlope, setSlope, delSlope, "Property for slope")
    # Methods and properties for the 'jump' attribute
    def getJump(self): return self._jump
    def setJump(self, jump):
        if jump is None:
            self._jump = None
        elif jump.__class__.__name__ == "XSDataDouble":
            self._jump = jump
        else:
            strMessage = "ERROR! XSDataResultJesf.setJump argument is not XSDataDouble but %s" % jump.__class__.__name__
            raise BaseException(strMessage)
    def delJump(self): self._jump = None
    jump = property(getJump, setJump, delJump, "Property for jump")
    # Methods and properties for the 'hwl' attribute
    def getHwl(self): return self._hwl
    def setHwl(self, hwl):
        if hwl is None:
            self._hwl = None
        elif hwl.__class__.__name__ == "XSDataDouble":
            self._hwl = hwl
        else:
            strMessage = "ERROR! XSDataResultJesf.setHwl argument is not XSDataDouble but %s" % hwl.__class__.__name__
            raise BaseException(strMessage)
    def delHwl(self): self._hwl = None
    hwl = property(getHwl, setHwl, delHwl, "Property for hwl")
    # Methods and properties for the 'ewl' attribute
    def getEwl(self): return self._ewl
    def setEwl(self, ewl):
        if ewl is None:
            self._ewl = None
        elif ewl.__class__.__name__ == "XSDataDouble":
            self._ewl = ewl
        else:
            strMessage = "ERROR! XSDataResultJesf.setEwl argument is not XSDataDouble but %s" % ewl.__class__.__name__
            raise BaseException(strMessage)
    def delEwl(self): self._ewl = None
    ewl = property(getEwl, setEwl, delEwl, "Property for ewl")
    # Methods and properties for the 'fort92' attribute
    def getFort92(self): return self._fort92
    def setFort92(self, fort92):
        if fort92 is None:
            self._fort92 = None
        elif fort92.__class__.__name__ == "XSDataArray":
            self._fort92 = fort92
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort92 argument is not XSDataArray but %s" % fort92.__class__.__name__
            raise BaseException(strMessage)
    def delFort92(self): self._fort92 = None
    fort92 = property(getFort92, setFort92, delFort92, "Property for fort92")
    # Methods and properties for the 'fort95' attribute
    def getFort95(self): return self._fort95
    def setFort95(self, fort95):
        if fort95 is None:
            self._fort95 = None
        elif fort95.__class__.__name__ == "XSDataArray":
            self._fort95 = fort95
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort95 argument is not XSDataArray but %s" % fort95.__class__.__name__
            raise BaseException(strMessage)
    def delFort95(self): self._fort95 = None
    fort95 = property(getFort95, setFort95, delFort95, "Property for fort95")
    # Methods and properties for the 'fort96' attribute
    def getFort96(self): return self._fort96
    def setFort96(self, fort96):
        if fort96 is None:
            self._fort96 = None
        elif fort96.__class__.__name__ == "XSDataArray":
            self._fort96 = fort96
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort96 argument is not XSDataArray but %s" % fort96.__class__.__name__
            raise BaseException(strMessage)
    def delFort96(self): self._fort96 = None
    fort96 = property(getFort96, setFort96, delFort96, "Property for fort96")
    # Methods and properties for the 'fort97' attribute
    def getFort97(self): return self._fort97
    def setFort97(self, fort97):
        if fort97 is None:
            self._fort97 = None
        elif fort97.__class__.__name__ == "XSDataArray":
            self._fort97 = fort97
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort97 argument is not XSDataArray but %s" % fort97.__class__.__name__
            raise BaseException(strMessage)
    def delFort97(self): self._fort97 = None
    fort97 = property(getFort97, setFort97, delFort97, "Property for fort97")
    # Methods and properties for the 'fort98' attribute
    def getFort98(self): return self._fort98
    def setFort98(self, fort98):
        if fort98 is None:
            self._fort98 = None
        elif fort98.__class__.__name__ == "XSDataArray":
            self._fort98 = fort98
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort98 argument is not XSDataArray but %s" % fort98.__class__.__name__
            raise BaseException(strMessage)
    def delFort98(self): self._fort98 = None
    fort98 = property(getFort98, setFort98, delFort98, "Property for fort98")
    # Methods and properties for the 'fort99' attribute
    def getFort99(self): return self._fort99
    def setFort99(self, fort99):
        if fort99 is None:
            self._fort99 = None
        elif fort99.__class__.__name__ == "XSDataArray":
            self._fort99 = fort99
        else:
            strMessage = "ERROR! XSDataResultJesf.setFort99 argument is not XSDataArray but %s" % fort99.__class__.__name__
            raise BaseException(strMessage)
    def delFort99(self): self._fort99 = None
    fort99 = property(getFort99, setFort99, delFort99, "Property for fort99")
    def export(self, outfile, level, name_='XSDataResultJesf'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultJesf'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._edge is not None:
            self.edge.export(outfile, level, name_='edge')
        if self._slope is not None:
            self.slope.export(outfile, level, name_='slope')
        if self._jump is not None:
            self.jump.export(outfile, level, name_='jump')
        if self._hwl is not None:
            self.hwl.export(outfile, level, name_='hwl')
        if self._ewl is not None:
            self.ewl.export(outfile, level, name_='ewl')
        if self._fort92 is not None:
            self.fort92.export(outfile, level, name_='fort92')
        if self._fort95 is not None:
            self.fort95.export(outfile, level, name_='fort95')
        if self._fort96 is not None:
            self.fort96.export(outfile, level, name_='fort96')
        if self._fort97 is not None:
            self.fort97.export(outfile, level, name_='fort97')
        if self._fort98 is not None:
            self.fort98.export(outfile, level, name_='fort98')
        if self._fort99 is not None:
            self.fort99.export(outfile, level, name_='fort99')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'edge':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setEdge(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slope':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSlope(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jump':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setJump(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hwl':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setHwl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ewl':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setEwl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort92':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort92(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort95':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort95(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort96':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort96(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort97':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort97(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort98':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort98(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fort99':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setFort99(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultJesf" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultJesf' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultJesf is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultJesf.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultJesf()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultJesf" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultJesf()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultJesf



# End of data representation classes.



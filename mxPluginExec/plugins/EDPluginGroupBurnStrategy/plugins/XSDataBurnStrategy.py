#!/usr/bin/env python

#
# Generated Mon Nov 5 02:24::56 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
}

try:
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
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
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString




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



class XSDataInputXdsBurnStrategy(XSDataInput):
    def __init__(self, configuration=None, unit_cell_gamma=None, unit_cell_beta=None, unit_cell_alpha=None, unit_cell_c=None, unit_cell_b=None, unit_cell_a=None, space_group=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if space_group is None:
            self._space_group = None
        elif space_group.__class__.__name__ == "XSDataInteger":
            self._space_group = space_group
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'space_group' is not XSDataInteger but %s" % self._space_group.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_a is None:
            self._unit_cell_a = None
        elif unit_cell_a.__class__.__name__ == "XSDataDouble":
            self._unit_cell_a = unit_cell_a
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_a' is not XSDataDouble but %s" % self._unit_cell_a.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_b is None:
            self._unit_cell_b = None
        elif unit_cell_b.__class__.__name__ == "XSDataDouble":
            self._unit_cell_b = unit_cell_b
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_b' is not XSDataDouble but %s" % self._unit_cell_b.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_c is None:
            self._unit_cell_c = None
        elif unit_cell_c.__class__.__name__ == "XSDataDouble":
            self._unit_cell_c = unit_cell_c
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_c' is not XSDataDouble but %s" % self._unit_cell_c.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_alpha is None:
            self._unit_cell_alpha = None
        elif unit_cell_alpha.__class__.__name__ == "XSDataDouble":
            self._unit_cell_alpha = unit_cell_alpha
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_alpha' is not XSDataDouble but %s" % self._unit_cell_alpha.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_beta is None:
            self._unit_cell_beta = None
        elif unit_cell_beta.__class__.__name__ == "XSDataDouble":
            self._unit_cell_beta = unit_cell_beta
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_beta' is not XSDataDouble but %s" % self._unit_cell_beta.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_gamma is None:
            self._unit_cell_gamma = None
        elif unit_cell_gamma.__class__.__name__ == "XSDataDouble":
            self._unit_cell_gamma = unit_cell_gamma
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy constructor argument 'unit_cell_gamma' is not XSDataDouble but %s" % self._unit_cell_gamma.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'space_group' attribute
    def getSpace_group(self): return self._space_group
    def setSpace_group(self, space_group):
        if space_group is None:
            self._space_group = None
        elif space_group.__class__.__name__ == "XSDataInteger":
            self._space_group = space_group
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setSpace_group argument is not XSDataInteger but %s" % space_group.__class__.__name__
            raise BaseException(strMessage)
    def delSpace_group(self): self._space_group = None
    space_group = property(getSpace_group, setSpace_group, delSpace_group, "Property for space_group")
    # Methods and properties for the 'unit_cell_a' attribute
    def getUnit_cell_a(self): return self._unit_cell_a
    def setUnit_cell_a(self, unit_cell_a):
        if unit_cell_a is None:
            self._unit_cell_a = None
        elif unit_cell_a.__class__.__name__ == "XSDataDouble":
            self._unit_cell_a = unit_cell_a
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_a argument is not XSDataDouble but %s" % unit_cell_a.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_a(self): self._unit_cell_a = None
    unit_cell_a = property(getUnit_cell_a, setUnit_cell_a, delUnit_cell_a, "Property for unit_cell_a")
    # Methods and properties for the 'unit_cell_b' attribute
    def getUnit_cell_b(self): return self._unit_cell_b
    def setUnit_cell_b(self, unit_cell_b):
        if unit_cell_b is None:
            self._unit_cell_b = None
        elif unit_cell_b.__class__.__name__ == "XSDataDouble":
            self._unit_cell_b = unit_cell_b
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_b argument is not XSDataDouble but %s" % unit_cell_b.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_b(self): self._unit_cell_b = None
    unit_cell_b = property(getUnit_cell_b, setUnit_cell_b, delUnit_cell_b, "Property for unit_cell_b")
    # Methods and properties for the 'unit_cell_c' attribute
    def getUnit_cell_c(self): return self._unit_cell_c
    def setUnit_cell_c(self, unit_cell_c):
        if unit_cell_c is None:
            self._unit_cell_c = None
        elif unit_cell_c.__class__.__name__ == "XSDataDouble":
            self._unit_cell_c = unit_cell_c
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_c argument is not XSDataDouble but %s" % unit_cell_c.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_c(self): self._unit_cell_c = None
    unit_cell_c = property(getUnit_cell_c, setUnit_cell_c, delUnit_cell_c, "Property for unit_cell_c")
    # Methods and properties for the 'unit_cell_alpha' attribute
    def getUnit_cell_alpha(self): return self._unit_cell_alpha
    def setUnit_cell_alpha(self, unit_cell_alpha):
        if unit_cell_alpha is None:
            self._unit_cell_alpha = None
        elif unit_cell_alpha.__class__.__name__ == "XSDataDouble":
            self._unit_cell_alpha = unit_cell_alpha
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_alpha argument is not XSDataDouble but %s" % unit_cell_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_alpha(self): self._unit_cell_alpha = None
    unit_cell_alpha = property(getUnit_cell_alpha, setUnit_cell_alpha, delUnit_cell_alpha, "Property for unit_cell_alpha")
    # Methods and properties for the 'unit_cell_beta' attribute
    def getUnit_cell_beta(self): return self._unit_cell_beta
    def setUnit_cell_beta(self, unit_cell_beta):
        if unit_cell_beta is None:
            self._unit_cell_beta = None
        elif unit_cell_beta.__class__.__name__ == "XSDataDouble":
            self._unit_cell_beta = unit_cell_beta
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_beta argument is not XSDataDouble but %s" % unit_cell_beta.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_beta(self): self._unit_cell_beta = None
    unit_cell_beta = property(getUnit_cell_beta, setUnit_cell_beta, delUnit_cell_beta, "Property for unit_cell_beta")
    # Methods and properties for the 'unit_cell_gamma' attribute
    def getUnit_cell_gamma(self): return self._unit_cell_gamma
    def setUnit_cell_gamma(self, unit_cell_gamma):
        if unit_cell_gamma is None:
            self._unit_cell_gamma = None
        elif unit_cell_gamma.__class__.__name__ == "XSDataDouble":
            self._unit_cell_gamma = unit_cell_gamma
        else:
            strMessage = "ERROR! XSDataInputXdsBurnStrategy.setUnit_cell_gamma argument is not XSDataDouble but %s" % unit_cell_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_gamma(self): self._unit_cell_gamma = None
    unit_cell_gamma = property(getUnit_cell_gamma, setUnit_cell_gamma, delUnit_cell_gamma, "Property for unit_cell_gamma")
    def export(self, outfile, level, name_='XSDataInputXdsBurnStrategy'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXdsBurnStrategy'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._space_group is not None:
            self.space_group.export(outfile, level, name_='space_group')
        else:
            warnEmptyAttribute("space_group", "XSDataInteger")
        if self._unit_cell_a is not None:
            self.unit_cell_a.export(outfile, level, name_='unit_cell_a')
        else:
            warnEmptyAttribute("unit_cell_a", "XSDataDouble")
        if self._unit_cell_b is not None:
            self.unit_cell_b.export(outfile, level, name_='unit_cell_b')
        else:
            warnEmptyAttribute("unit_cell_b", "XSDataDouble")
        if self._unit_cell_c is not None:
            self.unit_cell_c.export(outfile, level, name_='unit_cell_c')
        else:
            warnEmptyAttribute("unit_cell_c", "XSDataDouble")
        if self._unit_cell_alpha is not None:
            self.unit_cell_alpha.export(outfile, level, name_='unit_cell_alpha')
        else:
            warnEmptyAttribute("unit_cell_alpha", "XSDataDouble")
        if self._unit_cell_beta is not None:
            self.unit_cell_beta.export(outfile, level, name_='unit_cell_beta')
        else:
            warnEmptyAttribute("unit_cell_beta", "XSDataDouble")
        if self._unit_cell_gamma is not None:
            self.unit_cell_gamma.export(outfile, level, name_='unit_cell_gamma')
        else:
            warnEmptyAttribute("unit_cell_gamma", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'space_group':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpace_group(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_a':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_b':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_c':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_alpha':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_beta':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_gamma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnit_cell_gamma(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXdsBurnStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXdsBurnStrategy' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXdsBurnStrategy is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXdsBurnStrategy.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXdsBurnStrategy()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXdsBurnStrategy" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXdsBurnStrategy()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXdsBurnStrategy


class XSDataOutputXdsBurnStrategy(XSDataResult):
    def __init__(self, status=None, xds_hkl=None):
        XSDataResult.__init__(self, status)
        if xds_hkl is None:
            self._xds_hkl = None
        elif xds_hkl.__class__.__name__ == "XSDataString":
            self._xds_hkl = xds_hkl
        else:
            strMessage = "ERROR! XSDataOutputXdsBurnStrategy constructor argument 'xds_hkl' is not XSDataString but %s" % self._xds_hkl.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'xds_hkl' attribute
    def getXds_hkl(self): return self._xds_hkl
    def setXds_hkl(self, xds_hkl):
        if xds_hkl is None:
            self._xds_hkl = None
        elif xds_hkl.__class__.__name__ == "XSDataString":
            self._xds_hkl = xds_hkl
        else:
            strMessage = "ERROR! XSDataOutputXdsBurnStrategy.setXds_hkl argument is not XSDataString but %s" % xds_hkl.__class__.__name__
            raise BaseException(strMessage)
    def delXds_hkl(self): self._xds_hkl = None
    xds_hkl = property(getXds_hkl, setXds_hkl, delXds_hkl, "Property for xds_hkl")
    def export(self, outfile, level, name_='XSDataOutputXdsBurnStrategy'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataOutputXdsBurnStrategy'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._xds_hkl is not None:
            self.xds_hkl.export(outfile, level, name_='xds_hkl')
        else:
            warnEmptyAttribute("xds_hkl", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_hkl':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setXds_hkl(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataOutputXdsBurnStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataOutputXdsBurnStrategy' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataOutputXdsBurnStrategy is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataOutputXdsBurnStrategy.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataOutputXdsBurnStrategy()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataOutputXdsBurnStrategy" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataOutputXdsBurnStrategy()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataOutputXdsBurnStrategy



# End of data representation classes.



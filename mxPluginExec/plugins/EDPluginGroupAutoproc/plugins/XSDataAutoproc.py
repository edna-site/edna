#!/usr/bin/env python

#
# Generated Fri Jun 1 08:32::05 2012 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataFloat
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataVectorDouble
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble




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


class XSData2DCoordinates(object):
    def __init__(self, y=None, x=None):
    
    
        checkType("XSData2DCoordinates", "Constructor of XSData2DCoordinates", x, "XSDataFloat")
        self._x = x
        checkType("XSData2DCoordinates", "Constructor of XSData2DCoordinates", y, "XSDataFloat")
        self._y = y
    def getX(self): return self._x
    def setX(self, x):
        checkType("XSData2DCoordinates", "setX", x, "XSDataFloat")
        self._x = x
    def delX(self): self._x = None
    # Properties
    x = property(getX, setX, delX, "Property for x")
    def getY(self): return self._y
    def setY(self, y):
        checkType("XSData2DCoordinates", "setY", y, "XSDataFloat")
        self._y = y
    def delY(self): self._y = None
    # Properties
    y = property(getY, setY, delY, "Property for y")
    def export(self, outfile, level, name_='XSData2DCoordinates'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSData2DCoordinates'):
        pass
        if self._x is not None:
            self.x.export(outfile, level, name_='x')
        else:
            warnEmptyAttribute("x", "XSDataFloat")
        if self._y is not None:
            self.y.export(outfile, level, name_='y')
        else:
            warnEmptyAttribute("y", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setY(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSData2DCoordinates" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSData2DCoordinates' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSData2DCoordinates is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSData2DCoordinates.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSData2DCoordinates()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSData2DCoordinates" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSData2DCoordinates()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSData2DCoordinates

class XSDataXdsCompletenessEntry(object):
    def __init__(self, half_dataset_correlation=None, outer_isig=None, outer_rfactor=None, outer_complete=None, outer_possible=None, outer_unique=None, outer_observed=None, outer_res=None):
    
    
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_res, "XSDataFloat")
        self._outer_res = outer_res
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_observed, "XSDataFloat")
        self._outer_observed = outer_observed
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_unique, "XSDataFloat")
        self._outer_unique = outer_unique
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_possible, "XSDataFloat")
        self._outer_possible = outer_possible
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_complete, "XSDataFloat")
        self._outer_complete = outer_complete
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_rfactor, "XSDataFloat")
        self._outer_rfactor = outer_rfactor
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_isig, "XSDataFloat")
        self._outer_isig = outer_isig
        checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", half_dataset_correlation, "XSDataFloat")
        self._half_dataset_correlation = half_dataset_correlation
    def getOuter_res(self): return self._outer_res
    def setOuter_res(self, outer_res):
        checkType("XSDataXdsCompletenessEntry", "setOuter_res", outer_res, "XSDataFloat")
        self._outer_res = outer_res
    def delOuter_res(self): self._outer_res = None
    # Properties
    outer_res = property(getOuter_res, setOuter_res, delOuter_res, "Property for outer_res")
    def getOuter_observed(self): return self._outer_observed
    def setOuter_observed(self, outer_observed):
        checkType("XSDataXdsCompletenessEntry", "setOuter_observed", outer_observed, "XSDataFloat")
        self._outer_observed = outer_observed
    def delOuter_observed(self): self._outer_observed = None
    # Properties
    outer_observed = property(getOuter_observed, setOuter_observed, delOuter_observed, "Property for outer_observed")
    def getOuter_unique(self): return self._outer_unique
    def setOuter_unique(self, outer_unique):
        checkType("XSDataXdsCompletenessEntry", "setOuter_unique", outer_unique, "XSDataFloat")
        self._outer_unique = outer_unique
    def delOuter_unique(self): self._outer_unique = None
    # Properties
    outer_unique = property(getOuter_unique, setOuter_unique, delOuter_unique, "Property for outer_unique")
    def getOuter_possible(self): return self._outer_possible
    def setOuter_possible(self, outer_possible):
        checkType("XSDataXdsCompletenessEntry", "setOuter_possible", outer_possible, "XSDataFloat")
        self._outer_possible = outer_possible
    def delOuter_possible(self): self._outer_possible = None
    # Properties
    outer_possible = property(getOuter_possible, setOuter_possible, delOuter_possible, "Property for outer_possible")
    def getOuter_complete(self): return self._outer_complete
    def setOuter_complete(self, outer_complete):
        checkType("XSDataXdsCompletenessEntry", "setOuter_complete", outer_complete, "XSDataFloat")
        self._outer_complete = outer_complete
    def delOuter_complete(self): self._outer_complete = None
    # Properties
    outer_complete = property(getOuter_complete, setOuter_complete, delOuter_complete, "Property for outer_complete")
    def getOuter_rfactor(self): return self._outer_rfactor
    def setOuter_rfactor(self, outer_rfactor):
        checkType("XSDataXdsCompletenessEntry", "setOuter_rfactor", outer_rfactor, "XSDataFloat")
        self._outer_rfactor = outer_rfactor
    def delOuter_rfactor(self): self._outer_rfactor = None
    # Properties
    outer_rfactor = property(getOuter_rfactor, setOuter_rfactor, delOuter_rfactor, "Property for outer_rfactor")
    def getOuter_isig(self): return self._outer_isig
    def setOuter_isig(self, outer_isig):
        checkType("XSDataXdsCompletenessEntry", "setOuter_isig", outer_isig, "XSDataFloat")
        self._outer_isig = outer_isig
    def delOuter_isig(self): self._outer_isig = None
    # Properties
    outer_isig = property(getOuter_isig, setOuter_isig, delOuter_isig, "Property for outer_isig")
    def getHalf_dataset_correlation(self): return self._half_dataset_correlation
    def setHalf_dataset_correlation(self, half_dataset_correlation):
        checkType("XSDataXdsCompletenessEntry", "setHalf_dataset_correlation", half_dataset_correlation, "XSDataFloat")
        self._half_dataset_correlation = half_dataset_correlation
    def delHalf_dataset_correlation(self): self._half_dataset_correlation = None
    # Properties
    half_dataset_correlation = property(getHalf_dataset_correlation, setHalf_dataset_correlation, delHalf_dataset_correlation, "Property for half_dataset_correlation")
    def export(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
        pass
        if self._outer_res is not None:
            self.outer_res.export(outfile, level, name_='outer_res')
        else:
            warnEmptyAttribute("outer_res", "XSDataFloat")
        if self._outer_observed is not None:
            self.outer_observed.export(outfile, level, name_='outer_observed')
        else:
            warnEmptyAttribute("outer_observed", "XSDataFloat")
        if self._outer_unique is not None:
            self.outer_unique.export(outfile, level, name_='outer_unique')
        else:
            warnEmptyAttribute("outer_unique", "XSDataFloat")
        if self._outer_possible is not None:
            self.outer_possible.export(outfile, level, name_='outer_possible')
        else:
            warnEmptyAttribute("outer_possible", "XSDataFloat")
        if self._outer_complete is not None:
            self.outer_complete.export(outfile, level, name_='outer_complete')
        else:
            warnEmptyAttribute("outer_complete", "XSDataFloat")
        if self._outer_rfactor is not None:
            self.outer_rfactor.export(outfile, level, name_='outer_rfactor')
        else:
            warnEmptyAttribute("outer_rfactor", "XSDataFloat")
        if self._outer_isig is not None:
            self.outer_isig.export(outfile, level, name_='outer_isig')
        else:
            warnEmptyAttribute("outer_isig", "XSDataFloat")
        if self._half_dataset_correlation is not None:
            self.half_dataset_correlation.export(outfile, level, name_='half_dataset_correlation')
        else:
            warnEmptyAttribute("half_dataset_correlation", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_observed':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_observed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_unique':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_unique(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_possible':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_possible(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_complete':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_complete(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_rfactor':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_rfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outer_isig':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setOuter_isig(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'half_dataset_correlation':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setHalf_dataset_correlation(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsCompletenessEntry' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsCompletenessEntry is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsCompletenessEntry.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsCompletenessEntry()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsCompletenessEntry()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsCompletenessEntry

class XSDataXscaleCompletenessEntry(XSDataXdsCompletenessEntry):
    def __init__(self, half_dataset_correlation=None, outer_isig=None, outer_rfactor=None, outer_complete=None, outer_possible=None, outer_unique=None, outer_observed=None, outer_res=None, multiplicity=None):
        XSDataXdsCompletenessEntry.__init__(self, half_dataset_correlation, outer_isig, outer_rfactor, outer_complete, outer_possible, outer_unique, outer_observed, outer_res)
    
    
        checkType("XSDataXscaleCompletenessEntry", "Constructor of XSDataXscaleCompletenessEntry", multiplicity, "XSDataFloat")
        self._multiplicity = multiplicity
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        checkType("XSDataXscaleCompletenessEntry", "setMultiplicity", multiplicity, "XSDataFloat")
        self._multiplicity = multiplicity
    def delMultiplicity(self): self._multiplicity = None
    # Properties
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    def export(self, outfile, level, name_='XSDataXscaleCompletenessEntry'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleCompletenessEntry'):
        XSDataXdsCompletenessEntry.exportChildren(self, outfile, level, name_)
        if self._multiplicity is not None:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        else:
            warnEmptyAttribute("multiplicity", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        XSDataXdsCompletenessEntry.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleCompletenessEntry" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleCompletenessEntry' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleCompletenessEntry is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleCompletenessEntry.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleCompletenessEntry()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleCompletenessEntry" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleCompletenessEntry()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleCompletenessEntry

class XSDataAutoprocMasterInput(XSDataInput):
    def __init__(self, configuration=None, low_resolution_limit=None, detector_max_res=None, data_collection_id=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, input_file=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", input_file, "XSDataFile")
        self._input_file = input_file
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", res_override, "XSDataFloat")
        self._res_override = res_override
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", completeness_cutoff, "XSDataFloat")
        self._completeness_cutoff = completeness_cutoff
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", isig_cutoff, "XSDataFloat")
        self._isig_cutoff = isig_cutoff
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", r_value_cutoff, "XSDataFloat")
        self._r_value_cutoff = r_value_cutoff
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", cc_half_cutoff, "XSDataFloat")
        self._cc_half_cutoff = cc_half_cutoff
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", data_collection_id, "XSDataInteger")
        self._data_collection_id = data_collection_id
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", detector_max_res, "XSDataFloat")
        self._detector_max_res = detector_max_res
        checkType("XSDataAutoprocMasterInput", "Constructor of XSDataAutoprocMasterInput", low_resolution_limit, "XSDataFloat")
        self._low_resolution_limit = low_resolution_limit
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        checkType("XSDataAutoprocMasterInput", "setInput_file", input_file, "XSDataFile")
        self._input_file = input_file
    def delInput_file(self): self._input_file = None
    # Properties
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        checkType("XSDataAutoprocMasterInput", "setRes_override", res_override, "XSDataFloat")
        self._res_override = res_override
    def delRes_override(self): self._res_override = None
    # Properties
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        checkType("XSDataAutoprocMasterInput", "setCompleteness_cutoff", completeness_cutoff, "XSDataFloat")
        self._completeness_cutoff = completeness_cutoff
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    # Properties
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        checkType("XSDataAutoprocMasterInput", "setIsig_cutoff", isig_cutoff, "XSDataFloat")
        self._isig_cutoff = isig_cutoff
    def delIsig_cutoff(self): self._isig_cutoff = None
    # Properties
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        checkType("XSDataAutoprocMasterInput", "setR_value_cutoff", r_value_cutoff, "XSDataFloat")
        self._r_value_cutoff = r_value_cutoff
    def delR_value_cutoff(self): self._r_value_cutoff = None
    # Properties
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        checkType("XSDataAutoprocMasterInput", "setCc_half_cutoff", cc_half_cutoff, "XSDataFloat")
        self._cc_half_cutoff = cc_half_cutoff
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
    # Properties
    cc_half_cutoff = property(getCc_half_cutoff, setCc_half_cutoff, delCc_half_cutoff, "Property for cc_half_cutoff")
    def getData_collection_id(self): return self._data_collection_id
    def setData_collection_id(self, data_collection_id):
        checkType("XSDataAutoprocMasterInput", "setData_collection_id", data_collection_id, "XSDataInteger")
        self._data_collection_id = data_collection_id
    def delData_collection_id(self): self._data_collection_id = None
    # Properties
    data_collection_id = property(getData_collection_id, setData_collection_id, delData_collection_id, "Property for data_collection_id")
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        checkType("XSDataAutoprocMasterInput", "setDetector_max_res", detector_max_res, "XSDataFloat")
        self._detector_max_res = detector_max_res
    def delDetector_max_res(self): self._detector_max_res = None
    # Properties
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    def getLow_resolution_limit(self): return self._low_resolution_limit
    def setLow_resolution_limit(self, low_resolution_limit):
        checkType("XSDataAutoprocMasterInput", "setLow_resolution_limit", low_resolution_limit, "XSDataFloat")
        self._low_resolution_limit = low_resolution_limit
    def delLow_resolution_limit(self): self._low_resolution_limit = None
    # Properties
    low_resolution_limit = property(getLow_resolution_limit, setLow_resolution_limit, delLow_resolution_limit, "Property for low_resolution_limit")
    def export(self, outfile, level, name_='XSDataAutoprocMasterInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoprocMasterInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataFile")
        if self._res_override is not None:
            self.res_override.export(outfile, level, name_='res_override')
        if self._completeness_cutoff is not None:
            self.completeness_cutoff.export(outfile, level, name_='completeness_cutoff')
        if self._isig_cutoff is not None:
            self.isig_cutoff.export(outfile, level, name_='isig_cutoff')
        if self._r_value_cutoff is not None:
            self.r_value_cutoff.export(outfile, level, name_='r_value_cutoff')
        if self._cc_half_cutoff is not None:
            self.cc_half_cutoff.export(outfile, level, name_='cc_half_cutoff')
        if self._data_collection_id is not None:
            self.data_collection_id.export(outfile, level, name_='data_collection_id')
        if self._detector_max_res is not None:
            self.detector_max_res.export(outfile, level, name_='detector_max_res')
        if self._low_resolution_limit is not None:
            self.low_resolution_limit.export(outfile, level, name_='low_resolution_limit')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res_override':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes_override(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCompleteness_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isig_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setIsig_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'r_value_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setR_value_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cc_half_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCc_half_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data_collection_id':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setData_collection_id(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_max_res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setDetector_max_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'low_resolution_limit':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setLow_resolution_limit(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoprocMasterInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoprocMasterInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoprocMasterInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoprocMasterInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocMasterInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoprocMasterInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocMasterInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoprocMasterInput

class XSDataMatthewsCoeffIn(XSDataInput):
    def __init__(self, configuration=None, symm=None, gamma=None, beta=None, alpha=None, c=None, b=None, a=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", a, "XSDataDouble")
        self._a = a
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", b, "XSDataDouble")
        self._b = b
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", c, "XSDataDouble")
        self._c = c
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", alpha, "XSDataDouble")
        self._alpha = alpha
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", beta, "XSDataDouble")
        self._beta = beta
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", gamma, "XSDataDouble")
        self._gamma = gamma
        checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", symm, "XSDataString")
        self._symm = symm
    def getA(self): return self._a
    def setA(self, a):
        checkType("XSDataMatthewsCoeffIn", "setA", a, "XSDataDouble")
        self._a = a
    def delA(self): self._a = None
    # Properties
    a = property(getA, setA, delA, "Property for a")
    def getB(self): return self._b
    def setB(self, b):
        checkType("XSDataMatthewsCoeffIn", "setB", b, "XSDataDouble")
        self._b = b
    def delB(self): self._b = None
    # Properties
    b = property(getB, setB, delB, "Property for b")
    def getC(self): return self._c
    def setC(self, c):
        checkType("XSDataMatthewsCoeffIn", "setC", c, "XSDataDouble")
        self._c = c
    def delC(self): self._c = None
    # Properties
    c = property(getC, setC, delC, "Property for c")
    def getAlpha(self): return self._alpha
    def setAlpha(self, alpha):
        checkType("XSDataMatthewsCoeffIn", "setAlpha", alpha, "XSDataDouble")
        self._alpha = alpha
    def delAlpha(self): self._alpha = None
    # Properties
    alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
    def getBeta(self): return self._beta
    def setBeta(self, beta):
        checkType("XSDataMatthewsCoeffIn", "setBeta", beta, "XSDataDouble")
        self._beta = beta
    def delBeta(self): self._beta = None
    # Properties
    beta = property(getBeta, setBeta, delBeta, "Property for beta")
    def getGamma(self): return self._gamma
    def setGamma(self, gamma):
        checkType("XSDataMatthewsCoeffIn", "setGamma", gamma, "XSDataDouble")
        self._gamma = gamma
    def delGamma(self): self._gamma = None
    # Properties
    gamma = property(getGamma, setGamma, delGamma, "Property for gamma")
    def getSymm(self): return self._symm
    def setSymm(self, symm):
        checkType("XSDataMatthewsCoeffIn", "setSymm", symm, "XSDataString")
        self._symm = symm
    def delSymm(self): self._symm = None
    # Properties
    symm = property(getSymm, setSymm, delSymm, "Property for symm")
    def export(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
        XSDataInput.exportChildren(self, outfile, level, name_)
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
        else:
            warnEmptyAttribute("c", "XSDataDouble")
        if self._alpha is not None:
            self.alpha.export(outfile, level, name_='alpha')
        else:
            warnEmptyAttribute("alpha", "XSDataDouble")
        if self._beta is not None:
            self.beta.export(outfile, level, name_='beta')
        else:
            warnEmptyAttribute("beta", "XSDataDouble")
        if self._gamma is not None:
            self.gamma.export(outfile, level, name_='gamma')
        else:
            warnEmptyAttribute("gamma", "XSDataDouble")
        if self._symm is not None:
            self.symm.export(outfile, level, name_='symm')
        else:
            warnEmptyAttribute("symm", "XSDataString")
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
            nodeName_ == 'alpha':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAlpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beta':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gamma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setGamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symm':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymm(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMatthewsCoeffIn' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMatthewsCoeffIn is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMatthewsCoeffIn.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatthewsCoeffIn()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatthewsCoeffIn()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffIn

class XSDataMatthewsCoeffOut(XSDataResult):
    def __init__(self, status=None, best_sol=None, best_p=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_p, "XSDataDouble")
        self._best_p = best_p
        checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_sol, "XSDataString")
        self._best_sol = best_sol
    def getBest_p(self): return self._best_p
    def setBest_p(self, best_p):
        checkType("XSDataMatthewsCoeffOut", "setBest_p", best_p, "XSDataDouble")
        self._best_p = best_p
    def delBest_p(self): self._best_p = None
    # Properties
    best_p = property(getBest_p, setBest_p, delBest_p, "Property for best_p")
    def getBest_sol(self): return self._best_sol
    def setBest_sol(self, best_sol):
        checkType("XSDataMatthewsCoeffOut", "setBest_sol", best_sol, "XSDataString")
        self._best_sol = best_sol
    def delBest_sol(self): self._best_sol = None
    # Properties
    best_sol = property(getBest_sol, setBest_sol, delBest_sol, "Property for best_sol")
    def export(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._best_p is not None:
            self.best_p.export(outfile, level, name_='best_p')
        else:
            warnEmptyAttribute("best_p", "XSDataDouble")
        if self._best_sol is not None:
            self.best_sol.export(outfile, level, name_='best_sol')
        else:
            warnEmptyAttribute("best_sol", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'best_p':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBest_p(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'best_sol':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBest_sol(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMatthewsCoeffOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMatthewsCoeffOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMatthewsCoeffOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatthewsCoeffOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatthewsCoeffOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffOut

class XSDataMinimalXdsIn(XSDataInput):
    def __init__(self, configuration=None, resolution_range=None, friedels_law=None, maxjobs=None, maxproc=None, job=None, input_file=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", input_file, "XSDataString")
        self._input_file = input_file
        checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", job, "XSDataString")
        self._job = job
        checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", maxproc, "XSDataInteger")
        self._maxproc = maxproc
        checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", maxjobs, "XSDataInteger")
        self._maxjobs = maxjobs
        checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", friedels_law, "XSDataBoolean")
        self._friedels_law = friedels_law
        if resolution_range is None:
            self._resolution_range = []
        else:
            checkType("XSDataMinimalXdsIn", "Constructor of XSDataMinimalXdsIn", resolution_range, "list")
            self._resolution_range = resolution_range
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        checkType("XSDataMinimalXdsIn", "setInput_file", input_file, "XSDataString")
        self._input_file = input_file
    def delInput_file(self): self._input_file = None
    # Properties
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    def getJob(self): return self._job
    def setJob(self, job):
        checkType("XSDataMinimalXdsIn", "setJob", job, "XSDataString")
        self._job = job
    def delJob(self): self._job = None
    # Properties
    job = property(getJob, setJob, delJob, "Property for job")
    def getMaxproc(self): return self._maxproc
    def setMaxproc(self, maxproc):
        checkType("XSDataMinimalXdsIn", "setMaxproc", maxproc, "XSDataInteger")
        self._maxproc = maxproc
    def delMaxproc(self): self._maxproc = None
    # Properties
    maxproc = property(getMaxproc, setMaxproc, delMaxproc, "Property for maxproc")
    def getMaxjobs(self): return self._maxjobs
    def setMaxjobs(self, maxjobs):
        checkType("XSDataMinimalXdsIn", "setMaxjobs", maxjobs, "XSDataInteger")
        self._maxjobs = maxjobs
    def delMaxjobs(self): self._maxjobs = None
    # Properties
    maxjobs = property(getMaxjobs, setMaxjobs, delMaxjobs, "Property for maxjobs")
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        checkType("XSDataMinimalXdsIn", "setFriedels_law", friedels_law, "XSDataBoolean")
        self._friedels_law = friedels_law
    def delFriedels_law(self): self._friedels_law = None
    # Properties
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    def getResolution_range(self): return self._resolution_range
    def setResolution_range(self, resolution_range):
        checkType("XSDataMinimalXdsIn", "setResolution_range", resolution_range, "list")
        self._resolution_range = resolution_range
    def delResolution_range(self): self._resolution_range = None
    # Properties
    resolution_range = property(getResolution_range, setResolution_range, delResolution_range, "Property for resolution_range")
    def addResolution_range(self, value):
        checkType("XSDataMinimalXdsIn", "setResolution_range", value, "XSDataFloat")
        self._resolution_range.append(value)
    def insertResolution_range(self, index, value):
        checkType("XSDataMinimalXdsIn", "setResolution_range", value, "XSDataFloat")
        self._resolution_range[index] = value
    def export(self, outfile, level, name_='XSDataMinimalXdsIn'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMinimalXdsIn'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._job is not None:
            self.job.export(outfile, level, name_='job')
        if self._maxproc is not None:
            self.maxproc.export(outfile, level, name_='maxproc')
        if self._maxjobs is not None:
            self.maxjobs.export(outfile, level, name_='maxjobs')
        if self._friedels_law is not None:
            self.friedels_law.export(outfile, level, name_='friedels_law')
        for resolution_range_ in self.getResolution_range():
            resolution_range_.export(outfile, level, name_='resolution_range')
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
            nodeName_ == 'job':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setJob(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxproc':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMaxproc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxjobs':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMaxjobs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'friedels_law':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setFriedels_law(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution_range':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.resolution_range.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMinimalXdsIn" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMinimalXdsIn' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMinimalXdsIn is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMinimalXdsIn.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsIn()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMinimalXdsIn" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsIn()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMinimalXdsIn

class XSDataMinimalXdsOut(XSDataResult):
    def __init__(self, status=None, succeeded=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataMinimalXdsOut", "Constructor of XSDataMinimalXdsOut", succeeded, "XSDataBoolean")
        self._succeeded = succeeded
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        checkType("XSDataMinimalXdsOut", "setSucceeded", succeeded, "XSDataBoolean")
        self._succeeded = succeeded
    def delSucceeded(self): self._succeeded = None
    # Properties
    succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
    def export(self, outfile, level, name_='XSDataMinimalXdsOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMinimalXdsOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._succeeded is not None:
            self.succeeded.export(outfile, level, name_='succeeded')
        else:
            warnEmptyAttribute("succeeded", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'succeeded':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setSucceeded(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMinimalXdsOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMinimalXdsOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMinimalXdsOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMinimalXdsOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMinimalXdsOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMinimalXdsOut

class XSDataRBinsIn(XSDataInput):
    def __init__(self, configuration=None, high=None, low=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", low, "XSDataDouble")
        self._low = low
        checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", high, "XSDataDouble")
        self._high = high
    def getLow(self): return self._low
    def setLow(self, low):
        checkType("XSDataRBinsIn", "setLow", low, "XSDataDouble")
        self._low = low
    def delLow(self): self._low = None
    # Properties
    low = property(getLow, setLow, delLow, "Property for low")
    def getHigh(self): return self._high
    def setHigh(self, high):
        checkType("XSDataRBinsIn", "setHigh", high, "XSDataDouble")
        self._high = high
    def delHigh(self): self._high = None
    # Properties
    high = property(getHigh, setHigh, delHigh, "Property for high")
    def export(self, outfile, level, name_='XSDataRBinsIn'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataRBinsIn'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._low is not None:
            self.low.export(outfile, level, name_='low')
        else:
            warnEmptyAttribute("low", "XSDataDouble")
        if self._high is not None:
            self.high.export(outfile, level, name_='high')
        else:
            warnEmptyAttribute("high", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'low':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLow(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'high':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setHigh(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataRBinsIn" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataRBinsIn' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataRBinsIn is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataRBinsIn.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRBinsIn()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataRBinsIn" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRBinsIn()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataRBinsIn

class XSDataRBinsOut(XSDataResult):
    def __init__(self, status=None, bins=None):
        XSDataResult.__init__(self, status)
    
    
        if bins is None:
            self._bins = []
        else:
            checkType("XSDataRBinsOut", "Constructor of XSDataRBinsOut", bins, "list")
            self._bins = bins
    def getBins(self): return self._bins
    def setBins(self, bins):
        checkType("XSDataRBinsOut", "setBins", bins, "list")
        self._bins = bins
    def delBins(self): self._bins = None
    # Properties
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
        self._bins.append(value)
    def insertBins(self, index, value):
        checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
        self._bins[index] = value
    def export(self, outfile, level, name_='XSDataRBinsOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataRBinsOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for bins_ in self.getBins():
            bins_.export(outfile, level, name_='bins')
        if self.getBins() == []:
            warnEmptyAttribute("bins", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bins':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.bins.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataRBinsOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataRBinsOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataRBinsOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataRBinsOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRBinsOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataRBinsOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRBinsOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataRBinsOut

class XSDataResCutoff(XSDataInput):
    def __init__(self, configuration=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, total_completeness=None, detector_max_res=None, completeness_entries=None, xds_res=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", xds_res, "XSDataXdsOutput")
        self._xds_res = xds_res
        if completeness_entries is None:
            self._completeness_entries = []
        else:
            checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", completeness_entries, "list")
            self._completeness_entries = completeness_entries
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", detector_max_res, "XSDataFloat")
        self._detector_max_res = detector_max_res
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", total_completeness, "XSDataXdsCompletenessEntry")
        self._total_completeness = total_completeness
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", res_override, "XSDataFloat")
        self._res_override = res_override
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", completeness_cutoff, "XSDataFloat")
        self._completeness_cutoff = completeness_cutoff
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", isig_cutoff, "XSDataFloat")
        self._isig_cutoff = isig_cutoff
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", r_value_cutoff, "XSDataFloat")
        self._r_value_cutoff = r_value_cutoff
        checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", cc_half_cutoff, "XSDataFloat")
        self._cc_half_cutoff = cc_half_cutoff
    def getXds_res(self): return self._xds_res
    def setXds_res(self, xds_res):
        checkType("XSDataResCutoff", "setXds_res", xds_res, "XSDataXdsOutput")
        self._xds_res = xds_res
    def delXds_res(self): self._xds_res = None
    # Properties
    xds_res = property(getXds_res, setXds_res, delXds_res, "Property for xds_res")
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        checkType("XSDataResCutoff", "setCompleteness_entries", completeness_entries, "list")
        self._completeness_entries = completeness_entries
    def delCompleteness_entries(self): self._completeness_entries = None
    # Properties
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        checkType("XSDataResCutoff", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
        self._completeness_entries.append(value)
    def insertCompleteness_entries(self, index, value):
        checkType("XSDataResCutoff", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
        self._completeness_entries[index] = value
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        checkType("XSDataResCutoff", "setDetector_max_res", detector_max_res, "XSDataFloat")
        self._detector_max_res = detector_max_res
    def delDetector_max_res(self): self._detector_max_res = None
    # Properties
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        checkType("XSDataResCutoff", "setTotal_completeness", total_completeness, "XSDataXdsCompletenessEntry")
        self._total_completeness = total_completeness
    def delTotal_completeness(self): self._total_completeness = None
    # Properties
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        checkType("XSDataResCutoff", "setRes_override", res_override, "XSDataFloat")
        self._res_override = res_override
    def delRes_override(self): self._res_override = None
    # Properties
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        checkType("XSDataResCutoff", "setCompleteness_cutoff", completeness_cutoff, "XSDataFloat")
        self._completeness_cutoff = completeness_cutoff
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    # Properties
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        checkType("XSDataResCutoff", "setIsig_cutoff", isig_cutoff, "XSDataFloat")
        self._isig_cutoff = isig_cutoff
    def delIsig_cutoff(self): self._isig_cutoff = None
    # Properties
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        checkType("XSDataResCutoff", "setR_value_cutoff", r_value_cutoff, "XSDataFloat")
        self._r_value_cutoff = r_value_cutoff
    def delR_value_cutoff(self): self._r_value_cutoff = None
    # Properties
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        checkType("XSDataResCutoff", "setCc_half_cutoff", cc_half_cutoff, "XSDataFloat")
        self._cc_half_cutoff = cc_half_cutoff
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
    # Properties
    cc_half_cutoff = property(getCc_half_cutoff, setCc_half_cutoff, delCc_half_cutoff, "Property for cc_half_cutoff")
    def export(self, outfile, level, name_='XSDataResCutoff'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResCutoff'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._xds_res is not None:
            self.xds_res.export(outfile, level, name_='xds_res')
        else:
            warnEmptyAttribute("xds_res", "XSDataXdsOutput")
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXdsCompletenessEntry")
        if self._detector_max_res is not None:
            self.detector_max_res.export(outfile, level, name_='detector_max_res')
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXdsCompletenessEntry")
        if self._res_override is not None:
            self.res_override.export(outfile, level, name_='res_override')
        if self._completeness_cutoff is not None:
            self.completeness_cutoff.export(outfile, level, name_='completeness_cutoff')
        if self._isig_cutoff is not None:
            self.isig_cutoff.export(outfile, level, name_='isig_cutoff')
        if self._r_value_cutoff is not None:
            self.r_value_cutoff.export(outfile, level, name_='r_value_cutoff')
        if self._cc_half_cutoff is not None:
            self.cc_half_cutoff.export(outfile, level, name_='cc_half_cutoff')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_res':
            obj_ = XSDataXdsOutput()
            obj_.build(child_)
            self.setXds_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_max_res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setDetector_max_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res_override':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes_override(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCompleteness_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isig_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setIsig_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'r_value_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setR_value_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cc_half_cutoff':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCc_half_cutoff(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResCutoff" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResCutoff' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResCutoff is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResCutoff.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoff()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResCutoff" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoff()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResCutoff

class XSDataResCutoffResult(XSDataResult):
    def __init__(self, status=None, total_isig=None, total_rfactor=None, total_complete=None, bins=None, res=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", res, "XSDataFloat")
        self._res = res
        if bins is None:
            self._bins = []
        else:
            checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", bins, "list")
            self._bins = bins
        checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_complete, "XSDataFloat")
        self._total_complete = total_complete
        checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_rfactor, "XSDataFloat")
        self._total_rfactor = total_rfactor
        checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_isig, "XSDataFloat")
        self._total_isig = total_isig
    def getRes(self): return self._res
    def setRes(self, res):
        checkType("XSDataResCutoffResult", "setRes", res, "XSDataFloat")
        self._res = res
    def delRes(self): self._res = None
    # Properties
    res = property(getRes, setRes, delRes, "Property for res")
    def getBins(self): return self._bins
    def setBins(self, bins):
        checkType("XSDataResCutoffResult", "setBins", bins, "list")
        self._bins = bins
    def delBins(self): self._bins = None
    # Properties
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        checkType("XSDataResCutoffResult", "setBins", value, "XSDataFloat")
        self._bins.append(value)
    def insertBins(self, index, value):
        checkType("XSDataResCutoffResult", "setBins", value, "XSDataFloat")
        self._bins[index] = value
    def getTotal_complete(self): return self._total_complete
    def setTotal_complete(self, total_complete):
        checkType("XSDataResCutoffResult", "setTotal_complete", total_complete, "XSDataFloat")
        self._total_complete = total_complete
    def delTotal_complete(self): self._total_complete = None
    # Properties
    total_complete = property(getTotal_complete, setTotal_complete, delTotal_complete, "Property for total_complete")
    def getTotal_rfactor(self): return self._total_rfactor
    def setTotal_rfactor(self, total_rfactor):
        checkType("XSDataResCutoffResult", "setTotal_rfactor", total_rfactor, "XSDataFloat")
        self._total_rfactor = total_rfactor
    def delTotal_rfactor(self): self._total_rfactor = None
    # Properties
    total_rfactor = property(getTotal_rfactor, setTotal_rfactor, delTotal_rfactor, "Property for total_rfactor")
    def getTotal_isig(self): return self._total_isig
    def setTotal_isig(self, total_isig):
        checkType("XSDataResCutoffResult", "setTotal_isig", total_isig, "XSDataFloat")
        self._total_isig = total_isig
    def delTotal_isig(self): self._total_isig = None
    # Properties
    total_isig = property(getTotal_isig, setTotal_isig, delTotal_isig, "Property for total_isig")
    def export(self, outfile, level, name_='XSDataResCutoffResult'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResCutoffResult'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataFloat")
        for bins_ in self.getBins():
            bins_.export(outfile, level, name_='bins')
        if self.getBins() == []:
            warnEmptyAttribute("bins", "XSDataFloat")
        if self._total_complete is not None:
            self.total_complete.export(outfile, level, name_='total_complete')
        else:
            warnEmptyAttribute("total_complete", "XSDataFloat")
        if self._total_rfactor is not None:
            self.total_rfactor.export(outfile, level, name_='total_rfactor')
        else:
            warnEmptyAttribute("total_rfactor", "XSDataFloat")
        if self._total_isig is not None:
            self.total_isig.export(outfile, level, name_='total_isig')
        else:
            warnEmptyAttribute("total_isig", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bins':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.bins.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_complete':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setTotal_complete(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_rfactor':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setTotal_rfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_isig':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setTotal_isig(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResCutoffResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResCutoffResult' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResCutoffResult is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResCutoffResult.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoffResult()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResCutoffResult" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoffResult()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResCutoffResult

class XSDataXdsGenerateInput(XSDataInput):
    def __init__(self, configuration=None, resolution=None, previous_run_dir=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataXdsGenerateInput", "Constructor of XSDataXdsGenerateInput", previous_run_dir, "XSDataString")
        self._previous_run_dir = previous_run_dir
        checkType("XSDataXdsGenerateInput", "Constructor of XSDataXdsGenerateInput", resolution, "XSDataFloat")
        self._resolution = resolution
    def getPrevious_run_dir(self): return self._previous_run_dir
    def setPrevious_run_dir(self, previous_run_dir):
        checkType("XSDataXdsGenerateInput", "setPrevious_run_dir", previous_run_dir, "XSDataString")
        self._previous_run_dir = previous_run_dir
    def delPrevious_run_dir(self): self._previous_run_dir = None
    # Properties
    previous_run_dir = property(getPrevious_run_dir, setPrevious_run_dir, delPrevious_run_dir, "Property for previous_run_dir")
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        checkType("XSDataXdsGenerateInput", "setResolution", resolution, "XSDataFloat")
        self._resolution = resolution
    def delResolution(self): self._resolution = None
    # Properties
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    def export(self, outfile, level, name_='XSDataXdsGenerateInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsGenerateInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._previous_run_dir is not None:
            self.previous_run_dir.export(outfile, level, name_='previous_run_dir')
        else:
            warnEmptyAttribute("previous_run_dir", "XSDataString")
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        else:
            warnEmptyAttribute("resolution", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'previous_run_dir':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPrevious_run_dir(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setResolution(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsGenerateInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsGenerateInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsGenerateInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsGenerateInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsGenerateInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsGenerateInput

class XSDataXdsGenerateOutput(XSDataResult):
    def __init__(self, status=None, gxparm=None, correct_lp_no_anom=None, correct_lp_anom=None, hkl_no_anom=None, hkl_anom=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataXdsGenerateOutput", "Constructor of XSDataXdsGenerateOutput", hkl_anom, "XSDataString")
        self._hkl_anom = hkl_anom
        checkType("XSDataXdsGenerateOutput", "Constructor of XSDataXdsGenerateOutput", hkl_no_anom, "XSDataString")
        self._hkl_no_anom = hkl_no_anom
        checkType("XSDataXdsGenerateOutput", "Constructor of XSDataXdsGenerateOutput", correct_lp_anom, "XSDataString")
        self._correct_lp_anom = correct_lp_anom
        checkType("XSDataXdsGenerateOutput", "Constructor of XSDataXdsGenerateOutput", correct_lp_no_anom, "XSDataString")
        self._correct_lp_no_anom = correct_lp_no_anom
        checkType("XSDataXdsGenerateOutput", "Constructor of XSDataXdsGenerateOutput", gxparm, "XSDataString")
        self._gxparm = gxparm
    def getHkl_anom(self): return self._hkl_anom
    def setHkl_anom(self, hkl_anom):
        checkType("XSDataXdsGenerateOutput", "setHkl_anom", hkl_anom, "XSDataString")
        self._hkl_anom = hkl_anom
    def delHkl_anom(self): self._hkl_anom = None
    # Properties
    hkl_anom = property(getHkl_anom, setHkl_anom, delHkl_anom, "Property for hkl_anom")
    def getHkl_no_anom(self): return self._hkl_no_anom
    def setHkl_no_anom(self, hkl_no_anom):
        checkType("XSDataXdsGenerateOutput", "setHkl_no_anom", hkl_no_anom, "XSDataString")
        self._hkl_no_anom = hkl_no_anom
    def delHkl_no_anom(self): self._hkl_no_anom = None
    # Properties
    hkl_no_anom = property(getHkl_no_anom, setHkl_no_anom, delHkl_no_anom, "Property for hkl_no_anom")
    def getCorrect_lp_anom(self): return self._correct_lp_anom
    def setCorrect_lp_anom(self, correct_lp_anom):
        checkType("XSDataXdsGenerateOutput", "setCorrect_lp_anom", correct_lp_anom, "XSDataString")
        self._correct_lp_anom = correct_lp_anom
    def delCorrect_lp_anom(self): self._correct_lp_anom = None
    # Properties
    correct_lp_anom = property(getCorrect_lp_anom, setCorrect_lp_anom, delCorrect_lp_anom, "Property for correct_lp_anom")
    def getCorrect_lp_no_anom(self): return self._correct_lp_no_anom
    def setCorrect_lp_no_anom(self, correct_lp_no_anom):
        checkType("XSDataXdsGenerateOutput", "setCorrect_lp_no_anom", correct_lp_no_anom, "XSDataString")
        self._correct_lp_no_anom = correct_lp_no_anom
    def delCorrect_lp_no_anom(self): self._correct_lp_no_anom = None
    # Properties
    correct_lp_no_anom = property(getCorrect_lp_no_anom, setCorrect_lp_no_anom, delCorrect_lp_no_anom, "Property for correct_lp_no_anom")
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        checkType("XSDataXdsGenerateOutput", "setGxparm", gxparm, "XSDataString")
        self._gxparm = gxparm
    def delGxparm(self): self._gxparm = None
    # Properties
    gxparm = property(getGxparm, setGxparm, delGxparm, "Property for gxparm")
    def export(self, outfile, level, name_='XSDataXdsGenerateOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsGenerateOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._hkl_anom is not None:
            self.hkl_anom.export(outfile, level, name_='hkl_anom')
        else:
            warnEmptyAttribute("hkl_anom", "XSDataString")
        if self._hkl_no_anom is not None:
            self.hkl_no_anom.export(outfile, level, name_='hkl_no_anom')
        else:
            warnEmptyAttribute("hkl_no_anom", "XSDataString")
        if self._correct_lp_anom is not None:
            self.correct_lp_anom.export(outfile, level, name_='correct_lp_anom')
        else:
            warnEmptyAttribute("correct_lp_anom", "XSDataString")
        if self._correct_lp_no_anom is not None:
            self.correct_lp_no_anom.export(outfile, level, name_='correct_lp_no_anom')
        else:
            warnEmptyAttribute("correct_lp_no_anom", "XSDataString")
        if self._gxparm is not None:
            self.gxparm.export(outfile, level, name_='gxparm')
        else:
            warnEmptyAttribute("gxparm", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_no_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_no_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCorrect_lp_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp_no_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCorrect_lp_no_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gxparm':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGxparm(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsGenerateOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsGenerateOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsGenerateOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsGenerateOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsGenerateOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsGenerateOutput

class XSDataXdsOutput(XSDataResult):
    def __init__(self, status=None, xds_run_directory=None, sg_number=None, unit_cell_constants=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, coordinates_of_unit_cell_c_axis=None, coordinates_of_unit_cell_b_axis=None, coordinates_of_unit_cell_a_axis=None, crystal_to_detector_distance=None, detector_origin=None, direct_beam_detector_coordinates=None, direct_beam_coordinates=None, crystal_mosaicity=None, total_completeness=None, completeness_entries=None):
        XSDataResult.__init__(self, status)
    
    
        if completeness_entries is None:
            self._completeness_entries = []
        else:
            checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", completeness_entries, "list")
            self._completeness_entries = completeness_entries
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", total_completeness, "XSDataXdsCompletenessEntry")
        self._total_completeness = total_completeness
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", crystal_mosaicity, "XSDataFloat")
        self._crystal_mosaicity = crystal_mosaicity
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", direct_beam_coordinates, "XSDataVectorDouble")
        self._direct_beam_coordinates = direct_beam_coordinates
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", direct_beam_detector_coordinates, "XSData2DCoordinates")
        self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", detector_origin, "XSData2DCoordinates")
        self._detector_origin = detector_origin
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", crystal_to_detector_distance, "XSDataFloat")
        self._crystal_to_detector_distance = crystal_to_detector_distance
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_a_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_b_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_c_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_a, "XSDataFloat")
        self._cell_a = cell_a
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_b, "XSDataFloat")
        self._cell_b = cell_b
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_c, "XSDataFloat")
        self._cell_c = cell_c
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_alpha, "XSDataFloat")
        self._cell_alpha = cell_alpha
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_beta, "XSDataFloat")
        self._cell_beta = cell_beta
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_gamma, "XSDataFloat")
        self._cell_gamma = cell_gamma
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        else:
            checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", unit_cell_constants, "list")
            self._unit_cell_constants = unit_cell_constants
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", sg_number, "XSDataInteger")
        self._sg_number = sg_number
        checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", xds_run_directory, "XSDataString")
        self._xds_run_directory = xds_run_directory
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        checkType("XSDataXdsOutput", "setCompleteness_entries", completeness_entries, "list")
        self._completeness_entries = completeness_entries
    def delCompleteness_entries(self): self._completeness_entries = None
    # Properties
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        checkType("XSDataXdsOutput", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
        self._completeness_entries.append(value)
    def insertCompleteness_entries(self, index, value):
        checkType("XSDataXdsOutput", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
        self._completeness_entries[index] = value
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        checkType("XSDataXdsOutput", "setTotal_completeness", total_completeness, "XSDataXdsCompletenessEntry")
        self._total_completeness = total_completeness
    def delTotal_completeness(self): self._total_completeness = None
    # Properties
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    def getCrystal_mosaicity(self): return self._crystal_mosaicity
    def setCrystal_mosaicity(self, crystal_mosaicity):
        checkType("XSDataXdsOutput", "setCrystal_mosaicity", crystal_mosaicity, "XSDataFloat")
        self._crystal_mosaicity = crystal_mosaicity
    def delCrystal_mosaicity(self): self._crystal_mosaicity = None
    # Properties
    crystal_mosaicity = property(getCrystal_mosaicity, setCrystal_mosaicity, delCrystal_mosaicity, "Property for crystal_mosaicity")
    def getDirect_beam_coordinates(self): return self._direct_beam_coordinates
    def setDirect_beam_coordinates(self, direct_beam_coordinates):
        checkType("XSDataXdsOutput", "setDirect_beam_coordinates", direct_beam_coordinates, "XSDataVectorDouble")
        self._direct_beam_coordinates = direct_beam_coordinates
    def delDirect_beam_coordinates(self): self._direct_beam_coordinates = None
    # Properties
    direct_beam_coordinates = property(getDirect_beam_coordinates, setDirect_beam_coordinates, delDirect_beam_coordinates, "Property for direct_beam_coordinates")
    def getDirect_beam_detector_coordinates(self): return self._direct_beam_detector_coordinates
    def setDirect_beam_detector_coordinates(self, direct_beam_detector_coordinates):
        checkType("XSDataXdsOutput", "setDirect_beam_detector_coordinates", direct_beam_detector_coordinates, "XSData2DCoordinates")
        self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
    def delDirect_beam_detector_coordinates(self): self._direct_beam_detector_coordinates = None
    # Properties
    direct_beam_detector_coordinates = property(getDirect_beam_detector_coordinates, setDirect_beam_detector_coordinates, delDirect_beam_detector_coordinates, "Property for direct_beam_detector_coordinates")
    def getDetector_origin(self): return self._detector_origin
    def setDetector_origin(self, detector_origin):
        checkType("XSDataXdsOutput", "setDetector_origin", detector_origin, "XSData2DCoordinates")
        self._detector_origin = detector_origin
    def delDetector_origin(self): self._detector_origin = None
    # Properties
    detector_origin = property(getDetector_origin, setDetector_origin, delDetector_origin, "Property for detector_origin")
    def getCrystal_to_detector_distance(self): return self._crystal_to_detector_distance
    def setCrystal_to_detector_distance(self, crystal_to_detector_distance):
        checkType("XSDataXdsOutput", "setCrystal_to_detector_distance", crystal_to_detector_distance, "XSDataFloat")
        self._crystal_to_detector_distance = crystal_to_detector_distance
    def delCrystal_to_detector_distance(self): self._crystal_to_detector_distance = None
    # Properties
    crystal_to_detector_distance = property(getCrystal_to_detector_distance, setCrystal_to_detector_distance, delCrystal_to_detector_distance, "Property for crystal_to_detector_distance")
    def getCoordinates_of_unit_cell_a_axis(self): return self._coordinates_of_unit_cell_a_axis
    def setCoordinates_of_unit_cell_a_axis(self, coordinates_of_unit_cell_a_axis):
        checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_a_axis", coordinates_of_unit_cell_a_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
    def delCoordinates_of_unit_cell_a_axis(self): self._coordinates_of_unit_cell_a_axis = None
    # Properties
    coordinates_of_unit_cell_a_axis = property(getCoordinates_of_unit_cell_a_axis, setCoordinates_of_unit_cell_a_axis, delCoordinates_of_unit_cell_a_axis, "Property for coordinates_of_unit_cell_a_axis")
    def getCoordinates_of_unit_cell_b_axis(self): return self._coordinates_of_unit_cell_b_axis
    def setCoordinates_of_unit_cell_b_axis(self, coordinates_of_unit_cell_b_axis):
        checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_b_axis", coordinates_of_unit_cell_b_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
    def delCoordinates_of_unit_cell_b_axis(self): self._coordinates_of_unit_cell_b_axis = None
    # Properties
    coordinates_of_unit_cell_b_axis = property(getCoordinates_of_unit_cell_b_axis, setCoordinates_of_unit_cell_b_axis, delCoordinates_of_unit_cell_b_axis, "Property for coordinates_of_unit_cell_b_axis")
    def getCoordinates_of_unit_cell_c_axis(self): return self._coordinates_of_unit_cell_c_axis
    def setCoordinates_of_unit_cell_c_axis(self, coordinates_of_unit_cell_c_axis):
        checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_c_axis", coordinates_of_unit_cell_c_axis, "XSDataVectorDouble")
        self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
    def delCoordinates_of_unit_cell_c_axis(self): self._coordinates_of_unit_cell_c_axis = None
    # Properties
    coordinates_of_unit_cell_c_axis = property(getCoordinates_of_unit_cell_c_axis, setCoordinates_of_unit_cell_c_axis, delCoordinates_of_unit_cell_c_axis, "Property for coordinates_of_unit_cell_c_axis")
    def getCell_a(self): return self._cell_a
    def setCell_a(self, cell_a):
        checkType("XSDataXdsOutput", "setCell_a", cell_a, "XSDataFloat")
        self._cell_a = cell_a
    def delCell_a(self): self._cell_a = None
    # Properties
    cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
    def getCell_b(self): return self._cell_b
    def setCell_b(self, cell_b):
        checkType("XSDataXdsOutput", "setCell_b", cell_b, "XSDataFloat")
        self._cell_b = cell_b
    def delCell_b(self): self._cell_b = None
    # Properties
    cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
    def getCell_c(self): return self._cell_c
    def setCell_c(self, cell_c):
        checkType("XSDataXdsOutput", "setCell_c", cell_c, "XSDataFloat")
        self._cell_c = cell_c
    def delCell_c(self): self._cell_c = None
    # Properties
    cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
    def getCell_alpha(self): return self._cell_alpha
    def setCell_alpha(self, cell_alpha):
        checkType("XSDataXdsOutput", "setCell_alpha", cell_alpha, "XSDataFloat")
        self._cell_alpha = cell_alpha
    def delCell_alpha(self): self._cell_alpha = None
    # Properties
    cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
    def getCell_beta(self): return self._cell_beta
    def setCell_beta(self, cell_beta):
        checkType("XSDataXdsOutput", "setCell_beta", cell_beta, "XSDataFloat")
        self._cell_beta = cell_beta
    def delCell_beta(self): self._cell_beta = None
    # Properties
    cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
    def getCell_gamma(self): return self._cell_gamma
    def setCell_gamma(self, cell_gamma):
        checkType("XSDataXdsOutput", "setCell_gamma", cell_gamma, "XSDataFloat")
        self._cell_gamma = cell_gamma
    def delCell_gamma(self): self._cell_gamma = None
    # Properties
    cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        checkType("XSDataXdsOutput", "setUnit_cell_constants", unit_cell_constants, "list")
        self._unit_cell_constants = unit_cell_constants
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    # Properties
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        checkType("XSDataXdsOutput", "setUnit_cell_constants", value, "XSDataFloat")
        self._unit_cell_constants.append(value)
    def insertUnit_cell_constants(self, index, value):
        checkType("XSDataXdsOutput", "setUnit_cell_constants", value, "XSDataFloat")
        self._unit_cell_constants[index] = value
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        checkType("XSDataXdsOutput", "setSg_number", sg_number, "XSDataInteger")
        self._sg_number = sg_number
    def delSg_number(self): self._sg_number = None
    # Properties
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    def getXds_run_directory(self): return self._xds_run_directory
    def setXds_run_directory(self, xds_run_directory):
        checkType("XSDataXdsOutput", "setXds_run_directory", xds_run_directory, "XSDataString")
        self._xds_run_directory = xds_run_directory
    def delXds_run_directory(self): self._xds_run_directory = None
    # Properties
    xds_run_directory = property(getXds_run_directory, setXds_run_directory, delXds_run_directory, "Property for xds_run_directory")
    def export(self, outfile, level, name_='XSDataXdsOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXdsCompletenessEntry")
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXdsCompletenessEntry")
        if self._crystal_mosaicity is not None:
            self.crystal_mosaicity.export(outfile, level, name_='crystal_mosaicity')
        else:
            warnEmptyAttribute("crystal_mosaicity", "XSDataFloat")
        if self._direct_beam_coordinates is not None:
            self.direct_beam_coordinates.export(outfile, level, name_='direct_beam_coordinates')
        else:
            warnEmptyAttribute("direct_beam_coordinates", "XSDataVectorDouble")
        if self._direct_beam_detector_coordinates is not None:
            self.direct_beam_detector_coordinates.export(outfile, level, name_='direct_beam_detector_coordinates')
        else:
            warnEmptyAttribute("direct_beam_detector_coordinates", "XSData2DCoordinates")
        if self._detector_origin is not None:
            self.detector_origin.export(outfile, level, name_='detector_origin')
        else:
            warnEmptyAttribute("detector_origin", "XSData2DCoordinates")
        if self._crystal_to_detector_distance is not None:
            self.crystal_to_detector_distance.export(outfile, level, name_='crystal_to_detector_distance')
        else:
            warnEmptyAttribute("crystal_to_detector_distance", "XSDataFloat")
        if self._coordinates_of_unit_cell_a_axis is not None:
            self.coordinates_of_unit_cell_a_axis.export(outfile, level, name_='coordinates_of_unit_cell_a_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_a_axis", "XSDataVectorDouble")
        if self._coordinates_of_unit_cell_b_axis is not None:
            self.coordinates_of_unit_cell_b_axis.export(outfile, level, name_='coordinates_of_unit_cell_b_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_b_axis", "XSDataVectorDouble")
        if self._coordinates_of_unit_cell_c_axis is not None:
            self.coordinates_of_unit_cell_c_axis.export(outfile, level, name_='coordinates_of_unit_cell_c_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_c_axis", "XSDataVectorDouble")
        if self._cell_a is not None:
            self.cell_a.export(outfile, level, name_='cell_a')
        else:
            warnEmptyAttribute("cell_a", "XSDataFloat")
        if self._cell_b is not None:
            self.cell_b.export(outfile, level, name_='cell_b')
        else:
            warnEmptyAttribute("cell_b", "XSDataFloat")
        if self._cell_c is not None:
            self.cell_c.export(outfile, level, name_='cell_c')
        else:
            warnEmptyAttribute("cell_c", "XSDataFloat")
        if self._cell_alpha is not None:
            self.cell_alpha.export(outfile, level, name_='cell_alpha')
        else:
            warnEmptyAttribute("cell_alpha", "XSDataFloat")
        if self._cell_beta is not None:
            self.cell_beta.export(outfile, level, name_='cell_beta')
        else:
            warnEmptyAttribute("cell_beta", "XSDataFloat")
        if self._cell_gamma is not None:
            self.cell_gamma.export(outfile, level, name_='cell_gamma')
        else:
            warnEmptyAttribute("cell_gamma", "XSDataFloat")
        for unit_cell_constants_ in self.getUnit_cell_constants():
            unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
        if self._sg_number is not None:
            self.sg_number.export(outfile, level, name_='sg_number')
        if self._xds_run_directory is not None:
            self.xds_run_directory.export(outfile, level, name_='xds_run_directory')
        else:
            warnEmptyAttribute("xds_run_directory", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal_mosaicity':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCrystal_mosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direct_beam_coordinates':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDirect_beam_coordinates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direct_beam_detector_coordinates':
            obj_ = XSData2DCoordinates()
            obj_.build(child_)
            self.setDirect_beam_detector_coordinates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_origin':
            obj_ = XSData2DCoordinates()
            obj_.build(child_)
            self.setDetector_origin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal_to_detector_distance':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCrystal_to_detector_distance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_a_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_a_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_b_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_b_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_c_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_c_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_a':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_b':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_c':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_alpha':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_beta':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_gamma':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setCell_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_constants':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.unit_cell_constants.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sg_number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSg_number(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_run_directory':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setXds_run_directory(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsOutput

class XSDataXdsOutputFile(XSDataInput):
    def __init__(self, configuration=None, gxparm=None, correct_lp=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", correct_lp, "XSDataFile")
        self._correct_lp = correct_lp
        checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", gxparm, "XSDataFile")
        self._gxparm = gxparm
    def getCorrect_lp(self): return self._correct_lp
    def setCorrect_lp(self, correct_lp):
        checkType("XSDataXdsOutputFile", "setCorrect_lp", correct_lp, "XSDataFile")
        self._correct_lp = correct_lp
    def delCorrect_lp(self): self._correct_lp = None
    # Properties
    correct_lp = property(getCorrect_lp, setCorrect_lp, delCorrect_lp, "Property for correct_lp")
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        checkType("XSDataXdsOutputFile", "setGxparm", gxparm, "XSDataFile")
        self._gxparm = gxparm
    def delGxparm(self): self._gxparm = None
    # Properties
    gxparm = property(getGxparm, setGxparm, delGxparm, "Property for gxparm")
    def export(self, outfile, level, name_='XSDataXdsOutputFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsOutputFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._correct_lp is not None:
            self.correct_lp.export(outfile, level, name_='correct_lp')
        else:
            warnEmptyAttribute("correct_lp", "XSDataFile")
        if self._gxparm is not None:
            self.gxparm.export(outfile, level, name_='gxparm')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCorrect_lp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gxparm':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGxparm(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsOutputFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsOutputFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsOutputFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutputFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutputFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsOutputFile

class XSDataXscaleParsedOutput(XSDataResult):
    def __init__(self, status=None, completeness_entries=None, total_completeness=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataXscaleParsedOutput", "Constructor of XSDataXscaleParsedOutput", total_completeness, "XSDataXscaleCompletenessEntry")
        self._total_completeness = total_completeness
        if completeness_entries is None:
            self._completeness_entries = []
        else:
            checkType("XSDataXscaleParsedOutput", "Constructor of XSDataXscaleParsedOutput", completeness_entries, "list")
            self._completeness_entries = completeness_entries
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        checkType("XSDataXscaleParsedOutput", "setTotal_completeness", total_completeness, "XSDataXscaleCompletenessEntry")
        self._total_completeness = total_completeness
    def delTotal_completeness(self): self._total_completeness = None
    # Properties
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        checkType("XSDataXscaleParsedOutput", "setCompleteness_entries", completeness_entries, "list")
        self._completeness_entries = completeness_entries
    def delCompleteness_entries(self): self._completeness_entries = None
    # Properties
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        checkType("XSDataXscaleParsedOutput", "setCompleteness_entries", value, "XSDataXscaleCompletenessEntry")
        self._completeness_entries.append(value)
    def insertCompleteness_entries(self, index, value):
        checkType("XSDataXscaleParsedOutput", "setCompleteness_entries", value, "XSDataXscaleCompletenessEntry")
        self._completeness_entries[index] = value
    def export(self, outfile, level, name_='XSDataXscaleParsedOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleParsedOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXscaleCompletenessEntry")
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXscaleCompletenessEntry")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXscaleCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXscaleCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleParsedOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleParsedOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleParsedOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleParsedOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsedOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleParsedOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsedOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleParsedOutput

class XSDataXscaleGeneratedFiles(XSDataResult):
    def __init__(self, status=None, stats_noanom_unmerged=None, lp_noanom_unmerged=None, hkl_noanom_unmerged=None, stats_anom_unmerged=None, lp_anom_unmerged=None, hkl_anom_unmerged=None, stats_noanom_merged=None, lp_noanom_merged=None, hkl_noanom_merged=None, stats_anom_merged=None, lp_anom_merged=None, hkl_anom_merged=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", hkl_anom_merged, "XSDataString")
        self._hkl_anom_merged = hkl_anom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", lp_anom_merged, "XSDataString")
        self._lp_anom_merged = lp_anom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", stats_anom_merged, "XSDataXscaleParsedOutput")
        self._stats_anom_merged = stats_anom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", hkl_noanom_merged, "XSDataString")
        self._hkl_noanom_merged = hkl_noanom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", lp_noanom_merged, "XSDataString")
        self._lp_noanom_merged = lp_noanom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", stats_noanom_merged, "XSDataXscaleParsedOutput")
        self._stats_noanom_merged = stats_noanom_merged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", hkl_anom_unmerged, "XSDataString")
        self._hkl_anom_unmerged = hkl_anom_unmerged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", lp_anom_unmerged, "XSDataString")
        self._lp_anom_unmerged = lp_anom_unmerged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", stats_anom_unmerged, "XSDataXscaleParsedOutput")
        self._stats_anom_unmerged = stats_anom_unmerged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", hkl_noanom_unmerged, "XSDataString")
        self._hkl_noanom_unmerged = hkl_noanom_unmerged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", lp_noanom_unmerged, "XSDataString")
        self._lp_noanom_unmerged = lp_noanom_unmerged
        checkType("XSDataXscaleGeneratedFiles", "Constructor of XSDataXscaleGeneratedFiles", stats_noanom_unmerged, "XSDataXscaleParsedOutput")
        self._stats_noanom_unmerged = stats_noanom_unmerged
    def getHkl_anom_merged(self): return self._hkl_anom_merged
    def setHkl_anom_merged(self, hkl_anom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setHkl_anom_merged", hkl_anom_merged, "XSDataString")
        self._hkl_anom_merged = hkl_anom_merged
    def delHkl_anom_merged(self): self._hkl_anom_merged = None
    # Properties
    hkl_anom_merged = property(getHkl_anom_merged, setHkl_anom_merged, delHkl_anom_merged, "Property for hkl_anom_merged")
    def getLp_anom_merged(self): return self._lp_anom_merged
    def setLp_anom_merged(self, lp_anom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setLp_anom_merged", lp_anom_merged, "XSDataString")
        self._lp_anom_merged = lp_anom_merged
    def delLp_anom_merged(self): self._lp_anom_merged = None
    # Properties
    lp_anom_merged = property(getLp_anom_merged, setLp_anom_merged, delLp_anom_merged, "Property for lp_anom_merged")
    def getStats_anom_merged(self): return self._stats_anom_merged
    def setStats_anom_merged(self, stats_anom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setStats_anom_merged", stats_anom_merged, "XSDataXscaleParsedOutput")
        self._stats_anom_merged = stats_anom_merged
    def delStats_anom_merged(self): self._stats_anom_merged = None
    # Properties
    stats_anom_merged = property(getStats_anom_merged, setStats_anom_merged, delStats_anom_merged, "Property for stats_anom_merged")
    def getHkl_noanom_merged(self): return self._hkl_noanom_merged
    def setHkl_noanom_merged(self, hkl_noanom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setHkl_noanom_merged", hkl_noanom_merged, "XSDataString")
        self._hkl_noanom_merged = hkl_noanom_merged
    def delHkl_noanom_merged(self): self._hkl_noanom_merged = None
    # Properties
    hkl_noanom_merged = property(getHkl_noanom_merged, setHkl_noanom_merged, delHkl_noanom_merged, "Property for hkl_noanom_merged")
    def getLp_noanom_merged(self): return self._lp_noanom_merged
    def setLp_noanom_merged(self, lp_noanom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setLp_noanom_merged", lp_noanom_merged, "XSDataString")
        self._lp_noanom_merged = lp_noanom_merged
    def delLp_noanom_merged(self): self._lp_noanom_merged = None
    # Properties
    lp_noanom_merged = property(getLp_noanom_merged, setLp_noanom_merged, delLp_noanom_merged, "Property for lp_noanom_merged")
    def getStats_noanom_merged(self): return self._stats_noanom_merged
    def setStats_noanom_merged(self, stats_noanom_merged):
        checkType("XSDataXscaleGeneratedFiles", "setStats_noanom_merged", stats_noanom_merged, "XSDataXscaleParsedOutput")
        self._stats_noanom_merged = stats_noanom_merged
    def delStats_noanom_merged(self): self._stats_noanom_merged = None
    # Properties
    stats_noanom_merged = property(getStats_noanom_merged, setStats_noanom_merged, delStats_noanom_merged, "Property for stats_noanom_merged")
    def getHkl_anom_unmerged(self): return self._hkl_anom_unmerged
    def setHkl_anom_unmerged(self, hkl_anom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setHkl_anom_unmerged", hkl_anom_unmerged, "XSDataString")
        self._hkl_anom_unmerged = hkl_anom_unmerged
    def delHkl_anom_unmerged(self): self._hkl_anom_unmerged = None
    # Properties
    hkl_anom_unmerged = property(getHkl_anom_unmerged, setHkl_anom_unmerged, delHkl_anom_unmerged, "Property for hkl_anom_unmerged")
    def getLp_anom_unmerged(self): return self._lp_anom_unmerged
    def setLp_anom_unmerged(self, lp_anom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setLp_anom_unmerged", lp_anom_unmerged, "XSDataString")
        self._lp_anom_unmerged = lp_anom_unmerged
    def delLp_anom_unmerged(self): self._lp_anom_unmerged = None
    # Properties
    lp_anom_unmerged = property(getLp_anom_unmerged, setLp_anom_unmerged, delLp_anom_unmerged, "Property for lp_anom_unmerged")
    def getStats_anom_unmerged(self): return self._stats_anom_unmerged
    def setStats_anom_unmerged(self, stats_anom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setStats_anom_unmerged", stats_anom_unmerged, "XSDataXscaleParsedOutput")
        self._stats_anom_unmerged = stats_anom_unmerged
    def delStats_anom_unmerged(self): self._stats_anom_unmerged = None
    # Properties
    stats_anom_unmerged = property(getStats_anom_unmerged, setStats_anom_unmerged, delStats_anom_unmerged, "Property for stats_anom_unmerged")
    def getHkl_noanom_unmerged(self): return self._hkl_noanom_unmerged
    def setHkl_noanom_unmerged(self, hkl_noanom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setHkl_noanom_unmerged", hkl_noanom_unmerged, "XSDataString")
        self._hkl_noanom_unmerged = hkl_noanom_unmerged
    def delHkl_noanom_unmerged(self): self._hkl_noanom_unmerged = None
    # Properties
    hkl_noanom_unmerged = property(getHkl_noanom_unmerged, setHkl_noanom_unmerged, delHkl_noanom_unmerged, "Property for hkl_noanom_unmerged")
    def getLp_noanom_unmerged(self): return self._lp_noanom_unmerged
    def setLp_noanom_unmerged(self, lp_noanom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setLp_noanom_unmerged", lp_noanom_unmerged, "XSDataString")
        self._lp_noanom_unmerged = lp_noanom_unmerged
    def delLp_noanom_unmerged(self): self._lp_noanom_unmerged = None
    # Properties
    lp_noanom_unmerged = property(getLp_noanom_unmerged, setLp_noanom_unmerged, delLp_noanom_unmerged, "Property for lp_noanom_unmerged")
    def getStats_noanom_unmerged(self): return self._stats_noanom_unmerged
    def setStats_noanom_unmerged(self, stats_noanom_unmerged):
        checkType("XSDataXscaleGeneratedFiles", "setStats_noanom_unmerged", stats_noanom_unmerged, "XSDataXscaleParsedOutput")
        self._stats_noanom_unmerged = stats_noanom_unmerged
    def delStats_noanom_unmerged(self): self._stats_noanom_unmerged = None
    # Properties
    stats_noanom_unmerged = property(getStats_noanom_unmerged, setStats_noanom_unmerged, delStats_noanom_unmerged, "Property for stats_noanom_unmerged")
    def export(self, outfile, level, name_='XSDataXscaleGeneratedFiles'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleGeneratedFiles'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._hkl_anom_merged is not None:
            self.hkl_anom_merged.export(outfile, level, name_='hkl_anom_merged')
        else:
            warnEmptyAttribute("hkl_anom_merged", "XSDataString")
        if self._lp_anom_merged is not None:
            self.lp_anom_merged.export(outfile, level, name_='lp_anom_merged')
        else:
            warnEmptyAttribute("lp_anom_merged", "XSDataString")
        if self._stats_anom_merged is not None:
            self.stats_anom_merged.export(outfile, level, name_='stats_anom_merged')
        else:
            warnEmptyAttribute("stats_anom_merged", "XSDataXscaleParsedOutput")
        if self._hkl_noanom_merged is not None:
            self.hkl_noanom_merged.export(outfile, level, name_='hkl_noanom_merged')
        else:
            warnEmptyAttribute("hkl_noanom_merged", "XSDataString")
        if self._lp_noanom_merged is not None:
            self.lp_noanom_merged.export(outfile, level, name_='lp_noanom_merged')
        else:
            warnEmptyAttribute("lp_noanom_merged", "XSDataString")
        if self._stats_noanom_merged is not None:
            self.stats_noanom_merged.export(outfile, level, name_='stats_noanom_merged')
        else:
            warnEmptyAttribute("stats_noanom_merged", "XSDataXscaleParsedOutput")
        if self._hkl_anom_unmerged is not None:
            self.hkl_anom_unmerged.export(outfile, level, name_='hkl_anom_unmerged')
        else:
            warnEmptyAttribute("hkl_anom_unmerged", "XSDataString")
        if self._lp_anom_unmerged is not None:
            self.lp_anom_unmerged.export(outfile, level, name_='lp_anom_unmerged')
        else:
            warnEmptyAttribute("lp_anom_unmerged", "XSDataString")
        if self._stats_anom_unmerged is not None:
            self.stats_anom_unmerged.export(outfile, level, name_='stats_anom_unmerged')
        else:
            warnEmptyAttribute("stats_anom_unmerged", "XSDataXscaleParsedOutput")
        if self._hkl_noanom_unmerged is not None:
            self.hkl_noanom_unmerged.export(outfile, level, name_='hkl_noanom_unmerged')
        else:
            warnEmptyAttribute("hkl_noanom_unmerged", "XSDataString")
        if self._lp_noanom_unmerged is not None:
            self.lp_noanom_unmerged.export(outfile, level, name_='lp_noanom_unmerged')
        else:
            warnEmptyAttribute("lp_noanom_unmerged", "XSDataString")
        if self._stats_noanom_unmerged is not None:
            self.stats_noanom_unmerged.export(outfile, level, name_='stats_noanom_unmerged')
        else:
            warnEmptyAttribute("stats_noanom_unmerged", "XSDataXscaleParsedOutput")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_anom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_anom_merged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_noanom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_noanom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_noanom_merged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_anom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_anom_unmerged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_noanom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_noanom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_noanom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_noanom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_noanom_unmerged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_noanom_unmerged(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleGeneratedFiles" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleGeneratedFiles' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleGeneratedFiles is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleGeneratedFiles.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleGeneratedFiles()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleGeneratedFiles" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleGeneratedFiles()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleGeneratedFiles

class XSDataXscaleInputFile(XSDataInput):
    def __init__(self, configuration=None, res=None, path=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataXscaleInputFile", "Constructor of XSDataXscaleInputFile", path, "XSDataString")
        self._path = path
        checkType("XSDataXscaleInputFile", "Constructor of XSDataXscaleInputFile", res, "XSDataFloat")
        self._res = res
    def getPath(self): return self._path
    def setPath(self, path):
        checkType("XSDataXscaleInputFile", "setPath", path, "XSDataString")
        self._path = path
    def delPath(self): self._path = None
    # Properties
    path = property(getPath, setPath, delPath, "Property for path")
    def getRes(self): return self._res
    def setRes(self, res):
        checkType("XSDataXscaleInputFile", "setRes", res, "XSDataFloat")
        self._res = res
    def delRes(self): self._res = None
    # Properties
    res = property(getRes, setRes, delRes, "Property for res")
    def export(self, outfile, level, name_='XSDataXscaleInputFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleInputFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._path is not None:
            self.path.export(outfile, level, name_='path')
        else:
            warnEmptyAttribute("path", "XSDataString")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleInputFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleInputFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleInputFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleInputFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInputFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleInputFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInputFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleInputFile

class XSDataXscaleInput(XSDataInput):
    def __init__(self, configuration=None, bins=None, sg_number=None, unit_cell_constants=None, xds_files=None, friedels_law=None, merge=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", merge, "XSDataBoolean")
        self._merge = merge
        checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", friedels_law, "XSDataBoolean")
        self._friedels_law = friedels_law
        if xds_files is None:
            self._xds_files = []
        else:
            checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", xds_files, "list")
            self._xds_files = xds_files
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        else:
            checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", unit_cell_constants, "list")
            self._unit_cell_constants = unit_cell_constants
        checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", sg_number, "XSDataInteger")
        self._sg_number = sg_number
        if bins is None:
            self._bins = []
        else:
            checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", bins, "list")
            self._bins = bins
    def getMerge(self): return self._merge
    def setMerge(self, merge):
        checkType("XSDataXscaleInput", "setMerge", merge, "XSDataBoolean")
        self._merge = merge
    def delMerge(self): self._merge = None
    # Properties
    merge = property(getMerge, setMerge, delMerge, "Property for merge")
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        checkType("XSDataXscaleInput", "setFriedels_law", friedels_law, "XSDataBoolean")
        self._friedels_law = friedels_law
    def delFriedels_law(self): self._friedels_law = None
    # Properties
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    def getXds_files(self): return self._xds_files
    def setXds_files(self, xds_files):
        checkType("XSDataXscaleInput", "setXds_files", xds_files, "list")
        self._xds_files = xds_files
    def delXds_files(self): self._xds_files = None
    # Properties
    xds_files = property(getXds_files, setXds_files, delXds_files, "Property for xds_files")
    def addXds_files(self, value):
        checkType("XSDataXscaleInput", "setXds_files", value, "XSDataXscaleInputFile")
        self._xds_files.append(value)
    def insertXds_files(self, index, value):
        checkType("XSDataXscaleInput", "setXds_files", value, "XSDataXscaleInputFile")
        self._xds_files[index] = value
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        checkType("XSDataXscaleInput", "setUnit_cell_constants", unit_cell_constants, "list")
        self._unit_cell_constants = unit_cell_constants
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    # Properties
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        checkType("XSDataXscaleInput", "setUnit_cell_constants", value, "XSDataFloat")
        self._unit_cell_constants.append(value)
    def insertUnit_cell_constants(self, index, value):
        checkType("XSDataXscaleInput", "setUnit_cell_constants", value, "XSDataFloat")
        self._unit_cell_constants[index] = value
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        checkType("XSDataXscaleInput", "setSg_number", sg_number, "XSDataInteger")
        self._sg_number = sg_number
    def delSg_number(self): self._sg_number = None
    # Properties
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    def getBins(self): return self._bins
    def setBins(self, bins):
        checkType("XSDataXscaleInput", "setBins", bins, "list")
        self._bins = bins
    def delBins(self): self._bins = None
    # Properties
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        checkType("XSDataXscaleInput", "setBins", value, "XSDataDouble")
        self._bins.append(value)
    def insertBins(self, index, value):
        checkType("XSDataXscaleInput", "setBins", value, "XSDataDouble")
        self._bins[index] = value
    def export(self, outfile, level, name_='XSDataXscaleInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._merge is not None:
            self.merge.export(outfile, level, name_='merge')
        else:
            warnEmptyAttribute("merge", "XSDataBoolean")
        if self._friedels_law is not None:
            self.friedels_law.export(outfile, level, name_='friedels_law')
        else:
            warnEmptyAttribute("friedels_law", "XSDataBoolean")
        for xds_files_ in self.getXds_files():
            xds_files_.export(outfile, level, name_='xds_files')
        if self.getXds_files() == []:
            warnEmptyAttribute("xds_files", "XSDataXscaleInputFile")
        for unit_cell_constants_ in self.getUnit_cell_constants():
            unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
        if self.getUnit_cell_constants() == []:
            warnEmptyAttribute("unit_cell_constants", "XSDataFloat")
        if self._sg_number is not None:
            self.sg_number.export(outfile, level, name_='sg_number')
        else:
            warnEmptyAttribute("sg_number", "XSDataInteger")
        for bins_ in self.getBins():
            bins_.export(outfile, level, name_='bins')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'merge':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setMerge(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'friedels_law':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setFriedels_law(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_files':
            obj_ = XSDataXscaleInputFile()
            obj_.build(child_)
            self.xds_files.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_constants':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.unit_cell_constants.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sg_number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSg_number(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bins':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.bins.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleInput

class XSDataXscaleOutput(XSDataResult):
    def __init__(self, status=None, lp_file=None, hkl_file=None, succeeded=None):
        XSDataResult.__init__(self, status)
    
    
        checkType("XSDataXscaleOutput", "Constructor of XSDataXscaleOutput", succeeded, "XSDataBoolean")
        self._succeeded = succeeded
        checkType("XSDataXscaleOutput", "Constructor of XSDataXscaleOutput", hkl_file, "XSDataString")
        self._hkl_file = hkl_file
        checkType("XSDataXscaleOutput", "Constructor of XSDataXscaleOutput", lp_file, "XSDataString")
        self._lp_file = lp_file
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        checkType("XSDataXscaleOutput", "setSucceeded", succeeded, "XSDataBoolean")
        self._succeeded = succeeded
    def delSucceeded(self): self._succeeded = None
    # Properties
    succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
    def getHkl_file(self): return self._hkl_file
    def setHkl_file(self, hkl_file):
        checkType("XSDataXscaleOutput", "setHkl_file", hkl_file, "XSDataString")
        self._hkl_file = hkl_file
    def delHkl_file(self): self._hkl_file = None
    # Properties
    hkl_file = property(getHkl_file, setHkl_file, delHkl_file, "Property for hkl_file")
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        checkType("XSDataXscaleOutput", "setLp_file", lp_file, "XSDataString")
        self._lp_file = lp_file
    def delLp_file(self): self._lp_file = None
    # Properties
    lp_file = property(getLp_file, setLp_file, delLp_file, "Property for lp_file")
    def export(self, outfile, level, name_='XSDataXscaleOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._succeeded is not None:
            self.succeeded.export(outfile, level, name_='succeeded')
        else:
            warnEmptyAttribute("succeeded", "XSDataBoolean")
        if self._hkl_file is not None:
            self.hkl_file.export(outfile, level, name_='hkl_file')
        if self._lp_file is not None:
            self.lp_file.export(outfile, level, name_='lp_file')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'succeeded':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setSucceeded(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_file(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleOutput

class XSDataXscaleParsingInput(XSDataInput):
    def __init__(self, configuration=None, lp_file=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataXscaleParsingInput", "Constructor of XSDataXscaleParsingInput", lp_file, "XSDataString")
        self._lp_file = lp_file
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        checkType("XSDataXscaleParsingInput", "setLp_file", lp_file, "XSDataString")
        self._lp_file = lp_file
    def delLp_file(self): self._lp_file = None
    # Properties
    lp_file = property(getLp_file, setLp_file, delLp_file, "Property for lp_file")
    def export(self, outfile, level, name_='XSDataXscaleParsingInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleParsingInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._lp_file is not None:
            self.lp_file.export(outfile, level, name_='lp_file')
        else:
            warnEmptyAttribute("lp_file", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleParsingInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleParsingInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleParsingInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleParsingInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsingInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleParsingInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsingInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleParsingInput

class XSDataAutoprocInput(XSDataAutoprocMasterInput):
    def __init__(self, configuration=None, low_resolution_limit=None, detector_max_res=None, data_collection_id=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, input_file=None, output_file=None):
        XSDataAutoprocMasterInput.__init__(self, configuration, low_resolution_limit, detector_max_res, data_collection_id, cc_half_cutoff, r_value_cutoff, isig_cutoff, completeness_cutoff, res_override, input_file)
    
    
        checkType("XSDataAutoprocInput", "Constructor of XSDataAutoprocInput", output_file, "XSDataFile")
        self._output_file = output_file
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        checkType("XSDataAutoprocInput", "setOutput_file", output_file, "XSDataFile")
        self._output_file = output_file
    def delOutput_file(self): self._output_file = None
    # Properties
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataAutoprocInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoprocInput'):
        XSDataAutoprocMasterInput.exportChildren(self, outfile, level, name_)
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataAutoprocMasterInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoprocInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoprocInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoprocInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoprocInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoprocInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoprocInput



# End of data representation classes.



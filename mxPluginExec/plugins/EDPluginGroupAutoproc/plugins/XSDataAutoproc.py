#!/usr/bin/env python

#
# Generated Thu Jan 31 02:24::34 2013 by EDGenerateDS.
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
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
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



class XSData2DCoordinates(object):
    def __init__(self, y=None, x=None):
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataFloat":
            self._x = x
        else:
            strMessage = "ERROR! XSData2DCoordinates constructor argument 'x' is not XSDataFloat but %s" % self._x.__class__.__name__
            raise BaseException(strMessage)
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataFloat":
            self._y = y
        else:
            strMessage = "ERROR! XSData2DCoordinates constructor argument 'y' is not XSDataFloat but %s" % self._y.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'x' attribute
    def getX(self): return self._x
    def setX(self, x):
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataFloat":
            self._x = x
        else:
            strMessage = "ERROR! XSData2DCoordinates.setX argument is not XSDataFloat but %s" % x.__class__.__name__
            raise BaseException(strMessage)
    def delX(self): self._x = None
    x = property(getX, setX, delX, "Property for x")
    # Methods and properties for the 'y' attribute
    def getY(self): return self._y
    def setY(self, y):
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataFloat":
            self._y = y
        else:
            strMessage = "ERROR! XSData2DCoordinates.setY argument is not XSDataFloat but %s" % y.__class__.__name__
            raise BaseException(strMessage)
    def delY(self): self._y = None
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


class XSDataRange(object):
    def __init__(self, end=None, begin=None):
        if begin is None:
            self._begin = None
        else:
            self._begin = int(begin)
        if end is None:
            self._end = None
        else:
            self._end = int(end)
    # Methods and properties for the 'begin' attribute
    def getBegin(self): return self._begin
    def setBegin(self, begin):
        if begin is None:
            self._begin = None
        else:
            self._begin = int(begin)
    def delBegin(self): self._begin = None
    begin = property(getBegin, setBegin, delBegin, "Property for begin")
    # Methods and properties for the 'end' attribute
    def getEnd(self): return self._end
    def setEnd(self, end):
        if end is None:
            self._end = None
        else:
            self._end = int(end)
    def delEnd(self): self._end = None
    end = property(getEnd, setEnd, delEnd, "Property for end")
    def export(self, outfile, level, name_='XSDataRange'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataRange'):
        pass
        if self._begin is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<begin>%d</begin>\n' % self._begin))
        else:
            warnEmptyAttribute("begin", "integer")
        if self._end is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<end>%d</end>\n' % self._end))
        else:
            warnEmptyAttribute("end", "integer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'begin':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._begin = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._end = ival_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataRange" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataRange' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataRange is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataRange.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRange()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataRange" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRange()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataRange


class XSDataXdsCompletenessEntry(object):
    def __init__(self, half_dataset_correlation=None, outer_isig=None, outer_rfactor=None, outer_complete=None, outer_possible=None, outer_unique=None, outer_observed=None, outer_res=None):
        if outer_res is None:
            self._outer_res = None
        elif outer_res.__class__.__name__ == "XSDataFloat":
            self._outer_res = outer_res
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_res' is not XSDataFloat but %s" % self._outer_res.__class__.__name__
            raise BaseException(strMessage)
        if outer_observed is None:
            self._outer_observed = None
        elif outer_observed.__class__.__name__ == "XSDataFloat":
            self._outer_observed = outer_observed
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_observed' is not XSDataFloat but %s" % self._outer_observed.__class__.__name__
            raise BaseException(strMessage)
        if outer_unique is None:
            self._outer_unique = None
        elif outer_unique.__class__.__name__ == "XSDataFloat":
            self._outer_unique = outer_unique
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_unique' is not XSDataFloat but %s" % self._outer_unique.__class__.__name__
            raise BaseException(strMessage)
        if outer_possible is None:
            self._outer_possible = None
        elif outer_possible.__class__.__name__ == "XSDataFloat":
            self._outer_possible = outer_possible
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_possible' is not XSDataFloat but %s" % self._outer_possible.__class__.__name__
            raise BaseException(strMessage)
        if outer_complete is None:
            self._outer_complete = None
        elif outer_complete.__class__.__name__ == "XSDataFloat":
            self._outer_complete = outer_complete
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_complete' is not XSDataFloat but %s" % self._outer_complete.__class__.__name__
            raise BaseException(strMessage)
        if outer_rfactor is None:
            self._outer_rfactor = None
        elif outer_rfactor.__class__.__name__ == "XSDataFloat":
            self._outer_rfactor = outer_rfactor
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_rfactor' is not XSDataFloat but %s" % self._outer_rfactor.__class__.__name__
            raise BaseException(strMessage)
        if outer_isig is None:
            self._outer_isig = None
        elif outer_isig.__class__.__name__ == "XSDataFloat":
            self._outer_isig = outer_isig
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'outer_isig' is not XSDataFloat but %s" % self._outer_isig.__class__.__name__
            raise BaseException(strMessage)
        if half_dataset_correlation is None:
            self._half_dataset_correlation = None
        elif half_dataset_correlation.__class__.__name__ == "XSDataFloat":
            self._half_dataset_correlation = half_dataset_correlation
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'half_dataset_correlation' is not XSDataFloat but %s" % self._half_dataset_correlation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outer_res' attribute
    def getOuter_res(self): return self._outer_res
    def setOuter_res(self, outer_res):
        if outer_res is None:
            self._outer_res = None
        elif outer_res.__class__.__name__ == "XSDataFloat":
            self._outer_res = outer_res
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_res argument is not XSDataFloat but %s" % outer_res.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_res(self): self._outer_res = None
    outer_res = property(getOuter_res, setOuter_res, delOuter_res, "Property for outer_res")
    # Methods and properties for the 'outer_observed' attribute
    def getOuter_observed(self): return self._outer_observed
    def setOuter_observed(self, outer_observed):
        if outer_observed is None:
            self._outer_observed = None
        elif outer_observed.__class__.__name__ == "XSDataFloat":
            self._outer_observed = outer_observed
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_observed argument is not XSDataFloat but %s" % outer_observed.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_observed(self): self._outer_observed = None
    outer_observed = property(getOuter_observed, setOuter_observed, delOuter_observed, "Property for outer_observed")
    # Methods and properties for the 'outer_unique' attribute
    def getOuter_unique(self): return self._outer_unique
    def setOuter_unique(self, outer_unique):
        if outer_unique is None:
            self._outer_unique = None
        elif outer_unique.__class__.__name__ == "XSDataFloat":
            self._outer_unique = outer_unique
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_unique argument is not XSDataFloat but %s" % outer_unique.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_unique(self): self._outer_unique = None
    outer_unique = property(getOuter_unique, setOuter_unique, delOuter_unique, "Property for outer_unique")
    # Methods and properties for the 'outer_possible' attribute
    def getOuter_possible(self): return self._outer_possible
    def setOuter_possible(self, outer_possible):
        if outer_possible is None:
            self._outer_possible = None
        elif outer_possible.__class__.__name__ == "XSDataFloat":
            self._outer_possible = outer_possible
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_possible argument is not XSDataFloat but %s" % outer_possible.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_possible(self): self._outer_possible = None
    outer_possible = property(getOuter_possible, setOuter_possible, delOuter_possible, "Property for outer_possible")
    # Methods and properties for the 'outer_complete' attribute
    def getOuter_complete(self): return self._outer_complete
    def setOuter_complete(self, outer_complete):
        if outer_complete is None:
            self._outer_complete = None
        elif outer_complete.__class__.__name__ == "XSDataFloat":
            self._outer_complete = outer_complete
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_complete argument is not XSDataFloat but %s" % outer_complete.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_complete(self): self._outer_complete = None
    outer_complete = property(getOuter_complete, setOuter_complete, delOuter_complete, "Property for outer_complete")
    # Methods and properties for the 'outer_rfactor' attribute
    def getOuter_rfactor(self): return self._outer_rfactor
    def setOuter_rfactor(self, outer_rfactor):
        if outer_rfactor is None:
            self._outer_rfactor = None
        elif outer_rfactor.__class__.__name__ == "XSDataFloat":
            self._outer_rfactor = outer_rfactor
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_rfactor argument is not XSDataFloat but %s" % outer_rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_rfactor(self): self._outer_rfactor = None
    outer_rfactor = property(getOuter_rfactor, setOuter_rfactor, delOuter_rfactor, "Property for outer_rfactor")
    # Methods and properties for the 'outer_isig' attribute
    def getOuter_isig(self): return self._outer_isig
    def setOuter_isig(self, outer_isig):
        if outer_isig is None:
            self._outer_isig = None
        elif outer_isig.__class__.__name__ == "XSDataFloat":
            self._outer_isig = outer_isig
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setOuter_isig argument is not XSDataFloat but %s" % outer_isig.__class__.__name__
            raise BaseException(strMessage)
    def delOuter_isig(self): self._outer_isig = None
    outer_isig = property(getOuter_isig, setOuter_isig, delOuter_isig, "Property for outer_isig")
    # Methods and properties for the 'half_dataset_correlation' attribute
    def getHalf_dataset_correlation(self): return self._half_dataset_correlation
    def setHalf_dataset_correlation(self, half_dataset_correlation):
        if half_dataset_correlation is None:
            self._half_dataset_correlation = None
        elif half_dataset_correlation.__class__.__name__ == "XSDataFloat":
            self._half_dataset_correlation = half_dataset_correlation
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setHalf_dataset_correlation argument is not XSDataFloat but %s" % half_dataset_correlation.__class__.__name__
            raise BaseException(strMessage)
    def delHalf_dataset_correlation(self): self._half_dataset_correlation = None
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
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataFloat":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataXscaleCompletenessEntry constructor argument 'multiplicity' is not XSDataFloat but %s" % self._multiplicity.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataFloat":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataXscaleCompletenessEntry.setMultiplicity argument is not XSDataFloat but %s" % multiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delMultiplicity(self): self._multiplicity = None
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


class XSDataAimless(XSDataInput):
    def __init__(self, configuration=None, anom=None, res=None, end_image=None, start_image=None, dataCollectionID=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAimless.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAimless.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAimless.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionID(self): self._dataCollectionID = None
    dataCollectionID = property(getDataCollectionID, setDataCollectionID, delDataCollectionID, "Property for dataCollectionID")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAimless.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
            raise BaseException(strMessage)
    def delStart_image(self): self._start_image = None
    start_image = property(getStart_image, setStart_image, delStart_image, "Property for start_image")
    # Methods and properties for the 'end_image' attribute
    def getEnd_image(self): return self._end_image
    def setEnd_image(self, end_image):
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAimless.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAimless.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'anom' attribute
    def getAnom(self): return self._anom
    def setAnom(self, anom):
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataAimless.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    def export(self, outfile, level, name_='XSDataAimless'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAimless'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
        if self._dataCollectionID is not None:
            self.dataCollectionID.export(outfile, level, name_='dataCollectionID')
        else:
            warnEmptyAttribute("dataCollectionID", "XSDataInteger")
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        else:
            warnEmptyAttribute("start_image", "XSDataInteger")
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
        else:
            warnEmptyAttribute("end_image", "XSDataInteger")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataFloat")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
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
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionID':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionID(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStart_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEnd_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnom(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAimless" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAimless' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAimless is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAimless.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAimless()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAimless" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAimless()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAimless


class XSDataAutoprocImport(XSDataInput):
    def __init__(self, configuration=None, image_prefix=None, nres=None, res=None, end_image=None, start_image=None, dataCollectionID=None, output_directory=None, input_noanom=None, input_anom=None):
        XSDataInput.__init__(self, configuration)
        if input_anom is None:
            self._input_anom = None
        elif input_anom.__class__.__name__ == "XSDataString":
            self._input_anom = input_anom
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'input_anom' is not XSDataString but %s" % self._input_anom.__class__.__name__
            raise BaseException(strMessage)
        if input_noanom is None:
            self._input_noanom = None
        elif input_noanom.__class__.__name__ == "XSDataString":
            self._input_noanom = input_noanom
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'input_noanom' is not XSDataString but %s" % self._input_noanom.__class__.__name__
            raise BaseException(strMessage)
        if output_directory is None:
            self._output_directory = None
        elif output_directory.__class__.__name__ == "XSDataString":
            self._output_directory = output_directory
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'output_directory' is not XSDataString but %s" % self._output_directory.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'nres' is not XSDataFloat but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataAutoprocImport constructor argument 'image_prefix' is not XSDataString but %s" % self._image_prefix.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_anom' attribute
    def getInput_anom(self): return self._input_anom
    def setInput_anom(self, input_anom):
        if input_anom is None:
            self._input_anom = None
        elif input_anom.__class__.__name__ == "XSDataString":
            self._input_anom = input_anom
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setInput_anom argument is not XSDataString but %s" % input_anom.__class__.__name__
            raise BaseException(strMessage)
    def delInput_anom(self): self._input_anom = None
    input_anom = property(getInput_anom, setInput_anom, delInput_anom, "Property for input_anom")
    # Methods and properties for the 'input_noanom' attribute
    def getInput_noanom(self): return self._input_noanom
    def setInput_noanom(self, input_noanom):
        if input_noanom is None:
            self._input_noanom = None
        elif input_noanom.__class__.__name__ == "XSDataString":
            self._input_noanom = input_noanom
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setInput_noanom argument is not XSDataString but %s" % input_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delInput_noanom(self): self._input_noanom = None
    input_noanom = property(getInput_noanom, setInput_noanom, delInput_noanom, "Property for input_noanom")
    # Methods and properties for the 'output_directory' attribute
    def getOutput_directory(self): return self._output_directory
    def setOutput_directory(self, output_directory):
        if output_directory is None:
            self._output_directory = None
        elif output_directory.__class__.__name__ == "XSDataString":
            self._output_directory = output_directory
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setOutput_directory argument is not XSDataString but %s" % output_directory.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_directory(self): self._output_directory = None
    output_directory = property(getOutput_directory, setOutput_directory, delOutput_directory, "Property for output_directory")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionID(self): self._dataCollectionID = None
    dataCollectionID = property(getDataCollectionID, setDataCollectionID, delDataCollectionID, "Property for dataCollectionID")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
            raise BaseException(strMessage)
    def delStart_image(self): self._start_image = None
    start_image = property(getStart_image, setStart_image, delStart_image, "Property for start_image")
    # Methods and properties for the 'end_image' attribute
    def getEnd_image(self): return self._end_image
    def setEnd_image(self, end_image):
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setNres argument is not XSDataFloat but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'image_prefix' attribute
    def getImage_prefix(self): return self._image_prefix
    def setImage_prefix(self, image_prefix):
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataAutoprocImport.setImage_prefix argument is not XSDataString but %s" % image_prefix.__class__.__name__
            raise BaseException(strMessage)
    def delImage_prefix(self): self._image_prefix = None
    image_prefix = property(getImage_prefix, setImage_prefix, delImage_prefix, "Property for image_prefix")
    def export(self, outfile, level, name_='XSDataAutoprocImport'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoprocImport'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_anom is not None:
            self.input_anom.export(outfile, level, name_='input_anom')
        else:
            warnEmptyAttribute("input_anom", "XSDataString")
        if self._input_noanom is not None:
            self.input_noanom.export(outfile, level, name_='input_noanom')
        else:
            warnEmptyAttribute("input_noanom", "XSDataString")
        if self._output_directory is not None:
            self.output_directory.export(outfile, level, name_='output_directory')
        else:
            warnEmptyAttribute("output_directory", "XSDataString")
        if self._dataCollectionID is not None:
            self.dataCollectionID.export(outfile, level, name_='dataCollectionID')
        else:
            warnEmptyAttribute("dataCollectionID", "XSDataInteger")
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        else:
            warnEmptyAttribute("start_image", "XSDataInteger")
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
        else:
            warnEmptyAttribute("end_image", "XSDataInteger")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataFloat")
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataFloat")
        if self._image_prefix is not None:
            self.image_prefix.export(outfile, level, name_='image_prefix')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_noanom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_directory':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_directory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionID':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionID(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStart_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEnd_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image_prefix':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImage_prefix(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoprocImport" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoprocImport' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoprocImport is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoprocImport.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocImport()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoprocImport" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocImport()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoprocImport


class XSDataAutoprocImportOut(XSDataResult):
    def __init__(self, status=None, files=None):
        XSDataResult.__init__(self, status)
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataAutoprocImportOut constructor argument 'files' is not list but %s" % self._files.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'files' attribute
    def getFiles(self): return self._files
    def setFiles(self, files):
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataAutoprocImportOut.setFiles argument is not list but %s" % files.__class__.__name__
            raise BaseException(strMessage)
    def delFiles(self): self._files = None
    files = property(getFiles, setFiles, delFiles, "Property for files")
    def addFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataAutoprocImportOut.addFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._files.append(value)
        else:
            strMessage = "ERROR! XSDataAutoprocImportOut.addFiles argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataAutoprocImportOut.insertFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataAutoprocImportOut.insertFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._files[index] = value
        else:
            strMessage = "ERROR! XSDataAutoprocImportOut.addFiles argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataAutoprocImportOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoprocImportOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for files_ in self.getFiles():
            files_.export(outfile, level, name_='files')
        if self.getFiles() == []:
            warnEmptyAttribute("files", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'files':
            obj_ = XSDataString()
            obj_.build(child_)
            self.files.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoprocImportOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoprocImportOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoprocImportOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoprocImportOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocImportOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoprocImportOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoprocImportOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoprocImportOut


class XSDataAutoprocInput(XSDataInput):
    def __init__(self, configuration=None, output_file=None, unit_cell=None, spacegroup=None, nres=None, low_resolution_limit=None, detector_max_res=None, data_collection_id=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataFile":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'input_file' is not XSDataFile but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataFloat":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'res_override' is not XSDataFloat but %s" % self._res_override.__class__.__name__
            raise BaseException(strMessage)
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataFloat":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'completeness_cutoff' is not XSDataFloat but %s" % self._completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataFloat":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'isig_cutoff' is not XSDataFloat but %s" % self._isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataFloat":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'r_value_cutoff' is not XSDataFloat but %s" % self._r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataFloat":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'cc_half_cutoff' is not XSDataFloat but %s" % self._cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if data_collection_id is None:
            self._data_collection_id = None
        elif data_collection_id.__class__.__name__ == "XSDataInteger":
            self._data_collection_id = data_collection_id
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'data_collection_id' is not XSDataInteger but %s" % self._data_collection_id.__class__.__name__
            raise BaseException(strMessage)
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataFloat":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'detector_max_res' is not XSDataFloat but %s" % self._detector_max_res.__class__.__name__
            raise BaseException(strMessage)
        if low_resolution_limit is None:
            self._low_resolution_limit = None
        elif low_resolution_limit.__class__.__name__ == "XSDataFloat":
            self._low_resolution_limit = low_resolution_limit
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'low_resolution_limit' is not XSDataFloat but %s" % self._low_resolution_limit.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'nres' is not XSDataFloat but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'spacegroup' is not XSDataInteger but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'unit_cell' is not XSDataString but %s" % self._unit_cell.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataFile":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAutoprocInput constructor argument 'output_file' is not XSDataFile but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataFile":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setInput_file argument is not XSDataFile but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'res_override' attribute
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataFloat":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setRes_override argument is not XSDataFloat but %s" % res_override.__class__.__name__
            raise BaseException(strMessage)
    def delRes_override(self): self._res_override = None
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    # Methods and properties for the 'completeness_cutoff' attribute
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataFloat":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setCompleteness_cutoff argument is not XSDataFloat but %s" % completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    # Methods and properties for the 'isig_cutoff' attribute
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataFloat":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setIsig_cutoff argument is not XSDataFloat but %s" % isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delIsig_cutoff(self): self._isig_cutoff = None
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    # Methods and properties for the 'r_value_cutoff' attribute
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataFloat":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setR_value_cutoff argument is not XSDataFloat but %s" % r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delR_value_cutoff(self): self._r_value_cutoff = None
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    # Methods and properties for the 'cc_half_cutoff' attribute
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataFloat":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setCc_half_cutoff argument is not XSDataFloat but %s" % cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
    cc_half_cutoff = property(getCc_half_cutoff, setCc_half_cutoff, delCc_half_cutoff, "Property for cc_half_cutoff")
    # Methods and properties for the 'data_collection_id' attribute
    def getData_collection_id(self): return self._data_collection_id
    def setData_collection_id(self, data_collection_id):
        if data_collection_id is None:
            self._data_collection_id = None
        elif data_collection_id.__class__.__name__ == "XSDataInteger":
            self._data_collection_id = data_collection_id
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setData_collection_id argument is not XSDataInteger but %s" % data_collection_id.__class__.__name__
            raise BaseException(strMessage)
    def delData_collection_id(self): self._data_collection_id = None
    data_collection_id = property(getData_collection_id, setData_collection_id, delData_collection_id, "Property for data_collection_id")
    # Methods and properties for the 'detector_max_res' attribute
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataFloat":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setDetector_max_res argument is not XSDataFloat but %s" % detector_max_res.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_max_res(self): self._detector_max_res = None
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    # Methods and properties for the 'low_resolution_limit' attribute
    def getLow_resolution_limit(self): return self._low_resolution_limit
    def setLow_resolution_limit(self, low_resolution_limit):
        if low_resolution_limit is None:
            self._low_resolution_limit = None
        elif low_resolution_limit.__class__.__name__ == "XSDataFloat":
            self._low_resolution_limit = low_resolution_limit
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setLow_resolution_limit argument is not XSDataFloat but %s" % low_resolution_limit.__class__.__name__
            raise BaseException(strMessage)
    def delLow_resolution_limit(self): self._low_resolution_limit = None
    low_resolution_limit = property(getLow_resolution_limit, setLow_resolution_limit, delLow_resolution_limit, "Property for low_resolution_limit")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setNres argument is not XSDataFloat but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setSpacegroup argument is not XSDataInteger but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    # Methods and properties for the 'unit_cell' attribute
    def getUnit_cell(self): return self._unit_cell
    def setUnit_cell(self, unit_cell):
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setUnit_cell argument is not XSDataString but %s" % unit_cell.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell(self): self._unit_cell = None
    unit_cell = property(getUnit_cell, setUnit_cell, delUnit_cell, "Property for unit_cell")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataFile":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAutoprocInput.setOutput_file argument is not XSDataFile but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataAutoprocInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoprocInput'):
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
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
        if self._unit_cell is not None:
            self.unit_cell.export(outfile, level, name_='unit_cell')
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit_cell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
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


class XSDataFileConversion(XSDataInput):
    def __init__(self, configuration=None, image_prefix=None, anom=None, nres=None, res=None, end_image=None, start_image=None, dataCollectionID=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'nres' is not XSDataFloat but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'image_prefix' is not XSDataString but %s" % self._image_prefix.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataFileConversion.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataFileConversion.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataFileConversion.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionID(self): self._dataCollectionID = None
    dataCollectionID = property(getDataCollectionID, setDataCollectionID, delDataCollectionID, "Property for dataCollectionID")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataFileConversion.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
            raise BaseException(strMessage)
    def delStart_image(self): self._start_image = None
    start_image = property(getStart_image, setStart_image, delStart_image, "Property for start_image")
    # Methods and properties for the 'end_image' attribute
    def getEnd_image(self): return self._end_image
    def setEnd_image(self, end_image):
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataFileConversion.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataFileConversion.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataFileConversion.setNres argument is not XSDataFloat but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'anom' attribute
    def getAnom(self): return self._anom
    def setAnom(self, anom):
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataFileConversion.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    # Methods and properties for the 'image_prefix' attribute
    def getImage_prefix(self): return self._image_prefix
    def setImage_prefix(self, image_prefix):
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataFileConversion.setImage_prefix argument is not XSDataString but %s" % image_prefix.__class__.__name__
            raise BaseException(strMessage)
    def delImage_prefix(self): self._image_prefix = None
    image_prefix = property(getImage_prefix, setImage_prefix, delImage_prefix, "Property for image_prefix")
    def export(self, outfile, level, name_='XSDataFileConversion'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataFileConversion'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
        if self._dataCollectionID is not None:
            self.dataCollectionID.export(outfile, level, name_='dataCollectionID')
        else:
            warnEmptyAttribute("dataCollectionID", "XSDataInteger")
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        else:
            warnEmptyAttribute("start_image", "XSDataInteger")
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
        else:
            warnEmptyAttribute("end_image", "XSDataInteger")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataFloat")
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataFloat")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
        if self._image_prefix is not None:
            self.image_prefix.export(outfile, level, name_='image_prefix')
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
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionID':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionID(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStart_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEnd_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image_prefix':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImage_prefix(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataFileConversion" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataFileConversion' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataFileConversion is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataFileConversion.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversion()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataFileConversion" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversion()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataFileConversion


class XSDataMatthewsCoeffIn(XSDataInput):
    def __init__(self, configuration=None, symm=None, gamma=None, beta=None, alpha=None, c=None, b=None, a=None):
        XSDataInput.__init__(self, configuration)
        if a is None:
            self._a = None
        elif a.__class__.__name__ == "XSDataDouble":
            self._a = a
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'a' is not XSDataDouble but %s" % self._a.__class__.__name__
            raise BaseException(strMessage)
        if b is None:
            self._b = None
        elif b.__class__.__name__ == "XSDataDouble":
            self._b = b
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'b' is not XSDataDouble but %s" % self._b.__class__.__name__
            raise BaseException(strMessage)
        if c is None:
            self._c = None
        elif c.__class__.__name__ == "XSDataDouble":
            self._c = c
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'c' is not XSDataDouble but %s" % self._c.__class__.__name__
            raise BaseException(strMessage)
        if alpha is None:
            self._alpha = None
        elif alpha.__class__.__name__ == "XSDataDouble":
            self._alpha = alpha
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'alpha' is not XSDataDouble but %s" % self._alpha.__class__.__name__
            raise BaseException(strMessage)
        if beta is None:
            self._beta = None
        elif beta.__class__.__name__ == "XSDataDouble":
            self._beta = beta
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'beta' is not XSDataDouble but %s" % self._beta.__class__.__name__
            raise BaseException(strMessage)
        if gamma is None:
            self._gamma = None
        elif gamma.__class__.__name__ == "XSDataDouble":
            self._gamma = gamma
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'gamma' is not XSDataDouble but %s" % self._gamma.__class__.__name__
            raise BaseException(strMessage)
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn constructor argument 'symm' is not XSDataString but %s" % self._symm.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'a' attribute
    def getA(self): return self._a
    def setA(self, a):
        if a is None:
            self._a = None
        elif a.__class__.__name__ == "XSDataDouble":
            self._a = a
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setA argument is not XSDataDouble but %s" % a.__class__.__name__
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
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setB argument is not XSDataDouble but %s" % b.__class__.__name__
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
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setC argument is not XSDataDouble but %s" % c.__class__.__name__
            raise BaseException(strMessage)
    def delC(self): self._c = None
    c = property(getC, setC, delC, "Property for c")
    # Methods and properties for the 'alpha' attribute
    def getAlpha(self): return self._alpha
    def setAlpha(self, alpha):
        if alpha is None:
            self._alpha = None
        elif alpha.__class__.__name__ == "XSDataDouble":
            self._alpha = alpha
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setAlpha argument is not XSDataDouble but %s" % alpha.__class__.__name__
            raise BaseException(strMessage)
    def delAlpha(self): self._alpha = None
    alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
    # Methods and properties for the 'beta' attribute
    def getBeta(self): return self._beta
    def setBeta(self, beta):
        if beta is None:
            self._beta = None
        elif beta.__class__.__name__ == "XSDataDouble":
            self._beta = beta
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setBeta argument is not XSDataDouble but %s" % beta.__class__.__name__
            raise BaseException(strMessage)
    def delBeta(self): self._beta = None
    beta = property(getBeta, setBeta, delBeta, "Property for beta")
    # Methods and properties for the 'gamma' attribute
    def getGamma(self): return self._gamma
    def setGamma(self, gamma):
        if gamma is None:
            self._gamma = None
        elif gamma.__class__.__name__ == "XSDataDouble":
            self._gamma = gamma
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setGamma argument is not XSDataDouble but %s" % gamma.__class__.__name__
            raise BaseException(strMessage)
    def delGamma(self): self._gamma = None
    gamma = property(getGamma, setGamma, delGamma, "Property for gamma")
    # Methods and properties for the 'symm' attribute
    def getSymm(self): return self._symm
    def setSymm(self, symm):
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffIn.setSymm argument is not XSDataString but %s" % symm.__class__.__name__
            raise BaseException(strMessage)
    def delSymm(self): self._symm = None
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
        if best_p is None:
            self._best_p = None
        elif best_p.__class__.__name__ == "XSDataDouble":
            self._best_p = best_p
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffOut constructor argument 'best_p' is not XSDataDouble but %s" % self._best_p.__class__.__name__
            raise BaseException(strMessage)
        if best_sol is None:
            self._best_sol = None
        elif best_sol.__class__.__name__ == "XSDataString":
            self._best_sol = best_sol
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffOut constructor argument 'best_sol' is not XSDataString but %s" % self._best_sol.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'best_p' attribute
    def getBest_p(self): return self._best_p
    def setBest_p(self, best_p):
        if best_p is None:
            self._best_p = None
        elif best_p.__class__.__name__ == "XSDataDouble":
            self._best_p = best_p
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffOut.setBest_p argument is not XSDataDouble but %s" % best_p.__class__.__name__
            raise BaseException(strMessage)
    def delBest_p(self): self._best_p = None
    best_p = property(getBest_p, setBest_p, delBest_p, "Property for best_p")
    # Methods and properties for the 'best_sol' attribute
    def getBest_sol(self): return self._best_sol
    def setBest_sol(self, best_sol):
        if best_sol is None:
            self._best_sol = None
        elif best_sol.__class__.__name__ == "XSDataString":
            self._best_sol = best_sol
        else:
            strMessage = "ERROR! XSDataMatthewsCoeffOut.setBest_sol argument is not XSDataString but %s" % best_sol.__class__.__name__
            raise BaseException(strMessage)
    def delBest_sol(self): self._best_sol = None
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
    def __init__(self, configuration=None, unit_cell=None, spacegroup=None, spot_range=None, resolution_range=None, friedels_law=None, maxjobs=None, maxproc=None, job=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if job is None:
            self._job = None
        elif job.__class__.__name__ == "XSDataString":
            self._job = job
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'job' is not XSDataString but %s" % self._job.__class__.__name__
            raise BaseException(strMessage)
        if maxproc is None:
            self._maxproc = None
        elif maxproc.__class__.__name__ == "XSDataInteger":
            self._maxproc = maxproc
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'maxproc' is not XSDataInteger but %s" % self._maxproc.__class__.__name__
            raise BaseException(strMessage)
        if maxjobs is None:
            self._maxjobs = None
        elif maxjobs.__class__.__name__ == "XSDataInteger":
            self._maxjobs = maxjobs
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'maxjobs' is not XSDataInteger but %s" % self._maxjobs.__class__.__name__
            raise BaseException(strMessage)
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'friedels_law' is not XSDataBoolean but %s" % self._friedels_law.__class__.__name__
            raise BaseException(strMessage)
        if resolution_range is None:
            self._resolution_range = []
        elif resolution_range.__class__.__name__ == "list":
            self._resolution_range = resolution_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'resolution_range' is not list but %s" % self._resolution_range.__class__.__name__
            raise BaseException(strMessage)
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'spot_range' is not list but %s" % self._spot_range.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'spacegroup' is not XSDataInteger but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'unit_cell' is not XSDataString but %s" % self._unit_cell.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'job' attribute
    def getJob(self): return self._job
    def setJob(self, job):
        if job is None:
            self._job = None
        elif job.__class__.__name__ == "XSDataString":
            self._job = job
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setJob argument is not XSDataString but %s" % job.__class__.__name__
            raise BaseException(strMessage)
    def delJob(self): self._job = None
    job = property(getJob, setJob, delJob, "Property for job")
    # Methods and properties for the 'maxproc' attribute
    def getMaxproc(self): return self._maxproc
    def setMaxproc(self, maxproc):
        if maxproc is None:
            self._maxproc = None
        elif maxproc.__class__.__name__ == "XSDataInteger":
            self._maxproc = maxproc
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setMaxproc argument is not XSDataInteger but %s" % maxproc.__class__.__name__
            raise BaseException(strMessage)
    def delMaxproc(self): self._maxproc = None
    maxproc = property(getMaxproc, setMaxproc, delMaxproc, "Property for maxproc")
    # Methods and properties for the 'maxjobs' attribute
    def getMaxjobs(self): return self._maxjobs
    def setMaxjobs(self, maxjobs):
        if maxjobs is None:
            self._maxjobs = None
        elif maxjobs.__class__.__name__ == "XSDataInteger":
            self._maxjobs = maxjobs
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setMaxjobs argument is not XSDataInteger but %s" % maxjobs.__class__.__name__
            raise BaseException(strMessage)
    def delMaxjobs(self): self._maxjobs = None
    maxjobs = property(getMaxjobs, setMaxjobs, delMaxjobs, "Property for maxjobs")
    # Methods and properties for the 'friedels_law' attribute
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setFriedels_law argument is not XSDataBoolean but %s" % friedels_law.__class__.__name__
            raise BaseException(strMessage)
    def delFriedels_law(self): self._friedels_law = None
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    # Methods and properties for the 'resolution_range' attribute
    def getResolution_range(self): return self._resolution_range
    def setResolution_range(self, resolution_range):
        if resolution_range is None:
            self._resolution_range = []
        elif resolution_range.__class__.__name__ == "list":
            self._resolution_range = resolution_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setResolution_range argument is not list but %s" % resolution_range.__class__.__name__
            raise BaseException(strMessage)
    def delResolution_range(self): self._resolution_range = None
    resolution_range = property(getResolution_range, setResolution_range, delResolution_range, "Property for resolution_range")
    def addResolution_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._resolution_range.append(value)
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertResolution_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertResolution_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertResolution_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._resolution_range[index] = value
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spot_range' attribute
    def getSpot_range(self): return self._spot_range
    def setSpot_range(self, spot_range):
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setSpot_range argument is not list but %s" % spot_range.__class__.__name__
            raise BaseException(strMessage)
    def delSpot_range(self): self._spot_range = None
    spot_range = property(getSpot_range, setSpot_range, delSpot_range, "Property for spot_range")
    def addSpot_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._spot_range.append(value)
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSpot_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertSpot_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertSpot_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._spot_range[index] = value
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setSpacegroup argument is not XSDataInteger but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    # Methods and properties for the 'unit_cell' attribute
    def getUnit_cell(self): return self._unit_cell
    def setUnit_cell(self, unit_cell):
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setUnit_cell argument is not XSDataString but %s" % unit_cell.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell(self): self._unit_cell = None
    unit_cell = property(getUnit_cell, setUnit_cell, delUnit_cell, "Property for unit_cell")
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
        for spot_range_ in self.getSpot_range():
            spot_range_.export(outfile, level, name_='spot_range')
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
        if self._unit_cell is not None:
            self.unit_cell.export(outfile, level, name_='unit_cell')
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot_range':
            obj_ = XSDataRange()
            obj_.build(child_)
            self.spot_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit_cell(obj_)
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
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataMinimalXdsOut constructor argument 'succeeded' is not XSDataBoolean but %s" % self._succeeded.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'succeeded' attribute
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataMinimalXdsOut.setSucceeded argument is not XSDataBoolean but %s" % succeeded.__class__.__name__
            raise BaseException(strMessage)
    def delSucceeded(self): self._succeeded = None
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


class XSDataPointless(XSDataInput):
    def __init__(self, configuration=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataPointless constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataPointless constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataPointless.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataPointless.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataPointless'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPointless'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
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
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPointless" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPointless' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPointless is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPointless.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPointless()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPointless" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPointless()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPointless


class XSDataPointlessOut(XSDataResult):
    def __init__(self, status=None, sgstr=None, sgnumber=None):
        XSDataResult.__init__(self, status)
        if sgnumber is None:
            self._sgnumber = None
        elif sgnumber.__class__.__name__ == "XSDataInteger":
            self._sgnumber = sgnumber
        else:
            strMessage = "ERROR! XSDataPointlessOut constructor argument 'sgnumber' is not XSDataInteger but %s" % self._sgnumber.__class__.__name__
            raise BaseException(strMessage)
        if sgstr is None:
            self._sgstr = None
        elif sgstr.__class__.__name__ == "XSDataString":
            self._sgstr = sgstr
        else:
            strMessage = "ERROR! XSDataPointlessOut constructor argument 'sgstr' is not XSDataString but %s" % self._sgstr.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sgnumber' attribute
    def getSgnumber(self): return self._sgnumber
    def setSgnumber(self, sgnumber):
        if sgnumber is None:
            self._sgnumber = None
        elif sgnumber.__class__.__name__ == "XSDataInteger":
            self._sgnumber = sgnumber
        else:
            strMessage = "ERROR! XSDataPointlessOut.setSgnumber argument is not XSDataInteger but %s" % sgnumber.__class__.__name__
            raise BaseException(strMessage)
    def delSgnumber(self): self._sgnumber = None
    sgnumber = property(getSgnumber, setSgnumber, delSgnumber, "Property for sgnumber")
    # Methods and properties for the 'sgstr' attribute
    def getSgstr(self): return self._sgstr
    def setSgstr(self, sgstr):
        if sgstr is None:
            self._sgstr = None
        elif sgstr.__class__.__name__ == "XSDataString":
            self._sgstr = sgstr
        else:
            strMessage = "ERROR! XSDataPointlessOut.setSgstr argument is not XSDataString but %s" % sgstr.__class__.__name__
            raise BaseException(strMessage)
    def delSgstr(self): self._sgstr = None
    sgstr = property(getSgstr, setSgstr, delSgstr, "Property for sgstr")
    def export(self, outfile, level, name_='XSDataPointlessOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPointlessOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._sgnumber is not None:
            self.sgnumber.export(outfile, level, name_='sgnumber')
        if self._sgstr is not None:
            self.sgstr.export(outfile, level, name_='sgstr')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sgnumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSgnumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sgstr':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSgstr(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPointlessOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPointlessOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPointlessOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPointlessOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPointlessOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPointlessOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPointlessOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPointlessOut


class XSDataRBinsIn(XSDataInput):
    def __init__(self, configuration=None, high=None, low=None):
        XSDataInput.__init__(self, configuration)
        if low is None:
            self._low = None
        elif low.__class__.__name__ == "XSDataDouble":
            self._low = low
        else:
            strMessage = "ERROR! XSDataRBinsIn constructor argument 'low' is not XSDataDouble but %s" % self._low.__class__.__name__
            raise BaseException(strMessage)
        if high is None:
            self._high = None
        elif high.__class__.__name__ == "XSDataDouble":
            self._high = high
        else:
            strMessage = "ERROR! XSDataRBinsIn constructor argument 'high' is not XSDataDouble but %s" % self._high.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'low' attribute
    def getLow(self): return self._low
    def setLow(self, low):
        if low is None:
            self._low = None
        elif low.__class__.__name__ == "XSDataDouble":
            self._low = low
        else:
            strMessage = "ERROR! XSDataRBinsIn.setLow argument is not XSDataDouble but %s" % low.__class__.__name__
            raise BaseException(strMessage)
    def delLow(self): self._low = None
    low = property(getLow, setLow, delLow, "Property for low")
    # Methods and properties for the 'high' attribute
    def getHigh(self): return self._high
    def setHigh(self, high):
        if high is None:
            self._high = None
        elif high.__class__.__name__ == "XSDataDouble":
            self._high = high
        else:
            strMessage = "ERROR! XSDataRBinsIn.setHigh argument is not XSDataDouble but %s" % high.__class__.__name__
            raise BaseException(strMessage)
    def delHigh(self): self._high = None
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
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataRBinsOut constructor argument 'bins' is not list but %s" % self._bins.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bins' attribute
    def getBins(self): return self._bins
    def setBins(self, bins):
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataRBinsOut.setBins argument is not list but %s" % bins.__class__.__name__
            raise BaseException(strMessage)
    def delBins(self): self._bins = None
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        if value is None:
            strMessage = "ERROR! XSDataRBinsOut.addBins argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins.append(value)
        else:
            strMessage = "ERROR! XSDataRBinsOut.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBins(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataRBinsOut.insertBins argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataRBinsOut.insertBins argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins[index] = value
        else:
            strMessage = "ERROR! XSDataRBinsOut.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
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
        if xds_res is None:
            self._xds_res = None
        elif xds_res.__class__.__name__ == "XSDataXdsOutput":
            self._xds_res = xds_res
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'xds_res' is not XSDataXdsOutput but %s" % self._xds_res.__class__.__name__
            raise BaseException(strMessage)
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataFloat":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'detector_max_res' is not XSDataFloat but %s" % self._detector_max_res.__class__.__name__
            raise BaseException(strMessage)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'total_completeness' is not XSDataXdsCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataFloat":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'res_override' is not XSDataFloat but %s" % self._res_override.__class__.__name__
            raise BaseException(strMessage)
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataFloat":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'completeness_cutoff' is not XSDataFloat but %s" % self._completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataFloat":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'isig_cutoff' is not XSDataFloat but %s" % self._isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataFloat":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'r_value_cutoff' is not XSDataFloat but %s" % self._r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataFloat":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'cc_half_cutoff' is not XSDataFloat but %s" % self._cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'xds_res' attribute
    def getXds_res(self): return self._xds_res
    def setXds_res(self, xds_res):
        if xds_res is None:
            self._xds_res = None
        elif xds_res.__class__.__name__ == "XSDataXdsOutput":
            self._xds_res = xds_res
        else:
            strMessage = "ERROR! XSDataResCutoff.setXds_res argument is not XSDataXdsOutput but %s" % xds_res.__class__.__name__
            raise BaseException(strMessage)
    def delXds_res(self): self._xds_res = None
    xds_res = property(getXds_res, setXds_res, delXds_res, "Property for xds_res")
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataResCutoff.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResCutoff.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResCutoff.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector_max_res' attribute
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataFloat":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataResCutoff.setDetector_max_res argument is not XSDataFloat but %s" % detector_max_res.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_max_res(self): self._detector_max_res = None
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataResCutoff.setTotal_completeness argument is not XSDataXdsCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'res_override' attribute
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataFloat":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataResCutoff.setRes_override argument is not XSDataFloat but %s" % res_override.__class__.__name__
            raise BaseException(strMessage)
    def delRes_override(self): self._res_override = None
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    # Methods and properties for the 'completeness_cutoff' attribute
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataFloat":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setCompleteness_cutoff argument is not XSDataFloat but %s" % completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    # Methods and properties for the 'isig_cutoff' attribute
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataFloat":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setIsig_cutoff argument is not XSDataFloat but %s" % isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delIsig_cutoff(self): self._isig_cutoff = None
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    # Methods and properties for the 'r_value_cutoff' attribute
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataFloat":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setR_value_cutoff argument is not XSDataFloat but %s" % r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delR_value_cutoff(self): self._r_value_cutoff = None
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    # Methods and properties for the 'cc_half_cutoff' attribute
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataFloat":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setCc_half_cutoff argument is not XSDataFloat but %s" % cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
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
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'bins' is not list but %s" % self._bins.__class__.__name__
            raise BaseException(strMessage)
        if total_complete is None:
            self._total_complete = None
        elif total_complete.__class__.__name__ == "XSDataFloat":
            self._total_complete = total_complete
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_complete' is not XSDataFloat but %s" % self._total_complete.__class__.__name__
            raise BaseException(strMessage)
        if total_rfactor is None:
            self._total_rfactor = None
        elif total_rfactor.__class__.__name__ == "XSDataFloat":
            self._total_rfactor = total_rfactor
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_rfactor' is not XSDataFloat but %s" % self._total_rfactor.__class__.__name__
            raise BaseException(strMessage)
        if total_isig is None:
            self._total_isig = None
        elif total_isig.__class__.__name__ == "XSDataFloat":
            self._total_isig = total_isig
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_isig' is not XSDataFloat but %s" % self._total_isig.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'bins' attribute
    def getBins(self): return self._bins
    def setBins(self, bins):
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setBins argument is not list but %s" % bins.__class__.__name__
            raise BaseException(strMessage)
    def delBins(self): self._bins = None
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._bins.append(value)
        else:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBins(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResCutoffResult.insertBins argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResCutoffResult.insertBins argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._bins[index] = value
        else:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_complete' attribute
    def getTotal_complete(self): return self._total_complete
    def setTotal_complete(self, total_complete):
        if total_complete is None:
            self._total_complete = None
        elif total_complete.__class__.__name__ == "XSDataFloat":
            self._total_complete = total_complete
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_complete argument is not XSDataFloat but %s" % total_complete.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_complete(self): self._total_complete = None
    total_complete = property(getTotal_complete, setTotal_complete, delTotal_complete, "Property for total_complete")
    # Methods and properties for the 'total_rfactor' attribute
    def getTotal_rfactor(self): return self._total_rfactor
    def setTotal_rfactor(self, total_rfactor):
        if total_rfactor is None:
            self._total_rfactor = None
        elif total_rfactor.__class__.__name__ == "XSDataFloat":
            self._total_rfactor = total_rfactor
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_rfactor argument is not XSDataFloat but %s" % total_rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_rfactor(self): self._total_rfactor = None
    total_rfactor = property(getTotal_rfactor, setTotal_rfactor, delTotal_rfactor, "Property for total_rfactor")
    # Methods and properties for the 'total_isig' attribute
    def getTotal_isig(self): return self._total_isig
    def setTotal_isig(self, total_isig):
        if total_isig is None:
            self._total_isig = None
        elif total_isig.__class__.__name__ == "XSDataFloat":
            self._total_isig = total_isig
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_isig argument is not XSDataFloat but %s" % total_isig.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_isig(self): self._total_isig = None
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


class XSDataTruncate(XSDataInput):
    def __init__(self, configuration=None, res=None, anom=None, nres=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'nres' is not XSDataFloat but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataTruncate.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataTruncate.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataFloat":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataTruncate.setNres argument is not XSDataFloat but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'anom' attribute
    def getAnom(self): return self._anom
    def setAnom(self, anom):
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataTruncate.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataTruncate.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    def export(self, outfile, level, name_='XSDataTruncate'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataTruncate'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataFloat")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
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
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnom(obj_)
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
        self.export( oStreamString, 0, name_="XSDataTruncate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataTruncate' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataTruncate is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataTruncate.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataTruncate()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataTruncate" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataTruncate()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataTruncate


class XSDataUniqueify(XSDataInput):
    def __init__(self, configuration=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataUniqueify constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataUniqueify constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataUniqueify.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataUniqueify.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataUniqueify'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataUniqueify'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
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
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataUniqueify" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataUniqueify' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataUniqueify is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataUniqueify.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataUniqueify()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataUniqueify" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataUniqueify()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataUniqueify


class XSDataXdsGenerateInput(XSDataInput):
    def __init__(self, configuration=None, resolution=None, previous_run_dir=None):
        XSDataInput.__init__(self, configuration)
        if previous_run_dir is None:
            self._previous_run_dir = None
        elif previous_run_dir.__class__.__name__ == "XSDataString":
            self._previous_run_dir = previous_run_dir
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'previous_run_dir' is not XSDataString but %s" % self._previous_run_dir.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataFloat":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'resolution' is not XSDataFloat but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'previous_run_dir' attribute
    def getPrevious_run_dir(self): return self._previous_run_dir
    def setPrevious_run_dir(self, previous_run_dir):
        if previous_run_dir is None:
            self._previous_run_dir = None
        elif previous_run_dir.__class__.__name__ == "XSDataString":
            self._previous_run_dir = previous_run_dir
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setPrevious_run_dir argument is not XSDataString but %s" % previous_run_dir.__class__.__name__
            raise BaseException(strMessage)
    def delPrevious_run_dir(self): self._previous_run_dir = None
    previous_run_dir = property(getPrevious_run_dir, setPrevious_run_dir, delPrevious_run_dir, "Property for previous_run_dir")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataFloat":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setResolution argument is not XSDataFloat but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
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
        if hkl_anom is None:
            self._hkl_anom = None
        elif hkl_anom.__class__.__name__ == "XSDataString":
            self._hkl_anom = hkl_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'hkl_anom' is not XSDataString but %s" % self._hkl_anom.__class__.__name__
            raise BaseException(strMessage)
        if hkl_no_anom is None:
            self._hkl_no_anom = None
        elif hkl_no_anom.__class__.__name__ == "XSDataString":
            self._hkl_no_anom = hkl_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'hkl_no_anom' is not XSDataString but %s" % self._hkl_no_anom.__class__.__name__
            raise BaseException(strMessage)
        if correct_lp_anom is None:
            self._correct_lp_anom = None
        elif correct_lp_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_anom = correct_lp_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'correct_lp_anom' is not XSDataString but %s" % self._correct_lp_anom.__class__.__name__
            raise BaseException(strMessage)
        if correct_lp_no_anom is None:
            self._correct_lp_no_anom = None
        elif correct_lp_no_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_no_anom = correct_lp_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'correct_lp_no_anom' is not XSDataString but %s" % self._correct_lp_no_anom.__class__.__name__
            raise BaseException(strMessage)
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataString":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'gxparm' is not XSDataString but %s" % self._gxparm.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl_anom' attribute
    def getHkl_anom(self): return self._hkl_anom
    def setHkl_anom(self, hkl_anom):
        if hkl_anom is None:
            self._hkl_anom = None
        elif hkl_anom.__class__.__name__ == "XSDataString":
            self._hkl_anom = hkl_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setHkl_anom argument is not XSDataString but %s" % hkl_anom.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom(self): self._hkl_anom = None
    hkl_anom = property(getHkl_anom, setHkl_anom, delHkl_anom, "Property for hkl_anom")
    # Methods and properties for the 'hkl_no_anom' attribute
    def getHkl_no_anom(self): return self._hkl_no_anom
    def setHkl_no_anom(self, hkl_no_anom):
        if hkl_no_anom is None:
            self._hkl_no_anom = None
        elif hkl_no_anom.__class__.__name__ == "XSDataString":
            self._hkl_no_anom = hkl_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setHkl_no_anom argument is not XSDataString but %s" % hkl_no_anom.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_no_anom(self): self._hkl_no_anom = None
    hkl_no_anom = property(getHkl_no_anom, setHkl_no_anom, delHkl_no_anom, "Property for hkl_no_anom")
    # Methods and properties for the 'correct_lp_anom' attribute
    def getCorrect_lp_anom(self): return self._correct_lp_anom
    def setCorrect_lp_anom(self, correct_lp_anom):
        if correct_lp_anom is None:
            self._correct_lp_anom = None
        elif correct_lp_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_anom = correct_lp_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setCorrect_lp_anom argument is not XSDataString but %s" % correct_lp_anom.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp_anom(self): self._correct_lp_anom = None
    correct_lp_anom = property(getCorrect_lp_anom, setCorrect_lp_anom, delCorrect_lp_anom, "Property for correct_lp_anom")
    # Methods and properties for the 'correct_lp_no_anom' attribute
    def getCorrect_lp_no_anom(self): return self._correct_lp_no_anom
    def setCorrect_lp_no_anom(self, correct_lp_no_anom):
        if correct_lp_no_anom is None:
            self._correct_lp_no_anom = None
        elif correct_lp_no_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_no_anom = correct_lp_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setCorrect_lp_no_anom argument is not XSDataString but %s" % correct_lp_no_anom.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp_no_anom(self): self._correct_lp_no_anom = None
    correct_lp_no_anom = property(getCorrect_lp_no_anom, setCorrect_lp_no_anom, delCorrect_lp_no_anom, "Property for correct_lp_no_anom")
    # Methods and properties for the 'gxparm' attribute
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataString":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setGxparm argument is not XSDataString but %s" % gxparm.__class__.__name__
            raise BaseException(strMessage)
    def delGxparm(self): self._gxparm = None
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
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'total_completeness' is not XSDataXdsCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if crystal_mosaicity is None:
            self._crystal_mosaicity = None
        elif crystal_mosaicity.__class__.__name__ == "XSDataFloat":
            self._crystal_mosaicity = crystal_mosaicity
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'crystal_mosaicity' is not XSDataFloat but %s" % self._crystal_mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if direct_beam_coordinates is None:
            self._direct_beam_coordinates = None
        elif direct_beam_coordinates.__class__.__name__ == "XSDataVectorDouble":
            self._direct_beam_coordinates = direct_beam_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'direct_beam_coordinates' is not XSDataVectorDouble but %s" % self._direct_beam_coordinates.__class__.__name__
            raise BaseException(strMessage)
        if direct_beam_detector_coordinates is None:
            self._direct_beam_detector_coordinates = None
        elif direct_beam_detector_coordinates.__class__.__name__ == "XSData2DCoordinates":
            self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'direct_beam_detector_coordinates' is not XSData2DCoordinates but %s" % self._direct_beam_detector_coordinates.__class__.__name__
            raise BaseException(strMessage)
        if detector_origin is None:
            self._detector_origin = None
        elif detector_origin.__class__.__name__ == "XSData2DCoordinates":
            self._detector_origin = detector_origin
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'detector_origin' is not XSData2DCoordinates but %s" % self._detector_origin.__class__.__name__
            raise BaseException(strMessage)
        if crystal_to_detector_distance is None:
            self._crystal_to_detector_distance = None
        elif crystal_to_detector_distance.__class__.__name__ == "XSDataFloat":
            self._crystal_to_detector_distance = crystal_to_detector_distance
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'crystal_to_detector_distance' is not XSDataFloat but %s" % self._crystal_to_detector_distance.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_a_axis is None:
            self._coordinates_of_unit_cell_a_axis = None
        elif coordinates_of_unit_cell_a_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_a_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_a_axis.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_b_axis is None:
            self._coordinates_of_unit_cell_b_axis = None
        elif coordinates_of_unit_cell_b_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_b_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_b_axis.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_c_axis is None:
            self._coordinates_of_unit_cell_c_axis = None
        elif coordinates_of_unit_cell_c_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_c_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_c_axis.__class__.__name__
            raise BaseException(strMessage)
        if cell_a is None:
            self._cell_a = None
        elif cell_a.__class__.__name__ == "XSDataFloat":
            self._cell_a = cell_a
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_a' is not XSDataFloat but %s" % self._cell_a.__class__.__name__
            raise BaseException(strMessage)
        if cell_b is None:
            self._cell_b = None
        elif cell_b.__class__.__name__ == "XSDataFloat":
            self._cell_b = cell_b
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_b' is not XSDataFloat but %s" % self._cell_b.__class__.__name__
            raise BaseException(strMessage)
        if cell_c is None:
            self._cell_c = None
        elif cell_c.__class__.__name__ == "XSDataFloat":
            self._cell_c = cell_c
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_c' is not XSDataFloat but %s" % self._cell_c.__class__.__name__
            raise BaseException(strMessage)
        if cell_alpha is None:
            self._cell_alpha = None
        elif cell_alpha.__class__.__name__ == "XSDataFloat":
            self._cell_alpha = cell_alpha
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_alpha' is not XSDataFloat but %s" % self._cell_alpha.__class__.__name__
            raise BaseException(strMessage)
        if cell_beta is None:
            self._cell_beta = None
        elif cell_beta.__class__.__name__ == "XSDataFloat":
            self._cell_beta = cell_beta
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_beta' is not XSDataFloat but %s" % self._cell_beta.__class__.__name__
            raise BaseException(strMessage)
        if cell_gamma is None:
            self._cell_gamma = None
        elif cell_gamma.__class__.__name__ == "XSDataFloat":
            self._cell_gamma = cell_gamma
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_gamma' is not XSDataFloat but %s" % self._cell_gamma.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'unit_cell_constants' is not list but %s" % self._unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'sg_number' is not XSDataInteger but %s" % self._sg_number.__class__.__name__
            raise BaseException(strMessage)
        if xds_run_directory is None:
            self._xds_run_directory = None
        elif xds_run_directory.__class__.__name__ == "XSDataString":
            self._xds_run_directory = xds_run_directory
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'xds_run_directory' is not XSDataString but %s" % self._xds_run_directory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXdsOutput.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXdsOutput.setTotal_completeness argument is not XSDataXdsCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'crystal_mosaicity' attribute
    def getCrystal_mosaicity(self): return self._crystal_mosaicity
    def setCrystal_mosaicity(self, crystal_mosaicity):
        if crystal_mosaicity is None:
            self._crystal_mosaicity = None
        elif crystal_mosaicity.__class__.__name__ == "XSDataFloat":
            self._crystal_mosaicity = crystal_mosaicity
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCrystal_mosaicity argument is not XSDataFloat but %s" % crystal_mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delCrystal_mosaicity(self): self._crystal_mosaicity = None
    crystal_mosaicity = property(getCrystal_mosaicity, setCrystal_mosaicity, delCrystal_mosaicity, "Property for crystal_mosaicity")
    # Methods and properties for the 'direct_beam_coordinates' attribute
    def getDirect_beam_coordinates(self): return self._direct_beam_coordinates
    def setDirect_beam_coordinates(self, direct_beam_coordinates):
        if direct_beam_coordinates is None:
            self._direct_beam_coordinates = None
        elif direct_beam_coordinates.__class__.__name__ == "XSDataVectorDouble":
            self._direct_beam_coordinates = direct_beam_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDirect_beam_coordinates argument is not XSDataVectorDouble but %s" % direct_beam_coordinates.__class__.__name__
            raise BaseException(strMessage)
    def delDirect_beam_coordinates(self): self._direct_beam_coordinates = None
    direct_beam_coordinates = property(getDirect_beam_coordinates, setDirect_beam_coordinates, delDirect_beam_coordinates, "Property for direct_beam_coordinates")
    # Methods and properties for the 'direct_beam_detector_coordinates' attribute
    def getDirect_beam_detector_coordinates(self): return self._direct_beam_detector_coordinates
    def setDirect_beam_detector_coordinates(self, direct_beam_detector_coordinates):
        if direct_beam_detector_coordinates is None:
            self._direct_beam_detector_coordinates = None
        elif direct_beam_detector_coordinates.__class__.__name__ == "XSData2DCoordinates":
            self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDirect_beam_detector_coordinates argument is not XSData2DCoordinates but %s" % direct_beam_detector_coordinates.__class__.__name__
            raise BaseException(strMessage)
    def delDirect_beam_detector_coordinates(self): self._direct_beam_detector_coordinates = None
    direct_beam_detector_coordinates = property(getDirect_beam_detector_coordinates, setDirect_beam_detector_coordinates, delDirect_beam_detector_coordinates, "Property for direct_beam_detector_coordinates")
    # Methods and properties for the 'detector_origin' attribute
    def getDetector_origin(self): return self._detector_origin
    def setDetector_origin(self, detector_origin):
        if detector_origin is None:
            self._detector_origin = None
        elif detector_origin.__class__.__name__ == "XSData2DCoordinates":
            self._detector_origin = detector_origin
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDetector_origin argument is not XSData2DCoordinates but %s" % detector_origin.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_origin(self): self._detector_origin = None
    detector_origin = property(getDetector_origin, setDetector_origin, delDetector_origin, "Property for detector_origin")
    # Methods and properties for the 'crystal_to_detector_distance' attribute
    def getCrystal_to_detector_distance(self): return self._crystal_to_detector_distance
    def setCrystal_to_detector_distance(self, crystal_to_detector_distance):
        if crystal_to_detector_distance is None:
            self._crystal_to_detector_distance = None
        elif crystal_to_detector_distance.__class__.__name__ == "XSDataFloat":
            self._crystal_to_detector_distance = crystal_to_detector_distance
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCrystal_to_detector_distance argument is not XSDataFloat but %s" % crystal_to_detector_distance.__class__.__name__
            raise BaseException(strMessage)
    def delCrystal_to_detector_distance(self): self._crystal_to_detector_distance = None
    crystal_to_detector_distance = property(getCrystal_to_detector_distance, setCrystal_to_detector_distance, delCrystal_to_detector_distance, "Property for crystal_to_detector_distance")
    # Methods and properties for the 'coordinates_of_unit_cell_a_axis' attribute
    def getCoordinates_of_unit_cell_a_axis(self): return self._coordinates_of_unit_cell_a_axis
    def setCoordinates_of_unit_cell_a_axis(self, coordinates_of_unit_cell_a_axis):
        if coordinates_of_unit_cell_a_axis is None:
            self._coordinates_of_unit_cell_a_axis = None
        elif coordinates_of_unit_cell_a_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_a_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_a_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_a_axis(self): self._coordinates_of_unit_cell_a_axis = None
    coordinates_of_unit_cell_a_axis = property(getCoordinates_of_unit_cell_a_axis, setCoordinates_of_unit_cell_a_axis, delCoordinates_of_unit_cell_a_axis, "Property for coordinates_of_unit_cell_a_axis")
    # Methods and properties for the 'coordinates_of_unit_cell_b_axis' attribute
    def getCoordinates_of_unit_cell_b_axis(self): return self._coordinates_of_unit_cell_b_axis
    def setCoordinates_of_unit_cell_b_axis(self, coordinates_of_unit_cell_b_axis):
        if coordinates_of_unit_cell_b_axis is None:
            self._coordinates_of_unit_cell_b_axis = None
        elif coordinates_of_unit_cell_b_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_b_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_b_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_b_axis(self): self._coordinates_of_unit_cell_b_axis = None
    coordinates_of_unit_cell_b_axis = property(getCoordinates_of_unit_cell_b_axis, setCoordinates_of_unit_cell_b_axis, delCoordinates_of_unit_cell_b_axis, "Property for coordinates_of_unit_cell_b_axis")
    # Methods and properties for the 'coordinates_of_unit_cell_c_axis' attribute
    def getCoordinates_of_unit_cell_c_axis(self): return self._coordinates_of_unit_cell_c_axis
    def setCoordinates_of_unit_cell_c_axis(self, coordinates_of_unit_cell_c_axis):
        if coordinates_of_unit_cell_c_axis is None:
            self._coordinates_of_unit_cell_c_axis = None
        elif coordinates_of_unit_cell_c_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_c_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_c_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_c_axis(self): self._coordinates_of_unit_cell_c_axis = None
    coordinates_of_unit_cell_c_axis = property(getCoordinates_of_unit_cell_c_axis, setCoordinates_of_unit_cell_c_axis, delCoordinates_of_unit_cell_c_axis, "Property for coordinates_of_unit_cell_c_axis")
    # Methods and properties for the 'cell_a' attribute
    def getCell_a(self): return self._cell_a
    def setCell_a(self, cell_a):
        if cell_a is None:
            self._cell_a = None
        elif cell_a.__class__.__name__ == "XSDataFloat":
            self._cell_a = cell_a
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_a argument is not XSDataFloat but %s" % cell_a.__class__.__name__
            raise BaseException(strMessage)
    def delCell_a(self): self._cell_a = None
    cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
    # Methods and properties for the 'cell_b' attribute
    def getCell_b(self): return self._cell_b
    def setCell_b(self, cell_b):
        if cell_b is None:
            self._cell_b = None
        elif cell_b.__class__.__name__ == "XSDataFloat":
            self._cell_b = cell_b
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_b argument is not XSDataFloat but %s" % cell_b.__class__.__name__
            raise BaseException(strMessage)
    def delCell_b(self): self._cell_b = None
    cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
    # Methods and properties for the 'cell_c' attribute
    def getCell_c(self): return self._cell_c
    def setCell_c(self, cell_c):
        if cell_c is None:
            self._cell_c = None
        elif cell_c.__class__.__name__ == "XSDataFloat":
            self._cell_c = cell_c
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_c argument is not XSDataFloat but %s" % cell_c.__class__.__name__
            raise BaseException(strMessage)
    def delCell_c(self): self._cell_c = None
    cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
    # Methods and properties for the 'cell_alpha' attribute
    def getCell_alpha(self): return self._cell_alpha
    def setCell_alpha(self, cell_alpha):
        if cell_alpha is None:
            self._cell_alpha = None
        elif cell_alpha.__class__.__name__ == "XSDataFloat":
            self._cell_alpha = cell_alpha
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_alpha argument is not XSDataFloat but %s" % cell_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delCell_alpha(self): self._cell_alpha = None
    cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
    # Methods and properties for the 'cell_beta' attribute
    def getCell_beta(self): return self._cell_beta
    def setCell_beta(self, cell_beta):
        if cell_beta is None:
            self._cell_beta = None
        elif cell_beta.__class__.__name__ == "XSDataFloat":
            self._cell_beta = cell_beta
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_beta argument is not XSDataFloat but %s" % cell_beta.__class__.__name__
            raise BaseException(strMessage)
    def delCell_beta(self): self._cell_beta = None
    cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
    # Methods and properties for the 'cell_gamma' attribute
    def getCell_gamma(self): return self._cell_gamma
    def setCell_gamma(self, cell_gamma):
        if cell_gamma is None:
            self._cell_gamma = None
        elif cell_gamma.__class__.__name__ == "XSDataFloat":
            self._cell_gamma = cell_gamma
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_gamma argument is not XSDataFloat but %s" % cell_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delCell_gamma(self): self._cell_gamma = None
    cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
    # Methods and properties for the 'unit_cell_constants' attribute
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXdsOutput.setUnit_cell_constants argument is not list but %s" % unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._unit_cell_constants.append(value)
        else:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertUnit_cell_constants(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXdsOutput.insertUnit_cell_constants argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.insertUnit_cell_constants argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._unit_cell_constants[index] = value
        else:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sg_number' attribute
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXdsOutput.setSg_number argument is not XSDataInteger but %s" % sg_number.__class__.__name__
            raise BaseException(strMessage)
    def delSg_number(self): self._sg_number = None
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    # Methods and properties for the 'xds_run_directory' attribute
    def getXds_run_directory(self): return self._xds_run_directory
    def setXds_run_directory(self, xds_run_directory):
        if xds_run_directory is None:
            self._xds_run_directory = None
        elif xds_run_directory.__class__.__name__ == "XSDataString":
            self._xds_run_directory = xds_run_directory
        else:
            strMessage = "ERROR! XSDataXdsOutput.setXds_run_directory argument is not XSDataString but %s" % xds_run_directory.__class__.__name__
            raise BaseException(strMessage)
    def delXds_run_directory(self): self._xds_run_directory = None
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
        if correct_lp is None:
            self._correct_lp = None
        elif correct_lp.__class__.__name__ == "XSDataFile":
            self._correct_lp = correct_lp
        else:
            strMessage = "ERROR! XSDataXdsOutputFile constructor argument 'correct_lp' is not XSDataFile but %s" % self._correct_lp.__class__.__name__
            raise BaseException(strMessage)
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataFile":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsOutputFile constructor argument 'gxparm' is not XSDataFile but %s" % self._gxparm.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'correct_lp' attribute
    def getCorrect_lp(self): return self._correct_lp
    def setCorrect_lp(self, correct_lp):
        if correct_lp is None:
            self._correct_lp = None
        elif correct_lp.__class__.__name__ == "XSDataFile":
            self._correct_lp = correct_lp
        else:
            strMessage = "ERROR! XSDataXdsOutputFile.setCorrect_lp argument is not XSDataFile but %s" % correct_lp.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp(self): self._correct_lp = None
    correct_lp = property(getCorrect_lp, setCorrect_lp, delCorrect_lp, "Property for correct_lp")
    # Methods and properties for the 'gxparm' attribute
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataFile":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsOutputFile.setGxparm argument is not XSDataFile but %s" % gxparm.__class__.__name__
            raise BaseException(strMessage)
    def delGxparm(self): self._gxparm = None
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


class XSDataXdsToSca(XSDataInput):
    def __init__(self, configuration=None, sca_file=None, hkl_file=None):
        XSDataInput.__init__(self, configuration)
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataFile":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXdsToSca constructor argument 'hkl_file' is not XSDataFile but %s" % self._hkl_file.__class__.__name__
            raise BaseException(strMessage)
        if sca_file is None:
            self._sca_file = None
        elif sca_file.__class__.__name__ == "XSDataFile":
            self._sca_file = sca_file
        else:
            strMessage = "ERROR! XSDataXdsToSca constructor argument 'sca_file' is not XSDataFile but %s" % self._sca_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl_file' attribute
    def getHkl_file(self): return self._hkl_file
    def setHkl_file(self, hkl_file):
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataFile":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXdsToSca.setHkl_file argument is not XSDataFile but %s" % hkl_file.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_file(self): self._hkl_file = None
    hkl_file = property(getHkl_file, setHkl_file, delHkl_file, "Property for hkl_file")
    # Methods and properties for the 'sca_file' attribute
    def getSca_file(self): return self._sca_file
    def setSca_file(self, sca_file):
        if sca_file is None:
            self._sca_file = None
        elif sca_file.__class__.__name__ == "XSDataFile":
            self._sca_file = sca_file
        else:
            strMessage = "ERROR! XSDataXdsToSca.setSca_file argument is not XSDataFile but %s" % sca_file.__class__.__name__
            raise BaseException(strMessage)
    def delSca_file(self): self._sca_file = None
    sca_file = property(getSca_file, setSca_file, delSca_file, "Property for sca_file")
    def export(self, outfile, level, name_='XSDataXdsToSca'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsToSca'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._hkl_file is not None:
            self.hkl_file.export(outfile, level, name_='hkl_file')
        else:
            warnEmptyAttribute("hkl_file", "XSDataFile")
        if self._sca_file is not None:
            self.sca_file.export(outfile, level, name_='sca_file')
        else:
            warnEmptyAttribute("sca_file", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHkl_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sca_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSca_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsToSca" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsToSca' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsToSca is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsToSca.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsToSca()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsToSca" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsToSca()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsToSca


class XSDataXscaleGeneratedFiles(XSDataResult):
    def __init__(self, status=None, stats_noanom_unmerged=None, lp_noanom_unmerged=None, hkl_noanom_unmerged=None, stats_anom_unmerged=None, lp_anom_unmerged=None, hkl_anom_unmerged=None, stats_noanom_merged=None, lp_noanom_merged=None, hkl_noanom_merged=None, stats_anom_merged=None, lp_anom_merged=None, hkl_anom_merged=None):
        XSDataResult.__init__(self, status)
        if hkl_anom_merged is None:
            self._hkl_anom_merged = None
        elif hkl_anom_merged.__class__.__name__ == "XSDataString":
            self._hkl_anom_merged = hkl_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_anom_merged' is not XSDataString but %s" % self._hkl_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if lp_anom_merged is None:
            self._lp_anom_merged = None
        elif lp_anom_merged.__class__.__name__ == "XSDataString":
            self._lp_anom_merged = lp_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_anom_merged' is not XSDataString but %s" % self._lp_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if stats_anom_merged is None:
            self._stats_anom_merged = None
        elif stats_anom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_merged = stats_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_anom_merged' is not XSDataXscaleParsedOutput but %s" % self._stats_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_noanom_merged is None:
            self._hkl_noanom_merged = None
        elif hkl_noanom_merged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_merged = hkl_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_noanom_merged' is not XSDataString but %s" % self._hkl_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if lp_noanom_merged is None:
            self._lp_noanom_merged = None
        elif lp_noanom_merged.__class__.__name__ == "XSDataString":
            self._lp_noanom_merged = lp_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_noanom_merged' is not XSDataString but %s" % self._lp_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if stats_noanom_merged is None:
            self._stats_noanom_merged = None
        elif stats_noanom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_merged = stats_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_noanom_merged' is not XSDataXscaleParsedOutput but %s" % self._stats_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_anom_unmerged is None:
            self._hkl_anom_unmerged = None
        elif hkl_anom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_anom_unmerged = hkl_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_anom_unmerged' is not XSDataString but %s" % self._hkl_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if lp_anom_unmerged is None:
            self._lp_anom_unmerged = None
        elif lp_anom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_anom_unmerged = lp_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_anom_unmerged' is not XSDataString but %s" % self._lp_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if stats_anom_unmerged is None:
            self._stats_anom_unmerged = None
        elif stats_anom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_unmerged = stats_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_anom_unmerged' is not XSDataXscaleParsedOutput but %s" % self._stats_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_noanom_unmerged is None:
            self._hkl_noanom_unmerged = None
        elif hkl_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_unmerged = hkl_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_noanom_unmerged' is not XSDataString but %s" % self._hkl_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if lp_noanom_unmerged is None:
            self._lp_noanom_unmerged = None
        elif lp_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_noanom_unmerged = lp_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_noanom_unmerged' is not XSDataString but %s" % self._lp_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if stats_noanom_unmerged is None:
            self._stats_noanom_unmerged = None
        elif stats_noanom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_unmerged = stats_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_noanom_unmerged' is not XSDataXscaleParsedOutput but %s" % self._stats_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl_anom_merged' attribute
    def getHkl_anom_merged(self): return self._hkl_anom_merged
    def setHkl_anom_merged(self, hkl_anom_merged):
        if hkl_anom_merged is None:
            self._hkl_anom_merged = None
        elif hkl_anom_merged.__class__.__name__ == "XSDataString":
            self._hkl_anom_merged = hkl_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_anom_merged argument is not XSDataString but %s" % hkl_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom_merged(self): self._hkl_anom_merged = None
    hkl_anom_merged = property(getHkl_anom_merged, setHkl_anom_merged, delHkl_anom_merged, "Property for hkl_anom_merged")
    # Methods and properties for the 'lp_anom_merged' attribute
    def getLp_anom_merged(self): return self._lp_anom_merged
    def setLp_anom_merged(self, lp_anom_merged):
        if lp_anom_merged is None:
            self._lp_anom_merged = None
        elif lp_anom_merged.__class__.__name__ == "XSDataString":
            self._lp_anom_merged = lp_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_anom_merged argument is not XSDataString but %s" % lp_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_anom_merged(self): self._lp_anom_merged = None
    lp_anom_merged = property(getLp_anom_merged, setLp_anom_merged, delLp_anom_merged, "Property for lp_anom_merged")
    # Methods and properties for the 'stats_anom_merged' attribute
    def getStats_anom_merged(self): return self._stats_anom_merged
    def setStats_anom_merged(self, stats_anom_merged):
        if stats_anom_merged is None:
            self._stats_anom_merged = None
        elif stats_anom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_merged = stats_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_anom_merged argument is not XSDataXscaleParsedOutput but %s" % stats_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_anom_merged(self): self._stats_anom_merged = None
    stats_anom_merged = property(getStats_anom_merged, setStats_anom_merged, delStats_anom_merged, "Property for stats_anom_merged")
    # Methods and properties for the 'hkl_noanom_merged' attribute
    def getHkl_noanom_merged(self): return self._hkl_noanom_merged
    def setHkl_noanom_merged(self, hkl_noanom_merged):
        if hkl_noanom_merged is None:
            self._hkl_noanom_merged = None
        elif hkl_noanom_merged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_merged = hkl_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_noanom_merged argument is not XSDataString but %s" % hkl_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_noanom_merged(self): self._hkl_noanom_merged = None
    hkl_noanom_merged = property(getHkl_noanom_merged, setHkl_noanom_merged, delHkl_noanom_merged, "Property for hkl_noanom_merged")
    # Methods and properties for the 'lp_noanom_merged' attribute
    def getLp_noanom_merged(self): return self._lp_noanom_merged
    def setLp_noanom_merged(self, lp_noanom_merged):
        if lp_noanom_merged is None:
            self._lp_noanom_merged = None
        elif lp_noanom_merged.__class__.__name__ == "XSDataString":
            self._lp_noanom_merged = lp_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_noanom_merged argument is not XSDataString but %s" % lp_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_noanom_merged(self): self._lp_noanom_merged = None
    lp_noanom_merged = property(getLp_noanom_merged, setLp_noanom_merged, delLp_noanom_merged, "Property for lp_noanom_merged")
    # Methods and properties for the 'stats_noanom_merged' attribute
    def getStats_noanom_merged(self): return self._stats_noanom_merged
    def setStats_noanom_merged(self, stats_noanom_merged):
        if stats_noanom_merged is None:
            self._stats_noanom_merged = None
        elif stats_noanom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_merged = stats_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_noanom_merged argument is not XSDataXscaleParsedOutput but %s" % stats_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_noanom_merged(self): self._stats_noanom_merged = None
    stats_noanom_merged = property(getStats_noanom_merged, setStats_noanom_merged, delStats_noanom_merged, "Property for stats_noanom_merged")
    # Methods and properties for the 'hkl_anom_unmerged' attribute
    def getHkl_anom_unmerged(self): return self._hkl_anom_unmerged
    def setHkl_anom_unmerged(self, hkl_anom_unmerged):
        if hkl_anom_unmerged is None:
            self._hkl_anom_unmerged = None
        elif hkl_anom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_anom_unmerged = hkl_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_anom_unmerged argument is not XSDataString but %s" % hkl_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom_unmerged(self): self._hkl_anom_unmerged = None
    hkl_anom_unmerged = property(getHkl_anom_unmerged, setHkl_anom_unmerged, delHkl_anom_unmerged, "Property for hkl_anom_unmerged")
    # Methods and properties for the 'lp_anom_unmerged' attribute
    def getLp_anom_unmerged(self): return self._lp_anom_unmerged
    def setLp_anom_unmerged(self, lp_anom_unmerged):
        if lp_anom_unmerged is None:
            self._lp_anom_unmerged = None
        elif lp_anom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_anom_unmerged = lp_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_anom_unmerged argument is not XSDataString but %s" % lp_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_anom_unmerged(self): self._lp_anom_unmerged = None
    lp_anom_unmerged = property(getLp_anom_unmerged, setLp_anom_unmerged, delLp_anom_unmerged, "Property for lp_anom_unmerged")
    # Methods and properties for the 'stats_anom_unmerged' attribute
    def getStats_anom_unmerged(self): return self._stats_anom_unmerged
    def setStats_anom_unmerged(self, stats_anom_unmerged):
        if stats_anom_unmerged is None:
            self._stats_anom_unmerged = None
        elif stats_anom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_unmerged = stats_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_anom_unmerged argument is not XSDataXscaleParsedOutput but %s" % stats_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_anom_unmerged(self): self._stats_anom_unmerged = None
    stats_anom_unmerged = property(getStats_anom_unmerged, setStats_anom_unmerged, delStats_anom_unmerged, "Property for stats_anom_unmerged")
    # Methods and properties for the 'hkl_noanom_unmerged' attribute
    def getHkl_noanom_unmerged(self): return self._hkl_noanom_unmerged
    def setHkl_noanom_unmerged(self, hkl_noanom_unmerged):
        if hkl_noanom_unmerged is None:
            self._hkl_noanom_unmerged = None
        elif hkl_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_unmerged = hkl_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_noanom_unmerged argument is not XSDataString but %s" % hkl_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_noanom_unmerged(self): self._hkl_noanom_unmerged = None
    hkl_noanom_unmerged = property(getHkl_noanom_unmerged, setHkl_noanom_unmerged, delHkl_noanom_unmerged, "Property for hkl_noanom_unmerged")
    # Methods and properties for the 'lp_noanom_unmerged' attribute
    def getLp_noanom_unmerged(self): return self._lp_noanom_unmerged
    def setLp_noanom_unmerged(self, lp_noanom_unmerged):
        if lp_noanom_unmerged is None:
            self._lp_noanom_unmerged = None
        elif lp_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_noanom_unmerged = lp_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_noanom_unmerged argument is not XSDataString but %s" % lp_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_noanom_unmerged(self): self._lp_noanom_unmerged = None
    lp_noanom_unmerged = property(getLp_noanom_unmerged, setLp_noanom_unmerged, delLp_noanom_unmerged, "Property for lp_noanom_unmerged")
    # Methods and properties for the 'stats_noanom_unmerged' attribute
    def getStats_noanom_unmerged(self): return self._stats_noanom_unmerged
    def setStats_noanom_unmerged(self, stats_noanom_unmerged):
        if stats_noanom_unmerged is None:
            self._stats_noanom_unmerged = None
        elif stats_noanom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_unmerged = stats_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_noanom_unmerged argument is not XSDataXscaleParsedOutput but %s" % stats_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_noanom_unmerged(self): self._stats_noanom_unmerged = None
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
    def __init__(self, configuration=None, res=None, path_noanom=None, path_anom=None):
        XSDataInput.__init__(self, configuration)
        if path_anom is None:
            self._path_anom = None
        elif path_anom.__class__.__name__ == "XSDataString":
            self._path_anom = path_anom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'path_anom' is not XSDataString but %s" % self._path_anom.__class__.__name__
            raise BaseException(strMessage)
        if path_noanom is None:
            self._path_noanom = None
        elif path_noanom.__class__.__name__ == "XSDataString":
            self._path_noanom = path_noanom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'path_noanom' is not XSDataString but %s" % self._path_noanom.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'res' is not XSDataFloat but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'path_anom' attribute
    def getPath_anom(self): return self._path_anom
    def setPath_anom(self, path_anom):
        if path_anom is None:
            self._path_anom = None
        elif path_anom.__class__.__name__ == "XSDataString":
            self._path_anom = path_anom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setPath_anom argument is not XSDataString but %s" % path_anom.__class__.__name__
            raise BaseException(strMessage)
    def delPath_anom(self): self._path_anom = None
    path_anom = property(getPath_anom, setPath_anom, delPath_anom, "Property for path_anom")
    # Methods and properties for the 'path_noanom' attribute
    def getPath_noanom(self): return self._path_noanom
    def setPath_noanom(self, path_noanom):
        if path_noanom is None:
            self._path_noanom = None
        elif path_noanom.__class__.__name__ == "XSDataString":
            self._path_noanom = path_noanom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setPath_noanom argument is not XSDataString but %s" % path_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delPath_noanom(self): self._path_noanom = None
    path_noanom = property(getPath_noanom, setPath_noanom, delPath_noanom, "Property for path_noanom")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataFloat":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setRes argument is not XSDataFloat but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    def export(self, outfile, level, name_='XSDataXscaleInputFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleInputFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._path_anom is not None:
            self.path_anom.export(outfile, level, name_='path_anom')
        if self._path_noanom is not None:
            self.path_noanom.export(outfile, level, name_='path_noanom')
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
            nodeName_ == 'path_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPath_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPath_noanom(obj_)
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
        if merge is None:
            self._merge = None
        elif merge.__class__.__name__ == "XSDataBoolean":
            self._merge = merge
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'merge' is not XSDataBoolean but %s" % self._merge.__class__.__name__
            raise BaseException(strMessage)
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'friedels_law' is not XSDataBoolean but %s" % self._friedels_law.__class__.__name__
            raise BaseException(strMessage)
        if xds_files is None:
            self._xds_files = []
        elif xds_files.__class__.__name__ == "list":
            self._xds_files = xds_files
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'xds_files' is not list but %s" % self._xds_files.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'unit_cell_constants' is not list but %s" % self._unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'sg_number' is not XSDataInteger but %s" % self._sg_number.__class__.__name__
            raise BaseException(strMessage)
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'bins' is not list but %s" % self._bins.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'merge' attribute
    def getMerge(self): return self._merge
    def setMerge(self, merge):
        if merge is None:
            self._merge = None
        elif merge.__class__.__name__ == "XSDataBoolean":
            self._merge = merge
        else:
            strMessage = "ERROR! XSDataXscaleInput.setMerge argument is not XSDataBoolean but %s" % merge.__class__.__name__
            raise BaseException(strMessage)
    def delMerge(self): self._merge = None
    merge = property(getMerge, setMerge, delMerge, "Property for merge")
    # Methods and properties for the 'friedels_law' attribute
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXscaleInput.setFriedels_law argument is not XSDataBoolean but %s" % friedels_law.__class__.__name__
            raise BaseException(strMessage)
    def delFriedels_law(self): self._friedels_law = None
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    # Methods and properties for the 'xds_files' attribute
    def getXds_files(self): return self._xds_files
    def setXds_files(self, xds_files):
        if xds_files is None:
            self._xds_files = []
        elif xds_files.__class__.__name__ == "list":
            self._xds_files = xds_files
        else:
            strMessage = "ERROR! XSDataXscaleInput.setXds_files argument is not list but %s" % xds_files.__class__.__name__
            raise BaseException(strMessage)
    def delXds_files(self): self._xds_files = None
    xds_files = property(getXds_files, setXds_files, delXds_files, "Property for xds_files")
    def addXds_files(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleInputFile":
            self._xds_files.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is not XSDataXscaleInputFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXds_files(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertXds_files argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertXds_files argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleInputFile":
            self._xds_files[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is not XSDataXscaleInputFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'unit_cell_constants' attribute
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXscaleInput.setUnit_cell_constants argument is not list but %s" % unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._unit_cell_constants.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertUnit_cell_constants(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertUnit_cell_constants argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertUnit_cell_constants argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFloat":
            self._unit_cell_constants[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is not XSDataFloat but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sg_number' attribute
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXscaleInput.setSg_number argument is not XSDataInteger but %s" % sg_number.__class__.__name__
            raise BaseException(strMessage)
    def delSg_number(self): self._sg_number = None
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    # Methods and properties for the 'bins' attribute
    def getBins(self): return self._bins
    def setBins(self, bins):
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataXscaleInput.setBins argument is not list but %s" % bins.__class__.__name__
            raise BaseException(strMessage)
    def delBins(self): self._bins = None
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBins(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertBins argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertBins argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
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
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'succeeded' is not XSDataBoolean but %s" % self._succeeded.__class__.__name__
            raise BaseException(strMessage)
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataString":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'hkl_file' is not XSDataString but %s" % self._hkl_file.__class__.__name__
            raise BaseException(strMessage)
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'lp_file' is not XSDataString but %s" % self._lp_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'succeeded' attribute
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setSucceeded argument is not XSDataBoolean but %s" % succeeded.__class__.__name__
            raise BaseException(strMessage)
    def delSucceeded(self): self._succeeded = None
    succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
    # Methods and properties for the 'hkl_file' attribute
    def getHkl_file(self): return self._hkl_file
    def setHkl_file(self, hkl_file):
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataString":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setHkl_file argument is not XSDataString but %s" % hkl_file.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_file(self): self._hkl_file = None
    hkl_file = property(getHkl_file, setHkl_file, delHkl_file, "Property for hkl_file")
    # Methods and properties for the 'lp_file' attribute
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setLp_file argument is not XSDataString but %s" % lp_file.__class__.__name__
            raise BaseException(strMessage)
    def delLp_file(self): self._lp_file = None
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


class XSDataXscaleParsedOutput(XSDataResult):
    def __init__(self, status=None, completeness_entries=None, total_completeness=None):
        XSDataResult.__init__(self, status)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput constructor argument 'total_completeness' is not XSDataXscaleCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.setTotal_completeness argument is not XSDataXscaleCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is not XSDataXscaleCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is not XSDataXscaleCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
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


class XSDataXscaleParsingInput(XSDataInput):
    def __init__(self, configuration=None, lp_file=None):
        XSDataInput.__init__(self, configuration)
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleParsingInput constructor argument 'lp_file' is not XSDataString but %s" % self._lp_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lp_file' attribute
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleParsingInput.setLp_file argument is not XSDataString but %s" % lp_file.__class__.__name__
            raise BaseException(strMessage)
    def delLp_file(self): self._lp_file = None
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



# End of data representation classes.



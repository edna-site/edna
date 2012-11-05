#!/usr/bin/env python

#
# Generated Mon Oct 29 04:41::26 2012 by EDGenerateDS.
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
    from XSDataCommon import XSData
    from XSDataCommon import XSDataArray
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
from XSDataCommon import XSData
from XSDataCommon import XSDataArray
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



class XSDataGlePlot(XSData):
    def __init__(self, data=None, script=None):
        XSData.__init__(self, )
        if script is None:
            self._script = None
        elif script.__class__.__name__ == "XSDataFile":
            self._script = script
        else:
            strMessage = "ERROR! XSDataGlePlot constructor argument 'script' is not XSDataFile but %s" % self._script.__class__.__name__
            raise BaseException(strMessage)
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataFile":
            self._data = data
        else:
            strMessage = "ERROR! XSDataGlePlot constructor argument 'data' is not XSDataFile but %s" % self._data.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'script' attribute
    def getScript(self): return self._script
    def setScript(self, script):
        if script is None:
            self._script = None
        elif script.__class__.__name__ == "XSDataFile":
            self._script = script
        else:
            strMessage = "ERROR! XSDataGlePlot.setScript argument is not XSDataFile but %s" % script.__class__.__name__
            raise BaseException(strMessage)
    def delScript(self): self._script = None
    script = property(getScript, setScript, delScript, "Property for script")
    # Methods and properties for the 'data' attribute
    def getData(self): return self._data
    def setData(self, data):
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataFile":
            self._data = data
        else:
            strMessage = "ERROR! XSDataGlePlot.setData argument is not XSDataFile but %s" % data.__class__.__name__
            raise BaseException(strMessage)
    def delData(self): self._data = None
    data = property(getData, setData, delData, "Property for data")
    def export(self, outfile, level, name_='XSDataGlePlot'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataGlePlot'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._script is not None:
            self.script.export(outfile, level, name_='script')
        else:
            warnEmptyAttribute("script", "XSDataFile")
        if self._data is not None:
            self.data.export(outfile, level, name_='data')
        else:
            warnEmptyAttribute("data", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'script':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScript(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setData(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataGlePlot" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataGlePlot' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataGlePlot is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataGlePlot.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGlePlot()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataGlePlot" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGlePlot()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataGlePlot


class XSDataGraph(XSData):
    def __init__(self, data=None, markerColor=None, markerType=None, label=None, lineColor=None, lineWidth=None, lineStyle=None):
        XSData.__init__(self, )
        self._lineStyle = str(lineStyle)
        if lineWidth is None:
            self._lineWidth = None
        else:
            self._lineWidth = float(lineWidth)
        self._lineColor = str(lineColor)
        self._label = str(label)
        self._markerType = str(markerType)
        self._markerColor = str(markerColor)
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataArray":
            self._data = data
        else:
            strMessage = "ERROR! XSDataGraph constructor argument 'data' is not XSDataArray but %s" % self._data.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lineStyle' attribute
    def getLineStyle(self): return self._lineStyle
    def setLineStyle(self, lineStyle):
        self._lineStyle = str(lineStyle)
    def delLineStyle(self): self._lineStyle = None
    lineStyle = property(getLineStyle, setLineStyle, delLineStyle, "Property for lineStyle")
    # Methods and properties for the 'lineWidth' attribute
    def getLineWidth(self): return self._lineWidth
    def setLineWidth(self, lineWidth):
        if lineWidth is None:
            self._lineWidth = None
        else:
            self._lineWidth = float(lineWidth)
    def delLineWidth(self): self._lineWidth = None
    lineWidth = property(getLineWidth, setLineWidth, delLineWidth, "Property for lineWidth")
    # Methods and properties for the 'lineColor' attribute
    def getLineColor(self): return self._lineColor
    def setLineColor(self, lineColor):
        self._lineColor = str(lineColor)
    def delLineColor(self): self._lineColor = None
    lineColor = property(getLineColor, setLineColor, delLineColor, "Property for lineColor")
    # Methods and properties for the 'label' attribute
    def getLabel(self): return self._label
    def setLabel(self, label):
        self._label = str(label)
    def delLabel(self): self._label = None
    label = property(getLabel, setLabel, delLabel, "Property for label")
    # Methods and properties for the 'markerType' attribute
    def getMarkerType(self): return self._markerType
    def setMarkerType(self, markerType):
        self._markerType = str(markerType)
    def delMarkerType(self): self._markerType = None
    markerType = property(getMarkerType, setMarkerType, delMarkerType, "Property for markerType")
    # Methods and properties for the 'markerColor' attribute
    def getMarkerColor(self): return self._markerColor
    def setMarkerColor(self, markerColor):
        self._markerColor = str(markerColor)
    def delMarkerColor(self): self._markerColor = None
    markerColor = property(getMarkerColor, setMarkerColor, delMarkerColor, "Property for markerColor")
    # Methods and properties for the 'data' attribute
    def getData(self): return self._data
    def setData(self, data):
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataArray":
            self._data = data
        else:
            strMessage = "ERROR! XSDataGraph.setData argument is not XSDataArray but %s" % data.__class__.__name__
            raise BaseException(strMessage)
    def delData(self): self._data = None
    data = property(getData, setData, delData, "Property for data")
    def export(self, outfile, level, name_='XSDataGraph'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataGraph'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._lineStyle is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<lineStyle>%s</lineStyle>\n' % self._lineStyle))
        else:
            warnEmptyAttribute("lineStyle", "string")
        if self._lineWidth is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<lineWidth>%e</lineWidth>\n' % self._lineWidth))
        else:
            warnEmptyAttribute("lineWidth", "double")
        if self._lineColor is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<lineColor>%s</lineColor>\n' % self._lineColor))
        else:
            warnEmptyAttribute("lineColor", "string")
        if self._label is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<label>%s</label>\n' % self._label))
        else:
            warnEmptyAttribute("label", "string")
        if self._markerType is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<markerType>%s</markerType>\n' % self._markerType))
        else:
            warnEmptyAttribute("markerType", "string")
        if self._markerColor is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<markerColor>%s</markerColor>\n' % self._markerColor))
        else:
            warnEmptyAttribute("markerColor", "string")
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
            nodeName_ == 'lineStyle':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._lineStyle = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lineWidth':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._lineWidth = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lineColor':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._lineColor = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'label':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._label = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'markerType':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._markerType = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'markerColor':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._markerColor = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setData(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataGraph" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataGraph' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataGraph is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataGraph.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGraph()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataGraph" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGraph()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataGraph


class XSDataPlot(XSData):
    def __init__(self, graph=None, ytitle=None, xtitle=None, keypos=None, ymax=None, xmax=None, ymin=None, xmin=None, ysize=None, xsize=None, subTitle=None, title=None, plotType=None):
        XSData.__init__(self, )
        self._plotType = str(plotType)
        self._title = str(title)
        self._subTitle = str(subTitle)
        if xsize is None:
            self._xsize = None
        else:
            self._xsize = float(xsize)
        if ysize is None:
            self._ysize = None
        else:
            self._ysize = float(ysize)
        if xmin is None:
            self._xmin = None
        else:
            self._xmin = float(xmin)
        if ymin is None:
            self._ymin = None
        else:
            self._ymin = float(ymin)
        if xmax is None:
            self._xmax = None
        else:
            self._xmax = float(xmax)
        if ymax is None:
            self._ymax = None
        else:
            self._ymax = float(ymax)
        self._keypos = str(keypos)
        self._xtitle = str(xtitle)
        self._ytitle = str(ytitle)
        if graph is None:
            self._graph = []
        elif graph.__class__.__name__ == "list":
            self._graph = graph
        else:
            strMessage = "ERROR! XSDataPlot constructor argument 'graph' is not list but %s" % self._graph.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'plotType' attribute
    def getPlotType(self): return self._plotType
    def setPlotType(self, plotType):
        self._plotType = str(plotType)
    def delPlotType(self): self._plotType = None
    plotType = property(getPlotType, setPlotType, delPlotType, "Property for plotType")
    # Methods and properties for the 'title' attribute
    def getTitle(self): return self._title
    def setTitle(self, title):
        self._title = str(title)
    def delTitle(self): self._title = None
    title = property(getTitle, setTitle, delTitle, "Property for title")
    # Methods and properties for the 'subTitle' attribute
    def getSubTitle(self): return self._subTitle
    def setSubTitle(self, subTitle):
        self._subTitle = str(subTitle)
    def delSubTitle(self): self._subTitle = None
    subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
    # Methods and properties for the 'xsize' attribute
    def getXsize(self): return self._xsize
    def setXsize(self, xsize):
        if xsize is None:
            self._xsize = None
        else:
            self._xsize = float(xsize)
    def delXsize(self): self._xsize = None
    xsize = property(getXsize, setXsize, delXsize, "Property for xsize")
    # Methods and properties for the 'ysize' attribute
    def getYsize(self): return self._ysize
    def setYsize(self, ysize):
        if ysize is None:
            self._ysize = None
        else:
            self._ysize = float(ysize)
    def delYsize(self): self._ysize = None
    ysize = property(getYsize, setYsize, delYsize, "Property for ysize")
    # Methods and properties for the 'xmin' attribute
    def getXmin(self): return self._xmin
    def setXmin(self, xmin):
        if xmin is None:
            self._xmin = None
        else:
            self._xmin = float(xmin)
    def delXmin(self): self._xmin = None
    xmin = property(getXmin, setXmin, delXmin, "Property for xmin")
    # Methods and properties for the 'ymin' attribute
    def getYmin(self): return self._ymin
    def setYmin(self, ymin):
        if ymin is None:
            self._ymin = None
        else:
            self._ymin = float(ymin)
    def delYmin(self): self._ymin = None
    ymin = property(getYmin, setYmin, delYmin, "Property for ymin")
    # Methods and properties for the 'xmax' attribute
    def getXmax(self): return self._xmax
    def setXmax(self, xmax):
        if xmax is None:
            self._xmax = None
        else:
            self._xmax = float(xmax)
    def delXmax(self): self._xmax = None
    xmax = property(getXmax, setXmax, delXmax, "Property for xmax")
    # Methods and properties for the 'ymax' attribute
    def getYmax(self): return self._ymax
    def setYmax(self, ymax):
        if ymax is None:
            self._ymax = None
        else:
            self._ymax = float(ymax)
    def delYmax(self): self._ymax = None
    ymax = property(getYmax, setYmax, delYmax, "Property for ymax")
    # Methods and properties for the 'keypos' attribute
    def getKeypos(self): return self._keypos
    def setKeypos(self, keypos):
        self._keypos = str(keypos)
    def delKeypos(self): self._keypos = None
    keypos = property(getKeypos, setKeypos, delKeypos, "Property for keypos")
    # Methods and properties for the 'xtitle' attribute
    def getXtitle(self): return self._xtitle
    def setXtitle(self, xtitle):
        self._xtitle = str(xtitle)
    def delXtitle(self): self._xtitle = None
    xtitle = property(getXtitle, setXtitle, delXtitle, "Property for xtitle")
    # Methods and properties for the 'ytitle' attribute
    def getYtitle(self): return self._ytitle
    def setYtitle(self, ytitle):
        self._ytitle = str(ytitle)
    def delYtitle(self): self._ytitle = None
    ytitle = property(getYtitle, setYtitle, delYtitle, "Property for ytitle")
    # Methods and properties for the 'graph' attribute
    def getGraph(self): return self._graph
    def setGraph(self, graph):
        if graph is None:
            self._graph = []
        elif graph.__class__.__name__ == "list":
            self._graph = graph
        else:
            strMessage = "ERROR! XSDataPlot.setGraph argument is not list but %s" % graph.__class__.__name__
            raise BaseException(strMessage)
    def delGraph(self): self._graph = None
    graph = property(getGraph, setGraph, delGraph, "Property for graph")
    def addGraph(self, value):
        if value is None:
            strMessage = "ERROR! XSDataPlot.addGraph argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataGraph":
            self._graph.append(value)
        else:
            strMessage = "ERROR! XSDataPlot.addGraph argument is not XSDataGraph but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertGraph(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataPlot.insertGraph argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataPlot.insertGraph argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataGraph":
            self._graph[index] = value
        else:
            strMessage = "ERROR! XSDataPlot.addGraph argument is not XSDataGraph but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataPlot'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPlot'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._plotType is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<plotType>%s</plotType>\n' % self._plotType))
        else:
            warnEmptyAttribute("plotType", "string")
        if self._title is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<title>%s</title>\n' % self._title))
        else:
            warnEmptyAttribute("title", "string")
        if self._subTitle is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<subTitle>%s</subTitle>\n' % self._subTitle))
        else:
            warnEmptyAttribute("subTitle", "string")
        if self._xsize is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xsize>%e</xsize>\n' % self._xsize))
        if self._ysize is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ysize>%e</ysize>\n' % self._ysize))
        if self._xmin is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xmin>%e</xmin>\n' % self._xmin))
        if self._ymin is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ymin>%e</ymin>\n' % self._ymin))
        if self._xmax is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xmax>%e</xmax>\n' % self._xmax))
        if self._ymax is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ymax>%e</ymax>\n' % self._ymax))
        if self._keypos is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<keypos>%s</keypos>\n' % self._keypos))
        if self._xtitle is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtitle>%s</xtitle>\n' % self._xtitle))
        else:
            warnEmptyAttribute("xtitle", "string")
        if self._ytitle is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ytitle>%s</ytitle>\n' % self._ytitle))
        else:
            warnEmptyAttribute("ytitle", "string")
        for graph_ in self.getGraph():
            graph_.export(outfile, level, name_='graph')
        if self.getGraph() == []:
            warnEmptyAttribute("graph", "XSDataGraph")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plotType':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._plotType = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'title':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._title = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subTitle':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._subTitle = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xsize':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._xsize = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ysize':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ysize = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmin':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._xmin = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ymin':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ymin = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmax':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._xmax = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ymax':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ymax = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'keypos':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._keypos = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtitle':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtitle = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ytitle':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._ytitle = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'graph':
            obj_ = XSDataGraph()
            obj_.build(child_)
            self.graph.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPlot" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPlot' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPlot is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPlot.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPlot()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPlot" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPlot()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPlot


class XSDataPlotSet(XSData):
    def __init__(self, plot=None):
        XSData.__init__(self, )
        if plot is None:
            self._plot = []
        elif plot.__class__.__name__ == "list":
            self._plot = plot
        else:
            strMessage = "ERROR! XSDataPlotSet constructor argument 'plot' is not list but %s" % self._plot.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'plot' attribute
    def getPlot(self): return self._plot
    def setPlot(self, plot):
        if plot is None:
            self._plot = []
        elif plot.__class__.__name__ == "list":
            self._plot = plot
        else:
            strMessage = "ERROR! XSDataPlotSet.setPlot argument is not list but %s" % plot.__class__.__name__
            raise BaseException(strMessage)
    def delPlot(self): self._plot = None
    plot = property(getPlot, setPlot, delPlot, "Property for plot")
    def addPlot(self, value):
        if value is None:
            strMessage = "ERROR! XSDataPlotSet.addPlot argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataPlot":
            self._plot.append(value)
        else:
            strMessage = "ERROR! XSDataPlotSet.addPlot argument is not XSDataPlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPlot(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataPlotSet.insertPlot argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataPlotSet.insertPlot argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataPlot":
            self._plot[index] = value
        else:
            strMessage = "ERROR! XSDataPlotSet.addPlot argument is not XSDataPlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataPlotSet'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPlotSet'):
        XSData.exportChildren(self, outfile, level, name_)
        for plot_ in self.getPlot():
            plot_.export(outfile, level, name_='plot')
        if self.getPlot() == []:
            warnEmptyAttribute("plot", "XSDataPlot")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plot':
            obj_ = XSDataPlot()
            obj_.build(child_)
            self.plot.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPlotSet" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPlotSet' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPlotSet is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPlotSet.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPlotSet()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPlotSet" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPlotSet()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPlotSet


class XSDataInputPlotGle(XSDataInput):
    def __init__(self, configuration=None, glePlot=None, filePlotMtv=None, plotSet=None):
        XSDataInput.__init__(self, configuration)
        if plotSet is None:
            self._plotSet = None
        elif plotSet.__class__.__name__ == "XSDataPlotSet":
            self._plotSet = plotSet
        else:
            strMessage = "ERROR! XSDataInputPlotGle constructor argument 'plotSet' is not XSDataPlotSet but %s" % self._plotSet.__class__.__name__
            raise BaseException(strMessage)
        if filePlotMtv is None:
            self._filePlotMtv = None
        elif filePlotMtv.__class__.__name__ == "XSDataFile":
            self._filePlotMtv = filePlotMtv
        else:
            strMessage = "ERROR! XSDataInputPlotGle constructor argument 'filePlotMtv' is not XSDataFile but %s" % self._filePlotMtv.__class__.__name__
            raise BaseException(strMessage)
        if glePlot is None:
            self._glePlot = []
        elif glePlot.__class__.__name__ == "list":
            self._glePlot = glePlot
        else:
            strMessage = "ERROR! XSDataInputPlotGle constructor argument 'glePlot' is not list but %s" % self._glePlot.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'plotSet' attribute
    def getPlotSet(self): return self._plotSet
    def setPlotSet(self, plotSet):
        if plotSet is None:
            self._plotSet = None
        elif plotSet.__class__.__name__ == "XSDataPlotSet":
            self._plotSet = plotSet
        else:
            strMessage = "ERROR! XSDataInputPlotGle.setPlotSet argument is not XSDataPlotSet but %s" % plotSet.__class__.__name__
            raise BaseException(strMessage)
    def delPlotSet(self): self._plotSet = None
    plotSet = property(getPlotSet, setPlotSet, delPlotSet, "Property for plotSet")
    # Methods and properties for the 'filePlotMtv' attribute
    def getFilePlotMtv(self): return self._filePlotMtv
    def setFilePlotMtv(self, filePlotMtv):
        if filePlotMtv is None:
            self._filePlotMtv = None
        elif filePlotMtv.__class__.__name__ == "XSDataFile":
            self._filePlotMtv = filePlotMtv
        else:
            strMessage = "ERROR! XSDataInputPlotGle.setFilePlotMtv argument is not XSDataFile but %s" % filePlotMtv.__class__.__name__
            raise BaseException(strMessage)
    def delFilePlotMtv(self): self._filePlotMtv = None
    filePlotMtv = property(getFilePlotMtv, setFilePlotMtv, delFilePlotMtv, "Property for filePlotMtv")
    # Methods and properties for the 'glePlot' attribute
    def getGlePlot(self): return self._glePlot
    def setGlePlot(self, glePlot):
        if glePlot is None:
            self._glePlot = []
        elif glePlot.__class__.__name__ == "list":
            self._glePlot = glePlot
        else:
            strMessage = "ERROR! XSDataInputPlotGle.setGlePlot argument is not list but %s" % glePlot.__class__.__name__
            raise BaseException(strMessage)
    def delGlePlot(self): self._glePlot = None
    glePlot = property(getGlePlot, setGlePlot, delGlePlot, "Property for glePlot")
    def addGlePlot(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputPlotGle.addGlePlot argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataGlePlot":
            self._glePlot.append(value)
        else:
            strMessage = "ERROR! XSDataInputPlotGle.addGlePlot argument is not XSDataGlePlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertGlePlot(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputPlotGle.insertGlePlot argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputPlotGle.insertGlePlot argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataGlePlot":
            self._glePlot[index] = value
        else:
            strMessage = "ERROR! XSDataInputPlotGle.addGlePlot argument is not XSDataGlePlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputPlotGle'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputPlotGle'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._plotSet is not None:
            self.plotSet.export(outfile, level, name_='plotSet')
        if self._filePlotMtv is not None:
            self.filePlotMtv.export(outfile, level, name_='filePlotMtv')
        for glePlot_ in self.getGlePlot():
            glePlot_.export(outfile, level, name_='glePlot')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plotSet':
            obj_ = XSDataPlotSet()
            obj_.build(child_)
            self.setPlotSet(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePlotMtv':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFilePlotMtv(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'glePlot':
            obj_ = XSDataGlePlot()
            obj_.build(child_)
            self.glePlot.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputPlotGle" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputPlotGle' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputPlotGle is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputPlotGle.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputPlotGle()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputPlotGle" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputPlotGle()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputPlotGle


class XSDataResultPlotGle(XSDataResult):
    def __init__(self, status=None, fileGraph=None):
        XSDataResult.__init__(self, status)
        if fileGraph is None:
            self._fileGraph = []
        elif fileGraph.__class__.__name__ == "list":
            self._fileGraph = fileGraph
        else:
            strMessage = "ERROR! XSDataResultPlotGle constructor argument 'fileGraph' is not list but %s" % self._fileGraph.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fileGraph' attribute
    def getFileGraph(self): return self._fileGraph
    def setFileGraph(self, fileGraph):
        if fileGraph is None:
            self._fileGraph = []
        elif fileGraph.__class__.__name__ == "list":
            self._fileGraph = fileGraph
        else:
            strMessage = "ERROR! XSDataResultPlotGle.setFileGraph argument is not list but %s" % fileGraph.__class__.__name__
            raise BaseException(strMessage)
    def delFileGraph(self): self._fileGraph = None
    fileGraph = property(getFileGraph, setFileGraph, delFileGraph, "Property for fileGraph")
    def addFileGraph(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultPlotGle.addFileGraph argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._fileGraph.append(value)
        else:
            strMessage = "ERROR! XSDataResultPlotGle.addFileGraph argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFileGraph(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultPlotGle.insertFileGraph argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultPlotGle.insertFileGraph argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._fileGraph[index] = value
        else:
            strMessage = "ERROR! XSDataResultPlotGle.addFileGraph argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultPlotGle'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultPlotGle'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for fileGraph_ in self.getFileGraph():
            fileGraph_.export(outfile, level, name_='fileGraph')
        if self.getFileGraph() == []:
            warnEmptyAttribute("fileGraph", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileGraph':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.fileGraph.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultPlotGle" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultPlotGle' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultPlotGle is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultPlotGle.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultPlotGle()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultPlotGle" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultPlotGle()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultPlotGle



# End of data representation classes.



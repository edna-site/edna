#!/usr/bin/env python

#
# Generated Wed Feb 8 03:08::14 2012 by EDGenerateDS.
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


def checkType(_strClassName, _strMethodName, _value, _strExpectedType):
	if not _strExpectedType in ["float", "double", "string", "boolean", "integer"]:
		if _value != None:
			if _value.__class__.__name__ != _strExpectedType:
				strMessage = "ERROR! %s.%s argument is not %s but %s" % (_strClassName, _strMethodName, _strExpectedType, _value.__class__.__name__)
				print(strMessage)
				#raise BaseException(strMessage)
#	elif _value is None:
#		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
#		print(strMessage)
#		#raise BaseException(strMessage)


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
		else:	 # category == MixedContainer.CategoryComplex
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


class XSDataGraph(XSData):
	def __init__(self, data=None, markerColor=None, markerType=None, label=None, lineColor=None, lineWidth=None, lineStyle=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineStyle, "string")
		self._lineStyle = lineStyle
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineWidth, "double")
		self._lineWidth = lineWidth
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineColor, "string")
		self._lineColor = lineColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", label, "string")
		self._label = label
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerType, "string")
		self._markerType = markerType
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerColor, "string")
		self._markerColor = markerColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", data, "XSDataArray")
		self._data = data
	def getLineStyle(self): return self._lineStyle
	def setLineStyle(self, lineStyle):
		checkType("XSDataGraph", "setLineStyle", lineStyle, "string")
		self._lineStyle = lineStyle
	def delLineStyle(self): self._lineStyle = None
	# Properties
	lineStyle = property(getLineStyle, setLineStyle, delLineStyle, "Property for lineStyle")
	def getLineWidth(self): return self._lineWidth
	def setLineWidth(self, lineWidth):
		checkType("XSDataGraph", "setLineWidth", lineWidth, "double")
		self._lineWidth = lineWidth
	def delLineWidth(self): self._lineWidth = None
	# Properties
	lineWidth = property(getLineWidth, setLineWidth, delLineWidth, "Property for lineWidth")
	def getLineColor(self): return self._lineColor
	def setLineColor(self, lineColor):
		checkType("XSDataGraph", "setLineColor", lineColor, "string")
		self._lineColor = lineColor
	def delLineColor(self): self._lineColor = None
	# Properties
	lineColor = property(getLineColor, setLineColor, delLineColor, "Property for lineColor")
	def getLabel(self): return self._label
	def setLabel(self, label):
		checkType("XSDataGraph", "setLabel", label, "string")
		self._label = label
	def delLabel(self): self._label = None
	# Properties
	label = property(getLabel, setLabel, delLabel, "Property for label")
	def getMarkerType(self): return self._markerType
	def setMarkerType(self, markerType):
		checkType("XSDataGraph", "setMarkerType", markerType, "string")
		self._markerType = markerType
	def delMarkerType(self): self._markerType = None
	# Properties
	markerType = property(getMarkerType, setMarkerType, delMarkerType, "Property for markerType")
	def getMarkerColor(self): return self._markerColor
	def setMarkerColor(self, markerColor):
		checkType("XSDataGraph", "setMarkerColor", markerColor, "string")
		self._markerColor = markerColor
	def delMarkerColor(self): self._markerColor = None
	# Properties
	markerColor = property(getMarkerColor, setMarkerColor, delMarkerColor, "Property for markerColor")
	def getData(self): return self._data
	def setData(self, data):
		checkType("XSDataGraph", "setData", data, "XSDataArray")
		self._data = data
	def delData(self): self._data = None
	# Properties
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
	def __init__(self, graph=None, ytitle=None, xtitle=None, ymax=None, xmax=None, ymin=None, xmin=None, subTitle=None, title=None, plotType=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataPlot", "Constructor of XSDataPlot", plotType, "string")
		self._plotType = plotType
		checkType("XSDataPlot", "Constructor of XSDataPlot", title, "string")
		self._title = title
		checkType("XSDataPlot", "Constructor of XSDataPlot", subTitle, "string")
		self._subTitle = subTitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", xmin, "double")
		self._xmin = xmin
		checkType("XSDataPlot", "Constructor of XSDataPlot", ymin, "double")
		self._ymin = ymin
		checkType("XSDataPlot", "Constructor of XSDataPlot", xmax, "double")
		self._xmax = xmax
		checkType("XSDataPlot", "Constructor of XSDataPlot", ymax, "double")
		self._ymax = ymax
		checkType("XSDataPlot", "Constructor of XSDataPlot", xtitle, "string")
		self._xtitle = xtitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", ytitle, "string")
		self._ytitle = ytitle
		if graph is None:
			self._graph = []
		else:
			checkType("XSDataPlot", "Constructor of XSDataPlot", graph, "list")
			self._graph = graph
	def getPlotType(self): return self._plotType
	def setPlotType(self, plotType):
		checkType("XSDataPlot", "setPlotType", plotType, "string")
		self._plotType = plotType
	def delPlotType(self): self._plotType = None
	# Properties
	plotType = property(getPlotType, setPlotType, delPlotType, "Property for plotType")
	def getTitle(self): return self._title
	def setTitle(self, title):
		checkType("XSDataPlot", "setTitle", title, "string")
		self._title = title
	def delTitle(self): self._title = None
	# Properties
	title = property(getTitle, setTitle, delTitle, "Property for title")
	def getSubTitle(self): return self._subTitle
	def setSubTitle(self, subTitle):
		checkType("XSDataPlot", "setSubTitle", subTitle, "string")
		self._subTitle = subTitle
	def delSubTitle(self): self._subTitle = None
	# Properties
	subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
	def getXmin(self): return self._xmin
	def setXmin(self, xmin):
		checkType("XSDataPlot", "setXmin", xmin, "double")
		self._xmin = xmin
	def delXmin(self): self._xmin = None
	# Properties
	xmin = property(getXmin, setXmin, delXmin, "Property for xmin")
	def getYmin(self): return self._ymin
	def setYmin(self, ymin):
		checkType("XSDataPlot", "setYmin", ymin, "double")
		self._ymin = ymin
	def delYmin(self): self._ymin = None
	# Properties
	ymin = property(getYmin, setYmin, delYmin, "Property for ymin")
	def getXmax(self): return self._xmax
	def setXmax(self, xmax):
		checkType("XSDataPlot", "setXmax", xmax, "double")
		self._xmax = xmax
	def delXmax(self): self._xmax = None
	# Properties
	xmax = property(getXmax, setXmax, delXmax, "Property for xmax")
	def getYmax(self): return self._ymax
	def setYmax(self, ymax):
		checkType("XSDataPlot", "setYmax", ymax, "double")
		self._ymax = ymax
	def delYmax(self): self._ymax = None
	# Properties
	ymax = property(getYmax, setYmax, delYmax, "Property for ymax")
	def getXtitle(self): return self._xtitle
	def setXtitle(self, xtitle):
		checkType("XSDataPlot", "setXtitle", xtitle, "string")
		self._xtitle = xtitle
	def delXtitle(self): self._xtitle = None
	# Properties
	xtitle = property(getXtitle, setXtitle, delXtitle, "Property for xtitle")
	def getYtitle(self): return self._ytitle
	def setYtitle(self, ytitle):
		checkType("XSDataPlot", "setYtitle", ytitle, "string")
		self._ytitle = ytitle
	def delYtitle(self): self._ytitle = None
	# Properties
	ytitle = property(getYtitle, setYtitle, delYtitle, "Property for ytitle")
	def getGraph(self): return self._graph
	def setGraph(self, graph):
		checkType("XSDataPlot", "setGraph", graph, "list")
		self._graph = graph
	def delGraph(self): self._graph = None
	# Properties
	graph = property(getGraph, setGraph, delGraph, "Property for graph")
	def addGraph(self, value):
		checkType("XSDataPlot", "setGraph", value, "XSDataGraph")
		self._graph.append(value)
	def insertGraph(self, index, value):
		checkType("XSDataPlot", "setGraph", value, "XSDataGraph")
		self._graph[index] = value
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
		else:
			checkType("XSDataPlotSet", "Constructor of XSDataPlotSet", plot, "list")
			self._plot = plot
	def getPlot(self): return self._plot
	def setPlot(self, plot):
		checkType("XSDataPlotSet", "setPlot", plot, "list")
		self._plot = plot
	def delPlot(self): self._plot = None
	# Properties
	plot = property(getPlot, setPlot, delPlot, "Property for plot")
	def addPlot(self, value):
		checkType("XSDataPlotSet", "setPlot", value, "XSDataPlot")
		self._plot.append(value)
	def insertPlot(self, index, value):
		checkType("XSDataPlotSet", "setPlot", value, "XSDataPlot")
		self._plot[index] = value
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
	def __init__(self, configuration=None, filePlotMtv=None, plotSet=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputPlotGle", "Constructor of XSDataInputPlotGle", plotSet, "XSDataPlotSet")
		self._plotSet = plotSet
		checkType("XSDataInputPlotGle", "Constructor of XSDataInputPlotGle", filePlotMtv, "XSDataFile")
		self._filePlotMtv = filePlotMtv
	def getPlotSet(self): return self._plotSet
	def setPlotSet(self, plotSet):
		checkType("XSDataInputPlotGle", "setPlotSet", plotSet, "XSDataPlotSet")
		self._plotSet = plotSet
	def delPlotSet(self): self._plotSet = None
	# Properties
	plotSet = property(getPlotSet, setPlotSet, delPlotSet, "Property for plotSet")
	def getFilePlotMtv(self): return self._filePlotMtv
	def setFilePlotMtv(self, filePlotMtv):
		checkType("XSDataInputPlotGle", "setFilePlotMtv", filePlotMtv, "XSDataFile")
		self._filePlotMtv = filePlotMtv
	def delFilePlotMtv(self): self._filePlotMtv = None
	# Properties
	filePlotMtv = property(getFilePlotMtv, setFilePlotMtv, delFilePlotMtv, "Property for filePlotMtv")
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
	def __init__(self, status=None):
		XSDataResult.__init__(self, status)
	
	
	def export(self, outfile, level, name_='XSDataResultPlotGle'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultPlotGle'):
		XSDataResult.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
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



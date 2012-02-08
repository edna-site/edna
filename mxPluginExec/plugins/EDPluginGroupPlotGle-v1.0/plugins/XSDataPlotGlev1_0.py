#!/usr/bin/env python

#
# Generated Wed Feb 8 08:39::43 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "datamodel", \
 "XSDataCommon": "datamodel", \
 "XSDataCommon": "datamodel", \
 "XSDataCommon": "datamodel", \
 "XSDataCommon": "datamodel", \
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
	pass
	#if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
	#		print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

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
	def __init__(self, data=None, markerColor=None, markerType=None, lineLabel=None, lineColor=None, lineWidth=None, lineType=None):
		XSData.__init__(self, )
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineType, "string")
		self.__lineType = lineType
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineWidth, "integer")
		self.__lineWidth = lineWidth
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineColor, "string")
		self.__lineColor = lineColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineLabel, "string")
		self.__lineLabel = lineLabel
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerType, "integer")
		self.__markerType = markerType
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerColor, "string")
		self.__markerColor = markerColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", data, "XSDataArray")
		self.__data = data
	def getLineType(self): return self.__lineType
	def setLineType(self, lineType):
		checkType("XSDataGraph", "setLineType", lineType, "string")
		self.__lineType = lineType
	def delLineType(self): self.__lineType = None
	# Properties
	lineType = property(getLineType, setLineType, delLineType, "Property for lineType")
	def getLineWidth(self): return self.__lineWidth
	def setLineWidth(self, lineWidth):
		checkType("XSDataGraph", "setLineWidth", lineWidth, "integer")
		self.__lineWidth = lineWidth
	def delLineWidth(self): self.__lineWidth = None
	# Properties
	lineWidth = property(getLineWidth, setLineWidth, delLineWidth, "Property for lineWidth")
	def getLineColor(self): return self.__lineColor
	def setLineColor(self, lineColor):
		checkType("XSDataGraph", "setLineColor", lineColor, "string")
		self.__lineColor = lineColor
	def delLineColor(self): self.__lineColor = None
	# Properties
	lineColor = property(getLineColor, setLineColor, delLineColor, "Property for lineColor")
	def getLineLabel(self): return self.__lineLabel
	def setLineLabel(self, lineLabel):
		checkType("XSDataGraph", "setLineLabel", lineLabel, "string")
		self.__lineLabel = lineLabel
	def delLineLabel(self): self.__lineLabel = None
	# Properties
	lineLabel = property(getLineLabel, setLineLabel, delLineLabel, "Property for lineLabel")
	def getMarkerType(self): return self.__markerType
	def setMarkerType(self, markerType):
		checkType("XSDataGraph", "setMarkerType", markerType, "integer")
		self.__markerType = markerType
	def delMarkerType(self): self.__markerType = None
	# Properties
	markerType = property(getMarkerType, setMarkerType, delMarkerType, "Property for markerType")
	def getMarkerColor(self): return self.__markerColor
	def setMarkerColor(self, markerColor):
		checkType("XSDataGraph", "setMarkerColor", markerColor, "string")
		self.__markerColor = markerColor
	def delMarkerColor(self): self.__markerColor = None
	# Properties
	markerColor = property(getMarkerColor, setMarkerColor, delMarkerColor, "Property for markerColor")
	def getData(self): return self.__data
	def setData(self, data):
		checkType("XSDataGraph", "setData", data, "XSDataArray")
		self.__data = data
	def delData(self): self.__data = None
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
		if self.__lineType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineType>%s</lineType>\n' % self.__lineType))
		else:
			warnEmptyAttribute("lineType", "string")
		if self.__lineWidth is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineWidth>%d</lineWidth>\n' % self.__lineWidth))
		else:
			warnEmptyAttribute("lineWidth", "integer")
		if self.__lineColor is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineColor>%s</lineColor>\n' % self.__lineColor))
		else:
			warnEmptyAttribute("lineColor", "string")
		if self.__lineLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineLabel>%s</lineLabel>\n' % self.__lineLabel))
		else:
			warnEmptyAttribute("lineLabel", "string")
		if self.__markerType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<markerType>%d</markerType>\n' % self.__markerType))
		else:
			warnEmptyAttribute("markerType", "integer")
		if self.__markerColor is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<markerColor>%s</markerColor>\n' % self.__markerColor))
		else:
			warnEmptyAttribute("markerColor", "string")
		if self.__data is not None:
			self.data.export(outfile, level, name_='data')
		else:
			warnEmptyAttribute("data", "XSDataArray")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__lineType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineWidth':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__lineWidth = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineColor':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__lineColor = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__lineLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerType':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__markerType = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerColor':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__markerColor = value_
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
	def __init__(self, graph=None, yLabel=None, xLabel=None, yMax=None, xMax=None, yMin=None, xMin=None, subTitle=None, topLabel=None, plotType=None):
		XSData.__init__(self, )
		checkType("XSDataPlot", "Constructor of XSDataPlot", plotType, "string")
		self.__plotType = plotType
		checkType("XSDataPlot", "Constructor of XSDataPlot", topLabel, "string")
		self.__topLabel = topLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", subTitle, "string")
		self.__subTitle = subTitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMin, "double")
		self.__xMin = xMin
		checkType("XSDataPlot", "Constructor of XSDataPlot", yMin, "double")
		self.__yMin = yMin
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMax, "double")
		self.__xMax = xMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", yMax, "double")
		self.__yMax = yMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", xLabel, "string")
		self.__xLabel = xLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", yLabel, "string")
		self.__yLabel = yLabel
		if graph is None:
			self.__graph = []
		else:
			checkType("XSDataPlot", "Constructor of XSDataPlot", graph, "list")
			self.__graph = graph
	def getPlotType(self): return self.__plotType
	def setPlotType(self, plotType):
		checkType("XSDataPlot", "setPlotType", plotType, "string")
		self.__plotType = plotType
	def delPlotType(self): self.__plotType = None
	# Properties
	plotType = property(getPlotType, setPlotType, delPlotType, "Property for plotType")
	def getTopLabel(self): return self.__topLabel
	def setTopLabel(self, topLabel):
		checkType("XSDataPlot", "setTopLabel", topLabel, "string")
		self.__topLabel = topLabel
	def delTopLabel(self): self.__topLabel = None
	# Properties
	topLabel = property(getTopLabel, setTopLabel, delTopLabel, "Property for topLabel")
	def getSubTitle(self): return self.__subTitle
	def setSubTitle(self, subTitle):
		checkType("XSDataPlot", "setSubTitle", subTitle, "string")
		self.__subTitle = subTitle
	def delSubTitle(self): self.__subTitle = None
	# Properties
	subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
	def getXMin(self): return self.__xMin
	def setXMin(self, xMin):
		checkType("XSDataPlot", "setXMin", xMin, "double")
		self.__xMin = xMin
	def delXMin(self): self.__xMin = None
	# Properties
	xMin = property(getXMin, setXMin, delXMin, "Property for xMin")
	def getYMin(self): return self.__yMin
	def setYMin(self, yMin):
		checkType("XSDataPlot", "setYMin", yMin, "double")
		self.__yMin = yMin
	def delYMin(self): self.__yMin = None
	# Properties
	yMin = property(getYMin, setYMin, delYMin, "Property for yMin")
	def getXMax(self): return self.__xMax
	def setXMax(self, xMax):
		checkType("XSDataPlot", "setXMax", xMax, "double")
		self.__xMax = xMax
	def delXMax(self): self.__xMax = None
	# Properties
	xMax = property(getXMax, setXMax, delXMax, "Property for xMax")
	def getYMax(self): return self.__yMax
	def setYMax(self, yMax):
		checkType("XSDataPlot", "setYMax", yMax, "double")
		self.__yMax = yMax
	def delYMax(self): self.__yMax = None
	# Properties
	yMax = property(getYMax, setYMax, delYMax, "Property for yMax")
	def getXLabel(self): return self.__xLabel
	def setXLabel(self, xLabel):
		checkType("XSDataPlot", "setXLabel", xLabel, "string")
		self.__xLabel = xLabel
	def delXLabel(self): self.__xLabel = None
	# Properties
	xLabel = property(getXLabel, setXLabel, delXLabel, "Property for xLabel")
	def getYLabel(self): return self.__yLabel
	def setYLabel(self, yLabel):
		checkType("XSDataPlot", "setYLabel", yLabel, "string")
		self.__yLabel = yLabel
	def delYLabel(self): self.__yLabel = None
	# Properties
	yLabel = property(getYLabel, setYLabel, delYLabel, "Property for yLabel")
	def getGraph(self): return self.__graph
	def setGraph(self, graph):
		checkType("XSDataPlot", "setGraph", graph, "list")
		self.__graph = graph
	def delGraph(self): self.__graph = None
	# Properties
	graph = property(getGraph, setGraph, delGraph, "Property for graph")
	def addGraph(self, value):
		checkType("XSDataPlot", "setGraph", value, "XSDataGraph")
		self.__graph.append(value)
	def insertGraph(self, index, value):
		checkType("XSDataPlot", "setGraph", value, "XSDataGraph")
		self.__graph[index] = value
	def export(self, outfile, level, name_='XSDataPlot'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataPlot'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__plotType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<plotType>%s</plotType>\n' % self.__plotType))
		else:
			warnEmptyAttribute("plotType", "string")
		if self.__topLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<topLabel>%s</topLabel>\n' % self.__topLabel))
		else:
			warnEmptyAttribute("topLabel", "string")
		if self.__subTitle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<subTitle>%s</subTitle>\n' % self.__subTitle))
		else:
			warnEmptyAttribute("subTitle", "string")
		if self.__xMin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xMin>%e</xMin>\n' % self.__xMin))
		if self.__yMin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yMin>%e</yMin>\n' % self.__yMin))
		if self.__xMax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xMax>%e</xMax>\n' % self.__xMax))
		if self.__yMax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yMax>%e</yMax>\n' % self.__yMax))
		if self.__xLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xLabel>%s</xLabel>\n' % self.__xLabel))
		else:
			warnEmptyAttribute("xLabel", "string")
		if self.__yLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yLabel>%s</yLabel>\n' % self.__yLabel))
		else:
			warnEmptyAttribute("yLabel", "string")
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
			self.__plotType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'topLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__topLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subTitle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__subTitle = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xMin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yMin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__yMin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xMax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yMax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__yMax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__yLabel = value_
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
			self.__plot = []
		else:
			checkType("XSDataPlotSet", "Constructor of XSDataPlotSet", plot, "list")
			self.__plot = plot
	def getPlot(self): return self.__plot
	def setPlot(self, plot):
		checkType("XSDataPlotSet", "setPlot", plot, "list")
		self.__plot = plot
	def delPlot(self): self.__plot = None
	# Properties
	plot = property(getPlot, setPlot, delPlot, "Property for plot")
	def addPlot(self, value):
		checkType("XSDataPlotSet", "setPlot", value, "XSDataPlot")
		self.__plot.append(value)
	def insertPlot(self, index, value):
		checkType("XSDataPlotSet", "setPlot", value, "XSDataPlot")
		self.__plot[index] = value
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
		self.__plotSet = plotSet
		checkType("XSDataInputPlotGle", "Constructor of XSDataInputPlotGle", filePlotMtv, "XSDataFile")
		self.__filePlotMtv = filePlotMtv
	def getPlotSet(self): return self.__plotSet
	def setPlotSet(self, plotSet):
		checkType("XSDataInputPlotGle", "setPlotSet", plotSet, "XSDataPlotSet")
		self.__plotSet = plotSet
	def delPlotSet(self): self.__plotSet = None
	# Properties
	plotSet = property(getPlotSet, setPlotSet, delPlotSet, "Property for plotSet")
	def getFilePlotMtv(self): return self.__filePlotMtv
	def setFilePlotMtv(self, filePlotMtv):
		checkType("XSDataInputPlotGle", "setFilePlotMtv", filePlotMtv, "XSDataFile")
		self.__filePlotMtv = filePlotMtv
	def delFilePlotMtv(self): self.__filePlotMtv = None
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
		if self.__plotSet is not None:
			self.plotSet.export(outfile, level, name_='plotSet')
		if self.__filePlotMtv is not None:
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



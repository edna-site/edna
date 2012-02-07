#!/usr/bin/env python

#
# Generated Tue Feb 7 04:21::13 2012 by EDGenerateDS.
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
	from XSDataCommon import XSData
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
	def __init__(self, yData=None, xData=None, markerColor=None, markerType=None, lineLabel=None, lineColor=None, lineWidth=None, lineType=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineType, "string")
		self._lineType = lineType
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineWidth, "integer")
		self._lineWidth = lineWidth
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineColor, "string")
		self._lineColor = lineColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineLabel, "string")
		self._lineLabel = lineLabel
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerType, "integer")
		self._markerType = markerType
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerColor, "string")
		self._markerColor = markerColor
		if xData is None:
			self._xData = []
		else:
			checkType("XSDataGraph", "Constructor of XSDataGraph", xData, "list")
			self._xData = xData
		if yData is None:
			self._yData = []
		else:
			checkType("XSDataGraph", "Constructor of XSDataGraph", yData, "list")
			self._yData = yData
	def getLineType(self): return self._lineType
	def setLineType(self, lineType):
		checkType("XSDataGraph", "setLineType", lineType, "string")
		self._lineType = lineType
	def delLineType(self): self._lineType = None
	# Properties
	lineType = property(getLineType, setLineType, delLineType, "Property for lineType")
	def getLineWidth(self): return self._lineWidth
	def setLineWidth(self, lineWidth):
		checkType("XSDataGraph", "setLineWidth", lineWidth, "integer")
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
	def getLineLabel(self): return self._lineLabel
	def setLineLabel(self, lineLabel):
		checkType("XSDataGraph", "setLineLabel", lineLabel, "string")
		self._lineLabel = lineLabel
	def delLineLabel(self): self._lineLabel = None
	# Properties
	lineLabel = property(getLineLabel, setLineLabel, delLineLabel, "Property for lineLabel")
	def getMarkerType(self): return self._markerType
	def setMarkerType(self, markerType):
		checkType("XSDataGraph", "setMarkerType", markerType, "integer")
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
	def getXData(self): return self._xData
	def setXData(self, xData):
		checkType("XSDataGraph", "setXData", xData, "list")
		self._xData = xData
	def delXData(self): self._xData = None
	# Properties
	xData = property(getXData, setXData, delXData, "Property for xData")
	def addXData(self, value):
		checkType("XSDataGraph", "setXData", value, "double")
		self._xData.append(value)
	def insertXData(self, index, value):
		checkType("XSDataGraph", "setXData", value, "double")
		self._xData[index] = value
	def getYData(self): return self._yData
	def setYData(self, yData):
		checkType("XSDataGraph", "setYData", yData, "list")
		self._yData = yData
	def delYData(self): self._yData = None
	# Properties
	yData = property(getYData, setYData, delYData, "Property for yData")
	def addYData(self, value):
		checkType("XSDataGraph", "setYData", value, "double")
		self._yData.append(value)
	def insertYData(self, index, value):
		checkType("XSDataGraph", "setYData", value, "double")
		self._yData[index] = value
	def export(self, outfile, level, name_='XSDataGraph'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGraph'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._lineType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineType>%s</lineType>\n' % self._lineType))
		else:
			warnEmptyAttribute("lineType", "string")
		if self._lineWidth is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineWidth>%d</lineWidth>\n' % self._lineWidth))
		else:
			warnEmptyAttribute("lineWidth", "integer")
		if self._lineColor is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineColor>%s</lineColor>\n' % self._lineColor))
		else:
			warnEmptyAttribute("lineColor", "string")
		if self._lineLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineLabel>%s</lineLabel>\n' % self._lineLabel))
		else:
			warnEmptyAttribute("lineLabel", "string")
		if self._markerType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<markerType>%d</markerType>\n' % self._markerType))
		else:
			warnEmptyAttribute("markerType", "integer")
		if self._markerColor is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<markerColor>%s</markerColor>\n' % self._markerColor))
		else:
			warnEmptyAttribute("markerColor", "string")
		for xData_ in self.getXData():
			showIndent(outfile, level)
			outfile.write(unicode('<xData>%e</xData>\n' % xData_))
		if self.getXData() == []:
			warnEmptyAttribute("xData", "double")
		for yData_ in self.getYData():
			showIndent(outfile, level)
			outfile.write(unicode('<yData>%e</yData>\n' % yData_))
		if self.getYData() == []:
			warnEmptyAttribute("yData", "double")
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
			self._lineType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineWidth':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._lineWidth = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineColor':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._lineColor = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._lineLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerType':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._markerType = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerColor':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._markerColor = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xData':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._xData.append(fval_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yData':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._yData.append(fval_)
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
		self._plotType = plotType
		checkType("XSDataPlot", "Constructor of XSDataPlot", topLabel, "string")
		self._topLabel = topLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", subTitle, "string")
		self._subTitle = subTitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMin, "double")
		self._xMin = xMin
		checkType("XSDataPlot", "Constructor of XSDataPlot", yMin, "double")
		self._yMin = yMin
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMax, "double")
		self._xMax = xMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", yMax, "double")
		self._yMax = yMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", xLabel, "string")
		self._xLabel = xLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", yLabel, "string")
		self._yLabel = yLabel
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
	def getTopLabel(self): return self._topLabel
	def setTopLabel(self, topLabel):
		checkType("XSDataPlot", "setTopLabel", topLabel, "string")
		self._topLabel = topLabel
	def delTopLabel(self): self._topLabel = None
	# Properties
	topLabel = property(getTopLabel, setTopLabel, delTopLabel, "Property for topLabel")
	def getSubTitle(self): return self._subTitle
	def setSubTitle(self, subTitle):
		checkType("XSDataPlot", "setSubTitle", subTitle, "string")
		self._subTitle = subTitle
	def delSubTitle(self): self._subTitle = None
	# Properties
	subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
	def getXMin(self): return self._xMin
	def setXMin(self, xMin):
		checkType("XSDataPlot", "setXMin", xMin, "double")
		self._xMin = xMin
	def delXMin(self): self._xMin = None
	# Properties
	xMin = property(getXMin, setXMin, delXMin, "Property for xMin")
	def getYMin(self): return self._yMin
	def setYMin(self, yMin):
		checkType("XSDataPlot", "setYMin", yMin, "double")
		self._yMin = yMin
	def delYMin(self): self._yMin = None
	# Properties
	yMin = property(getYMin, setYMin, delYMin, "Property for yMin")
	def getXMax(self): return self._xMax
	def setXMax(self, xMax):
		checkType("XSDataPlot", "setXMax", xMax, "double")
		self._xMax = xMax
	def delXMax(self): self._xMax = None
	# Properties
	xMax = property(getXMax, setXMax, delXMax, "Property for xMax")
	def getYMax(self): return self._yMax
	def setYMax(self, yMax):
		checkType("XSDataPlot", "setYMax", yMax, "double")
		self._yMax = yMax
	def delYMax(self): self._yMax = None
	# Properties
	yMax = property(getYMax, setYMax, delYMax, "Property for yMax")
	def getXLabel(self): return self._xLabel
	def setXLabel(self, xLabel):
		checkType("XSDataPlot", "setXLabel", xLabel, "string")
		self._xLabel = xLabel
	def delXLabel(self): self._xLabel = None
	# Properties
	xLabel = property(getXLabel, setXLabel, delXLabel, "Property for xLabel")
	def getYLabel(self): return self._yLabel
	def setYLabel(self, yLabel):
		checkType("XSDataPlot", "setYLabel", yLabel, "string")
		self._yLabel = yLabel
	def delYLabel(self): self._yLabel = None
	# Properties
	yLabel = property(getYLabel, setYLabel, delYLabel, "Property for yLabel")
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
		if self._topLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<topLabel>%s</topLabel>\n' % self._topLabel))
		else:
			warnEmptyAttribute("topLabel", "string")
		if self._subTitle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<subTitle>%s</subTitle>\n' % self._subTitle))
		else:
			warnEmptyAttribute("subTitle", "string")
		if self._xMin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xMin>%e</xMin>\n' % self._xMin))
		if self._yMin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yMin>%e</yMin>\n' % self._yMin))
		if self._xMax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xMax>%e</xMax>\n' % self._xMax))
		if self._yMax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yMax>%e</yMax>\n' % self._yMax))
		if self._xLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xLabel>%s</xLabel>\n' % self._xLabel))
		else:
			warnEmptyAttribute("xLabel", "string")
		if self._yLabel is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<yLabel>%s</yLabel>\n' % self._yLabel))
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
			self._plotType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'topLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._topLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subTitle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._subTitle = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._xMin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yMin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._yMin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._xMax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yMax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._yMax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._xLabel = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yLabel':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._yLabel = value_
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



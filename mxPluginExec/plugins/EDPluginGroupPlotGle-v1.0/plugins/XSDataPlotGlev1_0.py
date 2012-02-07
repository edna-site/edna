#!/usr/bin/env python

#
# Generated Tue Feb 7 11:08::05 2012 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
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
from XSDataCommon import XSData
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
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
	
	
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineType, "XSDataString")
		self._lineType = lineType
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineWidth, "XSDataInteger")
		self._lineWidth = lineWidth
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineColor, "XSDataString")
		self._lineColor = lineColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineLabel, "XSDataString")
		self._lineLabel = lineLabel
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerType, "XSDataInteger")
		self._markerType = markerType
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerColor, "XSDataString")
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
		checkType("XSDataGraph", "setLineType", lineType, "XSDataString")
		self._lineType = lineType
	def delLineType(self): self._lineType = None
	# Properties
	lineType = property(getLineType, setLineType, delLineType, "Property for lineType")
	def getLineWidth(self): return self._lineWidth
	def setLineWidth(self, lineWidth):
		checkType("XSDataGraph", "setLineWidth", lineWidth, "XSDataInteger")
		self._lineWidth = lineWidth
	def delLineWidth(self): self._lineWidth = None
	# Properties
	lineWidth = property(getLineWidth, setLineWidth, delLineWidth, "Property for lineWidth")
	def getLineColor(self): return self._lineColor
	def setLineColor(self, lineColor):
		checkType("XSDataGraph", "setLineColor", lineColor, "XSDataString")
		self._lineColor = lineColor
	def delLineColor(self): self._lineColor = None
	# Properties
	lineColor = property(getLineColor, setLineColor, delLineColor, "Property for lineColor")
	def getLineLabel(self): return self._lineLabel
	def setLineLabel(self, lineLabel):
		checkType("XSDataGraph", "setLineLabel", lineLabel, "XSDataString")
		self._lineLabel = lineLabel
	def delLineLabel(self): self._lineLabel = None
	# Properties
	lineLabel = property(getLineLabel, setLineLabel, delLineLabel, "Property for lineLabel")
	def getMarkerType(self): return self._markerType
	def setMarkerType(self, markerType):
		checkType("XSDataGraph", "setMarkerType", markerType, "XSDataInteger")
		self._markerType = markerType
	def delMarkerType(self): self._markerType = None
	# Properties
	markerType = property(getMarkerType, setMarkerType, delMarkerType, "Property for markerType")
	def getMarkerColor(self): return self._markerColor
	def setMarkerColor(self, markerColor):
		checkType("XSDataGraph", "setMarkerColor", markerColor, "XSDataString")
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
		checkType("XSDataGraph", "setXData", value, "XSDataDouble")
		self._xData.append(value)
	def insertXData(self, index, value):
		checkType("XSDataGraph", "setXData", value, "XSDataDouble")
		self._xData[index] = value
	def getYData(self): return self._yData
	def setYData(self, yData):
		checkType("XSDataGraph", "setYData", yData, "list")
		self._yData = yData
	def delYData(self): self._yData = None
	# Properties
	yData = property(getYData, setYData, delYData, "Property for yData")
	def addYData(self, value):
		checkType("XSDataGraph", "setYData", value, "XSDataDouble")
		self._yData.append(value)
	def insertYData(self, index, value):
		checkType("XSDataGraph", "setYData", value, "XSDataDouble")
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
			self.lineType.export(outfile, level, name_='lineType')
		else:
			warnEmptyAttribute("lineType", "XSDataString")
		if self._lineWidth is not None:
			self.lineWidth.export(outfile, level, name_='lineWidth')
		else:
			warnEmptyAttribute("lineWidth", "XSDataInteger")
		if self._lineColor is not None:
			self.lineColor.export(outfile, level, name_='lineColor')
		else:
			warnEmptyAttribute("lineColor", "XSDataString")
		if self._lineLabel is not None:
			self.lineLabel.export(outfile, level, name_='lineLabel')
		else:
			warnEmptyAttribute("lineLabel", "XSDataString")
		if self._markerType is not None:
			self.markerType.export(outfile, level, name_='markerType')
		else:
			warnEmptyAttribute("markerType", "XSDataInteger")
		if self._markerColor is not None:
			self.markerColor.export(outfile, level, name_='markerColor')
		else:
			warnEmptyAttribute("markerColor", "XSDataString")
		for xData_ in self.getXData():
			xData_.export(outfile, level, name_='xData')
		if self.getXData() == []:
			warnEmptyAttribute("xData", "XSDataDouble")
		for yData_ in self.getYData():
			yData_.export(outfile, level, name_='yData')
		if self.getYData() == []:
			warnEmptyAttribute("yData", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLineType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineWidth':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setLineWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineColor':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLineColor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineLabel':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLineLabel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerType':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setMarkerType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerColor':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMarkerColor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xData':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.xData.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yData':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.yData.append(obj_)
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
	def __init__(self, graph=None, yLabel=None, xLabel=None, yMax=None, xMax=None, ymin=None, xMin=None, subTitle=None, topLabel=None, plotType=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataPlot", "Constructor of XSDataPlot", plotType, "XSDataString")
		self._plotType = plotType
		checkType("XSDataPlot", "Constructor of XSDataPlot", topLabel, "XSDataString")
		self._topLabel = topLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", subTitle, "XSDataString")
		self._subTitle = subTitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMin, "XSDataDouble")
		self._xMin = xMin
		checkType("XSDataPlot", "Constructor of XSDataPlot", ymin, "XSDataDouble")
		self._ymin = ymin
		checkType("XSDataPlot", "Constructor of XSDataPlot", xMax, "XSDataDouble")
		self._xMax = xMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", yMax, "XSDataDouble")
		self._yMax = yMax
		checkType("XSDataPlot", "Constructor of XSDataPlot", xLabel, "XSDataString")
		self._xLabel = xLabel
		checkType("XSDataPlot", "Constructor of XSDataPlot", yLabel, "XSDataString")
		self._yLabel = yLabel
		if graph is None:
			self._graph = []
		else:
			checkType("XSDataPlot", "Constructor of XSDataPlot", graph, "list")
			self._graph = graph
	def getPlotType(self): return self._plotType
	def setPlotType(self, plotType):
		checkType("XSDataPlot", "setPlotType", plotType, "XSDataString")
		self._plotType = plotType
	def delPlotType(self): self._plotType = None
	# Properties
	plotType = property(getPlotType, setPlotType, delPlotType, "Property for plotType")
	def getTopLabel(self): return self._topLabel
	def setTopLabel(self, topLabel):
		checkType("XSDataPlot", "setTopLabel", topLabel, "XSDataString")
		self._topLabel = topLabel
	def delTopLabel(self): self._topLabel = None
	# Properties
	topLabel = property(getTopLabel, setTopLabel, delTopLabel, "Property for topLabel")
	def getSubTitle(self): return self._subTitle
	def setSubTitle(self, subTitle):
		checkType("XSDataPlot", "setSubTitle", subTitle, "XSDataString")
		self._subTitle = subTitle
	def delSubTitle(self): self._subTitle = None
	# Properties
	subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
	def getXMin(self): return self._xMin
	def setXMin(self, xMin):
		checkType("XSDataPlot", "setXMin", xMin, "XSDataDouble")
		self._xMin = xMin
	def delXMin(self): self._xMin = None
	# Properties
	xMin = property(getXMin, setXMin, delXMin, "Property for xMin")
	def getYmin(self): return self._ymin
	def setYmin(self, ymin):
		checkType("XSDataPlot", "setYmin", ymin, "XSDataDouble")
		self._ymin = ymin
	def delYmin(self): self._ymin = None
	# Properties
	ymin = property(getYmin, setYmin, delYmin, "Property for ymin")
	def getXMax(self): return self._xMax
	def setXMax(self, xMax):
		checkType("XSDataPlot", "setXMax", xMax, "XSDataDouble")
		self._xMax = xMax
	def delXMax(self): self._xMax = None
	# Properties
	xMax = property(getXMax, setXMax, delXMax, "Property for xMax")
	def getYMax(self): return self._yMax
	def setYMax(self, yMax):
		checkType("XSDataPlot", "setYMax", yMax, "XSDataDouble")
		self._yMax = yMax
	def delYMax(self): self._yMax = None
	# Properties
	yMax = property(getYMax, setYMax, delYMax, "Property for yMax")
	def getXLabel(self): return self._xLabel
	def setXLabel(self, xLabel):
		checkType("XSDataPlot", "setXLabel", xLabel, "XSDataString")
		self._xLabel = xLabel
	def delXLabel(self): self._xLabel = None
	# Properties
	xLabel = property(getXLabel, setXLabel, delXLabel, "Property for xLabel")
	def getYLabel(self): return self._yLabel
	def setYLabel(self, yLabel):
		checkType("XSDataPlot", "setYLabel", yLabel, "XSDataString")
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
			self.plotType.export(outfile, level, name_='plotType')
		else:
			warnEmptyAttribute("plotType", "XSDataString")
		if self._topLabel is not None:
			self.topLabel.export(outfile, level, name_='topLabel')
		else:
			warnEmptyAttribute("topLabel", "XSDataString")
		if self._subTitle is not None:
			self.subTitle.export(outfile, level, name_='subTitle')
		else:
			warnEmptyAttribute("subTitle", "XSDataString")
		if self._xMin is not None:
			self.xMin.export(outfile, level, name_='xMin')
		if self._ymin is not None:
			self.ymin.export(outfile, level, name_='ymin')
		if self._xMax is not None:
			self.xMax.export(outfile, level, name_='xMax')
		if self._yMax is not None:
			self.yMax.export(outfile, level, name_='yMax')
		if self._xLabel is not None:
			self.xLabel.export(outfile, level, name_='xLabel')
		else:
			warnEmptyAttribute("xLabel", "XSDataString")
		if self._yLabel is not None:
			self.yLabel.export(outfile, level, name_='yLabel')
		else:
			warnEmptyAttribute("yLabel", "XSDataString")
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
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPlotType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'topLabel':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTopLabel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subTitle':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSubTitle(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setXMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ymin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setYmin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setXMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setYMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xLabel':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setXLabel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'yLabel':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setYLabel(obj_)
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

class XSDataInputPlotGle(XSDataInput):
	def __init__(self, configuration=None, filePlotMtv=None, plot=None):
		XSDataInput.__init__(self, configuration)
	
	
		if plot is None:
			self._plot = []
		else:
			checkType("XSDataInputPlotGle", "Constructor of XSDataInputPlotGle", plot, "list")
			self._plot = plot
		checkType("XSDataInputPlotGle", "Constructor of XSDataInputPlotGle", filePlotMtv, "XSDataFile")
		self._filePlotMtv = filePlotMtv
	def getPlot(self): return self._plot
	def setPlot(self, plot):
		checkType("XSDataInputPlotGle", "setPlot", plot, "list")
		self._plot = plot
	def delPlot(self): self._plot = None
	# Properties
	plot = property(getPlot, setPlot, delPlot, "Property for plot")
	def addPlot(self, value):
		checkType("XSDataInputPlotGle", "setPlot", value, "XSDataPlot")
		self._plot.append(value)
	def insertPlot(self, index, value):
		checkType("XSDataInputPlotGle", "setPlot", value, "XSDataPlot")
		self._plot[index] = value
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
		for plot_ in self.getPlot():
			plot_.export(outfile, level, name_='plot')
		if self._filePlotMtv is not None:
			self.filePlotMtv.export(outfile, level, name_='filePlotMtv')
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



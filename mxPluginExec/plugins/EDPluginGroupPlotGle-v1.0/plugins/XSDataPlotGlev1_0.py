#!/usr/bin/env python

#
# Generated Thu Feb 9 10:55::06 2012 by EDGenerateDS.
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
	def __init__(self, data=None, markerColor=None, markerType=None, label=None, lineColor=None, lineWidth=None, lineStyle=None):
		XSData.__init__(self, )
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineStyle, "string")
		self.__lineStyle = lineStyle
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineWidth, "double")
		self.__lineWidth = lineWidth
		checkType("XSDataGraph", "Constructor of XSDataGraph", lineColor, "string")
		self.__lineColor = lineColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", label, "string")
		self.__label = label
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerType, "string")
		self.__markerType = markerType
		checkType("XSDataGraph", "Constructor of XSDataGraph", markerColor, "string")
		self.__markerColor = markerColor
		checkType("XSDataGraph", "Constructor of XSDataGraph", data, "XSDataArray")
		self.__data = data
	def getLineStyle(self): return self.__lineStyle
	def setLineStyle(self, lineStyle):
		checkType("XSDataGraph", "setLineStyle", lineStyle, "string")
		self.__lineStyle = lineStyle
	def delLineStyle(self): self.__lineStyle = None
	# Properties
	lineStyle = property(getLineStyle, setLineStyle, delLineStyle, "Property for lineStyle")
	def getLineWidth(self): return self.__lineWidth
	def setLineWidth(self, lineWidth):
		checkType("XSDataGraph", "setLineWidth", lineWidth, "double")
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
	def getLabel(self): return self.__label
	def setLabel(self, label):
		checkType("XSDataGraph", "setLabel", label, "string")
		self.__label = label
	def delLabel(self): self.__label = None
	# Properties
	label = property(getLabel, setLabel, delLabel, "Property for label")
	def getMarkerType(self): return self.__markerType
	def setMarkerType(self, markerType):
		checkType("XSDataGraph", "setMarkerType", markerType, "string")
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
		if self.__lineStyle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineStyle>%s</lineStyle>\n' % self.__lineStyle))
		else:
			warnEmptyAttribute("lineStyle", "string")
		if self.__lineWidth is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineWidth>%e</lineWidth>\n' % self.__lineWidth))
		else:
			warnEmptyAttribute("lineWidth", "double")
		if self.__lineColor is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<lineColor>%s</lineColor>\n' % self.__lineColor))
		else:
			warnEmptyAttribute("lineColor", "string")
		if self.__label is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<label>%s</label>\n' % self.__label))
		else:
			warnEmptyAttribute("label", "string")
		if self.__markerType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<markerType>%s</markerType>\n' % self.__markerType))
		else:
			warnEmptyAttribute("markerType", "string")
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
			nodeName_ == 'lineStyle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__lineStyle = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineWidth':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__lineWidth = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineColor':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__lineColor = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'label':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__label = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'markerType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__markerType = value_
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
	def __init__(self, graph=None, ytitle=None, xtitle=None, keypos=None, ymax=None, xmax=None, ymin=None, xmin=None, ysize=None, xsize=None, subTitle=None, title=None, plotType=None):
		XSData.__init__(self, )
		checkType("XSDataPlot", "Constructor of XSDataPlot", plotType, "string")
		self.__plotType = plotType
		checkType("XSDataPlot", "Constructor of XSDataPlot", title, "string")
		self.__title = title
		checkType("XSDataPlot", "Constructor of XSDataPlot", subTitle, "string")
		self.__subTitle = subTitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", xsize, "double")
		self.__xsize = xsize
		checkType("XSDataPlot", "Constructor of XSDataPlot", ysize, "double")
		self.__ysize = ysize
		checkType("XSDataPlot", "Constructor of XSDataPlot", xmin, "double")
		self.__xmin = xmin
		checkType("XSDataPlot", "Constructor of XSDataPlot", ymin, "double")
		self.__ymin = ymin
		checkType("XSDataPlot", "Constructor of XSDataPlot", xmax, "double")
		self.__xmax = xmax
		checkType("XSDataPlot", "Constructor of XSDataPlot", ymax, "double")
		self.__ymax = ymax
		checkType("XSDataPlot", "Constructor of XSDataPlot", keypos, "string")
		self.__keypos = keypos
		checkType("XSDataPlot", "Constructor of XSDataPlot", xtitle, "string")
		self.__xtitle = xtitle
		checkType("XSDataPlot", "Constructor of XSDataPlot", ytitle, "string")
		self.__ytitle = ytitle
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
	def getTitle(self): return self.__title
	def setTitle(self, title):
		checkType("XSDataPlot", "setTitle", title, "string")
		self.__title = title
	def delTitle(self): self.__title = None
	# Properties
	title = property(getTitle, setTitle, delTitle, "Property for title")
	def getSubTitle(self): return self.__subTitle
	def setSubTitle(self, subTitle):
		checkType("XSDataPlot", "setSubTitle", subTitle, "string")
		self.__subTitle = subTitle
	def delSubTitle(self): self.__subTitle = None
	# Properties
	subTitle = property(getSubTitle, setSubTitle, delSubTitle, "Property for subTitle")
	def getXsize(self): return self.__xsize
	def setXsize(self, xsize):
		checkType("XSDataPlot", "setXsize", xsize, "double")
		self.__xsize = xsize
	def delXsize(self): self.__xsize = None
	# Properties
	xsize = property(getXsize, setXsize, delXsize, "Property for xsize")
	def getYsize(self): return self.__ysize
	def setYsize(self, ysize):
		checkType("XSDataPlot", "setYsize", ysize, "double")
		self.__ysize = ysize
	def delYsize(self): self.__ysize = None
	# Properties
	ysize = property(getYsize, setYsize, delYsize, "Property for ysize")
	def getXmin(self): return self.__xmin
	def setXmin(self, xmin):
		checkType("XSDataPlot", "setXmin", xmin, "double")
		self.__xmin = xmin
	def delXmin(self): self.__xmin = None
	# Properties
	xmin = property(getXmin, setXmin, delXmin, "Property for xmin")
	def getYmin(self): return self.__ymin
	def setYmin(self, ymin):
		checkType("XSDataPlot", "setYmin", ymin, "double")
		self.__ymin = ymin
	def delYmin(self): self.__ymin = None
	# Properties
	ymin = property(getYmin, setYmin, delYmin, "Property for ymin")
	def getXmax(self): return self.__xmax
	def setXmax(self, xmax):
		checkType("XSDataPlot", "setXmax", xmax, "double")
		self.__xmax = xmax
	def delXmax(self): self.__xmax = None
	# Properties
	xmax = property(getXmax, setXmax, delXmax, "Property for xmax")
	def getYmax(self): return self.__ymax
	def setYmax(self, ymax):
		checkType("XSDataPlot", "setYmax", ymax, "double")
		self.__ymax = ymax
	def delYmax(self): self.__ymax = None
	# Properties
	ymax = property(getYmax, setYmax, delYmax, "Property for ymax")
	def getKeypos(self): return self.__keypos
	def setKeypos(self, keypos):
		checkType("XSDataPlot", "setKeypos", keypos, "string")
		self.__keypos = keypos
	def delKeypos(self): self.__keypos = None
	# Properties
	keypos = property(getKeypos, setKeypos, delKeypos, "Property for keypos")
	def getXtitle(self): return self.__xtitle
	def setXtitle(self, xtitle):
		checkType("XSDataPlot", "setXtitle", xtitle, "string")
		self.__xtitle = xtitle
	def delXtitle(self): self.__xtitle = None
	# Properties
	xtitle = property(getXtitle, setXtitle, delXtitle, "Property for xtitle")
	def getYtitle(self): return self.__ytitle
	def setYtitle(self, ytitle):
		checkType("XSDataPlot", "setYtitle", ytitle, "string")
		self.__ytitle = ytitle
	def delYtitle(self): self.__ytitle = None
	# Properties
	ytitle = property(getYtitle, setYtitle, delYtitle, "Property for ytitle")
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
		if self.__title is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<title>%s</title>\n' % self.__title))
		else:
			warnEmptyAttribute("title", "string")
		if self.__subTitle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<subTitle>%s</subTitle>\n' % self.__subTitle))
		else:
			warnEmptyAttribute("subTitle", "string")
		if self.__xsize is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xsize>%e</xsize>\n' % self.__xsize))
		if self.__ysize is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ysize>%e</ysize>\n' % self.__ysize))
		if self.__xmin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xmin>%e</xmin>\n' % self.__xmin))
		if self.__ymin is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ymin>%e</ymin>\n' % self.__ymin))
		if self.__xmax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xmax>%e</xmax>\n' % self.__xmax))
		if self.__ymax is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ymax>%e</ymax>\n' % self.__ymax))
		if self.__keypos is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<keypos>%s</keypos>\n' % self.__keypos))
		if self.__xtitle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtitle>%s</xtitle>\n' % self.__xtitle))
		else:
			warnEmptyAttribute("xtitle", "string")
		if self.__ytitle is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ytitle>%s</ytitle>\n' % self.__ytitle))
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
			self.__plotType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'title':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__title = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subTitle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__subTitle = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xsize':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xsize = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ysize':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__ysize = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xmin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xmin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ymin':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__ymin = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xmax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xmax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ymax':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__ymax = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'keypos':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__keypos = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtitle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xtitle = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ytitle':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__ytitle = value_
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
	def __init__(self, status=None, fileGraph=None):
		XSDataResult.__init__(self, status)
		if fileGraph is None:
			self.__fileGraph = []
		else:
			checkType("XSDataResultPlotGle", "Constructor of XSDataResultPlotGle", fileGraph, "list")
			self.__fileGraph = fileGraph
	def getFileGraph(self): return self.__fileGraph
	def setFileGraph(self, fileGraph):
		checkType("XSDataResultPlotGle", "setFileGraph", fileGraph, "list")
		self.__fileGraph = fileGraph
	def delFileGraph(self): self.__fileGraph = None
	# Properties
	fileGraph = property(getFileGraph, setFileGraph, delFileGraph, "Property for fileGraph")
	def addFileGraph(self, value):
		checkType("XSDataResultPlotGle", "setFileGraph", value, "XSDataFile")
		self.__fileGraph.append(value)
	def insertFileGraph(self, index, value):
		checkType("XSDataResultPlotGle", "setFileGraph", value, "XSDataFile")
		self.__fileGraph[index] = value
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



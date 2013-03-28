#!/usr/bin/env python

#
# Generated Sun Mar 24 05:39::00 2013 by EDGenerateDS.
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
	from XSDataCommon import XSDataArray
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
from XSDataCommon import XSDataArray
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


class XSDataNexusAxis(XSData):
	def __init__(self, axisData=None, long_name=None, units=None, primary=None, axis=None, title=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", title, "XSDataString")
		self._title = title
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", axis, "XSDataInteger")
		self._axis = axis
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", primary, "XSDataInteger")
		self._primary = primary
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", units, "XSDataString")
		self._units = units
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", long_name, "XSDataString")
		self._long_name = long_name
		checkType("XSDataNexusAxis", "Constructor of XSDataNexusAxis", axisData, "XSDataArray")
		self._axisData = axisData
	def getTitle(self): return self._title
	def setTitle(self, title):
		checkType("XSDataNexusAxis", "setTitle", title, "XSDataString")
		self._title = title
	def delTitle(self): self._title = None
	# Properties
	title = property(getTitle, setTitle, delTitle, "Property for title")
	def getAxis(self): return self._axis
	def setAxis(self, axis):
		checkType("XSDataNexusAxis", "setAxis", axis, "XSDataInteger")
		self._axis = axis
	def delAxis(self): self._axis = None
	# Properties
	axis = property(getAxis, setAxis, delAxis, "Property for axis")
	def getPrimary(self): return self._primary
	def setPrimary(self, primary):
		checkType("XSDataNexusAxis", "setPrimary", primary, "XSDataInteger")
		self._primary = primary
	def delPrimary(self): self._primary = None
	# Properties
	primary = property(getPrimary, setPrimary, delPrimary, "Property for primary")
	def getUnits(self): return self._units
	def setUnits(self, units):
		checkType("XSDataNexusAxis", "setUnits", units, "XSDataString")
		self._units = units
	def delUnits(self): self._units = None
	# Properties
	units = property(getUnits, setUnits, delUnits, "Property for units")
	def getLong_name(self): return self._long_name
	def setLong_name(self, long_name):
		checkType("XSDataNexusAxis", "setLong_name", long_name, "XSDataString")
		self._long_name = long_name
	def delLong_name(self): self._long_name = None
	# Properties
	long_name = property(getLong_name, setLong_name, delLong_name, "Property for long_name")
	def getAxisData(self): return self._axisData
	def setAxisData(self, axisData):
		checkType("XSDataNexusAxis", "setAxisData", axisData, "XSDataArray")
		self._axisData = axisData
	def delAxisData(self): self._axisData = None
	# Properties
	axisData = property(getAxisData, setAxisData, delAxisData, "Property for axisData")
	def export(self, outfile, level, name_='XSDataNexusAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataNexusAxis'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._title is not None:
			self.title.export(outfile, level, name_='title')
		else:
			warnEmptyAttribute("title", "XSDataString")
		if self._axis is not None:
			self.axis.export(outfile, level, name_='axis')
		else:
			warnEmptyAttribute("axis", "XSDataInteger")
		if self._primary is not None:
			self.primary.export(outfile, level, name_='primary')
		else:
			warnEmptyAttribute("primary", "XSDataInteger")
		if self._units is not None:
			self.units.export(outfile, level, name_='units')
		else:
			warnEmptyAttribute("units", "XSDataString")
		if self._long_name is not None:
			self.long_name.export(outfile, level, name_='long_name')
		else:
			warnEmptyAttribute("long_name", "XSDataString")
		if self._axisData is not None:
			self.axisData.export(outfile, level, name_='axisData')
		else:
			warnEmptyAttribute("axisData", "XSDataArray")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'title':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTitle(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axis':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setAxis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'primary':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setPrimary(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'units':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setUnits(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'long_name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLong_name(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisData':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setAxisData(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataNexusAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataNexusAxis' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataNexusAxis is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataNexusAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataNexusAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataNexusAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataNexusAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataNexusAxis

class XSDataNexusArrayGroup(XSData):
	def __init__(self, signal=None, data=None, axis=None, long_name=None, title=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataNexusArrayGroup", "Constructor of XSDataNexusArrayGroup", title, "XSDataString")
		self._title = title
		checkType("XSDataNexusArrayGroup", "Constructor of XSDataNexusArrayGroup", long_name, "XSDataString")
		self._long_name = long_name
		if axis is None:
			self._axis = []
		else:
			checkType("XSDataNexusArrayGroup", "Constructor of XSDataNexusArrayGroup", axis, "list")
			self._axis = axis
		checkType("XSDataNexusArrayGroup", "Constructor of XSDataNexusArrayGroup", data, "XSDataArray")
		self._data = data
		checkType("XSDataNexusArrayGroup", "Constructor of XSDataNexusArrayGroup", signal, "XSDataInteger")
		self._signal = signal
	def getTitle(self): return self._title
	def setTitle(self, title):
		checkType("XSDataNexusArrayGroup", "setTitle", title, "XSDataString")
		self._title = title
	def delTitle(self): self._title = None
	# Properties
	title = property(getTitle, setTitle, delTitle, "Property for title")
	def getLong_name(self): return self._long_name
	def setLong_name(self, long_name):
		checkType("XSDataNexusArrayGroup", "setLong_name", long_name, "XSDataString")
		self._long_name = long_name
	def delLong_name(self): self._long_name = None
	# Properties
	long_name = property(getLong_name, setLong_name, delLong_name, "Property for long_name")
	def getAxis(self): return self._axis
	def setAxis(self, axis):
		checkType("XSDataNexusArrayGroup", "setAxis", axis, "list")
		self._axis = axis
	def delAxis(self): self._axis = None
	# Properties
	axis = property(getAxis, setAxis, delAxis, "Property for axis")
	def addAxis(self, value):
		checkType("XSDataNexusArrayGroup", "setAxis", value, "XSDataNexusAxis")
		self._axis.append(value)
	def insertAxis(self, index, value):
		checkType("XSDataNexusArrayGroup", "setAxis", value, "XSDataNexusAxis")
		self._axis[index] = value
	def getData(self): return self._data
	def setData(self, data):
		checkType("XSDataNexusArrayGroup", "setData", data, "XSDataArray")
		self._data = data
	def delData(self): self._data = None
	# Properties
	data = property(getData, setData, delData, "Property for data")
	def getSignal(self): return self._signal
	def setSignal(self, signal):
		checkType("XSDataNexusArrayGroup", "setSignal", signal, "XSDataInteger")
		self._signal = signal
	def delSignal(self): self._signal = None
	# Properties
	signal = property(getSignal, setSignal, delSignal, "Property for signal")
	def export(self, outfile, level, name_='XSDataNexusArrayGroup'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataNexusArrayGroup'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._title is not None:
			self.title.export(outfile, level, name_='title')
		else:
			warnEmptyAttribute("title", "XSDataString")
		if self._long_name is not None:
			self.long_name.export(outfile, level, name_='long_name')
		else:
			warnEmptyAttribute("long_name", "XSDataString")
		for axis_ in self.getAxis():
			axis_.export(outfile, level, name_='axis')
		if self.getAxis() == []:
			warnEmptyAttribute("axis", "XSDataNexusAxis")
		if self._data is not None:
			self.data.export(outfile, level, name_='data')
		else:
			warnEmptyAttribute("data", "XSDataArray")
		if self._signal is not None:
			self.signal.export(outfile, level, name_='signal')
		else:
			warnEmptyAttribute("signal", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'title':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTitle(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'long_name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLong_name(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axis':
			obj_ = XSDataNexusAxis()
			obj_.build(child_)
			self.axis.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'data':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setData(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'signal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSignal(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataNexusArrayGroup" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataNexusArrayGroup' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataNexusArrayGroup is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataNexusArrayGroup.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataNexusArrayGroup()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataNexusArrayGroup" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataNexusArrayGroup()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataNexusArrayGroup

class XSDataInputWriteNexusFile(XSDataInput):
	def __init__(self, configuration=None, nexusGroup=None, outputFileDirectory=None, outputFileName=None, instrument=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputWriteNexusFile", "Constructor of XSDataInputWriteNexusFile", instrument, "XSDataString")
		self._instrument = instrument
		checkType("XSDataInputWriteNexusFile", "Constructor of XSDataInputWriteNexusFile", outputFileName, "XSDataString")
		self._outputFileName = outputFileName
		checkType("XSDataInputWriteNexusFile", "Constructor of XSDataInputWriteNexusFile", outputFileDirectory, "XSDataFile")
		self._outputFileDirectory = outputFileDirectory
		if nexusGroup is None:
			self._nexusGroup = []
		else:
			checkType("XSDataInputWriteNexusFile", "Constructor of XSDataInputWriteNexusFile", nexusGroup, "list")
			self._nexusGroup = nexusGroup
	def getInstrument(self): return self._instrument
	def setInstrument(self, instrument):
		checkType("XSDataInputWriteNexusFile", "setInstrument", instrument, "XSDataString")
		self._instrument = instrument
	def delInstrument(self): self._instrument = None
	# Properties
	instrument = property(getInstrument, setInstrument, delInstrument, "Property for instrument")
	def getOutputFileName(self): return self._outputFileName
	def setOutputFileName(self, outputFileName):
		checkType("XSDataInputWriteNexusFile", "setOutputFileName", outputFileName, "XSDataString")
		self._outputFileName = outputFileName
	def delOutputFileName(self): self._outputFileName = None
	# Properties
	outputFileName = property(getOutputFileName, setOutputFileName, delOutputFileName, "Property for outputFileName")
	def getOutputFileDirectory(self): return self._outputFileDirectory
	def setOutputFileDirectory(self, outputFileDirectory):
		checkType("XSDataInputWriteNexusFile", "setOutputFileDirectory", outputFileDirectory, "XSDataFile")
		self._outputFileDirectory = outputFileDirectory
	def delOutputFileDirectory(self): self._outputFileDirectory = None
	# Properties
	outputFileDirectory = property(getOutputFileDirectory, setOutputFileDirectory, delOutputFileDirectory, "Property for outputFileDirectory")
	def getNexusGroup(self): return self._nexusGroup
	def setNexusGroup(self, nexusGroup):
		checkType("XSDataInputWriteNexusFile", "setNexusGroup", nexusGroup, "list")
		self._nexusGroup = nexusGroup
	def delNexusGroup(self): self._nexusGroup = None
	# Properties
	nexusGroup = property(getNexusGroup, setNexusGroup, delNexusGroup, "Property for nexusGroup")
	def addNexusGroup(self, value):
		checkType("XSDataInputWriteNexusFile", "setNexusGroup", value, "XSDataNexusArrayGroup")
		self._nexusGroup.append(value)
	def insertNexusGroup(self, index, value):
		checkType("XSDataInputWriteNexusFile", "setNexusGroup", value, "XSDataNexusArrayGroup")
		self._nexusGroup[index] = value
	def export(self, outfile, level, name_='XSDataInputWriteNexusFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputWriteNexusFile'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._instrument is not None:
			self.instrument.export(outfile, level, name_='instrument')
		else:
			warnEmptyAttribute("instrument", "XSDataString")
		if self._outputFileName is not None:
			self.outputFileName.export(outfile, level, name_='outputFileName')
		else:
			warnEmptyAttribute("outputFileName", "XSDataString")
		if self._outputFileDirectory is not None:
			self.outputFileDirectory.export(outfile, level, name_='outputFileDirectory')
		for nexusGroup_ in self.getNexusGroup():
			nexusGroup_.export(outfile, level, name_='nexusGroup')
		if self.getNexusGroup() == []:
			warnEmptyAttribute("nexusGroup", "XSDataNexusArrayGroup")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'instrument':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInstrument(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutputFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFileDirectory':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputFileDirectory(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nexusGroup':
			obj_ = XSDataNexusArrayGroup()
			obj_.build(child_)
			self.nexusGroup.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputWriteNexusFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputWriteNexusFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputWriteNexusFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputWriteNexusFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputWriteNexusFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputWriteNexusFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputWriteNexusFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputWriteNexusFile

class XSDataResultWriteNexusFile(XSDataResult):
	def __init__(self, status=None, outputFilePath=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultWriteNexusFile", "Constructor of XSDataResultWriteNexusFile", outputFilePath, "XSDataFile")
		self._outputFilePath = outputFilePath
	def getOutputFilePath(self): return self._outputFilePath
	def setOutputFilePath(self, outputFilePath):
		checkType("XSDataResultWriteNexusFile", "setOutputFilePath", outputFilePath, "XSDataFile")
		self._outputFilePath = outputFilePath
	def delOutputFilePath(self): self._outputFilePath = None
	# Properties
	outputFilePath = property(getOutputFilePath, setOutputFilePath, delOutputFilePath, "Property for outputFilePath")
	def export(self, outfile, level, name_='XSDataResultWriteNexusFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultWriteNexusFile'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._outputFilePath is not None:
			self.outputFilePath.export(outfile, level, name_='outputFilePath')
		else:
			warnEmptyAttribute("outputFilePath", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFilePath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputFilePath(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultWriteNexusFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultWriteNexusFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultWriteNexusFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultWriteNexusFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultWriteNexusFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultWriteNexusFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultWriteNexusFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultWriteNexusFile



# End of data representation classes.



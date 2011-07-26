#!/usr/bin/env python

#
# Generated Tue Jul 26 01:47::17 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataTime




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


class XSDataHDF5Attributes(XSData):
	"""Allows the fine definition of the metadata for group/datasets"""
	def __init__(self, metadata=None, h5path=None):
		XSData.__init__(self, )
		checkType("XSDataHDF5Attributes", "Constructor of XSDataHDF5Attributes", h5path, "XSDataString")
		self.__h5path = h5path
		checkType("XSDataHDF5Attributes", "Constructor of XSDataHDF5Attributes", metadata, "XSDataDictionary")
		self.__metadata = metadata
	def getH5path(self): return self.__h5path
	def setH5path(self, h5path):
		checkType("XSDataHDF5Attributes", "setH5path", h5path, "XSDataString")
		self.__h5path = h5path
	def delH5path(self): self.__h5path = None
	# Properties
	h5path = property(getH5path, setH5path, delH5path, "Property for h5path")
	def getMetadata(self): return self.__metadata
	def setMetadata(self, metadata):
		checkType("XSDataHDF5Attributes", "setMetadata", metadata, "XSDataDictionary")
		self.__metadata = metadata
	def delMetadata(self): self.__metadata = None
	# Properties
	metadata = property(getMetadata, setMetadata, delMetadata, "Property for metadata")
	def export(self, outfile, level, name_='XSDataHDF5Attributes'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataHDF5Attributes'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__h5path is not None:
			self.h5path.export(outfile, level, name_='h5path')
		else:
			warnEmptyAttribute("h5path", "XSDataString")
		if self.__metadata is not None:
			self.metadata.export(outfile, level, name_='metadata')
		else:
			warnEmptyAttribute("metadata", "XSDataDictionary")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'h5path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setH5path(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'metadata':
			obj_ = XSDataDictionary()
			obj_.build(child_)
			self.setMetadata(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataHDF5Attributes" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataHDF5Attributes' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataHDF5Attributes is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataHDF5Attributes.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataHDF5Attributes()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataHDF5Attributes" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataHDF5Attributes()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataHDF5Attributes

class XSDataMeshScan(XSData):
	def __init__(self, slowMotorStop=None, slowMotorStart=None, slowMotorName=None, slowMotorSteps=None, integrationTime=None, fastMotorStop=None, fastMotorSteps=None, fastMotorStart=None, fastMotorName=None):
		XSData.__init__(self, )
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", fastMotorName, "XSDataString")
		self.__fastMotorName = fastMotorName
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", fastMotorStart, "XSDataDouble")
		self.__fastMotorStart = fastMotorStart
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", fastMotorSteps, "XSDataInteger")
		self.__fastMotorSteps = fastMotorSteps
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", fastMotorStop, "XSDataDouble")
		self.__fastMotorStop = fastMotorStop
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", integrationTime, "XSDataTime")
		self.__integrationTime = integrationTime
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", slowMotorSteps, "XSDataInteger")
		self.__slowMotorSteps = slowMotorSteps
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", slowMotorName, "XSDataString")
		self.__slowMotorName = slowMotorName
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", slowMotorStart, "XSDataDouble")
		self.__slowMotorStart = slowMotorStart
		checkType("XSDataMeshScan", "Constructor of XSDataMeshScan", slowMotorStop, "XSDataDouble")
		self.__slowMotorStop = slowMotorStop
	def getFastMotorName(self): return self.__fastMotorName
	def setFastMotorName(self, fastMotorName):
		checkType("XSDataMeshScan", "setFastMotorName", fastMotorName, "XSDataString")
		self.__fastMotorName = fastMotorName
	def delFastMotorName(self): self.__fastMotorName = None
	# Properties
	fastMotorName = property(getFastMotorName, setFastMotorName, delFastMotorName, "Property for fastMotorName")
	def getFastMotorStart(self): return self.__fastMotorStart
	def setFastMotorStart(self, fastMotorStart):
		checkType("XSDataMeshScan", "setFastMotorStart", fastMotorStart, "XSDataDouble")
		self.__fastMotorStart = fastMotorStart
	def delFastMotorStart(self): self.__fastMotorStart = None
	# Properties
	fastMotorStart = property(getFastMotorStart, setFastMotorStart, delFastMotorStart, "Property for fastMotorStart")
	def getFastMotorSteps(self): return self.__fastMotorSteps
	def setFastMotorSteps(self, fastMotorSteps):
		checkType("XSDataMeshScan", "setFastMotorSteps", fastMotorSteps, "XSDataInteger")
		self.__fastMotorSteps = fastMotorSteps
	def delFastMotorSteps(self): self.__fastMotorSteps = None
	# Properties
	fastMotorSteps = property(getFastMotorSteps, setFastMotorSteps, delFastMotorSteps, "Property for fastMotorSteps")
	def getFastMotorStop(self): return self.__fastMotorStop
	def setFastMotorStop(self, fastMotorStop):
		checkType("XSDataMeshScan", "setFastMotorStop", fastMotorStop, "XSDataDouble")
		self.__fastMotorStop = fastMotorStop
	def delFastMotorStop(self): self.__fastMotorStop = None
	# Properties
	fastMotorStop = property(getFastMotorStop, setFastMotorStop, delFastMotorStop, "Property for fastMotorStop")
	def getIntegrationTime(self): return self.__integrationTime
	def setIntegrationTime(self, integrationTime):
		checkType("XSDataMeshScan", "setIntegrationTime", integrationTime, "XSDataTime")
		self.__integrationTime = integrationTime
	def delIntegrationTime(self): self.__integrationTime = None
	# Properties
	integrationTime = property(getIntegrationTime, setIntegrationTime, delIntegrationTime, "Property for integrationTime")
	def getSlowMotorSteps(self): return self.__slowMotorSteps
	def setSlowMotorSteps(self, slowMotorSteps):
		checkType("XSDataMeshScan", "setSlowMotorSteps", slowMotorSteps, "XSDataInteger")
		self.__slowMotorSteps = slowMotorSteps
	def delSlowMotorSteps(self): self.__slowMotorSteps = None
	# Properties
	slowMotorSteps = property(getSlowMotorSteps, setSlowMotorSteps, delSlowMotorSteps, "Property for slowMotorSteps")
	def getSlowMotorName(self): return self.__slowMotorName
	def setSlowMotorName(self, slowMotorName):
		checkType("XSDataMeshScan", "setSlowMotorName", slowMotorName, "XSDataString")
		self.__slowMotorName = slowMotorName
	def delSlowMotorName(self): self.__slowMotorName = None
	# Properties
	slowMotorName = property(getSlowMotorName, setSlowMotorName, delSlowMotorName, "Property for slowMotorName")
	def getSlowMotorStart(self): return self.__slowMotorStart
	def setSlowMotorStart(self, slowMotorStart):
		checkType("XSDataMeshScan", "setSlowMotorStart", slowMotorStart, "XSDataDouble")
		self.__slowMotorStart = slowMotorStart
	def delSlowMotorStart(self): self.__slowMotorStart = None
	# Properties
	slowMotorStart = property(getSlowMotorStart, setSlowMotorStart, delSlowMotorStart, "Property for slowMotorStart")
	def getSlowMotorStop(self): return self.__slowMotorStop
	def setSlowMotorStop(self, slowMotorStop):
		checkType("XSDataMeshScan", "setSlowMotorStop", slowMotorStop, "XSDataDouble")
		self.__slowMotorStop = slowMotorStop
	def delSlowMotorStop(self): self.__slowMotorStop = None
	# Properties
	slowMotorStop = property(getSlowMotorStop, setSlowMotorStop, delSlowMotorStop, "Property for slowMotorStop")
	def export(self, outfile, level, name_='XSDataMeshScan'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMeshScan'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__fastMotorName is not None:
			self.fastMotorName.export(outfile, level, name_='fastMotorName')
		if self.__fastMotorStart is not None:
			self.fastMotorStart.export(outfile, level, name_='fastMotorStart')
		else:
			warnEmptyAttribute("fastMotorStart", "XSDataDouble")
		if self.__fastMotorSteps is not None:
			self.fastMotorSteps.export(outfile, level, name_='fastMotorSteps')
		else:
			warnEmptyAttribute("fastMotorSteps", "XSDataInteger")
		if self.__fastMotorStop is not None:
			self.fastMotorStop.export(outfile, level, name_='fastMotorStop')
		else:
			warnEmptyAttribute("fastMotorStop", "XSDataDouble")
		if self.__integrationTime is not None:
			self.integrationTime.export(outfile, level, name_='integrationTime')
		if self.__slowMotorSteps is not None:
			self.slowMotorSteps.export(outfile, level, name_='slowMotorSteps')
		else:
			warnEmptyAttribute("slowMotorSteps", "XSDataInteger")
		if self.__slowMotorName is not None:
			self.slowMotorName.export(outfile, level, name_='slowMotorName')
		if self.__slowMotorStart is not None:
			self.slowMotorStart.export(outfile, level, name_='slowMotorStart')
		else:
			warnEmptyAttribute("slowMotorStart", "XSDataDouble")
		if self.__slowMotorStop is not None:
			self.slowMotorStop.export(outfile, level, name_='slowMotorStop')
		else:
			warnEmptyAttribute("slowMotorStop", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fastMotorName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFastMotorName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fastMotorStart':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFastMotorStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fastMotorSteps':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFastMotorSteps(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fastMotorStop':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFastMotorStop(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integrationTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setIntegrationTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slowMotorSteps':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSlowMotorSteps(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slowMotorName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSlowMotorName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slowMotorStart':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSlowMotorStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slowMotorStop':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSlowMotorStop(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMeshScan" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMeshScan' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMeshScan is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMeshScan.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMeshScan()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMeshScan" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMeshScan()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMeshScan

class XSDataSpectrum(XSData):
	def __init__(self, fileType=None, slowMotorPosition=None, meshScan=None, fastMotorPosition=None, array=None, path=None):
		XSData.__init__(self, )
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", path, "XSDataString")
		self.__path = path
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", array, "XSDataArray")
		self.__array = array
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", fastMotorPosition, "XSDataDouble")
		self.__fastMotorPosition = fastMotorPosition
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", meshScan, "XSDataMeshScan")
		self.__meshScan = meshScan
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", slowMotorPosition, "XSDataDouble")
		self.__slowMotorPosition = slowMotorPosition
		checkType("XSDataSpectrum", "Constructor of XSDataSpectrum", fileType, "XSDataString")
		self.__fileType = fileType
	def getPath(self): return self.__path
	def setPath(self, path):
		checkType("XSDataSpectrum", "setPath", path, "XSDataString")
		self.__path = path
	def delPath(self): self.__path = None
	# Properties
	path = property(getPath, setPath, delPath, "Property for path")
	def getArray(self): return self.__array
	def setArray(self, array):
		checkType("XSDataSpectrum", "setArray", array, "XSDataArray")
		self.__array = array
	def delArray(self): self.__array = None
	# Properties
	array = property(getArray, setArray, delArray, "Property for array")
	def getFastMotorPosition(self): return self.__fastMotorPosition
	def setFastMotorPosition(self, fastMotorPosition):
		checkType("XSDataSpectrum", "setFastMotorPosition", fastMotorPosition, "XSDataDouble")
		self.__fastMotorPosition = fastMotorPosition
	def delFastMotorPosition(self): self.__fastMotorPosition = None
	# Properties
	fastMotorPosition = property(getFastMotorPosition, setFastMotorPosition, delFastMotorPosition, "Property for fastMotorPosition")
	def getMeshScan(self): return self.__meshScan
	def setMeshScan(self, meshScan):
		checkType("XSDataSpectrum", "setMeshScan", meshScan, "XSDataMeshScan")
		self.__meshScan = meshScan
	def delMeshScan(self): self.__meshScan = None
	# Properties
	meshScan = property(getMeshScan, setMeshScan, delMeshScan, "Property for meshScan")
	def getSlowMotorPosition(self): return self.__slowMotorPosition
	def setSlowMotorPosition(self, slowMotorPosition):
		checkType("XSDataSpectrum", "setSlowMotorPosition", slowMotorPosition, "XSDataDouble")
		self.__slowMotorPosition = slowMotorPosition
	def delSlowMotorPosition(self): self.__slowMotorPosition = None
	# Properties
	slowMotorPosition = property(getSlowMotorPosition, setSlowMotorPosition, delSlowMotorPosition, "Property for slowMotorPosition")
	def getFileType(self): return self.__fileType
	def setFileType(self, fileType):
		checkType("XSDataSpectrum", "setFileType", fileType, "XSDataString")
		self.__fileType = fileType
	def delFileType(self): self.__fileType = None
	# Properties
	fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
	def export(self, outfile, level, name_='XSDataSpectrum'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSpectrum'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__path is not None:
			self.path.export(outfile, level, name_='path')
		if self.__array is not None:
			self.array.export(outfile, level, name_='array')
		if self.__fastMotorPosition is not None:
			self.fastMotorPosition.export(outfile, level, name_='fastMotorPosition')
		if self.__meshScan is not None:
			self.meshScan.export(outfile, level, name_='meshScan')
		if self.__slowMotorPosition is not None:
			self.slowMotorPosition.export(outfile, level, name_='slowMotorPosition')
		if self.__fileType is not None:
			self.fileType.export(outfile, level, name_='fileType')
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
			nodeName_ == 'array':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fastMotorPosition':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFastMotorPosition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'meshScan':
			obj_ = XSDataMeshScan()
			obj_.build(child_)
			self.setMeshScan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slowMotorPosition':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSlowMotorPosition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileType(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSpectrum" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSpectrum' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSpectrum is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSpectrum.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSpectrum()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSpectrum" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSpectrum()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSpectrum

class XSDataInputHDF5Writer(XSDataInput):
	"""Common XSDataInput class for all hdf5 writers
"""
	def __init__(self, configuration=None, chunkSegmentation=None, forceDtype=None, extraAttributes=None, multiFiles=None, internalHDF5Path=None, HDF5File=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
		checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", multiFiles, "XSDataBoolean")
		self.__multiFiles = multiFiles
		if extraAttributes is None:
			self.__extraAttributes = []
		else:
			checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", extraAttributes, "list")
			self.__extraAttributes = extraAttributes
		checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", forceDtype, "XSDataString")
		self.__forceDtype = forceDtype
		checkType("XSDataInputHDF5Writer", "Constructor of XSDataInputHDF5Writer", chunkSegmentation, "XSDataInteger")
		self.__chunkSegmentation = chunkSegmentation
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataInputHDF5Writer", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataInputHDF5Writer", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def getMultiFiles(self): return self.__multiFiles
	def setMultiFiles(self, multiFiles):
		checkType("XSDataInputHDF5Writer", "setMultiFiles", multiFiles, "XSDataBoolean")
		self.__multiFiles = multiFiles
	def delMultiFiles(self): self.__multiFiles = None
	# Properties
	multiFiles = property(getMultiFiles, setMultiFiles, delMultiFiles, "Property for multiFiles")
	def getExtraAttributes(self): return self.__extraAttributes
	def setExtraAttributes(self, extraAttributes):
		checkType("XSDataInputHDF5Writer", "setExtraAttributes", extraAttributes, "list")
		self.__extraAttributes = extraAttributes
	def delExtraAttributes(self): self.__extraAttributes = None
	# Properties
	extraAttributes = property(getExtraAttributes, setExtraAttributes, delExtraAttributes, "Property for extraAttributes")
	def addExtraAttributes(self, value):
		checkType("XSDataInputHDF5Writer", "setExtraAttributes", value, "XSDataHDF5Attributes")
		self.__extraAttributes.append(value)
	def insertExtraAttributes(self, index, value):
		checkType("XSDataInputHDF5Writer", "setExtraAttributes", value, "XSDataHDF5Attributes")
		self.__extraAttributes[index] = value
	def getForceDtype(self): return self.__forceDtype
	def setForceDtype(self, forceDtype):
		checkType("XSDataInputHDF5Writer", "setForceDtype", forceDtype, "XSDataString")
		self.__forceDtype = forceDtype
	def delForceDtype(self): self.__forceDtype = None
	# Properties
	forceDtype = property(getForceDtype, setForceDtype, delForceDtype, "Property for forceDtype")
	def getChunkSegmentation(self): return self.__chunkSegmentation
	def setChunkSegmentation(self, chunkSegmentation):
		checkType("XSDataInputHDF5Writer", "setChunkSegmentation", chunkSegmentation, "XSDataInteger")
		self.__chunkSegmentation = chunkSegmentation
	def delChunkSegmentation(self): self.__chunkSegmentation = None
	# Properties
	chunkSegmentation = property(getChunkSegmentation, setChunkSegmentation, delChunkSegmentation, "Property for chunkSegmentation")
	def export(self, outfile, level, name_='XSDataInputHDF5Writer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputHDF5Writer'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
		if self.__multiFiles is not None:
			self.multiFiles.export(outfile, level, name_='multiFiles')
		for extraAttributes_ in self.getExtraAttributes():
			extraAttributes_.export(outfile, level, name_='extraAttributes')
		if self.__forceDtype is not None:
			self.forceDtype.export(outfile, level, name_='forceDtype')
		if self.__chunkSegmentation is not None:
			self.chunkSegmentation.export(outfile, level, name_='chunkSegmentation')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiFiles':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setMultiFiles(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'extraAttributes':
			obj_ = XSDataHDF5Attributes()
			obj_.build(child_)
			self.extraAttributes.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'forceDtype':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setForceDtype(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chunkSegmentation':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setChunkSegmentation(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputHDF5Writer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputHDF5Writer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputHDF5Writer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputHDF5Writer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5Writer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputHDF5Writer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5Writer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputHDF5Writer

class XSDataResultHDF5Writer(XSDataResult):
	def __init__(self, status=None, internalHDF5Path=None, HDF5File=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultHDF5Writer", "Constructor of XSDataResultHDF5Writer", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		checkType("XSDataResultHDF5Writer", "Constructor of XSDataResultHDF5Writer", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataResultHDF5Writer", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataResultHDF5Writer", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def export(self, outfile, level, name_='XSDataResultHDF5Writer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultHDF5Writer'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultHDF5Writer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultHDF5Writer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultHDF5Writer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultHDF5Writer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5Writer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultHDF5Writer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5Writer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultHDF5Writer

class XSDataInputHDF5MapSpectra(XSDataInputHDF5Writer):
	def __init__(self, configuration=None, chunkSegmentation=None, forceDtype=None, extraAttributes=None, multiFiles=None, internalHDF5Path=None, HDF5File=None, inputSpectrumFile=None, deleteInputSpectrum=None):
		XSDataInputHDF5Writer.__init__(self, configuration, chunkSegmentation, forceDtype, extraAttributes, multiFiles, internalHDF5Path, HDF5File)
		checkType("XSDataInputHDF5MapSpectra", "Constructor of XSDataInputHDF5MapSpectra", deleteInputSpectrum, "XSDataBoolean")
		self.__deleteInputSpectrum = deleteInputSpectrum
		if inputSpectrumFile is None:
			self.__inputSpectrumFile = []
		else:
			checkType("XSDataInputHDF5MapSpectra", "Constructor of XSDataInputHDF5MapSpectra", inputSpectrumFile, "list")
			self.__inputSpectrumFile = inputSpectrumFile
	def getDeleteInputSpectrum(self): return self.__deleteInputSpectrum
	def setDeleteInputSpectrum(self, deleteInputSpectrum):
		checkType("XSDataInputHDF5MapSpectra", "setDeleteInputSpectrum", deleteInputSpectrum, "XSDataBoolean")
		self.__deleteInputSpectrum = deleteInputSpectrum
	def delDeleteInputSpectrum(self): self.__deleteInputSpectrum = None
	# Properties
	deleteInputSpectrum = property(getDeleteInputSpectrum, setDeleteInputSpectrum, delDeleteInputSpectrum, "Property for deleteInputSpectrum")
	def getInputSpectrumFile(self): return self.__inputSpectrumFile
	def setInputSpectrumFile(self, inputSpectrumFile):
		checkType("XSDataInputHDF5MapSpectra", "setInputSpectrumFile", inputSpectrumFile, "list")
		self.__inputSpectrumFile = inputSpectrumFile
	def delInputSpectrumFile(self): self.__inputSpectrumFile = None
	# Properties
	inputSpectrumFile = property(getInputSpectrumFile, setInputSpectrumFile, delInputSpectrumFile, "Property for inputSpectrumFile")
	def addInputSpectrumFile(self, value):
		checkType("XSDataInputHDF5MapSpectra", "setInputSpectrumFile", value, "XSDataSpectrum")
		self.__inputSpectrumFile.append(value)
	def insertInputSpectrumFile(self, index, value):
		checkType("XSDataInputHDF5MapSpectra", "setInputSpectrumFile", value, "XSDataSpectrum")
		self.__inputSpectrumFile[index] = value
	def export(self, outfile, level, name_='XSDataInputHDF5MapSpectra'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputHDF5MapSpectra'):
		XSDataInputHDF5Writer.exportChildren(self, outfile, level, name_)
		if self.__deleteInputSpectrum is not None:
			self.deleteInputSpectrum.export(outfile, level, name_='deleteInputSpectrum')
		for inputSpectrumFile_ in self.getInputSpectrumFile():
			inputSpectrumFile_.export(outfile, level, name_='inputSpectrumFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deleteInputSpectrum':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDeleteInputSpectrum(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputSpectrumFile':
			obj_ = XSDataSpectrum()
			obj_.build(child_)
			self.inputSpectrumFile.append(obj_)
		XSDataInputHDF5Writer.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputHDF5MapSpectra" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputHDF5MapSpectra' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputHDF5MapSpectra is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputHDF5MapSpectra.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5MapSpectra()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputHDF5MapSpectra" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5MapSpectra()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputHDF5MapSpectra

class XSDataInputHDF5StackImages(XSDataInputHDF5Writer):
	def __init__(self, configuration=None, chunkSegmentation=None, forceDtype=None, extraAttributes=None, multiFiles=None, internalHDF5Path=None, HDF5File=None, index=None, inputArray=None, inputImageFile=None, deleteInputImage=None):
		XSDataInputHDF5Writer.__init__(self, configuration, chunkSegmentation, forceDtype, extraAttributes, multiFiles, internalHDF5Path, HDF5File)
		checkType("XSDataInputHDF5StackImages", "Constructor of XSDataInputHDF5StackImages", deleteInputImage, "XSDataBoolean")
		self.__deleteInputImage = deleteInputImage
		if inputImageFile is None:
			self.__inputImageFile = []
		else:
			checkType("XSDataInputHDF5StackImages", "Constructor of XSDataInputHDF5StackImages", inputImageFile, "list")
			self.__inputImageFile = inputImageFile
		if inputArray is None:
			self.__inputArray = []
		else:
			checkType("XSDataInputHDF5StackImages", "Constructor of XSDataInputHDF5StackImages", inputArray, "list")
			self.__inputArray = inputArray
		if index is None:
			self.__index = []
		else:
			checkType("XSDataInputHDF5StackImages", "Constructor of XSDataInputHDF5StackImages", index, "list")
			self.__index = index
	def getDeleteInputImage(self): return self.__deleteInputImage
	def setDeleteInputImage(self, deleteInputImage):
		checkType("XSDataInputHDF5StackImages", "setDeleteInputImage", deleteInputImage, "XSDataBoolean")
		self.__deleteInputImage = deleteInputImage
	def delDeleteInputImage(self): self.__deleteInputImage = None
	# Properties
	deleteInputImage = property(getDeleteInputImage, setDeleteInputImage, delDeleteInputImage, "Property for deleteInputImage")
	def getInputImageFile(self): return self.__inputImageFile
	def setInputImageFile(self, inputImageFile):
		checkType("XSDataInputHDF5StackImages", "setInputImageFile", inputImageFile, "list")
		self.__inputImageFile = inputImageFile
	def delInputImageFile(self): self.__inputImageFile = None
	# Properties
	inputImageFile = property(getInputImageFile, setInputImageFile, delInputImageFile, "Property for inputImageFile")
	def addInputImageFile(self, value):
		checkType("XSDataInputHDF5StackImages", "setInputImageFile", value, "XSDataImage")
		self.__inputImageFile.append(value)
	def insertInputImageFile(self, index, value):
		checkType("XSDataInputHDF5StackImages", "setInputImageFile", value, "XSDataImage")
		self.__inputImageFile[index] = value
	def getInputArray(self): return self.__inputArray
	def setInputArray(self, inputArray):
		checkType("XSDataInputHDF5StackImages", "setInputArray", inputArray, "list")
		self.__inputArray = inputArray
	def delInputArray(self): self.__inputArray = None
	# Properties
	inputArray = property(getInputArray, setInputArray, delInputArray, "Property for inputArray")
	def addInputArray(self, value):
		checkType("XSDataInputHDF5StackImages", "setInputArray", value, "XSDataArray")
		self.__inputArray.append(value)
	def insertInputArray(self, index, value):
		checkType("XSDataInputHDF5StackImages", "setInputArray", value, "XSDataArray")
		self.__inputArray[index] = value
	def getIndex(self): return self.__index
	def setIndex(self, index):
		checkType("XSDataInputHDF5StackImages", "setIndex", index, "list")
		self.__index = index
	def delIndex(self): self.__index = None
	# Properties
	index = property(getIndex, setIndex, delIndex, "Property for index")
	def addIndex(self, value):
		checkType("XSDataInputHDF5StackImages", "setIndex", value, "XSDataInteger")
		self.__index.append(value)
	def insertIndex(self, index, value):
		checkType("XSDataInputHDF5StackImages", "setIndex", value, "XSDataInteger")
		self.__index[index] = value
	def export(self, outfile, level, name_='XSDataInputHDF5StackImages'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputHDF5StackImages'):
		XSDataInputHDF5Writer.exportChildren(self, outfile, level, name_)
		if self.__deleteInputImage is not None:
			self.deleteInputImage.export(outfile, level, name_='deleteInputImage')
		for inputImageFile_ in self.getInputImageFile():
			inputImageFile_.export(outfile, level, name_='inputImageFile')
		for inputArray_ in self.getInputArray():
			inputArray_.export(outfile, level, name_='inputArray')
		for index_ in self.getIndex():
			index_.export(outfile, level, name_='index')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deleteInputImage':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDeleteInputImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputImageFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.inputImageFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.inputArray.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'index':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.index.append(obj_)
		XSDataInputHDF5Writer.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputHDF5StackImages" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputHDF5StackImages' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputHDF5StackImages is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputHDF5StackImages.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5StackImages()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputHDF5StackImages" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputHDF5StackImages()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputHDF5StackImages

class XSDataResultHDF5MapSpectra(XSDataResultHDF5Writer):
	def __init__(self, status=None, internalHDF5Path=None, HDF5File=None):
		XSDataResultHDF5Writer.__init__(self, status, internalHDF5Path, HDF5File)
	def export(self, outfile, level, name_='XSDataResultHDF5MapSpectra'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultHDF5MapSpectra'):
		XSDataResultHDF5Writer.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataResultHDF5Writer.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultHDF5MapSpectra" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultHDF5MapSpectra' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultHDF5MapSpectra is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultHDF5MapSpectra.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5MapSpectra()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultHDF5MapSpectra" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5MapSpectra()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultHDF5MapSpectra

class XSDataResultHDF5StackImages(XSDataResultHDF5Writer):
	def __init__(self, status=None, internalHDF5Path=None, HDF5File=None):
		XSDataResultHDF5Writer.__init__(self, status, internalHDF5Path, HDF5File)
	def export(self, outfile, level, name_='XSDataResultHDF5StackImages'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultHDF5StackImages'):
		XSDataResultHDF5Writer.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataResultHDF5Writer.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultHDF5StackImages" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultHDF5StackImages' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultHDF5StackImages is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultHDF5StackImages.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5StackImages()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultHDF5StackImages" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultHDF5StackImages()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultHDF5StackImages



# End of data representation classes.



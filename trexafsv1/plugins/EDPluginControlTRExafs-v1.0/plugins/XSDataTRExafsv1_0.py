#!/usr/bin/env python

#
# Generated Thu Mar 28 07:15::23 2013 by EDGenerateDS.
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


class XSDataInputTRExafs(XSDataInput):
	def __init__(self, configuration=None, pathToDataArray=None, pathToEnergyArray=None, dataArray=None, energy=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputTRExafs", "Constructor of XSDataInputTRExafs", energy, "XSDataArray")
		self._energy = energy
		checkType("XSDataInputTRExafs", "Constructor of XSDataInputTRExafs", dataArray, "XSDataArray")
		self._dataArray = dataArray
		checkType("XSDataInputTRExafs", "Constructor of XSDataInputTRExafs", pathToEnergyArray, "XSDataFile")
		self._pathToEnergyArray = pathToEnergyArray
		checkType("XSDataInputTRExafs", "Constructor of XSDataInputTRExafs", pathToDataArray, "XSDataFile")
		self._pathToDataArray = pathToDataArray
	def getEnergy(self): return self._energy
	def setEnergy(self, energy):
		checkType("XSDataInputTRExafs", "setEnergy", energy, "XSDataArray")
		self._energy = energy
	def delEnergy(self): self._energy = None
	# Properties
	energy = property(getEnergy, setEnergy, delEnergy, "Property for energy")
	def getDataArray(self): return self._dataArray
	def setDataArray(self, dataArray):
		checkType("XSDataInputTRExafs", "setDataArray", dataArray, "XSDataArray")
		self._dataArray = dataArray
	def delDataArray(self): self._dataArray = None
	# Properties
	dataArray = property(getDataArray, setDataArray, delDataArray, "Property for dataArray")
	def getPathToEnergyArray(self): return self._pathToEnergyArray
	def setPathToEnergyArray(self, pathToEnergyArray):
		checkType("XSDataInputTRExafs", "setPathToEnergyArray", pathToEnergyArray, "XSDataFile")
		self._pathToEnergyArray = pathToEnergyArray
	def delPathToEnergyArray(self): self._pathToEnergyArray = None
	# Properties
	pathToEnergyArray = property(getPathToEnergyArray, setPathToEnergyArray, delPathToEnergyArray, "Property for pathToEnergyArray")
	def getPathToDataArray(self): return self._pathToDataArray
	def setPathToDataArray(self, pathToDataArray):
		checkType("XSDataInputTRExafs", "setPathToDataArray", pathToDataArray, "XSDataFile")
		self._pathToDataArray = pathToDataArray
	def delPathToDataArray(self): self._pathToDataArray = None
	# Properties
	pathToDataArray = property(getPathToDataArray, setPathToDataArray, delPathToDataArray, "Property for pathToDataArray")
	def export(self, outfile, level, name_='XSDataInputTRExafs'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputTRExafs'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._energy is not None:
			self.energy.export(outfile, level, name_='energy')
		if self._dataArray is not None:
			self.dataArray.export(outfile, level, name_='dataArray')
		if self._pathToEnergyArray is not None:
			self.pathToEnergyArray.export(outfile, level, name_='pathToEnergyArray')
		if self._pathToDataArray is not None:
			self.pathToDataArray.export(outfile, level, name_='pathToDataArray')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'energy':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setEnergy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setDataArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToEnergyArray':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToEnergyArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToDataArray':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToDataArray(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputTRExafs" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputTRExafs' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputTRExafs is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputTRExafs.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputTRExafs()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputTRExafs" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputTRExafs()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputTRExafs

class XSDataResultTRExafs(XSDataResult):
	def __init__(self, status=None, nexusFile=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultTRExafs", "Constructor of XSDataResultTRExafs", nexusFile, "XSDataFile")
		self._nexusFile = nexusFile
	def getNexusFile(self): return self._nexusFile
	def setNexusFile(self, nexusFile):
		checkType("XSDataResultTRExafs", "setNexusFile", nexusFile, "XSDataFile")
		self._nexusFile = nexusFile
	def delNexusFile(self): self._nexusFile = None
	# Properties
	nexusFile = property(getNexusFile, setNexusFile, delNexusFile, "Property for nexusFile")
	def export(self, outfile, level, name_='XSDataResultTRExafs'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultTRExafs'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._nexusFile is not None:
			self.nexusFile.export(outfile, level, name_='nexusFile')
		else:
			warnEmptyAttribute("nexusFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nexusFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setNexusFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultTRExafs" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultTRExafs' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultTRExafs is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultTRExafs.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultTRExafs()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultTRExafs" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultTRExafs()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultTRExafs



# End of data representation classes.



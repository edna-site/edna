#!/usr/bin/env python

#
# Generated Tue Jan 31 02:54::19 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { "XSDataCommon": "kernel/datamodel"}

try:
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


class XSDataInputEpydoc(XSDataInput):
	"""docType can be pdf ot html (default)
	verbosity is the one for epydoc, from -1 (-q) to +2 (-vv)
	
	"""
	def __init__(self, configuration=None, projectName=None, verbosity=None, docType=None, sources=None, docPath=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputEpydoc", "Constructor of XSDataInputEpydoc", docPath, "XSDataFile")
		self.__docPath = docPath
		if sources is None:
			self.__sources = []
		else:
			checkType("XSDataInputEpydoc", "Constructor of XSDataInputEpydoc", sources, "list")
			self.__sources = sources
		checkType("XSDataInputEpydoc", "Constructor of XSDataInputEpydoc", docType, "XSDataString")
		self.__docType = docType
		checkType("XSDataInputEpydoc", "Constructor of XSDataInputEpydoc", verbosity, "XSDataInteger")
		self.__verbosity = verbosity
		checkType("XSDataInputEpydoc", "Constructor of XSDataInputEpydoc", projectName, "XSDataString")
		self.__projectName = projectName
	def getDocPath(self): return self.__docPath
	def setDocPath(self, docPath):
		checkType("XSDataInputEpydoc", "setDocPath", docPath, "XSDataFile")
		self.__docPath = docPath
	def delDocPath(self): self.__docPath = None
	# Properties
	docPath = property(getDocPath, setDocPath, delDocPath, "Property for docPath")
	def getSources(self): return self.__sources
	def setSources(self, sources):
		checkType("XSDataInputEpydoc", "setSources", sources, "list")
		self.__sources = sources
	def delSources(self): self.__sources = None
	# Properties
	sources = property(getSources, setSources, delSources, "Property for sources")
	def addSources(self, value):
		checkType("XSDataInputEpydoc", "setSources", value, "XSDataFile")
		self.__sources.append(value)
	def insertSources(self, index, value):
		checkType("XSDataInputEpydoc", "setSources", value, "XSDataFile")
		self.__sources[index] = value
	def getDocType(self): return self.__docType
	def setDocType(self, docType):
		checkType("XSDataInputEpydoc", "setDocType", docType, "XSDataString")
		self.__docType = docType
	def delDocType(self): self.__docType = None
	# Properties
	docType = property(getDocType, setDocType, delDocType, "Property for docType")
	def getVerbosity(self): return self.__verbosity
	def setVerbosity(self, verbosity):
		checkType("XSDataInputEpydoc", "setVerbosity", verbosity, "XSDataInteger")
		self.__verbosity = verbosity
	def delVerbosity(self): self.__verbosity = None
	# Properties
	verbosity = property(getVerbosity, setVerbosity, delVerbosity, "Property for verbosity")
	def getProjectName(self): return self.__projectName
	def setProjectName(self, projectName):
		checkType("XSDataInputEpydoc", "setProjectName", projectName, "XSDataString")
		self.__projectName = projectName
	def delProjectName(self): self.__projectName = None
	# Properties
	projectName = property(getProjectName, setProjectName, delProjectName, "Property for projectName")
	def export(self, outfile, level, name_='XSDataInputEpydoc'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputEpydoc'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__docPath is not None:
			self.docPath.export(outfile, level, name_='docPath')
		else:
			warnEmptyAttribute("docPath", "XSDataFile")
		for sources_ in self.getSources():
			sources_.export(outfile, level, name_='sources')
		if self.getSources() == []:
			warnEmptyAttribute("sources", "XSDataFile")
		if self.__docType is not None:
			self.docType.export(outfile, level, name_='docType')
		if self.__verbosity is not None:
			self.verbosity.export(outfile, level, name_='verbosity')
		if self.__projectName is not None:
			self.projectName.export(outfile, level, name_='projectName')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'docPath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDocPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sources':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.sources.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'docType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDocType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'verbosity':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setVerbosity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'projectName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProjectName(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputEpydoc")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputEpydoc')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputEpydoc is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputEpydoc.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputEpydoc()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputEpydoc")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputEpydoc()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputEpydoc

class XSDataResultEpydoc(XSDataResult):
	def __init__(self, status=None, docPath=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultEpydoc", "Constructor of XSDataResultEpydoc", docPath, "XSDataFile")
		self.__docPath = docPath
	def getDocPath(self): return self.__docPath
	def setDocPath(self, docPath):
		checkType("XSDataResultEpydoc", "setDocPath", docPath, "XSDataFile")
		self.__docPath = docPath
	def delDocPath(self): self.__docPath = None
	# Properties
	docPath = property(getDocPath, setDocPath, delDocPath, "Property for docPath")
	def export(self, outfile, level, name_='XSDataResultEpydoc'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultEpydoc'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__docPath is not None:
			self.docPath.export(outfile, level, name_='docPath')
		else:
			warnEmptyAttribute("docPath", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'docPath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDocPath(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultEpydoc")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultEpydoc')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultEpydoc is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultEpydoc.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultEpydoc()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultEpydoc")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultEpydoc()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultEpydoc



# End of data representation classes.



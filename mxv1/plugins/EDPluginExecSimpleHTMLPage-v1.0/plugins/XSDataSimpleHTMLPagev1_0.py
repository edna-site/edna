#!/usr/bin/env python

#
# Generated Thu Feb 9 12:30::11 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
}

try:
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataResult
	from XSDataMXv1 import XSDataResultCharacterisation
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
from XSDataCommon import XSDataResult
from XSDataMXv1 import XSDataResultCharacterisation




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


class XSDataInputSimpleHTMLPage(XSDataInput):
	def __init__(self, configuration=None, fileGraph=None, characterisationResult=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputSimpleHTMLPage", "Constructor of XSDataInputSimpleHTMLPage", characterisationResult, "XSDataResultCharacterisation")
		self.__characterisationResult = characterisationResult
		if fileGraph is None:
			self.__fileGraph = []
		else:
			checkType("XSDataInputSimpleHTMLPage", "Constructor of XSDataInputSimpleHTMLPage", fileGraph, "list")
			self.__fileGraph = fileGraph
	def getCharacterisationResult(self): return self.__characterisationResult
	def setCharacterisationResult(self, characterisationResult):
		checkType("XSDataInputSimpleHTMLPage", "setCharacterisationResult", characterisationResult, "XSDataResultCharacterisation")
		self.__characterisationResult = characterisationResult
	def delCharacterisationResult(self): self.__characterisationResult = None
	# Properties
	characterisationResult = property(getCharacterisationResult, setCharacterisationResult, delCharacterisationResult, "Property for characterisationResult")
	def getFileGraph(self): return self.__fileGraph
	def setFileGraph(self, fileGraph):
		checkType("XSDataInputSimpleHTMLPage", "setFileGraph", fileGraph, "list")
		self.__fileGraph = fileGraph
	def delFileGraph(self): self.__fileGraph = None
	# Properties
	fileGraph = property(getFileGraph, setFileGraph, delFileGraph, "Property for fileGraph")
	def addFileGraph(self, value):
		checkType("XSDataInputSimpleHTMLPage", "setFileGraph", value, "XSDataFile")
		self.__fileGraph.append(value)
	def insertFileGraph(self, index, value):
		checkType("XSDataInputSimpleHTMLPage", "setFileGraph", value, "XSDataFile")
		self.__fileGraph[index] = value
	def export(self, outfile, level, name_='XSDataInputSimpleHTMLPage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSimpleHTMLPage'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__characterisationResult is not None:
			self.characterisationResult.export(outfile, level, name_='characterisationResult')
		else:
			warnEmptyAttribute("characterisationResult", "XSDataResultCharacterisation")
		for fileGraph_ in self.getFileGraph():
			fileGraph_.export(outfile, level, name_='fileGraph')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'characterisationResult':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setCharacterisationResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileGraph':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.fileGraph.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputSimpleHTMLPage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSimpleHTMLPage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputSimpleHTMLPage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSimpleHTMLPage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSimpleHTMLPage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSimpleHTMLPage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSimpleHTMLPage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSimpleHTMLPage

class XSDataResultSimpleHTMLPage(XSDataResult):
	def __init__(self, status=None, pathToHTMLDirectory=None, pathToHTMLFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultSimpleHTMLPage", "Constructor of XSDataResultSimpleHTMLPage", pathToHTMLFile, "XSDataFile")
		self.__pathToHTMLFile = pathToHTMLFile
		checkType("XSDataResultSimpleHTMLPage", "Constructor of XSDataResultSimpleHTMLPage", pathToHTMLDirectory, "XSDataFile")
		self.__pathToHTMLDirectory = pathToHTMLDirectory
	def getPathToHTMLFile(self): return self.__pathToHTMLFile
	def setPathToHTMLFile(self, pathToHTMLFile):
		checkType("XSDataResultSimpleHTMLPage", "setPathToHTMLFile", pathToHTMLFile, "XSDataFile")
		self.__pathToHTMLFile = pathToHTMLFile
	def delPathToHTMLFile(self): self.__pathToHTMLFile = None
	# Properties
	pathToHTMLFile = property(getPathToHTMLFile, setPathToHTMLFile, delPathToHTMLFile, "Property for pathToHTMLFile")
	def getPathToHTMLDirectory(self): return self.__pathToHTMLDirectory
	def setPathToHTMLDirectory(self, pathToHTMLDirectory):
		checkType("XSDataResultSimpleHTMLPage", "setPathToHTMLDirectory", pathToHTMLDirectory, "XSDataFile")
		self.__pathToHTMLDirectory = pathToHTMLDirectory
	def delPathToHTMLDirectory(self): self.__pathToHTMLDirectory = None
	# Properties
	pathToHTMLDirectory = property(getPathToHTMLDirectory, setPathToHTMLDirectory, delPathToHTMLDirectory, "Property for pathToHTMLDirectory")
	def export(self, outfile, level, name_='XSDataResultSimpleHTMLPage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSimpleHTMLPage'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__pathToHTMLFile is not None:
			self.pathToHTMLFile.export(outfile, level, name_='pathToHTMLFile')
		else:
			warnEmptyAttribute("pathToHTMLFile", "XSDataFile")
		if self.__pathToHTMLDirectory is not None:
			self.pathToHTMLDirectory.export(outfile, level, name_='pathToHTMLDirectory')
		else:
			warnEmptyAttribute("pathToHTMLDirectory", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToHTMLFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToHTMLFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToHTMLDirectory':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToHTMLDirectory(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSimpleHTMLPage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSimpleHTMLPage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultSimpleHTMLPage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSimpleHTMLPage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSimpleHTMLPage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSimpleHTMLPage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSimpleHTMLPage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSimpleHTMLPage



# End of data representation classes.



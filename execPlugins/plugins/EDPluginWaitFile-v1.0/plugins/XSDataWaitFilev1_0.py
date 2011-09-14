#!/usr/bin/env python

#
# Generated Wed Sep 14 05:43::49 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
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


class XSDataInputWaitFile(XSDataInput):
	"""XSDataSize is not applicable here it is the size of a file in Bytes, not the size of a physical object in meters."""
	def __init__(self, configuration=None, timeOut=None, expectedSize=None, expectedFile=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputWaitFile", "Constructor of XSDataInputWaitFile", expectedFile, "XSDataFile")
		self.__expectedFile = expectedFile
		checkType("XSDataInputWaitFile", "Constructor of XSDataInputWaitFile", expectedSize, "XSDataInteger")
		self.__expectedSize = expectedSize
		checkType("XSDataInputWaitFile", "Constructor of XSDataInputWaitFile", timeOut, "XSDataTime")
		self.__timeOut = timeOut
	def getExpectedFile(self): return self.__expectedFile
	def setExpectedFile(self, expectedFile):
		checkType("XSDataInputWaitFile", "setExpectedFile", expectedFile, "XSDataFile")
		self.__expectedFile = expectedFile
	def delExpectedFile(self): self.__expectedFile = None
	# Properties
	expectedFile = property(getExpectedFile, setExpectedFile, delExpectedFile, "Property for expectedFile")
	def getExpectedSize(self): return self.__expectedSize
	def setExpectedSize(self, expectedSize):
		checkType("XSDataInputWaitFile", "setExpectedSize", expectedSize, "XSDataInteger")
		self.__expectedSize = expectedSize
	def delExpectedSize(self): self.__expectedSize = None
	# Properties
	expectedSize = property(getExpectedSize, setExpectedSize, delExpectedSize, "Property for expectedSize")
	def getTimeOut(self): return self.__timeOut
	def setTimeOut(self, timeOut):
		checkType("XSDataInputWaitFile", "setTimeOut", timeOut, "XSDataTime")
		self.__timeOut = timeOut
	def delTimeOut(self): self.__timeOut = None
	# Properties
	timeOut = property(getTimeOut, setTimeOut, delTimeOut, "Property for timeOut")
	def export(self, outfile, level, name_='XSDataInputWaitFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputWaitFile'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__expectedFile is not None:
			self.expectedFile.export(outfile, level, name_='expectedFile')
		else:
			warnEmptyAttribute("expectedFile", "XSDataFile")
		if self.__expectedSize is not None:
			self.expectedSize.export(outfile, level, name_='expectedSize')
		else:
			warnEmptyAttribute("expectedSize", "XSDataInteger")
		if self.__timeOut is not None:
			self.timeOut.export(outfile, level, name_='timeOut')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setExpectedFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setExpectedSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeOut':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTimeOut(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputWaitFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputWaitFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputWaitFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputWaitFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputWaitFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputWaitFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputWaitFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputWaitFile

class XSDataInputWaitMultiFile(XSDataInput):
	def __init__(self, configuration=None, timeOut=None, expectedSize=None, expectedFile=None):
		XSDataInput.__init__(self, configuration)
		if expectedFile is None:
			self.__expectedFile = []
		else:
			checkType("XSDataInputWaitMultiFile", "Constructor of XSDataInputWaitMultiFile", expectedFile, "list")
			self.__expectedFile = expectedFile
		checkType("XSDataInputWaitMultiFile", "Constructor of XSDataInputWaitMultiFile", expectedSize, "XSDataInteger")
		self.__expectedSize = expectedSize
		checkType("XSDataInputWaitMultiFile", "Constructor of XSDataInputWaitMultiFile", timeOut, "XSDataTime")
		self.__timeOut = timeOut
	def getExpectedFile(self): return self.__expectedFile
	def setExpectedFile(self, expectedFile):
		checkType("XSDataInputWaitMultiFile", "setExpectedFile", expectedFile, "list")
		self.__expectedFile = expectedFile
	def delExpectedFile(self): self.__expectedFile = None
	# Properties
	expectedFile = property(getExpectedFile, setExpectedFile, delExpectedFile, "Property for expectedFile")
	def addExpectedFile(self, value):
		checkType("XSDataInputWaitMultiFile", "setExpectedFile", value, "XSDataFile")
		self.__expectedFile.append(value)
	def insertExpectedFile(self, index, value):
		checkType("XSDataInputWaitMultiFile", "setExpectedFile", value, "XSDataFile")
		self.__expectedFile[index] = value
	def getExpectedSize(self): return self.__expectedSize
	def setExpectedSize(self, expectedSize):
		checkType("XSDataInputWaitMultiFile", "setExpectedSize", expectedSize, "XSDataInteger")
		self.__expectedSize = expectedSize
	def delExpectedSize(self): self.__expectedSize = None
	# Properties
	expectedSize = property(getExpectedSize, setExpectedSize, delExpectedSize, "Property for expectedSize")
	def getTimeOut(self): return self.__timeOut
	def setTimeOut(self, timeOut):
		checkType("XSDataInputWaitMultiFile", "setTimeOut", timeOut, "XSDataTime")
		self.__timeOut = timeOut
	def delTimeOut(self): self.__timeOut = None
	# Properties
	timeOut = property(getTimeOut, setTimeOut, delTimeOut, "Property for timeOut")
	def export(self, outfile, level, name_='XSDataInputWaitMultiFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputWaitMultiFile'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for expectedFile_ in self.getExpectedFile():
			expectedFile_.export(outfile, level, name_='expectedFile')
		if self.getExpectedFile() == []:
			warnEmptyAttribute("expectedFile", "XSDataFile")
		if self.__expectedSize is not None:
			self.expectedSize.export(outfile, level, name_='expectedSize')
		else:
			warnEmptyAttribute("expectedSize", "XSDataInteger")
		if self.__timeOut is not None:
			self.timeOut.export(outfile, level, name_='timeOut')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.expectedFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setExpectedSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeOut':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTimeOut(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputWaitMultiFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputWaitMultiFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputWaitMultiFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputWaitMultiFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputWaitMultiFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputWaitMultiFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputWaitMultiFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputWaitMultiFile

class XSDataResultWaitFile(XSDataResult):
	def __init__(self, status=None, timedOut=None, actualSize=None, actualFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultWaitFile", "Constructor of XSDataResultWaitFile", actualFile, "XSDataFile")
		self.__actualFile = actualFile
		checkType("XSDataResultWaitFile", "Constructor of XSDataResultWaitFile", actualSize, "XSDataInteger")
		self.__actualSize = actualSize
		checkType("XSDataResultWaitFile", "Constructor of XSDataResultWaitFile", timedOut, "XSDataBoolean")
		self.__timedOut = timedOut
	def getActualFile(self): return self.__actualFile
	def setActualFile(self, actualFile):
		checkType("XSDataResultWaitFile", "setActualFile", actualFile, "XSDataFile")
		self.__actualFile = actualFile
	def delActualFile(self): self.__actualFile = None
	# Properties
	actualFile = property(getActualFile, setActualFile, delActualFile, "Property for actualFile")
	def getActualSize(self): return self.__actualSize
	def setActualSize(self, actualSize):
		checkType("XSDataResultWaitFile", "setActualSize", actualSize, "XSDataInteger")
		self.__actualSize = actualSize
	def delActualSize(self): self.__actualSize = None
	# Properties
	actualSize = property(getActualSize, setActualSize, delActualSize, "Property for actualSize")
	def getTimedOut(self): return self.__timedOut
	def setTimedOut(self, timedOut):
		checkType("XSDataResultWaitFile", "setTimedOut", timedOut, "XSDataBoolean")
		self.__timedOut = timedOut
	def delTimedOut(self): self.__timedOut = None
	# Properties
	timedOut = property(getTimedOut, setTimedOut, delTimedOut, "Property for timedOut")
	def export(self, outfile, level, name_='XSDataResultWaitFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultWaitFile'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__actualFile is not None:
			self.actualFile.export(outfile, level, name_='actualFile')
		if self.__actualSize is not None:
			self.actualSize.export(outfile, level, name_='actualSize')
		if self.__timedOut is not None:
			self.timedOut.export(outfile, level, name_='timedOut')
		else:
			warnEmptyAttribute("timedOut", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'actualFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setActualFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'actualSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setActualSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timedOut':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setTimedOut(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultWaitFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultWaitFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultWaitFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultWaitFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultWaitFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultWaitFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultWaitFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultWaitFile

class XSDataResultWaitMultiFile(XSDataResult):
	def __init__(self, status=None, timedOut=None, actualMinSize=None, actualFile=None):
		XSDataResult.__init__(self, status)
		if actualFile is None:
			self.__actualFile = []
		else:
			checkType("XSDataResultWaitMultiFile", "Constructor of XSDataResultWaitMultiFile", actualFile, "list")
			self.__actualFile = actualFile
		checkType("XSDataResultWaitMultiFile", "Constructor of XSDataResultWaitMultiFile", actualMinSize, "XSDataInteger")
		self.__actualMinSize = actualMinSize
		checkType("XSDataResultWaitMultiFile", "Constructor of XSDataResultWaitMultiFile", timedOut, "XSDataBoolean")
		self.__timedOut = timedOut
	def getActualFile(self): return self.__actualFile
	def setActualFile(self, actualFile):
		checkType("XSDataResultWaitMultiFile", "setActualFile", actualFile, "list")
		self.__actualFile = actualFile
	def delActualFile(self): self.__actualFile = None
	# Properties
	actualFile = property(getActualFile, setActualFile, delActualFile, "Property for actualFile")
	def addActualFile(self, value):
		checkType("XSDataResultWaitMultiFile", "setActualFile", value, "XSDataFile")
		self.__actualFile.append(value)
	def insertActualFile(self, index, value):
		checkType("XSDataResultWaitMultiFile", "setActualFile", value, "XSDataFile")
		self.__actualFile[index] = value
	def getActualMinSize(self): return self.__actualMinSize
	def setActualMinSize(self, actualMinSize):
		checkType("XSDataResultWaitMultiFile", "setActualMinSize", actualMinSize, "XSDataInteger")
		self.__actualMinSize = actualMinSize
	def delActualMinSize(self): self.__actualMinSize = None
	# Properties
	actualMinSize = property(getActualMinSize, setActualMinSize, delActualMinSize, "Property for actualMinSize")
	def getTimedOut(self): return self.__timedOut
	def setTimedOut(self, timedOut):
		checkType("XSDataResultWaitMultiFile", "setTimedOut", timedOut, "XSDataBoolean")
		self.__timedOut = timedOut
	def delTimedOut(self): self.__timedOut = None
	# Properties
	timedOut = property(getTimedOut, setTimedOut, delTimedOut, "Property for timedOut")
	def export(self, outfile, level, name_='XSDataResultWaitMultiFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultWaitMultiFile'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for actualFile_ in self.getActualFile():
			actualFile_.export(outfile, level, name_='actualFile')
		if self.__actualMinSize is not None:
			self.actualMinSize.export(outfile, level, name_='actualMinSize')
		if self.__timedOut is not None:
			self.timedOut.export(outfile, level, name_='timedOut')
		else:
			warnEmptyAttribute("timedOut", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'actualFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.actualFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'actualMinSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setActualMinSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timedOut':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setTimedOut(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultWaitMultiFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultWaitMultiFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultWaitMultiFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultWaitMultiFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultWaitMultiFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultWaitMultiFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultWaitMultiFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultWaitMultiFile



# End of data representation classes.



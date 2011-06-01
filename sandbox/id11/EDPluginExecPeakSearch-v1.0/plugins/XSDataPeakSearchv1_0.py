#!/usr/bin/env python

#
# Generated Tue Apr 5 03:31::23 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

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
	elif _value is None:
		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
		print(strMessage)
		#raise BaseException(strMessage)


def warnEmptyAttribute(_strName, _strTypeName):
	pass
	#if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
	#		print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer:
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


class XSDataInputPeakSearch(XSDataInput):
	def __init__(self, configuration=None, threshold=None, stem=None, outputStem=None, numberOfDigits=None, indexMin=None, indexMax=None, imageFormat=None, darkFile=None):
		XSDataInput.__init__(self, configuration)
		self.__darkFile = darkFile
		self.__imageFormat = imageFormat
		self.__indexMax = indexMax
		self.__indexMin = indexMin
		self.__numberOfDigits = numberOfDigits
		self.__outputStem = outputStem
		self.__stem = stem
		if threshold is None:
			self.__threshold = []
		else:
			self.__threshold = threshold
	def getDarkFile(self): return self.__darkFile
	def setDarkFile(self, darkFile):
		checkType("XSDataInputPeakSearch", "setDarkFile", darkFile, "XSDataFile")
		self.__darkFile = darkFile
	def delDarkFile(self): self.__darkFile = None
	# Properties
	darkFile = property(getDarkFile, setDarkFile, delDarkFile, "Property for darkFile")
	def getImageFormat(self): return self.__imageFormat
	def setImageFormat(self, imageFormat):
		checkType("XSDataInputPeakSearch", "setImageFormat", imageFormat, "XSDataString")
		self.__imageFormat = imageFormat
	def delImageFormat(self): self.__imageFormat = None
	# Properties
	imageFormat = property(getImageFormat, setImageFormat, delImageFormat, "Property for imageFormat")
	def getIndexMax(self): return self.__indexMax
	def setIndexMax(self, indexMax):
		checkType("XSDataInputPeakSearch", "setIndexMax", indexMax, "XSDataInteger")
		self.__indexMax = indexMax
	def delIndexMax(self): self.__indexMax = None
	# Properties
	indexMax = property(getIndexMax, setIndexMax, delIndexMax, "Property for indexMax")
	def getIndexMin(self): return self.__indexMin
	def setIndexMin(self, indexMin):
		checkType("XSDataInputPeakSearch", "setIndexMin", indexMin, "XSDataInteger")
		self.__indexMin = indexMin
	def delIndexMin(self): self.__indexMin = None
	# Properties
	indexMin = property(getIndexMin, setIndexMin, delIndexMin, "Property for indexMin")
	def getNumberOfDigits(self): return self.__numberOfDigits
	def setNumberOfDigits(self, numberOfDigits):
		checkType("XSDataInputPeakSearch", "setNumberOfDigits", numberOfDigits, "XSDataInteger")
		self.__numberOfDigits = numberOfDigits
	def delNumberOfDigits(self): self.__numberOfDigits = None
	# Properties
	numberOfDigits = property(getNumberOfDigits, setNumberOfDigits, delNumberOfDigits, "Property for numberOfDigits")
	def getOutputStem(self): return self.__outputStem
	def setOutputStem(self, outputStem):
		checkType("XSDataInputPeakSearch", "setOutputStem", outputStem, "XSDataString")
		self.__outputStem = outputStem
	def delOutputStem(self): self.__outputStem = None
	# Properties
	outputStem = property(getOutputStem, setOutputStem, delOutputStem, "Property for outputStem")
	def getStem(self): return self.__stem
	def setStem(self, stem):
		checkType("XSDataInputPeakSearch", "setStem", stem, "XSDataString")
		self.__stem = stem
	def delStem(self): self.__stem = None
	# Properties
	stem = property(getStem, setStem, delStem, "Property for stem")
	def getThreshold(self): return self.__threshold
	def setThreshold(self, threshold):
		checkType("XSDataInputPeakSearch", "setThreshold", threshold, "list")
		self.__threshold = threshold
	def delThreshold(self): self.__threshold = None
	# Properties
	threshold = property(getThreshold, setThreshold, delThreshold, "Property for threshold")
	def addThreshold(self, value):
		checkType("XSDataInputPeakSearch", "setThreshold", value, "XSDataDouble")
		self.__threshold.append(value)
	def insertThreshold(self, index, value):
		checkType("XSDataInputPeakSearch", "setThreshold", value, "XSDataDouble")
		self.__threshold[index] = value
	def export(self, outfile, level, name_='XSDataInputPeakSearch'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputPeakSearch'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__darkFile is not None:
			self.darkFile.export(outfile, level, name_='darkFile')
		if self.__imageFormat is not None:
			self.imageFormat.export(outfile, level, name_='imageFormat')
		if self.__indexMax is not None:
			self.indexMax.export(outfile, level, name_='indexMax')
		else:
			warnEmptyAttribute("indexMax", "XSDataInteger")
		if self.__indexMin is not None:
			self.indexMin.export(outfile, level, name_='indexMin')
		else:
			warnEmptyAttribute("indexMin", "XSDataInteger")
		if self.__numberOfDigits is not None:
			self.numberOfDigits.export(outfile, level, name_='numberOfDigits')
		if self.__outputStem is not None:
			self.outputStem.export(outfile, level, name_='outputStem')
		if self.__stem is not None:
			self.stem.export(outfile, level, name_='stem')
		else:
			warnEmptyAttribute("stem", "XSDataString")
		for threshold_ in self.getThreshold():
			threshold_.export(outfile, level, name_='threshold')
		if self.getThreshold() == []:
			warnEmptyAttribute("threshold", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDarkFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageFormat':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImageFormat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'indexMax':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIndexMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'indexMin':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIndexMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfDigits':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfDigits(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputStem':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutputStem(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'stem':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStem(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'threshold':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.threshold.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputPeakSearch" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputPeakSearch' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputPeakSearch.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputPeakSearch()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputPeakSearch" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputPeakSearch()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputPeakSearch

class XSDataResultPeakSearch(XSDataResult):
	def __init__(self, status=None, peakFile3D=None, peakFile2D=None):
		XSDataResult.__init__(self, status)
		if peakFile2D is None:
			self.__peakFile2D = []
		else:
			self.__peakFile2D = peakFile2D
		if peakFile3D is None:
			self.__peakFile3D = []
		else:
			self.__peakFile3D = peakFile3D
	def getPeakFile2D(self): return self.__peakFile2D
	def setPeakFile2D(self, peakFile2D):
		checkType("XSDataResultPeakSearch", "setPeakFile2D", peakFile2D, "list")
		self.__peakFile2D = peakFile2D
	def delPeakFile2D(self): self.__peakFile2D = None
	# Properties
	peakFile2D = property(getPeakFile2D, setPeakFile2D, delPeakFile2D, "Property for peakFile2D")
	def addPeakFile2D(self, value):
		checkType("XSDataResultPeakSearch", "setPeakFile2D", value, "XSDataFile")
		self.__peakFile2D.append(value)
	def insertPeakFile2D(self, index, value):
		checkType("XSDataResultPeakSearch", "setPeakFile2D", value, "XSDataFile")
		self.__peakFile2D[index] = value
	def getPeakFile3D(self): return self.__peakFile3D
	def setPeakFile3D(self, peakFile3D):
		checkType("XSDataResultPeakSearch", "setPeakFile3D", peakFile3D, "list")
		self.__peakFile3D = peakFile3D
	def delPeakFile3D(self): self.__peakFile3D = None
	# Properties
	peakFile3D = property(getPeakFile3D, setPeakFile3D, delPeakFile3D, "Property for peakFile3D")
	def addPeakFile3D(self, value):
		checkType("XSDataResultPeakSearch", "setPeakFile3D", value, "XSDataFile")
		self.__peakFile3D.append(value)
	def insertPeakFile3D(self, index, value):
		checkType("XSDataResultPeakSearch", "setPeakFile3D", value, "XSDataFile")
		self.__peakFile3D[index] = value
	def export(self, outfile, level, name_='XSDataResultPeakSearch'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultPeakSearch'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for peakFile2D_ in self.getPeakFile2D():
			peakFile2D_.export(outfile, level, name_='peakFile2D')
		if self.getPeakFile2D() == []:
			warnEmptyAttribute("peakFile2D", "XSDataFile")
		for peakFile3D_ in self.getPeakFile3D():
			peakFile3D_.export(outfile, level, name_='peakFile3D')
		if self.getPeakFile3D() == []:
			warnEmptyAttribute("peakFile3D", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'peakFile2D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.peakFile2D.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'peakFile3D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.peakFile3D.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultPeakSearch" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultPeakSearch' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultPeakSearch.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultPeakSearch()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultPeakSearch" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultPeakSearch()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultPeakSearch



# End of data representation classes.



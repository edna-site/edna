#!/usr/bin/env python

#
# Generated Mon Mar 5 04:13::45 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = {"XSDataCommon": "kernel/datamodel"}

try:
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataImageExt
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataImageExt




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


class XSDataInputNormalize(XSDataInput):
	"""Optionnaly can scale intensities on input data with the given factor"""
	def __init__(self, configuration=None, flatScaleFactor=None, darkScaleFactor=None, dataScaleFactor=None, output=None, flat=None, dark=None, data=None):
		XSDataInput.__init__(self, configuration)
		if data is None:
			self.__data = []
		else:
			checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", data, "list")
			self.__data = data
		if dark is None:
			self.__dark = []
		else:
			checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", dark, "list")
			self.__dark = dark
		if flat is None:
			self.__flat = []
		else:
			checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", flat, "list")
			self.__flat = flat
		checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", output, "XSDataImageExt")
		self.__output = output
		checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", dataScaleFactor, "XSDataDouble")
		self.__dataScaleFactor = dataScaleFactor
		checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", darkScaleFactor, "XSDataDouble")
		self.__darkScaleFactor = darkScaleFactor
		checkType("XSDataInputNormalize", "Constructor of XSDataInputNormalize", flatScaleFactor, "XSDataDouble")
		self.__flatScaleFactor = flatScaleFactor
	def getData(self): return self.__data
	def setData(self, data):
		checkType("XSDataInputNormalize", "setData", data, "list")
		self.__data = data
	def delData(self): self.__data = None
	# Properties
	data = property(getData, setData, delData, "Property for data")
	def addData(self, value):
		checkType("XSDataInputNormalize", "setData", value, "XSDataImageExt")
		self.__data.append(value)
	def insertData(self, index, value):
		checkType("XSDataInputNormalize", "setData", value, "XSDataImageExt")
		self.__data[index] = value
	def getDark(self): return self.__dark
	def setDark(self, dark):
		checkType("XSDataInputNormalize", "setDark", dark, "list")
		self.__dark = dark
	def delDark(self): self.__dark = None
	# Properties
	dark = property(getDark, setDark, delDark, "Property for dark")
	def addDark(self, value):
		checkType("XSDataInputNormalize", "setDark", value, "XSDataImageExt")
		self.__dark.append(value)
	def insertDark(self, index, value):
		checkType("XSDataInputNormalize", "setDark", value, "XSDataImageExt")
		self.__dark[index] = value
	def getFlat(self): return self.__flat
	def setFlat(self, flat):
		checkType("XSDataInputNormalize", "setFlat", flat, "list")
		self.__flat = flat
	def delFlat(self): self.__flat = None
	# Properties
	flat = property(getFlat, setFlat, delFlat, "Property for flat")
	def addFlat(self, value):
		checkType("XSDataInputNormalize", "setFlat", value, "XSDataImageExt")
		self.__flat.append(value)
	def insertFlat(self, index, value):
		checkType("XSDataInputNormalize", "setFlat", value, "XSDataImageExt")
		self.__flat[index] = value
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataInputNormalize", "setOutput", output, "XSDataImageExt")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def getDataScaleFactor(self): return self.__dataScaleFactor
	def setDataScaleFactor(self, dataScaleFactor):
		checkType("XSDataInputNormalize", "setDataScaleFactor", dataScaleFactor, "XSDataDouble")
		self.__dataScaleFactor = dataScaleFactor
	def delDataScaleFactor(self): self.__dataScaleFactor = None
	# Properties
	dataScaleFactor = property(getDataScaleFactor, setDataScaleFactor, delDataScaleFactor, "Property for dataScaleFactor")
	def getDarkScaleFactor(self): return self.__darkScaleFactor
	def setDarkScaleFactor(self, darkScaleFactor):
		checkType("XSDataInputNormalize", "setDarkScaleFactor", darkScaleFactor, "XSDataDouble")
		self.__darkScaleFactor = darkScaleFactor
	def delDarkScaleFactor(self): self.__darkScaleFactor = None
	# Properties
	darkScaleFactor = property(getDarkScaleFactor, setDarkScaleFactor, delDarkScaleFactor, "Property for darkScaleFactor")
	def getFlatScaleFactor(self): return self.__flatScaleFactor
	def setFlatScaleFactor(self, flatScaleFactor):
		checkType("XSDataInputNormalize", "setFlatScaleFactor", flatScaleFactor, "XSDataDouble")
		self.__flatScaleFactor = flatScaleFactor
	def delFlatScaleFactor(self): self.__flatScaleFactor = None
	# Properties
	flatScaleFactor = property(getFlatScaleFactor, setFlatScaleFactor, delFlatScaleFactor, "Property for flatScaleFactor")
	def export(self, outfile, level, name_='XSDataInputNormalize'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputNormalize'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for data_ in self.getData():
			data_.export(outfile, level, name_='data')
		if self.getData() == []:
			warnEmptyAttribute("data", "XSDataImageExt")
		for dark_ in self.getDark():
			dark_.export(outfile, level, name_='dark')
		for flat_ in self.getFlat():
			flat_.export(outfile, level, name_='flat')
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		if self.__dataScaleFactor is not None:
			self.dataScaleFactor.export(outfile, level, name_='dataScaleFactor')
		if self.__darkScaleFactor is not None:
			self.darkScaleFactor.export(outfile, level, name_='darkScaleFactor')
		if self.__flatScaleFactor is not None:
			self.flatScaleFactor.export(outfile, level, name_='flatScaleFactor')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'data':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.data.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dark':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.dark.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flat':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.flat.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDataScaleFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDarkScaleFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flatScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFlatScaleFactor(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputNormalize")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputNormalize')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputNormalize is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputNormalize.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputNormalize()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputNormalize")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputNormalize()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputNormalize

class XSDataResultNormalize(XSDataResult):
	def __init__(self, status=None, output=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultNormalize", "Constructor of XSDataResultNormalize", output, "XSDataImageExt")
		self.__output = output
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataResultNormalize", "setOutput", output, "XSDataImageExt")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def export(self, outfile, level, name_='XSDataResultNormalize'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultNormalize'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		else:
			warnEmptyAttribute("output", "XSDataImageExt")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setOutput(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultNormalize")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultNormalize')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultNormalize is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultNormalize.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultNormalize()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultNormalize")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultNormalize()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultNormalize



# End of data representation classes.



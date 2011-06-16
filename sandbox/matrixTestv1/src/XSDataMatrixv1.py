#!/usr/bin/env python

#
# Generated Thu Jun 16 03:07::23 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

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
	elif _value is None:
		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
		print(strMessage)
		#raise BaseException(strMessage)


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


class XSDataInputMatrixInvert(XSDataInput):
	def __init__(self, configuration=None, inputMatrix=None):
		XSDataInput.__init__(self, configuration)
		self.__inputMatrix = inputMatrix
	def getInputMatrix(self): return self.__inputMatrix
	def setInputMatrix(self, inputMatrix):
		checkType("XSDataInputMatrixInvert", "setInputMatrix", inputMatrix, "XSDataArray")
		self.__inputMatrix = inputMatrix
	def delInputMatrix(self): self.__inputMatrix = None
	# Properties
	inputMatrix = property(getInputMatrix, setInputMatrix, delInputMatrix, "Property for inputMatrix")
	def export(self, outfile, level, name_='XSDataInputMatrixInvert'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputMatrixInvert'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputMatrix is not None:
			self.inputMatrix.export(outfile, level, name_='inputMatrix')
		else:
			warnEmptyAttribute("inputMatrix", "XSDataArray")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputMatrix':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setInputMatrix(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputMatrixInvert" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputMatrixInvert' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputMatrixInvert.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputMatrixInvert()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputMatrixInvert" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputMatrixInvert()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputMatrixInvert

class XSDataInputMatrixInvertFile(XSDataInput):
	def __init__(self, configuration=None, outputMatrixFile=None, inputMatrixFile=None):
		XSDataInput.__init__(self, configuration)
		self.__inputMatrixFile = inputMatrixFile
		self.__outputMatrixFile = outputMatrixFile
	def getInputMatrixFile(self): return self.__inputMatrixFile
	def setInputMatrixFile(self, inputMatrixFile):
		checkType("XSDataInputMatrixInvertFile", "setInputMatrixFile", inputMatrixFile, "XSDataFile")
		self.__inputMatrixFile = inputMatrixFile
	def delInputMatrixFile(self): self.__inputMatrixFile = None
	# Properties
	inputMatrixFile = property(getInputMatrixFile, setInputMatrixFile, delInputMatrixFile, "Property for inputMatrixFile")
	def getOutputMatrixFile(self): return self.__outputMatrixFile
	def setOutputMatrixFile(self, outputMatrixFile):
		checkType("XSDataInputMatrixInvertFile", "setOutputMatrixFile", outputMatrixFile, "XSDataFile")
		self.__outputMatrixFile = outputMatrixFile
	def delOutputMatrixFile(self): self.__outputMatrixFile = None
	# Properties
	outputMatrixFile = property(getOutputMatrixFile, setOutputMatrixFile, delOutputMatrixFile, "Property for outputMatrixFile")
	def export(self, outfile, level, name_='XSDataInputMatrixInvertFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputMatrixInvertFile'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputMatrixFile is not None:
			self.inputMatrixFile.export(outfile, level, name_='inputMatrixFile')
		else:
			warnEmptyAttribute("inputMatrixFile", "XSDataFile")
		if self.__outputMatrixFile is not None:
			self.outputMatrixFile.export(outfile, level, name_='outputMatrixFile')
		else:
			warnEmptyAttribute("outputMatrixFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputMatrixFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputMatrixFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputMatrixInvertFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputMatrixInvertFile' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputMatrixInvertFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputMatrixInvertFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputMatrixInvertFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputMatrixInvertFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputMatrixInvertFile

class XSDataInputReadMatrix(XSDataInput):
	def __init__(self, configuration=None, inputMatrixFile=None):
		XSDataInput.__init__(self, configuration)
		self.__inputMatrixFile = inputMatrixFile
	def getInputMatrixFile(self): return self.__inputMatrixFile
	def setInputMatrixFile(self, inputMatrixFile):
		checkType("XSDataInputReadMatrix", "setInputMatrixFile", inputMatrixFile, "XSDataFile")
		self.__inputMatrixFile = inputMatrixFile
	def delInputMatrixFile(self): self.__inputMatrixFile = None
	# Properties
	inputMatrixFile = property(getInputMatrixFile, setInputMatrixFile, delInputMatrixFile, "Property for inputMatrixFile")
	def export(self, outfile, level, name_='XSDataInputReadMatrix'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputReadMatrix'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputMatrixFile is not None:
			self.inputMatrixFile.export(outfile, level, name_='inputMatrixFile')
		else:
			warnEmptyAttribute("inputMatrixFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputMatrixFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputReadMatrix" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputReadMatrix' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputReadMatrix.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadMatrix()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputReadMatrix" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadMatrix()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputReadMatrix

class XSDataInputWriteMatrix(XSDataInput):
	def __init__(self, configuration=None, outputMatrixFile=None, inputMatrix=None):
		XSDataInput.__init__(self, configuration)
		self.__inputMatrix = inputMatrix
		self.__outputMatrixFile = outputMatrixFile
	def getInputMatrix(self): return self.__inputMatrix
	def setInputMatrix(self, inputMatrix):
		checkType("XSDataInputWriteMatrix", "setInputMatrix", inputMatrix, "XSDataArray")
		self.__inputMatrix = inputMatrix
	def delInputMatrix(self): self.__inputMatrix = None
	# Properties
	inputMatrix = property(getInputMatrix, setInputMatrix, delInputMatrix, "Property for inputMatrix")
	def getOutputMatrixFile(self): return self.__outputMatrixFile
	def setOutputMatrixFile(self, outputMatrixFile):
		checkType("XSDataInputWriteMatrix", "setOutputMatrixFile", outputMatrixFile, "XSDataFile")
		self.__outputMatrixFile = outputMatrixFile
	def delOutputMatrixFile(self): self.__outputMatrixFile = None
	# Properties
	outputMatrixFile = property(getOutputMatrixFile, setOutputMatrixFile, delOutputMatrixFile, "Property for outputMatrixFile")
	def export(self, outfile, level, name_='XSDataInputWriteMatrix'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputWriteMatrix'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputMatrix is not None:
			self.inputMatrix.export(outfile, level, name_='inputMatrix')
		else:
			warnEmptyAttribute("inputMatrix", "XSDataArray")
		if self.__outputMatrixFile is not None:
			self.outputMatrixFile.export(outfile, level, name_='outputMatrixFile')
		else:
			warnEmptyAttribute("outputMatrixFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputMatrix':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setInputMatrix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputMatrixFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputWriteMatrix" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputWriteMatrix' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputWriteMatrix.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputWriteMatrix()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputWriteMatrix" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputWriteMatrix()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputWriteMatrix

class XSDataResultMatrixInvert(XSDataResult):
	def __init__(self, status=None, outputMatrix=None):
		XSDataResult.__init__(self, status)
		self.__outputMatrix = outputMatrix
	def getOutputMatrix(self): return self.__outputMatrix
	def setOutputMatrix(self, outputMatrix):
		checkType("XSDataResultMatrixInvert", "setOutputMatrix", outputMatrix, "XSDataArray")
		self.__outputMatrix = outputMatrix
	def delOutputMatrix(self): self.__outputMatrix = None
	# Properties
	outputMatrix = property(getOutputMatrix, setOutputMatrix, delOutputMatrix, "Property for outputMatrix")
	def export(self, outfile, level, name_='XSDataResultMatrixInvert'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultMatrixInvert'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputMatrix is not None:
			self.outputMatrix.export(outfile, level, name_='outputMatrix')
		else:
			warnEmptyAttribute("outputMatrix", "XSDataArray")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrix':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setOutputMatrix(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultMatrixInvert" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultMatrixInvert' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultMatrixInvert.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultMatrixInvert()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultMatrixInvert" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultMatrixInvert()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultMatrixInvert

class XSDataResultMatrixInvertFile(XSDataResult):
	def __init__(self, status=None, outputMatrixFile=None):
		XSDataResult.__init__(self, status)
		self.__outputMatrixFile = outputMatrixFile
	def getOutputMatrixFile(self): return self.__outputMatrixFile
	def setOutputMatrixFile(self, outputMatrixFile):
		checkType("XSDataResultMatrixInvertFile", "setOutputMatrixFile", outputMatrixFile, "XSDataFile")
		self.__outputMatrixFile = outputMatrixFile
	def delOutputMatrixFile(self): self.__outputMatrixFile = None
	# Properties
	outputMatrixFile = property(getOutputMatrixFile, setOutputMatrixFile, delOutputMatrixFile, "Property for outputMatrixFile")
	def export(self, outfile, level, name_='XSDataResultMatrixInvertFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultMatrixInvertFile'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputMatrixFile is not None:
			self.outputMatrixFile.export(outfile, level, name_='outputMatrixFile')
		else:
			warnEmptyAttribute("outputMatrixFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputMatrixFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultMatrixInvertFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultMatrixInvertFile' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultMatrixInvertFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultMatrixInvertFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultMatrixInvertFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultMatrixInvertFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultMatrixInvertFile

class XSDataResultReadMatrix(XSDataResult):
	def __init__(self, status=None, outputMatrix=None):
		XSDataResult.__init__(self, status)
		self.__outputMatrix = outputMatrix
	def getOutputMatrix(self): return self.__outputMatrix
	def setOutputMatrix(self, outputMatrix):
		checkType("XSDataResultReadMatrix", "setOutputMatrix", outputMatrix, "XSDataArray")
		self.__outputMatrix = outputMatrix
	def delOutputMatrix(self): self.__outputMatrix = None
	# Properties
	outputMatrix = property(getOutputMatrix, setOutputMatrix, delOutputMatrix, "Property for outputMatrix")
	def export(self, outfile, level, name_='XSDataResultReadMatrix'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultReadMatrix'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputMatrix is not None:
			self.outputMatrix.export(outfile, level, name_='outputMatrix')
		else:
			warnEmptyAttribute("outputMatrix", "XSDataArray")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrix':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setOutputMatrix(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultReadMatrix" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultReadMatrix' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultReadMatrix.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadMatrix()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultReadMatrix" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadMatrix()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultReadMatrix

class XSDataResultWriteMatrix(XSDataResult):
	def __init__(self, status=None, outputMatrixFile=None):
		XSDataResult.__init__(self, status)
		self.__outputMatrixFile = outputMatrixFile
	def getOutputMatrixFile(self): return self.__outputMatrixFile
	def setOutputMatrixFile(self, outputMatrixFile):
		checkType("XSDataResultWriteMatrix", "setOutputMatrixFile", outputMatrixFile, "XSDataFile")
		self.__outputMatrixFile = outputMatrixFile
	def delOutputMatrixFile(self): self.__outputMatrixFile = None
	# Properties
	outputMatrixFile = property(getOutputMatrixFile, setOutputMatrixFile, delOutputMatrixFile, "Property for outputMatrixFile")
	def export(self, outfile, level, name_='XSDataResultWriteMatrix'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultWriteMatrix'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputMatrixFile is not None:
			self.outputMatrixFile.export(outfile, level, name_='outputMatrixFile')
		else:
			warnEmptyAttribute("outputMatrixFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputMatrixFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputMatrixFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultWriteMatrix" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultWriteMatrix' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultWriteMatrix.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultWriteMatrix()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultWriteMatrix" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultWriteMatrix()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultWriteMatrix



# End of data representation classes.



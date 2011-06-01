#!/usr/bin/env python

#
# Generated Fri May 20 03:01::25 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSDataDouble
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


class XSDataInputDatcmp(XSDataInput):
	"""datcmp compares two curves from files
	"""
	def __init__(self, configuration=None, inputCurve=None):
		XSDataInput.__init__(self, configuration)
		if inputCurve is None:
			self.__inputCurve = []
		else:
			checkType("XSDataInputDatcmp", "Constructor of XSDataInputDatcmp", inputCurve, "XSDataFile")
			self.__inputCurve = inputCurve
	def getInputCurve(self): return self.__inputCurve
	def setInputCurve(self, inputCurve):
		checkType("XSDataInputDatcmp", "setInputCurve", inputCurve, "list")
		self.__inputCurve = inputCurve
	def delInputCurve(self): self.__inputCurve = None
	# Properties
	inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
	def addInputCurve(self, value):
		checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
		self.__inputCurve.append(value)
	def insertInputCurve(self, index, value):
		checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
		self.__inputCurve[index] = value
	def export(self, outfile, level, name_='XSDataInputDatcmp'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDatcmp'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputCurve_ in self.getInputCurve():
			inputCurve_.export(outfile, level, name_='inputCurve')
		if self.getInputCurve() == []:
			warnEmptyAttribute("inputCurve", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurve.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputDatcmp" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputDatcmp' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARING: Method outputFile in class XSDataInputDatcmp is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputDatcmp.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatcmp()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputDatcmp" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatcmp()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputDatcmp

class XSDataResultDatcmp(XSDataResult):
	"""Higher chi-values indicate dis-similarities in the input.

	 Fidelity gives the likelihood of the two data sets being identical.
	"""
	def __init__(self, status=None, fidelity=None, chi=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", chi, "XSDataDouble")
		self.__chi = chi
		checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", fidelity, "XSDataDouble")
		self.__fidelity = fidelity
	def getChi(self): return self.__chi
	def setChi(self, chi):
		checkType("XSDataResultDatcmp", "setChi", chi, "XSDataDouble")
		self.__chi = chi
	def delChi(self): self.__chi = None
	# Properties
	chi = property(getChi, setChi, delChi, "Property for chi")
	def getFidelity(self): return self.__fidelity
	def setFidelity(self, fidelity):
		checkType("XSDataResultDatcmp", "setFidelity", fidelity, "XSDataDouble")
		self.__fidelity = fidelity
	def delFidelity(self): self.__fidelity = None
	# Properties
	fidelity = property(getFidelity, setFidelity, delFidelity, "Property for fidelity")
	def export(self, outfile, level, name_='XSDataResultDatcmp'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDatcmp'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__chi is not None:
			self.chi.export(outfile, level, name_='chi')
		else:
			warnEmptyAttribute("chi", "XSDataDouble")
		if self.__fidelity is not None:
			self.fidelity.export(outfile, level, name_='fidelity')
		else:
			warnEmptyAttribute("fidelity", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chi':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setChi(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFidelity(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultDatcmp" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultDatcmp' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARING: Method outputFile in class XSDataResultDatcmp is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultDatcmp.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatcmp()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultDatcmp" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatcmp()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultDatcmp



# End of data representation classes.



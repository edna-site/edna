#!/usr/bin/env python

#
# Generated Sun Mar 31 03:10::29 2013 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSDataArray
	from XSDataCommon import XSDataDouble
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


class XSDataEnergyCalibration(object):
	def __init__(self, d=None, c=None, b=None, a=None):
	
	
		checkType("XSDataEnergyCalibration", "Constructor of XSDataEnergyCalibration", a, "XSDataDouble")
		self._a = a
		checkType("XSDataEnergyCalibration", "Constructor of XSDataEnergyCalibration", b, "XSDataDouble")
		self._b = b
		checkType("XSDataEnergyCalibration", "Constructor of XSDataEnergyCalibration", c, "XSDataDouble")
		self._c = c
		checkType("XSDataEnergyCalibration", "Constructor of XSDataEnergyCalibration", d, "XSDataDouble")
		self._d = d
	def getA(self): return self._a
	def setA(self, a):
		checkType("XSDataEnergyCalibration", "setA", a, "XSDataDouble")
		self._a = a
	def delA(self): self._a = None
	# Properties
	a = property(getA, setA, delA, "Property for a")
	def getB(self): return self._b
	def setB(self, b):
		checkType("XSDataEnergyCalibration", "setB", b, "XSDataDouble")
		self._b = b
	def delB(self): self._b = None
	# Properties
	b = property(getB, setB, delB, "Property for b")
	def getC(self): return self._c
	def setC(self, c):
		checkType("XSDataEnergyCalibration", "setC", c, "XSDataDouble")
		self._c = c
	def delC(self): self._c = None
	# Properties
	c = property(getC, setC, delC, "Property for c")
	def getD(self): return self._d
	def setD(self, d):
		checkType("XSDataEnergyCalibration", "setD", d, "XSDataDouble")
		self._d = d
	def delD(self): self._d = None
	# Properties
	d = property(getD, setD, delD, "Property for d")
	def export(self, outfile, level, name_='XSDataEnergyCalibration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataEnergyCalibration'):
		pass
		if self._a is not None:
			self.a.export(outfile, level, name_='a')
		else:
			warnEmptyAttribute("a", "XSDataDouble")
		if self._b is not None:
			self.b.export(outfile, level, name_='b')
		else:
			warnEmptyAttribute("b", "XSDataDouble")
		if self._c is not None:
			self.c.export(outfile, level, name_='c')
		if self._d is not None:
			self.d.export(outfile, level, name_='d')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'a':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'b':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setB(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'c':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setC(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'd':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setD(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataEnergyCalibration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataEnergyCalibration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataEnergyCalibration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataEnergyCalibration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataEnergyCalibration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataEnergyCalibration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataEnergyCalibration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataEnergyCalibration

class XSDataInputReadDataID24(XSDataInput):
	def __init__(self, configuration=None, energyCalibration=None, inputFile=None):
		XSDataInput.__init__(self, configuration)
	
	
		if inputFile is None:
			self._inputFile = []
		else:
			checkType("XSDataInputReadDataID24", "Constructor of XSDataInputReadDataID24", inputFile, "list")
			self._inputFile = inputFile
		checkType("XSDataInputReadDataID24", "Constructor of XSDataInputReadDataID24", energyCalibration, "XSDataEnergyCalibration")
		self._energyCalibration = energyCalibration
	def getInputFile(self): return self._inputFile
	def setInputFile(self, inputFile):
		checkType("XSDataInputReadDataID24", "setInputFile", inputFile, "list")
		self._inputFile = inputFile
	def delInputFile(self): self._inputFile = None
	# Properties
	inputFile = property(getInputFile, setInputFile, delInputFile, "Property for inputFile")
	def addInputFile(self, value):
		checkType("XSDataInputReadDataID24", "setInputFile", value, "XSDataFile")
		self._inputFile.append(value)
	def insertInputFile(self, index, value):
		checkType("XSDataInputReadDataID24", "setInputFile", value, "XSDataFile")
		self._inputFile[index] = value
	def getEnergyCalibration(self): return self._energyCalibration
	def setEnergyCalibration(self, energyCalibration):
		checkType("XSDataInputReadDataID24", "setEnergyCalibration", energyCalibration, "XSDataEnergyCalibration")
		self._energyCalibration = energyCalibration
	def delEnergyCalibration(self): self._energyCalibration = None
	# Properties
	energyCalibration = property(getEnergyCalibration, setEnergyCalibration, delEnergyCalibration, "Property for energyCalibration")
	def export(self, outfile, level, name_='XSDataInputReadDataID24'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputReadDataID24'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputFile_ in self.getInputFile():
			inputFile_.export(outfile, level, name_='inputFile')
		if self.getInputFile() == []:
			warnEmptyAttribute("inputFile", "XSDataFile")
		if self._energyCalibration is not None:
			self.energyCalibration.export(outfile, level, name_='energyCalibration')
		else:
			warnEmptyAttribute("energyCalibration", "XSDataEnergyCalibration")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'energyCalibration':
			obj_ = XSDataEnergyCalibration()
			obj_.build(child_)
			self.setEnergyCalibration(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputReadDataID24" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputReadDataID24' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputReadDataID24 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputReadDataID24.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadDataID24()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputReadDataID24" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadDataID24()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputReadDataID24

class XSDataResultReadDataID24(XSDataResult):
	def __init__(self, status=None, dataArray=None, energy=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultReadDataID24", "Constructor of XSDataResultReadDataID24", energy, "XSDataArray")
		self._energy = energy
		checkType("XSDataResultReadDataID24", "Constructor of XSDataResultReadDataID24", dataArray, "XSDataArray")
		self._dataArray = dataArray
	def getEnergy(self): return self._energy
	def setEnergy(self, energy):
		checkType("XSDataResultReadDataID24", "setEnergy", energy, "XSDataArray")
		self._energy = energy
	def delEnergy(self): self._energy = None
	# Properties
	energy = property(getEnergy, setEnergy, delEnergy, "Property for energy")
	def getDataArray(self): return self._dataArray
	def setDataArray(self, dataArray):
		checkType("XSDataResultReadDataID24", "setDataArray", dataArray, "XSDataArray")
		self._dataArray = dataArray
	def delDataArray(self): self._dataArray = None
	# Properties
	dataArray = property(getDataArray, setDataArray, delDataArray, "Property for dataArray")
	def export(self, outfile, level, name_='XSDataResultReadDataID24'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultReadDataID24'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._energy is not None:
			self.energy.export(outfile, level, name_='energy')
		if self._dataArray is not None:
			self.dataArray.export(outfile, level, name_='dataArray')
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
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultReadDataID24" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultReadDataID24' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultReadDataID24 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultReadDataID24.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadDataID24()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultReadDataID24" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadDataID24()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultReadDataID24



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Sat Apr 28 05:40::11 2012 by EDGenerateDS.
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
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataAngle
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataMatrixDouble
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataSize
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataVectorDouble
	from XSDataCommon import XSDataImage
	from XSDataCommon import XSDataAbsorbedDoseRate
	from XSDataCommon import XSDataAngularSpeed
	from XSDataCommon import XSDataFlux
	from XSDataCommon import XSDataLength
	from XSDataCommon import XSDataTime
	from XSDataCommon import XSDataWavelength
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
from XSDataCommon import XSData
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataAbsorbedDoseRate
from XSDataCommon import XSDataAngularSpeed
from XSDataCommon import XSDataFlux
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength




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


class XSDataStatisticsIntegrationAverageAndNumberOfReflections(object):
	def __init__(self, numberOfReflections=None, averageSigma=None, averageIntensity=None, averageIOverSigma=None):
	
	
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "Constructor of XSDataStatisticsIntegrationAverageAndNumberOfReflections", averageIOverSigma, "XSDataDouble")
		self._averageIOverSigma = averageIOverSigma
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "Constructor of XSDataStatisticsIntegrationAverageAndNumberOfReflections", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "Constructor of XSDataStatisticsIntegrationAverageAndNumberOfReflections", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "Constructor of XSDataStatisticsIntegrationAverageAndNumberOfReflections", numberOfReflections, "XSDataInteger")
		self._numberOfReflections = numberOfReflections
	def getAverageIOverSigma(self): return self._averageIOverSigma
	def setAverageIOverSigma(self, averageIOverSigma):
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "setAverageIOverSigma", averageIOverSigma, "XSDataDouble")
		self._averageIOverSigma = averageIOverSigma
	def delAverageIOverSigma(self): self._averageIOverSigma = None
	# Properties
	averageIOverSigma = property(getAverageIOverSigma, setAverageIOverSigma, delAverageIOverSigma, "Property for averageIOverSigma")
	def getAverageIntensity(self): return self._averageIntensity
	def setAverageIntensity(self, averageIntensity):
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "setAverageIntensity", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
	def delAverageIntensity(self): self._averageIntensity = None
	# Properties
	averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
	def getAverageSigma(self): return self._averageSigma
	def setAverageSigma(self, averageSigma):
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "setAverageSigma", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
	def delAverageSigma(self): self._averageSigma = None
	# Properties
	averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
	def getNumberOfReflections(self): return self._numberOfReflections
	def setNumberOfReflections(self, numberOfReflections):
		checkType("XSDataStatisticsIntegrationAverageAndNumberOfReflections", "setNumberOfReflections", numberOfReflections, "XSDataInteger")
		self._numberOfReflections = numberOfReflections
	def delNumberOfReflections(self): self._numberOfReflections = None
	# Properties
	numberOfReflections = property(getNumberOfReflections, setNumberOfReflections, delNumberOfReflections, "Property for numberOfReflections")
	def export(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
		pass
		if self._averageIOverSigma is not None:
			self.averageIOverSigma.export(outfile, level, name_='averageIOverSigma')
		else:
			warnEmptyAttribute("averageIOverSigma", "XSDataDouble")
		if self._averageIntensity is not None:
			self.averageIntensity.export(outfile, level, name_='averageIntensity')
		else:
			warnEmptyAttribute("averageIntensity", "XSDataDouble")
		if self._averageSigma is not None:
			self.averageSigma.export(outfile, level, name_='averageSigma')
		else:
			warnEmptyAttribute("averageSigma", "XSDataDouble")
		if self._numberOfReflections is not None:
			self.numberOfReflections.export(outfile, level, name_='numberOfReflections')
		else:
			warnEmptyAttribute("numberOfReflections", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIOverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIntensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfReflections(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationAverageAndNumberOfReflections" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsIntegrationAverageAndNumberOfReflections is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsIntegrationAverageAndNumberOfReflections.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationAverageAndNumberOfReflections()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsIntegrationAverageAndNumberOfReflections" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationAverageAndNumberOfReflections()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsIntegrationAverageAndNumberOfReflections

class XSDataAtom(XSData):
	"""This object describes a single atom content (of type 'symbol' i.e 'S') that could be either expressed in concentration if dilute in a solvent (mM) or in number in a structure"""
	def __init__(self, symbol=None, numberOf=None, concentration=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataAtom", "Constructor of XSDataAtom", concentration, "XSDataDouble")
		self._concentration = concentration
		checkType("XSDataAtom", "Constructor of XSDataAtom", numberOf, "XSDataDouble")
		self._numberOf = numberOf
		checkType("XSDataAtom", "Constructor of XSDataAtom", symbol, "XSDataString")
		self._symbol = symbol
	def getConcentration(self): return self._concentration
	def setConcentration(self, concentration):
		checkType("XSDataAtom", "setConcentration", concentration, "XSDataDouble")
		self._concentration = concentration
	def delConcentration(self): self._concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def getNumberOf(self): return self._numberOf
	def setNumberOf(self, numberOf):
		checkType("XSDataAtom", "setNumberOf", numberOf, "XSDataDouble")
		self._numberOf = numberOf
	def delNumberOf(self): self._numberOf = None
	# Properties
	numberOf = property(getNumberOf, setNumberOf, delNumberOf, "Property for numberOf")
	def getSymbol(self): return self._symbol
	def setSymbol(self, symbol):
		checkType("XSDataAtom", "setSymbol", symbol, "XSDataString")
		self._symbol = symbol
	def delSymbol(self): self._symbol = None
	# Properties
	symbol = property(getSymbol, setSymbol, delSymbol, "Property for symbol")
	def export(self, outfile, level, name_='XSDataAtom'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataAtom'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
		if self._numberOf is not None:
			self.numberOf.export(outfile, level, name_='numberOf')
		if self._symbol is not None:
			self.symbol.export(outfile, level, name_='symbol')
		else:
			warnEmptyAttribute("symbol", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'concentration':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOf':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOf(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symbol':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymbol(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataAtom" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataAtom' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataAtom is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataAtom.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataAtom()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataAtom" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataAtom()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataAtom

class XSDataAtomicComposition(XSData):
	def __init__(self, atom=None):
		XSData.__init__(self, )
	
	
		if atom is None:
			self._atom = []
		else:
			checkType("XSDataAtomicComposition", "Constructor of XSDataAtomicComposition", atom, "list")
			self._atom = atom
	def getAtom(self): return self._atom
	def setAtom(self, atom):
		checkType("XSDataAtomicComposition", "setAtom", atom, "list")
		self._atom = atom
	def delAtom(self): self._atom = None
	# Properties
	atom = property(getAtom, setAtom, delAtom, "Property for atom")
	def addAtom(self, value):
		checkType("XSDataAtomicComposition", "setAtom", value, "XSDataAtom")
		self._atom.append(value)
	def insertAtom(self, index, value):
		checkType("XSDataAtomicComposition", "setAtom", value, "XSDataAtom")
		self._atom[index] = value
	def export(self, outfile, level, name_='XSDataAtomicComposition'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataAtomicComposition'):
		XSData.exportChildren(self, outfile, level, name_)
		for atom_ in self.getAtom():
			atom_.export(outfile, level, name_='atom')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'atom':
			obj_ = XSDataAtom()
			obj_.build(child_)
			self.atom.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataAtomicComposition" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataAtomicComposition' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataAtomicComposition is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataAtomicComposition.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataAtomicComposition()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataAtomicComposition" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataAtomicComposition()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataAtomicComposition

class XSDataBeam(XSData):
	"""This object contains all the properties related to the beam:
- the exposure time (sec)
- the flux (photons/sec)
- The minimum exposure time permitted by hardware (sec)
- The size of the beam (mm x mm)
- The wavelength (a)
- Transmission in %"""
	def __init__(self, wavelength=None, transmission=None, size=None, minExposureTimePerImage=None, flux=None, exposureTime=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataBeam", "Constructor of XSDataBeam", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
		checkType("XSDataBeam", "Constructor of XSDataBeam", flux, "XSDataFlux")
		self._flux = flux
		checkType("XSDataBeam", "Constructor of XSDataBeam", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
		checkType("XSDataBeam", "Constructor of XSDataBeam", size, "XSDataSize")
		self._size = size
		checkType("XSDataBeam", "Constructor of XSDataBeam", transmission, "XSDataDouble")
		self._transmission = transmission
		checkType("XSDataBeam", "Constructor of XSDataBeam", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataBeam", "setExposureTime", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getFlux(self): return self._flux
	def setFlux(self, flux):
		checkType("XSDataBeam", "setFlux", flux, "XSDataFlux")
		self._flux = flux
	def delFlux(self): self._flux = None
	# Properties
	flux = property(getFlux, setFlux, delFlux, "Property for flux")
	def getMinExposureTimePerImage(self): return self._minExposureTimePerImage
	def setMinExposureTimePerImage(self, minExposureTimePerImage):
		checkType("XSDataBeam", "setMinExposureTimePerImage", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
	def delMinExposureTimePerImage(self): self._minExposureTimePerImage = None
	# Properties
	minExposureTimePerImage = property(getMinExposureTimePerImage, setMinExposureTimePerImage, delMinExposureTimePerImage, "Property for minExposureTimePerImage")
	def getSize(self): return self._size
	def setSize(self, size):
		checkType("XSDataBeam", "setSize", size, "XSDataSize")
		self._size = size
	def delSize(self): self._size = None
	# Properties
	size = property(getSize, setSize, delSize, "Property for size")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataBeam", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getWavelength(self): return self._wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataBeam", "setWavelength", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
	def delWavelength(self): self._wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def export(self, outfile, level, name_='XSDataBeam'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBeam'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self._flux is not None:
			self.flux.export(outfile, level, name_='flux')
		if self._minExposureTimePerImage is not None:
			self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
		if self._size is not None:
			self.size.export(outfile, level, name_='size')
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self._wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flux':
			obj_ = XSDataFlux()
			obj_.build(child_)
			self.setFlux(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minExposureTimePerImage':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setMinExposureTimePerImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'size':
			obj_ = XSDataSize()
			obj_.build(child_)
			self.setSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBeam" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBeam' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBeam is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBeam.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBeam()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBeam" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBeam()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBeam

class XSDataCell(XSData):
	"""Crystallographic properties"""
	def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataCell", "Constructor of XSDataCell", angle_alpha, "XSDataAngle")
		self._angle_alpha = angle_alpha
		checkType("XSDataCell", "Constructor of XSDataCell", angle_beta, "XSDataAngle")
		self._angle_beta = angle_beta
		checkType("XSDataCell", "Constructor of XSDataCell", angle_gamma, "XSDataAngle")
		self._angle_gamma = angle_gamma
		checkType("XSDataCell", "Constructor of XSDataCell", length_a, "XSDataLength")
		self._length_a = length_a
		checkType("XSDataCell", "Constructor of XSDataCell", length_b, "XSDataLength")
		self._length_b = length_b
		checkType("XSDataCell", "Constructor of XSDataCell", length_c, "XSDataLength")
		self._length_c = length_c
	def getAngle_alpha(self): return self._angle_alpha
	def setAngle_alpha(self, angle_alpha):
		checkType("XSDataCell", "setAngle_alpha", angle_alpha, "XSDataAngle")
		self._angle_alpha = angle_alpha
	def delAngle_alpha(self): self._angle_alpha = None
	# Properties
	angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
	def getAngle_beta(self): return self._angle_beta
	def setAngle_beta(self, angle_beta):
		checkType("XSDataCell", "setAngle_beta", angle_beta, "XSDataAngle")
		self._angle_beta = angle_beta
	def delAngle_beta(self): self._angle_beta = None
	# Properties
	angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
	def getAngle_gamma(self): return self._angle_gamma
	def setAngle_gamma(self, angle_gamma):
		checkType("XSDataCell", "setAngle_gamma", angle_gamma, "XSDataAngle")
		self._angle_gamma = angle_gamma
	def delAngle_gamma(self): self._angle_gamma = None
	# Properties
	angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
	def getLength_a(self): return self._length_a
	def setLength_a(self, length_a):
		checkType("XSDataCell", "setLength_a", length_a, "XSDataLength")
		self._length_a = length_a
	def delLength_a(self): self._length_a = None
	# Properties
	length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
	def getLength_b(self): return self._length_b
	def setLength_b(self, length_b):
		checkType("XSDataCell", "setLength_b", length_b, "XSDataLength")
		self._length_b = length_b
	def delLength_b(self): self._length_b = None
	# Properties
	length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
	def getLength_c(self): return self._length_c
	def setLength_c(self, length_c):
		checkType("XSDataCell", "setLength_c", length_c, "XSDataLength")
		self._length_c = length_c
	def delLength_c(self): self._length_c = None
	# Properties
	length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
	def export(self, outfile, level, name_='XSDataCell'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCell'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._angle_alpha is not None:
			self.angle_alpha.export(outfile, level, name_='angle_alpha')
		else:
			warnEmptyAttribute("angle_alpha", "XSDataAngle")
		if self._angle_beta is not None:
			self.angle_beta.export(outfile, level, name_='angle_beta')
		else:
			warnEmptyAttribute("angle_beta", "XSDataAngle")
		if self._angle_gamma is not None:
			self.angle_gamma.export(outfile, level, name_='angle_gamma')
		else:
			warnEmptyAttribute("angle_gamma", "XSDataAngle")
		if self._length_a is not None:
			self.length_a.export(outfile, level, name_='length_a')
		else:
			warnEmptyAttribute("length_a", "XSDataLength")
		if self._length_b is not None:
			self.length_b.export(outfile, level, name_='length_b')
		else:
			warnEmptyAttribute("length_b", "XSDataLength")
		if self._length_c is not None:
			self.length_c.export(outfile, level, name_='length_c')
		else:
			warnEmptyAttribute("length_c", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_alpha':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_alpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_beta':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_beta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_gamma':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_gamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_a':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_a(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_b':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_b(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_c':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_c(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCell" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCell' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCell is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCell.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCell()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCell" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCell()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCell

class XSDataChain(XSData):
	"""A polymer chain of type 'protein', 'dna' or 'rna' that contains monomers (which number is defined by numberOfMonomers) and a list of heavy atoms. The number of this is particular chain in the whole polymer is defined by numberOfCopies."""
	def __init__(self, type=None, numberOfMonomers=None, numberOfCopies=None, heavyAtoms=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataChain", "Constructor of XSDataChain", heavyAtoms, "XSDataAtomicComposition")
		self._heavyAtoms = heavyAtoms
		checkType("XSDataChain", "Constructor of XSDataChain", numberOfCopies, "XSDataDouble")
		self._numberOfCopies = numberOfCopies
		checkType("XSDataChain", "Constructor of XSDataChain", numberOfMonomers, "XSDataDouble")
		self._numberOfMonomers = numberOfMonomers
		checkType("XSDataChain", "Constructor of XSDataChain", type, "XSDataString")
		self._type = type
	def getHeavyAtoms(self): return self._heavyAtoms
	def setHeavyAtoms(self, heavyAtoms):
		checkType("XSDataChain", "setHeavyAtoms", heavyAtoms, "XSDataAtomicComposition")
		self._heavyAtoms = heavyAtoms
	def delHeavyAtoms(self): self._heavyAtoms = None
	# Properties
	heavyAtoms = property(getHeavyAtoms, setHeavyAtoms, delHeavyAtoms, "Property for heavyAtoms")
	def getNumberOfCopies(self): return self._numberOfCopies
	def setNumberOfCopies(self, numberOfCopies):
		checkType("XSDataChain", "setNumberOfCopies", numberOfCopies, "XSDataDouble")
		self._numberOfCopies = numberOfCopies
	def delNumberOfCopies(self): self._numberOfCopies = None
	# Properties
	numberOfCopies = property(getNumberOfCopies, setNumberOfCopies, delNumberOfCopies, "Property for numberOfCopies")
	def getNumberOfMonomers(self): return self._numberOfMonomers
	def setNumberOfMonomers(self, numberOfMonomers):
		checkType("XSDataChain", "setNumberOfMonomers", numberOfMonomers, "XSDataDouble")
		self._numberOfMonomers = numberOfMonomers
	def delNumberOfMonomers(self): self._numberOfMonomers = None
	# Properties
	numberOfMonomers = property(getNumberOfMonomers, setNumberOfMonomers, delNumberOfMonomers, "Property for numberOfMonomers")
	def getType(self): return self._type
	def setType(self, type):
		checkType("XSDataChain", "setType", type, "XSDataString")
		self._type = type
	def delType(self): self._type = None
	# Properties
	type = property(getType, setType, delType, "Property for type")
	def export(self, outfile, level, name_='XSDataChain'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataChain'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._heavyAtoms is not None:
			self.heavyAtoms.export(outfile, level, name_='heavyAtoms')
		else:
			warnEmptyAttribute("heavyAtoms", "XSDataAtomicComposition")
		if self._numberOfCopies is not None:
			self.numberOfCopies.export(outfile, level, name_='numberOfCopies')
		else:
			warnEmptyAttribute("numberOfCopies", "XSDataDouble")
		if self._numberOfMonomers is not None:
			self.numberOfMonomers.export(outfile, level, name_='numberOfMonomers')
		else:
			warnEmptyAttribute("numberOfMonomers", "XSDataDouble")
		if self._type is not None:
			self.type.export(outfile, level, name_='type')
		else:
			warnEmptyAttribute("type", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'heavyAtoms':
			obj_ = XSDataAtomicComposition()
			obj_.build(child_)
			self.setHeavyAtoms(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfCopies':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOfCopies(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfMonomers':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOfMonomers(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'type':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setType(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataChain" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataChain' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataChain is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataChain.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataChain()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataChain" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataChain()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataChain

class XSDataChemicalCompositionMM(XSData):
	"""This is the composition of a crystal sample of a Macro Molecule (MM stand for Macro Molecule)"""
	def __init__(self, structure=None, solvent=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataChemicalCompositionMM", "Constructor of XSDataChemicalCompositionMM", solvent, "XSDataSolvent")
		self._solvent = solvent
		checkType("XSDataChemicalCompositionMM", "Constructor of XSDataChemicalCompositionMM", structure, "XSDataStructure")
		self._structure = structure
	def getSolvent(self): return self._solvent
	def setSolvent(self, solvent):
		checkType("XSDataChemicalCompositionMM", "setSolvent", solvent, "XSDataSolvent")
		self._solvent = solvent
	def delSolvent(self): self._solvent = None
	# Properties
	solvent = property(getSolvent, setSolvent, delSolvent, "Property for solvent")
	def getStructure(self): return self._structure
	def setStructure(self, structure):
		checkType("XSDataChemicalCompositionMM", "setStructure", structure, "XSDataStructure")
		self._structure = structure
	def delStructure(self): self._structure = None
	# Properties
	structure = property(getStructure, setStructure, delStructure, "Property for structure")
	def export(self, outfile, level, name_='XSDataChemicalCompositionMM'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataChemicalCompositionMM'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._solvent is not None:
			self.solvent.export(outfile, level, name_='solvent')
		else:
			warnEmptyAttribute("solvent", "XSDataSolvent")
		if self._structure is not None:
			self.structure.export(outfile, level, name_='structure')
		else:
			warnEmptyAttribute("structure", "XSDataStructure")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'solvent':
			obj_ = XSDataSolvent()
			obj_.build(child_)
			self.setSolvent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'structure':
			obj_ = XSDataStructure()
			obj_.build(child_)
			self.setStructure(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataChemicalCompositionMM" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataChemicalCompositionMM' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataChemicalCompositionMM is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataChemicalCompositionMM.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataChemicalCompositionMM()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataChemicalCompositionMM" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataChemicalCompositionMM()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataChemicalCompositionMM

class XSDataCollection(XSData):
	"""The data collection carried out or to be carried out with a particular sample with specific user inputs defined by the diffraction plan."""
	def __init__(self, subWedge=None, sample=None, diffractionPlan=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataCollection", "Constructor of XSDataCollection", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
		checkType("XSDataCollection", "Constructor of XSDataCollection", sample, "XSDataSampleCrystalMM")
		self._sample = sample
		if subWedge is None:
			self._subWedge = []
		else:
			checkType("XSDataCollection", "Constructor of XSDataCollection", subWedge, "list")
			self._subWedge = subWedge
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataCollection", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getSample(self): return self._sample
	def setSample(self, sample):
		checkType("XSDataCollection", "setSample", sample, "XSDataSampleCrystalMM")
		self._sample = sample
	def delSample(self): self._sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getSubWedge(self): return self._subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataCollection", "setSubWedge", subWedge, "list")
		self._subWedge = subWedge
	def delSubWedge(self): self._subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def addSubWedge(self, value):
		checkType("XSDataCollection", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge.append(value)
	def insertSubWedge(self, index, value):
		checkType("XSDataCollection", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge[index] = value
	def export(self, outfile, level, name_='XSDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCollection'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		if self._sample is not None:
			self.sample.export(outfile, level, name_='sample')
		for subWedge_ in self.getSubWedge():
			subWedge_.export(outfile, level, name_='subWedge')
		if self.getSubWedge() == []:
			warnEmptyAttribute("subWedge", "XSDataSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSampleCrystalMM()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataSubWedge()
			obj_.build(child_)
			self.subWedge.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCollection

class XSDataCharacterisation(XSData):
	"""Deprecated - only used by EDPluginControlCharacterisationv10
"""
	def __init__(self, strategyResult=None, integrationResult=None, indexingResult=None, dataCollection=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataCharacterisation", "Constructor of XSDataCharacterisation", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
		checkType("XSDataCharacterisation", "Constructor of XSDataCharacterisation", indexingResult, "XSDataIndexingResult")
		self._indexingResult = indexingResult
		checkType("XSDataCharacterisation", "Constructor of XSDataCharacterisation", integrationResult, "XSDataIntegrationResult")
		self._integrationResult = integrationResult
		checkType("XSDataCharacterisation", "Constructor of XSDataCharacterisation", strategyResult, "XSDataStrategyResult")
		self._strategyResult = strategyResult
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataCharacterisation", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def getIndexingResult(self): return self._indexingResult
	def setIndexingResult(self, indexingResult):
		checkType("XSDataCharacterisation", "setIndexingResult", indexingResult, "XSDataIndexingResult")
		self._indexingResult = indexingResult
	def delIndexingResult(self): self._indexingResult = None
	# Properties
	indexingResult = property(getIndexingResult, setIndexingResult, delIndexingResult, "Property for indexingResult")
	def getIntegrationResult(self): return self._integrationResult
	def setIntegrationResult(self, integrationResult):
		checkType("XSDataCharacterisation", "setIntegrationResult", integrationResult, "XSDataIntegrationResult")
		self._integrationResult = integrationResult
	def delIntegrationResult(self): self._integrationResult = None
	# Properties
	integrationResult = property(getIntegrationResult, setIntegrationResult, delIntegrationResult, "Property for integrationResult")
	def getStrategyResult(self): return self._strategyResult
	def setStrategyResult(self, strategyResult):
		checkType("XSDataCharacterisation", "setStrategyResult", strategyResult, "XSDataStrategyResult")
		self._strategyResult = strategyResult
	def delStrategyResult(self): self._strategyResult = None
	# Properties
	strategyResult = property(getStrategyResult, setStrategyResult, delStrategyResult, "Property for strategyResult")
	def export(self, outfile, level, name_='XSDataCharacterisation'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCharacterisation'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
		if self._indexingResult is not None:
			self.indexingResult.export(outfile, level, name_='indexingResult')
		if self._integrationResult is not None:
			self.integrationResult.export(outfile, level, name_='integrationResult')
		if self._strategyResult is not None:
			self.strategyResult.export(outfile, level, name_='strategyResult')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'indexingResult':
			obj_ = XSDataIndexingResult()
			obj_.build(child_)
			self.setIndexingResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integrationResult':
			obj_ = XSDataIntegrationResult()
			obj_.build(child_)
			self.setIntegrationResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategyResult':
			obj_ = XSDataStrategyResult()
			obj_.build(child_)
			self.setStrategyResult(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCharacterisation" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCharacterisation' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCharacterisation is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCharacterisation.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCharacterisation()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCharacterisation" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCharacterisation()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCharacterisation

class XSDataCollectionPlan(XSData):
	"""The comment can be used for describing exotic data collections, for example without collecting any images."""
	def __init__(self, strategySummary=None, statistics=None, comment=None, collectionStrategy=None, collectionPlanNumber=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataCollectionPlan", "Constructor of XSDataCollectionPlan", collectionPlanNumber, "XSDataInteger")
		self._collectionPlanNumber = collectionPlanNumber
		checkType("XSDataCollectionPlan", "Constructor of XSDataCollectionPlan", collectionStrategy, "XSDataCollection")
		self._collectionStrategy = collectionStrategy
		checkType("XSDataCollectionPlan", "Constructor of XSDataCollectionPlan", comment, "XSDataString")
		self._comment = comment
		checkType("XSDataCollectionPlan", "Constructor of XSDataCollectionPlan", statistics, "XSDataStatisticsStrategy")
		self._statistics = statistics
		checkType("XSDataCollectionPlan", "Constructor of XSDataCollectionPlan", strategySummary, "XSDataStrategySummary")
		self._strategySummary = strategySummary
	def getCollectionPlanNumber(self): return self._collectionPlanNumber
	def setCollectionPlanNumber(self, collectionPlanNumber):
		checkType("XSDataCollectionPlan", "setCollectionPlanNumber", collectionPlanNumber, "XSDataInteger")
		self._collectionPlanNumber = collectionPlanNumber
	def delCollectionPlanNumber(self): self._collectionPlanNumber = None
	# Properties
	collectionPlanNumber = property(getCollectionPlanNumber, setCollectionPlanNumber, delCollectionPlanNumber, "Property for collectionPlanNumber")
	def getCollectionStrategy(self): return self._collectionStrategy
	def setCollectionStrategy(self, collectionStrategy):
		checkType("XSDataCollectionPlan", "setCollectionStrategy", collectionStrategy, "XSDataCollection")
		self._collectionStrategy = collectionStrategy
	def delCollectionStrategy(self): self._collectionStrategy = None
	# Properties
	collectionStrategy = property(getCollectionStrategy, setCollectionStrategy, delCollectionStrategy, "Property for collectionStrategy")
	def getComment(self): return self._comment
	def setComment(self, comment):
		checkType("XSDataCollectionPlan", "setComment", comment, "XSDataString")
		self._comment = comment
	def delComment(self): self._comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getStatistics(self): return self._statistics
	def setStatistics(self, statistics):
		checkType("XSDataCollectionPlan", "setStatistics", statistics, "XSDataStatisticsStrategy")
		self._statistics = statistics
	def delStatistics(self): self._statistics = None
	# Properties
	statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
	def getStrategySummary(self): return self._strategySummary
	def setStrategySummary(self, strategySummary):
		checkType("XSDataCollectionPlan", "setStrategySummary", strategySummary, "XSDataStrategySummary")
		self._strategySummary = strategySummary
	def delStrategySummary(self): self._strategySummary = None
	# Properties
	strategySummary = property(getStrategySummary, setStrategySummary, delStrategySummary, "Property for strategySummary")
	def export(self, outfile, level, name_='XSDataCollectionPlan'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCollectionPlan'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._collectionPlanNumber is not None:
			self.collectionPlanNumber.export(outfile, level, name_='collectionPlanNumber')
		else:
			warnEmptyAttribute("collectionPlanNumber", "XSDataInteger")
		if self._collectionStrategy is not None:
			self.collectionStrategy.export(outfile, level, name_='collectionStrategy')
		else:
			warnEmptyAttribute("collectionStrategy", "XSDataCollection")
		if self._comment is not None:
			self.comment.export(outfile, level, name_='comment')
		if self._statistics is not None:
			self.statistics.export(outfile, level, name_='statistics')
		else:
			warnEmptyAttribute("statistics", "XSDataStatisticsStrategy")
		if self._strategySummary is not None:
			self.strategySummary.export(outfile, level, name_='strategySummary')
		else:
			warnEmptyAttribute("strategySummary", "XSDataStrategySummary")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlanNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCollectionPlanNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionStrategy':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setCollectionStrategy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComment(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statistics':
			obj_ = XSDataStatisticsStrategy()
			obj_.build(child_)
			self.setStatistics(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategySummary':
			obj_ = XSDataStrategySummary()
			obj_.build(child_)
			self.setStrategySummary(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCollectionPlan" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCollectionPlan' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCollectionPlan is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCollectionPlan.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCollectionPlan()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCollectionPlan" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCollectionPlan()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCollectionPlan

class XSDataCrystal(XSData):
	"""Crystallographic properties"""
	def __init__(self, spaceGroup=None, mosaicity=None, cell=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataCrystal", "Constructor of XSDataCrystal", cell, "XSDataCell")
		self._cell = cell
		checkType("XSDataCrystal", "Constructor of XSDataCrystal", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
		checkType("XSDataCrystal", "Constructor of XSDataCrystal", spaceGroup, "XSDataSpaceGroup")
		self._spaceGroup = spaceGroup
	def getCell(self): return self._cell
	def setCell(self, cell):
		checkType("XSDataCrystal", "setCell", cell, "XSDataCell")
		self._cell = cell
	def delCell(self): self._cell = None
	# Properties
	cell = property(getCell, setCell, delCell, "Property for cell")
	def getMosaicity(self): return self._mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataCrystal", "setMosaicity", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
	def delMosaicity(self): self._mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getSpaceGroup(self): return self._spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("XSDataCrystal", "setSpaceGroup", spaceGroup, "XSDataSpaceGroup")
		self._spaceGroup = spaceGroup
	def delSpaceGroup(self): self._spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def export(self, outfile, level, name_='XSDataCrystal'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCrystal'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._cell is not None:
			self.cell.export(outfile, level, name_='cell')
		else:
			warnEmptyAttribute("cell", "XSDataCell")
		if self._mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self._spaceGroup is not None:
			self.spaceGroup.export(outfile, level, name_='spaceGroup')
		else:
			warnEmptyAttribute("spaceGroup", "XSDataSpaceGroup")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell':
			obj_ = XSDataCell()
			obj_.build(child_)
			self.setCell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spaceGroup':
			obj_ = XSDataSpaceGroup()
			obj_.build(child_)
			self.setSpaceGroup(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCrystal" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCrystal' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCrystal is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCrystal.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCrystal()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCrystal" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCrystal()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCrystal

class XSDataDetector(XSData):
	"""The properties of a detector. """
	def __init__(self, type=None, twoTheta=None, serialNumber=None, pixelSizeY=None, pixelSizeX=None, numberPixelY=None, numberPixelX=None, numberBytesInHeader=None, name=None, imageSaturation=None, gain=None, distance=None, dataType=None, byteOrder=None, bin=None, beamPositionY=None, beamPositionX=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataDetector", "Constructor of XSDataDetector", beamPositionX, "XSDataLength")
		self._beamPositionX = beamPositionX
		checkType("XSDataDetector", "Constructor of XSDataDetector", beamPositionY, "XSDataLength")
		self._beamPositionY = beamPositionY
		checkType("XSDataDetector", "Constructor of XSDataDetector", bin, "XSDataString")
		self._bin = bin
		checkType("XSDataDetector", "Constructor of XSDataDetector", byteOrder, "XSDataString")
		self._byteOrder = byteOrder
		checkType("XSDataDetector", "Constructor of XSDataDetector", dataType, "XSDataString")
		self._dataType = dataType
		checkType("XSDataDetector", "Constructor of XSDataDetector", distance, "XSDataLength")
		self._distance = distance
		checkType("XSDataDetector", "Constructor of XSDataDetector", gain, "XSDataFloat")
		self._gain = gain
		checkType("XSDataDetector", "Constructor of XSDataDetector", imageSaturation, "XSDataInteger")
		self._imageSaturation = imageSaturation
		checkType("XSDataDetector", "Constructor of XSDataDetector", name, "XSDataString")
		self._name = name
		checkType("XSDataDetector", "Constructor of XSDataDetector", numberBytesInHeader, "XSDataInteger")
		self._numberBytesInHeader = numberBytesInHeader
		checkType("XSDataDetector", "Constructor of XSDataDetector", numberPixelX, "XSDataInteger")
		self._numberPixelX = numberPixelX
		checkType("XSDataDetector", "Constructor of XSDataDetector", numberPixelY, "XSDataInteger")
		self._numberPixelY = numberPixelY
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeX, "XSDataLength")
		self._pixelSizeX = pixelSizeX
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeY, "XSDataLength")
		self._pixelSizeY = pixelSizeY
		checkType("XSDataDetector", "Constructor of XSDataDetector", serialNumber, "XSDataString")
		self._serialNumber = serialNumber
		checkType("XSDataDetector", "Constructor of XSDataDetector", twoTheta, "XSDataAngle")
		self._twoTheta = twoTheta
		checkType("XSDataDetector", "Constructor of XSDataDetector", type, "XSDataString")
		self._type = type
	def getBeamPositionX(self): return self._beamPositionX
	def setBeamPositionX(self, beamPositionX):
		checkType("XSDataDetector", "setBeamPositionX", beamPositionX, "XSDataLength")
		self._beamPositionX = beamPositionX
	def delBeamPositionX(self): self._beamPositionX = None
	# Properties
	beamPositionX = property(getBeamPositionX, setBeamPositionX, delBeamPositionX, "Property for beamPositionX")
	def getBeamPositionY(self): return self._beamPositionY
	def setBeamPositionY(self, beamPositionY):
		checkType("XSDataDetector", "setBeamPositionY", beamPositionY, "XSDataLength")
		self._beamPositionY = beamPositionY
	def delBeamPositionY(self): self._beamPositionY = None
	# Properties
	beamPositionY = property(getBeamPositionY, setBeamPositionY, delBeamPositionY, "Property for beamPositionY")
	def getBin(self): return self._bin
	def setBin(self, bin):
		checkType("XSDataDetector", "setBin", bin, "XSDataString")
		self._bin = bin
	def delBin(self): self._bin = None
	# Properties
	bin = property(getBin, setBin, delBin, "Property for bin")
	def getByteOrder(self): return self._byteOrder
	def setByteOrder(self, byteOrder):
		checkType("XSDataDetector", "setByteOrder", byteOrder, "XSDataString")
		self._byteOrder = byteOrder
	def delByteOrder(self): self._byteOrder = None
	# Properties
	byteOrder = property(getByteOrder, setByteOrder, delByteOrder, "Property for byteOrder")
	def getDataType(self): return self._dataType
	def setDataType(self, dataType):
		checkType("XSDataDetector", "setDataType", dataType, "XSDataString")
		self._dataType = dataType
	def delDataType(self): self._dataType = None
	# Properties
	dataType = property(getDataType, setDataType, delDataType, "Property for dataType")
	def getDistance(self): return self._distance
	def setDistance(self, distance):
		checkType("XSDataDetector", "setDistance", distance, "XSDataLength")
		self._distance = distance
	def delDistance(self): self._distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def getGain(self): return self._gain
	def setGain(self, gain):
		checkType("XSDataDetector", "setGain", gain, "XSDataFloat")
		self._gain = gain
	def delGain(self): self._gain = None
	# Properties
	gain = property(getGain, setGain, delGain, "Property for gain")
	def getImageSaturation(self): return self._imageSaturation
	def setImageSaturation(self, imageSaturation):
		checkType("XSDataDetector", "setImageSaturation", imageSaturation, "XSDataInteger")
		self._imageSaturation = imageSaturation
	def delImageSaturation(self): self._imageSaturation = None
	# Properties
	imageSaturation = property(getImageSaturation, setImageSaturation, delImageSaturation, "Property for imageSaturation")
	def getName(self): return self._name
	def setName(self, name):
		checkType("XSDataDetector", "setName", name, "XSDataString")
		self._name = name
	def delName(self): self._name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getNumberBytesInHeader(self): return self._numberBytesInHeader
	def setNumberBytesInHeader(self, numberBytesInHeader):
		checkType("XSDataDetector", "setNumberBytesInHeader", numberBytesInHeader, "XSDataInteger")
		self._numberBytesInHeader = numberBytesInHeader
	def delNumberBytesInHeader(self): self._numberBytesInHeader = None
	# Properties
	numberBytesInHeader = property(getNumberBytesInHeader, setNumberBytesInHeader, delNumberBytesInHeader, "Property for numberBytesInHeader")
	def getNumberPixelX(self): return self._numberPixelX
	def setNumberPixelX(self, numberPixelX):
		checkType("XSDataDetector", "setNumberPixelX", numberPixelX, "XSDataInteger")
		self._numberPixelX = numberPixelX
	def delNumberPixelX(self): self._numberPixelX = None
	# Properties
	numberPixelX = property(getNumberPixelX, setNumberPixelX, delNumberPixelX, "Property for numberPixelX")
	def getNumberPixelY(self): return self._numberPixelY
	def setNumberPixelY(self, numberPixelY):
		checkType("XSDataDetector", "setNumberPixelY", numberPixelY, "XSDataInteger")
		self._numberPixelY = numberPixelY
	def delNumberPixelY(self): self._numberPixelY = None
	# Properties
	numberPixelY = property(getNumberPixelY, setNumberPixelY, delNumberPixelY, "Property for numberPixelY")
	def getPixelSizeX(self): return self._pixelSizeX
	def setPixelSizeX(self, pixelSizeX):
		checkType("XSDataDetector", "setPixelSizeX", pixelSizeX, "XSDataLength")
		self._pixelSizeX = pixelSizeX
	def delPixelSizeX(self): self._pixelSizeX = None
	# Properties
	pixelSizeX = property(getPixelSizeX, setPixelSizeX, delPixelSizeX, "Property for pixelSizeX")
	def getPixelSizeY(self): return self._pixelSizeY
	def setPixelSizeY(self, pixelSizeY):
		checkType("XSDataDetector", "setPixelSizeY", pixelSizeY, "XSDataLength")
		self._pixelSizeY = pixelSizeY
	def delPixelSizeY(self): self._pixelSizeY = None
	# Properties
	pixelSizeY = property(getPixelSizeY, setPixelSizeY, delPixelSizeY, "Property for pixelSizeY")
	def getSerialNumber(self): return self._serialNumber
	def setSerialNumber(self, serialNumber):
		checkType("XSDataDetector", "setSerialNumber", serialNumber, "XSDataString")
		self._serialNumber = serialNumber
	def delSerialNumber(self): self._serialNumber = None
	# Properties
	serialNumber = property(getSerialNumber, setSerialNumber, delSerialNumber, "Property for serialNumber")
	def getTwoTheta(self): return self._twoTheta
	def setTwoTheta(self, twoTheta):
		checkType("XSDataDetector", "setTwoTheta", twoTheta, "XSDataAngle")
		self._twoTheta = twoTheta
	def delTwoTheta(self): self._twoTheta = None
	# Properties
	twoTheta = property(getTwoTheta, setTwoTheta, delTwoTheta, "Property for twoTheta")
	def getType(self): return self._type
	def setType(self, type):
		checkType("XSDataDetector", "setType", type, "XSDataString")
		self._type = type
	def delType(self): self._type = None
	# Properties
	type = property(getType, setType, delType, "Property for type")
	def export(self, outfile, level, name_='XSDataDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataDetector'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._beamPositionX is not None:
			self.beamPositionX.export(outfile, level, name_='beamPositionX')
		else:
			warnEmptyAttribute("beamPositionX", "XSDataLength")
		if self._beamPositionY is not None:
			self.beamPositionY.export(outfile, level, name_='beamPositionY')
		else:
			warnEmptyAttribute("beamPositionY", "XSDataLength")
		if self._bin is not None:
			self.bin.export(outfile, level, name_='bin')
		else:
			warnEmptyAttribute("bin", "XSDataString")
		if self._byteOrder is not None:
			self.byteOrder.export(outfile, level, name_='byteOrder')
		else:
			warnEmptyAttribute("byteOrder", "XSDataString")
		if self._dataType is not None:
			self.dataType.export(outfile, level, name_='dataType')
		else:
			warnEmptyAttribute("dataType", "XSDataString")
		if self._distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
		if self._gain is not None:
			self.gain.export(outfile, level, name_='gain')
		if self._imageSaturation is not None:
			self.imageSaturation.export(outfile, level, name_='imageSaturation')
		else:
			warnEmptyAttribute("imageSaturation", "XSDataInteger")
		if self._name is not None:
			self.name.export(outfile, level, name_='name')
		else:
			warnEmptyAttribute("name", "XSDataString")
		if self._numberBytesInHeader is not None:
			self.numberBytesInHeader.export(outfile, level, name_='numberBytesInHeader')
		else:
			warnEmptyAttribute("numberBytesInHeader", "XSDataInteger")
		if self._numberPixelX is not None:
			self.numberPixelX.export(outfile, level, name_='numberPixelX')
		else:
			warnEmptyAttribute("numberPixelX", "XSDataInteger")
		if self._numberPixelY is not None:
			self.numberPixelY.export(outfile, level, name_='numberPixelY')
		else:
			warnEmptyAttribute("numberPixelY", "XSDataInteger")
		if self._pixelSizeX is not None:
			self.pixelSizeX.export(outfile, level, name_='pixelSizeX')
		else:
			warnEmptyAttribute("pixelSizeX", "XSDataLength")
		if self._pixelSizeY is not None:
			self.pixelSizeY.export(outfile, level, name_='pixelSizeY')
		else:
			warnEmptyAttribute("pixelSizeY", "XSDataLength")
		if self._serialNumber is not None:
			self.serialNumber.export(outfile, level, name_='serialNumber')
		else:
			warnEmptyAttribute("serialNumber", "XSDataString")
		if self._twoTheta is not None:
			self.twoTheta.export(outfile, level, name_='twoTheta')
		else:
			warnEmptyAttribute("twoTheta", "XSDataAngle")
		if self._type is not None:
			self.type.export(outfile, level, name_='type')
		else:
			warnEmptyAttribute("type", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPositionX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamPositionX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPositionY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamPositionY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bin':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'byteOrder':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setByteOrder(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDataType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gain':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setGain(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageSaturation':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageSaturation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberBytesInHeader':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberBytesInHeader(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberPixelX':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberPixelX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberPixelY':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberPixelY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSizeX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSizeX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSizeY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSizeY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'serialNumber':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSerialNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'twoTheta':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setTwoTheta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'type':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setType(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataDetector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataDetector' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataDetector is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataDetector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataDetector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataDetector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataDetector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataDetector

class XSDataDiffractionPlan(XSData):
	"""This object contains the main properties a user can parameterize for a crystal characterisation:

- the aimed* parameters are the parameters that a user would like to reach for a BEST run.
- the required* are not yet used (the idea is to warn the user if these parameters cannot be reached)
- complexity: BEST complexity input, can be either "none" (always single wedge strategy). "min" (few subwedges) or "full" (many subwedges).
- maxExposureTimePerDataCollection is the max total exposure time (shutter open, not including readout time) the crystal can be exposed to the X-ray beam.
- forcedSpaceGroup: option to force the space group of the indexing solution
- strategyOption: extra option for BEST for more advanced strategies like estimating the sensitivity to radiation damage
- anomalousData: Depreccated! Boolean value for enabling anomalous strategy. In the future the strategyOption should be used instead of anomalousData.
- estimateRadiationDamage: Boolean value for enabling or disabling the use of Raddose for estimation of radiation damage. If estimateRadiationDamage is enabled also the flux and beamsize must be provided.
- detectorDistanceMin and detectorDistanceMax: optimal input to BEST for limiting the calculated strategy resolution to be in the range of the detector displacements with respect to the sample.
- minTransmission: optional input for BEST
- kappaStrategyOption: optional input for kappa strategies
- numberOfPositions: optional input for BEST"""
	def __init__(self, strategyOption=None, requiredResolution=None, requiredMultiplicity=None, requiredCompleteness=None, numberOfPositions=None, minTransmission=None, minExposureTimePerImage=None, maxExposureTimePerDataCollection=None, kappaStrategyOption=None, goniostatMinOscillationWidth=None, goniostatMaxOscillationSpeed=None, forcedSpaceGroup=None, estimateRadiationDamage=None, detectorDistanceMin=None, detectorDistanceMax=None, complexity=None, anomalousData=None, aimedResolution=None, aimedMultiplicity=None, aimedIOverSigmaAtHighestResolution=None, aimedCompleteness=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", aimedMultiplicity, "XSDataDouble")
		self._aimedMultiplicity = aimedMultiplicity
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", complexity, "XSDataString")
		self._complexity = complexity
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", detectorDistanceMax, "XSDataLength")
		self._detectorDistanceMax = detectorDistanceMax
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", detectorDistanceMin, "XSDataLength")
		self._detectorDistanceMin = detectorDistanceMin
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", estimateRadiationDamage, "XSDataBoolean")
		self._estimateRadiationDamage = estimateRadiationDamage
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", forcedSpaceGroup, "XSDataString")
		self._forcedSpaceGroup = forcedSpaceGroup
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", goniostatMaxOscillationSpeed, "XSDataAngularSpeed")
		self._goniostatMaxOscillationSpeed = goniostatMaxOscillationSpeed
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", goniostatMinOscillationWidth, "XSDataAngle")
		self._goniostatMinOscillationWidth = goniostatMinOscillationWidth
		if kappaStrategyOption is None:
			self._kappaStrategyOption = []
		else:
			checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", kappaStrategyOption, "list")
			self._kappaStrategyOption = kappaStrategyOption
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", maxExposureTimePerDataCollection, "XSDataTime")
		self._maxExposureTimePerDataCollection = maxExposureTimePerDataCollection
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", minTransmission, "XSDataDouble")
		self._minTransmission = minTransmission
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", numberOfPositions, "XSDataInteger")
		self._numberOfPositions = numberOfPositions
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", requiredCompleteness, "XSDataDouble")
		self._requiredCompleteness = requiredCompleteness
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", requiredMultiplicity, "XSDataDouble")
		self._requiredMultiplicity = requiredMultiplicity
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", requiredResolution, "XSDataDouble")
		self._requiredResolution = requiredResolution
		checkType("XSDataDiffractionPlan", "Constructor of XSDataDiffractionPlan", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
	def getAimedCompleteness(self): return self._aimedCompleteness
	def setAimedCompleteness(self, aimedCompleteness):
		checkType("XSDataDiffractionPlan", "setAimedCompleteness", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
	def delAimedCompleteness(self): self._aimedCompleteness = None
	# Properties
	aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
	def getAimedIOverSigmaAtHighestResolution(self): return self._aimedIOverSigmaAtHighestResolution
	def setAimedIOverSigmaAtHighestResolution(self, aimedIOverSigmaAtHighestResolution):
		checkType("XSDataDiffractionPlan", "setAimedIOverSigmaAtHighestResolution", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
	def delAimedIOverSigmaAtHighestResolution(self): self._aimedIOverSigmaAtHighestResolution = None
	# Properties
	aimedIOverSigmaAtHighestResolution = property(getAimedIOverSigmaAtHighestResolution, setAimedIOverSigmaAtHighestResolution, delAimedIOverSigmaAtHighestResolution, "Property for aimedIOverSigmaAtHighestResolution")
	def getAimedMultiplicity(self): return self._aimedMultiplicity
	def setAimedMultiplicity(self, aimedMultiplicity):
		checkType("XSDataDiffractionPlan", "setAimedMultiplicity", aimedMultiplicity, "XSDataDouble")
		self._aimedMultiplicity = aimedMultiplicity
	def delAimedMultiplicity(self): self._aimedMultiplicity = None
	# Properties
	aimedMultiplicity = property(getAimedMultiplicity, setAimedMultiplicity, delAimedMultiplicity, "Property for aimedMultiplicity")
	def getAimedResolution(self): return self._aimedResolution
	def setAimedResolution(self, aimedResolution):
		checkType("XSDataDiffractionPlan", "setAimedResolution", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
	def delAimedResolution(self): self._aimedResolution = None
	# Properties
	aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
	def getAnomalousData(self): return self._anomalousData
	def setAnomalousData(self, anomalousData):
		checkType("XSDataDiffractionPlan", "setAnomalousData", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
	def delAnomalousData(self): self._anomalousData = None
	# Properties
	anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
	def getComplexity(self): return self._complexity
	def setComplexity(self, complexity):
		checkType("XSDataDiffractionPlan", "setComplexity", complexity, "XSDataString")
		self._complexity = complexity
	def delComplexity(self): self._complexity = None
	# Properties
	complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
	def getDetectorDistanceMax(self): return self._detectorDistanceMax
	def setDetectorDistanceMax(self, detectorDistanceMax):
		checkType("XSDataDiffractionPlan", "setDetectorDistanceMax", detectorDistanceMax, "XSDataLength")
		self._detectorDistanceMax = detectorDistanceMax
	def delDetectorDistanceMax(self): self._detectorDistanceMax = None
	# Properties
	detectorDistanceMax = property(getDetectorDistanceMax, setDetectorDistanceMax, delDetectorDistanceMax, "Property for detectorDistanceMax")
	def getDetectorDistanceMin(self): return self._detectorDistanceMin
	def setDetectorDistanceMin(self, detectorDistanceMin):
		checkType("XSDataDiffractionPlan", "setDetectorDistanceMin", detectorDistanceMin, "XSDataLength")
		self._detectorDistanceMin = detectorDistanceMin
	def delDetectorDistanceMin(self): self._detectorDistanceMin = None
	# Properties
	detectorDistanceMin = property(getDetectorDistanceMin, setDetectorDistanceMin, delDetectorDistanceMin, "Property for detectorDistanceMin")
	def getEstimateRadiationDamage(self): return self._estimateRadiationDamage
	def setEstimateRadiationDamage(self, estimateRadiationDamage):
		checkType("XSDataDiffractionPlan", "setEstimateRadiationDamage", estimateRadiationDamage, "XSDataBoolean")
		self._estimateRadiationDamage = estimateRadiationDamage
	def delEstimateRadiationDamage(self): self._estimateRadiationDamage = None
	# Properties
	estimateRadiationDamage = property(getEstimateRadiationDamage, setEstimateRadiationDamage, delEstimateRadiationDamage, "Property for estimateRadiationDamage")
	def getForcedSpaceGroup(self): return self._forcedSpaceGroup
	def setForcedSpaceGroup(self, forcedSpaceGroup):
		checkType("XSDataDiffractionPlan", "setForcedSpaceGroup", forcedSpaceGroup, "XSDataString")
		self._forcedSpaceGroup = forcedSpaceGroup
	def delForcedSpaceGroup(self): self._forcedSpaceGroup = None
	# Properties
	forcedSpaceGroup = property(getForcedSpaceGroup, setForcedSpaceGroup, delForcedSpaceGroup, "Property for forcedSpaceGroup")
	def getGoniostatMaxOscillationSpeed(self): return self._goniostatMaxOscillationSpeed
	def setGoniostatMaxOscillationSpeed(self, goniostatMaxOscillationSpeed):
		checkType("XSDataDiffractionPlan", "setGoniostatMaxOscillationSpeed", goniostatMaxOscillationSpeed, "XSDataAngularSpeed")
		self._goniostatMaxOscillationSpeed = goniostatMaxOscillationSpeed
	def delGoniostatMaxOscillationSpeed(self): self._goniostatMaxOscillationSpeed = None
	# Properties
	goniostatMaxOscillationSpeed = property(getGoniostatMaxOscillationSpeed, setGoniostatMaxOscillationSpeed, delGoniostatMaxOscillationSpeed, "Property for goniostatMaxOscillationSpeed")
	def getGoniostatMinOscillationWidth(self): return self._goniostatMinOscillationWidth
	def setGoniostatMinOscillationWidth(self, goniostatMinOscillationWidth):
		checkType("XSDataDiffractionPlan", "setGoniostatMinOscillationWidth", goniostatMinOscillationWidth, "XSDataAngle")
		self._goniostatMinOscillationWidth = goniostatMinOscillationWidth
	def delGoniostatMinOscillationWidth(self): self._goniostatMinOscillationWidth = None
	# Properties
	goniostatMinOscillationWidth = property(getGoniostatMinOscillationWidth, setGoniostatMinOscillationWidth, delGoniostatMinOscillationWidth, "Property for goniostatMinOscillationWidth")
	def getKappaStrategyOption(self): return self._kappaStrategyOption
	def setKappaStrategyOption(self, kappaStrategyOption):
		checkType("XSDataDiffractionPlan", "setKappaStrategyOption", kappaStrategyOption, "list")
		self._kappaStrategyOption = kappaStrategyOption
	def delKappaStrategyOption(self): self._kappaStrategyOption = None
	# Properties
	kappaStrategyOption = property(getKappaStrategyOption, setKappaStrategyOption, delKappaStrategyOption, "Property for kappaStrategyOption")
	def addKappaStrategyOption(self, value):
		checkType("XSDataDiffractionPlan", "setKappaStrategyOption", value, "XSDataString")
		self._kappaStrategyOption.append(value)
	def insertKappaStrategyOption(self, index, value):
		checkType("XSDataDiffractionPlan", "setKappaStrategyOption", value, "XSDataString")
		self._kappaStrategyOption[index] = value
	def getMaxExposureTimePerDataCollection(self): return self._maxExposureTimePerDataCollection
	def setMaxExposureTimePerDataCollection(self, maxExposureTimePerDataCollection):
		checkType("XSDataDiffractionPlan", "setMaxExposureTimePerDataCollection", maxExposureTimePerDataCollection, "XSDataTime")
		self._maxExposureTimePerDataCollection = maxExposureTimePerDataCollection
	def delMaxExposureTimePerDataCollection(self): self._maxExposureTimePerDataCollection = None
	# Properties
	maxExposureTimePerDataCollection = property(getMaxExposureTimePerDataCollection, setMaxExposureTimePerDataCollection, delMaxExposureTimePerDataCollection, "Property for maxExposureTimePerDataCollection")
	def getMinExposureTimePerImage(self): return self._minExposureTimePerImage
	def setMinExposureTimePerImage(self, minExposureTimePerImage):
		checkType("XSDataDiffractionPlan", "setMinExposureTimePerImage", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
	def delMinExposureTimePerImage(self): self._minExposureTimePerImage = None
	# Properties
	minExposureTimePerImage = property(getMinExposureTimePerImage, setMinExposureTimePerImage, delMinExposureTimePerImage, "Property for minExposureTimePerImage")
	def getMinTransmission(self): return self._minTransmission
	def setMinTransmission(self, minTransmission):
		checkType("XSDataDiffractionPlan", "setMinTransmission", minTransmission, "XSDataDouble")
		self._minTransmission = minTransmission
	def delMinTransmission(self): self._minTransmission = None
	# Properties
	minTransmission = property(getMinTransmission, setMinTransmission, delMinTransmission, "Property for minTransmission")
	def getNumberOfPositions(self): return self._numberOfPositions
	def setNumberOfPositions(self, numberOfPositions):
		checkType("XSDataDiffractionPlan", "setNumberOfPositions", numberOfPositions, "XSDataInteger")
		self._numberOfPositions = numberOfPositions
	def delNumberOfPositions(self): self._numberOfPositions = None
	# Properties
	numberOfPositions = property(getNumberOfPositions, setNumberOfPositions, delNumberOfPositions, "Property for numberOfPositions")
	def getRequiredCompleteness(self): return self._requiredCompleteness
	def setRequiredCompleteness(self, requiredCompleteness):
		checkType("XSDataDiffractionPlan", "setRequiredCompleteness", requiredCompleteness, "XSDataDouble")
		self._requiredCompleteness = requiredCompleteness
	def delRequiredCompleteness(self): self._requiredCompleteness = None
	# Properties
	requiredCompleteness = property(getRequiredCompleteness, setRequiredCompleteness, delRequiredCompleteness, "Property for requiredCompleteness")
	def getRequiredMultiplicity(self): return self._requiredMultiplicity
	def setRequiredMultiplicity(self, requiredMultiplicity):
		checkType("XSDataDiffractionPlan", "setRequiredMultiplicity", requiredMultiplicity, "XSDataDouble")
		self._requiredMultiplicity = requiredMultiplicity
	def delRequiredMultiplicity(self): self._requiredMultiplicity = None
	# Properties
	requiredMultiplicity = property(getRequiredMultiplicity, setRequiredMultiplicity, delRequiredMultiplicity, "Property for requiredMultiplicity")
	def getRequiredResolution(self): return self._requiredResolution
	def setRequiredResolution(self, requiredResolution):
		checkType("XSDataDiffractionPlan", "setRequiredResolution", requiredResolution, "XSDataDouble")
		self._requiredResolution = requiredResolution
	def delRequiredResolution(self): self._requiredResolution = None
	# Properties
	requiredResolution = property(getRequiredResolution, setRequiredResolution, delRequiredResolution, "Property for requiredResolution")
	def getStrategyOption(self): return self._strategyOption
	def setStrategyOption(self, strategyOption):
		checkType("XSDataDiffractionPlan", "setStrategyOption", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
	def delStrategyOption(self): self._strategyOption = None
	# Properties
	strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
	def export(self, outfile, level, name_='XSDataDiffractionPlan'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataDiffractionPlan'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._aimedCompleteness is not None:
			self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
		if self._aimedIOverSigmaAtHighestResolution is not None:
			self.aimedIOverSigmaAtHighestResolution.export(outfile, level, name_='aimedIOverSigmaAtHighestResolution')
		if self._aimedMultiplicity is not None:
			self.aimedMultiplicity.export(outfile, level, name_='aimedMultiplicity')
		if self._aimedResolution is not None:
			self.aimedResolution.export(outfile, level, name_='aimedResolution')
		if self._anomalousData is not None:
			self.anomalousData.export(outfile, level, name_='anomalousData')
		if self._complexity is not None:
			self.complexity.export(outfile, level, name_='complexity')
		if self._detectorDistanceMax is not None:
			self.detectorDistanceMax.export(outfile, level, name_='detectorDistanceMax')
		if self._detectorDistanceMin is not None:
			self.detectorDistanceMin.export(outfile, level, name_='detectorDistanceMin')
		if self._estimateRadiationDamage is not None:
			self.estimateRadiationDamage.export(outfile, level, name_='estimateRadiationDamage')
		if self._forcedSpaceGroup is not None:
			self.forcedSpaceGroup.export(outfile, level, name_='forcedSpaceGroup')
		if self._goniostatMaxOscillationSpeed is not None:
			self.goniostatMaxOscillationSpeed.export(outfile, level, name_='goniostatMaxOscillationSpeed')
		if self._goniostatMinOscillationWidth is not None:
			self.goniostatMinOscillationWidth.export(outfile, level, name_='goniostatMinOscillationWidth')
		for kappaStrategyOption_ in self.getKappaStrategyOption():
			kappaStrategyOption_.export(outfile, level, name_='kappaStrategyOption')
		if self._maxExposureTimePerDataCollection is not None:
			self.maxExposureTimePerDataCollection.export(outfile, level, name_='maxExposureTimePerDataCollection')
		if self._minExposureTimePerImage is not None:
			self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
		if self._minTransmission is not None:
			self.minTransmission.export(outfile, level, name_='minTransmission')
		if self._numberOfPositions is not None:
			self.numberOfPositions.export(outfile, level, name_='numberOfPositions')
		if self._requiredCompleteness is not None:
			self.requiredCompleteness.export(outfile, level, name_='requiredCompleteness')
		if self._requiredMultiplicity is not None:
			self.requiredMultiplicity.export(outfile, level, name_='requiredMultiplicity')
		if self._requiredResolution is not None:
			self.requiredResolution.export(outfile, level, name_='requiredResolution')
		if self._strategyOption is not None:
			self.strategyOption.export(outfile, level, name_='strategyOption')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedCompleteness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedIOverSigmaAtHighestResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedIOverSigmaAtHighestResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedMultiplicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousData':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAnomalousData(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'complexity':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComplexity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistanceMax':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistanceMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistanceMin':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistanceMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'estimateRadiationDamage':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setEstimateRadiationDamage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'forcedSpaceGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setForcedSpaceGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostatMaxOscillationSpeed':
			obj_ = XSDataAngularSpeed()
			obj_.build(child_)
			self.setGoniostatMaxOscillationSpeed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostatMinOscillationWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setGoniostatMinOscillationWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappaStrategyOption':
			obj_ = XSDataString()
			obj_.build(child_)
			self.kappaStrategyOption.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxExposureTimePerDataCollection':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setMaxExposureTimePerDataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minExposureTimePerImage':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setMinExposureTimePerImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minTransmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfPositions':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfPositions(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'requiredCompleteness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRequiredCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'requiredMultiplicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRequiredMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'requiredResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRequiredResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategyOption':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStrategyOption(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataDiffractionPlan" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataDiffractionPlan' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataDiffractionPlan is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataDiffractionPlan.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataDiffractionPlan()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataDiffractionPlan" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataDiffractionPlan()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataDiffractionPlan

class XSDataGoniostat(XSData):
	"""The properties of a goniostat:
- the maximal rotation speed permitted
- the minimal width for an oscillation width of subwedge
- the name of the rotation axis (typically phi)
- the rotation start angle
- the rotation end angle"""
	def __init__(self, samplePosition=None, rotationAxisStart=None, rotationAxisEnd=None, rotationAxis=None, overlap=None, oscillationWidth=None, minOscillationWidth=None, maxOscillationSpeed=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", maxOscillationSpeed, "XSDataAngularSpeed")
		self._maxOscillationSpeed = maxOscillationSpeed
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", minOscillationWidth, "XSDataAngle")
		self._minOscillationWidth = minOscillationWidth
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", oscillationWidth, "XSDataAngle")
		self._oscillationWidth = oscillationWidth
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", overlap, "XSDataAngle")
		self._overlap = overlap
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", rotationAxis, "XSDataString")
		self._rotationAxis = rotationAxis
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", rotationAxisEnd, "XSDataAngle")
		self._rotationAxisEnd = rotationAxisEnd
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
		checkType("XSDataGoniostat", "Constructor of XSDataGoniostat", samplePosition, "XSDataVectorDouble")
		self._samplePosition = samplePosition
	def getMaxOscillationSpeed(self): return self._maxOscillationSpeed
	def setMaxOscillationSpeed(self, maxOscillationSpeed):
		checkType("XSDataGoniostat", "setMaxOscillationSpeed", maxOscillationSpeed, "XSDataAngularSpeed")
		self._maxOscillationSpeed = maxOscillationSpeed
	def delMaxOscillationSpeed(self): self._maxOscillationSpeed = None
	# Properties
	maxOscillationSpeed = property(getMaxOscillationSpeed, setMaxOscillationSpeed, delMaxOscillationSpeed, "Property for maxOscillationSpeed")
	def getMinOscillationWidth(self): return self._minOscillationWidth
	def setMinOscillationWidth(self, minOscillationWidth):
		checkType("XSDataGoniostat", "setMinOscillationWidth", minOscillationWidth, "XSDataAngle")
		self._minOscillationWidth = minOscillationWidth
	def delMinOscillationWidth(self): self._minOscillationWidth = None
	# Properties
	minOscillationWidth = property(getMinOscillationWidth, setMinOscillationWidth, delMinOscillationWidth, "Property for minOscillationWidth")
	def getOscillationWidth(self): return self._oscillationWidth
	def setOscillationWidth(self, oscillationWidth):
		checkType("XSDataGoniostat", "setOscillationWidth", oscillationWidth, "XSDataAngle")
		self._oscillationWidth = oscillationWidth
	def delOscillationWidth(self): self._oscillationWidth = None
	# Properties
	oscillationWidth = property(getOscillationWidth, setOscillationWidth, delOscillationWidth, "Property for oscillationWidth")
	def getOverlap(self): return self._overlap
	def setOverlap(self, overlap):
		checkType("XSDataGoniostat", "setOverlap", overlap, "XSDataAngle")
		self._overlap = overlap
	def delOverlap(self): self._overlap = None
	# Properties
	overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
	def getRotationAxis(self): return self._rotationAxis
	def setRotationAxis(self, rotationAxis):
		checkType("XSDataGoniostat", "setRotationAxis", rotationAxis, "XSDataString")
		self._rotationAxis = rotationAxis
	def delRotationAxis(self): self._rotationAxis = None
	# Properties
	rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
	def getRotationAxisEnd(self): return self._rotationAxisEnd
	def setRotationAxisEnd(self, rotationAxisEnd):
		checkType("XSDataGoniostat", "setRotationAxisEnd", rotationAxisEnd, "XSDataAngle")
		self._rotationAxisEnd = rotationAxisEnd
	def delRotationAxisEnd(self): self._rotationAxisEnd = None
	# Properties
	rotationAxisEnd = property(getRotationAxisEnd, setRotationAxisEnd, delRotationAxisEnd, "Property for rotationAxisEnd")
	def getRotationAxisStart(self): return self._rotationAxisStart
	def setRotationAxisStart(self, rotationAxisStart):
		checkType("XSDataGoniostat", "setRotationAxisStart", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
	def delRotationAxisStart(self): self._rotationAxisStart = None
	# Properties
	rotationAxisStart = property(getRotationAxisStart, setRotationAxisStart, delRotationAxisStart, "Property for rotationAxisStart")
	def getSamplePosition(self): return self._samplePosition
	def setSamplePosition(self, samplePosition):
		checkType("XSDataGoniostat", "setSamplePosition", samplePosition, "XSDataVectorDouble")
		self._samplePosition = samplePosition
	def delSamplePosition(self): self._samplePosition = None
	# Properties
	samplePosition = property(getSamplePosition, setSamplePosition, delSamplePosition, "Property for samplePosition")
	def export(self, outfile, level, name_='XSDataGoniostat'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGoniostat'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._maxOscillationSpeed is not None:
			self.maxOscillationSpeed.export(outfile, level, name_='maxOscillationSpeed')
		if self._minOscillationWidth is not None:
			self.minOscillationWidth.export(outfile, level, name_='minOscillationWidth')
		if self._oscillationWidth is not None:
			self.oscillationWidth.export(outfile, level, name_='oscillationWidth')
		else:
			warnEmptyAttribute("oscillationWidth", "XSDataAngle")
		if self._overlap is not None:
			self.overlap.export(outfile, level, name_='overlap')
		if self._rotationAxis is not None:
			self.rotationAxis.export(outfile, level, name_='rotationAxis')
		else:
			warnEmptyAttribute("rotationAxis", "XSDataString")
		if self._rotationAxisEnd is not None:
			self.rotationAxisEnd.export(outfile, level, name_='rotationAxisEnd')
		else:
			warnEmptyAttribute("rotationAxisEnd", "XSDataAngle")
		if self._rotationAxisStart is not None:
			self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
		else:
			warnEmptyAttribute("rotationAxisStart", "XSDataAngle")
		if self._samplePosition is not None:
			self.samplePosition.export(outfile, level, name_='samplePosition')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxOscillationSpeed':
			obj_ = XSDataAngularSpeed()
			obj_.build(child_)
			self.setMaxOscillationSpeed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minOscillationWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setMinOscillationWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'oscillationWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOscillationWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overlap':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOverlap(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxis':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRotationAxis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisEnd':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotationAxisEnd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisStart':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotationAxisStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'samplePosition':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setSamplePosition(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGoniostat" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGoniostat' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGoniostat is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGoniostat.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGoniostat()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGoniostat" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGoniostat()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGoniostat

class XSDataExperimentalCondition(XSData):
	"""This object encapsulates all the physical properties of an experiment instrumentation. i.e: Beam, detector, Goniostat."""
	def __init__(self, goniostat=None, detector=None, beam=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataExperimentalCondition", "Constructor of XSDataExperimentalCondition", beam, "XSDataBeam")
		self._beam = beam
		checkType("XSDataExperimentalCondition", "Constructor of XSDataExperimentalCondition", detector, "XSDataDetector")
		self._detector = detector
		checkType("XSDataExperimentalCondition", "Constructor of XSDataExperimentalCondition", goniostat, "XSDataGoniostat")
		self._goniostat = goniostat
	def getBeam(self): return self._beam
	def setBeam(self, beam):
		checkType("XSDataExperimentalCondition", "setBeam", beam, "XSDataBeam")
		self._beam = beam
	def delBeam(self): self._beam = None
	# Properties
	beam = property(getBeam, setBeam, delBeam, "Property for beam")
	def getDetector(self): return self._detector
	def setDetector(self, detector):
		checkType("XSDataExperimentalCondition", "setDetector", detector, "XSDataDetector")
		self._detector = detector
	def delDetector(self): self._detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getGoniostat(self): return self._goniostat
	def setGoniostat(self, goniostat):
		checkType("XSDataExperimentalCondition", "setGoniostat", goniostat, "XSDataGoniostat")
		self._goniostat = goniostat
	def delGoniostat(self): self._goniostat = None
	# Properties
	goniostat = property(getGoniostat, setGoniostat, delGoniostat, "Property for goniostat")
	def export(self, outfile, level, name_='XSDataExperimentalCondition'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataExperimentalCondition'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._beam is not None:
			self.beam.export(outfile, level, name_='beam')
		if self._detector is not None:
			self.detector.export(outfile, level, name_='detector')
		if self._goniostat is not None:
			self.goniostat.export(outfile, level, name_='goniostat')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beam':
			obj_ = XSDataBeam()
			obj_.build(child_)
			self.setBeam(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostat':
			obj_ = XSDataGoniostat()
			obj_.build(child_)
			self.setGoniostat(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataExperimentalCondition" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataExperimentalCondition' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataExperimentalCondition is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataExperimentalCondition.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataExperimentalCondition()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataExperimentalCondition" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataExperimentalCondition()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataExperimentalCondition

class XSDataImageQualityIndicators(XSData):
	def __init__(self, totalIntegratedSignal=None, spotTotal=None, signalRangeMin=None, signalRangeMax=None, signalRangeAverage=None, saturationRangeMin=None, saturationRangeMax=None, saturationRangeAverage=None, pctSaturationTop50Peaks=None, method2Res=None, method1Res=None, maxUnitCell=None, inResolutionOvrlSpots=None, inResTotal=None, image=None, iceRings=None, goodBraggCandidates=None, binPopCutOffMethod2Res=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", binPopCutOffMethod2Res, "XSDataDouble")
		self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", goodBraggCandidates, "XSDataInteger")
		self._goodBraggCandidates = goodBraggCandidates
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", iceRings, "XSDataInteger")
		self._iceRings = iceRings
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", image, "XSDataImage")
		self._image = image
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", inResTotal, "XSDataInteger")
		self._inResTotal = inResTotal
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", inResolutionOvrlSpots, "XSDataInteger")
		self._inResolutionOvrlSpots = inResolutionOvrlSpots
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", maxUnitCell, "XSDataDouble")
		self._maxUnitCell = maxUnitCell
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", method1Res, "XSDataDouble")
		self._method1Res = method1Res
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", method2Res, "XSDataDouble")
		self._method2Res = method2Res
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", pctSaturationTop50Peaks, "XSDataDouble")
		self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", saturationRangeAverage, "XSDataDouble")
		self._saturationRangeAverage = saturationRangeAverage
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", saturationRangeMax, "XSDataDouble")
		self._saturationRangeMax = saturationRangeMax
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", saturationRangeMin, "XSDataDouble")
		self._saturationRangeMin = saturationRangeMin
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", signalRangeAverage, "XSDataDouble")
		self._signalRangeAverage = signalRangeAverage
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", signalRangeMax, "XSDataDouble")
		self._signalRangeMax = signalRangeMax
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", signalRangeMin, "XSDataDouble")
		self._signalRangeMin = signalRangeMin
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", spotTotal, "XSDataInteger")
		self._spotTotal = spotTotal
		checkType("XSDataImageQualityIndicators", "Constructor of XSDataImageQualityIndicators", totalIntegratedSignal, "XSDataDouble")
		self._totalIntegratedSignal = totalIntegratedSignal
	def getBinPopCutOffMethod2Res(self): return self._binPopCutOffMethod2Res
	def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res):
		checkType("XSDataImageQualityIndicators", "setBinPopCutOffMethod2Res", binPopCutOffMethod2Res, "XSDataDouble")
		self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
	def delBinPopCutOffMethod2Res(self): self._binPopCutOffMethod2Res = None
	# Properties
	binPopCutOffMethod2Res = property(getBinPopCutOffMethod2Res, setBinPopCutOffMethod2Res, delBinPopCutOffMethod2Res, "Property for binPopCutOffMethod2Res")
	def getGoodBraggCandidates(self): return self._goodBraggCandidates
	def setGoodBraggCandidates(self, goodBraggCandidates):
		checkType("XSDataImageQualityIndicators", "setGoodBraggCandidates", goodBraggCandidates, "XSDataInteger")
		self._goodBraggCandidates = goodBraggCandidates
	def delGoodBraggCandidates(self): self._goodBraggCandidates = None
	# Properties
	goodBraggCandidates = property(getGoodBraggCandidates, setGoodBraggCandidates, delGoodBraggCandidates, "Property for goodBraggCandidates")
	def getIceRings(self): return self._iceRings
	def setIceRings(self, iceRings):
		checkType("XSDataImageQualityIndicators", "setIceRings", iceRings, "XSDataInteger")
		self._iceRings = iceRings
	def delIceRings(self): self._iceRings = None
	# Properties
	iceRings = property(getIceRings, setIceRings, delIceRings, "Property for iceRings")
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataImageQualityIndicators", "setImage", image, "XSDataImage")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getInResTotal(self): return self._inResTotal
	def setInResTotal(self, inResTotal):
		checkType("XSDataImageQualityIndicators", "setInResTotal", inResTotal, "XSDataInteger")
		self._inResTotal = inResTotal
	def delInResTotal(self): self._inResTotal = None
	# Properties
	inResTotal = property(getInResTotal, setInResTotal, delInResTotal, "Property for inResTotal")
	def getInResolutionOvrlSpots(self): return self._inResolutionOvrlSpots
	def setInResolutionOvrlSpots(self, inResolutionOvrlSpots):
		checkType("XSDataImageQualityIndicators", "setInResolutionOvrlSpots", inResolutionOvrlSpots, "XSDataInteger")
		self._inResolutionOvrlSpots = inResolutionOvrlSpots
	def delInResolutionOvrlSpots(self): self._inResolutionOvrlSpots = None
	# Properties
	inResolutionOvrlSpots = property(getInResolutionOvrlSpots, setInResolutionOvrlSpots, delInResolutionOvrlSpots, "Property for inResolutionOvrlSpots")
	def getMaxUnitCell(self): return self._maxUnitCell
	def setMaxUnitCell(self, maxUnitCell):
		checkType("XSDataImageQualityIndicators", "setMaxUnitCell", maxUnitCell, "XSDataDouble")
		self._maxUnitCell = maxUnitCell
	def delMaxUnitCell(self): self._maxUnitCell = None
	# Properties
	maxUnitCell = property(getMaxUnitCell, setMaxUnitCell, delMaxUnitCell, "Property for maxUnitCell")
	def getMethod1Res(self): return self._method1Res
	def setMethod1Res(self, method1Res):
		checkType("XSDataImageQualityIndicators", "setMethod1Res", method1Res, "XSDataDouble")
		self._method1Res = method1Res
	def delMethod1Res(self): self._method1Res = None
	# Properties
	method1Res = property(getMethod1Res, setMethod1Res, delMethod1Res, "Property for method1Res")
	def getMethod2Res(self): return self._method2Res
	def setMethod2Res(self, method2Res):
		checkType("XSDataImageQualityIndicators", "setMethod2Res", method2Res, "XSDataDouble")
		self._method2Res = method2Res
	def delMethod2Res(self): self._method2Res = None
	# Properties
	method2Res = property(getMethod2Res, setMethod2Res, delMethod2Res, "Property for method2Res")
	def getPctSaturationTop50Peaks(self): return self._pctSaturationTop50Peaks
	def setPctSaturationTop50Peaks(self, pctSaturationTop50Peaks):
		checkType("XSDataImageQualityIndicators", "setPctSaturationTop50Peaks", pctSaturationTop50Peaks, "XSDataDouble")
		self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
	def delPctSaturationTop50Peaks(self): self._pctSaturationTop50Peaks = None
	# Properties
	pctSaturationTop50Peaks = property(getPctSaturationTop50Peaks, setPctSaturationTop50Peaks, delPctSaturationTop50Peaks, "Property for pctSaturationTop50Peaks")
	def getSaturationRangeAverage(self): return self._saturationRangeAverage
	def setSaturationRangeAverage(self, saturationRangeAverage):
		checkType("XSDataImageQualityIndicators", "setSaturationRangeAverage", saturationRangeAverage, "XSDataDouble")
		self._saturationRangeAverage = saturationRangeAverage
	def delSaturationRangeAverage(self): self._saturationRangeAverage = None
	# Properties
	saturationRangeAverage = property(getSaturationRangeAverage, setSaturationRangeAverage, delSaturationRangeAverage, "Property for saturationRangeAverage")
	def getSaturationRangeMax(self): return self._saturationRangeMax
	def setSaturationRangeMax(self, saturationRangeMax):
		checkType("XSDataImageQualityIndicators", "setSaturationRangeMax", saturationRangeMax, "XSDataDouble")
		self._saturationRangeMax = saturationRangeMax
	def delSaturationRangeMax(self): self._saturationRangeMax = None
	# Properties
	saturationRangeMax = property(getSaturationRangeMax, setSaturationRangeMax, delSaturationRangeMax, "Property for saturationRangeMax")
	def getSaturationRangeMin(self): return self._saturationRangeMin
	def setSaturationRangeMin(self, saturationRangeMin):
		checkType("XSDataImageQualityIndicators", "setSaturationRangeMin", saturationRangeMin, "XSDataDouble")
		self._saturationRangeMin = saturationRangeMin
	def delSaturationRangeMin(self): self._saturationRangeMin = None
	# Properties
	saturationRangeMin = property(getSaturationRangeMin, setSaturationRangeMin, delSaturationRangeMin, "Property for saturationRangeMin")
	def getSignalRangeAverage(self): return self._signalRangeAverage
	def setSignalRangeAverage(self, signalRangeAverage):
		checkType("XSDataImageQualityIndicators", "setSignalRangeAverage", signalRangeAverage, "XSDataDouble")
		self._signalRangeAverage = signalRangeAverage
	def delSignalRangeAverage(self): self._signalRangeAverage = None
	# Properties
	signalRangeAverage = property(getSignalRangeAverage, setSignalRangeAverage, delSignalRangeAverage, "Property for signalRangeAverage")
	def getSignalRangeMax(self): return self._signalRangeMax
	def setSignalRangeMax(self, signalRangeMax):
		checkType("XSDataImageQualityIndicators", "setSignalRangeMax", signalRangeMax, "XSDataDouble")
		self._signalRangeMax = signalRangeMax
	def delSignalRangeMax(self): self._signalRangeMax = None
	# Properties
	signalRangeMax = property(getSignalRangeMax, setSignalRangeMax, delSignalRangeMax, "Property for signalRangeMax")
	def getSignalRangeMin(self): return self._signalRangeMin
	def setSignalRangeMin(self, signalRangeMin):
		checkType("XSDataImageQualityIndicators", "setSignalRangeMin", signalRangeMin, "XSDataDouble")
		self._signalRangeMin = signalRangeMin
	def delSignalRangeMin(self): self._signalRangeMin = None
	# Properties
	signalRangeMin = property(getSignalRangeMin, setSignalRangeMin, delSignalRangeMin, "Property for signalRangeMin")
	def getSpotTotal(self): return self._spotTotal
	def setSpotTotal(self, spotTotal):
		checkType("XSDataImageQualityIndicators", "setSpotTotal", spotTotal, "XSDataInteger")
		self._spotTotal = spotTotal
	def delSpotTotal(self): self._spotTotal = None
	# Properties
	spotTotal = property(getSpotTotal, setSpotTotal, delSpotTotal, "Property for spotTotal")
	def getTotalIntegratedSignal(self): return self._totalIntegratedSignal
	def setTotalIntegratedSignal(self, totalIntegratedSignal):
		checkType("XSDataImageQualityIndicators", "setTotalIntegratedSignal", totalIntegratedSignal, "XSDataDouble")
		self._totalIntegratedSignal = totalIntegratedSignal
	def delTotalIntegratedSignal(self): self._totalIntegratedSignal = None
	# Properties
	totalIntegratedSignal = property(getTotalIntegratedSignal, setTotalIntegratedSignal, delTotalIntegratedSignal, "Property for totalIntegratedSignal")
	def export(self, outfile, level, name_='XSDataImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataImageQualityIndicators'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._binPopCutOffMethod2Res is not None:
			self.binPopCutOffMethod2Res.export(outfile, level, name_='binPopCutOffMethod2Res')
		else:
			warnEmptyAttribute("binPopCutOffMethod2Res", "XSDataDouble")
		if self._goodBraggCandidates is not None:
			self.goodBraggCandidates.export(outfile, level, name_='goodBraggCandidates')
		else:
			warnEmptyAttribute("goodBraggCandidates", "XSDataInteger")
		if self._iceRings is not None:
			self.iceRings.export(outfile, level, name_='iceRings')
		else:
			warnEmptyAttribute("iceRings", "XSDataInteger")
		if self._image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataImage")
		if self._inResTotal is not None:
			self.inResTotal.export(outfile, level, name_='inResTotal')
		else:
			warnEmptyAttribute("inResTotal", "XSDataInteger")
		if self._inResolutionOvrlSpots is not None:
			self.inResolutionOvrlSpots.export(outfile, level, name_='inResolutionOvrlSpots')
		else:
			warnEmptyAttribute("inResolutionOvrlSpots", "XSDataInteger")
		if self._maxUnitCell is not None:
			self.maxUnitCell.export(outfile, level, name_='maxUnitCell')
		else:
			warnEmptyAttribute("maxUnitCell", "XSDataDouble")
		if self._method1Res is not None:
			self.method1Res.export(outfile, level, name_='method1Res')
		else:
			warnEmptyAttribute("method1Res", "XSDataDouble")
		if self._method2Res is not None:
			self.method2Res.export(outfile, level, name_='method2Res')
		else:
			warnEmptyAttribute("method2Res", "XSDataDouble")
		if self._pctSaturationTop50Peaks is not None:
			self.pctSaturationTop50Peaks.export(outfile, level, name_='pctSaturationTop50Peaks')
		else:
			warnEmptyAttribute("pctSaturationTop50Peaks", "XSDataDouble")
		if self._saturationRangeAverage is not None:
			self.saturationRangeAverage.export(outfile, level, name_='saturationRangeAverage')
		if self._saturationRangeMax is not None:
			self.saturationRangeMax.export(outfile, level, name_='saturationRangeMax')
		if self._saturationRangeMin is not None:
			self.saturationRangeMin.export(outfile, level, name_='saturationRangeMin')
		if self._signalRangeAverage is not None:
			self.signalRangeAverage.export(outfile, level, name_='signalRangeAverage')
		if self._signalRangeMax is not None:
			self.signalRangeMax.export(outfile, level, name_='signalRangeMax')
		if self._signalRangeMin is not None:
			self.signalRangeMin.export(outfile, level, name_='signalRangeMin')
		if self._spotTotal is not None:
			self.spotTotal.export(outfile, level, name_='spotTotal')
		else:
			warnEmptyAttribute("spotTotal", "XSDataInteger")
		if self._totalIntegratedSignal is not None:
			self.totalIntegratedSignal.export(outfile, level, name_='totalIntegratedSignal')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'binPopCutOffMethod2Res':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBinPopCutOffMethod2Res(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goodBraggCandidates':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setGoodBraggCandidates(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iceRings':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIceRings(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inResTotal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setInResTotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inResolutionOvrlSpots':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setInResolutionOvrlSpots(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxUnitCell':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxUnitCell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'method1Res':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMethod1Res(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'method2Res':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMethod2Res(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pctSaturationTop50Peaks':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPctSaturationTop50Peaks(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'saturationRangeAverage':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSaturationRangeAverage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'saturationRangeMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSaturationRangeMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'saturationRangeMin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSaturationRangeMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'signalRangeAverage':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSignalRangeAverage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'signalRangeMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSignalRangeMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'signalRangeMin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSignalRangeMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotTotal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpotTotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'totalIntegratedSignal':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTotalIntegratedSignal(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataImageQualityIndicators

class XSDataIndexingSolution(XSData):
	def __init__(self, penalty=None, number=None, crystal=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataIndexingSolution", "Constructor of XSDataIndexingSolution", crystal, "XSDataCrystal")
		self._crystal = crystal
		checkType("XSDataIndexingSolution", "Constructor of XSDataIndexingSolution", number, "XSDataInteger")
		self._number = number
		checkType("XSDataIndexingSolution", "Constructor of XSDataIndexingSolution", penalty, "XSDataFloat")
		self._penalty = penalty
	def getCrystal(self): return self._crystal
	def setCrystal(self, crystal):
		checkType("XSDataIndexingSolution", "setCrystal", crystal, "XSDataCrystal")
		self._crystal = crystal
	def delCrystal(self): self._crystal = None
	# Properties
	crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
	def getNumber(self): return self._number
	def setNumber(self, number):
		checkType("XSDataIndexingSolution", "setNumber", number, "XSDataInteger")
		self._number = number
	def delNumber(self): self._number = None
	# Properties
	number = property(getNumber, setNumber, delNumber, "Property for number")
	def getPenalty(self): return self._penalty
	def setPenalty(self, penalty):
		checkType("XSDataIndexingSolution", "setPenalty", penalty, "XSDataFloat")
		self._penalty = penalty
	def delPenalty(self): self._penalty = None
	# Properties
	penalty = property(getPenalty, setPenalty, delPenalty, "Property for penalty")
	def export(self, outfile, level, name_='XSDataIndexingSolution'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIndexingSolution'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._crystal is not None:
			self.crystal.export(outfile, level, name_='crystal')
		else:
			warnEmptyAttribute("crystal", "XSDataCrystal")
		if self._number is not None:
			self.number.export(outfile, level, name_='number')
		else:
			warnEmptyAttribute("number", "XSDataInteger")
		if self._penalty is not None:
			self.penalty.export(outfile, level, name_='penalty')
		else:
			warnEmptyAttribute("penalty", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'number':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'penalty':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setPenalty(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIndexingSolution" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIndexingSolution' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIndexingSolution is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIndexingSolution.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingSolution()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIndexingSolution" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingSolution()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIndexingSolution

class XSDataIntegrationSubWedgeResult(XSData):
	def __init__(self, subWedgeNumber=None, statisticsPerResolutionBin=None, statistics=None, integrationLogFile=None, generatedMTZFile=None, experimentalConditionRefined=None, bestfilePar=None, bestfileHKL=None, bestfileDat=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", bestfileDat, "XSDataString")
		self._bestfileDat = bestfileDat
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", bestfileHKL, "XSDataString")
		self._bestfileHKL = bestfileHKL
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", bestfilePar, "XSDataString")
		self._bestfilePar = bestfilePar
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", generatedMTZFile, "XSDataFile")
		self._generatedMTZFile = generatedMTZFile
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", integrationLogFile, "XSDataFile")
		self._integrationLogFile = integrationLogFile
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", statistics, "XSDataStatisticsIntegration")
		self._statistics = statistics
		if statisticsPerResolutionBin is None:
			self._statisticsPerResolutionBin = []
		else:
			checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", statisticsPerResolutionBin, "list")
			self._statisticsPerResolutionBin = statisticsPerResolutionBin
		checkType("XSDataIntegrationSubWedgeResult", "Constructor of XSDataIntegrationSubWedgeResult", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
	def getBestfileDat(self): return self._bestfileDat
	def setBestfileDat(self, bestfileDat):
		checkType("XSDataIntegrationSubWedgeResult", "setBestfileDat", bestfileDat, "XSDataString")
		self._bestfileDat = bestfileDat
	def delBestfileDat(self): self._bestfileDat = None
	# Properties
	bestfileDat = property(getBestfileDat, setBestfileDat, delBestfileDat, "Property for bestfileDat")
	def getBestfileHKL(self): return self._bestfileHKL
	def setBestfileHKL(self, bestfileHKL):
		checkType("XSDataIntegrationSubWedgeResult", "setBestfileHKL", bestfileHKL, "XSDataString")
		self._bestfileHKL = bestfileHKL
	def delBestfileHKL(self): self._bestfileHKL = None
	# Properties
	bestfileHKL = property(getBestfileHKL, setBestfileHKL, delBestfileHKL, "Property for bestfileHKL")
	def getBestfilePar(self): return self._bestfilePar
	def setBestfilePar(self, bestfilePar):
		checkType("XSDataIntegrationSubWedgeResult", "setBestfilePar", bestfilePar, "XSDataString")
		self._bestfilePar = bestfilePar
	def delBestfilePar(self): self._bestfilePar = None
	# Properties
	bestfilePar = property(getBestfilePar, setBestfilePar, delBestfilePar, "Property for bestfilePar")
	def getExperimentalConditionRefined(self): return self._experimentalConditionRefined
	def setExperimentalConditionRefined(self, experimentalConditionRefined):
		checkType("XSDataIntegrationSubWedgeResult", "setExperimentalConditionRefined", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
	def delExperimentalConditionRefined(self): self._experimentalConditionRefined = None
	# Properties
	experimentalConditionRefined = property(getExperimentalConditionRefined, setExperimentalConditionRefined, delExperimentalConditionRefined, "Property for experimentalConditionRefined")
	def getGeneratedMTZFile(self): return self._generatedMTZFile
	def setGeneratedMTZFile(self, generatedMTZFile):
		checkType("XSDataIntegrationSubWedgeResult", "setGeneratedMTZFile", generatedMTZFile, "XSDataFile")
		self._generatedMTZFile = generatedMTZFile
	def delGeneratedMTZFile(self): self._generatedMTZFile = None
	# Properties
	generatedMTZFile = property(getGeneratedMTZFile, setGeneratedMTZFile, delGeneratedMTZFile, "Property for generatedMTZFile")
	def getIntegrationLogFile(self): return self._integrationLogFile
	def setIntegrationLogFile(self, integrationLogFile):
		checkType("XSDataIntegrationSubWedgeResult", "setIntegrationLogFile", integrationLogFile, "XSDataFile")
		self._integrationLogFile = integrationLogFile
	def delIntegrationLogFile(self): self._integrationLogFile = None
	# Properties
	integrationLogFile = property(getIntegrationLogFile, setIntegrationLogFile, delIntegrationLogFile, "Property for integrationLogFile")
	def getStatistics(self): return self._statistics
	def setStatistics(self, statistics):
		checkType("XSDataIntegrationSubWedgeResult", "setStatistics", statistics, "XSDataStatisticsIntegration")
		self._statistics = statistics
	def delStatistics(self): self._statistics = None
	# Properties
	statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
	def getStatisticsPerResolutionBin(self): return self._statisticsPerResolutionBin
	def setStatisticsPerResolutionBin(self, statisticsPerResolutionBin):
		checkType("XSDataIntegrationSubWedgeResult", "setStatisticsPerResolutionBin", statisticsPerResolutionBin, "list")
		self._statisticsPerResolutionBin = statisticsPerResolutionBin
	def delStatisticsPerResolutionBin(self): self._statisticsPerResolutionBin = None
	# Properties
	statisticsPerResolutionBin = property(getStatisticsPerResolutionBin, setStatisticsPerResolutionBin, delStatisticsPerResolutionBin, "Property for statisticsPerResolutionBin")
	def addStatisticsPerResolutionBin(self, value):
		checkType("XSDataIntegrationSubWedgeResult", "setStatisticsPerResolutionBin", value, "XSDataStatisticsIntegrationPerResolutionBin")
		self._statisticsPerResolutionBin.append(value)
	def insertStatisticsPerResolutionBin(self, index, value):
		checkType("XSDataIntegrationSubWedgeResult", "setStatisticsPerResolutionBin", value, "XSDataStatisticsIntegrationPerResolutionBin")
		self._statisticsPerResolutionBin[index] = value
	def getSubWedgeNumber(self): return self._subWedgeNumber
	def setSubWedgeNumber(self, subWedgeNumber):
		checkType("XSDataIntegrationSubWedgeResult", "setSubWedgeNumber", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
	def delSubWedgeNumber(self): self._subWedgeNumber = None
	# Properties
	subWedgeNumber = property(getSubWedgeNumber, setSubWedgeNumber, delSubWedgeNumber, "Property for subWedgeNumber")
	def export(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._bestfileDat is not None:
			self.bestfileDat.export(outfile, level, name_='bestfileDat')
		else:
			warnEmptyAttribute("bestfileDat", "XSDataString")
		if self._bestfileHKL is not None:
			self.bestfileHKL.export(outfile, level, name_='bestfileHKL')
		else:
			warnEmptyAttribute("bestfileHKL", "XSDataString")
		if self._bestfilePar is not None:
			self.bestfilePar.export(outfile, level, name_='bestfilePar')
		else:
			warnEmptyAttribute("bestfilePar", "XSDataString")
		if self._experimentalConditionRefined is not None:
			self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
		else:
			warnEmptyAttribute("experimentalConditionRefined", "XSDataExperimentalCondition")
		if self._generatedMTZFile is not None:
			self.generatedMTZFile.export(outfile, level, name_='generatedMTZFile')
		else:
			warnEmptyAttribute("generatedMTZFile", "XSDataFile")
		if self._integrationLogFile is not None:
			self.integrationLogFile.export(outfile, level, name_='integrationLogFile')
		else:
			warnEmptyAttribute("integrationLogFile", "XSDataFile")
		if self._statistics is not None:
			self.statistics.export(outfile, level, name_='statistics')
		else:
			warnEmptyAttribute("statistics", "XSDataStatisticsIntegration")
		for statisticsPerResolutionBin_ in self.getStatisticsPerResolutionBin():
			statisticsPerResolutionBin_.export(outfile, level, name_='statisticsPerResolutionBin')
		if self.getStatisticsPerResolutionBin() == []:
			warnEmptyAttribute("statisticsPerResolutionBin", "XSDataStatisticsIntegrationPerResolutionBin")
		if self._subWedgeNumber is not None:
			self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
		else:
			warnEmptyAttribute("subWedgeNumber", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestfileDat':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestfileDat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestfileHKL':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestfileHKL(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestfilePar':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestfilePar(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalConditionRefined':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalConditionRefined(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'generatedMTZFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGeneratedMTZFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integrationLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegrationLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statistics':
			obj_ = XSDataStatisticsIntegration()
			obj_.build(child_)
			self.setStatistics(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statisticsPerResolutionBin':
			obj_ = XSDataStatisticsIntegrationPerResolutionBin()
			obj_.build(child_)
			self.statisticsPerResolutionBin.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedgeNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSubWedgeNumber(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIntegrationSubWedgeResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIntegrationSubWedgeResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIntegrationSubWedgeResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIntegrationSubWedgeResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationSubWedgeResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIntegrationSubWedgeResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationSubWedgeResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIntegrationSubWedgeResult

class XSDataLigand(XSData):
	"""A polymer ligand that contains a set of heavy atoms, the number of all the light atoms (weight <= Oxygen) and the number of copies of this particular ligand in the polymer."""
	def __init__(self, numberOfLightAtoms=None, numberOfCopies=None, heavyAtoms=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataLigand", "Constructor of XSDataLigand", heavyAtoms, "XSDataAtomicComposition")
		self._heavyAtoms = heavyAtoms
		checkType("XSDataLigand", "Constructor of XSDataLigand", numberOfCopies, "XSDataDouble")
		self._numberOfCopies = numberOfCopies
		checkType("XSDataLigand", "Constructor of XSDataLigand", numberOfLightAtoms, "XSDataDouble")
		self._numberOfLightAtoms = numberOfLightAtoms
	def getHeavyAtoms(self): return self._heavyAtoms
	def setHeavyAtoms(self, heavyAtoms):
		checkType("XSDataLigand", "setHeavyAtoms", heavyAtoms, "XSDataAtomicComposition")
		self._heavyAtoms = heavyAtoms
	def delHeavyAtoms(self): self._heavyAtoms = None
	# Properties
	heavyAtoms = property(getHeavyAtoms, setHeavyAtoms, delHeavyAtoms, "Property for heavyAtoms")
	def getNumberOfCopies(self): return self._numberOfCopies
	def setNumberOfCopies(self, numberOfCopies):
		checkType("XSDataLigand", "setNumberOfCopies", numberOfCopies, "XSDataDouble")
		self._numberOfCopies = numberOfCopies
	def delNumberOfCopies(self): self._numberOfCopies = None
	# Properties
	numberOfCopies = property(getNumberOfCopies, setNumberOfCopies, delNumberOfCopies, "Property for numberOfCopies")
	def getNumberOfLightAtoms(self): return self._numberOfLightAtoms
	def setNumberOfLightAtoms(self, numberOfLightAtoms):
		checkType("XSDataLigand", "setNumberOfLightAtoms", numberOfLightAtoms, "XSDataDouble")
		self._numberOfLightAtoms = numberOfLightAtoms
	def delNumberOfLightAtoms(self): self._numberOfLightAtoms = None
	# Properties
	numberOfLightAtoms = property(getNumberOfLightAtoms, setNumberOfLightAtoms, delNumberOfLightAtoms, "Property for numberOfLightAtoms")
	def export(self, outfile, level, name_='XSDataLigand'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataLigand'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._heavyAtoms is not None:
			self.heavyAtoms.export(outfile, level, name_='heavyAtoms')
		else:
			warnEmptyAttribute("heavyAtoms", "XSDataAtomicComposition")
		if self._numberOfCopies is not None:
			self.numberOfCopies.export(outfile, level, name_='numberOfCopies')
		else:
			warnEmptyAttribute("numberOfCopies", "XSDataDouble")
		if self._numberOfLightAtoms is not None:
			self.numberOfLightAtoms.export(outfile, level, name_='numberOfLightAtoms')
		else:
			warnEmptyAttribute("numberOfLightAtoms", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'heavyAtoms':
			obj_ = XSDataAtomicComposition()
			obj_.build(child_)
			self.setHeavyAtoms(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfCopies':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOfCopies(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfLightAtoms':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOfLightAtoms(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataLigand" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataLigand' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataLigand is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataLigand.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataLigand()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataLigand" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataLigand()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataLigand

class XSDataOrientation(XSData):
	def __init__(self, matrixU=None, matrixA=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataOrientation", "Constructor of XSDataOrientation", matrixA, "XSDataMatrixDouble")
		self._matrixA = matrixA
		checkType("XSDataOrientation", "Constructor of XSDataOrientation", matrixU, "XSDataMatrixDouble")
		self._matrixU = matrixU
	def getMatrixA(self): return self._matrixA
	def setMatrixA(self, matrixA):
		checkType("XSDataOrientation", "setMatrixA", matrixA, "XSDataMatrixDouble")
		self._matrixA = matrixA
	def delMatrixA(self): self._matrixA = None
	# Properties
	matrixA = property(getMatrixA, setMatrixA, delMatrixA, "Property for matrixA")
	def getMatrixU(self): return self._matrixU
	def setMatrixU(self, matrixU):
		checkType("XSDataOrientation", "setMatrixU", matrixU, "XSDataMatrixDouble")
		self._matrixU = matrixU
	def delMatrixU(self): self._matrixU = None
	# Properties
	matrixU = property(getMatrixU, setMatrixU, delMatrixU, "Property for matrixU")
	def export(self, outfile, level, name_='XSDataOrientation'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataOrientation'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._matrixA is not None:
			self.matrixA.export(outfile, level, name_='matrixA')
		else:
			warnEmptyAttribute("matrixA", "XSDataMatrixDouble")
		if self._matrixU is not None:
			self.matrixU.export(outfile, level, name_='matrixU')
		else:
			warnEmptyAttribute("matrixU", "XSDataMatrixDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'matrixA':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setMatrixA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'matrixU':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setMatrixU(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataOrientation" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataOrientation' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataOrientation is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataOrientation.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataOrientation()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataOrientation" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataOrientation()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataOrientation

class XSDataResolutionBin(XSData):
	def __init__(self, redundancy=None, rFriedel=None, rFactor=None, percentageOverload=None, minResolution=None, maxResolution=None, completeness=None, chi2=None, averageSigma=None, averageIntensityOverAverageSigma=None, averageIntensity=None, IOverSigmaChi=None, IOverSigma=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", IOverSigma, "XSDataDouble")
		self._IOverSigma = IOverSigma
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", IOverSigmaChi, "XSDataDouble")
		self._IOverSigmaChi = IOverSigmaChi
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", averageIntensityOverAverageSigma, "XSDataDouble")
		self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", chi2, "XSDataDouble")
		self._chi2 = chi2
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", minResolution, "XSDataDouble")
		self._minResolution = minResolution
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", percentageOverload, "XSDataDouble")
		self._percentageOverload = percentageOverload
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", rFactor, "XSDataDouble")
		self._rFactor = rFactor
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", rFriedel, "XSDataDouble")
		self._rFriedel = rFriedel
		checkType("XSDataResolutionBin", "Constructor of XSDataResolutionBin", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def getIOverSigma(self): return self._IOverSigma
	def setIOverSigma(self, IOverSigma):
		checkType("XSDataResolutionBin", "setIOverSigma", IOverSigma, "XSDataDouble")
		self._IOverSigma = IOverSigma
	def delIOverSigma(self): self._IOverSigma = None
	# Properties
	IOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for IOverSigma")
	def getIOverSigmaChi(self): return self._IOverSigmaChi
	def setIOverSigmaChi(self, IOverSigmaChi):
		checkType("XSDataResolutionBin", "setIOverSigmaChi", IOverSigmaChi, "XSDataDouble")
		self._IOverSigmaChi = IOverSigmaChi
	def delIOverSigmaChi(self): self._IOverSigmaChi = None
	# Properties
	IOverSigmaChi = property(getIOverSigmaChi, setIOverSigmaChi, delIOverSigmaChi, "Property for IOverSigmaChi")
	def getAverageIntensity(self): return self._averageIntensity
	def setAverageIntensity(self, averageIntensity):
		checkType("XSDataResolutionBin", "setAverageIntensity", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
	def delAverageIntensity(self): self._averageIntensity = None
	# Properties
	averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
	def getAverageIntensityOverAverageSigma(self): return self._averageIntensityOverAverageSigma
	def setAverageIntensityOverAverageSigma(self, averageIntensityOverAverageSigma):
		checkType("XSDataResolutionBin", "setAverageIntensityOverAverageSigma", averageIntensityOverAverageSigma, "XSDataDouble")
		self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
	def delAverageIntensityOverAverageSigma(self): self._averageIntensityOverAverageSigma = None
	# Properties
	averageIntensityOverAverageSigma = property(getAverageIntensityOverAverageSigma, setAverageIntensityOverAverageSigma, delAverageIntensityOverAverageSigma, "Property for averageIntensityOverAverageSigma")
	def getAverageSigma(self): return self._averageSigma
	def setAverageSigma(self, averageSigma):
		checkType("XSDataResolutionBin", "setAverageSigma", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
	def delAverageSigma(self): self._averageSigma = None
	# Properties
	averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
	def getChi2(self): return self._chi2
	def setChi2(self, chi2):
		checkType("XSDataResolutionBin", "setChi2", chi2, "XSDataDouble")
		self._chi2 = chi2
	def delChi2(self): self._chi2 = None
	# Properties
	chi2 = property(getChi2, setChi2, delChi2, "Property for chi2")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataResolutionBin", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMaxResolution(self): return self._maxResolution
	def setMaxResolution(self, maxResolution):
		checkType("XSDataResolutionBin", "setMaxResolution", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
	def delMaxResolution(self): self._maxResolution = None
	# Properties
	maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
	def getMinResolution(self): return self._minResolution
	def setMinResolution(self, minResolution):
		checkType("XSDataResolutionBin", "setMinResolution", minResolution, "XSDataDouble")
		self._minResolution = minResolution
	def delMinResolution(self): self._minResolution = None
	# Properties
	minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
	def getPercentageOverload(self): return self._percentageOverload
	def setPercentageOverload(self, percentageOverload):
		checkType("XSDataResolutionBin", "setPercentageOverload", percentageOverload, "XSDataDouble")
		self._percentageOverload = percentageOverload
	def delPercentageOverload(self): self._percentageOverload = None
	# Properties
	percentageOverload = property(getPercentageOverload, setPercentageOverload, delPercentageOverload, "Property for percentageOverload")
	def getRFactor(self): return self._rFactor
	def setRFactor(self, rFactor):
		checkType("XSDataResolutionBin", "setRFactor", rFactor, "XSDataDouble")
		self._rFactor = rFactor
	def delRFactor(self): self._rFactor = None
	# Properties
	rFactor = property(getRFactor, setRFactor, delRFactor, "Property for rFactor")
	def getRFriedel(self): return self._rFriedel
	def setRFriedel(self, rFriedel):
		checkType("XSDataResolutionBin", "setRFriedel", rFriedel, "XSDataDouble")
		self._rFriedel = rFriedel
	def delRFriedel(self): self._rFriedel = None
	# Properties
	rFriedel = property(getRFriedel, setRFriedel, delRFriedel, "Property for rFriedel")
	def getRedundancy(self): return self._redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataResolutionBin", "setRedundancy", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def delRedundancy(self): self._redundancy = None
	# Properties
	redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
	def export(self, outfile, level, name_='XSDataResolutionBin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResolutionBin'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._IOverSigma is not None:
			self.IOverSigma.export(outfile, level, name_='IOverSigma')
		else:
			warnEmptyAttribute("IOverSigma", "XSDataDouble")
		if self._IOverSigmaChi is not None:
			self.IOverSigmaChi.export(outfile, level, name_='IOverSigmaChi')
		if self._averageIntensity is not None:
			self.averageIntensity.export(outfile, level, name_='averageIntensity')
		else:
			warnEmptyAttribute("averageIntensity", "XSDataDouble")
		if self._averageIntensityOverAverageSigma is not None:
			self.averageIntensityOverAverageSigma.export(outfile, level, name_='averageIntensityOverAverageSigma')
		if self._averageSigma is not None:
			self.averageSigma.export(outfile, level, name_='averageSigma')
		else:
			warnEmptyAttribute("averageSigma", "XSDataDouble")
		if self._chi2 is not None:
			self.chi2.export(outfile, level, name_='chi2')
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self._maxResolution is not None:
			self.maxResolution.export(outfile, level, name_='maxResolution')
		else:
			warnEmptyAttribute("maxResolution", "XSDataDouble")
		if self._minResolution is not None:
			self.minResolution.export(outfile, level, name_='minResolution')
		else:
			warnEmptyAttribute("minResolution", "XSDataDouble")
		if self._percentageOverload is not None:
			self.percentageOverload.export(outfile, level, name_='percentageOverload')
		else:
			warnEmptyAttribute("percentageOverload", "XSDataDouble")
		if self._rFactor is not None:
			self.rFactor.export(outfile, level, name_='rFactor')
		else:
			warnEmptyAttribute("rFactor", "XSDataDouble")
		if self._rFriedel is not None:
			self.rFriedel.export(outfile, level, name_='rFriedel')
		if self._redundancy is not None:
			self.redundancy.export(outfile, level, name_='redundancy')
		else:
			warnEmptyAttribute("redundancy", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'IOverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'IOverSigmaChi':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigmaChi(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIntensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIntensityOverAverageSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIntensityOverAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chi2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setChi2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'percentageOverload':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPercentageOverload(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rFriedel':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRFriedel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'redundancy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRedundancy(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResolutionBin" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResolutionBin' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResolutionBin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResolutionBin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResolutionBin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResolutionBin" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResolutionBin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResolutionBin

class XSDataSample(XSData):
	"""This defines the main properties of a sample:
- absorbed dose rate in Gray/sec
- shape: the factor that is related to the sample and the beam size (1 if crystal smaller than beam size or = to the ratio of crystal size to the beam size if the beam is smaller then crystal).
- sample size
- the susceptibility of the sample to radiation damage."""
	def __init__(self, susceptibility=None, size=None, shape=None, absorbedDoseRate=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataSample", "Constructor of XSDataSample", absorbedDoseRate, "XSDataAbsorbedDoseRate")
		self._absorbedDoseRate = absorbedDoseRate
		checkType("XSDataSample", "Constructor of XSDataSample", shape, "XSDataDouble")
		self._shape = shape
		checkType("XSDataSample", "Constructor of XSDataSample", size, "XSDataSize")
		self._size = size
		checkType("XSDataSample", "Constructor of XSDataSample", susceptibility, "XSDataDouble")
		self._susceptibility = susceptibility
	def getAbsorbedDoseRate(self): return self._absorbedDoseRate
	def setAbsorbedDoseRate(self, absorbedDoseRate):
		checkType("XSDataSample", "setAbsorbedDoseRate", absorbedDoseRate, "XSDataAbsorbedDoseRate")
		self._absorbedDoseRate = absorbedDoseRate
	def delAbsorbedDoseRate(self): self._absorbedDoseRate = None
	# Properties
	absorbedDoseRate = property(getAbsorbedDoseRate, setAbsorbedDoseRate, delAbsorbedDoseRate, "Property for absorbedDoseRate")
	def getShape(self): return self._shape
	def setShape(self, shape):
		checkType("XSDataSample", "setShape", shape, "XSDataDouble")
		self._shape = shape
	def delShape(self): self._shape = None
	# Properties
	shape = property(getShape, setShape, delShape, "Property for shape")
	def getSize(self): return self._size
	def setSize(self, size):
		checkType("XSDataSample", "setSize", size, "XSDataSize")
		self._size = size
	def delSize(self): self._size = None
	# Properties
	size = property(getSize, setSize, delSize, "Property for size")
	def getSusceptibility(self): return self._susceptibility
	def setSusceptibility(self, susceptibility):
		checkType("XSDataSample", "setSusceptibility", susceptibility, "XSDataDouble")
		self._susceptibility = susceptibility
	def delSusceptibility(self): self._susceptibility = None
	# Properties
	susceptibility = property(getSusceptibility, setSusceptibility, delSusceptibility, "Property for susceptibility")
	def export(self, outfile, level, name_='XSDataSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSample'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._absorbedDoseRate is not None:
			self.absorbedDoseRate.export(outfile, level, name_='absorbedDoseRate')
		if self._shape is not None:
			self.shape.export(outfile, level, name_='shape')
		if self._size is not None:
			self.size.export(outfile, level, name_='size')
		if self._susceptibility is not None:
			self.susceptibility.export(outfile, level, name_='susceptibility')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absorbedDoseRate':
			obj_ = XSDataAbsorbedDoseRate()
			obj_.build(child_)
			self.setAbsorbedDoseRate(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'shape':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setShape(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'size':
			obj_ = XSDataSize()
			obj_.build(child_)
			self.setSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'susceptibility':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSusceptibility(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSample' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSample is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSample

class XSDataSolvent(XSData):
	"""Defines the content of the solvent by defining the concentration of elements in millimoles/litre. Note that this atom composition should not include oxygen and lighter atoms."""
	def __init__(self, atoms=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataSolvent", "Constructor of XSDataSolvent", atoms, "XSDataAtomicComposition")
		self._atoms = atoms
	def getAtoms(self): return self._atoms
	def setAtoms(self, atoms):
		checkType("XSDataSolvent", "setAtoms", atoms, "XSDataAtomicComposition")
		self._atoms = atoms
	def delAtoms(self): self._atoms = None
	# Properties
	atoms = property(getAtoms, setAtoms, delAtoms, "Property for atoms")
	def export(self, outfile, level, name_='XSDataSolvent'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSolvent'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._atoms is not None:
			self.atoms.export(outfile, level, name_='atoms')
		else:
			warnEmptyAttribute("atoms", "XSDataAtomicComposition")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'atoms':
			obj_ = XSDataAtomicComposition()
			obj_.build(child_)
			self.setAtoms(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSolvent" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSolvent' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSolvent is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSolvent.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSolvent()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSolvent" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSolvent()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSolvent

class XSDataSpaceGroup(XSData):
	"""Crystallographic properties"""
	def __init__(self, name=None, ITNumber=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataSpaceGroup", "Constructor of XSDataSpaceGroup", ITNumber, "XSDataInteger")
		self._ITNumber = ITNumber
		checkType("XSDataSpaceGroup", "Constructor of XSDataSpaceGroup", name, "XSDataString")
		self._name = name
	def getITNumber(self): return self._ITNumber
	def setITNumber(self, ITNumber):
		checkType("XSDataSpaceGroup", "setITNumber", ITNumber, "XSDataInteger")
		self._ITNumber = ITNumber
	def delITNumber(self): self._ITNumber = None
	# Properties
	ITNumber = property(getITNumber, setITNumber, delITNumber, "Property for ITNumber")
	def getName(self): return self._name
	def setName(self, name):
		checkType("XSDataSpaceGroup", "setName", name, "XSDataString")
		self._name = name
	def delName(self): self._name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def export(self, outfile, level, name_='XSDataSpaceGroup'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSpaceGroup'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._ITNumber is not None:
			self.ITNumber.export(outfile, level, name_='ITNumber')
		if self._name is not None:
			self.name.export(outfile, level, name_='name')
		else:
			warnEmptyAttribute("name", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ITNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setITNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSpaceGroup" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSpaceGroup' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSpaceGroup is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSpaceGroup.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSpaceGroup()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSpaceGroup" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSpaceGroup()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSpaceGroup

class XSDataStatisticsIndexing(XSData):
	def __init__(self, spotsUsed=None, spotsTotal=None, spotDeviationPositional=None, spotDeviationAngular=None, beamPositionShiftY=None, beamPositionShiftX=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", beamPositionShiftX, "XSDataLength")
		self._beamPositionShiftX = beamPositionShiftX
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", beamPositionShiftY, "XSDataLength")
		self._beamPositionShiftY = beamPositionShiftY
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", spotDeviationAngular, "XSDataAngle")
		self._spotDeviationAngular = spotDeviationAngular
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", spotDeviationPositional, "XSDataLength")
		self._spotDeviationPositional = spotDeviationPositional
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", spotsTotal, "XSDataInteger")
		self._spotsTotal = spotsTotal
		checkType("XSDataStatisticsIndexing", "Constructor of XSDataStatisticsIndexing", spotsUsed, "XSDataInteger")
		self._spotsUsed = spotsUsed
	def getBeamPositionShiftX(self): return self._beamPositionShiftX
	def setBeamPositionShiftX(self, beamPositionShiftX):
		checkType("XSDataStatisticsIndexing", "setBeamPositionShiftX", beamPositionShiftX, "XSDataLength")
		self._beamPositionShiftX = beamPositionShiftX
	def delBeamPositionShiftX(self): self._beamPositionShiftX = None
	# Properties
	beamPositionShiftX = property(getBeamPositionShiftX, setBeamPositionShiftX, delBeamPositionShiftX, "Property for beamPositionShiftX")
	def getBeamPositionShiftY(self): return self._beamPositionShiftY
	def setBeamPositionShiftY(self, beamPositionShiftY):
		checkType("XSDataStatisticsIndexing", "setBeamPositionShiftY", beamPositionShiftY, "XSDataLength")
		self._beamPositionShiftY = beamPositionShiftY
	def delBeamPositionShiftY(self): self._beamPositionShiftY = None
	# Properties
	beamPositionShiftY = property(getBeamPositionShiftY, setBeamPositionShiftY, delBeamPositionShiftY, "Property for beamPositionShiftY")
	def getSpotDeviationAngular(self): return self._spotDeviationAngular
	def setSpotDeviationAngular(self, spotDeviationAngular):
		checkType("XSDataStatisticsIndexing", "setSpotDeviationAngular", spotDeviationAngular, "XSDataAngle")
		self._spotDeviationAngular = spotDeviationAngular
	def delSpotDeviationAngular(self): self._spotDeviationAngular = None
	# Properties
	spotDeviationAngular = property(getSpotDeviationAngular, setSpotDeviationAngular, delSpotDeviationAngular, "Property for spotDeviationAngular")
	def getSpotDeviationPositional(self): return self._spotDeviationPositional
	def setSpotDeviationPositional(self, spotDeviationPositional):
		checkType("XSDataStatisticsIndexing", "setSpotDeviationPositional", spotDeviationPositional, "XSDataLength")
		self._spotDeviationPositional = spotDeviationPositional
	def delSpotDeviationPositional(self): self._spotDeviationPositional = None
	# Properties
	spotDeviationPositional = property(getSpotDeviationPositional, setSpotDeviationPositional, delSpotDeviationPositional, "Property for spotDeviationPositional")
	def getSpotsTotal(self): return self._spotsTotal
	def setSpotsTotal(self, spotsTotal):
		checkType("XSDataStatisticsIndexing", "setSpotsTotal", spotsTotal, "XSDataInteger")
		self._spotsTotal = spotsTotal
	def delSpotsTotal(self): self._spotsTotal = None
	# Properties
	spotsTotal = property(getSpotsTotal, setSpotsTotal, delSpotsTotal, "Property for spotsTotal")
	def getSpotsUsed(self): return self._spotsUsed
	def setSpotsUsed(self, spotsUsed):
		checkType("XSDataStatisticsIndexing", "setSpotsUsed", spotsUsed, "XSDataInteger")
		self._spotsUsed = spotsUsed
	def delSpotsUsed(self): self._spotsUsed = None
	# Properties
	spotsUsed = property(getSpotsUsed, setSpotsUsed, delSpotsUsed, "Property for spotsUsed")
	def export(self, outfile, level, name_='XSDataStatisticsIndexing'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsIndexing'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._beamPositionShiftX is not None:
			self.beamPositionShiftX.export(outfile, level, name_='beamPositionShiftX')
		else:
			warnEmptyAttribute("beamPositionShiftX", "XSDataLength")
		if self._beamPositionShiftY is not None:
			self.beamPositionShiftY.export(outfile, level, name_='beamPositionShiftY')
		else:
			warnEmptyAttribute("beamPositionShiftY", "XSDataLength")
		if self._spotDeviationAngular is not None:
			self.spotDeviationAngular.export(outfile, level, name_='spotDeviationAngular')
		else:
			warnEmptyAttribute("spotDeviationAngular", "XSDataAngle")
		if self._spotDeviationPositional is not None:
			self.spotDeviationPositional.export(outfile, level, name_='spotDeviationPositional')
		else:
			warnEmptyAttribute("spotDeviationPositional", "XSDataLength")
		if self._spotsTotal is not None:
			self.spotsTotal.export(outfile, level, name_='spotsTotal')
		else:
			warnEmptyAttribute("spotsTotal", "XSDataInteger")
		if self._spotsUsed is not None:
			self.spotsUsed.export(outfile, level, name_='spotsUsed')
		else:
			warnEmptyAttribute("spotsUsed", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPositionShiftX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamPositionShiftX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPositionShiftY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamPositionShiftY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationAngular':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setSpotDeviationAngular(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationPositional':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setSpotDeviationPositional(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotsTotal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpotsTotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotsUsed':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpotsUsed(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsIndexing" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsIndexing' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsIndexing is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsIndexing.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIndexing()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsIndexing" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIndexing()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsIndexing

class XSDataStatisticsIntegration(XSData):
	def __init__(self, numberOfReflectionsGenerated=None, numberOfPartialReflections=None, numberOfOverlappedReflections=None, numberOfNegativeReflections=None, numberOfFullyRecordedReflections=None, numberOfBadReflections=None, iOverSigmaOverall=None, iOverSigmaAtHighestResolution=None, RMSSpotDeviation=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", RMSSpotDeviation, "XSDataLength")
		self._RMSSpotDeviation = RMSSpotDeviation
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", iOverSigmaAtHighestResolution, "XSDataDouble")
		self._iOverSigmaAtHighestResolution = iOverSigmaAtHighestResolution
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", iOverSigmaOverall, "XSDataDouble")
		self._iOverSigmaOverall = iOverSigmaOverall
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfBadReflections, "XSDataInteger")
		self._numberOfBadReflections = numberOfBadReflections
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfFullyRecordedReflections, "XSDataInteger")
		self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfNegativeReflections, "XSDataInteger")
		self._numberOfNegativeReflections = numberOfNegativeReflections
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfOverlappedReflections, "XSDataInteger")
		self._numberOfOverlappedReflections = numberOfOverlappedReflections
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfPartialReflections, "XSDataInteger")
		self._numberOfPartialReflections = numberOfPartialReflections
		checkType("XSDataStatisticsIntegration", "Constructor of XSDataStatisticsIntegration", numberOfReflectionsGenerated, "XSDataInteger")
		self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
	def getRMSSpotDeviation(self): return self._RMSSpotDeviation
	def setRMSSpotDeviation(self, RMSSpotDeviation):
		checkType("XSDataStatisticsIntegration", "setRMSSpotDeviation", RMSSpotDeviation, "XSDataLength")
		self._RMSSpotDeviation = RMSSpotDeviation
	def delRMSSpotDeviation(self): self._RMSSpotDeviation = None
	# Properties
	RMSSpotDeviation = property(getRMSSpotDeviation, setRMSSpotDeviation, delRMSSpotDeviation, "Property for RMSSpotDeviation")
	def getIOverSigmaAtHighestResolution(self): return self._iOverSigmaAtHighestResolution
	def setIOverSigmaAtHighestResolution(self, iOverSigmaAtHighestResolution):
		checkType("XSDataStatisticsIntegration", "setIOverSigmaAtHighestResolution", iOverSigmaAtHighestResolution, "XSDataDouble")
		self._iOverSigmaAtHighestResolution = iOverSigmaAtHighestResolution
	def delIOverSigmaAtHighestResolution(self): self._iOverSigmaAtHighestResolution = None
	# Properties
	iOverSigmaAtHighestResolution = property(getIOverSigmaAtHighestResolution, setIOverSigmaAtHighestResolution, delIOverSigmaAtHighestResolution, "Property for iOverSigmaAtHighestResolution")
	def getIOverSigmaOverall(self): return self._iOverSigmaOverall
	def setIOverSigmaOverall(self, iOverSigmaOverall):
		checkType("XSDataStatisticsIntegration", "setIOverSigmaOverall", iOverSigmaOverall, "XSDataDouble")
		self._iOverSigmaOverall = iOverSigmaOverall
	def delIOverSigmaOverall(self): self._iOverSigmaOverall = None
	# Properties
	iOverSigmaOverall = property(getIOverSigmaOverall, setIOverSigmaOverall, delIOverSigmaOverall, "Property for iOverSigmaOverall")
	def getNumberOfBadReflections(self): return self._numberOfBadReflections
	def setNumberOfBadReflections(self, numberOfBadReflections):
		checkType("XSDataStatisticsIntegration", "setNumberOfBadReflections", numberOfBadReflections, "XSDataInteger")
		self._numberOfBadReflections = numberOfBadReflections
	def delNumberOfBadReflections(self): self._numberOfBadReflections = None
	# Properties
	numberOfBadReflections = property(getNumberOfBadReflections, setNumberOfBadReflections, delNumberOfBadReflections, "Property for numberOfBadReflections")
	def getNumberOfFullyRecordedReflections(self): return self._numberOfFullyRecordedReflections
	def setNumberOfFullyRecordedReflections(self, numberOfFullyRecordedReflections):
		checkType("XSDataStatisticsIntegration", "setNumberOfFullyRecordedReflections", numberOfFullyRecordedReflections, "XSDataInteger")
		self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
	def delNumberOfFullyRecordedReflections(self): self._numberOfFullyRecordedReflections = None
	# Properties
	numberOfFullyRecordedReflections = property(getNumberOfFullyRecordedReflections, setNumberOfFullyRecordedReflections, delNumberOfFullyRecordedReflections, "Property for numberOfFullyRecordedReflections")
	def getNumberOfNegativeReflections(self): return self._numberOfNegativeReflections
	def setNumberOfNegativeReflections(self, numberOfNegativeReflections):
		checkType("XSDataStatisticsIntegration", "setNumberOfNegativeReflections", numberOfNegativeReflections, "XSDataInteger")
		self._numberOfNegativeReflections = numberOfNegativeReflections
	def delNumberOfNegativeReflections(self): self._numberOfNegativeReflections = None
	# Properties
	numberOfNegativeReflections = property(getNumberOfNegativeReflections, setNumberOfNegativeReflections, delNumberOfNegativeReflections, "Property for numberOfNegativeReflections")
	def getNumberOfOverlappedReflections(self): return self._numberOfOverlappedReflections
	def setNumberOfOverlappedReflections(self, numberOfOverlappedReflections):
		checkType("XSDataStatisticsIntegration", "setNumberOfOverlappedReflections", numberOfOverlappedReflections, "XSDataInteger")
		self._numberOfOverlappedReflections = numberOfOverlappedReflections
	def delNumberOfOverlappedReflections(self): self._numberOfOverlappedReflections = None
	# Properties
	numberOfOverlappedReflections = property(getNumberOfOverlappedReflections, setNumberOfOverlappedReflections, delNumberOfOverlappedReflections, "Property for numberOfOverlappedReflections")
	def getNumberOfPartialReflections(self): return self._numberOfPartialReflections
	def setNumberOfPartialReflections(self, numberOfPartialReflections):
		checkType("XSDataStatisticsIntegration", "setNumberOfPartialReflections", numberOfPartialReflections, "XSDataInteger")
		self._numberOfPartialReflections = numberOfPartialReflections
	def delNumberOfPartialReflections(self): self._numberOfPartialReflections = None
	# Properties
	numberOfPartialReflections = property(getNumberOfPartialReflections, setNumberOfPartialReflections, delNumberOfPartialReflections, "Property for numberOfPartialReflections")
	def getNumberOfReflectionsGenerated(self): return self._numberOfReflectionsGenerated
	def setNumberOfReflectionsGenerated(self, numberOfReflectionsGenerated):
		checkType("XSDataStatisticsIntegration", "setNumberOfReflectionsGenerated", numberOfReflectionsGenerated, "XSDataInteger")
		self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
	def delNumberOfReflectionsGenerated(self): self._numberOfReflectionsGenerated = None
	# Properties
	numberOfReflectionsGenerated = property(getNumberOfReflectionsGenerated, setNumberOfReflectionsGenerated, delNumberOfReflectionsGenerated, "Property for numberOfReflectionsGenerated")
	def export(self, outfile, level, name_='XSDataStatisticsIntegration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegration'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._RMSSpotDeviation is not None:
			self.RMSSpotDeviation.export(outfile, level, name_='RMSSpotDeviation')
		else:
			warnEmptyAttribute("RMSSpotDeviation", "XSDataLength")
		if self._iOverSigmaAtHighestResolution is not None:
			self.iOverSigmaAtHighestResolution.export(outfile, level, name_='iOverSigmaAtHighestResolution')
		else:
			warnEmptyAttribute("iOverSigmaAtHighestResolution", "XSDataDouble")
		if self._iOverSigmaOverall is not None:
			self.iOverSigmaOverall.export(outfile, level, name_='iOverSigmaOverall')
		else:
			warnEmptyAttribute("iOverSigmaOverall", "XSDataDouble")
		if self._numberOfBadReflections is not None:
			self.numberOfBadReflections.export(outfile, level, name_='numberOfBadReflections')
		else:
			warnEmptyAttribute("numberOfBadReflections", "XSDataInteger")
		if self._numberOfFullyRecordedReflections is not None:
			self.numberOfFullyRecordedReflections.export(outfile, level, name_='numberOfFullyRecordedReflections')
		else:
			warnEmptyAttribute("numberOfFullyRecordedReflections", "XSDataInteger")
		if self._numberOfNegativeReflections is not None:
			self.numberOfNegativeReflections.export(outfile, level, name_='numberOfNegativeReflections')
		else:
			warnEmptyAttribute("numberOfNegativeReflections", "XSDataInteger")
		if self._numberOfOverlappedReflections is not None:
			self.numberOfOverlappedReflections.export(outfile, level, name_='numberOfOverlappedReflections')
		else:
			warnEmptyAttribute("numberOfOverlappedReflections", "XSDataInteger")
		if self._numberOfPartialReflections is not None:
			self.numberOfPartialReflections.export(outfile, level, name_='numberOfPartialReflections')
		else:
			warnEmptyAttribute("numberOfPartialReflections", "XSDataInteger")
		if self._numberOfReflectionsGenerated is not None:
			self.numberOfReflectionsGenerated.export(outfile, level, name_='numberOfReflectionsGenerated')
		else:
			warnEmptyAttribute("numberOfReflectionsGenerated", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'RMSSpotDeviation':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRMSSpotDeviation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iOverSigmaAtHighestResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigmaAtHighestResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iOverSigmaOverall':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigmaOverall(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfBadReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfBadReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfFullyRecordedReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfFullyRecordedReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfNegativeReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfNegativeReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfOverlappedReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfOverlappedReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfPartialReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfPartialReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfReflectionsGenerated':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfReflectionsGenerated(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsIntegration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsIntegration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsIntegration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsIntegration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsIntegration

class XSDataStatisticsIntegrationPerReflectionType(XSData):
	def __init__(self, partials=None, fullyRecorded=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataStatisticsIntegrationPerReflectionType", "Constructor of XSDataStatisticsIntegrationPerReflectionType", fullyRecorded, "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
		self._fullyRecorded = fullyRecorded
		checkType("XSDataStatisticsIntegrationPerReflectionType", "Constructor of XSDataStatisticsIntegrationPerReflectionType", partials, "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
		self._partials = partials
	def getFullyRecorded(self): return self._fullyRecorded
	def setFullyRecorded(self, fullyRecorded):
		checkType("XSDataStatisticsIntegrationPerReflectionType", "setFullyRecorded", fullyRecorded, "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
		self._fullyRecorded = fullyRecorded
	def delFullyRecorded(self): self._fullyRecorded = None
	# Properties
	fullyRecorded = property(getFullyRecorded, setFullyRecorded, delFullyRecorded, "Property for fullyRecorded")
	def getPartials(self): return self._partials
	def setPartials(self, partials):
		checkType("XSDataStatisticsIntegrationPerReflectionType", "setPartials", partials, "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
		self._partials = partials
	def delPartials(self): self._partials = None
	# Properties
	partials = property(getPartials, setPartials, delPartials, "Property for partials")
	def export(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._fullyRecorded is not None:
			self.fullyRecorded.export(outfile, level, name_='fullyRecorded')
		else:
			warnEmptyAttribute("fullyRecorded", "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
		if self._partials is not None:
			self.partials.export(outfile, level, name_='partials')
		else:
			warnEmptyAttribute("partials", "XSDataStatisticsIntegrationAverageAndNumberOfReflections")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fullyRecorded':
			obj_ = XSDataStatisticsIntegrationAverageAndNumberOfReflections()
			obj_.build(child_)
			self.setFullyRecorded(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'partials':
			obj_ = XSDataStatisticsIntegrationAverageAndNumberOfReflections()
			obj_.build(child_)
			self.setPartials(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerReflectionType" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsIntegrationPerReflectionType' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsIntegrationPerReflectionType is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsIntegrationPerReflectionType.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationPerReflectionType()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerReflectionType" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationPerReflectionType()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsIntegrationPerReflectionType

class XSDataStatisticsIntegrationPerResolutionBin(XSData):
	def __init__(self, summation=None, profileFitted=None, minResolution=None, maxResolution=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "Constructor of XSDataStatisticsIntegrationPerResolutionBin", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "Constructor of XSDataStatisticsIntegrationPerResolutionBin", minResolution, "XSDataDouble")
		self._minResolution = minResolution
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "Constructor of XSDataStatisticsIntegrationPerResolutionBin", profileFitted, "XSDataStatisticsIntegrationPerReflectionType")
		self._profileFitted = profileFitted
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "Constructor of XSDataStatisticsIntegrationPerResolutionBin", summation, "XSDataStatisticsIntegrationPerReflectionType")
		self._summation = summation
	def getMaxResolution(self): return self._maxResolution
	def setMaxResolution(self, maxResolution):
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "setMaxResolution", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
	def delMaxResolution(self): self._maxResolution = None
	# Properties
	maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
	def getMinResolution(self): return self._minResolution
	def setMinResolution(self, minResolution):
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "setMinResolution", minResolution, "XSDataDouble")
		self._minResolution = minResolution
	def delMinResolution(self): self._minResolution = None
	# Properties
	minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
	def getProfileFitted(self): return self._profileFitted
	def setProfileFitted(self, profileFitted):
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "setProfileFitted", profileFitted, "XSDataStatisticsIntegrationPerReflectionType")
		self._profileFitted = profileFitted
	def delProfileFitted(self): self._profileFitted = None
	# Properties
	profileFitted = property(getProfileFitted, setProfileFitted, delProfileFitted, "Property for profileFitted")
	def getSummation(self): return self._summation
	def setSummation(self, summation):
		checkType("XSDataStatisticsIntegrationPerResolutionBin", "setSummation", summation, "XSDataStatisticsIntegrationPerReflectionType")
		self._summation = summation
	def delSummation(self): self._summation = None
	# Properties
	summation = property(getSummation, setSummation, delSummation, "Property for summation")
	def export(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._maxResolution is not None:
			self.maxResolution.export(outfile, level, name_='maxResolution')
		else:
			warnEmptyAttribute("maxResolution", "XSDataDouble")
		if self._minResolution is not None:
			self.minResolution.export(outfile, level, name_='minResolution')
		else:
			warnEmptyAttribute("minResolution", "XSDataDouble")
		if self._profileFitted is not None:
			self.profileFitted.export(outfile, level, name_='profileFitted')
		else:
			warnEmptyAttribute("profileFitted", "XSDataStatisticsIntegrationPerReflectionType")
		if self._summation is not None:
			self.summation.export(outfile, level, name_='summation')
		else:
			warnEmptyAttribute("summation", "XSDataStatisticsIntegrationPerReflectionType")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'profileFitted':
			obj_ = XSDataStatisticsIntegrationPerReflectionType()
			obj_.build(child_)
			self.setProfileFitted(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'summation':
			obj_ = XSDataStatisticsIntegrationPerReflectionType()
			obj_.build(child_)
			self.setSummation(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerResolutionBin" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsIntegrationPerResolutionBin' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsIntegrationPerResolutionBin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsIntegrationPerResolutionBin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationPerResolutionBin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerResolutionBin" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsIntegrationPerResolutionBin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsIntegrationPerResolutionBin

class XSDataStatisticsStrategy(XSData):
	def __init__(self, resolutionBin=None):
		XSData.__init__(self, )
	
	
		if resolutionBin is None:
			self._resolutionBin = []
		else:
			checkType("XSDataStatisticsStrategy", "Constructor of XSDataStatisticsStrategy", resolutionBin, "list")
			self._resolutionBin = resolutionBin
	def getResolutionBin(self): return self._resolutionBin
	def setResolutionBin(self, resolutionBin):
		checkType("XSDataStatisticsStrategy", "setResolutionBin", resolutionBin, "list")
		self._resolutionBin = resolutionBin
	def delResolutionBin(self): self._resolutionBin = None
	# Properties
	resolutionBin = property(getResolutionBin, setResolutionBin, delResolutionBin, "Property for resolutionBin")
	def addResolutionBin(self, value):
		checkType("XSDataStatisticsStrategy", "setResolutionBin", value, "XSDataResolutionBin")
		self._resolutionBin.append(value)
	def insertResolutionBin(self, index, value):
		checkType("XSDataStatisticsStrategy", "setResolutionBin", value, "XSDataResolutionBin")
		self._resolutionBin[index] = value
	def export(self, outfile, level, name_='XSDataStatisticsStrategy'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStatisticsStrategy'):
		XSData.exportChildren(self, outfile, level, name_)
		for resolutionBin_ in self.getResolutionBin():
			resolutionBin_.export(outfile, level, name_='resolutionBin')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionBin':
			obj_ = XSDataResolutionBin()
			obj_.build(child_)
			self.resolutionBin.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStatisticsStrategy" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStatisticsStrategy' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStatisticsStrategy is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStatisticsStrategy.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsStrategy()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStatisticsStrategy" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStatisticsStrategy()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStatisticsStrategy

class XSDataStrategySummary(XSData):
	"""OBS! The attribute "attenuation" in XSDataStrategySummary is deprecated, see bug #379. Please use instead "transmission" in XSDataBeam."""
	def __init__(self, totalExposureTime=None, totalDataCollectionTime=None, resolutionReasoning=None, resolution=None, redundancy=None, rankingResolution=None, iSigma=None, completeness=None, attenuation=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", attenuation, "XSDataDouble")
		self._attenuation = attenuation
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", iSigma, "XSDataDouble")
		self._iSigma = iSigma
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", redundancy, "XSDataDouble")
		self._redundancy = redundancy
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", resolution, "XSDataDouble")
		self._resolution = resolution
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", resolutionReasoning, "XSDataString")
		self._resolutionReasoning = resolutionReasoning
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", totalDataCollectionTime, "XSDataTime")
		self._totalDataCollectionTime = totalDataCollectionTime
		checkType("XSDataStrategySummary", "Constructor of XSDataStrategySummary", totalExposureTime, "XSDataTime")
		self._totalExposureTime = totalExposureTime
	def getAttenuation(self): return self._attenuation
	def setAttenuation(self, attenuation):
		checkType("XSDataStrategySummary", "setAttenuation", attenuation, "XSDataDouble")
		self._attenuation = attenuation
	def delAttenuation(self): self._attenuation = None
	# Properties
	attenuation = property(getAttenuation, setAttenuation, delAttenuation, "Property for attenuation")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataStrategySummary", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getISigma(self): return self._iSigma
	def setISigma(self, iSigma):
		checkType("XSDataStrategySummary", "setISigma", iSigma, "XSDataDouble")
		self._iSigma = iSigma
	def delISigma(self): self._iSigma = None
	# Properties
	iSigma = property(getISigma, setISigma, delISigma, "Property for iSigma")
	def getRankingResolution(self): return self._rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataStrategySummary", "setRankingResolution", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
	def delRankingResolution(self): self._rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getRedundancy(self): return self._redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataStrategySummary", "setRedundancy", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def delRedundancy(self): self._redundancy = None
	# Properties
	redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataStrategySummary", "setResolution", resolution, "XSDataDouble")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolutionReasoning(self): return self._resolutionReasoning
	def setResolutionReasoning(self, resolutionReasoning):
		checkType("XSDataStrategySummary", "setResolutionReasoning", resolutionReasoning, "XSDataString")
		self._resolutionReasoning = resolutionReasoning
	def delResolutionReasoning(self): self._resolutionReasoning = None
	# Properties
	resolutionReasoning = property(getResolutionReasoning, setResolutionReasoning, delResolutionReasoning, "Property for resolutionReasoning")
	def getTotalDataCollectionTime(self): return self._totalDataCollectionTime
	def setTotalDataCollectionTime(self, totalDataCollectionTime):
		checkType("XSDataStrategySummary", "setTotalDataCollectionTime", totalDataCollectionTime, "XSDataTime")
		self._totalDataCollectionTime = totalDataCollectionTime
	def delTotalDataCollectionTime(self): self._totalDataCollectionTime = None
	# Properties
	totalDataCollectionTime = property(getTotalDataCollectionTime, setTotalDataCollectionTime, delTotalDataCollectionTime, "Property for totalDataCollectionTime")
	def getTotalExposureTime(self): return self._totalExposureTime
	def setTotalExposureTime(self, totalExposureTime):
		checkType("XSDataStrategySummary", "setTotalExposureTime", totalExposureTime, "XSDataTime")
		self._totalExposureTime = totalExposureTime
	def delTotalExposureTime(self): self._totalExposureTime = None
	# Properties
	totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
	def export(self, outfile, level, name_='XSDataStrategySummary'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStrategySummary'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._attenuation is not None:
			self.attenuation.export(outfile, level, name_='attenuation')
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self._iSigma is not None:
			self.iSigma.export(outfile, level, name_='iSigma')
		else:
			warnEmptyAttribute("iSigma", "XSDataDouble")
		if self._rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		else:
			warnEmptyAttribute("rankingResolution", "XSDataDouble")
		if self._redundancy is not None:
			self.redundancy.export(outfile, level, name_='redundancy')
		else:
			warnEmptyAttribute("redundancy", "XSDataDouble")
		if self._resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self._resolutionReasoning is not None:
			self.resolutionReasoning.export(outfile, level, name_='resolutionReasoning')
		else:
			warnEmptyAttribute("resolutionReasoning", "XSDataString")
		if self._totalDataCollectionTime is not None:
			self.totalDataCollectionTime.export(outfile, level, name_='totalDataCollectionTime')
		else:
			warnEmptyAttribute("totalDataCollectionTime", "XSDataTime")
		if self._totalExposureTime is not None:
			self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
		else:
			warnEmptyAttribute("totalExposureTime", "XSDataTime")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'attenuation':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAttenuation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setISigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRankingResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'redundancy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRedundancy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionReasoning':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setResolutionReasoning(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'totalDataCollectionTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTotalDataCollectionTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'totalExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTotalExposureTime(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStrategySummary" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStrategySummary' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStrategySummary is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStrategySummary.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStrategySummary()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStrategySummary" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStrategySummary()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStrategySummary

class XSDataStructure(XSData):
	"""This is the polymer structure composed by a list of chains and a list of ligands.
This structure is also defined by its number in the asymmetric unit."""
	def __init__(self, numberOfCopiesInAsymmetricUnit=None, ligand=None, chain=None):
		XSData.__init__(self, )
	
	
		if chain is None:
			self._chain = []
		else:
			checkType("XSDataStructure", "Constructor of XSDataStructure", chain, "list")
			self._chain = chain
		if ligand is None:
			self._ligand = []
		else:
			checkType("XSDataStructure", "Constructor of XSDataStructure", ligand, "list")
			self._ligand = ligand
		checkType("XSDataStructure", "Constructor of XSDataStructure", numberOfCopiesInAsymmetricUnit, "XSDataDouble")
		self._numberOfCopiesInAsymmetricUnit = numberOfCopiesInAsymmetricUnit
	def getChain(self): return self._chain
	def setChain(self, chain):
		checkType("XSDataStructure", "setChain", chain, "list")
		self._chain = chain
	def delChain(self): self._chain = None
	# Properties
	chain = property(getChain, setChain, delChain, "Property for chain")
	def addChain(self, value):
		checkType("XSDataStructure", "setChain", value, "XSDataChain")
		self._chain.append(value)
	def insertChain(self, index, value):
		checkType("XSDataStructure", "setChain", value, "XSDataChain")
		self._chain[index] = value
	def getLigand(self): return self._ligand
	def setLigand(self, ligand):
		checkType("XSDataStructure", "setLigand", ligand, "list")
		self._ligand = ligand
	def delLigand(self): self._ligand = None
	# Properties
	ligand = property(getLigand, setLigand, delLigand, "Property for ligand")
	def addLigand(self, value):
		checkType("XSDataStructure", "setLigand", value, "XSDataLigand")
		self._ligand.append(value)
	def insertLigand(self, index, value):
		checkType("XSDataStructure", "setLigand", value, "XSDataLigand")
		self._ligand[index] = value
	def getNumberOfCopiesInAsymmetricUnit(self): return self._numberOfCopiesInAsymmetricUnit
	def setNumberOfCopiesInAsymmetricUnit(self, numberOfCopiesInAsymmetricUnit):
		checkType("XSDataStructure", "setNumberOfCopiesInAsymmetricUnit", numberOfCopiesInAsymmetricUnit, "XSDataDouble")
		self._numberOfCopiesInAsymmetricUnit = numberOfCopiesInAsymmetricUnit
	def delNumberOfCopiesInAsymmetricUnit(self): self._numberOfCopiesInAsymmetricUnit = None
	# Properties
	numberOfCopiesInAsymmetricUnit = property(getNumberOfCopiesInAsymmetricUnit, setNumberOfCopiesInAsymmetricUnit, delNumberOfCopiesInAsymmetricUnit, "Property for numberOfCopiesInAsymmetricUnit")
	def export(self, outfile, level, name_='XSDataStructure'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStructure'):
		XSData.exportChildren(self, outfile, level, name_)
		for chain_ in self.getChain():
			chain_.export(outfile, level, name_='chain')
		for ligand_ in self.getLigand():
			ligand_.export(outfile, level, name_='ligand')
		if self._numberOfCopiesInAsymmetricUnit is not None:
			self.numberOfCopiesInAsymmetricUnit.export(outfile, level, name_='numberOfCopiesInAsymmetricUnit')
		else:
			warnEmptyAttribute("numberOfCopiesInAsymmetricUnit", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chain':
			obj_ = XSDataChain()
			obj_.build(child_)
			self.chain.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ligand':
			obj_ = XSDataLigand()
			obj_.build(child_)
			self.ligand.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfCopiesInAsymmetricUnit':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNumberOfCopiesInAsymmetricUnit(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStructure" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStructure' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStructure is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStructure.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStructure()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStructure" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStructure()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStructure

class XSDataSubWedge(XSData):
	"""A subwedge is defined as a list of images that been collected or is to be collected with some particular experimental condition. If the images are to be collected, the image list is empty.
The subWedgeNumber is an optional number for relating different subwedges, especially for planning data collections."""
	def __init__(self, subWedgeNumber=None, image=None, experimentalCondition=None, action=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataSubWedge", "Constructor of XSDataSubWedge", action, "XSDataString")
		self._action = action
		checkType("XSDataSubWedge", "Constructor of XSDataSubWedge", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
		if image is None:
			self._image = []
		else:
			checkType("XSDataSubWedge", "Constructor of XSDataSubWedge", image, "list")
			self._image = image
		checkType("XSDataSubWedge", "Constructor of XSDataSubWedge", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
	def getAction(self): return self._action
	def setAction(self, action):
		checkType("XSDataSubWedge", "setAction", action, "XSDataString")
		self._action = action
	def delAction(self): self._action = None
	# Properties
	action = property(getAction, setAction, delAction, "Property for action")
	def getExperimentalCondition(self): return self._experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataSubWedge", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self._experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataSubWedge", "setImage", image, "list")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def addImage(self, value):
		checkType("XSDataSubWedge", "setImage", value, "XSDataImage")
		self._image.append(value)
	def insertImage(self, index, value):
		checkType("XSDataSubWedge", "setImage", value, "XSDataImage")
		self._image[index] = value
	def getSubWedgeNumber(self): return self._subWedgeNumber
	def setSubWedgeNumber(self, subWedgeNumber):
		checkType("XSDataSubWedge", "setSubWedgeNumber", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
	def delSubWedgeNumber(self): self._subWedgeNumber = None
	# Properties
	subWedgeNumber = property(getSubWedgeNumber, setSubWedgeNumber, delSubWedgeNumber, "Property for subWedgeNumber")
	def export(self, outfile, level, name_='XSDataSubWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSubWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._action is not None:
			self.action.export(outfile, level, name_='action')
		if self._experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		else:
			warnEmptyAttribute("experimentalCondition", "XSDataExperimentalCondition")
		for image_ in self.getImage():
			image_.export(outfile, level, name_='image')
		if self._subWedgeNumber is not None:
			self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'action':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setAction(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.image.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedgeNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSubWedgeNumber(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSubWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSubWedge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSubWedge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSubWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSubWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSubWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSubWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSubWedge

class XSDataGeneratePredictionResult(XSDataResult):
	def __init__(self, status=None, predictionImage=None):
		XSDataResult.__init__(self, status)
	
	
		if predictionImage is None:
			self._predictionImage = []
		else:
			checkType("XSDataGeneratePredictionResult", "Constructor of XSDataGeneratePredictionResult", predictionImage, "list")
			self._predictionImage = predictionImage
	def getPredictionImage(self): return self._predictionImage
	def setPredictionImage(self, predictionImage):
		checkType("XSDataGeneratePredictionResult", "setPredictionImage", predictionImage, "list")
		self._predictionImage = predictionImage
	def delPredictionImage(self): self._predictionImage = None
	# Properties
	predictionImage = property(getPredictionImage, setPredictionImage, delPredictionImage, "Property for predictionImage")
	def addPredictionImage(self, value):
		checkType("XSDataGeneratePredictionResult", "setPredictionImage", value, "XSDataImage")
		self._predictionImage.append(value)
	def insertPredictionImage(self, index, value):
		checkType("XSDataGeneratePredictionResult", "setPredictionImage", value, "XSDataImage")
		self._predictionImage[index] = value
	def export(self, outfile, level, name_='XSDataGeneratePredictionResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeneratePredictionResult'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for predictionImage_ in self.getPredictionImage():
			predictionImage_.export(outfile, level, name_='predictionImage')
		if self.getPredictionImage() == []:
			warnEmptyAttribute("predictionImage", "XSDataImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'predictionImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.predictionImage.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeneratePredictionResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeneratePredictionResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeneratePredictionResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeneratePredictionResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeneratePredictionResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeneratePredictionResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeneratePredictionResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeneratePredictionResult

class XSDataIndexingInput(XSDataInput):
	def __init__(self, configuration=None, experimentalCondition=None, dataCollection=None, crystal=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataIndexingInput", "Constructor of XSDataIndexingInput", crystal, "XSDataCrystal")
		self._crystal = crystal
		checkType("XSDataIndexingInput", "Constructor of XSDataIndexingInput", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
		checkType("XSDataIndexingInput", "Constructor of XSDataIndexingInput", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def getCrystal(self): return self._crystal
	def setCrystal(self, crystal):
		checkType("XSDataIndexingInput", "setCrystal", crystal, "XSDataCrystal")
		self._crystal = crystal
	def delCrystal(self): self._crystal = None
	# Properties
	crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataIndexingInput", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def getExperimentalCondition(self): return self._experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataIndexingInput", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self._experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def export(self, outfile, level, name_='XSDataIndexingInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIndexingInput'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._crystal is not None:
			self.crystal.export(outfile, level, name_='crystal')
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
		if self._experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIndexingInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIndexingInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIndexingInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIndexingInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIndexingInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIndexingInput

class XSDataIndexingSolutionSelected(XSDataIndexingSolution):
	def __init__(self, penalty=None, number=None, crystal=None, statistics=None, orientation=None, mosaicityEstimation=None, experimentalConditionRefined=None):
		XSDataIndexingSolution.__init__(self, penalty, number, crystal)
	
	
		checkType("XSDataIndexingSolutionSelected", "Constructor of XSDataIndexingSolutionSelected", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
		checkType("XSDataIndexingSolutionSelected", "Constructor of XSDataIndexingSolutionSelected", mosaicityEstimation, "XSDataFloat")
		self._mosaicityEstimation = mosaicityEstimation
		checkType("XSDataIndexingSolutionSelected", "Constructor of XSDataIndexingSolutionSelected", orientation, "XSDataOrientation")
		self._orientation = orientation
		checkType("XSDataIndexingSolutionSelected", "Constructor of XSDataIndexingSolutionSelected", statistics, "XSDataStatisticsIndexing")
		self._statistics = statistics
	def getExperimentalConditionRefined(self): return self._experimentalConditionRefined
	def setExperimentalConditionRefined(self, experimentalConditionRefined):
		checkType("XSDataIndexingSolutionSelected", "setExperimentalConditionRefined", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
	def delExperimentalConditionRefined(self): self._experimentalConditionRefined = None
	# Properties
	experimentalConditionRefined = property(getExperimentalConditionRefined, setExperimentalConditionRefined, delExperimentalConditionRefined, "Property for experimentalConditionRefined")
	def getMosaicityEstimation(self): return self._mosaicityEstimation
	def setMosaicityEstimation(self, mosaicityEstimation):
		checkType("XSDataIndexingSolutionSelected", "setMosaicityEstimation", mosaicityEstimation, "XSDataFloat")
		self._mosaicityEstimation = mosaicityEstimation
	def delMosaicityEstimation(self): self._mosaicityEstimation = None
	# Properties
	mosaicityEstimation = property(getMosaicityEstimation, setMosaicityEstimation, delMosaicityEstimation, "Property for mosaicityEstimation")
	def getOrientation(self): return self._orientation
	def setOrientation(self, orientation):
		checkType("XSDataIndexingSolutionSelected", "setOrientation", orientation, "XSDataOrientation")
		self._orientation = orientation
	def delOrientation(self): self._orientation = None
	# Properties
	orientation = property(getOrientation, setOrientation, delOrientation, "Property for orientation")
	def getStatistics(self): return self._statistics
	def setStatistics(self, statistics):
		checkType("XSDataIndexingSolutionSelected", "setStatistics", statistics, "XSDataStatisticsIndexing")
		self._statistics = statistics
	def delStatistics(self): self._statistics = None
	# Properties
	statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
	def export(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
		XSDataIndexingSolution.exportChildren(self, outfile, level, name_)
		if self._experimentalConditionRefined is not None:
			self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
		else:
			warnEmptyAttribute("experimentalConditionRefined", "XSDataExperimentalCondition")
		if self._mosaicityEstimation is not None:
			self.mosaicityEstimation.export(outfile, level, name_='mosaicityEstimation')
		if self._orientation is not None:
			self.orientation.export(outfile, level, name_='orientation')
		else:
			warnEmptyAttribute("orientation", "XSDataOrientation")
		if self._statistics is not None:
			self.statistics.export(outfile, level, name_='statistics')
		else:
			warnEmptyAttribute("statistics", "XSDataStatisticsIndexing")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalConditionRefined':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalConditionRefined(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicityEstimation':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMosaicityEstimation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'orientation':
			obj_ = XSDataOrientation()
			obj_.build(child_)
			self.setOrientation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statistics':
			obj_ = XSDataStatisticsIndexing()
			obj_.build(child_)
			self.setStatistics(obj_)
		XSDataIndexingSolution.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIndexingSolutionSelected" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIndexingSolutionSelected' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIndexingSolutionSelected is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIndexingSolutionSelected.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingSolutionSelected()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIndexingSolutionSelected" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingSolutionSelected()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIndexingSolutionSelected

class XSDataGeneratePredictionInput(XSDataInput):
	"""This generalisation is not very logical in terms of names, it should be fixed after the prototype (see bug #49)."""
	def __init__(self, configuration=None, selectedIndexingSolution=None, dataCollection=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataGeneratePredictionInput", "Constructor of XSDataGeneratePredictionInput", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
		checkType("XSDataGeneratePredictionInput", "Constructor of XSDataGeneratePredictionInput", selectedIndexingSolution, "XSDataIndexingSolutionSelected")
		self._selectedIndexingSolution = selectedIndexingSolution
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataGeneratePredictionInput", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def getSelectedIndexingSolution(self): return self._selectedIndexingSolution
	def setSelectedIndexingSolution(self, selectedIndexingSolution):
		checkType("XSDataGeneratePredictionInput", "setSelectedIndexingSolution", selectedIndexingSolution, "XSDataIndexingSolutionSelected")
		self._selectedIndexingSolution = selectedIndexingSolution
	def delSelectedIndexingSolution(self): self._selectedIndexingSolution = None
	# Properties
	selectedIndexingSolution = property(getSelectedIndexingSolution, setSelectedIndexingSolution, delSelectedIndexingSolution, "Property for selectedIndexingSolution")
	def export(self, outfile, level, name_='XSDataGeneratePredictionInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeneratePredictionInput'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
		if self._selectedIndexingSolution is not None:
			self.selectedIndexingSolution.export(outfile, level, name_='selectedIndexingSolution')
		else:
			warnEmptyAttribute("selectedIndexingSolution", "XSDataIndexingSolutionSelected")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedIndexingSolution':
			obj_ = XSDataIndexingSolutionSelected()
			obj_.build(child_)
			self.setSelectedIndexingSolution(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeneratePredictionInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeneratePredictionInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeneratePredictionInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeneratePredictionInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeneratePredictionInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeneratePredictionInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeneratePredictionInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeneratePredictionInput

class XSDataIndexingResult(XSDataResult):
	def __init__(self, status=None, solution=None, selectedSolution=None, predictionResult=None, indexingLogFile=None, image=None):
		XSDataResult.__init__(self, status)
	
	
		if image is None:
			self._image = []
		else:
			checkType("XSDataIndexingResult", "Constructor of XSDataIndexingResult", image, "list")
			self._image = image
		checkType("XSDataIndexingResult", "Constructor of XSDataIndexingResult", indexingLogFile, "XSDataFile")
		self._indexingLogFile = indexingLogFile
		checkType("XSDataIndexingResult", "Constructor of XSDataIndexingResult", predictionResult, "XSDataGeneratePredictionResult")
		self._predictionResult = predictionResult
		checkType("XSDataIndexingResult", "Constructor of XSDataIndexingResult", selectedSolution, "XSDataIndexingSolutionSelected")
		self._selectedSolution = selectedSolution
		if solution is None:
			self._solution = []
		else:
			checkType("XSDataIndexingResult", "Constructor of XSDataIndexingResult", solution, "list")
			self._solution = solution
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataIndexingResult", "setImage", image, "list")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def addImage(self, value):
		checkType("XSDataIndexingResult", "setImage", value, "XSDataImage")
		self._image.append(value)
	def insertImage(self, index, value):
		checkType("XSDataIndexingResult", "setImage", value, "XSDataImage")
		self._image[index] = value
	def getIndexingLogFile(self): return self._indexingLogFile
	def setIndexingLogFile(self, indexingLogFile):
		checkType("XSDataIndexingResult", "setIndexingLogFile", indexingLogFile, "XSDataFile")
		self._indexingLogFile = indexingLogFile
	def delIndexingLogFile(self): self._indexingLogFile = None
	# Properties
	indexingLogFile = property(getIndexingLogFile, setIndexingLogFile, delIndexingLogFile, "Property for indexingLogFile")
	def getPredictionResult(self): return self._predictionResult
	def setPredictionResult(self, predictionResult):
		checkType("XSDataIndexingResult", "setPredictionResult", predictionResult, "XSDataGeneratePredictionResult")
		self._predictionResult = predictionResult
	def delPredictionResult(self): self._predictionResult = None
	# Properties
	predictionResult = property(getPredictionResult, setPredictionResult, delPredictionResult, "Property for predictionResult")
	def getSelectedSolution(self): return self._selectedSolution
	def setSelectedSolution(self, selectedSolution):
		checkType("XSDataIndexingResult", "setSelectedSolution", selectedSolution, "XSDataIndexingSolutionSelected")
		self._selectedSolution = selectedSolution
	def delSelectedSolution(self): self._selectedSolution = None
	# Properties
	selectedSolution = property(getSelectedSolution, setSelectedSolution, delSelectedSolution, "Property for selectedSolution")
	def getSolution(self): return self._solution
	def setSolution(self, solution):
		checkType("XSDataIndexingResult", "setSolution", solution, "list")
		self._solution = solution
	def delSolution(self): self._solution = None
	# Properties
	solution = property(getSolution, setSolution, delSolution, "Property for solution")
	def addSolution(self, value):
		checkType("XSDataIndexingResult", "setSolution", value, "XSDataIndexingSolution")
		self._solution.append(value)
	def insertSolution(self, index, value):
		checkType("XSDataIndexingResult", "setSolution", value, "XSDataIndexingSolution")
		self._solution[index] = value
	def export(self, outfile, level, name_='XSDataIndexingResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIndexingResult'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for image_ in self.getImage():
			image_.export(outfile, level, name_='image')
		if self.getImage() == []:
			warnEmptyAttribute("image", "XSDataImage")
		if self._indexingLogFile is not None:
			self.indexingLogFile.export(outfile, level, name_='indexingLogFile')
		if self._predictionResult is not None:
			self.predictionResult.export(outfile, level, name_='predictionResult')
		if self._selectedSolution is not None:
			self.selectedSolution.export(outfile, level, name_='selectedSolution')
		for solution_ in self.getSolution():
			solution_.export(outfile, level, name_='solution')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.image.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'indexingLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIndexingLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'predictionResult':
			obj_ = XSDataGeneratePredictionResult()
			obj_.build(child_)
			self.setPredictionResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedSolution':
			obj_ = XSDataIndexingSolutionSelected()
			obj_.build(child_)
			self.setSelectedSolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'solution':
			obj_ = XSDataIndexingSolution()
			obj_.build(child_)
			self.solution.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIndexingResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIndexingResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIndexingResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIndexingResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIndexingResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIndexingResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIndexingResult

class XSDataInputCharacterisation(XSDataInput):
	def __init__(self, configuration=None, dataCollection=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputCharacterisation", "Constructor of XSDataInputCharacterisation", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataInputCharacterisation", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def export(self, outfile, level, name_='XSDataInputCharacterisation'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputCharacterisation'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputCharacterisation" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputCharacterisation' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputCharacterisation is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputCharacterisation.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputCharacterisation()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputCharacterisation" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputCharacterisation()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputCharacterisation

class XSDataInputControlISPyB(XSDataInput):
	def __init__(self, configuration=None, dataCollectionId=None, characterisationResult=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputControlISPyB", "Constructor of XSDataInputControlISPyB", characterisationResult, "XSDataResultCharacterisation")
		self._characterisationResult = characterisationResult
		checkType("XSDataInputControlISPyB", "Constructor of XSDataInputControlISPyB", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
	def getCharacterisationResult(self): return self._characterisationResult
	def setCharacterisationResult(self, characterisationResult):
		checkType("XSDataInputControlISPyB", "setCharacterisationResult", characterisationResult, "XSDataResultCharacterisation")
		self._characterisationResult = characterisationResult
	def delCharacterisationResult(self): self._characterisationResult = None
	# Properties
	characterisationResult = property(getCharacterisationResult, setCharacterisationResult, delCharacterisationResult, "Property for characterisationResult")
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataInputControlISPyB", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def export(self, outfile, level, name_='XSDataInputControlISPyB'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputControlISPyB'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._characterisationResult is not None:
			self.characterisationResult.export(outfile, level, name_='characterisationResult')
		else:
			warnEmptyAttribute("characterisationResult", "XSDataResultCharacterisation")
		if self._dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
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
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputControlISPyB" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputControlISPyB' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputControlISPyB is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputControlISPyB.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlISPyB()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputControlISPyB" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlISPyB()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputControlISPyB

class XSDataInputControlImageQualityIndicators(XSDataInput):
	def __init__(self, configuration=None, image=None):
		XSDataInput.__init__(self, configuration)
	
	
		if image is None:
			self._image = []
		else:
			checkType("XSDataInputControlImageQualityIndicators", "Constructor of XSDataInputControlImageQualityIndicators", image, "list")
			self._image = image
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataInputControlImageQualityIndicators", "setImage", image, "list")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def addImage(self, value):
		checkType("XSDataInputControlImageQualityIndicators", "setImage", value, "XSDataImage")
		self._image.append(value)
	def insertImage(self, index, value):
		checkType("XSDataInputControlImageQualityIndicators", "setImage", value, "XSDataImage")
		self._image[index] = value
	def export(self, outfile, level, name_='XSDataInputControlImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputControlImageQualityIndicators'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for image_ in self.getImage():
			image_.export(outfile, level, name_='image')
		if self.getImage() == []:
			warnEmptyAttribute("image", "XSDataImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.image.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputControlImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputControlImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputControlImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputControlImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputControlImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputControlImageQualityIndicators

class XSDataInputControlXDSGenerateBackgroundImage(XSDataInput):
	def __init__(self, configuration=None, dataCollection=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputControlXDSGenerateBackgroundImage", "Constructor of XSDataInputControlXDSGenerateBackgroundImage", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataInputControlXDSGenerateBackgroundImage", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def export(self, outfile, level, name_='XSDataInputControlXDSGenerateBackgroundImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputControlXDSGenerateBackgroundImage'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputControlXDSGenerateBackgroundImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputControlXDSGenerateBackgroundImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputControlXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputControlXDSGenerateBackgroundImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputControlXDSGenerateBackgroundImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputControlXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputControlXDSGenerateBackgroundImage

class XSDataInputInducedRadiationProcess(XSDataInput):
	def __init__(self, configuration=None, characterisationResult=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputInducedRadiationProcess", "Constructor of XSDataInputInducedRadiationProcess", characterisationResult, "XSDataResultCharacterisation")
		self._characterisationResult = characterisationResult
	def getCharacterisationResult(self): return self._characterisationResult
	def setCharacterisationResult(self, characterisationResult):
		checkType("XSDataInputInducedRadiationProcess", "setCharacterisationResult", characterisationResult, "XSDataResultCharacterisation")
		self._characterisationResult = characterisationResult
	def delCharacterisationResult(self): self._characterisationResult = None
	# Properties
	characterisationResult = property(getCharacterisationResult, setCharacterisationResult, delCharacterisationResult, "Property for characterisationResult")
	def export(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._characterisationResult is not None:
			self.characterisationResult.export(outfile, level, name_='characterisationResult')
		else:
			warnEmptyAttribute("characterisationResult", "XSDataResultCharacterisation")
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
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputInducedRadiationProcess" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputInducedRadiationProcess' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputInducedRadiationProcess is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputInducedRadiationProcess.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputInducedRadiationProcess()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputInducedRadiationProcess" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputInducedRadiationProcess()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputInducedRadiationProcess

class XSDataInputReadImageHeader(XSDataInput):
	"""These two definitions are used by the read image header plugin."""
	def __init__(self, configuration=None, image=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputReadImageHeader", "Constructor of XSDataInputReadImageHeader", image, "XSDataFile")
		self._image = image
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataInputReadImageHeader", "setImage", image, "XSDataFile")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def export(self, outfile, level, name_='XSDataInputReadImageHeader'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputReadImageHeader'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setImage(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputReadImageHeader" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputReadImageHeader' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputReadImageHeader is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputReadImageHeader.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadImageHeader()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputReadImageHeader" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputReadImageHeader()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputReadImageHeader

class XSDataInputStrategy(XSDataInput):
	def __init__(self, configuration=None, xdsBackgroundImage=None, sample=None, experimentalCondition=None, diffractionPlan=None, crystalRefined=None, bestFileContentPar=None, bestFileContentHKL=None, bestFileContentDat=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
		if bestFileContentHKL is None:
			self._bestFileContentHKL = []
		else:
			checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", bestFileContentHKL, "list")
			self._bestFileContentHKL = bestFileContentHKL
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", sample, "XSDataSampleCrystalMM")
		self._sample = sample
		checkType("XSDataInputStrategy", "Constructor of XSDataInputStrategy", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def getBestFileContentDat(self): return self._bestFileContentDat
	def setBestFileContentDat(self, bestFileContentDat):
		checkType("XSDataInputStrategy", "setBestFileContentDat", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
	def delBestFileContentDat(self): self._bestFileContentDat = None
	# Properties
	bestFileContentDat = property(getBestFileContentDat, setBestFileContentDat, delBestFileContentDat, "Property for bestFileContentDat")
	def getBestFileContentHKL(self): return self._bestFileContentHKL
	def setBestFileContentHKL(self, bestFileContentHKL):
		checkType("XSDataInputStrategy", "setBestFileContentHKL", bestFileContentHKL, "list")
		self._bestFileContentHKL = bestFileContentHKL
	def delBestFileContentHKL(self): self._bestFileContentHKL = None
	# Properties
	bestFileContentHKL = property(getBestFileContentHKL, setBestFileContentHKL, delBestFileContentHKL, "Property for bestFileContentHKL")
	def addBestFileContentHKL(self, value):
		checkType("XSDataInputStrategy", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL.append(value)
	def insertBestFileContentHKL(self, index, value):
		checkType("XSDataInputStrategy", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL[index] = value
	def getBestFileContentPar(self): return self._bestFileContentPar
	def setBestFileContentPar(self, bestFileContentPar):
		checkType("XSDataInputStrategy", "setBestFileContentPar", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
	def delBestFileContentPar(self): self._bestFileContentPar = None
	# Properties
	bestFileContentPar = property(getBestFileContentPar, setBestFileContentPar, delBestFileContentPar, "Property for bestFileContentPar")
	def getCrystalRefined(self): return self._crystalRefined
	def setCrystalRefined(self, crystalRefined):
		checkType("XSDataInputStrategy", "setCrystalRefined", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
	def delCrystalRefined(self): self._crystalRefined = None
	# Properties
	crystalRefined = property(getCrystalRefined, setCrystalRefined, delCrystalRefined, "Property for crystalRefined")
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputStrategy", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getExperimentalCondition(self): return self._experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataInputStrategy", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self._experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getSample(self): return self._sample
	def setSample(self, sample):
		checkType("XSDataInputStrategy", "setSample", sample, "XSDataSampleCrystalMM")
		self._sample = sample
	def delSample(self): self._sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getXdsBackgroundImage(self): return self._xdsBackgroundImage
	def setXdsBackgroundImage(self, xdsBackgroundImage):
		checkType("XSDataInputStrategy", "setXdsBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
	# Properties
	xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
	def export(self, outfile, level, name_='XSDataInputStrategy'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputStrategy'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._bestFileContentDat is not None:
			self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
		else:
			warnEmptyAttribute("bestFileContentDat", "XSDataString")
		for bestFileContentHKL_ in self.getBestFileContentHKL():
			bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
		if self.getBestFileContentHKL() == []:
			warnEmptyAttribute("bestFileContentHKL", "XSDataString")
		if self._bestFileContentPar is not None:
			self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
		else:
			warnEmptyAttribute("bestFileContentPar", "XSDataString")
		if self._crystalRefined is not None:
			self.crystalRefined.export(outfile, level, name_='crystalRefined')
		else:
			warnEmptyAttribute("crystalRefined", "XSDataCrystal")
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		else:
			warnEmptyAttribute("diffractionPlan", "XSDataDiffractionPlan")
		if self._experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		else:
			warnEmptyAttribute("experimentalCondition", "XSDataExperimentalCondition")
		if self._sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataSampleCrystalMM")
		if self._xdsBackgroundImage is not None:
			self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentDat':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentDat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentHKL':
			obj_ = XSDataString()
			obj_.build(child_)
			self.bestFileContentHKL.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentPar':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentPar(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalRefined':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystalRefined(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSampleCrystalMM()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xdsBackgroundImage':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setXdsBackgroundImage(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputStrategy" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStrategy' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputStrategy is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputStrategy.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputStrategy()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputStrategy" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputStrategy()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputStrategy

class XSDataInputSubWedgeAssemble(XSDataInput):
	"""These two definitions are used by the sub wedge assemble plugin."""
	def __init__(self, configuration=None, file=None):
		XSDataInput.__init__(self, configuration)
	
	
		if file is None:
			self._file = []
		else:
			checkType("XSDataInputSubWedgeAssemble", "Constructor of XSDataInputSubWedgeAssemble", file, "list")
			self._file = file
	def getFile(self): return self._file
	def setFile(self, file):
		checkType("XSDataInputSubWedgeAssemble", "setFile", file, "list")
		self._file = file
	def delFile(self): self._file = None
	# Properties
	file = property(getFile, setFile, delFile, "Property for file")
	def addFile(self, value):
		checkType("XSDataInputSubWedgeAssemble", "setFile", value, "XSDataFile")
		self._file.append(value)
	def insertFile(self, index, value):
		checkType("XSDataInputSubWedgeAssemble", "setFile", value, "XSDataFile")
		self._file[index] = value
	def export(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for file_ in self.getFile():
			file_.export(outfile, level, name_='file')
		if self.getFile() == []:
			warnEmptyAttribute("file", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'file':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.file.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputSubWedgeAssemble" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSubWedgeAssemble' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputSubWedgeAssemble is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSubWedgeAssemble.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSubWedgeAssemble()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSubWedgeAssemble" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSubWedgeAssemble()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSubWedgeAssemble

class XSDataInputSubWedgeMerge(XSDataInput):
	"""These two definitions are used by the sub wedge merge plugins."""
	def __init__(self, configuration=None, subWedge=None):
		XSDataInput.__init__(self, configuration)
	
	
		if subWedge is None:
			self._subWedge = []
		else:
			checkType("XSDataInputSubWedgeMerge", "Constructor of XSDataInputSubWedgeMerge", subWedge, "list")
			self._subWedge = subWedge
	def getSubWedge(self): return self._subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataInputSubWedgeMerge", "setSubWedge", subWedge, "list")
		self._subWedge = subWedge
	def delSubWedge(self): self._subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def addSubWedge(self, value):
		checkType("XSDataInputSubWedgeMerge", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge.append(value)
	def insertSubWedge(self, index, value):
		checkType("XSDataInputSubWedgeMerge", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge[index] = value
	def export(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for subWedge_ in self.getSubWedge():
			subWedge_.export(outfile, level, name_='subWedge')
		if self.getSubWedge() == []:
			warnEmptyAttribute("subWedge", "XSDataSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataSubWedge()
			obj_.build(child_)
			self.subWedge.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputSubWedgeMerge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSubWedgeMerge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputSubWedgeMerge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSubWedgeMerge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSubWedgeMerge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSubWedgeMerge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSubWedgeMerge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSubWedgeMerge

class XSDataIntegrationResult(XSDataResult):
	def __init__(self, status=None, integrationSubWedgeResult=None):
		XSDataResult.__init__(self, status)
	
	
		if integrationSubWedgeResult is None:
			self._integrationSubWedgeResult = []
		else:
			checkType("XSDataIntegrationResult", "Constructor of XSDataIntegrationResult", integrationSubWedgeResult, "list")
			self._integrationSubWedgeResult = integrationSubWedgeResult
	def getIntegrationSubWedgeResult(self): return self._integrationSubWedgeResult
	def setIntegrationSubWedgeResult(self, integrationSubWedgeResult):
		checkType("XSDataIntegrationResult", "setIntegrationSubWedgeResult", integrationSubWedgeResult, "list")
		self._integrationSubWedgeResult = integrationSubWedgeResult
	def delIntegrationSubWedgeResult(self): self._integrationSubWedgeResult = None
	# Properties
	integrationSubWedgeResult = property(getIntegrationSubWedgeResult, setIntegrationSubWedgeResult, delIntegrationSubWedgeResult, "Property for integrationSubWedgeResult")
	def addIntegrationSubWedgeResult(self, value):
		checkType("XSDataIntegrationResult", "setIntegrationSubWedgeResult", value, "XSDataIntegrationSubWedgeResult")
		self._integrationSubWedgeResult.append(value)
	def insertIntegrationSubWedgeResult(self, index, value):
		checkType("XSDataIntegrationResult", "setIntegrationSubWedgeResult", value, "XSDataIntegrationSubWedgeResult")
		self._integrationSubWedgeResult[index] = value
	def export(self, outfile, level, name_='XSDataIntegrationResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIntegrationResult'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for integrationSubWedgeResult_ in self.getIntegrationSubWedgeResult():
			integrationSubWedgeResult_.export(outfile, level, name_='integrationSubWedgeResult')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integrationSubWedgeResult':
			obj_ = XSDataIntegrationSubWedgeResult()
			obj_.build(child_)
			self.integrationSubWedgeResult.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIntegrationResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIntegrationResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIntegrationResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIntegrationResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIntegrationResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIntegrationResult

class XSDataResultCharacterisation(XSDataResult):
	def __init__(self, status=None, strategyResult=None, statusMessage=None, shortSummary=None, integrationResult=None, indexingResult=None, imageQualityIndicators=None, executiveSummary=None, dataCollection=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", executiveSummary, "XSDataString")
		self._executiveSummary = executiveSummary
		if imageQualityIndicators is None:
			self._imageQualityIndicators = []
		else:
			checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", imageQualityIndicators, "list")
			self._imageQualityIndicators = imageQualityIndicators
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", indexingResult, "XSDataIndexingResult")
		self._indexingResult = indexingResult
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", integrationResult, "XSDataIntegrationResult")
		self._integrationResult = integrationResult
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", shortSummary, "XSDataString")
		self._shortSummary = shortSummary
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", statusMessage, "XSDataString")
		self._statusMessage = statusMessage
		checkType("XSDataResultCharacterisation", "Constructor of XSDataResultCharacterisation", strategyResult, "XSDataResultStrategy")
		self._strategyResult = strategyResult
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataResultCharacterisation", "setDataCollection", dataCollection, "XSDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def getExecutiveSummary(self): return self._executiveSummary
	def setExecutiveSummary(self, executiveSummary):
		checkType("XSDataResultCharacterisation", "setExecutiveSummary", executiveSummary, "XSDataString")
		self._executiveSummary = executiveSummary
	def delExecutiveSummary(self): self._executiveSummary = None
	# Properties
	executiveSummary = property(getExecutiveSummary, setExecutiveSummary, delExecutiveSummary, "Property for executiveSummary")
	def getImageQualityIndicators(self): return self._imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataResultCharacterisation", "setImageQualityIndicators", imageQualityIndicators, "list")
		self._imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self._imageQualityIndicators = None
	# Properties
	imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
	def addImageQualityIndicators(self, value):
		checkType("XSDataResultCharacterisation", "setImageQualityIndicators", value, "XSDataImageQualityIndicators")
		self._imageQualityIndicators.append(value)
	def insertImageQualityIndicators(self, index, value):
		checkType("XSDataResultCharacterisation", "setImageQualityIndicators", value, "XSDataImageQualityIndicators")
		self._imageQualityIndicators[index] = value
	def getIndexingResult(self): return self._indexingResult
	def setIndexingResult(self, indexingResult):
		checkType("XSDataResultCharacterisation", "setIndexingResult", indexingResult, "XSDataIndexingResult")
		self._indexingResult = indexingResult
	def delIndexingResult(self): self._indexingResult = None
	# Properties
	indexingResult = property(getIndexingResult, setIndexingResult, delIndexingResult, "Property for indexingResult")
	def getIntegrationResult(self): return self._integrationResult
	def setIntegrationResult(self, integrationResult):
		checkType("XSDataResultCharacterisation", "setIntegrationResult", integrationResult, "XSDataIntegrationResult")
		self._integrationResult = integrationResult
	def delIntegrationResult(self): self._integrationResult = None
	# Properties
	integrationResult = property(getIntegrationResult, setIntegrationResult, delIntegrationResult, "Property for integrationResult")
	def getShortSummary(self): return self._shortSummary
	def setShortSummary(self, shortSummary):
		checkType("XSDataResultCharacterisation", "setShortSummary", shortSummary, "XSDataString")
		self._shortSummary = shortSummary
	def delShortSummary(self): self._shortSummary = None
	# Properties
	shortSummary = property(getShortSummary, setShortSummary, delShortSummary, "Property for shortSummary")
	def getStatusMessage(self): return self._statusMessage
	def setStatusMessage(self, statusMessage):
		checkType("XSDataResultCharacterisation", "setStatusMessage", statusMessage, "XSDataString")
		self._statusMessage = statusMessage
	def delStatusMessage(self): self._statusMessage = None
	# Properties
	statusMessage = property(getStatusMessage, setStatusMessage, delStatusMessage, "Property for statusMessage")
	def getStrategyResult(self): return self._strategyResult
	def setStrategyResult(self, strategyResult):
		checkType("XSDataResultCharacterisation", "setStrategyResult", strategyResult, "XSDataResultStrategy")
		self._strategyResult = strategyResult
	def delStrategyResult(self): self._strategyResult = None
	# Properties
	strategyResult = property(getStrategyResult, setStrategyResult, delStrategyResult, "Property for strategyResult")
	def export(self, outfile, level, name_='XSDataResultCharacterisation'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultCharacterisation'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataCollection")
		if self._executiveSummary is not None:
			self.executiveSummary.export(outfile, level, name_='executiveSummary')
		else:
			warnEmptyAttribute("executiveSummary", "XSDataString")
		for imageQualityIndicators_ in self.getImageQualityIndicators():
			imageQualityIndicators_.export(outfile, level, name_='imageQualityIndicators')
		if self._indexingResult is not None:
			self.indexingResult.export(outfile, level, name_='indexingResult')
		if self._integrationResult is not None:
			self.integrationResult.export(outfile, level, name_='integrationResult')
		if self._shortSummary is not None:
			self.shortSummary.export(outfile, level, name_='shortSummary')
		else:
			warnEmptyAttribute("shortSummary", "XSDataString")
		if self._statusMessage is not None:
			self.statusMessage.export(outfile, level, name_='statusMessage')
		else:
			warnEmptyAttribute("statusMessage", "XSDataString")
		if self._strategyResult is not None:
			self.strategyResult.export(outfile, level, name_='strategyResult')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'executiveSummary':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setExecutiveSummary(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicators':
			obj_ = XSDataImageQualityIndicators()
			obj_.build(child_)
			self.imageQualityIndicators.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'indexingResult':
			obj_ = XSDataIndexingResult()
			obj_.build(child_)
			self.setIndexingResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integrationResult':
			obj_ = XSDataIntegrationResult()
			obj_.build(child_)
			self.setIntegrationResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'shortSummary':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setShortSummary(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statusMessage':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStatusMessage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategyResult':
			obj_ = XSDataResultStrategy()
			obj_.build(child_)
			self.setStrategyResult(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultCharacterisation" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultCharacterisation' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultCharacterisation is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultCharacterisation.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultCharacterisation()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultCharacterisation" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultCharacterisation()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultCharacterisation

class XSDataResultControlISPyB(XSDataResult):
	"""No attributes - the return value is XSDataStatus provided by XSDataResult"""
	def __init__(self, status=None, screeningId=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultControlISPyB", "Constructor of XSDataResultControlISPyB", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataResultControlISPyB", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def export(self, outfile, level, name_='XSDataResultControlISPyB'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultControlISPyB'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultControlISPyB" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultControlISPyB' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultControlISPyB is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultControlISPyB.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlISPyB()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultControlISPyB" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlISPyB()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultControlISPyB

class XSDataResultControlImageQualityIndicators(XSDataResult):
	def __init__(self, status=None, imageQualityIndicators=None):
		XSDataResult.__init__(self, status)
	
	
		if imageQualityIndicators is None:
			self._imageQualityIndicators = []
		else:
			checkType("XSDataResultControlImageQualityIndicators", "Constructor of XSDataResultControlImageQualityIndicators", imageQualityIndicators, "list")
			self._imageQualityIndicators = imageQualityIndicators
	def getImageQualityIndicators(self): return self._imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataResultControlImageQualityIndicators", "setImageQualityIndicators", imageQualityIndicators, "list")
		self._imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self._imageQualityIndicators = None
	# Properties
	imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
	def addImageQualityIndicators(self, value):
		checkType("XSDataResultControlImageQualityIndicators", "setImageQualityIndicators", value, "XSDataImageQualityIndicators")
		self._imageQualityIndicators.append(value)
	def insertImageQualityIndicators(self, index, value):
		checkType("XSDataResultControlImageQualityIndicators", "setImageQualityIndicators", value, "XSDataImageQualityIndicators")
		self._imageQualityIndicators[index] = value
	def export(self, outfile, level, name_='XSDataResultControlImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultControlImageQualityIndicators'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for imageQualityIndicators_ in self.getImageQualityIndicators():
			imageQualityIndicators_.export(outfile, level, name_='imageQualityIndicators')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicators':
			obj_ = XSDataImageQualityIndicators()
			obj_.build(child_)
			self.imageQualityIndicators.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultControlImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultControlImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultControlImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultControlImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultControlImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultControlImageQualityIndicators

class XSDataResultControlXDSGenerateBackgroundImage(XSDataResult):
	def __init__(self, status=None, xdsBackgroundImage=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultControlXDSGenerateBackgroundImage", "Constructor of XSDataResultControlXDSGenerateBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def getXdsBackgroundImage(self): return self._xdsBackgroundImage
	def setXdsBackgroundImage(self, xdsBackgroundImage):
		checkType("XSDataResultControlXDSGenerateBackgroundImage", "setXdsBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
	# Properties
	xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
	def export(self, outfile, level, name_='XSDataResultControlXDSGenerateBackgroundImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultControlXDSGenerateBackgroundImage'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._xdsBackgroundImage is not None:
			self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
		else:
			warnEmptyAttribute("xdsBackgroundImage", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xdsBackgroundImage':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setXdsBackgroundImage(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultControlXDSGenerateBackgroundImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultControlXDSGenerateBackgroundImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultControlXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultControlXDSGenerateBackgroundImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultControlXDSGenerateBackgroundImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultControlXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultControlXDSGenerateBackgroundImage

class XSDataResultInducedRadiationProcess(XSDataResult):
	def __init__(self, status=None, scale=None, crystal=None, bFactor=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultInducedRadiationProcess", "Constructor of XSDataResultInducedRadiationProcess", bFactor, "XSDataDouble")
		self._bFactor = bFactor
		checkType("XSDataResultInducedRadiationProcess", "Constructor of XSDataResultInducedRadiationProcess", crystal, "XSDataCrystal")
		self._crystal = crystal
		checkType("XSDataResultInducedRadiationProcess", "Constructor of XSDataResultInducedRadiationProcess", scale, "XSDataDouble")
		self._scale = scale
	def getBFactor(self): return self._bFactor
	def setBFactor(self, bFactor):
		checkType("XSDataResultInducedRadiationProcess", "setBFactor", bFactor, "XSDataDouble")
		self._bFactor = bFactor
	def delBFactor(self): self._bFactor = None
	# Properties
	bFactor = property(getBFactor, setBFactor, delBFactor, "Property for bFactor")
	def getCrystal(self): return self._crystal
	def setCrystal(self, crystal):
		checkType("XSDataResultInducedRadiationProcess", "setCrystal", crystal, "XSDataCrystal")
		self._crystal = crystal
	def delCrystal(self): self._crystal = None
	# Properties
	crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
	def getScale(self): return self._scale
	def setScale(self, scale):
		checkType("XSDataResultInducedRadiationProcess", "setScale", scale, "XSDataDouble")
		self._scale = scale
	def delScale(self): self._scale = None
	# Properties
	scale = property(getScale, setScale, delScale, "Property for scale")
	def export(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._bFactor is not None:
			self.bFactor.export(outfile, level, name_='bFactor')
		else:
			warnEmptyAttribute("bFactor", "XSDataDouble")
		if self._crystal is not None:
			self.crystal.export(outfile, level, name_='crystal')
		else:
			warnEmptyAttribute("crystal", "XSDataCrystal")
		if self._scale is not None:
			self.scale.export(outfile, level, name_='scale')
		else:
			warnEmptyAttribute("scale", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scale':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setScale(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultInducedRadiationProcess" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultInducedRadiationProcess' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultInducedRadiationProcess is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultInducedRadiationProcess.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultInducedRadiationProcess()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultInducedRadiationProcess" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultInducedRadiationProcess()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultInducedRadiationProcess

class XSDataResultReadImageHeader(XSDataResult):
	"""These two definitions are used by the read image header plugin."""
	def __init__(self, status=None, subWedge=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultReadImageHeader", "Constructor of XSDataResultReadImageHeader", subWedge, "XSDataSubWedge")
		self._subWedge = subWedge
	def getSubWedge(self): return self._subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataResultReadImageHeader", "setSubWedge", subWedge, "XSDataSubWedge")
		self._subWedge = subWedge
	def delSubWedge(self): self._subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def export(self, outfile, level, name_='XSDataResultReadImageHeader'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultReadImageHeader'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._subWedge is not None:
			self.subWedge.export(outfile, level, name_='subWedge')
		else:
			warnEmptyAttribute("subWedge", "XSDataSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataSubWedge()
			obj_.build(child_)
			self.setSubWedge(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultReadImageHeader" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultReadImageHeader' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultReadImageHeader is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultReadImageHeader.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadImageHeader()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultReadImageHeader" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultReadImageHeader()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultReadImageHeader

class XSDataResultStrategy(XSDataResult):
	"""Several collection plans could be present in case of multi-sweep strategy"""
	def __init__(self, status=None, raddoseLogFile=None, collectionPlan=None, bestLogFile=None, bestGraphFile=None):
		XSDataResult.__init__(self, status)
	
	
		if bestGraphFile is None:
			self._bestGraphFile = []
		else:
			checkType("XSDataResultStrategy", "Constructor of XSDataResultStrategy", bestGraphFile, "list")
			self._bestGraphFile = bestGraphFile
		checkType("XSDataResultStrategy", "Constructor of XSDataResultStrategy", bestLogFile, "XSDataFile")
		self._bestLogFile = bestLogFile
		if collectionPlan is None:
			self._collectionPlan = []
		else:
			checkType("XSDataResultStrategy", "Constructor of XSDataResultStrategy", collectionPlan, "list")
			self._collectionPlan = collectionPlan
		checkType("XSDataResultStrategy", "Constructor of XSDataResultStrategy", raddoseLogFile, "XSDataFile")
		self._raddoseLogFile = raddoseLogFile
	def getBestGraphFile(self): return self._bestGraphFile
	def setBestGraphFile(self, bestGraphFile):
		checkType("XSDataResultStrategy", "setBestGraphFile", bestGraphFile, "list")
		self._bestGraphFile = bestGraphFile
	def delBestGraphFile(self): self._bestGraphFile = None
	# Properties
	bestGraphFile = property(getBestGraphFile, setBestGraphFile, delBestGraphFile, "Property for bestGraphFile")
	def addBestGraphFile(self, value):
		checkType("XSDataResultStrategy", "setBestGraphFile", value, "XSDataFile")
		self._bestGraphFile.append(value)
	def insertBestGraphFile(self, index, value):
		checkType("XSDataResultStrategy", "setBestGraphFile", value, "XSDataFile")
		self._bestGraphFile[index] = value
	def getBestLogFile(self): return self._bestLogFile
	def setBestLogFile(self, bestLogFile):
		checkType("XSDataResultStrategy", "setBestLogFile", bestLogFile, "XSDataFile")
		self._bestLogFile = bestLogFile
	def delBestLogFile(self): self._bestLogFile = None
	# Properties
	bestLogFile = property(getBestLogFile, setBestLogFile, delBestLogFile, "Property for bestLogFile")
	def getCollectionPlan(self): return self._collectionPlan
	def setCollectionPlan(self, collectionPlan):
		checkType("XSDataResultStrategy", "setCollectionPlan", collectionPlan, "list")
		self._collectionPlan = collectionPlan
	def delCollectionPlan(self): self._collectionPlan = None
	# Properties
	collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
	def addCollectionPlan(self, value):
		checkType("XSDataResultStrategy", "setCollectionPlan", value, "XSDataCollectionPlan")
		self._collectionPlan.append(value)
	def insertCollectionPlan(self, index, value):
		checkType("XSDataResultStrategy", "setCollectionPlan", value, "XSDataCollectionPlan")
		self._collectionPlan[index] = value
	def getRaddoseLogFile(self): return self._raddoseLogFile
	def setRaddoseLogFile(self, raddoseLogFile):
		checkType("XSDataResultStrategy", "setRaddoseLogFile", raddoseLogFile, "XSDataFile")
		self._raddoseLogFile = raddoseLogFile
	def delRaddoseLogFile(self): self._raddoseLogFile = None
	# Properties
	raddoseLogFile = property(getRaddoseLogFile, setRaddoseLogFile, delRaddoseLogFile, "Property for raddoseLogFile")
	def export(self, outfile, level, name_='XSDataResultStrategy'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultStrategy'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for bestGraphFile_ in self.getBestGraphFile():
			bestGraphFile_.export(outfile, level, name_='bestGraphFile')
		if self._bestLogFile is not None:
			self.bestLogFile.export(outfile, level, name_='bestLogFile')
		for collectionPlan_ in self.getCollectionPlan():
			collectionPlan_.export(outfile, level, name_='collectionPlan')
		if self._raddoseLogFile is not None:
			self.raddoseLogFile.export(outfile, level, name_='raddoseLogFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestGraphFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.bestGraphFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBestLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlan':
			obj_ = XSDataCollectionPlan()
			obj_.build(child_)
			self.collectionPlan.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'raddoseLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setRaddoseLogFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultStrategy" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStrategy' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultStrategy is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultStrategy.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultStrategy()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultStrategy" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultStrategy()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultStrategy

class XSDataResultSubWedgeAssemble(XSDataResult):
	"""These two definitions are used by the sub wedge assemble plugin."""
	def __init__(self, status=None, subWedge=None):
		XSDataResult.__init__(self, status)
	
	
		if subWedge is None:
			self._subWedge = []
		else:
			checkType("XSDataResultSubWedgeAssemble", "Constructor of XSDataResultSubWedgeAssemble", subWedge, "list")
			self._subWedge = subWedge
	def getSubWedge(self): return self._subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataResultSubWedgeAssemble", "setSubWedge", subWedge, "list")
		self._subWedge = subWedge
	def delSubWedge(self): self._subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def addSubWedge(self, value):
		checkType("XSDataResultSubWedgeAssemble", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge.append(value)
	def insertSubWedge(self, index, value):
		checkType("XSDataResultSubWedgeAssemble", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge[index] = value
	def export(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for subWedge_ in self.getSubWedge():
			subWedge_.export(outfile, level, name_='subWedge')
		if self.getSubWedge() == []:
			warnEmptyAttribute("subWedge", "XSDataSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataSubWedge()
			obj_.build(child_)
			self.subWedge.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSubWedgeAssemble" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSubWedgeAssemble' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultSubWedgeAssemble is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSubWedgeAssemble.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSubWedgeAssemble()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSubWedgeAssemble" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSubWedgeAssemble()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSubWedgeAssemble

class XSDataResultSubWedgeMerge(XSDataResult):
	"""These two definitions are used by the sub wedge merge plugins."""
	def __init__(self, status=None, subWedge=None):
		XSDataResult.__init__(self, status)
	
	
		if subWedge is None:
			self._subWedge = []
		else:
			checkType("XSDataResultSubWedgeMerge", "Constructor of XSDataResultSubWedgeMerge", subWedge, "list")
			self._subWedge = subWedge
	def getSubWedge(self): return self._subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataResultSubWedgeMerge", "setSubWedge", subWedge, "list")
		self._subWedge = subWedge
	def delSubWedge(self): self._subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def addSubWedge(self, value):
		checkType("XSDataResultSubWedgeMerge", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge.append(value)
	def insertSubWedge(self, index, value):
		checkType("XSDataResultSubWedgeMerge", "setSubWedge", value, "XSDataSubWedge")
		self._subWedge[index] = value
	def export(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for subWedge_ in self.getSubWedge():
			subWedge_.export(outfile, level, name_='subWedge')
		if self.getSubWedge() == []:
			warnEmptyAttribute("subWedge", "XSDataSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataSubWedge()
			obj_.build(child_)
			self.subWedge.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSubWedgeMerge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSubWedgeMerge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultSubWedgeMerge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSubWedgeMerge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSubWedgeMerge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSubWedgeMerge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSubWedgeMerge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSubWedgeMerge

class XSDataSampleCrystal(XSDataSample):
	"""A crystal sample. Inherites of all the XSDataSample attributes (inheritance relationship). In addition has the crystallographic properties (cell, mosaicity, space, group)"""
	def __init__(self, susceptibility=None, size=None, shape=None, absorbedDoseRate=None, crystal=None):
		XSDataSample.__init__(self, susceptibility, size, shape, absorbedDoseRate)
	
	
		checkType("XSDataSampleCrystal", "Constructor of XSDataSampleCrystal", crystal, "XSDataCrystal")
		self._crystal = crystal
	def getCrystal(self): return self._crystal
	def setCrystal(self, crystal):
		checkType("XSDataSampleCrystal", "setCrystal", crystal, "XSDataCrystal")
		self._crystal = crystal
	def delCrystal(self): self._crystal = None
	# Properties
	crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
	def export(self, outfile, level, name_='XSDataSampleCrystal'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSampleCrystal'):
		XSDataSample.exportChildren(self, outfile, level, name_)
		if self._crystal is not None:
			self.crystal.export(outfile, level, name_='crystal')
		else:
			warnEmptyAttribute("crystal", "XSDataCrystal")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystal(obj_)
		XSDataSample.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSampleCrystal" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSampleCrystal' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSampleCrystal is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSampleCrystal.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSampleCrystal()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSampleCrystal" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSampleCrystal()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSampleCrystal

class XSDataStrategyInput(XSDataInput):
	"""These classes are deprecated and will be removed once the corresponding plugins that use them have been removed."""
	def __init__(self, configuration=None, sample=None, experimentalCondition=None, diffractionPlan=None, crystalRefined=None, bestFileContentPar=None, bestFileContentHKL=None, bestFileContentDat=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
		if bestFileContentHKL is None:
			self._bestFileContentHKL = []
		else:
			checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", bestFileContentHKL, "list")
			self._bestFileContentHKL = bestFileContentHKL
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
		checkType("XSDataStrategyInput", "Constructor of XSDataStrategyInput", sample, "XSDataSampleCrystalMM")
		self._sample = sample
	def getBestFileContentDat(self): return self._bestFileContentDat
	def setBestFileContentDat(self, bestFileContentDat):
		checkType("XSDataStrategyInput", "setBestFileContentDat", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
	def delBestFileContentDat(self): self._bestFileContentDat = None
	# Properties
	bestFileContentDat = property(getBestFileContentDat, setBestFileContentDat, delBestFileContentDat, "Property for bestFileContentDat")
	def getBestFileContentHKL(self): return self._bestFileContentHKL
	def setBestFileContentHKL(self, bestFileContentHKL):
		checkType("XSDataStrategyInput", "setBestFileContentHKL", bestFileContentHKL, "list")
		self._bestFileContentHKL = bestFileContentHKL
	def delBestFileContentHKL(self): self._bestFileContentHKL = None
	# Properties
	bestFileContentHKL = property(getBestFileContentHKL, setBestFileContentHKL, delBestFileContentHKL, "Property for bestFileContentHKL")
	def addBestFileContentHKL(self, value):
		checkType("XSDataStrategyInput", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL.append(value)
	def insertBestFileContentHKL(self, index, value):
		checkType("XSDataStrategyInput", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL[index] = value
	def getBestFileContentPar(self): return self._bestFileContentPar
	def setBestFileContentPar(self, bestFileContentPar):
		checkType("XSDataStrategyInput", "setBestFileContentPar", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
	def delBestFileContentPar(self): self._bestFileContentPar = None
	# Properties
	bestFileContentPar = property(getBestFileContentPar, setBestFileContentPar, delBestFileContentPar, "Property for bestFileContentPar")
	def getCrystalRefined(self): return self._crystalRefined
	def setCrystalRefined(self, crystalRefined):
		checkType("XSDataStrategyInput", "setCrystalRefined", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
	def delCrystalRefined(self): self._crystalRefined = None
	# Properties
	crystalRefined = property(getCrystalRefined, setCrystalRefined, delCrystalRefined, "Property for crystalRefined")
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataStrategyInput", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getExperimentalCondition(self): return self._experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataStrategyInput", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self._experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getSample(self): return self._sample
	def setSample(self, sample):
		checkType("XSDataStrategyInput", "setSample", sample, "XSDataSampleCrystalMM")
		self._sample = sample
	def delSample(self): self._sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def export(self, outfile, level, name_='XSDataStrategyInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStrategyInput'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._bestFileContentDat is not None:
			self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
		else:
			warnEmptyAttribute("bestFileContentDat", "XSDataString")
		for bestFileContentHKL_ in self.getBestFileContentHKL():
			bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
		if self.getBestFileContentHKL() == []:
			warnEmptyAttribute("bestFileContentHKL", "XSDataString")
		if self._bestFileContentPar is not None:
			self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
		else:
			warnEmptyAttribute("bestFileContentPar", "XSDataString")
		if self._crystalRefined is not None:
			self.crystalRefined.export(outfile, level, name_='crystalRefined')
		else:
			warnEmptyAttribute("crystalRefined", "XSDataCrystal")
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		else:
			warnEmptyAttribute("diffractionPlan", "XSDataDiffractionPlan")
		if self._experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		else:
			warnEmptyAttribute("experimentalCondition", "XSDataExperimentalCondition")
		if self._sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataSampleCrystalMM")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentDat':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentDat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentHKL':
			obj_ = XSDataString()
			obj_.build(child_)
			self.bestFileContentHKL.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentPar':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentPar(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalRefined':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystalRefined(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSampleCrystalMM()
			obj_.build(child_)
			self.setSample(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStrategyInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStrategyInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStrategyInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStrategyInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStrategyInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStrategyInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStrategyInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStrategyInput

class XSDataStrategyResult(XSDataResult):
	"""Several collection plans could be present in case of multi-sweep strategy"""
	def __init__(self, status=None, collectionPlan=None):
		XSDataResult.__init__(self, status)
	
	
		if collectionPlan is None:
			self._collectionPlan = []
		else:
			checkType("XSDataStrategyResult", "Constructor of XSDataStrategyResult", collectionPlan, "list")
			self._collectionPlan = collectionPlan
	def getCollectionPlan(self): return self._collectionPlan
	def setCollectionPlan(self, collectionPlan):
		checkType("XSDataStrategyResult", "setCollectionPlan", collectionPlan, "list")
		self._collectionPlan = collectionPlan
	def delCollectionPlan(self): self._collectionPlan = None
	# Properties
	collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
	def addCollectionPlan(self, value):
		checkType("XSDataStrategyResult", "setCollectionPlan", value, "XSDataCollectionPlan")
		self._collectionPlan.append(value)
	def insertCollectionPlan(self, index, value):
		checkType("XSDataStrategyResult", "setCollectionPlan", value, "XSDataCollectionPlan")
		self._collectionPlan[index] = value
	def export(self, outfile, level, name_='XSDataStrategyResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataStrategyResult'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for collectionPlan_ in self.getCollectionPlan():
			collectionPlan_.export(outfile, level, name_='collectionPlan')
		if self.getCollectionPlan() == []:
			warnEmptyAttribute("collectionPlan", "XSDataCollectionPlan")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlan':
			obj_ = XSDataCollectionPlan()
			obj_.build(child_)
			self.collectionPlan.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataStrategyResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataStrategyResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataStrategyResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataStrategyResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataStrategyResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataStrategyResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataStrategyResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataStrategyResult

class XSDataIntegrationInput(XSDataGeneratePredictionInput):
	"""This generalisation is not very logical in terms of names, it should be fixed after the prototype (see bug #49)."""
	def __init__(self, configuration=None, selectedIndexingSolution=None, dataCollection=None, experimentalConditionRefined=None, crystalRefined=None):
		XSDataGeneratePredictionInput.__init__(self, configuration, selectedIndexingSolution, dataCollection)
	
	
		checkType("XSDataIntegrationInput", "Constructor of XSDataIntegrationInput", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
		checkType("XSDataIntegrationInput", "Constructor of XSDataIntegrationInput", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
	def getCrystalRefined(self): return self._crystalRefined
	def setCrystalRefined(self, crystalRefined):
		checkType("XSDataIntegrationInput", "setCrystalRefined", crystalRefined, "XSDataCrystal")
		self._crystalRefined = crystalRefined
	def delCrystalRefined(self): self._crystalRefined = None
	# Properties
	crystalRefined = property(getCrystalRefined, setCrystalRefined, delCrystalRefined, "Property for crystalRefined")
	def getExperimentalConditionRefined(self): return self._experimentalConditionRefined
	def setExperimentalConditionRefined(self, experimentalConditionRefined):
		checkType("XSDataIntegrationInput", "setExperimentalConditionRefined", experimentalConditionRefined, "XSDataExperimentalCondition")
		self._experimentalConditionRefined = experimentalConditionRefined
	def delExperimentalConditionRefined(self): self._experimentalConditionRefined = None
	# Properties
	experimentalConditionRefined = property(getExperimentalConditionRefined, setExperimentalConditionRefined, delExperimentalConditionRefined, "Property for experimentalConditionRefined")
	def export(self, outfile, level, name_='XSDataIntegrationInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataIntegrationInput'):
		XSDataGeneratePredictionInput.exportChildren(self, outfile, level, name_)
		if self._crystalRefined is not None:
			self.crystalRefined.export(outfile, level, name_='crystalRefined')
		if self._experimentalConditionRefined is not None:
			self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalRefined':
			obj_ = XSDataCrystal()
			obj_.build(child_)
			self.setCrystalRefined(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalConditionRefined':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalConditionRefined(obj_)
		XSDataGeneratePredictionInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataIntegrationInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataIntegrationInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataIntegrationInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataIntegrationInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataIntegrationInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataIntegrationInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataIntegrationInput

class XSDataSampleCrystalMM(XSDataSampleCrystal):
	"""A particular crystal sample that contains a macro molecule defined by its chemical composition."""
	def __init__(self, susceptibility=None, size=None, shape=None, absorbedDoseRate=None, crystal=None, chemicalComposition=None):
		XSDataSampleCrystal.__init__(self, susceptibility, size, shape, absorbedDoseRate, crystal)
	
	
		checkType("XSDataSampleCrystalMM", "Constructor of XSDataSampleCrystalMM", chemicalComposition, "XSDataChemicalCompositionMM")
		self._chemicalComposition = chemicalComposition
	def getChemicalComposition(self): return self._chemicalComposition
	def setChemicalComposition(self, chemicalComposition):
		checkType("XSDataSampleCrystalMM", "setChemicalComposition", chemicalComposition, "XSDataChemicalCompositionMM")
		self._chemicalComposition = chemicalComposition
	def delChemicalComposition(self): self._chemicalComposition = None
	# Properties
	chemicalComposition = property(getChemicalComposition, setChemicalComposition, delChemicalComposition, "Property for chemicalComposition")
	def export(self, outfile, level, name_='XSDataSampleCrystalMM'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSampleCrystalMM'):
		XSDataSampleCrystal.exportChildren(self, outfile, level, name_)
		if self._chemicalComposition is not None:
			self.chemicalComposition.export(outfile, level, name_='chemicalComposition')
		else:
			warnEmptyAttribute("chemicalComposition", "XSDataChemicalCompositionMM")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chemicalComposition':
			obj_ = XSDataChemicalCompositionMM()
			obj_.build(child_)
			self.setChemicalComposition(obj_)
		XSDataSampleCrystal.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSampleCrystalMM" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSampleCrystalMM' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSampleCrystalMM is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSampleCrystalMM.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSampleCrystalMM()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSampleCrystalMM" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSampleCrystalMM()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSampleCrystalMM



# End of data representation classes.



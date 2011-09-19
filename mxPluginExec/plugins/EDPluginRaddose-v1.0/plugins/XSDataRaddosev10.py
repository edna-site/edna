#!/usr/bin/env python

#
# Generated Sat Sep 17 05:53::02 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataString
from XSDataCommon import XSDataAbsorbedDoseRate
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


class XSDataAtom(XSData):
	def __init__(self, symbol=None, numberOf=None, concentration=None):
		XSData.__init__(self, )
		checkType("XSDataAtom", "Constructor of XSDataAtom", concentration, "XSDataDouble")
		self.__concentration = concentration
		checkType("XSDataAtom", "Constructor of XSDataAtom", numberOf, "XSDataDouble")
		self.__numberOf = numberOf
		checkType("XSDataAtom", "Constructor of XSDataAtom", symbol, "XSDataString")
		self.__symbol = symbol
	def getConcentration(self): return self.__concentration
	def setConcentration(self, concentration):
		checkType("XSDataAtom", "setConcentration", concentration, "XSDataDouble")
		self.__concentration = concentration
	def delConcentration(self): self.__concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def getNumberOf(self): return self.__numberOf
	def setNumberOf(self, numberOf):
		checkType("XSDataAtom", "setNumberOf", numberOf, "XSDataDouble")
		self.__numberOf = numberOf
	def delNumberOf(self): self.__numberOf = None
	# Properties
	numberOf = property(getNumberOf, setNumberOf, delNumberOf, "Property for numberOf")
	def getSymbol(self): return self.__symbol
	def setSymbol(self, symbol):
		checkType("XSDataAtom", "setSymbol", symbol, "XSDataString")
		self.__symbol = symbol
	def delSymbol(self): self.__symbol = None
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
		if self.__concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
		else:
			warnEmptyAttribute("concentration", "XSDataDouble")
		if self.__numberOf is not None:
			self.numberOf.export(outfile, level, name_='numberOf')
		else:
			warnEmptyAttribute("numberOf", "XSDataDouble")
		if self.__symbol is not None:
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
			self.__atom = []
		else:
			checkType("XSDataAtomicComposition", "Constructor of XSDataAtomicComposition", atom, "list")
			self.__atom = atom
	def getAtom(self): return self.__atom
	def setAtom(self, atom):
		checkType("XSDataAtomicComposition", "setAtom", atom, "list")
		self.__atom = atom
	def delAtom(self): self.__atom = None
	# Properties
	atom = property(getAtom, setAtom, delAtom, "Property for atom")
	def addAtom(self, value):
		checkType("XSDataAtomicComposition", "setAtom", value, "XSDataAtom")
		self.__atom.append(value)
	def insertAtom(self, index, value):
		checkType("XSDataAtomicComposition", "setAtom", value, "XSDataAtom")
		self.__atom[index] = value
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

class XSDataCell(XSData):
	def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
		XSData.__init__(self, )
		checkType("XSDataCell", "Constructor of XSDataCell", angle_alpha, "XSDataAngle")
		self.__angle_alpha = angle_alpha
		checkType("XSDataCell", "Constructor of XSDataCell", angle_beta, "XSDataAngle")
		self.__angle_beta = angle_beta
		checkType("XSDataCell", "Constructor of XSDataCell", angle_gamma, "XSDataAngle")
		self.__angle_gamma = angle_gamma
		checkType("XSDataCell", "Constructor of XSDataCell", length_a, "XSDataLength")
		self.__length_a = length_a
		checkType("XSDataCell", "Constructor of XSDataCell", length_b, "XSDataLength")
		self.__length_b = length_b
		checkType("XSDataCell", "Constructor of XSDataCell", length_c, "XSDataLength")
		self.__length_c = length_c
	def getAngle_alpha(self): return self.__angle_alpha
	def setAngle_alpha(self, angle_alpha):
		checkType("XSDataCell", "setAngle_alpha", angle_alpha, "XSDataAngle")
		self.__angle_alpha = angle_alpha
	def delAngle_alpha(self): self.__angle_alpha = None
	# Properties
	angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
	def getAngle_beta(self): return self.__angle_beta
	def setAngle_beta(self, angle_beta):
		checkType("XSDataCell", "setAngle_beta", angle_beta, "XSDataAngle")
		self.__angle_beta = angle_beta
	def delAngle_beta(self): self.__angle_beta = None
	# Properties
	angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
	def getAngle_gamma(self): return self.__angle_gamma
	def setAngle_gamma(self, angle_gamma):
		checkType("XSDataCell", "setAngle_gamma", angle_gamma, "XSDataAngle")
		self.__angle_gamma = angle_gamma
	def delAngle_gamma(self): self.__angle_gamma = None
	# Properties
	angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
	def getLength_a(self): return self.__length_a
	def setLength_a(self, length_a):
		checkType("XSDataCell", "setLength_a", length_a, "XSDataLength")
		self.__length_a = length_a
	def delLength_a(self): self.__length_a = None
	# Properties
	length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
	def getLength_b(self): return self.__length_b
	def setLength_b(self, length_b):
		checkType("XSDataCell", "setLength_b", length_b, "XSDataLength")
		self.__length_b = length_b
	def delLength_b(self): self.__length_b = None
	# Properties
	length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
	def getLength_c(self): return self.__length_c
	def setLength_c(self, length_c):
		checkType("XSDataCell", "setLength_c", length_c, "XSDataLength")
		self.__length_c = length_c
	def delLength_c(self): self.__length_c = None
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
		if self.__angle_alpha is not None:
			self.angle_alpha.export(outfile, level, name_='angle_alpha')
		else:
			warnEmptyAttribute("angle_alpha", "XSDataAngle")
		if self.__angle_beta is not None:
			self.angle_beta.export(outfile, level, name_='angle_beta')
		else:
			warnEmptyAttribute("angle_beta", "XSDataAngle")
		if self.__angle_gamma is not None:
			self.angle_gamma.export(outfile, level, name_='angle_gamma')
		else:
			warnEmptyAttribute("angle_gamma", "XSDataAngle")
		if self.__length_a is not None:
			self.length_a.export(outfile, level, name_='length_a')
		else:
			warnEmptyAttribute("length_a", "XSDataLength")
		if self.__length_b is not None:
			self.length_b.export(outfile, level, name_='length_b')
		else:
			warnEmptyAttribute("length_b", "XSDataLength")
		if self.__length_c is not None:
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

class XSDataRaddoseInput(XSDataInput):
	def __init__(self, configuration=None, numberOfImages=None, crystalSize=None, crystalSATM=None, crystalPATM=None, crystalNRNA=None, crystalNRES=None, crystalNMON=None, crystalNDNA=None, crystalCell=None, beamWavelength=None, beamSize=None, beamFlux=None, beamExposureTime=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", beamExposureTime, "XSDataTime")
		self.__beamExposureTime = beamExposureTime
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", beamFlux, "XSDataFlux")
		self.__beamFlux = beamFlux
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", beamSize, "XSDataSize")
		self.__beamSize = beamSize
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", beamWavelength, "XSDataWavelength")
		self.__beamWavelength = beamWavelength
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalCell, "XSDataCell")
		self.__crystalCell = crystalCell
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalNDNA, "XSDataInteger")
		self.__crystalNDNA = crystalNDNA
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalNMON, "XSDataInteger")
		self.__crystalNMON = crystalNMON
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalNRES, "XSDataInteger")
		self.__crystalNRES = crystalNRES
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalNRNA, "XSDataInteger")
		self.__crystalNRNA = crystalNRNA
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalPATM, "XSDataAtomicComposition")
		self.__crystalPATM = crystalPATM
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalSATM, "XSDataAtomicComposition")
		self.__crystalSATM = crystalSATM
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", crystalSize, "XSDataSize")
		self.__crystalSize = crystalSize
		checkType("XSDataRaddoseInput", "Constructor of XSDataRaddoseInput", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def getBeamExposureTime(self): return self.__beamExposureTime
	def setBeamExposureTime(self, beamExposureTime):
		checkType("XSDataRaddoseInput", "setBeamExposureTime", beamExposureTime, "XSDataTime")
		self.__beamExposureTime = beamExposureTime
	def delBeamExposureTime(self): self.__beamExposureTime = None
	# Properties
	beamExposureTime = property(getBeamExposureTime, setBeamExposureTime, delBeamExposureTime, "Property for beamExposureTime")
	def getBeamFlux(self): return self.__beamFlux
	def setBeamFlux(self, beamFlux):
		checkType("XSDataRaddoseInput", "setBeamFlux", beamFlux, "XSDataFlux")
		self.__beamFlux = beamFlux
	def delBeamFlux(self): self.__beamFlux = None
	# Properties
	beamFlux = property(getBeamFlux, setBeamFlux, delBeamFlux, "Property for beamFlux")
	def getBeamSize(self): return self.__beamSize
	def setBeamSize(self, beamSize):
		checkType("XSDataRaddoseInput", "setBeamSize", beamSize, "XSDataSize")
		self.__beamSize = beamSize
	def delBeamSize(self): self.__beamSize = None
	# Properties
	beamSize = property(getBeamSize, setBeamSize, delBeamSize, "Property for beamSize")
	def getBeamWavelength(self): return self.__beamWavelength
	def setBeamWavelength(self, beamWavelength):
		checkType("XSDataRaddoseInput", "setBeamWavelength", beamWavelength, "XSDataWavelength")
		self.__beamWavelength = beamWavelength
	def delBeamWavelength(self): self.__beamWavelength = None
	# Properties
	beamWavelength = property(getBeamWavelength, setBeamWavelength, delBeamWavelength, "Property for beamWavelength")
	def getCrystalCell(self): return self.__crystalCell
	def setCrystalCell(self, crystalCell):
		checkType("XSDataRaddoseInput", "setCrystalCell", crystalCell, "XSDataCell")
		self.__crystalCell = crystalCell
	def delCrystalCell(self): self.__crystalCell = None
	# Properties
	crystalCell = property(getCrystalCell, setCrystalCell, delCrystalCell, "Property for crystalCell")
	def getCrystalNDNA(self): return self.__crystalNDNA
	def setCrystalNDNA(self, crystalNDNA):
		checkType("XSDataRaddoseInput", "setCrystalNDNA", crystalNDNA, "XSDataInteger")
		self.__crystalNDNA = crystalNDNA
	def delCrystalNDNA(self): self.__crystalNDNA = None
	# Properties
	crystalNDNA = property(getCrystalNDNA, setCrystalNDNA, delCrystalNDNA, "Property for crystalNDNA")
	def getCrystalNMON(self): return self.__crystalNMON
	def setCrystalNMON(self, crystalNMON):
		checkType("XSDataRaddoseInput", "setCrystalNMON", crystalNMON, "XSDataInteger")
		self.__crystalNMON = crystalNMON
	def delCrystalNMON(self): self.__crystalNMON = None
	# Properties
	crystalNMON = property(getCrystalNMON, setCrystalNMON, delCrystalNMON, "Property for crystalNMON")
	def getCrystalNRES(self): return self.__crystalNRES
	def setCrystalNRES(self, crystalNRES):
		checkType("XSDataRaddoseInput", "setCrystalNRES", crystalNRES, "XSDataInteger")
		self.__crystalNRES = crystalNRES
	def delCrystalNRES(self): self.__crystalNRES = None
	# Properties
	crystalNRES = property(getCrystalNRES, setCrystalNRES, delCrystalNRES, "Property for crystalNRES")
	def getCrystalNRNA(self): return self.__crystalNRNA
	def setCrystalNRNA(self, crystalNRNA):
		checkType("XSDataRaddoseInput", "setCrystalNRNA", crystalNRNA, "XSDataInteger")
		self.__crystalNRNA = crystalNRNA
	def delCrystalNRNA(self): self.__crystalNRNA = None
	# Properties
	crystalNRNA = property(getCrystalNRNA, setCrystalNRNA, delCrystalNRNA, "Property for crystalNRNA")
	def getCrystalPATM(self): return self.__crystalPATM
	def setCrystalPATM(self, crystalPATM):
		checkType("XSDataRaddoseInput", "setCrystalPATM", crystalPATM, "XSDataAtomicComposition")
		self.__crystalPATM = crystalPATM
	def delCrystalPATM(self): self.__crystalPATM = None
	# Properties
	crystalPATM = property(getCrystalPATM, setCrystalPATM, delCrystalPATM, "Property for crystalPATM")
	def getCrystalSATM(self): return self.__crystalSATM
	def setCrystalSATM(self, crystalSATM):
		checkType("XSDataRaddoseInput", "setCrystalSATM", crystalSATM, "XSDataAtomicComposition")
		self.__crystalSATM = crystalSATM
	def delCrystalSATM(self): self.__crystalSATM = None
	# Properties
	crystalSATM = property(getCrystalSATM, setCrystalSATM, delCrystalSATM, "Property for crystalSATM")
	def getCrystalSize(self): return self.__crystalSize
	def setCrystalSize(self, crystalSize):
		checkType("XSDataRaddoseInput", "setCrystalSize", crystalSize, "XSDataSize")
		self.__crystalSize = crystalSize
	def delCrystalSize(self): self.__crystalSize = None
	# Properties
	crystalSize = property(getCrystalSize, setCrystalSize, delCrystalSize, "Property for crystalSize")
	def getNumberOfImages(self): return self.__numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataRaddoseInput", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def delNumberOfImages(self): self.__numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def export(self, outfile, level, name_='XSDataRaddoseInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRaddoseInput'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__beamExposureTime is not None:
			self.beamExposureTime.export(outfile, level, name_='beamExposureTime')
		else:
			warnEmptyAttribute("beamExposureTime", "XSDataTime")
		if self.__beamFlux is not None:
			self.beamFlux.export(outfile, level, name_='beamFlux')
		else:
			warnEmptyAttribute("beamFlux", "XSDataFlux")
		if self.__beamSize is not None:
			self.beamSize.export(outfile, level, name_='beamSize')
		else:
			warnEmptyAttribute("beamSize", "XSDataSize")
		if self.__beamWavelength is not None:
			self.beamWavelength.export(outfile, level, name_='beamWavelength')
		else:
			warnEmptyAttribute("beamWavelength", "XSDataWavelength")
		if self.__crystalCell is not None:
			self.crystalCell.export(outfile, level, name_='crystalCell')
		else:
			warnEmptyAttribute("crystalCell", "XSDataCell")
		if self.__crystalNDNA is not None:
			self.crystalNDNA.export(outfile, level, name_='crystalNDNA')
		else:
			warnEmptyAttribute("crystalNDNA", "XSDataInteger")
		if self.__crystalNMON is not None:
			self.crystalNMON.export(outfile, level, name_='crystalNMON')
		else:
			warnEmptyAttribute("crystalNMON", "XSDataInteger")
		if self.__crystalNRES is not None:
			self.crystalNRES.export(outfile, level, name_='crystalNRES')
		else:
			warnEmptyAttribute("crystalNRES", "XSDataInteger")
		if self.__crystalNRNA is not None:
			self.crystalNRNA.export(outfile, level, name_='crystalNRNA')
		else:
			warnEmptyAttribute("crystalNRNA", "XSDataInteger")
		if self.__crystalPATM is not None:
			self.crystalPATM.export(outfile, level, name_='crystalPATM')
		else:
			warnEmptyAttribute("crystalPATM", "XSDataAtomicComposition")
		if self.__crystalSATM is not None:
			self.crystalSATM.export(outfile, level, name_='crystalSATM')
		else:
			warnEmptyAttribute("crystalSATM", "XSDataAtomicComposition")
		if self.__crystalSize is not None:
			self.crystalSize.export(outfile, level, name_='crystalSize')
		else:
			warnEmptyAttribute("crystalSize", "XSDataSize")
		if self.__numberOfImages is not None:
			self.numberOfImages.export(outfile, level, name_='numberOfImages')
		else:
			warnEmptyAttribute("numberOfImages", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setBeamExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamFlux':
			obj_ = XSDataFlux()
			obj_.build(child_)
			self.setBeamFlux(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSize':
			obj_ = XSDataSize()
			obj_.build(child_)
			self.setBeamSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamWavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setBeamWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalCell':
			obj_ = XSDataCell()
			obj_.build(child_)
			self.setCrystalCell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalNDNA':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCrystalNDNA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalNMON':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCrystalNMON(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalNRES':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCrystalNRES(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalNRNA':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCrystalNRNA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalPATM':
			obj_ = XSDataAtomicComposition()
			obj_.build(child_)
			self.setCrystalPATM(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalSATM':
			obj_ = XSDataAtomicComposition()
			obj_.build(child_)
			self.setCrystalSATM(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalSize':
			obj_ = XSDataSize()
			obj_.build(child_)
			self.setCrystalSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfImages(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRaddoseInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRaddoseInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRaddoseInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRaddoseInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRaddoseInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRaddoseInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRaddoseInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRaddoseInput

class XSDataRaddoseOutput(XSDataResult):
	def __init__(self, status=None, timeToReachHendersonLimit=None, pathToLogFile=None, absorbedDoseRate=None, absorbedDose=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataRaddoseOutput", "Constructor of XSDataRaddoseOutput", absorbedDose, "XSDataDouble")
		self.__absorbedDose = absorbedDose
		checkType("XSDataRaddoseOutput", "Constructor of XSDataRaddoseOutput", absorbedDoseRate, "XSDataAbsorbedDoseRate")
		self.__absorbedDoseRate = absorbedDoseRate
		checkType("XSDataRaddoseOutput", "Constructor of XSDataRaddoseOutput", pathToLogFile, "XSDataFile")
		self.__pathToLogFile = pathToLogFile
		checkType("XSDataRaddoseOutput", "Constructor of XSDataRaddoseOutput", timeToReachHendersonLimit, "XSDataTime")
		self.__timeToReachHendersonLimit = timeToReachHendersonLimit
	def getAbsorbedDose(self): return self.__absorbedDose
	def setAbsorbedDose(self, absorbedDose):
		checkType("XSDataRaddoseOutput", "setAbsorbedDose", absorbedDose, "XSDataDouble")
		self.__absorbedDose = absorbedDose
	def delAbsorbedDose(self): self.__absorbedDose = None
	# Properties
	absorbedDose = property(getAbsorbedDose, setAbsorbedDose, delAbsorbedDose, "Property for absorbedDose")
	def getAbsorbedDoseRate(self): return self.__absorbedDoseRate
	def setAbsorbedDoseRate(self, absorbedDoseRate):
		checkType("XSDataRaddoseOutput", "setAbsorbedDoseRate", absorbedDoseRate, "XSDataAbsorbedDoseRate")
		self.__absorbedDoseRate = absorbedDoseRate
	def delAbsorbedDoseRate(self): self.__absorbedDoseRate = None
	# Properties
	absorbedDoseRate = property(getAbsorbedDoseRate, setAbsorbedDoseRate, delAbsorbedDoseRate, "Property for absorbedDoseRate")
	def getPathToLogFile(self): return self.__pathToLogFile
	def setPathToLogFile(self, pathToLogFile):
		checkType("XSDataRaddoseOutput", "setPathToLogFile", pathToLogFile, "XSDataFile")
		self.__pathToLogFile = pathToLogFile
	def delPathToLogFile(self): self.__pathToLogFile = None
	# Properties
	pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
	def getTimeToReachHendersonLimit(self): return self.__timeToReachHendersonLimit
	def setTimeToReachHendersonLimit(self, timeToReachHendersonLimit):
		checkType("XSDataRaddoseOutput", "setTimeToReachHendersonLimit", timeToReachHendersonLimit, "XSDataTime")
		self.__timeToReachHendersonLimit = timeToReachHendersonLimit
	def delTimeToReachHendersonLimit(self): self.__timeToReachHendersonLimit = None
	# Properties
	timeToReachHendersonLimit = property(getTimeToReachHendersonLimit, setTimeToReachHendersonLimit, delTimeToReachHendersonLimit, "Property for timeToReachHendersonLimit")
	def export(self, outfile, level, name_='XSDataRaddoseOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRaddoseOutput'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__absorbedDose is not None:
			self.absorbedDose.export(outfile, level, name_='absorbedDose')
		if self.__absorbedDoseRate is not None:
			self.absorbedDoseRate.export(outfile, level, name_='absorbedDoseRate')
		if self.__pathToLogFile is not None:
			self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
		if self.__timeToReachHendersonLimit is not None:
			self.timeToReachHendersonLimit.export(outfile, level, name_='timeToReachHendersonLimit')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absorbedDose':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAbsorbedDose(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absorbedDoseRate':
			obj_ = XSDataAbsorbedDoseRate()
			obj_.build(child_)
			self.setAbsorbedDoseRate(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeToReachHendersonLimit':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTimeToReachHendersonLimit(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRaddoseOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRaddoseOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRaddoseOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRaddoseOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRaddoseOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRaddoseOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRaddoseOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRaddoseOutput



# End of data representation classes.



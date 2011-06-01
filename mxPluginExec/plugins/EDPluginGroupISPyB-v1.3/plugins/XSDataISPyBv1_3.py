#!/usr/bin/env python

#
# Generated Wed Apr 20 02:45::46 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataImage




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


class AutoProc:
	def __init__(self, refinedCell_gamma=None, refinedCell_beta=None, refinedCell_alpha=None, refinedCell_c=None, refinedCell_b=None, refinedCell_a=None, spaceGroup=None):
		self.__spaceGroup = spaceGroup
		self.__refinedCell_a = refinedCell_a
		self.__refinedCell_b = refinedCell_b
		self.__refinedCell_c = refinedCell_c
		self.__refinedCell_alpha = refinedCell_alpha
		self.__refinedCell_beta = refinedCell_beta
		self.__refinedCell_gamma = refinedCell_gamma
	def getSpaceGroup(self): return self.__spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("AutoProc", "setSpaceGroup", spaceGroup, "string")
		self.__spaceGroup = spaceGroup
	def delSpaceGroup(self): self.__spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def getRefinedCell_a(self): return self.__refinedCell_a
	def setRefinedCell_a(self, refinedCell_a):
		checkType("AutoProc", "setRefinedCell_a", refinedCell_a, "string")
		self.__refinedCell_a = refinedCell_a
	def delRefinedCell_a(self): self.__refinedCell_a = None
	# Properties
	refinedCell_a = property(getRefinedCell_a, setRefinedCell_a, delRefinedCell_a, "Property for refinedCell_a")
	def getRefinedCell_b(self): return self.__refinedCell_b
	def setRefinedCell_b(self, refinedCell_b):
		checkType("AutoProc", "setRefinedCell_b", refinedCell_b, "string")
		self.__refinedCell_b = refinedCell_b
	def delRefinedCell_b(self): self.__refinedCell_b = None
	# Properties
	refinedCell_b = property(getRefinedCell_b, setRefinedCell_b, delRefinedCell_b, "Property for refinedCell_b")
	def getRefinedCell_c(self): return self.__refinedCell_c
	def setRefinedCell_c(self, refinedCell_c):
		checkType("AutoProc", "setRefinedCell_c", refinedCell_c, "string")
		self.__refinedCell_c = refinedCell_c
	def delRefinedCell_c(self): self.__refinedCell_c = None
	# Properties
	refinedCell_c = property(getRefinedCell_c, setRefinedCell_c, delRefinedCell_c, "Property for refinedCell_c")
	def getRefinedCell_alpha(self): return self.__refinedCell_alpha
	def setRefinedCell_alpha(self, refinedCell_alpha):
		checkType("AutoProc", "setRefinedCell_alpha", refinedCell_alpha, "string")
		self.__refinedCell_alpha = refinedCell_alpha
	def delRefinedCell_alpha(self): self.__refinedCell_alpha = None
	# Properties
	refinedCell_alpha = property(getRefinedCell_alpha, setRefinedCell_alpha, delRefinedCell_alpha, "Property for refinedCell_alpha")
	def getRefinedCell_beta(self): return self.__refinedCell_beta
	def setRefinedCell_beta(self, refinedCell_beta):
		checkType("AutoProc", "setRefinedCell_beta", refinedCell_beta, "string")
		self.__refinedCell_beta = refinedCell_beta
	def delRefinedCell_beta(self): self.__refinedCell_beta = None
	# Properties
	refinedCell_beta = property(getRefinedCell_beta, setRefinedCell_beta, delRefinedCell_beta, "Property for refinedCell_beta")
	def getRefinedCell_gamma(self): return self.__refinedCell_gamma
	def setRefinedCell_gamma(self, refinedCell_gamma):
		checkType("AutoProc", "setRefinedCell_gamma", refinedCell_gamma, "string")
		self.__refinedCell_gamma = refinedCell_gamma
	def delRefinedCell_gamma(self): self.__refinedCell_gamma = None
	# Properties
	refinedCell_gamma = property(getRefinedCell_gamma, setRefinedCell_gamma, delRefinedCell_gamma, "Property for refinedCell_gamma")
	def export(self, outfile, level, name_='AutoProc'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProc'):
		pass
		if self.__spaceGroup is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<spaceGroup>%s</spaceGroup>\n' % self.__spaceGroup))
		else:
			warnEmptyAttribute("spaceGroup", "string")
		if self.__refinedCell_a is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_a>%s</refinedCell_a>\n' % self.__refinedCell_a))
		else:
			warnEmptyAttribute("refinedCell_a", "string")
		if self.__refinedCell_b is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_b>%s</refinedCell_b>\n' % self.__refinedCell_b))
		else:
			warnEmptyAttribute("refinedCell_b", "string")
		if self.__refinedCell_c is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_c>%s</refinedCell_c>\n' % self.__refinedCell_c))
		else:
			warnEmptyAttribute("refinedCell_c", "string")
		if self.__refinedCell_alpha is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_alpha>%s</refinedCell_alpha>\n' % self.__refinedCell_alpha))
		else:
			warnEmptyAttribute("refinedCell_alpha", "string")
		if self.__refinedCell_beta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_beta>%s</refinedCell_beta>\n' % self.__refinedCell_beta))
		else:
			warnEmptyAttribute("refinedCell_beta", "string")
		if self.__refinedCell_gamma is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_gamma>%s</refinedCell_gamma>\n' % self.__refinedCell_gamma))
		else:
			warnEmptyAttribute("refinedCell_gamma", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spaceGroup':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__spaceGroup = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_a':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_a = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_b':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_b = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_c':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_c = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_alpha':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_alpha = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_beta':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_beta = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_gamma':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__refinedCell_gamma = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProc" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProc' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProc.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProc()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProc" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProc()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProc

class AutoProcContainer:
	def __init__(self, AutoProcProgramContainer=None, AutoProcScalingContainer=None, AutoProc=None):
		self.__AutoProc = AutoProc
		self.__AutoProcScalingContainer = AutoProcScalingContainer
		self.__AutoProcProgramContainer = AutoProcProgramContainer
	def getAutoProc(self): return self.__AutoProc
	def setAutoProc(self, AutoProc):
		checkType("AutoProcContainer", "setAutoProc", AutoProc, "AutoProc")
		self.__AutoProc = AutoProc
	def delAutoProc(self): self.__AutoProc = None
	# Properties
	AutoProc = property(getAutoProc, setAutoProc, delAutoProc, "Property for AutoProc")
	def getAutoProcScalingContainer(self): return self.__AutoProcScalingContainer
	def setAutoProcScalingContainer(self, AutoProcScalingContainer):
		checkType("AutoProcContainer", "setAutoProcScalingContainer", AutoProcScalingContainer, "AutoProcScalingContainer")
		self.__AutoProcScalingContainer = AutoProcScalingContainer
	def delAutoProcScalingContainer(self): self.__AutoProcScalingContainer = None
	# Properties
	AutoProcScalingContainer = property(getAutoProcScalingContainer, setAutoProcScalingContainer, delAutoProcScalingContainer, "Property for AutoProcScalingContainer")
	def getAutoProcProgramContainer(self): return self.__AutoProcProgramContainer
	def setAutoProcProgramContainer(self, AutoProcProgramContainer):
		checkType("AutoProcContainer", "setAutoProcProgramContainer", AutoProcProgramContainer, "AutoProcProgramContainer")
		self.__AutoProcProgramContainer = AutoProcProgramContainer
	def delAutoProcProgramContainer(self): self.__AutoProcProgramContainer = None
	# Properties
	AutoProcProgramContainer = property(getAutoProcProgramContainer, setAutoProcProgramContainer, delAutoProcProgramContainer, "Property for AutoProcProgramContainer")
	def export(self, outfile, level, name_='AutoProcContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcContainer'):
		pass
		if self.__AutoProc is not None:
			self.AutoProc.export(outfile, level, name_='AutoProc')
		else:
			warnEmptyAttribute("AutoProc", "AutoProc")
		if self.__AutoProcScalingContainer is not None:
			self.AutoProcScalingContainer.export(outfile, level, name_='AutoProcScalingContainer')
		else:
			warnEmptyAttribute("AutoProcScalingContainer", "AutoProcScalingContainer")
		if self.__AutoProcProgramContainer is not None:
			self.AutoProcProgramContainer.export(outfile, level, name_='AutoProcProgramContainer')
		else:
			warnEmptyAttribute("AutoProcProgramContainer", "AutoProcProgramContainer")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProc':
			obj_ = AutoProc()
			obj_.build(child_)
			self.setAutoProc(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcScalingContainer':
			obj_ = AutoProcScalingContainer()
			obj_.build(child_)
			self.setAutoProcScalingContainer(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcProgramContainer':
			obj_ = AutoProcProgramContainer()
			obj_.build(child_)
			self.setAutoProcProgramContainer(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcContainer' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcContainer

class AutoProcIntegration:
	def __init__(self, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, beamVectorZ=None, beamVectorY=None, beamVectorX=None, rotationAxisZ=None, rotationAxisY=None, rotationAxisX=None, refinedYbeam=None, refinedXbeam=None, refinedDetectorDistance=None, endImageNumber=None, startImageNumber=None):
		self.__startImageNumber = startImageNumber
		self.__endImageNumber = endImageNumber
		self.__refinedDetectorDistance = refinedDetectorDistance
		self.__refinedXbeam = refinedXbeam
		self.__refinedYbeam = refinedYbeam
		self.__rotationAxisX = rotationAxisX
		self.__rotationAxisY = rotationAxisY
		self.__rotationAxisZ = rotationAxisZ
		self.__beamVectorX = beamVectorX
		self.__beamVectorY = beamVectorY
		self.__beamVectorZ = beamVectorZ
		self.__cell_a = cell_a
		self.__cell_b = cell_b
		self.__cell_c = cell_c
		self.__cell_alpha = cell_alpha
		self.__cell_beta = cell_beta
		self.__cell_gamma = cell_gamma
	def getStartImageNumber(self): return self.__startImageNumber
	def setStartImageNumber(self, startImageNumber):
		checkType("AutoProcIntegration", "setStartImageNumber", startImageNumber, "integer")
		self.__startImageNumber = startImageNumber
	def delStartImageNumber(self): self.__startImageNumber = None
	# Properties
	startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
	def getEndImageNumber(self): return self.__endImageNumber
	def setEndImageNumber(self, endImageNumber):
		checkType("AutoProcIntegration", "setEndImageNumber", endImageNumber, "integer")
		self.__endImageNumber = endImageNumber
	def delEndImageNumber(self): self.__endImageNumber = None
	# Properties
	endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
	def getRefinedDetectorDistance(self): return self.__refinedDetectorDistance
	def setRefinedDetectorDistance(self, refinedDetectorDistance):
		checkType("AutoProcIntegration", "setRefinedDetectorDistance", refinedDetectorDistance, "float")
		self.__refinedDetectorDistance = refinedDetectorDistance
	def delRefinedDetectorDistance(self): self.__refinedDetectorDistance = None
	# Properties
	refinedDetectorDistance = property(getRefinedDetectorDistance, setRefinedDetectorDistance, delRefinedDetectorDistance, "Property for refinedDetectorDistance")
	def getRefinedXbeam(self): return self.__refinedXbeam
	def setRefinedXbeam(self, refinedXbeam):
		checkType("AutoProcIntegration", "setRefinedXbeam", refinedXbeam, "float")
		self.__refinedXbeam = refinedXbeam
	def delRefinedXbeam(self): self.__refinedXbeam = None
	# Properties
	refinedXbeam = property(getRefinedXbeam, setRefinedXbeam, delRefinedXbeam, "Property for refinedXbeam")
	def getRefinedYbeam(self): return self.__refinedYbeam
	def setRefinedYbeam(self, refinedYbeam):
		checkType("AutoProcIntegration", "setRefinedYbeam", refinedYbeam, "float")
		self.__refinedYbeam = refinedYbeam
	def delRefinedYbeam(self): self.__refinedYbeam = None
	# Properties
	refinedYbeam = property(getRefinedYbeam, setRefinedYbeam, delRefinedYbeam, "Property for refinedYbeam")
	def getRotationAxisX(self): return self.__rotationAxisX
	def setRotationAxisX(self, rotationAxisX):
		checkType("AutoProcIntegration", "setRotationAxisX", rotationAxisX, "float")
		self.__rotationAxisX = rotationAxisX
	def delRotationAxisX(self): self.__rotationAxisX = None
	# Properties
	rotationAxisX = property(getRotationAxisX, setRotationAxisX, delRotationAxisX, "Property for rotationAxisX")
	def getRotationAxisY(self): return self.__rotationAxisY
	def setRotationAxisY(self, rotationAxisY):
		checkType("AutoProcIntegration", "setRotationAxisY", rotationAxisY, "float")
		self.__rotationAxisY = rotationAxisY
	def delRotationAxisY(self): self.__rotationAxisY = None
	# Properties
	rotationAxisY = property(getRotationAxisY, setRotationAxisY, delRotationAxisY, "Property for rotationAxisY")
	def getRotationAxisZ(self): return self.__rotationAxisZ
	def setRotationAxisZ(self, rotationAxisZ):
		checkType("AutoProcIntegration", "setRotationAxisZ", rotationAxisZ, "float")
		self.__rotationAxisZ = rotationAxisZ
	def delRotationAxisZ(self): self.__rotationAxisZ = None
	# Properties
	rotationAxisZ = property(getRotationAxisZ, setRotationAxisZ, delRotationAxisZ, "Property for rotationAxisZ")
	def getBeamVectorX(self): return self.__beamVectorX
	def setBeamVectorX(self, beamVectorX):
		checkType("AutoProcIntegration", "setBeamVectorX", beamVectorX, "float")
		self.__beamVectorX = beamVectorX
	def delBeamVectorX(self): self.__beamVectorX = None
	# Properties
	beamVectorX = property(getBeamVectorX, setBeamVectorX, delBeamVectorX, "Property for beamVectorX")
	def getBeamVectorY(self): return self.__beamVectorY
	def setBeamVectorY(self, beamVectorY):
		checkType("AutoProcIntegration", "setBeamVectorY", beamVectorY, "float")
		self.__beamVectorY = beamVectorY
	def delBeamVectorY(self): self.__beamVectorY = None
	# Properties
	beamVectorY = property(getBeamVectorY, setBeamVectorY, delBeamVectorY, "Property for beamVectorY")
	def getBeamVectorZ(self): return self.__beamVectorZ
	def setBeamVectorZ(self, beamVectorZ):
		checkType("AutoProcIntegration", "setBeamVectorZ", beamVectorZ, "float")
		self.__beamVectorZ = beamVectorZ
	def delBeamVectorZ(self): self.__beamVectorZ = None
	# Properties
	beamVectorZ = property(getBeamVectorZ, setBeamVectorZ, delBeamVectorZ, "Property for beamVectorZ")
	def getCell_a(self): return self.__cell_a
	def setCell_a(self, cell_a):
		checkType("AutoProcIntegration", "setCell_a", cell_a, "float")
		self.__cell_a = cell_a
	def delCell_a(self): self.__cell_a = None
	# Properties
	cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
	def getCell_b(self): return self.__cell_b
	def setCell_b(self, cell_b):
		checkType("AutoProcIntegration", "setCell_b", cell_b, "float")
		self.__cell_b = cell_b
	def delCell_b(self): self.__cell_b = None
	# Properties
	cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
	def getCell_c(self): return self.__cell_c
	def setCell_c(self, cell_c):
		checkType("AutoProcIntegration", "setCell_c", cell_c, "float")
		self.__cell_c = cell_c
	def delCell_c(self): self.__cell_c = None
	# Properties
	cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
	def getCell_alpha(self): return self.__cell_alpha
	def setCell_alpha(self, cell_alpha):
		checkType("AutoProcIntegration", "setCell_alpha", cell_alpha, "float")
		self.__cell_alpha = cell_alpha
	def delCell_alpha(self): self.__cell_alpha = None
	# Properties
	cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
	def getCell_beta(self): return self.__cell_beta
	def setCell_beta(self, cell_beta):
		checkType("AutoProcIntegration", "setCell_beta", cell_beta, "float")
		self.__cell_beta = cell_beta
	def delCell_beta(self): self.__cell_beta = None
	# Properties
	cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
	def getCell_gamma(self): return self.__cell_gamma
	def setCell_gamma(self, cell_gamma):
		checkType("AutoProcIntegration", "setCell_gamma", cell_gamma, "float")
		self.__cell_gamma = cell_gamma
	def delCell_gamma(self): self.__cell_gamma = None
	# Properties
	cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
	def export(self, outfile, level, name_='AutoProcIntegration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcIntegration'):
		pass
		if self.__startImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self.__startImageNumber))
		else:
			warnEmptyAttribute("startImageNumber", "integer")
		if self.__endImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<endImageNumber>%d</endImageNumber>\n' % self.__endImageNumber))
		else:
			warnEmptyAttribute("endImageNumber", "integer")
		if self.__refinedDetectorDistance is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedDetectorDistance>%e</refinedDetectorDistance>\n' % self.__refinedDetectorDistance))
		else:
			warnEmptyAttribute("refinedDetectorDistance", "float")
		if self.__refinedXbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedXbeam>%e</refinedXbeam>\n' % self.__refinedXbeam))
		else:
			warnEmptyAttribute("refinedXbeam", "float")
		if self.__refinedYbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedYbeam>%e</refinedYbeam>\n' % self.__refinedYbeam))
		else:
			warnEmptyAttribute("refinedYbeam", "float")
		if self.__rotationAxisX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisX>%e</rotationAxisX>\n' % self.__rotationAxisX))
		else:
			warnEmptyAttribute("rotationAxisX", "float")
		if self.__rotationAxisY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisY>%e</rotationAxisY>\n' % self.__rotationAxisY))
		else:
			warnEmptyAttribute("rotationAxisY", "float")
		if self.__rotationAxisZ is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisZ>%e</rotationAxisZ>\n' % self.__rotationAxisZ))
		else:
			warnEmptyAttribute("rotationAxisZ", "float")
		if self.__beamVectorX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorX>%e</beamVectorX>\n' % self.__beamVectorX))
		else:
			warnEmptyAttribute("beamVectorX", "float")
		if self.__beamVectorY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorY>%e</beamVectorY>\n' % self.__beamVectorY))
		else:
			warnEmptyAttribute("beamVectorY", "float")
		if self.__beamVectorZ is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorZ>%e</beamVectorZ>\n' % self.__beamVectorZ))
		else:
			warnEmptyAttribute("beamVectorZ", "float")
		if self.__cell_a is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_a>%e</cell_a>\n' % self.__cell_a))
		else:
			warnEmptyAttribute("cell_a", "float")
		if self.__cell_b is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_b>%e</cell_b>\n' % self.__cell_b))
		else:
			warnEmptyAttribute("cell_b", "float")
		if self.__cell_c is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_c>%e</cell_c>\n' % self.__cell_c))
		else:
			warnEmptyAttribute("cell_c", "float")
		if self.__cell_alpha is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_alpha>%e</cell_alpha>\n' % self.__cell_alpha))
		else:
			warnEmptyAttribute("cell_alpha", "float")
		if self.__cell_beta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_beta>%e</cell_beta>\n' % self.__cell_beta))
		else:
			warnEmptyAttribute("cell_beta", "float")
		if self.__cell_gamma is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_gamma>%e</cell_gamma>\n' % self.__cell_gamma))
		else:
			warnEmptyAttribute("cell_gamma", "float")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startImageNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__startImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'endImageNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__endImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedDetectorDistance':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__refinedDetectorDistance = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedXbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__refinedXbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedYbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__refinedYbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rotationAxisX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rotationAxisY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisZ':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rotationAxisZ = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beamVectorX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beamVectorY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorZ':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beamVectorZ = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_a':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_a = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_b':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_b = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_c':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_c = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_alpha':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_alpha = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_beta':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_beta = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_gamma':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__cell_gamma = fval_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcIntegration' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcIntegration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcIntegration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcIntegration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcIntegration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcIntegration

class AutoProcIntegrationContainer:
	def __init__(self, AutoProcIntegration=None, Image=None):
		self.__Image = Image
		self.__AutoProcIntegration = AutoProcIntegration
	def getImage(self): return self.__Image
	def setImage(self, Image):
		checkType("AutoProcIntegrationContainer", "setImage", Image, "Image")
		self.__Image = Image
	def delImage(self): self.__Image = None
	# Properties
	Image = property(getImage, setImage, delImage, "Property for Image")
	def getAutoProcIntegration(self): return self.__AutoProcIntegration
	def setAutoProcIntegration(self, AutoProcIntegration):
		checkType("AutoProcIntegrationContainer", "setAutoProcIntegration", AutoProcIntegration, "AutoProcIntegration")
		self.__AutoProcIntegration = AutoProcIntegration
	def delAutoProcIntegration(self): self.__AutoProcIntegration = None
	# Properties
	AutoProcIntegration = property(getAutoProcIntegration, setAutoProcIntegration, delAutoProcIntegration, "Property for AutoProcIntegration")
	def export(self, outfile, level, name_='AutoProcIntegrationContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcIntegrationContainer'):
		pass
		if self.__Image is not None:
			self.Image.export(outfile, level, name_='Image')
		else:
			warnEmptyAttribute("Image", "Image")
		if self.__AutoProcIntegration is not None:
			self.AutoProcIntegration.export(outfile, level, name_='AutoProcIntegration')
		else:
			warnEmptyAttribute("AutoProcIntegration", "AutoProcIntegration")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'Image':
			obj_ = Image()
			obj_.build(child_)
			self.setImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcIntegration':
			obj_ = AutoProcIntegration()
			obj_.build(child_)
			self.setAutoProcIntegration(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcIntegrationContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcIntegrationContainer' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcIntegrationContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcIntegrationContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcIntegrationContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcIntegrationContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcIntegrationContainer

class AutoProcProgram:
	def __init__(self, processingEnvironment=None, processingEndTime=None, processingStartTime=None, processingMessage=None, processingStatus=None, processingPrograms=None, processingCommandLine=None):
		self.__processingCommandLine = processingCommandLine
		self.__processingPrograms = processingPrograms
		self.__processingStatus = processingStatus
		self.__processingMessage = processingMessage
		self.__processingStartTime = processingStartTime
		self.__processingEndTime = processingEndTime
		self.__processingEnvironment = processingEnvironment
	def getProcessingCommandLine(self): return self.__processingCommandLine
	def setProcessingCommandLine(self, processingCommandLine):
		checkType("AutoProcProgram", "setProcessingCommandLine", processingCommandLine, "string")
		self.__processingCommandLine = processingCommandLine
	def delProcessingCommandLine(self): self.__processingCommandLine = None
	# Properties
	processingCommandLine = property(getProcessingCommandLine, setProcessingCommandLine, delProcessingCommandLine, "Property for processingCommandLine")
	def getProcessingPrograms(self): return self.__processingPrograms
	def setProcessingPrograms(self, processingPrograms):
		checkType("AutoProcProgram", "setProcessingPrograms", processingPrograms, "string")
		self.__processingPrograms = processingPrograms
	def delProcessingPrograms(self): self.__processingPrograms = None
	# Properties
	processingPrograms = property(getProcessingPrograms, setProcessingPrograms, delProcessingPrograms, "Property for processingPrograms")
	def getProcessingStatus(self): return self.__processingStatus
	def setProcessingStatus(self, processingStatus):
		checkType("AutoProcProgram", "setProcessingStatus", processingStatus, "boolean")
		self.__processingStatus = processingStatus
	def delProcessingStatus(self): self.__processingStatus = None
	# Properties
	processingStatus = property(getProcessingStatus, setProcessingStatus, delProcessingStatus, "Property for processingStatus")
	def getProcessingMessage(self): return self.__processingMessage
	def setProcessingMessage(self, processingMessage):
		checkType("AutoProcProgram", "setProcessingMessage", processingMessage, "string")
		self.__processingMessage = processingMessage
	def delProcessingMessage(self): self.__processingMessage = None
	# Properties
	processingMessage = property(getProcessingMessage, setProcessingMessage, delProcessingMessage, "Property for processingMessage")
	def getProcessingStartTime(self): return self.__processingStartTime
	def setProcessingStartTime(self, processingStartTime):
		checkType("AutoProcProgram", "setProcessingStartTime", processingStartTime, "string")
		self.__processingStartTime = processingStartTime
	def delProcessingStartTime(self): self.__processingStartTime = None
	# Properties
	processingStartTime = property(getProcessingStartTime, setProcessingStartTime, delProcessingStartTime, "Property for processingStartTime")
	def getProcessingEndTime(self): return self.__processingEndTime
	def setProcessingEndTime(self, processingEndTime):
		checkType("AutoProcProgram", "setProcessingEndTime", processingEndTime, "string")
		self.__processingEndTime = processingEndTime
	def delProcessingEndTime(self): self.__processingEndTime = None
	# Properties
	processingEndTime = property(getProcessingEndTime, setProcessingEndTime, delProcessingEndTime, "Property for processingEndTime")
	def getProcessingEnvironment(self): return self.__processingEnvironment
	def setProcessingEnvironment(self, processingEnvironment):
		checkType("AutoProcProgram", "setProcessingEnvironment", processingEnvironment, "string")
		self.__processingEnvironment = processingEnvironment
	def delProcessingEnvironment(self): self.__processingEnvironment = None
	# Properties
	processingEnvironment = property(getProcessingEnvironment, setProcessingEnvironment, delProcessingEnvironment, "Property for processingEnvironment")
	def export(self, outfile, level, name_='AutoProcProgram'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcProgram'):
		pass
		if self.__processingCommandLine is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingCommandLine>%s</processingCommandLine>\n' % self.__processingCommandLine))
		else:
			warnEmptyAttribute("processingCommandLine", "string")
		if self.__processingPrograms is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingPrograms>%s</processingPrograms>\n' % self.__processingPrograms))
		else:
			warnEmptyAttribute("processingPrograms", "string")
		if self.__processingStatus is not None:
			showIndent(outfile, level)
			if self.__processingStatus:
				outfile.write(unicode('<processingStatus>true</processingStatus>\n'))
			else:
				outfile.write(unicode('<processingStatus>false</processingStatus>\n'))
		else:
			warnEmptyAttribute("processingStatus", "boolean")
		if self.__processingMessage is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingMessage>%s</processingMessage>\n' % self.__processingMessage))
		else:
			warnEmptyAttribute("processingMessage", "string")
		if self.__processingStartTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingStartTime>%s</processingStartTime>\n' % self.__processingStartTime))
		else:
			warnEmptyAttribute("processingStartTime", "string")
		if self.__processingEndTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingEndTime>%s</processingEndTime>\n' % self.__processingEndTime))
		else:
			warnEmptyAttribute("processingEndTime", "string")
		if self.__processingEnvironment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingEnvironment>%s</processingEnvironment>\n' % self.__processingEnvironment))
		else:
			warnEmptyAttribute("processingEnvironment", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingCommandLine':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingCommandLine = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingPrograms':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingPrograms = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingStatus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__processingStatus = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingMessage':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingMessage = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingStartTime':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingStartTime = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingEndTime':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingEndTime = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingEnvironment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__processingEnvironment = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcProgram" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgram' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcProgram.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcProgram()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcProgram" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcProgram()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcProgram

class AutoProcProgramAttachment:
	def __init__(self, filePath=None, fileName=None, fileType=None):
		self.__fileType = fileType
		self.__fileName = fileName
		self.__filePath = filePath
	def getFileType(self): return self.__fileType
	def setFileType(self, fileType):
		checkType("AutoProcProgramAttachment", "setFileType", fileType, "string")
		self.__fileType = fileType
	def delFileType(self): self.__fileType = None
	# Properties
	fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
	def getFileName(self): return self.__fileName
	def setFileName(self, fileName):
		checkType("AutoProcProgramAttachment", "setFileName", fileName, "string")
		self.__fileName = fileName
	def delFileName(self): self.__fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFilePath(self): return self.__filePath
	def setFilePath(self, filePath):
		checkType("AutoProcProgramAttachment", "setFilePath", filePath, "string")
		self.__filePath = filePath
	def delFilePath(self): self.__filePath = None
	# Properties
	filePath = property(getFilePath, setFilePath, delFilePath, "Property for filePath")
	def export(self, outfile, level, name_='AutoProcProgramAttachment'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcProgramAttachment'):
		pass
		if self.__fileType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileType>%s</fileType>\n' % self.__fileType))
		else:
			warnEmptyAttribute("fileType", "string")
		if self.__fileName is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileName>%s</fileName>\n' % self.__fileName))
		else:
			warnEmptyAttribute("fileName", "string")
		if self.__filePath is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<filePath>%s</filePath>\n' % self.__filePath))
		else:
			warnEmptyAttribute("filePath", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__fileType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__fileName = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'filePath':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__filePath = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcProgramAttachment" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgramAttachment' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcProgramAttachment.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcProgramAttachment()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcProgramAttachment" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcProgramAttachment()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcProgramAttachment

class AutoProcProgramContainer:
	def __init__(self, AutoProcProgramAttachment=None, AutoProcProgram=None):
		self.__AutoProcProgram = AutoProcProgram
		if AutoProcProgramAttachment is None:
			self.__AutoProcProgramAttachment = []
		else:
			self.__AutoProcProgramAttachment = AutoProcProgramAttachment
	def getAutoProcProgram(self): return self.__AutoProcProgram
	def setAutoProcProgram(self, AutoProcProgram):
		checkType("AutoProcProgramContainer", "setAutoProcProgram", AutoProcProgram, "AutoProcProgram")
		self.__AutoProcProgram = AutoProcProgram
	def delAutoProcProgram(self): self.__AutoProcProgram = None
	# Properties
	AutoProcProgram = property(getAutoProcProgram, setAutoProcProgram, delAutoProcProgram, "Property for AutoProcProgram")
	def getAutoProcProgramAttachment(self): return self.__AutoProcProgramAttachment
	def setAutoProcProgramAttachment(self, AutoProcProgramAttachment):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", AutoProcProgramAttachment, "list")
		self.__AutoProcProgramAttachment = AutoProcProgramAttachment
	def delAutoProcProgramAttachment(self): self.__AutoProcProgramAttachment = None
	# Properties
	AutoProcProgramAttachment = property(getAutoProcProgramAttachment, setAutoProcProgramAttachment, delAutoProcProgramAttachment, "Property for AutoProcProgramAttachment")
	def addAutoProcProgramAttachment(self, value):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", value, "AutoProcProgramAttachment")
		self.__AutoProcProgramAttachment.append(value)
	def insertAutoProcProgramAttachment(self, index, value):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", value, "AutoProcProgramAttachment")
		self.__AutoProcProgramAttachment[index] = value
	def export(self, outfile, level, name_='AutoProcProgramContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcProgramContainer'):
		pass
		if self.__AutoProcProgram is not None:
			self.AutoProcProgram.export(outfile, level, name_='AutoProcProgram')
		else:
			warnEmptyAttribute("AutoProcProgram", "AutoProcProgram")
		for AutoProcProgramAttachment_ in self.getAutoProcProgramAttachment():
			AutoProcProgramAttachment_.export(outfile, level, name_='AutoProcProgramAttachment')
		if self.getAutoProcProgramAttachment() == []:
			warnEmptyAttribute("AutoProcProgramAttachment", "AutoProcProgramAttachment")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcProgram':
			obj_ = AutoProcProgram()
			obj_.build(child_)
			self.setAutoProcProgram(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcProgramAttachment':
			obj_ = AutoProcProgramAttachment()
			obj_.build(child_)
			self.AutoProcProgramAttachment.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcProgramContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgramContainer' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcProgramContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcProgramContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcProgramContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcProgramContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcProgramContainer

class AutoProcScaling:
	def __init__(self, recordTimeStamp=None):
		self.__recordTimeStamp = recordTimeStamp
	def getRecordTimeStamp(self): return self.__recordTimeStamp
	def setRecordTimeStamp(self, recordTimeStamp):
		checkType("AutoProcScaling", "setRecordTimeStamp", recordTimeStamp, "string")
		self.__recordTimeStamp = recordTimeStamp
	def delRecordTimeStamp(self): self.__recordTimeStamp = None
	# Properties
	recordTimeStamp = property(getRecordTimeStamp, setRecordTimeStamp, delRecordTimeStamp, "Property for recordTimeStamp")
	def export(self, outfile, level, name_='AutoProcScaling'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcScaling'):
		pass
		if self.__recordTimeStamp is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<recordTimeStamp>%s</recordTimeStamp>\n' % self.__recordTimeStamp))
		else:
			warnEmptyAttribute("recordTimeStamp", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'recordTimeStamp':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__recordTimeStamp = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcScaling" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScaling' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcScaling.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcScaling()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcScaling" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcScaling()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcScaling

class AutoProcScalingStatistics:
	def __init__(self, anomalousMultiplicity=None, anomalousCompleteness=None, multiplicity=None, completeness=None, meanIOverSigI=None, ntotalUniqueObservations=None, nTotalObservations=None, fractionalPartialBias=None, rpimAllIplusIminus=None, rpimWithinIplusIminus=None, rmeasAllIplusIminus=None, rmeasWithinIplusIminus=None, rMerge=None, resolutionLimitHigh=None, resolutionLimitLow=None, comments=None, scalingStatisticsType=None):
		self.__scalingStatisticsType = scalingStatisticsType
		self.__comments = comments
		self.__resolutionLimitLow = resolutionLimitLow
		self.__resolutionLimitHigh = resolutionLimitHigh
		self.__rMerge = rMerge
		self.__rmeasWithinIplusIminus = rmeasWithinIplusIminus
		self.__rmeasAllIplusIminus = rmeasAllIplusIminus
		self.__rpimWithinIplusIminus = rpimWithinIplusIminus
		self.__rpimAllIplusIminus = rpimAllIplusIminus
		self.__fractionalPartialBias = fractionalPartialBias
		self.__nTotalObservations = nTotalObservations
		self.__ntotalUniqueObservations = ntotalUniqueObservations
		self.__meanIOverSigI = meanIOverSigI
		self.__completeness = completeness
		self.__multiplicity = multiplicity
		self.__anomalousCompleteness = anomalousCompleteness
		self.__anomalousMultiplicity = anomalousMultiplicity
	def getScalingStatisticsType(self): return self.__scalingStatisticsType
	def setScalingStatisticsType(self, scalingStatisticsType):
		checkType("AutoProcScalingStatistics", "setScalingStatisticsType", scalingStatisticsType, "string")
		self.__scalingStatisticsType = scalingStatisticsType
	def delScalingStatisticsType(self): self.__scalingStatisticsType = None
	# Properties
	scalingStatisticsType = property(getScalingStatisticsType, setScalingStatisticsType, delScalingStatisticsType, "Property for scalingStatisticsType")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("AutoProcScalingStatistics", "setComments", comments, "string")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getResolutionLimitLow(self): return self.__resolutionLimitLow
	def setResolutionLimitLow(self, resolutionLimitLow):
		checkType("AutoProcScalingStatistics", "setResolutionLimitLow", resolutionLimitLow, "float")
		self.__resolutionLimitLow = resolutionLimitLow
	def delResolutionLimitLow(self): self.__resolutionLimitLow = None
	# Properties
	resolutionLimitLow = property(getResolutionLimitLow, setResolutionLimitLow, delResolutionLimitLow, "Property for resolutionLimitLow")
	def getResolutionLimitHigh(self): return self.__resolutionLimitHigh
	def setResolutionLimitHigh(self, resolutionLimitHigh):
		checkType("AutoProcScalingStatistics", "setResolutionLimitHigh", resolutionLimitHigh, "float")
		self.__resolutionLimitHigh = resolutionLimitHigh
	def delResolutionLimitHigh(self): self.__resolutionLimitHigh = None
	# Properties
	resolutionLimitHigh = property(getResolutionLimitHigh, setResolutionLimitHigh, delResolutionLimitHigh, "Property for resolutionLimitHigh")
	def getRMerge(self): return self.__rMerge
	def setRMerge(self, rMerge):
		checkType("AutoProcScalingStatistics", "setRMerge", rMerge, "float")
		self.__rMerge = rMerge
	def delRMerge(self): self.__rMerge = None
	# Properties
	rMerge = property(getRMerge, setRMerge, delRMerge, "Property for rMerge")
	def getRmeasWithinIplusIminus(self): return self.__rmeasWithinIplusIminus
	def setRmeasWithinIplusIminus(self, rmeasWithinIplusIminus):
		checkType("AutoProcScalingStatistics", "setRmeasWithinIplusIminus", rmeasWithinIplusIminus, "float")
		self.__rmeasWithinIplusIminus = rmeasWithinIplusIminus
	def delRmeasWithinIplusIminus(self): self.__rmeasWithinIplusIminus = None
	# Properties
	rmeasWithinIplusIminus = property(getRmeasWithinIplusIminus, setRmeasWithinIplusIminus, delRmeasWithinIplusIminus, "Property for rmeasWithinIplusIminus")
	def getRmeasAllIplusIminus(self): return self.__rmeasAllIplusIminus
	def setRmeasAllIplusIminus(self, rmeasAllIplusIminus):
		checkType("AutoProcScalingStatistics", "setRmeasAllIplusIminus", rmeasAllIplusIminus, "float")
		self.__rmeasAllIplusIminus = rmeasAllIplusIminus
	def delRmeasAllIplusIminus(self): self.__rmeasAllIplusIminus = None
	# Properties
	rmeasAllIplusIminus = property(getRmeasAllIplusIminus, setRmeasAllIplusIminus, delRmeasAllIplusIminus, "Property for rmeasAllIplusIminus")
	def getRpimWithinIplusIminus(self): return self.__rpimWithinIplusIminus
	def setRpimWithinIplusIminus(self, rpimWithinIplusIminus):
		checkType("AutoProcScalingStatistics", "setRpimWithinIplusIminus", rpimWithinIplusIminus, "float")
		self.__rpimWithinIplusIminus = rpimWithinIplusIminus
	def delRpimWithinIplusIminus(self): self.__rpimWithinIplusIminus = None
	# Properties
	rpimWithinIplusIminus = property(getRpimWithinIplusIminus, setRpimWithinIplusIminus, delRpimWithinIplusIminus, "Property for rpimWithinIplusIminus")
	def getRpimAllIplusIminus(self): return self.__rpimAllIplusIminus
	def setRpimAllIplusIminus(self, rpimAllIplusIminus):
		checkType("AutoProcScalingStatistics", "setRpimAllIplusIminus", rpimAllIplusIminus, "float")
		self.__rpimAllIplusIminus = rpimAllIplusIminus
	def delRpimAllIplusIminus(self): self.__rpimAllIplusIminus = None
	# Properties
	rpimAllIplusIminus = property(getRpimAllIplusIminus, setRpimAllIplusIminus, delRpimAllIplusIminus, "Property for rpimAllIplusIminus")
	def getFractionalPartialBias(self): return self.__fractionalPartialBias
	def setFractionalPartialBias(self, fractionalPartialBias):
		checkType("AutoProcScalingStatistics", "setFractionalPartialBias", fractionalPartialBias, "float")
		self.__fractionalPartialBias = fractionalPartialBias
	def delFractionalPartialBias(self): self.__fractionalPartialBias = None
	# Properties
	fractionalPartialBias = property(getFractionalPartialBias, setFractionalPartialBias, delFractionalPartialBias, "Property for fractionalPartialBias")
	def getNTotalObservations(self): return self.__nTotalObservations
	def setNTotalObservations(self, nTotalObservations):
		checkType("AutoProcScalingStatistics", "setNTotalObservations", nTotalObservations, "float")
		self.__nTotalObservations = nTotalObservations
	def delNTotalObservations(self): self.__nTotalObservations = None
	# Properties
	nTotalObservations = property(getNTotalObservations, setNTotalObservations, delNTotalObservations, "Property for nTotalObservations")
	def getNtotalUniqueObservations(self): return self.__ntotalUniqueObservations
	def setNtotalUniqueObservations(self, ntotalUniqueObservations):
		checkType("AutoProcScalingStatistics", "setNtotalUniqueObservations", ntotalUniqueObservations, "integer")
		self.__ntotalUniqueObservations = ntotalUniqueObservations
	def delNtotalUniqueObservations(self): self.__ntotalUniqueObservations = None
	# Properties
	ntotalUniqueObservations = property(getNtotalUniqueObservations, setNtotalUniqueObservations, delNtotalUniqueObservations, "Property for ntotalUniqueObservations")
	def getMeanIOverSigI(self): return self.__meanIOverSigI
	def setMeanIOverSigI(self, meanIOverSigI):
		checkType("AutoProcScalingStatistics", "setMeanIOverSigI", meanIOverSigI, "float")
		self.__meanIOverSigI = meanIOverSigI
	def delMeanIOverSigI(self): self.__meanIOverSigI = None
	# Properties
	meanIOverSigI = property(getMeanIOverSigI, setMeanIOverSigI, delMeanIOverSigI, "Property for meanIOverSigI")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("AutoProcScalingStatistics", "setCompleteness", completeness, "float")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self.__multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("AutoProcScalingStatistics", "setMultiplicity", multiplicity, "float")
		self.__multiplicity = multiplicity
	def delMultiplicity(self): self.__multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getAnomalousCompleteness(self): return self.__anomalousCompleteness
	def setAnomalousCompleteness(self, anomalousCompleteness):
		checkType("AutoProcScalingStatistics", "setAnomalousCompleteness", anomalousCompleteness, "float")
		self.__anomalousCompleteness = anomalousCompleteness
	def delAnomalousCompleteness(self): self.__anomalousCompleteness = None
	# Properties
	anomalousCompleteness = property(getAnomalousCompleteness, setAnomalousCompleteness, delAnomalousCompleteness, "Property for anomalousCompleteness")
	def getAnomalousMultiplicity(self): return self.__anomalousMultiplicity
	def setAnomalousMultiplicity(self, anomalousMultiplicity):
		checkType("AutoProcScalingStatistics", "setAnomalousMultiplicity", anomalousMultiplicity, "float")
		self.__anomalousMultiplicity = anomalousMultiplicity
	def delAnomalousMultiplicity(self): self.__anomalousMultiplicity = None
	# Properties
	anomalousMultiplicity = property(getAnomalousMultiplicity, setAnomalousMultiplicity, delAnomalousMultiplicity, "Property for anomalousMultiplicity")
	def export(self, outfile, level, name_='AutoProcScalingStatistics'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcScalingStatistics'):
		pass
		if self.__scalingStatisticsType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<scalingStatisticsType>%s</scalingStatisticsType>\n' % self.__scalingStatisticsType))
		else:
			warnEmptyAttribute("scalingStatisticsType", "string")
		if self.__comments is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comments>%s</comments>\n' % self.__comments))
		else:
			warnEmptyAttribute("comments", "string")
		if self.__resolutionLimitLow is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionLimitLow>%e</resolutionLimitLow>\n' % self.__resolutionLimitLow))
		else:
			warnEmptyAttribute("resolutionLimitLow", "float")
		if self.__resolutionLimitHigh is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionLimitHigh>%e</resolutionLimitHigh>\n' % self.__resolutionLimitHigh))
		else:
			warnEmptyAttribute("resolutionLimitHigh", "float")
		if self.__rMerge is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rMerge>%e</rMerge>\n' % self.__rMerge))
		else:
			warnEmptyAttribute("rMerge", "float")
		if self.__rmeasWithinIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rmeasWithinIplusIminus>%e</rmeasWithinIplusIminus>\n' % self.__rmeasWithinIplusIminus))
		else:
			warnEmptyAttribute("rmeasWithinIplusIminus", "float")
		if self.__rmeasAllIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rmeasAllIplusIminus>%e</rmeasAllIplusIminus>\n' % self.__rmeasAllIplusIminus))
		else:
			warnEmptyAttribute("rmeasAllIplusIminus", "float")
		if self.__rpimWithinIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rpimWithinIplusIminus>%e</rpimWithinIplusIminus>\n' % self.__rpimWithinIplusIminus))
		else:
			warnEmptyAttribute("rpimWithinIplusIminus", "float")
		if self.__rpimAllIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rpimAllIplusIminus>%e</rpimAllIplusIminus>\n' % self.__rpimAllIplusIminus))
		else:
			warnEmptyAttribute("rpimAllIplusIminus", "float")
		if self.__fractionalPartialBias is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fractionalPartialBias>%e</fractionalPartialBias>\n' % self.__fractionalPartialBias))
		else:
			warnEmptyAttribute("fractionalPartialBias", "float")
		if self.__nTotalObservations is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<nTotalObservations>%e</nTotalObservations>\n' % self.__nTotalObservations))
		else:
			warnEmptyAttribute("nTotalObservations", "float")
		if self.__ntotalUniqueObservations is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ntotalUniqueObservations>%d</ntotalUniqueObservations>\n' % self.__ntotalUniqueObservations))
		else:
			warnEmptyAttribute("ntotalUniqueObservations", "integer")
		if self.__meanIOverSigI is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<meanIOverSigI>%e</meanIOverSigI>\n' % self.__meanIOverSigI))
		else:
			warnEmptyAttribute("meanIOverSigI", "float")
		if self.__completeness is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<completeness>%e</completeness>\n' % self.__completeness))
		else:
			warnEmptyAttribute("completeness", "float")
		if self.__multiplicity is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<multiplicity>%e</multiplicity>\n' % self.__multiplicity))
		else:
			warnEmptyAttribute("multiplicity", "float")
		if self.__anomalousCompleteness is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<anomalousCompleteness>%e</anomalousCompleteness>\n' % self.__anomalousCompleteness))
		else:
			warnEmptyAttribute("anomalousCompleteness", "float")
		if self.__anomalousMultiplicity is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<anomalousMultiplicity>%e</anomalousMultiplicity>\n' % self.__anomalousMultiplicity))
		else:
			warnEmptyAttribute("anomalousMultiplicity", "float")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scalingStatisticsType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__scalingStatisticsType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comments = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionLimitLow':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolutionLimitLow = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionLimitHigh':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolutionLimitHigh = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMerge':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rMerge = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmeasWithinIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rmeasWithinIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmeasAllIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rmeasAllIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rpimWithinIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rpimWithinIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rpimAllIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rpimAllIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fractionalPartialBias':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__fractionalPartialBias = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nTotalObservations':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__nTotalObservations = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ntotalUniqueObservations':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__ntotalUniqueObservations = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'meanIOverSigI':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__meanIOverSigI = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__completeness = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__multiplicity = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousCompleteness':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__anomalousCompleteness = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousMultiplicity':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__anomalousMultiplicity = fval_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcScalingStatistics" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScalingStatistics' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcScalingStatistics.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcScalingStatistics()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcScalingStatistics" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcScalingStatistics()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcScalingStatistics

class AutoProcScalingContainer:
	def __init__(self, AutoProcIntegrationContainer=None, AutoProcScalingStatistics=None, AutoProcScaling=None):
		self.__AutoProcScaling = AutoProcScaling
		if AutoProcScalingStatistics is None:
			self.__AutoProcScalingStatistics = []
		else:
			self.__AutoProcScalingStatistics = AutoProcScalingStatistics
		self.__AutoProcIntegrationContainer = AutoProcIntegrationContainer
	def getAutoProcScaling(self): return self.__AutoProcScaling
	def setAutoProcScaling(self, AutoProcScaling):
		checkType("AutoProcScalingContainer", "setAutoProcScaling", AutoProcScaling, "AutoProcScaling")
		self.__AutoProcScaling = AutoProcScaling
	def delAutoProcScaling(self): self.__AutoProcScaling = None
	# Properties
	AutoProcScaling = property(getAutoProcScaling, setAutoProcScaling, delAutoProcScaling, "Property for AutoProcScaling")
	def getAutoProcScalingStatistics(self): return self.__AutoProcScalingStatistics
	def setAutoProcScalingStatistics(self, AutoProcScalingStatistics):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", AutoProcScalingStatistics, "list")
		self.__AutoProcScalingStatistics = AutoProcScalingStatistics
	def delAutoProcScalingStatistics(self): self.__AutoProcScalingStatistics = None
	# Properties
	AutoProcScalingStatistics = property(getAutoProcScalingStatistics, setAutoProcScalingStatistics, delAutoProcScalingStatistics, "Property for AutoProcScalingStatistics")
	def addAutoProcScalingStatistics(self, value):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", value, "AutoProcScalingStatistics")
		self.__AutoProcScalingStatistics.append(value)
	def insertAutoProcScalingStatistics(self, index, value):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", value, "AutoProcScalingStatistics")
		self.__AutoProcScalingStatistics[index] = value
	def getAutoProcIntegrationContainer(self): return self.__AutoProcIntegrationContainer
	def setAutoProcIntegrationContainer(self, AutoProcIntegrationContainer):
		checkType("AutoProcScalingContainer", "setAutoProcIntegrationContainer", AutoProcIntegrationContainer, "AutoProcIntegrationContainer")
		self.__AutoProcIntegrationContainer = AutoProcIntegrationContainer
	def delAutoProcIntegrationContainer(self): self.__AutoProcIntegrationContainer = None
	# Properties
	AutoProcIntegrationContainer = property(getAutoProcIntegrationContainer, setAutoProcIntegrationContainer, delAutoProcIntegrationContainer, "Property for AutoProcIntegrationContainer")
	def export(self, outfile, level, name_='AutoProcScalingContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcScalingContainer'):
		pass
		if self.__AutoProcScaling is not None:
			self.AutoProcScaling.export(outfile, level, name_='AutoProcScaling')
		else:
			warnEmptyAttribute("AutoProcScaling", "AutoProcScaling")
		for AutoProcScalingStatistics_ in self.getAutoProcScalingStatistics():
			AutoProcScalingStatistics_.export(outfile, level, name_='AutoProcScalingStatistics')
		if self.getAutoProcScalingStatistics() == []:
			warnEmptyAttribute("AutoProcScalingStatistics", "AutoProcScalingStatistics")
		if self.__AutoProcIntegrationContainer is not None:
			self.AutoProcIntegrationContainer.export(outfile, level, name_='AutoProcIntegrationContainer')
		else:
			warnEmptyAttribute("AutoProcIntegrationContainer", "AutoProcIntegrationContainer")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcScaling':
			obj_ = AutoProcScaling()
			obj_.build(child_)
			self.setAutoProcScaling(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcScalingStatistics':
			obj_ = AutoProcScalingStatistics()
			obj_.build(child_)
			self.AutoProcScalingStatistics.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcIntegrationContainer':
			obj_ = AutoProcIntegrationContainer()
			obj_.build(child_)
			self.setAutoProcIntegrationContainer(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcScalingContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScalingContainer' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return AutoProcScalingContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = AutoProcScalingContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="AutoProcScalingContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = AutoProcScalingContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class AutoProcScalingContainer

class Image:
	def __init__(self, dataCollectionId=None):
		self.__dataCollectionId = dataCollectionId
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("Image", "setDataCollectionId", dataCollectionId, "integer")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def export(self, outfile, level, name_='Image'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='Image'):
		pass
		if self.__dataCollectionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self.__dataCollectionId))
		else:
			warnEmptyAttribute("dataCollectionId", "integer")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__dataCollectionId = ival_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="Image" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='Image' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return Image.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = Image()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="Image" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = Image()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class Image

class XSDataISPyBImageQualityIndicators(XSData):
	def __init__(self, totalIntegratedSignal=None, spotTotal=None, signalRangeMin=None, signalRangeMax=None, signalRangeAverage=None, saturationRangeMin=None, saturationRangeMax=None, saturationRangeAverage=None, pctSaturationTop50Peaks=None, method2Res=None, method1Res=None, maxUnitCell=None, inResolutionOvrlSpots=None, inResTotal=None, image=None, iceRings=None, goodBraggCandidates=None, binPopCutOffMethod2Res=None):
		XSData.__init__(self, )
		self.__binPopCutOffMethod2Res = binPopCutOffMethod2Res
		self.__goodBraggCandidates = goodBraggCandidates
		self.__iceRings = iceRings
		self.__image = image
		self.__inResTotal = inResTotal
		self.__inResolutionOvrlSpots = inResolutionOvrlSpots
		self.__maxUnitCell = maxUnitCell
		self.__method1Res = method1Res
		self.__method2Res = method2Res
		self.__pctSaturationTop50Peaks = pctSaturationTop50Peaks
		self.__saturationRangeAverage = saturationRangeAverage
		self.__saturationRangeMax = saturationRangeMax
		self.__saturationRangeMin = saturationRangeMin
		self.__signalRangeAverage = signalRangeAverage
		self.__signalRangeMax = signalRangeMax
		self.__signalRangeMin = signalRangeMin
		self.__spotTotal = spotTotal
		self.__totalIntegratedSignal = totalIntegratedSignal
	def getBinPopCutOffMethod2Res(self): return self.__binPopCutOffMethod2Res
	def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res):
		checkType("XSDataISPyBImageQualityIndicators", "setBinPopCutOffMethod2Res", binPopCutOffMethod2Res, "XSDataDouble")
		self.__binPopCutOffMethod2Res = binPopCutOffMethod2Res
	def delBinPopCutOffMethod2Res(self): self.__binPopCutOffMethod2Res = None
	# Properties
	binPopCutOffMethod2Res = property(getBinPopCutOffMethod2Res, setBinPopCutOffMethod2Res, delBinPopCutOffMethod2Res, "Property for binPopCutOffMethod2Res")
	def getGoodBraggCandidates(self): return self.__goodBraggCandidates
	def setGoodBraggCandidates(self, goodBraggCandidates):
		checkType("XSDataISPyBImageQualityIndicators", "setGoodBraggCandidates", goodBraggCandidates, "XSDataInteger")
		self.__goodBraggCandidates = goodBraggCandidates
	def delGoodBraggCandidates(self): self.__goodBraggCandidates = None
	# Properties
	goodBraggCandidates = property(getGoodBraggCandidates, setGoodBraggCandidates, delGoodBraggCandidates, "Property for goodBraggCandidates")
	def getIceRings(self): return self.__iceRings
	def setIceRings(self, iceRings):
		checkType("XSDataISPyBImageQualityIndicators", "setIceRings", iceRings, "XSDataInteger")
		self.__iceRings = iceRings
	def delIceRings(self): self.__iceRings = None
	# Properties
	iceRings = property(getIceRings, setIceRings, delIceRings, "Property for iceRings")
	def getImage(self): return self.__image
	def setImage(self, image):
		checkType("XSDataISPyBImageQualityIndicators", "setImage", image, "XSDataImage")
		self.__image = image
	def delImage(self): self.__image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getInResTotal(self): return self.__inResTotal
	def setInResTotal(self, inResTotal):
		checkType("XSDataISPyBImageQualityIndicators", "setInResTotal", inResTotal, "XSDataInteger")
		self.__inResTotal = inResTotal
	def delInResTotal(self): self.__inResTotal = None
	# Properties
	inResTotal = property(getInResTotal, setInResTotal, delInResTotal, "Property for inResTotal")
	def getInResolutionOvrlSpots(self): return self.__inResolutionOvrlSpots
	def setInResolutionOvrlSpots(self, inResolutionOvrlSpots):
		checkType("XSDataISPyBImageQualityIndicators", "setInResolutionOvrlSpots", inResolutionOvrlSpots, "XSDataInteger")
		self.__inResolutionOvrlSpots = inResolutionOvrlSpots
	def delInResolutionOvrlSpots(self): self.__inResolutionOvrlSpots = None
	# Properties
	inResolutionOvrlSpots = property(getInResolutionOvrlSpots, setInResolutionOvrlSpots, delInResolutionOvrlSpots, "Property for inResolutionOvrlSpots")
	def getMaxUnitCell(self): return self.__maxUnitCell
	def setMaxUnitCell(self, maxUnitCell):
		checkType("XSDataISPyBImageQualityIndicators", "setMaxUnitCell", maxUnitCell, "XSDataDouble")
		self.__maxUnitCell = maxUnitCell
	def delMaxUnitCell(self): self.__maxUnitCell = None
	# Properties
	maxUnitCell = property(getMaxUnitCell, setMaxUnitCell, delMaxUnitCell, "Property for maxUnitCell")
	def getMethod1Res(self): return self.__method1Res
	def setMethod1Res(self, method1Res):
		checkType("XSDataISPyBImageQualityIndicators", "setMethod1Res", method1Res, "XSDataDouble")
		self.__method1Res = method1Res
	def delMethod1Res(self): self.__method1Res = None
	# Properties
	method1Res = property(getMethod1Res, setMethod1Res, delMethod1Res, "Property for method1Res")
	def getMethod2Res(self): return self.__method2Res
	def setMethod2Res(self, method2Res):
		checkType("XSDataISPyBImageQualityIndicators", "setMethod2Res", method2Res, "XSDataDouble")
		self.__method2Res = method2Res
	def delMethod2Res(self): self.__method2Res = None
	# Properties
	method2Res = property(getMethod2Res, setMethod2Res, delMethod2Res, "Property for method2Res")
	def getPctSaturationTop50Peaks(self): return self.__pctSaturationTop50Peaks
	def setPctSaturationTop50Peaks(self, pctSaturationTop50Peaks):
		checkType("XSDataISPyBImageQualityIndicators", "setPctSaturationTop50Peaks", pctSaturationTop50Peaks, "XSDataDouble")
		self.__pctSaturationTop50Peaks = pctSaturationTop50Peaks
	def delPctSaturationTop50Peaks(self): self.__pctSaturationTop50Peaks = None
	# Properties
	pctSaturationTop50Peaks = property(getPctSaturationTop50Peaks, setPctSaturationTop50Peaks, delPctSaturationTop50Peaks, "Property for pctSaturationTop50Peaks")
	def getSaturationRangeAverage(self): return self.__saturationRangeAverage
	def setSaturationRangeAverage(self, saturationRangeAverage):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeAverage", saturationRangeAverage, "XSDataDouble")
		self.__saturationRangeAverage = saturationRangeAverage
	def delSaturationRangeAverage(self): self.__saturationRangeAverage = None
	# Properties
	saturationRangeAverage = property(getSaturationRangeAverage, setSaturationRangeAverage, delSaturationRangeAverage, "Property for saturationRangeAverage")
	def getSaturationRangeMax(self): return self.__saturationRangeMax
	def setSaturationRangeMax(self, saturationRangeMax):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeMax", saturationRangeMax, "XSDataDouble")
		self.__saturationRangeMax = saturationRangeMax
	def delSaturationRangeMax(self): self.__saturationRangeMax = None
	# Properties
	saturationRangeMax = property(getSaturationRangeMax, setSaturationRangeMax, delSaturationRangeMax, "Property for saturationRangeMax")
	def getSaturationRangeMin(self): return self.__saturationRangeMin
	def setSaturationRangeMin(self, saturationRangeMin):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeMin", saturationRangeMin, "XSDataDouble")
		self.__saturationRangeMin = saturationRangeMin
	def delSaturationRangeMin(self): self.__saturationRangeMin = None
	# Properties
	saturationRangeMin = property(getSaturationRangeMin, setSaturationRangeMin, delSaturationRangeMin, "Property for saturationRangeMin")
	def getSignalRangeAverage(self): return self.__signalRangeAverage
	def setSignalRangeAverage(self, signalRangeAverage):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeAverage", signalRangeAverage, "XSDataDouble")
		self.__signalRangeAverage = signalRangeAverage
	def delSignalRangeAverage(self): self.__signalRangeAverage = None
	# Properties
	signalRangeAverage = property(getSignalRangeAverage, setSignalRangeAverage, delSignalRangeAverage, "Property for signalRangeAverage")
	def getSignalRangeMax(self): return self.__signalRangeMax
	def setSignalRangeMax(self, signalRangeMax):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeMax", signalRangeMax, "XSDataDouble")
		self.__signalRangeMax = signalRangeMax
	def delSignalRangeMax(self): self.__signalRangeMax = None
	# Properties
	signalRangeMax = property(getSignalRangeMax, setSignalRangeMax, delSignalRangeMax, "Property for signalRangeMax")
	def getSignalRangeMin(self): return self.__signalRangeMin
	def setSignalRangeMin(self, signalRangeMin):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeMin", signalRangeMin, "XSDataDouble")
		self.__signalRangeMin = signalRangeMin
	def delSignalRangeMin(self): self.__signalRangeMin = None
	# Properties
	signalRangeMin = property(getSignalRangeMin, setSignalRangeMin, delSignalRangeMin, "Property for signalRangeMin")
	def getSpotTotal(self): return self.__spotTotal
	def setSpotTotal(self, spotTotal):
		checkType("XSDataISPyBImageQualityIndicators", "setSpotTotal", spotTotal, "XSDataInteger")
		self.__spotTotal = spotTotal
	def delSpotTotal(self): self.__spotTotal = None
	# Properties
	spotTotal = property(getSpotTotal, setSpotTotal, delSpotTotal, "Property for spotTotal")
	def getTotalIntegratedSignal(self): return self.__totalIntegratedSignal
	def setTotalIntegratedSignal(self, totalIntegratedSignal):
		checkType("XSDataISPyBImageQualityIndicators", "setTotalIntegratedSignal", totalIntegratedSignal, "XSDataDouble")
		self.__totalIntegratedSignal = totalIntegratedSignal
	def delTotalIntegratedSignal(self): self.__totalIntegratedSignal = None
	# Properties
	totalIntegratedSignal = property(getTotalIntegratedSignal, setTotalIntegratedSignal, delTotalIntegratedSignal, "Property for totalIntegratedSignal")
	def export(self, outfile, level, name_='XSDataISPyBImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBImageQualityIndicators'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__binPopCutOffMethod2Res is not None:
			self.binPopCutOffMethod2Res.export(outfile, level, name_='binPopCutOffMethod2Res')
		else:
			warnEmptyAttribute("binPopCutOffMethod2Res", "XSDataDouble")
		if self.__goodBraggCandidates is not None:
			self.goodBraggCandidates.export(outfile, level, name_='goodBraggCandidates')
		else:
			warnEmptyAttribute("goodBraggCandidates", "XSDataInteger")
		if self.__iceRings is not None:
			self.iceRings.export(outfile, level, name_='iceRings')
		else:
			warnEmptyAttribute("iceRings", "XSDataInteger")
		if self.__image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataImage")
		if self.__inResTotal is not None:
			self.inResTotal.export(outfile, level, name_='inResTotal')
		else:
			warnEmptyAttribute("inResTotal", "XSDataInteger")
		if self.__inResolutionOvrlSpots is not None:
			self.inResolutionOvrlSpots.export(outfile, level, name_='inResolutionOvrlSpots')
		else:
			warnEmptyAttribute("inResolutionOvrlSpots", "XSDataInteger")
		if self.__maxUnitCell is not None:
			self.maxUnitCell.export(outfile, level, name_='maxUnitCell')
		else:
			warnEmptyAttribute("maxUnitCell", "XSDataDouble")
		if self.__method1Res is not None:
			self.method1Res.export(outfile, level, name_='method1Res')
		else:
			warnEmptyAttribute("method1Res", "XSDataDouble")
		if self.__method2Res is not None:
			self.method2Res.export(outfile, level, name_='method2Res')
		else:
			warnEmptyAttribute("method2Res", "XSDataDouble")
		if self.__pctSaturationTop50Peaks is not None:
			self.pctSaturationTop50Peaks.export(outfile, level, name_='pctSaturationTop50Peaks')
		else:
			warnEmptyAttribute("pctSaturationTop50Peaks", "XSDataDouble")
		if self.__saturationRangeAverage is not None:
			self.saturationRangeAverage.export(outfile, level, name_='saturationRangeAverage')
		if self.__saturationRangeMax is not None:
			self.saturationRangeMax.export(outfile, level, name_='saturationRangeMax')
		if self.__saturationRangeMin is not None:
			self.saturationRangeMin.export(outfile, level, name_='saturationRangeMin')
		if self.__signalRangeAverage is not None:
			self.signalRangeAverage.export(outfile, level, name_='signalRangeAverage')
		if self.__signalRangeMax is not None:
			self.signalRangeMax.export(outfile, level, name_='signalRangeMax')
		if self.__signalRangeMin is not None:
			self.signalRangeMin.export(outfile, level, name_='signalRangeMin')
		if self.__spotTotal is not None:
			self.spotTotal.export(outfile, level, name_='spotTotal')
		else:
			warnEmptyAttribute("spotTotal", "XSDataInteger")
		if self.__totalIntegratedSignal is not None:
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
		self.export( oStreamString, 0, name_="XSDataISPyBImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBImageQualityIndicators' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBImageQualityIndicators

class XSDataInputStoreAutoProc(XSDataInput):
	def __init__(self, configuration=None, AutoProcContainer=None):
		XSDataInput.__init__(self, configuration)
		self.__AutoProcContainer = AutoProcContainer
	def getAutoProcContainer(self): return self.__AutoProcContainer
	def setAutoProcContainer(self, AutoProcContainer):
		checkType("XSDataInputStoreAutoProc", "setAutoProcContainer", AutoProcContainer, "AutoProcContainer")
		self.__AutoProcContainer = AutoProcContainer
	def delAutoProcContainer(self): self.__AutoProcContainer = None
	# Properties
	AutoProcContainer = property(getAutoProcContainer, setAutoProcContainer, delAutoProcContainer, "Property for AutoProcContainer")
	def export(self, outfile, level, name_='XSDataInputStoreAutoProc'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputStoreAutoProc'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__AutoProcContainer is not None:
			self.AutoProcContainer.export(outfile, level, name_='AutoProcContainer')
		else:
			warnEmptyAttribute("AutoProcContainer", "AutoProcContainer")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'AutoProcContainer':
			obj_ = AutoProcContainer()
			obj_.build(child_)
			self.setAutoProcContainer(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputStoreAutoProc" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStoreAutoProc' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputStoreAutoProc.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreAutoProc()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputStoreAutoProc" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreAutoProc()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputStoreAutoProc

class XSDataInputStoreImageQualityIndicators(XSDataInput):
	def __init__(self, configuration=None, imageQualityIndicators=None):
		XSDataInput.__init__(self, configuration)
		self.__imageQualityIndicators = imageQualityIndicators
	def getImageQualityIndicators(self): return self.__imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataInputStoreImageQualityIndicators", "setImageQualityIndicators", imageQualityIndicators, "XSDataISPyBImageQualityIndicators")
		self.__imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self.__imageQualityIndicators = None
	# Properties
	imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
	def export(self, outfile, level, name_='XSDataInputStoreImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputStoreImageQualityIndicators'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__imageQualityIndicators is not None:
			self.imageQualityIndicators.export(outfile, level, name_='imageQualityIndicators')
		else:
			warnEmptyAttribute("imageQualityIndicators", "XSDataISPyBImageQualityIndicators")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicators':
			obj_ = XSDataISPyBImageQualityIndicators()
			obj_.build(child_)
			self.setImageQualityIndicators(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputStoreImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStoreImageQualityIndicators' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputStoreImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputStoreImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputStoreImageQualityIndicators

class XSDataResultStoreAutoProc(XSDataResult):
	def __init__(self, status=None, autoProcId=None):
		XSDataResult.__init__(self, status)
		self.__autoProcId = autoProcId
	def getAutoProcId(self): return self.__autoProcId
	def setAutoProcId(self, autoProcId):
		checkType("XSDataResultStoreAutoProc", "setAutoProcId", autoProcId, "XSDataInteger")
		self.__autoProcId = autoProcId
	def delAutoProcId(self): self.__autoProcId = None
	# Properties
	autoProcId = property(getAutoProcId, setAutoProcId, delAutoProcId, "Property for autoProcId")
	def export(self, outfile, level, name_='XSDataResultStoreAutoProc'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultStoreAutoProc'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__autoProcId is not None:
			self.autoProcId.export(outfile, level, name_='autoProcId')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'autoProcId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setAutoProcId(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultStoreAutoProc" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStoreAutoProc' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultStoreAutoProc.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreAutoProc()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultStoreAutoProc" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreAutoProc()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultStoreAutoProc

class XSDataResultStoreImageQualityIndicators(XSDataResult):
	def __init__(self, status=None, imageQualityIndicatorsId=None):
		XSDataResult.__init__(self, status)
		self.__imageQualityIndicatorsId = imageQualityIndicatorsId
	def getImageQualityIndicatorsId(self): return self.__imageQualityIndicatorsId
	def setImageQualityIndicatorsId(self, imageQualityIndicatorsId):
		checkType("XSDataResultStoreImageQualityIndicators", "setImageQualityIndicatorsId", imageQualityIndicatorsId, "XSDataInteger")
		self.__imageQualityIndicatorsId = imageQualityIndicatorsId
	def delImageQualityIndicatorsId(self): self.__imageQualityIndicatorsId = None
	# Properties
	imageQualityIndicatorsId = property(getImageQualityIndicatorsId, setImageQualityIndicatorsId, delImageQualityIndicatorsId, "Property for imageQualityIndicatorsId")
	def export(self, outfile, level, name_='XSDataResultStoreImageQualityIndicators'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultStoreImageQualityIndicators'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__imageQualityIndicatorsId is not None:
			self.imageQualityIndicatorsId.export(outfile, level, name_='imageQualityIndicatorsId')
		else:
			warnEmptyAttribute("imageQualityIndicatorsId", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicatorsId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageQualityIndicatorsId(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultStoreImageQualityIndicators" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStoreImageQualityIndicators' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultStoreImageQualityIndicators.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreImageQualityIndicators()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultStoreImageQualityIndicators" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreImageQualityIndicators()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultStoreImageQualityIndicators



# End of data representation classes.



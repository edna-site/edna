#!/usr/bin/env python

#
# Generated Thu Nov 24 05:05::51 2011 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataImage
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


class AutoProc(object):
	def __init__(self, refinedCell_gamma=None, refinedCell_beta=None, refinedCell_alpha=None, refinedCell_c=None, refinedCell_b=None, refinedCell_a=None, spaceGroup=None):
		checkType("AutoProc", "Constructor of AutoProc", spaceGroup, "string")
		self.__spaceGroup = spaceGroup
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_a, "string")
		self.__refinedCell_a = refinedCell_a
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_b, "string")
		self.__refinedCell_b = refinedCell_b
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_c, "string")
		self.__refinedCell_c = refinedCell_c
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_alpha, "string")
		self.__refinedCell_alpha = refinedCell_alpha
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_beta, "string")
		self.__refinedCell_beta = refinedCell_beta
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_gamma, "string")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProc' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProc is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcContainer(object):
	def __init__(self, AutoProcProgramContainer=None, AutoProcScalingContainer=None, AutoProc=None):
		checkType("AutoProcContainer", "Constructor of AutoProcContainer", AutoProc, "AutoProc")
		self.__AutoProc = AutoProc
		checkType("AutoProcContainer", "Constructor of AutoProcContainer", AutoProcScalingContainer, "AutoProcScalingContainer")
		self.__AutoProcScalingContainer = AutoProcScalingContainer
		checkType("AutoProcContainer", "Constructor of AutoProcContainer", AutoProcProgramContainer, "AutoProcProgramContainer")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcIntegration(object):
	def __init__(self, anomalous=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, beamVectorZ=None, beamVectorY=None, beamVectorX=None, rotationAxisZ=None, rotationAxisY=None, rotationAxisX=None, refinedYbeam=None, refinedXbeam=None, refinedDetectorDistance=None, endImageNumber=None, startImageNumber=None):
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", startImageNumber, "integer")
		self.__startImageNumber = startImageNumber
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", endImageNumber, "integer")
		self.__endImageNumber = endImageNumber
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedDetectorDistance, "float")
		self.__refinedDetectorDistance = refinedDetectorDistance
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedXbeam, "float")
		self.__refinedXbeam = refinedXbeam
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedYbeam, "float")
		self.__refinedYbeam = refinedYbeam
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisX, "float")
		self.__rotationAxisX = rotationAxisX
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisY, "float")
		self.__rotationAxisY = rotationAxisY
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisZ, "float")
		self.__rotationAxisZ = rotationAxisZ
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorX, "float")
		self.__beamVectorX = beamVectorX
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorY, "float")
		self.__beamVectorY = beamVectorY
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorZ, "float")
		self.__beamVectorZ = beamVectorZ
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_a, "float")
		self.__cell_a = cell_a
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_b, "float")
		self.__cell_b = cell_b
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_c, "float")
		self.__cell_c = cell_c
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_alpha, "float")
		self.__cell_alpha = cell_alpha
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_beta, "float")
		self.__cell_beta = cell_beta
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_gamma, "float")
		self.__cell_gamma = cell_gamma
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", anomalous, "boolean")
		self.__anomalous = anomalous
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
	def getAnomalous(self): return self.__anomalous
	def setAnomalous(self, anomalous):
		checkType("AutoProcIntegration", "setAnomalous", anomalous, "boolean")
		self.__anomalous = anomalous
	def delAnomalous(self): self.__anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
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
		if self.__anomalous is not None:
			showIndent(outfile, level)
			if self.__anomalous:
				outfile.write(unicode('<anomalous>true</anomalous>\n'))
			else:
				outfile.write(unicode('<anomalous>false</anomalous>\n'))
		else:
			warnEmptyAttribute("anomalous", "boolean")
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalous':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__anomalous = ival_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcIntegration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcIntegration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcProgram(object):
	def __init__(self, processingEnvironment=None, processingEndTime=None, processingStartTime=None, processingMessage=None, processingStatus=None, processingPrograms=None, processingCommandLine=None):
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingCommandLine, "string")
		self.__processingCommandLine = processingCommandLine
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingPrograms, "string")
		self.__processingPrograms = processingPrograms
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingStatus, "boolean")
		self.__processingStatus = processingStatus
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingMessage, "string")
		self.__processingMessage = processingMessage
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingStartTime, "string")
		self.__processingStartTime = processingStartTime
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingEndTime, "string")
		self.__processingEndTime = processingEndTime
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingEnvironment, "string")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgram' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcProgram is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcProgramAttachment(object):
	def __init__(self, filePath=None, fileName=None, fileType=None):
		checkType("AutoProcProgramAttachment", "Constructor of AutoProcProgramAttachment", fileType, "string")
		self.__fileType = fileType
		checkType("AutoProcProgramAttachment", "Constructor of AutoProcProgramAttachment", fileName, "string")
		self.__fileName = fileName
		checkType("AutoProcProgramAttachment", "Constructor of AutoProcProgramAttachment", filePath, "string")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgramAttachment' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcProgramAttachment is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcProgramContainer(object):
	def __init__(self, AutoProcProgramAttachment=None, AutoProcProgram=None):
		checkType("AutoProcProgramContainer", "Constructor of AutoProcProgramContainer", AutoProcProgram, "AutoProcProgram")
		self.__AutoProcProgram = AutoProcProgram
		if AutoProcProgramAttachment is None:
			self.__AutoProcProgramAttachment = []
		else:
			checkType("AutoProcProgramContainer", "Constructor of AutoProcProgramContainer", AutoProcProgramAttachment, "list")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcProgramContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcProgramContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcScaling(object):
	def __init__(self, recordTimeStamp=None):
		checkType("AutoProcScaling", "Constructor of AutoProcScaling", recordTimeStamp, "string")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScaling' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcScaling is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcScalingContainer(object):
	def __init__(self, AutoProcIntegrationContainer=None, AutoProcScalingStatistics=None, AutoProcScaling=None):
		checkType("AutoProcScalingContainer", "Constructor of AutoProcScalingContainer", AutoProcScaling, "AutoProcScaling")
		self.__AutoProcScaling = AutoProcScaling
		if AutoProcScalingStatistics is None:
			self.__AutoProcScalingStatistics = []
		else:
			checkType("AutoProcScalingContainer", "Constructor of AutoProcScalingContainer", AutoProcScalingStatistics, "list")
			self.__AutoProcScalingStatistics = AutoProcScalingStatistics
		checkType("AutoProcScalingContainer", "Constructor of AutoProcScalingContainer", AutoProcIntegrationContainer, "AutoProcIntegrationContainer")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScalingContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcScalingContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class Image(object):
	def __init__(self, dataCollectionId=None):
		checkType("Image", "Constructor of Image", dataCollectionId, "integer")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='Image' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class Image is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcIntegrationContainer(object):
	def __init__(self, AutoProcIntegration=None, Image=None):
		checkType("AutoProcIntegrationContainer", "Constructor of AutoProcIntegrationContainer", Image, "Image")
		self.__Image = Image
		checkType("AutoProcIntegrationContainer", "Constructor of AutoProcIntegrationContainer", AutoProcIntegration, "AutoProcIntegration")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcIntegrationContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcIntegrationContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class AutoProcScalingStatistics(object):
	def __init__(self, anomalous=None, anomalousMultiplicity=None, anomalousCompleteness=None, multiplicity=None, completeness=None, meanIOverSigI=None, ntotalUniqueObservations=None, nTotalObservations=None, fractionalPartialBias=None, rpimAllIplusIminus=None, rpimWithinIplusIminus=None, rmeasAllIplusIminus=None, rmeasWithinIplusIminus=None, rMerge=None, resolutionLimitHigh=None, resolutionLimitLow=None, comments=None, scalingStatisticsType=None):
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", scalingStatisticsType, "string")
		self.__scalingStatisticsType = scalingStatisticsType
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", comments, "string")
		self.__comments = comments
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", resolutionLimitLow, "float")
		self.__resolutionLimitLow = resolutionLimitLow
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", resolutionLimitHigh, "float")
		self.__resolutionLimitHigh = resolutionLimitHigh
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rMerge, "float")
		self.__rMerge = rMerge
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rmeasWithinIplusIminus, "float")
		self.__rmeasWithinIplusIminus = rmeasWithinIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rmeasAllIplusIminus, "float")
		self.__rmeasAllIplusIminus = rmeasAllIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rpimWithinIplusIminus, "float")
		self.__rpimWithinIplusIminus = rpimWithinIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rpimAllIplusIminus, "float")
		self.__rpimAllIplusIminus = rpimAllIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", fractionalPartialBias, "float")
		self.__fractionalPartialBias = fractionalPartialBias
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", nTotalObservations, "float")
		self.__nTotalObservations = nTotalObservations
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", ntotalUniqueObservations, "integer")
		self.__ntotalUniqueObservations = ntotalUniqueObservations
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", meanIOverSigI, "float")
		self.__meanIOverSigI = meanIOverSigI
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", completeness, "float")
		self.__completeness = completeness
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", multiplicity, "float")
		self.__multiplicity = multiplicity
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalousCompleteness, "float")
		self.__anomalousCompleteness = anomalousCompleteness
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalousMultiplicity, "float")
		self.__anomalousMultiplicity = anomalousMultiplicity
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalous, "boolean")
		self.__anomalous = anomalous
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
	def getAnomalous(self): return self.__anomalous
	def setAnomalous(self, anomalous):
		checkType("AutoProcScalingStatistics", "setAnomalous", anomalous, "boolean")
		self.__anomalous = anomalous
	def delAnomalous(self): self.__anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
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
		if self.__anomalous is not None:
			showIndent(outfile, level)
			if self.__anomalous:
				outfile.write(unicode('<anomalous>true</anomalous>\n'))
			else:
				outfile.write(unicode('<anomalous>false</anomalous>\n'))
		else:
			warnEmptyAttribute("anomalous", "boolean")
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalous':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__anomalous = ival_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="AutoProcScalingStatistics" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='AutoProcScalingStatistics' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class AutoProcScalingStatistics is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataISPyBDataCollection(object):
	def __init__(self, beamShape=None, xtalSnapshotFullPath4=None, xtalSnapshotFullPath3=None, xtalSnapshotFullPath2=None, xtalSnapshotFullPath1=None, printableForReport=None, comments=None, averageTemperature=None, centeringMethod=None, synchrotronMode=None, transmission=None, beamSizeAtSampleY=None, beamSizeAtSampleX=None, slitGapHorizontal=None, slitGapVertical=None, crystalClass=None, ybeam=None, xbeam=None, undulatorGap3=None, undulatorGap2=None, undulatorGap1=None, detectorMode=None, detector2theta=None, detectorDistance=None, resolutionAtCorner=None, resolution=None, wavelength=None, fileTemplate=None, imageSuffix=None, imagePrefix=None, imageDirectory=None, exposureTime=None, numberOfPasses=None, startImageNumber=None, numberOfImages=None, overlap=None, axisRange=None, axisEnd=None, axisStart=None, omegaStart=None, kappaStart=None, phiStart=None, rotationAxis=None, runStatus=None, endDate=None, startDate=None, dataCollectionNumber=None, experimentType=None, sessionId=None, blSampleId=None, dataCollectionId=None):
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", dataCollectionId, "integer")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", blSampleId, "integer")
		self.__blSampleId = blSampleId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", sessionId, "integer")
		self.__sessionId = sessionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", experimentType, "string")
		self.__experimentType = experimentType
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", dataCollectionNumber, "integer")
		self.__dataCollectionNumber = dataCollectionNumber
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", startDate, "string")
		self.__startDate = startDate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", endDate, "string")
		self.__endDate = endDate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", runStatus, "string")
		self.__runStatus = runStatus
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", rotationAxis, "string")
		self.__rotationAxis = rotationAxis
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", phiStart, "float")
		self.__phiStart = phiStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", kappaStart, "float")
		self.__kappaStart = kappaStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", omegaStart, "float")
		self.__omegaStart = omegaStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisStart, "float")
		self.__axisStart = axisStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisEnd, "float")
		self.__axisEnd = axisEnd
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisRange, "float")
		self.__axisRange = axisRange
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", overlap, "float")
		self.__overlap = overlap
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", numberOfImages, "integer")
		self.__numberOfImages = numberOfImages
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", startImageNumber, "integer")
		self.__startImageNumber = startImageNumber
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", numberOfPasses, "integer")
		self.__numberOfPasses = numberOfPasses
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", exposureTime, "float")
		self.__exposureTime = exposureTime
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imageDirectory, "string")
		self.__imageDirectory = imageDirectory
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imagePrefix, "string")
		self.__imagePrefix = imagePrefix
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imageSuffix, "string")
		self.__imageSuffix = imageSuffix
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", fileTemplate, "string")
		self.__fileTemplate = fileTemplate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", wavelength, "float")
		self.__wavelength = wavelength
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", resolution, "float")
		self.__resolution = resolution
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", resolutionAtCorner, "float")
		self.__resolutionAtCorner = resolutionAtCorner
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detectorDistance, "float")
		self.__detectorDistance = detectorDistance
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detector2theta, "float")
		self.__detector2theta = detector2theta
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detectorMode, "string")
		self.__detectorMode = detectorMode
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap1, "float")
		self.__undulatorGap1 = undulatorGap1
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap2, "float")
		self.__undulatorGap2 = undulatorGap2
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap3, "float")
		self.__undulatorGap3 = undulatorGap3
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xbeam, "float")
		self.__xbeam = xbeam
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", ybeam, "float")
		self.__ybeam = ybeam
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", crystalClass, "string")
		self.__crystalClass = crystalClass
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", slitGapVertical, "float")
		self.__slitGapVertical = slitGapVertical
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", slitGapHorizontal, "float")
		self.__slitGapHorizontal = slitGapHorizontal
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamSizeAtSampleX, "float")
		self.__beamSizeAtSampleX = beamSizeAtSampleX
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamSizeAtSampleY, "float")
		self.__beamSizeAtSampleY = beamSizeAtSampleY
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", transmission, "float")
		self.__transmission = transmission
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", synchrotronMode, "string")
		self.__synchrotronMode = synchrotronMode
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", centeringMethod, "string")
		self.__centeringMethod = centeringMethod
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", averageTemperature, "float")
		self.__averageTemperature = averageTemperature
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", comments, "string")
		self.__comments = comments
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", printableForReport, "boolean")
		self.__printableForReport = printableForReport
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath1, "string")
		self.__xtalSnapshotFullPath1 = xtalSnapshotFullPath1
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath2, "string")
		self.__xtalSnapshotFullPath2 = xtalSnapshotFullPath2
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath3, "string")
		self.__xtalSnapshotFullPath3 = xtalSnapshotFullPath3
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath4, "string")
		self.__xtalSnapshotFullPath4 = xtalSnapshotFullPath4
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamShape, "string")
		self.__beamShape = beamShape
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBDataCollection", "setDataCollectionId", dataCollectionId, "integer")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getBlSampleId(self): return self.__blSampleId
	def setBlSampleId(self, blSampleId):
		checkType("XSDataISPyBDataCollection", "setBlSampleId", blSampleId, "integer")
		self.__blSampleId = blSampleId
	def delBlSampleId(self): self.__blSampleId = None
	# Properties
	blSampleId = property(getBlSampleId, setBlSampleId, delBlSampleId, "Property for blSampleId")
	def getSessionId(self): return self.__sessionId
	def setSessionId(self, sessionId):
		checkType("XSDataISPyBDataCollection", "setSessionId", sessionId, "integer")
		self.__sessionId = sessionId
	def delSessionId(self): self.__sessionId = None
	# Properties
	sessionId = property(getSessionId, setSessionId, delSessionId, "Property for sessionId")
	def getExperimentType(self): return self.__experimentType
	def setExperimentType(self, experimentType):
		checkType("XSDataISPyBDataCollection", "setExperimentType", experimentType, "string")
		self.__experimentType = experimentType
	def delExperimentType(self): self.__experimentType = None
	# Properties
	experimentType = property(getExperimentType, setExperimentType, delExperimentType, "Property for experimentType")
	def getDataCollectionNumber(self): return self.__dataCollectionNumber
	def setDataCollectionNumber(self, dataCollectionNumber):
		checkType("XSDataISPyBDataCollection", "setDataCollectionNumber", dataCollectionNumber, "integer")
		self.__dataCollectionNumber = dataCollectionNumber
	def delDataCollectionNumber(self): self.__dataCollectionNumber = None
	# Properties
	dataCollectionNumber = property(getDataCollectionNumber, setDataCollectionNumber, delDataCollectionNumber, "Property for dataCollectionNumber")
	def getStartDate(self): return self.__startDate
	def setStartDate(self, startDate):
		checkType("XSDataISPyBDataCollection", "setStartDate", startDate, "string")
		self.__startDate = startDate
	def delStartDate(self): self.__startDate = None
	# Properties
	startDate = property(getStartDate, setStartDate, delStartDate, "Property for startDate")
	def getEndDate(self): return self.__endDate
	def setEndDate(self, endDate):
		checkType("XSDataISPyBDataCollection", "setEndDate", endDate, "string")
		self.__endDate = endDate
	def delEndDate(self): self.__endDate = None
	# Properties
	endDate = property(getEndDate, setEndDate, delEndDate, "Property for endDate")
	def getRunStatus(self): return self.__runStatus
	def setRunStatus(self, runStatus):
		checkType("XSDataISPyBDataCollection", "setRunStatus", runStatus, "string")
		self.__runStatus = runStatus
	def delRunStatus(self): self.__runStatus = None
	# Properties
	runStatus = property(getRunStatus, setRunStatus, delRunStatus, "Property for runStatus")
	def getRotationAxis(self): return self.__rotationAxis
	def setRotationAxis(self, rotationAxis):
		checkType("XSDataISPyBDataCollection", "setRotationAxis", rotationAxis, "string")
		self.__rotationAxis = rotationAxis
	def delRotationAxis(self): self.__rotationAxis = None
	# Properties
	rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
	def getPhiStart(self): return self.__phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataISPyBDataCollection", "setPhiStart", phiStart, "float")
		self.__phiStart = phiStart
	def delPhiStart(self): self.__phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getKappaStart(self): return self.__kappaStart
	def setKappaStart(self, kappaStart):
		checkType("XSDataISPyBDataCollection", "setKappaStart", kappaStart, "float")
		self.__kappaStart = kappaStart
	def delKappaStart(self): self.__kappaStart = None
	# Properties
	kappaStart = property(getKappaStart, setKappaStart, delKappaStart, "Property for kappaStart")
	def getOmegaStart(self): return self.__omegaStart
	def setOmegaStart(self, omegaStart):
		checkType("XSDataISPyBDataCollection", "setOmegaStart", omegaStart, "float")
		self.__omegaStart = omegaStart
	def delOmegaStart(self): self.__omegaStart = None
	# Properties
	omegaStart = property(getOmegaStart, setOmegaStart, delOmegaStart, "Property for omegaStart")
	def getAxisStart(self): return self.__axisStart
	def setAxisStart(self, axisStart):
		checkType("XSDataISPyBDataCollection", "setAxisStart", axisStart, "float")
		self.__axisStart = axisStart
	def delAxisStart(self): self.__axisStart = None
	# Properties
	axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
	def getAxisEnd(self): return self.__axisEnd
	def setAxisEnd(self, axisEnd):
		checkType("XSDataISPyBDataCollection", "setAxisEnd", axisEnd, "float")
		self.__axisEnd = axisEnd
	def delAxisEnd(self): self.__axisEnd = None
	# Properties
	axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
	def getAxisRange(self): return self.__axisRange
	def setAxisRange(self, axisRange):
		checkType("XSDataISPyBDataCollection", "setAxisRange", axisRange, "float")
		self.__axisRange = axisRange
	def delAxisRange(self): self.__axisRange = None
	# Properties
	axisRange = property(getAxisRange, setAxisRange, delAxisRange, "Property for axisRange")
	def getOverlap(self): return self.__overlap
	def setOverlap(self, overlap):
		checkType("XSDataISPyBDataCollection", "setOverlap", overlap, "float")
		self.__overlap = overlap
	def delOverlap(self): self.__overlap = None
	# Properties
	overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
	def getNumberOfImages(self): return self.__numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBDataCollection", "setNumberOfImages", numberOfImages, "integer")
		self.__numberOfImages = numberOfImages
	def delNumberOfImages(self): self.__numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getStartImageNumber(self): return self.__startImageNumber
	def setStartImageNumber(self, startImageNumber):
		checkType("XSDataISPyBDataCollection", "setStartImageNumber", startImageNumber, "integer")
		self.__startImageNumber = startImageNumber
	def delStartImageNumber(self): self.__startImageNumber = None
	# Properties
	startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
	def getNumberOfPasses(self): return self.__numberOfPasses
	def setNumberOfPasses(self, numberOfPasses):
		checkType("XSDataISPyBDataCollection", "setNumberOfPasses", numberOfPasses, "integer")
		self.__numberOfPasses = numberOfPasses
	def delNumberOfPasses(self): self.__numberOfPasses = None
	# Properties
	numberOfPasses = property(getNumberOfPasses, setNumberOfPasses, delNumberOfPasses, "Property for numberOfPasses")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBDataCollection", "setExposureTime", exposureTime, "float")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getImageDirectory(self): return self.__imageDirectory
	def setImageDirectory(self, imageDirectory):
		checkType("XSDataISPyBDataCollection", "setImageDirectory", imageDirectory, "string")
		self.__imageDirectory = imageDirectory
	def delImageDirectory(self): self.__imageDirectory = None
	# Properties
	imageDirectory = property(getImageDirectory, setImageDirectory, delImageDirectory, "Property for imageDirectory")
	def getImagePrefix(self): return self.__imagePrefix
	def setImagePrefix(self, imagePrefix):
		checkType("XSDataISPyBDataCollection", "setImagePrefix", imagePrefix, "string")
		self.__imagePrefix = imagePrefix
	def delImagePrefix(self): self.__imagePrefix = None
	# Properties
	imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
	def getImageSuffix(self): return self.__imageSuffix
	def setImageSuffix(self, imageSuffix):
		checkType("XSDataISPyBDataCollection", "setImageSuffix", imageSuffix, "string")
		self.__imageSuffix = imageSuffix
	def delImageSuffix(self): self.__imageSuffix = None
	# Properties
	imageSuffix = property(getImageSuffix, setImageSuffix, delImageSuffix, "Property for imageSuffix")
	def getFileTemplate(self): return self.__fileTemplate
	def setFileTemplate(self, fileTemplate):
		checkType("XSDataISPyBDataCollection", "setFileTemplate", fileTemplate, "string")
		self.__fileTemplate = fileTemplate
	def delFileTemplate(self): self.__fileTemplate = None
	# Properties
	fileTemplate = property(getFileTemplate, setFileTemplate, delFileTemplate, "Property for fileTemplate")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataISPyBDataCollection", "setWavelength", wavelength, "float")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBDataCollection", "setResolution", resolution, "float")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolutionAtCorner(self): return self.__resolutionAtCorner
	def setResolutionAtCorner(self, resolutionAtCorner):
		checkType("XSDataISPyBDataCollection", "setResolutionAtCorner", resolutionAtCorner, "float")
		self.__resolutionAtCorner = resolutionAtCorner
	def delResolutionAtCorner(self): self.__resolutionAtCorner = None
	# Properties
	resolutionAtCorner = property(getResolutionAtCorner, setResolutionAtCorner, delResolutionAtCorner, "Property for resolutionAtCorner")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataISPyBDataCollection", "setDetectorDistance", detectorDistance, "float")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getDetector2theta(self): return self.__detector2theta
	def setDetector2theta(self, detector2theta):
		checkType("XSDataISPyBDataCollection", "setDetector2theta", detector2theta, "float")
		self.__detector2theta = detector2theta
	def delDetector2theta(self): self.__detector2theta = None
	# Properties
	detector2theta = property(getDetector2theta, setDetector2theta, delDetector2theta, "Property for detector2theta")
	def getDetectorMode(self): return self.__detectorMode
	def setDetectorMode(self, detectorMode):
		checkType("XSDataISPyBDataCollection", "setDetectorMode", detectorMode, "string")
		self.__detectorMode = detectorMode
	def delDetectorMode(self): self.__detectorMode = None
	# Properties
	detectorMode = property(getDetectorMode, setDetectorMode, delDetectorMode, "Property for detectorMode")
	def getUndulatorGap1(self): return self.__undulatorGap1
	def setUndulatorGap1(self, undulatorGap1):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap1", undulatorGap1, "float")
		self.__undulatorGap1 = undulatorGap1
	def delUndulatorGap1(self): self.__undulatorGap1 = None
	# Properties
	undulatorGap1 = property(getUndulatorGap1, setUndulatorGap1, delUndulatorGap1, "Property for undulatorGap1")
	def getUndulatorGap2(self): return self.__undulatorGap2
	def setUndulatorGap2(self, undulatorGap2):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap2", undulatorGap2, "float")
		self.__undulatorGap2 = undulatorGap2
	def delUndulatorGap2(self): self.__undulatorGap2 = None
	# Properties
	undulatorGap2 = property(getUndulatorGap2, setUndulatorGap2, delUndulatorGap2, "Property for undulatorGap2")
	def getUndulatorGap3(self): return self.__undulatorGap3
	def setUndulatorGap3(self, undulatorGap3):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap3", undulatorGap3, "float")
		self.__undulatorGap3 = undulatorGap3
	def delUndulatorGap3(self): self.__undulatorGap3 = None
	# Properties
	undulatorGap3 = property(getUndulatorGap3, setUndulatorGap3, delUndulatorGap3, "Property for undulatorGap3")
	def getXbeam(self): return self.__xbeam
	def setXbeam(self, xbeam):
		checkType("XSDataISPyBDataCollection", "setXbeam", xbeam, "float")
		self.__xbeam = xbeam
	def delXbeam(self): self.__xbeam = None
	# Properties
	xbeam = property(getXbeam, setXbeam, delXbeam, "Property for xbeam")
	def getYbeam(self): return self.__ybeam
	def setYbeam(self, ybeam):
		checkType("XSDataISPyBDataCollection", "setYbeam", ybeam, "float")
		self.__ybeam = ybeam
	def delYbeam(self): self.__ybeam = None
	# Properties
	ybeam = property(getYbeam, setYbeam, delYbeam, "Property for ybeam")
	def getCrystalClass(self): return self.__crystalClass
	def setCrystalClass(self, crystalClass):
		checkType("XSDataISPyBDataCollection", "setCrystalClass", crystalClass, "string")
		self.__crystalClass = crystalClass
	def delCrystalClass(self): self.__crystalClass = None
	# Properties
	crystalClass = property(getCrystalClass, setCrystalClass, delCrystalClass, "Property for crystalClass")
	def getSlitGapVertical(self): return self.__slitGapVertical
	def setSlitGapVertical(self, slitGapVertical):
		checkType("XSDataISPyBDataCollection", "setSlitGapVertical", slitGapVertical, "float")
		self.__slitGapVertical = slitGapVertical
	def delSlitGapVertical(self): self.__slitGapVertical = None
	# Properties
	slitGapVertical = property(getSlitGapVertical, setSlitGapVertical, delSlitGapVertical, "Property for slitGapVertical")
	def getSlitGapHorizontal(self): return self.__slitGapHorizontal
	def setSlitGapHorizontal(self, slitGapHorizontal):
		checkType("XSDataISPyBDataCollection", "setSlitGapHorizontal", slitGapHorizontal, "float")
		self.__slitGapHorizontal = slitGapHorizontal
	def delSlitGapHorizontal(self): self.__slitGapHorizontal = None
	# Properties
	slitGapHorizontal = property(getSlitGapHorizontal, setSlitGapHorizontal, delSlitGapHorizontal, "Property for slitGapHorizontal")
	def getBeamSizeAtSampleX(self): return self.__beamSizeAtSampleX
	def setBeamSizeAtSampleX(self, beamSizeAtSampleX):
		checkType("XSDataISPyBDataCollection", "setBeamSizeAtSampleX", beamSizeAtSampleX, "float")
		self.__beamSizeAtSampleX = beamSizeAtSampleX
	def delBeamSizeAtSampleX(self): self.__beamSizeAtSampleX = None
	# Properties
	beamSizeAtSampleX = property(getBeamSizeAtSampleX, setBeamSizeAtSampleX, delBeamSizeAtSampleX, "Property for beamSizeAtSampleX")
	def getBeamSizeAtSampleY(self): return self.__beamSizeAtSampleY
	def setBeamSizeAtSampleY(self, beamSizeAtSampleY):
		checkType("XSDataISPyBDataCollection", "setBeamSizeAtSampleY", beamSizeAtSampleY, "float")
		self.__beamSizeAtSampleY = beamSizeAtSampleY
	def delBeamSizeAtSampleY(self): self.__beamSizeAtSampleY = None
	# Properties
	beamSizeAtSampleY = property(getBeamSizeAtSampleY, setBeamSizeAtSampleY, delBeamSizeAtSampleY, "Property for beamSizeAtSampleY")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBDataCollection", "setTransmission", transmission, "float")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getSynchrotronMode(self): return self.__synchrotronMode
	def setSynchrotronMode(self, synchrotronMode):
		checkType("XSDataISPyBDataCollection", "setSynchrotronMode", synchrotronMode, "string")
		self.__synchrotronMode = synchrotronMode
	def delSynchrotronMode(self): self.__synchrotronMode = None
	# Properties
	synchrotronMode = property(getSynchrotronMode, setSynchrotronMode, delSynchrotronMode, "Property for synchrotronMode")
	def getCenteringMethod(self): return self.__centeringMethod
	def setCenteringMethod(self, centeringMethod):
		checkType("XSDataISPyBDataCollection", "setCenteringMethod", centeringMethod, "string")
		self.__centeringMethod = centeringMethod
	def delCenteringMethod(self): self.__centeringMethod = None
	# Properties
	centeringMethod = property(getCenteringMethod, setCenteringMethod, delCenteringMethod, "Property for centeringMethod")
	def getAverageTemperature(self): return self.__averageTemperature
	def setAverageTemperature(self, averageTemperature):
		checkType("XSDataISPyBDataCollection", "setAverageTemperature", averageTemperature, "float")
		self.__averageTemperature = averageTemperature
	def delAverageTemperature(self): self.__averageTemperature = None
	# Properties
	averageTemperature = property(getAverageTemperature, setAverageTemperature, delAverageTemperature, "Property for averageTemperature")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataISPyBDataCollection", "setComments", comments, "string")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getPrintableForReport(self): return self.__printableForReport
	def setPrintableForReport(self, printableForReport):
		checkType("XSDataISPyBDataCollection", "setPrintableForReport", printableForReport, "boolean")
		self.__printableForReport = printableForReport
	def delPrintableForReport(self): self.__printableForReport = None
	# Properties
	printableForReport = property(getPrintableForReport, setPrintableForReport, delPrintableForReport, "Property for printableForReport")
	def getXtalSnapshotFullPath1(self): return self.__xtalSnapshotFullPath1
	def setXtalSnapshotFullPath1(self, xtalSnapshotFullPath1):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath1", xtalSnapshotFullPath1, "string")
		self.__xtalSnapshotFullPath1 = xtalSnapshotFullPath1
	def delXtalSnapshotFullPath1(self): self.__xtalSnapshotFullPath1 = None
	# Properties
	xtalSnapshotFullPath1 = property(getXtalSnapshotFullPath1, setXtalSnapshotFullPath1, delXtalSnapshotFullPath1, "Property for xtalSnapshotFullPath1")
	def getXtalSnapshotFullPath2(self): return self.__xtalSnapshotFullPath2
	def setXtalSnapshotFullPath2(self, xtalSnapshotFullPath2):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath2", xtalSnapshotFullPath2, "string")
		self.__xtalSnapshotFullPath2 = xtalSnapshotFullPath2
	def delXtalSnapshotFullPath2(self): self.__xtalSnapshotFullPath2 = None
	# Properties
	xtalSnapshotFullPath2 = property(getXtalSnapshotFullPath2, setXtalSnapshotFullPath2, delXtalSnapshotFullPath2, "Property for xtalSnapshotFullPath2")
	def getXtalSnapshotFullPath3(self): return self.__xtalSnapshotFullPath3
	def setXtalSnapshotFullPath3(self, xtalSnapshotFullPath3):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath3", xtalSnapshotFullPath3, "string")
		self.__xtalSnapshotFullPath3 = xtalSnapshotFullPath3
	def delXtalSnapshotFullPath3(self): self.__xtalSnapshotFullPath3 = None
	# Properties
	xtalSnapshotFullPath3 = property(getXtalSnapshotFullPath3, setXtalSnapshotFullPath3, delXtalSnapshotFullPath3, "Property for xtalSnapshotFullPath3")
	def getXtalSnapshotFullPath4(self): return self.__xtalSnapshotFullPath4
	def setXtalSnapshotFullPath4(self, xtalSnapshotFullPath4):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath4", xtalSnapshotFullPath4, "string")
		self.__xtalSnapshotFullPath4 = xtalSnapshotFullPath4
	def delXtalSnapshotFullPath4(self): self.__xtalSnapshotFullPath4 = None
	# Properties
	xtalSnapshotFullPath4 = property(getXtalSnapshotFullPath4, setXtalSnapshotFullPath4, delXtalSnapshotFullPath4, "Property for xtalSnapshotFullPath4")
	def getBeamShape(self): return self.__beamShape
	def setBeamShape(self, beamShape):
		checkType("XSDataISPyBDataCollection", "setBeamShape", beamShape, "string")
		self.__beamShape = beamShape
	def delBeamShape(self): self.__beamShape = None
	# Properties
	beamShape = property(getBeamShape, setBeamShape, delBeamShape, "Property for beamShape")
	def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
		pass
		if self.__dataCollectionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self.__dataCollectionId))
		else:
			warnEmptyAttribute("dataCollectionId", "integer")
		if self.__blSampleId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<blSampleId>%d</blSampleId>\n' % self.__blSampleId))
		else:
			warnEmptyAttribute("blSampleId", "integer")
		if self.__sessionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<sessionId>%d</sessionId>\n' % self.__sessionId))
		else:
			warnEmptyAttribute("sessionId", "integer")
		if self.__experimentType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<experimentType>%s</experimentType>\n' % self.__experimentType))
		else:
			warnEmptyAttribute("experimentType", "string")
		if self.__dataCollectionNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionNumber>%d</dataCollectionNumber>\n' % self.__dataCollectionNumber))
		else:
			warnEmptyAttribute("dataCollectionNumber", "integer")
		if self.__startDate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startDate>%s</startDate>\n' % self.__startDate))
		else:
			warnEmptyAttribute("startDate", "string")
		if self.__endDate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<endDate>%s</endDate>\n' % self.__endDate))
		else:
			warnEmptyAttribute("endDate", "string")
		if self.__runStatus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<runStatus>%s</runStatus>\n' % self.__runStatus))
		else:
			warnEmptyAttribute("runStatus", "string")
		if self.__rotationAxis is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxis>%s</rotationAxis>\n' % self.__rotationAxis))
		else:
			warnEmptyAttribute("rotationAxis", "string")
		if self.__phiStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<phiStart>%e</phiStart>\n' % self.__phiStart))
		else:
			warnEmptyAttribute("phiStart", "float")
		if self.__kappaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<kappaStart>%e</kappaStart>\n' % self.__kappaStart))
		else:
			warnEmptyAttribute("kappaStart", "float")
		if self.__omegaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<omegaStart>%e</omegaStart>\n' % self.__omegaStart))
		else:
			warnEmptyAttribute("omegaStart", "float")
		if self.__axisStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisStart>%e</axisStart>\n' % self.__axisStart))
		else:
			warnEmptyAttribute("axisStart", "float")
		if self.__axisEnd is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisEnd>%e</axisEnd>\n' % self.__axisEnd))
		else:
			warnEmptyAttribute("axisEnd", "float")
		if self.__axisRange is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisRange>%e</axisRange>\n' % self.__axisRange))
		else:
			warnEmptyAttribute("axisRange", "float")
		if self.__overlap is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<overlap>%e</overlap>\n' % self.__overlap))
		else:
			warnEmptyAttribute("overlap", "float")
		if self.__numberOfImages is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<numberOfImages>%d</numberOfImages>\n' % self.__numberOfImages))
		else:
			warnEmptyAttribute("numberOfImages", "integer")
		if self.__startImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self.__startImageNumber))
		else:
			warnEmptyAttribute("startImageNumber", "integer")
		if self.__numberOfPasses is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<numberOfPasses>%d</numberOfPasses>\n' % self.__numberOfPasses))
		else:
			warnEmptyAttribute("numberOfPasses", "integer")
		if self.__exposureTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<exposureTime>%e</exposureTime>\n' % self.__exposureTime))
		else:
			warnEmptyAttribute("exposureTime", "float")
		if self.__imageDirectory is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imageDirectory>%s</imageDirectory>\n' % self.__imageDirectory))
		else:
			warnEmptyAttribute("imageDirectory", "string")
		if self.__imagePrefix is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imagePrefix>%s</imagePrefix>\n' % self.__imagePrefix))
		else:
			warnEmptyAttribute("imagePrefix", "string")
		if self.__imageSuffix is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imageSuffix>%s</imageSuffix>\n' % self.__imageSuffix))
		else:
			warnEmptyAttribute("imageSuffix", "string")
		if self.__fileTemplate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileTemplate>%s</fileTemplate>\n' % self.__fileTemplate))
		else:
			warnEmptyAttribute("fileTemplate", "string")
		if self.__wavelength is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<wavelength>%e</wavelength>\n' % self.__wavelength))
		else:
			warnEmptyAttribute("wavelength", "float")
		if self.__resolution is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolution>%e</resolution>\n' % self.__resolution))
		else:
			warnEmptyAttribute("resolution", "float")
		if self.__resolutionAtCorner is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionAtCorner>%e</resolutionAtCorner>\n' % self.__resolutionAtCorner))
		else:
			warnEmptyAttribute("resolutionAtCorner", "float")
		if self.__detectorDistance is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detectorDistance>%e</detectorDistance>\n' % self.__detectorDistance))
		else:
			warnEmptyAttribute("detectorDistance", "float")
		if self.__detector2theta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detector2theta>%e</detector2theta>\n' % self.__detector2theta))
		else:
			warnEmptyAttribute("detector2theta", "float")
		if self.__detectorMode is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detectorMode>%s</detectorMode>\n' % self.__detectorMode))
		else:
			warnEmptyAttribute("detectorMode", "string")
		if self.__undulatorGap1 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap1>%e</undulatorGap1>\n' % self.__undulatorGap1))
		else:
			warnEmptyAttribute("undulatorGap1", "float")
		if self.__undulatorGap2 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap2>%e</undulatorGap2>\n' % self.__undulatorGap2))
		else:
			warnEmptyAttribute("undulatorGap2", "float")
		if self.__undulatorGap3 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap3>%e</undulatorGap3>\n' % self.__undulatorGap3))
		else:
			warnEmptyAttribute("undulatorGap3", "float")
		if self.__xbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xbeam>%e</xbeam>\n' % self.__xbeam))
		else:
			warnEmptyAttribute("xbeam", "float")
		if self.__ybeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ybeam>%e</ybeam>\n' % self.__ybeam))
		else:
			warnEmptyAttribute("ybeam", "float")
		if self.__crystalClass is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<crystalClass>%s</crystalClass>\n' % self.__crystalClass))
		else:
			warnEmptyAttribute("crystalClass", "string")
		if self.__slitGapVertical is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<slitGapVertical>%e</slitGapVertical>\n' % self.__slitGapVertical))
		else:
			warnEmptyAttribute("slitGapVertical", "float")
		if self.__slitGapHorizontal is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<slitGapHorizontal>%e</slitGapHorizontal>\n' % self.__slitGapHorizontal))
		else:
			warnEmptyAttribute("slitGapHorizontal", "float")
		if self.__beamSizeAtSampleX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamSizeAtSampleX>%e</beamSizeAtSampleX>\n' % self.__beamSizeAtSampleX))
		else:
			warnEmptyAttribute("beamSizeAtSampleX", "float")
		if self.__beamSizeAtSampleY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamSizeAtSampleY>%e</beamSizeAtSampleY>\n' % self.__beamSizeAtSampleY))
		else:
			warnEmptyAttribute("beamSizeAtSampleY", "float")
		if self.__transmission is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<transmission>%e</transmission>\n' % self.__transmission))
		else:
			warnEmptyAttribute("transmission", "float")
		if self.__synchrotronMode is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<synchrotronMode>%s</synchrotronMode>\n' % self.__synchrotronMode))
		else:
			warnEmptyAttribute("synchrotronMode", "string")
		if self.__centeringMethod is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<centeringMethod>%s</centeringMethod>\n' % self.__centeringMethod))
		else:
			warnEmptyAttribute("centeringMethod", "string")
		if self.__averageTemperature is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<averageTemperature>%e</averageTemperature>\n' % self.__averageTemperature))
		else:
			warnEmptyAttribute("averageTemperature", "float")
		if self.__comments is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comments>%s</comments>\n' % self.__comments))
		else:
			warnEmptyAttribute("comments", "string")
		if self.__printableForReport is not None:
			showIndent(outfile, level)
			if self.__printableForReport:
				outfile.write(unicode('<printableForReport>true</printableForReport>\n'))
			else:
				outfile.write(unicode('<printableForReport>false</printableForReport>\n'))
		else:
			warnEmptyAttribute("printableForReport", "boolean")
		if self.__xtalSnapshotFullPath1 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath1>%s</xtalSnapshotFullPath1>\n' % self.__xtalSnapshotFullPath1))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath1", "string")
		if self.__xtalSnapshotFullPath2 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath2>%s</xtalSnapshotFullPath2>\n' % self.__xtalSnapshotFullPath2))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath2", "string")
		if self.__xtalSnapshotFullPath3 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath3>%s</xtalSnapshotFullPath3>\n' % self.__xtalSnapshotFullPath3))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath3", "string")
		if self.__xtalSnapshotFullPath4 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath4>%s</xtalSnapshotFullPath4>\n' % self.__xtalSnapshotFullPath4))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath4", "string")
		if self.__beamShape is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamShape>%s</beamShape>\n' % self.__beamShape))
		else:
			warnEmptyAttribute("beamShape", "string")
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'blSampleId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__blSampleId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sessionId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__sessionId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__experimentType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__dataCollectionNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startDate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__startDate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'endDate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__endDate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'runStatus':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__runStatus = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxis':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__rotationAxis = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__phiStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__kappaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omegaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__omegaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__axisStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisEnd':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__axisEnd = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisRange':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__axisRange = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overlap':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__overlap = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__numberOfImages = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startImageNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__startImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfPasses':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__numberOfPasses = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__exposureTime = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageDirectory':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__imageDirectory = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagePrefix':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__imagePrefix = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageSuffix':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__imageSuffix = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileTemplate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__fileTemplate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__wavelength = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolution = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionAtCorner':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolutionAtCorner = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistance':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__detectorDistance = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector2theta':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__detector2theta = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorMode':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__detectorMode = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap1':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__undulatorGap1 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap2':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__undulatorGap2 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap3':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__undulatorGap3 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__xbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ybeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__ybeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalClass':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__crystalClass = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slitGapVertical':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__slitGapVertical = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slitGapHorizontal':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__slitGapHorizontal = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeAtSampleX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beamSizeAtSampleX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeAtSampleY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beamSizeAtSampleY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__transmission = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'synchrotronMode':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__synchrotronMode = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'centeringMethod':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__centeringMethod = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageTemperature':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__averageTemperature = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comments = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'printableForReport':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__printableForReport = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath1':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xtalSnapshotFullPath1 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath2':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xtalSnapshotFullPath2 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath3':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xtalSnapshotFullPath3 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath4':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__xtalSnapshotFullPath4 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShape':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__beamShape = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBDataCollection

class XSDataISPyBImageQualityIndicators(XSData):
	def __init__(self, totalIntegratedSignal=None, spotTotal=None, signalRangeMin=None, signalRangeMax=None, signalRangeAverage=None, saturationRangeMin=None, saturationRangeMax=None, saturationRangeAverage=None, pctSaturationTop50Peaks=None, method2Res=None, method1Res=None, maxUnitCell=None, inResolutionOvrlSpots=None, inResTotal=None, image=None, iceRings=None, goodBraggCandidates=None, binPopCutOffMethod2Res=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", binPopCutOffMethod2Res, "XSDataDouble")
		self.__binPopCutOffMethod2Res = binPopCutOffMethod2Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", goodBraggCandidates, "XSDataInteger")
		self.__goodBraggCandidates = goodBraggCandidates
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", iceRings, "XSDataInteger")
		self.__iceRings = iceRings
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", image, "XSDataImage")
		self.__image = image
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", inResTotal, "XSDataInteger")
		self.__inResTotal = inResTotal
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", inResolutionOvrlSpots, "XSDataInteger")
		self.__inResolutionOvrlSpots = inResolutionOvrlSpots
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", maxUnitCell, "XSDataDouble")
		self.__maxUnitCell = maxUnitCell
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", method1Res, "XSDataDouble")
		self.__method1Res = method1Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", method2Res, "XSDataDouble")
		self.__method2Res = method2Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", pctSaturationTop50Peaks, "XSDataDouble")
		self.__pctSaturationTop50Peaks = pctSaturationTop50Peaks
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeAverage, "XSDataDouble")
		self.__saturationRangeAverage = saturationRangeAverage
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeMax, "XSDataDouble")
		self.__saturationRangeMax = saturationRangeMax
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeMin, "XSDataDouble")
		self.__saturationRangeMin = saturationRangeMin
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeAverage, "XSDataDouble")
		self.__signalRangeAverage = signalRangeAverage
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeMax, "XSDataDouble")
		self.__signalRangeMax = signalRangeMax
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeMin, "XSDataDouble")
		self.__signalRangeMin = signalRangeMin
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", spotTotal, "XSDataInteger")
		self.__spotTotal = spotTotal
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", totalIntegratedSignal, "XSDataDouble")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataInputRetrieveDataCollection(XSDataInput):
	def __init__(self, configuration=None, image=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputRetrieveDataCollection", "Constructor of XSDataInputRetrieveDataCollection", image, "XSDataImage")
		self.__image = image
	def getImage(self): return self.__image
	def setImage(self, image):
		checkType("XSDataInputRetrieveDataCollection", "setImage", image, "XSDataImage")
		self.__image = image
	def delImage(self): self.__image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def export(self, outfile, level, name_='XSDataInputRetrieveDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputRetrieveDataCollection'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__image is not None:
			self.image.export(outfile, level, name_='image')
		else:
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
			self.setImage(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputRetrieveDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputRetrieveDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputRetrieveDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputRetrieveDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputRetrieveDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputRetrieveDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputRetrieveDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputRetrieveDataCollection

class XSDataInputStoreAutoProc(XSDataInput):
	def __init__(self, configuration=None, AutoProcContainer=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputStoreAutoProc", "Constructor of XSDataInputStoreAutoProc", AutoProcContainer, "AutoProcContainer")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStoreAutoProc' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputStoreAutoProc is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataInputStoreDataCollection(XSDataInput):
	def __init__(self, configuration=None, dataCollection=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputStoreDataCollection", "Constructor of XSDataInputStoreDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self.__dataCollection = dataCollection
	def getDataCollection(self): return self.__dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataInputStoreDataCollection", "setDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self.__dataCollection = dataCollection
	def delDataCollection(self): self.__dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def export(self, outfile, level, name_='XSDataInputStoreDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputStoreDataCollection'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataISPyBDataCollection")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataISPyBDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputStoreDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStoreDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputStoreDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputStoreDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputStoreDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputStoreDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputStoreDataCollection

class XSDataInputStoreImageQualityIndicators(XSDataInput):
	def __init__(self, configuration=None, imageQualityIndicators=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputStoreImageQualityIndicators", "Constructor of XSDataInputStoreImageQualityIndicators", imageQualityIndicators, "XSDataISPyBImageQualityIndicators")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputStoreImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputStoreImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataResultRetrieveDataCollection(XSDataResult):
	def __init__(self, status=None, dataCollection=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultRetrieveDataCollection", "Constructor of XSDataResultRetrieveDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self.__dataCollection = dataCollection
	def getDataCollection(self): return self.__dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataResultRetrieveDataCollection", "setDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self.__dataCollection = dataCollection
	def delDataCollection(self): self.__dataCollection = None
	# Properties
	dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
	def export(self, outfile, level, name_='XSDataResultRetrieveDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultRetrieveDataCollection'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__dataCollection is not None:
			self.dataCollection.export(outfile, level, name_='dataCollection')
		else:
			warnEmptyAttribute("dataCollection", "XSDataISPyBDataCollection")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollection':
			obj_ = XSDataISPyBDataCollection()
			obj_.build(child_)
			self.setDataCollection(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultRetrieveDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultRetrieveDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultRetrieveDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultRetrieveDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultRetrieveDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultRetrieveDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultRetrieveDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultRetrieveDataCollection

class XSDataResultStoreAutoProc(XSDataResult):
	def __init__(self, status=None, autoProcId=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultStoreAutoProc", "Constructor of XSDataResultStoreAutoProc", autoProcId, "XSDataInteger")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStoreAutoProc' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultStoreAutoProc is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataResultStoreDataCollection(XSDataResult):
	def __init__(self, status=None, dataCollectionId=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultStoreDataCollection", "Constructor of XSDataResultStoreDataCollection", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataResultStoreDataCollection", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def export(self, outfile, level, name_='XSDataResultStoreDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultStoreDataCollection'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultStoreDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStoreDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultStoreDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultStoreDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultStoreDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultStoreDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultStoreDataCollection

class XSDataResultStoreImageQualityIndicators(XSDataResult):
	def __init__(self, status=None, imageQualityIndicatorsId=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultStoreImageQualityIndicators", "Constructor of XSDataResultStoreImageQualityIndicators", imageQualityIndicatorsId, "XSDataInteger")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStoreImageQualityIndicators' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultStoreImageQualityIndicators is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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



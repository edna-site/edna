#!/usr/bin/env python

#
# Generated Fri Mar 2 09:31::23 2012 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataAngle
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataImage
	from XSDataCommon import XSDataLength
	from XSDataCommon import XSDataTime
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
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
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

class XSDataISPyBDiffractionPlan(XSData):
	def __init__(self, numberOfPositions=None, kappaStrategyOption=None, strategyOption=None, requiredResolution=None, requiredMultiplicity=None, requiredCompleteness=None, forcedSpaceGroup=None, estimateRadiationDamage=None, complexity=None, anomalousData=None, aimedResolution=None, aimedMultiplicity=None, aimedIOverSigmaAtHighestResolution=None, aimedCompleteness=None, comments=None, preferredBeamSizeY=None, preferredBeamSizeX=None, anomalousScatterer=None, radiationSensitivity=None, screeningResolution=None, maximalResolution=None, oscillationRange=None, exposureTime=None, minimalResolution=None, observedResolution=None, experimentKind=None, xmlDocumentId=None, diffractionPlanId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", diffractionPlanId, "XSDataInteger")
		self.__diffractionPlanId = diffractionPlanId
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", xmlDocumentId, "XSDataInteger")
		self.__xmlDocumentId = xmlDocumentId
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", experimentKind, "XSDataString")
		self.__experimentKind = experimentKind
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", observedResolution, "XSDataDouble")
		self.__observedResolution = observedResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", minimalResolution, "XSDataDouble")
		self.__minimalResolution = minimalResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", exposureTime, "XSDataDouble")
		self.__exposureTime = exposureTime
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", oscillationRange, "XSDataDouble")
		self.__oscillationRange = oscillationRange
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", maximalResolution, "XSDataDouble")
		self.__maximalResolution = maximalResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", screeningResolution, "XSDataDouble")
		self.__screeningResolution = screeningResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", radiationSensitivity, "XSDataDouble")
		self.__radiationSensitivity = radiationSensitivity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", anomalousScatterer, "XSDataString")
		self.__anomalousScatterer = anomalousScatterer
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", preferredBeamSizeX, "XSDataDouble")
		self.__preferredBeamSizeX = preferredBeamSizeX
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", preferredBeamSizeY, "XSDataDouble")
		self.__preferredBeamSizeY = preferredBeamSizeY
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedCompleteness, "XSDataDouble")
		self.__aimedCompleteness = aimedCompleteness
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self.__aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedMultiplicity, "XSDataDouble")
		self.__aimedMultiplicity = aimedMultiplicity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedResolution, "XSDataDouble")
		self.__aimedResolution = aimedResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", anomalousData, "XSDataBoolean")
		self.__anomalousData = anomalousData
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", complexity, "XSDataString")
		self.__complexity = complexity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", estimateRadiationDamage, "XSDataBoolean")
		self.__estimateRadiationDamage = estimateRadiationDamage
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", forcedSpaceGroup, "XSDataString")
		self.__forcedSpaceGroup = forcedSpaceGroup
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredCompleteness, "XSDataDouble")
		self.__requiredCompleteness = requiredCompleteness
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredMultiplicity, "XSDataDouble")
		self.__requiredMultiplicity = requiredMultiplicity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredResolution, "XSDataDouble")
		self.__requiredResolution = requiredResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", strategyOption, "XSDataString")
		self.__strategyOption = strategyOption
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", kappaStrategyOption, "XSDataString")
		self.__kappaStrategyOption = kappaStrategyOption
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", numberOfPositions, "XSDataInteger")
		self.__numberOfPositions = numberOfPositions
	def getDiffractionPlanId(self): return self.__diffractionPlanId
	def setDiffractionPlanId(self, diffractionPlanId):
		checkType("XSDataISPyBDiffractionPlan", "setDiffractionPlanId", diffractionPlanId, "XSDataInteger")
		self.__diffractionPlanId = diffractionPlanId
	def delDiffractionPlanId(self): self.__diffractionPlanId = None
	# Properties
	diffractionPlanId = property(getDiffractionPlanId, setDiffractionPlanId, delDiffractionPlanId, "Property for diffractionPlanId")
	def getXmlDocumentId(self): return self.__xmlDocumentId
	def setXmlDocumentId(self, xmlDocumentId):
		checkType("XSDataISPyBDiffractionPlan", "setXmlDocumentId", xmlDocumentId, "XSDataInteger")
		self.__xmlDocumentId = xmlDocumentId
	def delXmlDocumentId(self): self.__xmlDocumentId = None
	# Properties
	xmlDocumentId = property(getXmlDocumentId, setXmlDocumentId, delXmlDocumentId, "Property for xmlDocumentId")
	def getExperimentKind(self): return self.__experimentKind
	def setExperimentKind(self, experimentKind):
		checkType("XSDataISPyBDiffractionPlan", "setExperimentKind", experimentKind, "XSDataString")
		self.__experimentKind = experimentKind
	def delExperimentKind(self): self.__experimentKind = None
	# Properties
	experimentKind = property(getExperimentKind, setExperimentKind, delExperimentKind, "Property for experimentKind")
	def getObservedResolution(self): return self.__observedResolution
	def setObservedResolution(self, observedResolution):
		checkType("XSDataISPyBDiffractionPlan", "setObservedResolution", observedResolution, "XSDataDouble")
		self.__observedResolution = observedResolution
	def delObservedResolution(self): self.__observedResolution = None
	# Properties
	observedResolution = property(getObservedResolution, setObservedResolution, delObservedResolution, "Property for observedResolution")
	def getMinimalResolution(self): return self.__minimalResolution
	def setMinimalResolution(self, minimalResolution):
		checkType("XSDataISPyBDiffractionPlan", "setMinimalResolution", minimalResolution, "XSDataDouble")
		self.__minimalResolution = minimalResolution
	def delMinimalResolution(self): self.__minimalResolution = None
	# Properties
	minimalResolution = property(getMinimalResolution, setMinimalResolution, delMinimalResolution, "Property for minimalResolution")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBDiffractionPlan", "setExposureTime", exposureTime, "XSDataDouble")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getOscillationRange(self): return self.__oscillationRange
	def setOscillationRange(self, oscillationRange):
		checkType("XSDataISPyBDiffractionPlan", "setOscillationRange", oscillationRange, "XSDataDouble")
		self.__oscillationRange = oscillationRange
	def delOscillationRange(self): self.__oscillationRange = None
	# Properties
	oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
	def getMaximalResolution(self): return self.__maximalResolution
	def setMaximalResolution(self, maximalResolution):
		checkType("XSDataISPyBDiffractionPlan", "setMaximalResolution", maximalResolution, "XSDataDouble")
		self.__maximalResolution = maximalResolution
	def delMaximalResolution(self): self.__maximalResolution = None
	# Properties
	maximalResolution = property(getMaximalResolution, setMaximalResolution, delMaximalResolution, "Property for maximalResolution")
	def getScreeningResolution(self): return self.__screeningResolution
	def setScreeningResolution(self, screeningResolution):
		checkType("XSDataISPyBDiffractionPlan", "setScreeningResolution", screeningResolution, "XSDataDouble")
		self.__screeningResolution = screeningResolution
	def delScreeningResolution(self): self.__screeningResolution = None
	# Properties
	screeningResolution = property(getScreeningResolution, setScreeningResolution, delScreeningResolution, "Property for screeningResolution")
	def getRadiationSensitivity(self): return self.__radiationSensitivity
	def setRadiationSensitivity(self, radiationSensitivity):
		checkType("XSDataISPyBDiffractionPlan", "setRadiationSensitivity", radiationSensitivity, "XSDataDouble")
		self.__radiationSensitivity = radiationSensitivity
	def delRadiationSensitivity(self): self.__radiationSensitivity = None
	# Properties
	radiationSensitivity = property(getRadiationSensitivity, setRadiationSensitivity, delRadiationSensitivity, "Property for radiationSensitivity")
	def getAnomalousScatterer(self): return self.__anomalousScatterer
	def setAnomalousScatterer(self, anomalousScatterer):
		checkType("XSDataISPyBDiffractionPlan", "setAnomalousScatterer", anomalousScatterer, "XSDataString")
		self.__anomalousScatterer = anomalousScatterer
	def delAnomalousScatterer(self): self.__anomalousScatterer = None
	# Properties
	anomalousScatterer = property(getAnomalousScatterer, setAnomalousScatterer, delAnomalousScatterer, "Property for anomalousScatterer")
	def getPreferredBeamSizeX(self): return self.__preferredBeamSizeX
	def setPreferredBeamSizeX(self, preferredBeamSizeX):
		checkType("XSDataISPyBDiffractionPlan", "setPreferredBeamSizeX", preferredBeamSizeX, "XSDataDouble")
		self.__preferredBeamSizeX = preferredBeamSizeX
	def delPreferredBeamSizeX(self): self.__preferredBeamSizeX = None
	# Properties
	preferredBeamSizeX = property(getPreferredBeamSizeX, setPreferredBeamSizeX, delPreferredBeamSizeX, "Property for preferredBeamSizeX")
	def getPreferredBeamSizeY(self): return self.__preferredBeamSizeY
	def setPreferredBeamSizeY(self, preferredBeamSizeY):
		checkType("XSDataISPyBDiffractionPlan", "setPreferredBeamSizeY", preferredBeamSizeY, "XSDataDouble")
		self.__preferredBeamSizeY = preferredBeamSizeY
	def delPreferredBeamSizeY(self): self.__preferredBeamSizeY = None
	# Properties
	preferredBeamSizeY = property(getPreferredBeamSizeY, setPreferredBeamSizeY, delPreferredBeamSizeY, "Property for preferredBeamSizeY")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataISPyBDiffractionPlan", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getAimedCompleteness(self): return self.__aimedCompleteness
	def setAimedCompleteness(self, aimedCompleteness):
		checkType("XSDataISPyBDiffractionPlan", "setAimedCompleteness", aimedCompleteness, "XSDataDouble")
		self.__aimedCompleteness = aimedCompleteness
	def delAimedCompleteness(self): self.__aimedCompleteness = None
	# Properties
	aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
	def getAimedIOverSigmaAtHighestResolution(self): return self.__aimedIOverSigmaAtHighestResolution
	def setAimedIOverSigmaAtHighestResolution(self, aimedIOverSigmaAtHighestResolution):
		checkType("XSDataISPyBDiffractionPlan", "setAimedIOverSigmaAtHighestResolution", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self.__aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
	def delAimedIOverSigmaAtHighestResolution(self): self.__aimedIOverSigmaAtHighestResolution = None
	# Properties
	aimedIOverSigmaAtHighestResolution = property(getAimedIOverSigmaAtHighestResolution, setAimedIOverSigmaAtHighestResolution, delAimedIOverSigmaAtHighestResolution, "Property for aimedIOverSigmaAtHighestResolution")
	def getAimedMultiplicity(self): return self.__aimedMultiplicity
	def setAimedMultiplicity(self, aimedMultiplicity):
		checkType("XSDataISPyBDiffractionPlan", "setAimedMultiplicity", aimedMultiplicity, "XSDataDouble")
		self.__aimedMultiplicity = aimedMultiplicity
	def delAimedMultiplicity(self): self.__aimedMultiplicity = None
	# Properties
	aimedMultiplicity = property(getAimedMultiplicity, setAimedMultiplicity, delAimedMultiplicity, "Property for aimedMultiplicity")
	def getAimedResolution(self): return self.__aimedResolution
	def setAimedResolution(self, aimedResolution):
		checkType("XSDataISPyBDiffractionPlan", "setAimedResolution", aimedResolution, "XSDataDouble")
		self.__aimedResolution = aimedResolution
	def delAimedResolution(self): self.__aimedResolution = None
	# Properties
	aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
	def getAnomalousData(self): return self.__anomalousData
	def setAnomalousData(self, anomalousData):
		checkType("XSDataISPyBDiffractionPlan", "setAnomalousData", anomalousData, "XSDataBoolean")
		self.__anomalousData = anomalousData
	def delAnomalousData(self): self.__anomalousData = None
	# Properties
	anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
	def getComplexity(self): return self.__complexity
	def setComplexity(self, complexity):
		checkType("XSDataISPyBDiffractionPlan", "setComplexity", complexity, "XSDataString")
		self.__complexity = complexity
	def delComplexity(self): self.__complexity = None
	# Properties
	complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
	def getEstimateRadiationDamage(self): return self.__estimateRadiationDamage
	def setEstimateRadiationDamage(self, estimateRadiationDamage):
		checkType("XSDataISPyBDiffractionPlan", "setEstimateRadiationDamage", estimateRadiationDamage, "XSDataBoolean")
		self.__estimateRadiationDamage = estimateRadiationDamage
	def delEstimateRadiationDamage(self): self.__estimateRadiationDamage = None
	# Properties
	estimateRadiationDamage = property(getEstimateRadiationDamage, setEstimateRadiationDamage, delEstimateRadiationDamage, "Property for estimateRadiationDamage")
	def getForcedSpaceGroup(self): return self.__forcedSpaceGroup
	def setForcedSpaceGroup(self, forcedSpaceGroup):
		checkType("XSDataISPyBDiffractionPlan", "setForcedSpaceGroup", forcedSpaceGroup, "XSDataString")
		self.__forcedSpaceGroup = forcedSpaceGroup
	def delForcedSpaceGroup(self): self.__forcedSpaceGroup = None
	# Properties
	forcedSpaceGroup = property(getForcedSpaceGroup, setForcedSpaceGroup, delForcedSpaceGroup, "Property for forcedSpaceGroup")
	def getRequiredCompleteness(self): return self.__requiredCompleteness
	def setRequiredCompleteness(self, requiredCompleteness):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredCompleteness", requiredCompleteness, "XSDataDouble")
		self.__requiredCompleteness = requiredCompleteness
	def delRequiredCompleteness(self): self.__requiredCompleteness = None
	# Properties
	requiredCompleteness = property(getRequiredCompleteness, setRequiredCompleteness, delRequiredCompleteness, "Property for requiredCompleteness")
	def getRequiredMultiplicity(self): return self.__requiredMultiplicity
	def setRequiredMultiplicity(self, requiredMultiplicity):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredMultiplicity", requiredMultiplicity, "XSDataDouble")
		self.__requiredMultiplicity = requiredMultiplicity
	def delRequiredMultiplicity(self): self.__requiredMultiplicity = None
	# Properties
	requiredMultiplicity = property(getRequiredMultiplicity, setRequiredMultiplicity, delRequiredMultiplicity, "Property for requiredMultiplicity")
	def getRequiredResolution(self): return self.__requiredResolution
	def setRequiredResolution(self, requiredResolution):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredResolution", requiredResolution, "XSDataDouble")
		self.__requiredResolution = requiredResolution
	def delRequiredResolution(self): self.__requiredResolution = None
	# Properties
	requiredResolution = property(getRequiredResolution, setRequiredResolution, delRequiredResolution, "Property for requiredResolution")
	def getStrategyOption(self): return self.__strategyOption
	def setStrategyOption(self, strategyOption):
		checkType("XSDataISPyBDiffractionPlan", "setStrategyOption", strategyOption, "XSDataString")
		self.__strategyOption = strategyOption
	def delStrategyOption(self): self.__strategyOption = None
	# Properties
	strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
	def getKappaStrategyOption(self): return self.__kappaStrategyOption
	def setKappaStrategyOption(self, kappaStrategyOption):
		checkType("XSDataISPyBDiffractionPlan", "setKappaStrategyOption", kappaStrategyOption, "XSDataString")
		self.__kappaStrategyOption = kappaStrategyOption
	def delKappaStrategyOption(self): self.__kappaStrategyOption = None
	# Properties
	kappaStrategyOption = property(getKappaStrategyOption, setKappaStrategyOption, delKappaStrategyOption, "Property for kappaStrategyOption")
	def getNumberOfPositions(self): return self.__numberOfPositions
	def setNumberOfPositions(self, numberOfPositions):
		checkType("XSDataISPyBDiffractionPlan", "setNumberOfPositions", numberOfPositions, "XSDataInteger")
		self.__numberOfPositions = numberOfPositions
	def delNumberOfPositions(self): self.__numberOfPositions = None
	# Properties
	numberOfPositions = property(getNumberOfPositions, setNumberOfPositions, delNumberOfPositions, "Property for numberOfPositions")
	def export(self, outfile, level, name_='XSDataISPyBDiffractionPlan'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBDiffractionPlan'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__diffractionPlanId is not None:
			self.diffractionPlanId.export(outfile, level, name_='diffractionPlanId')
		if self.__xmlDocumentId is not None:
			self.xmlDocumentId.export(outfile, level, name_='xmlDocumentId')
		if self.__experimentKind is not None:
			self.experimentKind.export(outfile, level, name_='experimentKind')
		if self.__observedResolution is not None:
			self.observedResolution.export(outfile, level, name_='observedResolution')
		if self.__minimalResolution is not None:
			self.minimalResolution.export(outfile, level, name_='minimalResolution')
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self.__oscillationRange is not None:
			self.oscillationRange.export(outfile, level, name_='oscillationRange')
		if self.__maximalResolution is not None:
			self.maximalResolution.export(outfile, level, name_='maximalResolution')
		if self.__screeningResolution is not None:
			self.screeningResolution.export(outfile, level, name_='screeningResolution')
		if self.__radiationSensitivity is not None:
			self.radiationSensitivity.export(outfile, level, name_='radiationSensitivity')
		if self.__anomalousScatterer is not None:
			self.anomalousScatterer.export(outfile, level, name_='anomalousScatterer')
		if self.__preferredBeamSizeX is not None:
			self.preferredBeamSizeX.export(outfile, level, name_='preferredBeamSizeX')
		if self.__preferredBeamSizeY is not None:
			self.preferredBeamSizeY.export(outfile, level, name_='preferredBeamSizeY')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__aimedCompleteness is not None:
			self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
		if self.__aimedIOverSigmaAtHighestResolution is not None:
			self.aimedIOverSigmaAtHighestResolution.export(outfile, level, name_='aimedIOverSigmaAtHighestResolution')
		if self.__aimedMultiplicity is not None:
			self.aimedMultiplicity.export(outfile, level, name_='aimedMultiplicity')
		if self.__aimedResolution is not None:
			self.aimedResolution.export(outfile, level, name_='aimedResolution')
		if self.__anomalousData is not None:
			self.anomalousData.export(outfile, level, name_='anomalousData')
		if self.__complexity is not None:
			self.complexity.export(outfile, level, name_='complexity')
		if self.__estimateRadiationDamage is not None:
			self.estimateRadiationDamage.export(outfile, level, name_='estimateRadiationDamage')
		if self.__forcedSpaceGroup is not None:
			self.forcedSpaceGroup.export(outfile, level, name_='forcedSpaceGroup')
		if self.__requiredCompleteness is not None:
			self.requiredCompleteness.export(outfile, level, name_='requiredCompleteness')
		if self.__requiredMultiplicity is not None:
			self.requiredMultiplicity.export(outfile, level, name_='requiredMultiplicity')
		if self.__requiredResolution is not None:
			self.requiredResolution.export(outfile, level, name_='requiredResolution')
		if self.__strategyOption is not None:
			self.strategyOption.export(outfile, level, name_='strategyOption')
		if self.__kappaStrategyOption is not None:
			self.kappaStrategyOption.export(outfile, level, name_='kappaStrategyOption')
		if self.__numberOfPositions is not None:
			self.numberOfPositions.export(outfile, level, name_='numberOfPositions')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlanId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDiffractionPlanId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xmlDocumentId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setXmlDocumentId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentKind':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setExperimentKind(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'observedResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setObservedResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimalResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinimalResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'oscillationRange':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setOscillationRange(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maximalResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaximalResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setScreeningResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'radiationSensitivity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRadiationSensitivity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousScatterer':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setAnomalousScatterer(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'preferredBeamSizeX':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPreferredBeamSizeX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'preferredBeamSizeY':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPreferredBeamSizeY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappaStrategyOption':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setKappaStrategyOption(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfPositions':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfPositions(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBDiffractionPlan" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBDiffractionPlan' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBDiffractionPlan is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBDiffractionPlan.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDiffractionPlan()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBDiffractionPlan" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDiffractionPlan()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBDiffractionPlan

class XSDataISPyBImage(XSData):
	def __init__(self, temperature=None, synchrotronCurrent=None, measuredIntensity=None, machineMessage=None, jpegThumbnailFileFullPath=None, jpegFileFullPath=None, imageNumber=None, imageId=None, fileName=None, fileLocation=None, cumulativeIntensity=None, comments=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", cumulativeIntensity, "XSDataDouble")
		self.__cumulativeIntensity = cumulativeIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileLocation, "XSDataString")
		self.__fileLocation = fileLocation
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileName, "XSDataString")
		self.__fileName = fileName
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageId, "XSDataInteger")
		self.__imageId = imageId
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageNumber, "XSDataInteger")
		self.__imageNumber = imageNumber
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegFileFullPath, "XSDataString")
		self.__jpegFileFullPath = jpegFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegThumbnailFileFullPath, "XSDataString")
		self.__jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", machineMessage, "XSDataString")
		self.__machineMessage = machineMessage
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", measuredIntensity, "XSDataDouble")
		self.__measuredIntensity = measuredIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", synchrotronCurrent, "XSDataDouble")
		self.__synchrotronCurrent = synchrotronCurrent
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", temperature, "XSDataDouble")
		self.__temperature = temperature
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataISPyBImage", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getCumulativeIntensity(self): return self.__cumulativeIntensity
	def setCumulativeIntensity(self, cumulativeIntensity):
		checkType("XSDataISPyBImage", "setCumulativeIntensity", cumulativeIntensity, "XSDataDouble")
		self.__cumulativeIntensity = cumulativeIntensity
	def delCumulativeIntensity(self): self.__cumulativeIntensity = None
	# Properties
	cumulativeIntensity = property(getCumulativeIntensity, setCumulativeIntensity, delCumulativeIntensity, "Property for cumulativeIntensity")
	def getFileLocation(self): return self.__fileLocation
	def setFileLocation(self, fileLocation):
		checkType("XSDataISPyBImage", "setFileLocation", fileLocation, "XSDataString")
		self.__fileLocation = fileLocation
	def delFileLocation(self): self.__fileLocation = None
	# Properties
	fileLocation = property(getFileLocation, setFileLocation, delFileLocation, "Property for fileLocation")
	def getFileName(self): return self.__fileName
	def setFileName(self, fileName):
		checkType("XSDataISPyBImage", "setFileName", fileName, "XSDataString")
		self.__fileName = fileName
	def delFileName(self): self.__fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getImageId(self): return self.__imageId
	def setImageId(self, imageId):
		checkType("XSDataISPyBImage", "setImageId", imageId, "XSDataInteger")
		self.__imageId = imageId
	def delImageId(self): self.__imageId = None
	# Properties
	imageId = property(getImageId, setImageId, delImageId, "Property for imageId")
	def getImageNumber(self): return self.__imageNumber
	def setImageNumber(self, imageNumber):
		checkType("XSDataISPyBImage", "setImageNumber", imageNumber, "XSDataInteger")
		self.__imageNumber = imageNumber
	def delImageNumber(self): self.__imageNumber = None
	# Properties
	imageNumber = property(getImageNumber, setImageNumber, delImageNumber, "Property for imageNumber")
	def getJpegFileFullPath(self): return self.__jpegFileFullPath
	def setJpegFileFullPath(self, jpegFileFullPath):
		checkType("XSDataISPyBImage", "setJpegFileFullPath", jpegFileFullPath, "XSDataString")
		self.__jpegFileFullPath = jpegFileFullPath
	def delJpegFileFullPath(self): self.__jpegFileFullPath = None
	# Properties
	jpegFileFullPath = property(getJpegFileFullPath, setJpegFileFullPath, delJpegFileFullPath, "Property for jpegFileFullPath")
	def getJpegThumbnailFileFullPath(self): return self.__jpegThumbnailFileFullPath
	def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath):
		checkType("XSDataISPyBImage", "setJpegThumbnailFileFullPath", jpegThumbnailFileFullPath, "XSDataString")
		self.__jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
	def delJpegThumbnailFileFullPath(self): self.__jpegThumbnailFileFullPath = None
	# Properties
	jpegThumbnailFileFullPath = property(getJpegThumbnailFileFullPath, setJpegThumbnailFileFullPath, delJpegThumbnailFileFullPath, "Property for jpegThumbnailFileFullPath")
	def getMachineMessage(self): return self.__machineMessage
	def setMachineMessage(self, machineMessage):
		checkType("XSDataISPyBImage", "setMachineMessage", machineMessage, "XSDataString")
		self.__machineMessage = machineMessage
	def delMachineMessage(self): self.__machineMessage = None
	# Properties
	machineMessage = property(getMachineMessage, setMachineMessage, delMachineMessage, "Property for machineMessage")
	def getMeasuredIntensity(self): return self.__measuredIntensity
	def setMeasuredIntensity(self, measuredIntensity):
		checkType("XSDataISPyBImage", "setMeasuredIntensity", measuredIntensity, "XSDataDouble")
		self.__measuredIntensity = measuredIntensity
	def delMeasuredIntensity(self): self.__measuredIntensity = None
	# Properties
	measuredIntensity = property(getMeasuredIntensity, setMeasuredIntensity, delMeasuredIntensity, "Property for measuredIntensity")
	def getSynchrotronCurrent(self): return self.__synchrotronCurrent
	def setSynchrotronCurrent(self, synchrotronCurrent):
		checkType("XSDataISPyBImage", "setSynchrotronCurrent", synchrotronCurrent, "XSDataDouble")
		self.__synchrotronCurrent = synchrotronCurrent
	def delSynchrotronCurrent(self): self.__synchrotronCurrent = None
	# Properties
	synchrotronCurrent = property(getSynchrotronCurrent, setSynchrotronCurrent, delSynchrotronCurrent, "Property for synchrotronCurrent")
	def getTemperature(self): return self.__temperature
	def setTemperature(self, temperature):
		checkType("XSDataISPyBImage", "setTemperature", temperature, "XSDataDouble")
		self.__temperature = temperature
	def delTemperature(self): self.__temperature = None
	# Properties
	temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
	def export(self, outfile, level, name_='XSDataISPyBImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBImage'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		else:
			warnEmptyAttribute("comments", "XSDataString")
		if self.__cumulativeIntensity is not None:
			self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
		else:
			warnEmptyAttribute("cumulativeIntensity", "XSDataDouble")
		if self.__fileLocation is not None:
			self.fileLocation.export(outfile, level, name_='fileLocation')
		else:
			warnEmptyAttribute("fileLocation", "XSDataString")
		if self.__fileName is not None:
			self.fileName.export(outfile, level, name_='fileName')
		else:
			warnEmptyAttribute("fileName", "XSDataString")
		if self.__imageId is not None:
			self.imageId.export(outfile, level, name_='imageId')
		else:
			warnEmptyAttribute("imageId", "XSDataInteger")
		if self.__imageNumber is not None:
			self.imageNumber.export(outfile, level, name_='imageNumber')
		else:
			warnEmptyAttribute("imageNumber", "XSDataInteger")
		if self.__jpegFileFullPath is not None:
			self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
		else:
			warnEmptyAttribute("jpegFileFullPath", "XSDataString")
		if self.__jpegThumbnailFileFullPath is not None:
			self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
		else:
			warnEmptyAttribute("jpegThumbnailFileFullPath", "XSDataString")
		if self.__machineMessage is not None:
			self.machineMessage.export(outfile, level, name_='machineMessage')
		else:
			warnEmptyAttribute("machineMessage", "XSDataString")
		if self.__measuredIntensity is not None:
			self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
		else:
			warnEmptyAttribute("measuredIntensity", "XSDataDouble")
		if self.__synchrotronCurrent is not None:
			self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
		else:
			warnEmptyAttribute("synchrotronCurrent", "XSDataDouble")
		if self.__temperature is not None:
			self.temperature.export(outfile, level, name_='temperature')
		else:
			warnEmptyAttribute("temperature", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cumulativeIntensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCumulativeIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileLocation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileLocation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'jpegFileFullPath':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setJpegFileFullPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'jpegThumbnailFileFullPath':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setJpegThumbnailFileFullPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineMessage':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMachineMessage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'measuredIntensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMeasuredIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'synchrotronCurrent':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSynchrotronCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'temperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTemperature(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBImage

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

class XSDataISPyBScreening(XSData):
	def __init__(self, shortComments=None, comments=None, programVersion=None, timeStamp=None, dataCollectionId=None, screeningId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", programVersion, "XSDataString")
		self.__programVersion = programVersion
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", shortComments, "XSDataString")
		self.__shortComments = shortComments
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreening", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBScreening", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getTimeStamp(self): return self.__timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreening", "setTimeStamp", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
	def delTimeStamp(self): self.__timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def getProgramVersion(self): return self.__programVersion
	def setProgramVersion(self, programVersion):
		checkType("XSDataISPyBScreening", "setProgramVersion", programVersion, "XSDataString")
		self.__programVersion = programVersion
	def delProgramVersion(self): self.__programVersion = None
	# Properties
	programVersion = property(getProgramVersion, setProgramVersion, delProgramVersion, "Property for programVersion")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataISPyBScreening", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getShortComments(self): return self.__shortComments
	def setShortComments(self, shortComments):
		checkType("XSDataISPyBScreening", "setShortComments", shortComments, "XSDataString")
		self.__shortComments = shortComments
	def delShortComments(self): self.__shortComments = None
	# Properties
	shortComments = property(getShortComments, setShortComments, delShortComments, "Property for shortComments")
	def export(self, outfile, level, name_='XSDataISPyBScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreening'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		else:
			warnEmptyAttribute("dataCollectionId", "XSDataInteger")
		if self.__timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataString")
		if self.__programVersion is not None:
			self.programVersion.export(outfile, level, name_='programVersion')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__shortComments is not None:
			self.shortComments.export(outfile, level, name_='shortComments')
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeStamp':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTimeStamp(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'programVersion':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProgramVersion(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'shortComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setShortComments(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreening

class XSDataISPyBScreeningFile(XSData):
	def __init__(self, timeStamp=None, description=None, filePath=None, fileName=None, fileType=None, screeningId=None, screeningFileId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", screeningFileId, "XSDataInteger")
		self.__screeningFileId = screeningFileId
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", fileType, "XSDataString")
		self.__fileType = fileType
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", fileName, "XSDataString")
		self.__fileName = fileName
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", filePath, "XSDataString")
		self.__filePath = filePath
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", description, "XSDataString")
		self.__description = description
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
	def getScreeningFileId(self): return self.__screeningFileId
	def setScreeningFileId(self, screeningFileId):
		checkType("XSDataISPyBScreeningFile", "setScreeningFileId", screeningFileId, "XSDataInteger")
		self.__screeningFileId = screeningFileId
	def delScreeningFileId(self): self.__screeningFileId = None
	# Properties
	screeningFileId = property(getScreeningFileId, setScreeningFileId, delScreeningFileId, "Property for screeningFileId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningFile", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getFileType(self): return self.__fileType
	def setFileType(self, fileType):
		checkType("XSDataISPyBScreeningFile", "setFileType", fileType, "XSDataString")
		self.__fileType = fileType
	def delFileType(self): self.__fileType = None
	# Properties
	fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
	def getFileName(self): return self.__fileName
	def setFileName(self, fileName):
		checkType("XSDataISPyBScreeningFile", "setFileName", fileName, "XSDataString")
		self.__fileName = fileName
	def delFileName(self): self.__fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFilePath(self): return self.__filePath
	def setFilePath(self, filePath):
		checkType("XSDataISPyBScreeningFile", "setFilePath", filePath, "XSDataString")
		self.__filePath = filePath
	def delFilePath(self): self.__filePath = None
	# Properties
	filePath = property(getFilePath, setFilePath, delFilePath, "Property for filePath")
	def getDescription(self): return self.__description
	def setDescription(self, description):
		checkType("XSDataISPyBScreeningFile", "setDescription", description, "XSDataString")
		self.__description = description
	def delDescription(self): self.__description = None
	# Properties
	description = property(getDescription, setDescription, delDescription, "Property for description")
	def getTimeStamp(self): return self.__timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreeningFile", "setTimeStamp", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
	def delTimeStamp(self): self.__timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def export(self, outfile, level, name_='XSDataISPyBScreeningFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningFile'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningFileId is not None:
			self.screeningFileId.export(outfile, level, name_='screeningFileId')
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__fileType is not None:
			self.fileType.export(outfile, level, name_='fileType')
		if self.__fileName is not None:
			self.fileName.export(outfile, level, name_='fileName')
		else:
			warnEmptyAttribute("fileName", "XSDataString")
		if self.__filePath is not None:
			self.filePath.export(outfile, level, name_='filePath')
		else:
			warnEmptyAttribute("filePath", "XSDataString")
		if self.__description is not None:
			self.description.export(outfile, level, name_='description')
		if self.__timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningFileId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningFileId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'filePath':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFilePath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'description':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDescription(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeStamp':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTimeStamp(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningFile

class XSDataISPyBScreeningInput(XSData):
	def __init__(self, xmlSampleInformation=None, minimumSignalToNoise=None, maximumFractionRejected=None, minimumFractionIndexed=None, rmsErrorLimits=None, beamY=None, beamX=None, diffractionPlanId=None, screeningId=None, screeningInputId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", diffractionPlanId, "XSDataInteger")
		self.__diffractionPlanId = diffractionPlanId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamX, "XSDataLength")
		self.__beamX = beamX
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamY, "XSDataLength")
		self.__beamY = beamY
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", rmsErrorLimits, "XSDataDouble")
		self.__rmsErrorLimits = rmsErrorLimits
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumFractionIndexed, "XSDataDouble")
		self.__minimumFractionIndexed = minimumFractionIndexed
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", maximumFractionRejected, "XSDataDouble")
		self.__maximumFractionRejected = maximumFractionRejected
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumSignalToNoise, "XSDataDouble")
		self.__minimumSignalToNoise = minimumSignalToNoise
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", xmlSampleInformation, "XSDataString")
		self.__xmlSampleInformation = xmlSampleInformation
	def getScreeningInputId(self): return self.__screeningInputId
	def setScreeningInputId(self, screeningInputId):
		checkType("XSDataISPyBScreeningInput", "setScreeningInputId", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
	def delScreeningInputId(self): self.__screeningInputId = None
	# Properties
	screeningInputId = property(getScreeningInputId, setScreeningInputId, delScreeningInputId, "Property for screeningInputId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningInput", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getDiffractionPlanId(self): return self.__diffractionPlanId
	def setDiffractionPlanId(self, diffractionPlanId):
		checkType("XSDataISPyBScreeningInput", "setDiffractionPlanId", diffractionPlanId, "XSDataInteger")
		self.__diffractionPlanId = diffractionPlanId
	def delDiffractionPlanId(self): self.__diffractionPlanId = None
	# Properties
	diffractionPlanId = property(getDiffractionPlanId, setDiffractionPlanId, delDiffractionPlanId, "Property for diffractionPlanId")
	def getBeamX(self): return self.__beamX
	def setBeamX(self, beamX):
		checkType("XSDataISPyBScreeningInput", "setBeamX", beamX, "XSDataLength")
		self.__beamX = beamX
	def delBeamX(self): self.__beamX = None
	# Properties
	beamX = property(getBeamX, setBeamX, delBeamX, "Property for beamX")
	def getBeamY(self): return self.__beamY
	def setBeamY(self, beamY):
		checkType("XSDataISPyBScreeningInput", "setBeamY", beamY, "XSDataLength")
		self.__beamY = beamY
	def delBeamY(self): self.__beamY = None
	# Properties
	beamY = property(getBeamY, setBeamY, delBeamY, "Property for beamY")
	def getRmsErrorLimits(self): return self.__rmsErrorLimits
	def setRmsErrorLimits(self, rmsErrorLimits):
		checkType("XSDataISPyBScreeningInput", "setRmsErrorLimits", rmsErrorLimits, "XSDataDouble")
		self.__rmsErrorLimits = rmsErrorLimits
	def delRmsErrorLimits(self): self.__rmsErrorLimits = None
	# Properties
	rmsErrorLimits = property(getRmsErrorLimits, setRmsErrorLimits, delRmsErrorLimits, "Property for rmsErrorLimits")
	def getMinimumFractionIndexed(self): return self.__minimumFractionIndexed
	def setMinimumFractionIndexed(self, minimumFractionIndexed):
		checkType("XSDataISPyBScreeningInput", "setMinimumFractionIndexed", minimumFractionIndexed, "XSDataDouble")
		self.__minimumFractionIndexed = minimumFractionIndexed
	def delMinimumFractionIndexed(self): self.__minimumFractionIndexed = None
	# Properties
	minimumFractionIndexed = property(getMinimumFractionIndexed, setMinimumFractionIndexed, delMinimumFractionIndexed, "Property for minimumFractionIndexed")
	def getMaximumFractionRejected(self): return self.__maximumFractionRejected
	def setMaximumFractionRejected(self, maximumFractionRejected):
		checkType("XSDataISPyBScreeningInput", "setMaximumFractionRejected", maximumFractionRejected, "XSDataDouble")
		self.__maximumFractionRejected = maximumFractionRejected
	def delMaximumFractionRejected(self): self.__maximumFractionRejected = None
	# Properties
	maximumFractionRejected = property(getMaximumFractionRejected, setMaximumFractionRejected, delMaximumFractionRejected, "Property for maximumFractionRejected")
	def getMinimumSignalToNoise(self): return self.__minimumSignalToNoise
	def setMinimumSignalToNoise(self, minimumSignalToNoise):
		checkType("XSDataISPyBScreeningInput", "setMinimumSignalToNoise", minimumSignalToNoise, "XSDataDouble")
		self.__minimumSignalToNoise = minimumSignalToNoise
	def delMinimumSignalToNoise(self): self.__minimumSignalToNoise = None
	# Properties
	minimumSignalToNoise = property(getMinimumSignalToNoise, setMinimumSignalToNoise, delMinimumSignalToNoise, "Property for minimumSignalToNoise")
	def getXmlSampleInformation(self): return self.__xmlSampleInformation
	def setXmlSampleInformation(self, xmlSampleInformation):
		checkType("XSDataISPyBScreeningInput", "setXmlSampleInformation", xmlSampleInformation, "XSDataString")
		self.__xmlSampleInformation = xmlSampleInformation
	def delXmlSampleInformation(self): self.__xmlSampleInformation = None
	# Properties
	xmlSampleInformation = property(getXmlSampleInformation, setXmlSampleInformation, delXmlSampleInformation, "Property for xmlSampleInformation")
	def export(self, outfile, level, name_='XSDataISPyBScreeningInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningInputId is not None:
			self.screeningInputId.export(outfile, level, name_='screeningInputId')
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__diffractionPlanId is not None:
			self.diffractionPlanId.export(outfile, level, name_='diffractionPlanId')
		else:
			warnEmptyAttribute("diffractionPlanId", "XSDataInteger")
		if self.__beamX is not None:
			self.beamX.export(outfile, level, name_='beamX')
		else:
			warnEmptyAttribute("beamX", "XSDataLength")
		if self.__beamY is not None:
			self.beamY.export(outfile, level, name_='beamY')
		else:
			warnEmptyAttribute("beamY", "XSDataLength")
		if self.__rmsErrorLimits is not None:
			self.rmsErrorLimits.export(outfile, level, name_='rmsErrorLimits')
		else:
			warnEmptyAttribute("rmsErrorLimits", "XSDataDouble")
		if self.__minimumFractionIndexed is not None:
			self.minimumFractionIndexed.export(outfile, level, name_='minimumFractionIndexed')
		else:
			warnEmptyAttribute("minimumFractionIndexed", "XSDataDouble")
		if self.__maximumFractionRejected is not None:
			self.maximumFractionRejected.export(outfile, level, name_='maximumFractionRejected')
		else:
			warnEmptyAttribute("maximumFractionRejected", "XSDataDouble")
		if self.__minimumSignalToNoise is not None:
			self.minimumSignalToNoise.export(outfile, level, name_='minimumSignalToNoise')
		else:
			warnEmptyAttribute("minimumSignalToNoise", "XSDataDouble")
		if self.__xmlSampleInformation is not None:
			self.xmlSampleInformation.export(outfile, level, name_='xmlSampleInformation')
		else:
			warnEmptyAttribute("xmlSampleInformation", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningInputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlanId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDiffractionPlanId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmsErrorLimits':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRmsErrorLimits(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimumFractionIndexed':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinimumFractionIndexed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maximumFractionRejected':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaximumFractionRejected(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimumSignalToNoise':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinimumSignalToNoise(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xmlSampleInformation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setXmlSampleInformation(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningInput

class XSDataISPyBScreeningInputContainer(XSData):
	def __init__(self, screeningInput=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningInputContainer", "Constructor of XSDataISPyBScreeningInputContainer", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
	def getScreeningInput(self): return self.__screeningInput
	def setScreeningInput(self, screeningInput):
		checkType("XSDataISPyBScreeningInputContainer", "setScreeningInput", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
	def delScreeningInput(self): self.__screeningInput = None
	# Properties
	screeningInput = property(getScreeningInput, setScreeningInput, delScreeningInput, "Property for screeningInput")
	def export(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningInput is not None:
			self.screeningInput.export(outfile, level, name_='screeningInput')
		else:
			warnEmptyAttribute("screeningInput", "XSDataISPyBScreeningInput")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInput':
			obj_ = XSDataISPyBScreeningInput()
			obj_.build(child_)
			self.setScreeningInput(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningInputContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningInputContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningInputContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningInputContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInputContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningInputContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInputContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningInputContainer

class XSDataISPyBScreeningOutput(XSData):
	def __init__(self, mosaicityEstimated=None, screeningSuccess=None, diffractionRings=None, iOverSigma=None, mosaicity=None, numSpotsRejected=None, numSpotsUsed=None, numSpotsFound=None, beamShiftY=None, beamShiftX=None, spotDeviationTheta=None, spotDeviationR=None, resolutionObtained=None, rejectedReflections=None, statusDescription=None, screeningId=None, screeningOutputId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", statusDescription, "XSDataString")
		self.__statusDescription = statusDescription
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", rejectedReflections, "XSDataInteger")
		self.__rejectedReflections = rejectedReflections
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", resolutionObtained, "XSDataDouble")
		self.__resolutionObtained = resolutionObtained
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationR, "XSDataLength")
		self.__spotDeviationR = spotDeviationR
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationTheta, "XSDataAngle")
		self.__spotDeviationTheta = spotDeviationTheta
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftX, "XSDataLength")
		self.__beamShiftX = beamShiftX
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftY, "XSDataLength")
		self.__beamShiftY = beamShiftY
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsFound, "XSDataInteger")
		self.__numSpotsFound = numSpotsFound
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsUsed, "XSDataInteger")
		self.__numSpotsUsed = numSpotsUsed
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsRejected, "XSDataInteger")
		self.__numSpotsRejected = numSpotsRejected
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicity, "XSDataDouble")
		self.__mosaicity = mosaicity
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", iOverSigma, "XSDataDouble")
		self.__iOverSigma = iOverSigma
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", diffractionRings, "XSDataBoolean")
		self.__diffractionRings = diffractionRings
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningSuccess, "XSDataBoolean")
		self.__screeningSuccess = screeningSuccess
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicityEstimated, "XSDataBoolean")
		self.__mosaicityEstimated = mosaicityEstimated
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getStatusDescription(self): return self.__statusDescription
	def setStatusDescription(self, statusDescription):
		checkType("XSDataISPyBScreeningOutput", "setStatusDescription", statusDescription, "XSDataString")
		self.__statusDescription = statusDescription
	def delStatusDescription(self): self.__statusDescription = None
	# Properties
	statusDescription = property(getStatusDescription, setStatusDescription, delStatusDescription, "Property for statusDescription")
	def getRejectedReflections(self): return self.__rejectedReflections
	def setRejectedReflections(self, rejectedReflections):
		checkType("XSDataISPyBScreeningOutput", "setRejectedReflections", rejectedReflections, "XSDataInteger")
		self.__rejectedReflections = rejectedReflections
	def delRejectedReflections(self): self.__rejectedReflections = None
	# Properties
	rejectedReflections = property(getRejectedReflections, setRejectedReflections, delRejectedReflections, "Property for rejectedReflections")
	def getResolutionObtained(self): return self.__resolutionObtained
	def setResolutionObtained(self, resolutionObtained):
		checkType("XSDataISPyBScreeningOutput", "setResolutionObtained", resolutionObtained, "XSDataDouble")
		self.__resolutionObtained = resolutionObtained
	def delResolutionObtained(self): self.__resolutionObtained = None
	# Properties
	resolutionObtained = property(getResolutionObtained, setResolutionObtained, delResolutionObtained, "Property for resolutionObtained")
	def getSpotDeviationR(self): return self.__spotDeviationR
	def setSpotDeviationR(self, spotDeviationR):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationR", spotDeviationR, "XSDataLength")
		self.__spotDeviationR = spotDeviationR
	def delSpotDeviationR(self): self.__spotDeviationR = None
	# Properties
	spotDeviationR = property(getSpotDeviationR, setSpotDeviationR, delSpotDeviationR, "Property for spotDeviationR")
	def getSpotDeviationTheta(self): return self.__spotDeviationTheta
	def setSpotDeviationTheta(self, spotDeviationTheta):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationTheta", spotDeviationTheta, "XSDataAngle")
		self.__spotDeviationTheta = spotDeviationTheta
	def delSpotDeviationTheta(self): self.__spotDeviationTheta = None
	# Properties
	spotDeviationTheta = property(getSpotDeviationTheta, setSpotDeviationTheta, delSpotDeviationTheta, "Property for spotDeviationTheta")
	def getBeamShiftX(self): return self.__beamShiftX
	def setBeamShiftX(self, beamShiftX):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftX", beamShiftX, "XSDataLength")
		self.__beamShiftX = beamShiftX
	def delBeamShiftX(self): self.__beamShiftX = None
	# Properties
	beamShiftX = property(getBeamShiftX, setBeamShiftX, delBeamShiftX, "Property for beamShiftX")
	def getBeamShiftY(self): return self.__beamShiftY
	def setBeamShiftY(self, beamShiftY):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftY", beamShiftY, "XSDataLength")
		self.__beamShiftY = beamShiftY
	def delBeamShiftY(self): self.__beamShiftY = None
	# Properties
	beamShiftY = property(getBeamShiftY, setBeamShiftY, delBeamShiftY, "Property for beamShiftY")
	def getNumSpotsFound(self): return self.__numSpotsFound
	def setNumSpotsFound(self, numSpotsFound):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsFound", numSpotsFound, "XSDataInteger")
		self.__numSpotsFound = numSpotsFound
	def delNumSpotsFound(self): self.__numSpotsFound = None
	# Properties
	numSpotsFound = property(getNumSpotsFound, setNumSpotsFound, delNumSpotsFound, "Property for numSpotsFound")
	def getNumSpotsUsed(self): return self.__numSpotsUsed
	def setNumSpotsUsed(self, numSpotsUsed):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsUsed", numSpotsUsed, "XSDataInteger")
		self.__numSpotsUsed = numSpotsUsed
	def delNumSpotsUsed(self): self.__numSpotsUsed = None
	# Properties
	numSpotsUsed = property(getNumSpotsUsed, setNumSpotsUsed, delNumSpotsUsed, "Property for numSpotsUsed")
	def getNumSpotsRejected(self): return self.__numSpotsRejected
	def setNumSpotsRejected(self, numSpotsRejected):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsRejected", numSpotsRejected, "XSDataInteger")
		self.__numSpotsRejected = numSpotsRejected
	def delNumSpotsRejected(self): self.__numSpotsRejected = None
	# Properties
	numSpotsRejected = property(getNumSpotsRejected, setNumSpotsRejected, delNumSpotsRejected, "Property for numSpotsRejected")
	def getMosaicity(self): return self.__mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataISPyBScreeningOutput", "setMosaicity", mosaicity, "XSDataDouble")
		self.__mosaicity = mosaicity
	def delMosaicity(self): self.__mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getIOverSigma(self): return self.__iOverSigma
	def setIOverSigma(self, iOverSigma):
		checkType("XSDataISPyBScreeningOutput", "setIOverSigma", iOverSigma, "XSDataDouble")
		self.__iOverSigma = iOverSigma
	def delIOverSigma(self): self.__iOverSigma = None
	# Properties
	iOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for iOverSigma")
	def getDiffractionRings(self): return self.__diffractionRings
	def setDiffractionRings(self, diffractionRings):
		checkType("XSDataISPyBScreeningOutput", "setDiffractionRings", diffractionRings, "XSDataBoolean")
		self.__diffractionRings = diffractionRings
	def delDiffractionRings(self): self.__diffractionRings = None
	# Properties
	diffractionRings = property(getDiffractionRings, setDiffractionRings, delDiffractionRings, "Property for diffractionRings")
	def getScreeningSuccess(self): return self.__screeningSuccess
	def setScreeningSuccess(self, screeningSuccess):
		checkType("XSDataISPyBScreeningOutput", "setScreeningSuccess", screeningSuccess, "XSDataBoolean")
		self.__screeningSuccess = screeningSuccess
	def delScreeningSuccess(self): self.__screeningSuccess = None
	# Properties
	screeningSuccess = property(getScreeningSuccess, setScreeningSuccess, delScreeningSuccess, "Property for screeningSuccess")
	def getMosaicityEstimated(self): return self.__mosaicityEstimated
	def setMosaicityEstimated(self, mosaicityEstimated):
		checkType("XSDataISPyBScreeningOutput", "setMosaicityEstimated", mosaicityEstimated, "XSDataBoolean")
		self.__mosaicityEstimated = mosaicityEstimated
	def delMosaicityEstimated(self): self.__mosaicityEstimated = None
	# Properties
	mosaicityEstimated = property(getMosaicityEstimated, setMosaicityEstimated, delMosaicityEstimated, "Property for mosaicityEstimated")
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__statusDescription is not None:
			self.statusDescription.export(outfile, level, name_='statusDescription')
		if self.__rejectedReflections is not None:
			self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
		if self.__resolutionObtained is not None:
			self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
		if self.__spotDeviationR is not None:
			self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
		if self.__spotDeviationTheta is not None:
			self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
		if self.__beamShiftX is not None:
			self.beamShiftX.export(outfile, level, name_='beamShiftX')
		if self.__beamShiftY is not None:
			self.beamShiftY.export(outfile, level, name_='beamShiftY')
		if self.__numSpotsFound is not None:
			self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
		if self.__numSpotsUsed is not None:
			self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
		if self.__numSpotsRejected is not None:
			self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
		if self.__mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self.__iOverSigma is not None:
			self.iOverSigma.export(outfile, level, name_='iOverSigma')
		if self.__diffractionRings is not None:
			self.diffractionRings.export(outfile, level, name_='diffractionRings')
		if self.__screeningSuccess is not None:
			self.screeningSuccess.export(outfile, level, name_='screeningSuccess')
		else:
			warnEmptyAttribute("screeningSuccess", "XSDataBoolean")
		if self.__mosaicityEstimated is not None:
			self.mosaicityEstimated.export(outfile, level, name_='mosaicityEstimated')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statusDescription':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStatusDescription(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rejectedReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRejectedReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionObtained':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolutionObtained(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationR':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setSpotDeviationR(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationTheta':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setSpotDeviationTheta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShiftX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamShiftX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShiftY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamShiftY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsFound':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsFound(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsUsed':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsUsed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsRejected':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsRejected(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iOverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionRings':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDiffractionRings(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningSuccess':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setScreeningSuccess(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicityEstimated':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setMosaicityEstimated(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutput

class XSDataISPyBScreeningOutputLattice(XSData):
	def __init__(self, timeStamp=None, unitCell_gamma=None, unitCell_c=None, unitCell_beta=None, unitCell_b=None, unitCell_alpha=None, unitCell_a=None, rawOrientationMatrix_c_z=None, rawOrientationMatrix_c_y=None, rawOrientationMatrix_c_x=None, rawOrientationMatrix_b_z=None, rawOrientationMatrix_b_y=None, rawOrientationMatrix_b_x=None, rawOrientationMatrix_a_z=None, rawOrientationMatrix_a_y=None, rawOrientationMatrix_a_x=None, bravaisLattice=None, pointGroup=None, spaceGroup=None, screeningOutputId=None, screeningOutputLatticeId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", spaceGroup, "XSDataString")
		self.__spaceGroup = spaceGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", pointGroup, "XSDataString")
		self.__pointGroup = pointGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_x, "XSDataDouble")
		self.__rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_y, "XSDataDouble")
		self.__rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_z, "XSDataDouble")
		self.__rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_x, "XSDataDouble")
		self.__rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_y, "XSDataDouble")
		self.__rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_z, "XSDataDouble")
		self.__rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_x, "XSDataDouble")
		self.__rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_y, "XSDataDouble")
		self.__rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_z, "XSDataDouble")
		self.__rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_a, "XSDataLength")
		self.__unitCell_a = unitCell_a
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_alpha, "XSDataAngle")
		self.__unitCell_alpha = unitCell_alpha
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_b, "XSDataLength")
		self.__unitCell_b = unitCell_b
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_beta, "XSDataAngle")
		self.__unitCell_beta = unitCell_beta
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_c, "XSDataLength")
		self.__unitCell_c = unitCell_c
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_gamma, "XSDataAngle")
		self.__unitCell_gamma = unitCell_gamma
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", timeStamp, "XSDataLength")
		self.__timeStamp = timeStamp
	def getScreeningOutputLatticeId(self): return self.__screeningOutputLatticeId
	def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputLatticeId", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
	def delScreeningOutputLatticeId(self): self.__screeningOutputLatticeId = None
	# Properties
	screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getSpaceGroup(self): return self.__spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setSpaceGroup", spaceGroup, "XSDataString")
		self.__spaceGroup = spaceGroup
	def delSpaceGroup(self): self.__spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def getPointGroup(self): return self.__pointGroup
	def setPointGroup(self, pointGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setPointGroup", pointGroup, "XSDataString")
		self.__pointGroup = pointGroup
	def delPointGroup(self): self.__pointGroup = None
	# Properties
	pointGroup = property(getPointGroup, setPointGroup, delPointGroup, "Property for pointGroup")
	def getBravaisLattice(self): return self.__bravaisLattice
	def setBravaisLattice(self, bravaisLattice):
		checkType("XSDataISPyBScreeningOutputLattice", "setBravaisLattice", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
	def delBravaisLattice(self): self.__bravaisLattice = None
	# Properties
	bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
	def getRawOrientationMatrix_a_x(self): return self.__rawOrientationMatrix_a_x
	def setRawOrientationMatrix_a_x(self, rawOrientationMatrix_a_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_x", rawOrientationMatrix_a_x, "XSDataDouble")
		self.__rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
	def delRawOrientationMatrix_a_x(self): self.__rawOrientationMatrix_a_x = None
	# Properties
	rawOrientationMatrix_a_x = property(getRawOrientationMatrix_a_x, setRawOrientationMatrix_a_x, delRawOrientationMatrix_a_x, "Property for rawOrientationMatrix_a_x")
	def getRawOrientationMatrix_a_y(self): return self.__rawOrientationMatrix_a_y
	def setRawOrientationMatrix_a_y(self, rawOrientationMatrix_a_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_y", rawOrientationMatrix_a_y, "XSDataDouble")
		self.__rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
	def delRawOrientationMatrix_a_y(self): self.__rawOrientationMatrix_a_y = None
	# Properties
	rawOrientationMatrix_a_y = property(getRawOrientationMatrix_a_y, setRawOrientationMatrix_a_y, delRawOrientationMatrix_a_y, "Property for rawOrientationMatrix_a_y")
	def getRawOrientationMatrix_a_z(self): return self.__rawOrientationMatrix_a_z
	def setRawOrientationMatrix_a_z(self, rawOrientationMatrix_a_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_z", rawOrientationMatrix_a_z, "XSDataDouble")
		self.__rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
	def delRawOrientationMatrix_a_z(self): self.__rawOrientationMatrix_a_z = None
	# Properties
	rawOrientationMatrix_a_z = property(getRawOrientationMatrix_a_z, setRawOrientationMatrix_a_z, delRawOrientationMatrix_a_z, "Property for rawOrientationMatrix_a_z")
	def getRawOrientationMatrix_b_x(self): return self.__rawOrientationMatrix_b_x
	def setRawOrientationMatrix_b_x(self, rawOrientationMatrix_b_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_x", rawOrientationMatrix_b_x, "XSDataDouble")
		self.__rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
	def delRawOrientationMatrix_b_x(self): self.__rawOrientationMatrix_b_x = None
	# Properties
	rawOrientationMatrix_b_x = property(getRawOrientationMatrix_b_x, setRawOrientationMatrix_b_x, delRawOrientationMatrix_b_x, "Property for rawOrientationMatrix_b_x")
	def getRawOrientationMatrix_b_y(self): return self.__rawOrientationMatrix_b_y
	def setRawOrientationMatrix_b_y(self, rawOrientationMatrix_b_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_y", rawOrientationMatrix_b_y, "XSDataDouble")
		self.__rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
	def delRawOrientationMatrix_b_y(self): self.__rawOrientationMatrix_b_y = None
	# Properties
	rawOrientationMatrix_b_y = property(getRawOrientationMatrix_b_y, setRawOrientationMatrix_b_y, delRawOrientationMatrix_b_y, "Property for rawOrientationMatrix_b_y")
	def getRawOrientationMatrix_b_z(self): return self.__rawOrientationMatrix_b_z
	def setRawOrientationMatrix_b_z(self, rawOrientationMatrix_b_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_z", rawOrientationMatrix_b_z, "XSDataDouble")
		self.__rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
	def delRawOrientationMatrix_b_z(self): self.__rawOrientationMatrix_b_z = None
	# Properties
	rawOrientationMatrix_b_z = property(getRawOrientationMatrix_b_z, setRawOrientationMatrix_b_z, delRawOrientationMatrix_b_z, "Property for rawOrientationMatrix_b_z")
	def getRawOrientationMatrix_c_x(self): return self.__rawOrientationMatrix_c_x
	def setRawOrientationMatrix_c_x(self, rawOrientationMatrix_c_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_x", rawOrientationMatrix_c_x, "XSDataDouble")
		self.__rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
	def delRawOrientationMatrix_c_x(self): self.__rawOrientationMatrix_c_x = None
	# Properties
	rawOrientationMatrix_c_x = property(getRawOrientationMatrix_c_x, setRawOrientationMatrix_c_x, delRawOrientationMatrix_c_x, "Property for rawOrientationMatrix_c_x")
	def getRawOrientationMatrix_c_y(self): return self.__rawOrientationMatrix_c_y
	def setRawOrientationMatrix_c_y(self, rawOrientationMatrix_c_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_y", rawOrientationMatrix_c_y, "XSDataDouble")
		self.__rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
	def delRawOrientationMatrix_c_y(self): self.__rawOrientationMatrix_c_y = None
	# Properties
	rawOrientationMatrix_c_y = property(getRawOrientationMatrix_c_y, setRawOrientationMatrix_c_y, delRawOrientationMatrix_c_y, "Property for rawOrientationMatrix_c_y")
	def getRawOrientationMatrix_c_z(self): return self.__rawOrientationMatrix_c_z
	def setRawOrientationMatrix_c_z(self, rawOrientationMatrix_c_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_z", rawOrientationMatrix_c_z, "XSDataDouble")
		self.__rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
	def delRawOrientationMatrix_c_z(self): self.__rawOrientationMatrix_c_z = None
	# Properties
	rawOrientationMatrix_c_z = property(getRawOrientationMatrix_c_z, setRawOrientationMatrix_c_z, delRawOrientationMatrix_c_z, "Property for rawOrientationMatrix_c_z")
	def getUnitCell_a(self): return self.__unitCell_a
	def setUnitCell_a(self, unitCell_a):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_a", unitCell_a, "XSDataLength")
		self.__unitCell_a = unitCell_a
	def delUnitCell_a(self): self.__unitCell_a = None
	# Properties
	unitCell_a = property(getUnitCell_a, setUnitCell_a, delUnitCell_a, "Property for unitCell_a")
	def getUnitCell_alpha(self): return self.__unitCell_alpha
	def setUnitCell_alpha(self, unitCell_alpha):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_alpha", unitCell_alpha, "XSDataAngle")
		self.__unitCell_alpha = unitCell_alpha
	def delUnitCell_alpha(self): self.__unitCell_alpha = None
	# Properties
	unitCell_alpha = property(getUnitCell_alpha, setUnitCell_alpha, delUnitCell_alpha, "Property for unitCell_alpha")
	def getUnitCell_b(self): return self.__unitCell_b
	def setUnitCell_b(self, unitCell_b):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_b", unitCell_b, "XSDataLength")
		self.__unitCell_b = unitCell_b
	def delUnitCell_b(self): self.__unitCell_b = None
	# Properties
	unitCell_b = property(getUnitCell_b, setUnitCell_b, delUnitCell_b, "Property for unitCell_b")
	def getUnitCell_beta(self): return self.__unitCell_beta
	def setUnitCell_beta(self, unitCell_beta):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_beta", unitCell_beta, "XSDataAngle")
		self.__unitCell_beta = unitCell_beta
	def delUnitCell_beta(self): self.__unitCell_beta = None
	# Properties
	unitCell_beta = property(getUnitCell_beta, setUnitCell_beta, delUnitCell_beta, "Property for unitCell_beta")
	def getUnitCell_c(self): return self.__unitCell_c
	def setUnitCell_c(self, unitCell_c):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_c", unitCell_c, "XSDataLength")
		self.__unitCell_c = unitCell_c
	def delUnitCell_c(self): self.__unitCell_c = None
	# Properties
	unitCell_c = property(getUnitCell_c, setUnitCell_c, delUnitCell_c, "Property for unitCell_c")
	def getUnitCell_gamma(self): return self.__unitCell_gamma
	def setUnitCell_gamma(self, unitCell_gamma):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_gamma", unitCell_gamma, "XSDataAngle")
		self.__unitCell_gamma = unitCell_gamma
	def delUnitCell_gamma(self): self.__unitCell_gamma = None
	# Properties
	unitCell_gamma = property(getUnitCell_gamma, setUnitCell_gamma, delUnitCell_gamma, "Property for unitCell_gamma")
	def getTimeStamp(self): return self.__timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreeningOutputLattice", "setTimeStamp", timeStamp, "XSDataLength")
		self.__timeStamp = timeStamp
	def delTimeStamp(self): self.__timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningOutputLatticeId is not None:
			self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__spaceGroup is not None:
			self.spaceGroup.export(outfile, level, name_='spaceGroup')
		else:
			warnEmptyAttribute("spaceGroup", "XSDataString")
		if self.__pointGroup is not None:
			self.pointGroup.export(outfile, level, name_='pointGroup')
		else:
			warnEmptyAttribute("pointGroup", "XSDataString")
		if self.__bravaisLattice is not None:
			self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
		else:
			warnEmptyAttribute("bravaisLattice", "XSDataString")
		if self.__rawOrientationMatrix_a_x is not None:
			self.rawOrientationMatrix_a_x.export(outfile, level, name_='rawOrientationMatrix_a_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_x", "XSDataDouble")
		if self.__rawOrientationMatrix_a_y is not None:
			self.rawOrientationMatrix_a_y.export(outfile, level, name_='rawOrientationMatrix_a_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_y", "XSDataDouble")
		if self.__rawOrientationMatrix_a_z is not None:
			self.rawOrientationMatrix_a_z.export(outfile, level, name_='rawOrientationMatrix_a_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_z", "XSDataDouble")
		if self.__rawOrientationMatrix_b_x is not None:
			self.rawOrientationMatrix_b_x.export(outfile, level, name_='rawOrientationMatrix_b_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_x", "XSDataDouble")
		if self.__rawOrientationMatrix_b_y is not None:
			self.rawOrientationMatrix_b_y.export(outfile, level, name_='rawOrientationMatrix_b_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_y", "XSDataDouble")
		if self.__rawOrientationMatrix_b_z is not None:
			self.rawOrientationMatrix_b_z.export(outfile, level, name_='rawOrientationMatrix_b_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_z", "XSDataDouble")
		if self.__rawOrientationMatrix_c_x is not None:
			self.rawOrientationMatrix_c_x.export(outfile, level, name_='rawOrientationMatrix_c_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_x", "XSDataDouble")
		if self.__rawOrientationMatrix_c_y is not None:
			self.rawOrientationMatrix_c_y.export(outfile, level, name_='rawOrientationMatrix_c_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_y", "XSDataDouble")
		if self.__rawOrientationMatrix_c_z is not None:
			self.rawOrientationMatrix_c_z.export(outfile, level, name_='rawOrientationMatrix_c_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_z", "XSDataDouble")
		if self.__unitCell_a is not None:
			self.unitCell_a.export(outfile, level, name_='unitCell_a')
		else:
			warnEmptyAttribute("unitCell_a", "XSDataLength")
		if self.__unitCell_alpha is not None:
			self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
		else:
			warnEmptyAttribute("unitCell_alpha", "XSDataAngle")
		if self.__unitCell_b is not None:
			self.unitCell_b.export(outfile, level, name_='unitCell_b')
		else:
			warnEmptyAttribute("unitCell_b", "XSDataLength")
		if self.__unitCell_beta is not None:
			self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
		else:
			warnEmptyAttribute("unitCell_beta", "XSDataAngle")
		if self.__unitCell_c is not None:
			self.unitCell_c.export(outfile, level, name_='unitCell_c')
		else:
			warnEmptyAttribute("unitCell_c", "XSDataLength")
		if self.__unitCell_gamma is not None:
			self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
		else:
			warnEmptyAttribute("unitCell_gamma", "XSDataAngle")
		if self.__timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLatticeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputLatticeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spaceGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpaceGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pointGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPointGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bravaisLattice':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBravaisLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_x':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_y':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_z':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_x':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_y':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_z':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_x':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_y':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_z':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_a':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setUnitCell_a(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_alpha':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setUnitCell_alpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_b':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setUnitCell_b(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_beta':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setUnitCell_beta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_c':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setUnitCell_c(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_gamma':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setUnitCell_gamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeStamp':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setTimeStamp(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningOutputLattice' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningOutputLattice is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningOutputLattice.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputLattice()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputLattice()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutputLattice

class XSDataISPyBScreeningRank(XSData):
	def __init__(self, rankInformation=None, rankValue=None, screeningId=None, screeningRankSetId=None, screeningRankId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankValue, "XSDataDouble")
		self.__rankValue = rankValue
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankInformation, "XSDataString")
		self.__rankInformation = rankInformation
	def getScreeningRankId(self): return self.__screeningRankId
	def setScreeningRankId(self, screeningRankId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankId", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
	def delScreeningRankId(self): self.__screeningRankId = None
	# Properties
	screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningRank", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getRankValue(self): return self.__rankValue
	def setRankValue(self, rankValue):
		checkType("XSDataISPyBScreeningRank", "setRankValue", rankValue, "XSDataDouble")
		self.__rankValue = rankValue
	def delRankValue(self): self.__rankValue = None
	# Properties
	rankValue = property(getRankValue, setRankValue, delRankValue, "Property for rankValue")
	def getRankInformation(self): return self.__rankInformation
	def setRankInformation(self, rankInformation):
		checkType("XSDataISPyBScreeningRank", "setRankInformation", rankInformation, "XSDataString")
		self.__rankInformation = rankInformation
	def delRankInformation(self): self.__rankInformation = None
	# Properties
	rankInformation = property(getRankInformation, setRankInformation, delRankInformation, "Property for rankInformation")
	def export(self, outfile, level, name_='XSDataISPyBScreeningRank'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRank'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningRankId is not None:
			self.screeningRankId.export(outfile, level, name_='screeningRankId')
		if self.__screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__rankValue is not None:
			self.rankValue.export(outfile, level, name_='rankValue')
		else:
			warnEmptyAttribute("rankValue", "XSDataDouble")
		if self.__rankInformation is not None:
			self.rankInformation.export(outfile, level, name_='rankInformation')
		else:
			warnEmptyAttribute("rankInformation", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankSetId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankValue':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRankValue(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankInformation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankInformation(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningRank' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningRank is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningRank.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRank()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRank()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRank

class XSDataISPyBScreeningRankSet(XSData):
	def __init__(self, rankingSummaryFileName=None, rankingProjectFileName=None, rankEngine=None, screeningRankSetId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankEngine, "XSDataString")
		self.__rankEngine = rankEngine
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingProjectFileName, "XSDataString")
		self.__rankingProjectFileName = rankingProjectFileName
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingSummaryFileName, "XSDataString")
		self.__rankingSummaryFileName = rankingSummaryFileName
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRankSet", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getRankEngine(self): return self.__rankEngine
	def setRankEngine(self, rankEngine):
		checkType("XSDataISPyBScreeningRankSet", "setRankEngine", rankEngine, "XSDataString")
		self.__rankEngine = rankEngine
	def delRankEngine(self): self.__rankEngine = None
	# Properties
	rankEngine = property(getRankEngine, setRankEngine, delRankEngine, "Property for rankEngine")
	def getRankingProjectFileName(self): return self.__rankingProjectFileName
	def setRankingProjectFileName(self, rankingProjectFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingProjectFileName", rankingProjectFileName, "XSDataString")
		self.__rankingProjectFileName = rankingProjectFileName
	def delRankingProjectFileName(self): self.__rankingProjectFileName = None
	# Properties
	rankingProjectFileName = property(getRankingProjectFileName, setRankingProjectFileName, delRankingProjectFileName, "Property for rankingProjectFileName")
	def getRankingSummaryFileName(self): return self.__rankingSummaryFileName
	def setRankingSummaryFileName(self, rankingSummaryFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingSummaryFileName", rankingSummaryFileName, "XSDataString")
		self.__rankingSummaryFileName = rankingSummaryFileName
	def delRankingSummaryFileName(self): self.__rankingSummaryFileName = None
	# Properties
	rankingSummaryFileName = property(getRankingSummaryFileName, setRankingSummaryFileName, delRankingSummaryFileName, "Property for rankingSummaryFileName")
	def export(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self.__rankEngine is not None:
			self.rankEngine.export(outfile, level, name_='rankEngine')
		else:
			warnEmptyAttribute("rankEngine", "XSDataString")
		if self.__rankingProjectFileName is not None:
			self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
		else:
			warnEmptyAttribute("rankingProjectFileName", "XSDataString")
		if self.__rankingSummaryFileName is not None:
			self.rankingSummaryFileName.export(outfile, level, name_='rankingSummaryFileName')
		else:
			warnEmptyAttribute("rankingSummaryFileName", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankSetId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankEngine':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankEngine(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingProjectFileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankingProjectFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingSummaryFileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankingSummaryFileName(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningRankSet' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningRankSet is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningRankSet.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRankSet()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRankSet()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRankSet

class XSDataISPyBScreeningStrategy(XSData):
	def __init__(self, transmission=None, rankingResolution=None, program=None, anomalous=None, multiplicity=None, completeness=None, resolution=None, exposureTime=None, rotation=None, phiEnd=None, phiStart=None, screeningOutputId=None, screeningStrategyId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiStart, "XSDataDouble")
		self.__phiStart = phiStart
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiEnd, "XSDataDouble")
		self.__phiEnd = phiEnd
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rotation, "XSDataDouble")
		self.__rotation = rotation
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", exposureTime, "XSDataDouble")
		self.__exposureTime = exposureTime
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", resolution, "XSDataDouble")
		self.__resolution = resolution
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", completeness, "XSDataDouble")
		self.__completeness = completeness
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", anomalous, "XSDataBoolean")
		self.__anomalous = anomalous
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", program, "XSDataString")
		self.__program = program
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rankingResolution, "XSDataDouble")
		self.__rankingResolution = rankingResolution
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", transmission, "XSDataDouble")
		self.__transmission = transmission
	def getScreeningStrategyId(self): return self.__screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self.__screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getPhiStart(self): return self.__phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataISPyBScreeningStrategy", "setPhiStart", phiStart, "XSDataDouble")
		self.__phiStart = phiStart
	def delPhiStart(self): self.__phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getPhiEnd(self): return self.__phiEnd
	def setPhiEnd(self, phiEnd):
		checkType("XSDataISPyBScreeningStrategy", "setPhiEnd", phiEnd, "XSDataDouble")
		self.__phiEnd = phiEnd
	def delPhiEnd(self): self.__phiEnd = None
	# Properties
	phiEnd = property(getPhiEnd, setPhiEnd, delPhiEnd, "Property for phiEnd")
	def getRotation(self): return self.__rotation
	def setRotation(self, rotation):
		checkType("XSDataISPyBScreeningStrategy", "setRotation", rotation, "XSDataDouble")
		self.__rotation = rotation
	def delRotation(self): self.__rotation = None
	# Properties
	rotation = property(getRotation, setRotation, delRotation, "Property for rotation")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBScreeningStrategy", "setExposureTime", exposureTime, "XSDataDouble")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategy", "setResolution", resolution, "XSDataDouble")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategy", "setCompleteness", completeness, "XSDataDouble")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self.__multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategy", "setMultiplicity", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
	def delMultiplicity(self): self.__multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getAnomalous(self): return self.__anomalous
	def setAnomalous(self, anomalous):
		checkType("XSDataISPyBScreeningStrategy", "setAnomalous", anomalous, "XSDataBoolean")
		self.__anomalous = anomalous
	def delAnomalous(self): self.__anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
	def getProgram(self): return self.__program
	def setProgram(self, program):
		checkType("XSDataISPyBScreeningStrategy", "setProgram", program, "XSDataString")
		self.__program = program
	def delProgram(self): self.__program = None
	# Properties
	program = property(getProgram, setProgram, delProgram, "Property for program")
	def getRankingResolution(self): return self.__rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataISPyBScreeningStrategy", "setRankingResolution", rankingResolution, "XSDataDouble")
		self.__rankingResolution = rankingResolution
	def delRankingResolution(self): self.__rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBScreeningStrategy", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__phiStart is not None:
			self.phiStart.export(outfile, level, name_='phiStart')
		else:
			warnEmptyAttribute("phiStart", "XSDataDouble")
		if self.__phiEnd is not None:
			self.phiEnd.export(outfile, level, name_='phiEnd')
		else:
			warnEmptyAttribute("phiEnd", "XSDataDouble")
		if self.__rotation is not None:
			self.rotation.export(outfile, level, name_='rotation')
		else:
			warnEmptyAttribute("rotation", "XSDataDouble")
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataDouble")
		if self.__resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self.__multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		else:
			warnEmptyAttribute("multiplicity", "XSDataDouble")
		if self.__anomalous is not None:
			self.anomalous.export(outfile, level, name_='anomalous')
		else:
			warnEmptyAttribute("anomalous", "XSDataBoolean")
		if self.__program is not None:
			self.program.export(outfile, level, name_='program')
		else:
			warnEmptyAttribute("program", "XSDataString")
		if self.__rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		else:
			warnEmptyAttribute("rankingResolution", "XSDataDouble")
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		else:
			warnEmptyAttribute("transmission", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPhiStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiEnd':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPhiEnd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRotation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalous':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAnomalous(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'program':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProgram(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRankingResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategy' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategy is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategy.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategy()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategy()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategy

class XSDataISPyBScreeningStrategyContainer(XSData):
	def __init__(self, screeningStrategyWedgeContainer=None, screeningStrategy=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningStrategyContainer", "Constructor of XSDataISPyBScreeningStrategyContainer", screeningStrategy, "XSDataISPyBScreeningStrategy")
		self.__screeningStrategy = screeningStrategy
		if screeningStrategyWedgeContainer is None:
			self.__screeningStrategyWedgeContainer = []
		else:
			checkType("XSDataISPyBScreeningStrategyContainer", "Constructor of XSDataISPyBScreeningStrategyContainer", screeningStrategyWedgeContainer, "list")
			self.__screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
	def getScreeningStrategy(self): return self.__screeningStrategy
	def setScreeningStrategy(self, screeningStrategy):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategy", screeningStrategy, "XSDataISPyBScreeningStrategy")
		self.__screeningStrategy = screeningStrategy
	def delScreeningStrategy(self): self.__screeningStrategy = None
	# Properties
	screeningStrategy = property(getScreeningStrategy, setScreeningStrategy, delScreeningStrategy, "Property for screeningStrategy")
	def getScreeningStrategyWedgeContainer(self): return self.__screeningStrategyWedgeContainer
	def setScreeningStrategyWedgeContainer(self, screeningStrategyWedgeContainer):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", screeningStrategyWedgeContainer, "list")
		self.__screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
	def delScreeningStrategyWedgeContainer(self): self.__screeningStrategyWedgeContainer = None
	# Properties
	screeningStrategyWedgeContainer = property(getScreeningStrategyWedgeContainer, setScreeningStrategyWedgeContainer, delScreeningStrategyWedgeContainer, "Property for screeningStrategyWedgeContainer")
	def addScreeningStrategyWedgeContainer(self, value):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", value, "XSDataISPyBScreeningStrategyWedgeContainer")
		self.__screeningStrategyWedgeContainer.append(value)
	def insertScreeningStrategyWedgeContainer(self, index, value):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", value, "XSDataISPyBScreeningStrategyWedgeContainer")
		self.__screeningStrategyWedgeContainer[index] = value
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningStrategy is not None:
			self.screeningStrategy.export(outfile, level, name_='screeningStrategy')
		else:
			warnEmptyAttribute("screeningStrategy", "XSDataISPyBScreeningStrategy")
		for screeningStrategyWedgeContainer_ in self.getScreeningStrategyWedgeContainer():
			screeningStrategyWedgeContainer_.export(outfile, level, name_='screeningStrategyWedgeContainer')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategy':
			obj_ = XSDataISPyBScreeningStrategy()
			obj_.build(child_)
			self.setScreeningStrategy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyWedgeContainer':
			obj_ = XSDataISPyBScreeningStrategyWedgeContainer()
			obj_.build(child_)
			self.screeningStrategyWedgeContainer.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategyContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyContainer

class XSDataISPyBScreeningOutputContainer(XSData):
	def __init__(self, screeningStrategyContainer=None, screeningOutputLattice=None, screeningOutput=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningOutputContainer", "Constructor of XSDataISPyBScreeningOutputContainer", screeningOutput, "XSDataISPyBScreeningOutput")
		self.__screeningOutput = screeningOutput
		if screeningOutputLattice is None:
			self.__screeningOutputLattice = []
		else:
			checkType("XSDataISPyBScreeningOutputContainer", "Constructor of XSDataISPyBScreeningOutputContainer", screeningOutputLattice, "list")
			self.__screeningOutputLattice = screeningOutputLattice
		if screeningStrategyContainer is None:
			self.__screeningStrategyContainer = []
		else:
			checkType("XSDataISPyBScreeningOutputContainer", "Constructor of XSDataISPyBScreeningOutputContainer", screeningStrategyContainer, "list")
			self.__screeningStrategyContainer = screeningStrategyContainer
	def getScreeningOutput(self): return self.__screeningOutput
	def setScreeningOutput(self, screeningOutput):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutput", screeningOutput, "XSDataISPyBScreeningOutput")
		self.__screeningOutput = screeningOutput
	def delScreeningOutput(self): self.__screeningOutput = None
	# Properties
	screeningOutput = property(getScreeningOutput, setScreeningOutput, delScreeningOutput, "Property for screeningOutput")
	def getScreeningOutputLattice(self): return self.__screeningOutputLattice
	def setScreeningOutputLattice(self, screeningOutputLattice):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", screeningOutputLattice, "list")
		self.__screeningOutputLattice = screeningOutputLattice
	def delScreeningOutputLattice(self): self.__screeningOutputLattice = None
	# Properties
	screeningOutputLattice = property(getScreeningOutputLattice, setScreeningOutputLattice, delScreeningOutputLattice, "Property for screeningOutputLattice")
	def addScreeningOutputLattice(self, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", value, "XSDataISPyBScreeningOutputLattice")
		self.__screeningOutputLattice.append(value)
	def insertScreeningOutputLattice(self, index, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", value, "XSDataISPyBScreeningOutputLattice")
		self.__screeningOutputLattice[index] = value
	def getScreeningStrategyContainer(self): return self.__screeningStrategyContainer
	def setScreeningStrategyContainer(self, screeningStrategyContainer):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", screeningStrategyContainer, "list")
		self.__screeningStrategyContainer = screeningStrategyContainer
	def delScreeningStrategyContainer(self): self.__screeningStrategyContainer = None
	# Properties
	screeningStrategyContainer = property(getScreeningStrategyContainer, setScreeningStrategyContainer, delScreeningStrategyContainer, "Property for screeningStrategyContainer")
	def addScreeningStrategyContainer(self, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", value, "XSDataISPyBScreeningStrategyContainer")
		self.__screeningStrategyContainer.append(value)
	def insertScreeningStrategyContainer(self, index, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", value, "XSDataISPyBScreeningStrategyContainer")
		self.__screeningStrategyContainer[index] = value
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningOutput is not None:
			self.screeningOutput.export(outfile, level, name_='screeningOutput')
		else:
			warnEmptyAttribute("screeningOutput", "XSDataISPyBScreeningOutput")
		for screeningOutputLattice_ in self.getScreeningOutputLattice():
			screeningOutputLattice_.export(outfile, level, name_='screeningOutputLattice')
		for screeningStrategyContainer_ in self.getScreeningStrategyContainer():
			screeningStrategyContainer_.export(outfile, level, name_='screeningStrategyContainer')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutput':
			obj_ = XSDataISPyBScreeningOutput()
			obj_.build(child_)
			self.setScreeningOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLattice':
			obj_ = XSDataISPyBScreeningOutputLattice()
			obj_.build(child_)
			self.screeningOutputLattice.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyContainer':
			obj_ = XSDataISPyBScreeningStrategyContainer()
			obj_.build(child_)
			self.screeningStrategyContainer.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningOutputContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningOutputContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningOutputContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutputContainer

class XSDataISPyBScreeningStrategySubWedge(XSData):
	def __init__(self, numberOfImages=None, doseTotal=None, resolution=None, multiplicity=None, completeness=None, oscillationRange=None, transmission=None, exposureTime=None, axisEnd=None, axisStart=None, rotationAxis=None, subWedgeNumber=None, screeningStrategyWedgeId=None, screeningStrategySubWedgeId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", screeningStrategySubWedgeId, "XSDataInteger")
		self.__screeningStrategySubWedgeId = screeningStrategySubWedgeId
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", screeningStrategyWedgeId, "XSDataInteger")
		self.__screeningStrategyWedgeId = screeningStrategyWedgeId
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", subWedgeNumber, "XSDataInteger")
		self.__subWedgeNumber = subWedgeNumber
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", rotationAxis, "XSDataString")
		self.__rotationAxis = rotationAxis
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", axisStart, "XSDataAngle")
		self.__axisStart = axisStart
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", axisEnd, "XSDataAngle")
		self.__axisEnd = axisEnd
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", transmission, "XSDataDouble")
		self.__transmission = transmission
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", oscillationRange, "XSDataAngle")
		self.__oscillationRange = oscillationRange
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", completeness, "XSDataDouble")
		self.__completeness = completeness
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", resolution, "XSDataDouble")
		self.__resolution = resolution
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", doseTotal, "XSDataDouble")
		self.__doseTotal = doseTotal
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def getScreeningStrategySubWedgeId(self): return self.__screeningStrategySubWedgeId
	def setScreeningStrategySubWedgeId(self, screeningStrategySubWedgeId):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setScreeningStrategySubWedgeId", screeningStrategySubWedgeId, "XSDataInteger")
		self.__screeningStrategySubWedgeId = screeningStrategySubWedgeId
	def delScreeningStrategySubWedgeId(self): self.__screeningStrategySubWedgeId = None
	# Properties
	screeningStrategySubWedgeId = property(getScreeningStrategySubWedgeId, setScreeningStrategySubWedgeId, delScreeningStrategySubWedgeId, "Property for screeningStrategySubWedgeId")
	def getScreeningStrategyWedgeId(self): return self.__screeningStrategyWedgeId
	def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setScreeningStrategyWedgeId", screeningStrategyWedgeId, "XSDataInteger")
		self.__screeningStrategyWedgeId = screeningStrategyWedgeId
	def delScreeningStrategyWedgeId(self): self.__screeningStrategyWedgeId = None
	# Properties
	screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
	def getSubWedgeNumber(self): return self.__subWedgeNumber
	def setSubWedgeNumber(self, subWedgeNumber):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setSubWedgeNumber", subWedgeNumber, "XSDataInteger")
		self.__subWedgeNumber = subWedgeNumber
	def delSubWedgeNumber(self): self.__subWedgeNumber = None
	# Properties
	subWedgeNumber = property(getSubWedgeNumber, setSubWedgeNumber, delSubWedgeNumber, "Property for subWedgeNumber")
	def getRotationAxis(self): return self.__rotationAxis
	def setRotationAxis(self, rotationAxis):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setRotationAxis", rotationAxis, "XSDataString")
		self.__rotationAxis = rotationAxis
	def delRotationAxis(self): self.__rotationAxis = None
	# Properties
	rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
	def getAxisStart(self): return self.__axisStart
	def setAxisStart(self, axisStart):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setAxisStart", axisStart, "XSDataAngle")
		self.__axisStart = axisStart
	def delAxisStart(self): self.__axisStart = None
	# Properties
	axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
	def getAxisEnd(self): return self.__axisEnd
	def setAxisEnd(self, axisEnd):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setAxisEnd", axisEnd, "XSDataAngle")
		self.__axisEnd = axisEnd
	def delAxisEnd(self): self.__axisEnd = None
	# Properties
	axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setExposureTime", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getOscillationRange(self): return self.__oscillationRange
	def setOscillationRange(self, oscillationRange):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setOscillationRange", oscillationRange, "XSDataAngle")
		self.__oscillationRange = oscillationRange
	def delOscillationRange(self): self.__oscillationRange = None
	# Properties
	oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setCompleteness", completeness, "XSDataDouble")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self.__multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setMultiplicity", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
	def delMultiplicity(self): self.__multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setResolution", resolution, "XSDataDouble")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getDoseTotal(self): return self.__doseTotal
	def setDoseTotal(self, doseTotal):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setDoseTotal", doseTotal, "XSDataDouble")
		self.__doseTotal = doseTotal
	def delDoseTotal(self): self.__doseTotal = None
	# Properties
	doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
	def getNumberOfImages(self): return self.__numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def delNumberOfImages(self): self.__numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningStrategySubWedgeId is not None:
			self.screeningStrategySubWedgeId.export(outfile, level, name_='screeningStrategySubWedgeId')
		if self.__screeningStrategyWedgeId is not None:
			self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
		else:
			warnEmptyAttribute("screeningStrategyWedgeId", "XSDataInteger")
		if self.__subWedgeNumber is not None:
			self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
		else:
			warnEmptyAttribute("subWedgeNumber", "XSDataInteger")
		if self.__rotationAxis is not None:
			self.rotationAxis.export(outfile, level, name_='rotationAxis')
		else:
			warnEmptyAttribute("rotationAxis", "XSDataString")
		if self.__axisStart is not None:
			self.axisStart.export(outfile, level, name_='axisStart')
		else:
			warnEmptyAttribute("axisStart", "XSDataAngle")
		if self.__axisEnd is not None:
			self.axisEnd.export(outfile, level, name_='axisEnd')
		else:
			warnEmptyAttribute("axisEnd", "XSDataAngle")
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataTime")
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		else:
			warnEmptyAttribute("transmission", "XSDataDouble")
		if self.__oscillationRange is not None:
			self.oscillationRange.export(outfile, level, name_='oscillationRange')
		else:
			warnEmptyAttribute("oscillationRange", "XSDataAngle")
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self.__multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		else:
			warnEmptyAttribute("multiplicity", "XSDataDouble")
		if self.__resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self.__doseTotal is not None:
			self.doseTotal.export(outfile, level, name_='doseTotal')
		else:
			warnEmptyAttribute("doseTotal", "XSDataDouble")
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
			nodeName_ == 'screeningStrategySubWedgeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategySubWedgeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyWedgeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyWedgeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedgeNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSubWedgeNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxis':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRotationAxis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisStart':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAxisStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisEnd':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAxisEnd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'oscillationRange':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOscillationRange(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'doseTotal':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDoseTotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfImages(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategySubWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategySubWedge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategySubWedge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategySubWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategySubWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategySubWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategySubWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategySubWedge

class XSDataISPyBScreeningStrategyWedge(XSData):
	def __init__(self, kappa=None, phi=None, numberOfImages=None, doseTotal=None, multiplicity=None, completeness=None, resolution=None, wedgeNumber=None, screeningStrategyId=None, screeningStrategyWedgeId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", screeningStrategyWedgeId, "XSDataInteger")
		self.__screeningStrategyWedgeId = screeningStrategyWedgeId
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", wedgeNumber, "XSDataInteger")
		self.__wedgeNumber = wedgeNumber
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", resolution, "XSDataDouble")
		self.__resolution = resolution
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", completeness, "XSDataDouble")
		self.__completeness = completeness
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", doseTotal, "XSDataDouble")
		self.__doseTotal = doseTotal
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", phi, "XSDataDouble")
		self.__phi = phi
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", kappa, "XSDataDouble")
		self.__kappa = kappa
	def getScreeningStrategyWedgeId(self): return self.__screeningStrategyWedgeId
	def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
		checkType("XSDataISPyBScreeningStrategyWedge", "setScreeningStrategyWedgeId", screeningStrategyWedgeId, "XSDataInteger")
		self.__screeningStrategyWedgeId = screeningStrategyWedgeId
	def delScreeningStrategyWedgeId(self): self.__screeningStrategyWedgeId = None
	# Properties
	screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
	def getScreeningStrategyId(self): return self.__screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataISPyBScreeningStrategyWedge", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self.__screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getWedgeNumber(self): return self.__wedgeNumber
	def setWedgeNumber(self, wedgeNumber):
		checkType("XSDataISPyBScreeningStrategyWedge", "setWedgeNumber", wedgeNumber, "XSDataInteger")
		self.__wedgeNumber = wedgeNumber
	def delWedgeNumber(self): self.__wedgeNumber = None
	# Properties
	wedgeNumber = property(getWedgeNumber, setWedgeNumber, delWedgeNumber, "Property for wedgeNumber")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategyWedge", "setResolution", resolution, "XSDataDouble")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategyWedge", "setCompleteness", completeness, "XSDataDouble")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self.__multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategyWedge", "setMultiplicity", multiplicity, "XSDataDouble")
		self.__multiplicity = multiplicity
	def delMultiplicity(self): self.__multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getDoseTotal(self): return self.__doseTotal
	def setDoseTotal(self, doseTotal):
		checkType("XSDataISPyBScreeningStrategyWedge", "setDoseTotal", doseTotal, "XSDataDouble")
		self.__doseTotal = doseTotal
	def delDoseTotal(self): self.__doseTotal = None
	# Properties
	doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
	def getNumberOfImages(self): return self.__numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBScreeningStrategyWedge", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def delNumberOfImages(self): self.__numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getPhi(self): return self.__phi
	def setPhi(self, phi):
		checkType("XSDataISPyBScreeningStrategyWedge", "setPhi", phi, "XSDataDouble")
		self.__phi = phi
	def delPhi(self): self.__phi = None
	# Properties
	phi = property(getPhi, setPhi, delPhi, "Property for phi")
	def getKappa(self): return self.__kappa
	def setKappa(self, kappa):
		checkType("XSDataISPyBScreeningStrategyWedge", "setKappa", kappa, "XSDataDouble")
		self.__kappa = kappa
	def delKappa(self): self.__kappa = None
	# Properties
	kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningStrategyWedgeId is not None:
			self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
		if self.__screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		else:
			warnEmptyAttribute("screeningStrategyId", "XSDataInteger")
		if self.__wedgeNumber is not None:
			self.wedgeNumber.export(outfile, level, name_='wedgeNumber')
		else:
			warnEmptyAttribute("wedgeNumber", "XSDataInteger")
		if self.__resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self.__multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		else:
			warnEmptyAttribute("multiplicity", "XSDataDouble")
		if self.__doseTotal is not None:
			self.doseTotal.export(outfile, level, name_='doseTotal')
		else:
			warnEmptyAttribute("doseTotal", "XSDataDouble")
		if self.__numberOfImages is not None:
			self.numberOfImages.export(outfile, level, name_='numberOfImages')
		else:
			warnEmptyAttribute("numberOfImages", "XSDataInteger")
		if self.__phi is not None:
			self.phi.export(outfile, level, name_='phi')
		else:
			warnEmptyAttribute("phi", "XSDataDouble")
		if self.__kappa is not None:
			self.kappa.export(outfile, level, name_='kappa')
		else:
			warnEmptyAttribute("kappa", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyWedgeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyWedgeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wedgeNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setWedgeNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'doseTotal':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDoseTotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfImages(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phi':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPhi(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappa':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setKappa(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyWedge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategyWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyWedge

class XSDataISPyBScreeningStrategyWedgeContainer(XSData):
	def __init__(self, screeningStrategyWedge=None, screeningStrategySubWedge=None):
		XSData.__init__(self, )
		if screeningStrategySubWedge is None:
			self.__screeningStrategySubWedge = []
		else:
			checkType("XSDataISPyBScreeningStrategyWedgeContainer", "Constructor of XSDataISPyBScreeningStrategyWedgeContainer", screeningStrategySubWedge, "list")
			self.__screeningStrategySubWedge = screeningStrategySubWedge
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "Constructor of XSDataISPyBScreeningStrategyWedgeContainer", screeningStrategyWedge, "XSDataISPyBScreeningStrategyWedge")
		self.__screeningStrategyWedge = screeningStrategyWedge
	def getScreeningStrategySubWedge(self): return self.__screeningStrategySubWedge
	def setScreeningStrategySubWedge(self, screeningStrategySubWedge):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", screeningStrategySubWedge, "list")
		self.__screeningStrategySubWedge = screeningStrategySubWedge
	def delScreeningStrategySubWedge(self): self.__screeningStrategySubWedge = None
	# Properties
	screeningStrategySubWedge = property(getScreeningStrategySubWedge, setScreeningStrategySubWedge, delScreeningStrategySubWedge, "Property for screeningStrategySubWedge")
	def addScreeningStrategySubWedge(self, value):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", value, "XSDataISPyBScreeningStrategySubWedge")
		self.__screeningStrategySubWedge.append(value)
	def insertScreeningStrategySubWedge(self, index, value):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", value, "XSDataISPyBScreeningStrategySubWedge")
		self.__screeningStrategySubWedge[index] = value
	def getScreeningStrategyWedge(self): return self.__screeningStrategyWedge
	def setScreeningStrategyWedge(self, screeningStrategyWedge):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategyWedge", screeningStrategyWedge, "XSDataISPyBScreeningStrategyWedge")
		self.__screeningStrategyWedge = screeningStrategyWedge
	def delScreeningStrategyWedge(self): self.__screeningStrategyWedge = None
	# Properties
	screeningStrategyWedge = property(getScreeningStrategyWedge, setScreeningStrategyWedge, delScreeningStrategyWedge, "Property for screeningStrategyWedge")
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		for screeningStrategySubWedge_ in self.getScreeningStrategySubWedge():
			screeningStrategySubWedge_.export(outfile, level, name_='screeningStrategySubWedge')
		if self.__screeningStrategyWedge is not None:
			self.screeningStrategyWedge.export(outfile, level, name_='screeningStrategyWedge')
		else:
			warnEmptyAttribute("screeningStrategyWedge", "XSDataISPyBScreeningStrategyWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategySubWedge':
			obj_ = XSDataISPyBScreeningStrategySubWedge()
			obj_.build(child_)
			self.screeningStrategySubWedge.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyWedge':
			obj_ = XSDataISPyBScreeningStrategyWedge()
			obj_.build(child_)
			self.setScreeningStrategyWedge(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedgeContainer" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedgeContainer' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyWedgeContainer is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategyWedgeContainer.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyWedgeContainer()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedgeContainer" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategyWedgeContainer()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyWedgeContainer

class XSDataInputISPyBStoreScreening(XSDataInput):
	def __init__(self, configuration=None, screeningRankSet=None, screeningRank=None, screeningOutputContainer=None, screeningInput=None, screening=None, image=None, file=None, diffractionPlan=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", diffractionPlan, "XSDataISPyBDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
		if file is None:
			self.__file = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", file, "list")
			self.__file = file
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", image, "XSDataISPyBImage")
		self.__image = image
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screening, "XSDataISPyBScreening")
		self.__screening = screening
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
		if screeningOutputContainer is None:
			self.__screeningOutputContainer = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningOutputContainer, "list")
			self.__screeningOutputContainer = screeningOutputContainer
		if screeningRank is None:
			self.__screeningRank = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningRank, "list")
			self.__screeningRank = screeningRank
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self.__screeningRankSet = screeningRankSet
	def getDiffractionPlan(self): return self.__diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputISPyBStoreScreening", "setDiffractionPlan", diffractionPlan, "XSDataISPyBDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self.__diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getFile(self): return self.__file
	def setFile(self, file):
		checkType("XSDataInputISPyBStoreScreening", "setFile", file, "list")
		self.__file = file
	def delFile(self): self.__file = None
	# Properties
	file = property(getFile, setFile, delFile, "Property for file")
	def addFile(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setFile", value, "XSDataISPyBScreeningFile")
		self.__file.append(value)
	def insertFile(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setFile", value, "XSDataISPyBScreeningFile")
		self.__file[index] = value
	def getImage(self): return self.__image
	def setImage(self, image):
		checkType("XSDataInputISPyBStoreScreening", "setImage", image, "XSDataISPyBImage")
		self.__image = image
	def delImage(self): self.__image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getScreening(self): return self.__screening
	def setScreening(self, screening):
		checkType("XSDataInputISPyBStoreScreening", "setScreening", screening, "XSDataISPyBScreening")
		self.__screening = screening
	def delScreening(self): self.__screening = None
	# Properties
	screening = property(getScreening, setScreening, delScreening, "Property for screening")
	def getScreeningInput(self): return self.__screeningInput
	def setScreeningInput(self, screeningInput):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningInput", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
	def delScreeningInput(self): self.__screeningInput = None
	# Properties
	screeningInput = property(getScreeningInput, setScreeningInput, delScreeningInput, "Property for screeningInput")
	def getScreeningOutputContainer(self): return self.__screeningOutputContainer
	def setScreeningOutputContainer(self, screeningOutputContainer):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", screeningOutputContainer, "list")
		self.__screeningOutputContainer = screeningOutputContainer
	def delScreeningOutputContainer(self): self.__screeningOutputContainer = None
	# Properties
	screeningOutputContainer = property(getScreeningOutputContainer, setScreeningOutputContainer, delScreeningOutputContainer, "Property for screeningOutputContainer")
	def addScreeningOutputContainer(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", value, "XSDataISPyBScreeningOutputContainer")
		self.__screeningOutputContainer.append(value)
	def insertScreeningOutputContainer(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", value, "XSDataISPyBScreeningOutputContainer")
		self.__screeningOutputContainer[index] = value
	def getScreeningRank(self): return self.__screeningRank
	def setScreeningRank(self, screeningRank):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", screeningRank, "list")
		self.__screeningRank = screeningRank
	def delScreeningRank(self): self.__screeningRank = None
	# Properties
	screeningRank = property(getScreeningRank, setScreeningRank, delScreeningRank, "Property for screeningRank")
	def addScreeningRank(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", value, "XSDataISPyBScreeningRank")
		self.__screeningRank.append(value)
	def insertScreeningRank(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", value, "XSDataISPyBScreeningRank")
		self.__screeningRank[index] = value
	def getScreeningRankSet(self): return self.__screeningRankSet
	def setScreeningRankSet(self, screeningRankSet):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRankSet", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self.__screeningRankSet = screeningRankSet
	def delScreeningRankSet(self): self.__screeningRankSet = None
	# Properties
	screeningRankSet = property(getScreeningRankSet, setScreeningRankSet, delScreeningRankSet, "Property for screeningRankSet")
	def export(self, outfile, level, name_='XSDataInputISPyBStoreScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputISPyBStoreScreening'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		for file_ in self.getFile():
			file_.export(outfile, level, name_='file')
		if self.__image is not None:
			self.image.export(outfile, level, name_='image')
		if self.__screening is not None:
			self.screening.export(outfile, level, name_='screening')
		if self.__screeningInput is not None:
			self.screeningInput.export(outfile, level, name_='screeningInput')
		for screeningOutputContainer_ in self.getScreeningOutputContainer():
			screeningOutputContainer_.export(outfile, level, name_='screeningOutputContainer')
		for screeningRank_ in self.getScreeningRank():
			screeningRank_.export(outfile, level, name_='screeningRank')
		if self.__screeningRankSet is not None:
			self.screeningRankSet.export(outfile, level, name_='screeningRankSet')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataISPyBDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'file':
			obj_ = XSDataISPyBScreeningFile()
			obj_.build(child_)
			self.file.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataISPyBImage()
			obj_.build(child_)
			self.setImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screening':
			obj_ = XSDataISPyBScreening()
			obj_.build(child_)
			self.setScreening(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInput':
			obj_ = XSDataISPyBScreeningInput()
			obj_.build(child_)
			self.setScreeningInput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputContainer':
			obj_ = XSDataISPyBScreeningOutputContainer()
			obj_.build(child_)
			self.screeningOutputContainer.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRank':
			obj_ = XSDataISPyBScreeningRank()
			obj_.build(child_)
			self.screeningRank.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSet':
			obj_ = XSDataISPyBScreeningRankSet()
			obj_.build(child_)
			self.setScreeningRankSet(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputISPyBStoreScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputISPyBStoreScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputISPyBStoreScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputISPyBStoreScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputISPyBStoreScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputISPyBStoreScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputISPyBStoreScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputISPyBStoreScreening

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

class XSDataResultISPyBStoreScreening(XSDataResult):
	def __init__(self, status=None, screeningId=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultISPyBStoreScreening", "Constructor of XSDataResultISPyBStoreScreening", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataResultISPyBStoreScreening", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def export(self, outfile, level, name_='XSDataResultISPyBStoreScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultISPyBStoreScreening'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__screeningId is not None:
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
		self.export( oStreamString, 0, name_="XSDataResultISPyBStoreScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultISPyBStoreScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultISPyBStoreScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultISPyBStoreScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultISPyBStoreScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultISPyBStoreScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultISPyBStoreScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultISPyBStoreScreening

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



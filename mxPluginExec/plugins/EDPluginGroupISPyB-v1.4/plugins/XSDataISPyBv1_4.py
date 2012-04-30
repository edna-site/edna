#!/usr/bin/env python

#
# Generated Mon Apr 30 02:45::55 2012 by EDGenerateDS.
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
#	if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
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
		self._spaceGroup = spaceGroup
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_a, "string")
		self._refinedCell_a = refinedCell_a
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_b, "string")
		self._refinedCell_b = refinedCell_b
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_c, "string")
		self._refinedCell_c = refinedCell_c
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_alpha, "string")
		self._refinedCell_alpha = refinedCell_alpha
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_beta, "string")
		self._refinedCell_beta = refinedCell_beta
		checkType("AutoProc", "Constructor of AutoProc", refinedCell_gamma, "string")
		self._refinedCell_gamma = refinedCell_gamma
	def getSpaceGroup(self): return self._spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("AutoProc", "setSpaceGroup", spaceGroup, "string")
		self._spaceGroup = spaceGroup
	def delSpaceGroup(self): self._spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def getRefinedCell_a(self): return self._refinedCell_a
	def setRefinedCell_a(self, refinedCell_a):
		checkType("AutoProc", "setRefinedCell_a", refinedCell_a, "string")
		self._refinedCell_a = refinedCell_a
	def delRefinedCell_a(self): self._refinedCell_a = None
	# Properties
	refinedCell_a = property(getRefinedCell_a, setRefinedCell_a, delRefinedCell_a, "Property for refinedCell_a")
	def getRefinedCell_b(self): return self._refinedCell_b
	def setRefinedCell_b(self, refinedCell_b):
		checkType("AutoProc", "setRefinedCell_b", refinedCell_b, "string")
		self._refinedCell_b = refinedCell_b
	def delRefinedCell_b(self): self._refinedCell_b = None
	# Properties
	refinedCell_b = property(getRefinedCell_b, setRefinedCell_b, delRefinedCell_b, "Property for refinedCell_b")
	def getRefinedCell_c(self): return self._refinedCell_c
	def setRefinedCell_c(self, refinedCell_c):
		checkType("AutoProc", "setRefinedCell_c", refinedCell_c, "string")
		self._refinedCell_c = refinedCell_c
	def delRefinedCell_c(self): self._refinedCell_c = None
	# Properties
	refinedCell_c = property(getRefinedCell_c, setRefinedCell_c, delRefinedCell_c, "Property for refinedCell_c")
	def getRefinedCell_alpha(self): return self._refinedCell_alpha
	def setRefinedCell_alpha(self, refinedCell_alpha):
		checkType("AutoProc", "setRefinedCell_alpha", refinedCell_alpha, "string")
		self._refinedCell_alpha = refinedCell_alpha
	def delRefinedCell_alpha(self): self._refinedCell_alpha = None
	# Properties
	refinedCell_alpha = property(getRefinedCell_alpha, setRefinedCell_alpha, delRefinedCell_alpha, "Property for refinedCell_alpha")
	def getRefinedCell_beta(self): return self._refinedCell_beta
	def setRefinedCell_beta(self, refinedCell_beta):
		checkType("AutoProc", "setRefinedCell_beta", refinedCell_beta, "string")
		self._refinedCell_beta = refinedCell_beta
	def delRefinedCell_beta(self): self._refinedCell_beta = None
	# Properties
	refinedCell_beta = property(getRefinedCell_beta, setRefinedCell_beta, delRefinedCell_beta, "Property for refinedCell_beta")
	def getRefinedCell_gamma(self): return self._refinedCell_gamma
	def setRefinedCell_gamma(self, refinedCell_gamma):
		checkType("AutoProc", "setRefinedCell_gamma", refinedCell_gamma, "string")
		self._refinedCell_gamma = refinedCell_gamma
	def delRefinedCell_gamma(self): self._refinedCell_gamma = None
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
		if self._spaceGroup is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<spaceGroup>%s</spaceGroup>\n' % self._spaceGroup))
		else:
			warnEmptyAttribute("spaceGroup", "string")
		if self._refinedCell_a is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_a>%s</refinedCell_a>\n' % self._refinedCell_a))
		else:
			warnEmptyAttribute("refinedCell_a", "string")
		if self._refinedCell_b is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_b>%s</refinedCell_b>\n' % self._refinedCell_b))
		else:
			warnEmptyAttribute("refinedCell_b", "string")
		if self._refinedCell_c is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_c>%s</refinedCell_c>\n' % self._refinedCell_c))
		else:
			warnEmptyAttribute("refinedCell_c", "string")
		if self._refinedCell_alpha is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_alpha>%s</refinedCell_alpha>\n' % self._refinedCell_alpha))
		else:
			warnEmptyAttribute("refinedCell_alpha", "string")
		if self._refinedCell_beta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_beta>%s</refinedCell_beta>\n' % self._refinedCell_beta))
		else:
			warnEmptyAttribute("refinedCell_beta", "string")
		if self._refinedCell_gamma is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedCell_gamma>%s</refinedCell_gamma>\n' % self._refinedCell_gamma))
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
			self._spaceGroup = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_a':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_a = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_b':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_b = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_c':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_c = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_alpha':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_alpha = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_beta':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_beta = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell_gamma':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._refinedCell_gamma = value_
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
		self._AutoProc = AutoProc
		checkType("AutoProcContainer", "Constructor of AutoProcContainer", AutoProcScalingContainer, "AutoProcScalingContainer")
		self._AutoProcScalingContainer = AutoProcScalingContainer
		checkType("AutoProcContainer", "Constructor of AutoProcContainer", AutoProcProgramContainer, "AutoProcProgramContainer")
		self._AutoProcProgramContainer = AutoProcProgramContainer
	def getAutoProc(self): return self._AutoProc
	def setAutoProc(self, AutoProc):
		checkType("AutoProcContainer", "setAutoProc", AutoProc, "AutoProc")
		self._AutoProc = AutoProc
	def delAutoProc(self): self._AutoProc = None
	# Properties
	AutoProc = property(getAutoProc, setAutoProc, delAutoProc, "Property for AutoProc")
	def getAutoProcScalingContainer(self): return self._AutoProcScalingContainer
	def setAutoProcScalingContainer(self, AutoProcScalingContainer):
		checkType("AutoProcContainer", "setAutoProcScalingContainer", AutoProcScalingContainer, "AutoProcScalingContainer")
		self._AutoProcScalingContainer = AutoProcScalingContainer
	def delAutoProcScalingContainer(self): self._AutoProcScalingContainer = None
	# Properties
	AutoProcScalingContainer = property(getAutoProcScalingContainer, setAutoProcScalingContainer, delAutoProcScalingContainer, "Property for AutoProcScalingContainer")
	def getAutoProcProgramContainer(self): return self._AutoProcProgramContainer
	def setAutoProcProgramContainer(self, AutoProcProgramContainer):
		checkType("AutoProcContainer", "setAutoProcProgramContainer", AutoProcProgramContainer, "AutoProcProgramContainer")
		self._AutoProcProgramContainer = AutoProcProgramContainer
	def delAutoProcProgramContainer(self): self._AutoProcProgramContainer = None
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
		if self._AutoProc is not None:
			self.AutoProc.export(outfile, level, name_='AutoProc')
		else:
			warnEmptyAttribute("AutoProc", "AutoProc")
		if self._AutoProcScalingContainer is not None:
			self.AutoProcScalingContainer.export(outfile, level, name_='AutoProcScalingContainer')
		else:
			warnEmptyAttribute("AutoProcScalingContainer", "AutoProcScalingContainer")
		if self._AutoProcProgramContainer is not None:
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
		self._startImageNumber = startImageNumber
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", endImageNumber, "integer")
		self._endImageNumber = endImageNumber
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedDetectorDistance, "float")
		self._refinedDetectorDistance = refinedDetectorDistance
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedXbeam, "float")
		self._refinedXbeam = refinedXbeam
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", refinedYbeam, "float")
		self._refinedYbeam = refinedYbeam
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisX, "float")
		self._rotationAxisX = rotationAxisX
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisY, "float")
		self._rotationAxisY = rotationAxisY
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", rotationAxisZ, "float")
		self._rotationAxisZ = rotationAxisZ
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorX, "float")
		self._beamVectorX = beamVectorX
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorY, "float")
		self._beamVectorY = beamVectorY
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", beamVectorZ, "float")
		self._beamVectorZ = beamVectorZ
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_a, "float")
		self._cell_a = cell_a
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_b, "float")
		self._cell_b = cell_b
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_c, "float")
		self._cell_c = cell_c
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_alpha, "float")
		self._cell_alpha = cell_alpha
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_beta, "float")
		self._cell_beta = cell_beta
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", cell_gamma, "float")
		self._cell_gamma = cell_gamma
		checkType("AutoProcIntegration", "Constructor of AutoProcIntegration", anomalous, "boolean")
		self._anomalous = anomalous
	def getStartImageNumber(self): return self._startImageNumber
	def setStartImageNumber(self, startImageNumber):
		checkType("AutoProcIntegration", "setStartImageNumber", startImageNumber, "integer")
		self._startImageNumber = startImageNumber
	def delStartImageNumber(self): self._startImageNumber = None
	# Properties
	startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
	def getEndImageNumber(self): return self._endImageNumber
	def setEndImageNumber(self, endImageNumber):
		checkType("AutoProcIntegration", "setEndImageNumber", endImageNumber, "integer")
		self._endImageNumber = endImageNumber
	def delEndImageNumber(self): self._endImageNumber = None
	# Properties
	endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
	def getRefinedDetectorDistance(self): return self._refinedDetectorDistance
	def setRefinedDetectorDistance(self, refinedDetectorDistance):
		checkType("AutoProcIntegration", "setRefinedDetectorDistance", refinedDetectorDistance, "float")
		self._refinedDetectorDistance = refinedDetectorDistance
	def delRefinedDetectorDistance(self): self._refinedDetectorDistance = None
	# Properties
	refinedDetectorDistance = property(getRefinedDetectorDistance, setRefinedDetectorDistance, delRefinedDetectorDistance, "Property for refinedDetectorDistance")
	def getRefinedXbeam(self): return self._refinedXbeam
	def setRefinedXbeam(self, refinedXbeam):
		checkType("AutoProcIntegration", "setRefinedXbeam", refinedXbeam, "float")
		self._refinedXbeam = refinedXbeam
	def delRefinedXbeam(self): self._refinedXbeam = None
	# Properties
	refinedXbeam = property(getRefinedXbeam, setRefinedXbeam, delRefinedXbeam, "Property for refinedXbeam")
	def getRefinedYbeam(self): return self._refinedYbeam
	def setRefinedYbeam(self, refinedYbeam):
		checkType("AutoProcIntegration", "setRefinedYbeam", refinedYbeam, "float")
		self._refinedYbeam = refinedYbeam
	def delRefinedYbeam(self): self._refinedYbeam = None
	# Properties
	refinedYbeam = property(getRefinedYbeam, setRefinedYbeam, delRefinedYbeam, "Property for refinedYbeam")
	def getRotationAxisX(self): return self._rotationAxisX
	def setRotationAxisX(self, rotationAxisX):
		checkType("AutoProcIntegration", "setRotationAxisX", rotationAxisX, "float")
		self._rotationAxisX = rotationAxisX
	def delRotationAxisX(self): self._rotationAxisX = None
	# Properties
	rotationAxisX = property(getRotationAxisX, setRotationAxisX, delRotationAxisX, "Property for rotationAxisX")
	def getRotationAxisY(self): return self._rotationAxisY
	def setRotationAxisY(self, rotationAxisY):
		checkType("AutoProcIntegration", "setRotationAxisY", rotationAxisY, "float")
		self._rotationAxisY = rotationAxisY
	def delRotationAxisY(self): self._rotationAxisY = None
	# Properties
	rotationAxisY = property(getRotationAxisY, setRotationAxisY, delRotationAxisY, "Property for rotationAxisY")
	def getRotationAxisZ(self): return self._rotationAxisZ
	def setRotationAxisZ(self, rotationAxisZ):
		checkType("AutoProcIntegration", "setRotationAxisZ", rotationAxisZ, "float")
		self._rotationAxisZ = rotationAxisZ
	def delRotationAxisZ(self): self._rotationAxisZ = None
	# Properties
	rotationAxisZ = property(getRotationAxisZ, setRotationAxisZ, delRotationAxisZ, "Property for rotationAxisZ")
	def getBeamVectorX(self): return self._beamVectorX
	def setBeamVectorX(self, beamVectorX):
		checkType("AutoProcIntegration", "setBeamVectorX", beamVectorX, "float")
		self._beamVectorX = beamVectorX
	def delBeamVectorX(self): self._beamVectorX = None
	# Properties
	beamVectorX = property(getBeamVectorX, setBeamVectorX, delBeamVectorX, "Property for beamVectorX")
	def getBeamVectorY(self): return self._beamVectorY
	def setBeamVectorY(self, beamVectorY):
		checkType("AutoProcIntegration", "setBeamVectorY", beamVectorY, "float")
		self._beamVectorY = beamVectorY
	def delBeamVectorY(self): self._beamVectorY = None
	# Properties
	beamVectorY = property(getBeamVectorY, setBeamVectorY, delBeamVectorY, "Property for beamVectorY")
	def getBeamVectorZ(self): return self._beamVectorZ
	def setBeamVectorZ(self, beamVectorZ):
		checkType("AutoProcIntegration", "setBeamVectorZ", beamVectorZ, "float")
		self._beamVectorZ = beamVectorZ
	def delBeamVectorZ(self): self._beamVectorZ = None
	# Properties
	beamVectorZ = property(getBeamVectorZ, setBeamVectorZ, delBeamVectorZ, "Property for beamVectorZ")
	def getCell_a(self): return self._cell_a
	def setCell_a(self, cell_a):
		checkType("AutoProcIntegration", "setCell_a", cell_a, "float")
		self._cell_a = cell_a
	def delCell_a(self): self._cell_a = None
	# Properties
	cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
	def getCell_b(self): return self._cell_b
	def setCell_b(self, cell_b):
		checkType("AutoProcIntegration", "setCell_b", cell_b, "float")
		self._cell_b = cell_b
	def delCell_b(self): self._cell_b = None
	# Properties
	cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
	def getCell_c(self): return self._cell_c
	def setCell_c(self, cell_c):
		checkType("AutoProcIntegration", "setCell_c", cell_c, "float")
		self._cell_c = cell_c
	def delCell_c(self): self._cell_c = None
	# Properties
	cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
	def getCell_alpha(self): return self._cell_alpha
	def setCell_alpha(self, cell_alpha):
		checkType("AutoProcIntegration", "setCell_alpha", cell_alpha, "float")
		self._cell_alpha = cell_alpha
	def delCell_alpha(self): self._cell_alpha = None
	# Properties
	cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
	def getCell_beta(self): return self._cell_beta
	def setCell_beta(self, cell_beta):
		checkType("AutoProcIntegration", "setCell_beta", cell_beta, "float")
		self._cell_beta = cell_beta
	def delCell_beta(self): self._cell_beta = None
	# Properties
	cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
	def getCell_gamma(self): return self._cell_gamma
	def setCell_gamma(self, cell_gamma):
		checkType("AutoProcIntegration", "setCell_gamma", cell_gamma, "float")
		self._cell_gamma = cell_gamma
	def delCell_gamma(self): self._cell_gamma = None
	# Properties
	cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
	def getAnomalous(self): return self._anomalous
	def setAnomalous(self, anomalous):
		checkType("AutoProcIntegration", "setAnomalous", anomalous, "boolean")
		self._anomalous = anomalous
	def delAnomalous(self): self._anomalous = None
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
		if self._startImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self._startImageNumber))
		else:
			warnEmptyAttribute("startImageNumber", "integer")
		if self._endImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<endImageNumber>%d</endImageNumber>\n' % self._endImageNumber))
		else:
			warnEmptyAttribute("endImageNumber", "integer")
		if self._refinedDetectorDistance is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedDetectorDistance>%e</refinedDetectorDistance>\n' % self._refinedDetectorDistance))
		else:
			warnEmptyAttribute("refinedDetectorDistance", "float")
		if self._refinedXbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedXbeam>%e</refinedXbeam>\n' % self._refinedXbeam))
		else:
			warnEmptyAttribute("refinedXbeam", "float")
		if self._refinedYbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<refinedYbeam>%e</refinedYbeam>\n' % self._refinedYbeam))
		else:
			warnEmptyAttribute("refinedYbeam", "float")
		if self._rotationAxisX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisX>%e</rotationAxisX>\n' % self._rotationAxisX))
		else:
			warnEmptyAttribute("rotationAxisX", "float")
		if self._rotationAxisY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisY>%e</rotationAxisY>\n' % self._rotationAxisY))
		else:
			warnEmptyAttribute("rotationAxisY", "float")
		if self._rotationAxisZ is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxisZ>%e</rotationAxisZ>\n' % self._rotationAxisZ))
		else:
			warnEmptyAttribute("rotationAxisZ", "float")
		if self._beamVectorX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorX>%e</beamVectorX>\n' % self._beamVectorX))
		else:
			warnEmptyAttribute("beamVectorX", "float")
		if self._beamVectorY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorY>%e</beamVectorY>\n' % self._beamVectorY))
		else:
			warnEmptyAttribute("beamVectorY", "float")
		if self._beamVectorZ is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamVectorZ>%e</beamVectorZ>\n' % self._beamVectorZ))
		else:
			warnEmptyAttribute("beamVectorZ", "float")
		if self._cell_a is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_a>%e</cell_a>\n' % self._cell_a))
		else:
			warnEmptyAttribute("cell_a", "float")
		if self._cell_b is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_b>%e</cell_b>\n' % self._cell_b))
		else:
			warnEmptyAttribute("cell_b", "float")
		if self._cell_c is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_c>%e</cell_c>\n' % self._cell_c))
		else:
			warnEmptyAttribute("cell_c", "float")
		if self._cell_alpha is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_alpha>%e</cell_alpha>\n' % self._cell_alpha))
		else:
			warnEmptyAttribute("cell_alpha", "float")
		if self._cell_beta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_beta>%e</cell_beta>\n' % self._cell_beta))
		else:
			warnEmptyAttribute("cell_beta", "float")
		if self._cell_gamma is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<cell_gamma>%e</cell_gamma>\n' % self._cell_gamma))
		else:
			warnEmptyAttribute("cell_gamma", "float")
		if self._anomalous is not None:
			showIndent(outfile, level)
			if self._anomalous:
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
				self._startImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'endImageNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._endImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedDetectorDistance':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._refinedDetectorDistance = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedXbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._refinedXbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedYbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._refinedYbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rotationAxisX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rotationAxisY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisZ':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rotationAxisZ = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._beamVectorX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._beamVectorY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamVectorZ':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._beamVectorZ = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_a':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_a = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_b':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_b = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_c':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_c = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_alpha':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_alpha = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_beta':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_beta = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_gamma':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._cell_gamma = fval_
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
				self._anomalous = ival_
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
		self._Image = Image
		checkType("AutoProcIntegrationContainer", "Constructor of AutoProcIntegrationContainer", AutoProcIntegration, "AutoProcIntegration")
		self._AutoProcIntegration = AutoProcIntegration
	def getImage(self): return self._Image
	def setImage(self, Image):
		checkType("AutoProcIntegrationContainer", "setImage", Image, "Image")
		self._Image = Image
	def delImage(self): self._Image = None
	# Properties
	Image = property(getImage, setImage, delImage, "Property for Image")
	def getAutoProcIntegration(self): return self._AutoProcIntegration
	def setAutoProcIntegration(self, AutoProcIntegration):
		checkType("AutoProcIntegrationContainer", "setAutoProcIntegration", AutoProcIntegration, "AutoProcIntegration")
		self._AutoProcIntegration = AutoProcIntegration
	def delAutoProcIntegration(self): self._AutoProcIntegration = None
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
		if self._Image is not None:
			self.Image.export(outfile, level, name_='Image')
		else:
			warnEmptyAttribute("Image", "Image")
		if self._AutoProcIntegration is not None:
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
		self._processingCommandLine = processingCommandLine
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingPrograms, "string")
		self._processingPrograms = processingPrograms
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingStatus, "boolean")
		self._processingStatus = processingStatus
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingMessage, "string")
		self._processingMessage = processingMessage
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingStartTime, "string")
		self._processingStartTime = processingStartTime
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingEndTime, "string")
		self._processingEndTime = processingEndTime
		checkType("AutoProcProgram", "Constructor of AutoProcProgram", processingEnvironment, "string")
		self._processingEnvironment = processingEnvironment
	def getProcessingCommandLine(self): return self._processingCommandLine
	def setProcessingCommandLine(self, processingCommandLine):
		checkType("AutoProcProgram", "setProcessingCommandLine", processingCommandLine, "string")
		self._processingCommandLine = processingCommandLine
	def delProcessingCommandLine(self): self._processingCommandLine = None
	# Properties
	processingCommandLine = property(getProcessingCommandLine, setProcessingCommandLine, delProcessingCommandLine, "Property for processingCommandLine")
	def getProcessingPrograms(self): return self._processingPrograms
	def setProcessingPrograms(self, processingPrograms):
		checkType("AutoProcProgram", "setProcessingPrograms", processingPrograms, "string")
		self._processingPrograms = processingPrograms
	def delProcessingPrograms(self): self._processingPrograms = None
	# Properties
	processingPrograms = property(getProcessingPrograms, setProcessingPrograms, delProcessingPrograms, "Property for processingPrograms")
	def getProcessingStatus(self): return self._processingStatus
	def setProcessingStatus(self, processingStatus):
		checkType("AutoProcProgram", "setProcessingStatus", processingStatus, "boolean")
		self._processingStatus = processingStatus
	def delProcessingStatus(self): self._processingStatus = None
	# Properties
	processingStatus = property(getProcessingStatus, setProcessingStatus, delProcessingStatus, "Property for processingStatus")
	def getProcessingMessage(self): return self._processingMessage
	def setProcessingMessage(self, processingMessage):
		checkType("AutoProcProgram", "setProcessingMessage", processingMessage, "string")
		self._processingMessage = processingMessage
	def delProcessingMessage(self): self._processingMessage = None
	# Properties
	processingMessage = property(getProcessingMessage, setProcessingMessage, delProcessingMessage, "Property for processingMessage")
	def getProcessingStartTime(self): return self._processingStartTime
	def setProcessingStartTime(self, processingStartTime):
		checkType("AutoProcProgram", "setProcessingStartTime", processingStartTime, "string")
		self._processingStartTime = processingStartTime
	def delProcessingStartTime(self): self._processingStartTime = None
	# Properties
	processingStartTime = property(getProcessingStartTime, setProcessingStartTime, delProcessingStartTime, "Property for processingStartTime")
	def getProcessingEndTime(self): return self._processingEndTime
	def setProcessingEndTime(self, processingEndTime):
		checkType("AutoProcProgram", "setProcessingEndTime", processingEndTime, "string")
		self._processingEndTime = processingEndTime
	def delProcessingEndTime(self): self._processingEndTime = None
	# Properties
	processingEndTime = property(getProcessingEndTime, setProcessingEndTime, delProcessingEndTime, "Property for processingEndTime")
	def getProcessingEnvironment(self): return self._processingEnvironment
	def setProcessingEnvironment(self, processingEnvironment):
		checkType("AutoProcProgram", "setProcessingEnvironment", processingEnvironment, "string")
		self._processingEnvironment = processingEnvironment
	def delProcessingEnvironment(self): self._processingEnvironment = None
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
		if self._processingCommandLine is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingCommandLine>%s</processingCommandLine>\n' % self._processingCommandLine))
		else:
			warnEmptyAttribute("processingCommandLine", "string")
		if self._processingPrograms is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingPrograms>%s</processingPrograms>\n' % self._processingPrograms))
		else:
			warnEmptyAttribute("processingPrograms", "string")
		if self._processingStatus is not None:
			showIndent(outfile, level)
			if self._processingStatus:
				outfile.write(unicode('<processingStatus>true</processingStatus>\n'))
			else:
				outfile.write(unicode('<processingStatus>false</processingStatus>\n'))
		else:
			warnEmptyAttribute("processingStatus", "boolean")
		if self._processingMessage is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingMessage>%s</processingMessage>\n' % self._processingMessage))
		else:
			warnEmptyAttribute("processingMessage", "string")
		if self._processingStartTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingStartTime>%s</processingStartTime>\n' % self._processingStartTime))
		else:
			warnEmptyAttribute("processingStartTime", "string")
		if self._processingEndTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingEndTime>%s</processingEndTime>\n' % self._processingEndTime))
		else:
			warnEmptyAttribute("processingEndTime", "string")
		if self._processingEnvironment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<processingEnvironment>%s</processingEnvironment>\n' % self._processingEnvironment))
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
			self._processingCommandLine = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingPrograms':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._processingPrograms = value_
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
				self._processingStatus = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingMessage':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._processingMessage = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingStartTime':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._processingStartTime = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingEndTime':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._processingEndTime = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processingEnvironment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._processingEnvironment = value_
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
		self._fileType = fileType
		checkType("AutoProcProgramAttachment", "Constructor of AutoProcProgramAttachment", fileName, "string")
		self._fileName = fileName
		checkType("AutoProcProgramAttachment", "Constructor of AutoProcProgramAttachment", filePath, "string")
		self._filePath = filePath
	def getFileType(self): return self._fileType
	def setFileType(self, fileType):
		checkType("AutoProcProgramAttachment", "setFileType", fileType, "string")
		self._fileType = fileType
	def delFileType(self): self._fileType = None
	# Properties
	fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
	def getFileName(self): return self._fileName
	def setFileName(self, fileName):
		checkType("AutoProcProgramAttachment", "setFileName", fileName, "string")
		self._fileName = fileName
	def delFileName(self): self._fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFilePath(self): return self._filePath
	def setFilePath(self, filePath):
		checkType("AutoProcProgramAttachment", "setFilePath", filePath, "string")
		self._filePath = filePath
	def delFilePath(self): self._filePath = None
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
		if self._fileType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileType>%s</fileType>\n' % self._fileType))
		else:
			warnEmptyAttribute("fileType", "string")
		if self._fileName is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileName>%s</fileName>\n' % self._fileName))
		else:
			warnEmptyAttribute("fileName", "string")
		if self._filePath is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<filePath>%s</filePath>\n' % self._filePath))
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
			self._fileType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._fileName = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'filePath':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._filePath = value_
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
		self._AutoProcProgram = AutoProcProgram
		if AutoProcProgramAttachment is None:
			self._AutoProcProgramAttachment = []
		else:
			checkType("AutoProcProgramContainer", "Constructor of AutoProcProgramContainer", AutoProcProgramAttachment, "list")
			self._AutoProcProgramAttachment = AutoProcProgramAttachment
	def getAutoProcProgram(self): return self._AutoProcProgram
	def setAutoProcProgram(self, AutoProcProgram):
		checkType("AutoProcProgramContainer", "setAutoProcProgram", AutoProcProgram, "AutoProcProgram")
		self._AutoProcProgram = AutoProcProgram
	def delAutoProcProgram(self): self._AutoProcProgram = None
	# Properties
	AutoProcProgram = property(getAutoProcProgram, setAutoProcProgram, delAutoProcProgram, "Property for AutoProcProgram")
	def getAutoProcProgramAttachment(self): return self._AutoProcProgramAttachment
	def setAutoProcProgramAttachment(self, AutoProcProgramAttachment):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", AutoProcProgramAttachment, "list")
		self._AutoProcProgramAttachment = AutoProcProgramAttachment
	def delAutoProcProgramAttachment(self): self._AutoProcProgramAttachment = None
	# Properties
	AutoProcProgramAttachment = property(getAutoProcProgramAttachment, setAutoProcProgramAttachment, delAutoProcProgramAttachment, "Property for AutoProcProgramAttachment")
	def addAutoProcProgramAttachment(self, value):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", value, "AutoProcProgramAttachment")
		self._AutoProcProgramAttachment.append(value)
	def insertAutoProcProgramAttachment(self, index, value):
		checkType("AutoProcProgramContainer", "setAutoProcProgramAttachment", value, "AutoProcProgramAttachment")
		self._AutoProcProgramAttachment[index] = value
	def export(self, outfile, level, name_='AutoProcProgramContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='AutoProcProgramContainer'):
		pass
		if self._AutoProcProgram is not None:
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
		self._recordTimeStamp = recordTimeStamp
	def getRecordTimeStamp(self): return self._recordTimeStamp
	def setRecordTimeStamp(self, recordTimeStamp):
		checkType("AutoProcScaling", "setRecordTimeStamp", recordTimeStamp, "string")
		self._recordTimeStamp = recordTimeStamp
	def delRecordTimeStamp(self): self._recordTimeStamp = None
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
		if self._recordTimeStamp is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<recordTimeStamp>%s</recordTimeStamp>\n' % self._recordTimeStamp))
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
			self._recordTimeStamp = value_
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
		self._scalingStatisticsType = scalingStatisticsType
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", comments, "string")
		self._comments = comments
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", resolutionLimitLow, "float")
		self._resolutionLimitLow = resolutionLimitLow
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", resolutionLimitHigh, "float")
		self._resolutionLimitHigh = resolutionLimitHigh
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rMerge, "float")
		self._rMerge = rMerge
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rmeasWithinIplusIminus, "float")
		self._rmeasWithinIplusIminus = rmeasWithinIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rmeasAllIplusIminus, "float")
		self._rmeasAllIplusIminus = rmeasAllIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rpimWithinIplusIminus, "float")
		self._rpimWithinIplusIminus = rpimWithinIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", rpimAllIplusIminus, "float")
		self._rpimAllIplusIminus = rpimAllIplusIminus
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", fractionalPartialBias, "float")
		self._fractionalPartialBias = fractionalPartialBias
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", nTotalObservations, "integer")
		self._nTotalObservations = nTotalObservations
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", ntotalUniqueObservations, "integer")
		self._ntotalUniqueObservations = ntotalUniqueObservations
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", meanIOverSigI, "float")
		self._meanIOverSigI = meanIOverSigI
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", completeness, "float")
		self._completeness = completeness
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", multiplicity, "float")
		self._multiplicity = multiplicity
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalousCompleteness, "float")
		self._anomalousCompleteness = anomalousCompleteness
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalousMultiplicity, "float")
		self._anomalousMultiplicity = anomalousMultiplicity
		checkType("AutoProcScalingStatistics", "Constructor of AutoProcScalingStatistics", anomalous, "boolean")
		self._anomalous = anomalous
	def getScalingStatisticsType(self): return self._scalingStatisticsType
	def setScalingStatisticsType(self, scalingStatisticsType):
		checkType("AutoProcScalingStatistics", "setScalingStatisticsType", scalingStatisticsType, "string")
		self._scalingStatisticsType = scalingStatisticsType
	def delScalingStatisticsType(self): self._scalingStatisticsType = None
	# Properties
	scalingStatisticsType = property(getScalingStatisticsType, setScalingStatisticsType, delScalingStatisticsType, "Property for scalingStatisticsType")
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("AutoProcScalingStatistics", "setComments", comments, "string")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getResolutionLimitLow(self): return self._resolutionLimitLow
	def setResolutionLimitLow(self, resolutionLimitLow):
		checkType("AutoProcScalingStatistics", "setResolutionLimitLow", resolutionLimitLow, "float")
		self._resolutionLimitLow = resolutionLimitLow
	def delResolutionLimitLow(self): self._resolutionLimitLow = None
	# Properties
	resolutionLimitLow = property(getResolutionLimitLow, setResolutionLimitLow, delResolutionLimitLow, "Property for resolutionLimitLow")
	def getResolutionLimitHigh(self): return self._resolutionLimitHigh
	def setResolutionLimitHigh(self, resolutionLimitHigh):
		checkType("AutoProcScalingStatistics", "setResolutionLimitHigh", resolutionLimitHigh, "float")
		self._resolutionLimitHigh = resolutionLimitHigh
	def delResolutionLimitHigh(self): self._resolutionLimitHigh = None
	# Properties
	resolutionLimitHigh = property(getResolutionLimitHigh, setResolutionLimitHigh, delResolutionLimitHigh, "Property for resolutionLimitHigh")
	def getRMerge(self): return self._rMerge
	def setRMerge(self, rMerge):
		checkType("AutoProcScalingStatistics", "setRMerge", rMerge, "float")
		self._rMerge = rMerge
	def delRMerge(self): self._rMerge = None
	# Properties
	rMerge = property(getRMerge, setRMerge, delRMerge, "Property for rMerge")
	def getRmeasWithinIplusIminus(self): return self._rmeasWithinIplusIminus
	def setRmeasWithinIplusIminus(self, rmeasWithinIplusIminus):
		checkType("AutoProcScalingStatistics", "setRmeasWithinIplusIminus", rmeasWithinIplusIminus, "float")
		self._rmeasWithinIplusIminus = rmeasWithinIplusIminus
	def delRmeasWithinIplusIminus(self): self._rmeasWithinIplusIminus = None
	# Properties
	rmeasWithinIplusIminus = property(getRmeasWithinIplusIminus, setRmeasWithinIplusIminus, delRmeasWithinIplusIminus, "Property for rmeasWithinIplusIminus")
	def getRmeasAllIplusIminus(self): return self._rmeasAllIplusIminus
	def setRmeasAllIplusIminus(self, rmeasAllIplusIminus):
		checkType("AutoProcScalingStatistics", "setRmeasAllIplusIminus", rmeasAllIplusIminus, "float")
		self._rmeasAllIplusIminus = rmeasAllIplusIminus
	def delRmeasAllIplusIminus(self): self._rmeasAllIplusIminus = None
	# Properties
	rmeasAllIplusIminus = property(getRmeasAllIplusIminus, setRmeasAllIplusIminus, delRmeasAllIplusIminus, "Property for rmeasAllIplusIminus")
	def getRpimWithinIplusIminus(self): return self._rpimWithinIplusIminus
	def setRpimWithinIplusIminus(self, rpimWithinIplusIminus):
		checkType("AutoProcScalingStatistics", "setRpimWithinIplusIminus", rpimWithinIplusIminus, "float")
		self._rpimWithinIplusIminus = rpimWithinIplusIminus
	def delRpimWithinIplusIminus(self): self._rpimWithinIplusIminus = None
	# Properties
	rpimWithinIplusIminus = property(getRpimWithinIplusIminus, setRpimWithinIplusIminus, delRpimWithinIplusIminus, "Property for rpimWithinIplusIminus")
	def getRpimAllIplusIminus(self): return self._rpimAllIplusIminus
	def setRpimAllIplusIminus(self, rpimAllIplusIminus):
		checkType("AutoProcScalingStatistics", "setRpimAllIplusIminus", rpimAllIplusIminus, "float")
		self._rpimAllIplusIminus = rpimAllIplusIminus
	def delRpimAllIplusIminus(self): self._rpimAllIplusIminus = None
	# Properties
	rpimAllIplusIminus = property(getRpimAllIplusIminus, setRpimAllIplusIminus, delRpimAllIplusIminus, "Property for rpimAllIplusIminus")
	def getFractionalPartialBias(self): return self._fractionalPartialBias
	def setFractionalPartialBias(self, fractionalPartialBias):
		checkType("AutoProcScalingStatistics", "setFractionalPartialBias", fractionalPartialBias, "float")
		self._fractionalPartialBias = fractionalPartialBias
	def delFractionalPartialBias(self): self._fractionalPartialBias = None
	# Properties
	fractionalPartialBias = property(getFractionalPartialBias, setFractionalPartialBias, delFractionalPartialBias, "Property for fractionalPartialBias")
	def getNTotalObservations(self): return self._nTotalObservations
	def setNTotalObservations(self, nTotalObservations):
		checkType("AutoProcScalingStatistics", "setNTotalObservations", nTotalObservations, "integer")
		self._nTotalObservations = nTotalObservations
	def delNTotalObservations(self): self._nTotalObservations = None
	# Properties
	nTotalObservations = property(getNTotalObservations, setNTotalObservations, delNTotalObservations, "Property for nTotalObservations")
	def getNtotalUniqueObservations(self): return self._ntotalUniqueObservations
	def setNtotalUniqueObservations(self, ntotalUniqueObservations):
		checkType("AutoProcScalingStatistics", "setNtotalUniqueObservations", ntotalUniqueObservations, "integer")
		self._ntotalUniqueObservations = ntotalUniqueObservations
	def delNtotalUniqueObservations(self): self._ntotalUniqueObservations = None
	# Properties
	ntotalUniqueObservations = property(getNtotalUniqueObservations, setNtotalUniqueObservations, delNtotalUniqueObservations, "Property for ntotalUniqueObservations")
	def getMeanIOverSigI(self): return self._meanIOverSigI
	def setMeanIOverSigI(self, meanIOverSigI):
		checkType("AutoProcScalingStatistics", "setMeanIOverSigI", meanIOverSigI, "float")
		self._meanIOverSigI = meanIOverSigI
	def delMeanIOverSigI(self): self._meanIOverSigI = None
	# Properties
	meanIOverSigI = property(getMeanIOverSigI, setMeanIOverSigI, delMeanIOverSigI, "Property for meanIOverSigI")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("AutoProcScalingStatistics", "setCompleteness", completeness, "float")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self._multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("AutoProcScalingStatistics", "setMultiplicity", multiplicity, "float")
		self._multiplicity = multiplicity
	def delMultiplicity(self): self._multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getAnomalousCompleteness(self): return self._anomalousCompleteness
	def setAnomalousCompleteness(self, anomalousCompleteness):
		checkType("AutoProcScalingStatistics", "setAnomalousCompleteness", anomalousCompleteness, "float")
		self._anomalousCompleteness = anomalousCompleteness
	def delAnomalousCompleteness(self): self._anomalousCompleteness = None
	# Properties
	anomalousCompleteness = property(getAnomalousCompleteness, setAnomalousCompleteness, delAnomalousCompleteness, "Property for anomalousCompleteness")
	def getAnomalousMultiplicity(self): return self._anomalousMultiplicity
	def setAnomalousMultiplicity(self, anomalousMultiplicity):
		checkType("AutoProcScalingStatistics", "setAnomalousMultiplicity", anomalousMultiplicity, "float")
		self._anomalousMultiplicity = anomalousMultiplicity
	def delAnomalousMultiplicity(self): self._anomalousMultiplicity = None
	# Properties
	anomalousMultiplicity = property(getAnomalousMultiplicity, setAnomalousMultiplicity, delAnomalousMultiplicity, "Property for anomalousMultiplicity")
	def getAnomalous(self): return self._anomalous
	def setAnomalous(self, anomalous):
		checkType("AutoProcScalingStatistics", "setAnomalous", anomalous, "boolean")
		self._anomalous = anomalous
	def delAnomalous(self): self._anomalous = None
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
		if self._scalingStatisticsType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<scalingStatisticsType>%s</scalingStatisticsType>\n' % self._scalingStatisticsType))
		else:
			warnEmptyAttribute("scalingStatisticsType", "string")
		if self._comments is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
		else:
			warnEmptyAttribute("comments", "string")
		if self._resolutionLimitLow is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionLimitLow>%e</resolutionLimitLow>\n' % self._resolutionLimitLow))
		else:
			warnEmptyAttribute("resolutionLimitLow", "float")
		if self._resolutionLimitHigh is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionLimitHigh>%e</resolutionLimitHigh>\n' % self._resolutionLimitHigh))
		else:
			warnEmptyAttribute("resolutionLimitHigh", "float")
		if self._rMerge is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rMerge>%e</rMerge>\n' % self._rMerge))
		else:
			warnEmptyAttribute("rMerge", "float")
		if self._rmeasWithinIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rmeasWithinIplusIminus>%e</rmeasWithinIplusIminus>\n' % self._rmeasWithinIplusIminus))
		else:
			warnEmptyAttribute("rmeasWithinIplusIminus", "float")
		if self._rmeasAllIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rmeasAllIplusIminus>%e</rmeasAllIplusIminus>\n' % self._rmeasAllIplusIminus))
		else:
			warnEmptyAttribute("rmeasAllIplusIminus", "float")
		if self._rpimWithinIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rpimWithinIplusIminus>%e</rpimWithinIplusIminus>\n' % self._rpimWithinIplusIminus))
		else:
			warnEmptyAttribute("rpimWithinIplusIminus", "float")
		if self._rpimAllIplusIminus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rpimAllIplusIminus>%e</rpimAllIplusIminus>\n' % self._rpimAllIplusIminus))
		else:
			warnEmptyAttribute("rpimAllIplusIminus", "float")
		if self._fractionalPartialBias is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fractionalPartialBias>%e</fractionalPartialBias>\n' % self._fractionalPartialBias))
		else:
			warnEmptyAttribute("fractionalPartialBias", "float")
		if self._nTotalObservations is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<nTotalObservations>%d</nTotalObservations>\n' % self._nTotalObservations))
		else:
			warnEmptyAttribute("nTotalObservations", "integer")
		if self._ntotalUniqueObservations is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ntotalUniqueObservations>%d</ntotalUniqueObservations>\n' % self._ntotalUniqueObservations))
		else:
			warnEmptyAttribute("ntotalUniqueObservations", "integer")
		if self._meanIOverSigI is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<meanIOverSigI>%e</meanIOverSigI>\n' % self._meanIOverSigI))
		else:
			warnEmptyAttribute("meanIOverSigI", "float")
		if self._completeness is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<completeness>%e</completeness>\n' % self._completeness))
		else:
			warnEmptyAttribute("completeness", "float")
		if self._multiplicity is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<multiplicity>%e</multiplicity>\n' % self._multiplicity))
		else:
			warnEmptyAttribute("multiplicity", "float")
		if self._anomalousCompleteness is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<anomalousCompleteness>%e</anomalousCompleteness>\n' % self._anomalousCompleteness))
		else:
			warnEmptyAttribute("anomalousCompleteness", "float")
		if self._anomalousMultiplicity is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<anomalousMultiplicity>%e</anomalousMultiplicity>\n' % self._anomalousMultiplicity))
		else:
			warnEmptyAttribute("anomalousMultiplicity", "float")
		if self._anomalous is not None:
			showIndent(outfile, level)
			if self._anomalous:
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
			self._scalingStatisticsType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._comments = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionLimitLow':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._resolutionLimitLow = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionLimitHigh':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._resolutionLimitHigh = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMerge':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rMerge = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmeasWithinIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rmeasWithinIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmeasAllIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rmeasAllIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rpimWithinIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rpimWithinIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rpimAllIplusIminus':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._rpimAllIplusIminus = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fractionalPartialBias':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._fractionalPartialBias = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nTotalObservations':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._nTotalObservations = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ntotalUniqueObservations':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._ntotalUniqueObservations = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'meanIOverSigI':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._meanIOverSigI = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._completeness = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._multiplicity = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousCompleteness':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._anomalousCompleteness = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousMultiplicity':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._anomalousMultiplicity = fval_
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
				self._anomalous = ival_
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
		self._AutoProcScaling = AutoProcScaling
		if AutoProcScalingStatistics is None:
			self._AutoProcScalingStatistics = []
		else:
			checkType("AutoProcScalingContainer", "Constructor of AutoProcScalingContainer", AutoProcScalingStatistics, "list")
			self._AutoProcScalingStatistics = AutoProcScalingStatistics
		checkType("AutoProcScalingContainer", "Constructor of AutoProcScalingContainer", AutoProcIntegrationContainer, "AutoProcIntegrationContainer")
		self._AutoProcIntegrationContainer = AutoProcIntegrationContainer
	def getAutoProcScaling(self): return self._AutoProcScaling
	def setAutoProcScaling(self, AutoProcScaling):
		checkType("AutoProcScalingContainer", "setAutoProcScaling", AutoProcScaling, "AutoProcScaling")
		self._AutoProcScaling = AutoProcScaling
	def delAutoProcScaling(self): self._AutoProcScaling = None
	# Properties
	AutoProcScaling = property(getAutoProcScaling, setAutoProcScaling, delAutoProcScaling, "Property for AutoProcScaling")
	def getAutoProcScalingStatistics(self): return self._AutoProcScalingStatistics
	def setAutoProcScalingStatistics(self, AutoProcScalingStatistics):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", AutoProcScalingStatistics, "list")
		self._AutoProcScalingStatistics = AutoProcScalingStatistics
	def delAutoProcScalingStatistics(self): self._AutoProcScalingStatistics = None
	# Properties
	AutoProcScalingStatistics = property(getAutoProcScalingStatistics, setAutoProcScalingStatistics, delAutoProcScalingStatistics, "Property for AutoProcScalingStatistics")
	def addAutoProcScalingStatistics(self, value):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", value, "AutoProcScalingStatistics")
		self._AutoProcScalingStatistics.append(value)
	def insertAutoProcScalingStatistics(self, index, value):
		checkType("AutoProcScalingContainer", "setAutoProcScalingStatistics", value, "AutoProcScalingStatistics")
		self._AutoProcScalingStatistics[index] = value
	def getAutoProcIntegrationContainer(self): return self._AutoProcIntegrationContainer
	def setAutoProcIntegrationContainer(self, AutoProcIntegrationContainer):
		checkType("AutoProcScalingContainer", "setAutoProcIntegrationContainer", AutoProcIntegrationContainer, "AutoProcIntegrationContainer")
		self._AutoProcIntegrationContainer = AutoProcIntegrationContainer
	def delAutoProcIntegrationContainer(self): self._AutoProcIntegrationContainer = None
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
		if self._AutoProcScaling is not None:
			self.AutoProcScaling.export(outfile, level, name_='AutoProcScaling')
		else:
			warnEmptyAttribute("AutoProcScaling", "AutoProcScaling")
		for AutoProcScalingStatistics_ in self.getAutoProcScalingStatistics():
			AutoProcScalingStatistics_.export(outfile, level, name_='AutoProcScalingStatistics')
		if self.getAutoProcScalingStatistics() == []:
			warnEmptyAttribute("AutoProcScalingStatistics", "AutoProcScalingStatistics")
		if self._AutoProcIntegrationContainer is not None:
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
		self._dataCollectionId = dataCollectionId
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("Image", "setDataCollectionId", dataCollectionId, "integer")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
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
		if self._dataCollectionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
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
				self._dataCollectionId = ival_
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
		self._dataCollectionId = dataCollectionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", blSampleId, "integer")
		self._blSampleId = blSampleId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", sessionId, "integer")
		self._sessionId = sessionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", experimentType, "string")
		self._experimentType = experimentType
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", dataCollectionNumber, "integer")
		self._dataCollectionNumber = dataCollectionNumber
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", startDate, "string")
		self._startDate = startDate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", endDate, "string")
		self._endDate = endDate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", runStatus, "string")
		self._runStatus = runStatus
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", rotationAxis, "string")
		self._rotationAxis = rotationAxis
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", phiStart, "float")
		self._phiStart = phiStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", kappaStart, "float")
		self._kappaStart = kappaStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", omegaStart, "float")
		self._omegaStart = omegaStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisStart, "float")
		self._axisStart = axisStart
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisEnd, "float")
		self._axisEnd = axisEnd
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", axisRange, "float")
		self._axisRange = axisRange
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", overlap, "float")
		self._overlap = overlap
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", numberOfImages, "integer")
		self._numberOfImages = numberOfImages
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", startImageNumber, "integer")
		self._startImageNumber = startImageNumber
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", numberOfPasses, "integer")
		self._numberOfPasses = numberOfPasses
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", exposureTime, "float")
		self._exposureTime = exposureTime
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imageDirectory, "string")
		self._imageDirectory = imageDirectory
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imagePrefix, "string")
		self._imagePrefix = imagePrefix
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imageSuffix, "string")
		self._imageSuffix = imageSuffix
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", fileTemplate, "string")
		self._fileTemplate = fileTemplate
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", wavelength, "float")
		self._wavelength = wavelength
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", resolution, "float")
		self._resolution = resolution
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", resolutionAtCorner, "float")
		self._resolutionAtCorner = resolutionAtCorner
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detectorDistance, "float")
		self._detectorDistance = detectorDistance
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detector2theta, "float")
		self._detector2theta = detector2theta
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", detectorMode, "string")
		self._detectorMode = detectorMode
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap1, "float")
		self._undulatorGap1 = undulatorGap1
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap2, "float")
		self._undulatorGap2 = undulatorGap2
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", undulatorGap3, "float")
		self._undulatorGap3 = undulatorGap3
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xbeam, "float")
		self._xbeam = xbeam
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", ybeam, "float")
		self._ybeam = ybeam
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", crystalClass, "string")
		self._crystalClass = crystalClass
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", slitGapVertical, "float")
		self._slitGapVertical = slitGapVertical
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", slitGapHorizontal, "float")
		self._slitGapHorizontal = slitGapHorizontal
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamSizeAtSampleX, "float")
		self._beamSizeAtSampleX = beamSizeAtSampleX
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamSizeAtSampleY, "float")
		self._beamSizeAtSampleY = beamSizeAtSampleY
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", transmission, "float")
		self._transmission = transmission
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", synchrotronMode, "string")
		self._synchrotronMode = synchrotronMode
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", centeringMethod, "string")
		self._centeringMethod = centeringMethod
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", averageTemperature, "float")
		self._averageTemperature = averageTemperature
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", comments, "string")
		self._comments = comments
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", printableForReport, "boolean")
		self._printableForReport = printableForReport
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath1, "string")
		self._xtalSnapshotFullPath1 = xtalSnapshotFullPath1
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath2, "string")
		self._xtalSnapshotFullPath2 = xtalSnapshotFullPath2
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath3, "string")
		self._xtalSnapshotFullPath3 = xtalSnapshotFullPath3
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", xtalSnapshotFullPath4, "string")
		self._xtalSnapshotFullPath4 = xtalSnapshotFullPath4
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", beamShape, "string")
		self._beamShape = beamShape
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBDataCollection", "setDataCollectionId", dataCollectionId, "integer")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getBlSampleId(self): return self._blSampleId
	def setBlSampleId(self, blSampleId):
		checkType("XSDataISPyBDataCollection", "setBlSampleId", blSampleId, "integer")
		self._blSampleId = blSampleId
	def delBlSampleId(self): self._blSampleId = None
	# Properties
	blSampleId = property(getBlSampleId, setBlSampleId, delBlSampleId, "Property for blSampleId")
	def getSessionId(self): return self._sessionId
	def setSessionId(self, sessionId):
		checkType("XSDataISPyBDataCollection", "setSessionId", sessionId, "integer")
		self._sessionId = sessionId
	def delSessionId(self): self._sessionId = None
	# Properties
	sessionId = property(getSessionId, setSessionId, delSessionId, "Property for sessionId")
	def getExperimentType(self): return self._experimentType
	def setExperimentType(self, experimentType):
		checkType("XSDataISPyBDataCollection", "setExperimentType", experimentType, "string")
		self._experimentType = experimentType
	def delExperimentType(self): self._experimentType = None
	# Properties
	experimentType = property(getExperimentType, setExperimentType, delExperimentType, "Property for experimentType")
	def getDataCollectionNumber(self): return self._dataCollectionNumber
	def setDataCollectionNumber(self, dataCollectionNumber):
		checkType("XSDataISPyBDataCollection", "setDataCollectionNumber", dataCollectionNumber, "integer")
		self._dataCollectionNumber = dataCollectionNumber
	def delDataCollectionNumber(self): self._dataCollectionNumber = None
	# Properties
	dataCollectionNumber = property(getDataCollectionNumber, setDataCollectionNumber, delDataCollectionNumber, "Property for dataCollectionNumber")
	def getStartDate(self): return self._startDate
	def setStartDate(self, startDate):
		checkType("XSDataISPyBDataCollection", "setStartDate", startDate, "string")
		self._startDate = startDate
	def delStartDate(self): self._startDate = None
	# Properties
	startDate = property(getStartDate, setStartDate, delStartDate, "Property for startDate")
	def getEndDate(self): return self._endDate
	def setEndDate(self, endDate):
		checkType("XSDataISPyBDataCollection", "setEndDate", endDate, "string")
		self._endDate = endDate
	def delEndDate(self): self._endDate = None
	# Properties
	endDate = property(getEndDate, setEndDate, delEndDate, "Property for endDate")
	def getRunStatus(self): return self._runStatus
	def setRunStatus(self, runStatus):
		checkType("XSDataISPyBDataCollection", "setRunStatus", runStatus, "string")
		self._runStatus = runStatus
	def delRunStatus(self): self._runStatus = None
	# Properties
	runStatus = property(getRunStatus, setRunStatus, delRunStatus, "Property for runStatus")
	def getRotationAxis(self): return self._rotationAxis
	def setRotationAxis(self, rotationAxis):
		checkType("XSDataISPyBDataCollection", "setRotationAxis", rotationAxis, "string")
		self._rotationAxis = rotationAxis
	def delRotationAxis(self): self._rotationAxis = None
	# Properties
	rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
	def getPhiStart(self): return self._phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataISPyBDataCollection", "setPhiStart", phiStart, "float")
		self._phiStart = phiStart
	def delPhiStart(self): self._phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getKappaStart(self): return self._kappaStart
	def setKappaStart(self, kappaStart):
		checkType("XSDataISPyBDataCollection", "setKappaStart", kappaStart, "float")
		self._kappaStart = kappaStart
	def delKappaStart(self): self._kappaStart = None
	# Properties
	kappaStart = property(getKappaStart, setKappaStart, delKappaStart, "Property for kappaStart")
	def getOmegaStart(self): return self._omegaStart
	def setOmegaStart(self, omegaStart):
		checkType("XSDataISPyBDataCollection", "setOmegaStart", omegaStart, "float")
		self._omegaStart = omegaStart
	def delOmegaStart(self): self._omegaStart = None
	# Properties
	omegaStart = property(getOmegaStart, setOmegaStart, delOmegaStart, "Property for omegaStart")
	def getAxisStart(self): return self._axisStart
	def setAxisStart(self, axisStart):
		checkType("XSDataISPyBDataCollection", "setAxisStart", axisStart, "float")
		self._axisStart = axisStart
	def delAxisStart(self): self._axisStart = None
	# Properties
	axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
	def getAxisEnd(self): return self._axisEnd
	def setAxisEnd(self, axisEnd):
		checkType("XSDataISPyBDataCollection", "setAxisEnd", axisEnd, "float")
		self._axisEnd = axisEnd
	def delAxisEnd(self): self._axisEnd = None
	# Properties
	axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
	def getAxisRange(self): return self._axisRange
	def setAxisRange(self, axisRange):
		checkType("XSDataISPyBDataCollection", "setAxisRange", axisRange, "float")
		self._axisRange = axisRange
	def delAxisRange(self): self._axisRange = None
	# Properties
	axisRange = property(getAxisRange, setAxisRange, delAxisRange, "Property for axisRange")
	def getOverlap(self): return self._overlap
	def setOverlap(self, overlap):
		checkType("XSDataISPyBDataCollection", "setOverlap", overlap, "float")
		self._overlap = overlap
	def delOverlap(self): self._overlap = None
	# Properties
	overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
	def getNumberOfImages(self): return self._numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBDataCollection", "setNumberOfImages", numberOfImages, "integer")
		self._numberOfImages = numberOfImages
	def delNumberOfImages(self): self._numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getStartImageNumber(self): return self._startImageNumber
	def setStartImageNumber(self, startImageNumber):
		checkType("XSDataISPyBDataCollection", "setStartImageNumber", startImageNumber, "integer")
		self._startImageNumber = startImageNumber
	def delStartImageNumber(self): self._startImageNumber = None
	# Properties
	startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
	def getNumberOfPasses(self): return self._numberOfPasses
	def setNumberOfPasses(self, numberOfPasses):
		checkType("XSDataISPyBDataCollection", "setNumberOfPasses", numberOfPasses, "integer")
		self._numberOfPasses = numberOfPasses
	def delNumberOfPasses(self): self._numberOfPasses = None
	# Properties
	numberOfPasses = property(getNumberOfPasses, setNumberOfPasses, delNumberOfPasses, "Property for numberOfPasses")
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBDataCollection", "setExposureTime", exposureTime, "float")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getImageDirectory(self): return self._imageDirectory
	def setImageDirectory(self, imageDirectory):
		checkType("XSDataISPyBDataCollection", "setImageDirectory", imageDirectory, "string")
		self._imageDirectory = imageDirectory
	def delImageDirectory(self): self._imageDirectory = None
	# Properties
	imageDirectory = property(getImageDirectory, setImageDirectory, delImageDirectory, "Property for imageDirectory")
	def getImagePrefix(self): return self._imagePrefix
	def setImagePrefix(self, imagePrefix):
		checkType("XSDataISPyBDataCollection", "setImagePrefix", imagePrefix, "string")
		self._imagePrefix = imagePrefix
	def delImagePrefix(self): self._imagePrefix = None
	# Properties
	imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
	def getImageSuffix(self): return self._imageSuffix
	def setImageSuffix(self, imageSuffix):
		checkType("XSDataISPyBDataCollection", "setImageSuffix", imageSuffix, "string")
		self._imageSuffix = imageSuffix
	def delImageSuffix(self): self._imageSuffix = None
	# Properties
	imageSuffix = property(getImageSuffix, setImageSuffix, delImageSuffix, "Property for imageSuffix")
	def getFileTemplate(self): return self._fileTemplate
	def setFileTemplate(self, fileTemplate):
		checkType("XSDataISPyBDataCollection", "setFileTemplate", fileTemplate, "string")
		self._fileTemplate = fileTemplate
	def delFileTemplate(self): self._fileTemplate = None
	# Properties
	fileTemplate = property(getFileTemplate, setFileTemplate, delFileTemplate, "Property for fileTemplate")
	def getWavelength(self): return self._wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataISPyBDataCollection", "setWavelength", wavelength, "float")
		self._wavelength = wavelength
	def delWavelength(self): self._wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBDataCollection", "setResolution", resolution, "float")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolutionAtCorner(self): return self._resolutionAtCorner
	def setResolutionAtCorner(self, resolutionAtCorner):
		checkType("XSDataISPyBDataCollection", "setResolutionAtCorner", resolutionAtCorner, "float")
		self._resolutionAtCorner = resolutionAtCorner
	def delResolutionAtCorner(self): self._resolutionAtCorner = None
	# Properties
	resolutionAtCorner = property(getResolutionAtCorner, setResolutionAtCorner, delResolutionAtCorner, "Property for resolutionAtCorner")
	def getDetectorDistance(self): return self._detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataISPyBDataCollection", "setDetectorDistance", detectorDistance, "float")
		self._detectorDistance = detectorDistance
	def delDetectorDistance(self): self._detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getDetector2theta(self): return self._detector2theta
	def setDetector2theta(self, detector2theta):
		checkType("XSDataISPyBDataCollection", "setDetector2theta", detector2theta, "float")
		self._detector2theta = detector2theta
	def delDetector2theta(self): self._detector2theta = None
	# Properties
	detector2theta = property(getDetector2theta, setDetector2theta, delDetector2theta, "Property for detector2theta")
	def getDetectorMode(self): return self._detectorMode
	def setDetectorMode(self, detectorMode):
		checkType("XSDataISPyBDataCollection", "setDetectorMode", detectorMode, "string")
		self._detectorMode = detectorMode
	def delDetectorMode(self): self._detectorMode = None
	# Properties
	detectorMode = property(getDetectorMode, setDetectorMode, delDetectorMode, "Property for detectorMode")
	def getUndulatorGap1(self): return self._undulatorGap1
	def setUndulatorGap1(self, undulatorGap1):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap1", undulatorGap1, "float")
		self._undulatorGap1 = undulatorGap1
	def delUndulatorGap1(self): self._undulatorGap1 = None
	# Properties
	undulatorGap1 = property(getUndulatorGap1, setUndulatorGap1, delUndulatorGap1, "Property for undulatorGap1")
	def getUndulatorGap2(self): return self._undulatorGap2
	def setUndulatorGap2(self, undulatorGap2):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap2", undulatorGap2, "float")
		self._undulatorGap2 = undulatorGap2
	def delUndulatorGap2(self): self._undulatorGap2 = None
	# Properties
	undulatorGap2 = property(getUndulatorGap2, setUndulatorGap2, delUndulatorGap2, "Property for undulatorGap2")
	def getUndulatorGap3(self): return self._undulatorGap3
	def setUndulatorGap3(self, undulatorGap3):
		checkType("XSDataISPyBDataCollection", "setUndulatorGap3", undulatorGap3, "float")
		self._undulatorGap3 = undulatorGap3
	def delUndulatorGap3(self): self._undulatorGap3 = None
	# Properties
	undulatorGap3 = property(getUndulatorGap3, setUndulatorGap3, delUndulatorGap3, "Property for undulatorGap3")
	def getXbeam(self): return self._xbeam
	def setXbeam(self, xbeam):
		checkType("XSDataISPyBDataCollection", "setXbeam", xbeam, "float")
		self._xbeam = xbeam
	def delXbeam(self): self._xbeam = None
	# Properties
	xbeam = property(getXbeam, setXbeam, delXbeam, "Property for xbeam")
	def getYbeam(self): return self._ybeam
	def setYbeam(self, ybeam):
		checkType("XSDataISPyBDataCollection", "setYbeam", ybeam, "float")
		self._ybeam = ybeam
	def delYbeam(self): self._ybeam = None
	# Properties
	ybeam = property(getYbeam, setYbeam, delYbeam, "Property for ybeam")
	def getCrystalClass(self): return self._crystalClass
	def setCrystalClass(self, crystalClass):
		checkType("XSDataISPyBDataCollection", "setCrystalClass", crystalClass, "string")
		self._crystalClass = crystalClass
	def delCrystalClass(self): self._crystalClass = None
	# Properties
	crystalClass = property(getCrystalClass, setCrystalClass, delCrystalClass, "Property for crystalClass")
	def getSlitGapVertical(self): return self._slitGapVertical
	def setSlitGapVertical(self, slitGapVertical):
		checkType("XSDataISPyBDataCollection", "setSlitGapVertical", slitGapVertical, "float")
		self._slitGapVertical = slitGapVertical
	def delSlitGapVertical(self): self._slitGapVertical = None
	# Properties
	slitGapVertical = property(getSlitGapVertical, setSlitGapVertical, delSlitGapVertical, "Property for slitGapVertical")
	def getSlitGapHorizontal(self): return self._slitGapHorizontal
	def setSlitGapHorizontal(self, slitGapHorizontal):
		checkType("XSDataISPyBDataCollection", "setSlitGapHorizontal", slitGapHorizontal, "float")
		self._slitGapHorizontal = slitGapHorizontal
	def delSlitGapHorizontal(self): self._slitGapHorizontal = None
	# Properties
	slitGapHorizontal = property(getSlitGapHorizontal, setSlitGapHorizontal, delSlitGapHorizontal, "Property for slitGapHorizontal")
	def getBeamSizeAtSampleX(self): return self._beamSizeAtSampleX
	def setBeamSizeAtSampleX(self, beamSizeAtSampleX):
		checkType("XSDataISPyBDataCollection", "setBeamSizeAtSampleX", beamSizeAtSampleX, "float")
		self._beamSizeAtSampleX = beamSizeAtSampleX
	def delBeamSizeAtSampleX(self): self._beamSizeAtSampleX = None
	# Properties
	beamSizeAtSampleX = property(getBeamSizeAtSampleX, setBeamSizeAtSampleX, delBeamSizeAtSampleX, "Property for beamSizeAtSampleX")
	def getBeamSizeAtSampleY(self): return self._beamSizeAtSampleY
	def setBeamSizeAtSampleY(self, beamSizeAtSampleY):
		checkType("XSDataISPyBDataCollection", "setBeamSizeAtSampleY", beamSizeAtSampleY, "float")
		self._beamSizeAtSampleY = beamSizeAtSampleY
	def delBeamSizeAtSampleY(self): self._beamSizeAtSampleY = None
	# Properties
	beamSizeAtSampleY = property(getBeamSizeAtSampleY, setBeamSizeAtSampleY, delBeamSizeAtSampleY, "Property for beamSizeAtSampleY")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBDataCollection", "setTransmission", transmission, "float")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getSynchrotronMode(self): return self._synchrotronMode
	def setSynchrotronMode(self, synchrotronMode):
		checkType("XSDataISPyBDataCollection", "setSynchrotronMode", synchrotronMode, "string")
		self._synchrotronMode = synchrotronMode
	def delSynchrotronMode(self): self._synchrotronMode = None
	# Properties
	synchrotronMode = property(getSynchrotronMode, setSynchrotronMode, delSynchrotronMode, "Property for synchrotronMode")
	def getCenteringMethod(self): return self._centeringMethod
	def setCenteringMethod(self, centeringMethod):
		checkType("XSDataISPyBDataCollection", "setCenteringMethod", centeringMethod, "string")
		self._centeringMethod = centeringMethod
	def delCenteringMethod(self): self._centeringMethod = None
	# Properties
	centeringMethod = property(getCenteringMethod, setCenteringMethod, delCenteringMethod, "Property for centeringMethod")
	def getAverageTemperature(self): return self._averageTemperature
	def setAverageTemperature(self, averageTemperature):
		checkType("XSDataISPyBDataCollection", "setAverageTemperature", averageTemperature, "float")
		self._averageTemperature = averageTemperature
	def delAverageTemperature(self): self._averageTemperature = None
	# Properties
	averageTemperature = property(getAverageTemperature, setAverageTemperature, delAverageTemperature, "Property for averageTemperature")
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("XSDataISPyBDataCollection", "setComments", comments, "string")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getPrintableForReport(self): return self._printableForReport
	def setPrintableForReport(self, printableForReport):
		checkType("XSDataISPyBDataCollection", "setPrintableForReport", printableForReport, "boolean")
		self._printableForReport = printableForReport
	def delPrintableForReport(self): self._printableForReport = None
	# Properties
	printableForReport = property(getPrintableForReport, setPrintableForReport, delPrintableForReport, "Property for printableForReport")
	def getXtalSnapshotFullPath1(self): return self._xtalSnapshotFullPath1
	def setXtalSnapshotFullPath1(self, xtalSnapshotFullPath1):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath1", xtalSnapshotFullPath1, "string")
		self._xtalSnapshotFullPath1 = xtalSnapshotFullPath1
	def delXtalSnapshotFullPath1(self): self._xtalSnapshotFullPath1 = None
	# Properties
	xtalSnapshotFullPath1 = property(getXtalSnapshotFullPath1, setXtalSnapshotFullPath1, delXtalSnapshotFullPath1, "Property for xtalSnapshotFullPath1")
	def getXtalSnapshotFullPath2(self): return self._xtalSnapshotFullPath2
	def setXtalSnapshotFullPath2(self, xtalSnapshotFullPath2):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath2", xtalSnapshotFullPath2, "string")
		self._xtalSnapshotFullPath2 = xtalSnapshotFullPath2
	def delXtalSnapshotFullPath2(self): self._xtalSnapshotFullPath2 = None
	# Properties
	xtalSnapshotFullPath2 = property(getXtalSnapshotFullPath2, setXtalSnapshotFullPath2, delXtalSnapshotFullPath2, "Property for xtalSnapshotFullPath2")
	def getXtalSnapshotFullPath3(self): return self._xtalSnapshotFullPath3
	def setXtalSnapshotFullPath3(self, xtalSnapshotFullPath3):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath3", xtalSnapshotFullPath3, "string")
		self._xtalSnapshotFullPath3 = xtalSnapshotFullPath3
	def delXtalSnapshotFullPath3(self): self._xtalSnapshotFullPath3 = None
	# Properties
	xtalSnapshotFullPath3 = property(getXtalSnapshotFullPath3, setXtalSnapshotFullPath3, delXtalSnapshotFullPath3, "Property for xtalSnapshotFullPath3")
	def getXtalSnapshotFullPath4(self): return self._xtalSnapshotFullPath4
	def setXtalSnapshotFullPath4(self, xtalSnapshotFullPath4):
		checkType("XSDataISPyBDataCollection", "setXtalSnapshotFullPath4", xtalSnapshotFullPath4, "string")
		self._xtalSnapshotFullPath4 = xtalSnapshotFullPath4
	def delXtalSnapshotFullPath4(self): self._xtalSnapshotFullPath4 = None
	# Properties
	xtalSnapshotFullPath4 = property(getXtalSnapshotFullPath4, setXtalSnapshotFullPath4, delXtalSnapshotFullPath4, "Property for xtalSnapshotFullPath4")
	def getBeamShape(self): return self._beamShape
	def setBeamShape(self, beamShape):
		checkType("XSDataISPyBDataCollection", "setBeamShape", beamShape, "string")
		self._beamShape = beamShape
	def delBeamShape(self): self._beamShape = None
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
		if self._dataCollectionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
		else:
			warnEmptyAttribute("dataCollectionId", "integer")
		if self._blSampleId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<blSampleId>%d</blSampleId>\n' % self._blSampleId))
		else:
			warnEmptyAttribute("blSampleId", "integer")
		if self._sessionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<sessionId>%d</sessionId>\n' % self._sessionId))
		else:
			warnEmptyAttribute("sessionId", "integer")
		if self._experimentType is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<experimentType>%s</experimentType>\n' % self._experimentType))
		else:
			warnEmptyAttribute("experimentType", "string")
		if self._dataCollectionNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<dataCollectionNumber>%d</dataCollectionNumber>\n' % self._dataCollectionNumber))
		else:
			warnEmptyAttribute("dataCollectionNumber", "integer")
		if self._startDate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startDate>%s</startDate>\n' % self._startDate))
		else:
			warnEmptyAttribute("startDate", "string")
		if self._endDate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<endDate>%s</endDate>\n' % self._endDate))
		else:
			warnEmptyAttribute("endDate", "string")
		if self._runStatus is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<runStatus>%s</runStatus>\n' % self._runStatus))
		else:
			warnEmptyAttribute("runStatus", "string")
		if self._rotationAxis is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rotationAxis>%s</rotationAxis>\n' % self._rotationAxis))
		else:
			warnEmptyAttribute("rotationAxis", "string")
		if self._phiStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<phiStart>%e</phiStart>\n' % self._phiStart))
		else:
			warnEmptyAttribute("phiStart", "float")
		if self._kappaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<kappaStart>%e</kappaStart>\n' % self._kappaStart))
		else:
			warnEmptyAttribute("kappaStart", "float")
		if self._omegaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<omegaStart>%e</omegaStart>\n' % self._omegaStart))
		else:
			warnEmptyAttribute("omegaStart", "float")
		if self._axisStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisStart>%e</axisStart>\n' % self._axisStart))
		else:
			warnEmptyAttribute("axisStart", "float")
		if self._axisEnd is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisEnd>%e</axisEnd>\n' % self._axisEnd))
		else:
			warnEmptyAttribute("axisEnd", "float")
		if self._axisRange is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<axisRange>%e</axisRange>\n' % self._axisRange))
		else:
			warnEmptyAttribute("axisRange", "float")
		if self._overlap is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<overlap>%e</overlap>\n' % self._overlap))
		else:
			warnEmptyAttribute("overlap", "float")
		if self._numberOfImages is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<numberOfImages>%d</numberOfImages>\n' % self._numberOfImages))
		else:
			warnEmptyAttribute("numberOfImages", "integer")
		if self._startImageNumber is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self._startImageNumber))
		else:
			warnEmptyAttribute("startImageNumber", "integer")
		if self._numberOfPasses is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<numberOfPasses>%d</numberOfPasses>\n' % self._numberOfPasses))
		else:
			warnEmptyAttribute("numberOfPasses", "integer")
		if self._exposureTime is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<exposureTime>%e</exposureTime>\n' % self._exposureTime))
		else:
			warnEmptyAttribute("exposureTime", "float")
		if self._imageDirectory is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imageDirectory>%s</imageDirectory>\n' % self._imageDirectory))
		else:
			warnEmptyAttribute("imageDirectory", "string")
		if self._imagePrefix is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imagePrefix>%s</imagePrefix>\n' % self._imagePrefix))
		else:
			warnEmptyAttribute("imagePrefix", "string")
		if self._imageSuffix is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<imageSuffix>%s</imageSuffix>\n' % self._imageSuffix))
		else:
			warnEmptyAttribute("imageSuffix", "string")
		if self._fileTemplate is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileTemplate>%s</fileTemplate>\n' % self._fileTemplate))
		else:
			warnEmptyAttribute("fileTemplate", "string")
		if self._wavelength is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<wavelength>%e</wavelength>\n' % self._wavelength))
		else:
			warnEmptyAttribute("wavelength", "float")
		if self._resolution is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolution>%e</resolution>\n' % self._resolution))
		else:
			warnEmptyAttribute("resolution", "float")
		if self._resolutionAtCorner is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolutionAtCorner>%e</resolutionAtCorner>\n' % self._resolutionAtCorner))
		else:
			warnEmptyAttribute("resolutionAtCorner", "float")
		if self._detectorDistance is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detectorDistance>%e</detectorDistance>\n' % self._detectorDistance))
		else:
			warnEmptyAttribute("detectorDistance", "float")
		if self._detector2theta is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detector2theta>%e</detector2theta>\n' % self._detector2theta))
		else:
			warnEmptyAttribute("detector2theta", "float")
		if self._detectorMode is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detectorMode>%s</detectorMode>\n' % self._detectorMode))
		else:
			warnEmptyAttribute("detectorMode", "string")
		if self._undulatorGap1 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap1>%e</undulatorGap1>\n' % self._undulatorGap1))
		else:
			warnEmptyAttribute("undulatorGap1", "float")
		if self._undulatorGap2 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap2>%e</undulatorGap2>\n' % self._undulatorGap2))
		else:
			warnEmptyAttribute("undulatorGap2", "float")
		if self._undulatorGap3 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<undulatorGap3>%e</undulatorGap3>\n' % self._undulatorGap3))
		else:
			warnEmptyAttribute("undulatorGap3", "float")
		if self._xbeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xbeam>%e</xbeam>\n' % self._xbeam))
		else:
			warnEmptyAttribute("xbeam", "float")
		if self._ybeam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<ybeam>%e</ybeam>\n' % self._ybeam))
		else:
			warnEmptyAttribute("ybeam", "float")
		if self._crystalClass is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<crystalClass>%s</crystalClass>\n' % self._crystalClass))
		else:
			warnEmptyAttribute("crystalClass", "string")
		if self._slitGapVertical is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<slitGapVertical>%e</slitGapVertical>\n' % self._slitGapVertical))
		else:
			warnEmptyAttribute("slitGapVertical", "float")
		if self._slitGapHorizontal is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<slitGapHorizontal>%e</slitGapHorizontal>\n' % self._slitGapHorizontal))
		else:
			warnEmptyAttribute("slitGapHorizontal", "float")
		if self._beamSizeAtSampleX is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamSizeAtSampleX>%e</beamSizeAtSampleX>\n' % self._beamSizeAtSampleX))
		else:
			warnEmptyAttribute("beamSizeAtSampleX", "float")
		if self._beamSizeAtSampleY is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamSizeAtSampleY>%e</beamSizeAtSampleY>\n' % self._beamSizeAtSampleY))
		else:
			warnEmptyAttribute("beamSizeAtSampleY", "float")
		if self._transmission is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<transmission>%e</transmission>\n' % self._transmission))
		else:
			warnEmptyAttribute("transmission", "float")
		if self._synchrotronMode is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<synchrotronMode>%s</synchrotronMode>\n' % self._synchrotronMode))
		else:
			warnEmptyAttribute("synchrotronMode", "string")
		if self._centeringMethod is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<centeringMethod>%s</centeringMethod>\n' % self._centeringMethod))
		else:
			warnEmptyAttribute("centeringMethod", "string")
		if self._averageTemperature is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<averageTemperature>%e</averageTemperature>\n' % self._averageTemperature))
		else:
			warnEmptyAttribute("averageTemperature", "float")
		if self._comments is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
		else:
			warnEmptyAttribute("comments", "string")
		if self._printableForReport is not None:
			showIndent(outfile, level)
			if self._printableForReport:
				outfile.write(unicode('<printableForReport>true</printableForReport>\n'))
			else:
				outfile.write(unicode('<printableForReport>false</printableForReport>\n'))
		else:
			warnEmptyAttribute("printableForReport", "boolean")
		if self._xtalSnapshotFullPath1 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath1>%s</xtalSnapshotFullPath1>\n' % self._xtalSnapshotFullPath1))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath1", "string")
		if self._xtalSnapshotFullPath2 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath2>%s</xtalSnapshotFullPath2>\n' % self._xtalSnapshotFullPath2))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath2", "string")
		if self._xtalSnapshotFullPath3 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath3>%s</xtalSnapshotFullPath3>\n' % self._xtalSnapshotFullPath3))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath3", "string")
		if self._xtalSnapshotFullPath4 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<xtalSnapshotFullPath4>%s</xtalSnapshotFullPath4>\n' % self._xtalSnapshotFullPath4))
		else:
			warnEmptyAttribute("xtalSnapshotFullPath4", "string")
		if self._beamShape is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beamShape>%s</beamShape>\n' % self._beamShape))
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
				self._dataCollectionId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'blSampleId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._blSampleId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sessionId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._sessionId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentType':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._experimentType = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._dataCollectionNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startDate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._startDate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'endDate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._endDate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'runStatus':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._runStatus = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxis':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._rotationAxis = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._phiStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._kappaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omegaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._omegaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._axisStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisEnd':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._axisEnd = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axisRange':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._axisRange = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overlap':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._overlap = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._numberOfImages = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startImageNumber':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._startImageNumber = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfPasses':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self._numberOfPasses = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._exposureTime = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageDirectory':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._imageDirectory = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagePrefix':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._imagePrefix = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageSuffix':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._imageSuffix = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileTemplate':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._fileTemplate = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._wavelength = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._resolution = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionAtCorner':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._resolutionAtCorner = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistance':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._detectorDistance = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector2theta':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._detector2theta = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorMode':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._detectorMode = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap1':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._undulatorGap1 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap2':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._undulatorGap2 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'undulatorGap3':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._undulatorGap3 = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xbeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._xbeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ybeam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._ybeam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalClass':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._crystalClass = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slitGapVertical':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._slitGapVertical = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'slitGapHorizontal':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._slitGapHorizontal = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeAtSampleX':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._beamSizeAtSampleX = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeAtSampleY':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._beamSizeAtSampleY = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._transmission = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'synchrotronMode':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._synchrotronMode = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'centeringMethod':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._centeringMethod = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageTemperature':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self._averageTemperature = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._comments = value_
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
				self._printableForReport = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath1':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._xtalSnapshotFullPath1 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath2':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._xtalSnapshotFullPath2 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath3':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._xtalSnapshotFullPath3 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xtalSnapshotFullPath4':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._xtalSnapshotFullPath4 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShape':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._beamShape = value_
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
		self._diffractionPlanId = diffractionPlanId
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", xmlDocumentId, "XSDataInteger")
		self._xmlDocumentId = xmlDocumentId
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", experimentKind, "XSDataString")
		self._experimentKind = experimentKind
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", observedResolution, "XSDataDouble")
		self._observedResolution = observedResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", minimalResolution, "XSDataDouble")
		self._minimalResolution = minimalResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", exposureTime, "XSDataDouble")
		self._exposureTime = exposureTime
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", oscillationRange, "XSDataDouble")
		self._oscillationRange = oscillationRange
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", maximalResolution, "XSDataDouble")
		self._maximalResolution = maximalResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", screeningResolution, "XSDataDouble")
		self._screeningResolution = screeningResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", radiationSensitivity, "XSDataDouble")
		self._radiationSensitivity = radiationSensitivity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", anomalousScatterer, "XSDataString")
		self._anomalousScatterer = anomalousScatterer
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", preferredBeamSizeX, "XSDataDouble")
		self._preferredBeamSizeX = preferredBeamSizeX
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", preferredBeamSizeY, "XSDataDouble")
		self._preferredBeamSizeY = preferredBeamSizeY
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", comments, "XSDataString")
		self._comments = comments
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedMultiplicity, "XSDataDouble")
		self._aimedMultiplicity = aimedMultiplicity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", complexity, "XSDataString")
		self._complexity = complexity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", estimateRadiationDamage, "XSDataBoolean")
		self._estimateRadiationDamage = estimateRadiationDamage
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", forcedSpaceGroup, "XSDataString")
		self._forcedSpaceGroup = forcedSpaceGroup
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredCompleteness, "XSDataDouble")
		self._requiredCompleteness = requiredCompleteness
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredMultiplicity, "XSDataDouble")
		self._requiredMultiplicity = requiredMultiplicity
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", requiredResolution, "XSDataDouble")
		self._requiredResolution = requiredResolution
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", kappaStrategyOption, "XSDataString")
		self._kappaStrategyOption = kappaStrategyOption
		checkType("XSDataISPyBDiffractionPlan", "Constructor of XSDataISPyBDiffractionPlan", numberOfPositions, "XSDataInteger")
		self._numberOfPositions = numberOfPositions
	def getDiffractionPlanId(self): return self._diffractionPlanId
	def setDiffractionPlanId(self, diffractionPlanId):
		checkType("XSDataISPyBDiffractionPlan", "setDiffractionPlanId", diffractionPlanId, "XSDataInteger")
		self._diffractionPlanId = diffractionPlanId
	def delDiffractionPlanId(self): self._diffractionPlanId = None
	# Properties
	diffractionPlanId = property(getDiffractionPlanId, setDiffractionPlanId, delDiffractionPlanId, "Property for diffractionPlanId")
	def getXmlDocumentId(self): return self._xmlDocumentId
	def setXmlDocumentId(self, xmlDocumentId):
		checkType("XSDataISPyBDiffractionPlan", "setXmlDocumentId", xmlDocumentId, "XSDataInteger")
		self._xmlDocumentId = xmlDocumentId
	def delXmlDocumentId(self): self._xmlDocumentId = None
	# Properties
	xmlDocumentId = property(getXmlDocumentId, setXmlDocumentId, delXmlDocumentId, "Property for xmlDocumentId")
	def getExperimentKind(self): return self._experimentKind
	def setExperimentKind(self, experimentKind):
		checkType("XSDataISPyBDiffractionPlan", "setExperimentKind", experimentKind, "XSDataString")
		self._experimentKind = experimentKind
	def delExperimentKind(self): self._experimentKind = None
	# Properties
	experimentKind = property(getExperimentKind, setExperimentKind, delExperimentKind, "Property for experimentKind")
	def getObservedResolution(self): return self._observedResolution
	def setObservedResolution(self, observedResolution):
		checkType("XSDataISPyBDiffractionPlan", "setObservedResolution", observedResolution, "XSDataDouble")
		self._observedResolution = observedResolution
	def delObservedResolution(self): self._observedResolution = None
	# Properties
	observedResolution = property(getObservedResolution, setObservedResolution, delObservedResolution, "Property for observedResolution")
	def getMinimalResolution(self): return self._minimalResolution
	def setMinimalResolution(self, minimalResolution):
		checkType("XSDataISPyBDiffractionPlan", "setMinimalResolution", minimalResolution, "XSDataDouble")
		self._minimalResolution = minimalResolution
	def delMinimalResolution(self): self._minimalResolution = None
	# Properties
	minimalResolution = property(getMinimalResolution, setMinimalResolution, delMinimalResolution, "Property for minimalResolution")
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBDiffractionPlan", "setExposureTime", exposureTime, "XSDataDouble")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getOscillationRange(self): return self._oscillationRange
	def setOscillationRange(self, oscillationRange):
		checkType("XSDataISPyBDiffractionPlan", "setOscillationRange", oscillationRange, "XSDataDouble")
		self._oscillationRange = oscillationRange
	def delOscillationRange(self): self._oscillationRange = None
	# Properties
	oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
	def getMaximalResolution(self): return self._maximalResolution
	def setMaximalResolution(self, maximalResolution):
		checkType("XSDataISPyBDiffractionPlan", "setMaximalResolution", maximalResolution, "XSDataDouble")
		self._maximalResolution = maximalResolution
	def delMaximalResolution(self): self._maximalResolution = None
	# Properties
	maximalResolution = property(getMaximalResolution, setMaximalResolution, delMaximalResolution, "Property for maximalResolution")
	def getScreeningResolution(self): return self._screeningResolution
	def setScreeningResolution(self, screeningResolution):
		checkType("XSDataISPyBDiffractionPlan", "setScreeningResolution", screeningResolution, "XSDataDouble")
		self._screeningResolution = screeningResolution
	def delScreeningResolution(self): self._screeningResolution = None
	# Properties
	screeningResolution = property(getScreeningResolution, setScreeningResolution, delScreeningResolution, "Property for screeningResolution")
	def getRadiationSensitivity(self): return self._radiationSensitivity
	def setRadiationSensitivity(self, radiationSensitivity):
		checkType("XSDataISPyBDiffractionPlan", "setRadiationSensitivity", radiationSensitivity, "XSDataDouble")
		self._radiationSensitivity = radiationSensitivity
	def delRadiationSensitivity(self): self._radiationSensitivity = None
	# Properties
	radiationSensitivity = property(getRadiationSensitivity, setRadiationSensitivity, delRadiationSensitivity, "Property for radiationSensitivity")
	def getAnomalousScatterer(self): return self._anomalousScatterer
	def setAnomalousScatterer(self, anomalousScatterer):
		checkType("XSDataISPyBDiffractionPlan", "setAnomalousScatterer", anomalousScatterer, "XSDataString")
		self._anomalousScatterer = anomalousScatterer
	def delAnomalousScatterer(self): self._anomalousScatterer = None
	# Properties
	anomalousScatterer = property(getAnomalousScatterer, setAnomalousScatterer, delAnomalousScatterer, "Property for anomalousScatterer")
	def getPreferredBeamSizeX(self): return self._preferredBeamSizeX
	def setPreferredBeamSizeX(self, preferredBeamSizeX):
		checkType("XSDataISPyBDiffractionPlan", "setPreferredBeamSizeX", preferredBeamSizeX, "XSDataDouble")
		self._preferredBeamSizeX = preferredBeamSizeX
	def delPreferredBeamSizeX(self): self._preferredBeamSizeX = None
	# Properties
	preferredBeamSizeX = property(getPreferredBeamSizeX, setPreferredBeamSizeX, delPreferredBeamSizeX, "Property for preferredBeamSizeX")
	def getPreferredBeamSizeY(self): return self._preferredBeamSizeY
	def setPreferredBeamSizeY(self, preferredBeamSizeY):
		checkType("XSDataISPyBDiffractionPlan", "setPreferredBeamSizeY", preferredBeamSizeY, "XSDataDouble")
		self._preferredBeamSizeY = preferredBeamSizeY
	def delPreferredBeamSizeY(self): self._preferredBeamSizeY = None
	# Properties
	preferredBeamSizeY = property(getPreferredBeamSizeY, setPreferredBeamSizeY, delPreferredBeamSizeY, "Property for preferredBeamSizeY")
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("XSDataISPyBDiffractionPlan", "setComments", comments, "XSDataString")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getAimedCompleteness(self): return self._aimedCompleteness
	def setAimedCompleteness(self, aimedCompleteness):
		checkType("XSDataISPyBDiffractionPlan", "setAimedCompleteness", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
	def delAimedCompleteness(self): self._aimedCompleteness = None
	# Properties
	aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
	def getAimedIOverSigmaAtHighestResolution(self): return self._aimedIOverSigmaAtHighestResolution
	def setAimedIOverSigmaAtHighestResolution(self, aimedIOverSigmaAtHighestResolution):
		checkType("XSDataISPyBDiffractionPlan", "setAimedIOverSigmaAtHighestResolution", aimedIOverSigmaAtHighestResolution, "XSDataDouble")
		self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
	def delAimedIOverSigmaAtHighestResolution(self): self._aimedIOverSigmaAtHighestResolution = None
	# Properties
	aimedIOverSigmaAtHighestResolution = property(getAimedIOverSigmaAtHighestResolution, setAimedIOverSigmaAtHighestResolution, delAimedIOverSigmaAtHighestResolution, "Property for aimedIOverSigmaAtHighestResolution")
	def getAimedMultiplicity(self): return self._aimedMultiplicity
	def setAimedMultiplicity(self, aimedMultiplicity):
		checkType("XSDataISPyBDiffractionPlan", "setAimedMultiplicity", aimedMultiplicity, "XSDataDouble")
		self._aimedMultiplicity = aimedMultiplicity
	def delAimedMultiplicity(self): self._aimedMultiplicity = None
	# Properties
	aimedMultiplicity = property(getAimedMultiplicity, setAimedMultiplicity, delAimedMultiplicity, "Property for aimedMultiplicity")
	def getAimedResolution(self): return self._aimedResolution
	def setAimedResolution(self, aimedResolution):
		checkType("XSDataISPyBDiffractionPlan", "setAimedResolution", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
	def delAimedResolution(self): self._aimedResolution = None
	# Properties
	aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
	def getAnomalousData(self): return self._anomalousData
	def setAnomalousData(self, anomalousData):
		checkType("XSDataISPyBDiffractionPlan", "setAnomalousData", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
	def delAnomalousData(self): self._anomalousData = None
	# Properties
	anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
	def getComplexity(self): return self._complexity
	def setComplexity(self, complexity):
		checkType("XSDataISPyBDiffractionPlan", "setComplexity", complexity, "XSDataString")
		self._complexity = complexity
	def delComplexity(self): self._complexity = None
	# Properties
	complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
	def getEstimateRadiationDamage(self): return self._estimateRadiationDamage
	def setEstimateRadiationDamage(self, estimateRadiationDamage):
		checkType("XSDataISPyBDiffractionPlan", "setEstimateRadiationDamage", estimateRadiationDamage, "XSDataBoolean")
		self._estimateRadiationDamage = estimateRadiationDamage
	def delEstimateRadiationDamage(self): self._estimateRadiationDamage = None
	# Properties
	estimateRadiationDamage = property(getEstimateRadiationDamage, setEstimateRadiationDamage, delEstimateRadiationDamage, "Property for estimateRadiationDamage")
	def getForcedSpaceGroup(self): return self._forcedSpaceGroup
	def setForcedSpaceGroup(self, forcedSpaceGroup):
		checkType("XSDataISPyBDiffractionPlan", "setForcedSpaceGroup", forcedSpaceGroup, "XSDataString")
		self._forcedSpaceGroup = forcedSpaceGroup
	def delForcedSpaceGroup(self): self._forcedSpaceGroup = None
	# Properties
	forcedSpaceGroup = property(getForcedSpaceGroup, setForcedSpaceGroup, delForcedSpaceGroup, "Property for forcedSpaceGroup")
	def getRequiredCompleteness(self): return self._requiredCompleteness
	def setRequiredCompleteness(self, requiredCompleteness):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredCompleteness", requiredCompleteness, "XSDataDouble")
		self._requiredCompleteness = requiredCompleteness
	def delRequiredCompleteness(self): self._requiredCompleteness = None
	# Properties
	requiredCompleteness = property(getRequiredCompleteness, setRequiredCompleteness, delRequiredCompleteness, "Property for requiredCompleteness")
	def getRequiredMultiplicity(self): return self._requiredMultiplicity
	def setRequiredMultiplicity(self, requiredMultiplicity):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredMultiplicity", requiredMultiplicity, "XSDataDouble")
		self._requiredMultiplicity = requiredMultiplicity
	def delRequiredMultiplicity(self): self._requiredMultiplicity = None
	# Properties
	requiredMultiplicity = property(getRequiredMultiplicity, setRequiredMultiplicity, delRequiredMultiplicity, "Property for requiredMultiplicity")
	def getRequiredResolution(self): return self._requiredResolution
	def setRequiredResolution(self, requiredResolution):
		checkType("XSDataISPyBDiffractionPlan", "setRequiredResolution", requiredResolution, "XSDataDouble")
		self._requiredResolution = requiredResolution
	def delRequiredResolution(self): self._requiredResolution = None
	# Properties
	requiredResolution = property(getRequiredResolution, setRequiredResolution, delRequiredResolution, "Property for requiredResolution")
	def getStrategyOption(self): return self._strategyOption
	def setStrategyOption(self, strategyOption):
		checkType("XSDataISPyBDiffractionPlan", "setStrategyOption", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
	def delStrategyOption(self): self._strategyOption = None
	# Properties
	strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
	def getKappaStrategyOption(self): return self._kappaStrategyOption
	def setKappaStrategyOption(self, kappaStrategyOption):
		checkType("XSDataISPyBDiffractionPlan", "setKappaStrategyOption", kappaStrategyOption, "XSDataString")
		self._kappaStrategyOption = kappaStrategyOption
	def delKappaStrategyOption(self): self._kappaStrategyOption = None
	# Properties
	kappaStrategyOption = property(getKappaStrategyOption, setKappaStrategyOption, delKappaStrategyOption, "Property for kappaStrategyOption")
	def getNumberOfPositions(self): return self._numberOfPositions
	def setNumberOfPositions(self, numberOfPositions):
		checkType("XSDataISPyBDiffractionPlan", "setNumberOfPositions", numberOfPositions, "XSDataInteger")
		self._numberOfPositions = numberOfPositions
	def delNumberOfPositions(self): self._numberOfPositions = None
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
		if self._diffractionPlanId is not None:
			self.diffractionPlanId.export(outfile, level, name_='diffractionPlanId')
		if self._xmlDocumentId is not None:
			self.xmlDocumentId.export(outfile, level, name_='xmlDocumentId')
		if self._experimentKind is not None:
			self.experimentKind.export(outfile, level, name_='experimentKind')
		if self._observedResolution is not None:
			self.observedResolution.export(outfile, level, name_='observedResolution')
		if self._minimalResolution is not None:
			self.minimalResolution.export(outfile, level, name_='minimalResolution')
		if self._exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self._oscillationRange is not None:
			self.oscillationRange.export(outfile, level, name_='oscillationRange')
		if self._maximalResolution is not None:
			self.maximalResolution.export(outfile, level, name_='maximalResolution')
		if self._screeningResolution is not None:
			self.screeningResolution.export(outfile, level, name_='screeningResolution')
		if self._radiationSensitivity is not None:
			self.radiationSensitivity.export(outfile, level, name_='radiationSensitivity')
		if self._anomalousScatterer is not None:
			self.anomalousScatterer.export(outfile, level, name_='anomalousScatterer')
		if self._preferredBeamSizeX is not None:
			self.preferredBeamSizeX.export(outfile, level, name_='preferredBeamSizeX')
		if self._preferredBeamSizeY is not None:
			self.preferredBeamSizeY.export(outfile, level, name_='preferredBeamSizeY')
		if self._comments is not None:
			self.comments.export(outfile, level, name_='comments')
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
		if self._estimateRadiationDamage is not None:
			self.estimateRadiationDamage.export(outfile, level, name_='estimateRadiationDamage')
		if self._forcedSpaceGroup is not None:
			self.forcedSpaceGroup.export(outfile, level, name_='forcedSpaceGroup')
		if self._requiredCompleteness is not None:
			self.requiredCompleteness.export(outfile, level, name_='requiredCompleteness')
		if self._requiredMultiplicity is not None:
			self.requiredMultiplicity.export(outfile, level, name_='requiredMultiplicity')
		if self._requiredResolution is not None:
			self.requiredResolution.export(outfile, level, name_='requiredResolution')
		if self._strategyOption is not None:
			self.strategyOption.export(outfile, level, name_='strategyOption')
		if self._kappaStrategyOption is not None:
			self.kappaStrategyOption.export(outfile, level, name_='kappaStrategyOption')
		if self._numberOfPositions is not None:
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
		self._comments = comments
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", cumulativeIntensity, "XSDataDouble")
		self._cumulativeIntensity = cumulativeIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileLocation, "XSDataString")
		self._fileLocation = fileLocation
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileName, "XSDataString")
		self._fileName = fileName
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageId, "XSDataInteger")
		self._imageId = imageId
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageNumber, "XSDataInteger")
		self._imageNumber = imageNumber
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegFileFullPath, "XSDataString")
		self._jpegFileFullPath = jpegFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegThumbnailFileFullPath, "XSDataString")
		self._jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", machineMessage, "XSDataString")
		self._machineMessage = machineMessage
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", measuredIntensity, "XSDataDouble")
		self._measuredIntensity = measuredIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", synchrotronCurrent, "XSDataDouble")
		self._synchrotronCurrent = synchrotronCurrent
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", temperature, "XSDataDouble")
		self._temperature = temperature
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("XSDataISPyBImage", "setComments", comments, "XSDataString")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getCumulativeIntensity(self): return self._cumulativeIntensity
	def setCumulativeIntensity(self, cumulativeIntensity):
		checkType("XSDataISPyBImage", "setCumulativeIntensity", cumulativeIntensity, "XSDataDouble")
		self._cumulativeIntensity = cumulativeIntensity
	def delCumulativeIntensity(self): self._cumulativeIntensity = None
	# Properties
	cumulativeIntensity = property(getCumulativeIntensity, setCumulativeIntensity, delCumulativeIntensity, "Property for cumulativeIntensity")
	def getFileLocation(self): return self._fileLocation
	def setFileLocation(self, fileLocation):
		checkType("XSDataISPyBImage", "setFileLocation", fileLocation, "XSDataString")
		self._fileLocation = fileLocation
	def delFileLocation(self): self._fileLocation = None
	# Properties
	fileLocation = property(getFileLocation, setFileLocation, delFileLocation, "Property for fileLocation")
	def getFileName(self): return self._fileName
	def setFileName(self, fileName):
		checkType("XSDataISPyBImage", "setFileName", fileName, "XSDataString")
		self._fileName = fileName
	def delFileName(self): self._fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getImageId(self): return self._imageId
	def setImageId(self, imageId):
		checkType("XSDataISPyBImage", "setImageId", imageId, "XSDataInteger")
		self._imageId = imageId
	def delImageId(self): self._imageId = None
	# Properties
	imageId = property(getImageId, setImageId, delImageId, "Property for imageId")
	def getImageNumber(self): return self._imageNumber
	def setImageNumber(self, imageNumber):
		checkType("XSDataISPyBImage", "setImageNumber", imageNumber, "XSDataInteger")
		self._imageNumber = imageNumber
	def delImageNumber(self): self._imageNumber = None
	# Properties
	imageNumber = property(getImageNumber, setImageNumber, delImageNumber, "Property for imageNumber")
	def getJpegFileFullPath(self): return self._jpegFileFullPath
	def setJpegFileFullPath(self, jpegFileFullPath):
		checkType("XSDataISPyBImage", "setJpegFileFullPath", jpegFileFullPath, "XSDataString")
		self._jpegFileFullPath = jpegFileFullPath
	def delJpegFileFullPath(self): self._jpegFileFullPath = None
	# Properties
	jpegFileFullPath = property(getJpegFileFullPath, setJpegFileFullPath, delJpegFileFullPath, "Property for jpegFileFullPath")
	def getJpegThumbnailFileFullPath(self): return self._jpegThumbnailFileFullPath
	def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath):
		checkType("XSDataISPyBImage", "setJpegThumbnailFileFullPath", jpegThumbnailFileFullPath, "XSDataString")
		self._jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
	def delJpegThumbnailFileFullPath(self): self._jpegThumbnailFileFullPath = None
	# Properties
	jpegThumbnailFileFullPath = property(getJpegThumbnailFileFullPath, setJpegThumbnailFileFullPath, delJpegThumbnailFileFullPath, "Property for jpegThumbnailFileFullPath")
	def getMachineMessage(self): return self._machineMessage
	def setMachineMessage(self, machineMessage):
		checkType("XSDataISPyBImage", "setMachineMessage", machineMessage, "XSDataString")
		self._machineMessage = machineMessage
	def delMachineMessage(self): self._machineMessage = None
	# Properties
	machineMessage = property(getMachineMessage, setMachineMessage, delMachineMessage, "Property for machineMessage")
	def getMeasuredIntensity(self): return self._measuredIntensity
	def setMeasuredIntensity(self, measuredIntensity):
		checkType("XSDataISPyBImage", "setMeasuredIntensity", measuredIntensity, "XSDataDouble")
		self._measuredIntensity = measuredIntensity
	def delMeasuredIntensity(self): self._measuredIntensity = None
	# Properties
	measuredIntensity = property(getMeasuredIntensity, setMeasuredIntensity, delMeasuredIntensity, "Property for measuredIntensity")
	def getSynchrotronCurrent(self): return self._synchrotronCurrent
	def setSynchrotronCurrent(self, synchrotronCurrent):
		checkType("XSDataISPyBImage", "setSynchrotronCurrent", synchrotronCurrent, "XSDataDouble")
		self._synchrotronCurrent = synchrotronCurrent
	def delSynchrotronCurrent(self): self._synchrotronCurrent = None
	# Properties
	synchrotronCurrent = property(getSynchrotronCurrent, setSynchrotronCurrent, delSynchrotronCurrent, "Property for synchrotronCurrent")
	def getTemperature(self): return self._temperature
	def setTemperature(self, temperature):
		checkType("XSDataISPyBImage", "setTemperature", temperature, "XSDataDouble")
		self._temperature = temperature
	def delTemperature(self): self._temperature = None
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
		if self._comments is not None:
			self.comments.export(outfile, level, name_='comments')
		else:
			warnEmptyAttribute("comments", "XSDataString")
		if self._cumulativeIntensity is not None:
			self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
		else:
			warnEmptyAttribute("cumulativeIntensity", "XSDataDouble")
		if self._fileLocation is not None:
			self.fileLocation.export(outfile, level, name_='fileLocation')
		else:
			warnEmptyAttribute("fileLocation", "XSDataString")
		if self._fileName is not None:
			self.fileName.export(outfile, level, name_='fileName')
		else:
			warnEmptyAttribute("fileName", "XSDataString")
		if self._imageId is not None:
			self.imageId.export(outfile, level, name_='imageId')
		else:
			warnEmptyAttribute("imageId", "XSDataInteger")
		if self._imageNumber is not None:
			self.imageNumber.export(outfile, level, name_='imageNumber')
		else:
			warnEmptyAttribute("imageNumber", "XSDataInteger")
		if self._jpegFileFullPath is not None:
			self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
		else:
			warnEmptyAttribute("jpegFileFullPath", "XSDataString")
		if self._jpegThumbnailFileFullPath is not None:
			self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
		else:
			warnEmptyAttribute("jpegThumbnailFileFullPath", "XSDataString")
		if self._machineMessage is not None:
			self.machineMessage.export(outfile, level, name_='machineMessage')
		else:
			warnEmptyAttribute("machineMessage", "XSDataString")
		if self._measuredIntensity is not None:
			self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
		else:
			warnEmptyAttribute("measuredIntensity", "XSDataDouble")
		if self._synchrotronCurrent is not None:
			self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
		else:
			warnEmptyAttribute("synchrotronCurrent", "XSDataDouble")
		if self._temperature is not None:
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
		self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", goodBraggCandidates, "XSDataInteger")
		self._goodBraggCandidates = goodBraggCandidates
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", iceRings, "XSDataInteger")
		self._iceRings = iceRings
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", image, "XSDataImage")
		self._image = image
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", inResTotal, "XSDataInteger")
		self._inResTotal = inResTotal
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", inResolutionOvrlSpots, "XSDataInteger")
		self._inResolutionOvrlSpots = inResolutionOvrlSpots
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", maxUnitCell, "XSDataDouble")
		self._maxUnitCell = maxUnitCell
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", method1Res, "XSDataDouble")
		self._method1Res = method1Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", method2Res, "XSDataDouble")
		self._method2Res = method2Res
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", pctSaturationTop50Peaks, "XSDataDouble")
		self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeAverage, "XSDataDouble")
		self._saturationRangeAverage = saturationRangeAverage
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeMax, "XSDataDouble")
		self._saturationRangeMax = saturationRangeMax
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", saturationRangeMin, "XSDataDouble")
		self._saturationRangeMin = saturationRangeMin
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeAverage, "XSDataDouble")
		self._signalRangeAverage = signalRangeAverage
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeMax, "XSDataDouble")
		self._signalRangeMax = signalRangeMax
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", signalRangeMin, "XSDataDouble")
		self._signalRangeMin = signalRangeMin
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", spotTotal, "XSDataInteger")
		self._spotTotal = spotTotal
		checkType("XSDataISPyBImageQualityIndicators", "Constructor of XSDataISPyBImageQualityIndicators", totalIntegratedSignal, "XSDataDouble")
		self._totalIntegratedSignal = totalIntegratedSignal
	def getBinPopCutOffMethod2Res(self): return self._binPopCutOffMethod2Res
	def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res):
		checkType("XSDataISPyBImageQualityIndicators", "setBinPopCutOffMethod2Res", binPopCutOffMethod2Res, "XSDataDouble")
		self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
	def delBinPopCutOffMethod2Res(self): self._binPopCutOffMethod2Res = None
	# Properties
	binPopCutOffMethod2Res = property(getBinPopCutOffMethod2Res, setBinPopCutOffMethod2Res, delBinPopCutOffMethod2Res, "Property for binPopCutOffMethod2Res")
	def getGoodBraggCandidates(self): return self._goodBraggCandidates
	def setGoodBraggCandidates(self, goodBraggCandidates):
		checkType("XSDataISPyBImageQualityIndicators", "setGoodBraggCandidates", goodBraggCandidates, "XSDataInteger")
		self._goodBraggCandidates = goodBraggCandidates
	def delGoodBraggCandidates(self): self._goodBraggCandidates = None
	# Properties
	goodBraggCandidates = property(getGoodBraggCandidates, setGoodBraggCandidates, delGoodBraggCandidates, "Property for goodBraggCandidates")
	def getIceRings(self): return self._iceRings
	def setIceRings(self, iceRings):
		checkType("XSDataISPyBImageQualityIndicators", "setIceRings", iceRings, "XSDataInteger")
		self._iceRings = iceRings
	def delIceRings(self): self._iceRings = None
	# Properties
	iceRings = property(getIceRings, setIceRings, delIceRings, "Property for iceRings")
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataISPyBImageQualityIndicators", "setImage", image, "XSDataImage")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getInResTotal(self): return self._inResTotal
	def setInResTotal(self, inResTotal):
		checkType("XSDataISPyBImageQualityIndicators", "setInResTotal", inResTotal, "XSDataInteger")
		self._inResTotal = inResTotal
	def delInResTotal(self): self._inResTotal = None
	# Properties
	inResTotal = property(getInResTotal, setInResTotal, delInResTotal, "Property for inResTotal")
	def getInResolutionOvrlSpots(self): return self._inResolutionOvrlSpots
	def setInResolutionOvrlSpots(self, inResolutionOvrlSpots):
		checkType("XSDataISPyBImageQualityIndicators", "setInResolutionOvrlSpots", inResolutionOvrlSpots, "XSDataInteger")
		self._inResolutionOvrlSpots = inResolutionOvrlSpots
	def delInResolutionOvrlSpots(self): self._inResolutionOvrlSpots = None
	# Properties
	inResolutionOvrlSpots = property(getInResolutionOvrlSpots, setInResolutionOvrlSpots, delInResolutionOvrlSpots, "Property for inResolutionOvrlSpots")
	def getMaxUnitCell(self): return self._maxUnitCell
	def setMaxUnitCell(self, maxUnitCell):
		checkType("XSDataISPyBImageQualityIndicators", "setMaxUnitCell", maxUnitCell, "XSDataDouble")
		self._maxUnitCell = maxUnitCell
	def delMaxUnitCell(self): self._maxUnitCell = None
	# Properties
	maxUnitCell = property(getMaxUnitCell, setMaxUnitCell, delMaxUnitCell, "Property for maxUnitCell")
	def getMethod1Res(self): return self._method1Res
	def setMethod1Res(self, method1Res):
		checkType("XSDataISPyBImageQualityIndicators", "setMethod1Res", method1Res, "XSDataDouble")
		self._method1Res = method1Res
	def delMethod1Res(self): self._method1Res = None
	# Properties
	method1Res = property(getMethod1Res, setMethod1Res, delMethod1Res, "Property for method1Res")
	def getMethod2Res(self): return self._method2Res
	def setMethod2Res(self, method2Res):
		checkType("XSDataISPyBImageQualityIndicators", "setMethod2Res", method2Res, "XSDataDouble")
		self._method2Res = method2Res
	def delMethod2Res(self): self._method2Res = None
	# Properties
	method2Res = property(getMethod2Res, setMethod2Res, delMethod2Res, "Property for method2Res")
	def getPctSaturationTop50Peaks(self): return self._pctSaturationTop50Peaks
	def setPctSaturationTop50Peaks(self, pctSaturationTop50Peaks):
		checkType("XSDataISPyBImageQualityIndicators", "setPctSaturationTop50Peaks", pctSaturationTop50Peaks, "XSDataDouble")
		self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
	def delPctSaturationTop50Peaks(self): self._pctSaturationTop50Peaks = None
	# Properties
	pctSaturationTop50Peaks = property(getPctSaturationTop50Peaks, setPctSaturationTop50Peaks, delPctSaturationTop50Peaks, "Property for pctSaturationTop50Peaks")
	def getSaturationRangeAverage(self): return self._saturationRangeAverage
	def setSaturationRangeAverage(self, saturationRangeAverage):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeAverage", saturationRangeAverage, "XSDataDouble")
		self._saturationRangeAverage = saturationRangeAverage
	def delSaturationRangeAverage(self): self._saturationRangeAverage = None
	# Properties
	saturationRangeAverage = property(getSaturationRangeAverage, setSaturationRangeAverage, delSaturationRangeAverage, "Property for saturationRangeAverage")
	def getSaturationRangeMax(self): return self._saturationRangeMax
	def setSaturationRangeMax(self, saturationRangeMax):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeMax", saturationRangeMax, "XSDataDouble")
		self._saturationRangeMax = saturationRangeMax
	def delSaturationRangeMax(self): self._saturationRangeMax = None
	# Properties
	saturationRangeMax = property(getSaturationRangeMax, setSaturationRangeMax, delSaturationRangeMax, "Property for saturationRangeMax")
	def getSaturationRangeMin(self): return self._saturationRangeMin
	def setSaturationRangeMin(self, saturationRangeMin):
		checkType("XSDataISPyBImageQualityIndicators", "setSaturationRangeMin", saturationRangeMin, "XSDataDouble")
		self._saturationRangeMin = saturationRangeMin
	def delSaturationRangeMin(self): self._saturationRangeMin = None
	# Properties
	saturationRangeMin = property(getSaturationRangeMin, setSaturationRangeMin, delSaturationRangeMin, "Property for saturationRangeMin")
	def getSignalRangeAverage(self): return self._signalRangeAverage
	def setSignalRangeAverage(self, signalRangeAverage):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeAverage", signalRangeAverage, "XSDataDouble")
		self._signalRangeAverage = signalRangeAverage
	def delSignalRangeAverage(self): self._signalRangeAverage = None
	# Properties
	signalRangeAverage = property(getSignalRangeAverage, setSignalRangeAverage, delSignalRangeAverage, "Property for signalRangeAverage")
	def getSignalRangeMax(self): return self._signalRangeMax
	def setSignalRangeMax(self, signalRangeMax):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeMax", signalRangeMax, "XSDataDouble")
		self._signalRangeMax = signalRangeMax
	def delSignalRangeMax(self): self._signalRangeMax = None
	# Properties
	signalRangeMax = property(getSignalRangeMax, setSignalRangeMax, delSignalRangeMax, "Property for signalRangeMax")
	def getSignalRangeMin(self): return self._signalRangeMin
	def setSignalRangeMin(self, signalRangeMin):
		checkType("XSDataISPyBImageQualityIndicators", "setSignalRangeMin", signalRangeMin, "XSDataDouble")
		self._signalRangeMin = signalRangeMin
	def delSignalRangeMin(self): self._signalRangeMin = None
	# Properties
	signalRangeMin = property(getSignalRangeMin, setSignalRangeMin, delSignalRangeMin, "Property for signalRangeMin")
	def getSpotTotal(self): return self._spotTotal
	def setSpotTotal(self, spotTotal):
		checkType("XSDataISPyBImageQualityIndicators", "setSpotTotal", spotTotal, "XSDataInteger")
		self._spotTotal = spotTotal
	def delSpotTotal(self): self._spotTotal = None
	# Properties
	spotTotal = property(getSpotTotal, setSpotTotal, delSpotTotal, "Property for spotTotal")
	def getTotalIntegratedSignal(self): return self._totalIntegratedSignal
	def setTotalIntegratedSignal(self, totalIntegratedSignal):
		checkType("XSDataISPyBImageQualityIndicators", "setTotalIntegratedSignal", totalIntegratedSignal, "XSDataDouble")
		self._totalIntegratedSignal = totalIntegratedSignal
	def delTotalIntegratedSignal(self): self._totalIntegratedSignal = None
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
		self._screeningId = screeningId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", timeStamp, "XSDataString")
		self._timeStamp = timeStamp
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", programVersion, "XSDataString")
		self._programVersion = programVersion
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", comments, "XSDataString")
		self._comments = comments
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", shortComments, "XSDataString")
		self._shortComments = shortComments
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreening", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBScreening", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getTimeStamp(self): return self._timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreening", "setTimeStamp", timeStamp, "XSDataString")
		self._timeStamp = timeStamp
	def delTimeStamp(self): self._timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def getProgramVersion(self): return self._programVersion
	def setProgramVersion(self, programVersion):
		checkType("XSDataISPyBScreening", "setProgramVersion", programVersion, "XSDataString")
		self._programVersion = programVersion
	def delProgramVersion(self): self._programVersion = None
	# Properties
	programVersion = property(getProgramVersion, setProgramVersion, delProgramVersion, "Property for programVersion")
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("XSDataISPyBScreening", "setComments", comments, "XSDataString")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getShortComments(self): return self._shortComments
	def setShortComments(self, shortComments):
		checkType("XSDataISPyBScreening", "setShortComments", shortComments, "XSDataString")
		self._shortComments = shortComments
	def delShortComments(self): self._shortComments = None
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
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		if self._dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		else:
			warnEmptyAttribute("dataCollectionId", "XSDataInteger")
		if self._timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataString")
		if self._programVersion is not None:
			self.programVersion.export(outfile, level, name_='programVersion')
		if self._comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self._shortComments is not None:
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
		self._screeningFileId = screeningFileId
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", screeningId, "XSDataInteger")
		self._screeningId = screeningId
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", fileType, "XSDataString")
		self._fileType = fileType
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", fileName, "XSDataString")
		self._fileName = fileName
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", filePath, "XSDataString")
		self._filePath = filePath
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", description, "XSDataString")
		self._description = description
		checkType("XSDataISPyBScreeningFile", "Constructor of XSDataISPyBScreeningFile", timeStamp, "XSDataString")
		self._timeStamp = timeStamp
	def getScreeningFileId(self): return self._screeningFileId
	def setScreeningFileId(self, screeningFileId):
		checkType("XSDataISPyBScreeningFile", "setScreeningFileId", screeningFileId, "XSDataInteger")
		self._screeningFileId = screeningFileId
	def delScreeningFileId(self): self._screeningFileId = None
	# Properties
	screeningFileId = property(getScreeningFileId, setScreeningFileId, delScreeningFileId, "Property for screeningFileId")
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningFile", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getFileType(self): return self._fileType
	def setFileType(self, fileType):
		checkType("XSDataISPyBScreeningFile", "setFileType", fileType, "XSDataString")
		self._fileType = fileType
	def delFileType(self): self._fileType = None
	# Properties
	fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
	def getFileName(self): return self._fileName
	def setFileName(self, fileName):
		checkType("XSDataISPyBScreeningFile", "setFileName", fileName, "XSDataString")
		self._fileName = fileName
	def delFileName(self): self._fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFilePath(self): return self._filePath
	def setFilePath(self, filePath):
		checkType("XSDataISPyBScreeningFile", "setFilePath", filePath, "XSDataString")
		self._filePath = filePath
	def delFilePath(self): self._filePath = None
	# Properties
	filePath = property(getFilePath, setFilePath, delFilePath, "Property for filePath")
	def getDescription(self): return self._description
	def setDescription(self, description):
		checkType("XSDataISPyBScreeningFile", "setDescription", description, "XSDataString")
		self._description = description
	def delDescription(self): self._description = None
	# Properties
	description = property(getDescription, setDescription, delDescription, "Property for description")
	def getTimeStamp(self): return self._timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreeningFile", "setTimeStamp", timeStamp, "XSDataString")
		self._timeStamp = timeStamp
	def delTimeStamp(self): self._timeStamp = None
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
		if self._screeningFileId is not None:
			self.screeningFileId.export(outfile, level, name_='screeningFileId')
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		if self._fileType is not None:
			self.fileType.export(outfile, level, name_='fileType')
		if self._fileName is not None:
			self.fileName.export(outfile, level, name_='fileName')
		else:
			warnEmptyAttribute("fileName", "XSDataString")
		if self._filePath is not None:
			self.filePath.export(outfile, level, name_='filePath')
		else:
			warnEmptyAttribute("filePath", "XSDataString")
		if self._description is not None:
			self.description.export(outfile, level, name_='description')
		if self._timeStamp is not None:
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
		self._screeningInputId = screeningInputId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", screeningId, "XSDataInteger")
		self._screeningId = screeningId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", diffractionPlanId, "XSDataInteger")
		self._diffractionPlanId = diffractionPlanId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamX, "XSDataLength")
		self._beamX = beamX
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamY, "XSDataLength")
		self._beamY = beamY
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", rmsErrorLimits, "XSDataDouble")
		self._rmsErrorLimits = rmsErrorLimits
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumFractionIndexed, "XSDataDouble")
		self._minimumFractionIndexed = minimumFractionIndexed
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", maximumFractionRejected, "XSDataDouble")
		self._maximumFractionRejected = maximumFractionRejected
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumSignalToNoise, "XSDataDouble")
		self._minimumSignalToNoise = minimumSignalToNoise
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", xmlSampleInformation, "XSDataString")
		self._xmlSampleInformation = xmlSampleInformation
	def getScreeningInputId(self): return self._screeningInputId
	def setScreeningInputId(self, screeningInputId):
		checkType("XSDataISPyBScreeningInput", "setScreeningInputId", screeningInputId, "XSDataInteger")
		self._screeningInputId = screeningInputId
	def delScreeningInputId(self): self._screeningInputId = None
	# Properties
	screeningInputId = property(getScreeningInputId, setScreeningInputId, delScreeningInputId, "Property for screeningInputId")
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningInput", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getDiffractionPlanId(self): return self._diffractionPlanId
	def setDiffractionPlanId(self, diffractionPlanId):
		checkType("XSDataISPyBScreeningInput", "setDiffractionPlanId", diffractionPlanId, "XSDataInteger")
		self._diffractionPlanId = diffractionPlanId
	def delDiffractionPlanId(self): self._diffractionPlanId = None
	# Properties
	diffractionPlanId = property(getDiffractionPlanId, setDiffractionPlanId, delDiffractionPlanId, "Property for diffractionPlanId")
	def getBeamX(self): return self._beamX
	def setBeamX(self, beamX):
		checkType("XSDataISPyBScreeningInput", "setBeamX", beamX, "XSDataLength")
		self._beamX = beamX
	def delBeamX(self): self._beamX = None
	# Properties
	beamX = property(getBeamX, setBeamX, delBeamX, "Property for beamX")
	def getBeamY(self): return self._beamY
	def setBeamY(self, beamY):
		checkType("XSDataISPyBScreeningInput", "setBeamY", beamY, "XSDataLength")
		self._beamY = beamY
	def delBeamY(self): self._beamY = None
	# Properties
	beamY = property(getBeamY, setBeamY, delBeamY, "Property for beamY")
	def getRmsErrorLimits(self): return self._rmsErrorLimits
	def setRmsErrorLimits(self, rmsErrorLimits):
		checkType("XSDataISPyBScreeningInput", "setRmsErrorLimits", rmsErrorLimits, "XSDataDouble")
		self._rmsErrorLimits = rmsErrorLimits
	def delRmsErrorLimits(self): self._rmsErrorLimits = None
	# Properties
	rmsErrorLimits = property(getRmsErrorLimits, setRmsErrorLimits, delRmsErrorLimits, "Property for rmsErrorLimits")
	def getMinimumFractionIndexed(self): return self._minimumFractionIndexed
	def setMinimumFractionIndexed(self, minimumFractionIndexed):
		checkType("XSDataISPyBScreeningInput", "setMinimumFractionIndexed", minimumFractionIndexed, "XSDataDouble")
		self._minimumFractionIndexed = minimumFractionIndexed
	def delMinimumFractionIndexed(self): self._minimumFractionIndexed = None
	# Properties
	minimumFractionIndexed = property(getMinimumFractionIndexed, setMinimumFractionIndexed, delMinimumFractionIndexed, "Property for minimumFractionIndexed")
	def getMaximumFractionRejected(self): return self._maximumFractionRejected
	def setMaximumFractionRejected(self, maximumFractionRejected):
		checkType("XSDataISPyBScreeningInput", "setMaximumFractionRejected", maximumFractionRejected, "XSDataDouble")
		self._maximumFractionRejected = maximumFractionRejected
	def delMaximumFractionRejected(self): self._maximumFractionRejected = None
	# Properties
	maximumFractionRejected = property(getMaximumFractionRejected, setMaximumFractionRejected, delMaximumFractionRejected, "Property for maximumFractionRejected")
	def getMinimumSignalToNoise(self): return self._minimumSignalToNoise
	def setMinimumSignalToNoise(self, minimumSignalToNoise):
		checkType("XSDataISPyBScreeningInput", "setMinimumSignalToNoise", minimumSignalToNoise, "XSDataDouble")
		self._minimumSignalToNoise = minimumSignalToNoise
	def delMinimumSignalToNoise(self): self._minimumSignalToNoise = None
	# Properties
	minimumSignalToNoise = property(getMinimumSignalToNoise, setMinimumSignalToNoise, delMinimumSignalToNoise, "Property for minimumSignalToNoise")
	def getXmlSampleInformation(self): return self._xmlSampleInformation
	def setXmlSampleInformation(self, xmlSampleInformation):
		checkType("XSDataISPyBScreeningInput", "setXmlSampleInformation", xmlSampleInformation, "XSDataString")
		self._xmlSampleInformation = xmlSampleInformation
	def delXmlSampleInformation(self): self._xmlSampleInformation = None
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
		if self._screeningInputId is not None:
			self.screeningInputId.export(outfile, level, name_='screeningInputId')
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		if self._diffractionPlanId is not None:
			self.diffractionPlanId.export(outfile, level, name_='diffractionPlanId')
		if self._beamX is not None:
			self.beamX.export(outfile, level, name_='beamX')
		if self._beamY is not None:
			self.beamY.export(outfile, level, name_='beamY')
		if self._rmsErrorLimits is not None:
			self.rmsErrorLimits.export(outfile, level, name_='rmsErrorLimits')
		if self._minimumFractionIndexed is not None:
			self.minimumFractionIndexed.export(outfile, level, name_='minimumFractionIndexed')
		if self._maximumFractionRejected is not None:
			self.maximumFractionRejected.export(outfile, level, name_='maximumFractionRejected')
		if self._minimumSignalToNoise is not None:
			self.minimumSignalToNoise.export(outfile, level, name_='minimumSignalToNoise')
		if self._xmlSampleInformation is not None:
			self.xmlSampleInformation.export(outfile, level, name_='xmlSampleInformation')
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
		self._screeningInput = screeningInput
	def getScreeningInput(self): return self._screeningInput
	def setScreeningInput(self, screeningInput):
		checkType("XSDataISPyBScreeningInputContainer", "setScreeningInput", screeningInput, "XSDataISPyBScreeningInput")
		self._screeningInput = screeningInput
	def delScreeningInput(self): self._screeningInput = None
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
		if self._screeningInput is not None:
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
		self._screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningId, "XSDataInteger")
		self._screeningId = screeningId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", statusDescription, "XSDataString")
		self._statusDescription = statusDescription
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", rejectedReflections, "XSDataInteger")
		self._rejectedReflections = rejectedReflections
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", resolutionObtained, "XSDataDouble")
		self._resolutionObtained = resolutionObtained
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationR, "XSDataLength")
		self._spotDeviationR = spotDeviationR
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationTheta, "XSDataAngle")
		self._spotDeviationTheta = spotDeviationTheta
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftX, "XSDataLength")
		self._beamShiftX = beamShiftX
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftY, "XSDataLength")
		self._beamShiftY = beamShiftY
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsFound, "XSDataInteger")
		self._numSpotsFound = numSpotsFound
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsUsed, "XSDataInteger")
		self._numSpotsUsed = numSpotsUsed
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsRejected, "XSDataInteger")
		self._numSpotsRejected = numSpotsRejected
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", iOverSigma, "XSDataDouble")
		self._iOverSigma = iOverSigma
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", diffractionRings, "XSDataBoolean")
		self._diffractionRings = diffractionRings
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningSuccess, "XSDataBoolean")
		self._screeningSuccess = screeningSuccess
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicityEstimated, "XSDataBoolean")
		self._mosaicityEstimated = mosaicityEstimated
	def getScreeningOutputId(self): return self._screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self._screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self._screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getStatusDescription(self): return self._statusDescription
	def setStatusDescription(self, statusDescription):
		checkType("XSDataISPyBScreeningOutput", "setStatusDescription", statusDescription, "XSDataString")
		self._statusDescription = statusDescription
	def delStatusDescription(self): self._statusDescription = None
	# Properties
	statusDescription = property(getStatusDescription, setStatusDescription, delStatusDescription, "Property for statusDescription")
	def getRejectedReflections(self): return self._rejectedReflections
	def setRejectedReflections(self, rejectedReflections):
		checkType("XSDataISPyBScreeningOutput", "setRejectedReflections", rejectedReflections, "XSDataInteger")
		self._rejectedReflections = rejectedReflections
	def delRejectedReflections(self): self._rejectedReflections = None
	# Properties
	rejectedReflections = property(getRejectedReflections, setRejectedReflections, delRejectedReflections, "Property for rejectedReflections")
	def getResolutionObtained(self): return self._resolutionObtained
	def setResolutionObtained(self, resolutionObtained):
		checkType("XSDataISPyBScreeningOutput", "setResolutionObtained", resolutionObtained, "XSDataDouble")
		self._resolutionObtained = resolutionObtained
	def delResolutionObtained(self): self._resolutionObtained = None
	# Properties
	resolutionObtained = property(getResolutionObtained, setResolutionObtained, delResolutionObtained, "Property for resolutionObtained")
	def getSpotDeviationR(self): return self._spotDeviationR
	def setSpotDeviationR(self, spotDeviationR):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationR", spotDeviationR, "XSDataLength")
		self._spotDeviationR = spotDeviationR
	def delSpotDeviationR(self): self._spotDeviationR = None
	# Properties
	spotDeviationR = property(getSpotDeviationR, setSpotDeviationR, delSpotDeviationR, "Property for spotDeviationR")
	def getSpotDeviationTheta(self): return self._spotDeviationTheta
	def setSpotDeviationTheta(self, spotDeviationTheta):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationTheta", spotDeviationTheta, "XSDataAngle")
		self._spotDeviationTheta = spotDeviationTheta
	def delSpotDeviationTheta(self): self._spotDeviationTheta = None
	# Properties
	spotDeviationTheta = property(getSpotDeviationTheta, setSpotDeviationTheta, delSpotDeviationTheta, "Property for spotDeviationTheta")
	def getBeamShiftX(self): return self._beamShiftX
	def setBeamShiftX(self, beamShiftX):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftX", beamShiftX, "XSDataLength")
		self._beamShiftX = beamShiftX
	def delBeamShiftX(self): self._beamShiftX = None
	# Properties
	beamShiftX = property(getBeamShiftX, setBeamShiftX, delBeamShiftX, "Property for beamShiftX")
	def getBeamShiftY(self): return self._beamShiftY
	def setBeamShiftY(self, beamShiftY):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftY", beamShiftY, "XSDataLength")
		self._beamShiftY = beamShiftY
	def delBeamShiftY(self): self._beamShiftY = None
	# Properties
	beamShiftY = property(getBeamShiftY, setBeamShiftY, delBeamShiftY, "Property for beamShiftY")
	def getNumSpotsFound(self): return self._numSpotsFound
	def setNumSpotsFound(self, numSpotsFound):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsFound", numSpotsFound, "XSDataInteger")
		self._numSpotsFound = numSpotsFound
	def delNumSpotsFound(self): self._numSpotsFound = None
	# Properties
	numSpotsFound = property(getNumSpotsFound, setNumSpotsFound, delNumSpotsFound, "Property for numSpotsFound")
	def getNumSpotsUsed(self): return self._numSpotsUsed
	def setNumSpotsUsed(self, numSpotsUsed):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsUsed", numSpotsUsed, "XSDataInteger")
		self._numSpotsUsed = numSpotsUsed
	def delNumSpotsUsed(self): self._numSpotsUsed = None
	# Properties
	numSpotsUsed = property(getNumSpotsUsed, setNumSpotsUsed, delNumSpotsUsed, "Property for numSpotsUsed")
	def getNumSpotsRejected(self): return self._numSpotsRejected
	def setNumSpotsRejected(self, numSpotsRejected):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsRejected", numSpotsRejected, "XSDataInteger")
		self._numSpotsRejected = numSpotsRejected
	def delNumSpotsRejected(self): self._numSpotsRejected = None
	# Properties
	numSpotsRejected = property(getNumSpotsRejected, setNumSpotsRejected, delNumSpotsRejected, "Property for numSpotsRejected")
	def getMosaicity(self): return self._mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataISPyBScreeningOutput", "setMosaicity", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
	def delMosaicity(self): self._mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getIOverSigma(self): return self._iOverSigma
	def setIOverSigma(self, iOverSigma):
		checkType("XSDataISPyBScreeningOutput", "setIOverSigma", iOverSigma, "XSDataDouble")
		self._iOverSigma = iOverSigma
	def delIOverSigma(self): self._iOverSigma = None
	# Properties
	iOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for iOverSigma")
	def getDiffractionRings(self): return self._diffractionRings
	def setDiffractionRings(self, diffractionRings):
		checkType("XSDataISPyBScreeningOutput", "setDiffractionRings", diffractionRings, "XSDataBoolean")
		self._diffractionRings = diffractionRings
	def delDiffractionRings(self): self._diffractionRings = None
	# Properties
	diffractionRings = property(getDiffractionRings, setDiffractionRings, delDiffractionRings, "Property for diffractionRings")
	def getScreeningSuccess(self): return self._screeningSuccess
	def setScreeningSuccess(self, screeningSuccess):
		checkType("XSDataISPyBScreeningOutput", "setScreeningSuccess", screeningSuccess, "XSDataBoolean")
		self._screeningSuccess = screeningSuccess
	def delScreeningSuccess(self): self._screeningSuccess = None
	# Properties
	screeningSuccess = property(getScreeningSuccess, setScreeningSuccess, delScreeningSuccess, "Property for screeningSuccess")
	def getMosaicityEstimated(self): return self._mosaicityEstimated
	def setMosaicityEstimated(self, mosaicityEstimated):
		checkType("XSDataISPyBScreeningOutput", "setMosaicityEstimated", mosaicityEstimated, "XSDataBoolean")
		self._mosaicityEstimated = mosaicityEstimated
	def delMosaicityEstimated(self): self._mosaicityEstimated = None
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
		if self._screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self._statusDescription is not None:
			self.statusDescription.export(outfile, level, name_='statusDescription')
		if self._rejectedReflections is not None:
			self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
		if self._resolutionObtained is not None:
			self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
		if self._spotDeviationR is not None:
			self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
		if self._spotDeviationTheta is not None:
			self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
		if self._beamShiftX is not None:
			self.beamShiftX.export(outfile, level, name_='beamShiftX')
		if self._beamShiftY is not None:
			self.beamShiftY.export(outfile, level, name_='beamShiftY')
		if self._numSpotsFound is not None:
			self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
		if self._numSpotsUsed is not None:
			self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
		if self._numSpotsRejected is not None:
			self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
		if self._mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self._iOverSigma is not None:
			self.iOverSigma.export(outfile, level, name_='iOverSigma')
		if self._diffractionRings is not None:
			self.diffractionRings.export(outfile, level, name_='diffractionRings')
		if self._screeningSuccess is not None:
			self.screeningSuccess.export(outfile, level, name_='screeningSuccess')
		else:
			warnEmptyAttribute("screeningSuccess", "XSDataBoolean")
		if self._mosaicityEstimated is not None:
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
		self._screeningOutputLatticeId = screeningOutputLatticeId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", screeningOutputId, "XSDataInteger")
		self._screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", spaceGroup, "XSDataString")
		self._spaceGroup = spaceGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", pointGroup, "XSDataString")
		self._pointGroup = pointGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", bravaisLattice, "XSDataString")
		self._bravaisLattice = bravaisLattice
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_x, "XSDataDouble")
		self._rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_y, "XSDataDouble")
		self._rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_z, "XSDataDouble")
		self._rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_x, "XSDataDouble")
		self._rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_y, "XSDataDouble")
		self._rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_z, "XSDataDouble")
		self._rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_x, "XSDataDouble")
		self._rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_y, "XSDataDouble")
		self._rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_z, "XSDataDouble")
		self._rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_a, "XSDataLength")
		self._unitCell_a = unitCell_a
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_alpha, "XSDataAngle")
		self._unitCell_alpha = unitCell_alpha
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_b, "XSDataLength")
		self._unitCell_b = unitCell_b
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_beta, "XSDataAngle")
		self._unitCell_beta = unitCell_beta
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_c, "XSDataLength")
		self._unitCell_c = unitCell_c
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_gamma, "XSDataAngle")
		self._unitCell_gamma = unitCell_gamma
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", timeStamp, "XSDataLength")
		self._timeStamp = timeStamp
	def getScreeningOutputLatticeId(self): return self._screeningOutputLatticeId
	def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputLatticeId", screeningOutputLatticeId, "XSDataInteger")
		self._screeningOutputLatticeId = screeningOutputLatticeId
	def delScreeningOutputLatticeId(self): self._screeningOutputLatticeId = None
	# Properties
	screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
	def getScreeningOutputId(self): return self._screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self._screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self._screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getSpaceGroup(self): return self._spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setSpaceGroup", spaceGroup, "XSDataString")
		self._spaceGroup = spaceGroup
	def delSpaceGroup(self): self._spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def getPointGroup(self): return self._pointGroup
	def setPointGroup(self, pointGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setPointGroup", pointGroup, "XSDataString")
		self._pointGroup = pointGroup
	def delPointGroup(self): self._pointGroup = None
	# Properties
	pointGroup = property(getPointGroup, setPointGroup, delPointGroup, "Property for pointGroup")
	def getBravaisLattice(self): return self._bravaisLattice
	def setBravaisLattice(self, bravaisLattice):
		checkType("XSDataISPyBScreeningOutputLattice", "setBravaisLattice", bravaisLattice, "XSDataString")
		self._bravaisLattice = bravaisLattice
	def delBravaisLattice(self): self._bravaisLattice = None
	# Properties
	bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
	def getRawOrientationMatrix_a_x(self): return self._rawOrientationMatrix_a_x
	def setRawOrientationMatrix_a_x(self, rawOrientationMatrix_a_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_x", rawOrientationMatrix_a_x, "XSDataDouble")
		self._rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
	def delRawOrientationMatrix_a_x(self): self._rawOrientationMatrix_a_x = None
	# Properties
	rawOrientationMatrix_a_x = property(getRawOrientationMatrix_a_x, setRawOrientationMatrix_a_x, delRawOrientationMatrix_a_x, "Property for rawOrientationMatrix_a_x")
	def getRawOrientationMatrix_a_y(self): return self._rawOrientationMatrix_a_y
	def setRawOrientationMatrix_a_y(self, rawOrientationMatrix_a_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_y", rawOrientationMatrix_a_y, "XSDataDouble")
		self._rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
	def delRawOrientationMatrix_a_y(self): self._rawOrientationMatrix_a_y = None
	# Properties
	rawOrientationMatrix_a_y = property(getRawOrientationMatrix_a_y, setRawOrientationMatrix_a_y, delRawOrientationMatrix_a_y, "Property for rawOrientationMatrix_a_y")
	def getRawOrientationMatrix_a_z(self): return self._rawOrientationMatrix_a_z
	def setRawOrientationMatrix_a_z(self, rawOrientationMatrix_a_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_z", rawOrientationMatrix_a_z, "XSDataDouble")
		self._rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
	def delRawOrientationMatrix_a_z(self): self._rawOrientationMatrix_a_z = None
	# Properties
	rawOrientationMatrix_a_z = property(getRawOrientationMatrix_a_z, setRawOrientationMatrix_a_z, delRawOrientationMatrix_a_z, "Property for rawOrientationMatrix_a_z")
	def getRawOrientationMatrix_b_x(self): return self._rawOrientationMatrix_b_x
	def setRawOrientationMatrix_b_x(self, rawOrientationMatrix_b_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_x", rawOrientationMatrix_b_x, "XSDataDouble")
		self._rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
	def delRawOrientationMatrix_b_x(self): self._rawOrientationMatrix_b_x = None
	# Properties
	rawOrientationMatrix_b_x = property(getRawOrientationMatrix_b_x, setRawOrientationMatrix_b_x, delRawOrientationMatrix_b_x, "Property for rawOrientationMatrix_b_x")
	def getRawOrientationMatrix_b_y(self): return self._rawOrientationMatrix_b_y
	def setRawOrientationMatrix_b_y(self, rawOrientationMatrix_b_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_y", rawOrientationMatrix_b_y, "XSDataDouble")
		self._rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
	def delRawOrientationMatrix_b_y(self): self._rawOrientationMatrix_b_y = None
	# Properties
	rawOrientationMatrix_b_y = property(getRawOrientationMatrix_b_y, setRawOrientationMatrix_b_y, delRawOrientationMatrix_b_y, "Property for rawOrientationMatrix_b_y")
	def getRawOrientationMatrix_b_z(self): return self._rawOrientationMatrix_b_z
	def setRawOrientationMatrix_b_z(self, rawOrientationMatrix_b_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_z", rawOrientationMatrix_b_z, "XSDataDouble")
		self._rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
	def delRawOrientationMatrix_b_z(self): self._rawOrientationMatrix_b_z = None
	# Properties
	rawOrientationMatrix_b_z = property(getRawOrientationMatrix_b_z, setRawOrientationMatrix_b_z, delRawOrientationMatrix_b_z, "Property for rawOrientationMatrix_b_z")
	def getRawOrientationMatrix_c_x(self): return self._rawOrientationMatrix_c_x
	def setRawOrientationMatrix_c_x(self, rawOrientationMatrix_c_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_x", rawOrientationMatrix_c_x, "XSDataDouble")
		self._rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
	def delRawOrientationMatrix_c_x(self): self._rawOrientationMatrix_c_x = None
	# Properties
	rawOrientationMatrix_c_x = property(getRawOrientationMatrix_c_x, setRawOrientationMatrix_c_x, delRawOrientationMatrix_c_x, "Property for rawOrientationMatrix_c_x")
	def getRawOrientationMatrix_c_y(self): return self._rawOrientationMatrix_c_y
	def setRawOrientationMatrix_c_y(self, rawOrientationMatrix_c_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_y", rawOrientationMatrix_c_y, "XSDataDouble")
		self._rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
	def delRawOrientationMatrix_c_y(self): self._rawOrientationMatrix_c_y = None
	# Properties
	rawOrientationMatrix_c_y = property(getRawOrientationMatrix_c_y, setRawOrientationMatrix_c_y, delRawOrientationMatrix_c_y, "Property for rawOrientationMatrix_c_y")
	def getRawOrientationMatrix_c_z(self): return self._rawOrientationMatrix_c_z
	def setRawOrientationMatrix_c_z(self, rawOrientationMatrix_c_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_z", rawOrientationMatrix_c_z, "XSDataDouble")
		self._rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
	def delRawOrientationMatrix_c_z(self): self._rawOrientationMatrix_c_z = None
	# Properties
	rawOrientationMatrix_c_z = property(getRawOrientationMatrix_c_z, setRawOrientationMatrix_c_z, delRawOrientationMatrix_c_z, "Property for rawOrientationMatrix_c_z")
	def getUnitCell_a(self): return self._unitCell_a
	def setUnitCell_a(self, unitCell_a):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_a", unitCell_a, "XSDataLength")
		self._unitCell_a = unitCell_a
	def delUnitCell_a(self): self._unitCell_a = None
	# Properties
	unitCell_a = property(getUnitCell_a, setUnitCell_a, delUnitCell_a, "Property for unitCell_a")
	def getUnitCell_alpha(self): return self._unitCell_alpha
	def setUnitCell_alpha(self, unitCell_alpha):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_alpha", unitCell_alpha, "XSDataAngle")
		self._unitCell_alpha = unitCell_alpha
	def delUnitCell_alpha(self): self._unitCell_alpha = None
	# Properties
	unitCell_alpha = property(getUnitCell_alpha, setUnitCell_alpha, delUnitCell_alpha, "Property for unitCell_alpha")
	def getUnitCell_b(self): return self._unitCell_b
	def setUnitCell_b(self, unitCell_b):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_b", unitCell_b, "XSDataLength")
		self._unitCell_b = unitCell_b
	def delUnitCell_b(self): self._unitCell_b = None
	# Properties
	unitCell_b = property(getUnitCell_b, setUnitCell_b, delUnitCell_b, "Property for unitCell_b")
	def getUnitCell_beta(self): return self._unitCell_beta
	def setUnitCell_beta(self, unitCell_beta):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_beta", unitCell_beta, "XSDataAngle")
		self._unitCell_beta = unitCell_beta
	def delUnitCell_beta(self): self._unitCell_beta = None
	# Properties
	unitCell_beta = property(getUnitCell_beta, setUnitCell_beta, delUnitCell_beta, "Property for unitCell_beta")
	def getUnitCell_c(self): return self._unitCell_c
	def setUnitCell_c(self, unitCell_c):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_c", unitCell_c, "XSDataLength")
		self._unitCell_c = unitCell_c
	def delUnitCell_c(self): self._unitCell_c = None
	# Properties
	unitCell_c = property(getUnitCell_c, setUnitCell_c, delUnitCell_c, "Property for unitCell_c")
	def getUnitCell_gamma(self): return self._unitCell_gamma
	def setUnitCell_gamma(self, unitCell_gamma):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_gamma", unitCell_gamma, "XSDataAngle")
		self._unitCell_gamma = unitCell_gamma
	def delUnitCell_gamma(self): self._unitCell_gamma = None
	# Properties
	unitCell_gamma = property(getUnitCell_gamma, setUnitCell_gamma, delUnitCell_gamma, "Property for unitCell_gamma")
	def getTimeStamp(self): return self._timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreeningOutputLattice", "setTimeStamp", timeStamp, "XSDataLength")
		self._timeStamp = timeStamp
	def delTimeStamp(self): self._timeStamp = None
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
		if self._screeningOutputLatticeId is not None:
			self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
		if self._screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self._spaceGroup is not None:
			self.spaceGroup.export(outfile, level, name_='spaceGroup')
		if self._pointGroup is not None:
			self.pointGroup.export(outfile, level, name_='pointGroup')
		if self._bravaisLattice is not None:
			self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
		if self._rawOrientationMatrix_a_x is not None:
			self.rawOrientationMatrix_a_x.export(outfile, level, name_='rawOrientationMatrix_a_x')
		if self._rawOrientationMatrix_a_y is not None:
			self.rawOrientationMatrix_a_y.export(outfile, level, name_='rawOrientationMatrix_a_y')
		if self._rawOrientationMatrix_a_z is not None:
			self.rawOrientationMatrix_a_z.export(outfile, level, name_='rawOrientationMatrix_a_z')
		if self._rawOrientationMatrix_b_x is not None:
			self.rawOrientationMatrix_b_x.export(outfile, level, name_='rawOrientationMatrix_b_x')
		if self._rawOrientationMatrix_b_y is not None:
			self.rawOrientationMatrix_b_y.export(outfile, level, name_='rawOrientationMatrix_b_y')
		if self._rawOrientationMatrix_b_z is not None:
			self.rawOrientationMatrix_b_z.export(outfile, level, name_='rawOrientationMatrix_b_z')
		if self._rawOrientationMatrix_c_x is not None:
			self.rawOrientationMatrix_c_x.export(outfile, level, name_='rawOrientationMatrix_c_x')
		if self._rawOrientationMatrix_c_y is not None:
			self.rawOrientationMatrix_c_y.export(outfile, level, name_='rawOrientationMatrix_c_y')
		if self._rawOrientationMatrix_c_z is not None:
			self.rawOrientationMatrix_c_z.export(outfile, level, name_='rawOrientationMatrix_c_z')
		if self._unitCell_a is not None:
			self.unitCell_a.export(outfile, level, name_='unitCell_a')
		else:
			warnEmptyAttribute("unitCell_a", "XSDataLength")
		if self._unitCell_alpha is not None:
			self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
		else:
			warnEmptyAttribute("unitCell_alpha", "XSDataAngle")
		if self._unitCell_b is not None:
			self.unitCell_b.export(outfile, level, name_='unitCell_b')
		else:
			warnEmptyAttribute("unitCell_b", "XSDataLength")
		if self._unitCell_beta is not None:
			self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
		else:
			warnEmptyAttribute("unitCell_beta", "XSDataAngle")
		if self._unitCell_c is not None:
			self.unitCell_c.export(outfile, level, name_='unitCell_c')
		else:
			warnEmptyAttribute("unitCell_c", "XSDataLength")
		if self._unitCell_gamma is not None:
			self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
		else:
			warnEmptyAttribute("unitCell_gamma", "XSDataAngle")
		if self._timeStamp is not None:
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
		self._screeningRankId = screeningRankId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningRankSetId, "XSDataInteger")
		self._screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningId, "XSDataInteger")
		self._screeningId = screeningId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankValue, "XSDataDouble")
		self._rankValue = rankValue
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankInformation, "XSDataString")
		self._rankInformation = rankInformation
	def getScreeningRankId(self): return self._screeningRankId
	def setScreeningRankId(self, screeningRankId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankId", screeningRankId, "XSDataInteger")
		self._screeningRankId = screeningRankId
	def delScreeningRankId(self): self._screeningRankId = None
	# Properties
	screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
	def getScreeningRankSetId(self): return self._screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self._screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self._screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningRank", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getRankValue(self): return self._rankValue
	def setRankValue(self, rankValue):
		checkType("XSDataISPyBScreeningRank", "setRankValue", rankValue, "XSDataDouble")
		self._rankValue = rankValue
	def delRankValue(self): self._rankValue = None
	# Properties
	rankValue = property(getRankValue, setRankValue, delRankValue, "Property for rankValue")
	def getRankInformation(self): return self._rankInformation
	def setRankInformation(self, rankInformation):
		checkType("XSDataISPyBScreeningRank", "setRankInformation", rankInformation, "XSDataString")
		self._rankInformation = rankInformation
	def delRankInformation(self): self._rankInformation = None
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
		if self._screeningRankId is not None:
			self.screeningRankId.export(outfile, level, name_='screeningRankId')
		if self._screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self._screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		if self._rankValue is not None:
			self.rankValue.export(outfile, level, name_='rankValue')
		else:
			warnEmptyAttribute("rankValue", "XSDataDouble")
		if self._rankInformation is not None:
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
		self._screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankEngine, "XSDataString")
		self._rankEngine = rankEngine
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingProjectFileName, "XSDataString")
		self._rankingProjectFileName = rankingProjectFileName
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingSummaryFileName, "XSDataString")
		self._rankingSummaryFileName = rankingSummaryFileName
	def getScreeningRankSetId(self): return self._screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRankSet", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self._screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self._screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getRankEngine(self): return self._rankEngine
	def setRankEngine(self, rankEngine):
		checkType("XSDataISPyBScreeningRankSet", "setRankEngine", rankEngine, "XSDataString")
		self._rankEngine = rankEngine
	def delRankEngine(self): self._rankEngine = None
	# Properties
	rankEngine = property(getRankEngine, setRankEngine, delRankEngine, "Property for rankEngine")
	def getRankingProjectFileName(self): return self._rankingProjectFileName
	def setRankingProjectFileName(self, rankingProjectFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingProjectFileName", rankingProjectFileName, "XSDataString")
		self._rankingProjectFileName = rankingProjectFileName
	def delRankingProjectFileName(self): self._rankingProjectFileName = None
	# Properties
	rankingProjectFileName = property(getRankingProjectFileName, setRankingProjectFileName, delRankingProjectFileName, "Property for rankingProjectFileName")
	def getRankingSummaryFileName(self): return self._rankingSummaryFileName
	def setRankingSummaryFileName(self, rankingSummaryFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingSummaryFileName", rankingSummaryFileName, "XSDataString")
		self._rankingSummaryFileName = rankingSummaryFileName
	def delRankingSummaryFileName(self): self._rankingSummaryFileName = None
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
		if self._screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self._rankEngine is not None:
			self.rankEngine.export(outfile, level, name_='rankEngine')
		else:
			warnEmptyAttribute("rankEngine", "XSDataString")
		if self._rankingProjectFileName is not None:
			self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
		else:
			warnEmptyAttribute("rankingProjectFileName", "XSDataString")
		if self._rankingSummaryFileName is not None:
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
		self._screeningStrategyId = screeningStrategyId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", screeningOutputId, "XSDataInteger")
		self._screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiStart, "XSDataDouble")
		self._phiStart = phiStart
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiEnd, "XSDataDouble")
		self._phiEnd = phiEnd
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rotation, "XSDataDouble")
		self._rotation = rotation
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", exposureTime, "XSDataDouble")
		self._exposureTime = exposureTime
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", resolution, "XSDataDouble")
		self._resolution = resolution
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", anomalous, "XSDataBoolean")
		self._anomalous = anomalous
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", program, "XSDataString")
		self._program = program
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", transmission, "XSDataDouble")
		self._transmission = transmission
	def getScreeningStrategyId(self): return self._screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self._screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self._screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getScreeningOutputId(self): return self._screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self._screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self._screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getPhiStart(self): return self._phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataISPyBScreeningStrategy", "setPhiStart", phiStart, "XSDataDouble")
		self._phiStart = phiStart
	def delPhiStart(self): self._phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getPhiEnd(self): return self._phiEnd
	def setPhiEnd(self, phiEnd):
		checkType("XSDataISPyBScreeningStrategy", "setPhiEnd", phiEnd, "XSDataDouble")
		self._phiEnd = phiEnd
	def delPhiEnd(self): self._phiEnd = None
	# Properties
	phiEnd = property(getPhiEnd, setPhiEnd, delPhiEnd, "Property for phiEnd")
	def getRotation(self): return self._rotation
	def setRotation(self, rotation):
		checkType("XSDataISPyBScreeningStrategy", "setRotation", rotation, "XSDataDouble")
		self._rotation = rotation
	def delRotation(self): self._rotation = None
	# Properties
	rotation = property(getRotation, setRotation, delRotation, "Property for rotation")
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBScreeningStrategy", "setExposureTime", exposureTime, "XSDataDouble")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategy", "setResolution", resolution, "XSDataDouble")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategy", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self._multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategy", "setMultiplicity", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
	def delMultiplicity(self): self._multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getAnomalous(self): return self._anomalous
	def setAnomalous(self, anomalous):
		checkType("XSDataISPyBScreeningStrategy", "setAnomalous", anomalous, "XSDataBoolean")
		self._anomalous = anomalous
	def delAnomalous(self): self._anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
	def getProgram(self): return self._program
	def setProgram(self, program):
		checkType("XSDataISPyBScreeningStrategy", "setProgram", program, "XSDataString")
		self._program = program
	def delProgram(self): self._program = None
	# Properties
	program = property(getProgram, setProgram, delProgram, "Property for program")
	def getRankingResolution(self): return self._rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataISPyBScreeningStrategy", "setRankingResolution", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
	def delRankingResolution(self): self._rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBScreeningStrategy", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
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
		if self._screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		if self._screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self._phiStart is not None:
			self.phiStart.export(outfile, level, name_='phiStart')
		if self._phiEnd is not None:
			self.phiEnd.export(outfile, level, name_='phiEnd')
		if self._rotation is not None:
			self.rotation.export(outfile, level, name_='rotation')
		if self._exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self._resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		if self._multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		if self._anomalous is not None:
			self.anomalous.export(outfile, level, name_='anomalous')
		if self._program is not None:
			self.program.export(outfile, level, name_='program')
		if self._rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
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
		self._screeningStrategy = screeningStrategy
		if screeningStrategyWedgeContainer is None:
			self._screeningStrategyWedgeContainer = []
		else:
			checkType("XSDataISPyBScreeningStrategyContainer", "Constructor of XSDataISPyBScreeningStrategyContainer", screeningStrategyWedgeContainer, "list")
			self._screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
	def getScreeningStrategy(self): return self._screeningStrategy
	def setScreeningStrategy(self, screeningStrategy):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategy", screeningStrategy, "XSDataISPyBScreeningStrategy")
		self._screeningStrategy = screeningStrategy
	def delScreeningStrategy(self): self._screeningStrategy = None
	# Properties
	screeningStrategy = property(getScreeningStrategy, setScreeningStrategy, delScreeningStrategy, "Property for screeningStrategy")
	def getScreeningStrategyWedgeContainer(self): return self._screeningStrategyWedgeContainer
	def setScreeningStrategyWedgeContainer(self, screeningStrategyWedgeContainer):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", screeningStrategyWedgeContainer, "list")
		self._screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
	def delScreeningStrategyWedgeContainer(self): self._screeningStrategyWedgeContainer = None
	# Properties
	screeningStrategyWedgeContainer = property(getScreeningStrategyWedgeContainer, setScreeningStrategyWedgeContainer, delScreeningStrategyWedgeContainer, "Property for screeningStrategyWedgeContainer")
	def addScreeningStrategyWedgeContainer(self, value):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", value, "XSDataISPyBScreeningStrategyWedgeContainer")
		self._screeningStrategyWedgeContainer.append(value)
	def insertScreeningStrategyWedgeContainer(self, index, value):
		checkType("XSDataISPyBScreeningStrategyContainer", "setScreeningStrategyWedgeContainer", value, "XSDataISPyBScreeningStrategyWedgeContainer")
		self._screeningStrategyWedgeContainer[index] = value
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._screeningStrategy is not None:
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
		self._screeningOutput = screeningOutput
		if screeningOutputLattice is None:
			self._screeningOutputLattice = []
		else:
			checkType("XSDataISPyBScreeningOutputContainer", "Constructor of XSDataISPyBScreeningOutputContainer", screeningOutputLattice, "list")
			self._screeningOutputLattice = screeningOutputLattice
		if screeningStrategyContainer is None:
			self._screeningStrategyContainer = []
		else:
			checkType("XSDataISPyBScreeningOutputContainer", "Constructor of XSDataISPyBScreeningOutputContainer", screeningStrategyContainer, "list")
			self._screeningStrategyContainer = screeningStrategyContainer
	def getScreeningOutput(self): return self._screeningOutput
	def setScreeningOutput(self, screeningOutput):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutput", screeningOutput, "XSDataISPyBScreeningOutput")
		self._screeningOutput = screeningOutput
	def delScreeningOutput(self): self._screeningOutput = None
	# Properties
	screeningOutput = property(getScreeningOutput, setScreeningOutput, delScreeningOutput, "Property for screeningOutput")
	def getScreeningOutputLattice(self): return self._screeningOutputLattice
	def setScreeningOutputLattice(self, screeningOutputLattice):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", screeningOutputLattice, "list")
		self._screeningOutputLattice = screeningOutputLattice
	def delScreeningOutputLattice(self): self._screeningOutputLattice = None
	# Properties
	screeningOutputLattice = property(getScreeningOutputLattice, setScreeningOutputLattice, delScreeningOutputLattice, "Property for screeningOutputLattice")
	def addScreeningOutputLattice(self, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", value, "XSDataISPyBScreeningOutputLattice")
		self._screeningOutputLattice.append(value)
	def insertScreeningOutputLattice(self, index, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningOutputLattice", value, "XSDataISPyBScreeningOutputLattice")
		self._screeningOutputLattice[index] = value
	def getScreeningStrategyContainer(self): return self._screeningStrategyContainer
	def setScreeningStrategyContainer(self, screeningStrategyContainer):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", screeningStrategyContainer, "list")
		self._screeningStrategyContainer = screeningStrategyContainer
	def delScreeningStrategyContainer(self): self._screeningStrategyContainer = None
	# Properties
	screeningStrategyContainer = property(getScreeningStrategyContainer, setScreeningStrategyContainer, delScreeningStrategyContainer, "Property for screeningStrategyContainer")
	def addScreeningStrategyContainer(self, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", value, "XSDataISPyBScreeningStrategyContainer")
		self._screeningStrategyContainer.append(value)
	def insertScreeningStrategyContainer(self, index, value):
		checkType("XSDataISPyBScreeningOutputContainer", "setScreeningStrategyContainer", value, "XSDataISPyBScreeningStrategyContainer")
		self._screeningStrategyContainer[index] = value
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._screeningOutput is not None:
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
		self._screeningStrategySubWedgeId = screeningStrategySubWedgeId
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", screeningStrategyWedgeId, "XSDataInteger")
		self._screeningStrategyWedgeId = screeningStrategyWedgeId
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", rotationAxis, "XSDataString")
		self._rotationAxis = rotationAxis
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", axisStart, "XSDataAngle")
		self._axisStart = axisStart
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", axisEnd, "XSDataAngle")
		self._axisEnd = axisEnd
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", transmission, "XSDataDouble")
		self._transmission = transmission
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", oscillationRange, "XSDataAngle")
		self._oscillationRange = oscillationRange
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", resolution, "XSDataDouble")
		self._resolution = resolution
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", doseTotal, "XSDataDouble")
		self._doseTotal = doseTotal
		checkType("XSDataISPyBScreeningStrategySubWedge", "Constructor of XSDataISPyBScreeningStrategySubWedge", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
	def getScreeningStrategySubWedgeId(self): return self._screeningStrategySubWedgeId
	def setScreeningStrategySubWedgeId(self, screeningStrategySubWedgeId):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setScreeningStrategySubWedgeId", screeningStrategySubWedgeId, "XSDataInteger")
		self._screeningStrategySubWedgeId = screeningStrategySubWedgeId
	def delScreeningStrategySubWedgeId(self): self._screeningStrategySubWedgeId = None
	# Properties
	screeningStrategySubWedgeId = property(getScreeningStrategySubWedgeId, setScreeningStrategySubWedgeId, delScreeningStrategySubWedgeId, "Property for screeningStrategySubWedgeId")
	def getScreeningStrategyWedgeId(self): return self._screeningStrategyWedgeId
	def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setScreeningStrategyWedgeId", screeningStrategyWedgeId, "XSDataInteger")
		self._screeningStrategyWedgeId = screeningStrategyWedgeId
	def delScreeningStrategyWedgeId(self): self._screeningStrategyWedgeId = None
	# Properties
	screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
	def getSubWedgeNumber(self): return self._subWedgeNumber
	def setSubWedgeNumber(self, subWedgeNumber):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setSubWedgeNumber", subWedgeNumber, "XSDataInteger")
		self._subWedgeNumber = subWedgeNumber
	def delSubWedgeNumber(self): self._subWedgeNumber = None
	# Properties
	subWedgeNumber = property(getSubWedgeNumber, setSubWedgeNumber, delSubWedgeNumber, "Property for subWedgeNumber")
	def getRotationAxis(self): return self._rotationAxis
	def setRotationAxis(self, rotationAxis):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setRotationAxis", rotationAxis, "XSDataString")
		self._rotationAxis = rotationAxis
	def delRotationAxis(self): self._rotationAxis = None
	# Properties
	rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
	def getAxisStart(self): return self._axisStart
	def setAxisStart(self, axisStart):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setAxisStart", axisStart, "XSDataAngle")
		self._axisStart = axisStart
	def delAxisStart(self): self._axisStart = None
	# Properties
	axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
	def getAxisEnd(self): return self._axisEnd
	def setAxisEnd(self, axisEnd):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setAxisEnd", axisEnd, "XSDataAngle")
		self._axisEnd = axisEnd
	def delAxisEnd(self): self._axisEnd = None
	# Properties
	axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setExposureTime", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getOscillationRange(self): return self._oscillationRange
	def setOscillationRange(self, oscillationRange):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setOscillationRange", oscillationRange, "XSDataAngle")
		self._oscillationRange = oscillationRange
	def delOscillationRange(self): self._oscillationRange = None
	# Properties
	oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self._multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setMultiplicity", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
	def delMultiplicity(self): self._multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setResolution", resolution, "XSDataDouble")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getDoseTotal(self): return self._doseTotal
	def setDoseTotal(self, doseTotal):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setDoseTotal", doseTotal, "XSDataDouble")
		self._doseTotal = doseTotal
	def delDoseTotal(self): self._doseTotal = None
	# Properties
	doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
	def getNumberOfImages(self): return self._numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBScreeningStrategySubWedge", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
	def delNumberOfImages(self): self._numberOfImages = None
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
		if self._screeningStrategySubWedgeId is not None:
			self.screeningStrategySubWedgeId.export(outfile, level, name_='screeningStrategySubWedgeId')
		if self._screeningStrategyWedgeId is not None:
			self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
		else:
			warnEmptyAttribute("screeningStrategyWedgeId", "XSDataInteger")
		if self._subWedgeNumber is not None:
			self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
		else:
			warnEmptyAttribute("subWedgeNumber", "XSDataInteger")
		if self._rotationAxis is not None:
			self.rotationAxis.export(outfile, level, name_='rotationAxis')
		if self._axisStart is not None:
			self.axisStart.export(outfile, level, name_='axisStart')
		else:
			warnEmptyAttribute("axisStart", "XSDataAngle")
		if self._axisEnd is not None:
			self.axisEnd.export(outfile, level, name_='axisEnd')
		else:
			warnEmptyAttribute("axisEnd", "XSDataAngle")
		if self._exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataTime")
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self._oscillationRange is not None:
			self.oscillationRange.export(outfile, level, name_='oscillationRange')
		else:
			warnEmptyAttribute("oscillationRange", "XSDataAngle")
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		if self._multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		if self._resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		if self._doseTotal is not None:
			self.doseTotal.export(outfile, level, name_='doseTotal')
		if self._numberOfImages is not None:
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
		self._screeningStrategyWedgeId = screeningStrategyWedgeId
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", screeningStrategyId, "XSDataInteger")
		self._screeningStrategyId = screeningStrategyId
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", wedgeNumber, "XSDataInteger")
		self._wedgeNumber = wedgeNumber
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", resolution, "XSDataDouble")
		self._resolution = resolution
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", doseTotal, "XSDataDouble")
		self._doseTotal = doseTotal
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", phi, "XSDataDouble")
		self._phi = phi
		checkType("XSDataISPyBScreeningStrategyWedge", "Constructor of XSDataISPyBScreeningStrategyWedge", kappa, "XSDataDouble")
		self._kappa = kappa
	def getScreeningStrategyWedgeId(self): return self._screeningStrategyWedgeId
	def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
		checkType("XSDataISPyBScreeningStrategyWedge", "setScreeningStrategyWedgeId", screeningStrategyWedgeId, "XSDataInteger")
		self._screeningStrategyWedgeId = screeningStrategyWedgeId
	def delScreeningStrategyWedgeId(self): self._screeningStrategyWedgeId = None
	# Properties
	screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
	def getScreeningStrategyId(self): return self._screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataISPyBScreeningStrategyWedge", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self._screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self._screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getWedgeNumber(self): return self._wedgeNumber
	def setWedgeNumber(self, wedgeNumber):
		checkType("XSDataISPyBScreeningStrategyWedge", "setWedgeNumber", wedgeNumber, "XSDataInteger")
		self._wedgeNumber = wedgeNumber
	def delWedgeNumber(self): self._wedgeNumber = None
	# Properties
	wedgeNumber = property(getWedgeNumber, setWedgeNumber, delWedgeNumber, "Property for wedgeNumber")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategyWedge", "setResolution", resolution, "XSDataDouble")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategyWedge", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self._multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategyWedge", "setMultiplicity", multiplicity, "XSDataDouble")
		self._multiplicity = multiplicity
	def delMultiplicity(self): self._multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getDoseTotal(self): return self._doseTotal
	def setDoseTotal(self, doseTotal):
		checkType("XSDataISPyBScreeningStrategyWedge", "setDoseTotal", doseTotal, "XSDataDouble")
		self._doseTotal = doseTotal
	def delDoseTotal(self): self._doseTotal = None
	# Properties
	doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
	def getNumberOfImages(self): return self._numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataISPyBScreeningStrategyWedge", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
	def delNumberOfImages(self): self._numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getPhi(self): return self._phi
	def setPhi(self, phi):
		checkType("XSDataISPyBScreeningStrategyWedge", "setPhi", phi, "XSDataDouble")
		self._phi = phi
	def delPhi(self): self._phi = None
	# Properties
	phi = property(getPhi, setPhi, delPhi, "Property for phi")
	def getKappa(self): return self._kappa
	def setKappa(self, kappa):
		checkType("XSDataISPyBScreeningStrategyWedge", "setKappa", kappa, "XSDataDouble")
		self._kappa = kappa
	def delKappa(self): self._kappa = None
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
		if self._screeningStrategyWedgeId is not None:
			self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
		if self._screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		else:
			warnEmptyAttribute("screeningStrategyId", "XSDataInteger")
		if self._wedgeNumber is not None:
			self.wedgeNumber.export(outfile, level, name_='wedgeNumber')
		else:
			warnEmptyAttribute("wedgeNumber", "XSDataInteger")
		if self._resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self._multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		else:
			warnEmptyAttribute("multiplicity", "XSDataDouble")
		if self._doseTotal is not None:
			self.doseTotal.export(outfile, level, name_='doseTotal')
		if self._numberOfImages is not None:
			self.numberOfImages.export(outfile, level, name_='numberOfImages')
		else:
			warnEmptyAttribute("numberOfImages", "XSDataInteger")
		if self._phi is not None:
			self.phi.export(outfile, level, name_='phi')
		if self._kappa is not None:
			self.kappa.export(outfile, level, name_='kappa')
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
			self._screeningStrategySubWedge = []
		else:
			checkType("XSDataISPyBScreeningStrategyWedgeContainer", "Constructor of XSDataISPyBScreeningStrategyWedgeContainer", screeningStrategySubWedge, "list")
			self._screeningStrategySubWedge = screeningStrategySubWedge
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "Constructor of XSDataISPyBScreeningStrategyWedgeContainer", screeningStrategyWedge, "XSDataISPyBScreeningStrategyWedge")
		self._screeningStrategyWedge = screeningStrategyWedge
	def getScreeningStrategySubWedge(self): return self._screeningStrategySubWedge
	def setScreeningStrategySubWedge(self, screeningStrategySubWedge):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", screeningStrategySubWedge, "list")
		self._screeningStrategySubWedge = screeningStrategySubWedge
	def delScreeningStrategySubWedge(self): self._screeningStrategySubWedge = None
	# Properties
	screeningStrategySubWedge = property(getScreeningStrategySubWedge, setScreeningStrategySubWedge, delScreeningStrategySubWedge, "Property for screeningStrategySubWedge")
	def addScreeningStrategySubWedge(self, value):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", value, "XSDataISPyBScreeningStrategySubWedge")
		self._screeningStrategySubWedge.append(value)
	def insertScreeningStrategySubWedge(self, index, value):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategySubWedge", value, "XSDataISPyBScreeningStrategySubWedge")
		self._screeningStrategySubWedge[index] = value
	def getScreeningStrategyWedge(self): return self._screeningStrategyWedge
	def setScreeningStrategyWedge(self, screeningStrategyWedge):
		checkType("XSDataISPyBScreeningStrategyWedgeContainer", "setScreeningStrategyWedge", screeningStrategyWedge, "XSDataISPyBScreeningStrategyWedge")
		self._screeningStrategyWedge = screeningStrategyWedge
	def delScreeningStrategyWedge(self): self._screeningStrategyWedge = None
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
		if self._screeningStrategyWedge is not None:
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
		self._diffractionPlan = diffractionPlan
		if file is None:
			self._file = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", file, "list")
			self._file = file
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", image, "XSDataISPyBImage")
		self._image = image
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screening, "XSDataISPyBScreening")
		self._screening = screening
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningInput, "XSDataISPyBScreeningInput")
		self._screeningInput = screeningInput
		if screeningOutputContainer is None:
			self._screeningOutputContainer = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningOutputContainer, "list")
			self._screeningOutputContainer = screeningOutputContainer
		if screeningRank is None:
			self._screeningRank = []
		else:
			checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningRank, "list")
			self._screeningRank = screeningRank
		checkType("XSDataInputISPyBStoreScreening", "Constructor of XSDataInputISPyBStoreScreening", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self._screeningRankSet = screeningRankSet
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputISPyBStoreScreening", "setDiffractionPlan", diffractionPlan, "XSDataISPyBDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getFile(self): return self._file
	def setFile(self, file):
		checkType("XSDataInputISPyBStoreScreening", "setFile", file, "list")
		self._file = file
	def delFile(self): self._file = None
	# Properties
	file = property(getFile, setFile, delFile, "Property for file")
	def addFile(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setFile", value, "XSDataISPyBScreeningFile")
		self._file.append(value)
	def insertFile(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setFile", value, "XSDataISPyBScreeningFile")
		self._file[index] = value
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataInputISPyBStoreScreening", "setImage", image, "XSDataISPyBImage")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getScreening(self): return self._screening
	def setScreening(self, screening):
		checkType("XSDataInputISPyBStoreScreening", "setScreening", screening, "XSDataISPyBScreening")
		self._screening = screening
	def delScreening(self): self._screening = None
	# Properties
	screening = property(getScreening, setScreening, delScreening, "Property for screening")
	def getScreeningInput(self): return self._screeningInput
	def setScreeningInput(self, screeningInput):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningInput", screeningInput, "XSDataISPyBScreeningInput")
		self._screeningInput = screeningInput
	def delScreeningInput(self): self._screeningInput = None
	# Properties
	screeningInput = property(getScreeningInput, setScreeningInput, delScreeningInput, "Property for screeningInput")
	def getScreeningOutputContainer(self): return self._screeningOutputContainer
	def setScreeningOutputContainer(self, screeningOutputContainer):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", screeningOutputContainer, "list")
		self._screeningOutputContainer = screeningOutputContainer
	def delScreeningOutputContainer(self): self._screeningOutputContainer = None
	# Properties
	screeningOutputContainer = property(getScreeningOutputContainer, setScreeningOutputContainer, delScreeningOutputContainer, "Property for screeningOutputContainer")
	def addScreeningOutputContainer(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", value, "XSDataISPyBScreeningOutputContainer")
		self._screeningOutputContainer.append(value)
	def insertScreeningOutputContainer(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningOutputContainer", value, "XSDataISPyBScreeningOutputContainer")
		self._screeningOutputContainer[index] = value
	def getScreeningRank(self): return self._screeningRank
	def setScreeningRank(self, screeningRank):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", screeningRank, "list")
		self._screeningRank = screeningRank
	def delScreeningRank(self): self._screeningRank = None
	# Properties
	screeningRank = property(getScreeningRank, setScreeningRank, delScreeningRank, "Property for screeningRank")
	def addScreeningRank(self, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", value, "XSDataISPyBScreeningRank")
		self._screeningRank.append(value)
	def insertScreeningRank(self, index, value):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRank", value, "XSDataISPyBScreeningRank")
		self._screeningRank[index] = value
	def getScreeningRankSet(self): return self._screeningRankSet
	def setScreeningRankSet(self, screeningRankSet):
		checkType("XSDataInputISPyBStoreScreening", "setScreeningRankSet", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self._screeningRankSet = screeningRankSet
	def delScreeningRankSet(self): self._screeningRankSet = None
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
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		for file_ in self.getFile():
			file_.export(outfile, level, name_='file')
		if self._image is not None:
			self.image.export(outfile, level, name_='image')
		if self._screening is not None:
			self.screening.export(outfile, level, name_='screening')
		if self._screeningInput is not None:
			self.screeningInput.export(outfile, level, name_='screeningInput')
		for screeningOutputContainer_ in self.getScreeningOutputContainer():
			screeningOutputContainer_.export(outfile, level, name_='screeningOutputContainer')
		for screeningRank_ in self.getScreeningRank():
			screeningRank_.export(outfile, level, name_='screeningRank')
		if self._screeningRankSet is not None:
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
		self._image = image
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataInputRetrieveDataCollection", "setImage", image, "XSDataImage")
		self._image = image
	def delImage(self): self._image = None
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
		if self._image is not None:
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
		self._AutoProcContainer = AutoProcContainer
	def getAutoProcContainer(self): return self._AutoProcContainer
	def setAutoProcContainer(self, AutoProcContainer):
		checkType("XSDataInputStoreAutoProc", "setAutoProcContainer", AutoProcContainer, "AutoProcContainer")
		self._AutoProcContainer = AutoProcContainer
	def delAutoProcContainer(self): self._AutoProcContainer = None
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
		if self._AutoProcContainer is not None:
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
		self._dataCollection = dataCollection
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataInputStoreDataCollection", "setDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
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
		if self._dataCollection is not None:
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
		self._imageQualityIndicators = imageQualityIndicators
	def getImageQualityIndicators(self): return self._imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataInputStoreImageQualityIndicators", "setImageQualityIndicators", imageQualityIndicators, "XSDataISPyBImageQualityIndicators")
		self._imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self._imageQualityIndicators = None
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
		if self._imageQualityIndicators is not None:
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
		self._screeningId = screeningId
	def getScreeningId(self): return self._screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataResultISPyBStoreScreening", "setScreeningId", screeningId, "XSDataInteger")
		self._screeningId = screeningId
	def delScreeningId(self): self._screeningId = None
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
		self._dataCollection = dataCollection
	def getDataCollection(self): return self._dataCollection
	def setDataCollection(self, dataCollection):
		checkType("XSDataResultRetrieveDataCollection", "setDataCollection", dataCollection, "XSDataISPyBDataCollection")
		self._dataCollection = dataCollection
	def delDataCollection(self): self._dataCollection = None
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
		if self._dataCollection is not None:
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
		self._autoProcId = autoProcId
	def getAutoProcId(self): return self._autoProcId
	def setAutoProcId(self, autoProcId):
		checkType("XSDataResultStoreAutoProc", "setAutoProcId", autoProcId, "XSDataInteger")
		self._autoProcId = autoProcId
	def delAutoProcId(self): self._autoProcId = None
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
		if self._autoProcId is not None:
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
		self._dataCollectionId = dataCollectionId
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataResultStoreDataCollection", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
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
		if self._dataCollectionId is not None:
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
		self._imageQualityIndicatorsId = imageQualityIndicatorsId
	def getImageQualityIndicatorsId(self): return self._imageQualityIndicatorsId
	def setImageQualityIndicatorsId(self, imageQualityIndicatorsId):
		checkType("XSDataResultStoreImageQualityIndicators", "setImageQualityIndicatorsId", imageQualityIndicatorsId, "XSDataInteger")
		self._imageQualityIndicatorsId = imageQualityIndicatorsId
	def delImageQualityIndicatorsId(self): self._imageQualityIndicatorsId = None
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
		if self._imageQualityIndicatorsId is not None:
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



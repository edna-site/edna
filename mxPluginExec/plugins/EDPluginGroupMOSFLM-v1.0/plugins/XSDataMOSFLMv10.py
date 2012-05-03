#!/usr/bin/env python

#
# Generated Thu May 3 11:58::53 2012 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataAngle
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataMatrixDouble
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataImage
	from XSDataCommon import XSDataLength
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
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


class XSDataMOSFLMDetector(object):
	def __init__(self, type=None, pixelSizeY=None, pixelSizeX=None, numberPixelY=None, numberPixelX=None):
	
	
		checkType("XSDataMOSFLMDetector", "Constructor of XSDataMOSFLMDetector", numberPixelX, "XSDataInteger")
		self._numberPixelX = numberPixelX
		checkType("XSDataMOSFLMDetector", "Constructor of XSDataMOSFLMDetector", numberPixelY, "XSDataInteger")
		self._numberPixelY = numberPixelY
		checkType("XSDataMOSFLMDetector", "Constructor of XSDataMOSFLMDetector", pixelSizeX, "XSDataLength")
		self._pixelSizeX = pixelSizeX
		checkType("XSDataMOSFLMDetector", "Constructor of XSDataMOSFLMDetector", pixelSizeY, "XSDataLength")
		self._pixelSizeY = pixelSizeY
		checkType("XSDataMOSFLMDetector", "Constructor of XSDataMOSFLMDetector", type, "XSDataString")
		self._type = type
	def getNumberPixelX(self): return self._numberPixelX
	def setNumberPixelX(self, numberPixelX):
		checkType("XSDataMOSFLMDetector", "setNumberPixelX", numberPixelX, "XSDataInteger")
		self._numberPixelX = numberPixelX
	def delNumberPixelX(self): self._numberPixelX = None
	# Properties
	numberPixelX = property(getNumberPixelX, setNumberPixelX, delNumberPixelX, "Property for numberPixelX")
	def getNumberPixelY(self): return self._numberPixelY
	def setNumberPixelY(self, numberPixelY):
		checkType("XSDataMOSFLMDetector", "setNumberPixelY", numberPixelY, "XSDataInteger")
		self._numberPixelY = numberPixelY
	def delNumberPixelY(self): self._numberPixelY = None
	# Properties
	numberPixelY = property(getNumberPixelY, setNumberPixelY, delNumberPixelY, "Property for numberPixelY")
	def getPixelSizeX(self): return self._pixelSizeX
	def setPixelSizeX(self, pixelSizeX):
		checkType("XSDataMOSFLMDetector", "setPixelSizeX", pixelSizeX, "XSDataLength")
		self._pixelSizeX = pixelSizeX
	def delPixelSizeX(self): self._pixelSizeX = None
	# Properties
	pixelSizeX = property(getPixelSizeX, setPixelSizeX, delPixelSizeX, "Property for pixelSizeX")
	def getPixelSizeY(self): return self._pixelSizeY
	def setPixelSizeY(self, pixelSizeY):
		checkType("XSDataMOSFLMDetector", "setPixelSizeY", pixelSizeY, "XSDataLength")
		self._pixelSizeY = pixelSizeY
	def delPixelSizeY(self): self._pixelSizeY = None
	# Properties
	pixelSizeY = property(getPixelSizeY, setPixelSizeY, delPixelSizeY, "Property for pixelSizeY")
	def getType(self): return self._type
	def setType(self, type):
		checkType("XSDataMOSFLMDetector", "setType", type, "XSDataString")
		self._type = type
	def delType(self): self._type = None
	# Properties
	type = property(getType, setType, delType, "Property for type")
	def export(self, outfile, level, name_='XSDataMOSFLMDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMDetector'):
		pass
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
			nodeName_ == 'type':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setType(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMDetector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMDetector' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMDetector is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMDetector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMDetector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMDetector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMDetector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMDetector

class XSDataCell(XSData):
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

class XSDataMOSFLMBeamPosition(XSData):
	def __init__(self, y=None, x=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMBeamPosition", "Constructor of XSDataMOSFLMBeamPosition", x, "XSDataLength")
		self._x = x
		checkType("XSDataMOSFLMBeamPosition", "Constructor of XSDataMOSFLMBeamPosition", y, "XSDataLength")
		self._y = y
	def getX(self): return self._x
	def setX(self, x):
		checkType("XSDataMOSFLMBeamPosition", "setX", x, "XSDataLength")
		self._x = x
	def delX(self): self._x = None
	# Properties
	x = property(getX, setX, delX, "Property for x")
	def getY(self): return self._y
	def setY(self, y):
		checkType("XSDataMOSFLMBeamPosition", "setY", y, "XSDataLength")
		self._y = y
	def delY(self): self._y = None
	# Properties
	y = property(getY, setY, delY, "Property for y")
	def export(self, outfile, level, name_='XSDataMOSFLMBeamPosition'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMBeamPosition'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._x is not None:
			self.x.export(outfile, level, name_='x')
		else:
			warnEmptyAttribute("x", "XSDataLength")
		if self._y is not None:
			self.y.export(outfile, level, name_='y')
		else:
			warnEmptyAttribute("y", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'y':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setY(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMBeamPosition" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMBeamPosition' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMBeamPosition is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMBeamPosition.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMBeamPosition()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMBeamPosition" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMBeamPosition()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMBeamPosition

class XSDataMOSFLMImage(XSData):
	def __init__(self, rotationAxisStart=None, rotationAxisEnd=None, number=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMImage", "Constructor of XSDataMOSFLMImage", number, "XSDataInteger")
		self._number = number
		checkType("XSDataMOSFLMImage", "Constructor of XSDataMOSFLMImage", rotationAxisEnd, "XSDataAngle")
		self._rotationAxisEnd = rotationAxisEnd
		checkType("XSDataMOSFLMImage", "Constructor of XSDataMOSFLMImage", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
	def getNumber(self): return self._number
	def setNumber(self, number):
		checkType("XSDataMOSFLMImage", "setNumber", number, "XSDataInteger")
		self._number = number
	def delNumber(self): self._number = None
	# Properties
	number = property(getNumber, setNumber, delNumber, "Property for number")
	def getRotationAxisEnd(self): return self._rotationAxisEnd
	def setRotationAxisEnd(self, rotationAxisEnd):
		checkType("XSDataMOSFLMImage", "setRotationAxisEnd", rotationAxisEnd, "XSDataAngle")
		self._rotationAxisEnd = rotationAxisEnd
	def delRotationAxisEnd(self): self._rotationAxisEnd = None
	# Properties
	rotationAxisEnd = property(getRotationAxisEnd, setRotationAxisEnd, delRotationAxisEnd, "Property for rotationAxisEnd")
	def getRotationAxisStart(self): return self._rotationAxisStart
	def setRotationAxisStart(self, rotationAxisStart):
		checkType("XSDataMOSFLMImage", "setRotationAxisStart", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
	def delRotationAxisStart(self): self._rotationAxisStart = None
	# Properties
	rotationAxisStart = property(getRotationAxisStart, setRotationAxisStart, delRotationAxisStart, "Property for rotationAxisStart")
	def export(self, outfile, level, name_='XSDataMOSFLMImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMImage'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._number is not None:
			self.number.export(outfile, level, name_='number')
		else:
			warnEmptyAttribute("number", "XSDataInteger")
		if self._rotationAxisEnd is not None:
			self.rotationAxisEnd.export(outfile, level, name_='rotationAxisEnd')
		else:
			warnEmptyAttribute("rotationAxisEnd", "XSDataAngle")
		if self._rotationAxisStart is not None:
			self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
		else:
			warnEmptyAttribute("rotationAxisStart", "XSDataAngle")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'number':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumber(obj_)
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
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMImage

class XSDataMOSFLMIndexingSolution(XSData):
	def __init__(self, penalty=None, lattice=None, index=None, cell=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMIndexingSolution", "Constructor of XSDataMOSFLMIndexingSolution", cell, "XSDataCell")
		self._cell = cell
		checkType("XSDataMOSFLMIndexingSolution", "Constructor of XSDataMOSFLMIndexingSolution", index, "XSDataInteger")
		self._index = index
		checkType("XSDataMOSFLMIndexingSolution", "Constructor of XSDataMOSFLMIndexingSolution", lattice, "XSDataString")
		self._lattice = lattice
		checkType("XSDataMOSFLMIndexingSolution", "Constructor of XSDataMOSFLMIndexingSolution", penalty, "XSDataInteger")
		self._penalty = penalty
	def getCell(self): return self._cell
	def setCell(self, cell):
		checkType("XSDataMOSFLMIndexingSolution", "setCell", cell, "XSDataCell")
		self._cell = cell
	def delCell(self): self._cell = None
	# Properties
	cell = property(getCell, setCell, delCell, "Property for cell")
	def getIndex(self): return self._index
	def setIndex(self, index):
		checkType("XSDataMOSFLMIndexingSolution", "setIndex", index, "XSDataInteger")
		self._index = index
	def delIndex(self): self._index = None
	# Properties
	index = property(getIndex, setIndex, delIndex, "Property for index")
	def getLattice(self): return self._lattice
	def setLattice(self, lattice):
		checkType("XSDataMOSFLMIndexingSolution", "setLattice", lattice, "XSDataString")
		self._lattice = lattice
	def delLattice(self): self._lattice = None
	# Properties
	lattice = property(getLattice, setLattice, delLattice, "Property for lattice")
	def getPenalty(self): return self._penalty
	def setPenalty(self, penalty):
		checkType("XSDataMOSFLMIndexingSolution", "setPenalty", penalty, "XSDataInteger")
		self._penalty = penalty
	def delPenalty(self): self._penalty = None
	# Properties
	penalty = property(getPenalty, setPenalty, delPenalty, "Property for penalty")
	def export(self, outfile, level, name_='XSDataMOSFLMIndexingSolution'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMIndexingSolution'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._cell is not None:
			self.cell.export(outfile, level, name_='cell')
		else:
			warnEmptyAttribute("cell", "XSDataCell")
		if self._index is not None:
			self.index.export(outfile, level, name_='index')
		else:
			warnEmptyAttribute("index", "XSDataInteger")
		if self._lattice is not None:
			self.lattice.export(outfile, level, name_='lattice')
		else:
			warnEmptyAttribute("lattice", "XSDataString")
		if self._penalty is not None:
			self.penalty.export(outfile, level, name_='penalty')
		else:
			warnEmptyAttribute("penalty", "XSDataInteger")
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
			nodeName_ == 'index':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIndex(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lattice':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'penalty':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setPenalty(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMIndexingSolution" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMIndexingSolution' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMIndexingSolution is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMIndexingSolution.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIndexingSolution()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIndexingSolution" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIndexingSolution()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIndexingSolution

class XSDataMOSFLMIntegrationStatistics(XSData):
	def __init__(self, numberOfReflections=None, averageSigma=None, averageIOverSigma=None, averageIntensity=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMIntegrationStatistics", "Constructor of XSDataMOSFLMIntegrationStatistics", averageIntensity, "XSDataFloat")
		self._averageIntensity = averageIntensity
		checkType("XSDataMOSFLMIntegrationStatistics", "Constructor of XSDataMOSFLMIntegrationStatistics", averageIOverSigma, "XSDataFloat")
		self._averageIOverSigma = averageIOverSigma
		checkType("XSDataMOSFLMIntegrationStatistics", "Constructor of XSDataMOSFLMIntegrationStatistics", averageSigma, "XSDataFloat")
		self._averageSigma = averageSigma
		checkType("XSDataMOSFLMIntegrationStatistics", "Constructor of XSDataMOSFLMIntegrationStatistics", numberOfReflections, "XSDataInteger")
		self._numberOfReflections = numberOfReflections
	def getAverageIntensity(self): return self._averageIntensity
	def setAverageIntensity(self, averageIntensity):
		checkType("XSDataMOSFLMIntegrationStatistics", "setAverageIntensity", averageIntensity, "XSDataFloat")
		self._averageIntensity = averageIntensity
	def delAverageIntensity(self): self._averageIntensity = None
	# Properties
	averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
	def getAverageIOverSigma(self): return self._averageIOverSigma
	def setAverageIOverSigma(self, averageIOverSigma):
		checkType("XSDataMOSFLMIntegrationStatistics", "setAverageIOverSigma", averageIOverSigma, "XSDataFloat")
		self._averageIOverSigma = averageIOverSigma
	def delAverageIOverSigma(self): self._averageIOverSigma = None
	# Properties
	averageIOverSigma = property(getAverageIOverSigma, setAverageIOverSigma, delAverageIOverSigma, "Property for averageIOverSigma")
	def getAverageSigma(self): return self._averageSigma
	def setAverageSigma(self, averageSigma):
		checkType("XSDataMOSFLMIntegrationStatistics", "setAverageSigma", averageSigma, "XSDataFloat")
		self._averageSigma = averageSigma
	def delAverageSigma(self): self._averageSigma = None
	# Properties
	averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
	def getNumberOfReflections(self): return self._numberOfReflections
	def setNumberOfReflections(self, numberOfReflections):
		checkType("XSDataMOSFLMIntegrationStatistics", "setNumberOfReflections", numberOfReflections, "XSDataInteger")
		self._numberOfReflections = numberOfReflections
	def delNumberOfReflections(self): self._numberOfReflections = None
	# Properties
	numberOfReflections = property(getNumberOfReflections, setNumberOfReflections, delNumberOfReflections, "Property for numberOfReflections")
	def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatistics'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatistics'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._averageIntensity is not None:
			self.averageIntensity.export(outfile, level, name_='averageIntensity')
		else:
			warnEmptyAttribute("averageIntensity", "XSDataFloat")
		if self._averageIOverSigma is not None:
			self.averageIOverSigma.export(outfile, level, name_='averageIOverSigma')
		else:
			warnEmptyAttribute("averageIOverSigma", "XSDataFloat")
		if self._averageSigma is not None:
			self.averageSigma.export(outfile, level, name_='averageSigma')
		else:
			warnEmptyAttribute("averageSigma", "XSDataFloat")
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
			nodeName_ == 'averageIntensity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setAverageIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIOverSigma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setAverageIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageSigma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfReflections(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatistics" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatistics' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatistics is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMIntegrationStatistics.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatistics()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatistics" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatistics()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatistics

class XSDataMOSFLMIntegrationStatisticsPerReflectionType(XSData):
	def __init__(self, partials=None, fullyRecorded=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMIntegrationStatisticsPerReflectionType", "Constructor of XSDataMOSFLMIntegrationStatisticsPerReflectionType", fullyRecorded, "XSDataMOSFLMIntegrationStatistics")
		self._fullyRecorded = fullyRecorded
		checkType("XSDataMOSFLMIntegrationStatisticsPerReflectionType", "Constructor of XSDataMOSFLMIntegrationStatisticsPerReflectionType", partials, "XSDataMOSFLMIntegrationStatistics")
		self._partials = partials
	def getFullyRecorded(self): return self._fullyRecorded
	def setFullyRecorded(self, fullyRecorded):
		checkType("XSDataMOSFLMIntegrationStatisticsPerReflectionType", "setFullyRecorded", fullyRecorded, "XSDataMOSFLMIntegrationStatistics")
		self._fullyRecorded = fullyRecorded
	def delFullyRecorded(self): self._fullyRecorded = None
	# Properties
	fullyRecorded = property(getFullyRecorded, setFullyRecorded, delFullyRecorded, "Property for fullyRecorded")
	def getPartials(self): return self._partials
	def setPartials(self, partials):
		checkType("XSDataMOSFLMIntegrationStatisticsPerReflectionType", "setPartials", partials, "XSDataMOSFLMIntegrationStatistics")
		self._partials = partials
	def delPartials(self): self._partials = None
	# Properties
	partials = property(getPartials, setPartials, delPartials, "Property for partials")
	def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._fullyRecorded is not None:
			self.fullyRecorded.export(outfile, level, name_='fullyRecorded')
		else:
			warnEmptyAttribute("fullyRecorded", "XSDataMOSFLMIntegrationStatistics")
		if self._partials is not None:
			self.partials.export(outfile, level, name_='partials')
		else:
			warnEmptyAttribute("partials", "XSDataMOSFLMIntegrationStatistics")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fullyRecorded':
			obj_ = XSDataMOSFLMIntegrationStatistics()
			obj_.build(child_)
			self.setFullyRecorded(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'partials':
			obj_ = XSDataMOSFLMIntegrationStatistics()
			obj_.build(child_)
			self.setPartials(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerReflectionType" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatisticsPerReflectionType' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatisticsPerReflectionType is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMIntegrationStatisticsPerReflectionType.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerReflectionType" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatisticsPerReflectionType

class XSDataMOSFLMIntegrationStatisticsPerResolutionBin(XSData):
	def __init__(self, summation=None, profileFitted=None, minResolution=None, maxResolution=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "Constructor of XSDataMOSFLMIntegrationStatisticsPerResolutionBin", maxResolution, "XSDataFloat")
		self._maxResolution = maxResolution
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "Constructor of XSDataMOSFLMIntegrationStatisticsPerResolutionBin", minResolution, "XSDataFloat")
		self._minResolution = minResolution
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "Constructor of XSDataMOSFLMIntegrationStatisticsPerResolutionBin", profileFitted, "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
		self._profileFitted = profileFitted
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "Constructor of XSDataMOSFLMIntegrationStatisticsPerResolutionBin", summation, "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
		self._summation = summation
	def getMaxResolution(self): return self._maxResolution
	def setMaxResolution(self, maxResolution):
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "setMaxResolution", maxResolution, "XSDataFloat")
		self._maxResolution = maxResolution
	def delMaxResolution(self): self._maxResolution = None
	# Properties
	maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
	def getMinResolution(self): return self._minResolution
	def setMinResolution(self, minResolution):
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "setMinResolution", minResolution, "XSDataFloat")
		self._minResolution = minResolution
	def delMinResolution(self): self._minResolution = None
	# Properties
	minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
	def getProfileFitted(self): return self._profileFitted
	def setProfileFitted(self, profileFitted):
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "setProfileFitted", profileFitted, "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
		self._profileFitted = profileFitted
	def delProfileFitted(self): self._profileFitted = None
	# Properties
	profileFitted = property(getProfileFitted, setProfileFitted, delProfileFitted, "Property for profileFitted")
	def getSummation(self): return self._summation
	def setSummation(self, summation):
		checkType("XSDataMOSFLMIntegrationStatisticsPerResolutionBin", "setSummation", summation, "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
		self._summation = summation
	def delSummation(self): self._summation = None
	# Properties
	summation = property(getSummation, setSummation, delSummation, "Property for summation")
	def export(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._maxResolution is not None:
			self.maxResolution.export(outfile, level, name_='maxResolution')
		if self._minResolution is not None:
			self.minResolution.export(outfile, level, name_='minResolution')
		if self._profileFitted is not None:
			self.profileFitted.export(outfile, level, name_='profileFitted')
		else:
			warnEmptyAttribute("profileFitted", "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
		if self._summation is not None:
			self.summation.export(outfile, level, name_='summation')
		else:
			warnEmptyAttribute("summation", "XSDataMOSFLMIntegrationStatisticsPerReflectionType")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxResolution':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMaxResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minResolution':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMinResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'profileFitted':
			obj_ = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
			obj_.build(child_)
			self.setProfileFitted(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'summation':
			obj_ = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
			obj_.build(child_)
			self.setSummation(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerResolutionBin" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMIntegrationStatisticsPerResolutionBin' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMIntegrationStatisticsPerResolutionBin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMIntegrationStatisticsPerResolutionBin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMIntegrationStatisticsPerResolutionBin" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMIntegrationStatisticsPerResolutionBin

class XSDataMOSFLMMissettingsAngles(XSData):
	def __init__(self, phiz=None, phiy=None, phix=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMMissettingsAngles", "Constructor of XSDataMOSFLMMissettingsAngles", phix, "XSDataAngle")
		self._phix = phix
		checkType("XSDataMOSFLMMissettingsAngles", "Constructor of XSDataMOSFLMMissettingsAngles", phiy, "XSDataAngle")
		self._phiy = phiy
		checkType("XSDataMOSFLMMissettingsAngles", "Constructor of XSDataMOSFLMMissettingsAngles", phiz, "XSDataAngle")
		self._phiz = phiz
	def getPhix(self): return self._phix
	def setPhix(self, phix):
		checkType("XSDataMOSFLMMissettingsAngles", "setPhix", phix, "XSDataAngle")
		self._phix = phix
	def delPhix(self): self._phix = None
	# Properties
	phix = property(getPhix, setPhix, delPhix, "Property for phix")
	def getPhiy(self): return self._phiy
	def setPhiy(self, phiy):
		checkType("XSDataMOSFLMMissettingsAngles", "setPhiy", phiy, "XSDataAngle")
		self._phiy = phiy
	def delPhiy(self): self._phiy = None
	# Properties
	phiy = property(getPhiy, setPhiy, delPhiy, "Property for phiy")
	def getPhiz(self): return self._phiz
	def setPhiz(self, phiz):
		checkType("XSDataMOSFLMMissettingsAngles", "setPhiz", phiz, "XSDataAngle")
		self._phiz = phiz
	def delPhiz(self): self._phiz = None
	# Properties
	phiz = property(getPhiz, setPhiz, delPhiz, "Property for phiz")
	def export(self, outfile, level, name_='XSDataMOSFLMMissettingsAngles'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMMissettingsAngles'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._phix is not None:
			self.phix.export(outfile, level, name_='phix')
		else:
			warnEmptyAttribute("phix", "XSDataAngle")
		if self._phiy is not None:
			self.phiy.export(outfile, level, name_='phiy')
		else:
			warnEmptyAttribute("phiy", "XSDataAngle")
		if self._phiz is not None:
			self.phiz.export(outfile, level, name_='phiz')
		else:
			warnEmptyAttribute("phiz", "XSDataAngle")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phix':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiy':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhiy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiz':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhiz(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMMissettingsAngles" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMMissettingsAngles' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMMissettingsAngles is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMMissettingsAngles.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMMissettingsAngles()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMMissettingsAngles" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMMissettingsAngles()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMMissettingsAngles

class XSDataMOSFLMNewmat(XSData):
	def __init__(self, uMatrix=None, refinedCell=None, missettingAngles=None, aMatrix=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMNewmat", "Constructor of XSDataMOSFLMNewmat", aMatrix, "XSDataMatrixDouble")
		self._aMatrix = aMatrix
		checkType("XSDataMOSFLMNewmat", "Constructor of XSDataMOSFLMNewmat", missettingAngles, "XSDataMOSFLMMissettingsAngles")
		self._missettingAngles = missettingAngles
		checkType("XSDataMOSFLMNewmat", "Constructor of XSDataMOSFLMNewmat", refinedCell, "XSDataCell")
		self._refinedCell = refinedCell
		checkType("XSDataMOSFLMNewmat", "Constructor of XSDataMOSFLMNewmat", uMatrix, "XSDataMatrixDouble")
		self._uMatrix = uMatrix
	def getAMatrix(self): return self._aMatrix
	def setAMatrix(self, aMatrix):
		checkType("XSDataMOSFLMNewmat", "setAMatrix", aMatrix, "XSDataMatrixDouble")
		self._aMatrix = aMatrix
	def delAMatrix(self): self._aMatrix = None
	# Properties
	aMatrix = property(getAMatrix, setAMatrix, delAMatrix, "Property for aMatrix")
	def getMissettingAngles(self): return self._missettingAngles
	def setMissettingAngles(self, missettingAngles):
		checkType("XSDataMOSFLMNewmat", "setMissettingAngles", missettingAngles, "XSDataMOSFLMMissettingsAngles")
		self._missettingAngles = missettingAngles
	def delMissettingAngles(self): self._missettingAngles = None
	# Properties
	missettingAngles = property(getMissettingAngles, setMissettingAngles, delMissettingAngles, "Property for missettingAngles")
	def getRefinedCell(self): return self._refinedCell
	def setRefinedCell(self, refinedCell):
		checkType("XSDataMOSFLMNewmat", "setRefinedCell", refinedCell, "XSDataCell")
		self._refinedCell = refinedCell
	def delRefinedCell(self): self._refinedCell = None
	# Properties
	refinedCell = property(getRefinedCell, setRefinedCell, delRefinedCell, "Property for refinedCell")
	def getUMatrix(self): return self._uMatrix
	def setUMatrix(self, uMatrix):
		checkType("XSDataMOSFLMNewmat", "setUMatrix", uMatrix, "XSDataMatrixDouble")
		self._uMatrix = uMatrix
	def delUMatrix(self): self._uMatrix = None
	# Properties
	uMatrix = property(getUMatrix, setUMatrix, delUMatrix, "Property for uMatrix")
	def export(self, outfile, level, name_='XSDataMOSFLMNewmat'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMNewmat'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._aMatrix is not None:
			self.aMatrix.export(outfile, level, name_='aMatrix')
		else:
			warnEmptyAttribute("aMatrix", "XSDataMatrixDouble")
		if self._missettingAngles is not None:
			self.missettingAngles.export(outfile, level, name_='missettingAngles')
		else:
			warnEmptyAttribute("missettingAngles", "XSDataMOSFLMMissettingsAngles")
		if self._refinedCell is not None:
			self.refinedCell.export(outfile, level, name_='refinedCell')
		else:
			warnEmptyAttribute("refinedCell", "XSDataCell")
		if self._uMatrix is not None:
			self.uMatrix.export(outfile, level, name_='uMatrix')
		else:
			warnEmptyAttribute("uMatrix", "XSDataMatrixDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aMatrix':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setAMatrix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'missettingAngles':
			obj_ = XSDataMOSFLMMissettingsAngles()
			obj_.build(child_)
			self.setMissettingAngles(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedCell':
			obj_ = XSDataCell()
			obj_.build(child_)
			self.setRefinedCell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'uMatrix':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setUMatrix(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMNewmat" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMNewmat' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMNewmat is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMNewmat.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMNewmat()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMNewmat" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMNewmat()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMNewmat

class XSDataMOSFLMOutputGeneratePrediction(XSData):
	def __init__(self, pathToLogFile=None, predictionImage=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataMOSFLMOutputGeneratePrediction", "Constructor of XSDataMOSFLMOutputGeneratePrediction", predictionImage, "XSDataImage")
		self._predictionImage = predictionImage
		checkType("XSDataMOSFLMOutputGeneratePrediction", "Constructor of XSDataMOSFLMOutputGeneratePrediction", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
	def getPredictionImage(self): return self._predictionImage
	def setPredictionImage(self, predictionImage):
		checkType("XSDataMOSFLMOutputGeneratePrediction", "setPredictionImage", predictionImage, "XSDataImage")
		self._predictionImage = predictionImage
	def delPredictionImage(self): self._predictionImage = None
	# Properties
	predictionImage = property(getPredictionImage, setPredictionImage, delPredictionImage, "Property for predictionImage")
	def getPathToLogFile(self): return self._pathToLogFile
	def setPathToLogFile(self, pathToLogFile):
		checkType("XSDataMOSFLMOutputGeneratePrediction", "setPathToLogFile", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
	def delPathToLogFile(self): self._pathToLogFile = None
	# Properties
	pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
	def export(self, outfile, level, name_='XSDataMOSFLMOutputGeneratePrediction'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputGeneratePrediction'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._predictionImage is not None:
			self.predictionImage.export(outfile, level, name_='predictionImage')
		else:
			warnEmptyAttribute("predictionImage", "XSDataImage")
		if self._pathToLogFile is not None:
			self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'predictionImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setPredictionImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToLogFile(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMOutputGeneratePrediction" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMOutputGeneratePrediction' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMOutputGeneratePrediction is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMOutputGeneratePrediction.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputGeneratePrediction()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputGeneratePrediction" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputGeneratePrediction()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputGeneratePrediction

class XSDataMOSFLMInput(XSDataInput):
	def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", beam, "XSDataMOSFLMBeamPosition")
		self._beam = beam
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", detector, "XSDataMOSFLMDetector")
		self._detector = detector
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", directory, "XSDataString")
		self._directory = directory
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", distance, "XSDataLength")
		self._distance = distance
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", matrix, "XSDataMOSFLMNewmat")
		self._matrix = matrix
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", symmetry, "XSDataString")
		self._symmetry = symmetry
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", template, "XSDataString")
		self._template = template
		checkType("XSDataMOSFLMInput", "Constructor of XSDataMOSFLMInput", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
	def getBeam(self): return self._beam
	def setBeam(self, beam):
		checkType("XSDataMOSFLMInput", "setBeam", beam, "XSDataMOSFLMBeamPosition")
		self._beam = beam
	def delBeam(self): self._beam = None
	# Properties
	beam = property(getBeam, setBeam, delBeam, "Property for beam")
	def getDetector(self): return self._detector
	def setDetector(self, detector):
		checkType("XSDataMOSFLMInput", "setDetector", detector, "XSDataMOSFLMDetector")
		self._detector = detector
	def delDetector(self): self._detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDirectory(self): return self._directory
	def setDirectory(self, directory):
		checkType("XSDataMOSFLMInput", "setDirectory", directory, "XSDataString")
		self._directory = directory
	def delDirectory(self): self._directory = None
	# Properties
	directory = property(getDirectory, setDirectory, delDirectory, "Property for directory")
	def getDistance(self): return self._distance
	def setDistance(self, distance):
		checkType("XSDataMOSFLMInput", "setDistance", distance, "XSDataLength")
		self._distance = distance
	def delDistance(self): self._distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def getMatrix(self): return self._matrix
	def setMatrix(self, matrix):
		checkType("XSDataMOSFLMInput", "setMatrix", matrix, "XSDataMOSFLMNewmat")
		self._matrix = matrix
	def delMatrix(self): self._matrix = None
	# Properties
	matrix = property(getMatrix, setMatrix, delMatrix, "Property for matrix")
	def getMosaicity(self): return self._mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataMOSFLMInput", "setMosaicity", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
	def delMosaicity(self): self._mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getSymmetry(self): return self._symmetry
	def setSymmetry(self, symmetry):
		checkType("XSDataMOSFLMInput", "setSymmetry", symmetry, "XSDataString")
		self._symmetry = symmetry
	def delSymmetry(self): self._symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def getTemplate(self): return self._template
	def setTemplate(self, template):
		checkType("XSDataMOSFLMInput", "setTemplate", template, "XSDataString")
		self._template = template
	def delTemplate(self): self._template = None
	# Properties
	template = property(getTemplate, setTemplate, delTemplate, "Property for template")
	def getWavelength(self): return self._wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataMOSFLMInput", "setWavelength", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
	def delWavelength(self): self._wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def export(self, outfile, level, name_='XSDataMOSFLMInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMInput'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._beam is not None:
			self.beam.export(outfile, level, name_='beam')
		else:
			warnEmptyAttribute("beam", "XSDataMOSFLMBeamPosition")
		if self._detector is not None:
			self.detector.export(outfile, level, name_='detector')
		else:
			warnEmptyAttribute("detector", "XSDataMOSFLMDetector")
		if self._directory is not None:
			self.directory.export(outfile, level, name_='directory')
		else:
			warnEmptyAttribute("directory", "XSDataString")
		if self._distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
		if self._matrix is not None:
			self.matrix.export(outfile, level, name_='matrix')
		if self._mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self._symmetry is not None:
			self.symmetry.export(outfile, level, name_='symmetry')
		if self._template is not None:
			self.template.export(outfile, level, name_='template')
		else:
			warnEmptyAttribute("template", "XSDataString")
		if self._wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		else:
			warnEmptyAttribute("wavelength", "XSDataWavelength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beam':
			obj_ = XSDataMOSFLMBeamPosition()
			obj_.build(child_)
			self.setBeam(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataMOSFLMDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDirectory(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'matrix':
			obj_ = XSDataMOSFLMNewmat()
			obj_.build(child_)
			self.setMatrix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymmetry(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'template':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTemplate(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInput

class XSDataMOSFLMOutput(XSDataResult):
	def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataMOSFLMOutput", "Constructor of XSDataMOSFLMOutput", refinedBeam, "XSDataMOSFLMBeamPosition")
		self._refinedBeam = refinedBeam
		checkType("XSDataMOSFLMOutput", "Constructor of XSDataMOSFLMOutput", refinedDistance, "XSDataLength")
		self._refinedDistance = refinedDistance
		checkType("XSDataMOSFLMOutput", "Constructor of XSDataMOSFLMOutput", refinedNewmat, "XSDataMOSFLMNewmat")
		self._refinedNewmat = refinedNewmat
		checkType("XSDataMOSFLMOutput", "Constructor of XSDataMOSFLMOutput", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
	def getRefinedBeam(self): return self._refinedBeam
	def setRefinedBeam(self, refinedBeam):
		checkType("XSDataMOSFLMOutput", "setRefinedBeam", refinedBeam, "XSDataMOSFLMBeamPosition")
		self._refinedBeam = refinedBeam
	def delRefinedBeam(self): self._refinedBeam = None
	# Properties
	refinedBeam = property(getRefinedBeam, setRefinedBeam, delRefinedBeam, "Property for refinedBeam")
	def getRefinedDistance(self): return self._refinedDistance
	def setRefinedDistance(self, refinedDistance):
		checkType("XSDataMOSFLMOutput", "setRefinedDistance", refinedDistance, "XSDataLength")
		self._refinedDistance = refinedDistance
	def delRefinedDistance(self): self._refinedDistance = None
	# Properties
	refinedDistance = property(getRefinedDistance, setRefinedDistance, delRefinedDistance, "Property for refinedDistance")
	def getRefinedNewmat(self): return self._refinedNewmat
	def setRefinedNewmat(self, refinedNewmat):
		checkType("XSDataMOSFLMOutput", "setRefinedNewmat", refinedNewmat, "XSDataMOSFLMNewmat")
		self._refinedNewmat = refinedNewmat
	def delRefinedNewmat(self): self._refinedNewmat = None
	# Properties
	refinedNewmat = property(getRefinedNewmat, setRefinedNewmat, delRefinedNewmat, "Property for refinedNewmat")
	def getPathToLogFile(self): return self._pathToLogFile
	def setPathToLogFile(self, pathToLogFile):
		checkType("XSDataMOSFLMOutput", "setPathToLogFile", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
	def delPathToLogFile(self): self._pathToLogFile = None
	# Properties
	pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
	def export(self, outfile, level, name_='XSDataMOSFLMOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutput'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._refinedBeam is not None:
			self.refinedBeam.export(outfile, level, name_='refinedBeam')
		else:
			warnEmptyAttribute("refinedBeam", "XSDataMOSFLMBeamPosition")
		if self._refinedDistance is not None:
			self.refinedDistance.export(outfile, level, name_='refinedDistance')
		else:
			warnEmptyAttribute("refinedDistance", "XSDataLength")
		if self._refinedNewmat is not None:
			self.refinedNewmat.export(outfile, level, name_='refinedNewmat')
		else:
			warnEmptyAttribute("refinedNewmat", "XSDataMOSFLMNewmat")
		if self._pathToLogFile is not None:
			self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedBeam':
			obj_ = XSDataMOSFLMBeamPosition()
			obj_.build(child_)
			self.setRefinedBeam(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRefinedDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedNewmat':
			obj_ = XSDataMOSFLMNewmat()
			obj_.build(child_)
			self.setRefinedNewmat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToLogFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToLogFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutput

class XSDataMOSFLMInputGeneratePrediction(XSDataMOSFLMInput):
	def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, image=None):
		XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
	
	
		checkType("XSDataMOSFLMInputGeneratePrediction", "Constructor of XSDataMOSFLMInputGeneratePrediction", image, "XSDataMOSFLMImage")
		self._image = image
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataMOSFLMInputGeneratePrediction", "setImage", image, "XSDataMOSFLMImage")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def export(self, outfile, level, name_='XSDataMOSFLMInputGeneratePrediction'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputGeneratePrediction'):
		XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
		if self._image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataMOSFLMImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataMOSFLMImage()
			obj_.build(child_)
			self.setImage(obj_)
		XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMInputGeneratePrediction" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMInputGeneratePrediction' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMInputGeneratePrediction is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMInputGeneratePrediction.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputGeneratePrediction()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputGeneratePrediction" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputGeneratePrediction()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputGeneratePrediction

class XSDataMOSFLMInputIndexing(XSDataMOSFLMInput):
	def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, image=None):
		XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
	
	
		if image is None:
			self._image = []
		else:
			checkType("XSDataMOSFLMInputIndexing", "Constructor of XSDataMOSFLMInputIndexing", image, "list")
			self._image = image
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataMOSFLMInputIndexing", "setImage", image, "list")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def addImage(self, value):
		checkType("XSDataMOSFLMInputIndexing", "setImage", value, "XSDataMOSFLMImage")
		self._image.append(value)
	def insertImage(self, index, value):
		checkType("XSDataMOSFLMInputIndexing", "setImage", value, "XSDataMOSFLMImage")
		self._image[index] = value
	def export(self, outfile, level, name_='XSDataMOSFLMInputIndexing'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputIndexing'):
		XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
		for image_ in self.getImage():
			image_.export(outfile, level, name_='image')
		if self.getImage() == []:
			warnEmptyAttribute("image", "XSDataMOSFLMImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataMOSFLMImage()
			obj_.build(child_)
			self.image.append(obj_)
		XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMInputIndexing" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMInputIndexing' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMInputIndexing is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMInputIndexing.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputIndexing()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputIndexing" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputIndexing()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputIndexing

class XSDataMOSFLMInputIntegration(XSDataMOSFLMInput):
	def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None, rotationAxisStart=None, oscillationWidth=None, imageStart=None, imageEnd=None):
		XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
	
	
		checkType("XSDataMOSFLMInputIntegration", "Constructor of XSDataMOSFLMInputIntegration", imageEnd, "XSDataInteger")
		self._imageEnd = imageEnd
		checkType("XSDataMOSFLMInputIntegration", "Constructor of XSDataMOSFLMInputIntegration", imageStart, "XSDataInteger")
		self._imageStart = imageStart
		checkType("XSDataMOSFLMInputIntegration", "Constructor of XSDataMOSFLMInputIntegration", oscillationWidth, "XSDataAngle")
		self._oscillationWidth = oscillationWidth
		checkType("XSDataMOSFLMInputIntegration", "Constructor of XSDataMOSFLMInputIntegration", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
	def getImageEnd(self): return self._imageEnd
	def setImageEnd(self, imageEnd):
		checkType("XSDataMOSFLMInputIntegration", "setImageEnd", imageEnd, "XSDataInteger")
		self._imageEnd = imageEnd
	def delImageEnd(self): self._imageEnd = None
	# Properties
	imageEnd = property(getImageEnd, setImageEnd, delImageEnd, "Property for imageEnd")
	def getImageStart(self): return self._imageStart
	def setImageStart(self, imageStart):
		checkType("XSDataMOSFLMInputIntegration", "setImageStart", imageStart, "XSDataInteger")
		self._imageStart = imageStart
	def delImageStart(self): self._imageStart = None
	# Properties
	imageStart = property(getImageStart, setImageStart, delImageStart, "Property for imageStart")
	def getOscillationWidth(self): return self._oscillationWidth
	def setOscillationWidth(self, oscillationWidth):
		checkType("XSDataMOSFLMInputIntegration", "setOscillationWidth", oscillationWidth, "XSDataAngle")
		self._oscillationWidth = oscillationWidth
	def delOscillationWidth(self): self._oscillationWidth = None
	# Properties
	oscillationWidth = property(getOscillationWidth, setOscillationWidth, delOscillationWidth, "Property for oscillationWidth")
	def getRotationAxisStart(self): return self._rotationAxisStart
	def setRotationAxisStart(self, rotationAxisStart):
		checkType("XSDataMOSFLMInputIntegration", "setRotationAxisStart", rotationAxisStart, "XSDataAngle")
		self._rotationAxisStart = rotationAxisStart
	def delRotationAxisStart(self): self._rotationAxisStart = None
	# Properties
	rotationAxisStart = property(getRotationAxisStart, setRotationAxisStart, delRotationAxisStart, "Property for rotationAxisStart")
	def export(self, outfile, level, name_='XSDataMOSFLMInputIntegration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputIntegration'):
		XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
		if self._imageEnd is not None:
			self.imageEnd.export(outfile, level, name_='imageEnd')
		else:
			warnEmptyAttribute("imageEnd", "XSDataInteger")
		if self._imageStart is not None:
			self.imageStart.export(outfile, level, name_='imageStart')
		else:
			warnEmptyAttribute("imageStart", "XSDataInteger")
		if self._oscillationWidth is not None:
			self.oscillationWidth.export(outfile, level, name_='oscillationWidth')
		else:
			warnEmptyAttribute("oscillationWidth", "XSDataAngle")
		if self._rotationAxisStart is not None:
			self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
		else:
			warnEmptyAttribute("rotationAxisStart", "XSDataAngle")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageEnd':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageEnd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageStart':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'oscillationWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOscillationWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotationAxisStart':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotationAxisStart(obj_)
		XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMInputIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMInputIntegration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMInputIntegration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMInputIntegration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputIntegration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputIntegration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputIntegration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputIntegration

class XSDataMOSFLMInputPostRefinement(XSDataMOSFLMInput):
	def __init__(self, configuration=None, wavelength=None, template=None, symmetry=None, mosaicity=None, matrix=None, distance=None, directory=None, detector=None, beam=None):
		XSDataMOSFLMInput.__init__(self, configuration, wavelength, template, symmetry, mosaicity, matrix, distance, directory, detector, beam)
	
	
	def export(self, outfile, level, name_='XSDataMOSFLMInputPostRefinement'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMInputPostRefinement'):
		XSDataMOSFLMInput.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataMOSFLMInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMInputPostRefinement" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMInputPostRefinement' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMInputPostRefinement is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMInputPostRefinement.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputPostRefinement()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMInputPostRefinement" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMInputPostRefinement()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMInputPostRefinement

class XSDataMOSFLMOutputIndexing(XSDataMOSFLMOutput):
	def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None, spotsUsed=None, spotsTotal=None, selectedSolutionSpaceGroupNumber=None, selectedSolutionSpaceGroup=None, selectedSolutionNumber=None, possibleSolutions=None, mosaicityEstimation=None, deviationPositional=None, deviationAngular=None, beamShift=None):
		XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
	
	
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", beamShift, "XSDataMOSFLMBeamPosition")
		self._beamShift = beamShift
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", deviationAngular, "XSDataAngle")
		self._deviationAngular = deviationAngular
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", deviationPositional, "XSDataLength")
		self._deviationPositional = deviationPositional
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", mosaicityEstimation, "XSDataFloat")
		self._mosaicityEstimation = mosaicityEstimation
		if possibleSolutions is None:
			self._possibleSolutions = []
		else:
			checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", possibleSolutions, "list")
			self._possibleSolutions = possibleSolutions
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", selectedSolutionNumber, "XSDataInteger")
		self._selectedSolutionNumber = selectedSolutionNumber
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", selectedSolutionSpaceGroup, "XSDataString")
		self._selectedSolutionSpaceGroup = selectedSolutionSpaceGroup
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", selectedSolutionSpaceGroupNumber, "XSDataInteger")
		self._selectedSolutionSpaceGroupNumber = selectedSolutionSpaceGroupNumber
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", spotsTotal, "XSDataInteger")
		self._spotsTotal = spotsTotal
		checkType("XSDataMOSFLMOutputIndexing", "Constructor of XSDataMOSFLMOutputIndexing", spotsUsed, "XSDataInteger")
		self._spotsUsed = spotsUsed
	def getBeamShift(self): return self._beamShift
	def setBeamShift(self, beamShift):
		checkType("XSDataMOSFLMOutputIndexing", "setBeamShift", beamShift, "XSDataMOSFLMBeamPosition")
		self._beamShift = beamShift
	def delBeamShift(self): self._beamShift = None
	# Properties
	beamShift = property(getBeamShift, setBeamShift, delBeamShift, "Property for beamShift")
	def getDeviationAngular(self): return self._deviationAngular
	def setDeviationAngular(self, deviationAngular):
		checkType("XSDataMOSFLMOutputIndexing", "setDeviationAngular", deviationAngular, "XSDataAngle")
		self._deviationAngular = deviationAngular
	def delDeviationAngular(self): self._deviationAngular = None
	# Properties
	deviationAngular = property(getDeviationAngular, setDeviationAngular, delDeviationAngular, "Property for deviationAngular")
	def getDeviationPositional(self): return self._deviationPositional
	def setDeviationPositional(self, deviationPositional):
		checkType("XSDataMOSFLMOutputIndexing", "setDeviationPositional", deviationPositional, "XSDataLength")
		self._deviationPositional = deviationPositional
	def delDeviationPositional(self): self._deviationPositional = None
	# Properties
	deviationPositional = property(getDeviationPositional, setDeviationPositional, delDeviationPositional, "Property for deviationPositional")
	def getMosaicityEstimation(self): return self._mosaicityEstimation
	def setMosaicityEstimation(self, mosaicityEstimation):
		checkType("XSDataMOSFLMOutputIndexing", "setMosaicityEstimation", mosaicityEstimation, "XSDataFloat")
		self._mosaicityEstimation = mosaicityEstimation
	def delMosaicityEstimation(self): self._mosaicityEstimation = None
	# Properties
	mosaicityEstimation = property(getMosaicityEstimation, setMosaicityEstimation, delMosaicityEstimation, "Property for mosaicityEstimation")
	def getPossibleSolutions(self): return self._possibleSolutions
	def setPossibleSolutions(self, possibleSolutions):
		checkType("XSDataMOSFLMOutputIndexing", "setPossibleSolutions", possibleSolutions, "list")
		self._possibleSolutions = possibleSolutions
	def delPossibleSolutions(self): self._possibleSolutions = None
	# Properties
	possibleSolutions = property(getPossibleSolutions, setPossibleSolutions, delPossibleSolutions, "Property for possibleSolutions")
	def addPossibleSolutions(self, value):
		checkType("XSDataMOSFLMOutputIndexing", "setPossibleSolutions", value, "XSDataMOSFLMIndexingSolution")
		self._possibleSolutions.append(value)
	def insertPossibleSolutions(self, index, value):
		checkType("XSDataMOSFLMOutputIndexing", "setPossibleSolutions", value, "XSDataMOSFLMIndexingSolution")
		self._possibleSolutions[index] = value
	def getSelectedSolutionNumber(self): return self._selectedSolutionNumber
	def setSelectedSolutionNumber(self, selectedSolutionNumber):
		checkType("XSDataMOSFLMOutputIndexing", "setSelectedSolutionNumber", selectedSolutionNumber, "XSDataInteger")
		self._selectedSolutionNumber = selectedSolutionNumber
	def delSelectedSolutionNumber(self): self._selectedSolutionNumber = None
	# Properties
	selectedSolutionNumber = property(getSelectedSolutionNumber, setSelectedSolutionNumber, delSelectedSolutionNumber, "Property for selectedSolutionNumber")
	def getSelectedSolutionSpaceGroup(self): return self._selectedSolutionSpaceGroup
	def setSelectedSolutionSpaceGroup(self, selectedSolutionSpaceGroup):
		checkType("XSDataMOSFLMOutputIndexing", "setSelectedSolutionSpaceGroup", selectedSolutionSpaceGroup, "XSDataString")
		self._selectedSolutionSpaceGroup = selectedSolutionSpaceGroup
	def delSelectedSolutionSpaceGroup(self): self._selectedSolutionSpaceGroup = None
	# Properties
	selectedSolutionSpaceGroup = property(getSelectedSolutionSpaceGroup, setSelectedSolutionSpaceGroup, delSelectedSolutionSpaceGroup, "Property for selectedSolutionSpaceGroup")
	def getSelectedSolutionSpaceGroupNumber(self): return self._selectedSolutionSpaceGroupNumber
	def setSelectedSolutionSpaceGroupNumber(self, selectedSolutionSpaceGroupNumber):
		checkType("XSDataMOSFLMOutputIndexing", "setSelectedSolutionSpaceGroupNumber", selectedSolutionSpaceGroupNumber, "XSDataInteger")
		self._selectedSolutionSpaceGroupNumber = selectedSolutionSpaceGroupNumber
	def delSelectedSolutionSpaceGroupNumber(self): self._selectedSolutionSpaceGroupNumber = None
	# Properties
	selectedSolutionSpaceGroupNumber = property(getSelectedSolutionSpaceGroupNumber, setSelectedSolutionSpaceGroupNumber, delSelectedSolutionSpaceGroupNumber, "Property for selectedSolutionSpaceGroupNumber")
	def getSpotsTotal(self): return self._spotsTotal
	def setSpotsTotal(self, spotsTotal):
		checkType("XSDataMOSFLMOutputIndexing", "setSpotsTotal", spotsTotal, "XSDataInteger")
		self._spotsTotal = spotsTotal
	def delSpotsTotal(self): self._spotsTotal = None
	# Properties
	spotsTotal = property(getSpotsTotal, setSpotsTotal, delSpotsTotal, "Property for spotsTotal")
	def getSpotsUsed(self): return self._spotsUsed
	def setSpotsUsed(self, spotsUsed):
		checkType("XSDataMOSFLMOutputIndexing", "setSpotsUsed", spotsUsed, "XSDataInteger")
		self._spotsUsed = spotsUsed
	def delSpotsUsed(self): self._spotsUsed = None
	# Properties
	spotsUsed = property(getSpotsUsed, setSpotsUsed, delSpotsUsed, "Property for spotsUsed")
	def export(self, outfile, level, name_='XSDataMOSFLMOutputIndexing'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputIndexing'):
		XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
		if self._beamShift is not None:
			self.beamShift.export(outfile, level, name_='beamShift')
		else:
			warnEmptyAttribute("beamShift", "XSDataMOSFLMBeamPosition")
		if self._deviationAngular is not None:
			self.deviationAngular.export(outfile, level, name_='deviationAngular')
		else:
			warnEmptyAttribute("deviationAngular", "XSDataAngle")
		if self._deviationPositional is not None:
			self.deviationPositional.export(outfile, level, name_='deviationPositional')
		else:
			warnEmptyAttribute("deviationPositional", "XSDataLength")
		if self._mosaicityEstimation is not None:
			self.mosaicityEstimation.export(outfile, level, name_='mosaicityEstimation')
		else:
			warnEmptyAttribute("mosaicityEstimation", "XSDataFloat")
		for possibleSolutions_ in self.getPossibleSolutions():
			possibleSolutions_.export(outfile, level, name_='possibleSolutions')
		if self._selectedSolutionNumber is not None:
			self.selectedSolutionNumber.export(outfile, level, name_='selectedSolutionNumber')
		else:
			warnEmptyAttribute("selectedSolutionNumber", "XSDataInteger")
		if self._selectedSolutionSpaceGroup is not None:
			self.selectedSolutionSpaceGroup.export(outfile, level, name_='selectedSolutionSpaceGroup')
		else:
			warnEmptyAttribute("selectedSolutionSpaceGroup", "XSDataString")
		if self._selectedSolutionSpaceGroupNumber is not None:
			self.selectedSolutionSpaceGroupNumber.export(outfile, level, name_='selectedSolutionSpaceGroupNumber')
		else:
			warnEmptyAttribute("selectedSolutionSpaceGroupNumber", "XSDataInteger")
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
			nodeName_ == 'beamShift':
			obj_ = XSDataMOSFLMBeamPosition()
			obj_.build(child_)
			self.setBeamShift(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deviationAngular':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setDeviationAngular(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deviationPositional':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDeviationPositional(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicityEstimation':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMosaicityEstimation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'possibleSolutions':
			obj_ = XSDataMOSFLMIndexingSolution()
			obj_.build(child_)
			self.possibleSolutions.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedSolutionNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSelectedSolutionNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedSolutionSpaceGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSelectedSolutionSpaceGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedSolutionSpaceGroupNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSelectedSolutionSpaceGroupNumber(obj_)
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
		XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMOutputIndexing" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMOutputIndexing' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMOutputIndexing is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMOutputIndexing.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputIndexing()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputIndexing" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputIndexing()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputIndexing

class XSDataMOSFLMOutputIntegration(XSDataMOSFLMOutput):
	def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None, statisticsPerResolutionBin=None, RMSSpotDeviation=None, refinedYScale=None, refinedMosaicity=None, overallStatistics=None, overallIOverSigma=None, numberOfReflectionsGenerated=None, numberOfPartialReflections=None, numberOfOverlappedReflections=None, numberOfNegativeReflections=None, numberOfFullyRecordedReflections=None, numberOfBadReflections=None, highestResolutionIOverSigma=None, generatedMTZFile=None, bestfilePar=None, bestfileHKL=None, bestfileDat=None):
		XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
	
	
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", bestfileDat, "XSDataString")
		self._bestfileDat = bestfileDat
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", bestfileHKL, "XSDataString")
		self._bestfileHKL = bestfileHKL
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", bestfilePar, "XSDataString")
		self._bestfilePar = bestfilePar
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", generatedMTZFile, "XSDataFile")
		self._generatedMTZFile = generatedMTZFile
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", highestResolutionIOverSigma, "XSDataFloat")
		self._highestResolutionIOverSigma = highestResolutionIOverSigma
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfBadReflections, "XSDataInteger")
		self._numberOfBadReflections = numberOfBadReflections
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfFullyRecordedReflections, "XSDataInteger")
		self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfNegativeReflections, "XSDataInteger")
		self._numberOfNegativeReflections = numberOfNegativeReflections
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfOverlappedReflections, "XSDataInteger")
		self._numberOfOverlappedReflections = numberOfOverlappedReflections
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfPartialReflections, "XSDataInteger")
		self._numberOfPartialReflections = numberOfPartialReflections
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", numberOfReflectionsGenerated, "XSDataInteger")
		self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", overallIOverSigma, "XSDataFloat")
		self._overallIOverSigma = overallIOverSigma
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", overallStatistics, "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
		self._overallStatistics = overallStatistics
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", refinedMosaicity, "XSDataFloat")
		self._refinedMosaicity = refinedMosaicity
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", refinedYScale, "XSDataFloat")
		self._refinedYScale = refinedYScale
		checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", RMSSpotDeviation, "XSDataLength")
		self._RMSSpotDeviation = RMSSpotDeviation
		if statisticsPerResolutionBin is None:
			self._statisticsPerResolutionBin = []
		else:
			checkType("XSDataMOSFLMOutputIntegration", "Constructor of XSDataMOSFLMOutputIntegration", statisticsPerResolutionBin, "list")
			self._statisticsPerResolutionBin = statisticsPerResolutionBin
	def getBestfileDat(self): return self._bestfileDat
	def setBestfileDat(self, bestfileDat):
		checkType("XSDataMOSFLMOutputIntegration", "setBestfileDat", bestfileDat, "XSDataString")
		self._bestfileDat = bestfileDat
	def delBestfileDat(self): self._bestfileDat = None
	# Properties
	bestfileDat = property(getBestfileDat, setBestfileDat, delBestfileDat, "Property for bestfileDat")
	def getBestfileHKL(self): return self._bestfileHKL
	def setBestfileHKL(self, bestfileHKL):
		checkType("XSDataMOSFLMOutputIntegration", "setBestfileHKL", bestfileHKL, "XSDataString")
		self._bestfileHKL = bestfileHKL
	def delBestfileHKL(self): self._bestfileHKL = None
	# Properties
	bestfileHKL = property(getBestfileHKL, setBestfileHKL, delBestfileHKL, "Property for bestfileHKL")
	def getBestfilePar(self): return self._bestfilePar
	def setBestfilePar(self, bestfilePar):
		checkType("XSDataMOSFLMOutputIntegration", "setBestfilePar", bestfilePar, "XSDataString")
		self._bestfilePar = bestfilePar
	def delBestfilePar(self): self._bestfilePar = None
	# Properties
	bestfilePar = property(getBestfilePar, setBestfilePar, delBestfilePar, "Property for bestfilePar")
	def getGeneratedMTZFile(self): return self._generatedMTZFile
	def setGeneratedMTZFile(self, generatedMTZFile):
		checkType("XSDataMOSFLMOutputIntegration", "setGeneratedMTZFile", generatedMTZFile, "XSDataFile")
		self._generatedMTZFile = generatedMTZFile
	def delGeneratedMTZFile(self): self._generatedMTZFile = None
	# Properties
	generatedMTZFile = property(getGeneratedMTZFile, setGeneratedMTZFile, delGeneratedMTZFile, "Property for generatedMTZFile")
	def getHighestResolutionIOverSigma(self): return self._highestResolutionIOverSigma
	def setHighestResolutionIOverSigma(self, highestResolutionIOverSigma):
		checkType("XSDataMOSFLMOutputIntegration", "setHighestResolutionIOverSigma", highestResolutionIOverSigma, "XSDataFloat")
		self._highestResolutionIOverSigma = highestResolutionIOverSigma
	def delHighestResolutionIOverSigma(self): self._highestResolutionIOverSigma = None
	# Properties
	highestResolutionIOverSigma = property(getHighestResolutionIOverSigma, setHighestResolutionIOverSigma, delHighestResolutionIOverSigma, "Property for highestResolutionIOverSigma")
	def getNumberOfBadReflections(self): return self._numberOfBadReflections
	def setNumberOfBadReflections(self, numberOfBadReflections):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfBadReflections", numberOfBadReflections, "XSDataInteger")
		self._numberOfBadReflections = numberOfBadReflections
	def delNumberOfBadReflections(self): self._numberOfBadReflections = None
	# Properties
	numberOfBadReflections = property(getNumberOfBadReflections, setNumberOfBadReflections, delNumberOfBadReflections, "Property for numberOfBadReflections")
	def getNumberOfFullyRecordedReflections(self): return self._numberOfFullyRecordedReflections
	def setNumberOfFullyRecordedReflections(self, numberOfFullyRecordedReflections):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfFullyRecordedReflections", numberOfFullyRecordedReflections, "XSDataInteger")
		self._numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
	def delNumberOfFullyRecordedReflections(self): self._numberOfFullyRecordedReflections = None
	# Properties
	numberOfFullyRecordedReflections = property(getNumberOfFullyRecordedReflections, setNumberOfFullyRecordedReflections, delNumberOfFullyRecordedReflections, "Property for numberOfFullyRecordedReflections")
	def getNumberOfNegativeReflections(self): return self._numberOfNegativeReflections
	def setNumberOfNegativeReflections(self, numberOfNegativeReflections):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfNegativeReflections", numberOfNegativeReflections, "XSDataInteger")
		self._numberOfNegativeReflections = numberOfNegativeReflections
	def delNumberOfNegativeReflections(self): self._numberOfNegativeReflections = None
	# Properties
	numberOfNegativeReflections = property(getNumberOfNegativeReflections, setNumberOfNegativeReflections, delNumberOfNegativeReflections, "Property for numberOfNegativeReflections")
	def getNumberOfOverlappedReflections(self): return self._numberOfOverlappedReflections
	def setNumberOfOverlappedReflections(self, numberOfOverlappedReflections):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfOverlappedReflections", numberOfOverlappedReflections, "XSDataInteger")
		self._numberOfOverlappedReflections = numberOfOverlappedReflections
	def delNumberOfOverlappedReflections(self): self._numberOfOverlappedReflections = None
	# Properties
	numberOfOverlappedReflections = property(getNumberOfOverlappedReflections, setNumberOfOverlappedReflections, delNumberOfOverlappedReflections, "Property for numberOfOverlappedReflections")
	def getNumberOfPartialReflections(self): return self._numberOfPartialReflections
	def setNumberOfPartialReflections(self, numberOfPartialReflections):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfPartialReflections", numberOfPartialReflections, "XSDataInteger")
		self._numberOfPartialReflections = numberOfPartialReflections
	def delNumberOfPartialReflections(self): self._numberOfPartialReflections = None
	# Properties
	numberOfPartialReflections = property(getNumberOfPartialReflections, setNumberOfPartialReflections, delNumberOfPartialReflections, "Property for numberOfPartialReflections")
	def getNumberOfReflectionsGenerated(self): return self._numberOfReflectionsGenerated
	def setNumberOfReflectionsGenerated(self, numberOfReflectionsGenerated):
		checkType("XSDataMOSFLMOutputIntegration", "setNumberOfReflectionsGenerated", numberOfReflectionsGenerated, "XSDataInteger")
		self._numberOfReflectionsGenerated = numberOfReflectionsGenerated
	def delNumberOfReflectionsGenerated(self): self._numberOfReflectionsGenerated = None
	# Properties
	numberOfReflectionsGenerated = property(getNumberOfReflectionsGenerated, setNumberOfReflectionsGenerated, delNumberOfReflectionsGenerated, "Property for numberOfReflectionsGenerated")
	def getOverallIOverSigma(self): return self._overallIOverSigma
	def setOverallIOverSigma(self, overallIOverSigma):
		checkType("XSDataMOSFLMOutputIntegration", "setOverallIOverSigma", overallIOverSigma, "XSDataFloat")
		self._overallIOverSigma = overallIOverSigma
	def delOverallIOverSigma(self): self._overallIOverSigma = None
	# Properties
	overallIOverSigma = property(getOverallIOverSigma, setOverallIOverSigma, delOverallIOverSigma, "Property for overallIOverSigma")
	def getOverallStatistics(self): return self._overallStatistics
	def setOverallStatistics(self, overallStatistics):
		checkType("XSDataMOSFLMOutputIntegration", "setOverallStatistics", overallStatistics, "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
		self._overallStatistics = overallStatistics
	def delOverallStatistics(self): self._overallStatistics = None
	# Properties
	overallStatistics = property(getOverallStatistics, setOverallStatistics, delOverallStatistics, "Property for overallStatistics")
	def getRefinedMosaicity(self): return self._refinedMosaicity
	def setRefinedMosaicity(self, refinedMosaicity):
		checkType("XSDataMOSFLMOutputIntegration", "setRefinedMosaicity", refinedMosaicity, "XSDataFloat")
		self._refinedMosaicity = refinedMosaicity
	def delRefinedMosaicity(self): self._refinedMosaicity = None
	# Properties
	refinedMosaicity = property(getRefinedMosaicity, setRefinedMosaicity, delRefinedMosaicity, "Property for refinedMosaicity")
	def getRefinedYScale(self): return self._refinedYScale
	def setRefinedYScale(self, refinedYScale):
		checkType("XSDataMOSFLMOutputIntegration", "setRefinedYScale", refinedYScale, "XSDataFloat")
		self._refinedYScale = refinedYScale
	def delRefinedYScale(self): self._refinedYScale = None
	# Properties
	refinedYScale = property(getRefinedYScale, setRefinedYScale, delRefinedYScale, "Property for refinedYScale")
	def getRMSSpotDeviation(self): return self._RMSSpotDeviation
	def setRMSSpotDeviation(self, RMSSpotDeviation):
		checkType("XSDataMOSFLMOutputIntegration", "setRMSSpotDeviation", RMSSpotDeviation, "XSDataLength")
		self._RMSSpotDeviation = RMSSpotDeviation
	def delRMSSpotDeviation(self): self._RMSSpotDeviation = None
	# Properties
	RMSSpotDeviation = property(getRMSSpotDeviation, setRMSSpotDeviation, delRMSSpotDeviation, "Property for RMSSpotDeviation")
	def getStatisticsPerResolutionBin(self): return self._statisticsPerResolutionBin
	def setStatisticsPerResolutionBin(self, statisticsPerResolutionBin):
		checkType("XSDataMOSFLMOutputIntegration", "setStatisticsPerResolutionBin", statisticsPerResolutionBin, "list")
		self._statisticsPerResolutionBin = statisticsPerResolutionBin
	def delStatisticsPerResolutionBin(self): self._statisticsPerResolutionBin = None
	# Properties
	statisticsPerResolutionBin = property(getStatisticsPerResolutionBin, setStatisticsPerResolutionBin, delStatisticsPerResolutionBin, "Property for statisticsPerResolutionBin")
	def addStatisticsPerResolutionBin(self, value):
		checkType("XSDataMOSFLMOutputIntegration", "setStatisticsPerResolutionBin", value, "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
		self._statisticsPerResolutionBin.append(value)
	def insertStatisticsPerResolutionBin(self, index, value):
		checkType("XSDataMOSFLMOutputIntegration", "setStatisticsPerResolutionBin", value, "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
		self._statisticsPerResolutionBin[index] = value
	def export(self, outfile, level, name_='XSDataMOSFLMOutputIntegration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputIntegration'):
		XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
		if self._bestfileDat is not None:
			self.bestfileDat.export(outfile, level, name_='bestfileDat')
		else:
			warnEmptyAttribute("bestfileDat", "XSDataString")
		if self._bestfileHKL is not None:
			self.bestfileHKL.export(outfile, level, name_='bestfileHKL')
		if self._bestfilePar is not None:
			self.bestfilePar.export(outfile, level, name_='bestfilePar')
		else:
			warnEmptyAttribute("bestfilePar", "XSDataString")
		if self._generatedMTZFile is not None:
			self.generatedMTZFile.export(outfile, level, name_='generatedMTZFile')
		else:
			warnEmptyAttribute("generatedMTZFile", "XSDataFile")
		if self._highestResolutionIOverSigma is not None:
			self.highestResolutionIOverSigma.export(outfile, level, name_='highestResolutionIOverSigma')
		else:
			warnEmptyAttribute("highestResolutionIOverSigma", "XSDataFloat")
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
		if self._overallIOverSigma is not None:
			self.overallIOverSigma.export(outfile, level, name_='overallIOverSigma')
		else:
			warnEmptyAttribute("overallIOverSigma", "XSDataFloat")
		if self._overallStatistics is not None:
			self.overallStatistics.export(outfile, level, name_='overallStatistics')
		else:
			warnEmptyAttribute("overallStatistics", "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
		if self._refinedMosaicity is not None:
			self.refinedMosaicity.export(outfile, level, name_='refinedMosaicity')
		if self._refinedYScale is not None:
			self.refinedYScale.export(outfile, level, name_='refinedYScale')
		else:
			warnEmptyAttribute("refinedYScale", "XSDataFloat")
		if self._RMSSpotDeviation is not None:
			self.RMSSpotDeviation.export(outfile, level, name_='RMSSpotDeviation')
		else:
			warnEmptyAttribute("RMSSpotDeviation", "XSDataLength")
		for statisticsPerResolutionBin_ in self.getStatisticsPerResolutionBin():
			statisticsPerResolutionBin_.export(outfile, level, name_='statisticsPerResolutionBin')
		if self.getStatisticsPerResolutionBin() == []:
			warnEmptyAttribute("statisticsPerResolutionBin", "XSDataMOSFLMIntegrationStatisticsPerResolutionBin")
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
			nodeName_ == 'generatedMTZFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGeneratedMTZFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'highestResolutionIOverSigma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setHighestResolutionIOverSigma(obj_)
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overallIOverSigma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setOverallIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overallStatistics':
			obj_ = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
			obj_.build(child_)
			self.setOverallStatistics(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedMosaicity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRefinedMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedYScale':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRefinedYScale(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'RMSSpotDeviation':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRMSSpotDeviation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statisticsPerResolutionBin':
			obj_ = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
			obj_.build(child_)
			self.statisticsPerResolutionBin.append(obj_)
		XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMOutputIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMOutputIntegration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMOutputIntegration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMOutputIntegration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputIntegration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputIntegration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputIntegration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputIntegration

class XSDataMOSFLMOutputPostRefinement(XSDataMOSFLMOutput):
	def __init__(self, status=None, pathToLogFile=None, refinedNewmat=None, refinedDistance=None, refinedBeam=None):
		XSDataMOSFLMOutput.__init__(self, status, pathToLogFile, refinedNewmat, refinedDistance, refinedBeam)
	
	
	def export(self, outfile, level, name_='XSDataMOSFLMOutputPostRefinement'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMOSFLMOutputPostRefinement'):
		XSDataMOSFLMOutput.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataMOSFLMOutput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMOSFLMOutputPostRefinement" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMOSFLMOutputPostRefinement' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMOSFLMOutputPostRefinement is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMOSFLMOutputPostRefinement.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputPostRefinement()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMOSFLMOutputPostRefinement" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMOSFLMOutputPostRefinement()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMOSFLMOutputPostRefinement



# End of data representation classes.



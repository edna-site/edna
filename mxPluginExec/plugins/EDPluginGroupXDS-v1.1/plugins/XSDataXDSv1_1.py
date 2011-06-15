#!/usr/bin/env python

#
# Generated Tue Jun 14 11:25::30 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString




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


class XSDataXDSDetector(XSData):
	def __init__(self, qy=None, qx=None, ny=None, nx=None, image_format=None, detector_name=None):
		XSData.__init__(self, )
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", detector_name, "XSDataString")
		self.__detector_name = detector_name
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", image_format, "XSDataString")
		self.__image_format = image_format
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", nx, "XSDataInteger")
		self.__nx = nx
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", ny, "XSDataInteger")
		self.__ny = ny
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", qx, "XSDataDouble")
		self.__qx = qx
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", qy, "XSDataDouble")
		self.__qy = qy
	def getDetector_name(self): return self.__detector_name
	def setDetector_name(self, detector_name):
		checkType("XSDataXDSDetector", "setDetector_name", detector_name, "XSDataString")
		self.__detector_name = detector_name
	def delDetector_name(self): self.__detector_name = None
	# Properties
	detector_name = property(getDetector_name, setDetector_name, delDetector_name, "Property for detector_name")
	def getImage_format(self): return self.__image_format
	def setImage_format(self, image_format):
		checkType("XSDataXDSDetector", "setImage_format", image_format, "XSDataString")
		self.__image_format = image_format
	def delImage_format(self): self.__image_format = None
	# Properties
	image_format = property(getImage_format, setImage_format, delImage_format, "Property for image_format")
	def getNx(self): return self.__nx
	def setNx(self, nx):
		checkType("XSDataXDSDetector", "setNx", nx, "XSDataInteger")
		self.__nx = nx
	def delNx(self): self.__nx = None
	# Properties
	nx = property(getNx, setNx, delNx, "Property for nx")
	def getNy(self): return self.__ny
	def setNy(self, ny):
		checkType("XSDataXDSDetector", "setNy", ny, "XSDataInteger")
		self.__ny = ny
	def delNy(self): self.__ny = None
	# Properties
	ny = property(getNy, setNy, delNy, "Property for ny")
	def getQx(self): return self.__qx
	def setQx(self, qx):
		checkType("XSDataXDSDetector", "setQx", qx, "XSDataDouble")
		self.__qx = qx
	def delQx(self): self.__qx = None
	# Properties
	qx = property(getQx, setQx, delQx, "Property for qx")
	def getQy(self): return self.__qy
	def setQy(self, qy):
		checkType("XSDataXDSDetector", "setQy", qy, "XSDataDouble")
		self.__qy = qy
	def delQy(self): self.__qy = None
	# Properties
	qy = property(getQy, setQy, delQy, "Property for qy")
	def export(self, outfile, level, name_='XSDataXDSDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSDetector'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__detector_name is not None:
			self.detector_name.export(outfile, level, name_='detector_name')
		else:
			warnEmptyAttribute("detector_name", "XSDataString")
		if self.__image_format is not None:
			self.image_format.export(outfile, level, name_='image_format')
		else:
			warnEmptyAttribute("image_format", "XSDataString")
		if self.__nx is not None:
			self.nx.export(outfile, level, name_='nx')
		else:
			warnEmptyAttribute("nx", "XSDataInteger")
		if self.__ny is not None:
			self.ny.export(outfile, level, name_='ny')
		else:
			warnEmptyAttribute("ny", "XSDataInteger")
		if self.__qx is not None:
			self.qx.export(outfile, level, name_='qx')
		else:
			warnEmptyAttribute("qx", "XSDataDouble")
		if self.__qy is not None:
			self.qy.export(outfile, level, name_='qy')
		else:
			warnEmptyAttribute("qy", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector_name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetector_name(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image_format':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImage_format(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nx':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNx(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ny':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qx':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setQx(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setQy(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSDetector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSDetector' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSDetector is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSDetector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDetector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSDetector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDetector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSDetector

class XSDataXDSRange(XSData):
	def __init__(self, upper=None, lower=None):
		XSData.__init__(self, )
		checkType("XSDataXDSRange", "Constructor of XSDataXDSRange", lower, "XSDataInteger")
		self.__lower = lower
		checkType("XSDataXDSRange", "Constructor of XSDataXDSRange", upper, "XSDataInteger")
		self.__upper = upper
	def getLower(self): return self.__lower
	def setLower(self, lower):
		checkType("XSDataXDSRange", "setLower", lower, "XSDataInteger")
		self.__lower = lower
	def delLower(self): self.__lower = None
	# Properties
	lower = property(getLower, setLower, delLower, "Property for lower")
	def getUpper(self): return self.__upper
	def setUpper(self, upper):
		checkType("XSDataXDSRange", "setUpper", upper, "XSDataInteger")
		self.__upper = upper
	def delUpper(self): self.__upper = None
	# Properties
	upper = property(getUpper, setUpper, delUpper, "Property for upper")
	def export(self, outfile, level, name_='XSDataXDSRange'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSRange'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__lower is not None:
			self.lower.export(outfile, level, name_='lower')
		else:
			warnEmptyAttribute("lower", "XSDataInteger")
		if self.__upper is not None:
			self.upper.export(outfile, level, name_='upper')
		else:
			warnEmptyAttribute("upper", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lower':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setLower(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'upper':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setUpper(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSRange" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSRange' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSRange is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSRange.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSRange()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSRange" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSRange()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSRange

class XSDataXDSSpot(XSData):
	def __init__(self, IoverSigma=None, centroidY=None, centroidX=None, centroidFrame=None):
		XSData.__init__(self, )
		checkType("XSDataXDSSpot", "Constructor of XSDataXDSSpot", centroidFrame, "XSDataDouble")
		self.__centroidFrame = centroidFrame
		checkType("XSDataXDSSpot", "Constructor of XSDataXDSSpot", centroidX, "XSDataDouble")
		self.__centroidX = centroidX
		checkType("XSDataXDSSpot", "Constructor of XSDataXDSSpot", centroidY, "XSDataDouble")
		self.__centroidY = centroidY
		checkType("XSDataXDSSpot", "Constructor of XSDataXDSSpot", IoverSigma, "XSDataDouble")
		self.__IoverSigma = IoverSigma
	def getCentroidFrame(self): return self.__centroidFrame
	def setCentroidFrame(self, centroidFrame):
		checkType("XSDataXDSSpot", "setCentroidFrame", centroidFrame, "XSDataDouble")
		self.__centroidFrame = centroidFrame
	def delCentroidFrame(self): self.__centroidFrame = None
	# Properties
	centroidFrame = property(getCentroidFrame, setCentroidFrame, delCentroidFrame, "Property for centroidFrame")
	def getCentroidX(self): return self.__centroidX
	def setCentroidX(self, centroidX):
		checkType("XSDataXDSSpot", "setCentroidX", centroidX, "XSDataDouble")
		self.__centroidX = centroidX
	def delCentroidX(self): self.__centroidX = None
	# Properties
	centroidX = property(getCentroidX, setCentroidX, delCentroidX, "Property for centroidX")
	def getCentroidY(self): return self.__centroidY
	def setCentroidY(self, centroidY):
		checkType("XSDataXDSSpot", "setCentroidY", centroidY, "XSDataDouble")
		self.__centroidY = centroidY
	def delCentroidY(self): self.__centroidY = None
	# Properties
	centroidY = property(getCentroidY, setCentroidY, delCentroidY, "Property for centroidY")
	def getIoverSigma(self): return self.__IoverSigma
	def setIoverSigma(self, IoverSigma):
		checkType("XSDataXDSSpot", "setIoverSigma", IoverSigma, "XSDataDouble")
		self.__IoverSigma = IoverSigma
	def delIoverSigma(self): self.__IoverSigma = None
	# Properties
	IoverSigma = property(getIoverSigma, setIoverSigma, delIoverSigma, "Property for IoverSigma")
	def export(self, outfile, level, name_='XSDataXDSSpot'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSSpot'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__centroidFrame is not None:
			self.centroidFrame.export(outfile, level, name_='centroidFrame')
		else:
			warnEmptyAttribute("centroidFrame", "XSDataDouble")
		if self.__centroidX is not None:
			self.centroidX.export(outfile, level, name_='centroidX')
		else:
			warnEmptyAttribute("centroidX", "XSDataDouble")
		if self.__centroidY is not None:
			self.centroidY.export(outfile, level, name_='centroidY')
		else:
			warnEmptyAttribute("centroidY", "XSDataDouble")
		if self.__IoverSigma is not None:
			self.IoverSigma.export(outfile, level, name_='IoverSigma')
		else:
			warnEmptyAttribute("IoverSigma", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'centroidFrame':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCentroidFrame(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'centroidX':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCentroidX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'centroidY':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCentroidY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'IoverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIoverSigma(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSSpot" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSSpot' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSSpot is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSSpot.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSSpot()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSSpot" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSSpot()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSSpot

class XSDataXDSSubWedge(XSData):
	def __init__(self, XSDataXDSRange=None, name_template_of_data_frames=None, data_range=None, background_range=None):
		XSData.__init__(self, )
		checkType("XSDataXDSSubWedge", "Constructor of XSDataXDSSubWedge", background_range, "XSDataXDSRange")
		self.__background_range = background_range
		checkType("XSDataXDSSubWedge", "Constructor of XSDataXDSSubWedge", data_range, "XSDataXDSRange")
		self.__data_range = data_range
		checkType("XSDataXDSSubWedge", "Constructor of XSDataXDSSubWedge", name_template_of_data_frames, "XSDataString")
		self.__name_template_of_data_frames = name_template_of_data_frames
		checkType("XSDataXDSSubWedge", "Constructor of XSDataXDSSubWedge", XSDataXDSRange, "XSDataXDSRange")
		self.__XSDataXDSRange = XSDataXDSRange
	def getBackground_range(self): return self.__background_range
	def setBackground_range(self, background_range):
		checkType("XSDataXDSSubWedge", "setBackground_range", background_range, "XSDataXDSRange")
		self.__background_range = background_range
	def delBackground_range(self): self.__background_range = None
	# Properties
	background_range = property(getBackground_range, setBackground_range, delBackground_range, "Property for background_range")
	def getData_range(self): return self.__data_range
	def setData_range(self, data_range):
		checkType("XSDataXDSSubWedge", "setData_range", data_range, "XSDataXDSRange")
		self.__data_range = data_range
	def delData_range(self): self.__data_range = None
	# Properties
	data_range = property(getData_range, setData_range, delData_range, "Property for data_range")
	def getName_template_of_data_frames(self): return self.__name_template_of_data_frames
	def setName_template_of_data_frames(self, name_template_of_data_frames):
		checkType("XSDataXDSSubWedge", "setName_template_of_data_frames", name_template_of_data_frames, "XSDataString")
		self.__name_template_of_data_frames = name_template_of_data_frames
	def delName_template_of_data_frames(self): self.__name_template_of_data_frames = None
	# Properties
	name_template_of_data_frames = property(getName_template_of_data_frames, setName_template_of_data_frames, delName_template_of_data_frames, "Property for name_template_of_data_frames")
	def getXSDataXDSRange(self): return self.__XSDataXDSRange
	def setXSDataXDSRange(self, XSDataXDSRange):
		checkType("XSDataXDSSubWedge", "setXSDataXDSRange", XSDataXDSRange, "XSDataXDSRange")
		self.__XSDataXDSRange = XSDataXDSRange
	def delXSDataXDSRange(self): self.__XSDataXDSRange = None
	# Properties
	XSDataXDSRange = property(getXSDataXDSRange, setXSDataXDSRange, delXSDataXDSRange, "Property for XSDataXDSRange")
	def export(self, outfile, level, name_='XSDataXDSSubWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSSubWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__background_range is not None:
			self.background_range.export(outfile, level, name_='background_range')
		else:
			warnEmptyAttribute("background_range", "XSDataXDSRange")
		if self.__data_range is not None:
			self.data_range.export(outfile, level, name_='data_range')
		else:
			warnEmptyAttribute("data_range", "XSDataXDSRange")
		if self.__name_template_of_data_frames is not None:
			self.name_template_of_data_frames.export(outfile, level, name_='name_template_of_data_frames')
		else:
			warnEmptyAttribute("name_template_of_data_frames", "XSDataString")
		if self.__XSDataXDSRange is not None:
			self.XSDataXDSRange.export(outfile, level, name_='XSDataXDSRange')
		else:
			warnEmptyAttribute("XSDataXDSRange", "XSDataXDSRange")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'background_range':
			obj_ = XSDataXDSRange()
			obj_.build(child_)
			self.setBackground_range(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'data_range':
			obj_ = XSDataXDSRange()
			obj_.build(child_)
			self.setData_range(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name_template_of_data_frames':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName_template_of_data_frames(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDataXDSRange':
			obj_ = XSDataXDSRange()
			obj_.build(child_)
			self.setXSDataXDSRange(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSSubWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSSubWedge' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSSubWedge is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSSubWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSSubWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSSubWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSSubWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSSubWedge

class XSDataInputXDSSpotSearch(XSDataInput):
	def __init__(self, configuration=None, detector=None, subWedge=None, job=None):
		XSDataInput.__init__(self, configuration)
		if job is None:
			self.__job = []
		else:
			checkType("XSDataInputXDSSpotSearch", "Constructor of XSDataInputXDSSpotSearch", job, "XSDataString")
			self.__job = job
		checkType("XSDataInputXDSSpotSearch", "Constructor of XSDataInputXDSSpotSearch", subWedge, "XSDataXDSSubWedge")
		self.__subWedge = subWedge
		checkType("XSDataInputXDSSpotSearch", "Constructor of XSDataInputXDSSpotSearch", detector, "XSDataXDSDetector")
		self.__detector = detector
	def getJob(self): return self.__job
	def setJob(self, job):
		checkType("XSDataInputXDSSpotSearch", "setJob", job, "list")
		self.__job = job
	def delJob(self): self.__job = None
	# Properties
	job = property(getJob, setJob, delJob, "Property for job")
	def addJob(self, value):
		checkType("XSDataInputXDSSpotSearch", "setJob", value, "XSDataString")
		self.__job.append(value)
	def insertJob(self, index, value):
		checkType("XSDataInputXDSSpotSearch", "setJob", value, "XSDataString")
		self.__job[index] = value
	def getSubWedge(self): return self.__subWedge
	def setSubWedge(self, subWedge):
		checkType("XSDataInputXDSSpotSearch", "setSubWedge", subWedge, "XSDataXDSSubWedge")
		self.__subWedge = subWedge
	def delSubWedge(self): self.__subWedge = None
	# Properties
	subWedge = property(getSubWedge, setSubWedge, delSubWedge, "Property for subWedge")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputXDSSpotSearch", "setDetector", detector, "XSDataXDSDetector")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def export(self, outfile, level, name_='XSDataInputXDSSpotSearch'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputXDSSpotSearch'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for job_ in self.getJob():
			job_.export(outfile, level, name_='job')
		if self.getJob() == []:
			warnEmptyAttribute("job", "XSDataString")
		if self.__subWedge is not None:
			self.subWedge.export(outfile, level, name_='subWedge')
		else:
			warnEmptyAttribute("subWedge", "XSDataXDSSubWedge")
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		else:
			warnEmptyAttribute("detector", "XSDataXDSDetector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'job':
			obj_ = XSDataString()
			obj_.build(child_)
			self.job.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'subWedge':
			obj_ = XSDataXDSSubWedge()
			obj_.build(child_)
			self.setSubWedge(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataXDSDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputXDSSpotSearch" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputXDSSpotSearch' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputXDSSpotSearch is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputXDSSpotSearch.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSSpotSearch()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputXDSSpotSearch" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSSpotSearch()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputXDSSpotSearch

class XSDataResultXDSSpotSearch(XSDataResult):
	def __init__(self, status=None, spot=None):
		XSDataResult.__init__(self, status)
		if spot is None:
			self.__spot = []
		else:
			checkType("XSDataResultXDSSpotSearch", "Constructor of XSDataResultXDSSpotSearch", spot, "XSDataXDSSpot")
			self.__spot = spot
	def getSpot(self): return self.__spot
	def setSpot(self, spot):
		checkType("XSDataResultXDSSpotSearch", "setSpot", spot, "list")
		self.__spot = spot
	def delSpot(self): self.__spot = None
	# Properties
	spot = property(getSpot, setSpot, delSpot, "Property for spot")
	def addSpot(self, value):
		checkType("XSDataResultXDSSpotSearch", "setSpot", value, "XSDataXDSSpot")
		self.__spot.append(value)
	def insertSpot(self, index, value):
		checkType("XSDataResultXDSSpotSearch", "setSpot", value, "XSDataXDSSpot")
		self.__spot[index] = value
	def export(self, outfile, level, name_='XSDataResultXDSSpotSearch'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultXDSSpotSearch'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for spot_ in self.getSpot():
			spot_.export(outfile, level, name_='spot')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spot':
			obj_ = XSDataXDSSpot()
			obj_.build(child_)
			self.spot.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultXDSSpotSearch" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultXDSSpotSearch' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultXDSSpotSearch is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultXDSSpotSearch.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDSSpotSearch()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultXDSSpotSearch" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDSSpotSearch()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultXDSSpotSearch



# End of data representation classes.



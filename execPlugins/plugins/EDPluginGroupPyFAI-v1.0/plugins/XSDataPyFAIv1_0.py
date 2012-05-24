#!/usr/bin/env python

#
# Generated Wed May 2 04:51::09 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node

strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataAngle
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataImageExt
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
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataImageExt
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

class XSDataDetector(XSData):
	"""Number 1 and 2 refer to Y and X axis"""
	def __init__(self, distortionFileY=None, distortionFileX=None, pixelSizeY=None, pixelSizeX=None, splineFile=None, name=None):
		XSData.__init__(self, )
		checkType("XSDataDetector", "Constructor of XSDataDetector", name, "XSDataString")
		self.__name = name
		checkType("XSDataDetector", "Constructor of XSDataDetector", splineFile, "XSDataFile")
		self.__splineFile = splineFile
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeX, "XSDataLength")
		self.__pixelSizeX = pixelSizeX
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeY, "XSDataLength")
		self.__pixelSizeY = pixelSizeY
		checkType("XSDataDetector", "Constructor of XSDataDetector", distortionFileX, "XSDataImageExt")
		self.__distortionFileX = distortionFileX
		checkType("XSDataDetector", "Constructor of XSDataDetector", distortionFileY, "XSDataImageExt")
		self.__distortionFileY = distortionFileY
	def getName(self): return self.__name
	def setName(self, name):
		checkType("XSDataDetector", "setName", name, "XSDataString")
		self.__name = name
	def delName(self): self.__name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getSplineFile(self): return self.__splineFile
	def setSplineFile(self, splineFile):
		checkType("XSDataDetector", "setSplineFile", splineFile, "XSDataFile")
		self.__splineFile = splineFile
	def delSplineFile(self): self.__splineFile = None
	# Properties
	splineFile = property(getSplineFile, setSplineFile, delSplineFile, "Property for splineFile")
	def getPixelSizeX(self): return self.__pixelSizeX
	def setPixelSizeX(self, pixelSizeX):
		checkType("XSDataDetector", "setPixelSizeX", pixelSizeX, "XSDataLength")
		self.__pixelSizeX = pixelSizeX
	def delPixelSizeX(self): self.__pixelSizeX = None
	# Properties
	pixelSizeX = property(getPixelSizeX, setPixelSizeX, delPixelSizeX, "Property for pixelSizeX")
	def getPixelSizeY(self): return self.__pixelSizeY
	def setPixelSizeY(self, pixelSizeY):
		checkType("XSDataDetector", "setPixelSizeY", pixelSizeY, "XSDataLength")
		self.__pixelSizeY = pixelSizeY
	def delPixelSizeY(self): self.__pixelSizeY = None
	# Properties
	pixelSizeY = property(getPixelSizeY, setPixelSizeY, delPixelSizeY, "Property for pixelSizeY")
	def getDistortionFileX(self): return self.__distortionFileX
	def setDistortionFileX(self, distortionFileX):
		checkType("XSDataDetector", "setDistortionFileX", distortionFileX, "XSDataImageExt")
		self.__distortionFileX = distortionFileX
	def delDistortionFileX(self): self.__distortionFileX = None
	# Properties
	distortionFileX = property(getDistortionFileX, setDistortionFileX, delDistortionFileX, "Property for distortionFileX")
	def getDistortionFileY(self): return self.__distortionFileY
	def setDistortionFileY(self, distortionFileY):
		checkType("XSDataDetector", "setDistortionFileY", distortionFileY, "XSDataImageExt")
		self.__distortionFileY = distortionFileY
	def delDistortionFileY(self): self.__distortionFileY = None
	# Properties
	distortionFileY = property(getDistortionFileY, setDistortionFileY, delDistortionFileY, "Property for distortionFileY")
	def export(self, outfile, level, name_='XSDataDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataDetector'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__name is not None:
			self.name.export(outfile, level, name_='name')
		if self.__splineFile is not None:
			self.splineFile.export(outfile, level, name_='splineFile')
		if self.__pixelSizeX is not None:
			self.pixelSizeX.export(outfile, level, name_='pixelSizeX')
		if self.__pixelSizeY is not None:
			self.pixelSizeY.export(outfile, level, name_='pixelSizeY')
		if self.__distortionFileX is not None:
			self.distortionFileX.export(outfile, level, name_='distortionFileX')
		if self.__distortionFileY is not None:
			self.distortionFileY.export(outfile, level, name_='distortionFileY')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'splineFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSplineFile(obj_)
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
			nodeName_ == 'distortionFileX':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setDistortionFileX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distortionFileY':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setDistortionFileY(obj_)
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

class XSDataGeometry(XSData):
	"""place holder"""
	def __init__(self, detector=None):
		XSData.__init__(self, )
		checkType("XSDataGeometry", "Constructor of XSDataGeometry", detector, "XSDataDetector")
		self.__detector = detector
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataGeometry", "setDetector", detector, "XSDataDetector")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def export(self, outfile, level, name_='XSDataGeometry'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeometry'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		else:
			warnEmptyAttribute("detector", "XSDataDetector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeometry" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeometry' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeometry is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeometry.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeometry()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeometry" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeometry()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeometry

class XSDataPeakPosition(XSData):
	"""Set of pixel coordinates and the associated 2Theta diffraction angle"""
	def __init__(self, twoTheta=None, positionY=None, positionX=None):
		XSData.__init__(self, )
		checkType("XSDataPeakPosition", "Constructor of XSDataPeakPosition", positionX, "XSDataDouble")
		self.__positionX = positionX
		checkType("XSDataPeakPosition", "Constructor of XSDataPeakPosition", positionY, "XSDataDouble")
		self.__positionY = positionY
		checkType("XSDataPeakPosition", "Constructor of XSDataPeakPosition", twoTheta, "XSDataDouble")
		self.__twoTheta = twoTheta
	def getPositionX(self): return self.__positionX
	def setPositionX(self, positionX):
		checkType("XSDataPeakPosition", "setPositionX", positionX, "XSDataDouble")
		self.__positionX = positionX
	def delPositionX(self): self.__positionX = None
	# Properties
	positionX = property(getPositionX, setPositionX, delPositionX, "Property for positionX")
	def getPositionY(self): return self.__positionY
	def setPositionY(self, positionY):
		checkType("XSDataPeakPosition", "setPositionY", positionY, "XSDataDouble")
		self.__positionY = positionY
	def delPositionY(self): self.__positionY = None
	# Properties
	positionY = property(getPositionY, setPositionY, delPositionY, "Property for positionY")
	def getTwoTheta(self): return self.__twoTheta
	def setTwoTheta(self, twoTheta):
		checkType("XSDataPeakPosition", "setTwoTheta", twoTheta, "XSDataDouble")
		self.__twoTheta = twoTheta
	def delTwoTheta(self): self.__twoTheta = None
	# Properties
	twoTheta = property(getTwoTheta, setTwoTheta, delTwoTheta, "Property for twoTheta")
	def export(self, outfile, level, name_='XSDataPeakPosition'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataPeakPosition'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__positionX is not None:
			self.positionX.export(outfile, level, name_='positionX')
		else:
			warnEmptyAttribute("positionX", "XSDataDouble")
		if self.__positionY is not None:
			self.positionY.export(outfile, level, name_='positionY')
		else:
			warnEmptyAttribute("positionY", "XSDataDouble")
		if self.__twoTheta is not None:
			self.twoTheta.export(outfile, level, name_='twoTheta')
		else:
			warnEmptyAttribute("twoTheta", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'positionX':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPositionX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'positionY':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPositionY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'twoTheta':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTwoTheta(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataPeakPosition" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataPeakPosition' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataPeakPosition is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataPeakPosition.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataPeakPosition()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataPeakPosition" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataPeakPosition()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataPeakPosition

class XSDataGeometryFit2D(XSDataGeometry):
	def __init__(self, detector=None, distance=None, beamCentreInPixelsY=None, beamCentreInPixelsX=None, tiltRotation=None, angleOfTilt=None):
		XSDataGeometry.__init__(self, detector)
		checkType("XSDataGeometryFit2D", "Constructor of XSDataGeometryFit2D", angleOfTilt, "XSDataAngle")
		self.__angleOfTilt = angleOfTilt
		checkType("XSDataGeometryFit2D", "Constructor of XSDataGeometryFit2D", tiltRotation, "XSDataAngle")
		self.__tiltRotation = tiltRotation
		checkType("XSDataGeometryFit2D", "Constructor of XSDataGeometryFit2D", beamCentreInPixelsX, "XSDataDouble")
		self.__beamCentreInPixelsX = beamCentreInPixelsX
		checkType("XSDataGeometryFit2D", "Constructor of XSDataGeometryFit2D", beamCentreInPixelsY, "XSDataDouble")
		self.__beamCentreInPixelsY = beamCentreInPixelsY
		checkType("XSDataGeometryFit2D", "Constructor of XSDataGeometryFit2D", distance, "XSDataLength")
		self.__distance = distance
	def getAngleOfTilt(self): return self.__angleOfTilt
	def setAngleOfTilt(self, angleOfTilt):
		checkType("XSDataGeometryFit2D", "setAngleOfTilt", angleOfTilt, "XSDataAngle")
		self.__angleOfTilt = angleOfTilt
	def delAngleOfTilt(self): self.__angleOfTilt = None
	# Properties
	angleOfTilt = property(getAngleOfTilt, setAngleOfTilt, delAngleOfTilt, "Property for angleOfTilt")
	def getTiltRotation(self): return self.__tiltRotation
	def setTiltRotation(self, tiltRotation):
		checkType("XSDataGeometryFit2D", "setTiltRotation", tiltRotation, "XSDataAngle")
		self.__tiltRotation = tiltRotation
	def delTiltRotation(self): self.__tiltRotation = None
	# Properties
	tiltRotation = property(getTiltRotation, setTiltRotation, delTiltRotation, "Property for tiltRotation")
	def getBeamCentreInPixelsX(self): return self.__beamCentreInPixelsX
	def setBeamCentreInPixelsX(self, beamCentreInPixelsX):
		checkType("XSDataGeometryFit2D", "setBeamCentreInPixelsX", beamCentreInPixelsX, "XSDataDouble")
		self.__beamCentreInPixelsX = beamCentreInPixelsX
	def delBeamCentreInPixelsX(self): self.__beamCentreInPixelsX = None
	# Properties
	beamCentreInPixelsX = property(getBeamCentreInPixelsX, setBeamCentreInPixelsX, delBeamCentreInPixelsX, "Property for beamCentreInPixelsX")
	def getBeamCentreInPixelsY(self): return self.__beamCentreInPixelsY
	def setBeamCentreInPixelsY(self, beamCentreInPixelsY):
		checkType("XSDataGeometryFit2D", "setBeamCentreInPixelsY", beamCentreInPixelsY, "XSDataDouble")
		self.__beamCentreInPixelsY = beamCentreInPixelsY
	def delBeamCentreInPixelsY(self): self.__beamCentreInPixelsY = None
	# Properties
	beamCentreInPixelsY = property(getBeamCentreInPixelsY, setBeamCentreInPixelsY, delBeamCentreInPixelsY, "Property for beamCentreInPixelsY")
	def getDistance(self): return self.__distance
	def setDistance(self, distance):
		checkType("XSDataGeometryFit2D", "setDistance", distance, "XSDataLength")
		self.__distance = distance
	def delDistance(self): self.__distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def export(self, outfile, level, name_='XSDataGeometryFit2D'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeometryFit2D'):
		XSDataGeometry.exportChildren(self, outfile, level, name_)
		if self.__angleOfTilt is not None:
			self.angleOfTilt.export(outfile, level, name_='angleOfTilt')
		else:
			warnEmptyAttribute("angleOfTilt", "XSDataAngle")
		if self.__tiltRotation is not None:
			self.tiltRotation.export(outfile, level, name_='tiltRotation')
		else:
			warnEmptyAttribute("tiltRotation", "XSDataAngle")
		if self.__beamCentreInPixelsX is not None:
			self.beamCentreInPixelsX.export(outfile, level, name_='beamCentreInPixelsX')
		else:
			warnEmptyAttribute("beamCentreInPixelsX", "XSDataDouble")
		if self.__beamCentreInPixelsY is not None:
			self.beamCentreInPixelsY.export(outfile, level, name_='beamCentreInPixelsY')
		else:
			warnEmptyAttribute("beamCentreInPixelsY", "XSDataDouble")
		if self.__distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angleOfTilt':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngleOfTilt(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'tiltRotation':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setTiltRotation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCentreInPixelsX':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCentreInPixelsX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCentreInPixelsY':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCentreInPixelsY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDistance(obj_)
		XSDataGeometry.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeometryFit2D" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeometryFit2D' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeometryFit2D is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeometryFit2D.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeometryFit2D()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeometryFit2D" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeometryFit2D()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeometryFit2D

class XSDataGeometryPyFAI(XSDataGeometry):
	def __init__(self, detector=None, rotation3=None, rotation2=None, rotation1=None, pointOfNormalIncidence2=None, pointOfNormalIncidence1=None, sampleDetectorDistance=None):
		XSDataGeometry.__init__(self, detector)
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", sampleDetectorDistance, "XSDataLength")
		self.__sampleDetectorDistance = sampleDetectorDistance
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", pointOfNormalIncidence1, "XSDataLength")
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", pointOfNormalIncidence2, "XSDataLength")
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", rotation1, "XSDataAngle")
		self.__rotation1 = rotation1
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", rotation2, "XSDataAngle")
		self.__rotation2 = rotation2
		checkType("XSDataGeometryPyFAI", "Constructor of XSDataGeometryPyFAI", rotation3, "XSDataAngle")
		self.__rotation3 = rotation3
	def getSampleDetectorDistance(self): return self.__sampleDetectorDistance
	def setSampleDetectorDistance(self, sampleDetectorDistance):
		checkType("XSDataGeometryPyFAI", "setSampleDetectorDistance", sampleDetectorDistance, "XSDataLength")
		self.__sampleDetectorDistance = sampleDetectorDistance
	def delSampleDetectorDistance(self): self.__sampleDetectorDistance = None
	# Properties
	sampleDetectorDistance = property(getSampleDetectorDistance, setSampleDetectorDistance, delSampleDetectorDistance, "Property for sampleDetectorDistance")
	def getPointOfNormalIncidence1(self): return self.__pointOfNormalIncidence1
	def setPointOfNormalIncidence1(self, pointOfNormalIncidence1):
		checkType("XSDataGeometryPyFAI", "setPointOfNormalIncidence1", pointOfNormalIncidence1, "XSDataLength")
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
	def delPointOfNormalIncidence1(self): self.__pointOfNormalIncidence1 = None
	# Properties
	pointOfNormalIncidence1 = property(getPointOfNormalIncidence1, setPointOfNormalIncidence1, delPointOfNormalIncidence1, "Property for pointOfNormalIncidence1")
	def getPointOfNormalIncidence2(self): return self.__pointOfNormalIncidence2
	def setPointOfNormalIncidence2(self, pointOfNormalIncidence2):
		checkType("XSDataGeometryPyFAI", "setPointOfNormalIncidence2", pointOfNormalIncidence2, "XSDataLength")
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
	def delPointOfNormalIncidence2(self): self.__pointOfNormalIncidence2 = None
	# Properties
	pointOfNormalIncidence2 = property(getPointOfNormalIncidence2, setPointOfNormalIncidence2, delPointOfNormalIncidence2, "Property for pointOfNormalIncidence2")
	def getRotation1(self): return self.__rotation1
	def setRotation1(self, rotation1):
		checkType("XSDataGeometryPyFAI", "setRotation1", rotation1, "XSDataAngle")
		self.__rotation1 = rotation1
	def delRotation1(self): self.__rotation1 = None
	# Properties
	rotation1 = property(getRotation1, setRotation1, delRotation1, "Property for rotation1")
	def getRotation2(self): return self.__rotation2
	def setRotation2(self, rotation2):
		checkType("XSDataGeometryPyFAI", "setRotation2", rotation2, "XSDataAngle")
		self.__rotation2 = rotation2
	def delRotation2(self): self.__rotation2 = None
	# Properties
	rotation2 = property(getRotation2, setRotation2, delRotation2, "Property for rotation2")
	def getRotation3(self): return self.__rotation3
	def setRotation3(self, rotation3):
		checkType("XSDataGeometryPyFAI", "setRotation3", rotation3, "XSDataAngle")
		self.__rotation3 = rotation3
	def delRotation3(self): self.__rotation3 = None
	# Properties
	rotation3 = property(getRotation3, setRotation3, delRotation3, "Property for rotation3")
	def export(self, outfile, level, name_='XSDataGeometryPyFAI'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeometryPyFAI'):
		XSDataGeometry.exportChildren(self, outfile, level, name_)
		if self.__sampleDetectorDistance is not None:
			self.sampleDetectorDistance.export(outfile, level, name_='sampleDetectorDistance')
		else:
			warnEmptyAttribute("sampleDetectorDistance", "XSDataLength")
		if self.__pointOfNormalIncidence1 is not None:
			self.pointOfNormalIncidence1.export(outfile, level, name_='pointOfNormalIncidence1')
		else:
			warnEmptyAttribute("pointOfNormalIncidence1", "XSDataLength")
		if self.__pointOfNormalIncidence2 is not None:
			self.pointOfNormalIncidence2.export(outfile, level, name_='pointOfNormalIncidence2')
		else:
			warnEmptyAttribute("pointOfNormalIncidence2", "XSDataLength")
		if self.__rotation1 is not None:
			self.rotation1.export(outfile, level, name_='rotation1')
		else:
			warnEmptyAttribute("rotation1", "XSDataAngle")
		if self.__rotation2 is not None:
			self.rotation2.export(outfile, level, name_='rotation2')
		else:
			warnEmptyAttribute("rotation2", "XSDataAngle")
		if self.__rotation3 is not None:
			self.rotation3.export(outfile, level, name_='rotation3')
		else:
			warnEmptyAttribute("rotation3", "XSDataAngle")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleDetectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setSampleDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pointOfNormalIncidence1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPointOfNormalIncidence1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pointOfNormalIncidence2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPointOfNormalIncidence2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation1':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotation1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation2':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotation2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation3':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setRotation3(obj_)
		XSDataGeometry.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeometryPyFAI" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeometryPyFAI' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeometryPyFAI is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeometryPyFAI.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeometryPyFAI()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeometryPyFAI" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeometryPyFAI()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeometryPyFAI

class XSDataInputPyFAI(XSDataInput):
	"""saxsWaxs can be saxs or waxs"""
	def __init__(self, configuration=None, deltaDummy=None, dummy=None, saxsWaxs=None, geometryFit2D=None, geometryPyFAI=None, mask=None, wavelength=None, output=None, input=None, flat=None, dark=None, nbPt=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", nbPt, "XSDataInteger")
		self.__nbPt = nbPt
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", dark, "XSDataImageExt")
		self.__dark = dark
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", flat, "XSDataImageExt")
		self.__flat = flat
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", input, "XSDataImageExt")
		self.__input = input
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", output, "XSDataImageExt")
		self.__output = output
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", mask, "XSDataImageExt")
		self.__mask = mask
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", geometryPyFAI, "XSDataGeometryPyFAI")
		self.__geometryPyFAI = geometryPyFAI
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", saxsWaxs, "XSDataString")
		self.__saxsWaxs = saxsWaxs
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", dummy, "XSDataDouble")
		self.__dummy = dummy
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", deltaDummy, "XSDataDouble")
		self.__deltaDummy = deltaDummy
	def getNbPt(self): return self.__nbPt
	def setNbPt(self, nbPt):
		checkType("XSDataInputPyFAI", "setNbPt", nbPt, "XSDataInteger")
		self.__nbPt = nbPt
	def delNbPt(self): self.__nbPt = None
	# Properties
	nbPt = property(getNbPt, setNbPt, delNbPt, "Property for nbPt")
	def getDark(self): return self.__dark
	def setDark(self, dark):
		checkType("XSDataInputPyFAI", "setDark", dark, "XSDataImageExt")
		self.__dark = dark
	def delDark(self): self.__dark = None
	# Properties
	dark = property(getDark, setDark, delDark, "Property for dark")
	def getFlat(self): return self.__flat
	def setFlat(self, flat):
		checkType("XSDataInputPyFAI", "setFlat", flat, "XSDataImageExt")
		self.__flat = flat
	def delFlat(self): self.__flat = None
	# Properties
	flat = property(getFlat, setFlat, delFlat, "Property for flat")
	def getInput(self): return self.__input
	def setInput(self, input):
		checkType("XSDataInputPyFAI", "setInput", input, "XSDataImageExt")
		self.__input = input
	def delInput(self): self.__input = None
	# Properties
	input = property(getInput, setInput, delInput, "Property for input")
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataInputPyFAI", "setOutput", output, "XSDataImageExt")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputPyFAI", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMask(self): return self.__mask
	def setMask(self, mask):
		checkType("XSDataInputPyFAI", "setMask", mask, "XSDataImageExt")
		self.__mask = mask
	def delMask(self): self.__mask = None
	# Properties
	mask = property(getMask, setMask, delMask, "Property for mask")
	def getGeometryPyFAI(self): return self.__geometryPyFAI
	def setGeometryPyFAI(self, geometryPyFAI):
		checkType("XSDataInputPyFAI", "setGeometryPyFAI", geometryPyFAI, "XSDataGeometryPyFAI")
		self.__geometryPyFAI = geometryPyFAI
	def delGeometryPyFAI(self): self.__geometryPyFAI = None
	# Properties
	geometryPyFAI = property(getGeometryPyFAI, setGeometryPyFAI, delGeometryPyFAI, "Property for geometryPyFAI")
	def getGeometryFit2D(self): return self.__geometryFit2D
	def setGeometryFit2D(self, geometryFit2D):
		checkType("XSDataInputPyFAI", "setGeometryFit2D", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
	def delGeometryFit2D(self): self.__geometryFit2D = None
	# Properties
	geometryFit2D = property(getGeometryFit2D, setGeometryFit2D, delGeometryFit2D, "Property for geometryFit2D")
	def getSaxsWaxs(self): return self.__saxsWaxs
	def setSaxsWaxs(self, saxsWaxs):
		checkType("XSDataInputPyFAI", "setSaxsWaxs", saxsWaxs, "XSDataString")
		self.__saxsWaxs = saxsWaxs
	def delSaxsWaxs(self): self.__saxsWaxs = None
	# Properties
	saxsWaxs = property(getSaxsWaxs, setSaxsWaxs, delSaxsWaxs, "Property for saxsWaxs")
	def getDummy(self): return self.__dummy
	def setDummy(self, dummy):
		checkType("XSDataInputPyFAI", "setDummy", dummy, "XSDataDouble")
		self.__dummy = dummy
	def delDummy(self): self.__dummy = None
	# Properties
	dummy = property(getDummy, setDummy, delDummy, "Property for dummy")
	def getDeltaDummy(self): return self.__deltaDummy
	def setDeltaDummy(self, deltaDummy):
		checkType("XSDataInputPyFAI", "setDeltaDummy", deltaDummy, "XSDataDouble")
		self.__deltaDummy = deltaDummy
	def delDeltaDummy(self): self.__deltaDummy = None
	# Properties
	deltaDummy = property(getDeltaDummy, setDeltaDummy, delDeltaDummy, "Property for deltaDummy")
	def export(self, outfile, level, name_='XSDataInputPyFAI'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputPyFAI'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__nbPt is not None:
			self.nbPt.export(outfile, level, name_='nbPt')
		else:
			warnEmptyAttribute("nbPt", "XSDataInteger")
		if self.__dark is not None:
			self.dark.export(outfile, level, name_='dark')
		if self.__flat is not None:
			self.flat.export(outfile, level, name_='flat')
		if self.__input is not None:
			self.input.export(outfile, level, name_='input')
		else:
			warnEmptyAttribute("input", "XSDataImageExt")
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__mask is not None:
			self.mask.export(outfile, level, name_='mask')
		if self.__geometryPyFAI is not None:
			self.geometryPyFAI.export(outfile, level, name_='geometryPyFAI')
		if self.__geometryFit2D is not None:
			self.geometryFit2D.export(outfile, level, name_='geometryFit2D')
		if self.__saxsWaxs is not None:
			self.saxsWaxs.export(outfile, level, name_='saxsWaxs')
		if self.__dummy is not None:
			self.dummy.export(outfile, level, name_='dummy')
		if self.__deltaDummy is not None:
			self.deltaDummy.export(outfile, level, name_='deltaDummy')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nbPt':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNbPt(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dark':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setDark(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flat':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setFlat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'input':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setInput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mask':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setMask(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometryPyFAI':
			obj_ = XSDataGeometryPyFAI()
			obj_.build(child_)
			self.setGeometryPyFAI(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometryFit2D':
			obj_ = XSDataGeometryFit2D()
			obj_.build(child_)
			self.setGeometryFit2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'saxsWaxs':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSaxsWaxs(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dummy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDummy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deltaDummy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDeltaDummy(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputPyFAI" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputPyFAI' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputPyFAI is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputPyFAI.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputPyFAI()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputPyFAI" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputPyFAI()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputPyFAI

class XSDataInputRefineDiffractionGeometry(XSDataInput):
	def __init__(self, configuration=None, detector=None, geometrySPD=None, geometryFit2D=None, points=None):
		XSDataInput.__init__(self, configuration)
		if points is None:
			self.__points = []
		else:
			checkType("XSDataInputRefineDiffractionGeometry", "Constructor of XSDataInputRefineDiffractionGeometry", points, "list")
			self.__points = points
		checkType("XSDataInputRefineDiffractionGeometry", "Constructor of XSDataInputRefineDiffractionGeometry", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
		checkType("XSDataInputRefineDiffractionGeometry", "Constructor of XSDataInputRefineDiffractionGeometry", geometrySPD, "XSDataGeometryPyFAI")
		self.__geometrySPD = geometrySPD
		checkType("XSDataInputRefineDiffractionGeometry", "Constructor of XSDataInputRefineDiffractionGeometry", detector, "XSDataDetector")
		self.__detector = detector
	def getPoints(self): return self.__points
	def setPoints(self, points):
		checkType("XSDataInputRefineDiffractionGeometry", "setPoints", points, "list")
		self.__points = points
	def delPoints(self): self.__points = None
	# Properties
	points = property(getPoints, setPoints, delPoints, "Property for points")
	def addPoints(self, value):
		checkType("XSDataInputRefineDiffractionGeometry", "setPoints", value, "XSDataPeakPosition")
		self.__points.append(value)
	def insertPoints(self, index, value):
		checkType("XSDataInputRefineDiffractionGeometry", "setPoints", value, "XSDataPeakPosition")
		self.__points[index] = value
	def getGeometryFit2D(self): return self.__geometryFit2D
	def setGeometryFit2D(self, geometryFit2D):
		checkType("XSDataInputRefineDiffractionGeometry", "setGeometryFit2D", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
	def delGeometryFit2D(self): self.__geometryFit2D = None
	# Properties
	geometryFit2D = property(getGeometryFit2D, setGeometryFit2D, delGeometryFit2D, "Property for geometryFit2D")
	def getGeometrySPD(self): return self.__geometrySPD
	def setGeometrySPD(self, geometrySPD):
		checkType("XSDataInputRefineDiffractionGeometry", "setGeometrySPD", geometrySPD, "XSDataGeometryPyFAI")
		self.__geometrySPD = geometrySPD
	def delGeometrySPD(self): self.__geometrySPD = None
	# Properties
	geometrySPD = property(getGeometrySPD, setGeometrySPD, delGeometrySPD, "Property for geometrySPD")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputRefineDiffractionGeometry", "setDetector", detector, "XSDataDetector")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def export(self, outfile, level, name_='XSDataInputRefineDiffractionGeometry'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputRefineDiffractionGeometry'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for points_ in self.getPoints():
			points_.export(outfile, level, name_='points')
		if self.getPoints() == []:
			warnEmptyAttribute("points", "XSDataPeakPosition")
		if self.__geometryFit2D is not None:
			self.geometryFit2D.export(outfile, level, name_='geometryFit2D')
		if self.__geometrySPD is not None:
			self.geometrySPD.export(outfile, level, name_='geometrySPD')
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		else:
			warnEmptyAttribute("detector", "XSDataDetector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'points':
			obj_ = XSDataPeakPosition()
			obj_.build(child_)
			self.points.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometryFit2D':
			obj_ = XSDataGeometryFit2D()
			obj_.build(child_)
			self.setGeometryFit2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometrySPD':
			obj_ = XSDataGeometryPyFAI()
			obj_.build(child_)
			self.setGeometrySPD(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputRefineDiffractionGeometry" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputRefineDiffractionGeometry' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputRefineDiffractionGeometry is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputRefineDiffractionGeometry.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputRefineDiffractionGeometry()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputRefineDiffractionGeometry" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputRefineDiffractionGeometry()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputRefineDiffractionGeometry

class XSDataResultPyFAI(XSDataResult):
	def __init__(self, status=None, output=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultPyFAI", "Constructor of XSDataResultPyFAI", output, "XSDataImageExt")
		self.__output = output
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataResultPyFAI", "setOutput", output, "XSDataImageExt")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def export(self, outfile, level, name_='XSDataResultPyFAI'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultPyFAI'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		else:
			warnEmptyAttribute("output", "XSDataImageExt")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.setOutput(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultPyFAI" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultPyFAI' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultPyFAI is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultPyFAI.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultPyFAI()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultPyFAI" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultPyFAI()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultPyFAI

class XSDataResultRefineDiffractionGeometry(XSDataResult):
	def __init__(self, status=None, geometrySPD=None, geometryFit2D=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultRefineDiffractionGeometry", "Constructor of XSDataResultRefineDiffractionGeometry", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
		checkType("XSDataResultRefineDiffractionGeometry", "Constructor of XSDataResultRefineDiffractionGeometry", geometrySPD, "XSDataGeometryPyFAI")
		self.__geometrySPD = geometrySPD
	def getGeometryFit2D(self): return self.__geometryFit2D
	def setGeometryFit2D(self, geometryFit2D):
		checkType("XSDataResultRefineDiffractionGeometry", "setGeometryFit2D", geometryFit2D, "XSDataGeometryFit2D")
		self.__geometryFit2D = geometryFit2D
	def delGeometryFit2D(self): self.__geometryFit2D = None
	# Properties
	geometryFit2D = property(getGeometryFit2D, setGeometryFit2D, delGeometryFit2D, "Property for geometryFit2D")
	def getGeometrySPD(self): return self.__geometrySPD
	def setGeometrySPD(self, geometrySPD):
		checkType("XSDataResultRefineDiffractionGeometry", "setGeometrySPD", geometrySPD, "XSDataGeometryPyFAI")
		self.__geometrySPD = geometrySPD
	def delGeometrySPD(self): self.__geometrySPD = None
	# Properties
	geometrySPD = property(getGeometrySPD, setGeometrySPD, delGeometrySPD, "Property for geometrySPD")
	def export(self, outfile, level, name_='XSDataResultRefineDiffractionGeometry'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultRefineDiffractionGeometry'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__geometryFit2D is not None:
			self.geometryFit2D.export(outfile, level, name_='geometryFit2D')
		if self.__geometrySPD is not None:
			self.geometrySPD.export(outfile, level, name_='geometrySPD')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometryFit2D':
			obj_ = XSDataGeometryFit2D()
			obj_.build(child_)
			self.setGeometryFit2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'geometrySPD':
			obj_ = XSDataGeometryPyFAI()
			obj_.build(child_)
			self.setGeometrySPD(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultRefineDiffractionGeometry" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultRefineDiffractionGeometry' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultRefineDiffractionGeometry is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultRefineDiffractionGeometry.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultRefineDiffractionGeometry()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultRefineDiffractionGeometry" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultRefineDiffractionGeometry()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultRefineDiffractionGeometry

# End of data representation classes.


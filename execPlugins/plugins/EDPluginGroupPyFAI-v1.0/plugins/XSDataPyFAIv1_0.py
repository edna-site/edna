#!/usr/bin/env python

#
# Generated Tue Mar 13 03:53::21 2012 by EDGenerateDS.
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
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataResult
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
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
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
	def __init__(self, distortionFileY=None, distortionFileX=None, pixelSizeY=None, pixelSizeX=None, spatialDistortionFile=None):
		XSData.__init__(self, )
		checkType("XSDataDetector", "Constructor of XSDataDetector", spatialDistortionFile, "XSDataFile")
		self.__spatialDistortionFile = spatialDistortionFile
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeX, "XSDataLength")
		self.__pixelSizeX = pixelSizeX
		checkType("XSDataDetector", "Constructor of XSDataDetector", pixelSizeY, "XSDataLength")
		self.__pixelSizeY = pixelSizeY
		checkType("XSDataDetector", "Constructor of XSDataDetector", distortionFileX, "XSDataImageExt")
		self.__distortionFileX = distortionFileX
		checkType("XSDataDetector", "Constructor of XSDataDetector", distortionFileY, "XSDataImageExt")
		self.__distortionFileY = distortionFileY
	def getSpatialDistortionFile(self): return self.__spatialDistortionFile
	def setSpatialDistortionFile(self, spatialDistortionFile):
		checkType("XSDataDetector", "setSpatialDistortionFile", spatialDistortionFile, "XSDataFile")
		self.__spatialDistortionFile = spatialDistortionFile
	def delSpatialDistortionFile(self): self.__spatialDistortionFile = None
	# Properties
	spatialDistortionFile = property(getSpatialDistortionFile, setSpatialDistortionFile, delSpatialDistortionFile, "Property for spatialDistortionFile")
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
		if self.__spatialDistortionFile is not None:
			self.spatialDistortionFile.export(outfile, level, name_='spatialDistortionFile')
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
			nodeName_ == 'spatialDistortionFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSpatialDistortionFile(obj_)
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

class XSDataGeometryFit2D(XSData):
	def __init__(self, distance=None, beamCentreInPixelsY=None, beamCentreInPixelsX=None, tiltRotation=None, angleOfTilt=None):
		XSData.__init__(self, )
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
		XSData.exportChildren(self, outfile, level, name_)
		if self.__angleOfTilt is not None:
			self.angleOfTilt.export(outfile, level, name_='angleOfTilt')
		if self.__tiltRotation is not None:
			self.tiltRotation.export(outfile, level, name_='tiltRotation')
		if self.__beamCentreInPixelsX is not None:
			self.beamCentreInPixelsX.export(outfile, level, name_='beamCentreInPixelsX')
		if self.__beamCentreInPixelsY is not None:
			self.beamCentreInPixelsY.export(outfile, level, name_='beamCentreInPixelsY')
		if self.__distance is not None:
			self.distance.export(outfile, level, name_='distance')
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
		XSData.buildChildren(self, child_, nodeName_)
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

class XSDataGeometrySPD(XSData):
	def __init__(self, rotation3=None, rotation2=None, rotation1=None, pointOfNormalIncidence2=None, pointOfNormalIncidence1=None, sampleDetectorDistance=None):
		XSData.__init__(self, )
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", sampleDetectorDistance, "XSDataLength")
		self.__sampleDetectorDistance = sampleDetectorDistance
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", pointOfNormalIncidence1, "XSDataLength")
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", pointOfNormalIncidence2, "XSDataLength")
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", rotation1, "XSDataAngle")
		self.__rotation1 = rotation1
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", rotation2, "XSDataAngle")
		self.__rotation2 = rotation2
		checkType("XSDataGeometrySPD", "Constructor of XSDataGeometrySPD", rotation3, "XSDataAngle")
		self.__rotation3 = rotation3
	def getSampleDetectorDistance(self): return self.__sampleDetectorDistance
	def setSampleDetectorDistance(self, sampleDetectorDistance):
		checkType("XSDataGeometrySPD", "setSampleDetectorDistance", sampleDetectorDistance, "XSDataLength")
		self.__sampleDetectorDistance = sampleDetectorDistance
	def delSampleDetectorDistance(self): self.__sampleDetectorDistance = None
	# Properties
	sampleDetectorDistance = property(getSampleDetectorDistance, setSampleDetectorDistance, delSampleDetectorDistance, "Property for sampleDetectorDistance")
	def getPointOfNormalIncidence1(self): return self.__pointOfNormalIncidence1
	def setPointOfNormalIncidence1(self, pointOfNormalIncidence1):
		checkType("XSDataGeometrySPD", "setPointOfNormalIncidence1", pointOfNormalIncidence1, "XSDataLength")
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
	def delPointOfNormalIncidence1(self): self.__pointOfNormalIncidence1 = None
	# Properties
	pointOfNormalIncidence1 = property(getPointOfNormalIncidence1, setPointOfNormalIncidence1, delPointOfNormalIncidence1, "Property for pointOfNormalIncidence1")
	def getPointOfNormalIncidence2(self): return self.__pointOfNormalIncidence2
	def setPointOfNormalIncidence2(self, pointOfNormalIncidence2):
		checkType("XSDataGeometrySPD", "setPointOfNormalIncidence2", pointOfNormalIncidence2, "XSDataLength")
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
	def delPointOfNormalIncidence2(self): self.__pointOfNormalIncidence2 = None
	# Properties
	pointOfNormalIncidence2 = property(getPointOfNormalIncidence2, setPointOfNormalIncidence2, delPointOfNormalIncidence2, "Property for pointOfNormalIncidence2")
	def getRotation1(self): return self.__rotation1
	def setRotation1(self, rotation1):
		checkType("XSDataGeometrySPD", "setRotation1", rotation1, "XSDataAngle")
		self.__rotation1 = rotation1
	def delRotation1(self): self.__rotation1 = None
	# Properties
	rotation1 = property(getRotation1, setRotation1, delRotation1, "Property for rotation1")
	def getRotation2(self): return self.__rotation2
	def setRotation2(self, rotation2):
		checkType("XSDataGeometrySPD", "setRotation2", rotation2, "XSDataAngle")
		self.__rotation2 = rotation2
	def delRotation2(self): self.__rotation2 = None
	# Properties
	rotation2 = property(getRotation2, setRotation2, delRotation2, "Property for rotation2")
	def getRotation3(self): return self.__rotation3
	def setRotation3(self, rotation3):
		checkType("XSDataGeometrySPD", "setRotation3", rotation3, "XSDataAngle")
		self.__rotation3 = rotation3
	def delRotation3(self): self.__rotation3 = None
	# Properties
	rotation3 = property(getRotation3, setRotation3, delRotation3, "Property for rotation3")
	def export(self, outfile, level, name_='XSDataGeometrySPD'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGeometrySPD'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__sampleDetectorDistance is not None:
			self.sampleDetectorDistance.export(outfile, level, name_='sampleDetectorDistance')
		if self.__pointOfNormalIncidence1 is not None:
			self.pointOfNormalIncidence1.export(outfile, level, name_='pointOfNormalIncidence1')
		if self.__pointOfNormalIncidence2 is not None:
			self.pointOfNormalIncidence2.export(outfile, level, name_='pointOfNormalIncidence2')
		if self.__rotation1 is not None:
			self.rotation1.export(outfile, level, name_='rotation1')
		if self.__rotation2 is not None:
			self.rotation2.export(outfile, level, name_='rotation2')
		if self.__rotation3 is not None:
			self.rotation3.export(outfile, level, name_='rotation3')
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
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGeometrySPD" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGeometrySPD' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGeometrySPD is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGeometrySPD.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGeometrySPD()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGeometrySPD" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGeometrySPD()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGeometrySPD

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

class XSDataInputPyFAI(XSDataInput):
	def __init__(self, configuration=None, maskFile=None, wavelength=None, output=None, input=None, flatFieldImageFile=None, darkCurrentImageFile=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", darkCurrentImageFile, "XSDataFile")
		self.__darkCurrentImageFile = darkCurrentImageFile
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", flatFieldImageFile, "XSDataFile")
		self.__flatFieldImageFile = flatFieldImageFile
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", input, "XSDataImageExt")
		self.__input = input
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", output, "XSDataImageExt")
		self.__output = output
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataInputPyFAI", "Constructor of XSDataInputPyFAI", maskFile, "XSDataFile")
		self.__maskFile = maskFile
	def getDarkCurrentImageFile(self): return self.__darkCurrentImageFile
	def setDarkCurrentImageFile(self, darkCurrentImageFile):
		checkType("XSDataInputPyFAI", "setDarkCurrentImageFile", darkCurrentImageFile, "XSDataFile")
		self.__darkCurrentImageFile = darkCurrentImageFile
	def delDarkCurrentImageFile(self): self.__darkCurrentImageFile = None
	# Properties
	darkCurrentImageFile = property(getDarkCurrentImageFile, setDarkCurrentImageFile, delDarkCurrentImageFile, "Property for darkCurrentImageFile")
	def getFlatFieldImageFile(self): return self.__flatFieldImageFile
	def setFlatFieldImageFile(self, flatFieldImageFile):
		checkType("XSDataInputPyFAI", "setFlatFieldImageFile", flatFieldImageFile, "XSDataFile")
		self.__flatFieldImageFile = flatFieldImageFile
	def delFlatFieldImageFile(self): self.__flatFieldImageFile = None
	# Properties
	flatFieldImageFile = property(getFlatFieldImageFile, setFlatFieldImageFile, delFlatFieldImageFile, "Property for flatFieldImageFile")
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
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputPyFAI", "setMaskFile", maskFile, "XSDataFile")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def export(self, outfile, level, name_='XSDataInputPyFAI'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputPyFAI'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__darkCurrentImageFile is not None:
			self.darkCurrentImageFile.export(outfile, level, name_='darkCurrentImageFile')
		if self.__flatFieldImageFile is not None:
			self.flatFieldImageFile.export(outfile, level, name_='flatFieldImageFile')
		if self.__input is not None:
			self.input.export(outfile, level, name_='input')
		else:
			warnEmptyAttribute("input", "XSDataImageExt")
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__maskFile is not None:
			self.maskFile.export(outfile, level, name_='maskFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkCurrentImageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDarkCurrentImageFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flatFieldImageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFlatFieldImageFile(obj_)
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
			nodeName_ == 'maskFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMaskFile(obj_)
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
		checkType("XSDataInputRefineDiffractionGeometry", "Constructor of XSDataInputRefineDiffractionGeometry", geometrySPD, "XSDataGeometrySPD")
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
		checkType("XSDataInputRefineDiffractionGeometry", "setGeometrySPD", geometrySPD, "XSDataGeometrySPD")
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
			obj_ = XSDataGeometrySPD()
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
		checkType("XSDataResultRefineDiffractionGeometry", "Constructor of XSDataResultRefineDiffractionGeometry", geometrySPD, "XSDataGeometrySPD")
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
		checkType("XSDataResultRefineDiffractionGeometry", "setGeometrySPD", geometrySPD, "XSDataGeometrySPD")
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
			obj_ = XSDataGeometrySPD()
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


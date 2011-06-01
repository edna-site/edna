#!/usr/bin/env python

#
# Generated Thu May 19 10:00::47 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
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
	elif _value is None:
		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
		print(strMessage)
		#raise BaseException(strMessage)


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


class XSDataPeakPosition(XSData):
	"""Set of pixel coordinates and the associated 2Theta diffraction angle"""
	def __init__(self, twoTheta=None, position2=None, position1=None):
		XSData.__init__(self, )
		self.__position1 = position1
		self.__position2 = position2
		self.__twoTheta = twoTheta
	def getPosition1(self): return self.__position1
	def setPosition1(self, position1):
		checkType("XSDataPeakPosition", "setPosition1", position1, "XSDataDouble")
		self.__position1 = position1
	def delPosition1(self): self.__position1 = None
	# Properties
	position1 = property(getPosition1, setPosition1, delPosition1, "Property for position1")
	def getPosition2(self): return self.__position2
	def setPosition2(self, position2):
		checkType("XSDataPeakPosition", "setPosition2", position2, "XSDataDouble")
		self.__position2 = position2
	def delPosition2(self): self.__position2 = None
	# Properties
	position2 = property(getPosition2, setPosition2, delPosition2, "Property for position2")
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
		if self.__position1 is not None:
			self.position1.export(outfile, level, name_='position1')
		else:
			warnEmptyAttribute("position1", "XSDataDouble")
		if self.__position2 is not None:
			self.position2.export(outfile, level, name_='position2')
		else:
			warnEmptyAttribute("position2", "XSDataDouble")
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
			nodeName_ == 'position1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPosition1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'position2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPosition2(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataPeakPosition' )
		outfile.close()
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

class XSDataInputRefineDiffractionGeometry(XSDataInput):
	def __init__(self, configuration=None, guessRotation3=None, guessRotation2=None, guessRotation1=None, guessPointOfNormalIncidence2=None, guessPointOfNormalIncidence1=None, guessSampleDetectorDistance=None, splineFile=None, pixelSize2=None, pixelSize1=None, points=None):
		XSDataInput.__init__(self, configuration)
		if points is None:
			self.__points = []
		else:
			self.__points = points
		self.__pixelSize1 = pixelSize1
		self.__pixelSize2 = pixelSize2
		self.__splineFile = splineFile
		self.__guessSampleDetectorDistance = guessSampleDetectorDistance
		self.__guessPointOfNormalIncidence1 = guessPointOfNormalIncidence1
		self.__guessPointOfNormalIncidence2 = guessPointOfNormalIncidence2
		self.__guessRotation1 = guessRotation1
		self.__guessRotation2 = guessRotation2
		self.__guessRotation3 = guessRotation3
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
	def getPixelSize1(self): return self.__pixelSize1
	def setPixelSize1(self, pixelSize1):
		checkType("XSDataInputRefineDiffractionGeometry", "setPixelSize1", pixelSize1, "XSDataLength")
		self.__pixelSize1 = pixelSize1
	def delPixelSize1(self): self.__pixelSize1 = None
	# Properties
	pixelSize1 = property(getPixelSize1, setPixelSize1, delPixelSize1, "Property for pixelSize1")
	def getPixelSize2(self): return self.__pixelSize2
	def setPixelSize2(self, pixelSize2):
		checkType("XSDataInputRefineDiffractionGeometry", "setPixelSize2", pixelSize2, "XSDataLength")
		self.__pixelSize2 = pixelSize2
	def delPixelSize2(self): self.__pixelSize2 = None
	# Properties
	pixelSize2 = property(getPixelSize2, setPixelSize2, delPixelSize2, "Property for pixelSize2")
	def getSplineFile(self): return self.__splineFile
	def setSplineFile(self, splineFile):
		checkType("XSDataInputRefineDiffractionGeometry", "setSplineFile", splineFile, "XSDataFile")
		self.__splineFile = splineFile
	def delSplineFile(self): self.__splineFile = None
	# Properties
	splineFile = property(getSplineFile, setSplineFile, delSplineFile, "Property for splineFile")
	def getGuessSampleDetectorDistance(self): return self.__guessSampleDetectorDistance
	def setGuessSampleDetectorDistance(self, guessSampleDetectorDistance):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessSampleDetectorDistance", guessSampleDetectorDistance, "XSDataLength")
		self.__guessSampleDetectorDistance = guessSampleDetectorDistance
	def delGuessSampleDetectorDistance(self): self.__guessSampleDetectorDistance = None
	# Properties
	guessSampleDetectorDistance = property(getGuessSampleDetectorDistance, setGuessSampleDetectorDistance, delGuessSampleDetectorDistance, "Property for guessSampleDetectorDistance")
	def getGuessPointOfNormalIncidence1(self): return self.__guessPointOfNormalIncidence1
	def setGuessPointOfNormalIncidence1(self, guessPointOfNormalIncidence1):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessPointOfNormalIncidence1", guessPointOfNormalIncidence1, "XSDataLength")
		self.__guessPointOfNormalIncidence1 = guessPointOfNormalIncidence1
	def delGuessPointOfNormalIncidence1(self): self.__guessPointOfNormalIncidence1 = None
	# Properties
	guessPointOfNormalIncidence1 = property(getGuessPointOfNormalIncidence1, setGuessPointOfNormalIncidence1, delGuessPointOfNormalIncidence1, "Property for guessPointOfNormalIncidence1")
	def getGuessPointOfNormalIncidence2(self): return self.__guessPointOfNormalIncidence2
	def setGuessPointOfNormalIncidence2(self, guessPointOfNormalIncidence2):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessPointOfNormalIncidence2", guessPointOfNormalIncidence2, "XSDataLength")
		self.__guessPointOfNormalIncidence2 = guessPointOfNormalIncidence2
	def delGuessPointOfNormalIncidence2(self): self.__guessPointOfNormalIncidence2 = None
	# Properties
	guessPointOfNormalIncidence2 = property(getGuessPointOfNormalIncidence2, setGuessPointOfNormalIncidence2, delGuessPointOfNormalIncidence2, "Property for guessPointOfNormalIncidence2")
	def getGuessRotation1(self): return self.__guessRotation1
	def setGuessRotation1(self, guessRotation1):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessRotation1", guessRotation1, "XSDataAngle")
		self.__guessRotation1 = guessRotation1
	def delGuessRotation1(self): self.__guessRotation1 = None
	# Properties
	guessRotation1 = property(getGuessRotation1, setGuessRotation1, delGuessRotation1, "Property for guessRotation1")
	def getGuessRotation2(self): return self.__guessRotation2
	def setGuessRotation2(self, guessRotation2):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessRotation2", guessRotation2, "XSDataAngle")
		self.__guessRotation2 = guessRotation2
	def delGuessRotation2(self): self.__guessRotation2 = None
	# Properties
	guessRotation2 = property(getGuessRotation2, setGuessRotation2, delGuessRotation2, "Property for guessRotation2")
	def getGuessRotation3(self): return self.__guessRotation3
	def setGuessRotation3(self, guessRotation3):
		checkType("XSDataInputRefineDiffractionGeometry", "setGuessRotation3", guessRotation3, "XSDataAngle")
		self.__guessRotation3 = guessRotation3
	def delGuessRotation3(self): self.__guessRotation3 = None
	# Properties
	guessRotation3 = property(getGuessRotation3, setGuessRotation3, delGuessRotation3, "Property for guessRotation3")
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
		if self.__pixelSize1 is not None:
			self.pixelSize1.export(outfile, level, name_='pixelSize1')
		else:
			warnEmptyAttribute("pixelSize1", "XSDataLength")
		if self.__pixelSize2 is not None:
			self.pixelSize2.export(outfile, level, name_='pixelSize2')
		else:
			warnEmptyAttribute("pixelSize2", "XSDataLength")
		if self.__splineFile is not None:
			self.splineFile.export(outfile, level, name_='splineFile')
		if self.__guessSampleDetectorDistance is not None:
			self.guessSampleDetectorDistance.export(outfile, level, name_='guessSampleDetectorDistance')
		if self.__guessPointOfNormalIncidence1 is not None:
			self.guessPointOfNormalIncidence1.export(outfile, level, name_='guessPointOfNormalIncidence1')
		if self.__guessPointOfNormalIncidence2 is not None:
			self.guessPointOfNormalIncidence2.export(outfile, level, name_='guessPointOfNormalIncidence2')
		if self.__guessRotation1 is not None:
			self.guessRotation1.export(outfile, level, name_='guessRotation1')
		if self.__guessRotation2 is not None:
			self.guessRotation2.export(outfile, level, name_='guessRotation2')
		if self.__guessRotation3 is not None:
			self.guessRotation3.export(outfile, level, name_='guessRotation3')
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
			nodeName_ == 'pixelSize1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'splineFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSplineFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessSampleDetectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setGuessSampleDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessPointOfNormalIncidence1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setGuessPointOfNormalIncidence1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessPointOfNormalIncidence2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setGuessPointOfNormalIncidence2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessRotation1':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setGuessRotation1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessRotation2':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setGuessRotation2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'guessRotation3':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setGuessRotation3(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputRefineDiffractionGeometry' )
		outfile.close()
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

class XSDataInputSPD(XSDataInput):
	def __init__(self, configuration=None, outputDir=None, wavelength=None, tiltRotation=None, spatialDistortionFile=None, sampleToDetectorDistance=None, pixelSizeY=None, pixelSizeX=None, outputFileType=None, inputFile=None, flatFieldImageFile=None, distortionFileY=None, distortionFileX=None, darkCurrentImageFile=None, bufferSizeY=None, bufferSizeX=None, beamCentreInPixelsY=None, beamCentreInPixelsX=None, angleOfTilt=None):
		XSDataInput.__init__(self, configuration)
		self.__angleOfTilt = angleOfTilt
		self.__beamCentreInPixelsX = beamCentreInPixelsX
		self.__beamCentreInPixelsY = beamCentreInPixelsY
		self.__bufferSizeX = bufferSizeX
		self.__bufferSizeY = bufferSizeY
		self.__darkCurrentImageFile = darkCurrentImageFile
		self.__distortionFileX = distortionFileX
		self.__distortionFileY = distortionFileY
		self.__flatFieldImageFile = flatFieldImageFile
		self.__inputFile = inputFile
		self.__outputFileType = outputFileType
		self.__pixelSizeX = pixelSizeX
		self.__pixelSizeY = pixelSizeY
		self.__sampleToDetectorDistance = sampleToDetectorDistance
		self.__spatialDistortionFile = spatialDistortionFile
		self.__tiltRotation = tiltRotation
		self.__wavelength = wavelength
		self.__outputDir = outputDir
	def getAngleOfTilt(self): return self.__angleOfTilt
	def setAngleOfTilt(self, angleOfTilt):
		checkType("XSDataInputSPD", "setAngleOfTilt", angleOfTilt, "XSDataAngle")
		self.__angleOfTilt = angleOfTilt
	def delAngleOfTilt(self): self.__angleOfTilt = None
	# Properties
	angleOfTilt = property(getAngleOfTilt, setAngleOfTilt, delAngleOfTilt, "Property for angleOfTilt")
	def getBeamCentreInPixelsX(self): return self.__beamCentreInPixelsX
	def setBeamCentreInPixelsX(self, beamCentreInPixelsX):
		checkType("XSDataInputSPD", "setBeamCentreInPixelsX", beamCentreInPixelsX, "XSDataDouble")
		self.__beamCentreInPixelsX = beamCentreInPixelsX
	def delBeamCentreInPixelsX(self): self.__beamCentreInPixelsX = None
	# Properties
	beamCentreInPixelsX = property(getBeamCentreInPixelsX, setBeamCentreInPixelsX, delBeamCentreInPixelsX, "Property for beamCentreInPixelsX")
	def getBeamCentreInPixelsY(self): return self.__beamCentreInPixelsY
	def setBeamCentreInPixelsY(self, beamCentreInPixelsY):
		checkType("XSDataInputSPD", "setBeamCentreInPixelsY", beamCentreInPixelsY, "XSDataDouble")
		self.__beamCentreInPixelsY = beamCentreInPixelsY
	def delBeamCentreInPixelsY(self): self.__beamCentreInPixelsY = None
	# Properties
	beamCentreInPixelsY = property(getBeamCentreInPixelsY, setBeamCentreInPixelsY, delBeamCentreInPixelsY, "Property for beamCentreInPixelsY")
	def getBufferSizeX(self): return self.__bufferSizeX
	def setBufferSizeX(self, bufferSizeX):
		checkType("XSDataInputSPD", "setBufferSizeX", bufferSizeX, "XSDataInteger")
		self.__bufferSizeX = bufferSizeX
	def delBufferSizeX(self): self.__bufferSizeX = None
	# Properties
	bufferSizeX = property(getBufferSizeX, setBufferSizeX, delBufferSizeX, "Property for bufferSizeX")
	def getBufferSizeY(self): return self.__bufferSizeY
	def setBufferSizeY(self, bufferSizeY):
		checkType("XSDataInputSPD", "setBufferSizeY", bufferSizeY, "XSDataInteger")
		self.__bufferSizeY = bufferSizeY
	def delBufferSizeY(self): self.__bufferSizeY = None
	# Properties
	bufferSizeY = property(getBufferSizeY, setBufferSizeY, delBufferSizeY, "Property for bufferSizeY")
	def getDarkCurrentImageFile(self): return self.__darkCurrentImageFile
	def setDarkCurrentImageFile(self, darkCurrentImageFile):
		checkType("XSDataInputSPD", "setDarkCurrentImageFile", darkCurrentImageFile, "XSDataFile")
		self.__darkCurrentImageFile = darkCurrentImageFile
	def delDarkCurrentImageFile(self): self.__darkCurrentImageFile = None
	# Properties
	darkCurrentImageFile = property(getDarkCurrentImageFile, setDarkCurrentImageFile, delDarkCurrentImageFile, "Property for darkCurrentImageFile")
	def getDistortionFileX(self): return self.__distortionFileX
	def setDistortionFileX(self, distortionFileX):
		checkType("XSDataInputSPD", "setDistortionFileX", distortionFileX, "XSDataFile")
		self.__distortionFileX = distortionFileX
	def delDistortionFileX(self): self.__distortionFileX = None
	# Properties
	distortionFileX = property(getDistortionFileX, setDistortionFileX, delDistortionFileX, "Property for distortionFileX")
	def getDistortionFileY(self): return self.__distortionFileY
	def setDistortionFileY(self, distortionFileY):
		checkType("XSDataInputSPD", "setDistortionFileY", distortionFileY, "XSDataFile")
		self.__distortionFileY = distortionFileY
	def delDistortionFileY(self): self.__distortionFileY = None
	# Properties
	distortionFileY = property(getDistortionFileY, setDistortionFileY, delDistortionFileY, "Property for distortionFileY")
	def getFlatFieldImageFile(self): return self.__flatFieldImageFile
	def setFlatFieldImageFile(self, flatFieldImageFile):
		checkType("XSDataInputSPD", "setFlatFieldImageFile", flatFieldImageFile, "XSDataFile")
		self.__flatFieldImageFile = flatFieldImageFile
	def delFlatFieldImageFile(self): self.__flatFieldImageFile = None
	# Properties
	flatFieldImageFile = property(getFlatFieldImageFile, setFlatFieldImageFile, delFlatFieldImageFile, "Property for flatFieldImageFile")
	def getInputFile(self): return self.__inputFile
	def setInputFile(self, inputFile):
		checkType("XSDataInputSPD", "setInputFile", inputFile, "XSDataFile")
		self.__inputFile = inputFile
	def delInputFile(self): self.__inputFile = None
	# Properties
	inputFile = property(getInputFile, setInputFile, delInputFile, "Property for inputFile")
	def getOutputFileType(self): return self.__outputFileType
	def setOutputFileType(self, outputFileType):
		checkType("XSDataInputSPD", "setOutputFileType", outputFileType, "XSDataString")
		self.__outputFileType = outputFileType
	def delOutputFileType(self): self.__outputFileType = None
	# Properties
	outputFileType = property(getOutputFileType, setOutputFileType, delOutputFileType, "Property for outputFileType")
	def getPixelSizeX(self): return self.__pixelSizeX
	def setPixelSizeX(self, pixelSizeX):
		checkType("XSDataInputSPD", "setPixelSizeX", pixelSizeX, "XSDataLength")
		self.__pixelSizeX = pixelSizeX
	def delPixelSizeX(self): self.__pixelSizeX = None
	# Properties
	pixelSizeX = property(getPixelSizeX, setPixelSizeX, delPixelSizeX, "Property for pixelSizeX")
	def getPixelSizeY(self): return self.__pixelSizeY
	def setPixelSizeY(self, pixelSizeY):
		checkType("XSDataInputSPD", "setPixelSizeY", pixelSizeY, "XSDataLength")
		self.__pixelSizeY = pixelSizeY
	def delPixelSizeY(self): self.__pixelSizeY = None
	# Properties
	pixelSizeY = property(getPixelSizeY, setPixelSizeY, delPixelSizeY, "Property for pixelSizeY")
	def getSampleToDetectorDistance(self): return self.__sampleToDetectorDistance
	def setSampleToDetectorDistance(self, sampleToDetectorDistance):
		checkType("XSDataInputSPD", "setSampleToDetectorDistance", sampleToDetectorDistance, "XSDataLength")
		self.__sampleToDetectorDistance = sampleToDetectorDistance
	def delSampleToDetectorDistance(self): self.__sampleToDetectorDistance = None
	# Properties
	sampleToDetectorDistance = property(getSampleToDetectorDistance, setSampleToDetectorDistance, delSampleToDetectorDistance, "Property for sampleToDetectorDistance")
	def getSpatialDistortionFile(self): return self.__spatialDistortionFile
	def setSpatialDistortionFile(self, spatialDistortionFile):
		checkType("XSDataInputSPD", "setSpatialDistortionFile", spatialDistortionFile, "XSDataFile")
		self.__spatialDistortionFile = spatialDistortionFile
	def delSpatialDistortionFile(self): self.__spatialDistortionFile = None
	# Properties
	spatialDistortionFile = property(getSpatialDistortionFile, setSpatialDistortionFile, delSpatialDistortionFile, "Property for spatialDistortionFile")
	def getTiltRotation(self): return self.__tiltRotation
	def setTiltRotation(self, tiltRotation):
		checkType("XSDataInputSPD", "setTiltRotation", tiltRotation, "XSDataAngle")
		self.__tiltRotation = tiltRotation
	def delTiltRotation(self): self.__tiltRotation = None
	# Properties
	tiltRotation = property(getTiltRotation, setTiltRotation, delTiltRotation, "Property for tiltRotation")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputSPD", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getOutputDir(self): return self.__outputDir
	def setOutputDir(self, outputDir):
		checkType("XSDataInputSPD", "setOutputDir", outputDir, "XSDataFile")
		self.__outputDir = outputDir
	def delOutputDir(self): self.__outputDir = None
	# Properties
	outputDir = property(getOutputDir, setOutputDir, delOutputDir, "Property for outputDir")
	def export(self, outfile, level, name_='XSDataInputSPD'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSPD'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__angleOfTilt is not None:
			self.angleOfTilt.export(outfile, level, name_='angleOfTilt')
		if self.__beamCentreInPixelsX is not None:
			self.beamCentreInPixelsX.export(outfile, level, name_='beamCentreInPixelsX')
		if self.__beamCentreInPixelsY is not None:
			self.beamCentreInPixelsY.export(outfile, level, name_='beamCentreInPixelsY')
		if self.__bufferSizeX is not None:
			self.bufferSizeX.export(outfile, level, name_='bufferSizeX')
		if self.__bufferSizeY is not None:
			self.bufferSizeY.export(outfile, level, name_='bufferSizeY')
		if self.__darkCurrentImageFile is not None:
			self.darkCurrentImageFile.export(outfile, level, name_='darkCurrentImageFile')
		if self.__distortionFileX is not None:
			self.distortionFileX.export(outfile, level, name_='distortionFileX')
		if self.__distortionFileY is not None:
			self.distortionFileY.export(outfile, level, name_='distortionFileY')
		if self.__flatFieldImageFile is not None:
			self.flatFieldImageFile.export(outfile, level, name_='flatFieldImageFile')
		if self.__inputFile is not None:
			self.inputFile.export(outfile, level, name_='inputFile')
		else:
			warnEmptyAttribute("inputFile", "XSDataFile")
		if self.__outputFileType is not None:
			self.outputFileType.export(outfile, level, name_='outputFileType')
		if self.__pixelSizeX is not None:
			self.pixelSizeX.export(outfile, level, name_='pixelSizeX')
		if self.__pixelSizeY is not None:
			self.pixelSizeY.export(outfile, level, name_='pixelSizeY')
		if self.__sampleToDetectorDistance is not None:
			self.sampleToDetectorDistance.export(outfile, level, name_='sampleToDetectorDistance')
		if self.__spatialDistortionFile is not None:
			self.spatialDistortionFile.export(outfile, level, name_='spatialDistortionFile')
		if self.__tiltRotation is not None:
			self.tiltRotation.export(outfile, level, name_='tiltRotation')
		else:
			warnEmptyAttribute("tiltRotation", "XSDataAngle")
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__outputDir is not None:
			self.outputDir.export(outfile, level, name_='outputDir')
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
			nodeName_ == 'bufferSizeX':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setBufferSizeX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bufferSizeY':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setBufferSizeY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkCurrentImageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDarkCurrentImageFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distortionFileX':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDistortionFileX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distortionFileY':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDistortionFileY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flatFieldImageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFlatFieldImageFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFileType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutputFileType(obj_)
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
			nodeName_ == 'sampleToDetectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setSampleToDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spatialDistortionFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSpatialDistortionFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'tiltRotation':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setTiltRotation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputDir':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputDir(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputSPD" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSPD' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSPD.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSPD()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSPD" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSPD()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSPD

class XSDataResultRefineDiffractionGeometry(XSDataResult):
	def __init__(self, status=None, rotation3=None, rotation2=None, rotation1=None, pointOfNormalIncidence2=None, pointOfNormalIncidence1=None, sampleDetectorDistance=None):
		XSDataResult.__init__(self, status)
		self.__sampleDetectorDistance = sampleDetectorDistance
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
		self.__rotation1 = rotation1
		self.__rotation2 = rotation2
		self.__rotation3 = rotation3
	def getSampleDetectorDistance(self): return self.__sampleDetectorDistance
	def setSampleDetectorDistance(self, sampleDetectorDistance):
		checkType("XSDataResultRefineDiffractionGeometry", "setSampleDetectorDistance", sampleDetectorDistance, "XSDataLength")
		self.__sampleDetectorDistance = sampleDetectorDistance
	def delSampleDetectorDistance(self): self.__sampleDetectorDistance = None
	# Properties
	sampleDetectorDistance = property(getSampleDetectorDistance, setSampleDetectorDistance, delSampleDetectorDistance, "Property for sampleDetectorDistance")
	def getPointOfNormalIncidence1(self): return self.__pointOfNormalIncidence1
	def setPointOfNormalIncidence1(self, pointOfNormalIncidence1):
		checkType("XSDataResultRefineDiffractionGeometry", "setPointOfNormalIncidence1", pointOfNormalIncidence1, "XSDataLength")
		self.__pointOfNormalIncidence1 = pointOfNormalIncidence1
	def delPointOfNormalIncidence1(self): self.__pointOfNormalIncidence1 = None
	# Properties
	pointOfNormalIncidence1 = property(getPointOfNormalIncidence1, setPointOfNormalIncidence1, delPointOfNormalIncidence1, "Property for pointOfNormalIncidence1")
	def getPointOfNormalIncidence2(self): return self.__pointOfNormalIncidence2
	def setPointOfNormalIncidence2(self, pointOfNormalIncidence2):
		checkType("XSDataResultRefineDiffractionGeometry", "setPointOfNormalIncidence2", pointOfNormalIncidence2, "XSDataLength")
		self.__pointOfNormalIncidence2 = pointOfNormalIncidence2
	def delPointOfNormalIncidence2(self): self.__pointOfNormalIncidence2 = None
	# Properties
	pointOfNormalIncidence2 = property(getPointOfNormalIncidence2, setPointOfNormalIncidence2, delPointOfNormalIncidence2, "Property for pointOfNormalIncidence2")
	def getRotation1(self): return self.__rotation1
	def setRotation1(self, rotation1):
		checkType("XSDataResultRefineDiffractionGeometry", "setRotation1", rotation1, "XSDataAngle")
		self.__rotation1 = rotation1
	def delRotation1(self): self.__rotation1 = None
	# Properties
	rotation1 = property(getRotation1, setRotation1, delRotation1, "Property for rotation1")
	def getRotation2(self): return self.__rotation2
	def setRotation2(self, rotation2):
		checkType("XSDataResultRefineDiffractionGeometry", "setRotation2", rotation2, "XSDataAngle")
		self.__rotation2 = rotation2
	def delRotation2(self): self.__rotation2 = None
	# Properties
	rotation2 = property(getRotation2, setRotation2, delRotation2, "Property for rotation2")
	def getRotation3(self): return self.__rotation3
	def setRotation3(self, rotation3):
		checkType("XSDataResultRefineDiffractionGeometry", "setRotation3", rotation3, "XSDataAngle")
		self.__rotation3 = rotation3
	def delRotation3(self): self.__rotation3 = None
	# Properties
	rotation3 = property(getRotation3, setRotation3, delRotation3, "Property for rotation3")
	def export(self, outfile, level, name_='XSDataResultRefineDiffractionGeometry'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultRefineDiffractionGeometry'):
		XSDataResult.exportChildren(self, outfile, level, name_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultRefineDiffractionGeometry' )
		outfile.close()
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

class XSDataResultSPD(XSDataResult):
	def __init__(self, status=None, correctedFile=None):
		XSDataResult.__init__(self, status)
		self.__correctedFile = correctedFile
	def getCorrectedFile(self): return self.__correctedFile
	def setCorrectedFile(self, correctedFile):
		checkType("XSDataResultSPD", "setCorrectedFile", correctedFile, "XSDataFile")
		self.__correctedFile = correctedFile
	def delCorrectedFile(self): self.__correctedFile = None
	# Properties
	correctedFile = property(getCorrectedFile, setCorrectedFile, delCorrectedFile, "Property for correctedFile")
	def export(self, outfile, level, name_='XSDataResultSPD'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSPD'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__correctedFile is not None:
			self.correctedFile.export(outfile, level, name_='correctedFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correctedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setCorrectedFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSPD" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSPD' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSPD.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSPD()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSPD" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSPD()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSPD

class XSDataInputSPDCake(XSDataInputSPD):
	def __init__(self, configuration=None, outputDir=None, wavelength=None, tiltRotation=None, spatialDistortionFile=None, sampleToDetectorDistance=None, pixelSizeY=None, pixelSizeX=None, outputFileType=None, inputFile=None, flatFieldImageFile=None, distortionFileY=None, distortionFileX=None, darkCurrentImageFile=None, bufferSizeY=None, bufferSizeX=None, beamCentreInPixelsY=None, beamCentreInPixelsX=None, angleOfTilt=None, correctTiltMask=None, intensityScaleFactor=None, maskFile=None, stopAzimuth=None, stepAzimuth=None, startAzimuth=None, deleteCorImg=None, outputDirCake=None, outputAxis=None, outerRadius=None, innerRadius=None):
		XSDataInputSPD.__init__(self, configuration, outputDir, wavelength, tiltRotation, spatialDistortionFile, sampleToDetectorDistance, pixelSizeY, pixelSizeX, outputFileType, inputFile, flatFieldImageFile, distortionFileY, distortionFileX, darkCurrentImageFile, bufferSizeY, bufferSizeX, beamCentreInPixelsY, beamCentreInPixelsX, angleOfTilt)
		self.__innerRadius = innerRadius
		self.__outerRadius = outerRadius
		self.__outputAxis = outputAxis
		self.__outputDirCake = outputDirCake
		self.__deleteCorImg = deleteCorImg
		self.__startAzimuth = startAzimuth
		self.__stepAzimuth = stepAzimuth
		self.__stopAzimuth = stopAzimuth
		self.__maskFile = maskFile
		self.__intensityScaleFactor = intensityScaleFactor
		self.__correctTiltMask = correctTiltMask
	def getInnerRadius(self): return self.__innerRadius
	def setInnerRadius(self, innerRadius):
		checkType("XSDataInputSPDCake", "setInnerRadius", innerRadius, "XSDataDouble")
		self.__innerRadius = innerRadius
	def delInnerRadius(self): self.__innerRadius = None
	# Properties
	innerRadius = property(getInnerRadius, setInnerRadius, delInnerRadius, "Property for innerRadius")
	def getOuterRadius(self): return self.__outerRadius
	def setOuterRadius(self, outerRadius):
		checkType("XSDataInputSPDCake", "setOuterRadius", outerRadius, "XSDataDouble")
		self.__outerRadius = outerRadius
	def delOuterRadius(self): self.__outerRadius = None
	# Properties
	outerRadius = property(getOuterRadius, setOuterRadius, delOuterRadius, "Property for outerRadius")
	def getOutputAxis(self): return self.__outputAxis
	def setOutputAxis(self, outputAxis):
		checkType("XSDataInputSPDCake", "setOutputAxis", outputAxis, "XSDataString")
		self.__outputAxis = outputAxis
	def delOutputAxis(self): self.__outputAxis = None
	# Properties
	outputAxis = property(getOutputAxis, setOutputAxis, delOutputAxis, "Property for outputAxis")
	def getOutputDirCake(self): return self.__outputDirCake
	def setOutputDirCake(self, outputDirCake):
		checkType("XSDataInputSPDCake", "setOutputDirCake", outputDirCake, "XSDataFile")
		self.__outputDirCake = outputDirCake
	def delOutputDirCake(self): self.__outputDirCake = None
	# Properties
	outputDirCake = property(getOutputDirCake, setOutputDirCake, delOutputDirCake, "Property for outputDirCake")
	def getDeleteCorImg(self): return self.__deleteCorImg
	def setDeleteCorImg(self, deleteCorImg):
		checkType("XSDataInputSPDCake", "setDeleteCorImg", deleteCorImg, "XSDataBoolean")
		self.__deleteCorImg = deleteCorImg
	def delDeleteCorImg(self): self.__deleteCorImg = None
	# Properties
	deleteCorImg = property(getDeleteCorImg, setDeleteCorImg, delDeleteCorImg, "Property for deleteCorImg")
	def getStartAzimuth(self): return self.__startAzimuth
	def setStartAzimuth(self, startAzimuth):
		checkType("XSDataInputSPDCake", "setStartAzimuth", startAzimuth, "XSDataAngle")
		self.__startAzimuth = startAzimuth
	def delStartAzimuth(self): self.__startAzimuth = None
	# Properties
	startAzimuth = property(getStartAzimuth, setStartAzimuth, delStartAzimuth, "Property for startAzimuth")
	def getStepAzimuth(self): return self.__stepAzimuth
	def setStepAzimuth(self, stepAzimuth):
		checkType("XSDataInputSPDCake", "setStepAzimuth", stepAzimuth, "XSDataAngle")
		self.__stepAzimuth = stepAzimuth
	def delStepAzimuth(self): self.__stepAzimuth = None
	# Properties
	stepAzimuth = property(getStepAzimuth, setStepAzimuth, delStepAzimuth, "Property for stepAzimuth")
	def getStopAzimuth(self): return self.__stopAzimuth
	def setStopAzimuth(self, stopAzimuth):
		checkType("XSDataInputSPDCake", "setStopAzimuth", stopAzimuth, "XSDataAngle")
		self.__stopAzimuth = stopAzimuth
	def delStopAzimuth(self): self.__stopAzimuth = None
	# Properties
	stopAzimuth = property(getStopAzimuth, setStopAzimuth, delStopAzimuth, "Property for stopAzimuth")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputSPDCake", "setMaskFile", maskFile, "XSDataFile")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getIntensityScaleFactor(self): return self.__intensityScaleFactor
	def setIntensityScaleFactor(self, intensityScaleFactor):
		checkType("XSDataInputSPDCake", "setIntensityScaleFactor", intensityScaleFactor, "XSDataDouble")
		self.__intensityScaleFactor = intensityScaleFactor
	def delIntensityScaleFactor(self): self.__intensityScaleFactor = None
	# Properties
	intensityScaleFactor = property(getIntensityScaleFactor, setIntensityScaleFactor, delIntensityScaleFactor, "Property for intensityScaleFactor")
	def getCorrectTiltMask(self): return self.__correctTiltMask
	def setCorrectTiltMask(self, correctTiltMask):
		checkType("XSDataInputSPDCake", "setCorrectTiltMask", correctTiltMask, "XSDataBoolean")
		self.__correctTiltMask = correctTiltMask
	def delCorrectTiltMask(self): self.__correctTiltMask = None
	# Properties
	correctTiltMask = property(getCorrectTiltMask, setCorrectTiltMask, delCorrectTiltMask, "Property for correctTiltMask")
	def export(self, outfile, level, name_='XSDataInputSPDCake'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSPDCake'):
		XSDataInputSPD.exportChildren(self, outfile, level, name_)
		if self.__innerRadius is not None:
			self.innerRadius.export(outfile, level, name_='innerRadius')
		if self.__outerRadius is not None:
			self.outerRadius.export(outfile, level, name_='outerRadius')
		if self.__outputAxis is not None:
			self.outputAxis.export(outfile, level, name_='outputAxis')
		if self.__outputDirCake is not None:
			self.outputDirCake.export(outfile, level, name_='outputDirCake')
		if self.__deleteCorImg is not None:
			self.deleteCorImg.export(outfile, level, name_='deleteCorImg')
		if self.__startAzimuth is not None:
			self.startAzimuth.export(outfile, level, name_='startAzimuth')
		if self.__stepAzimuth is not None:
			self.stepAzimuth.export(outfile, level, name_='stepAzimuth')
		if self.__stopAzimuth is not None:
			self.stopAzimuth.export(outfile, level, name_='stopAzimuth')
		if self.__maskFile is not None:
			self.maskFile.export(outfile, level, name_='maskFile')
		if self.__intensityScaleFactor is not None:
			self.intensityScaleFactor.export(outfile, level, name_='intensityScaleFactor')
		if self.__correctTiltMask is not None:
			self.correctTiltMask.export(outfile, level, name_='correctTiltMask')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'innerRadius':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setInnerRadius(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outerRadius':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setOuterRadius(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputAxis':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutputAxis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputDirCake':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputDirCake(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deleteCorImg':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDeleteCorImg(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startAzimuth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setStartAzimuth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'stepAzimuth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setStepAzimuth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'stopAzimuth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setStopAzimuth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'intensityScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIntensityScaleFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correctTiltMask':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setCorrectTiltMask(obj_)
		XSDataInputSPD.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputSPDCake" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSPDCake' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSPDCake.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSPDCake()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSPDCake" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSPDCake()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSPDCake

class XSDataResultSPDCake(XSDataResultSPD):
	def __init__(self, status=None, correctedFile=None, cakedFile=None):
		XSDataResultSPD.__init__(self, status, correctedFile)
		self.__cakedFile = cakedFile
	def getCakedFile(self): return self.__cakedFile
	def setCakedFile(self, cakedFile):
		checkType("XSDataResultSPDCake", "setCakedFile", cakedFile, "XSDataFile")
		self.__cakedFile = cakedFile
	def delCakedFile(self): self.__cakedFile = None
	# Properties
	cakedFile = property(getCakedFile, setCakedFile, delCakedFile, "Property for cakedFile")
	def export(self, outfile, level, name_='XSDataResultSPDCake'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSPDCake'):
		XSDataResultSPD.exportChildren(self, outfile, level, name_)
		if self.__cakedFile is not None:
			self.cakedFile.export(outfile, level, name_='cakedFile')
		else:
			warnEmptyAttribute("cakedFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cakedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setCakedFile(obj_)
		XSDataResultSPD.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSPDCake" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSPDCake' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSPDCake.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSPDCake()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSPDCake" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSPDCake()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSPDCake



# End of data representation classes.



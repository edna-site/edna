#!/usr/bin/env python

#
# Generated Tue Oct 18 11:46::29 2011 by EDGenerateDS.
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
 "XSDataEdnaSaxs": "ednaSaxs/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataEdnaSaxs import XSDataAutoRg
	from XSDataCommon import XSDataImage
	from XSDataCommon import XSDataLength
	from XSDataCommon import XSDataTime
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataEdnaSaxs import XSDataAutoRg
from XSDataCommon import XSDataImage
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


class XSDataBioSaxsExperimentSetup(XSData):
	def __init__(self, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
		XSData.__init__(self, )
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", detector, "XSDataString")
		self.__detector = detector
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", maskFile, "XSDataImage")
		self.__maskFile = maskFile
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
		checkType("XSDataBioSaxsExperimentSetup", "Constructor of XSDataBioSaxsExperimentSetup", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataBioSaxsExperimentSetup", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataBioSaxsExperimentSetup", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataBioSaxsExperimentSetup", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataBioSaxsExperimentSetup", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataBioSaxsExperimentSetup", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataBioSaxsExperimentSetup", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataBioSaxsExperimentSetup", "setMachineCurrent", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataBioSaxsExperimentSetup", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataBioSaxsExperimentSetup", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getStorageTemperature(self): return self.__storageTemperature
	def setStorageTemperature(self, storageTemperature):
		checkType("XSDataBioSaxsExperimentSetup", "setStorageTemperature", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
	def delStorageTemperature(self): self.__storageTemperature = None
	# Properties
	storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
	def getExposureTemperature(self): return self.__exposureTemperature
	def setExposureTemperature(self, exposureTemperature):
		checkType("XSDataBioSaxsExperimentSetup", "setExposureTemperature", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
	def delExposureTemperature(self): self.__exposureTemperature = None
	# Properties
	exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataBioSaxsExperimentSetup", "setExposureTime", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getFrameNumber(self): return self.__frameNumber
	def setFrameNumber(self, frameNumber):
		checkType("XSDataBioSaxsExperimentSetup", "setFrameNumber", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
	def delFrameNumber(self): self.__frameNumber = None
	# Properties
	frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
	def getFrameMax(self): return self.__frameMax
	def setFrameMax(self, frameMax):
		checkType("XSDataBioSaxsExperimentSetup", "setFrameMax", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def delFrameMax(self): self.__frameMax = None
	# Properties
	frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
	def export(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		if self.__detectorDistance is not None:
			self.detectorDistance.export(outfile, level, name_='detectorDistance')
		if self.__pixelSize_1 is not None:
			self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
		if self.__pixelSize_2 is not None:
			self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
		if self.__beamCenter_1 is not None:
			self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
		if self.__beamCenter_2 is not None:
			self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
		if self.__beamStopDiode is not None:
			self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__machineCurrent is not None:
			self.machineCurrent.export(outfile, level, name_='machineCurrent')
		if self.__maskFile is not None:
			self.maskFile.export(outfile, level, name_='maskFile')
		if self.__normalizationFactor is not None:
			self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
		if self.__storageTemperature is not None:
			self.storageTemperature.export(outfile, level, name_='storageTemperature')
		if self.__exposureTemperature is not None:
			self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self.__frameNumber is not None:
			self.frameNumber.export(outfile, level, name_='frameNumber')
		if self.__frameMax is not None:
			self.frameMax.export(outfile, level, name_='frameMax')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'storageTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setStorageTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setExposureTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameMax':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameMax(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBioSaxsExperimentSetup' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBioSaxsExperimentSetup is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBioSaxsExperimentSetup.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBioSaxsExperimentSetup()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBioSaxsExperimentSetup()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsExperimentSetup

class XSDataBioSaxsSample(XSData):
	def __init__(self, code=None, comments=None, concentration=None):
		XSData.__init__(self, )
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", concentration, "XSDataDouble")
		self.__concentration = concentration
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", code, "XSDataString")
		self.__code = code
	def getConcentration(self): return self.__concentration
	def setConcentration(self, concentration):
		checkType("XSDataBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
		self.__concentration = concentration
	def delConcentration(self): self.__concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataBioSaxsSample", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDataBioSaxsSample", "setCode", code, "XSDataString")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def export(self, outfile, level, name_='XSDataBioSaxsSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBioSaxsSample'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
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
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCode(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBioSaxsSample' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBioSaxsSample is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBioSaxsSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBioSaxsSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBioSaxsSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsSample

class XSDataFileSeries(XSData):
	def __init__(self, files=None):
		XSData.__init__(self, )
		if files is None:
			self.__files = []
		else:
			checkType("XSDataFileSeries", "Constructor of XSDataFileSeries", files, "list")
			self.__files = files
	def getFiles(self): return self.__files
	def setFiles(self, files):
		checkType("XSDataFileSeries", "setFiles", files, "list")
		self.__files = files
	def delFiles(self): self.__files = None
	# Properties
	files = property(getFiles, setFiles, delFiles, "Property for files")
	def addFiles(self, value):
		checkType("XSDataFileSeries", "setFiles", value, "XSDataFile")
		self.__files.append(value)
	def insertFiles(self, index, value):
		checkType("XSDataFileSeries", "setFiles", value, "XSDataFile")
		self.__files[index] = value
	def export(self, outfile, level, name_='XSDataFileSeries'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataFileSeries'):
		XSData.exportChildren(self, outfile, level, name_)
		for files_ in self.getFiles():
			files_.export(outfile, level, name_='files')
		if self.getFiles() == []:
			warnEmptyAttribute("files", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'files':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.files.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataFileSeries" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataFileSeries' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataFileSeries is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataFileSeries.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataFileSeries()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataFileSeries" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataFileSeries()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataFileSeries

class XSDataInputBioSaxsAsciiExportv1_0(XSDataInput):
	def __init__(self, configuration=None, experimentSetup=None, sample=None, integratedCurve=None, integratedImage=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "Constructor of XSDataInputBioSaxsAsciiExportv1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def export(self, outfile, level, name_='XSDataInputBioSaxsAsciiExportv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAsciiExportv1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		else:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
		else:
			warnEmptyAttribute("integratedCurve", "XSDataFile")
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setIntegratedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAsciiExportv1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsAsciiExportv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAsciiExportv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAsciiExportv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAsciiExportv1_0

class XSDataInputBioSaxsAzimutIntv1_0(XSDataInput):
	def __init__(self, configuration=None, experimentSetup=None, sample=None, correctedImage=None, integratedCurve=None, integratedImage=None, normalizedImageSize=None, normalizedImage=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", normalizedImageSize, "XSDataInteger")
		self.__normalizedImageSize = normalizedImageSize
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", correctedImage, "XSDataImage")
		self.__correctedImage = correctedImage
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "Constructor of XSDataInputBioSaxsAzimutIntv1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def getNormalizedImage(self): return self.__normalizedImage
	def setNormalizedImage(self, normalizedImage):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
	def delNormalizedImage(self): self.__normalizedImage = None
	# Properties
	normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
	def getNormalizedImageSize(self): return self.__normalizedImageSize
	def setNormalizedImageSize(self, normalizedImageSize):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setNormalizedImageSize", normalizedImageSize, "XSDataInteger")
		self.__normalizedImageSize = normalizedImageSize
	def delNormalizedImageSize(self): self.__normalizedImageSize = None
	# Properties
	normalizedImageSize = property(getNormalizedImageSize, setNormalizedImageSize, delNormalizedImageSize, "Property for normalizedImageSize")
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def getCorrectedImage(self): return self.__correctedImage
	def setCorrectedImage(self, correctedImage):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setCorrectedImage", correctedImage, "XSDataImage")
		self.__correctedImage = correctedImage
	def delCorrectedImage(self): self.__correctedImage = None
	# Properties
	correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def export(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__normalizedImageSize is not None:
			self.normalizedImageSize.export(outfile, level, name_='normalizedImageSize')
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		else:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
		else:
			warnEmptyAttribute("integratedCurve", "XSDataFile")
		if self.__correctedImage is not None:
			self.correctedImage.export(outfile, level, name_='correctedImage')
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataBioSaxsSample")
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
		else:
			warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setNormalizedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImageSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNormalizedImageSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setIntegratedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correctedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setCorrectedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAzimutIntv1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsAzimutIntv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAzimutIntv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAzimutIntv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAzimutIntv1_0

class XSDataInputBioSaxsNormalizev1_0(XSDataInput):
	def __init__(self, configuration=None, experimentSetup=None, sample=None, rawImageSize=None, normalizedImage=None, logFile=None, rawImage=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", rawImage, "XSDataImage")
		self.__rawImage = rawImage
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsNormalizev1_0", "Constructor of XSDataInputBioSaxsNormalizev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def getRawImage(self): return self.__rawImage
	def setRawImage(self, rawImage):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setRawImage", rawImage, "XSDataImage")
		self.__rawImage = rawImage
	def delRawImage(self): self.__rawImage = None
	# Properties
	rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getNormalizedImage(self): return self.__normalizedImage
	def setNormalizedImage(self, normalizedImage):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
	def delNormalizedImage(self): self.__normalizedImage = None
	# Properties
	normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
	def getRawImageSize(self): return self.__rawImageSize
	def setRawImageSize(self, rawImageSize):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def delRawImageSize(self): self.__rawImageSize = None
	# Properties
	rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def export(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__rawImage is not None:
			self.rawImage.export(outfile, level, name_='rawImage')
		else:
			warnEmptyAttribute("rawImage", "XSDataImage")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__rawImageSize is not None:
			self.rawImageSize.export(outfile, level, name_='rawImageSize')
		else:
			warnEmptyAttribute("rawImageSize", "XSDataInteger")
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataBioSaxsSample")
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
		else:
			warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setRawImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setNormalizedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawImageSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRawImageSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsNormalizev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsNormalizev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsNormalizev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsNormalizev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsNormalizev1_0

class XSDataInputBioSaxsProcessOneFilev1_0(XSDataInput):
	"""Plugin that runs subsequently Normalize and Azimuthal integration"""
	def __init__(self, configuration=None, integratedCurve=None, integratedImage=None, normalizedImage=None, logFile=None, rawImageSize=None, experimentSetup=None, sample=None, rawImage=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", rawImage, "XSDataImage")
		self.__rawImage = rawImage
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "Constructor of XSDataInputBioSaxsProcessOneFilev1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def getRawImage(self): return self.__rawImage
	def setRawImage(self, rawImage):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setRawImage", rawImage, "XSDataImage")
		self.__rawImage = rawImage
	def delRawImage(self): self.__rawImage = None
	# Properties
	rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def getRawImageSize(self): return self.__rawImageSize
	def setRawImageSize(self, rawImageSize):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def delRawImageSize(self): self.__rawImageSize = None
	# Properties
	rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getNormalizedImage(self): return self.__normalizedImage
	def setNormalizedImage(self, normalizedImage):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
	def delNormalizedImage(self): self.__normalizedImage = None
	# Properties
	normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataInputBioSaxsProcessOneFilev1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def export(self, outfile, level, name_='XSDataInputBioSaxsProcessOneFilev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsProcessOneFilev1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__rawImage is not None:
			self.rawImage.export(outfile, level, name_='rawImage')
		else:
			warnEmptyAttribute("rawImage", "XSDataImage")
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataBioSaxsSample")
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
		else:
			warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
		if self.__rawImageSize is not None:
			self.rawImageSize.export(outfile, level, name_='rawImageSize')
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setRawImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawImageSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRawImageSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setNormalizedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setIntegratedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsProcessOneFilev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsProcessOneFilev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsProcessOneFilev1_0

class XSDataInputBioSaxsReduceFileSeriev1_0(XSDataInput):
	"""Run ProcessOneFile on each file of a time time serie  """
	def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", fileSerie, "XSDataFileSeries")
		self.__fileSerie = fileSerie
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directory1D, "XSDataFile")
		self.__directory1D = directory1D
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directory2D, "XSDataFile")
		self.__directory2D = directory2D
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "Constructor of XSDataInputBioSaxsReduceFileSeriev1_0", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def getFileSerie(self): return self.__fileSerie
	def setFileSerie(self, fileSerie):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setFileSerie", fileSerie, "XSDataFileSeries")
		self.__fileSerie = fileSerie
	def delFileSerie(self): self.__fileSerie = None
	# Properties
	fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def getDirectoryMisc(self): return self.__directoryMisc
	def setDirectoryMisc(self, directoryMisc):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def delDirectoryMisc(self): self.__directoryMisc = None
	# Properties
	directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
	def getForceReprocess(self): return self.__forceReprocess
	def setForceReprocess(self, forceReprocess):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setForceReprocess", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
	def delForceReprocess(self): self.__forceReprocess = None
	# Properties
	forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
	def getAbsoluteFidelity(self): return self.__absoluteFidelity
	def setAbsoluteFidelity(self, absoluteFidelity):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
	def delAbsoluteFidelity(self): self.__absoluteFidelity = None
	# Properties
	absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
	def getRelativeFidelity(self): return self.__relativeFidelity
	def setRelativeFidelity(self, relativeFidelity):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
	def delRelativeFidelity(self): self.__relativeFidelity = None
	# Properties
	relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
	def getRawImageSize(self): return self.__rawImageSize
	def setRawImageSize(self, rawImageSize):
		checkType("XSDataInputBioSaxsReduceFileSeriev1_0", "setRawImageSize", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def delRawImageSize(self): self.__rawImageSize = None
	# Properties
	rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
	def export(self, outfile, level, name_='XSDataInputBioSaxsReduceFileSeriev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsReduceFileSeriev1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__fileSerie is not None:
			self.fileSerie.export(outfile, level, name_='fileSerie')
		else:
			warnEmptyAttribute("fileSerie", "XSDataFileSeries")
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataBioSaxsSample")
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
		else:
			warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
		if self.__directory1D is not None:
			self.directory1D.export(outfile, level, name_='directory1D')
		else:
			warnEmptyAttribute("directory1D", "XSDataFile")
		if self.__directory2D is not None:
			self.directory2D.export(outfile, level, name_='directory2D')
		else:
			warnEmptyAttribute("directory2D", "XSDataFile")
		if self.__directoryMisc is not None:
			self.directoryMisc.export(outfile, level, name_='directoryMisc')
		else:
			warnEmptyAttribute("directoryMisc", "XSDataFile")
		if self.__forceReprocess is not None:
			self.forceReprocess.export(outfile, level, name_='forceReprocess')
		if self.__absoluteFidelity is not None:
			self.absoluteFidelity.export(outfile, level, name_='absoluteFidelity')
		if self.__relativeFidelity is not None:
			self.relativeFidelity.export(outfile, level, name_='relativeFidelity')
		if self.__rawImageSize is not None:
			self.rawImageSize.export(outfile, level, name_='rawImageSize')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileSerie':
			obj_ = XSDataFileSeries()
			obj_.build(child_)
			self.setFileSerie(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory1D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory1D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory2D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directoryMisc':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectoryMisc(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'forceReprocess':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setForceReprocess(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absoluteFidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAbsoluteFidelity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'relativeFidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRelativeFidelity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawImageSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRawImageSize(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsReduceFileSeriev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsReduceFileSeriev1_0

class XSDataInputBioSaxsSample(XSDataInput):
	"""temporary class for multiple inhertitance emulation"""
	def __init__(self, configuration=None, code=None, comments=None, concentration=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", concentration, "XSDataDouble")
		self.__concentration = concentration
		checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataInputBioSaxsSample", "Constructor of XSDataInputBioSaxsSample", code, "XSDataString")
		self.__code = code
	def getConcentration(self): return self.__concentration
	def setConcentration(self, concentration):
		checkType("XSDataInputBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
		self.__concentration = concentration
	def delConcentration(self): self.__concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataInputBioSaxsSample", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDataInputBioSaxsSample", "setCode", code, "XSDataString")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def export(self, outfile, level, name_='XSDataInputBioSaxsSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSample'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
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
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCode(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsSample' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsSample is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSample

class XSDataInputBioSaxsSmartMergev1_0(XSDataInput):
	def __init__(self, configuration=None, mergedCurve=None, sample=None, relativeFidelity=None, absoluteFidelity=None, inputCurves=None):
		XSDataInput.__init__(self, configuration)
		if inputCurves is None:
			self.__inputCurves = []
		else:
			checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", inputCurves, "list")
			self.__inputCurves = inputCurves
		checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
		checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
		checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputBioSaxsSmartMergev1_0", "Constructor of XSDataInputBioSaxsSmartMergev1_0", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
	def getInputCurves(self): return self.__inputCurves
	def setInputCurves(self, inputCurves):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", inputCurves, "list")
		self.__inputCurves = inputCurves
	def delInputCurves(self): self.__inputCurves = None
	# Properties
	inputCurves = property(getInputCurves, setInputCurves, delInputCurves, "Property for inputCurves")
	def addInputCurves(self, value):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", value, "XSDataFile")
		self.__inputCurves.append(value)
	def insertInputCurves(self, index, value):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputCurves", value, "XSDataFile")
		self.__inputCurves[index] = value
	def getAbsoluteFidelity(self): return self.__absoluteFidelity
	def setAbsoluteFidelity(self, absoluteFidelity):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
	def delAbsoluteFidelity(self): self.__absoluteFidelity = None
	# Properties
	absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
	def getRelativeFidelity(self): return self.__relativeFidelity
	def setRelativeFidelity(self, relativeFidelity):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
	def delRelativeFidelity(self): self.__relativeFidelity = None
	# Properties
	relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getMergedCurve(self): return self.__mergedCurve
	def setMergedCurve(self, mergedCurve):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
	def delMergedCurve(self): self.__mergedCurve = None
	# Properties
	mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
	def export(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputCurves_ in self.getInputCurves():
			inputCurves_.export(outfile, level, name_='inputCurves')
		if self.getInputCurves() == []:
			warnEmptyAttribute("inputCurves", "XSDataFile")
		if self.__absoluteFidelity is not None:
			self.absoluteFidelity.export(outfile, level, name_='absoluteFidelity')
		if self.__relativeFidelity is not None:
			self.relativeFidelity.export(outfile, level, name_='relativeFidelity')
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		if self.__mergedCurve is not None:
			self.mergedCurve.export(outfile, level, name_='mergedCurve')
		else:
			warnEmptyAttribute("mergedCurve", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurves':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurves.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absoluteFidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAbsoluteFidelity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'relativeFidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRelativeFidelity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mergedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMergedCurve(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsSmartMergev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsSmartMergev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSmartMergev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSmartMergev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSmartMergev1_0

class XSDataResultBioSaxsAsciiExportv1_0(XSDataResult):
	def __init__(self, status=None, processLog=None, integratedCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsAsciiExportv1_0", "Constructor of XSDataResultBioSaxsAsciiExportv1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
		checkType("XSDataResultBioSaxsAsciiExportv1_0", "Constructor of XSDataResultBioSaxsAsciiExportv1_0", processLog, "XSDataString")
		self.__processLog = processLog
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataResultBioSaxsAsciiExportv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def getProcessLog(self): return self.__processLog
	def setProcessLog(self, processLog):
		checkType("XSDataResultBioSaxsAsciiExportv1_0", "setProcessLog", processLog, "XSDataString")
		self.__processLog = processLog
	def delProcessLog(self): self.__processLog = None
	# Properties
	processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
	def export(self, outfile, level, name_='XSDataResultBioSaxsAsciiExportv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAsciiExportv1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
		else:
			warnEmptyAttribute("integratedCurve", "XSDataFile")
		if self.__processLog is not None:
			self.processLog.export(outfile, level, name_='processLog')
		else:
			warnEmptyAttribute("processLog", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processLog':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProcessLog(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAsciiExportv1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsAsciiExportv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAsciiExportv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAsciiExportv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAsciiExportv1_0

class XSDataResultBioSaxsAveragev1_0(XSDataResult):
	def __init__(self, status=None, logFile=None, processLog=None, averagedCurve=None, averagedImage=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", averagedImage, "XSDataImage")
		self.__averagedImage = averagedImage
		checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", averagedCurve, "XSDataFile")
		self.__averagedCurve = averagedCurve
		checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", processLog, "XSDataString")
		self.__processLog = processLog
		checkType("XSDataResultBioSaxsAveragev1_0", "Constructor of XSDataResultBioSaxsAveragev1_0", logFile, "XSDataFile")
		self.__logFile = logFile
	def getAveragedImage(self): return self.__averagedImage
	def setAveragedImage(self, averagedImage):
		checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedImage", averagedImage, "XSDataImage")
		self.__averagedImage = averagedImage
	def delAveragedImage(self): self.__averagedImage = None
	# Properties
	averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
	def getAveragedCurve(self): return self.__averagedCurve
	def setAveragedCurve(self, averagedCurve):
		checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedCurve", averagedCurve, "XSDataFile")
		self.__averagedCurve = averagedCurve
	def delAveragedCurve(self): self.__averagedCurve = None
	# Properties
	averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
	def getProcessLog(self): return self.__processLog
	def setProcessLog(self, processLog):
		checkType("XSDataResultBioSaxsAveragev1_0", "setProcessLog", processLog, "XSDataString")
		self.__processLog = processLog
	def delProcessLog(self): self.__processLog = None
	# Properties
	processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataResultBioSaxsAveragev1_0", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def export(self, outfile, level, name_='XSDataResultBioSaxsAveragev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAveragev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__averagedImage is not None:
			self.averagedImage.export(outfile, level, name_='averagedImage')
		else:
			warnEmptyAttribute("averagedImage", "XSDataImage")
		if self.__averagedCurve is not None:
			self.averagedCurve.export(outfile, level, name_='averagedCurve')
		else:
			warnEmptyAttribute("averagedCurve", "XSDataFile")
		if self.__processLog is not None:
			self.processLog.export(outfile, level, name_='processLog')
		else:
			warnEmptyAttribute("processLog", "XSDataString")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averagedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setAveragedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averagedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setAveragedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processLog':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProcessLog(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAveragev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsAveragev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAveragev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAveragev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAveragev1_0

class XSDataResultBioSaxsAzimutIntv1_0(XSDataResult):
	def __init__(self, status=None, integratedCurve=None, integratedImage=None, correctedImage=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", correctedImage, "XSDataImage")
		self.__correctedImage = correctedImage
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "Constructor of XSDataResultBioSaxsAzimutIntv1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def getCorrectedImage(self): return self.__correctedImage
	def setCorrectedImage(self, correctedImage):
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "setCorrectedImage", correctedImage, "XSDataImage")
		self.__correctedImage = correctedImage
	def delCorrectedImage(self): self.__correctedImage = None
	# Properties
	correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def export(self, outfile, level, name_='XSDataResultBioSaxsAzimutIntv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsAzimutIntv1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__correctedImage is not None:
			self.correctedImage.export(outfile, level, name_='correctedImage')
		else:
			warnEmptyAttribute("correctedImage", "XSDataImage")
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		else:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
		else:
			warnEmptyAttribute("integratedCurve", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correctedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setCorrectedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setIntegratedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAzimutIntv1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsAzimutIntv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAzimutIntv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsAzimutIntv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsAzimutIntv1_0

class XSDataResultBioSaxsNormalizev1_0(XSDataResult):
	def __init__(self, status=None, processLog=None, logFile=None, normalizedImage=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
		checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataResultBioSaxsNormalizev1_0", "Constructor of XSDataResultBioSaxsNormalizev1_0", processLog, "XSDataString")
		self.__processLog = processLog
	def getNormalizedImage(self): return self.__normalizedImage
	def setNormalizedImage(self, normalizedImage):
		checkType("XSDataResultBioSaxsNormalizev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
	def delNormalizedImage(self): self.__normalizedImage = None
	# Properties
	normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataResultBioSaxsNormalizev1_0", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getProcessLog(self): return self.__processLog
	def setProcessLog(self, processLog):
		checkType("XSDataResultBioSaxsNormalizev1_0", "setProcessLog", processLog, "XSDataString")
		self.__processLog = processLog
	def delProcessLog(self): self.__processLog = None
	# Properties
	processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
	def export(self, outfile, level, name_='XSDataResultBioSaxsNormalizev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsNormalizev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
		if self.__processLog is not None:
			self.processLog.export(outfile, level, name_='processLog')
		else:
			warnEmptyAttribute("processLog", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setNormalizedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processLog':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProcessLog(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsNormalizev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsNormalizev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsNormalizev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsNormalizev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsNormalizev1_0

class XSDataResultBioSaxsProcessOneFilev1_0(XSDataResult):
	def __init__(self, status=None, integratedCurve=None, integratedImage=None, normalizedImage=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "Constructor of XSDataResultBioSaxsProcessOneFilev1_0", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def getNormalizedImage(self): return self.__normalizedImage
	def setNormalizedImage(self, normalizedImage):
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setNormalizedImage", normalizedImage, "XSDataImage")
		self.__normalizedImage = normalizedImage
	def delNormalizedImage(self): self.__normalizedImage = None
	# Properties
	normalizedImage = property(getNormalizedImage, setNormalizedImage, delNormalizedImage, "Property for normalizedImage")
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedCurve(self): return self.__integratedCurve
	def setIntegratedCurve(self, integratedCurve):
		checkType("XSDataResultBioSaxsProcessOneFilev1_0", "setIntegratedCurve", integratedCurve, "XSDataFile")
		self.__integratedCurve = integratedCurve
	def delIntegratedCurve(self): self.__integratedCurve = None
	# Properties
	integratedCurve = property(getIntegratedCurve, setIntegratedCurve, delIntegratedCurve, "Property for integratedCurve")
	def export(self, outfile, level, name_='XSDataResultBioSaxsProcessOneFilev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsProcessOneFilev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		else:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedCurve is not None:
			self.integratedCurve.export(outfile, level, name_='integratedCurve')
		else:
			warnEmptyAttribute("integratedCurve", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setNormalizedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setIntegratedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedCurve(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsProcessOneFilev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsProcessOneFilev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsProcessOneFilev1_0

class XSDataResultBioSaxsReduceFileSeriev1_0(XSDataResult):
	def __init__(self, status=None, directoryMisc=None, directory2D=None, directory1D=None, mergedCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directory1D, "XSDataFile")
		self.__directory1D = directory1D
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directory2D, "XSDataFile")
		self.__directory2D = directory2D
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "Constructor of XSDataResultBioSaxsReduceFileSeriev1_0", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def getMergedCurve(self): return self.__mergedCurve
	def setMergedCurve(self, mergedCurve):
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
	def delMergedCurve(self): self.__mergedCurve = None
	# Properties
	mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def getDirectoryMisc(self): return self.__directoryMisc
	def setDirectoryMisc(self, directoryMisc):
		checkType("XSDataResultBioSaxsReduceFileSeriev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def delDirectoryMisc(self): self.__directoryMisc = None
	# Properties
	directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
	def export(self, outfile, level, name_='XSDataResultBioSaxsReduceFileSeriev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsReduceFileSeriev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__mergedCurve is not None:
			self.mergedCurve.export(outfile, level, name_='mergedCurve')
		else:
			warnEmptyAttribute("mergedCurve", "XSDataFile")
		if self.__directory1D is not None:
			self.directory1D.export(outfile, level, name_='directory1D')
		else:
			warnEmptyAttribute("directory1D", "XSDataFile")
		if self.__directory2D is not None:
			self.directory2D.export(outfile, level, name_='directory2D')
		else:
			warnEmptyAttribute("directory2D", "XSDataFile")
		if self.__directoryMisc is not None:
			self.directoryMisc.export(outfile, level, name_='directoryMisc')
		else:
			warnEmptyAttribute("directoryMisc", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mergedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMergedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory1D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory1D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory2D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directoryMisc':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectoryMisc(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsReduceFileSeriev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsReduceFileSeriev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsReduceFileSeriev1_0

class XSDataResultBioSaxsSample(XSDataResult):
	"""temporary class for multiple inhertitance emulation"""
	def __init__(self, status=None, code=None, comments=None, concentration=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", concentration, "XSDataDouble")
		self.__concentration = concentration
		checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataResultBioSaxsSample", "Constructor of XSDataResultBioSaxsSample", code, "XSDataString")
		self.__code = code
	def getConcentration(self): return self.__concentration
	def setConcentration(self, concentration):
		checkType("XSDataResultBioSaxsSample", "setConcentration", concentration, "XSDataDouble")
		self.__concentration = concentration
	def delConcentration(self): self.__concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataResultBioSaxsSample", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDataResultBioSaxsSample", "setCode", code, "XSDataString")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def export(self, outfile, level, name_='XSDataResultBioSaxsSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSample'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
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
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCode(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsSample' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsSample is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSample

class XSDataResultBioSaxsSingleSamplev1_0(XSDataResult):
	"""Class for precessing a single sample (at 1 single concentration)"""
	def __init__(self, status=None, directory2D=None, directory1D=None, outputCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", directory1D, "XSDataFile")
		self.__directory1D = directory1D
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "Constructor of XSDataResultBioSaxsSingleSamplev1_0", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def getOutputCurve(self): return self.__outputCurve
	def setOutputCurve(self, outputCurve):
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "setOutputCurve", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def delOutputCurve(self): self.__outputCurve = None
	# Properties
	outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataResultBioSaxsSingleSamplev1_0", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def export(self, outfile, level, name_='XSDataResultBioSaxsSingleSamplev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSingleSamplev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputCurve is not None:
			self.outputCurve.export(outfile, level, name_='outputCurve')
		else:
			warnEmptyAttribute("outputCurve", "XSDataFile")
		if self.__directory1D is not None:
			self.directory1D.export(outfile, level, name_='directory1D')
		else:
			warnEmptyAttribute("directory1D", "XSDataFile")
		if self.__directory2D is not None:
			self.directory2D.export(outfile, level, name_='directory2D')
		else:
			warnEmptyAttribute("directory2D", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory1D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory1D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory2D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory2D(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsSingleSamplev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsSingleSamplev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSingleSamplev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSingleSamplev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSingleSamplev1_0

class XSDataResultBioSaxsSmartMergev1_0(XSDataResult):
	def __init__(self, status=None, autoRg=None, mergedCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
		checkType("XSDataResultBioSaxsSmartMergev1_0", "Constructor of XSDataResultBioSaxsSmartMergev1_0", autoRg, "XSDataAutoRg")
		self.__autoRg = autoRg
	def getMergedCurve(self): return self.__mergedCurve
	def setMergedCurve(self, mergedCurve):
		checkType("XSDataResultBioSaxsSmartMergev1_0", "setMergedCurve", mergedCurve, "XSDataFile")
		self.__mergedCurve = mergedCurve
	def delMergedCurve(self): self.__mergedCurve = None
	# Properties
	mergedCurve = property(getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve")
	def getAutoRg(self): return self.__autoRg
	def setAutoRg(self, autoRg):
		checkType("XSDataResultBioSaxsSmartMergev1_0", "setAutoRg", autoRg, "XSDataAutoRg")
		self.__autoRg = autoRg
	def delAutoRg(self): self.__autoRg = None
	# Properties
	autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
	def export(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__mergedCurve is not None:
			self.mergedCurve.export(outfile, level, name_='mergedCurve')
		else:
			warnEmptyAttribute("mergedCurve", "XSDataFile")
		if self.__autoRg is not None:
			self.autoRg.export(outfile, level, name_='autoRg')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mergedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMergedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'autoRg':
			obj_ = XSDataAutoRg()
			obj_.build(child_)
			self.setAutoRg(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsSmartMergev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsSmartMergev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSmartMergev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSmartMergev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSmartMergev1_0

class XSDataInputBioSaxsSampleExperiment(XSDataInputBioSaxsSample):
	"""temporary class for multiple inhertitance emulation"""
	def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
		XSDataInputBioSaxsSample.__init__(self, configuration, code, comments, concentration)
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", detector, "XSDataString")
		self.__detector = detector
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", maskFile, "XSDataImage")
		self.__maskFile = maskFile
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
		checkType("XSDataInputBioSaxsSampleExperiment", "Constructor of XSDataInputBioSaxsSampleExperiment", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsSampleExperiment", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsSampleExperiment", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsSampleExperiment", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsSampleExperiment", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsSampleExperiment", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsSampleExperiment", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsSampleExperiment", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsSampleExperiment", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsSampleExperiment", "setMachineCurrent", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsSampleExperiment", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsSampleExperiment", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getStorageTemperature(self): return self.__storageTemperature
	def setStorageTemperature(self, storageTemperature):
		checkType("XSDataInputBioSaxsSampleExperiment", "setStorageTemperature", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
	def delStorageTemperature(self): self.__storageTemperature = None
	# Properties
	storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
	def getExposureTemperature(self): return self.__exposureTemperature
	def setExposureTemperature(self, exposureTemperature):
		checkType("XSDataInputBioSaxsSampleExperiment", "setExposureTemperature", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
	def delExposureTemperature(self): self.__exposureTemperature = None
	# Properties
	exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataInputBioSaxsSampleExperiment", "setExposureTime", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getFrameNumber(self): return self.__frameNumber
	def setFrameNumber(self, frameNumber):
		checkType("XSDataInputBioSaxsSampleExperiment", "setFrameNumber", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
	def delFrameNumber(self): self.__frameNumber = None
	# Properties
	frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
	def getFrameMax(self): return self.__frameMax
	def setFrameMax(self, frameMax):
		checkType("XSDataInputBioSaxsSampleExperiment", "setFrameMax", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def delFrameMax(self): self.__frameMax = None
	# Properties
	frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
	def export(self, outfile, level, name_='XSDataInputBioSaxsSampleExperiment'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSampleExperiment'):
		XSDataInputBioSaxsSample.exportChildren(self, outfile, level, name_)
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		if self.__detectorDistance is not None:
			self.detectorDistance.export(outfile, level, name_='detectorDistance')
		if self.__pixelSize_1 is not None:
			self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
		if self.__pixelSize_2 is not None:
			self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
		if self.__beamCenter_1 is not None:
			self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
		if self.__beamCenter_2 is not None:
			self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
		if self.__beamStopDiode is not None:
			self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__machineCurrent is not None:
			self.machineCurrent.export(outfile, level, name_='machineCurrent')
		if self.__maskFile is not None:
			self.maskFile.export(outfile, level, name_='maskFile')
		if self.__normalizationFactor is not None:
			self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
		if self.__storageTemperature is not None:
			self.storageTemperature.export(outfile, level, name_='storageTemperature')
		if self.__exposureTemperature is not None:
			self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self.__frameNumber is not None:
			self.frameNumber.export(outfile, level, name_='frameNumber')
		if self.__frameMax is not None:
			self.frameMax.export(outfile, level, name_='frameMax')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'storageTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setStorageTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setExposureTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameMax':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameMax(obj_)
		XSDataInputBioSaxsSample.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsSampleExperiment' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsSampleExperiment.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSampleExperiment()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSampleExperiment()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSampleExperiment

class XSDataResultBioSaxsSampleExperiment(XSDataResultBioSaxsSample):
	"""temporary class for multiple inhertitance emulation"""
	def __init__(self, status=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
		XSDataResultBioSaxsSample.__init__(self, status, code, comments, concentration)
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", detector, "XSDataString")
		self.__detector = detector
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", maskFile, "XSDataImage")
		self.__maskFile = maskFile
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
		checkType("XSDataResultBioSaxsSampleExperiment", "Constructor of XSDataResultBioSaxsSampleExperiment", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataResultBioSaxsSampleExperiment", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataResultBioSaxsSampleExperiment", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataResultBioSaxsSampleExperiment", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataResultBioSaxsSampleExperiment", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataResultBioSaxsSampleExperiment", "setBeamCenter_1", beamCenter_1, "XSDataDouble")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataResultBioSaxsSampleExperiment", "setBeamCenter_2", beamCenter_2, "XSDataDouble")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataResultBioSaxsSampleExperiment", "setBeamStopDiode", beamStopDiode, "XSDataDouble")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataResultBioSaxsSampleExperiment", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataResultBioSaxsSampleExperiment", "setMachineCurrent", machineCurrent, "XSDataDouble")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataResultBioSaxsSampleExperiment", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataResultBioSaxsSampleExperiment", "setNormalizationFactor", normalizationFactor, "XSDataDouble")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getStorageTemperature(self): return self.__storageTemperature
	def setStorageTemperature(self, storageTemperature):
		checkType("XSDataResultBioSaxsSampleExperiment", "setStorageTemperature", storageTemperature, "XSDataDouble")
		self.__storageTemperature = storageTemperature
	def delStorageTemperature(self): self.__storageTemperature = None
	# Properties
	storageTemperature = property(getStorageTemperature, setStorageTemperature, delStorageTemperature, "Property for storageTemperature")
	def getExposureTemperature(self): return self.__exposureTemperature
	def setExposureTemperature(self, exposureTemperature):
		checkType("XSDataResultBioSaxsSampleExperiment", "setExposureTemperature", exposureTemperature, "XSDataDouble")
		self.__exposureTemperature = exposureTemperature
	def delExposureTemperature(self): self.__exposureTemperature = None
	# Properties
	exposureTemperature = property(getExposureTemperature, setExposureTemperature, delExposureTemperature, "Property for exposureTemperature")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataResultBioSaxsSampleExperiment", "setExposureTime", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getFrameNumber(self): return self.__frameNumber
	def setFrameNumber(self, frameNumber):
		checkType("XSDataResultBioSaxsSampleExperiment", "setFrameNumber", frameNumber, "XSDataInteger")
		self.__frameNumber = frameNumber
	def delFrameNumber(self): self.__frameNumber = None
	# Properties
	frameNumber = property(getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber")
	def getFrameMax(self): return self.__frameMax
	def setFrameMax(self, frameMax):
		checkType("XSDataResultBioSaxsSampleExperiment", "setFrameMax", frameMax, "XSDataInteger")
		self.__frameMax = frameMax
	def delFrameMax(self): self.__frameMax = None
	# Properties
	frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
	def export(self, outfile, level, name_='XSDataResultBioSaxsSampleExperiment'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSampleExperiment'):
		XSDataResultBioSaxsSample.exportChildren(self, outfile, level, name_)
		if self.__detector is not None:
			self.detector.export(outfile, level, name_='detector')
		if self.__detectorDistance is not None:
			self.detectorDistance.export(outfile, level, name_='detectorDistance')
		if self.__pixelSize_1 is not None:
			self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
		if self.__pixelSize_2 is not None:
			self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
		if self.__beamCenter_1 is not None:
			self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
		if self.__beamCenter_2 is not None:
			self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
		if self.__beamStopDiode is not None:
			self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__machineCurrent is not None:
			self.machineCurrent.export(outfile, level, name_='machineCurrent')
		if self.__maskFile is not None:
			self.maskFile.export(outfile, level, name_='maskFile')
		if self.__normalizationFactor is not None:
			self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
		if self.__storageTemperature is not None:
			self.storageTemperature.export(outfile, level, name_='storageTemperature')
		if self.__exposureTemperature is not None:
			self.exposureTemperature.export(outfile, level, name_='exposureTemperature')
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		if self.__frameNumber is not None:
			self.frameNumber.export(outfile, level, name_='frameNumber')
		if self.__frameMax is not None:
			self.frameMax.export(outfile, level, name_='frameMax')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_1':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelSize_2':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setPixelSize_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'storageTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setStorageTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTemperature':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setExposureTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameMax':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameMax(obj_)
		XSDataResultBioSaxsSample.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsSampleExperiment' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsSampleExperiment is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsSampleExperiment.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSampleExperiment()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsSampleExperiment()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsSampleExperiment

class XSDataInputBioSaxsAveragev1_0(XSDataInputBioSaxsSampleExperiment):
	def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, logFile=None, averagedCurve=None, averagedImage=None, integratedImageSize=None, integratedImage=None):
		XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
		if integratedImage is None:
			self.__integratedImage = []
		else:
			checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", integratedImage, "list")
			self.__integratedImage = integratedImage
		checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", integratedImageSize, "XSDataInteger")
		self.__integratedImageSize = integratedImageSize
		checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", averagedImage, "XSDataImage")
		self.__averagedImage = averagedImage
		checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", averagedCurve, "XSDataFile")
		self.__averagedCurve = averagedCurve
		checkType("XSDataInputBioSaxsAveragev1_0", "Constructor of XSDataInputBioSaxsAveragev1_0", logFile, "XSDataFile")
		self.__logFile = logFile
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", integratedImage, "list")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def addIntegratedImage(self, value):
		checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", value, "XSDataImage")
		self.__integratedImage.append(value)
	def insertIntegratedImage(self, index, value):
		checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImage", value, "XSDataImage")
		self.__integratedImage[index] = value
	def getIntegratedImageSize(self): return self.__integratedImageSize
	def setIntegratedImageSize(self, integratedImageSize):
		checkType("XSDataInputBioSaxsAveragev1_0", "setIntegratedImageSize", integratedImageSize, "XSDataInteger")
		self.__integratedImageSize = integratedImageSize
	def delIntegratedImageSize(self): self.__integratedImageSize = None
	# Properties
	integratedImageSize = property(getIntegratedImageSize, setIntegratedImageSize, delIntegratedImageSize, "Property for integratedImageSize")
	def getAveragedImage(self): return self.__averagedImage
	def setAveragedImage(self, averagedImage):
		checkType("XSDataInputBioSaxsAveragev1_0", "setAveragedImage", averagedImage, "XSDataImage")
		self.__averagedImage = averagedImage
	def delAveragedImage(self): self.__averagedImage = None
	# Properties
	averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
	def getAveragedCurve(self): return self.__averagedCurve
	def setAveragedCurve(self, averagedCurve):
		checkType("XSDataInputBioSaxsAveragev1_0", "setAveragedCurve", averagedCurve, "XSDataFile")
		self.__averagedCurve = averagedCurve
	def delAveragedCurve(self): self.__averagedCurve = None
	# Properties
	averagedCurve = property(getAveragedCurve, setAveragedCurve, delAveragedCurve, "Property for averagedCurve")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataInputBioSaxsAveragev1_0", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def export(self, outfile, level, name_='XSDataInputBioSaxsAveragev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAveragev1_0'):
		XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
		for integratedImage_ in self.getIntegratedImage():
			integratedImage_.export(outfile, level, name_='integratedImage')
		if self.getIntegratedImage() == []:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedImageSize is not None:
			self.integratedImageSize.export(outfile, level, name_='integratedImageSize')
		else:
			warnEmptyAttribute("integratedImageSize", "XSDataInteger")
		if self.__averagedImage is not None:
			self.averagedImage.export(outfile, level, name_='averagedImage')
		else:
			warnEmptyAttribute("averagedImage", "XSDataImage")
		if self.__averagedCurve is not None:
			self.averagedCurve.export(outfile, level, name_='averagedCurve')
		else:
			warnEmptyAttribute("averagedCurve", "XSDataFile")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.integratedImage.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedImageSize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIntegratedImageSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averagedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setAveragedImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averagedCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setAveragedCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAveragev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsAveragev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAveragev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsAveragev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsAveragev1_0

class XSDataInputBioSaxsMetadatav1_0(XSDataInputBioSaxsSampleExperiment):
	def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, inputImage=None):
		XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
		checkType("XSDataInputBioSaxsMetadatav1_0", "Constructor of XSDataInputBioSaxsMetadatav1_0", inputImage, "XSDataImage")
		self.__inputImage = inputImage
		checkType("XSDataInputBioSaxsMetadatav1_0", "Constructor of XSDataInputBioSaxsMetadatav1_0", outputImage, "XSDataImage")
		self.__outputImage = outputImage
	def getInputImage(self): return self.__inputImage
	def setInputImage(self, inputImage):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setInputImage", inputImage, "XSDataImage")
		self.__inputImage = inputImage
	def delInputImage(self): self.__inputImage = None
	# Properties
	inputImage = property(getInputImage, setInputImage, delInputImage, "Property for inputImage")
	def getOutputImage(self): return self.__outputImage
	def setOutputImage(self, outputImage):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setOutputImage", outputImage, "XSDataImage")
		self.__outputImage = outputImage
	def delOutputImage(self): self.__outputImage = None
	# Properties
	outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
	def export(self, outfile, level, name_='XSDataInputBioSaxsMetadatav1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsMetadatav1_0'):
		XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
		if self.__inputImage is not None:
			self.inputImage.export(outfile, level, name_='inputImage')
		else:
			warnEmptyAttribute("inputImage", "XSDataImage")
		if self.__outputImage is not None:
			self.outputImage.export(outfile, level, name_='outputImage')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setInputImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setOutputImage(obj_)
		XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsMetadatav1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsMetadatav1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsMetadatav1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsMetadatav1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsMetadatav1_0

class XSDataInputBioSaxsSingleSamplev1_0(XSDataInputBioSaxsSampleExperiment):
	"""Class for precessing a single sample (at 1 single concentration)"""
	def __init__(self, configuration=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, forceReprocess=None, sampleSeries=None, bufferSeries=None, directoryMisc=None, directory2D=None, directory1D=None):
		XSDataInputBioSaxsSampleExperiment.__init__(self, configuration, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directory1D, "XSDataFile")
		self.__directory1D = directory1D
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directory2D, "XSDataFile")
		self.__directory2D = directory2D
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
		if bufferSeries is None:
			self.__bufferSeries = []
		else:
			checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", bufferSeries, "list")
			self.__bufferSeries = bufferSeries
		if sampleSeries is None:
			self.__sampleSeries = []
		else:
			checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", sampleSeries, "list")
			self.__sampleSeries = sampleSeries
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "Constructor of XSDataInputBioSaxsSingleSamplev1_0", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def getDirectoryMisc(self): return self.__directoryMisc
	def setDirectoryMisc(self, directoryMisc):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def delDirectoryMisc(self): self.__directoryMisc = None
	# Properties
	directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
	def getBufferSeries(self): return self.__bufferSeries
	def setBufferSeries(self, bufferSeries):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", bufferSeries, "list")
		self.__bufferSeries = bufferSeries
	def delBufferSeries(self): self.__bufferSeries = None
	# Properties
	bufferSeries = property(getBufferSeries, setBufferSeries, delBufferSeries, "Property for bufferSeries")
	def addBufferSeries(self, value):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", value, "XSDataFileSeries")
		self.__bufferSeries.append(value)
	def insertBufferSeries(self, index, value):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setBufferSeries", value, "XSDataFileSeries")
		self.__bufferSeries[index] = value
	def getSampleSeries(self): return self.__sampleSeries
	def setSampleSeries(self, sampleSeries):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", sampleSeries, "list")
		self.__sampleSeries = sampleSeries
	def delSampleSeries(self): self.__sampleSeries = None
	# Properties
	sampleSeries = property(getSampleSeries, setSampleSeries, delSampleSeries, "Property for sampleSeries")
	def addSampleSeries(self, value):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", value, "XSDataFileSeries")
		self.__sampleSeries.append(value)
	def insertSampleSeries(self, index, value):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setSampleSeries", value, "XSDataFileSeries")
		self.__sampleSeries[index] = value
	def getForceReprocess(self): return self.__forceReprocess
	def setForceReprocess(self, forceReprocess):
		checkType("XSDataInputBioSaxsSingleSamplev1_0", "setForceReprocess", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
	def delForceReprocess(self): self.__forceReprocess = None
	# Properties
	forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
	def export(self, outfile, level, name_='XSDataInputBioSaxsSingleSamplev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSingleSamplev1_0'):
		XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
		if self.__directory1D is not None:
			self.directory1D.export(outfile, level, name_='directory1D')
		else:
			warnEmptyAttribute("directory1D", "XSDataFile")
		if self.__directory2D is not None:
			self.directory2D.export(outfile, level, name_='directory2D')
		else:
			warnEmptyAttribute("directory2D", "XSDataFile")
		if self.__directoryMisc is not None:
			self.directoryMisc.export(outfile, level, name_='directoryMisc')
		else:
			warnEmptyAttribute("directoryMisc", "XSDataFile")
		for bufferSeries_ in self.getBufferSeries():
			bufferSeries_.export(outfile, level, name_='bufferSeries')
		if self.getBufferSeries() == []:
			warnEmptyAttribute("bufferSeries", "XSDataFileSeries")
		for sampleSeries_ in self.getSampleSeries():
			sampleSeries_.export(outfile, level, name_='sampleSeries')
		if self.getSampleSeries() == []:
			warnEmptyAttribute("sampleSeries", "XSDataFileSeries")
		if self.__forceReprocess is not None:
			self.forceReprocess.export(outfile, level, name_='forceReprocess')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory1D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory1D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory2D':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory2D(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directoryMisc':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectoryMisc(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bufferSeries':
			obj_ = XSDataFileSeries()
			obj_.build(child_)
			self.bufferSeries.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleSeries':
			obj_ = XSDataFileSeries()
			obj_.build(child_)
			self.sampleSeries.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'forceReprocess':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setForceReprocess(obj_)
		XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsSingleSamplev1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsSingleSamplev1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSingleSamplev1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsSingleSamplev1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsSingleSamplev1_0

class XSDataResultBioSaxsMetadatav1_0(XSDataResultBioSaxsSampleExperiment):
	def __init__(self, status=None, code=None, comments=None, concentration=None, frameMax=None, frameNumber=None, exposureTime=None, exposureTemperature=None, storageTemperature=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, outputImage=None, experimentSetup=None, sample=None):
		XSDataResultBioSaxsSampleExperiment.__init__(self, status, code, comments, concentration, frameMax, frameNumber, exposureTime, exposureTemperature, storageTemperature, normalizationFactor, maskFile, machineCurrent, wavelength, beamStopDiode, beamCenter_2, beamCenter_1, pixelSize_2, pixelSize_1, detectorDistance, detector)
		checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
		checkType("XSDataResultBioSaxsMetadatav1_0", "Constructor of XSDataResultBioSaxsMetadatav1_0", outputImage, "XSDataImage")
		self.__outputImage = outputImage
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def getOutputImage(self): return self.__outputImage
	def setOutputImage(self, outputImage):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setOutputImage", outputImage, "XSDataImage")
		self.__outputImage = outputImage
	def delOutputImage(self): self.__outputImage = None
	# Properties
	outputImage = property(getOutputImage, setOutputImage, delOutputImage, "Property for outputImage")
	def export(self, outfile, level, name_='XSDataResultBioSaxsMetadatav1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsMetadatav1_0'):
		XSDataResultBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		if self.__experimentSetup is not None:
			self.experimentSetup.export(outfile, level, name_='experimentSetup')
		if self.__outputImage is not None:
			self.outputImage.export(outfile, level, name_='outputImage')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataBioSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentSetup':
			obj_ = XSDataBioSaxsExperimentSetup()
			obj_.build(child_)
			self.setExperimentSetup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setOutputImage(obj_)
		XSDataResultBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsMetadatav1_0' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsMetadatav1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsMetadatav1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsMetadatav1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsMetadatav1_0



# End of data representation classes.



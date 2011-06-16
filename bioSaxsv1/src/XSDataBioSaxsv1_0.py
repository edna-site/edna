#!/usr/bin/env python

#
# Generated Thu Jun 16 06:16::08 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSConfiguration
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataStatus
from XSDataCommon import XSDataResult
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


class XSDataBioSaxsExperimentSetup(object):
	def __init__(self, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
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
		checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataBioSaxsExperimentSetup", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataBioSaxsExperimentSetup", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
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
		checkType("XSDataBioSaxsExperimentSetup", "setMachineCurrent", machineCurrent, "XSDataFloat")
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
		checkType("XSDataBioSaxsExperimentSetup", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def export(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
		pass
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBioSaxsExperimentSetup' )
		outfile.close()
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

class XSDataBioSaxsSample(object):
	def __init__(self, sampleCode=None, sampleComments=None, sampleConcentration=None):
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataBioSaxsSample", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataBioSaxsSample", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataBioSaxsSample", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
	def export(self, outfile, level, name_='XSDataBioSaxsSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBioSaxsSample'):
		pass
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBioSaxsSample' )
		outfile.close()
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

class XSDataInputBioSaxsAveragev1_0(object):
	def __init__(self, logFile=None, averagedSpectrum=None, averagedImage=None, integratedImageSize=None, integratedImage=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, configuration=None):
		self.__configuration = configuration
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		if integratedImage is None:
			self.__integratedImage = []
		else:
			self.__integratedImage = integratedImage
		self.__integratedImageSize = integratedImageSize
		self.__averagedImage = averagedImage
		self.__averagedSpectrum = averagedSpectrum
		self.__logFile = logFile
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsAveragev1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsAveragev1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsAveragev1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsAveragev1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsAveragev1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsAveragev1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsAveragev1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsAveragev1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsAveragev1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsAveragev1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsAveragev1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsAveragev1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsAveragev1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsAveragev1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsAveragev1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
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
	def getAveragedSpectrum(self): return self.__averagedSpectrum
	def setAveragedSpectrum(self, averagedSpectrum):
		checkType("XSDataInputBioSaxsAveragev1_0", "setAveragedSpectrum", averagedSpectrum, "XSDataFile")
		self.__averagedSpectrum = averagedSpectrum
	def delAveragedSpectrum(self): self.__averagedSpectrum = None
	# Properties
	averagedSpectrum = property(getAveragedSpectrum, setAveragedSpectrum, delAveragedSpectrum, "Property for averagedSpectrum")
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
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
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
		if self.__averagedSpectrum is not None:
			self.averagedSpectrum.export(outfile, level, name_='averagedSpectrum')
		else:
			warnEmptyAttribute("averagedSpectrum", "XSDataFile")
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
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			nodeName_ == 'averagedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setAveragedSpectrum(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAveragev1_0' )
		outfile.close()
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

class XSDataInputBioSaxsAzimutIntv1_0(object):
	def __init__(self, correctedImage=None, integratedSpectrum=None, integratedImage=None, normalizedImageSize=None, normalizedImage=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, configuration=None):
		self.__configuration = configuration
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__normalizedImage = normalizedImage
		self.__normalizedImageSize = normalizedImageSize
		self.__integratedImage = integratedImage
		self.__integratedSpectrum = integratedSpectrum
		self.__correctedImage = correctedImage
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
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
	def getIntegratedSpectrum(self): return self.__integratedSpectrum
	def setIntegratedSpectrum(self, integratedSpectrum):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setIntegratedSpectrum", integratedSpectrum, "XSDataFile")
		self.__integratedSpectrum = integratedSpectrum
	def delIntegratedSpectrum(self): self.__integratedSpectrum = None
	# Properties
	integratedSpectrum = property(getIntegratedSpectrum, setIntegratedSpectrum, delIntegratedSpectrum, "Property for integratedSpectrum")
	def getCorrectedImage(self): return self.__correctedImage
	def setCorrectedImage(self, correctedImage):
		checkType("XSDataInputBioSaxsAzimutIntv1_0", "setCorrectedImage", correctedImage, "XSDataImage")
		self.__correctedImage = correctedImage
	def delCorrectedImage(self): self.__correctedImage = None
	# Properties
	correctedImage = property(getCorrectedImage, setCorrectedImage, delCorrectedImage, "Property for correctedImage")
	def export(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsAzimutIntv1_0'):
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__normalizedImageSize is not None:
			self.normalizedImageSize.export(outfile, level, name_='normalizedImageSize')
		else:
			warnEmptyAttribute("normalizedImageSize", "XSDataInteger")
		if self.__integratedImage is not None:
			self.integratedImage.export(outfile, level, name_='integratedImage')
		else:
			warnEmptyAttribute("integratedImage", "XSDataImage")
		if self.__integratedSpectrum is not None:
			self.integratedSpectrum.export(outfile, level, name_='integratedSpectrum')
		else:
			warnEmptyAttribute("integratedSpectrum", "XSDataFile")
		if self.__correctedImage is not None:
			self.correctedImage.export(outfile, level, name_='correctedImage')
		else:
			warnEmptyAttribute("correctedImage", "XSDataImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			nodeName_ == 'integratedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedSpectrum(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correctedImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setCorrectedImage(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAzimutIntv1_0' )
		outfile.close()
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

class XSDataInputBioSaxsMetadatav1_0(object):
	def __init__(self, outputImage=None, inputImage=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, configuration=None):
		self.__configuration = configuration
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__inputImage = inputImage
		self.__outputImage = outputImage
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsMetadatav1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
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
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
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
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setInputImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setOutputImage(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsMetadatav1_0' )
		outfile.close()
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

class XSDataInputBioSaxsNormalizev1_0(object):
	def __init__(self, rawImageSize=None, normalizedImage=None, logFile=None, rawImage=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, configuration=None):
		self.__configuration = configuration
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__rawImage = rawImage
		self.__logFile = logFile
		self.__normalizedImage = normalizedImage
		self.__rawImageSize = rawImageSize
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsNormalizev1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
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
	def export(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsNormalizev1_0'):
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
		if self.__rawImage is not None:
			self.rawImage.export(outfile, level, name_='rawImage')
		else:
			warnEmptyAttribute("rawImage", "XSDataImage")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
		if self.__normalizedImage is not None:
			self.normalizedImage.export(outfile, level, name_='normalizedImage')
		else:
			warnEmptyAttribute("normalizedImage", "XSDataImage")
		if self.__rawImageSize is not None:
			self.rawImageSize.export(outfile, level, name_='rawImageSize')
		else:
			warnEmptyAttribute("rawImageSize", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsNormalizev1_0' )
		outfile.close()
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

class XSDataInputBioSaxsProcessOneRunv1_0(object):
	def __init__(self, directoryMisc=None, directory2D=None, directory1D=None, directoryRaw=None, prefix=None, isOnline=None, frames=None, runNumber=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, specVariableAbort=None, specVariableStatus=None, specVersion=None, configuration=None):
		self.__configuration = configuration
		self.__specVersion = specVersion
		self.__specVariableStatus = specVariableStatus
		self.__specVariableAbort = specVariableAbort
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__runNumber = runNumber
		if frames is None:
			self.__frames = []
		else:
			self.__frames = frames
		self.__isOnline = isOnline
		self.__prefix = prefix
		self.__directoryRaw = directoryRaw
		self.__directory1D = directory1D
		self.__directory2D = directory2D
		self.__directoryMisc = directoryMisc
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getSpecVersion(self): return self.__specVersion
	def setSpecVersion(self, specVersion):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSpecVersion", specVersion, "XSDataString")
		self.__specVersion = specVersion
	def delSpecVersion(self): self.__specVersion = None
	# Properties
	specVersion = property(getSpecVersion, setSpecVersion, delSpecVersion, "Property for specVersion")
	def getSpecVariableStatus(self): return self.__specVariableStatus
	def setSpecVariableStatus(self, specVariableStatus):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSpecVariableStatus", specVariableStatus, "XSDataString")
		self.__specVariableStatus = specVariableStatus
	def delSpecVariableStatus(self): self.__specVariableStatus = None
	# Properties
	specVariableStatus = property(getSpecVariableStatus, setSpecVariableStatus, delSpecVariableStatus, "Property for specVariableStatus")
	def getSpecVariableAbort(self): return self.__specVariableAbort
	def setSpecVariableAbort(self, specVariableAbort):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSpecVariableAbort", specVariableAbort, "XSDataString")
		self.__specVariableAbort = specVariableAbort
	def delSpecVariableAbort(self): self.__specVariableAbort = None
	# Properties
	specVariableAbort = property(getSpecVariableAbort, setSpecVariableAbort, delSpecVariableAbort, "Property for specVariableAbort")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
	def getRunNumber(self): return self.__runNumber
	def setRunNumber(self, runNumber):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setRunNumber", runNumber, "XSDataInteger")
		self.__runNumber = runNumber
	def delRunNumber(self): self.__runNumber = None
	# Properties
	runNumber = property(getRunNumber, setRunNumber, delRunNumber, "Property for runNumber")
	def getFrames(self): return self.__frames
	def setFrames(self, frames):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setFrames", frames, "list")
		self.__frames = frames
	def delFrames(self): self.__frames = None
	# Properties
	frames = property(getFrames, setFrames, delFrames, "Property for frames")
	def addFrames(self, value):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setFrames", value, "XSDataInteger")
		self.__frames.append(value)
	def insertFrames(self, index, value):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setFrames", value, "XSDataInteger")
		self.__frames[index] = value
	def getIsOnline(self): return self.__isOnline
	def setIsOnline(self, isOnline):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setIsOnline", isOnline, "XSDataBoolean")
		self.__isOnline = isOnline
	def delIsOnline(self): self.__isOnline = None
	# Properties
	isOnline = property(getIsOnline, setIsOnline, delIsOnline, "Property for isOnline")
	def getPrefix(self): return self.__prefix
	def setPrefix(self, prefix):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setPrefix", prefix, "XSDataString")
		self.__prefix = prefix
	def delPrefix(self): self.__prefix = None
	# Properties
	prefix = property(getPrefix, setPrefix, delPrefix, "Property for prefix")
	def getDirectoryRaw(self): return self.__directoryRaw
	def setDirectoryRaw(self, directoryRaw):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDirectoryRaw", directoryRaw, "XSDataFile")
		self.__directoryRaw = directoryRaw
	def delDirectoryRaw(self): self.__directoryRaw = None
	# Properties
	directoryRaw = property(getDirectoryRaw, setDirectoryRaw, delDirectoryRaw, "Property for directoryRaw")
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def getDirectoryMisc(self): return self.__directoryMisc
	def setDirectoryMisc(self, directoryMisc):
		checkType("XSDataInputBioSaxsProcessOneRunv1_0", "setDirectoryMisc", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def delDirectoryMisc(self): self.__directoryMisc = None
	# Properties
	directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
	def export(self, outfile, level, name_='XSDataInputBioSaxsProcessOneRunv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsProcessOneRunv1_0'):
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
		if self.__specVersion is not None:
			self.specVersion.export(outfile, level, name_='specVersion')
		if self.__specVariableStatus is not None:
			self.specVariableStatus.export(outfile, level, name_='specVariableStatus')
		if self.__specVariableAbort is not None:
			self.specVariableAbort.export(outfile, level, name_='specVariableAbort')
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
		if self.__runNumber is not None:
			self.runNumber.export(outfile, level, name_='runNumber')
		else:
			warnEmptyAttribute("runNumber", "XSDataInteger")
		for frames_ in self.getFrames():
			frames_.export(outfile, level, name_='frames')
		if self.getFrames() == []:
			warnEmptyAttribute("frames", "XSDataInteger")
		if self.__isOnline is not None:
			self.isOnline.export(outfile, level, name_='isOnline')
		else:
			warnEmptyAttribute("isOnline", "XSDataBoolean")
		if self.__prefix is not None:
			self.prefix.export(outfile, level, name_='prefix')
		else:
			warnEmptyAttribute("prefix", "XSDataString")
		if self.__directoryRaw is not None:
			self.directoryRaw.export(outfile, level, name_='directoryRaw')
		else:
			warnEmptyAttribute("directoryRaw", "XSDataFile")
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
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVersion':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVersion(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableStatus':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableStatus(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableAbort':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableAbort(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'runNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRunNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frames':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.frames.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'isOnline':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setIsOnline(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'prefix':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPrefix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directoryRaw':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectoryRaw(obj_)
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
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneRunv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsProcessOneRunv1_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsProcessOneRunv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsProcessOneRunv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsProcessOneRunv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsProcessOneRunv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsProcessOneRunv1_0

class XSDataInputBioSaxsReprocessv1_0(object):
	def __init__(self, runNumber=None, prefix=None, operation=None, normalisation=None, keepOriginal=None, isOnline=None, frameLast=None, frameFirst=None, directory=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, specVariableAbort=None, specVariableStatus=None, specVersion=None, configuration=None):
		self.__configuration = configuration
		self.__specVersion = specVersion
		self.__specVariableStatus = specVariableStatus
		self.__specVariableAbort = specVariableAbort
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__directory = directory
		self.__frameFirst = frameFirst
		self.__frameLast = frameLast
		self.__isOnline = isOnline
		self.__keepOriginal = keepOriginal
		self.__normalisation = normalisation
		self.__operation = operation
		self.__prefix = prefix
		if runNumber is None:
			self.__runNumber = []
		else:
			self.__runNumber = runNumber
	def getConfiguration(self): return self.__configuration
	def setConfiguration(self, configuration):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setConfiguration", configuration, "XSConfiguration")
		self.__configuration = configuration
	def delConfiguration(self): self.__configuration = None
	# Properties
	configuration = property(getConfiguration, setConfiguration, delConfiguration, "Property for configuration")
	def getSpecVersion(self): return self.__specVersion
	def setSpecVersion(self, specVersion):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSpecVersion", specVersion, "XSDataString")
		self.__specVersion = specVersion
	def delSpecVersion(self): self.__specVersion = None
	# Properties
	specVersion = property(getSpecVersion, setSpecVersion, delSpecVersion, "Property for specVersion")
	def getSpecVariableStatus(self): return self.__specVariableStatus
	def setSpecVariableStatus(self, specVariableStatus):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSpecVariableStatus", specVariableStatus, "XSDataString")
		self.__specVariableStatus = specVariableStatus
	def delSpecVariableStatus(self): self.__specVariableStatus = None
	# Properties
	specVariableStatus = property(getSpecVariableStatus, setSpecVariableStatus, delSpecVariableStatus, "Property for specVariableStatus")
	def getSpecVariableAbort(self): return self.__specVariableAbort
	def setSpecVariableAbort(self, specVariableAbort):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSpecVariableAbort", specVariableAbort, "XSDataString")
		self.__specVariableAbort = specVariableAbort
	def delSpecVariableAbort(self): self.__specVariableAbort = None
	# Properties
	specVariableAbort = property(getSpecVariableAbort, setSpecVariableAbort, delSpecVariableAbort, "Property for specVariableAbort")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
	def getDirectory(self): return self.__directory
	def setDirectory(self, directory):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setDirectory", directory, "XSDataFile")
		self.__directory = directory
	def delDirectory(self): self.__directory = None
	# Properties
	directory = property(getDirectory, setDirectory, delDirectory, "Property for directory")
	def getFrameFirst(self): return self.__frameFirst
	def setFrameFirst(self, frameFirst):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setFrameFirst", frameFirst, "XSDataInteger")
		self.__frameFirst = frameFirst
	def delFrameFirst(self): self.__frameFirst = None
	# Properties
	frameFirst = property(getFrameFirst, setFrameFirst, delFrameFirst, "Property for frameFirst")
	def getFrameLast(self): return self.__frameLast
	def setFrameLast(self, frameLast):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setFrameLast", frameLast, "XSDataInteger")
		self.__frameLast = frameLast
	def delFrameLast(self): self.__frameLast = None
	# Properties
	frameLast = property(getFrameLast, setFrameLast, delFrameLast, "Property for frameLast")
	def getIsOnline(self): return self.__isOnline
	def setIsOnline(self, isOnline):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setIsOnline", isOnline, "XSDataBoolean")
		self.__isOnline = isOnline
	def delIsOnline(self): self.__isOnline = None
	# Properties
	isOnline = property(getIsOnline, setIsOnline, delIsOnline, "Property for isOnline")
	def getKeepOriginal(self): return self.__keepOriginal
	def setKeepOriginal(self, keepOriginal):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setKeepOriginal", keepOriginal, "XSDataBoolean")
		self.__keepOriginal = keepOriginal
	def delKeepOriginal(self): self.__keepOriginal = None
	# Properties
	keepOriginal = property(getKeepOriginal, setKeepOriginal, delKeepOriginal, "Property for keepOriginal")
	def getNormalisation(self): return self.__normalisation
	def setNormalisation(self, normalisation):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setNormalisation", normalisation, "XSDataString")
		self.__normalisation = normalisation
	def delNormalisation(self): self.__normalisation = None
	# Properties
	normalisation = property(getNormalisation, setNormalisation, delNormalisation, "Property for normalisation")
	def getOperation(self): return self.__operation
	def setOperation(self, operation):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setOperation", operation, "XSDataString")
		self.__operation = operation
	def delOperation(self): self.__operation = None
	# Properties
	operation = property(getOperation, setOperation, delOperation, "Property for operation")
	def getPrefix(self): return self.__prefix
	def setPrefix(self, prefix):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setPrefix", prefix, "XSDataString")
		self.__prefix = prefix
	def delPrefix(self): self.__prefix = None
	# Properties
	prefix = property(getPrefix, setPrefix, delPrefix, "Property for prefix")
	def getRunNumber(self): return self.__runNumber
	def setRunNumber(self, runNumber):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setRunNumber", runNumber, "list")
		self.__runNumber = runNumber
	def delRunNumber(self): self.__runNumber = None
	# Properties
	runNumber = property(getRunNumber, setRunNumber, delRunNumber, "Property for runNumber")
	def addRunNumber(self, value):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setRunNumber", value, "XSDataInteger")
		self.__runNumber.append(value)
	def insertRunNumber(self, index, value):
		checkType("XSDataInputBioSaxsReprocessv1_0", "setRunNumber", value, "XSDataInteger")
		self.__runNumber[index] = value
	def export(self, outfile, level, name_='XSDataInputBioSaxsReprocessv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsReprocessv1_0'):
		pass
		if self.__configuration is not None:
			self.configuration.export(outfile, level, name_='configuration')
		else:
			warnEmptyAttribute("configuration", "XSConfiguration")
		if self.__specVersion is not None:
			self.specVersion.export(outfile, level, name_='specVersion')
		if self.__specVariableStatus is not None:
			self.specVariableStatus.export(outfile, level, name_='specVariableStatus')
		if self.__specVariableAbort is not None:
			self.specVariableAbort.export(outfile, level, name_='specVariableAbort')
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
		if self.__directory is not None:
			self.directory.export(outfile, level, name_='directory')
		else:
			warnEmptyAttribute("directory", "XSDataFile")
		if self.__frameFirst is not None:
			self.frameFirst.export(outfile, level, name_='frameFirst')
		if self.__frameLast is not None:
			self.frameLast.export(outfile, level, name_='frameLast')
		if self.__isOnline is not None:
			self.isOnline.export(outfile, level, name_='isOnline')
		if self.__keepOriginal is not None:
			self.keepOriginal.export(outfile, level, name_='keepOriginal')
		if self.__normalisation is not None:
			self.normalisation.export(outfile, level, name_='normalisation')
		else:
			warnEmptyAttribute("normalisation", "XSDataString")
		if self.__operation is not None:
			self.operation.export(outfile, level, name_='operation')
		else:
			warnEmptyAttribute("operation", "XSDataString")
		if self.__prefix is not None:
			self.prefix.export(outfile, level, name_='prefix')
		else:
			warnEmptyAttribute("prefix", "XSDataString")
		for runNumber_ in self.getRunNumber():
			runNumber_.export(outfile, level, name_='runNumber')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'configuration':
			obj_ = XSConfiguration()
			obj_.build(child_)
			self.setConfiguration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVersion':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVersion(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableStatus':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableStatus(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableAbort':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableAbort(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDirectory(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameFirst':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameFirst(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameLast':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameLast(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'isOnline':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setIsOnline(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'keepOriginal':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setKeepOriginal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalisation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setNormalisation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'operation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOperation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'prefix':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPrefix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'runNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.runNumber.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBioSaxsReprocessv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsReprocessv1_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBioSaxsReprocessv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsReprocessv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBioSaxsReprocessv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBioSaxsReprocessv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBioSaxsReprocessv1_0

class XSDataResultBioSaxsMetadatav1_0(object):
	def __init__(self, outputImage=None, sampleCode=None, sampleComments=None, sampleConcentration=None, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None, status=None):
		self.__status = status
		self.__detector = detector
		self.__detectorDistance = detectorDistance
		self.__pixelSize_1 = pixelSize_1
		self.__pixelSize_2 = pixelSize_2
		self.__beamCenter_1 = beamCenter_1
		self.__beamCenter_2 = beamCenter_2
		self.__beamStopDiode = beamStopDiode
		self.__wavelength = wavelength
		self.__machineCurrent = machineCurrent
		self.__maskFile = maskFile
		self.__normalizationFactor = normalizationFactor
		self.__sampleConcentration = sampleConcentration
		self.__sampleComments = sampleComments
		self.__sampleCode = sampleCode
		self.__outputImage = outputImage
	def getStatus(self): return self.__status
	def setStatus(self, status):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setStatus", status, "XSDataStatus")
		self.__status = status
	def delStatus(self): self.__status = None
	# Properties
	status = property(getStatus, setStatus, delStatus, "Property for status")
	def getDetector(self): return self.__detector
	def setDetector(self, detector):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setDetector", detector, "XSDataString")
		self.__detector = detector
	def delDetector(self): self.__detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getDetectorDistance(self): return self.__detectorDistance
	def setDetectorDistance(self, detectorDistance):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setDetectorDistance", detectorDistance, "XSDataLength")
		self.__detectorDistance = detectorDistance
	def delDetectorDistance(self): self.__detectorDistance = None
	# Properties
	detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
	def getPixelSize_1(self): return self.__pixelSize_1
	def setPixelSize_1(self, pixelSize_1):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setPixelSize_1", pixelSize_1, "XSDataLength")
		self.__pixelSize_1 = pixelSize_1
	def delPixelSize_1(self): self.__pixelSize_1 = None
	# Properties
	pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
	def getPixelSize_2(self): return self.__pixelSize_2
	def setPixelSize_2(self, pixelSize_2):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setPixelSize_2", pixelSize_2, "XSDataLength")
		self.__pixelSize_2 = pixelSize_2
	def delPixelSize_2(self): self.__pixelSize_2 = None
	# Properties
	pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
	def getBeamCenter_1(self): return self.__beamCenter_1
	def setBeamCenter_1(self, beamCenter_1):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setBeamCenter_1", beamCenter_1, "XSDataFloat")
		self.__beamCenter_1 = beamCenter_1
	def delBeamCenter_1(self): self.__beamCenter_1 = None
	# Properties
	beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
	def getBeamCenter_2(self): return self.__beamCenter_2
	def setBeamCenter_2(self, beamCenter_2):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setBeamCenter_2", beamCenter_2, "XSDataFloat")
		self.__beamCenter_2 = beamCenter_2
	def delBeamCenter_2(self): self.__beamCenter_2 = None
	# Properties
	beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
	def getBeamStopDiode(self): return self.__beamStopDiode
	def setBeamStopDiode(self, beamStopDiode):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setBeamStopDiode", beamStopDiode, "XSDataFloat")
		self.__beamStopDiode = beamStopDiode
	def delBeamStopDiode(self): self.__beamStopDiode = None
	# Properties
	beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getMachineCurrent(self): return self.__machineCurrent
	def setMachineCurrent(self, machineCurrent):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setMachineCurrent", machineCurrent, "XSDataFloat")
		self.__machineCurrent = machineCurrent
	def delMachineCurrent(self): self.__machineCurrent = None
	# Properties
	machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
	def getMaskFile(self): return self.__maskFile
	def setMaskFile(self, maskFile):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setMaskFile", maskFile, "XSDataImage")
		self.__maskFile = maskFile
	def delMaskFile(self): self.__maskFile = None
	# Properties
	maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
	def getNormalizationFactor(self): return self.__normalizationFactor
	def setNormalizationFactor(self, normalizationFactor):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setNormalizationFactor", normalizationFactor, "XSDataFloat")
		self.__normalizationFactor = normalizationFactor
	def delNormalizationFactor(self): self.__normalizationFactor = None
	# Properties
	normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
	def getSampleConcentration(self): return self.__sampleConcentration
	def setSampleConcentration(self, sampleConcentration):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setSampleConcentration", sampleConcentration, "XSDataFloat")
		self.__sampleConcentration = sampleConcentration
	def delSampleConcentration(self): self.__sampleConcentration = None
	# Properties
	sampleConcentration = property(getSampleConcentration, setSampleConcentration, delSampleConcentration, "Property for sampleConcentration")
	def getSampleComments(self): return self.__sampleComments
	def setSampleComments(self, sampleComments):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setSampleComments", sampleComments, "XSDataString")
		self.__sampleComments = sampleComments
	def delSampleComments(self): self.__sampleComments = None
	# Properties
	sampleComments = property(getSampleComments, setSampleComments, delSampleComments, "Property for sampleComments")
	def getSampleCode(self): return self.__sampleCode
	def setSampleCode(self, sampleCode):
		checkType("XSDataResultBioSaxsMetadatav1_0", "setSampleCode", sampleCode, "XSDataString")
		self.__sampleCode = sampleCode
	def delSampleCode(self): self.__sampleCode = None
	# Properties
	sampleCode = property(getSampleCode, setSampleCode, delSampleCode, "Property for sampleCode")
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
		pass
		if self.__status is not None:
			self.status.export(outfile, level, name_='status')
		else:
			warnEmptyAttribute("status", "XSDataStatus")
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
		if self.__sampleConcentration is not None:
			self.sampleConcentration.export(outfile, level, name_='sampleConcentration')
		if self.__sampleComments is not None:
			self.sampleComments.export(outfile, level, name_='sampleComments')
		if self.__sampleCode is not None:
			self.sampleCode.export(outfile, level, name_='sampleCode')
		if self.__outputImage is not None:
			self.outputImage.export(outfile, level, name_='outputImage')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'status':
			obj_ = XSDataStatus()
			obj_.build(child_)
			self.setStatus(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
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
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCenter_2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamCenter_2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamStopDiode':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamStopDiode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMachineCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maskFile':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setMaskFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'normalizationFactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setNormalizationFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleConcentration':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSampleConcentration(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sampleCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSampleCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputImage':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.setOutputImage(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsMetadatav1_0' )
		outfile.close()
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

class XSDataSpecCommunication(object):
	def __init__(self, specVariableAbort=None, specVariableStatus=None, specVersion=None):
		self.__specVersion = specVersion
		self.__specVariableStatus = specVariableStatus
		self.__specVariableAbort = specVariableAbort
	def getSpecVersion(self): return self.__specVersion
	def setSpecVersion(self, specVersion):
		checkType("XSDataSpecCommunication", "setSpecVersion", specVersion, "XSDataString")
		self.__specVersion = specVersion
	def delSpecVersion(self): self.__specVersion = None
	# Properties
	specVersion = property(getSpecVersion, setSpecVersion, delSpecVersion, "Property for specVersion")
	def getSpecVariableStatus(self): return self.__specVariableStatus
	def setSpecVariableStatus(self, specVariableStatus):
		checkType("XSDataSpecCommunication", "setSpecVariableStatus", specVariableStatus, "XSDataString")
		self.__specVariableStatus = specVariableStatus
	def delSpecVariableStatus(self): self.__specVariableStatus = None
	# Properties
	specVariableStatus = property(getSpecVariableStatus, setSpecVariableStatus, delSpecVariableStatus, "Property for specVariableStatus")
	def getSpecVariableAbort(self): return self.__specVariableAbort
	def setSpecVariableAbort(self, specVariableAbort):
		checkType("XSDataSpecCommunication", "setSpecVariableAbort", specVariableAbort, "XSDataString")
		self.__specVariableAbort = specVariableAbort
	def delSpecVariableAbort(self): self.__specVariableAbort = None
	# Properties
	specVariableAbort = property(getSpecVariableAbort, setSpecVariableAbort, delSpecVariableAbort, "Property for specVariableAbort")
	def export(self, outfile, level, name_='XSDataSpecCommunication'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSpecCommunication'):
		pass
		if self.__specVersion is not None:
			self.specVersion.export(outfile, level, name_='specVersion')
		if self.__specVariableStatus is not None:
			self.specVariableStatus.export(outfile, level, name_='specVariableStatus')
		if self.__specVariableAbort is not None:
			self.specVariableAbort.export(outfile, level, name_='specVariableAbort')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVersion':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVersion(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableStatus':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableStatus(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'specVariableAbort':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpecVariableAbort(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSpecCommunication" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSpecCommunication' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSpecCommunication.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSpecCommunication()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSpecCommunication" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSpecCommunication()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSpecCommunication

class XSDataInputBioSaxsAsciiExportv1_0(XSDataInput):
	def __init__(self, configuration=None, integratedSpectrum=None, integratedImage=None):
		XSDataInput.__init__(self, configuration)
		self.__integratedImage = integratedImage
		self.__integratedSpectrum = integratedSpectrum
	def getIntegratedImage(self): return self.__integratedImage
	def setIntegratedImage(self, integratedImage):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedImage", integratedImage, "XSDataImage")
		self.__integratedImage = integratedImage
	def delIntegratedImage(self): self.__integratedImage = None
	# Properties
	integratedImage = property(getIntegratedImage, setIntegratedImage, delIntegratedImage, "Property for integratedImage")
	def getIntegratedSpectrum(self): return self.__integratedSpectrum
	def setIntegratedSpectrum(self, integratedSpectrum):
		checkType("XSDataInputBioSaxsAsciiExportv1_0", "setIntegratedSpectrum", integratedSpectrum, "XSDataFile")
		self.__integratedSpectrum = integratedSpectrum
	def delIntegratedSpectrum(self): self.__integratedSpectrum = None
	# Properties
	integratedSpectrum = property(getIntegratedSpectrum, setIntegratedSpectrum, delIntegratedSpectrum, "Property for integratedSpectrum")
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
		if self.__integratedSpectrum is not None:
			self.integratedSpectrum.export(outfile, level, name_='integratedSpectrum')
		else:
			warnEmptyAttribute("integratedSpectrum", "XSDataFile")
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
			nodeName_ == 'integratedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedSpectrum(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsAsciiExportv1_0' )
		outfile.close()
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

class XSDataInputBioSaxsSmartMergev1_0(XSDataInput):
	def __init__(self, configuration=None, mergedFile=None, relativeSimilarity=None, absoluteSimilarity=None, inputFile=None):
		XSDataInput.__init__(self, configuration)
		if inputFile is None:
			self.__inputFile = []
		else:
			self.__inputFile = inputFile
		self.__absoluteSimilarity = absoluteSimilarity
		self.__relativeSimilarity = relativeSimilarity
		self.__mergedFile = mergedFile
	def getInputFile(self): return self.__inputFile
	def setInputFile(self, inputFile):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputFile", inputFile, "list")
		self.__inputFile = inputFile
	def delInputFile(self): self.__inputFile = None
	# Properties
	inputFile = property(getInputFile, setInputFile, delInputFile, "Property for inputFile")
	def addInputFile(self, value):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputFile", value, "XSDataFile")
		self.__inputFile.append(value)
	def insertInputFile(self, index, value):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setInputFile", value, "XSDataFile")
		self.__inputFile[index] = value
	def getAbsoluteSimilarity(self): return self.__absoluteSimilarity
	def setAbsoluteSimilarity(self, absoluteSimilarity):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setAbsoluteSimilarity", absoluteSimilarity, "XSDataDouble")
		self.__absoluteSimilarity = absoluteSimilarity
	def delAbsoluteSimilarity(self): self.__absoluteSimilarity = None
	# Properties
	absoluteSimilarity = property(getAbsoluteSimilarity, setAbsoluteSimilarity, delAbsoluteSimilarity, "Property for absoluteSimilarity")
	def getRelativeSimilarity(self): return self.__relativeSimilarity
	def setRelativeSimilarity(self, relativeSimilarity):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setRelativeSimilarity", relativeSimilarity, "XSDataDouble")
		self.__relativeSimilarity = relativeSimilarity
	def delRelativeSimilarity(self): self.__relativeSimilarity = None
	# Properties
	relativeSimilarity = property(getRelativeSimilarity, setRelativeSimilarity, delRelativeSimilarity, "Property for relativeSimilarity")
	def getMergedFile(self): return self.__mergedFile
	def setMergedFile(self, mergedFile):
		checkType("XSDataInputBioSaxsSmartMergev1_0", "setMergedFile", mergedFile, "XSDataFile")
		self.__mergedFile = mergedFile
	def delMergedFile(self): self.__mergedFile = None
	# Properties
	mergedFile = property(getMergedFile, setMergedFile, delMergedFile, "Property for mergedFile")
	def export(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBioSaxsSmartMergev1_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputFile_ in self.getInputFile():
			inputFile_.export(outfile, level, name_='inputFile')
		if self.getInputFile() == []:
			warnEmptyAttribute("inputFile", "XSDataFile")
		if self.__absoluteSimilarity is not None:
			self.absoluteSimilarity.export(outfile, level, name_='absoluteSimilarity')
		if self.__relativeSimilarity is not None:
			self.relativeSimilarity.export(outfile, level, name_='relativeSimilarity')
		if self.__mergedFile is not None:
			self.mergedFile.export(outfile, level, name_='mergedFile')
		else:
			warnEmptyAttribute("mergedFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'absoluteSimilarity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAbsoluteSimilarity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'relativeSimilarity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRelativeSimilarity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mergedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMergedFile(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBioSaxsSmartMergev1_0' )
		outfile.close()
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
	def __init__(self, status=None, processLog=None, integratedSpectrum=None):
		XSDataResult.__init__(self, status)
		self.__integratedSpectrum = integratedSpectrum
		self.__processLog = processLog
	def getIntegratedSpectrum(self): return self.__integratedSpectrum
	def setIntegratedSpectrum(self, integratedSpectrum):
		checkType("XSDataResultBioSaxsAsciiExportv1_0", "setIntegratedSpectrum", integratedSpectrum, "XSDataFile")
		self.__integratedSpectrum = integratedSpectrum
	def delIntegratedSpectrum(self): self.__integratedSpectrum = None
	# Properties
	integratedSpectrum = property(getIntegratedSpectrum, setIntegratedSpectrum, delIntegratedSpectrum, "Property for integratedSpectrum")
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
		if self.__integratedSpectrum is not None:
			self.integratedSpectrum.export(outfile, level, name_='integratedSpectrum')
		else:
			warnEmptyAttribute("integratedSpectrum", "XSDataFile")
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
			nodeName_ == 'integratedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedSpectrum(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAsciiExportv1_0' )
		outfile.close()
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
	def __init__(self, status=None, logFile=None, processLog=None, averagedSpectrum=None, averagedImage=None):
		XSDataResult.__init__(self, status)
		self.__averagedImage = averagedImage
		self.__averagedSpectrum = averagedSpectrum
		self.__processLog = processLog
		self.__logFile = logFile
	def getAveragedImage(self): return self.__averagedImage
	def setAveragedImage(self, averagedImage):
		checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedImage", averagedImage, "XSDataImage")
		self.__averagedImage = averagedImage
	def delAveragedImage(self): self.__averagedImage = None
	# Properties
	averagedImage = property(getAveragedImage, setAveragedImage, delAveragedImage, "Property for averagedImage")
	def getAveragedSpectrum(self): return self.__averagedSpectrum
	def setAveragedSpectrum(self, averagedSpectrum):
		checkType("XSDataResultBioSaxsAveragev1_0", "setAveragedSpectrum", averagedSpectrum, "XSDataFile")
		self.__averagedSpectrum = averagedSpectrum
	def delAveragedSpectrum(self): self.__averagedSpectrum = None
	# Properties
	averagedSpectrum = property(getAveragedSpectrum, setAveragedSpectrum, delAveragedSpectrum, "Property for averagedSpectrum")
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
		if self.__averagedSpectrum is not None:
			self.averagedSpectrum.export(outfile, level, name_='averagedSpectrum')
		else:
			warnEmptyAttribute("averagedSpectrum", "XSDataFile")
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
			nodeName_ == 'averagedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setAveragedSpectrum(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAveragev1_0' )
		outfile.close()
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
	def __init__(self, status=None, processLog=None, integratedSpectrum=None, integratedImage=None, correctedImage=None):
		XSDataResult.__init__(self, status)
		self.__correctedImage = correctedImage
		self.__integratedImage = integratedImage
		self.__integratedSpectrum = integratedSpectrum
		self.__processLog = processLog
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
	def getIntegratedSpectrum(self): return self.__integratedSpectrum
	def setIntegratedSpectrum(self, integratedSpectrum):
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "setIntegratedSpectrum", integratedSpectrum, "XSDataFile")
		self.__integratedSpectrum = integratedSpectrum
	def delIntegratedSpectrum(self): self.__integratedSpectrum = None
	# Properties
	integratedSpectrum = property(getIntegratedSpectrum, setIntegratedSpectrum, delIntegratedSpectrum, "Property for integratedSpectrum")
	def getProcessLog(self): return self.__processLog
	def setProcessLog(self, processLog):
		checkType("XSDataResultBioSaxsAzimutIntv1_0", "setProcessLog", processLog, "XSDataString")
		self.__processLog = processLog
	def delProcessLog(self): self.__processLog = None
	# Properties
	processLog = property(getProcessLog, setProcessLog, delProcessLog, "Property for processLog")
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
		if self.__integratedSpectrum is not None:
			self.integratedSpectrum.export(outfile, level, name_='integratedSpectrum')
		else:
			warnEmptyAttribute("integratedSpectrum", "XSDataFile")
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
			nodeName_ == 'integratedSpectrum':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setIntegratedSpectrum(obj_)
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
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsAzimutIntv1_0' )
		outfile.close()
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
		self.__normalizedImage = normalizedImage
		self.__logFile = logFile
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsNormalizev1_0' )
		outfile.close()
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

class XSDataResultBioSaxsProcessOneRunv1_0(XSDataResult):
	def __init__(self, status=None):
		XSDataResult.__init__(self, status)
	def export(self, outfile, level, name_='XSDataResultBioSaxsProcessOneRunv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsProcessOneRunv1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneRunv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsProcessOneRunv1_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsProcessOneRunv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsProcessOneRunv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsProcessOneRunv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsProcessOneRunv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsProcessOneRunv1_0

class XSDataResultBioSaxsReprocessv1_0(XSDataResult):
	def __init__(self, status=None):
		XSDataResult.__init__(self, status)
	def export(self, outfile, level, name_='XSDataResultBioSaxsReprocessv1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsReprocessv1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultBioSaxsReprocessv1_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsReprocessv1_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBioSaxsReprocessv1_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsReprocessv1_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBioSaxsReprocessv1_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBioSaxsReprocessv1_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBioSaxsReprocessv1_0

class XSDataResultBioSaxsSmartMergev1_0(XSDataResult):
	def __init__(self, status=None, mergedFile=None):
		XSDataResult.__init__(self, status)
		self.__mergedFile = mergedFile
	def getMergedFile(self): return self.__mergedFile
	def setMergedFile(self, mergedFile):
		checkType("XSDataResultBioSaxsSmartMergev1_0", "setMergedFile", mergedFile, "XSDataFile")
		self.__mergedFile = mergedFile
	def delMergedFile(self): self.__mergedFile = None
	# Properties
	mergedFile = property(getMergedFile, setMergedFile, delMergedFile, "Property for mergedFile")
	def export(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBioSaxsSmartMergev1_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__mergedFile is not None:
			self.mergedFile.export(outfile, level, name_='mergedFile')
		else:
			warnEmptyAttribute("mergedFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mergedFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMergedFile(obj_)
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBioSaxsSmartMergev1_0' )
		outfile.close()
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



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Mon Sep 26 10:10::58 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
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


class XSDataAutoRg(XSData):
	def __init__(self, isagregated=None, quality=None, lastPointUsed=None, firstPointUsed=None, i0Stdev=None, i0=None, rgStdev=None, rg=None, filename=None):
		XSData.__init__(self, )
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", filename, "XSDataFile")
		self.__filename = filename
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", rg, "XSDataLength")
		self.__rg = rg
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", rgStdev, "XSDataLength")
		self.__rgStdev = rgStdev
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", i0, "XSDataDouble")
		self.__i0 = i0
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", i0Stdev, "XSDataDouble")
		self.__i0Stdev = i0Stdev
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", firstPointUsed, "XSDataInteger")
		self.__firstPointUsed = firstPointUsed
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", lastPointUsed, "XSDataInteger")
		self.__lastPointUsed = lastPointUsed
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", quality, "XSDataDouble")
		self.__quality = quality
		checkType("XSDataAutoRg", "Constructor of XSDataAutoRg", isagregated, "XSDataBoolean")
		self.__isagregated = isagregated
	def getFilename(self): return self.__filename
	def setFilename(self, filename):
		checkType("XSDataAutoRg", "setFilename", filename, "XSDataFile")
		self.__filename = filename
	def delFilename(self): self.__filename = None
	# Properties
	filename = property(getFilename, setFilename, delFilename, "Property for filename")
	def getRg(self): return self.__rg
	def setRg(self, rg):
		checkType("XSDataAutoRg", "setRg", rg, "XSDataLength")
		self.__rg = rg
	def delRg(self): self.__rg = None
	# Properties
	rg = property(getRg, setRg, delRg, "Property for rg")
	def getRgStdev(self): return self.__rgStdev
	def setRgStdev(self, rgStdev):
		checkType("XSDataAutoRg", "setRgStdev", rgStdev, "XSDataLength")
		self.__rgStdev = rgStdev
	def delRgStdev(self): self.__rgStdev = None
	# Properties
	rgStdev = property(getRgStdev, setRgStdev, delRgStdev, "Property for rgStdev")
	def getI0(self): return self.__i0
	def setI0(self, i0):
		checkType("XSDataAutoRg", "setI0", i0, "XSDataDouble")
		self.__i0 = i0
	def delI0(self): self.__i0 = None
	# Properties
	i0 = property(getI0, setI0, delI0, "Property for i0")
	def getI0Stdev(self): return self.__i0Stdev
	def setI0Stdev(self, i0Stdev):
		checkType("XSDataAutoRg", "setI0Stdev", i0Stdev, "XSDataDouble")
		self.__i0Stdev = i0Stdev
	def delI0Stdev(self): self.__i0Stdev = None
	# Properties
	i0Stdev = property(getI0Stdev, setI0Stdev, delI0Stdev, "Property for i0Stdev")
	def getFirstPointUsed(self): return self.__firstPointUsed
	def setFirstPointUsed(self, firstPointUsed):
		checkType("XSDataAutoRg", "setFirstPointUsed", firstPointUsed, "XSDataInteger")
		self.__firstPointUsed = firstPointUsed
	def delFirstPointUsed(self): self.__firstPointUsed = None
	# Properties
	firstPointUsed = property(getFirstPointUsed, setFirstPointUsed, delFirstPointUsed, "Property for firstPointUsed")
	def getLastPointUsed(self): return self.__lastPointUsed
	def setLastPointUsed(self, lastPointUsed):
		checkType("XSDataAutoRg", "setLastPointUsed", lastPointUsed, "XSDataInteger")
		self.__lastPointUsed = lastPointUsed
	def delLastPointUsed(self): self.__lastPointUsed = None
	# Properties
	lastPointUsed = property(getLastPointUsed, setLastPointUsed, delLastPointUsed, "Property for lastPointUsed")
	def getQuality(self): return self.__quality
	def setQuality(self, quality):
		checkType("XSDataAutoRg", "setQuality", quality, "XSDataDouble")
		self.__quality = quality
	def delQuality(self): self.__quality = None
	# Properties
	quality = property(getQuality, setQuality, delQuality, "Property for quality")
	def getIsagregated(self): return self.__isagregated
	def setIsagregated(self, isagregated):
		checkType("XSDataAutoRg", "setIsagregated", isagregated, "XSDataBoolean")
		self.__isagregated = isagregated
	def delIsagregated(self): self.__isagregated = None
	# Properties
	isagregated = property(getIsagregated, setIsagregated, delIsagregated, "Property for isagregated")
	def export(self, outfile, level, name_='XSDataAutoRg'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataAutoRg'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__filename is not None:
			self.filename.export(outfile, level, name_='filename')
		else:
			warnEmptyAttribute("filename", "XSDataFile")
		if self.__rg is not None:
			self.rg.export(outfile, level, name_='rg')
		else:
			warnEmptyAttribute("rg", "XSDataLength")
		if self.__rgStdev is not None:
			self.rgStdev.export(outfile, level, name_='rgStdev')
		else:
			warnEmptyAttribute("rgStdev", "XSDataLength")
		if self.__i0 is not None:
			self.i0.export(outfile, level, name_='i0')
		else:
			warnEmptyAttribute("i0", "XSDataDouble")
		if self.__i0Stdev is not None:
			self.i0Stdev.export(outfile, level, name_='i0Stdev')
		else:
			warnEmptyAttribute("i0Stdev", "XSDataDouble")
		if self.__firstPointUsed is not None:
			self.firstPointUsed.export(outfile, level, name_='firstPointUsed')
		else:
			warnEmptyAttribute("firstPointUsed", "XSDataInteger")
		if self.__lastPointUsed is not None:
			self.lastPointUsed.export(outfile, level, name_='lastPointUsed')
		else:
			warnEmptyAttribute("lastPointUsed", "XSDataInteger")
		if self.__quality is not None:
			self.quality.export(outfile, level, name_='quality')
		else:
			warnEmptyAttribute("quality", "XSDataDouble")
		if self.__isagregated is not None:
			self.isagregated.export(outfile, level, name_='isagregated')
		else:
			warnEmptyAttribute("isagregated", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'filename':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFilename(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rg':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRg(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rgStdev':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRgStdev(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'i0':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setI0(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'i0Stdev':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setI0Stdev(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'firstPointUsed':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFirstPointUsed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lastPointUsed':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setLastPointUsed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'quality':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setQuality(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'isagregated':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setIsagregated(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataAutoRg" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataAutoRg' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataAutoRg is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataAutoRg.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataAutoRg()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataAutoRg" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataAutoRg()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataAutoRg

class XSDataBioSaxsExperimentSetup(XSData):
	def __init__(self, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
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
	def __init__(self, temperature=None, code=None, comments=None, concentration=None):
		XSData.__init__(self, )
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", concentration, "XSDataDouble")
		self.__concentration = concentration
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", code, "XSDataString")
		self.__code = code
		checkType("XSDataBioSaxsSample", "Constructor of XSDataBioSaxsSample", temperature, "XSDataDouble")
		self.__temperature = temperature
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
	def getTemperature(self): return self.__temperature
	def setTemperature(self, temperature):
		checkType("XSDataBioSaxsSample", "setTemperature", temperature, "XSDataDouble")
		self.__temperature = temperature
	def delTemperature(self): self.__temperature = None
	# Properties
	temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
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
		if self.__temperature is not None:
			self.temperature.export(outfile, level, name_='temperature')
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

class XSDataSaxsSample(XSData):
	"""Everything describing the sample"""
	def __init__(self, code=None, comment=None, name=None):
		XSData.__init__(self, )
		checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", name, "XSDataString")
		self.__name = name
		checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", comment, "XSDataString")
		self.__comment = comment
		checkType("XSDataSaxsSample", "Constructor of XSDataSaxsSample", code, "XSDataString")
		self.__code = code
	def getName(self): return self.__name
	def setName(self, name):
		checkType("XSDataSaxsSample", "setName", name, "XSDataString")
		self.__name = name
	def delName(self): self.__name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("XSDataSaxsSample", "setComment", comment, "XSDataString")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDataSaxsSample", "setCode", code, "XSDataString")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def export(self, outfile, level, name_='XSDataSaxsSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSaxsSample'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__name is not None:
			self.name.export(outfile, level, name_='name')
		if self.__comment is not None:
			self.comment.export(outfile, level, name_='comment')
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
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
			nodeName_ == 'comment':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComment(obj_)
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
		self.export( oStreamString, 0, name_="XSDataSaxsSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSaxsSample' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSaxsSample is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSaxsSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSaxsSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSaxsSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSaxsSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSaxsSample

class XSDataSaxsSeries(XSData):
	"""Basical"""
	def __init__(self, concentration=None, curve=None):
		XSData.__init__(self, )
		checkType("XSDataSaxsSeries", "Constructor of XSDataSaxsSeries", curve, "XSDataFile")
		self.__curve = curve
		checkType("XSDataSaxsSeries", "Constructor of XSDataSaxsSeries", concentration, "XSDataDouble")
		self.__concentration = concentration
	def getCurve(self): return self.__curve
	def setCurve(self, curve):
		checkType("XSDataSaxsSeries", "setCurve", curve, "XSDataFile")
		self.__curve = curve
	def delCurve(self): self.__curve = None
	# Properties
	curve = property(getCurve, setCurve, delCurve, "Property for curve")
	def getConcentration(self): return self.__concentration
	def setConcentration(self, concentration):
		checkType("XSDataSaxsSeries", "setConcentration", concentration, "XSDataDouble")
		self.__concentration = concentration
	def delConcentration(self): self.__concentration = None
	# Properties
	concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
	def export(self, outfile, level, name_='XSDataSaxsSeries'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSaxsSeries'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__curve is not None:
			self.curve.export(outfile, level, name_='curve')
		else:
			warnEmptyAttribute("curve", "XSDataFile")
		if self.__concentration is not None:
			self.concentration.export(outfile, level, name_='concentration')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'curve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'concentration':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setConcentration(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSaxsSeries" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSaxsSeries' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataSaxsSeries is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSaxsSeries.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSaxsSeries()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSaxsSeries" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSaxsSeries()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSaxsSeries

class XSDataInputAutoRg(XSDataInput):
	def __init__(self, configuration=None, maxSminRg=None, maxSmaxRg=None, minIntervalLength=None, inputCurve=None, sample=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", sample, "XSDataSaxsSample")
		self.__sample = sample
		if inputCurve is None:
			self.__inputCurve = []
		else:
			checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", inputCurve, "list")
			self.__inputCurve = inputCurve
		checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", minIntervalLength, "XSDataInteger")
		self.__minIntervalLength = minIntervalLength
		checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", maxSmaxRg, "XSDataDouble")
		self.__maxSmaxRg = maxSmaxRg
		checkType("XSDataInputAutoRg", "Constructor of XSDataInputAutoRg", maxSminRg, "XSDataDouble")
		self.__maxSminRg = maxSminRg
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputAutoRg", "setSample", sample, "XSDataSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getInputCurve(self): return self.__inputCurve
	def setInputCurve(self, inputCurve):
		checkType("XSDataInputAutoRg", "setInputCurve", inputCurve, "list")
		self.__inputCurve = inputCurve
	def delInputCurve(self): self.__inputCurve = None
	# Properties
	inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
	def addInputCurve(self, value):
		checkType("XSDataInputAutoRg", "setInputCurve", value, "XSDataFile")
		self.__inputCurve.append(value)
	def insertInputCurve(self, index, value):
		checkType("XSDataInputAutoRg", "setInputCurve", value, "XSDataFile")
		self.__inputCurve[index] = value
	def getMinIntervalLength(self): return self.__minIntervalLength
	def setMinIntervalLength(self, minIntervalLength):
		checkType("XSDataInputAutoRg", "setMinIntervalLength", minIntervalLength, "XSDataInteger")
		self.__minIntervalLength = minIntervalLength
	def delMinIntervalLength(self): self.__minIntervalLength = None
	# Properties
	minIntervalLength = property(getMinIntervalLength, setMinIntervalLength, delMinIntervalLength, "Property for minIntervalLength")
	def getMaxSmaxRg(self): return self.__maxSmaxRg
	def setMaxSmaxRg(self, maxSmaxRg):
		checkType("XSDataInputAutoRg", "setMaxSmaxRg", maxSmaxRg, "XSDataDouble")
		self.__maxSmaxRg = maxSmaxRg
	def delMaxSmaxRg(self): self.__maxSmaxRg = None
	# Properties
	maxSmaxRg = property(getMaxSmaxRg, setMaxSmaxRg, delMaxSmaxRg, "Property for maxSmaxRg")
	def getMaxSminRg(self): return self.__maxSminRg
	def setMaxSminRg(self, maxSminRg):
		checkType("XSDataInputAutoRg", "setMaxSminRg", maxSminRg, "XSDataDouble")
		self.__maxSminRg = maxSminRg
	def delMaxSminRg(self): self.__maxSminRg = None
	# Properties
	maxSminRg = property(getMaxSminRg, setMaxSminRg, delMaxSminRg, "Property for maxSminRg")
	def export(self, outfile, level, name_='XSDataInputAutoRg'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputAutoRg'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		for inputCurve_ in self.getInputCurve():
			inputCurve_.export(outfile, level, name_='inputCurve')
		if self.getInputCurve() == []:
			warnEmptyAttribute("inputCurve", "XSDataFile")
		if self.__minIntervalLength is not None:
			self.minIntervalLength.export(outfile, level, name_='minIntervalLength')
		if self.__maxSmaxRg is not None:
			self.maxSmaxRg.export(outfile, level, name_='maxSmaxRg')
		if self.__maxSminRg is not None:
			self.maxSminRg.export(outfile, level, name_='maxSminRg')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSaxsSample()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurve.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minIntervalLength':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setMinIntervalLength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxSmaxRg':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxSmaxRg(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxSminRg':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxSminRg(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputAutoRg" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputAutoRg' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputAutoRg is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputAutoRg.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputAutoRg()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputAutoRg" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputAutoRg()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputAutoRg

class XSDataInputDataver(XSDataInput):
	"""dataver averages two or more curves from files"""
	def __init__(self, configuration=None, outputCurve=None, inputCurve=None):
		XSDataInput.__init__(self, configuration)
		if inputCurve is None:
			self.__inputCurve = []
		else:
			checkType("XSDataInputDataver", "Constructor of XSDataInputDataver", inputCurve, "list")
			self.__inputCurve = inputCurve
		checkType("XSDataInputDataver", "Constructor of XSDataInputDataver", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def getInputCurve(self): return self.__inputCurve
	def setInputCurve(self, inputCurve):
		checkType("XSDataInputDataver", "setInputCurve", inputCurve, "list")
		self.__inputCurve = inputCurve
	def delInputCurve(self): self.__inputCurve = None
	# Properties
	inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
	def addInputCurve(self, value):
		checkType("XSDataInputDataver", "setInputCurve", value, "XSDataFile")
		self.__inputCurve.append(value)
	def insertInputCurve(self, index, value):
		checkType("XSDataInputDataver", "setInputCurve", value, "XSDataFile")
		self.__inputCurve[index] = value
	def getOutputCurve(self): return self.__outputCurve
	def setOutputCurve(self, outputCurve):
		checkType("XSDataInputDataver", "setOutputCurve", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def delOutputCurve(self): self.__outputCurve = None
	# Properties
	outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
	def export(self, outfile, level, name_='XSDataInputDataver'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDataver'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputCurve_ in self.getInputCurve():
			inputCurve_.export(outfile, level, name_='inputCurve')
		if self.getInputCurve() == []:
			warnEmptyAttribute("inputCurve", "XSDataFile")
		if self.__outputCurve is not None:
			self.outputCurve.export(outfile, level, name_='outputCurve')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurve.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputCurve(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputDataver" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputDataver' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputDataver is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputDataver.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDataver()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputDataver" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDataver()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputDataver

class XSDataInputDatcmp(XSDataInput):
	"""datcmp compares two curves from files
	"""
	def __init__(self, configuration=None, inputCurve=None):
		XSDataInput.__init__(self, configuration)
		if inputCurve is None:
			self.__inputCurve = []
		else:
			checkType("XSDataInputDatcmp", "Constructor of XSDataInputDatcmp", inputCurve, "list")
			self.__inputCurve = inputCurve
	def getInputCurve(self): return self.__inputCurve
	def setInputCurve(self, inputCurve):
		checkType("XSDataInputDatcmp", "setInputCurve", inputCurve, "list")
		self.__inputCurve = inputCurve
	def delInputCurve(self): self.__inputCurve = None
	# Properties
	inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
	def addInputCurve(self, value):
		checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
		self.__inputCurve.append(value)
	def insertInputCurve(self, index, value):
		checkType("XSDataInputDatcmp", "setInputCurve", value, "XSDataFile")
		self.__inputCurve[index] = value
	def export(self, outfile, level, name_='XSDataInputDatcmp'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDatcmp'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputCurve_ in self.getInputCurve():
			inputCurve_.export(outfile, level, name_='inputCurve')
		if self.getInputCurve() == []:
			warnEmptyAttribute("inputCurve", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurve.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputDatcmp" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputDatcmp' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputDatcmp is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputDatcmp.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatcmp()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputDatcmp" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatcmp()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputDatcmp

class XSDataInputDatop(XSDataInput):
	"""datop makes an operation on curves"""
	def __init__(self, configuration=None, constant=None, operation=None, outputCurve=None, inputCurve=None):
		XSDataInput.__init__(self, configuration)
		if inputCurve is None:
			self.__inputCurve = []
		else:
			checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", inputCurve, "list")
			self.__inputCurve = inputCurve
		checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
		checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", operation, "XSDataString")
		self.__operation = operation
		checkType("XSDataInputDatop", "Constructor of XSDataInputDatop", constant, "XSDataDouble")
		self.__constant = constant
	def getInputCurve(self): return self.__inputCurve
	def setInputCurve(self, inputCurve):
		checkType("XSDataInputDatop", "setInputCurve", inputCurve, "list")
		self.__inputCurve = inputCurve
	def delInputCurve(self): self.__inputCurve = None
	# Properties
	inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
	def addInputCurve(self, value):
		checkType("XSDataInputDatop", "setInputCurve", value, "XSDataFile")
		self.__inputCurve.append(value)
	def insertInputCurve(self, index, value):
		checkType("XSDataInputDatop", "setInputCurve", value, "XSDataFile")
		self.__inputCurve[index] = value
	def getOutputCurve(self): return self.__outputCurve
	def setOutputCurve(self, outputCurve):
		checkType("XSDataInputDatop", "setOutputCurve", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def delOutputCurve(self): self.__outputCurve = None
	# Properties
	outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
	def getOperation(self): return self.__operation
	def setOperation(self, operation):
		checkType("XSDataInputDatop", "setOperation", operation, "XSDataString")
		self.__operation = operation
	def delOperation(self): self.__operation = None
	# Properties
	operation = property(getOperation, setOperation, delOperation, "Property for operation")
	def getConstant(self): return self.__constant
	def setConstant(self, constant):
		checkType("XSDataInputDatop", "setConstant", constant, "XSDataDouble")
		self.__constant = constant
	def delConstant(self): self.__constant = None
	# Properties
	constant = property(getConstant, setConstant, delConstant, "Property for constant")
	def export(self, outfile, level, name_='XSDataInputDatop'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDatop'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for inputCurve_ in self.getInputCurve():
			inputCurve_.export(outfile, level, name_='inputCurve')
		if self.getInputCurve() == []:
			warnEmptyAttribute("inputCurve", "XSDataFile")
		if self.__outputCurve is not None:
			self.outputCurve.export(outfile, level, name_='outputCurve')
		else:
			warnEmptyAttribute("outputCurve", "XSDataFile")
		if self.__operation is not None:
			self.operation.export(outfile, level, name_='operation')
		else:
			warnEmptyAttribute("operation", "XSDataString")
		if self.__constant is not None:
			self.constant.export(outfile, level, name_='constant')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.inputCurve.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputCurve':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputCurve(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'operation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOperation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'constant':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setConstant(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputDatop" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputDatop' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputDatop is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputDatop.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatop()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputDatop" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDatop()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputDatop

class XSDataInputSaxsPipeline(XSDataInput):
	"""Run ProcessOneFile on each file of a time time serie until autorg """
	def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", fileSerie, "XSDataFileSeries")
		self.__fileSerie = fileSerie
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", sample, "XSDataBioSaxsSample")
		self.__sample = sample
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directory1D, "XSDataFile")
		self.__directory1D = directory1D
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directory2D, "XSDataFile")
		self.__directory2D = directory2D
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
		checkType("XSDataInputSaxsPipeline", "Constructor of XSDataInputSaxsPipeline", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def getFileSerie(self): return self.__fileSerie
	def setFileSerie(self, fileSerie):
		checkType("XSDataInputSaxsPipeline", "setFileSerie", fileSerie, "XSDataFileSeries")
		self.__fileSerie = fileSerie
	def delFileSerie(self): self.__fileSerie = None
	# Properties
	fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputSaxsPipeline", "setSample", sample, "XSDataBioSaxsSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getExperimentSetup(self): return self.__experimentSetup
	def setExperimentSetup(self, experimentSetup):
		checkType("XSDataInputSaxsPipeline", "setExperimentSetup", experimentSetup, "XSDataBioSaxsExperimentSetup")
		self.__experimentSetup = experimentSetup
	def delExperimentSetup(self): self.__experimentSetup = None
	# Properties
	experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
	def getDirectory1D(self): return self.__directory1D
	def setDirectory1D(self, directory1D):
		checkType("XSDataInputSaxsPipeline", "setDirectory1D", directory1D, "XSDataFile")
		self.__directory1D = directory1D
	def delDirectory1D(self): self.__directory1D = None
	# Properties
	directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
	def getDirectory2D(self): return self.__directory2D
	def setDirectory2D(self, directory2D):
		checkType("XSDataInputSaxsPipeline", "setDirectory2D", directory2D, "XSDataFile")
		self.__directory2D = directory2D
	def delDirectory2D(self): self.__directory2D = None
	# Properties
	directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
	def getDirectoryMisc(self): return self.__directoryMisc
	def setDirectoryMisc(self, directoryMisc):
		checkType("XSDataInputSaxsPipeline", "setDirectoryMisc", directoryMisc, "XSDataFile")
		self.__directoryMisc = directoryMisc
	def delDirectoryMisc(self): self.__directoryMisc = None
	# Properties
	directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
	def getForceReprocess(self): return self.__forceReprocess
	def setForceReprocess(self, forceReprocess):
		checkType("XSDataInputSaxsPipeline", "setForceReprocess", forceReprocess, "XSDataBoolean")
		self.__forceReprocess = forceReprocess
	def delForceReprocess(self): self.__forceReprocess = None
	# Properties
	forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
	def getAbsoluteFidelity(self): return self.__absoluteFidelity
	def setAbsoluteFidelity(self, absoluteFidelity):
		checkType("XSDataInputSaxsPipeline", "setAbsoluteFidelity", absoluteFidelity, "XSDataDouble")
		self.__absoluteFidelity = absoluteFidelity
	def delAbsoluteFidelity(self): self.__absoluteFidelity = None
	# Properties
	absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
	def getRelativeFidelity(self): return self.__relativeFidelity
	def setRelativeFidelity(self, relativeFidelity):
		checkType("XSDataInputSaxsPipeline", "setRelativeFidelity", relativeFidelity, "XSDataDouble")
		self.__relativeFidelity = relativeFidelity
	def delRelativeFidelity(self): self.__relativeFidelity = None
	# Properties
	relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
	def getRawImageSize(self): return self.__rawImageSize
	def setRawImageSize(self, rawImageSize):
		checkType("XSDataInputSaxsPipeline", "setRawImageSize", rawImageSize, "XSDataInteger")
		self.__rawImageSize = rawImageSize
	def delRawImageSize(self): self.__rawImageSize = None
	# Properties
	rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
	def export(self, outfile, level, name_='XSDataInputSaxsPipeline'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSaxsPipeline'):
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
		self.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputSaxsPipeline' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputSaxsPipeline is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputSaxsPipeline.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSaxsPipeline()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSaxsPipeline()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsPipeline

class XSDataResultAutoRg(XSDataResult):
	def __init__(self, status=None, autoRgOut=None):
		XSDataResult.__init__(self, status)
		if autoRgOut is None:
			self.__autoRgOut = []
		else:
			checkType("XSDataResultAutoRg", "Constructor of XSDataResultAutoRg", autoRgOut, "list")
			self.__autoRgOut = autoRgOut
	def getAutoRgOut(self): return self.__autoRgOut
	def setAutoRgOut(self, autoRgOut):
		checkType("XSDataResultAutoRg", "setAutoRgOut", autoRgOut, "list")
		self.__autoRgOut = autoRgOut
	def delAutoRgOut(self): self.__autoRgOut = None
	# Properties
	autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
	def addAutoRgOut(self, value):
		checkType("XSDataResultAutoRg", "setAutoRgOut", value, "XSDataAutoRg")
		self.__autoRgOut.append(value)
	def insertAutoRgOut(self, index, value):
		checkType("XSDataResultAutoRg", "setAutoRgOut", value, "XSDataAutoRg")
		self.__autoRgOut[index] = value
	def export(self, outfile, level, name_='XSDataResultAutoRg'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultAutoRg'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for autoRgOut_ in self.getAutoRgOut():
			autoRgOut_.export(outfile, level, name_='autoRgOut')
		if self.getAutoRgOut() == []:
			warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'autoRgOut':
			obj_ = XSDataAutoRg()
			obj_.build(child_)
			self.autoRgOut.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultAutoRg" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultAutoRg' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultAutoRg is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultAutoRg.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultAutoRg()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultAutoRg" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultAutoRg()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultAutoRg

class XSDataResultDataver(XSDataResult):
	"""Result of Dataver 	"""
	def __init__(self, status=None, outputCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDataver", "Constructor of XSDataResultDataver", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def getOutputCurve(self): return self.__outputCurve
	def setOutputCurve(self, outputCurve):
		checkType("XSDataResultDataver", "setOutputCurve", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def delOutputCurve(self): self.__outputCurve = None
	# Properties
	outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
	def export(self, outfile, level, name_='XSDataResultDataver'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDataver'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputCurve is not None:
			self.outputCurve.export(outfile, level, name_='outputCurve')
		else:
			warnEmptyAttribute("outputCurve", "XSDataFile")
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
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultDataver" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultDataver' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultDataver is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultDataver.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDataver()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultDataver" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDataver()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultDataver

class XSDataResultDatcmp(XSDataResult):
	"""Higher chi-values indicate dis-similarities in the input.

	 Fidelity gives the likelihood of the two data sets being identical.
	"""
	def __init__(self, status=None, fidelity=None, chi=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", chi, "XSDataDouble")
		self.__chi = chi
		checkType("XSDataResultDatcmp", "Constructor of XSDataResultDatcmp", fidelity, "XSDataDouble")
		self.__fidelity = fidelity
	def getChi(self): return self.__chi
	def setChi(self, chi):
		checkType("XSDataResultDatcmp", "setChi", chi, "XSDataDouble")
		self.__chi = chi
	def delChi(self): self.__chi = None
	# Properties
	chi = property(getChi, setChi, delChi, "Property for chi")
	def getFidelity(self): return self.__fidelity
	def setFidelity(self, fidelity):
		checkType("XSDataResultDatcmp", "setFidelity", fidelity, "XSDataDouble")
		self.__fidelity = fidelity
	def delFidelity(self): self.__fidelity = None
	# Properties
	fidelity = property(getFidelity, setFidelity, delFidelity, "Property for fidelity")
	def export(self, outfile, level, name_='XSDataResultDatcmp'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDatcmp'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__chi is not None:
			self.chi.export(outfile, level, name_='chi')
		else:
			warnEmptyAttribute("chi", "XSDataDouble")
		if self.__fidelity is not None:
			self.fidelity.export(outfile, level, name_='fidelity')
		else:
			warnEmptyAttribute("fidelity", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chi':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setChi(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fidelity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFidelity(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultDatcmp" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultDatcmp' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultDatcmp is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultDatcmp.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatcmp()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultDatcmp" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatcmp()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultDatcmp

class XSDataResultDatop(XSDataResult):
	"""Result of Datop 	"""
	def __init__(self, status=None, outputCurve=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDatop", "Constructor of XSDataResultDatop", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def getOutputCurve(self): return self.__outputCurve
	def setOutputCurve(self, outputCurve):
		checkType("XSDataResultDatop", "setOutputCurve", outputCurve, "XSDataFile")
		self.__outputCurve = outputCurve
	def delOutputCurve(self): self.__outputCurve = None
	# Properties
	outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
	def export(self, outfile, level, name_='XSDataResultDatop'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDatop'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputCurve is not None:
			self.outputCurve.export(outfile, level, name_='outputCurve')
		else:
			warnEmptyAttribute("outputCurve", "XSDataFile")
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
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultDatop" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultDatop' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultDatop is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultDatop.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatop()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultDatop" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDatop()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultDatop

class XSDataResultSaxsPipeline(XSDataResult):
	def __init__(self, status=None, autoRgOut=None):
		XSDataResult.__init__(self, status)
		if autoRgOut is None:
			self.__autoRgOut = []
		else:
			checkType("XSDataResultSaxsPipeline", "Constructor of XSDataResultSaxsPipeline", autoRgOut, "list")
			self.__autoRgOut = autoRgOut
	def getAutoRgOut(self): return self.__autoRgOut
	def setAutoRgOut(self, autoRgOut):
		checkType("XSDataResultSaxsPipeline", "setAutoRgOut", autoRgOut, "list")
		self.__autoRgOut = autoRgOut
	def delAutoRgOut(self): self.__autoRgOut = None
	# Properties
	autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
	def addAutoRgOut(self, value):
		checkType("XSDataResultSaxsPipeline", "setAutoRgOut", value, "XSDataAutoRg")
		self.__autoRgOut.append(value)
	def insertAutoRgOut(self, index, value):
		checkType("XSDataResultSaxsPipeline", "setAutoRgOut", value, "XSDataAutoRg")
		self.__autoRgOut[index] = value
	def export(self, outfile, level, name_='XSDataResultSaxsPipeline'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSaxsPipeline'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for autoRgOut_ in self.getAutoRgOut():
			autoRgOut_.export(outfile, level, name_='autoRgOut')
		if self.getAutoRgOut() == []:
			warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'autoRgOut':
			obj_ = XSDataAutoRg()
			obj_.build(child_)
			self.autoRgOut.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultSaxsPipeline' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultSaxsPipeline is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultSaxsPipeline.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSaxsPipeline()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSaxsPipeline()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsPipeline



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Mon May 14 10:38::44 2012 by EDGenerateDS.
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
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
}

try:
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataString
	from XSDataMXv1 import XSDataDiffractionPlan
	from XSDataMXv1 import XSDataExperimentalCondition
	from XSDataMXv1 import XSDataInputCharacterisation
	from XSDataMXv1 import XSDataResultCharacterisation
	from XSDataMXv1 import XSDataResultControlISPyB
	from XSDataCommon import XSDataLength
	from XSDataCommon import XSDataTime
	from XSDataCommon import XSDataWavelength
	from XSDataMXv1 import XSDataSampleCrystalMM
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataResultControlISPyB
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength
from XSDataMXv1 import XSDataSampleCrystalMM




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


class XSDataInputInterface(object):
	def __init__(self, inputCharacterisation=None, comments=None, shortComments=None, dataCollectionId=None, transmission=None, wavelength=None, beamPosY=None, beamPosX=None, resultsFilePath=None, generatedTemplateFile=None, templateMode=None, beamSizeY=None, beamSizeX=None, beamSize=None, minExposureTimePerImage=None, flux=None, imagePath=None, sample=None, diffractionPlan=None, experimentalCondition=None):
	
	
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", sample, "XSDataSampleCrystalMM")
		self._sample = sample
		if imagePath is None:
			self._imagePath = []
		else:
			checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", imagePath, "list")
			self._imagePath = imagePath
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", flux, "XSDataFloat")
		self._flux = flux
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSize, "XSDataLength")
		self._beamSize = beamSize
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSizeX, "XSDataLength")
		self._beamSizeX = beamSizeX
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSizeY, "XSDataLength")
		self._beamSizeY = beamSizeY
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", templateMode, "XSDataBoolean")
		self._templateMode = templateMode
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", generatedTemplateFile, "XSDataFile")
		self._generatedTemplateFile = generatedTemplateFile
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", resultsFilePath, "XSDataFile")
		self._resultsFilePath = resultsFilePath
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamPosX, "XSDataFloat")
		self._beamPosX = beamPosX
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamPosY, "XSDataFloat")
		self._beamPosY = beamPosY
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", transmission, "XSDataDouble")
		self._transmission = transmission
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", shortComments, "XSDataString")
		self._shortComments = shortComments
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", comments, "XSDataString")
		self._comments = comments
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", inputCharacterisation, "XSDataInputCharacterisation")
		self._inputCharacterisation = inputCharacterisation
	def getExperimentalCondition(self): return self._experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataInputInterface", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self._experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self._experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputInterface", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getSample(self): return self._sample
	def setSample(self, sample):
		checkType("XSDataInputInterface", "setSample", sample, "XSDataSampleCrystalMM")
		self._sample = sample
	def delSample(self): self._sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getImagePath(self): return self._imagePath
	def setImagePath(self, imagePath):
		checkType("XSDataInputInterface", "setImagePath", imagePath, "list")
		self._imagePath = imagePath
	def delImagePath(self): self._imagePath = None
	# Properties
	imagePath = property(getImagePath, setImagePath, delImagePath, "Property for imagePath")
	def addImagePath(self, value):
		checkType("XSDataInputInterface", "setImagePath", value, "XSDataFile")
		self._imagePath.append(value)
	def insertImagePath(self, index, value):
		checkType("XSDataInputInterface", "setImagePath", value, "XSDataFile")
		self._imagePath[index] = value
	def getFlux(self): return self._flux
	def setFlux(self, flux):
		checkType("XSDataInputInterface", "setFlux", flux, "XSDataFloat")
		self._flux = flux
	def delFlux(self): self._flux = None
	# Properties
	flux = property(getFlux, setFlux, delFlux, "Property for flux")
	def getMinExposureTimePerImage(self): return self._minExposureTimePerImage
	def setMinExposureTimePerImage(self, minExposureTimePerImage):
		checkType("XSDataInputInterface", "setMinExposureTimePerImage", minExposureTimePerImage, "XSDataTime")
		self._minExposureTimePerImage = minExposureTimePerImage
	def delMinExposureTimePerImage(self): self._minExposureTimePerImage = None
	# Properties
	minExposureTimePerImage = property(getMinExposureTimePerImage, setMinExposureTimePerImage, delMinExposureTimePerImage, "Property for minExposureTimePerImage")
	def getBeamSize(self): return self._beamSize
	def setBeamSize(self, beamSize):
		checkType("XSDataInputInterface", "setBeamSize", beamSize, "XSDataLength")
		self._beamSize = beamSize
	def delBeamSize(self): self._beamSize = None
	# Properties
	beamSize = property(getBeamSize, setBeamSize, delBeamSize, "Property for beamSize")
	def getBeamSizeX(self): return self._beamSizeX
	def setBeamSizeX(self, beamSizeX):
		checkType("XSDataInputInterface", "setBeamSizeX", beamSizeX, "XSDataLength")
		self._beamSizeX = beamSizeX
	def delBeamSizeX(self): self._beamSizeX = None
	# Properties
	beamSizeX = property(getBeamSizeX, setBeamSizeX, delBeamSizeX, "Property for beamSizeX")
	def getBeamSizeY(self): return self._beamSizeY
	def setBeamSizeY(self, beamSizeY):
		checkType("XSDataInputInterface", "setBeamSizeY", beamSizeY, "XSDataLength")
		self._beamSizeY = beamSizeY
	def delBeamSizeY(self): self._beamSizeY = None
	# Properties
	beamSizeY = property(getBeamSizeY, setBeamSizeY, delBeamSizeY, "Property for beamSizeY")
	def getTemplateMode(self): return self._templateMode
	def setTemplateMode(self, templateMode):
		checkType("XSDataInputInterface", "setTemplateMode", templateMode, "XSDataBoolean")
		self._templateMode = templateMode
	def delTemplateMode(self): self._templateMode = None
	# Properties
	templateMode = property(getTemplateMode, setTemplateMode, delTemplateMode, "Property for templateMode")
	def getGeneratedTemplateFile(self): return self._generatedTemplateFile
	def setGeneratedTemplateFile(self, generatedTemplateFile):
		checkType("XSDataInputInterface", "setGeneratedTemplateFile", generatedTemplateFile, "XSDataFile")
		self._generatedTemplateFile = generatedTemplateFile
	def delGeneratedTemplateFile(self): self._generatedTemplateFile = None
	# Properties
	generatedTemplateFile = property(getGeneratedTemplateFile, setGeneratedTemplateFile, delGeneratedTemplateFile, "Property for generatedTemplateFile")
	def getResultsFilePath(self): return self._resultsFilePath
	def setResultsFilePath(self, resultsFilePath):
		checkType("XSDataInputInterface", "setResultsFilePath", resultsFilePath, "XSDataFile")
		self._resultsFilePath = resultsFilePath
	def delResultsFilePath(self): self._resultsFilePath = None
	# Properties
	resultsFilePath = property(getResultsFilePath, setResultsFilePath, delResultsFilePath, "Property for resultsFilePath")
	def getBeamPosX(self): return self._beamPosX
	def setBeamPosX(self, beamPosX):
		checkType("XSDataInputInterface", "setBeamPosX", beamPosX, "XSDataFloat")
		self._beamPosX = beamPosX
	def delBeamPosX(self): self._beamPosX = None
	# Properties
	beamPosX = property(getBeamPosX, setBeamPosX, delBeamPosX, "Property for beamPosX")
	def getBeamPosY(self): return self._beamPosY
	def setBeamPosY(self, beamPosY):
		checkType("XSDataInputInterface", "setBeamPosY", beamPosY, "XSDataFloat")
		self._beamPosY = beamPosY
	def delBeamPosY(self): self._beamPosY = None
	# Properties
	beamPosY = property(getBeamPosY, setBeamPosY, delBeamPosY, "Property for beamPosY")
	def getWavelength(self): return self._wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputInterface", "setWavelength", wavelength, "XSDataWavelength")
		self._wavelength = wavelength
	def delWavelength(self): self._wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataInputInterface", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getDataCollectionId(self): return self._dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataInputInterface", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self._dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self._dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getShortComments(self): return self._shortComments
	def setShortComments(self, shortComments):
		checkType("XSDataInputInterface", "setShortComments", shortComments, "XSDataString")
		self._shortComments = shortComments
	def delShortComments(self): self._shortComments = None
	# Properties
	shortComments = property(getShortComments, setShortComments, delShortComments, "Property for shortComments")
	def getComments(self): return self._comments
	def setComments(self, comments):
		checkType("XSDataInputInterface", "setComments", comments, "XSDataString")
		self._comments = comments
	def delComments(self): self._comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getInputCharacterisation(self): return self._inputCharacterisation
	def setInputCharacterisation(self, inputCharacterisation):
		checkType("XSDataInputInterface", "setInputCharacterisation", inputCharacterisation, "XSDataInputCharacterisation")
		self._inputCharacterisation = inputCharacterisation
	def delInputCharacterisation(self): self._inputCharacterisation = None
	# Properties
	inputCharacterisation = property(getInputCharacterisation, setInputCharacterisation, delInputCharacterisation, "Property for inputCharacterisation")
	def export(self, outfile, level, name_='XSDataInputInterface'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputInterface'):
		pass
		if self._experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		if self._sample is not None:
			self.sample.export(outfile, level, name_='sample')
		for imagePath_ in self.getImagePath():
			imagePath_.export(outfile, level, name_='imagePath')
		if self._flux is not None:
			self.flux.export(outfile, level, name_='flux')
		if self._minExposureTimePerImage is not None:
			self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
		if self._beamSize is not None:
			self.beamSize.export(outfile, level, name_='beamSize')
		if self._beamSizeX is not None:
			self.beamSizeX.export(outfile, level, name_='beamSizeX')
		if self._beamSizeY is not None:
			self.beamSizeY.export(outfile, level, name_='beamSizeY')
		if self._templateMode is not None:
			self.templateMode.export(outfile, level, name_='templateMode')
		if self._generatedTemplateFile is not None:
			self.generatedTemplateFile.export(outfile, level, name_='generatedTemplateFile')
		if self._resultsFilePath is not None:
			self.resultsFilePath.export(outfile, level, name_='resultsFilePath')
		if self._beamPosX is not None:
			self.beamPosX.export(outfile, level, name_='beamPosX')
		if self._beamPosY is not None:
			self.beamPosY.export(outfile, level, name_='beamPosY')
		if self._wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self._dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		if self._shortComments is not None:
			self.shortComments.export(outfile, level, name_='shortComments')
		if self._comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self._inputCharacterisation is not None:
			self.inputCharacterisation.export(outfile, level, name_='inputCharacterisation')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSampleCrystalMM()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagePath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.imagePath.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flux':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setFlux(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minExposureTimePerImage':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setMinExposureTimePerImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSize':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamSize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamSizeX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamSizeY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamSizeY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'templateMode':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setTemplateMode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'generatedTemplateFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGeneratedTemplateFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultsFilePath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setResultsFilePath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPosX':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamPosX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamPosY':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamPosY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'shortComments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setShortComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputCharacterisation':
			obj_ = XSDataInputCharacterisation()
			obj_.build(child_)
			self.setInputCharacterisation(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputInterface" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputInterface' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputInterface is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputInterface.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputInterface()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputInterface" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputInterface()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputInterface

class XSDataResultInterface(object):
	def __init__(self, resultControlISPyB=None, resultCharacterisation=None):
	
	
		checkType("XSDataResultInterface", "Constructor of XSDataResultInterface", resultCharacterisation, "XSDataResultCharacterisation")
		self._resultCharacterisation = resultCharacterisation
		checkType("XSDataResultInterface", "Constructor of XSDataResultInterface", resultControlISPyB, "XSDataResultControlISPyB")
		self._resultControlISPyB = resultControlISPyB
	def getResultCharacterisation(self): return self._resultCharacterisation
	def setResultCharacterisation(self, resultCharacterisation):
		checkType("XSDataResultInterface", "setResultCharacterisation", resultCharacterisation, "XSDataResultCharacterisation")
		self._resultCharacterisation = resultCharacterisation
	def delResultCharacterisation(self): self._resultCharacterisation = None
	# Properties
	resultCharacterisation = property(getResultCharacterisation, setResultCharacterisation, delResultCharacterisation, "Property for resultCharacterisation")
	def getResultControlISPyB(self): return self._resultControlISPyB
	def setResultControlISPyB(self, resultControlISPyB):
		checkType("XSDataResultInterface", "setResultControlISPyB", resultControlISPyB, "XSDataResultControlISPyB")
		self._resultControlISPyB = resultControlISPyB
	def delResultControlISPyB(self): self._resultControlISPyB = None
	# Properties
	resultControlISPyB = property(getResultControlISPyB, setResultControlISPyB, delResultControlISPyB, "Property for resultControlISPyB")
	def export(self, outfile, level, name_='XSDataResultInterface'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultInterface'):
		pass
		if self._resultCharacterisation is not None:
			self.resultCharacterisation.export(outfile, level, name_='resultCharacterisation')
		if self._resultControlISPyB is not None:
			self.resultControlISPyB.export(outfile, level, name_='resultControlISPyB')
		else:
			warnEmptyAttribute("resultControlISPyB", "XSDataResultControlISPyB")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultCharacterisation':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setResultCharacterisation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultControlISPyB':
			obj_ = XSDataResultControlISPyB()
			obj_.build(child_)
			self.setResultControlISPyB(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultInterface" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultInterface' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultInterface is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultInterface.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultInterface()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultInterface" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultInterface()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultInterface



# End of data representation classes.



#!/usr/bin/env python

#
# Generated Mon Jun 27 04:13::52 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataSample
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataResultControlISPyB
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


class XSDataInputInterface(object):
	def __init__(self, inputCharacterisation=None, comments=None, shortComments=None, dataCollectionId=None, transmission=None, wavelength=None, beamPosY=None, beamPosX=None, resultsFilePath=None, generatedTemplateFile=None, templateMode=None, beamSizeY=None, beamSizeX=None, beamSize=None, minExposureTimePerImage=None, flux=None, imagePath=None, sample=None, diffractionPlan=None, experimentalCondition=None):
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", experimentalCondition, "XSDataExperimentalCondition")
		self.__experimentalCondition = experimentalCondition
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", diffractionPlan, "XSDataDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", sample, "XSDataSample")
		self.__sample = sample
		if imagePath is None:
			self.__imagePath = []
		else:
			checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", imagePath, "list")
			self.__imagePath = imagePath
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", flux, "XSDataFloat")
		self.__flux = flux
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", minExposureTimePerImage, "XSDataTime")
		self.__minExposureTimePerImage = minExposureTimePerImage
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSize, "XSDataLength")
		self.__beamSize = beamSize
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSizeX, "XSDataLength")
		self.__beamSizeX = beamSizeX
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamSizeY, "XSDataLength")
		self.__beamSizeY = beamSizeY
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", templateMode, "XSDataBoolean")
		self.__templateMode = templateMode
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", generatedTemplateFile, "XSDataFile")
		self.__generatedTemplateFile = generatedTemplateFile
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", resultsFilePath, "XSDataFile")
		self.__resultsFilePath = resultsFilePath
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamPosX, "XSDataFloat")
		self.__beamPosX = beamPosX
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", beamPosY, "XSDataFloat")
		self.__beamPosY = beamPosY
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", transmission, "XSDataDouble")
		self.__transmission = transmission
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", shortComments, "XSDataString")
		self.__shortComments = shortComments
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataInputInterface", "Constructor of XSDataInputInterface", inputCharacterisation, "XSDataInputCharacterisation")
		self.__inputCharacterisation = inputCharacterisation
	def getExperimentalCondition(self): return self.__experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataInputInterface", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self.__experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self.__experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getDiffractionPlan(self): return self.__diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputInterface", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self.__diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputInterface", "setSample", sample, "XSDataSample")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getImagePath(self): return self.__imagePath
	def setImagePath(self, imagePath):
		checkType("XSDataInputInterface", "setImagePath", imagePath, "list")
		self.__imagePath = imagePath
	def delImagePath(self): self.__imagePath = None
	# Properties
	imagePath = property(getImagePath, setImagePath, delImagePath, "Property for imagePath")
	def addImagePath(self, value):
		checkType("XSDataInputInterface", "setImagePath", value, "XSDataFile")
		self.__imagePath.append(value)
	def insertImagePath(self, index, value):
		checkType("XSDataInputInterface", "setImagePath", value, "XSDataFile")
		self.__imagePath[index] = value
	def getFlux(self): return self.__flux
	def setFlux(self, flux):
		checkType("XSDataInputInterface", "setFlux", flux, "XSDataFloat")
		self.__flux = flux
	def delFlux(self): self.__flux = None
	# Properties
	flux = property(getFlux, setFlux, delFlux, "Property for flux")
	def getMinExposureTimePerImage(self): return self.__minExposureTimePerImage
	def setMinExposureTimePerImage(self, minExposureTimePerImage):
		checkType("XSDataInputInterface", "setMinExposureTimePerImage", minExposureTimePerImage, "XSDataTime")
		self.__minExposureTimePerImage = minExposureTimePerImage
	def delMinExposureTimePerImage(self): self.__minExposureTimePerImage = None
	# Properties
	minExposureTimePerImage = property(getMinExposureTimePerImage, setMinExposureTimePerImage, delMinExposureTimePerImage, "Property for minExposureTimePerImage")
	def getBeamSize(self): return self.__beamSize
	def setBeamSize(self, beamSize):
		checkType("XSDataInputInterface", "setBeamSize", beamSize, "XSDataLength")
		self.__beamSize = beamSize
	def delBeamSize(self): self.__beamSize = None
	# Properties
	beamSize = property(getBeamSize, setBeamSize, delBeamSize, "Property for beamSize")
	def getBeamSizeX(self): return self.__beamSizeX
	def setBeamSizeX(self, beamSizeX):
		checkType("XSDataInputInterface", "setBeamSizeX", beamSizeX, "XSDataLength")
		self.__beamSizeX = beamSizeX
	def delBeamSizeX(self): self.__beamSizeX = None
	# Properties
	beamSizeX = property(getBeamSizeX, setBeamSizeX, delBeamSizeX, "Property for beamSizeX")
	def getBeamSizeY(self): return self.__beamSizeY
	def setBeamSizeY(self, beamSizeY):
		checkType("XSDataInputInterface", "setBeamSizeY", beamSizeY, "XSDataLength")
		self.__beamSizeY = beamSizeY
	def delBeamSizeY(self): self.__beamSizeY = None
	# Properties
	beamSizeY = property(getBeamSizeY, setBeamSizeY, delBeamSizeY, "Property for beamSizeY")
	def getTemplateMode(self): return self.__templateMode
	def setTemplateMode(self, templateMode):
		checkType("XSDataInputInterface", "setTemplateMode", templateMode, "XSDataBoolean")
		self.__templateMode = templateMode
	def delTemplateMode(self): self.__templateMode = None
	# Properties
	templateMode = property(getTemplateMode, setTemplateMode, delTemplateMode, "Property for templateMode")
	def getGeneratedTemplateFile(self): return self.__generatedTemplateFile
	def setGeneratedTemplateFile(self, generatedTemplateFile):
		checkType("XSDataInputInterface", "setGeneratedTemplateFile", generatedTemplateFile, "XSDataFile")
		self.__generatedTemplateFile = generatedTemplateFile
	def delGeneratedTemplateFile(self): self.__generatedTemplateFile = None
	# Properties
	generatedTemplateFile = property(getGeneratedTemplateFile, setGeneratedTemplateFile, delGeneratedTemplateFile, "Property for generatedTemplateFile")
	def getResultsFilePath(self): return self.__resultsFilePath
	def setResultsFilePath(self, resultsFilePath):
		checkType("XSDataInputInterface", "setResultsFilePath", resultsFilePath, "XSDataFile")
		self.__resultsFilePath = resultsFilePath
	def delResultsFilePath(self): self.__resultsFilePath = None
	# Properties
	resultsFilePath = property(getResultsFilePath, setResultsFilePath, delResultsFilePath, "Property for resultsFilePath")
	def getBeamPosX(self): return self.__beamPosX
	def setBeamPosX(self, beamPosX):
		checkType("XSDataInputInterface", "setBeamPosX", beamPosX, "XSDataFloat")
		self.__beamPosX = beamPosX
	def delBeamPosX(self): self.__beamPosX = None
	# Properties
	beamPosX = property(getBeamPosX, setBeamPosX, delBeamPosX, "Property for beamPosX")
	def getBeamPosY(self): return self.__beamPosY
	def setBeamPosY(self, beamPosY):
		checkType("XSDataInputInterface", "setBeamPosY", beamPosY, "XSDataFloat")
		self.__beamPosY = beamPosY
	def delBeamPosY(self): self.__beamPosY = None
	# Properties
	beamPosY = property(getBeamPosY, setBeamPosY, delBeamPosY, "Property for beamPosY")
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSDataInputInterface", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataInputInterface", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataInputInterface", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getShortComments(self): return self.__shortComments
	def setShortComments(self, shortComments):
		checkType("XSDataInputInterface", "setShortComments", shortComments, "XSDataString")
		self.__shortComments = shortComments
	def delShortComments(self): self.__shortComments = None
	# Properties
	shortComments = property(getShortComments, setShortComments, delShortComments, "Property for shortComments")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataInputInterface", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getInputCharacterisation(self): return self.__inputCharacterisation
	def setInputCharacterisation(self, inputCharacterisation):
		checkType("XSDataInputInterface", "setInputCharacterisation", inputCharacterisation, "XSDataInputCharacterisation")
		self.__inputCharacterisation = inputCharacterisation
	def delInputCharacterisation(self): self.__inputCharacterisation = None
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
		if self.__experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		if self.__diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		for imagePath_ in self.getImagePath():
			imagePath_.export(outfile, level, name_='imagePath')
		if self.__flux is not None:
			self.flux.export(outfile, level, name_='flux')
		if self.__minExposureTimePerImage is not None:
			self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
		if self.__beamSize is not None:
			self.beamSize.export(outfile, level, name_='beamSize')
		if self.__beamSizeX is not None:
			self.beamSizeX.export(outfile, level, name_='beamSizeX')
		if self.__beamSizeY is not None:
			self.beamSizeY.export(outfile, level, name_='beamSizeY')
		if self.__templateMode is not None:
			self.templateMode.export(outfile, level, name_='templateMode')
		if self.__generatedTemplateFile is not None:
			self.generatedTemplateFile.export(outfile, level, name_='generatedTemplateFile')
		if self.__resultsFilePath is not None:
			self.resultsFilePath.export(outfile, level, name_='resultsFilePath')
		if self.__beamPosX is not None:
			self.beamPosX.export(outfile, level, name_='beamPosX')
		if self.__beamPosY is not None:
			self.beamPosY.export(outfile, level, name_='beamPosY')
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		if self.__shortComments is not None:
			self.shortComments.export(outfile, level, name_='shortComments')
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		if self.__inputCharacterisation is not None:
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
			obj_ = XSDataSample()
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
		self.__resultCharacterisation = resultCharacterisation
		checkType("XSDataResultInterface", "Constructor of XSDataResultInterface", resultControlISPyB, "XSDataResultControlISPyB")
		self.__resultControlISPyB = resultControlISPyB
	def getResultCharacterisation(self): return self.__resultCharacterisation
	def setResultCharacterisation(self, resultCharacterisation):
		checkType("XSDataResultInterface", "setResultCharacterisation", resultCharacterisation, "XSDataResultCharacterisation")
		self.__resultCharacterisation = resultCharacterisation
	def delResultCharacterisation(self): self.__resultCharacterisation = None
	# Properties
	resultCharacterisation = property(getResultCharacterisation, setResultCharacterisation, delResultCharacterisation, "Property for resultCharacterisation")
	def getResultControlISPyB(self): return self.__resultControlISPyB
	def setResultControlISPyB(self, resultControlISPyB):
		checkType("XSDataResultInterface", "setResultControlISPyB", resultControlISPyB, "XSDataResultControlISPyB")
		self.__resultControlISPyB = resultControlISPyB
	def delResultControlISPyB(self): self.__resultControlISPyB = None
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
		if self.__resultCharacterisation is not None:
			self.resultCharacterisation.export(outfile, level, name_='resultCharacterisation')
		if self.__resultControlISPyB is not None:
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



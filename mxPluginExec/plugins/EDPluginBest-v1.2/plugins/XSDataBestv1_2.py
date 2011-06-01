#!/usr/bin/env python

#
# Generated Fri May 6 11:59::15 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataAbsorbedDoseRate
from XSDataCommon import XSDataAngularSpeed
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime




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


class XSDataBestCollectionRun(object):
	def __init__(self, transmission=None, phiWidth=None, phiStart=None, overlaps=None, numberOfImages=None, exposureTime=None, collectionRunNumber=None, action=None):
		self.__action = action
		self.__collectionRunNumber = collectionRunNumber
		self.__exposureTime = exposureTime
		self.__numberOfImages = numberOfImages
		self.__overlaps = overlaps
		self.__phiStart = phiStart
		self.__phiWidth = phiWidth
		self.__transmission = transmission
	def getAction(self): return self.__action
	def setAction(self, action):
		checkType("XSDataBestCollectionRun", "setAction", action, "XSDataString")
		self.__action = action
	def delAction(self): self.__action = None
	# Properties
	action = property(getAction, setAction, delAction, "Property for action")
	def getCollectionRunNumber(self): return self.__collectionRunNumber
	def setCollectionRunNumber(self, collectionRunNumber):
		checkType("XSDataBestCollectionRun", "setCollectionRunNumber", collectionRunNumber, "XSDataInteger")
		self.__collectionRunNumber = collectionRunNumber
	def delCollectionRunNumber(self): self.__collectionRunNumber = None
	# Properties
	collectionRunNumber = property(getCollectionRunNumber, setCollectionRunNumber, delCollectionRunNumber, "Property for collectionRunNumber")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataBestCollectionRun", "setExposureTime", exposureTime, "XSDataTime")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getNumberOfImages(self): return self.__numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataBestCollectionRun", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self.__numberOfImages = numberOfImages
	def delNumberOfImages(self): self.__numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getOverlaps(self): return self.__overlaps
	def setOverlaps(self, overlaps):
		checkType("XSDataBestCollectionRun", "setOverlaps", overlaps, "XSDataString")
		self.__overlaps = overlaps
	def delOverlaps(self): self.__overlaps = None
	# Properties
	overlaps = property(getOverlaps, setOverlaps, delOverlaps, "Property for overlaps")
	def getPhiStart(self): return self.__phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataBestCollectionRun", "setPhiStart", phiStart, "XSDataAngle")
		self.__phiStart = phiStart
	def delPhiStart(self): self.__phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getPhiWidth(self): return self.__phiWidth
	def setPhiWidth(self, phiWidth):
		checkType("XSDataBestCollectionRun", "setPhiWidth", phiWidth, "XSDataAngle")
		self.__phiWidth = phiWidth
	def delPhiWidth(self): self.__phiWidth = None
	# Properties
	phiWidth = property(getPhiWidth, setPhiWidth, delPhiWidth, "Property for phiWidth")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataBestCollectionRun", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def export(self, outfile, level, name_='XSDataBestCollectionRun'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBestCollectionRun'):
		pass
		if self.__action is not None:
			self.action.export(outfile, level, name_='action')
		else:
			warnEmptyAttribute("action", "XSDataString")
		if self.__collectionRunNumber is not None:
			self.collectionRunNumber.export(outfile, level, name_='collectionRunNumber')
		else:
			warnEmptyAttribute("collectionRunNumber", "XSDataInteger")
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataTime")
		if self.__numberOfImages is not None:
			self.numberOfImages.export(outfile, level, name_='numberOfImages')
		else:
			warnEmptyAttribute("numberOfImages", "XSDataInteger")
		if self.__overlaps is not None:
			self.overlaps.export(outfile, level, name_='overlaps')
		else:
			warnEmptyAttribute("overlaps", "XSDataString")
		if self.__phiStart is not None:
			self.phiStart.export(outfile, level, name_='phiStart')
		else:
			warnEmptyAttribute("phiStart", "XSDataAngle")
		if self.__phiWidth is not None:
			self.phiWidth.export(outfile, level, name_='phiWidth')
		else:
			warnEmptyAttribute("phiWidth", "XSDataAngle")
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		else:
			warnEmptyAttribute("transmission", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'action':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setAction(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionRunNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCollectionRunNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfImages':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfImages(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overlaps':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOverlaps(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhiStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhiWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBestCollectionRun" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestCollectionRun' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBestCollectionRun.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBestCollectionRun()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBestCollectionRun" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBestCollectionRun()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBestCollectionRun

class XSDataBestResolutionBin(object):
	def __init__(self, redundancy=None, rFriedel=None, rFactor=None, percentageOverload=None, minResolution=None, maxResolution=None, completeness=None, averageSigma=None, averageIntensityOverAverageSigma=None, averageIntensity=None, IOverSigma=None):
		self.__IOverSigma = IOverSigma
		self.__averageIntensity = averageIntensity
		self.__averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
		self.__averageSigma = averageSigma
		self.__completeness = completeness
		self.__maxResolution = maxResolution
		self.__minResolution = minResolution
		self.__percentageOverload = percentageOverload
		self.__rFactor = rFactor
		self.__rFriedel = rFriedel
		self.__redundancy = redundancy
	def getIOverSigma(self): return self.__IOverSigma
	def setIOverSigma(self, IOverSigma):
		checkType("XSDataBestResolutionBin", "setIOverSigma", IOverSigma, "XSDataDouble")
		self.__IOverSigma = IOverSigma
	def delIOverSigma(self): self.__IOverSigma = None
	# Properties
	IOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for IOverSigma")
	def getAverageIntensity(self): return self.__averageIntensity
	def setAverageIntensity(self, averageIntensity):
		checkType("XSDataBestResolutionBin", "setAverageIntensity", averageIntensity, "XSDataDouble")
		self.__averageIntensity = averageIntensity
	def delAverageIntensity(self): self.__averageIntensity = None
	# Properties
	averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
	def getAverageIntensityOverAverageSigma(self): return self.__averageIntensityOverAverageSigma
	def setAverageIntensityOverAverageSigma(self, averageIntensityOverAverageSigma):
		checkType("XSDataBestResolutionBin", "setAverageIntensityOverAverageSigma", averageIntensityOverAverageSigma, "XSDataDouble")
		self.__averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
	def delAverageIntensityOverAverageSigma(self): self.__averageIntensityOverAverageSigma = None
	# Properties
	averageIntensityOverAverageSigma = property(getAverageIntensityOverAverageSigma, setAverageIntensityOverAverageSigma, delAverageIntensityOverAverageSigma, "Property for averageIntensityOverAverageSigma")
	def getAverageSigma(self): return self.__averageSigma
	def setAverageSigma(self, averageSigma):
		checkType("XSDataBestResolutionBin", "setAverageSigma", averageSigma, "XSDataDouble")
		self.__averageSigma = averageSigma
	def delAverageSigma(self): self.__averageSigma = None
	# Properties
	averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataBestResolutionBin", "setCompleteness", completeness, "XSDataDouble")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMaxResolution(self): return self.__maxResolution
	def setMaxResolution(self, maxResolution):
		checkType("XSDataBestResolutionBin", "setMaxResolution", maxResolution, "XSDataDouble")
		self.__maxResolution = maxResolution
	def delMaxResolution(self): self.__maxResolution = None
	# Properties
	maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
	def getMinResolution(self): return self.__minResolution
	def setMinResolution(self, minResolution):
		checkType("XSDataBestResolutionBin", "setMinResolution", minResolution, "XSDataDouble")
		self.__minResolution = minResolution
	def delMinResolution(self): self.__minResolution = None
	# Properties
	minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
	def getPercentageOverload(self): return self.__percentageOverload
	def setPercentageOverload(self, percentageOverload):
		checkType("XSDataBestResolutionBin", "setPercentageOverload", percentageOverload, "XSDataDouble")
		self.__percentageOverload = percentageOverload
	def delPercentageOverload(self): self.__percentageOverload = None
	# Properties
	percentageOverload = property(getPercentageOverload, setPercentageOverload, delPercentageOverload, "Property for percentageOverload")
	def getRFactor(self): return self.__rFactor
	def setRFactor(self, rFactor):
		checkType("XSDataBestResolutionBin", "setRFactor", rFactor, "XSDataDouble")
		self.__rFactor = rFactor
	def delRFactor(self): self.__rFactor = None
	# Properties
	rFactor = property(getRFactor, setRFactor, delRFactor, "Property for rFactor")
	def getRFriedel(self): return self.__rFriedel
	def setRFriedel(self, rFriedel):
		checkType("XSDataBestResolutionBin", "setRFriedel", rFriedel, "XSDataDouble")
		self.__rFriedel = rFriedel
	def delRFriedel(self): self.__rFriedel = None
	# Properties
	rFriedel = property(getRFriedel, setRFriedel, delRFriedel, "Property for rFriedel")
	def getRedundancy(self): return self.__redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataBestResolutionBin", "setRedundancy", redundancy, "XSDataDouble")
		self.__redundancy = redundancy
	def delRedundancy(self): self.__redundancy = None
	# Properties
	redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
	def export(self, outfile, level, name_='XSDataBestResolutionBin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBestResolutionBin'):
		pass
		if self.__IOverSigma is not None:
			self.IOverSigma.export(outfile, level, name_='IOverSigma')
		else:
			warnEmptyAttribute("IOverSigma", "XSDataDouble")
		if self.__averageIntensity is not None:
			self.averageIntensity.export(outfile, level, name_='averageIntensity')
		else:
			warnEmptyAttribute("averageIntensity", "XSDataDouble")
		if self.__averageIntensityOverAverageSigma is not None:
			self.averageIntensityOverAverageSigma.export(outfile, level, name_='averageIntensityOverAverageSigma')
		else:
			warnEmptyAttribute("averageIntensityOverAverageSigma", "XSDataDouble")
		if self.__averageSigma is not None:
			self.averageSigma.export(outfile, level, name_='averageSigma')
		else:
			warnEmptyAttribute("averageSigma", "XSDataDouble")
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self.__maxResolution is not None:
			self.maxResolution.export(outfile, level, name_='maxResolution')
		else:
			warnEmptyAttribute("maxResolution", "XSDataDouble")
		if self.__minResolution is not None:
			self.minResolution.export(outfile, level, name_='minResolution')
		else:
			warnEmptyAttribute("minResolution", "XSDataDouble")
		if self.__percentageOverload is not None:
			self.percentageOverload.export(outfile, level, name_='percentageOverload')
		else:
			warnEmptyAttribute("percentageOverload", "XSDataDouble")
		if self.__rFactor is not None:
			self.rFactor.export(outfile, level, name_='rFactor')
		else:
			warnEmptyAttribute("rFactor", "XSDataDouble")
		if self.__rFriedel is not None:
			self.rFriedel.export(outfile, level, name_='rFriedel')
		else:
			warnEmptyAttribute("rFriedel", "XSDataDouble")
		if self.__redundancy is not None:
			self.redundancy.export(outfile, level, name_='redundancy')
		else:
			warnEmptyAttribute("redundancy", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'IOverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIntensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageIntensityOverAverageSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageIntensityOverAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'averageSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAverageSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMaxResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'percentageOverload':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPercentageOverload(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rFriedel':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRFriedel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'redundancy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRedundancy(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBestResolutionBin" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestResolutionBin' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBestResolutionBin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBestResolutionBin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBestResolutionBin" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBestResolutionBin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBestResolutionBin

class XSDataBestStatisticalPrediction(object):
	def __init__(self, resolutionBin=None):
		if resolutionBin is None:
			self.__resolutionBin = []
		else:
			self.__resolutionBin = resolutionBin
	def getResolutionBin(self): return self.__resolutionBin
	def setResolutionBin(self, resolutionBin):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", resolutionBin, "list")
		self.__resolutionBin = resolutionBin
	def delResolutionBin(self): self.__resolutionBin = None
	# Properties
	resolutionBin = property(getResolutionBin, setResolutionBin, delResolutionBin, "Property for resolutionBin")
	def addResolutionBin(self, value):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", value, "XSDataBestResolutionBin")
		self.__resolutionBin.append(value)
	def insertResolutionBin(self, index, value):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", value, "XSDataBestResolutionBin")
		self.__resolutionBin[index] = value
	def export(self, outfile, level, name_='XSDataBestStatisticalPrediction'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBestStatisticalPrediction'):
		pass
		for resolutionBin_ in self.getResolutionBin():
			resolutionBin_.export(outfile, level, name_='resolutionBin')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionBin':
			obj_ = XSDataBestResolutionBin()
			obj_.build(child_)
			self.resolutionBin.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBestStatisticalPrediction" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestStatisticalPrediction' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBestStatisticalPrediction.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBestStatisticalPrediction()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBestStatisticalPrediction" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBestStatisticalPrediction()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBestStatisticalPrediction

class XSDataBestStrategySummary(object):
	def __init__(self, transmission=None, totalExposureTime=None, totalDataCollectionTime=None, resolutionReasoning=None, resolution=None, redundancy=None, rankingResolution=None, iSigma=None, distance=None, completeness=None):
		self.__completeness = completeness
		self.__distance = distance
		self.__iSigma = iSigma
		self.__rankingResolution = rankingResolution
		self.__redundancy = redundancy
		self.__resolution = resolution
		self.__resolutionReasoning = resolutionReasoning
		self.__totalDataCollectionTime = totalDataCollectionTime
		self.__totalExposureTime = totalExposureTime
		self.__transmission = transmission
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataBestStrategySummary", "setCompleteness", completeness, "XSDataDouble")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getDistance(self): return self.__distance
	def setDistance(self, distance):
		checkType("XSDataBestStrategySummary", "setDistance", distance, "XSDataLength")
		self.__distance = distance
	def delDistance(self): self.__distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def getISigma(self): return self.__iSigma
	def setISigma(self, iSigma):
		checkType("XSDataBestStrategySummary", "setISigma", iSigma, "XSDataDouble")
		self.__iSigma = iSigma
	def delISigma(self): self.__iSigma = None
	# Properties
	iSigma = property(getISigma, setISigma, delISigma, "Property for iSigma")
	def getRankingResolution(self): return self.__rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataBestStrategySummary", "setRankingResolution", rankingResolution, "XSDataDouble")
		self.__rankingResolution = rankingResolution
	def delRankingResolution(self): self.__rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getRedundancy(self): return self.__redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataBestStrategySummary", "setRedundancy", redundancy, "XSDataDouble")
		self.__redundancy = redundancy
	def delRedundancy(self): self.__redundancy = None
	# Properties
	redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataBestStrategySummary", "setResolution", resolution, "XSDataDouble")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolutionReasoning(self): return self.__resolutionReasoning
	def setResolutionReasoning(self, resolutionReasoning):
		checkType("XSDataBestStrategySummary", "setResolutionReasoning", resolutionReasoning, "XSDataString")
		self.__resolutionReasoning = resolutionReasoning
	def delResolutionReasoning(self): self.__resolutionReasoning = None
	# Properties
	resolutionReasoning = property(getResolutionReasoning, setResolutionReasoning, delResolutionReasoning, "Property for resolutionReasoning")
	def getTotalDataCollectionTime(self): return self.__totalDataCollectionTime
	def setTotalDataCollectionTime(self, totalDataCollectionTime):
		checkType("XSDataBestStrategySummary", "setTotalDataCollectionTime", totalDataCollectionTime, "XSDataTime")
		self.__totalDataCollectionTime = totalDataCollectionTime
	def delTotalDataCollectionTime(self): self.__totalDataCollectionTime = None
	# Properties
	totalDataCollectionTime = property(getTotalDataCollectionTime, setTotalDataCollectionTime, delTotalDataCollectionTime, "Property for totalDataCollectionTime")
	def getTotalExposureTime(self): return self.__totalExposureTime
	def setTotalExposureTime(self, totalExposureTime):
		checkType("XSDataBestStrategySummary", "setTotalExposureTime", totalExposureTime, "XSDataTime")
		self.__totalExposureTime = totalExposureTime
	def delTotalExposureTime(self): self.__totalExposureTime = None
	# Properties
	totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataBestStrategySummary", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def export(self, outfile, level, name_='XSDataBestStrategySummary'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBestStrategySummary'):
		pass
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self.__distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
		if self.__iSigma is not None:
			self.iSigma.export(outfile, level, name_='iSigma')
		else:
			warnEmptyAttribute("iSigma", "XSDataDouble")
		if self.__rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		else:
			warnEmptyAttribute("rankingResolution", "XSDataDouble")
		if self.__redundancy is not None:
			self.redundancy.export(outfile, level, name_='redundancy')
		else:
			warnEmptyAttribute("redundancy", "XSDataDouble")
		if self.__resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self.__resolutionReasoning is not None:
			self.resolutionReasoning.export(outfile, level, name_='resolutionReasoning')
		else:
			warnEmptyAttribute("resolutionReasoning", "XSDataString")
		if self.__totalDataCollectionTime is not None:
			self.totalDataCollectionTime.export(outfile, level, name_='totalDataCollectionTime')
		else:
			warnEmptyAttribute("totalDataCollectionTime", "XSDataTime")
		if self.__totalExposureTime is not None:
			self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
		else:
			warnEmptyAttribute("totalExposureTime", "XSDataTime")
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		else:
			warnEmptyAttribute("transmission", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setISigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRankingResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'redundancy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRedundancy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionReasoning':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setResolutionReasoning(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'totalDataCollectionTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTotalDataCollectionTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'totalExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setTotalExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBestStrategySummary" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestStrategySummary' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBestStrategySummary.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBestStrategySummary()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBestStrategySummary" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBestStrategySummary()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBestStrategySummary

class XSDataCrystalScale(object):
	def __init__(self, scale=None, bFactor=None):
		self.__bFactor = bFactor
		self.__scale = scale
	def getBFactor(self): return self.__bFactor
	def setBFactor(self, bFactor):
		checkType("XSDataCrystalScale", "setBFactor", bFactor, "XSDataDouble")
		self.__bFactor = bFactor
	def delBFactor(self): self.__bFactor = None
	# Properties
	bFactor = property(getBFactor, setBFactor, delBFactor, "Property for bFactor")
	def getScale(self): return self.__scale
	def setScale(self, scale):
		checkType("XSDataCrystalScale", "setScale", scale, "XSDataDouble")
		self.__scale = scale
	def delScale(self): self.__scale = None
	# Properties
	scale = property(getScale, setScale, delScale, "Property for scale")
	def export(self, outfile, level, name_='XSDataCrystalScale'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCrystalScale'):
		pass
		if self.__bFactor is not None:
			self.bFactor.export(outfile, level, name_='bFactor')
		else:
			warnEmptyAttribute("bFactor", "XSDataDouble")
		if self.__scale is not None:
			self.scale.export(outfile, level, name_='scale')
		else:
			warnEmptyAttribute("scale", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scale':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setScale(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCrystalScale" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCrystalScale' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCrystalScale.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCrystalScale()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCrystalScale" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCrystalScale()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCrystalScale

class XSDataBestCollectionPlan(object):
	def __init__(self, strategySummary=None, statisticalPrediction=None, crystalScale=None, comment=None, collectionRun=None, collectionPlanNumber=None):
		self.__collectionPlanNumber = collectionPlanNumber
		if collectionRun is None:
			self.__collectionRun = []
		else:
			self.__collectionRun = collectionRun
		self.__comment = comment
		self.__crystalScale = crystalScale
		self.__statisticalPrediction = statisticalPrediction
		self.__strategySummary = strategySummary
	def getCollectionPlanNumber(self): return self.__collectionPlanNumber
	def setCollectionPlanNumber(self, collectionPlanNumber):
		checkType("XSDataBestCollectionPlan", "setCollectionPlanNumber", collectionPlanNumber, "XSDataInteger")
		self.__collectionPlanNumber = collectionPlanNumber
	def delCollectionPlanNumber(self): self.__collectionPlanNumber = None
	# Properties
	collectionPlanNumber = property(getCollectionPlanNumber, setCollectionPlanNumber, delCollectionPlanNumber, "Property for collectionPlanNumber")
	def getCollectionRun(self): return self.__collectionRun
	def setCollectionRun(self, collectionRun):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", collectionRun, "list")
		self.__collectionRun = collectionRun
	def delCollectionRun(self): self.__collectionRun = None
	# Properties
	collectionRun = property(getCollectionRun, setCollectionRun, delCollectionRun, "Property for collectionRun")
	def addCollectionRun(self, value):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", value, "XSDataBestCollectionRun")
		self.__collectionRun.append(value)
	def insertCollectionRun(self, index, value):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", value, "XSDataBestCollectionRun")
		self.__collectionRun[index] = value
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("XSDataBestCollectionPlan", "setComment", comment, "XSDataString")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getCrystalScale(self): return self.__crystalScale
	def setCrystalScale(self, crystalScale):
		checkType("XSDataBestCollectionPlan", "setCrystalScale", crystalScale, "XSDataCrystalScale")
		self.__crystalScale = crystalScale
	def delCrystalScale(self): self.__crystalScale = None
	# Properties
	crystalScale = property(getCrystalScale, setCrystalScale, delCrystalScale, "Property for crystalScale")
	def getStatisticalPrediction(self): return self.__statisticalPrediction
	def setStatisticalPrediction(self, statisticalPrediction):
		checkType("XSDataBestCollectionPlan", "setStatisticalPrediction", statisticalPrediction, "XSDataBestStatisticalPrediction")
		self.__statisticalPrediction = statisticalPrediction
	def delStatisticalPrediction(self): self.__statisticalPrediction = None
	# Properties
	statisticalPrediction = property(getStatisticalPrediction, setStatisticalPrediction, delStatisticalPrediction, "Property for statisticalPrediction")
	def getStrategySummary(self): return self.__strategySummary
	def setStrategySummary(self, strategySummary):
		checkType("XSDataBestCollectionPlan", "setStrategySummary", strategySummary, "XSDataBestStrategySummary")
		self.__strategySummary = strategySummary
	def delStrategySummary(self): self.__strategySummary = None
	# Properties
	strategySummary = property(getStrategySummary, setStrategySummary, delStrategySummary, "Property for strategySummary")
	def export(self, outfile, level, name_='XSDataBestCollectionPlan'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataBestCollectionPlan'):
		pass
		if self.__collectionPlanNumber is not None:
			self.collectionPlanNumber.export(outfile, level, name_='collectionPlanNumber')
		else:
			warnEmptyAttribute("collectionPlanNumber", "XSDataInteger")
		for collectionRun_ in self.getCollectionRun():
			collectionRun_.export(outfile, level, name_='collectionRun')
		if self.__comment is not None:
			self.comment.export(outfile, level, name_='comment')
		else:
			warnEmptyAttribute("comment", "XSDataString")
		if self.__crystalScale is not None:
			self.crystalScale.export(outfile, level, name_='crystalScale')
		else:
			warnEmptyAttribute("crystalScale", "XSDataCrystalScale")
		if self.__statisticalPrediction is not None:
			self.statisticalPrediction.export(outfile, level, name_='statisticalPrediction')
		else:
			warnEmptyAttribute("statisticalPrediction", "XSDataBestStatisticalPrediction")
		if self.__strategySummary is not None:
			self.strategySummary.export(outfile, level, name_='strategySummary')
		else:
			warnEmptyAttribute("strategySummary", "XSDataBestStrategySummary")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlanNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCollectionPlanNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionRun':
			obj_ = XSDataBestCollectionRun()
			obj_.build(child_)
			self.collectionRun.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComment(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalScale':
			obj_ = XSDataCrystalScale()
			obj_.build(child_)
			self.setCrystalScale(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statisticalPrediction':
			obj_ = XSDataBestStatisticalPrediction()
			obj_.build(child_)
			self.setStatisticalPrediction(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategySummary':
			obj_ = XSDataBestStrategySummary()
			obj_.build(child_)
			self.setStrategySummary(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataBestCollectionPlan" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestCollectionPlan' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataBestCollectionPlan.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataBestCollectionPlan()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataBestCollectionPlan" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataBestCollectionPlan()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataBestCollectionPlan

class XSDataInputBest(XSDataInput):
	"""- anomalousData is deprecated, please use strategyOption instead.

- minTransmission will work only with version v3.4 or higher of Best

- xdsBackgroundFile will only work with version v3.4.1 or higher of Best

- detectorDistanceMin and detectorDistanceMax (in mm) will work only with version v3.4.3 or higher of Best
"""
	def __init__(self, configuration=None, xdsBackgroundImage=None, transmission=None, strategyOption=None, numberOfCrystalPositions=None, minTransmission=None, goniostatMinRotationWidth=None, goniostatMaxRotationSpeed=None, detectorType=None, detectorDistanceMin=None, detectorDistanceMax=None, crystalSusceptibility=None, crystalShape=None, crystalAbsorbedDoseRate=None, complexity=None, bestFileContentPar=None, bestFileContentHKL=None, bestFileContentDat=None, beamMinExposureTime=None, beamMaxExposureTime=None, beamExposureTime=None, anomalousData=None, aimedResolution=None, aimedRedundancy=None, aimedIOverSigma=None, aimedCompleteness=None):
		XSDataInput.__init__(self, configuration)
		self.__aimedCompleteness = aimedCompleteness
		self.__aimedIOverSigma = aimedIOverSigma
		self.__aimedRedundancy = aimedRedundancy
		self.__aimedResolution = aimedResolution
		self.__anomalousData = anomalousData
		self.__beamExposureTime = beamExposureTime
		self.__beamMaxExposureTime = beamMaxExposureTime
		self.__beamMinExposureTime = beamMinExposureTime
		self.__bestFileContentDat = bestFileContentDat
		if bestFileContentHKL is None:
			self.__bestFileContentHKL = []
		else:
			self.__bestFileContentHKL = bestFileContentHKL
		self.__bestFileContentPar = bestFileContentPar
		self.__complexity = complexity
		self.__crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
		self.__crystalShape = crystalShape
		self.__crystalSusceptibility = crystalSusceptibility
		self.__detectorDistanceMax = detectorDistanceMax
		self.__detectorDistanceMin = detectorDistanceMin
		self.__detectorType = detectorType
		self.__goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
		self.__goniostatMinRotationWidth = goniostatMinRotationWidth
		self.__minTransmission = minTransmission
		self.__numberOfCrystalPositions = numberOfCrystalPositions
		self.__strategyOption = strategyOption
		self.__transmission = transmission
		self.__xdsBackgroundImage = xdsBackgroundImage
	def getAimedCompleteness(self): return self.__aimedCompleteness
	def setAimedCompleteness(self, aimedCompleteness):
		checkType("XSDataInputBest", "setAimedCompleteness", aimedCompleteness, "XSDataDouble")
		self.__aimedCompleteness = aimedCompleteness
	def delAimedCompleteness(self): self.__aimedCompleteness = None
	# Properties
	aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
	def getAimedIOverSigma(self): return self.__aimedIOverSigma
	def setAimedIOverSigma(self, aimedIOverSigma):
		checkType("XSDataInputBest", "setAimedIOverSigma", aimedIOverSigma, "XSDataDouble")
		self.__aimedIOverSigma = aimedIOverSigma
	def delAimedIOverSigma(self): self.__aimedIOverSigma = None
	# Properties
	aimedIOverSigma = property(getAimedIOverSigma, setAimedIOverSigma, delAimedIOverSigma, "Property for aimedIOverSigma")
	def getAimedRedundancy(self): return self.__aimedRedundancy
	def setAimedRedundancy(self, aimedRedundancy):
		checkType("XSDataInputBest", "setAimedRedundancy", aimedRedundancy, "XSDataDouble")
		self.__aimedRedundancy = aimedRedundancy
	def delAimedRedundancy(self): self.__aimedRedundancy = None
	# Properties
	aimedRedundancy = property(getAimedRedundancy, setAimedRedundancy, delAimedRedundancy, "Property for aimedRedundancy")
	def getAimedResolution(self): return self.__aimedResolution
	def setAimedResolution(self, aimedResolution):
		checkType("XSDataInputBest", "setAimedResolution", aimedResolution, "XSDataDouble")
		self.__aimedResolution = aimedResolution
	def delAimedResolution(self): self.__aimedResolution = None
	# Properties
	aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
	def getAnomalousData(self): return self.__anomalousData
	def setAnomalousData(self, anomalousData):
		checkType("XSDataInputBest", "setAnomalousData", anomalousData, "XSDataBoolean")
		self.__anomalousData = anomalousData
	def delAnomalousData(self): self.__anomalousData = None
	# Properties
	anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
	def getBeamExposureTime(self): return self.__beamExposureTime
	def setBeamExposureTime(self, beamExposureTime):
		checkType("XSDataInputBest", "setBeamExposureTime", beamExposureTime, "XSDataTime")
		self.__beamExposureTime = beamExposureTime
	def delBeamExposureTime(self): self.__beamExposureTime = None
	# Properties
	beamExposureTime = property(getBeamExposureTime, setBeamExposureTime, delBeamExposureTime, "Property for beamExposureTime")
	def getBeamMaxExposureTime(self): return self.__beamMaxExposureTime
	def setBeamMaxExposureTime(self, beamMaxExposureTime):
		checkType("XSDataInputBest", "setBeamMaxExposureTime", beamMaxExposureTime, "XSDataTime")
		self.__beamMaxExposureTime = beamMaxExposureTime
	def delBeamMaxExposureTime(self): self.__beamMaxExposureTime = None
	# Properties
	beamMaxExposureTime = property(getBeamMaxExposureTime, setBeamMaxExposureTime, delBeamMaxExposureTime, "Property for beamMaxExposureTime")
	def getBeamMinExposureTime(self): return self.__beamMinExposureTime
	def setBeamMinExposureTime(self, beamMinExposureTime):
		checkType("XSDataInputBest", "setBeamMinExposureTime", beamMinExposureTime, "XSDataTime")
		self.__beamMinExposureTime = beamMinExposureTime
	def delBeamMinExposureTime(self): self.__beamMinExposureTime = None
	# Properties
	beamMinExposureTime = property(getBeamMinExposureTime, setBeamMinExposureTime, delBeamMinExposureTime, "Property for beamMinExposureTime")
	def getBestFileContentDat(self): return self.__bestFileContentDat
	def setBestFileContentDat(self, bestFileContentDat):
		checkType("XSDataInputBest", "setBestFileContentDat", bestFileContentDat, "XSDataString")
		self.__bestFileContentDat = bestFileContentDat
	def delBestFileContentDat(self): self.__bestFileContentDat = None
	# Properties
	bestFileContentDat = property(getBestFileContentDat, setBestFileContentDat, delBestFileContentDat, "Property for bestFileContentDat")
	def getBestFileContentHKL(self): return self.__bestFileContentHKL
	def setBestFileContentHKL(self, bestFileContentHKL):
		checkType("XSDataInputBest", "setBestFileContentHKL", bestFileContentHKL, "list")
		self.__bestFileContentHKL = bestFileContentHKL
	def delBestFileContentHKL(self): self.__bestFileContentHKL = None
	# Properties
	bestFileContentHKL = property(getBestFileContentHKL, setBestFileContentHKL, delBestFileContentHKL, "Property for bestFileContentHKL")
	def addBestFileContentHKL(self, value):
		checkType("XSDataInputBest", "setBestFileContentHKL", value, "XSDataString")
		self.__bestFileContentHKL.append(value)
	def insertBestFileContentHKL(self, index, value):
		checkType("XSDataInputBest", "setBestFileContentHKL", value, "XSDataString")
		self.__bestFileContentHKL[index] = value
	def getBestFileContentPar(self): return self.__bestFileContentPar
	def setBestFileContentPar(self, bestFileContentPar):
		checkType("XSDataInputBest", "setBestFileContentPar", bestFileContentPar, "XSDataString")
		self.__bestFileContentPar = bestFileContentPar
	def delBestFileContentPar(self): self.__bestFileContentPar = None
	# Properties
	bestFileContentPar = property(getBestFileContentPar, setBestFileContentPar, delBestFileContentPar, "Property for bestFileContentPar")
	def getComplexity(self): return self.__complexity
	def setComplexity(self, complexity):
		checkType("XSDataInputBest", "setComplexity", complexity, "XSDataString")
		self.__complexity = complexity
	def delComplexity(self): self.__complexity = None
	# Properties
	complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
	def getCrystalAbsorbedDoseRate(self): return self.__crystalAbsorbedDoseRate
	def setCrystalAbsorbedDoseRate(self, crystalAbsorbedDoseRate):
		checkType("XSDataInputBest", "setCrystalAbsorbedDoseRate", crystalAbsorbedDoseRate, "XSDataAbsorbedDoseRate")
		self.__crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
	def delCrystalAbsorbedDoseRate(self): self.__crystalAbsorbedDoseRate = None
	# Properties
	crystalAbsorbedDoseRate = property(getCrystalAbsorbedDoseRate, setCrystalAbsorbedDoseRate, delCrystalAbsorbedDoseRate, "Property for crystalAbsorbedDoseRate")
	def getCrystalShape(self): return self.__crystalShape
	def setCrystalShape(self, crystalShape):
		checkType("XSDataInputBest", "setCrystalShape", crystalShape, "XSDataDouble")
		self.__crystalShape = crystalShape
	def delCrystalShape(self): self.__crystalShape = None
	# Properties
	crystalShape = property(getCrystalShape, setCrystalShape, delCrystalShape, "Property for crystalShape")
	def getCrystalSusceptibility(self): return self.__crystalSusceptibility
	def setCrystalSusceptibility(self, crystalSusceptibility):
		checkType("XSDataInputBest", "setCrystalSusceptibility", crystalSusceptibility, "XSDataDouble")
		self.__crystalSusceptibility = crystalSusceptibility
	def delCrystalSusceptibility(self): self.__crystalSusceptibility = None
	# Properties
	crystalSusceptibility = property(getCrystalSusceptibility, setCrystalSusceptibility, delCrystalSusceptibility, "Property for crystalSusceptibility")
	def getDetectorDistanceMax(self): return self.__detectorDistanceMax
	def setDetectorDistanceMax(self, detectorDistanceMax):
		checkType("XSDataInputBest", "setDetectorDistanceMax", detectorDistanceMax, "XSDataLength")
		self.__detectorDistanceMax = detectorDistanceMax
	def delDetectorDistanceMax(self): self.__detectorDistanceMax = None
	# Properties
	detectorDistanceMax = property(getDetectorDistanceMax, setDetectorDistanceMax, delDetectorDistanceMax, "Property for detectorDistanceMax")
	def getDetectorDistanceMin(self): return self.__detectorDistanceMin
	def setDetectorDistanceMin(self, detectorDistanceMin):
		checkType("XSDataInputBest", "setDetectorDistanceMin", detectorDistanceMin, "XSDataLength")
		self.__detectorDistanceMin = detectorDistanceMin
	def delDetectorDistanceMin(self): self.__detectorDistanceMin = None
	# Properties
	detectorDistanceMin = property(getDetectorDistanceMin, setDetectorDistanceMin, delDetectorDistanceMin, "Property for detectorDistanceMin")
	def getDetectorType(self): return self.__detectorType
	def setDetectorType(self, detectorType):
		checkType("XSDataInputBest", "setDetectorType", detectorType, "XSDataString")
		self.__detectorType = detectorType
	def delDetectorType(self): self.__detectorType = None
	# Properties
	detectorType = property(getDetectorType, setDetectorType, delDetectorType, "Property for detectorType")
	def getGoniostatMaxRotationSpeed(self): return self.__goniostatMaxRotationSpeed
	def setGoniostatMaxRotationSpeed(self, goniostatMaxRotationSpeed):
		checkType("XSDataInputBest", "setGoniostatMaxRotationSpeed", goniostatMaxRotationSpeed, "XSDataAngularSpeed")
		self.__goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
	def delGoniostatMaxRotationSpeed(self): self.__goniostatMaxRotationSpeed = None
	# Properties
	goniostatMaxRotationSpeed = property(getGoniostatMaxRotationSpeed, setGoniostatMaxRotationSpeed, delGoniostatMaxRotationSpeed, "Property for goniostatMaxRotationSpeed")
	def getGoniostatMinRotationWidth(self): return self.__goniostatMinRotationWidth
	def setGoniostatMinRotationWidth(self, goniostatMinRotationWidth):
		checkType("XSDataInputBest", "setGoniostatMinRotationWidth", goniostatMinRotationWidth, "XSDataAngle")
		self.__goniostatMinRotationWidth = goniostatMinRotationWidth
	def delGoniostatMinRotationWidth(self): self.__goniostatMinRotationWidth = None
	# Properties
	goniostatMinRotationWidth = property(getGoniostatMinRotationWidth, setGoniostatMinRotationWidth, delGoniostatMinRotationWidth, "Property for goniostatMinRotationWidth")
	def getMinTransmission(self): return self.__minTransmission
	def setMinTransmission(self, minTransmission):
		checkType("XSDataInputBest", "setMinTransmission", minTransmission, "XSDataDouble")
		self.__minTransmission = minTransmission
	def delMinTransmission(self): self.__minTransmission = None
	# Properties
	minTransmission = property(getMinTransmission, setMinTransmission, delMinTransmission, "Property for minTransmission")
	def getNumberOfCrystalPositions(self): return self.__numberOfCrystalPositions
	def setNumberOfCrystalPositions(self, numberOfCrystalPositions):
		checkType("XSDataInputBest", "setNumberOfCrystalPositions", numberOfCrystalPositions, "XSDataInteger")
		self.__numberOfCrystalPositions = numberOfCrystalPositions
	def delNumberOfCrystalPositions(self): self.__numberOfCrystalPositions = None
	# Properties
	numberOfCrystalPositions = property(getNumberOfCrystalPositions, setNumberOfCrystalPositions, delNumberOfCrystalPositions, "Property for numberOfCrystalPositions")
	def getStrategyOption(self): return self.__strategyOption
	def setStrategyOption(self, strategyOption):
		checkType("XSDataInputBest", "setStrategyOption", strategyOption, "XSDataString")
		self.__strategyOption = strategyOption
	def delStrategyOption(self): self.__strategyOption = None
	# Properties
	strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataInputBest", "setTransmission", transmission, "XSDataDouble")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getXdsBackgroundImage(self): return self.__xdsBackgroundImage
	def setXdsBackgroundImage(self, xdsBackgroundImage):
		checkType("XSDataInputBest", "setXdsBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self.__xdsBackgroundImage = xdsBackgroundImage
	def delXdsBackgroundImage(self): self.__xdsBackgroundImage = None
	# Properties
	xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
	def export(self, outfile, level, name_='XSDataInputBest'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputBest'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__aimedCompleteness is not None:
			self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
		if self.__aimedIOverSigma is not None:
			self.aimedIOverSigma.export(outfile, level, name_='aimedIOverSigma')
		if self.__aimedRedundancy is not None:
			self.aimedRedundancy.export(outfile, level, name_='aimedRedundancy')
		if self.__aimedResolution is not None:
			self.aimedResolution.export(outfile, level, name_='aimedResolution')
		if self.__anomalousData is not None:
			self.anomalousData.export(outfile, level, name_='anomalousData')
		if self.__beamExposureTime is not None:
			self.beamExposureTime.export(outfile, level, name_='beamExposureTime')
		else:
			warnEmptyAttribute("beamExposureTime", "XSDataTime")
		if self.__beamMaxExposureTime is not None:
			self.beamMaxExposureTime.export(outfile, level, name_='beamMaxExposureTime')
		if self.__beamMinExposureTime is not None:
			self.beamMinExposureTime.export(outfile, level, name_='beamMinExposureTime')
		if self.__bestFileContentDat is not None:
			self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
		else:
			warnEmptyAttribute("bestFileContentDat", "XSDataString")
		for bestFileContentHKL_ in self.getBestFileContentHKL():
			bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
		if self.getBestFileContentHKL() == []:
			warnEmptyAttribute("bestFileContentHKL", "XSDataString")
		if self.__bestFileContentPar is not None:
			self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
		else:
			warnEmptyAttribute("bestFileContentPar", "XSDataString")
		if self.__complexity is not None:
			self.complexity.export(outfile, level, name_='complexity')
		if self.__crystalAbsorbedDoseRate is not None:
			self.crystalAbsorbedDoseRate.export(outfile, level, name_='crystalAbsorbedDoseRate')
		if self.__crystalShape is not None:
			self.crystalShape.export(outfile, level, name_='crystalShape')
		if self.__crystalSusceptibility is not None:
			self.crystalSusceptibility.export(outfile, level, name_='crystalSusceptibility')
		if self.__detectorDistanceMax is not None:
			self.detectorDistanceMax.export(outfile, level, name_='detectorDistanceMax')
		if self.__detectorDistanceMin is not None:
			self.detectorDistanceMin.export(outfile, level, name_='detectorDistanceMin')
		if self.__detectorType is not None:
			self.detectorType.export(outfile, level, name_='detectorType')
		else:
			warnEmptyAttribute("detectorType", "XSDataString")
		if self.__goniostatMaxRotationSpeed is not None:
			self.goniostatMaxRotationSpeed.export(outfile, level, name_='goniostatMaxRotationSpeed')
		if self.__goniostatMinRotationWidth is not None:
			self.goniostatMinRotationWidth.export(outfile, level, name_='goniostatMinRotationWidth')
		if self.__minTransmission is not None:
			self.minTransmission.export(outfile, level, name_='minTransmission')
		if self.__numberOfCrystalPositions is not None:
			self.numberOfCrystalPositions.export(outfile, level, name_='numberOfCrystalPositions')
		if self.__strategyOption is not None:
			self.strategyOption.export(outfile, level, name_='strategyOption')
		if self.__transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self.__xdsBackgroundImage is not None:
			self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedCompleteness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedIOverSigma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedRedundancy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedRedundancy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aimedResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAimedResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalousData':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAnomalousData(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setBeamExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamMaxExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setBeamMaxExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamMinExposureTime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setBeamMinExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentDat':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentDat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentHKL':
			obj_ = XSDataString()
			obj_.build(child_)
			self.bestFileContentHKL.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestFileContentPar':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBestFileContentPar(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'complexity':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComplexity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalAbsorbedDoseRate':
			obj_ = XSDataAbsorbedDoseRate()
			obj_.build(child_)
			self.setCrystalAbsorbedDoseRate(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalShape':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCrystalShape(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalSusceptibility':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCrystalSusceptibility(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistanceMax':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistanceMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorDistanceMin':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetectorDistanceMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetectorType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostatMaxRotationSpeed':
			obj_ = XSDataAngularSpeed()
			obj_.build(child_)
			self.setGoniostatMaxRotationSpeed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostatMinRotationWidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setGoniostatMinRotationWidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minTransmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMinTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfCrystalPositions':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfCrystalPositions(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strategyOption':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStrategyOption(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setTransmission(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xdsBackgroundImage':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setXdsBackgroundImage(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputBest" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBest' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputBest.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputBest()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputBest" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputBest()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputBest

class XSDataResultBest(XSDataResult):
	def __init__(self, status=None, pathToLogFile=None, collectionPlan=None):
		XSDataResult.__init__(self, status)
		if collectionPlan is None:
			self.__collectionPlan = []
		else:
			self.__collectionPlan = collectionPlan
		self.__pathToLogFile = pathToLogFile
	def getCollectionPlan(self): return self.__collectionPlan
	def setCollectionPlan(self, collectionPlan):
		checkType("XSDataResultBest", "setCollectionPlan", collectionPlan, "list")
		self.__collectionPlan = collectionPlan
	def delCollectionPlan(self): self.__collectionPlan = None
	# Properties
	collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
	def addCollectionPlan(self, value):
		checkType("XSDataResultBest", "setCollectionPlan", value, "XSDataBestCollectionPlan")
		self.__collectionPlan.append(value)
	def insertCollectionPlan(self, index, value):
		checkType("XSDataResultBest", "setCollectionPlan", value, "XSDataBestCollectionPlan")
		self.__collectionPlan[index] = value
	def getPathToLogFile(self): return self.__pathToLogFile
	def setPathToLogFile(self, pathToLogFile):
		checkType("XSDataResultBest", "setPathToLogFile", pathToLogFile, "XSDataFile")
		self.__pathToLogFile = pathToLogFile
	def delPathToLogFile(self): self.__pathToLogFile = None
	# Properties
	pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
	def export(self, outfile, level, name_='XSDataResultBest'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultBest'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for collectionPlan_ in self.getCollectionPlan():
			collectionPlan_.export(outfile, level, name_='collectionPlan')
		if self.__pathToLogFile is not None:
			self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
		else:
			warnEmptyAttribute("pathToLogFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlan':
			obj_ = XSDataBestCollectionPlan()
			obj_.build(child_)
			self.collectionPlan.append(obj_)
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
		self.export( oStreamString, 0, name_="XSDataResultBest" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBest' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultBest.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultBest()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultBest" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultBest()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultBest



# End of data representation classes.



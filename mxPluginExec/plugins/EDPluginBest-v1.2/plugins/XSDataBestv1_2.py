#!/usr/bin/env python

#
# Generated Wed Apr 25 10:17::26 2012 by EDGenerateDS.
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
}

try:
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


class XSDataBestCollectionRun(object):
	def __init__(self, transmission=None, phiWidth=None, phiStart=None, overlaps=None, numberOfImages=None, exposureTime=None, crystalPosition=None, collectionRunNumber=None, action=None):
	
	
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", action, "XSDataString")
		self._action = action
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", collectionRunNumber, "XSDataInteger")
		self._collectionRunNumber = collectionRunNumber
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", crystalPosition, "XSDataInteger")
		self._crystalPosition = crystalPosition
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", overlaps, "XSDataString")
		self._overlaps = overlaps
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", phiStart, "XSDataAngle")
		self._phiStart = phiStart
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", phiWidth, "XSDataAngle")
		self._phiWidth = phiWidth
		checkType("XSDataBestCollectionRun", "Constructor of XSDataBestCollectionRun", transmission, "XSDataDouble")
		self._transmission = transmission
	def getAction(self): return self._action
	def setAction(self, action):
		checkType("XSDataBestCollectionRun", "setAction", action, "XSDataString")
		self._action = action
	def delAction(self): self._action = None
	# Properties
	action = property(getAction, setAction, delAction, "Property for action")
	def getCollectionRunNumber(self): return self._collectionRunNumber
	def setCollectionRunNumber(self, collectionRunNumber):
		checkType("XSDataBestCollectionRun", "setCollectionRunNumber", collectionRunNumber, "XSDataInteger")
		self._collectionRunNumber = collectionRunNumber
	def delCollectionRunNumber(self): self._collectionRunNumber = None
	# Properties
	collectionRunNumber = property(getCollectionRunNumber, setCollectionRunNumber, delCollectionRunNumber, "Property for collectionRunNumber")
	def getCrystalPosition(self): return self._crystalPosition
	def setCrystalPosition(self, crystalPosition):
		checkType("XSDataBestCollectionRun", "setCrystalPosition", crystalPosition, "XSDataInteger")
		self._crystalPosition = crystalPosition
	def delCrystalPosition(self): self._crystalPosition = None
	# Properties
	crystalPosition = property(getCrystalPosition, setCrystalPosition, delCrystalPosition, "Property for crystalPosition")
	def getExposureTime(self): return self._exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataBestCollectionRun", "setExposureTime", exposureTime, "XSDataTime")
		self._exposureTime = exposureTime
	def delExposureTime(self): self._exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getNumberOfImages(self): return self._numberOfImages
	def setNumberOfImages(self, numberOfImages):
		checkType("XSDataBestCollectionRun", "setNumberOfImages", numberOfImages, "XSDataInteger")
		self._numberOfImages = numberOfImages
	def delNumberOfImages(self): self._numberOfImages = None
	# Properties
	numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
	def getOverlaps(self): return self._overlaps
	def setOverlaps(self, overlaps):
		checkType("XSDataBestCollectionRun", "setOverlaps", overlaps, "XSDataString")
		self._overlaps = overlaps
	def delOverlaps(self): self._overlaps = None
	# Properties
	overlaps = property(getOverlaps, setOverlaps, delOverlaps, "Property for overlaps")
	def getPhiStart(self): return self._phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataBestCollectionRun", "setPhiStart", phiStart, "XSDataAngle")
		self._phiStart = phiStart
	def delPhiStart(self): self._phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getPhiWidth(self): return self._phiWidth
	def setPhiWidth(self, phiWidth):
		checkType("XSDataBestCollectionRun", "setPhiWidth", phiWidth, "XSDataAngle")
		self._phiWidth = phiWidth
	def delPhiWidth(self): self._phiWidth = None
	# Properties
	phiWidth = property(getPhiWidth, setPhiWidth, delPhiWidth, "Property for phiWidth")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataBestCollectionRun", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
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
		if self._action is not None:
			self.action.export(outfile, level, name_='action')
		if self._collectionRunNumber is not None:
			self.collectionRunNumber.export(outfile, level, name_='collectionRunNumber')
		else:
			warnEmptyAttribute("collectionRunNumber", "XSDataInteger")
		if self._crystalPosition is not None:
			self.crystalPosition.export(outfile, level, name_='crystalPosition')
		if self._exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataTime")
		if self._numberOfImages is not None:
			self.numberOfImages.export(outfile, level, name_='numberOfImages')
		else:
			warnEmptyAttribute("numberOfImages", "XSDataInteger")
		if self._overlaps is not None:
			self.overlaps.export(outfile, level, name_='overlaps')
		if self._phiStart is not None:
			self.phiStart.export(outfile, level, name_='phiStart')
		else:
			warnEmptyAttribute("phiStart", "XSDataAngle")
		if self._phiWidth is not None:
			self.phiWidth.export(outfile, level, name_='phiWidth')
		else:
			warnEmptyAttribute("phiWidth", "XSDataAngle")
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
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
			nodeName_ == 'crystalPosition':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setCrystalPosition(obj_)
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestCollectionRun' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBestCollectionRun is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	
	
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", IOverSigma, "XSDataDouble")
		self._IOverSigma = IOverSigma
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", averageIntensityOverAverageSigma, "XSDataDouble")
		self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", minResolution, "XSDataDouble")
		self._minResolution = minResolution
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", percentageOverload, "XSDataDouble")
		self._percentageOverload = percentageOverload
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", rFactor, "XSDataDouble")
		self._rFactor = rFactor
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", rFriedel, "XSDataDouble")
		self._rFriedel = rFriedel
		checkType("XSDataBestResolutionBin", "Constructor of XSDataBestResolutionBin", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def getIOverSigma(self): return self._IOverSigma
	def setIOverSigma(self, IOverSigma):
		checkType("XSDataBestResolutionBin", "setIOverSigma", IOverSigma, "XSDataDouble")
		self._IOverSigma = IOverSigma
	def delIOverSigma(self): self._IOverSigma = None
	# Properties
	IOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for IOverSigma")
	def getAverageIntensity(self): return self._averageIntensity
	def setAverageIntensity(self, averageIntensity):
		checkType("XSDataBestResolutionBin", "setAverageIntensity", averageIntensity, "XSDataDouble")
		self._averageIntensity = averageIntensity
	def delAverageIntensity(self): self._averageIntensity = None
	# Properties
	averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
	def getAverageIntensityOverAverageSigma(self): return self._averageIntensityOverAverageSigma
	def setAverageIntensityOverAverageSigma(self, averageIntensityOverAverageSigma):
		checkType("XSDataBestResolutionBin", "setAverageIntensityOverAverageSigma", averageIntensityOverAverageSigma, "XSDataDouble")
		self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
	def delAverageIntensityOverAverageSigma(self): self._averageIntensityOverAverageSigma = None
	# Properties
	averageIntensityOverAverageSigma = property(getAverageIntensityOverAverageSigma, setAverageIntensityOverAverageSigma, delAverageIntensityOverAverageSigma, "Property for averageIntensityOverAverageSigma")
	def getAverageSigma(self): return self._averageSigma
	def setAverageSigma(self, averageSigma):
		checkType("XSDataBestResolutionBin", "setAverageSigma", averageSigma, "XSDataDouble")
		self._averageSigma = averageSigma
	def delAverageSigma(self): self._averageSigma = None
	# Properties
	averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataBestResolutionBin", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMaxResolution(self): return self._maxResolution
	def setMaxResolution(self, maxResolution):
		checkType("XSDataBestResolutionBin", "setMaxResolution", maxResolution, "XSDataDouble")
		self._maxResolution = maxResolution
	def delMaxResolution(self): self._maxResolution = None
	# Properties
	maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
	def getMinResolution(self): return self._minResolution
	def setMinResolution(self, minResolution):
		checkType("XSDataBestResolutionBin", "setMinResolution", minResolution, "XSDataDouble")
		self._minResolution = minResolution
	def delMinResolution(self): self._minResolution = None
	# Properties
	minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
	def getPercentageOverload(self): return self._percentageOverload
	def setPercentageOverload(self, percentageOverload):
		checkType("XSDataBestResolutionBin", "setPercentageOverload", percentageOverload, "XSDataDouble")
		self._percentageOverload = percentageOverload
	def delPercentageOverload(self): self._percentageOverload = None
	# Properties
	percentageOverload = property(getPercentageOverload, setPercentageOverload, delPercentageOverload, "Property for percentageOverload")
	def getRFactor(self): return self._rFactor
	def setRFactor(self, rFactor):
		checkType("XSDataBestResolutionBin", "setRFactor", rFactor, "XSDataDouble")
		self._rFactor = rFactor
	def delRFactor(self): self._rFactor = None
	# Properties
	rFactor = property(getRFactor, setRFactor, delRFactor, "Property for rFactor")
	def getRFriedel(self): return self._rFriedel
	def setRFriedel(self, rFriedel):
		checkType("XSDataBestResolutionBin", "setRFriedel", rFriedel, "XSDataDouble")
		self._rFriedel = rFriedel
	def delRFriedel(self): self._rFriedel = None
	# Properties
	rFriedel = property(getRFriedel, setRFriedel, delRFriedel, "Property for rFriedel")
	def getRedundancy(self): return self._redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataBestResolutionBin", "setRedundancy", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def delRedundancy(self): self._redundancy = None
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
		if self._IOverSigma is not None:
			self.IOverSigma.export(outfile, level, name_='IOverSigma')
		else:
			warnEmptyAttribute("IOverSigma", "XSDataDouble")
		if self._averageIntensity is not None:
			self.averageIntensity.export(outfile, level, name_='averageIntensity')
		else:
			warnEmptyAttribute("averageIntensity", "XSDataDouble")
		if self._averageIntensityOverAverageSigma is not None:
			self.averageIntensityOverAverageSigma.export(outfile, level, name_='averageIntensityOverAverageSigma')
		if self._averageSigma is not None:
			self.averageSigma.export(outfile, level, name_='averageSigma')
		else:
			warnEmptyAttribute("averageSigma", "XSDataDouble")
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataDouble")
		if self._maxResolution is not None:
			self.maxResolution.export(outfile, level, name_='maxResolution')
		else:
			warnEmptyAttribute("maxResolution", "XSDataDouble")
		if self._minResolution is not None:
			self.minResolution.export(outfile, level, name_='minResolution')
		else:
			warnEmptyAttribute("minResolution", "XSDataDouble")
		if self._percentageOverload is not None:
			self.percentageOverload.export(outfile, level, name_='percentageOverload')
		else:
			warnEmptyAttribute("percentageOverload", "XSDataDouble")
		if self._rFactor is not None:
			self.rFactor.export(outfile, level, name_='rFactor')
		else:
			warnEmptyAttribute("rFactor", "XSDataDouble")
		if self._rFriedel is not None:
			self.rFriedel.export(outfile, level, name_='rFriedel')
		if self._redundancy is not None:
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestResolutionBin' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBestResolutionBin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
			self._resolutionBin = []
		else:
			checkType("XSDataBestStatisticalPrediction", "Constructor of XSDataBestStatisticalPrediction", resolutionBin, "list")
			self._resolutionBin = resolutionBin
	def getResolutionBin(self): return self._resolutionBin
	def setResolutionBin(self, resolutionBin):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", resolutionBin, "list")
		self._resolutionBin = resolutionBin
	def delResolutionBin(self): self._resolutionBin = None
	# Properties
	resolutionBin = property(getResolutionBin, setResolutionBin, delResolutionBin, "Property for resolutionBin")
	def addResolutionBin(self, value):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", value, "XSDataBestResolutionBin")
		self._resolutionBin.append(value)
	def insertResolutionBin(self, index, value):
		checkType("XSDataBestStatisticalPrediction", "setResolutionBin", value, "XSDataBestResolutionBin")
		self._resolutionBin[index] = value
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestStatisticalPrediction' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBestStatisticalPrediction is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	
	
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", completeness, "XSDataDouble")
		self._completeness = completeness
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", distance, "XSDataLength")
		self._distance = distance
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", iSigma, "XSDataDouble")
		self._iSigma = iSigma
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", redundancy, "XSDataDouble")
		self._redundancy = redundancy
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", resolution, "XSDataDouble")
		self._resolution = resolution
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", resolutionReasoning, "XSDataString")
		self._resolutionReasoning = resolutionReasoning
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", totalDataCollectionTime, "XSDataTime")
		self._totalDataCollectionTime = totalDataCollectionTime
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", totalExposureTime, "XSDataTime")
		self._totalExposureTime = totalExposureTime
		checkType("XSDataBestStrategySummary", "Constructor of XSDataBestStrategySummary", transmission, "XSDataDouble")
		self._transmission = transmission
	def getCompleteness(self): return self._completeness
	def setCompleteness(self, completeness):
		checkType("XSDataBestStrategySummary", "setCompleteness", completeness, "XSDataDouble")
		self._completeness = completeness
	def delCompleteness(self): self._completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getDistance(self): return self._distance
	def setDistance(self, distance):
		checkType("XSDataBestStrategySummary", "setDistance", distance, "XSDataLength")
		self._distance = distance
	def delDistance(self): self._distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def getISigma(self): return self._iSigma
	def setISigma(self, iSigma):
		checkType("XSDataBestStrategySummary", "setISigma", iSigma, "XSDataDouble")
		self._iSigma = iSigma
	def delISigma(self): self._iSigma = None
	# Properties
	iSigma = property(getISigma, setISigma, delISigma, "Property for iSigma")
	def getRankingResolution(self): return self._rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataBestStrategySummary", "setRankingResolution", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
	def delRankingResolution(self): self._rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getRedundancy(self): return self._redundancy
	def setRedundancy(self, redundancy):
		checkType("XSDataBestStrategySummary", "setRedundancy", redundancy, "XSDataDouble")
		self._redundancy = redundancy
	def delRedundancy(self): self._redundancy = None
	# Properties
	redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
	def getResolution(self): return self._resolution
	def setResolution(self, resolution):
		checkType("XSDataBestStrategySummary", "setResolution", resolution, "XSDataDouble")
		self._resolution = resolution
	def delResolution(self): self._resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolutionReasoning(self): return self._resolutionReasoning
	def setResolutionReasoning(self, resolutionReasoning):
		checkType("XSDataBestStrategySummary", "setResolutionReasoning", resolutionReasoning, "XSDataString")
		self._resolutionReasoning = resolutionReasoning
	def delResolutionReasoning(self): self._resolutionReasoning = None
	# Properties
	resolutionReasoning = property(getResolutionReasoning, setResolutionReasoning, delResolutionReasoning, "Property for resolutionReasoning")
	def getTotalDataCollectionTime(self): return self._totalDataCollectionTime
	def setTotalDataCollectionTime(self, totalDataCollectionTime):
		checkType("XSDataBestStrategySummary", "setTotalDataCollectionTime", totalDataCollectionTime, "XSDataTime")
		self._totalDataCollectionTime = totalDataCollectionTime
	def delTotalDataCollectionTime(self): self._totalDataCollectionTime = None
	# Properties
	totalDataCollectionTime = property(getTotalDataCollectionTime, setTotalDataCollectionTime, delTotalDataCollectionTime, "Property for totalDataCollectionTime")
	def getTotalExposureTime(self): return self._totalExposureTime
	def setTotalExposureTime(self, totalExposureTime):
		checkType("XSDataBestStrategySummary", "setTotalExposureTime", totalExposureTime, "XSDataTime")
		self._totalExposureTime = totalExposureTime
	def delTotalExposureTime(self): self._totalExposureTime = None
	# Properties
	totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataBestStrategySummary", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
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
		if self._completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		if self._distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
		if self._iSigma is not None:
			self.iSigma.export(outfile, level, name_='iSigma')
		if self._rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		if self._redundancy is not None:
			self.redundancy.export(outfile, level, name_='redundancy')
		if self._resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataDouble")
		if self._resolutionReasoning is not None:
			self.resolutionReasoning.export(outfile, level, name_='resolutionReasoning')
		if self._totalDataCollectionTime is not None:
			self.totalDataCollectionTime.export(outfile, level, name_='totalDataCollectionTime')
		if self._totalExposureTime is not None:
			self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestStrategySummary' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBestStrategySummary is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	
	
		checkType("XSDataCrystalScale", "Constructor of XSDataCrystalScale", bFactor, "XSDataDouble")
		self._bFactor = bFactor
		checkType("XSDataCrystalScale", "Constructor of XSDataCrystalScale", scale, "XSDataDouble")
		self._scale = scale
	def getBFactor(self): return self._bFactor
	def setBFactor(self, bFactor):
		checkType("XSDataCrystalScale", "setBFactor", bFactor, "XSDataDouble")
		self._bFactor = bFactor
	def delBFactor(self): self._bFactor = None
	# Properties
	bFactor = property(getBFactor, setBFactor, delBFactor, "Property for bFactor")
	def getScale(self): return self._scale
	def setScale(self, scale):
		checkType("XSDataCrystalScale", "setScale", scale, "XSDataDouble")
		self._scale = scale
	def delScale(self): self._scale = None
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
		if self._bFactor is not None:
			self.bFactor.export(outfile, level, name_='bFactor')
		else:
			warnEmptyAttribute("bFactor", "XSDataDouble")
		if self._scale is not None:
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCrystalScale' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCrystalScale is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	
	
		checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", collectionPlanNumber, "XSDataInteger")
		self._collectionPlanNumber = collectionPlanNumber
		if collectionRun is None:
			self._collectionRun = []
		else:
			checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", collectionRun, "list")
			self._collectionRun = collectionRun
		checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", comment, "XSDataString")
		self._comment = comment
		checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", crystalScale, "XSDataCrystalScale")
		self._crystalScale = crystalScale
		checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", statisticalPrediction, "XSDataBestStatisticalPrediction")
		self._statisticalPrediction = statisticalPrediction
		checkType("XSDataBestCollectionPlan", "Constructor of XSDataBestCollectionPlan", strategySummary, "XSDataBestStrategySummary")
		self._strategySummary = strategySummary
	def getCollectionPlanNumber(self): return self._collectionPlanNumber
	def setCollectionPlanNumber(self, collectionPlanNumber):
		checkType("XSDataBestCollectionPlan", "setCollectionPlanNumber", collectionPlanNumber, "XSDataInteger")
		self._collectionPlanNumber = collectionPlanNumber
	def delCollectionPlanNumber(self): self._collectionPlanNumber = None
	# Properties
	collectionPlanNumber = property(getCollectionPlanNumber, setCollectionPlanNumber, delCollectionPlanNumber, "Property for collectionPlanNumber")
	def getCollectionRun(self): return self._collectionRun
	def setCollectionRun(self, collectionRun):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", collectionRun, "list")
		self._collectionRun = collectionRun
	def delCollectionRun(self): self._collectionRun = None
	# Properties
	collectionRun = property(getCollectionRun, setCollectionRun, delCollectionRun, "Property for collectionRun")
	def addCollectionRun(self, value):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", value, "XSDataBestCollectionRun")
		self._collectionRun.append(value)
	def insertCollectionRun(self, index, value):
		checkType("XSDataBestCollectionPlan", "setCollectionRun", value, "XSDataBestCollectionRun")
		self._collectionRun[index] = value
	def getComment(self): return self._comment
	def setComment(self, comment):
		checkType("XSDataBestCollectionPlan", "setComment", comment, "XSDataString")
		self._comment = comment
	def delComment(self): self._comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getCrystalScale(self): return self._crystalScale
	def setCrystalScale(self, crystalScale):
		checkType("XSDataBestCollectionPlan", "setCrystalScale", crystalScale, "XSDataCrystalScale")
		self._crystalScale = crystalScale
	def delCrystalScale(self): self._crystalScale = None
	# Properties
	crystalScale = property(getCrystalScale, setCrystalScale, delCrystalScale, "Property for crystalScale")
	def getStatisticalPrediction(self): return self._statisticalPrediction
	def setStatisticalPrediction(self, statisticalPrediction):
		checkType("XSDataBestCollectionPlan", "setStatisticalPrediction", statisticalPrediction, "XSDataBestStatisticalPrediction")
		self._statisticalPrediction = statisticalPrediction
	def delStatisticalPrediction(self): self._statisticalPrediction = None
	# Properties
	statisticalPrediction = property(getStatisticalPrediction, setStatisticalPrediction, delStatisticalPrediction, "Property for statisticalPrediction")
	def getStrategySummary(self): return self._strategySummary
	def setStrategySummary(self, strategySummary):
		checkType("XSDataBestCollectionPlan", "setStrategySummary", strategySummary, "XSDataBestStrategySummary")
		self._strategySummary = strategySummary
	def delStrategySummary(self): self._strategySummary = None
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
		if self._collectionPlanNumber is not None:
			self.collectionPlanNumber.export(outfile, level, name_='collectionPlanNumber')
		for collectionRun_ in self.getCollectionRun():
			collectionRun_.export(outfile, level, name_='collectionRun')
		if self._comment is not None:
			self.comment.export(outfile, level, name_='comment')
		if self._crystalScale is not None:
			self.crystalScale.export(outfile, level, name_='crystalScale')
		if self._statisticalPrediction is not None:
			self.statisticalPrediction.export(outfile, level, name_='statisticalPrediction')
		if self._strategySummary is not None:
			self.strategySummary.export(outfile, level, name_='strategySummary')
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataBestCollectionPlan' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataBestCollectionPlan is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	
	
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", aimedIOverSigma, "XSDataDouble")
		self._aimedIOverSigma = aimedIOverSigma
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", aimedRedundancy, "XSDataDouble")
		self._aimedRedundancy = aimedRedundancy
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", beamExposureTime, "XSDataTime")
		self._beamExposureTime = beamExposureTime
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", beamMaxExposureTime, "XSDataTime")
		self._beamMaxExposureTime = beamMaxExposureTime
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", beamMinExposureTime, "XSDataTime")
		self._beamMinExposureTime = beamMinExposureTime
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
		if bestFileContentHKL is None:
			self._bestFileContentHKL = []
		else:
			checkType("XSDataInputBest", "Constructor of XSDataInputBest", bestFileContentHKL, "list")
			self._bestFileContentHKL = bestFileContentHKL
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", complexity, "XSDataString")
		self._complexity = complexity
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", crystalAbsorbedDoseRate, "XSDataAbsorbedDoseRate")
		self._crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", crystalShape, "XSDataDouble")
		self._crystalShape = crystalShape
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", crystalSusceptibility, "XSDataDouble")
		self._crystalSusceptibility = crystalSusceptibility
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", detectorDistanceMax, "XSDataLength")
		self._detectorDistanceMax = detectorDistanceMax
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", detectorDistanceMin, "XSDataLength")
		self._detectorDistanceMin = detectorDistanceMin
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", detectorType, "XSDataString")
		self._detectorType = detectorType
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", goniostatMaxRotationSpeed, "XSDataAngularSpeed")
		self._goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", goniostatMinRotationWidth, "XSDataAngle")
		self._goniostatMinRotationWidth = goniostatMinRotationWidth
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", minTransmission, "XSDataDouble")
		self._minTransmission = minTransmission
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", numberOfCrystalPositions, "XSDataInteger")
		self._numberOfCrystalPositions = numberOfCrystalPositions
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", transmission, "XSDataDouble")
		self._transmission = transmission
		checkType("XSDataInputBest", "Constructor of XSDataInputBest", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def getAimedCompleteness(self): return self._aimedCompleteness
	def setAimedCompleteness(self, aimedCompleteness):
		checkType("XSDataInputBest", "setAimedCompleteness", aimedCompleteness, "XSDataDouble")
		self._aimedCompleteness = aimedCompleteness
	def delAimedCompleteness(self): self._aimedCompleteness = None
	# Properties
	aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
	def getAimedIOverSigma(self): return self._aimedIOverSigma
	def setAimedIOverSigma(self, aimedIOverSigma):
		checkType("XSDataInputBest", "setAimedIOverSigma", aimedIOverSigma, "XSDataDouble")
		self._aimedIOverSigma = aimedIOverSigma
	def delAimedIOverSigma(self): self._aimedIOverSigma = None
	# Properties
	aimedIOverSigma = property(getAimedIOverSigma, setAimedIOverSigma, delAimedIOverSigma, "Property for aimedIOverSigma")
	def getAimedRedundancy(self): return self._aimedRedundancy
	def setAimedRedundancy(self, aimedRedundancy):
		checkType("XSDataInputBest", "setAimedRedundancy", aimedRedundancy, "XSDataDouble")
		self._aimedRedundancy = aimedRedundancy
	def delAimedRedundancy(self): self._aimedRedundancy = None
	# Properties
	aimedRedundancy = property(getAimedRedundancy, setAimedRedundancy, delAimedRedundancy, "Property for aimedRedundancy")
	def getAimedResolution(self): return self._aimedResolution
	def setAimedResolution(self, aimedResolution):
		checkType("XSDataInputBest", "setAimedResolution", aimedResolution, "XSDataDouble")
		self._aimedResolution = aimedResolution
	def delAimedResolution(self): self._aimedResolution = None
	# Properties
	aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
	def getAnomalousData(self): return self._anomalousData
	def setAnomalousData(self, anomalousData):
		checkType("XSDataInputBest", "setAnomalousData", anomalousData, "XSDataBoolean")
		self._anomalousData = anomalousData
	def delAnomalousData(self): self._anomalousData = None
	# Properties
	anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
	def getBeamExposureTime(self): return self._beamExposureTime
	def setBeamExposureTime(self, beamExposureTime):
		checkType("XSDataInputBest", "setBeamExposureTime", beamExposureTime, "XSDataTime")
		self._beamExposureTime = beamExposureTime
	def delBeamExposureTime(self): self._beamExposureTime = None
	# Properties
	beamExposureTime = property(getBeamExposureTime, setBeamExposureTime, delBeamExposureTime, "Property for beamExposureTime")
	def getBeamMaxExposureTime(self): return self._beamMaxExposureTime
	def setBeamMaxExposureTime(self, beamMaxExposureTime):
		checkType("XSDataInputBest", "setBeamMaxExposureTime", beamMaxExposureTime, "XSDataTime")
		self._beamMaxExposureTime = beamMaxExposureTime
	def delBeamMaxExposureTime(self): self._beamMaxExposureTime = None
	# Properties
	beamMaxExposureTime = property(getBeamMaxExposureTime, setBeamMaxExposureTime, delBeamMaxExposureTime, "Property for beamMaxExposureTime")
	def getBeamMinExposureTime(self): return self._beamMinExposureTime
	def setBeamMinExposureTime(self, beamMinExposureTime):
		checkType("XSDataInputBest", "setBeamMinExposureTime", beamMinExposureTime, "XSDataTime")
		self._beamMinExposureTime = beamMinExposureTime
	def delBeamMinExposureTime(self): self._beamMinExposureTime = None
	# Properties
	beamMinExposureTime = property(getBeamMinExposureTime, setBeamMinExposureTime, delBeamMinExposureTime, "Property for beamMinExposureTime")
	def getBestFileContentDat(self): return self._bestFileContentDat
	def setBestFileContentDat(self, bestFileContentDat):
		checkType("XSDataInputBest", "setBestFileContentDat", bestFileContentDat, "XSDataString")
		self._bestFileContentDat = bestFileContentDat
	def delBestFileContentDat(self): self._bestFileContentDat = None
	# Properties
	bestFileContentDat = property(getBestFileContentDat, setBestFileContentDat, delBestFileContentDat, "Property for bestFileContentDat")
	def getBestFileContentHKL(self): return self._bestFileContentHKL
	def setBestFileContentHKL(self, bestFileContentHKL):
		checkType("XSDataInputBest", "setBestFileContentHKL", bestFileContentHKL, "list")
		self._bestFileContentHKL = bestFileContentHKL
	def delBestFileContentHKL(self): self._bestFileContentHKL = None
	# Properties
	bestFileContentHKL = property(getBestFileContentHKL, setBestFileContentHKL, delBestFileContentHKL, "Property for bestFileContentHKL")
	def addBestFileContentHKL(self, value):
		checkType("XSDataInputBest", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL.append(value)
	def insertBestFileContentHKL(self, index, value):
		checkType("XSDataInputBest", "setBestFileContentHKL", value, "XSDataString")
		self._bestFileContentHKL[index] = value
	def getBestFileContentPar(self): return self._bestFileContentPar
	def setBestFileContentPar(self, bestFileContentPar):
		checkType("XSDataInputBest", "setBestFileContentPar", bestFileContentPar, "XSDataString")
		self._bestFileContentPar = bestFileContentPar
	def delBestFileContentPar(self): self._bestFileContentPar = None
	# Properties
	bestFileContentPar = property(getBestFileContentPar, setBestFileContentPar, delBestFileContentPar, "Property for bestFileContentPar")
	def getComplexity(self): return self._complexity
	def setComplexity(self, complexity):
		checkType("XSDataInputBest", "setComplexity", complexity, "XSDataString")
		self._complexity = complexity
	def delComplexity(self): self._complexity = None
	# Properties
	complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
	def getCrystalAbsorbedDoseRate(self): return self._crystalAbsorbedDoseRate
	def setCrystalAbsorbedDoseRate(self, crystalAbsorbedDoseRate):
		checkType("XSDataInputBest", "setCrystalAbsorbedDoseRate", crystalAbsorbedDoseRate, "XSDataAbsorbedDoseRate")
		self._crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
	def delCrystalAbsorbedDoseRate(self): self._crystalAbsorbedDoseRate = None
	# Properties
	crystalAbsorbedDoseRate = property(getCrystalAbsorbedDoseRate, setCrystalAbsorbedDoseRate, delCrystalAbsorbedDoseRate, "Property for crystalAbsorbedDoseRate")
	def getCrystalShape(self): return self._crystalShape
	def setCrystalShape(self, crystalShape):
		checkType("XSDataInputBest", "setCrystalShape", crystalShape, "XSDataDouble")
		self._crystalShape = crystalShape
	def delCrystalShape(self): self._crystalShape = None
	# Properties
	crystalShape = property(getCrystalShape, setCrystalShape, delCrystalShape, "Property for crystalShape")
	def getCrystalSusceptibility(self): return self._crystalSusceptibility
	def setCrystalSusceptibility(self, crystalSusceptibility):
		checkType("XSDataInputBest", "setCrystalSusceptibility", crystalSusceptibility, "XSDataDouble")
		self._crystalSusceptibility = crystalSusceptibility
	def delCrystalSusceptibility(self): self._crystalSusceptibility = None
	# Properties
	crystalSusceptibility = property(getCrystalSusceptibility, setCrystalSusceptibility, delCrystalSusceptibility, "Property for crystalSusceptibility")
	def getDetectorDistanceMax(self): return self._detectorDistanceMax
	def setDetectorDistanceMax(self, detectorDistanceMax):
		checkType("XSDataInputBest", "setDetectorDistanceMax", detectorDistanceMax, "XSDataLength")
		self._detectorDistanceMax = detectorDistanceMax
	def delDetectorDistanceMax(self): self._detectorDistanceMax = None
	# Properties
	detectorDistanceMax = property(getDetectorDistanceMax, setDetectorDistanceMax, delDetectorDistanceMax, "Property for detectorDistanceMax")
	def getDetectorDistanceMin(self): return self._detectorDistanceMin
	def setDetectorDistanceMin(self, detectorDistanceMin):
		checkType("XSDataInputBest", "setDetectorDistanceMin", detectorDistanceMin, "XSDataLength")
		self._detectorDistanceMin = detectorDistanceMin
	def delDetectorDistanceMin(self): self._detectorDistanceMin = None
	# Properties
	detectorDistanceMin = property(getDetectorDistanceMin, setDetectorDistanceMin, delDetectorDistanceMin, "Property for detectorDistanceMin")
	def getDetectorType(self): return self._detectorType
	def setDetectorType(self, detectorType):
		checkType("XSDataInputBest", "setDetectorType", detectorType, "XSDataString")
		self._detectorType = detectorType
	def delDetectorType(self): self._detectorType = None
	# Properties
	detectorType = property(getDetectorType, setDetectorType, delDetectorType, "Property for detectorType")
	def getGoniostatMaxRotationSpeed(self): return self._goniostatMaxRotationSpeed
	def setGoniostatMaxRotationSpeed(self, goniostatMaxRotationSpeed):
		checkType("XSDataInputBest", "setGoniostatMaxRotationSpeed", goniostatMaxRotationSpeed, "XSDataAngularSpeed")
		self._goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
	def delGoniostatMaxRotationSpeed(self): self._goniostatMaxRotationSpeed = None
	# Properties
	goniostatMaxRotationSpeed = property(getGoniostatMaxRotationSpeed, setGoniostatMaxRotationSpeed, delGoniostatMaxRotationSpeed, "Property for goniostatMaxRotationSpeed")
	def getGoniostatMinRotationWidth(self): return self._goniostatMinRotationWidth
	def setGoniostatMinRotationWidth(self, goniostatMinRotationWidth):
		checkType("XSDataInputBest", "setGoniostatMinRotationWidth", goniostatMinRotationWidth, "XSDataAngle")
		self._goniostatMinRotationWidth = goniostatMinRotationWidth
	def delGoniostatMinRotationWidth(self): self._goniostatMinRotationWidth = None
	# Properties
	goniostatMinRotationWidth = property(getGoniostatMinRotationWidth, setGoniostatMinRotationWidth, delGoniostatMinRotationWidth, "Property for goniostatMinRotationWidth")
	def getMinTransmission(self): return self._minTransmission
	def setMinTransmission(self, minTransmission):
		checkType("XSDataInputBest", "setMinTransmission", minTransmission, "XSDataDouble")
		self._minTransmission = minTransmission
	def delMinTransmission(self): self._minTransmission = None
	# Properties
	minTransmission = property(getMinTransmission, setMinTransmission, delMinTransmission, "Property for minTransmission")
	def getNumberOfCrystalPositions(self): return self._numberOfCrystalPositions
	def setNumberOfCrystalPositions(self, numberOfCrystalPositions):
		checkType("XSDataInputBest", "setNumberOfCrystalPositions", numberOfCrystalPositions, "XSDataInteger")
		self._numberOfCrystalPositions = numberOfCrystalPositions
	def delNumberOfCrystalPositions(self): self._numberOfCrystalPositions = None
	# Properties
	numberOfCrystalPositions = property(getNumberOfCrystalPositions, setNumberOfCrystalPositions, delNumberOfCrystalPositions, "Property for numberOfCrystalPositions")
	def getStrategyOption(self): return self._strategyOption
	def setStrategyOption(self, strategyOption):
		checkType("XSDataInputBest", "setStrategyOption", strategyOption, "XSDataString")
		self._strategyOption = strategyOption
	def delStrategyOption(self): self._strategyOption = None
	# Properties
	strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
	def getTransmission(self): return self._transmission
	def setTransmission(self, transmission):
		checkType("XSDataInputBest", "setTransmission", transmission, "XSDataDouble")
		self._transmission = transmission
	def delTransmission(self): self._transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def getXdsBackgroundImage(self): return self._xdsBackgroundImage
	def setXdsBackgroundImage(self, xdsBackgroundImage):
		checkType("XSDataInputBest", "setXdsBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
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
		if self._aimedCompleteness is not None:
			self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
		if self._aimedIOverSigma is not None:
			self.aimedIOverSigma.export(outfile, level, name_='aimedIOverSigma')
		if self._aimedRedundancy is not None:
			self.aimedRedundancy.export(outfile, level, name_='aimedRedundancy')
		if self._aimedResolution is not None:
			self.aimedResolution.export(outfile, level, name_='aimedResolution')
		if self._anomalousData is not None:
			self.anomalousData.export(outfile, level, name_='anomalousData')
		if self._beamExposureTime is not None:
			self.beamExposureTime.export(outfile, level, name_='beamExposureTime')
		else:
			warnEmptyAttribute("beamExposureTime", "XSDataTime")
		if self._beamMaxExposureTime is not None:
			self.beamMaxExposureTime.export(outfile, level, name_='beamMaxExposureTime')
		if self._beamMinExposureTime is not None:
			self.beamMinExposureTime.export(outfile, level, name_='beamMinExposureTime')
		if self._bestFileContentDat is not None:
			self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
		else:
			warnEmptyAttribute("bestFileContentDat", "XSDataString")
		for bestFileContentHKL_ in self.getBestFileContentHKL():
			bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
		if self.getBestFileContentHKL() == []:
			warnEmptyAttribute("bestFileContentHKL", "XSDataString")
		if self._bestFileContentPar is not None:
			self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
		else:
			warnEmptyAttribute("bestFileContentPar", "XSDataString")
		if self._complexity is not None:
			self.complexity.export(outfile, level, name_='complexity')
		if self._crystalAbsorbedDoseRate is not None:
			self.crystalAbsorbedDoseRate.export(outfile, level, name_='crystalAbsorbedDoseRate')
		if self._crystalShape is not None:
			self.crystalShape.export(outfile, level, name_='crystalShape')
		if self._crystalSusceptibility is not None:
			self.crystalSusceptibility.export(outfile, level, name_='crystalSusceptibility')
		if self._detectorDistanceMax is not None:
			self.detectorDistanceMax.export(outfile, level, name_='detectorDistanceMax')
		if self._detectorDistanceMin is not None:
			self.detectorDistanceMin.export(outfile, level, name_='detectorDistanceMin')
		if self._detectorType is not None:
			self.detectorType.export(outfile, level, name_='detectorType')
		else:
			warnEmptyAttribute("detectorType", "XSDataString")
		if self._goniostatMaxRotationSpeed is not None:
			self.goniostatMaxRotationSpeed.export(outfile, level, name_='goniostatMaxRotationSpeed')
		if self._goniostatMinRotationWidth is not None:
			self.goniostatMinRotationWidth.export(outfile, level, name_='goniostatMinRotationWidth')
		if self._minTransmission is not None:
			self.minTransmission.export(outfile, level, name_='minTransmission')
		if self._numberOfCrystalPositions is not None:
			self.numberOfCrystalPositions.export(outfile, level, name_='numberOfCrystalPositions')
		if self._strategyOption is not None:
			self.strategyOption.export(outfile, level, name_='strategyOption')
		if self._transmission is not None:
			self.transmission.export(outfile, level, name_='transmission')
		if self._xdsBackgroundImage is not None:
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputBest' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputBest is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	def __init__(self, status=None, pathToPlotMtvFile=None, pathToLogFile=None, collectionPlan=None):
		XSDataResult.__init__(self, status)
	
	
		if collectionPlan is None:
			self._collectionPlan = []
		else:
			checkType("XSDataResultBest", "Constructor of XSDataResultBest", collectionPlan, "list")
			self._collectionPlan = collectionPlan
		checkType("XSDataResultBest", "Constructor of XSDataResultBest", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
		checkType("XSDataResultBest", "Constructor of XSDataResultBest", pathToPlotMtvFile, "XSDataFile")
		self._pathToPlotMtvFile = pathToPlotMtvFile
	def getCollectionPlan(self): return self._collectionPlan
	def setCollectionPlan(self, collectionPlan):
		checkType("XSDataResultBest", "setCollectionPlan", collectionPlan, "list")
		self._collectionPlan = collectionPlan
	def delCollectionPlan(self): self._collectionPlan = None
	# Properties
	collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
	def addCollectionPlan(self, value):
		checkType("XSDataResultBest", "setCollectionPlan", value, "XSDataBestCollectionPlan")
		self._collectionPlan.append(value)
	def insertCollectionPlan(self, index, value):
		checkType("XSDataResultBest", "setCollectionPlan", value, "XSDataBestCollectionPlan")
		self._collectionPlan[index] = value
	def getPathToLogFile(self): return self._pathToLogFile
	def setPathToLogFile(self, pathToLogFile):
		checkType("XSDataResultBest", "setPathToLogFile", pathToLogFile, "XSDataFile")
		self._pathToLogFile = pathToLogFile
	def delPathToLogFile(self): self._pathToLogFile = None
	# Properties
	pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
	def getPathToPlotMtvFile(self): return self._pathToPlotMtvFile
	def setPathToPlotMtvFile(self, pathToPlotMtvFile):
		checkType("XSDataResultBest", "setPathToPlotMtvFile", pathToPlotMtvFile, "XSDataFile")
		self._pathToPlotMtvFile = pathToPlotMtvFile
	def delPathToPlotMtvFile(self): self._pathToPlotMtvFile = None
	# Properties
	pathToPlotMtvFile = property(getPathToPlotMtvFile, setPathToPlotMtvFile, delPathToPlotMtvFile, "Property for pathToPlotMtvFile")
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
		if self._pathToLogFile is not None:
			self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
		else:
			warnEmptyAttribute("pathToLogFile", "XSDataFile")
		if self._pathToPlotMtvFile is not None:
			self.pathToPlotMtvFile.export(outfile, level, name_='pathToPlotMtvFile')
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pathToPlotMtvFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPathToPlotMtvFile(obj_)
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultBest' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultBest is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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



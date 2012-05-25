#!/usr/bin/env python

#
# Generated Fri May 25 03:00::22 2012 by EDGenerateDS.
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
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataMXv1 import XSDataDiffractionPlan
	from XSDataMXv1 import XSDataImageQualityIndicators
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
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataImageQualityIndicators




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


class XSDataGridScreeningFileNameParameters(XSData):
	def __init__(self, scanId2=None, scanId1=None, motorPosition2=None, motorPosition1=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataGridScreeningFileNameParameters", "Constructor of XSDataGridScreeningFileNameParameters", motorPosition1, "XSDataString")
		self._motorPosition1 = motorPosition1
		checkType("XSDataGridScreeningFileNameParameters", "Constructor of XSDataGridScreeningFileNameParameters", motorPosition2, "XSDataString")
		self._motorPosition2 = motorPosition2
		checkType("XSDataGridScreeningFileNameParameters", "Constructor of XSDataGridScreeningFileNameParameters", scanId1, "XSDataString")
		self._scanId1 = scanId1
		checkType("XSDataGridScreeningFileNameParameters", "Constructor of XSDataGridScreeningFileNameParameters", scanId2, "XSDataString")
		self._scanId2 = scanId2
	def getMotorPosition1(self): return self._motorPosition1
	def setMotorPosition1(self, motorPosition1):
		checkType("XSDataGridScreeningFileNameParameters", "setMotorPosition1", motorPosition1, "XSDataString")
		self._motorPosition1 = motorPosition1
	def delMotorPosition1(self): self._motorPosition1 = None
	# Properties
	motorPosition1 = property(getMotorPosition1, setMotorPosition1, delMotorPosition1, "Property for motorPosition1")
	def getMotorPosition2(self): return self._motorPosition2
	def setMotorPosition2(self, motorPosition2):
		checkType("XSDataGridScreeningFileNameParameters", "setMotorPosition2", motorPosition2, "XSDataString")
		self._motorPosition2 = motorPosition2
	def delMotorPosition2(self): self._motorPosition2 = None
	# Properties
	motorPosition2 = property(getMotorPosition2, setMotorPosition2, delMotorPosition2, "Property for motorPosition2")
	def getScanId1(self): return self._scanId1
	def setScanId1(self, scanId1):
		checkType("XSDataGridScreeningFileNameParameters", "setScanId1", scanId1, "XSDataString")
		self._scanId1 = scanId1
	def delScanId1(self): self._scanId1 = None
	# Properties
	scanId1 = property(getScanId1, setScanId1, delScanId1, "Property for scanId1")
	def getScanId2(self): return self._scanId2
	def setScanId2(self, scanId2):
		checkType("XSDataGridScreeningFileNameParameters", "setScanId2", scanId2, "XSDataString")
		self._scanId2 = scanId2
	def delScanId2(self): self._scanId2 = None
	# Properties
	scanId2 = property(getScanId2, setScanId2, delScanId2, "Property for scanId2")
	def export(self, outfile, level, name_='XSDataGridScreeningFileNameParameters'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGridScreeningFileNameParameters'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._motorPosition1 is not None:
			self.motorPosition1.export(outfile, level, name_='motorPosition1')
		else:
			warnEmptyAttribute("motorPosition1", "XSDataString")
		if self._motorPosition2 is not None:
			self.motorPosition2.export(outfile, level, name_='motorPosition2')
		else:
			warnEmptyAttribute("motorPosition2", "XSDataString")
		if self._scanId1 is not None:
			self.scanId1.export(outfile, level, name_='scanId1')
		else:
			warnEmptyAttribute("scanId1", "XSDataString")
		if self._scanId2 is not None:
			self.scanId2.export(outfile, level, name_='scanId2')
		else:
			warnEmptyAttribute("scanId2", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'motorPosition1':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMotorPosition1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'motorPosition2':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMotorPosition2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scanId1':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setScanId1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scanId2':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setScanId2(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGridScreeningFileNameParameters" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGridScreeningFileNameParameters' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGridScreeningFileNameParameters is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGridScreeningFileNameParameters.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGridScreeningFileNameParameters()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGridScreeningFileNameParameters" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGridScreeningFileNameParameters()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGridScreeningFileNameParameters

class XSDataGridScreeningResultIntegration(XSData):
	def __init__(self, integratedData=None, fileDirectory=None, fileName=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataGridScreeningResultIntegration", "Constructor of XSDataGridScreeningResultIntegration", fileName, "string")
		self._fileName = fileName
		checkType("XSDataGridScreeningResultIntegration", "Constructor of XSDataGridScreeningResultIntegration", fileDirectory, "string")
		self._fileDirectory = fileDirectory
		checkType("XSDataGridScreeningResultIntegration", "Constructor of XSDataGridScreeningResultIntegration", integratedData, "string")
		self._integratedData = integratedData
	def getFileName(self): return self._fileName
	def setFileName(self, fileName):
		checkType("XSDataGridScreeningResultIntegration", "setFileName", fileName, "string")
		self._fileName = fileName
	def delFileName(self): self._fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFileDirectory(self): return self._fileDirectory
	def setFileDirectory(self, fileDirectory):
		checkType("XSDataGridScreeningResultIntegration", "setFileDirectory", fileDirectory, "string")
		self._fileDirectory = fileDirectory
	def delFileDirectory(self): self._fileDirectory = None
	# Properties
	fileDirectory = property(getFileDirectory, setFileDirectory, delFileDirectory, "Property for fileDirectory")
	def getIntegratedData(self): return self._integratedData
	def setIntegratedData(self, integratedData):
		checkType("XSDataGridScreeningResultIntegration", "setIntegratedData", integratedData, "string")
		self._integratedData = integratedData
	def delIntegratedData(self): self._integratedData = None
	# Properties
	integratedData = property(getIntegratedData, setIntegratedData, delIntegratedData, "Property for integratedData")
	def export(self, outfile, level, name_='XSDataGridScreeningResultIntegration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataGridScreeningResultIntegration'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._fileName is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileName>%s</fileName>\n' % self._fileName))
		else:
			warnEmptyAttribute("fileName", "string")
		if self._fileDirectory is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<fileDirectory>%s</fileDirectory>\n' % self._fileDirectory))
		else:
			warnEmptyAttribute("fileDirectory", "string")
		if self._integratedData is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<integratedData>%s</integratedData>\n' % self._integratedData))
		else:
			warnEmptyAttribute("integratedData", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._fileName = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileDirectory':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._fileDirectory = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'integratedData':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self._integratedData = value_
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataGridScreeningResultIntegration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGridScreeningResultIntegration' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataGridScreeningResultIntegration is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataGridScreeningResultIntegration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataGridScreeningResultIntegration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataGridScreeningResultIntegration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataGridScreeningResultIntegration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataGridScreeningResultIntegration

class XSDataInputGridScreening(XSDataInput):
	def __init__(self, configuration=None, doOnlyIntegrationWithXMLOutput=None, doOnlyImageQualityIndicators=None, storeImageQualityIndicatorsInISPyB=None, diffractionPlan=None, imageFile=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputGridScreening", "Constructor of XSDataInputGridScreening", imageFile, "XSDataFile")
		self._imageFile = imageFile
		checkType("XSDataInputGridScreening", "Constructor of XSDataInputGridScreening", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
		checkType("XSDataInputGridScreening", "Constructor of XSDataInputGridScreening", storeImageQualityIndicatorsInISPyB, "XSDataBoolean")
		self._storeImageQualityIndicatorsInISPyB = storeImageQualityIndicatorsInISPyB
		checkType("XSDataInputGridScreening", "Constructor of XSDataInputGridScreening", doOnlyImageQualityIndicators, "XSDataBoolean")
		self._doOnlyImageQualityIndicators = doOnlyImageQualityIndicators
		checkType("XSDataInputGridScreening", "Constructor of XSDataInputGridScreening", doOnlyIntegrationWithXMLOutput, "XSDataBoolean")
		self._doOnlyIntegrationWithXMLOutput = doOnlyIntegrationWithXMLOutput
	def getImageFile(self): return self._imageFile
	def setImageFile(self, imageFile):
		checkType("XSDataInputGridScreening", "setImageFile", imageFile, "XSDataFile")
		self._imageFile = imageFile
	def delImageFile(self): self._imageFile = None
	# Properties
	imageFile = property(getImageFile, setImageFile, delImageFile, "Property for imageFile")
	def getDiffractionPlan(self): return self._diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputGridScreening", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self._diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self._diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getStoreImageQualityIndicatorsInISPyB(self): return self._storeImageQualityIndicatorsInISPyB
	def setStoreImageQualityIndicatorsInISPyB(self, storeImageQualityIndicatorsInISPyB):
		checkType("XSDataInputGridScreening", "setStoreImageQualityIndicatorsInISPyB", storeImageQualityIndicatorsInISPyB, "XSDataBoolean")
		self._storeImageQualityIndicatorsInISPyB = storeImageQualityIndicatorsInISPyB
	def delStoreImageQualityIndicatorsInISPyB(self): self._storeImageQualityIndicatorsInISPyB = None
	# Properties
	storeImageQualityIndicatorsInISPyB = property(getStoreImageQualityIndicatorsInISPyB, setStoreImageQualityIndicatorsInISPyB, delStoreImageQualityIndicatorsInISPyB, "Property for storeImageQualityIndicatorsInISPyB")
	def getDoOnlyImageQualityIndicators(self): return self._doOnlyImageQualityIndicators
	def setDoOnlyImageQualityIndicators(self, doOnlyImageQualityIndicators):
		checkType("XSDataInputGridScreening", "setDoOnlyImageQualityIndicators", doOnlyImageQualityIndicators, "XSDataBoolean")
		self._doOnlyImageQualityIndicators = doOnlyImageQualityIndicators
	def delDoOnlyImageQualityIndicators(self): self._doOnlyImageQualityIndicators = None
	# Properties
	doOnlyImageQualityIndicators = property(getDoOnlyImageQualityIndicators, setDoOnlyImageQualityIndicators, delDoOnlyImageQualityIndicators, "Property for doOnlyImageQualityIndicators")
	def getDoOnlyIntegrationWithXMLOutput(self): return self._doOnlyIntegrationWithXMLOutput
	def setDoOnlyIntegrationWithXMLOutput(self, doOnlyIntegrationWithXMLOutput):
		checkType("XSDataInputGridScreening", "setDoOnlyIntegrationWithXMLOutput", doOnlyIntegrationWithXMLOutput, "XSDataBoolean")
		self._doOnlyIntegrationWithXMLOutput = doOnlyIntegrationWithXMLOutput
	def delDoOnlyIntegrationWithXMLOutput(self): self._doOnlyIntegrationWithXMLOutput = None
	# Properties
	doOnlyIntegrationWithXMLOutput = property(getDoOnlyIntegrationWithXMLOutput, setDoOnlyIntegrationWithXMLOutput, delDoOnlyIntegrationWithXMLOutput, "Property for doOnlyIntegrationWithXMLOutput")
	def export(self, outfile, level, name_='XSDataInputGridScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputGridScreening'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._imageFile is not None:
			self.imageFile.export(outfile, level, name_='imageFile')
		else:
			warnEmptyAttribute("imageFile", "XSDataFile")
		if self._diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		if self._storeImageQualityIndicatorsInISPyB is not None:
			self.storeImageQualityIndicatorsInISPyB.export(outfile, level, name_='storeImageQualityIndicatorsInISPyB')
		if self._doOnlyImageQualityIndicators is not None:
			self.doOnlyImageQualityIndicators.export(outfile, level, name_='doOnlyImageQualityIndicators')
		if self._doOnlyIntegrationWithXMLOutput is not None:
			self.doOnlyIntegrationWithXMLOutput.export(outfile, level, name_='doOnlyIntegrationWithXMLOutput')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setImageFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'storeImageQualityIndicatorsInISPyB':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setStoreImageQualityIndicatorsInISPyB(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'doOnlyImageQualityIndicators':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDoOnlyImageQualityIndicators(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'doOnlyIntegrationWithXMLOutput':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDoOnlyIntegrationWithXMLOutput(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputGridScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputGridScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputGridScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputGridScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputGridScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputGridScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputGridScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputGridScreening

class XSDataResultGridScreening(XSDataResult):
	def __init__(self, status=None, resultIntegration=None, imageQualityIndicatorsId=None, comment=None, rankingResolution=None, mosaicity=None, imageQualityIndicators=None, fileNameParameters=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", fileNameParameters, "XSDataGridScreeningFileNameParameters")
		self._fileNameParameters = fileNameParameters
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", imageQualityIndicators, "XSDataImageQualityIndicators")
		self._imageQualityIndicators = imageQualityIndicators
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", comment, "XSDataString")
		self._comment = comment
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", imageQualityIndicatorsId, "XSDataInteger")
		self._imageQualityIndicatorsId = imageQualityIndicatorsId
		checkType("XSDataResultGridScreening", "Constructor of XSDataResultGridScreening", resultIntegration, "XSDataGridScreeningResultIntegration")
		self._resultIntegration = resultIntegration
	def getFileNameParameters(self): return self._fileNameParameters
	def setFileNameParameters(self, fileNameParameters):
		checkType("XSDataResultGridScreening", "setFileNameParameters", fileNameParameters, "XSDataGridScreeningFileNameParameters")
		self._fileNameParameters = fileNameParameters
	def delFileNameParameters(self): self._fileNameParameters = None
	# Properties
	fileNameParameters = property(getFileNameParameters, setFileNameParameters, delFileNameParameters, "Property for fileNameParameters")
	def getImageQualityIndicators(self): return self._imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataResultGridScreening", "setImageQualityIndicators", imageQualityIndicators, "XSDataImageQualityIndicators")
		self._imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self._imageQualityIndicators = None
	# Properties
	imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
	def getMosaicity(self): return self._mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataResultGridScreening", "setMosaicity", mosaicity, "XSDataDouble")
		self._mosaicity = mosaicity
	def delMosaicity(self): self._mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getRankingResolution(self): return self._rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataResultGridScreening", "setRankingResolution", rankingResolution, "XSDataDouble")
		self._rankingResolution = rankingResolution
	def delRankingResolution(self): self._rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getComment(self): return self._comment
	def setComment(self, comment):
		checkType("XSDataResultGridScreening", "setComment", comment, "XSDataString")
		self._comment = comment
	def delComment(self): self._comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getImageQualityIndicatorsId(self): return self._imageQualityIndicatorsId
	def setImageQualityIndicatorsId(self, imageQualityIndicatorsId):
		checkType("XSDataResultGridScreening", "setImageQualityIndicatorsId", imageQualityIndicatorsId, "XSDataInteger")
		self._imageQualityIndicatorsId = imageQualityIndicatorsId
	def delImageQualityIndicatorsId(self): self._imageQualityIndicatorsId = None
	# Properties
	imageQualityIndicatorsId = property(getImageQualityIndicatorsId, setImageQualityIndicatorsId, delImageQualityIndicatorsId, "Property for imageQualityIndicatorsId")
	def getResultIntegration(self): return self._resultIntegration
	def setResultIntegration(self, resultIntegration):
		checkType("XSDataResultGridScreening", "setResultIntegration", resultIntegration, "XSDataGridScreeningResultIntegration")
		self._resultIntegration = resultIntegration
	def delResultIntegration(self): self._resultIntegration = None
	# Properties
	resultIntegration = property(getResultIntegration, setResultIntegration, delResultIntegration, "Property for resultIntegration")
	def export(self, outfile, level, name_='XSDataResultGridScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultGridScreening'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._fileNameParameters is not None:
			self.fileNameParameters.export(outfile, level, name_='fileNameParameters')
		if self._imageQualityIndicators is not None:
			self.imageQualityIndicators.export(outfile, level, name_='imageQualityIndicators')
		if self._mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self._rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		if self._comment is not None:
			self.comment.export(outfile, level, name_='comment')
		if self._imageQualityIndicatorsId is not None:
			self.imageQualityIndicatorsId.export(outfile, level, name_='imageQualityIndicatorsId')
		if self._resultIntegration is not None:
			self.resultIntegration.export(outfile, level, name_='resultIntegration')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileNameParameters':
			obj_ = XSDataGridScreeningFileNameParameters()
			obj_.build(child_)
			self.setFileNameParameters(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicators':
			obj_ = XSDataImageQualityIndicators()
			obj_.build(child_)
			self.setImageQualityIndicators(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingResolution':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRankingResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComment(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageQualityIndicatorsId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageQualityIndicatorsId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultIntegration':
			obj_ = XSDataGridScreeningResultIntegration()
			obj_.build(child_)
			self.setResultIntegration(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultGridScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultGridScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultGridScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultGridScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultGridScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultGridScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultGridScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultGridScreening



# End of data representation classes.



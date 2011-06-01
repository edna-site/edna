#!/usr/bin/env python

#
# Generated Mon Mar 28 03:27::32 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataCollectionPlan
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
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
	elif _value is None:
		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
		print(strMessage)
		#raise BaseException(strMessage)


def warnEmptyAttribute(_strName, _strTypeName):
	pass
	#if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
	#		print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer:
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


class XSDataMXCuBEDataSet:
	def __init__(self, imageFile=None):
		if imageFile is None:
			self.__imageFile = []
		else:
			self.__imageFile = imageFile
	def getImageFile(self): return self.__imageFile
	def setImageFile(self, imageFile):
		checkType("XSDataMXCuBEDataSet", "setImageFile", imageFile, "list")
		self.__imageFile = imageFile
	def delImageFile(self): self.__imageFile = None
	# Properties
	imageFile = property(getImageFile, setImageFile, delImageFile, "Property for imageFile")
	def addImageFile(self, value):
		checkType("XSDataMXCuBEDataSet", "setImageFile", value, "XSDataFile")
		self.__imageFile.append(value)
	def insertImageFile(self, index, value):
		checkType("XSDataMXCuBEDataSet", "setImageFile", value, "XSDataFile")
		self.__imageFile[index] = value
	def export(self, outfile, level, name_='XSDataMXCuBEDataSet'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMXCuBEDataSet'):
		pass
		for imageFile_ in self.getImageFile():
			imageFile_.export(outfile, level, name_='imageFile')
		if self.getImageFile() == []:
			warnEmptyAttribute("imageFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.imageFile.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMXCuBEDataSet" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMXCuBEDataSet' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMXCuBEDataSet.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMXCuBEDataSet()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMXCuBEDataSet" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMXCuBEDataSet()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMXCuBEDataSet

class XSDataInputMXCuBE(XSDataInput):
	def __init__(self, configuration=None, dataSet=None, sample=None, outputFileDirectory=None, experimentalCondition=None, diffractionPlan=None, dataCollectionId=None, characterisationInput=None):
		XSDataInput.__init__(self, configuration)
		self.__characterisationInput = characterisationInput
		self.__dataCollectionId = dataCollectionId
		self.__diffractionPlan = diffractionPlan
		self.__experimentalCondition = experimentalCondition
		self.__outputFileDirectory = outputFileDirectory
		self.__sample = sample
		if dataSet is None:
			self.__dataSet = []
		else:
			self.__dataSet = dataSet
	def getCharacterisationInput(self): return self.__characterisationInput
	def setCharacterisationInput(self, characterisationInput):
		checkType("XSDataInputMXCuBE", "setCharacterisationInput", characterisationInput, "XSDataInputCharacterisation")
		self.__characterisationInput = characterisationInput
	def delCharacterisationInput(self): self.__characterisationInput = None
	# Properties
	characterisationInput = property(getCharacterisationInput, setCharacterisationInput, delCharacterisationInput, "Property for characterisationInput")
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataInputMXCuBE", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getDiffractionPlan(self): return self.__diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputMXCuBE", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self.__diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getExperimentalCondition(self): return self.__experimentalCondition
	def setExperimentalCondition(self, experimentalCondition):
		checkType("XSDataInputMXCuBE", "setExperimentalCondition", experimentalCondition, "XSDataExperimentalCondition")
		self.__experimentalCondition = experimentalCondition
	def delExperimentalCondition(self): self.__experimentalCondition = None
	# Properties
	experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
	def getOutputFileDirectory(self): return self.__outputFileDirectory
	def setOutputFileDirectory(self, outputFileDirectory):
		checkType("XSDataInputMXCuBE", "setOutputFileDirectory", outputFileDirectory, "XSDataFile")
		self.__outputFileDirectory = outputFileDirectory
	def delOutputFileDirectory(self): self.__outputFileDirectory = None
	# Properties
	outputFileDirectory = property(getOutputFileDirectory, setOutputFileDirectory, delOutputFileDirectory, "Property for outputFileDirectory")
	def getSample(self): return self.__sample
	def setSample(self, sample):
		checkType("XSDataInputMXCuBE", "setSample", sample, "XSDataSampleCrystalMM")
		self.__sample = sample
	def delSample(self): self.__sample = None
	# Properties
	sample = property(getSample, setSample, delSample, "Property for sample")
	def getDataSet(self): return self.__dataSet
	def setDataSet(self, dataSet):
		checkType("XSDataInputMXCuBE", "setDataSet", dataSet, "list")
		self.__dataSet = dataSet
	def delDataSet(self): self.__dataSet = None
	# Properties
	dataSet = property(getDataSet, setDataSet, delDataSet, "Property for dataSet")
	def addDataSet(self, value):
		checkType("XSDataInputMXCuBE", "setDataSet", value, "XSDataMXCuBEDataSet")
		self.__dataSet.append(value)
	def insertDataSet(self, index, value):
		checkType("XSDataInputMXCuBE", "setDataSet", value, "XSDataMXCuBEDataSet")
		self.__dataSet[index] = value
	def export(self, outfile, level, name_='XSDataInputMXCuBE'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputMXCuBE'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__characterisationInput is not None:
			self.characterisationInput.export(outfile, level, name_='characterisationInput')
		else:
			warnEmptyAttribute("characterisationInput", "XSDataInputCharacterisation")
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		if self.__diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		else:
			warnEmptyAttribute("diffractionPlan", "XSDataDiffractionPlan")
		if self.__experimentalCondition is not None:
			self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
		if self.__outputFileDirectory is not None:
			self.outputFileDirectory.export(outfile, level, name_='outputFileDirectory')
		else:
			warnEmptyAttribute("outputFileDirectory", "XSDataFile")
		if self.__sample is not None:
			self.sample.export(outfile, level, name_='sample')
		else:
			warnEmptyAttribute("sample", "XSDataSampleCrystalMM")
		for dataSet_ in self.getDataSet():
			dataSet_.export(outfile, level, name_='dataSet')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'characterisationInput':
			obj_ = XSDataInputCharacterisation()
			obj_.build(child_)
			self.setCharacterisationInput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionPlan':
			obj_ = XSDataDiffractionPlan()
			obj_.build(child_)
			self.setDiffractionPlan(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalCondition':
			obj_ = XSDataExperimentalCondition()
			obj_.build(child_)
			self.setExperimentalCondition(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFileDirectory':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputFileDirectory(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sample':
			obj_ = XSDataSampleCrystalMM()
			obj_.build(child_)
			self.setSample(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataSet':
			obj_ = XSDataMXCuBEDataSet()
			obj_.build(child_)
			self.dataSet.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputMXCuBE" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputMXCuBE' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputMXCuBE.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputMXCuBE()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputMXCuBE" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputMXCuBE()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputMXCuBE

class XSDataResultMXCuBE(XSDataResult):
	def __init__(self, status=None, outputFileDictionary=None, listOfOutputFiles=None, collectionPlan=None, characterisationResult=None, characterisationExecutiveSummary=None):
		XSDataResult.__init__(self, status)
		self.__characterisationExecutiveSummary = characterisationExecutiveSummary
		self.__characterisationResult = characterisationResult
		if collectionPlan is None:
			self.__collectionPlan = []
		else:
			self.__collectionPlan = collectionPlan
		self.__listOfOutputFiles = listOfOutputFiles
		self.__outputFileDictionary = outputFileDictionary
	def getCharacterisationExecutiveSummary(self): return self.__characterisationExecutiveSummary
	def setCharacterisationExecutiveSummary(self, characterisationExecutiveSummary):
		checkType("XSDataResultMXCuBE", "setCharacterisationExecutiveSummary", characterisationExecutiveSummary, "XSDataString")
		self.__characterisationExecutiveSummary = characterisationExecutiveSummary
	def delCharacterisationExecutiveSummary(self): self.__characterisationExecutiveSummary = None
	# Properties
	characterisationExecutiveSummary = property(getCharacterisationExecutiveSummary, setCharacterisationExecutiveSummary, delCharacterisationExecutiveSummary, "Property for characterisationExecutiveSummary")
	def getCharacterisationResult(self): return self.__characterisationResult
	def setCharacterisationResult(self, characterisationResult):
		checkType("XSDataResultMXCuBE", "setCharacterisationResult", characterisationResult, "XSDataResultCharacterisation")
		self.__characterisationResult = characterisationResult
	def delCharacterisationResult(self): self.__characterisationResult = None
	# Properties
	characterisationResult = property(getCharacterisationResult, setCharacterisationResult, delCharacterisationResult, "Property for characterisationResult")
	def getCollectionPlan(self): return self.__collectionPlan
	def setCollectionPlan(self, collectionPlan):
		checkType("XSDataResultMXCuBE", "setCollectionPlan", collectionPlan, "list")
		self.__collectionPlan = collectionPlan
	def delCollectionPlan(self): self.__collectionPlan = None
	# Properties
	collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
	def addCollectionPlan(self, value):
		checkType("XSDataResultMXCuBE", "setCollectionPlan", value, "XSDataCollectionPlan")
		self.__collectionPlan.append(value)
	def insertCollectionPlan(self, index, value):
		checkType("XSDataResultMXCuBE", "setCollectionPlan", value, "XSDataCollectionPlan")
		self.__collectionPlan[index] = value
	def getListOfOutputFiles(self): return self.__listOfOutputFiles
	def setListOfOutputFiles(self, listOfOutputFiles):
		checkType("XSDataResultMXCuBE", "setListOfOutputFiles", listOfOutputFiles, "XSDataString")
		self.__listOfOutputFiles = listOfOutputFiles
	def delListOfOutputFiles(self): self.__listOfOutputFiles = None
	# Properties
	listOfOutputFiles = property(getListOfOutputFiles, setListOfOutputFiles, delListOfOutputFiles, "Property for listOfOutputFiles")
	def getOutputFileDictionary(self): return self.__outputFileDictionary
	def setOutputFileDictionary(self, outputFileDictionary):
		checkType("XSDataResultMXCuBE", "setOutputFileDictionary", outputFileDictionary, "XSDataDictionary")
		self.__outputFileDictionary = outputFileDictionary
	def delOutputFileDictionary(self): self.__outputFileDictionary = None
	# Properties
	outputFileDictionary = property(getOutputFileDictionary, setOutputFileDictionary, delOutputFileDictionary, "Property for outputFileDictionary")
	def export(self, outfile, level, name_='XSDataResultMXCuBE'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultMXCuBE'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__characterisationExecutiveSummary is not None:
			self.characterisationExecutiveSummary.export(outfile, level, name_='characterisationExecutiveSummary')
		else:
			warnEmptyAttribute("characterisationExecutiveSummary", "XSDataString")
		if self.__characterisationResult is not None:
			self.characterisationResult.export(outfile, level, name_='characterisationResult')
		else:
			warnEmptyAttribute("characterisationResult", "XSDataResultCharacterisation")
		for collectionPlan_ in self.getCollectionPlan():
			collectionPlan_.export(outfile, level, name_='collectionPlan')
		if self.__listOfOutputFiles is not None:
			self.listOfOutputFiles.export(outfile, level, name_='listOfOutputFiles')
		else:
			warnEmptyAttribute("listOfOutputFiles", "XSDataString")
		if self.__outputFileDictionary is not None:
			self.outputFileDictionary.export(outfile, level, name_='outputFileDictionary')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'characterisationExecutiveSummary':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCharacterisationExecutiveSummary(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'characterisationResult':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setCharacterisationResult(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'collectionPlan':
			obj_ = XSDataCollectionPlan()
			obj_.build(child_)
			self.collectionPlan.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'listOfOutputFiles':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setListOfOutputFiles(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFileDictionary':
			obj_ = XSDataDictionary()
			obj_.build(child_)
			self.setOutputFileDictionary(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultMXCuBE" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultMXCuBE' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultMXCuBE.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultMXCuBE()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultMXCuBE" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultMXCuBE()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultMXCuBE



# End of data representation classes.



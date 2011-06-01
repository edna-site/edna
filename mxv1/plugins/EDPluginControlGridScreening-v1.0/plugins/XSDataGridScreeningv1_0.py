#!/usr/bin/env python

#
# Generated Mon Apr 18 10:29::10 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

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


class XSDataGridScreeningFileNameParameters(XSData):
	def __init__(self, scanId2=None, scanId1=None, motorPosition2=None, motorPosition1=None):
		XSData.__init__(self, )
		self.__motorPosition1 = motorPosition1
		self.__motorPosition2 = motorPosition2
		self.__scanId1 = scanId1
		self.__scanId2 = scanId2
	def getMotorPosition1(self): return self.__motorPosition1
	def setMotorPosition1(self, motorPosition1):
		checkType("XSDataGridScreeningFileNameParameters", "setMotorPosition1", motorPosition1, "XSDataString")
		self.__motorPosition1 = motorPosition1
	def delMotorPosition1(self): self.__motorPosition1 = None
	# Properties
	motorPosition1 = property(getMotorPosition1, setMotorPosition1, delMotorPosition1, "Property for motorPosition1")
	def getMotorPosition2(self): return self.__motorPosition2
	def setMotorPosition2(self, motorPosition2):
		checkType("XSDataGridScreeningFileNameParameters", "setMotorPosition2", motorPosition2, "XSDataString")
		self.__motorPosition2 = motorPosition2
	def delMotorPosition2(self): self.__motorPosition2 = None
	# Properties
	motorPosition2 = property(getMotorPosition2, setMotorPosition2, delMotorPosition2, "Property for motorPosition2")
	def getScanId1(self): return self.__scanId1
	def setScanId1(self, scanId1):
		checkType("XSDataGridScreeningFileNameParameters", "setScanId1", scanId1, "XSDataString")
		self.__scanId1 = scanId1
	def delScanId1(self): self.__scanId1 = None
	# Properties
	scanId1 = property(getScanId1, setScanId1, delScanId1, "Property for scanId1")
	def getScanId2(self): return self.__scanId2
	def setScanId2(self, scanId2):
		checkType("XSDataGridScreeningFileNameParameters", "setScanId2", scanId2, "XSDataString")
		self.__scanId2 = scanId2
	def delScanId2(self): self.__scanId2 = None
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
		if self.__motorPosition1 is not None:
			self.motorPosition1.export(outfile, level, name_='motorPosition1')
		else:
			warnEmptyAttribute("motorPosition1", "XSDataString")
		if self.__motorPosition2 is not None:
			self.motorPosition2.export(outfile, level, name_='motorPosition2')
		else:
			warnEmptyAttribute("motorPosition2", "XSDataString")
		if self.__scanId1 is not None:
			self.scanId1.export(outfile, level, name_='scanId1')
		else:
			warnEmptyAttribute("scanId1", "XSDataString")
		if self.__scanId2 is not None:
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataGridScreeningFileNameParameters' )
		outfile.close()
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

class XSDataInputGridScreening(XSDataInput):
	def __init__(self, configuration=None, doOnlyImageQualityIndicators=None, storeImageQualityIndicatorsInISPyB=None, diffractionPlan=None, imageFile=None):
		XSDataInput.__init__(self, configuration)
		self.__imageFile = imageFile
		self.__diffractionPlan = diffractionPlan
		self.__storeImageQualityIndicatorsInISPyB = storeImageQualityIndicatorsInISPyB
		self.__doOnlyImageQualityIndicators = doOnlyImageQualityIndicators
	def getImageFile(self): return self.__imageFile
	def setImageFile(self, imageFile):
		checkType("XSDataInputGridScreening", "setImageFile", imageFile, "XSDataFile")
		self.__imageFile = imageFile
	def delImageFile(self): self.__imageFile = None
	# Properties
	imageFile = property(getImageFile, setImageFile, delImageFile, "Property for imageFile")
	def getDiffractionPlan(self): return self.__diffractionPlan
	def setDiffractionPlan(self, diffractionPlan):
		checkType("XSDataInputGridScreening", "setDiffractionPlan", diffractionPlan, "XSDataDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
	def delDiffractionPlan(self): self.__diffractionPlan = None
	# Properties
	diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
	def getStoreImageQualityIndicatorsInISPyB(self): return self.__storeImageQualityIndicatorsInISPyB
	def setStoreImageQualityIndicatorsInISPyB(self, storeImageQualityIndicatorsInISPyB):
		checkType("XSDataInputGridScreening", "setStoreImageQualityIndicatorsInISPyB", storeImageQualityIndicatorsInISPyB, "XSDataBoolean")
		self.__storeImageQualityIndicatorsInISPyB = storeImageQualityIndicatorsInISPyB
	def delStoreImageQualityIndicatorsInISPyB(self): self.__storeImageQualityIndicatorsInISPyB = None
	# Properties
	storeImageQualityIndicatorsInISPyB = property(getStoreImageQualityIndicatorsInISPyB, setStoreImageQualityIndicatorsInISPyB, delStoreImageQualityIndicatorsInISPyB, "Property for storeImageQualityIndicatorsInISPyB")
	def getDoOnlyImageQualityIndicators(self): return self.__doOnlyImageQualityIndicators
	def setDoOnlyImageQualityIndicators(self, doOnlyImageQualityIndicators):
		checkType("XSDataInputGridScreening", "setDoOnlyImageQualityIndicators", doOnlyImageQualityIndicators, "XSDataBoolean")
		self.__doOnlyImageQualityIndicators = doOnlyImageQualityIndicators
	def delDoOnlyImageQualityIndicators(self): self.__doOnlyImageQualityIndicators = None
	# Properties
	doOnlyImageQualityIndicators = property(getDoOnlyImageQualityIndicators, setDoOnlyImageQualityIndicators, delDoOnlyImageQualityIndicators, "Property for doOnlyImageQualityIndicators")
	def export(self, outfile, level, name_='XSDataInputGridScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputGridScreening'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__imageFile is not None:
			self.imageFile.export(outfile, level, name_='imageFile')
		else:
			warnEmptyAttribute("imageFile", "XSDataFile")
		if self.__diffractionPlan is not None:
			self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
		if self.__storeImageQualityIndicatorsInISPyB is not None:
			self.storeImageQualityIndicatorsInISPyB.export(outfile, level, name_='storeImageQualityIndicatorsInISPyB')
		if self.__doOnlyImageQualityIndicators is not None:
			self.doOnlyImageQualityIndicators.export(outfile, level, name_='doOnlyImageQualityIndicators')
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputGridScreening' )
		outfile.close()
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
	def __init__(self, status=None, imageQualityIndicatorsId=None, comment=None, rankingResolution=None, mosaicity=None, imageQualityIndicators=None, fileNameParameters=None):
		XSDataResult.__init__(self, status)
		self.__fileNameParameters = fileNameParameters
		self.__imageQualityIndicators = imageQualityIndicators
		self.__mosaicity = mosaicity
		self.__rankingResolution = rankingResolution
		self.__comment = comment
		self.__imageQualityIndicatorsId = imageQualityIndicatorsId
	def getFileNameParameters(self): return self.__fileNameParameters
	def setFileNameParameters(self, fileNameParameters):
		checkType("XSDataResultGridScreening", "setFileNameParameters", fileNameParameters, "XSDataGridScreeningFileNameParameters")
		self.__fileNameParameters = fileNameParameters
	def delFileNameParameters(self): self.__fileNameParameters = None
	# Properties
	fileNameParameters = property(getFileNameParameters, setFileNameParameters, delFileNameParameters, "Property for fileNameParameters")
	def getImageQualityIndicators(self): return self.__imageQualityIndicators
	def setImageQualityIndicators(self, imageQualityIndicators):
		checkType("XSDataResultGridScreening", "setImageQualityIndicators", imageQualityIndicators, "XSDataImageQualityIndicators")
		self.__imageQualityIndicators = imageQualityIndicators
	def delImageQualityIndicators(self): self.__imageQualityIndicators = None
	# Properties
	imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
	def getMosaicity(self): return self.__mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataResultGridScreening", "setMosaicity", mosaicity, "XSDataDouble")
		self.__mosaicity = mosaicity
	def delMosaicity(self): self.__mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getRankingResolution(self): return self.__rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataResultGridScreening", "setRankingResolution", rankingResolution, "XSDataDouble")
		self.__rankingResolution = rankingResolution
	def delRankingResolution(self): self.__rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("XSDataResultGridScreening", "setComment", comment, "XSDataString")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getImageQualityIndicatorsId(self): return self.__imageQualityIndicatorsId
	def setImageQualityIndicatorsId(self, imageQualityIndicatorsId):
		checkType("XSDataResultGridScreening", "setImageQualityIndicatorsId", imageQualityIndicatorsId, "XSDataInteger")
		self.__imageQualityIndicatorsId = imageQualityIndicatorsId
	def delImageQualityIndicatorsId(self): self.__imageQualityIndicatorsId = None
	# Properties
	imageQualityIndicatorsId = property(getImageQualityIndicatorsId, setImageQualityIndicatorsId, delImageQualityIndicatorsId, "Property for imageQualityIndicatorsId")
	def export(self, outfile, level, name_='XSDataResultGridScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultGridScreening'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__fileNameParameters is not None:
			self.fileNameParameters.export(outfile, level, name_='fileNameParameters')
		if self.__imageQualityIndicators is not None:
			self.imageQualityIndicators.export(outfile, level, name_='imageQualityIndicators')
		if self.__mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		if self.__rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		if self.__comment is not None:
			self.comment.export(outfile, level, name_='comment')
		if self.__imageQualityIndicatorsId is not None:
			self.imageQualityIndicatorsId.export(outfile, level, name_='imageQualityIndicatorsId')
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
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultGridScreening' )
		outfile.close()
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



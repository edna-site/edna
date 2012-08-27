#!/usr/bin/env python

#
# Generated Wed Feb 22 11:27::01 2012 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
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
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString




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


class XSDataISPyBDataCollection(XSData):
	def __init__(self, imagePrefix=None, imageDirectory=None, dataCollectionNumber=None, experimentType=None, sessionId=None, blSampleId=None, dataCollectionId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", blSampleId, "XSDataInteger")
		self.__blSampleId = blSampleId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", sessionId, "XSDataInteger")
		self.__sessionId = sessionId
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", experimentType, "XSDataString")
		self.__experimentType = experimentType
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", dataCollectionNumber, "XSDataInteger")
		self.__dataCollectionNumber = dataCollectionNumber
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imageDirectory, "XSDataString")
		self.__imageDirectory = imageDirectory
		checkType("XSDataISPyBDataCollection", "Constructor of XSDataISPyBDataCollection", imagePrefix, "XSDataString")
		self.__imagePrefix = imagePrefix
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBDataCollection", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getBlSampleId(self): return self.__blSampleId
	def setBlSampleId(self, blSampleId):
		checkType("XSDataISPyBDataCollection", "setBlSampleId", blSampleId, "XSDataInteger")
		self.__blSampleId = blSampleId
	def delBlSampleId(self): self.__blSampleId = None
	# Properties
	blSampleId = property(getBlSampleId, setBlSampleId, delBlSampleId, "Property for blSampleId")
	def getSessionId(self): return self.__sessionId
	def setSessionId(self, sessionId):
		checkType("XSDataISPyBDataCollection", "setSessionId", sessionId, "XSDataInteger")
		self.__sessionId = sessionId
	def delSessionId(self): self.__sessionId = None
	# Properties
	sessionId = property(getSessionId, setSessionId, delSessionId, "Property for sessionId")
	def getExperimentType(self): return self.__experimentType
	def setExperimentType(self, experimentType):
		checkType("XSDataISPyBDataCollection", "setExperimentType", experimentType, "XSDataString")
		self.__experimentType = experimentType
	def delExperimentType(self): self.__experimentType = None
	# Properties
	experimentType = property(getExperimentType, setExperimentType, delExperimentType, "Property for experimentType")
	def getDataCollectionNumber(self): return self.__dataCollectionNumber
	def setDataCollectionNumber(self, dataCollectionNumber):
		checkType("XSDataISPyBDataCollection", "setDataCollectionNumber", dataCollectionNumber, "XSDataInteger")
		self.__dataCollectionNumber = dataCollectionNumber
	def delDataCollectionNumber(self): self.__dataCollectionNumber = None
	# Properties
	dataCollectionNumber = property(getDataCollectionNumber, setDataCollectionNumber, delDataCollectionNumber, "Property for dataCollectionNumber")
	def getImageDirectory(self): return self.__imageDirectory
	def setImageDirectory(self, imageDirectory):
		checkType("XSDataISPyBDataCollection", "setImageDirectory", imageDirectory, "XSDataString")
		self.__imageDirectory = imageDirectory
	def delImageDirectory(self): self.__imageDirectory = None
	# Properties
	imageDirectory = property(getImageDirectory, setImageDirectory, delImageDirectory, "Property for imageDirectory")
	def getImagePrefix(self): return self.__imagePrefix
	def setImagePrefix(self, imagePrefix):
		checkType("XSDataISPyBDataCollection", "setImagePrefix", imagePrefix, "XSDataString")
		self.__imagePrefix = imagePrefix
	def delImagePrefix(self): self.__imagePrefix = None
	# Properties
	imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
	def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		else:
			warnEmptyAttribute("dataCollectionId", "XSDataInteger")
		if self.__blSampleId is not None:
			self.blSampleId.export(outfile, level, name_='blSampleId')
		else:
			warnEmptyAttribute("blSampleId", "XSDataInteger")
		if self.__sessionId is not None:
			self.sessionId.export(outfile, level, name_='sessionId')
		else:
			warnEmptyAttribute("sessionId", "XSDataInteger")
		if self.__experimentType is not None:
			self.experimentType.export(outfile, level, name_='experimentType')
		else:
			warnEmptyAttribute("experimentType", "XSDataString")
		if self.__dataCollectionNumber is not None:
			self.dataCollectionNumber.export(outfile, level, name_='dataCollectionNumber')
		else:
			warnEmptyAttribute("dataCollectionNumber", "XSDataInteger")
		if self.__imageDirectory is not None:
			self.imageDirectory.export(outfile, level, name_='imageDirectory')
		else:
			warnEmptyAttribute("imageDirectory", "XSDataString")
		if self.__imagePrefix is not None:
			self.imagePrefix.export(outfile, level, name_='imagePrefix')
		else:
			warnEmptyAttribute("imagePrefix", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'blSampleId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setBlSampleId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sessionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSessionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setExperimentType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageDirectory':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImageDirectory(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagePrefix':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImagePrefix(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBDataCollection' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBDataCollection is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBDataCollection

class XSDataISPyBImage(XSData):
	def __init__(self, machineMessage=None, comments=None, synchrotronCurrent=None, cumulativeIntensity=None, temperature=None, jpegThumbnailFileFullPath=None, jpegFileFullPath=None, measuredIntensity=None, fileLocation=None, fileName=None, imageNumber=None, imageId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageId, "XSDataInteger")
		self.__imageId = imageId
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", imageNumber, "XSDataInteger")
		self.__imageNumber = imageNumber
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileName, "XSDataString")
		self.__fileName = fileName
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", fileLocation, "XSDataString")
		self.__fileLocation = fileLocation
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", measuredIntensity, "XSDataFloat")
		self.__measuredIntensity = measuredIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegFileFullPath, "XSDataString")
		self.__jpegFileFullPath = jpegFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", jpegThumbnailFileFullPath, "XSDataString")
		self.__jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", temperature, "XSDataFloat")
		self.__temperature = temperature
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", cumulativeIntensity, "XSDataFloat")
		self.__cumulativeIntensity = cumulativeIntensity
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", synchrotronCurrent, "XSDataFloat")
		self.__synchrotronCurrent = synchrotronCurrent
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", comments, "XSDataString")
		self.__comments = comments
		checkType("XSDataISPyBImage", "Constructor of XSDataISPyBImage", machineMessage, "XSDataString")
		self.__machineMessage = machineMessage
	def getImageId(self): return self.__imageId
	def setImageId(self, imageId):
		checkType("XSDataISPyBImage", "setImageId", imageId, "XSDataInteger")
		self.__imageId = imageId
	def delImageId(self): self.__imageId = None
	# Properties
	imageId = property(getImageId, setImageId, delImageId, "Property for imageId")
	def getImageNumber(self): return self.__imageNumber
	def setImageNumber(self, imageNumber):
		checkType("XSDataISPyBImage", "setImageNumber", imageNumber, "XSDataInteger")
		self.__imageNumber = imageNumber
	def delImageNumber(self): self.__imageNumber = None
	# Properties
	imageNumber = property(getImageNumber, setImageNumber, delImageNumber, "Property for imageNumber")
	def getFileName(self): return self.__fileName
	def setFileName(self, fileName):
		checkType("XSDataISPyBImage", "setFileName", fileName, "XSDataString")
		self.__fileName = fileName
	def delFileName(self): self.__fileName = None
	# Properties
	fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
	def getFileLocation(self): return self.__fileLocation
	def setFileLocation(self, fileLocation):
		checkType("XSDataISPyBImage", "setFileLocation", fileLocation, "XSDataString")
		self.__fileLocation = fileLocation
	def delFileLocation(self): self.__fileLocation = None
	# Properties
	fileLocation = property(getFileLocation, setFileLocation, delFileLocation, "Property for fileLocation")
	def getMeasuredIntensity(self): return self.__measuredIntensity
	def setMeasuredIntensity(self, measuredIntensity):
		checkType("XSDataISPyBImage", "setMeasuredIntensity", measuredIntensity, "XSDataFloat")
		self.__measuredIntensity = measuredIntensity
	def delMeasuredIntensity(self): self.__measuredIntensity = None
	# Properties
	measuredIntensity = property(getMeasuredIntensity, setMeasuredIntensity, delMeasuredIntensity, "Property for measuredIntensity")
	def getJpegFileFullPath(self): return self.__jpegFileFullPath
	def setJpegFileFullPath(self, jpegFileFullPath):
		checkType("XSDataISPyBImage", "setJpegFileFullPath", jpegFileFullPath, "XSDataString")
		self.__jpegFileFullPath = jpegFileFullPath
	def delJpegFileFullPath(self): self.__jpegFileFullPath = None
	# Properties
	jpegFileFullPath = property(getJpegFileFullPath, setJpegFileFullPath, delJpegFileFullPath, "Property for jpegFileFullPath")
	def getJpegThumbnailFileFullPath(self): return self.__jpegThumbnailFileFullPath
	def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath):
		checkType("XSDataISPyBImage", "setJpegThumbnailFileFullPath", jpegThumbnailFileFullPath, "XSDataString")
		self.__jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
	def delJpegThumbnailFileFullPath(self): self.__jpegThumbnailFileFullPath = None
	# Properties
	jpegThumbnailFileFullPath = property(getJpegThumbnailFileFullPath, setJpegThumbnailFileFullPath, delJpegThumbnailFileFullPath, "Property for jpegThumbnailFileFullPath")
	def getTemperature(self): return self.__temperature
	def setTemperature(self, temperature):
		checkType("XSDataISPyBImage", "setTemperature", temperature, "XSDataFloat")
		self.__temperature = temperature
	def delTemperature(self): self.__temperature = None
	# Properties
	temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
	def getCumulativeIntensity(self): return self.__cumulativeIntensity
	def setCumulativeIntensity(self, cumulativeIntensity):
		checkType("XSDataISPyBImage", "setCumulativeIntensity", cumulativeIntensity, "XSDataFloat")
		self.__cumulativeIntensity = cumulativeIntensity
	def delCumulativeIntensity(self): self.__cumulativeIntensity = None
	# Properties
	cumulativeIntensity = property(getCumulativeIntensity, setCumulativeIntensity, delCumulativeIntensity, "Property for cumulativeIntensity")
	def getSynchrotronCurrent(self): return self.__synchrotronCurrent
	def setSynchrotronCurrent(self, synchrotronCurrent):
		checkType("XSDataISPyBImage", "setSynchrotronCurrent", synchrotronCurrent, "XSDataFloat")
		self.__synchrotronCurrent = synchrotronCurrent
	def delSynchrotronCurrent(self): self.__synchrotronCurrent = None
	# Properties
	synchrotronCurrent = property(getSynchrotronCurrent, setSynchrotronCurrent, delSynchrotronCurrent, "Property for synchrotronCurrent")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataISPyBImage", "setComments", comments, "XSDataString")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getMachineMessage(self): return self.__machineMessage
	def setMachineMessage(self, machineMessage):
		checkType("XSDataISPyBImage", "setMachineMessage", machineMessage, "XSDataString")
		self.__machineMessage = machineMessage
	def delMachineMessage(self): self.__machineMessage = None
	# Properties
	machineMessage = property(getMachineMessage, setMachineMessage, delMachineMessage, "Property for machineMessage")
	def export(self, outfile, level, name_='XSDataISPyBImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBImage'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__imageId is not None:
			self.imageId.export(outfile, level, name_='imageId')
		else:
			warnEmptyAttribute("imageId", "XSDataInteger")
		if self.__imageNumber is not None:
			self.imageNumber.export(outfile, level, name_='imageNumber')
		else:
			warnEmptyAttribute("imageNumber", "XSDataInteger")
		if self.__fileName is not None:
			self.fileName.export(outfile, level, name_='fileName')
		else:
			warnEmptyAttribute("fileName", "XSDataString")
		if self.__fileLocation is not None:
			self.fileLocation.export(outfile, level, name_='fileLocation')
		else:
			warnEmptyAttribute("fileLocation", "XSDataString")
		if self.__measuredIntensity is not None:
			self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
		else:
			warnEmptyAttribute("measuredIntensity", "XSDataFloat")
		if self.__jpegFileFullPath is not None:
			self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
		else:
			warnEmptyAttribute("jpegFileFullPath", "XSDataString")
		if self.__jpegThumbnailFileFullPath is not None:
			self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
		else:
			warnEmptyAttribute("jpegThumbnailFileFullPath", "XSDataString")
		if self.__temperature is not None:
			self.temperature.export(outfile, level, name_='temperature')
		else:
			warnEmptyAttribute("temperature", "XSDataFloat")
		if self.__cumulativeIntensity is not None:
			self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
		else:
			warnEmptyAttribute("cumulativeIntensity", "XSDataFloat")
		if self.__synchrotronCurrent is not None:
			self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
		else:
			warnEmptyAttribute("synchrotronCurrent", "XSDataFloat")
		if self.__comments is not None:
			self.comments.export(outfile, level, name_='comments')
		else:
			warnEmptyAttribute("comments", "XSDataString")
		if self.__machineMessage is not None:
			self.machineMessage.export(outfile, level, name_='machineMessage')
		else:
			warnEmptyAttribute("machineMessage", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imageNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setImageNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fileLocation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFileLocation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'measuredIntensity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMeasuredIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'jpegFileFullPath':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setJpegFileFullPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'jpegThumbnailFileFullPath':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setJpegThumbnailFileFullPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'temperature':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setTemperature(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cumulativeIntensity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCumulativeIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'synchrotronCurrent':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSynchrotronCurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setComments(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'machineMessage':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMachineMessage(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBImage

class XSDataISPyBScreening(XSData):
	def __init__(self, programVersion=None, timeStamp=None, screeningId=None, dataCollectionId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
		checkType("XSDataISPyBScreening", "Constructor of XSDataISPyBScreening", programVersion, "XSDataString")
		self.__programVersion = programVersion
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataISPyBScreening", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreening", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getTimeStamp(self): return self.__timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreening", "setTimeStamp", timeStamp, "XSDataString")
		self.__timeStamp = timeStamp
	def delTimeStamp(self): self.__timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def getProgramVersion(self): return self.__programVersion
	def setProgramVersion(self, programVersion):
		checkType("XSDataISPyBScreening", "setProgramVersion", programVersion, "XSDataString")
		self.__programVersion = programVersion
	def delProgramVersion(self): self.__programVersion = None
	# Properties
	programVersion = property(getProgramVersion, setProgramVersion, delProgramVersion, "Property for programVersion")
	def export(self, outfile, level, name_='XSDataISPyBScreening'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreening'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		else:
			warnEmptyAttribute("dataCollectionId", "XSDataInteger")
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataString")
		if self.__programVersion is not None:
			self.programVersion.export(outfile, level, name_='programVersion')
		else:
			warnEmptyAttribute("programVersion", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeStamp':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTimeStamp(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'programVersion':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProgramVersion(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreening" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreening' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreening is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreening.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreening()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreening" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreening()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreening

class XSDataISPyBScreeningInput(XSData):
	def __init__(self, minimumSignalToNoise=None, maximumFractionRejected=None, minimumFractionIndexed=None, rmsErrorLimits=None, beamY=None, beamX=None, screeningId=None, screeningInputId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamX, "XSDataFloat")
		self.__beamX = beamX
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", beamY, "XSDataFloat")
		self.__beamY = beamY
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", rmsErrorLimits, "XSDataFloat")
		self.__rmsErrorLimits = rmsErrorLimits
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumFractionIndexed, "XSDataFloat")
		self.__minimumFractionIndexed = minimumFractionIndexed
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", maximumFractionRejected, "XSDataFloat")
		self.__maximumFractionRejected = maximumFractionRejected
		checkType("XSDataISPyBScreeningInput", "Constructor of XSDataISPyBScreeningInput", minimumSignalToNoise, "XSDataFloat")
		self.__minimumSignalToNoise = minimumSignalToNoise
	def getScreeningInputId(self): return self.__screeningInputId
	def setScreeningInputId(self, screeningInputId):
		checkType("XSDataISPyBScreeningInput", "setScreeningInputId", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
	def delScreeningInputId(self): self.__screeningInputId = None
	# Properties
	screeningInputId = property(getScreeningInputId, setScreeningInputId, delScreeningInputId, "Property for screeningInputId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningInput", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getBeamX(self): return self.__beamX
	def setBeamX(self, beamX):
		checkType("XSDataISPyBScreeningInput", "setBeamX", beamX, "XSDataFloat")
		self.__beamX = beamX
	def delBeamX(self): self.__beamX = None
	# Properties
	beamX = property(getBeamX, setBeamX, delBeamX, "Property for beamX")
	def getBeamY(self): return self.__beamY
	def setBeamY(self, beamY):
		checkType("XSDataISPyBScreeningInput", "setBeamY", beamY, "XSDataFloat")
		self.__beamY = beamY
	def delBeamY(self): self.__beamY = None
	# Properties
	beamY = property(getBeamY, setBeamY, delBeamY, "Property for beamY")
	def getRmsErrorLimits(self): return self.__rmsErrorLimits
	def setRmsErrorLimits(self, rmsErrorLimits):
		checkType("XSDataISPyBScreeningInput", "setRmsErrorLimits", rmsErrorLimits, "XSDataFloat")
		self.__rmsErrorLimits = rmsErrorLimits
	def delRmsErrorLimits(self): self.__rmsErrorLimits = None
	# Properties
	rmsErrorLimits = property(getRmsErrorLimits, setRmsErrorLimits, delRmsErrorLimits, "Property for rmsErrorLimits")
	def getMinimumFractionIndexed(self): return self.__minimumFractionIndexed
	def setMinimumFractionIndexed(self, minimumFractionIndexed):
		checkType("XSDataISPyBScreeningInput", "setMinimumFractionIndexed", minimumFractionIndexed, "XSDataFloat")
		self.__minimumFractionIndexed = minimumFractionIndexed
	def delMinimumFractionIndexed(self): self.__minimumFractionIndexed = None
	# Properties
	minimumFractionIndexed = property(getMinimumFractionIndexed, setMinimumFractionIndexed, delMinimumFractionIndexed, "Property for minimumFractionIndexed")
	def getMaximumFractionRejected(self): return self.__maximumFractionRejected
	def setMaximumFractionRejected(self, maximumFractionRejected):
		checkType("XSDataISPyBScreeningInput", "setMaximumFractionRejected", maximumFractionRejected, "XSDataFloat")
		self.__maximumFractionRejected = maximumFractionRejected
	def delMaximumFractionRejected(self): self.__maximumFractionRejected = None
	# Properties
	maximumFractionRejected = property(getMaximumFractionRejected, setMaximumFractionRejected, delMaximumFractionRejected, "Property for maximumFractionRejected")
	def getMinimumSignalToNoise(self): return self.__minimumSignalToNoise
	def setMinimumSignalToNoise(self, minimumSignalToNoise):
		checkType("XSDataISPyBScreeningInput", "setMinimumSignalToNoise", minimumSignalToNoise, "XSDataFloat")
		self.__minimumSignalToNoise = minimumSignalToNoise
	def delMinimumSignalToNoise(self): self.__minimumSignalToNoise = None
	# Properties
	minimumSignalToNoise = property(getMinimumSignalToNoise, setMinimumSignalToNoise, delMinimumSignalToNoise, "Property for minimumSignalToNoise")
	def export(self, outfile, level, name_='XSDataISPyBScreeningInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningInputId is not None:
			self.screeningInputId.export(outfile, level, name_='screeningInputId')
		else:
			warnEmptyAttribute("screeningInputId", "XSDataInteger")
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__beamX is not None:
			self.beamX.export(outfile, level, name_='beamX')
		else:
			warnEmptyAttribute("beamX", "XSDataFloat")
		if self.__beamY is not None:
			self.beamY.export(outfile, level, name_='beamY')
		else:
			warnEmptyAttribute("beamY", "XSDataFloat")
		if self.__rmsErrorLimits is not None:
			self.rmsErrorLimits.export(outfile, level, name_='rmsErrorLimits')
		else:
			warnEmptyAttribute("rmsErrorLimits", "XSDataFloat")
		if self.__minimumFractionIndexed is not None:
			self.minimumFractionIndexed.export(outfile, level, name_='minimumFractionIndexed')
		else:
			warnEmptyAttribute("minimumFractionIndexed", "XSDataFloat")
		if self.__maximumFractionRejected is not None:
			self.maximumFractionRejected.export(outfile, level, name_='maximumFractionRejected')
		else:
			warnEmptyAttribute("maximumFractionRejected", "XSDataFloat")
		if self.__minimumSignalToNoise is not None:
			self.minimumSignalToNoise.export(outfile, level, name_='minimumSignalToNoise')
		else:
			warnEmptyAttribute("minimumSignalToNoise", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningInputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamX':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamY':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmsErrorLimits':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRmsErrorLimits(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimumFractionIndexed':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMinimumFractionIndexed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maximumFractionRejected':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMaximumFractionRejected(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimumSignalToNoise':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMinimumSignalToNoise(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningInput

class XSDataISPyBScreeningOutput(XSData):
	def __init__(self, mosaicityEstimated=None, screeningSuccess=None, diffractionRings=None, iOverSigma=None, mosaicity=None, numSpotsRejected=None, numSpotsUsed=None, numSpotsFound=None, beamShiftY=None, beamShiftX=None, spotDeviationTheta=None, spotDeviationR=None, resolutionObtained=None, rejectedReflections=None, statusDescription=None, screeningId=None, screeningOutputId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", statusDescription, "XSDataString")
		self.__statusDescription = statusDescription
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", rejectedReflections, "XSDataInteger")
		self.__rejectedReflections = rejectedReflections
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", resolutionObtained, "XSDataFloat")
		self.__resolutionObtained = resolutionObtained
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationR, "XSDataFloat")
		self.__spotDeviationR = spotDeviationR
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", spotDeviationTheta, "XSDataFloat")
		self.__spotDeviationTheta = spotDeviationTheta
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftX, "XSDataFloat")
		self.__beamShiftX = beamShiftX
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", beamShiftY, "XSDataFloat")
		self.__beamShiftY = beamShiftY
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsFound, "XSDataInteger")
		self.__numSpotsFound = numSpotsFound
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsUsed, "XSDataInteger")
		self.__numSpotsUsed = numSpotsUsed
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", numSpotsRejected, "XSDataInteger")
		self.__numSpotsRejected = numSpotsRejected
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicity, "XSDataFloat")
		self.__mosaicity = mosaicity
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", iOverSigma, "XSDataFloat")
		self.__iOverSigma = iOverSigma
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", diffractionRings, "XSDataBoolean")
		self.__diffractionRings = diffractionRings
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", screeningSuccess, "XSDataBoolean")
		self.__screeningSuccess = screeningSuccess
		checkType("XSDataISPyBScreeningOutput", "Constructor of XSDataISPyBScreeningOutput", mosaicityEstimated, "XSDataBoolean")
		self.__mosaicityEstimated = mosaicityEstimated
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningOutput", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getStatusDescription(self): return self.__statusDescription
	def setStatusDescription(self, statusDescription):
		checkType("XSDataISPyBScreeningOutput", "setStatusDescription", statusDescription, "XSDataString")
		self.__statusDescription = statusDescription
	def delStatusDescription(self): self.__statusDescription = None
	# Properties
	statusDescription = property(getStatusDescription, setStatusDescription, delStatusDescription, "Property for statusDescription")
	def getRejectedReflections(self): return self.__rejectedReflections
	def setRejectedReflections(self, rejectedReflections):
		checkType("XSDataISPyBScreeningOutput", "setRejectedReflections", rejectedReflections, "XSDataInteger")
		self.__rejectedReflections = rejectedReflections
	def delRejectedReflections(self): self.__rejectedReflections = None
	# Properties
	rejectedReflections = property(getRejectedReflections, setRejectedReflections, delRejectedReflections, "Property for rejectedReflections")
	def getResolutionObtained(self): return self.__resolutionObtained
	def setResolutionObtained(self, resolutionObtained):
		checkType("XSDataISPyBScreeningOutput", "setResolutionObtained", resolutionObtained, "XSDataFloat")
		self.__resolutionObtained = resolutionObtained
	def delResolutionObtained(self): self.__resolutionObtained = None
	# Properties
	resolutionObtained = property(getResolutionObtained, setResolutionObtained, delResolutionObtained, "Property for resolutionObtained")
	def getSpotDeviationR(self): return self.__spotDeviationR
	def setSpotDeviationR(self, spotDeviationR):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationR", spotDeviationR, "XSDataFloat")
		self.__spotDeviationR = spotDeviationR
	def delSpotDeviationR(self): self.__spotDeviationR = None
	# Properties
	spotDeviationR = property(getSpotDeviationR, setSpotDeviationR, delSpotDeviationR, "Property for spotDeviationR")
	def getSpotDeviationTheta(self): return self.__spotDeviationTheta
	def setSpotDeviationTheta(self, spotDeviationTheta):
		checkType("XSDataISPyBScreeningOutput", "setSpotDeviationTheta", spotDeviationTheta, "XSDataFloat")
		self.__spotDeviationTheta = spotDeviationTheta
	def delSpotDeviationTheta(self): self.__spotDeviationTheta = None
	# Properties
	spotDeviationTheta = property(getSpotDeviationTheta, setSpotDeviationTheta, delSpotDeviationTheta, "Property for spotDeviationTheta")
	def getBeamShiftX(self): return self.__beamShiftX
	def setBeamShiftX(self, beamShiftX):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftX", beamShiftX, "XSDataFloat")
		self.__beamShiftX = beamShiftX
	def delBeamShiftX(self): self.__beamShiftX = None
	# Properties
	beamShiftX = property(getBeamShiftX, setBeamShiftX, delBeamShiftX, "Property for beamShiftX")
	def getBeamShiftY(self): return self.__beamShiftY
	def setBeamShiftY(self, beamShiftY):
		checkType("XSDataISPyBScreeningOutput", "setBeamShiftY", beamShiftY, "XSDataFloat")
		self.__beamShiftY = beamShiftY
	def delBeamShiftY(self): self.__beamShiftY = None
	# Properties
	beamShiftY = property(getBeamShiftY, setBeamShiftY, delBeamShiftY, "Property for beamShiftY")
	def getNumSpotsFound(self): return self.__numSpotsFound
	def setNumSpotsFound(self, numSpotsFound):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsFound", numSpotsFound, "XSDataInteger")
		self.__numSpotsFound = numSpotsFound
	def delNumSpotsFound(self): self.__numSpotsFound = None
	# Properties
	numSpotsFound = property(getNumSpotsFound, setNumSpotsFound, delNumSpotsFound, "Property for numSpotsFound")
	def getNumSpotsUsed(self): return self.__numSpotsUsed
	def setNumSpotsUsed(self, numSpotsUsed):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsUsed", numSpotsUsed, "XSDataInteger")
		self.__numSpotsUsed = numSpotsUsed
	def delNumSpotsUsed(self): self.__numSpotsUsed = None
	# Properties
	numSpotsUsed = property(getNumSpotsUsed, setNumSpotsUsed, delNumSpotsUsed, "Property for numSpotsUsed")
	def getNumSpotsRejected(self): return self.__numSpotsRejected
	def setNumSpotsRejected(self, numSpotsRejected):
		checkType("XSDataISPyBScreeningOutput", "setNumSpotsRejected", numSpotsRejected, "XSDataInteger")
		self.__numSpotsRejected = numSpotsRejected
	def delNumSpotsRejected(self): self.__numSpotsRejected = None
	# Properties
	numSpotsRejected = property(getNumSpotsRejected, setNumSpotsRejected, delNumSpotsRejected, "Property for numSpotsRejected")
	def getMosaicity(self): return self.__mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataISPyBScreeningOutput", "setMosaicity", mosaicity, "XSDataFloat")
		self.__mosaicity = mosaicity
	def delMosaicity(self): self.__mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getIOverSigma(self): return self.__iOverSigma
	def setIOverSigma(self, iOverSigma):
		checkType("XSDataISPyBScreeningOutput", "setIOverSigma", iOverSigma, "XSDataFloat")
		self.__iOverSigma = iOverSigma
	def delIOverSigma(self): self.__iOverSigma = None
	# Properties
	iOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for iOverSigma")
	def getDiffractionRings(self): return self.__diffractionRings
	def setDiffractionRings(self, diffractionRings):
		checkType("XSDataISPyBScreeningOutput", "setDiffractionRings", diffractionRings, "XSDataBoolean")
		self.__diffractionRings = diffractionRings
	def delDiffractionRings(self): self.__diffractionRings = None
	# Properties
	diffractionRings = property(getDiffractionRings, setDiffractionRings, delDiffractionRings, "Property for diffractionRings")
	def getScreeningSuccess(self): return self.__screeningSuccess
	def setScreeningSuccess(self, screeningSuccess):
		checkType("XSDataISPyBScreeningOutput", "setScreeningSuccess", screeningSuccess, "XSDataBoolean")
		self.__screeningSuccess = screeningSuccess
	def delScreeningSuccess(self): self.__screeningSuccess = None
	# Properties
	screeningSuccess = property(getScreeningSuccess, setScreeningSuccess, delScreeningSuccess, "Property for screeningSuccess")
	def getMosaicityEstimated(self): return self.__mosaicityEstimated
	def setMosaicityEstimated(self, mosaicityEstimated):
		checkType("XSDataISPyBScreeningOutput", "setMosaicityEstimated", mosaicityEstimated, "XSDataBoolean")
		self.__mosaicityEstimated = mosaicityEstimated
	def delMosaicityEstimated(self): self.__mosaicityEstimated = None
	# Properties
	mosaicityEstimated = property(getMosaicityEstimated, setMosaicityEstimated, delMosaicityEstimated, "Property for mosaicityEstimated")
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__statusDescription is not None:
			self.statusDescription.export(outfile, level, name_='statusDescription')
		else:
			warnEmptyAttribute("statusDescription", "XSDataString")
		if self.__rejectedReflections is not None:
			self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
		else:
			warnEmptyAttribute("rejectedReflections", "XSDataInteger")
		if self.__resolutionObtained is not None:
			self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
		else:
			warnEmptyAttribute("resolutionObtained", "XSDataFloat")
		if self.__spotDeviationR is not None:
			self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
		else:
			warnEmptyAttribute("spotDeviationR", "XSDataFloat")
		if self.__spotDeviationTheta is not None:
			self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
		else:
			warnEmptyAttribute("spotDeviationTheta", "XSDataFloat")
		if self.__beamShiftX is not None:
			self.beamShiftX.export(outfile, level, name_='beamShiftX')
		else:
			warnEmptyAttribute("beamShiftX", "XSDataFloat")
		if self.__beamShiftY is not None:
			self.beamShiftY.export(outfile, level, name_='beamShiftY')
		else:
			warnEmptyAttribute("beamShiftY", "XSDataFloat")
		if self.__numSpotsFound is not None:
			self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
		else:
			warnEmptyAttribute("numSpotsFound", "XSDataInteger")
		if self.__numSpotsUsed is not None:
			self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
		else:
			warnEmptyAttribute("numSpotsUsed", "XSDataInteger")
		if self.__numSpotsRejected is not None:
			self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
		else:
			warnEmptyAttribute("numSpotsRejected", "XSDataInteger")
		if self.__mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		else:
			warnEmptyAttribute("mosaicity", "XSDataFloat")
		if self.__iOverSigma is not None:
			self.iOverSigma.export(outfile, level, name_='iOverSigma')
		else:
			warnEmptyAttribute("iOverSigma", "XSDataFloat")
		if self.__diffractionRings is not None:
			self.diffractionRings.export(outfile, level, name_='diffractionRings')
		else:
			warnEmptyAttribute("diffractionRings", "XSDataBoolean")
		if self.__screeningSuccess is not None:
			self.screeningSuccess.export(outfile, level, name_='screeningSuccess')
		else:
			warnEmptyAttribute("screeningSuccess", "XSDataBoolean")
		if self.__mosaicityEstimated is not None:
			self.mosaicityEstimated.export(outfile, level, name_='mosaicityEstimated')
		else:
			warnEmptyAttribute("mosaicityEstimated", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statusDescription':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setStatusDescription(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rejectedReflections':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRejectedReflections(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolutionObtained':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setResolutionObtained(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationR':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSpotDeviationR(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotDeviationTheta':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setSpotDeviationTheta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShiftX':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamShiftX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamShiftY':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setBeamShiftY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsFound':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsFound(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsUsed':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsUsed(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numSpotsRejected':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumSpotsRejected(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iOverSigma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setIOverSigma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'diffractionRings':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDiffractionRings(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningSuccess':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setScreeningSuccess(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicityEstimated':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setMosaicityEstimated(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutput

class XSDataISPyBScreeningOutputLattice(XSData):
	def __init__(self, timeStamp=None, unitCell_gamma=None, unitCell_beta=None, unitCell_alpha=None, unitCell_c=None, unitCell_b=None, unitCell_a=None, rawOrientationMatrix_c_z=None, rawOrientationMatrix_c_y=None, rawOrientationMatrix_c_x=None, rawOrientationMatrix_b_z=None, rawOrientationMatrix_b_y=None, rawOrientationMatrix_b_x=None, rawOrientationMatrix_a_z=None, rawOrientationMatrix_a_y=None, rawOrientationMatrix_a_x=None, bravaisLattice=None, pointGroup=None, spaceGroup=None, screeningOutputId=None, screeningOutputLatticeId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", spaceGroup, "XSDataString")
		self.__spaceGroup = spaceGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", pointGroup, "XSDataString")
		self.__pointGroup = pointGroup
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_x, "XSDataFloat")
		self.__rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_y, "XSDataFloat")
		self.__rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_a_z, "XSDataFloat")
		self.__rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_x, "XSDataFloat")
		self.__rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_y, "XSDataFloat")
		self.__rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_b_z, "XSDataFloat")
		self.__rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_x, "XSDataFloat")
		self.__rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_y, "XSDataFloat")
		self.__rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", rawOrientationMatrix_c_z, "XSDataFloat")
		self.__rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_a, "XSDataFloat")
		self.__unitCell_a = unitCell_a
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_b, "XSDataFloat")
		self.__unitCell_b = unitCell_b
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_c, "XSDataFloat")
		self.__unitCell_c = unitCell_c
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_alpha, "XSDataFloat")
		self.__unitCell_alpha = unitCell_alpha
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_beta, "XSDataFloat")
		self.__unitCell_beta = unitCell_beta
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", unitCell_gamma, "XSDataFloat")
		self.__unitCell_gamma = unitCell_gamma
		checkType("XSDataISPyBScreeningOutputLattice", "Constructor of XSDataISPyBScreeningOutputLattice", timeStamp, "XSDataFloat")
		self.__timeStamp = timeStamp
	def getScreeningOutputLatticeId(self): return self.__screeningOutputLatticeId
	def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputLatticeId", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
	def delScreeningOutputLatticeId(self): self.__screeningOutputLatticeId = None
	# Properties
	screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningOutputLattice", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getSpaceGroup(self): return self.__spaceGroup
	def setSpaceGroup(self, spaceGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setSpaceGroup", spaceGroup, "XSDataString")
		self.__spaceGroup = spaceGroup
	def delSpaceGroup(self): self.__spaceGroup = None
	# Properties
	spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
	def getPointGroup(self): return self.__pointGroup
	def setPointGroup(self, pointGroup):
		checkType("XSDataISPyBScreeningOutputLattice", "setPointGroup", pointGroup, "XSDataString")
		self.__pointGroup = pointGroup
	def delPointGroup(self): self.__pointGroup = None
	# Properties
	pointGroup = property(getPointGroup, setPointGroup, delPointGroup, "Property for pointGroup")
	def getBravaisLattice(self): return self.__bravaisLattice
	def setBravaisLattice(self, bravaisLattice):
		checkType("XSDataISPyBScreeningOutputLattice", "setBravaisLattice", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
	def delBravaisLattice(self): self.__bravaisLattice = None
	# Properties
	bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
	def getRawOrientationMatrix_a_x(self): return self.__rawOrientationMatrix_a_x
	def setRawOrientationMatrix_a_x(self, rawOrientationMatrix_a_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_x", rawOrientationMatrix_a_x, "XSDataFloat")
		self.__rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
	def delRawOrientationMatrix_a_x(self): self.__rawOrientationMatrix_a_x = None
	# Properties
	rawOrientationMatrix_a_x = property(getRawOrientationMatrix_a_x, setRawOrientationMatrix_a_x, delRawOrientationMatrix_a_x, "Property for rawOrientationMatrix_a_x")
	def getRawOrientationMatrix_a_y(self): return self.__rawOrientationMatrix_a_y
	def setRawOrientationMatrix_a_y(self, rawOrientationMatrix_a_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_y", rawOrientationMatrix_a_y, "XSDataFloat")
		self.__rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
	def delRawOrientationMatrix_a_y(self): self.__rawOrientationMatrix_a_y = None
	# Properties
	rawOrientationMatrix_a_y = property(getRawOrientationMatrix_a_y, setRawOrientationMatrix_a_y, delRawOrientationMatrix_a_y, "Property for rawOrientationMatrix_a_y")
	def getRawOrientationMatrix_a_z(self): return self.__rawOrientationMatrix_a_z
	def setRawOrientationMatrix_a_z(self, rawOrientationMatrix_a_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_a_z", rawOrientationMatrix_a_z, "XSDataFloat")
		self.__rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
	def delRawOrientationMatrix_a_z(self): self.__rawOrientationMatrix_a_z = None
	# Properties
	rawOrientationMatrix_a_z = property(getRawOrientationMatrix_a_z, setRawOrientationMatrix_a_z, delRawOrientationMatrix_a_z, "Property for rawOrientationMatrix_a_z")
	def getRawOrientationMatrix_b_x(self): return self.__rawOrientationMatrix_b_x
	def setRawOrientationMatrix_b_x(self, rawOrientationMatrix_b_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_x", rawOrientationMatrix_b_x, "XSDataFloat")
		self.__rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
	def delRawOrientationMatrix_b_x(self): self.__rawOrientationMatrix_b_x = None
	# Properties
	rawOrientationMatrix_b_x = property(getRawOrientationMatrix_b_x, setRawOrientationMatrix_b_x, delRawOrientationMatrix_b_x, "Property for rawOrientationMatrix_b_x")
	def getRawOrientationMatrix_b_y(self): return self.__rawOrientationMatrix_b_y
	def setRawOrientationMatrix_b_y(self, rawOrientationMatrix_b_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_y", rawOrientationMatrix_b_y, "XSDataFloat")
		self.__rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
	def delRawOrientationMatrix_b_y(self): self.__rawOrientationMatrix_b_y = None
	# Properties
	rawOrientationMatrix_b_y = property(getRawOrientationMatrix_b_y, setRawOrientationMatrix_b_y, delRawOrientationMatrix_b_y, "Property for rawOrientationMatrix_b_y")
	def getRawOrientationMatrix_b_z(self): return self.__rawOrientationMatrix_b_z
	def setRawOrientationMatrix_b_z(self, rawOrientationMatrix_b_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_b_z", rawOrientationMatrix_b_z, "XSDataFloat")
		self.__rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
	def delRawOrientationMatrix_b_z(self): self.__rawOrientationMatrix_b_z = None
	# Properties
	rawOrientationMatrix_b_z = property(getRawOrientationMatrix_b_z, setRawOrientationMatrix_b_z, delRawOrientationMatrix_b_z, "Property for rawOrientationMatrix_b_z")
	def getRawOrientationMatrix_c_x(self): return self.__rawOrientationMatrix_c_x
	def setRawOrientationMatrix_c_x(self, rawOrientationMatrix_c_x):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_x", rawOrientationMatrix_c_x, "XSDataFloat")
		self.__rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
	def delRawOrientationMatrix_c_x(self): self.__rawOrientationMatrix_c_x = None
	# Properties
	rawOrientationMatrix_c_x = property(getRawOrientationMatrix_c_x, setRawOrientationMatrix_c_x, delRawOrientationMatrix_c_x, "Property for rawOrientationMatrix_c_x")
	def getRawOrientationMatrix_c_y(self): return self.__rawOrientationMatrix_c_y
	def setRawOrientationMatrix_c_y(self, rawOrientationMatrix_c_y):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_y", rawOrientationMatrix_c_y, "XSDataFloat")
		self.__rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
	def delRawOrientationMatrix_c_y(self): self.__rawOrientationMatrix_c_y = None
	# Properties
	rawOrientationMatrix_c_y = property(getRawOrientationMatrix_c_y, setRawOrientationMatrix_c_y, delRawOrientationMatrix_c_y, "Property for rawOrientationMatrix_c_y")
	def getRawOrientationMatrix_c_z(self): return self.__rawOrientationMatrix_c_z
	def setRawOrientationMatrix_c_z(self, rawOrientationMatrix_c_z):
		checkType("XSDataISPyBScreeningOutputLattice", "setRawOrientationMatrix_c_z", rawOrientationMatrix_c_z, "XSDataFloat")
		self.__rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
	def delRawOrientationMatrix_c_z(self): self.__rawOrientationMatrix_c_z = None
	# Properties
	rawOrientationMatrix_c_z = property(getRawOrientationMatrix_c_z, setRawOrientationMatrix_c_z, delRawOrientationMatrix_c_z, "Property for rawOrientationMatrix_c_z")
	def getUnitCell_a(self): return self.__unitCell_a
	def setUnitCell_a(self, unitCell_a):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_a", unitCell_a, "XSDataFloat")
		self.__unitCell_a = unitCell_a
	def delUnitCell_a(self): self.__unitCell_a = None
	# Properties
	unitCell_a = property(getUnitCell_a, setUnitCell_a, delUnitCell_a, "Property for unitCell_a")
	def getUnitCell_b(self): return self.__unitCell_b
	def setUnitCell_b(self, unitCell_b):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_b", unitCell_b, "XSDataFloat")
		self.__unitCell_b = unitCell_b
	def delUnitCell_b(self): self.__unitCell_b = None
	# Properties
	unitCell_b = property(getUnitCell_b, setUnitCell_b, delUnitCell_b, "Property for unitCell_b")
	def getUnitCell_c(self): return self.__unitCell_c
	def setUnitCell_c(self, unitCell_c):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_c", unitCell_c, "XSDataFloat")
		self.__unitCell_c = unitCell_c
	def delUnitCell_c(self): self.__unitCell_c = None
	# Properties
	unitCell_c = property(getUnitCell_c, setUnitCell_c, delUnitCell_c, "Property for unitCell_c")
	def getUnitCell_alpha(self): return self.__unitCell_alpha
	def setUnitCell_alpha(self, unitCell_alpha):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_alpha", unitCell_alpha, "XSDataFloat")
		self.__unitCell_alpha = unitCell_alpha
	def delUnitCell_alpha(self): self.__unitCell_alpha = None
	# Properties
	unitCell_alpha = property(getUnitCell_alpha, setUnitCell_alpha, delUnitCell_alpha, "Property for unitCell_alpha")
	def getUnitCell_beta(self): return self.__unitCell_beta
	def setUnitCell_beta(self, unitCell_beta):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_beta", unitCell_beta, "XSDataFloat")
		self.__unitCell_beta = unitCell_beta
	def delUnitCell_beta(self): self.__unitCell_beta = None
	# Properties
	unitCell_beta = property(getUnitCell_beta, setUnitCell_beta, delUnitCell_beta, "Property for unitCell_beta")
	def getUnitCell_gamma(self): return self.__unitCell_gamma
	def setUnitCell_gamma(self, unitCell_gamma):
		checkType("XSDataISPyBScreeningOutputLattice", "setUnitCell_gamma", unitCell_gamma, "XSDataFloat")
		self.__unitCell_gamma = unitCell_gamma
	def delUnitCell_gamma(self): self.__unitCell_gamma = None
	# Properties
	unitCell_gamma = property(getUnitCell_gamma, setUnitCell_gamma, delUnitCell_gamma, "Property for unitCell_gamma")
	def getTimeStamp(self): return self.__timeStamp
	def setTimeStamp(self, timeStamp):
		checkType("XSDataISPyBScreeningOutputLattice", "setTimeStamp", timeStamp, "XSDataFloat")
		self.__timeStamp = timeStamp
	def delTimeStamp(self): self.__timeStamp = None
	# Properties
	timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
	def export(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningOutputLatticeId is not None:
			self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
		else:
			warnEmptyAttribute("screeningOutputLatticeId", "XSDataInteger")
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__spaceGroup is not None:
			self.spaceGroup.export(outfile, level, name_='spaceGroup')
		else:
			warnEmptyAttribute("spaceGroup", "XSDataString")
		if self.__pointGroup is not None:
			self.pointGroup.export(outfile, level, name_='pointGroup')
		else:
			warnEmptyAttribute("pointGroup", "XSDataString")
		if self.__bravaisLattice is not None:
			self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
		else:
			warnEmptyAttribute("bravaisLattice", "XSDataString")
		if self.__rawOrientationMatrix_a_x is not None:
			self.rawOrientationMatrix_a_x.export(outfile, level, name_='rawOrientationMatrix_a_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_x", "XSDataFloat")
		if self.__rawOrientationMatrix_a_y is not None:
			self.rawOrientationMatrix_a_y.export(outfile, level, name_='rawOrientationMatrix_a_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_y", "XSDataFloat")
		if self.__rawOrientationMatrix_a_z is not None:
			self.rawOrientationMatrix_a_z.export(outfile, level, name_='rawOrientationMatrix_a_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_a_z", "XSDataFloat")
		if self.__rawOrientationMatrix_b_x is not None:
			self.rawOrientationMatrix_b_x.export(outfile, level, name_='rawOrientationMatrix_b_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_x", "XSDataFloat")
		if self.__rawOrientationMatrix_b_y is not None:
			self.rawOrientationMatrix_b_y.export(outfile, level, name_='rawOrientationMatrix_b_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_y", "XSDataFloat")
		if self.__rawOrientationMatrix_b_z is not None:
			self.rawOrientationMatrix_b_z.export(outfile, level, name_='rawOrientationMatrix_b_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_b_z", "XSDataFloat")
		if self.__rawOrientationMatrix_c_x is not None:
			self.rawOrientationMatrix_c_x.export(outfile, level, name_='rawOrientationMatrix_c_x')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_x", "XSDataFloat")
		if self.__rawOrientationMatrix_c_y is not None:
			self.rawOrientationMatrix_c_y.export(outfile, level, name_='rawOrientationMatrix_c_y')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_y", "XSDataFloat")
		if self.__rawOrientationMatrix_c_z is not None:
			self.rawOrientationMatrix_c_z.export(outfile, level, name_='rawOrientationMatrix_c_z')
		else:
			warnEmptyAttribute("rawOrientationMatrix_c_z", "XSDataFloat")
		if self.__unitCell_a is not None:
			self.unitCell_a.export(outfile, level, name_='unitCell_a')
		else:
			warnEmptyAttribute("unitCell_a", "XSDataFloat")
		if self.__unitCell_b is not None:
			self.unitCell_b.export(outfile, level, name_='unitCell_b')
		else:
			warnEmptyAttribute("unitCell_b", "XSDataFloat")
		if self.__unitCell_c is not None:
			self.unitCell_c.export(outfile, level, name_='unitCell_c')
		else:
			warnEmptyAttribute("unitCell_c", "XSDataFloat")
		if self.__unitCell_alpha is not None:
			self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
		else:
			warnEmptyAttribute("unitCell_alpha", "XSDataFloat")
		if self.__unitCell_beta is not None:
			self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
		else:
			warnEmptyAttribute("unitCell_beta", "XSDataFloat")
		if self.__unitCell_gamma is not None:
			self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
		else:
			warnEmptyAttribute("unitCell_gamma", "XSDataFloat")
		if self.__timeStamp is not None:
			self.timeStamp.export(outfile, level, name_='timeStamp')
		else:
			warnEmptyAttribute("timeStamp", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLatticeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputLatticeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spaceGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSpaceGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pointGroup':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPointGroup(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bravaisLattice':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBravaisLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_x':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_y':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_a_z':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_a_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_x':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_y':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_b_z':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_b_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_x':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_x(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_y':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_y(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rawOrientationMatrix_c_z':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRawOrientationMatrix_c_z(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_a':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_a(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_b':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_b(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_c':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_c(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_alpha':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_alpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_beta':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_beta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell_gamma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setUnitCell_gamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'timeStamp':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setTimeStamp(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningOutputLattice' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningOutputLattice is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningOutputLattice.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputLattice()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningOutputLattice()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutputLattice

class XSDataISPyBScreeningRank(XSData):
	def __init__(self, rankInformation=None, rankValue=None, screeningId=None, screeningRankSetId=None, screeningRankId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankValue, "XSDataFloat")
		self.__rankValue = rankValue
		checkType("XSDataISPyBScreeningRank", "Constructor of XSDataISPyBScreeningRank", rankInformation, "XSDataString")
		self.__rankInformation = rankInformation
	def getScreeningRankId(self): return self.__screeningRankId
	def setScreeningRankId(self, screeningRankId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankId", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
	def delScreeningRankId(self): self.__screeningRankId = None
	# Properties
	screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRank", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataISPyBScreeningRank", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getRankValue(self): return self.__rankValue
	def setRankValue(self, rankValue):
		checkType("XSDataISPyBScreeningRank", "setRankValue", rankValue, "XSDataFloat")
		self.__rankValue = rankValue
	def delRankValue(self): self.__rankValue = None
	# Properties
	rankValue = property(getRankValue, setRankValue, delRankValue, "Property for rankValue")
	def getRankInformation(self): return self.__rankInformation
	def setRankInformation(self, rankInformation):
		checkType("XSDataISPyBScreeningRank", "setRankInformation", rankInformation, "XSDataString")
		self.__rankInformation = rankInformation
	def delRankInformation(self): self.__rankInformation = None
	# Properties
	rankInformation = property(getRankInformation, setRankInformation, delRankInformation, "Property for rankInformation")
	def export(self, outfile, level, name_='XSDataISPyBScreeningRank'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRank'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningRankId is not None:
			self.screeningRankId.export(outfile, level, name_='screeningRankId')
		else:
			warnEmptyAttribute("screeningRankId", "XSDataInteger")
		if self.__screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__rankValue is not None:
			self.rankValue.export(outfile, level, name_='rankValue')
		else:
			warnEmptyAttribute("rankValue", "XSDataFloat")
		if self.__rankInformation is not None:
			self.rankInformation.export(outfile, level, name_='rankInformation')
		else:
			warnEmptyAttribute("rankInformation", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankSetId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankValue':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRankValue(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankInformation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankInformation(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningRank' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningRank is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningRank.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRank()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRank()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRank

class XSDataISPyBScreeningRankSet(XSData):
	def __init__(self, rankingSummaryFileName=None, rankingProjectFileName=None, rankEngine=None, screeningRankSetId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankEngine, "XSDataString")
		self.__rankEngine = rankEngine
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingProjectFileName, "XSDataString")
		self.__rankingProjectFileName = rankingProjectFileName
		checkType("XSDataISPyBScreeningRankSet", "Constructor of XSDataISPyBScreeningRankSet", rankingSummaryFileName, "XSDataString")
		self.__rankingSummaryFileName = rankingSummaryFileName
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataISPyBScreeningRankSet", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getRankEngine(self): return self.__rankEngine
	def setRankEngine(self, rankEngine):
		checkType("XSDataISPyBScreeningRankSet", "setRankEngine", rankEngine, "XSDataString")
		self.__rankEngine = rankEngine
	def delRankEngine(self): self.__rankEngine = None
	# Properties
	rankEngine = property(getRankEngine, setRankEngine, delRankEngine, "Property for rankEngine")
	def getRankingProjectFileName(self): return self.__rankingProjectFileName
	def setRankingProjectFileName(self, rankingProjectFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingProjectFileName", rankingProjectFileName, "XSDataString")
		self.__rankingProjectFileName = rankingProjectFileName
	def delRankingProjectFileName(self): self.__rankingProjectFileName = None
	# Properties
	rankingProjectFileName = property(getRankingProjectFileName, setRankingProjectFileName, delRankingProjectFileName, "Property for rankingProjectFileName")
	def getRankingSummaryFileName(self): return self.__rankingSummaryFileName
	def setRankingSummaryFileName(self, rankingSummaryFileName):
		checkType("XSDataISPyBScreeningRankSet", "setRankingSummaryFileName", rankingSummaryFileName, "XSDataString")
		self.__rankingSummaryFileName = rankingSummaryFileName
	def delRankingSummaryFileName(self): self.__rankingSummaryFileName = None
	# Properties
	rankingSummaryFileName = property(getRankingSummaryFileName, setRankingSummaryFileName, delRankingSummaryFileName, "Property for rankingSummaryFileName")
	def export(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self.__rankEngine is not None:
			self.rankEngine.export(outfile, level, name_='rankEngine')
		else:
			warnEmptyAttribute("rankEngine", "XSDataString")
		if self.__rankingProjectFileName is not None:
			self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
		else:
			warnEmptyAttribute("rankingProjectFileName", "XSDataString")
		if self.__rankingSummaryFileName is not None:
			self.rankingSummaryFileName.export(outfile, level, name_='rankingSummaryFileName')
		else:
			warnEmptyAttribute("rankingSummaryFileName", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankSetId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankEngine':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankEngine(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingProjectFileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankingProjectFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingSummaryFileName':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setRankingSummaryFileName(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningRankSet' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningRankSet is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningRankSet.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRankSet()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningRankSet()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRankSet

class XSDataISPyBScreeningStrategy(XSData):
	def __init__(self, rankingResolution=None, program=None, anomalous=None, multiplicity=None, completeness=None, resolution=None, exposureTime=None, rotation=None, phiEnd=None, phiStart=None, screeningOutputId=None, screeningStrategyId=None):
		XSData.__init__(self, )
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiStart, "XSDataFloat")
		self.__phiStart = phiStart
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", phiEnd, "XSDataFloat")
		self.__phiEnd = phiEnd
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rotation, "XSDataFloat")
		self.__rotation = rotation
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", exposureTime, "XSDataFloat")
		self.__exposureTime = exposureTime
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", resolution, "XSDataFloat")
		self.__resolution = resolution
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", completeness, "XSDataFloat")
		self.__completeness = completeness
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", multiplicity, "XSDataFloat")
		self.__multiplicity = multiplicity
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", anomalous, "XSDataBoolean")
		self.__anomalous = anomalous
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", program, "XSDataString")
		self.__program = program
		checkType("XSDataISPyBScreeningStrategy", "Constructor of XSDataISPyBScreeningStrategy", rankingResolution, "XSDataFloat")
		self.__rankingResolution = rankingResolution
	def getScreeningStrategyId(self): return self.__screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self.__screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataISPyBScreeningStrategy", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getPhiStart(self): return self.__phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataISPyBScreeningStrategy", "setPhiStart", phiStart, "XSDataFloat")
		self.__phiStart = phiStart
	def delPhiStart(self): self.__phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getPhiEnd(self): return self.__phiEnd
	def setPhiEnd(self, phiEnd):
		checkType("XSDataISPyBScreeningStrategy", "setPhiEnd", phiEnd, "XSDataFloat")
		self.__phiEnd = phiEnd
	def delPhiEnd(self): self.__phiEnd = None
	# Properties
	phiEnd = property(getPhiEnd, setPhiEnd, delPhiEnd, "Property for phiEnd")
	def getRotation(self): return self.__rotation
	def setRotation(self, rotation):
		checkType("XSDataISPyBScreeningStrategy", "setRotation", rotation, "XSDataFloat")
		self.__rotation = rotation
	def delRotation(self): self.__rotation = None
	# Properties
	rotation = property(getRotation, setRotation, delRotation, "Property for rotation")
	def getExposureTime(self): return self.__exposureTime
	def setExposureTime(self, exposureTime):
		checkType("XSDataISPyBScreeningStrategy", "setExposureTime", exposureTime, "XSDataFloat")
		self.__exposureTime = exposureTime
	def delExposureTime(self): self.__exposureTime = None
	# Properties
	exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataISPyBScreeningStrategy", "setResolution", resolution, "XSDataFloat")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("XSDataISPyBScreeningStrategy", "setCompleteness", completeness, "XSDataFloat")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getMultiplicity(self): return self.__multiplicity
	def setMultiplicity(self, multiplicity):
		checkType("XSDataISPyBScreeningStrategy", "setMultiplicity", multiplicity, "XSDataFloat")
		self.__multiplicity = multiplicity
	def delMultiplicity(self): self.__multiplicity = None
	# Properties
	multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
	def getAnomalous(self): return self.__anomalous
	def setAnomalous(self, anomalous):
		checkType("XSDataISPyBScreeningStrategy", "setAnomalous", anomalous, "XSDataBoolean")
		self.__anomalous = anomalous
	def delAnomalous(self): self.__anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
	def getProgram(self): return self.__program
	def setProgram(self, program):
		checkType("XSDataISPyBScreeningStrategy", "setProgram", program, "XSDataString")
		self.__program = program
	def delProgram(self): self.__program = None
	# Properties
	program = property(getProgram, setProgram, delProgram, "Property for program")
	def getRankingResolution(self): return self.__rankingResolution
	def setRankingResolution(self, rankingResolution):
		checkType("XSDataISPyBScreeningStrategy", "setRankingResolution", rankingResolution, "XSDataFloat")
		self.__rankingResolution = rankingResolution
	def delRankingResolution(self): self.__rankingResolution = None
	# Properties
	rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
	def export(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		else:
			warnEmptyAttribute("screeningStrategyId", "XSDataInteger")
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__phiStart is not None:
			self.phiStart.export(outfile, level, name_='phiStart')
		else:
			warnEmptyAttribute("phiStart", "XSDataFloat")
		if self.__phiEnd is not None:
			self.phiEnd.export(outfile, level, name_='phiEnd')
		else:
			warnEmptyAttribute("phiEnd", "XSDataFloat")
		if self.__rotation is not None:
			self.rotation.export(outfile, level, name_='rotation')
		else:
			warnEmptyAttribute("rotation", "XSDataFloat")
		if self.__exposureTime is not None:
			self.exposureTime.export(outfile, level, name_='exposureTime')
		else:
			warnEmptyAttribute("exposureTime", "XSDataFloat")
		if self.__resolution is not None:
			self.resolution.export(outfile, level, name_='resolution')
		else:
			warnEmptyAttribute("resolution", "XSDataFloat")
		if self.__completeness is not None:
			self.completeness.export(outfile, level, name_='completeness')
		else:
			warnEmptyAttribute("completeness", "XSDataFloat")
		if self.__multiplicity is not None:
			self.multiplicity.export(outfile, level, name_='multiplicity')
		else:
			warnEmptyAttribute("multiplicity", "XSDataFloat")
		if self.__anomalous is not None:
			self.anomalous.export(outfile, level, name_='anomalous')
		else:
			warnEmptyAttribute("anomalous", "XSDataBoolean")
		if self.__program is not None:
			self.program.export(outfile, level, name_='program')
		else:
			warnEmptyAttribute("program", "XSDataString")
		if self.__rankingResolution is not None:
			self.rankingResolution.export(outfile, level, name_='rankingResolution')
		else:
			warnEmptyAttribute("rankingResolution", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setPhiStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiEnd':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setPhiEnd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRotation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposureTime':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setExposureTime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setResolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCompleteness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'multiplicity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setMultiplicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalous':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAnomalous(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'program':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setProgram(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rankingResolution':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRankingResolution(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataISPyBScreeningStrategy' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategy is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataISPyBScreeningStrategy.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategy()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataISPyBScreeningStrategy()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategy

class XSDataResultStatus(XSData):
	def __init__(self, message=None, code=None, screeningObject=None):
		XSData.__init__(self, )
		checkType("XSDataResultStatus", "Constructor of XSDataResultStatus", screeningObject, "XSData")
		self.__screeningObject = screeningObject
		checkType("XSDataResultStatus", "Constructor of XSDataResultStatus", code, "XSDataString")
		self.__code = code
		checkType("XSDataResultStatus", "Constructor of XSDataResultStatus", message, "XSDataString")
		self.__message = message
	def getScreeningObject(self): return self.__screeningObject
	def setScreeningObject(self, screeningObject):
		checkType("XSDataResultStatus", "setScreeningObject", screeningObject, "XSData")
		self.__screeningObject = screeningObject
	def delScreeningObject(self): self.__screeningObject = None
	# Properties
	screeningObject = property(getScreeningObject, setScreeningObject, delScreeningObject, "Property for screeningObject")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDataResultStatus", "setCode", code, "XSDataString")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def getMessage(self): return self.__message
	def setMessage(self, message):
		checkType("XSDataResultStatus", "setMessage", message, "XSDataString")
		self.__message = message
	def delMessage(self): self.__message = None
	# Properties
	message = property(getMessage, setMessage, delMessage, "Property for message")
	def export(self, outfile, level, name_='XSDataResultStatus'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultStatus'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningObject is not None:
			self.screeningObject.export(outfile, level, name_='screeningObject')
		else:
			warnEmptyAttribute("screeningObject", "XSData")
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
		else:
			warnEmptyAttribute("code", "XSDataString")
		if self.__message is not None:
			self.message.export(outfile, level, name_='message')
		else:
			warnEmptyAttribute("message", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningObject':
			obj_ = XSData()
			obj_.build(child_)
			self.setScreeningObject(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'message':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMessage(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultStatus" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultStatus' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultStatus is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultStatus.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultStatus()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultStatus" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultStatus()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultStatus

class XSDatadbstatus(XSData):
	def __init__(self, message=None, code=None, screeningRankSetId=None, screeningRankId=None, screeningStrategyId=None, screeningOutputLatticeId=None, screeningOutputId=None, screeningInputId=None, screeningId=None):
		XSData.__init__(self, )
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningId, "integer")
		self.__screeningId = screeningId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningInputId, "integer")
		self.__screeningInputId = screeningInputId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningOutputId, "integer")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningOutputLatticeId, "integer")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningStrategyId, "integer")
		self.__screeningStrategyId = screeningStrategyId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningRankId, "integer")
		self.__screeningRankId = screeningRankId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", screeningRankSetId, "integer")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", code, "string")
		self.__code = code
		checkType("XSDatadbstatus", "Constructor of XSDatadbstatus", message, "string")
		self.__message = message
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDatadbstatus", "setScreeningId", screeningId, "integer")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getScreeningInputId(self): return self.__screeningInputId
	def setScreeningInputId(self, screeningInputId):
		checkType("XSDatadbstatus", "setScreeningInputId", screeningInputId, "integer")
		self.__screeningInputId = screeningInputId
	def delScreeningInputId(self): self.__screeningInputId = None
	# Properties
	screeningInputId = property(getScreeningInputId, setScreeningInputId, delScreeningInputId, "Property for screeningInputId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDatadbstatus", "setScreeningOutputId", screeningOutputId, "integer")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getScreeningOutputLatticeId(self): return self.__screeningOutputLatticeId
	def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
		checkType("XSDatadbstatus", "setScreeningOutputLatticeId", screeningOutputLatticeId, "integer")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
	def delScreeningOutputLatticeId(self): self.__screeningOutputLatticeId = None
	# Properties
	screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
	def getScreeningStrategyId(self): return self.__screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDatadbstatus", "setScreeningStrategyId", screeningStrategyId, "integer")
		self.__screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self.__screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getScreeningRankId(self): return self.__screeningRankId
	def setScreeningRankId(self, screeningRankId):
		checkType("XSDatadbstatus", "setScreeningRankId", screeningRankId, "integer")
		self.__screeningRankId = screeningRankId
	def delScreeningRankId(self): self.__screeningRankId = None
	# Properties
	screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDatadbstatus", "setScreeningRankSetId", screeningRankSetId, "integer")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("XSDatadbstatus", "setCode", code, "string")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def getMessage(self): return self.__message
	def setMessage(self, message):
		checkType("XSDatadbstatus", "setMessage", message, "string")
		self.__message = message
	def delMessage(self): self.__message = None
	# Properties
	message = property(getMessage, setMessage, delMessage, "Property for message")
	def export(self, outfile, level, name_='XSDatadbstatus'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDatadbstatus'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__screeningId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningId>%d</screeningId>\n' % self.__screeningId))
		else:
			warnEmptyAttribute("screeningId", "integer")
		if self.__screeningInputId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningInputId>%d</screeningInputId>\n' % self.__screeningInputId))
		else:
			warnEmptyAttribute("screeningInputId", "integer")
		if self.__screeningOutputId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningOutputId>%d</screeningOutputId>\n' % self.__screeningOutputId))
		else:
			warnEmptyAttribute("screeningOutputId", "integer")
		if self.__screeningOutputLatticeId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningOutputLatticeId>%d</screeningOutputLatticeId>\n' % self.__screeningOutputLatticeId))
		else:
			warnEmptyAttribute("screeningOutputLatticeId", "integer")
		if self.__screeningStrategyId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningStrategyId>%d</screeningStrategyId>\n' % self.__screeningStrategyId))
		else:
			warnEmptyAttribute("screeningStrategyId", "integer")
		if self.__screeningRankId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningRankId>%d</screeningRankId>\n' % self.__screeningRankId))
		else:
			warnEmptyAttribute("screeningRankId", "integer")
		if self.__screeningRankSetId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<screeningRankSetId>%d</screeningRankSetId>\n' % self.__screeningRankSetId))
		else:
			warnEmptyAttribute("screeningRankSetId", "integer")
		if self.__code is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<code>%s</code>\n' % self.__code))
		else:
			warnEmptyAttribute("code", "string")
		if self.__message is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<message>%s</message>\n' % self.__message))
		else:
			warnEmptyAttribute("message", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInputId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningInputId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningOutputId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLatticeId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningOutputLatticeId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningStrategyId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningRankId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__screeningRankSetId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__code = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'message':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__message = value_
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDatadbstatus" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDatadbstatus' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDatadbstatus is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDatadbstatus.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDatadbstatus()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDatadbstatus" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDatadbstatus()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDatadbstatus

class XSDataInputISPyB(XSDataInput):
	def __init__(self, configuration=None, image=None, screeningStrategy=None, screeningOutputLattice=None, screeningRankSet=None, screeningRank=None, screeningOutput=None, screeningInput=None, screening=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screening, "XSDataISPyBScreening")
		self.__screening = screening
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningOutput, "XSDataISPyBScreeningOutput")
		self.__screeningOutput = screeningOutput
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningRank, "XSDataISPyBScreeningRank")
		self.__screeningRank = screeningRank
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self.__screeningRankSet = screeningRankSet
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningOutputLattice, "XSDataISPyBScreeningOutputLattice")
		self.__screeningOutputLattice = screeningOutputLattice
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", screeningStrategy, "XSDataISPyBScreeningStrategy")
		self.__screeningStrategy = screeningStrategy
		checkType("XSDataInputISPyB", "Constructor of XSDataInputISPyB", image, "XSDataISPyBImage")
		self.__image = image
	def getScreening(self): return self.__screening
	def setScreening(self, screening):
		checkType("XSDataInputISPyB", "setScreening", screening, "XSDataISPyBScreening")
		self.__screening = screening
	def delScreening(self): self.__screening = None
	# Properties
	screening = property(getScreening, setScreening, delScreening, "Property for screening")
	def getScreeningInput(self): return self.__screeningInput
	def setScreeningInput(self, screeningInput):
		checkType("XSDataInputISPyB", "setScreeningInput", screeningInput, "XSDataISPyBScreeningInput")
		self.__screeningInput = screeningInput
	def delScreeningInput(self): self.__screeningInput = None
	# Properties
	screeningInput = property(getScreeningInput, setScreeningInput, delScreeningInput, "Property for screeningInput")
	def getScreeningOutput(self): return self.__screeningOutput
	def setScreeningOutput(self, screeningOutput):
		checkType("XSDataInputISPyB", "setScreeningOutput", screeningOutput, "XSDataISPyBScreeningOutput")
		self.__screeningOutput = screeningOutput
	def delScreeningOutput(self): self.__screeningOutput = None
	# Properties
	screeningOutput = property(getScreeningOutput, setScreeningOutput, delScreeningOutput, "Property for screeningOutput")
	def getScreeningRank(self): return self.__screeningRank
	def setScreeningRank(self, screeningRank):
		checkType("XSDataInputISPyB", "setScreeningRank", screeningRank, "XSDataISPyBScreeningRank")
		self.__screeningRank = screeningRank
	def delScreeningRank(self): self.__screeningRank = None
	# Properties
	screeningRank = property(getScreeningRank, setScreeningRank, delScreeningRank, "Property for screeningRank")
	def getScreeningRankSet(self): return self.__screeningRankSet
	def setScreeningRankSet(self, screeningRankSet):
		checkType("XSDataInputISPyB", "setScreeningRankSet", screeningRankSet, "XSDataISPyBScreeningRankSet")
		self.__screeningRankSet = screeningRankSet
	def delScreeningRankSet(self): self.__screeningRankSet = None
	# Properties
	screeningRankSet = property(getScreeningRankSet, setScreeningRankSet, delScreeningRankSet, "Property for screeningRankSet")
	def getScreeningOutputLattice(self): return self.__screeningOutputLattice
	def setScreeningOutputLattice(self, screeningOutputLattice):
		checkType("XSDataInputISPyB", "setScreeningOutputLattice", screeningOutputLattice, "XSDataISPyBScreeningOutputLattice")
		self.__screeningOutputLattice = screeningOutputLattice
	def delScreeningOutputLattice(self): self.__screeningOutputLattice = None
	# Properties
	screeningOutputLattice = property(getScreeningOutputLattice, setScreeningOutputLattice, delScreeningOutputLattice, "Property for screeningOutputLattice")
	def getScreeningStrategy(self): return self.__screeningStrategy
	def setScreeningStrategy(self, screeningStrategy):
		checkType("XSDataInputISPyB", "setScreeningStrategy", screeningStrategy, "XSDataISPyBScreeningStrategy")
		self.__screeningStrategy = screeningStrategy
	def delScreeningStrategy(self): self.__screeningStrategy = None
	# Properties
	screeningStrategy = property(getScreeningStrategy, setScreeningStrategy, delScreeningStrategy, "Property for screeningStrategy")
	def getImage(self): return self.__image
	def setImage(self, image):
		checkType("XSDataInputISPyB", "setImage", image, "XSDataISPyBImage")
		self.__image = image
	def delImage(self): self.__image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def export(self, outfile, level, name_='XSDataInputISPyB'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputISPyB'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__screening is not None:
			self.screening.export(outfile, level, name_='screening')
		else:
			warnEmptyAttribute("screening", "XSDataISPyBScreening")
		if self.__screeningInput is not None:
			self.screeningInput.export(outfile, level, name_='screeningInput')
		else:
			warnEmptyAttribute("screeningInput", "XSDataISPyBScreeningInput")
		if self.__screeningOutput is not None:
			self.screeningOutput.export(outfile, level, name_='screeningOutput')
		else:
			warnEmptyAttribute("screeningOutput", "XSDataISPyBScreeningOutput")
		if self.__screeningRank is not None:
			self.screeningRank.export(outfile, level, name_='screeningRank')
		else:
			warnEmptyAttribute("screeningRank", "XSDataISPyBScreeningRank")
		if self.__screeningRankSet is not None:
			self.screeningRankSet.export(outfile, level, name_='screeningRankSet')
		else:
			warnEmptyAttribute("screeningRankSet", "XSDataISPyBScreeningRankSet")
		if self.__screeningOutputLattice is not None:
			self.screeningOutputLattice.export(outfile, level, name_='screeningOutputLattice')
		else:
			warnEmptyAttribute("screeningOutputLattice", "XSDataISPyBScreeningOutputLattice")
		if self.__screeningStrategy is not None:
			self.screeningStrategy.export(outfile, level, name_='screeningStrategy')
		else:
			warnEmptyAttribute("screeningStrategy", "XSDataISPyBScreeningStrategy")
		if self.__image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataISPyBImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screening':
			obj_ = XSDataISPyBScreening()
			obj_.build(child_)
			self.setScreening(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInput':
			obj_ = XSDataISPyBScreeningInput()
			obj_.build(child_)
			self.setScreeningInput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutput':
			obj_ = XSDataISPyBScreeningOutput()
			obj_.build(child_)
			self.setScreeningOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRank':
			obj_ = XSDataISPyBScreeningRank()
			obj_.build(child_)
			self.setScreeningRank(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSet':
			obj_ = XSDataISPyBScreeningRankSet()
			obj_.build(child_)
			self.setScreeningRankSet(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLattice':
			obj_ = XSDataISPyBScreeningOutputLattice()
			obj_.build(child_)
			self.setScreeningOutputLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategy':
			obj_ = XSDataISPyBScreeningStrategy()
			obj_.build(child_)
			self.setScreeningStrategy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataISPyBImage()
			obj_.build(child_)
			self.setImage(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputISPyB" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputISPyB' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputISPyB is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputISPyB.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputISPyB()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputISPyB" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputISPyB()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputISPyB

class XSDataResultISPyB(XSDataResult):
	def __init__(self, status=None, resultStatus=None, dataCollectionId=None, screeningStrategyId=None, screeningRankSetId=None, screeningRankId=None, screeningOutputLatticeId=None, screeningOutputId=None, screeningInputId=None, screeningId=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
		checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		if resultStatus is None:
			self.__resultStatus = []
		else:
			checkType("XSDataResultISPyB", "Constructor of XSDataResultISPyB", resultStatus, "list")
			self.__resultStatus = resultStatus
	def getScreeningId(self): return self.__screeningId
	def setScreeningId(self, screeningId):
		checkType("XSDataResultISPyB", "setScreeningId", screeningId, "XSDataInteger")
		self.__screeningId = screeningId
	def delScreeningId(self): self.__screeningId = None
	# Properties
	screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
	def getScreeningInputId(self): return self.__screeningInputId
	def setScreeningInputId(self, screeningInputId):
		checkType("XSDataResultISPyB", "setScreeningInputId", screeningInputId, "XSDataInteger")
		self.__screeningInputId = screeningInputId
	def delScreeningInputId(self): self.__screeningInputId = None
	# Properties
	screeningInputId = property(getScreeningInputId, setScreeningInputId, delScreeningInputId, "Property for screeningInputId")
	def getScreeningOutputId(self): return self.__screeningOutputId
	def setScreeningOutputId(self, screeningOutputId):
		checkType("XSDataResultISPyB", "setScreeningOutputId", screeningOutputId, "XSDataInteger")
		self.__screeningOutputId = screeningOutputId
	def delScreeningOutputId(self): self.__screeningOutputId = None
	# Properties
	screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
	def getScreeningOutputLatticeId(self): return self.__screeningOutputLatticeId
	def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
		checkType("XSDataResultISPyB", "setScreeningOutputLatticeId", screeningOutputLatticeId, "XSDataInteger")
		self.__screeningOutputLatticeId = screeningOutputLatticeId
	def delScreeningOutputLatticeId(self): self.__screeningOutputLatticeId = None
	# Properties
	screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
	def getScreeningRankId(self): return self.__screeningRankId
	def setScreeningRankId(self, screeningRankId):
		checkType("XSDataResultISPyB", "setScreeningRankId", screeningRankId, "XSDataInteger")
		self.__screeningRankId = screeningRankId
	def delScreeningRankId(self): self.__screeningRankId = None
	# Properties
	screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
	def getScreeningRankSetId(self): return self.__screeningRankSetId
	def setScreeningRankSetId(self, screeningRankSetId):
		checkType("XSDataResultISPyB", "setScreeningRankSetId", screeningRankSetId, "XSDataInteger")
		self.__screeningRankSetId = screeningRankSetId
	def delScreeningRankSetId(self): self.__screeningRankSetId = None
	# Properties
	screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
	def getScreeningStrategyId(self): return self.__screeningStrategyId
	def setScreeningStrategyId(self, screeningStrategyId):
		checkType("XSDataResultISPyB", "setScreeningStrategyId", screeningStrategyId, "XSDataInteger")
		self.__screeningStrategyId = screeningStrategyId
	def delScreeningStrategyId(self): self.__screeningStrategyId = None
	# Properties
	screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
	def getDataCollectionId(self): return self.__dataCollectionId
	def setDataCollectionId(self, dataCollectionId):
		checkType("XSDataResultISPyB", "setDataCollectionId", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
	def delDataCollectionId(self): self.__dataCollectionId = None
	# Properties
	dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
	def getResultStatus(self): return self.__resultStatus
	def setResultStatus(self, resultStatus):
		checkType("XSDataResultISPyB", "setResultStatus", resultStatus, "list")
		self.__resultStatus = resultStatus
	def delResultStatus(self): self.__resultStatus = None
	# Properties
	resultStatus = property(getResultStatus, setResultStatus, delResultStatus, "Property for resultStatus")
	def addResultStatus(self, value):
		checkType("XSDataResultISPyB", "setResultStatus", value, "XSDataResultStatus")
		self.__resultStatus.append(value)
	def insertResultStatus(self, index, value):
		checkType("XSDataResultISPyB", "setResultStatus", value, "XSDataResultStatus")
		self.__resultStatus[index] = value
	def export(self, outfile, level, name_='XSDataResultISPyB'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultISPyB'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__screeningId is not None:
			self.screeningId.export(outfile, level, name_='screeningId')
		else:
			warnEmptyAttribute("screeningId", "XSDataInteger")
		if self.__screeningInputId is not None:
			self.screeningInputId.export(outfile, level, name_='screeningInputId')
		else:
			warnEmptyAttribute("screeningInputId", "XSDataInteger")
		if self.__screeningOutputId is not None:
			self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
		else:
			warnEmptyAttribute("screeningOutputId", "XSDataInteger")
		if self.__screeningOutputLatticeId is not None:
			self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
		else:
			warnEmptyAttribute("screeningOutputLatticeId", "XSDataInteger")
		if self.__screeningRankId is not None:
			self.screeningRankId.export(outfile, level, name_='screeningRankId')
		else:
			warnEmptyAttribute("screeningRankId", "XSDataInteger")
		if self.__screeningRankSetId is not None:
			self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
		else:
			warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
		if self.__screeningStrategyId is not None:
			self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
		else:
			warnEmptyAttribute("screeningStrategyId", "XSDataInteger")
		if self.__dataCollectionId is not None:
			self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
		else:
			warnEmptyAttribute("dataCollectionId", "XSDataInteger")
		for resultStatus_ in self.getResultStatus():
			resultStatus_.export(outfile, level, name_='resultStatus')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningInputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningInputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningOutputLatticeId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningOutputLatticeId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningRankSetId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningRankSetId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'screeningStrategyId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setScreeningStrategyId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataCollectionId':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setDataCollectionId(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultStatus':
			obj_ = XSDataResultStatus()
			obj_.build(child_)
			self.resultStatus.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultISPyB" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultISPyB' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultISPyB is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultISPyB.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultISPyB()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultISPyB" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultISPyB()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultISPyB



# End of data representation classes.



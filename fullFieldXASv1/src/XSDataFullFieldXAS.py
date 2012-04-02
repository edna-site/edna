#!/usr/bin/env python

#
# Generated Mon Mar 5 05:38::21 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = {  "XSDataCommon": "kernel/datamodel"}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataDictionary
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataImageExt
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
from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImageExt




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


class MeasureOffset(XSData):
	def __init__(self, useSift=None, sobelFilter=None, smoothBorders=None, removeBackground=None, cropBorders=None, alwaysVersusRef=None):
		XSData.__init__(self,)
		checkType("MeasureOffset", "Constructor of MeasureOffset", alwaysVersusRef, "XSDataBoolean")
		self.__alwaysVersusRef = alwaysVersusRef
		if cropBorders is None:
			self.__cropBorders = []
		else:
			checkType("MeasureOffset", "Constructor of MeasureOffset", cropBorders, "list")
			self.__cropBorders = cropBorders
		checkType("MeasureOffset", "Constructor of MeasureOffset", removeBackground, "XSDataBoolean")
		self.__removeBackground = removeBackground
		if smoothBorders is None:
			self.__smoothBorders = []
		else:
			checkType("MeasureOffset", "Constructor of MeasureOffset", smoothBorders, "list")
			self.__smoothBorders = smoothBorders
		checkType("MeasureOffset", "Constructor of MeasureOffset", sobelFilter, "XSDataBoolean")
		self.__sobelFilter = sobelFilter
		checkType("MeasureOffset", "Constructor of MeasureOffset", useSift, "XSDataBoolean")
		self.__useSift = useSift
	def getAlwaysVersusRef(self): return self.__alwaysVersusRef
	def setAlwaysVersusRef(self, alwaysVersusRef):
		checkType("MeasureOffset", "setAlwaysVersusRef", alwaysVersusRef, "XSDataBoolean")
		self.__alwaysVersusRef = alwaysVersusRef
	def delAlwaysVersusRef(self): self.__alwaysVersusRef = None
	# Properties
	alwaysVersusRef = property(getAlwaysVersusRef, setAlwaysVersusRef, delAlwaysVersusRef, "Property for alwaysVersusRef")
	def getCropBorders(self): return self.__cropBorders
	def setCropBorders(self, cropBorders):
		checkType("MeasureOffset", "setCropBorders", cropBorders, "list")
		self.__cropBorders = cropBorders
	def delCropBorders(self): self.__cropBorders = None
	# Properties
	cropBorders = property(getCropBorders, setCropBorders, delCropBorders, "Property for cropBorders")
	def addCropBorders(self, value):
		checkType("MeasureOffset", "setCropBorders", value, "XSDataInteger")
		self.__cropBorders.append(value)
	def insertCropBorders(self, index, value):
		checkType("MeasureOffset", "setCropBorders", value, "XSDataInteger")
		self.__cropBorders[index] = value
	def getRemoveBackground(self): return self.__removeBackground
	def setRemoveBackground(self, removeBackground):
		checkType("MeasureOffset", "setRemoveBackground", removeBackground, "XSDataBoolean")
		self.__removeBackground = removeBackground
	def delRemoveBackground(self): self.__removeBackground = None
	# Properties
	removeBackground = property(getRemoveBackground, setRemoveBackground, delRemoveBackground, "Property for removeBackground")
	def getSmoothBorders(self): return self.__smoothBorders
	def setSmoothBorders(self, smoothBorders):
		checkType("MeasureOffset", "setSmoothBorders", smoothBorders, "list")
		self.__smoothBorders = smoothBorders
	def delSmoothBorders(self): self.__smoothBorders = None
	# Properties
	smoothBorders = property(getSmoothBorders, setSmoothBorders, delSmoothBorders, "Property for smoothBorders")
	def addSmoothBorders(self, value):
		checkType("MeasureOffset", "setSmoothBorders", value, "XSDataInteger")
		self.__smoothBorders.append(value)
	def insertSmoothBorders(self, index, value):
		checkType("MeasureOffset", "setSmoothBorders", value, "XSDataInteger")
		self.__smoothBorders[index] = value
	def getSobelFilter(self): return self.__sobelFilter
	def setSobelFilter(self, sobelFilter):
		checkType("MeasureOffset", "setSobelFilter", sobelFilter, "XSDataBoolean")
		self.__sobelFilter = sobelFilter
	def delSobelFilter(self): self.__sobelFilter = None
	# Properties
	sobelFilter = property(getSobelFilter, setSobelFilter, delSobelFilter, "Property for sobelFilter")
	def getUseSift(self): return self.__useSift
	def setUseSift(self, useSift):
		checkType("MeasureOffset", "setUseSift", useSift, "XSDataBoolean")
		self.__useSift = useSift
	def delUseSift(self): self.__useSift = None
	# Properties
	useSift = property(getUseSift, setUseSift, delUseSift, "Property for useSift")
	def export(self, outfile, level, name_='MeasureOffset'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='MeasureOffset'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__alwaysVersusRef is not None:
			self.alwaysVersusRef.export(outfile, level, name_='alwaysVersusRef')
		for cropBorders_ in self.getCropBorders():
			cropBorders_.export(outfile, level, name_='cropBorders')
		if self.__removeBackground is not None:
			self.removeBackground.export(outfile, level, name_='removeBackground')
		for smoothBorders_ in self.getSmoothBorders():
			smoothBorders_.export(outfile, level, name_='smoothBorders')
		if self.__sobelFilter is not None:
			self.sobelFilter.export(outfile, level, name_='sobelFilter')
		if self.__useSift is not None:
			self.useSift.export(outfile, level, name_='useSift')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'alwaysVersusRef':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAlwaysVersusRef(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cropBorders':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.cropBorders.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'removeBackground':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setRemoveBackground(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'smoothBorders':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.smoothBorders.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sobelFilter':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setSobelFilter(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'useSift':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setUseSift(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="MeasureOffset")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='MeasureOffset')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class MeasureOffset is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return MeasureOffset.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = MeasureOffset()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="MeasureOffset")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = MeasureOffset()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class MeasureOffset

class XSDataHDF5Attributes(XSData):
	"""Allows the fine definition of the metadata for group/datasets"""
	def __init__(self, metadata=None, h5path=None):
		XSData.__init__(self,)
		checkType("XSDataHDF5Attributes", "Constructor of XSDataHDF5Attributes", h5path, "XSDataString")
		self.__h5path = h5path
		checkType("XSDataHDF5Attributes", "Constructor of XSDataHDF5Attributes", metadata, "XSDataDictionary")
		self.__metadata = metadata
	def getH5path(self): return self.__h5path
	def setH5path(self, h5path):
		checkType("XSDataHDF5Attributes", "setH5path", h5path, "XSDataString")
		self.__h5path = h5path
	def delH5path(self): self.__h5path = None
	# Properties
	h5path = property(getH5path, setH5path, delH5path, "Property for h5path")
	def getMetadata(self): return self.__metadata
	def setMetadata(self, metadata):
		checkType("XSDataHDF5Attributes", "setMetadata", metadata, "XSDataDictionary")
		self.__metadata = metadata
	def delMetadata(self): self.__metadata = None
	# Properties
	metadata = property(getMetadata, setMetadata, delMetadata, "Property for metadata")
	def export(self, outfile, level, name_='XSDataHDF5Attributes'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataHDF5Attributes'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__h5path is not None:
			self.h5path.export(outfile, level, name_='h5path')
		else:
			warnEmptyAttribute("h5path", "XSDataString")
		if self.__metadata is not None:
			self.metadata.export(outfile, level, name_='metadata')
		else:
			warnEmptyAttribute("metadata", "XSDataDictionary")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'h5path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setH5path(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'metadata':
			obj_ = XSDataDictionary()
			obj_.build(child_)
			self.setMetadata(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataHDF5Attributes")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataHDF5Attributes')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataHDF5Attributes is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataHDF5Attributes.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataHDF5Attributes()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataHDF5Attributes")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataHDF5Attributes()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataHDF5Attributes

class XSDataInputAlignStack(XSDataInput):
	def __init__(self, configuration=None, dontAlign=None, useSift=None, sobelFilterMO=None, smoothBordersMO=None, measureOffset=None, internalHDF5Path=None, index=None, images=None, frameReference=None, extraAttributes=None, cropBordersMO=None, backgroundSubtractionMO=None, alwaysMOvsRef=None, HDF5File=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", alwaysMOvsRef, "XSDataBoolean")
		self.__alwaysMOvsRef = alwaysMOvsRef
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", backgroundSubtractionMO, "XSDataBoolean")
		self.__backgroundSubtractionMO = backgroundSubtractionMO
		if cropBordersMO is None:
			self.__cropBordersMO = []
		else:
			checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", cropBordersMO, "list")
			self.__cropBordersMO = cropBordersMO
		if extraAttributes is None:
			self.__extraAttributes = []
		else:
			checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", extraAttributes, "list")
			self.__extraAttributes = extraAttributes
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", frameReference, "XSDataInteger")
		self.__frameReference = frameReference
		if images is None:
			self.__images = []
		else:
			checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", images, "list")
			self.__images = images
		if index is None:
			self.__index = []
		else:
			checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", index, "list")
			self.__index = index
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", measureOffset, "MeasureOffset")
		self.__measureOffset = measureOffset
		if smoothBordersMO is None:
			self.__smoothBordersMO = []
		else:
			checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", smoothBordersMO, "list")
			self.__smoothBordersMO = smoothBordersMO
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", sobelFilterMO, "XSDataBoolean")
		self.__sobelFilterMO = sobelFilterMO
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", useSift, "XSDataBoolean")
		self.__useSift = useSift
		checkType("XSDataInputAlignStack", "Constructor of XSDataInputAlignStack", dontAlign, "XSDataBoolean")
		self.__dontAlign = dontAlign
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataInputAlignStack", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getAlwaysMOvsRef(self): return self.__alwaysMOvsRef
	def setAlwaysMOvsRef(self, alwaysMOvsRef):
		checkType("XSDataInputAlignStack", "setAlwaysMOvsRef", alwaysMOvsRef, "XSDataBoolean")
		self.__alwaysMOvsRef = alwaysMOvsRef
	def delAlwaysMOvsRef(self): self.__alwaysMOvsRef = None
	# Properties
	alwaysMOvsRef = property(getAlwaysMOvsRef, setAlwaysMOvsRef, delAlwaysMOvsRef, "Property for alwaysMOvsRef")
	def getBackgroundSubtractionMO(self): return self.__backgroundSubtractionMO
	def setBackgroundSubtractionMO(self, backgroundSubtractionMO):
		checkType("XSDataInputAlignStack", "setBackgroundSubtractionMO", backgroundSubtractionMO, "XSDataBoolean")
		self.__backgroundSubtractionMO = backgroundSubtractionMO
	def delBackgroundSubtractionMO(self): self.__backgroundSubtractionMO = None
	# Properties
	backgroundSubtractionMO = property(getBackgroundSubtractionMO, setBackgroundSubtractionMO, delBackgroundSubtractionMO, "Property for backgroundSubtractionMO")
	def getCropBordersMO(self): return self.__cropBordersMO
	def setCropBordersMO(self, cropBordersMO):
		checkType("XSDataInputAlignStack", "setCropBordersMO", cropBordersMO, "list")
		self.__cropBordersMO = cropBordersMO
	def delCropBordersMO(self): self.__cropBordersMO = None
	# Properties
	cropBordersMO = property(getCropBordersMO, setCropBordersMO, delCropBordersMO, "Property for cropBordersMO")
	def addCropBordersMO(self, value):
		checkType("XSDataInputAlignStack", "setCropBordersMO", value, "XSDataInteger")
		self.__cropBordersMO.append(value)
	def insertCropBordersMO(self, index, value):
		checkType("XSDataInputAlignStack", "setCropBordersMO", value, "XSDataInteger")
		self.__cropBordersMO[index] = value
	def getExtraAttributes(self): return self.__extraAttributes
	def setExtraAttributes(self, extraAttributes):
		checkType("XSDataInputAlignStack", "setExtraAttributes", extraAttributes, "list")
		self.__extraAttributes = extraAttributes
	def delExtraAttributes(self): self.__extraAttributes = None
	# Properties
	extraAttributes = property(getExtraAttributes, setExtraAttributes, delExtraAttributes, "Property for extraAttributes")
	def addExtraAttributes(self, value):
		checkType("XSDataInputAlignStack", "setExtraAttributes", value, "XSDataHDF5Attributes")
		self.__extraAttributes.append(value)
	def insertExtraAttributes(self, index, value):
		checkType("XSDataInputAlignStack", "setExtraAttributes", value, "XSDataHDF5Attributes")
		self.__extraAttributes[index] = value
	def getFrameReference(self): return self.__frameReference
	def setFrameReference(self, frameReference):
		checkType("XSDataInputAlignStack", "setFrameReference", frameReference, "XSDataInteger")
		self.__frameReference = frameReference
	def delFrameReference(self): self.__frameReference = None
	# Properties
	frameReference = property(getFrameReference, setFrameReference, delFrameReference, "Property for frameReference")
	def getImages(self): return self.__images
	def setImages(self, images):
		checkType("XSDataInputAlignStack", "setImages", images, "list")
		self.__images = images
	def delImages(self): self.__images = None
	# Properties
	images = property(getImages, setImages, delImages, "Property for images")
	def addImages(self, value):
		checkType("XSDataInputAlignStack", "setImages", value, "XSDataImageExt")
		self.__images.append(value)
	def insertImages(self, index, value):
		checkType("XSDataInputAlignStack", "setImages", value, "XSDataImageExt")
		self.__images[index] = value
	def getIndex(self): return self.__index
	def setIndex(self, index):
		checkType("XSDataInputAlignStack", "setIndex", index, "list")
		self.__index = index
	def delIndex(self): self.__index = None
	# Properties
	index = property(getIndex, setIndex, delIndex, "Property for index")
	def addIndex(self, value):
		checkType("XSDataInputAlignStack", "setIndex", value, "XSDataInteger")
		self.__index.append(value)
	def insertIndex(self, index, value):
		checkType("XSDataInputAlignStack", "setIndex", value, "XSDataInteger")
		self.__index[index] = value
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataInputAlignStack", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def getMeasureOffset(self): return self.__measureOffset
	def setMeasureOffset(self, measureOffset):
		checkType("XSDataInputAlignStack", "setMeasureOffset", measureOffset, "MeasureOffset")
		self.__measureOffset = measureOffset
	def delMeasureOffset(self): self.__measureOffset = None
	# Properties
	measureOffset = property(getMeasureOffset, setMeasureOffset, delMeasureOffset, "Property for measureOffset")
	def getSmoothBordersMO(self): return self.__smoothBordersMO
	def setSmoothBordersMO(self, smoothBordersMO):
		checkType("XSDataInputAlignStack", "setSmoothBordersMO", smoothBordersMO, "list")
		self.__smoothBordersMO = smoothBordersMO
	def delSmoothBordersMO(self): self.__smoothBordersMO = None
	# Properties
	smoothBordersMO = property(getSmoothBordersMO, setSmoothBordersMO, delSmoothBordersMO, "Property for smoothBordersMO")
	def addSmoothBordersMO(self, value):
		checkType("XSDataInputAlignStack", "setSmoothBordersMO", value, "XSDataInteger")
		self.__smoothBordersMO.append(value)
	def insertSmoothBordersMO(self, index, value):
		checkType("XSDataInputAlignStack", "setSmoothBordersMO", value, "XSDataInteger")
		self.__smoothBordersMO[index] = value
	def getSobelFilterMO(self): return self.__sobelFilterMO
	def setSobelFilterMO(self, sobelFilterMO):
		checkType("XSDataInputAlignStack", "setSobelFilterMO", sobelFilterMO, "XSDataBoolean")
		self.__sobelFilterMO = sobelFilterMO
	def delSobelFilterMO(self): self.__sobelFilterMO = None
	# Properties
	sobelFilterMO = property(getSobelFilterMO, setSobelFilterMO, delSobelFilterMO, "Property for sobelFilterMO")
	def getUseSift(self): return self.__useSift
	def setUseSift(self, useSift):
		checkType("XSDataInputAlignStack", "setUseSift", useSift, "XSDataBoolean")
		self.__useSift = useSift
	def delUseSift(self): self.__useSift = None
	# Properties
	useSift = property(getUseSift, setUseSift, delUseSift, "Property for useSift")
	def getDontAlign(self): return self.__dontAlign
	def setDontAlign(self, dontAlign):
		checkType("XSDataInputAlignStack", "setDontAlign", dontAlign, "XSDataBoolean")
		self.__dontAlign = dontAlign
	def delDontAlign(self): self.__dontAlign = None
	# Properties
	dontAlign = property(getDontAlign, setDontAlign, delDontAlign, "Property for dontAlign")
	def export(self, outfile, level, name_='XSDataInputAlignStack'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputAlignStack'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		if self.__alwaysMOvsRef is not None:
			self.alwaysMOvsRef.export(outfile, level, name_='alwaysMOvsRef')
		if self.__backgroundSubtractionMO is not None:
			self.backgroundSubtractionMO.export(outfile, level, name_='backgroundSubtractionMO')
		for cropBordersMO_ in self.getCropBordersMO():
			cropBordersMO_.export(outfile, level, name_='cropBordersMO')
		for extraAttributes_ in self.getExtraAttributes():
			extraAttributes_.export(outfile, level, name_='extraAttributes')
		if self.__frameReference is not None:
			self.frameReference.export(outfile, level, name_='frameReference')
		for images_ in self.getImages():
			images_.export(outfile, level, name_='images')
		for index_ in self.getIndex():
			index_.export(outfile, level, name_='index')
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
		if self.__measureOffset is not None:
			self.measureOffset.export(outfile, level, name_='measureOffset')
		for smoothBordersMO_ in self.getSmoothBordersMO():
			smoothBordersMO_.export(outfile, level, name_='smoothBordersMO')
		if self.__sobelFilterMO is not None:
			self.sobelFilterMO.export(outfile, level, name_='sobelFilterMO')
		if self.__useSift is not None:
			self.useSift.export(outfile, level, name_='useSift')
		if self.__dontAlign is not None:
			self.dontAlign.export(outfile, level, name_='dontAlign')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'alwaysMOvsRef':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAlwaysMOvsRef(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'backgroundSubtractionMO':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setBackgroundSubtractionMO(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cropBordersMO':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.cropBordersMO.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'extraAttributes':
			obj_ = XSDataHDF5Attributes()
			obj_.build(child_)
			self.extraAttributes.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'frameReference':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setFrameReference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'images':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.images.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'index':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.index.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'measureOffset':
			obj_ = MeasureOffset()
			obj_.build(child_)
			self.setMeasureOffset(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'smoothBordersMO':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.smoothBordersMO.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sobelFilterMO':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setSobelFilterMO(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'useSift':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setUseSift(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dontAlign':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDontAlign(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputAlignStack")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputAlignStack')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputAlignStack is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputAlignStack.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputAlignStack()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputAlignStack")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputAlignStack()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputAlignStack

class XSDataInputFullFieldXAS(XSDataInput):
	def __init__(self, configuration=None, flatScaleFactor=None, darkScaleFactor=None, dataScaleFactor=None, dontAlign=None, saveNormalized=None, reference=None, measureOffset=None, internalHDF5Path=None, index=None, flat=None, energy=None, data=None, dark=None, HDF5File=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		if dark is None:
			self.__dark = []
		else:
			checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", dark, "list")
			self.__dark = dark
		if data is None:
			self.__data = []
		else:
			checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", data, "list")
			self.__data = data
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", energy, "XSDataDouble")
		self.__energy = energy
		if flat is None:
			self.__flat = []
		else:
			checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", flat, "list")
			self.__flat = flat
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", index, "XSDataInteger")
		self.__index = index
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", measureOffset, "MeasureOffset")
		self.__measureOffset = measureOffset
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", reference, "XSDataInteger")
		self.__reference = reference
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", saveNormalized, "XSDataFile")
		self.__saveNormalized = saveNormalized
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", dontAlign, "XSDataBoolean")
		self.__dontAlign = dontAlign
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", dataScaleFactor, "XSDataDouble")
		self.__dataScaleFactor = dataScaleFactor
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", darkScaleFactor, "XSDataDouble")
		self.__darkScaleFactor = darkScaleFactor
		checkType("XSDataInputFullFieldXAS", "Constructor of XSDataInputFullFieldXAS", flatScaleFactor, "XSDataDouble")
		self.__flatScaleFactor = flatScaleFactor
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataInputFullFieldXAS", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getDark(self): return self.__dark
	def setDark(self, dark):
		checkType("XSDataInputFullFieldXAS", "setDark", dark, "list")
		self.__dark = dark
	def delDark(self): self.__dark = None
	# Properties
	dark = property(getDark, setDark, delDark, "Property for dark")
	def addDark(self, value):
		checkType("XSDataInputFullFieldXAS", "setDark", value, "XSDataImageExt")
		self.__dark.append(value)
	def insertDark(self, index, value):
		checkType("XSDataInputFullFieldXAS", "setDark", value, "XSDataImageExt")
		self.__dark[index] = value
	def getData(self): return self.__data
	def setData(self, data):
		checkType("XSDataInputFullFieldXAS", "setData", data, "list")
		self.__data = data
	def delData(self): self.__data = None
	# Properties
	data = property(getData, setData, delData, "Property for data")
	def addData(self, value):
		checkType("XSDataInputFullFieldXAS", "setData", value, "XSDataImageExt")
		self.__data.append(value)
	def insertData(self, index, value):
		checkType("XSDataInputFullFieldXAS", "setData", value, "XSDataImageExt")
		self.__data[index] = value
	def getEnergy(self): return self.__energy
	def setEnergy(self, energy):
		checkType("XSDataInputFullFieldXAS", "setEnergy", energy, "XSDataDouble")
		self.__energy = energy
	def delEnergy(self): self.__energy = None
	# Properties
	energy = property(getEnergy, setEnergy, delEnergy, "Property for energy")
	def getFlat(self): return self.__flat
	def setFlat(self, flat):
		checkType("XSDataInputFullFieldXAS", "setFlat", flat, "list")
		self.__flat = flat
	def delFlat(self): self.__flat = None
	# Properties
	flat = property(getFlat, setFlat, delFlat, "Property for flat")
	def addFlat(self, value):
		checkType("XSDataInputFullFieldXAS", "setFlat", value, "XSDataImageExt")
		self.__flat.append(value)
	def insertFlat(self, index, value):
		checkType("XSDataInputFullFieldXAS", "setFlat", value, "XSDataImageExt")
		self.__flat[index] = value
	def getIndex(self): return self.__index
	def setIndex(self, index):
		checkType("XSDataInputFullFieldXAS", "setIndex", index, "XSDataInteger")
		self.__index = index
	def delIndex(self): self.__index = None
	# Properties
	index = property(getIndex, setIndex, delIndex, "Property for index")
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataInputFullFieldXAS", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def getMeasureOffset(self): return self.__measureOffset
	def setMeasureOffset(self, measureOffset):
		checkType("XSDataInputFullFieldXAS", "setMeasureOffset", measureOffset, "MeasureOffset")
		self.__measureOffset = measureOffset
	def delMeasureOffset(self): self.__measureOffset = None
	# Properties
	measureOffset = property(getMeasureOffset, setMeasureOffset, delMeasureOffset, "Property for measureOffset")
	def getReference(self): return self.__reference
	def setReference(self, reference):
		checkType("XSDataInputFullFieldXAS", "setReference", reference, "XSDataInteger")
		self.__reference = reference
	def delReference(self): self.__reference = None
	# Properties
	reference = property(getReference, setReference, delReference, "Property for reference")
	def getSaveNormalized(self): return self.__saveNormalized
	def setSaveNormalized(self, saveNormalized):
		checkType("XSDataInputFullFieldXAS", "setSaveNormalized", saveNormalized, "XSDataFile")
		self.__saveNormalized = saveNormalized
	def delSaveNormalized(self): self.__saveNormalized = None
	# Properties
	saveNormalized = property(getSaveNormalized, setSaveNormalized, delSaveNormalized, "Property for saveNormalized")
	def getDontAlign(self): return self.__dontAlign
	def setDontAlign(self, dontAlign):
		checkType("XSDataInputFullFieldXAS", "setDontAlign", dontAlign, "XSDataBoolean")
		self.__dontAlign = dontAlign
	def delDontAlign(self): self.__dontAlign = None
	# Properties
	dontAlign = property(getDontAlign, setDontAlign, delDontAlign, "Property for dontAlign")
	def getDataScaleFactor(self): return self.__dataScaleFactor
	def setDataScaleFactor(self, dataScaleFactor):
		checkType("XSDataInputFullFieldXAS", "setDataScaleFactor", dataScaleFactor, "XSDataDouble")
		self.__dataScaleFactor = dataScaleFactor
	def delDataScaleFactor(self): self.__dataScaleFactor = None
	# Properties
	dataScaleFactor = property(getDataScaleFactor, setDataScaleFactor, delDataScaleFactor, "Property for dataScaleFactor")
	def getDarkScaleFactor(self): return self.__darkScaleFactor
	def setDarkScaleFactor(self, darkScaleFactor):
		checkType("XSDataInputFullFieldXAS", "setDarkScaleFactor", darkScaleFactor, "XSDataDouble")
		self.__darkScaleFactor = darkScaleFactor
	def delDarkScaleFactor(self): self.__darkScaleFactor = None
	# Properties
	darkScaleFactor = property(getDarkScaleFactor, setDarkScaleFactor, delDarkScaleFactor, "Property for darkScaleFactor")
	def getFlatScaleFactor(self): return self.__flatScaleFactor
	def setFlatScaleFactor(self, flatScaleFactor):
		checkType("XSDataInputFullFieldXAS", "setFlatScaleFactor", flatScaleFactor, "XSDataDouble")
		self.__flatScaleFactor = flatScaleFactor
	def delFlatScaleFactor(self): self.__flatScaleFactor = None
	# Properties
	flatScaleFactor = property(getFlatScaleFactor, setFlatScaleFactor, delFlatScaleFactor, "Property for flatScaleFactor")
	def export(self, outfile, level, name_='XSDataInputFullFieldXAS'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputFullFieldXAS'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		for dark_ in self.getDark():
			dark_.export(outfile, level, name_='dark')
		for data_ in self.getData():
			data_.export(outfile, level, name_='data')
		if self.getData() == []:
			warnEmptyAttribute("data", "XSDataImageExt")
		if self.__energy is not None:
			self.energy.export(outfile, level, name_='energy')
		for flat_ in self.getFlat():
			flat_.export(outfile, level, name_='flat')
		if self.__index is not None:
			self.index.export(outfile, level, name_='index')
		else:
			warnEmptyAttribute("index", "XSDataInteger")
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
		if self.__measureOffset is not None:
			self.measureOffset.export(outfile, level, name_='measureOffset')
		if self.__reference is not None:
			self.reference.export(outfile, level, name_='reference')
		if self.__saveNormalized is not None:
			self.saveNormalized.export(outfile, level, name_='saveNormalized')
		if self.__dontAlign is not None:
			self.dontAlign.export(outfile, level, name_='dontAlign')
		if self.__dataScaleFactor is not None:
			self.dataScaleFactor.export(outfile, level, name_='dataScaleFactor')
		if self.__darkScaleFactor is not None:
			self.darkScaleFactor.export(outfile, level, name_='darkScaleFactor')
		if self.__flatScaleFactor is not None:
			self.flatScaleFactor.export(outfile, level, name_='flatScaleFactor')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dark':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.dark.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'data':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.data.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'energy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setEnergy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flat':
			obj_ = XSDataImageExt()
			obj_.build(child_)
			self.flat.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'index':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIndex(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'measureOffset':
			obj_ = MeasureOffset()
			obj_.build(child_)
			self.setMeasureOffset(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'reference':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setReference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'saveNormalized':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSaveNormalized(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dontAlign':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setDontAlign(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dataScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDataScaleFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDarkScaleFactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flatScaleFactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFlatScaleFactor(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputFullFieldXAS")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputFullFieldXAS')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputFullFieldXAS is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputFullFieldXAS.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputFullFieldXAS()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputFullFieldXAS")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputFullFieldXAS()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputFullFieldXAS

class XSDataResultAlignStack(XSDataResult):
	def __init__(self, status=None, internalHDF5Path=None, HDF5File=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultAlignStack", "Constructor of XSDataResultAlignStack", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		checkType("XSDataResultAlignStack", "Constructor of XSDataResultAlignStack", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataResultAlignStack", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataResultAlignStack", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def export(self, outfile, level, name_='XSDataResultAlignStack'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultAlignStack'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultAlignStack")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultAlignStack')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultAlignStack is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultAlignStack.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultAlignStack()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultAlignStack")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultAlignStack()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultAlignStack

class XSDataResultFullFieldXAS(XSDataResult):
	def __init__(self, status=None, internalHDF5Path=None, HDF5File=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultFullFieldXAS", "Constructor of XSDataResultFullFieldXAS", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
		checkType("XSDataResultFullFieldXAS", "Constructor of XSDataResultFullFieldXAS", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def getHDF5File(self): return self.__HDF5File
	def setHDF5File(self, HDF5File):
		checkType("XSDataResultFullFieldXAS", "setHDF5File", HDF5File, "XSDataFile")
		self.__HDF5File = HDF5File
	def delHDF5File(self): self.__HDF5File = None
	# Properties
	HDF5File = property(getHDF5File, setHDF5File, delHDF5File, "Property for HDF5File")
	def getInternalHDF5Path(self): return self.__internalHDF5Path
	def setInternalHDF5Path(self, internalHDF5Path):
		checkType("XSDataResultFullFieldXAS", "setInternalHDF5Path", internalHDF5Path, "XSDataString")
		self.__internalHDF5Path = internalHDF5Path
	def delInternalHDF5Path(self): self.__internalHDF5Path = None
	# Properties
	internalHDF5Path = property(getInternalHDF5Path, setInternalHDF5Path, delInternalHDF5Path, "Property for internalHDF5Path")
	def export(self, outfile, level, name_='XSDataResultFullFieldXAS'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultFullFieldXAS'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__HDF5File is not None:
			self.HDF5File.export(outfile, level, name_='HDF5File')
		else:
			warnEmptyAttribute("HDF5File", "XSDataFile")
		if self.__internalHDF5Path is not None:
			self.internalHDF5Path.export(outfile, level, name_='internalHDF5Path')
		else:
			warnEmptyAttribute("internalHDF5Path", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'HDF5File':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHDF5File(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'internalHDF5Path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInternalHDF5Path(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultFullFieldXAS")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultFullFieldXAS')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultFullFieldXAS is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultFullFieldXAS.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultFullFieldXAS()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultFullFieldXAS")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultFullFieldXAS()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultFullFieldXAS



# End of data representation classes.



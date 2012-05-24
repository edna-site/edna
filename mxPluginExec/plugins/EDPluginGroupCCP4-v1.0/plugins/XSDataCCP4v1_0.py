#!/usr/bin/env python

#
# Generated Thu May 24 10:31::15 2012 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
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
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
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


class XSDataInputMtz2Various(XSDataInput):
	def __init__(self, configuration=None, format=None, output=None, labin=None, mtzfile=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputMtz2Various", "Constructor of XSDataInputMtz2Various", mtzfile, "XSDataFile")
		self._mtzfile = mtzfile
		if labin is None:
			self._labin = []
		else:
			checkType("XSDataInputMtz2Various", "Constructor of XSDataInputMtz2Various", labin, "list")
			self._labin = labin
		checkType("XSDataInputMtz2Various", "Constructor of XSDataInputMtz2Various", output, "XSDataString")
		self._output = output
		checkType("XSDataInputMtz2Various", "Constructor of XSDataInputMtz2Various", format, "XSDataString")
		self._format = format
	def getMtzfile(self): return self._mtzfile
	def setMtzfile(self, mtzfile):
		checkType("XSDataInputMtz2Various", "setMtzfile", mtzfile, "XSDataFile")
		self._mtzfile = mtzfile
	def delMtzfile(self): self._mtzfile = None
	# Properties
	mtzfile = property(getMtzfile, setMtzfile, delMtzfile, "Property for mtzfile")
	def getLabin(self): return self._labin
	def setLabin(self, labin):
		checkType("XSDataInputMtz2Various", "setLabin", labin, "list")
		self._labin = labin
	def delLabin(self): self._labin = None
	# Properties
	labin = property(getLabin, setLabin, delLabin, "Property for labin")
	def addLabin(self, value):
		checkType("XSDataInputMtz2Various", "setLabin", value, "XSDataString")
		self._labin.append(value)
	def insertLabin(self, index, value):
		checkType("XSDataInputMtz2Various", "setLabin", value, "XSDataString")
		self._labin[index] = value
	def getOutput(self): return self._output
	def setOutput(self, output):
		checkType("XSDataInputMtz2Various", "setOutput", output, "XSDataString")
		self._output = output
	def delOutput(self): self._output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def getFormat(self): return self._format
	def setFormat(self, format):
		checkType("XSDataInputMtz2Various", "setFormat", format, "XSDataString")
		self._format = format
	def delFormat(self): self._format = None
	# Properties
	format = property(getFormat, setFormat, delFormat, "Property for format")
	def export(self, outfile, level, name_='XSDataInputMtz2Various'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputMtz2Various'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._mtzfile is not None:
			self.mtzfile.export(outfile, level, name_='mtzfile')
		else:
			warnEmptyAttribute("mtzfile", "XSDataFile")
		for labin_ in self.getLabin():
			labin_.export(outfile, level, name_='labin')
		if self.getLabin() == []:
			warnEmptyAttribute("labin", "XSDataString")
		if self._output is not None:
			self.output.export(outfile, level, name_='output')
		if self._format is not None:
			self.format.export(outfile, level, name_='format')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mtzfile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setMtzfile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'labin':
			obj_ = XSDataString()
			obj_.build(child_)
			self.labin.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'format':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFormat(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputMtz2Various" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputMtz2Various' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputMtz2Various is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputMtz2Various.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputMtz2Various()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputMtz2Various" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputMtz2Various()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputMtz2Various

class XSDataResultMtz2Various(XSDataResult):
	def __init__(self, status=None, hklfile=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultMtz2Various", "Constructor of XSDataResultMtz2Various", hklfile, "XSDataFile")
		self._hklfile = hklfile
	def getHklfile(self): return self._hklfile
	def setHklfile(self, hklfile):
		checkType("XSDataResultMtz2Various", "setHklfile", hklfile, "XSDataFile")
		self._hklfile = hklfile
	def delHklfile(self): self._hklfile = None
	# Properties
	hklfile = property(getHklfile, setHklfile, delHklfile, "Property for hklfile")
	def export(self, outfile, level, name_='XSDataResultMtz2Various'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultMtz2Various'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._hklfile is not None:
			self.hklfile.export(outfile, level, name_='hklfile')
		else:
			warnEmptyAttribute("hklfile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'hklfile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHklfile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultMtz2Various" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultMtz2Various' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultMtz2Various is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultMtz2Various.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultMtz2Various()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultMtz2Various" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultMtz2Various()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultMtz2Various



# End of data representation classes.



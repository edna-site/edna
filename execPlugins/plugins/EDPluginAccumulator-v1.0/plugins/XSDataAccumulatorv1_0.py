#!/usr/bin/env python

#
# Generated Tue Mar 13 09:46::30 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node

strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataBoolean
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
from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
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

class XSDataQuery(XSData):
	def __init__(self, removeItems=None, item=None):
		XSData.__init__(self, )
		if item is None:
			self.__item = []
		else:
			checkType("XSDataQuery", "Constructor of XSDataQuery", item, "list")
			self.__item = item
		checkType("XSDataQuery", "Constructor of XSDataQuery", removeItems, "XSDataBoolean")
		self.__removeItems = removeItems
	def getItem(self): return self.__item
	def setItem(self, item):
		checkType("XSDataQuery", "setItem", item, "list")
		self.__item = item
	def delItem(self): self.__item = None
	# Properties
	item = property(getItem, setItem, delItem, "Property for item")
	def addItem(self, value):
		checkType("XSDataQuery", "setItem", value, "XSDataString")
		self.__item.append(value)
	def insertItem(self, index, value):
		checkType("XSDataQuery", "setItem", value, "XSDataString")
		self.__item[index] = value
	def getRemoveItems(self): return self.__removeItems
	def setRemoveItems(self, removeItems):
		checkType("XSDataQuery", "setRemoveItems", removeItems, "XSDataBoolean")
		self.__removeItems = removeItems
	def delRemoveItems(self): self.__removeItems = None
	# Properties
	removeItems = property(getRemoveItems, setRemoveItems, delRemoveItems, "Property for removeItems")
	def export(self, outfile, level, name_='XSDataQuery'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataQuery'):
		XSData.exportChildren(self, outfile, level, name_)
		for item_ in self.getItem():
			item_.export(outfile, level, name_='item')
		if self.getItem() == []:
			warnEmptyAttribute("item", "XSDataString")
		if self.__removeItems is not None:
			self.removeItems.export(outfile, level, name_='removeItems')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'item':
			obj_ = XSDataString()
			obj_.build(child_)
			self.item.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'removeItems':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setRemoveItems(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataQuery" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataQuery' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataQuery is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataQuery.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataQuery()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataQuery" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataQuery()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataQuery

class XSDataInputAccumulator(XSDataInput):
	def __init__(self, configuration=None, query=None, item=None, flush=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputAccumulator", "Constructor of XSDataInputAccumulator", flush, "XSDataBoolean")
		self.__flush = flush
		if item is None:
			self.__item = []
		else:
			checkType("XSDataInputAccumulator", "Constructor of XSDataInputAccumulator", item, "list")
			self.__item = item
		if query is None:
			self.__query = []
		else:
			checkType("XSDataInputAccumulator", "Constructor of XSDataInputAccumulator", query, "list")
			self.__query = query
	def getFlush(self): return self.__flush
	def setFlush(self, flush):
		checkType("XSDataInputAccumulator", "setFlush", flush, "XSDataBoolean")
		self.__flush = flush
	def delFlush(self): self.__flush = None
	# Properties
	flush = property(getFlush, setFlush, delFlush, "Property for flush")
	def getItem(self): return self.__item
	def setItem(self, item):
		checkType("XSDataInputAccumulator", "setItem", item, "list")
		self.__item = item
	def delItem(self): self.__item = None
	# Properties
	item = property(getItem, setItem, delItem, "Property for item")
	def addItem(self, value):
		checkType("XSDataInputAccumulator", "setItem", value, "XSDataString")
		self.__item.append(value)
	def insertItem(self, index, value):
		checkType("XSDataInputAccumulator", "setItem", value, "XSDataString")
		self.__item[index] = value
	def getQuery(self): return self.__query
	def setQuery(self, query):
		checkType("XSDataInputAccumulator", "setQuery", query, "list")
		self.__query = query
	def delQuery(self): self.__query = None
	# Properties
	query = property(getQuery, setQuery, delQuery, "Property for query")
	def addQuery(self, value):
		checkType("XSDataInputAccumulator", "setQuery", value, "XSDataQuery")
		self.__query.append(value)
	def insertQuery(self, index, value):
		checkType("XSDataInputAccumulator", "setQuery", value, "XSDataQuery")
		self.__query[index] = value
	def export(self, outfile, level, name_='XSDataInputAccumulator'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputAccumulator'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__flush is not None:
			self.flush.export(outfile, level, name_='flush')
		for item_ in self.getItem():
			item_.export(outfile, level, name_='item')
		for query_ in self.getQuery():
			query_.export(outfile, level, name_='query')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'flush':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setFlush(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'item':
			obj_ = XSDataString()
			obj_.build(child_)
			self.item.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'query':
			obj_ = XSDataQuery()
			obj_.build(child_)
			self.query.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputAccumulator" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputAccumulator' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputAccumulator is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputAccumulator.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputAccumulator()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputAccumulator" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputAccumulator()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputAccumulator

class XSDataResultAccumulator(XSDataResult):
	def __init__(self, status=None, query=None):
		XSDataResult.__init__(self, status)
		if query is None:
			self.__query = []
		else:
			checkType("XSDataResultAccumulator", "Constructor of XSDataResultAccumulator", query, "list")
			self.__query = query
	def getQuery(self): return self.__query
	def setQuery(self, query):
		checkType("XSDataResultAccumulator", "setQuery", query, "list")
		self.__query = query
	def delQuery(self): self.__query = None
	# Properties
	query = property(getQuery, setQuery, delQuery, "Property for query")
	def addQuery(self, value):
		checkType("XSDataResultAccumulator", "setQuery", value, "XSDataQuery")
		self.__query.append(value)
	def insertQuery(self, index, value):
		checkType("XSDataResultAccumulator", "setQuery", value, "XSDataQuery")
		self.__query[index] = value
	def export(self, outfile, level, name_='XSDataResultAccumulator'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultAccumulator'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for query_ in self.getQuery():
			query_.export(outfile, level, name_='query')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'query':
			obj_ = XSDataQuery()
			obj_.build(child_)
			self.query.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultAccumulator" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultAccumulator' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultAccumulator is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultAccumulator.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultAccumulator()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultAccumulator" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultAccumulator()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultAccumulator

# End of data representation classes.


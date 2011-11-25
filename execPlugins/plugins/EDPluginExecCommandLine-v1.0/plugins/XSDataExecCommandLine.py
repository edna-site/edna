#!/usr/bin/env python

#
# Generated Fri Nov 25 05:38::50 2011 by EDGenerateDS.
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
}

try:
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataResult
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataResult




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


class XSDataInputExecCommandLine(XSDataInput):
	def __init__(self, configuration=None, outputPath=None, outfileFromStdout=None, inputFileType=None, inputFileName=None, fireAndForget=None, commandLineProgram=None, commandLineOptions=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", commandLineOptions, "XSDataString")
		self.__commandLineOptions = commandLineOptions
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", commandLineProgram, "XSDataFile")
		self.__commandLineProgram = commandLineProgram
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", fireAndForget, "XSDataBoolean")
		self.__fireAndForget = fireAndForget
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", inputFileName, "XSDataFile")
		self.__inputFileName = inputFileName
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", inputFileType, "XSDataString")
		self.__inputFileType = inputFileType
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", outfileFromStdout, "XSDataBoolean")
		self.__outfileFromStdout = outfileFromStdout
		checkType("XSDataInputExecCommandLine", "Constructor of XSDataInputExecCommandLine", outputPath, "XSDataFile")
		self.__outputPath = outputPath
	def getCommandLineOptions(self): return self.__commandLineOptions
	def setCommandLineOptions(self, commandLineOptions):
		checkType("XSDataInputExecCommandLine", "setCommandLineOptions", commandLineOptions, "XSDataString")
		self.__commandLineOptions = commandLineOptions
	def delCommandLineOptions(self): self.__commandLineOptions = None
	# Properties
	commandLineOptions = property(getCommandLineOptions, setCommandLineOptions, delCommandLineOptions, "Property for commandLineOptions")
	def getCommandLineProgram(self): return self.__commandLineProgram
	def setCommandLineProgram(self, commandLineProgram):
		checkType("XSDataInputExecCommandLine", "setCommandLineProgram", commandLineProgram, "XSDataFile")
		self.__commandLineProgram = commandLineProgram
	def delCommandLineProgram(self): self.__commandLineProgram = None
	# Properties
	commandLineProgram = property(getCommandLineProgram, setCommandLineProgram, delCommandLineProgram, "Property for commandLineProgram")
	def getFireAndForget(self): return self.__fireAndForget
	def setFireAndForget(self, fireAndForget):
		checkType("XSDataInputExecCommandLine", "setFireAndForget", fireAndForget, "XSDataBoolean")
		self.__fireAndForget = fireAndForget
	def delFireAndForget(self): self.__fireAndForget = None
	# Properties
	fireAndForget = property(getFireAndForget, setFireAndForget, delFireAndForget, "Property for fireAndForget")
	def getInputFileName(self): return self.__inputFileName
	def setInputFileName(self, inputFileName):
		checkType("XSDataInputExecCommandLine", "setInputFileName", inputFileName, "XSDataFile")
		self.__inputFileName = inputFileName
	def delInputFileName(self): self.__inputFileName = None
	# Properties
	inputFileName = property(getInputFileName, setInputFileName, delInputFileName, "Property for inputFileName")
	def getInputFileType(self): return self.__inputFileType
	def setInputFileType(self, inputFileType):
		checkType("XSDataInputExecCommandLine", "setInputFileType", inputFileType, "XSDataString")
		self.__inputFileType = inputFileType
	def delInputFileType(self): self.__inputFileType = None
	# Properties
	inputFileType = property(getInputFileType, setInputFileType, delInputFileType, "Property for inputFileType")
	def getOutfileFromStdout(self): return self.__outfileFromStdout
	def setOutfileFromStdout(self, outfileFromStdout):
		checkType("XSDataInputExecCommandLine", "setOutfileFromStdout", outfileFromStdout, "XSDataBoolean")
		self.__outfileFromStdout = outfileFromStdout
	def delOutfileFromStdout(self): self.__outfileFromStdout = None
	# Properties
	outfileFromStdout = property(getOutfileFromStdout, setOutfileFromStdout, delOutfileFromStdout, "Property for outfileFromStdout")
	def getOutputPath(self): return self.__outputPath
	def setOutputPath(self, outputPath):
		checkType("XSDataInputExecCommandLine", "setOutputPath", outputPath, "XSDataFile")
		self.__outputPath = outputPath
	def delOutputPath(self): self.__outputPath = None
	# Properties
	outputPath = property(getOutputPath, setOutputPath, delOutputPath, "Property for outputPath")
	def export(self, outfile, level, name_='XSDataInputExecCommandLine'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputExecCommandLine'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__commandLineOptions is not None:
			self.commandLineOptions.export(outfile, level, name_='commandLineOptions')
		if self.__commandLineProgram is not None:
			self.commandLineProgram.export(outfile, level, name_='commandLineProgram')
		else:
			warnEmptyAttribute("commandLineProgram", "XSDataFile")
		if self.__fireAndForget is not None:
			self.fireAndForget.export(outfile, level, name_='fireAndForget')
		if self.__inputFileName is not None:
			self.inputFileName.export(outfile, level, name_='inputFileName')
		else:
			warnEmptyAttribute("inputFileName", "XSDataFile")
		if self.__inputFileType is not None:
			self.inputFileType.export(outfile, level, name_='inputFileType')
		if self.__outfileFromStdout is not None:
			self.outfileFromStdout.export(outfile, level, name_='outfileFromStdout')
		if self.__outputPath is not None:
			self.outputPath.export(outfile, level, name_='outputPath')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'commandLineOptions':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCommandLineOptions(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'commandLineProgram':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setCommandLineProgram(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fireAndForget':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setFireAndForget(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputFileName':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputFileName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputFileType':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInputFileType(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outfileFromStdout':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setOutfileFromStdout(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputPath':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputPath(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputExecCommandLine" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputExecCommandLine' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputExecCommandLine is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputExecCommandLine.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputExecCommandLine()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputExecCommandLine" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputExecCommandLine()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputExecCommandLine

class XSDataInputRsync(XSDataInput):
	def __init__(self, configuration=None, fireAndForget=None, destination=None, source=None, options=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputRsync", "Constructor of XSDataInputRsync", options, "XSDataString")
		self.__options = options
		checkType("XSDataInputRsync", "Constructor of XSDataInputRsync", source, "XSDataString")
		self.__source = source
		checkType("XSDataInputRsync", "Constructor of XSDataInputRsync", destination, "XSDataString")
		self.__destination = destination
		checkType("XSDataInputRsync", "Constructor of XSDataInputRsync", fireAndForget, "XSDataBoolean")
		self.__fireAndForget = fireAndForget
	def getOptions(self): return self.__options
	def setOptions(self, options):
		checkType("XSDataInputRsync", "setOptions", options, "XSDataString")
		self.__options = options
	def delOptions(self): self.__options = None
	# Properties
	options = property(getOptions, setOptions, delOptions, "Property for options")
	def getSource(self): return self.__source
	def setSource(self, source):
		checkType("XSDataInputRsync", "setSource", source, "XSDataString")
		self.__source = source
	def delSource(self): self.__source = None
	# Properties
	source = property(getSource, setSource, delSource, "Property for source")
	def getDestination(self): return self.__destination
	def setDestination(self, destination):
		checkType("XSDataInputRsync", "setDestination", destination, "XSDataString")
		self.__destination = destination
	def delDestination(self): self.__destination = None
	# Properties
	destination = property(getDestination, setDestination, delDestination, "Property for destination")
	def getFireAndForget(self): return self.__fireAndForget
	def setFireAndForget(self, fireAndForget):
		checkType("XSDataInputRsync", "setFireAndForget", fireAndForget, "XSDataBoolean")
		self.__fireAndForget = fireAndForget
	def delFireAndForget(self): self.__fireAndForget = None
	# Properties
	fireAndForget = property(getFireAndForget, setFireAndForget, delFireAndForget, "Property for fireAndForget")
	def export(self, outfile, level, name_='XSDataInputRsync'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputRsync'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__options is not None:
			self.options.export(outfile, level, name_='options')
		if self.__source is not None:
			self.source.export(outfile, level, name_='source')
		else:
			warnEmptyAttribute("source", "XSDataString")
		if self.__destination is not None:
			self.destination.export(outfile, level, name_='destination')
		else:
			warnEmptyAttribute("destination", "XSDataString")
		if self.__fireAndForget is not None:
			self.fireAndForget.export(outfile, level, name_='fireAndForget')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'options':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOptions(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'source':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSource(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'destination':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDestination(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fireAndForget':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setFireAndForget(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputRsync" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputRsync' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputRsync is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputRsync.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputRsync()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputRsync" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputRsync()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputRsync

class XSDataResultExecCommandLine(XSDataResult):
	def __init__(self, status=None, outputFilename=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultExecCommandLine", "Constructor of XSDataResultExecCommandLine", outputFilename, "XSDataFile")
		self.__outputFilename = outputFilename
	def getOutputFilename(self): return self.__outputFilename
	def setOutputFilename(self, outputFilename):
		checkType("XSDataResultExecCommandLine", "setOutputFilename", outputFilename, "XSDataFile")
		self.__outputFilename = outputFilename
	def delOutputFilename(self): self.__outputFilename = None
	# Properties
	outputFilename = property(getOutputFilename, setOutputFilename, delOutputFilename, "Property for outputFilename")
	def export(self, outfile, level, name_='XSDataResultExecCommandLine'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultExecCommandLine'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputFilename is not None:
			self.outputFilename.export(outfile, level, name_='outputFilename')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputFilename':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputFilename(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultExecCommandLine" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultExecCommandLine' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultExecCommandLine is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultExecCommandLine.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultExecCommandLine()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultExecCommandLine" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultExecCommandLine()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultExecCommandLine

class XSDataResultExecCommandLine(XSDataResult):
	def __init__(self, status=None, log=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultExecCommandLine", "Constructor of XSDataResultExecCommandLine", log, "XSDataString")
		self.__log = log
	def getLog(self): return self.__log
	def setLog(self, log):
		checkType("XSDataResultExecCommandLine", "setLog", log, "XSDataString")
		self.__log = log
	def delLog(self): self.__log = None
	# Properties
	log = property(getLog, setLog, delLog, "Property for log")
	def export(self, outfile, level, name_='XSDataResultExecCommandLine'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultExecCommandLine'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__log is not None:
			self.log.export(outfile, level, name_='log')
		else:
			warnEmptyAttribute("log", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'log':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setLog(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultExecCommandLine" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultExecCommandLine' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultExecCommandLine is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultExecCommandLine.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultExecCommandLine()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultExecCommandLine" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultExecCommandLine()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultExecCommandLine



# End of data representation classes.



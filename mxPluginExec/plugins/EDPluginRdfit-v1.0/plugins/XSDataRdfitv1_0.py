#!/usr/bin/env python

#
# Generated Sat Oct 6 06:51::46 2012 by EDGenerateDS.
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
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInput
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
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


class XSDataInputRdfit(XSDataInput):
	def __init__(self, configuration=None, resultsXmlFile=None, resultsFile=None, bScaleIntensityGleFile=None, bScaleIntensityMtvPlotFile=None, bFactorGlePlotFile=None, bFactorMtvplotFile=None, defaultGama=None, defaultBeta=None, dmin=None, xdsHklFile=None, bestXmlFile=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", bestXmlFile, "XSDataFile")
		self._bestXmlFile = bestXmlFile
		if xdsHklFile is None:
			self._xdsHklFile = []
		else:
			checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", xdsHklFile, "list")
			self._xdsHklFile = xdsHklFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", dmin, "XSDataDouble")
		self._dmin = dmin
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", defaultBeta, "XSDataDouble")
		self._defaultBeta = defaultBeta
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", defaultGama, "XSDataDouble")
		self._defaultGama = defaultGama
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", bFactorMtvplotFile, "XSDataFile")
		self._bFactorMtvplotFile = bFactorMtvplotFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", bFactorGlePlotFile, "XSDataFile")
		self._bFactorGlePlotFile = bFactorGlePlotFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", bScaleIntensityMtvPlotFile, "XSDataFile")
		self._bScaleIntensityMtvPlotFile = bScaleIntensityMtvPlotFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", bScaleIntensityGleFile, "XSDataFile")
		self._bScaleIntensityGleFile = bScaleIntensityGleFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", resultsFile, "XSDataFile")
		self._resultsFile = resultsFile
		checkType("XSDataInputRdfit", "Constructor of XSDataInputRdfit", resultsXmlFile, "XSDataFile")
		self._resultsXmlFile = resultsXmlFile
	def getBestXmlFile(self): return self._bestXmlFile
	def setBestXmlFile(self, bestXmlFile):
		checkType("XSDataInputRdfit", "setBestXmlFile", bestXmlFile, "XSDataFile")
		self._bestXmlFile = bestXmlFile
	def delBestXmlFile(self): self._bestXmlFile = None
	# Properties
	bestXmlFile = property(getBestXmlFile, setBestXmlFile, delBestXmlFile, "Property for bestXmlFile")
	def getXdsHklFile(self): return self._xdsHklFile
	def setXdsHklFile(self, xdsHklFile):
		checkType("XSDataInputRdfit", "setXdsHklFile", xdsHklFile, "list")
		self._xdsHklFile = xdsHklFile
	def delXdsHklFile(self): self._xdsHklFile = None
	# Properties
	xdsHklFile = property(getXdsHklFile, setXdsHklFile, delXdsHklFile, "Property for xdsHklFile")
	def addXdsHklFile(self, value):
		checkType("XSDataInputRdfit", "setXdsHklFile", value, "XSDataFile")
		self._xdsHklFile.append(value)
	def insertXdsHklFile(self, index, value):
		checkType("XSDataInputRdfit", "setXdsHklFile", value, "XSDataFile")
		self._xdsHklFile[index] = value
	def getDmin(self): return self._dmin
	def setDmin(self, dmin):
		checkType("XSDataInputRdfit", "setDmin", dmin, "XSDataDouble")
		self._dmin = dmin
	def delDmin(self): self._dmin = None
	# Properties
	dmin = property(getDmin, setDmin, delDmin, "Property for dmin")
	def getDefaultBeta(self): return self._defaultBeta
	def setDefaultBeta(self, defaultBeta):
		checkType("XSDataInputRdfit", "setDefaultBeta", defaultBeta, "XSDataDouble")
		self._defaultBeta = defaultBeta
	def delDefaultBeta(self): self._defaultBeta = None
	# Properties
	defaultBeta = property(getDefaultBeta, setDefaultBeta, delDefaultBeta, "Property for defaultBeta")
	def getDefaultGama(self): return self._defaultGama
	def setDefaultGama(self, defaultGama):
		checkType("XSDataInputRdfit", "setDefaultGama", defaultGama, "XSDataDouble")
		self._defaultGama = defaultGama
	def delDefaultGama(self): self._defaultGama = None
	# Properties
	defaultGama = property(getDefaultGama, setDefaultGama, delDefaultGama, "Property for defaultGama")
	def getBFactorMtvplotFile(self): return self._bFactorMtvplotFile
	def setBFactorMtvplotFile(self, bFactorMtvplotFile):
		checkType("XSDataInputRdfit", "setBFactorMtvplotFile", bFactorMtvplotFile, "XSDataFile")
		self._bFactorMtvplotFile = bFactorMtvplotFile
	def delBFactorMtvplotFile(self): self._bFactorMtvplotFile = None
	# Properties
	bFactorMtvplotFile = property(getBFactorMtvplotFile, setBFactorMtvplotFile, delBFactorMtvplotFile, "Property for bFactorMtvplotFile")
	def getBFactorGlePlotFile(self): return self._bFactorGlePlotFile
	def setBFactorGlePlotFile(self, bFactorGlePlotFile):
		checkType("XSDataInputRdfit", "setBFactorGlePlotFile", bFactorGlePlotFile, "XSDataFile")
		self._bFactorGlePlotFile = bFactorGlePlotFile
	def delBFactorGlePlotFile(self): self._bFactorGlePlotFile = None
	# Properties
	bFactorGlePlotFile = property(getBFactorGlePlotFile, setBFactorGlePlotFile, delBFactorGlePlotFile, "Property for bFactorGlePlotFile")
	def getBScaleIntensityMtvPlotFile(self): return self._bScaleIntensityMtvPlotFile
	def setBScaleIntensityMtvPlotFile(self, bScaleIntensityMtvPlotFile):
		checkType("XSDataInputRdfit", "setBScaleIntensityMtvPlotFile", bScaleIntensityMtvPlotFile, "XSDataFile")
		self._bScaleIntensityMtvPlotFile = bScaleIntensityMtvPlotFile
	def delBScaleIntensityMtvPlotFile(self): self._bScaleIntensityMtvPlotFile = None
	# Properties
	bScaleIntensityMtvPlotFile = property(getBScaleIntensityMtvPlotFile, setBScaleIntensityMtvPlotFile, delBScaleIntensityMtvPlotFile, "Property for bScaleIntensityMtvPlotFile")
	def getBScaleIntensityGleFile(self): return self._bScaleIntensityGleFile
	def setBScaleIntensityGleFile(self, bScaleIntensityGleFile):
		checkType("XSDataInputRdfit", "setBScaleIntensityGleFile", bScaleIntensityGleFile, "XSDataFile")
		self._bScaleIntensityGleFile = bScaleIntensityGleFile
	def delBScaleIntensityGleFile(self): self._bScaleIntensityGleFile = None
	# Properties
	bScaleIntensityGleFile = property(getBScaleIntensityGleFile, setBScaleIntensityGleFile, delBScaleIntensityGleFile, "Property for bScaleIntensityGleFile")
	def getResultsFile(self): return self._resultsFile
	def setResultsFile(self, resultsFile):
		checkType("XSDataInputRdfit", "setResultsFile", resultsFile, "XSDataFile")
		self._resultsFile = resultsFile
	def delResultsFile(self): self._resultsFile = None
	# Properties
	resultsFile = property(getResultsFile, setResultsFile, delResultsFile, "Property for resultsFile")
	def getResultsXmlFile(self): return self._resultsXmlFile
	def setResultsXmlFile(self, resultsXmlFile):
		checkType("XSDataInputRdfit", "setResultsXmlFile", resultsXmlFile, "XSDataFile")
		self._resultsXmlFile = resultsXmlFile
	def delResultsXmlFile(self): self._resultsXmlFile = None
	# Properties
	resultsXmlFile = property(getResultsXmlFile, setResultsXmlFile, delResultsXmlFile, "Property for resultsXmlFile")
	def export(self, outfile, level, name_='XSDataInputRdfit'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputRdfit'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._bestXmlFile is not None:
			self.bestXmlFile.export(outfile, level, name_='bestXmlFile')
		else:
			warnEmptyAttribute("bestXmlFile", "XSDataFile")
		for xdsHklFile_ in self.getXdsHklFile():
			xdsHklFile_.export(outfile, level, name_='xdsHklFile')
		if self.getXdsHklFile() == []:
			warnEmptyAttribute("xdsHklFile", "XSDataFile")
		if self._dmin is not None:
			self.dmin.export(outfile, level, name_='dmin')
		if self._defaultBeta is not None:
			self.defaultBeta.export(outfile, level, name_='defaultBeta')
		if self._defaultGama is not None:
			self.defaultGama.export(outfile, level, name_='defaultGama')
		if self._bFactorMtvplotFile is not None:
			self.bFactorMtvplotFile.export(outfile, level, name_='bFactorMtvplotFile')
		if self._bFactorGlePlotFile is not None:
			self.bFactorGlePlotFile.export(outfile, level, name_='bFactorGlePlotFile')
		if self._bScaleIntensityMtvPlotFile is not None:
			self.bScaleIntensityMtvPlotFile.export(outfile, level, name_='bScaleIntensityMtvPlotFile')
		if self._bScaleIntensityGleFile is not None:
			self.bScaleIntensityGleFile.export(outfile, level, name_='bScaleIntensityGleFile')
		if self._resultsFile is not None:
			self.resultsFile.export(outfile, level, name_='resultsFile')
		if self._resultsXmlFile is not None:
			self.resultsXmlFile.export(outfile, level, name_='resultsXmlFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bestXmlFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBestXmlFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xdsHklFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.xdsHklFile.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dmin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDmin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'defaultBeta':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDefaultBeta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'defaultGama':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDefaultGama(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bFactorMtvplotFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBFactorMtvplotFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bFactorGlePlotFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBFactorGlePlotFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bScaleIntensityMtvPlotFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBScaleIntensityMtvPlotFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bScaleIntensityGleFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setBScaleIntensityGleFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultsFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setResultsFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resultsXmlFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setResultsXmlFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputRdfit" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputRdfit' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputRdfit is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputRdfit.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputRdfit()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputRdfit" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputRdfit()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputRdfit

class XSDataResultRdfit(XSDataResult):
	def __init__(self, status=None, relative_radiation_sensitivity=None, dose_half=None, dose_half_th=None, gama=None, beta=None):
		XSDataResult.__init__(self, status)
	
	
		checkType("XSDataResultRdfit", "Constructor of XSDataResultRdfit", beta, "XSDataDouble")
		self._beta = beta
		checkType("XSDataResultRdfit", "Constructor of XSDataResultRdfit", gama, "XSDataDouble")
		self._gama = gama
		checkType("XSDataResultRdfit", "Constructor of XSDataResultRdfit", dose_half_th, "XSDataDouble")
		self._dose_half_th = dose_half_th
		checkType("XSDataResultRdfit", "Constructor of XSDataResultRdfit", dose_half, "XSDataDouble")
		self._dose_half = dose_half
		checkType("XSDataResultRdfit", "Constructor of XSDataResultRdfit", relative_radiation_sensitivity, "XSDataDouble")
		self._relative_radiation_sensitivity = relative_radiation_sensitivity
	def getBeta(self): return self._beta
	def setBeta(self, beta):
		checkType("XSDataResultRdfit", "setBeta", beta, "XSDataDouble")
		self._beta = beta
	def delBeta(self): self._beta = None
	# Properties
	beta = property(getBeta, setBeta, delBeta, "Property for beta")
	def getGama(self): return self._gama
	def setGama(self, gama):
		checkType("XSDataResultRdfit", "setGama", gama, "XSDataDouble")
		self._gama = gama
	def delGama(self): self._gama = None
	# Properties
	gama = property(getGama, setGama, delGama, "Property for gama")
	def getDose_half_th(self): return self._dose_half_th
	def setDose_half_th(self, dose_half_th):
		checkType("XSDataResultRdfit", "setDose_half_th", dose_half_th, "XSDataDouble")
		self._dose_half_th = dose_half_th
	def delDose_half_th(self): self._dose_half_th = None
	# Properties
	dose_half_th = property(getDose_half_th, setDose_half_th, delDose_half_th, "Property for dose_half_th")
	def getDose_half(self): return self._dose_half
	def setDose_half(self, dose_half):
		checkType("XSDataResultRdfit", "setDose_half", dose_half, "XSDataDouble")
		self._dose_half = dose_half
	def delDose_half(self): self._dose_half = None
	# Properties
	dose_half = property(getDose_half, setDose_half, delDose_half, "Property for dose_half")
	def getRelative_radiation_sensitivity(self): return self._relative_radiation_sensitivity
	def setRelative_radiation_sensitivity(self, relative_radiation_sensitivity):
		checkType("XSDataResultRdfit", "setRelative_radiation_sensitivity", relative_radiation_sensitivity, "XSDataDouble")
		self._relative_radiation_sensitivity = relative_radiation_sensitivity
	def delRelative_radiation_sensitivity(self): self._relative_radiation_sensitivity = None
	# Properties
	relative_radiation_sensitivity = property(getRelative_radiation_sensitivity, setRelative_radiation_sensitivity, delRelative_radiation_sensitivity, "Property for relative_radiation_sensitivity")
	def export(self, outfile, level, name_='XSDataResultRdfit'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultRdfit'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self._beta is not None:
			self.beta.export(outfile, level, name_='beta')
		if self._gama is not None:
			self.gama.export(outfile, level, name_='gama')
		if self._dose_half_th is not None:
			self.dose_half_th.export(outfile, level, name_='dose_half_th')
		if self._dose_half is not None:
			self.dose_half.export(outfile, level, name_='dose_half')
		if self._relative_radiation_sensitivity is not None:
			self.relative_radiation_sensitivity.export(outfile, level, name_='relative_radiation_sensitivity')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beta':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gama':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setGama(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dose_half_th':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDose_half_th(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'dose_half':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDose_half(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'relative_radiation_sensitivity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRelative_radiation_sensitivity(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultRdfit" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultRdfit' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultRdfit is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultRdfit.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultRdfit()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultRdfit" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultRdfit()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultRdfit



# End of data representation classes.



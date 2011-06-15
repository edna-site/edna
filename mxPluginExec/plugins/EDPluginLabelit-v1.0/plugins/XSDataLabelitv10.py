#!/usr/bin/env python

#
# Generated Tue Jun 14 12:05::47 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength




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


class XSDataCell(object):
	def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
		checkType("XSDataCell", "Constructor of XSDataCell", angle_alpha, "XSDataAngle")
		self.__angle_alpha = angle_alpha
		checkType("XSDataCell", "Constructor of XSDataCell", angle_beta, "XSDataAngle")
		self.__angle_beta = angle_beta
		checkType("XSDataCell", "Constructor of XSDataCell", angle_gamma, "XSDataAngle")
		self.__angle_gamma = angle_gamma
		checkType("XSDataCell", "Constructor of XSDataCell", length_a, "XSDataLength")
		self.__length_a = length_a
		checkType("XSDataCell", "Constructor of XSDataCell", length_b, "XSDataLength")
		self.__length_b = length_b
		checkType("XSDataCell", "Constructor of XSDataCell", length_c, "XSDataLength")
		self.__length_c = length_c
	def getAngle_alpha(self): return self.__angle_alpha
	def setAngle_alpha(self, angle_alpha):
		checkType("XSDataCell", "setAngle_alpha", angle_alpha, "XSDataAngle")
		self.__angle_alpha = angle_alpha
	def delAngle_alpha(self): self.__angle_alpha = None
	# Properties
	angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
	def getAngle_beta(self): return self.__angle_beta
	def setAngle_beta(self, angle_beta):
		checkType("XSDataCell", "setAngle_beta", angle_beta, "XSDataAngle")
		self.__angle_beta = angle_beta
	def delAngle_beta(self): self.__angle_beta = None
	# Properties
	angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
	def getAngle_gamma(self): return self.__angle_gamma
	def setAngle_gamma(self, angle_gamma):
		checkType("XSDataCell", "setAngle_gamma", angle_gamma, "XSDataAngle")
		self.__angle_gamma = angle_gamma
	def delAngle_gamma(self): self.__angle_gamma = None
	# Properties
	angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
	def getLength_a(self): return self.__length_a
	def setLength_a(self, length_a):
		checkType("XSDataCell", "setLength_a", length_a, "XSDataLength")
		self.__length_a = length_a
	def delLength_a(self): self.__length_a = None
	# Properties
	length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
	def getLength_b(self): return self.__length_b
	def setLength_b(self, length_b):
		checkType("XSDataCell", "setLength_b", length_b, "XSDataLength")
		self.__length_b = length_b
	def delLength_b(self): self.__length_b = None
	# Properties
	length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
	def getLength_c(self): return self.__length_c
	def setLength_c(self, length_c):
		checkType("XSDataCell", "setLength_c", length_c, "XSDataLength")
		self.__length_c = length_c
	def delLength_c(self): self.__length_c = None
	# Properties
	length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
	def export(self, outfile, level, name_='XSDataCell'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCell'):
		pass
		if self.__angle_alpha is not None:
			self.angle_alpha.export(outfile, level, name_='angle_alpha')
		else:
			warnEmptyAttribute("angle_alpha", "XSDataAngle")
		if self.__angle_beta is not None:
			self.angle_beta.export(outfile, level, name_='angle_beta')
		else:
			warnEmptyAttribute("angle_beta", "XSDataAngle")
		if self.__angle_gamma is not None:
			self.angle_gamma.export(outfile, level, name_='angle_gamma')
		else:
			warnEmptyAttribute("angle_gamma", "XSDataAngle")
		if self.__length_a is not None:
			self.length_a.export(outfile, level, name_='length_a')
		else:
			warnEmptyAttribute("length_a", "XSDataLength")
		if self.__length_b is not None:
			self.length_b.export(outfile, level, name_='length_b')
		else:
			warnEmptyAttribute("length_b", "XSDataLength")
		if self.__length_c is not None:
			self.length_c.export(outfile, level, name_='length_c')
		else:
			warnEmptyAttribute("length_c", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_alpha':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_alpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_beta':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_beta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_gamma':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_gamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_a':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_a(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_b':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_b(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'length_c':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setLength_c(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCell" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCell' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataCell is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCell.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCell()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCell" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCell()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCell

class XSDataLabelitMosflmScriptsOutput(XSData):
	def __init__(self, uMatrix=None, aMatrix=None):
		XSData.__init__(self, )
		checkType("XSDataLabelitMosflmScriptsOutput", "Constructor of XSDataLabelitMosflmScriptsOutput", aMatrix, "XSDataMatrixDouble")
		self.__aMatrix = aMatrix
		checkType("XSDataLabelitMosflmScriptsOutput", "Constructor of XSDataLabelitMosflmScriptsOutput", uMatrix, "XSDataMatrixDouble")
		self.__uMatrix = uMatrix
	def getAMatrix(self): return self.__aMatrix
	def setAMatrix(self, aMatrix):
		checkType("XSDataLabelitMosflmScriptsOutput", "setAMatrix", aMatrix, "XSDataMatrixDouble")
		self.__aMatrix = aMatrix
	def delAMatrix(self): self.__aMatrix = None
	# Properties
	aMatrix = property(getAMatrix, setAMatrix, delAMatrix, "Property for aMatrix")
	def getUMatrix(self): return self.__uMatrix
	def setUMatrix(self, uMatrix):
		checkType("XSDataLabelitMosflmScriptsOutput", "setUMatrix", uMatrix, "XSDataMatrixDouble")
		self.__uMatrix = uMatrix
	def delUMatrix(self): self.__uMatrix = None
	# Properties
	uMatrix = property(getUMatrix, setUMatrix, delUMatrix, "Property for uMatrix")
	def export(self, outfile, level, name_='XSDataLabelitMosflmScriptsOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataLabelitMosflmScriptsOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__aMatrix is not None:
			self.aMatrix.export(outfile, level, name_='aMatrix')
		else:
			warnEmptyAttribute("aMatrix", "XSDataMatrixDouble")
		if self.__uMatrix is not None:
			self.uMatrix.export(outfile, level, name_='uMatrix')
		else:
			warnEmptyAttribute("uMatrix", "XSDataMatrixDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aMatrix':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setAMatrix(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'uMatrix':
			obj_ = XSDataMatrixDouble()
			obj_.build(child_)
			self.setUMatrix(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataLabelitMosflmScriptsOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataLabelitMosflmScriptsOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataLabelitMosflmScriptsOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataLabelitMosflmScriptsOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitMosflmScriptsOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataLabelitMosflmScriptsOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitMosflmScriptsOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataLabelitMosflmScriptsOutput

class XSDataLabelitScreenSolution(XSData):
	def __init__(self, volume=None, unitCell=None, solutionNumber=None, rmsd=None, numberOfSpots=None, metricFitValue=None, metricFitCode=None, happy=None, crystalSystem=None, bravaisLattice=None):
		XSData.__init__(self, )
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", crystalSystem, "XSDataString")
		self.__crystalSystem = crystalSystem
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", happy, "XSDataBoolean")
		self.__happy = happy
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", metricFitCode, "XSDataString")
		self.__metricFitCode = metricFitCode
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", metricFitValue, "XSDataDouble")
		self.__metricFitValue = metricFitValue
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", numberOfSpots, "XSDataInteger")
		self.__numberOfSpots = numberOfSpots
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", rmsd, "XSDataLength")
		self.__rmsd = rmsd
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", solutionNumber, "XSDataInteger")
		self.__solutionNumber = solutionNumber
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", unitCell, "XSDataCell")
		self.__unitCell = unitCell
		checkType("XSDataLabelitScreenSolution", "Constructor of XSDataLabelitScreenSolution", volume, "XSDataInteger")
		self.__volume = volume
	def getBravaisLattice(self): return self.__bravaisLattice
	def setBravaisLattice(self, bravaisLattice):
		checkType("XSDataLabelitScreenSolution", "setBravaisLattice", bravaisLattice, "XSDataString")
		self.__bravaisLattice = bravaisLattice
	def delBravaisLattice(self): self.__bravaisLattice = None
	# Properties
	bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
	def getCrystalSystem(self): return self.__crystalSystem
	def setCrystalSystem(self, crystalSystem):
		checkType("XSDataLabelitScreenSolution", "setCrystalSystem", crystalSystem, "XSDataString")
		self.__crystalSystem = crystalSystem
	def delCrystalSystem(self): self.__crystalSystem = None
	# Properties
	crystalSystem = property(getCrystalSystem, setCrystalSystem, delCrystalSystem, "Property for crystalSystem")
	def getHappy(self): return self.__happy
	def setHappy(self, happy):
		checkType("XSDataLabelitScreenSolution", "setHappy", happy, "XSDataBoolean")
		self.__happy = happy
	def delHappy(self): self.__happy = None
	# Properties
	happy = property(getHappy, setHappy, delHappy, "Property for happy")
	def getMetricFitCode(self): return self.__metricFitCode
	def setMetricFitCode(self, metricFitCode):
		checkType("XSDataLabelitScreenSolution", "setMetricFitCode", metricFitCode, "XSDataString")
		self.__metricFitCode = metricFitCode
	def delMetricFitCode(self): self.__metricFitCode = None
	# Properties
	metricFitCode = property(getMetricFitCode, setMetricFitCode, delMetricFitCode, "Property for metricFitCode")
	def getMetricFitValue(self): return self.__metricFitValue
	def setMetricFitValue(self, metricFitValue):
		checkType("XSDataLabelitScreenSolution", "setMetricFitValue", metricFitValue, "XSDataDouble")
		self.__metricFitValue = metricFitValue
	def delMetricFitValue(self): self.__metricFitValue = None
	# Properties
	metricFitValue = property(getMetricFitValue, setMetricFitValue, delMetricFitValue, "Property for metricFitValue")
	def getNumberOfSpots(self): return self.__numberOfSpots
	def setNumberOfSpots(self, numberOfSpots):
		checkType("XSDataLabelitScreenSolution", "setNumberOfSpots", numberOfSpots, "XSDataInteger")
		self.__numberOfSpots = numberOfSpots
	def delNumberOfSpots(self): self.__numberOfSpots = None
	# Properties
	numberOfSpots = property(getNumberOfSpots, setNumberOfSpots, delNumberOfSpots, "Property for numberOfSpots")
	def getRmsd(self): return self.__rmsd
	def setRmsd(self, rmsd):
		checkType("XSDataLabelitScreenSolution", "setRmsd", rmsd, "XSDataLength")
		self.__rmsd = rmsd
	def delRmsd(self): self.__rmsd = None
	# Properties
	rmsd = property(getRmsd, setRmsd, delRmsd, "Property for rmsd")
	def getSolutionNumber(self): return self.__solutionNumber
	def setSolutionNumber(self, solutionNumber):
		checkType("XSDataLabelitScreenSolution", "setSolutionNumber", solutionNumber, "XSDataInteger")
		self.__solutionNumber = solutionNumber
	def delSolutionNumber(self): self.__solutionNumber = None
	# Properties
	solutionNumber = property(getSolutionNumber, setSolutionNumber, delSolutionNumber, "Property for solutionNumber")
	def getUnitCell(self): return self.__unitCell
	def setUnitCell(self, unitCell):
		checkType("XSDataLabelitScreenSolution", "setUnitCell", unitCell, "XSDataCell")
		self.__unitCell = unitCell
	def delUnitCell(self): self.__unitCell = None
	# Properties
	unitCell = property(getUnitCell, setUnitCell, delUnitCell, "Property for unitCell")
	def getVolume(self): return self.__volume
	def setVolume(self, volume):
		checkType("XSDataLabelitScreenSolution", "setVolume", volume, "XSDataInteger")
		self.__volume = volume
	def delVolume(self): self.__volume = None
	# Properties
	volume = property(getVolume, setVolume, delVolume, "Property for volume")
	def export(self, outfile, level, name_='XSDataLabelitScreenSolution'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataLabelitScreenSolution'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__bravaisLattice is not None:
			self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
		else:
			warnEmptyAttribute("bravaisLattice", "XSDataString")
		if self.__crystalSystem is not None:
			self.crystalSystem.export(outfile, level, name_='crystalSystem')
		else:
			warnEmptyAttribute("crystalSystem", "XSDataString")
		if self.__happy is not None:
			self.happy.export(outfile, level, name_='happy')
		else:
			warnEmptyAttribute("happy", "XSDataBoolean")
		if self.__metricFitCode is not None:
			self.metricFitCode.export(outfile, level, name_='metricFitCode')
		else:
			warnEmptyAttribute("metricFitCode", "XSDataString")
		if self.__metricFitValue is not None:
			self.metricFitValue.export(outfile, level, name_='metricFitValue')
		else:
			warnEmptyAttribute("metricFitValue", "XSDataDouble")
		if self.__numberOfSpots is not None:
			self.numberOfSpots.export(outfile, level, name_='numberOfSpots')
		else:
			warnEmptyAttribute("numberOfSpots", "XSDataInteger")
		if self.__rmsd is not None:
			self.rmsd.export(outfile, level, name_='rmsd')
		else:
			warnEmptyAttribute("rmsd", "XSDataLength")
		if self.__solutionNumber is not None:
			self.solutionNumber.export(outfile, level, name_='solutionNumber')
		else:
			warnEmptyAttribute("solutionNumber", "XSDataInteger")
		if self.__unitCell is not None:
			self.unitCell.export(outfile, level, name_='unitCell')
		else:
			warnEmptyAttribute("unitCell", "XSDataCell")
		if self.__volume is not None:
			self.volume.export(outfile, level, name_='volume')
		else:
			warnEmptyAttribute("volume", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bravaisLattice':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBravaisLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystalSystem':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setCrystalSystem(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'happy':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setHappy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'metricFitCode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMetricFitCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'metricFitValue':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMetricFitValue(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberOfSpots':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberOfSpots(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmsd':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setRmsd(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'solutionNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSolutionNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitCell':
			obj_ = XSDataCell()
			obj_.build(child_)
			self.setUnitCell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'volume':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setVolume(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataLabelitScreenSolution" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataLabelitScreenSolution' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataLabelitScreenSolution is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataLabelitScreenSolution.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitScreenSolution()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataLabelitScreenSolution" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitScreenSolution()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataLabelitScreenSolution

class XSDataLabelitScreenOutput(XSData):
	def __init__(self, labelitScreenSolution=None, selectedSolutionNumber=None, mosaicity=None, distance=None, beamCentreY=None, beamCentreX=None):
		XSData.__init__(self, )
		checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", beamCentreX, "XSDataLength")
		self.__beamCentreX = beamCentreX
		checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", beamCentreY, "XSDataLength")
		self.__beamCentreY = beamCentreY
		checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", distance, "XSDataLength")
		self.__distance = distance
		checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", mosaicity, "XSDataAngle")
		self.__mosaicity = mosaicity
		checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", selectedSolutionNumber, "XSDataInteger")
		self.__selectedSolutionNumber = selectedSolutionNumber
		if labelitScreenSolution is None:
			self.__labelitScreenSolution = []
		else:
			checkType("XSDataLabelitScreenOutput", "Constructor of XSDataLabelitScreenOutput", labelitScreenSolution, "XSDataLabelitScreenSolution")
			self.__labelitScreenSolution = labelitScreenSolution
	def getBeamCentreX(self): return self.__beamCentreX
	def setBeamCentreX(self, beamCentreX):
		checkType("XSDataLabelitScreenOutput", "setBeamCentreX", beamCentreX, "XSDataLength")
		self.__beamCentreX = beamCentreX
	def delBeamCentreX(self): self.__beamCentreX = None
	# Properties
	beamCentreX = property(getBeamCentreX, setBeamCentreX, delBeamCentreX, "Property for beamCentreX")
	def getBeamCentreY(self): return self.__beamCentreY
	def setBeamCentreY(self, beamCentreY):
		checkType("XSDataLabelitScreenOutput", "setBeamCentreY", beamCentreY, "XSDataLength")
		self.__beamCentreY = beamCentreY
	def delBeamCentreY(self): self.__beamCentreY = None
	# Properties
	beamCentreY = property(getBeamCentreY, setBeamCentreY, delBeamCentreY, "Property for beamCentreY")
	def getDistance(self): return self.__distance
	def setDistance(self, distance):
		checkType("XSDataLabelitScreenOutput", "setDistance", distance, "XSDataLength")
		self.__distance = distance
	def delDistance(self): self.__distance = None
	# Properties
	distance = property(getDistance, setDistance, delDistance, "Property for distance")
	def getMosaicity(self): return self.__mosaicity
	def setMosaicity(self, mosaicity):
		checkType("XSDataLabelitScreenOutput", "setMosaicity", mosaicity, "XSDataAngle")
		self.__mosaicity = mosaicity
	def delMosaicity(self): self.__mosaicity = None
	# Properties
	mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
	def getSelectedSolutionNumber(self): return self.__selectedSolutionNumber
	def setSelectedSolutionNumber(self, selectedSolutionNumber):
		checkType("XSDataLabelitScreenOutput", "setSelectedSolutionNumber", selectedSolutionNumber, "XSDataInteger")
		self.__selectedSolutionNumber = selectedSolutionNumber
	def delSelectedSolutionNumber(self): self.__selectedSolutionNumber = None
	# Properties
	selectedSolutionNumber = property(getSelectedSolutionNumber, setSelectedSolutionNumber, delSelectedSolutionNumber, "Property for selectedSolutionNumber")
	def getLabelitScreenSolution(self): return self.__labelitScreenSolution
	def setLabelitScreenSolution(self, labelitScreenSolution):
		checkType("XSDataLabelitScreenOutput", "setLabelitScreenSolution", labelitScreenSolution, "list")
		self.__labelitScreenSolution = labelitScreenSolution
	def delLabelitScreenSolution(self): self.__labelitScreenSolution = None
	# Properties
	labelitScreenSolution = property(getLabelitScreenSolution, setLabelitScreenSolution, delLabelitScreenSolution, "Property for labelitScreenSolution")
	def addLabelitScreenSolution(self, value):
		checkType("XSDataLabelitScreenOutput", "setLabelitScreenSolution", value, "XSDataLabelitScreenSolution")
		self.__labelitScreenSolution.append(value)
	def insertLabelitScreenSolution(self, index, value):
		checkType("XSDataLabelitScreenOutput", "setLabelitScreenSolution", value, "XSDataLabelitScreenSolution")
		self.__labelitScreenSolution[index] = value
	def export(self, outfile, level, name_='XSDataLabelitScreenOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataLabelitScreenOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__beamCentreX is not None:
			self.beamCentreX.export(outfile, level, name_='beamCentreX')
		else:
			warnEmptyAttribute("beamCentreX", "XSDataLength")
		if self.__beamCentreY is not None:
			self.beamCentreY.export(outfile, level, name_='beamCentreY')
		else:
			warnEmptyAttribute("beamCentreY", "XSDataLength")
		if self.__distance is not None:
			self.distance.export(outfile, level, name_='distance')
		else:
			warnEmptyAttribute("distance", "XSDataLength")
		if self.__mosaicity is not None:
			self.mosaicity.export(outfile, level, name_='mosaicity')
		else:
			warnEmptyAttribute("mosaicity", "XSDataAngle")
		if self.__selectedSolutionNumber is not None:
			self.selectedSolutionNumber.export(outfile, level, name_='selectedSolutionNumber')
		else:
			warnEmptyAttribute("selectedSolutionNumber", "XSDataInteger")
		for labelitScreenSolution_ in self.getLabelitScreenSolution():
			labelitScreenSolution_.export(outfile, level, name_='labelitScreenSolution')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCentreX':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamCentreX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beamCentreY':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setBeamCentreY(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDistance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicity':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setMosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedSolutionNumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSelectedSolutionNumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'labelitScreenSolution':
			obj_ = XSDataLabelitScreenSolution()
			obj_.build(child_)
			self.labelitScreenSolution.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataLabelitScreenOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataLabelitScreenOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataLabelitScreenOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataLabelitScreenOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitScreenOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataLabelitScreenOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataLabelitScreenOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataLabelitScreenOutput

class XSDataInputLabelit(XSDataInput):
	def __init__(self, configuration=None, image=None):
		XSDataInput.__init__(self, configuration)
		if image is None:
			self.__image = []
		else:
			checkType("XSDataInputLabelit", "Constructor of XSDataInputLabelit", image, "XSDataImage")
			self.__image = image
	def getImage(self): return self.__image
	def setImage(self, image):
		checkType("XSDataInputLabelit", "setImage", image, "list")
		self.__image = image
	def delImage(self): self.__image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def addImage(self, value):
		checkType("XSDataInputLabelit", "setImage", value, "XSDataImage")
		self.__image.append(value)
	def insertImage(self, index, value):
		checkType("XSDataInputLabelit", "setImage", value, "XSDataImage")
		self.__image[index] = value
	def export(self, outfile, level, name_='XSDataInputLabelit'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputLabelit'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for image_ in self.getImage():
			image_.export(outfile, level, name_='image')
		if self.getImage() == []:
			warnEmptyAttribute("image", "XSDataImage")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataImage()
			obj_.build(child_)
			self.image.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputLabelit" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputLabelit' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputLabelit is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputLabelit.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputLabelit()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputLabelit" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputLabelit()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputLabelit

class XSDataResultLabelit(XSDataResult):
	def __init__(self, status=None, labelitScreenOutput=None, labelitMosflmScriptsOutput=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultLabelit", "Constructor of XSDataResultLabelit", labelitMosflmScriptsOutput, "XSDataLabelitMosflmScriptsOutput")
		self.__labelitMosflmScriptsOutput = labelitMosflmScriptsOutput
		checkType("XSDataResultLabelit", "Constructor of XSDataResultLabelit", labelitScreenOutput, "XSDataLabelitScreenOutput")
		self.__labelitScreenOutput = labelitScreenOutput
	def getLabelitMosflmScriptsOutput(self): return self.__labelitMosflmScriptsOutput
	def setLabelitMosflmScriptsOutput(self, labelitMosflmScriptsOutput):
		checkType("XSDataResultLabelit", "setLabelitMosflmScriptsOutput", labelitMosflmScriptsOutput, "XSDataLabelitMosflmScriptsOutput")
		self.__labelitMosflmScriptsOutput = labelitMosflmScriptsOutput
	def delLabelitMosflmScriptsOutput(self): self.__labelitMosflmScriptsOutput = None
	# Properties
	labelitMosflmScriptsOutput = property(getLabelitMosflmScriptsOutput, setLabelitMosflmScriptsOutput, delLabelitMosflmScriptsOutput, "Property for labelitMosflmScriptsOutput")
	def getLabelitScreenOutput(self): return self.__labelitScreenOutput
	def setLabelitScreenOutput(self, labelitScreenOutput):
		checkType("XSDataResultLabelit", "setLabelitScreenOutput", labelitScreenOutput, "XSDataLabelitScreenOutput")
		self.__labelitScreenOutput = labelitScreenOutput
	def delLabelitScreenOutput(self): self.__labelitScreenOutput = None
	# Properties
	labelitScreenOutput = property(getLabelitScreenOutput, setLabelitScreenOutput, delLabelitScreenOutput, "Property for labelitScreenOutput")
	def export(self, outfile, level, name_='XSDataResultLabelit'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultLabelit'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__labelitMosflmScriptsOutput is not None:
			self.labelitMosflmScriptsOutput.export(outfile, level, name_='labelitMosflmScriptsOutput')
		else:
			warnEmptyAttribute("labelitMosflmScriptsOutput", "XSDataLabelitMosflmScriptsOutput")
		if self.__labelitScreenOutput is not None:
			self.labelitScreenOutput.export(outfile, level, name_='labelitScreenOutput')
		else:
			warnEmptyAttribute("labelitScreenOutput", "XSDataLabelitScreenOutput")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'labelitMosflmScriptsOutput':
			obj_ = XSDataLabelitMosflmScriptsOutput()
			obj_.build(child_)
			self.setLabelitMosflmScriptsOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'labelitScreenOutput':
			obj_ = XSDataLabelitScreenOutput()
			obj_.build(child_)
			self.setLabelitScreenOutput(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultLabelit" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultLabelit' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultLabelit is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultLabelit.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultLabelit()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultLabelit" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultLabelit()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultLabelit



# End of data representation classes.



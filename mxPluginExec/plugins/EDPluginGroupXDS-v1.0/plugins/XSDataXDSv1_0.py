#!/usr/bin/env python

#
# Generated Mon Feb 20 06:38::46 2012 by EDGenerateDS.
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
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataAngle
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataVectorDouble
	from XSDataCommon import XSDataLength
	from XSDataCommon import XSDataWavelength
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
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength




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


class XSDataXDSBeam(XSData):
	def __init__(self, x_ray_wavelength=None, polarization_plane_normal=None, incident_beam_direction=None, fraction_of_polarization=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSBeam", "Constructor of XSDataXDSBeam", fraction_of_polarization, "XSDataDouble")
		self._fraction_of_polarization = fraction_of_polarization
		checkType("XSDataXDSBeam", "Constructor of XSDataXDSBeam", incident_beam_direction, "XSDataVectorDouble")
		self._incident_beam_direction = incident_beam_direction
		checkType("XSDataXDSBeam", "Constructor of XSDataXDSBeam", polarization_plane_normal, "XSDataVectorDouble")
		self._polarization_plane_normal = polarization_plane_normal
		checkType("XSDataXDSBeam", "Constructor of XSDataXDSBeam", x_ray_wavelength, "XSDataWavelength")
		self._x_ray_wavelength = x_ray_wavelength
	def getFraction_of_polarization(self): return self._fraction_of_polarization
	def setFraction_of_polarization(self, fraction_of_polarization):
		checkType("XSDataXDSBeam", "setFraction_of_polarization", fraction_of_polarization, "XSDataDouble")
		self._fraction_of_polarization = fraction_of_polarization
	def delFraction_of_polarization(self): self._fraction_of_polarization = None
	# Properties
	fraction_of_polarization = property(getFraction_of_polarization, setFraction_of_polarization, delFraction_of_polarization, "Property for fraction_of_polarization")
	def getIncident_beam_direction(self): return self._incident_beam_direction
	def setIncident_beam_direction(self, incident_beam_direction):
		checkType("XSDataXDSBeam", "setIncident_beam_direction", incident_beam_direction, "XSDataVectorDouble")
		self._incident_beam_direction = incident_beam_direction
	def delIncident_beam_direction(self): self._incident_beam_direction = None
	# Properties
	incident_beam_direction = property(getIncident_beam_direction, setIncident_beam_direction, delIncident_beam_direction, "Property for incident_beam_direction")
	def getPolarization_plane_normal(self): return self._polarization_plane_normal
	def setPolarization_plane_normal(self, polarization_plane_normal):
		checkType("XSDataXDSBeam", "setPolarization_plane_normal", polarization_plane_normal, "XSDataVectorDouble")
		self._polarization_plane_normal = polarization_plane_normal
	def delPolarization_plane_normal(self): self._polarization_plane_normal = None
	# Properties
	polarization_plane_normal = property(getPolarization_plane_normal, setPolarization_plane_normal, delPolarization_plane_normal, "Property for polarization_plane_normal")
	def getX_ray_wavelength(self): return self._x_ray_wavelength
	def setX_ray_wavelength(self, x_ray_wavelength):
		checkType("XSDataXDSBeam", "setX_ray_wavelength", x_ray_wavelength, "XSDataWavelength")
		self._x_ray_wavelength = x_ray_wavelength
	def delX_ray_wavelength(self): self._x_ray_wavelength = None
	# Properties
	x_ray_wavelength = property(getX_ray_wavelength, setX_ray_wavelength, delX_ray_wavelength, "Property for x_ray_wavelength")
	def export(self, outfile, level, name_='XSDataXDSBeam'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSBeam'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._fraction_of_polarization is not None:
			self.fraction_of_polarization.export(outfile, level, name_='fraction_of_polarization')
		if self._incident_beam_direction is not None:
			self.incident_beam_direction.export(outfile, level, name_='incident_beam_direction')
		else:
			warnEmptyAttribute("incident_beam_direction", "XSDataVectorDouble")
		if self._polarization_plane_normal is not None:
			self.polarization_plane_normal.export(outfile, level, name_='polarization_plane_normal')
		else:
			warnEmptyAttribute("polarization_plane_normal", "XSDataVectorDouble")
		if self._x_ray_wavelength is not None:
			self.x_ray_wavelength.export(outfile, level, name_='x_ray_wavelength')
		else:
			warnEmptyAttribute("x_ray_wavelength", "XSDataWavelength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fraction_of_polarization':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFraction_of_polarization(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'incident_beam_direction':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setIncident_beam_direction(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'polarization_plane_normal':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setPolarization_plane_normal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x_ray_wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setX_ray_wavelength(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSBeam" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSBeam' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSBeam is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSBeam.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSBeam()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSBeam" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSBeam()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSBeam

class XSDataXDSCell(XSData):
	def __init__(self, angle_gamma=None, length_c=None, length_b=None, length_a=None, angle_beta=None, angle_alpha=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", angle_alpha, "XSDataAngle")
		self._angle_alpha = angle_alpha
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", angle_beta, "XSDataAngle")
		self._angle_beta = angle_beta
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", length_a, "XSDataLength")
		self._length_a = length_a
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", length_b, "XSDataLength")
		self._length_b = length_b
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", length_c, "XSDataLength")
		self._length_c = length_c
		checkType("XSDataXDSCell", "Constructor of XSDataXDSCell", angle_gamma, "XSDataAngle")
		self._angle_gamma = angle_gamma
	def getAngle_alpha(self): return self._angle_alpha
	def setAngle_alpha(self, angle_alpha):
		checkType("XSDataXDSCell", "setAngle_alpha", angle_alpha, "XSDataAngle")
		self._angle_alpha = angle_alpha
	def delAngle_alpha(self): self._angle_alpha = None
	# Properties
	angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
	def getAngle_beta(self): return self._angle_beta
	def setAngle_beta(self, angle_beta):
		checkType("XSDataXDSCell", "setAngle_beta", angle_beta, "XSDataAngle")
		self._angle_beta = angle_beta
	def delAngle_beta(self): self._angle_beta = None
	# Properties
	angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
	def getLength_a(self): return self._length_a
	def setLength_a(self, length_a):
		checkType("XSDataXDSCell", "setLength_a", length_a, "XSDataLength")
		self._length_a = length_a
	def delLength_a(self): self._length_a = None
	# Properties
	length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
	def getLength_b(self): return self._length_b
	def setLength_b(self, length_b):
		checkType("XSDataXDSCell", "setLength_b", length_b, "XSDataLength")
		self._length_b = length_b
	def delLength_b(self): self._length_b = None
	# Properties
	length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
	def getLength_c(self): return self._length_c
	def setLength_c(self, length_c):
		checkType("XSDataXDSCell", "setLength_c", length_c, "XSDataLength")
		self._length_c = length_c
	def delLength_c(self): self._length_c = None
	# Properties
	length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
	def getAngle_gamma(self): return self._angle_gamma
	def setAngle_gamma(self, angle_gamma):
		checkType("XSDataXDSCell", "setAngle_gamma", angle_gamma, "XSDataAngle")
		self._angle_gamma = angle_gamma
	def delAngle_gamma(self): self._angle_gamma = None
	# Properties
	angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
	def export(self, outfile, level, name_='XSDataXDSCell'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSCell'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._angle_alpha is not None:
			self.angle_alpha.export(outfile, level, name_='angle_alpha')
		else:
			warnEmptyAttribute("angle_alpha", "XSDataAngle")
		if self._angle_beta is not None:
			self.angle_beta.export(outfile, level, name_='angle_beta')
		else:
			warnEmptyAttribute("angle_beta", "XSDataAngle")
		if self._length_a is not None:
			self.length_a.export(outfile, level, name_='length_a')
		else:
			warnEmptyAttribute("length_a", "XSDataLength")
		if self._length_b is not None:
			self.length_b.export(outfile, level, name_='length_b')
		else:
			warnEmptyAttribute("length_b", "XSDataLength")
		if self._length_c is not None:
			self.length_c.export(outfile, level, name_='length_c')
		else:
			warnEmptyAttribute("length_c", "XSDataLength")
		if self._angle_gamma is not None:
			self.angle_gamma.export(outfile, level, name_='angle_gamma')
		else:
			warnEmptyAttribute("angle_gamma", "XSDataAngle")
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angle_gamma':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setAngle_gamma(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSCell" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSCell' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSCell is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSCell.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSCell()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSCell" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSCell()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSCell

class XSDataXDSCrystal(XSData):
	def __init__(self, unit_cell_constants=None, strong_pixel=None, space_group_number=None, friedels_law=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSCrystal", "Constructor of XSDataXDSCrystal", friedels_law, "XSDataString")
		self._friedels_law = friedels_law
		checkType("XSDataXDSCrystal", "Constructor of XSDataXDSCrystal", space_group_number, "XSDataInteger")
		self._space_group_number = space_group_number
		checkType("XSDataXDSCrystal", "Constructor of XSDataXDSCrystal", strong_pixel, "XSDataInteger")
		self._strong_pixel = strong_pixel
		checkType("XSDataXDSCrystal", "Constructor of XSDataXDSCrystal", unit_cell_constants, "XSDataXDSCell")
		self._unit_cell_constants = unit_cell_constants
	def getFriedels_law(self): return self._friedels_law
	def setFriedels_law(self, friedels_law):
		checkType("XSDataXDSCrystal", "setFriedels_law", friedels_law, "XSDataString")
		self._friedels_law = friedels_law
	def delFriedels_law(self): self._friedels_law = None
	# Properties
	friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
	def getSpace_group_number(self): return self._space_group_number
	def setSpace_group_number(self, space_group_number):
		checkType("XSDataXDSCrystal", "setSpace_group_number", space_group_number, "XSDataInteger")
		self._space_group_number = space_group_number
	def delSpace_group_number(self): self._space_group_number = None
	# Properties
	space_group_number = property(getSpace_group_number, setSpace_group_number, delSpace_group_number, "Property for space_group_number")
	def getStrong_pixel(self): return self._strong_pixel
	def setStrong_pixel(self, strong_pixel):
		checkType("XSDataXDSCrystal", "setStrong_pixel", strong_pixel, "XSDataInteger")
		self._strong_pixel = strong_pixel
	def delStrong_pixel(self): self._strong_pixel = None
	# Properties
	strong_pixel = property(getStrong_pixel, setStrong_pixel, delStrong_pixel, "Property for strong_pixel")
	def getUnit_cell_constants(self): return self._unit_cell_constants
	def setUnit_cell_constants(self, unit_cell_constants):
		checkType("XSDataXDSCrystal", "setUnit_cell_constants", unit_cell_constants, "XSDataXDSCell")
		self._unit_cell_constants = unit_cell_constants
	def delUnit_cell_constants(self): self._unit_cell_constants = None
	# Properties
	unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
	def export(self, outfile, level, name_='XSDataXDSCrystal'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSCrystal'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._friedels_law is not None:
			self.friedels_law.export(outfile, level, name_='friedels_law')
		else:
			warnEmptyAttribute("friedels_law", "XSDataString")
		if self._space_group_number is not None:
			self.space_group_number.export(outfile, level, name_='space_group_number')
		else:
			warnEmptyAttribute("space_group_number", "XSDataInteger")
		if self._strong_pixel is not None:
			self.strong_pixel.export(outfile, level, name_='strong_pixel')
		else:
			warnEmptyAttribute("strong_pixel", "XSDataInteger")
		if self._unit_cell_constants is not None:
			self.unit_cell_constants.export(outfile, level, name_='unit_cell_constants')
		else:
			warnEmptyAttribute("unit_cell_constants", "XSDataXDSCell")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'friedels_law':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFriedels_law(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'space_group_number':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpace_group_number(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'strong_pixel':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setStrong_pixel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unit_cell_constants':
			obj_ = XSDataXDSCell()
			obj_.build(child_)
			self.setUnit_cell_constants(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSCrystal" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSCrystal' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSCrystal is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSCrystal.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSCrystal()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSCrystal" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSCrystal()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSCrystal

class XSDataXDSDoubleRange(XSData):
	def __init__(self, upper=None, lower=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSDoubleRange", "Constructor of XSDataXDSDoubleRange", lower, "XSDataDouble")
		self._lower = lower
		checkType("XSDataXDSDoubleRange", "Constructor of XSDataXDSDoubleRange", upper, "XSDataDouble")
		self._upper = upper
	def getLower(self): return self._lower
	def setLower(self, lower):
		checkType("XSDataXDSDoubleRange", "setLower", lower, "XSDataDouble")
		self._lower = lower
	def delLower(self): self._lower = None
	# Properties
	lower = property(getLower, setLower, delLower, "Property for lower")
	def getUpper(self): return self._upper
	def setUpper(self, upper):
		checkType("XSDataXDSDoubleRange", "setUpper", upper, "XSDataDouble")
		self._upper = upper
	def delUpper(self): self._upper = None
	# Properties
	upper = property(getUpper, setUpper, delUpper, "Property for upper")
	def export(self, outfile, level, name_='XSDataXDSDoubleRange'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSDoubleRange'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._lower is not None:
			self.lower.export(outfile, level, name_='lower')
		else:
			warnEmptyAttribute("lower", "XSDataDouble")
		if self._upper is not None:
			self.upper.export(outfile, level, name_='upper')
		else:
			warnEmptyAttribute("upper", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lower':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLower(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'upper':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setUpper(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSDoubleRange" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSDoubleRange' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSDoubleRange is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSDoubleRange.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDoubleRange()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSDoubleRange" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDoubleRange()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSDoubleRange

class XSDataXDSGoniostat(XSData):
	def __init__(self, starting_angle=None, rotation_axis=None, oscillation_range=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSGoniostat", "Constructor of XSDataXDSGoniostat", oscillation_range, "XSDataAngle")
		self._oscillation_range = oscillation_range
		checkType("XSDataXDSGoniostat", "Constructor of XSDataXDSGoniostat", rotation_axis, "XSDataVectorDouble")
		self._rotation_axis = rotation_axis
		checkType("XSDataXDSGoniostat", "Constructor of XSDataXDSGoniostat", starting_angle, "XSDataAngle")
		self._starting_angle = starting_angle
	def getOscillation_range(self): return self._oscillation_range
	def setOscillation_range(self, oscillation_range):
		checkType("XSDataXDSGoniostat", "setOscillation_range", oscillation_range, "XSDataAngle")
		self._oscillation_range = oscillation_range
	def delOscillation_range(self): self._oscillation_range = None
	# Properties
	oscillation_range = property(getOscillation_range, setOscillation_range, delOscillation_range, "Property for oscillation_range")
	def getRotation_axis(self): return self._rotation_axis
	def setRotation_axis(self, rotation_axis):
		checkType("XSDataXDSGoniostat", "setRotation_axis", rotation_axis, "XSDataVectorDouble")
		self._rotation_axis = rotation_axis
	def delRotation_axis(self): self._rotation_axis = None
	# Properties
	rotation_axis = property(getRotation_axis, setRotation_axis, delRotation_axis, "Property for rotation_axis")
	def getStarting_angle(self): return self._starting_angle
	def setStarting_angle(self, starting_angle):
		checkType("XSDataXDSGoniostat", "setStarting_angle", starting_angle, "XSDataAngle")
		self._starting_angle = starting_angle
	def delStarting_angle(self): self._starting_angle = None
	# Properties
	starting_angle = property(getStarting_angle, setStarting_angle, delStarting_angle, "Property for starting_angle")
	def export(self, outfile, level, name_='XSDataXDSGoniostat'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSGoniostat'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._oscillation_range is not None:
			self.oscillation_range.export(outfile, level, name_='oscillation_range')
		else:
			warnEmptyAttribute("oscillation_range", "XSDataAngle")
		if self._rotation_axis is not None:
			self.rotation_axis.export(outfile, level, name_='rotation_axis')
		else:
			warnEmptyAttribute("rotation_axis", "XSDataVectorDouble")
		if self._starting_angle is not None:
			self.starting_angle.export(outfile, level, name_='starting_angle')
		else:
			warnEmptyAttribute("starting_angle", "XSDataAngle")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'oscillation_range':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOscillation_range(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rotation_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setRotation_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'starting_angle':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setStarting_angle(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSGoniostat" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSGoniostat' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSGoniostat is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSGoniostat.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSGoniostat()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSGoniostat" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSGoniostat()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSGoniostat

class XSDataXDSImageLink(XSData):
	def __init__(self, target=None, source=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSImageLink", "Constructor of XSDataXDSImageLink", source, "XSDataFile")
		self._source = source
		checkType("XSDataXDSImageLink", "Constructor of XSDataXDSImageLink", target, "XSDataString")
		self._target = target
	def getSource(self): return self._source
	def setSource(self, source):
		checkType("XSDataXDSImageLink", "setSource", source, "XSDataFile")
		self._source = source
	def delSource(self): self._source = None
	# Properties
	source = property(getSource, setSource, delSource, "Property for source")
	def getTarget(self): return self._target
	def setTarget(self, target):
		checkType("XSDataXDSImageLink", "setTarget", target, "XSDataString")
		self._target = target
	def delTarget(self): self._target = None
	# Properties
	target = property(getTarget, setTarget, delTarget, "Property for target")
	def export(self, outfile, level, name_='XSDataXDSImageLink'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSImageLink'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._source is not None:
			self.source.export(outfile, level, name_='source')
		else:
			warnEmptyAttribute("source", "XSDataFile")
		if self._target is not None:
			self.target.export(outfile, level, name_='target')
		else:
			warnEmptyAttribute("target", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'source':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSource(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'target':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTarget(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSImageLink" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSImageLink' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSImageLink is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSImageLink.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSImageLink()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSImageLink" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSImageLink()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSImageLink

class XSDataXDSIntegerRange(XSData):
	def __init__(self, upper=None, lower=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSIntegerRange", "Constructor of XSDataXDSIntegerRange", lower, "XSDataInteger")
		self._lower = lower
		checkType("XSDataXDSIntegerRange", "Constructor of XSDataXDSIntegerRange", upper, "XSDataInteger")
		self._upper = upper
	def getLower(self): return self._lower
	def setLower(self, lower):
		checkType("XSDataXDSIntegerRange", "setLower", lower, "XSDataInteger")
		self._lower = lower
	def delLower(self): self._lower = None
	# Properties
	lower = property(getLower, setLower, delLower, "Property for lower")
	def getUpper(self): return self._upper
	def setUpper(self, upper):
		checkType("XSDataXDSIntegerRange", "setUpper", upper, "XSDataInteger")
		self._upper = upper
	def delUpper(self): self._upper = None
	# Properties
	upper = property(getUpper, setUpper, delUpper, "Property for upper")
	def export(self, outfile, level, name_='XSDataXDSIntegerRange'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSIntegerRange'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._lower is not None:
			self.lower.export(outfile, level, name_='lower')
		else:
			warnEmptyAttribute("lower", "XSDataInteger")
		if self._upper is not None:
			self.upper.export(outfile, level, name_='upper')
		else:
			warnEmptyAttribute("upper", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lower':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setLower(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'upper':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setUpper(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSIntegerRange" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSIntegerRange' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSIntegerRange is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSIntegerRange.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSIntegerRange()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSIntegerRange" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSIntegerRange()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSIntegerRange

class XSDataXDSRectangle(XSData):
	def __init__(self, y2=None, y1=None, x2=None, x1=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSRectangle", "Constructor of XSDataXDSRectangle", x1, "XSDataInteger")
		self._x1 = x1
		checkType("XSDataXDSRectangle", "Constructor of XSDataXDSRectangle", x2, "XSDataInteger")
		self._x2 = x2
		checkType("XSDataXDSRectangle", "Constructor of XSDataXDSRectangle", y1, "XSDataInteger")
		self._y1 = y1
		checkType("XSDataXDSRectangle", "Constructor of XSDataXDSRectangle", y2, "XSDataInteger")
		self._y2 = y2
	def getX1(self): return self._x1
	def setX1(self, x1):
		checkType("XSDataXDSRectangle", "setX1", x1, "XSDataInteger")
		self._x1 = x1
	def delX1(self): self._x1 = None
	# Properties
	x1 = property(getX1, setX1, delX1, "Property for x1")
	def getX2(self): return self._x2
	def setX2(self, x2):
		checkType("XSDataXDSRectangle", "setX2", x2, "XSDataInteger")
		self._x2 = x2
	def delX2(self): self._x2 = None
	# Properties
	x2 = property(getX2, setX2, delX2, "Property for x2")
	def getY1(self): return self._y1
	def setY1(self, y1):
		checkType("XSDataXDSRectangle", "setY1", y1, "XSDataInteger")
		self._y1 = y1
	def delY1(self): self._y1 = None
	# Properties
	y1 = property(getY1, setY1, delY1, "Property for y1")
	def getY2(self): return self._y2
	def setY2(self, y2):
		checkType("XSDataXDSRectangle", "setY2", y2, "XSDataInteger")
		self._y2 = y2
	def delY2(self): self._y2 = None
	# Properties
	y2 = property(getY2, setY2, delY2, "Property for y2")
	def export(self, outfile, level, name_='XSDataXDSRectangle'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSRectangle'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._x1 is not None:
			self.x1.export(outfile, level, name_='x1')
		else:
			warnEmptyAttribute("x1", "XSDataInteger")
		if self._x2 is not None:
			self.x2.export(outfile, level, name_='x2')
		else:
			warnEmptyAttribute("x2", "XSDataInteger")
		if self._y1 is not None:
			self.y1.export(outfile, level, name_='y1')
		else:
			warnEmptyAttribute("y1", "XSDataInteger")
		if self._y2 is not None:
			self.y2.export(outfile, level, name_='y2')
		else:
			warnEmptyAttribute("y2", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x1':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setX1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x2':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setX2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'y1':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setY1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'y2':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setY2(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSRectangle" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSRectangle' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSRectangle is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSRectangle.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSRectangle()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSRectangle" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSRectangle()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSRectangle

class XSDataXDSDetector(XSData):
	def __init__(self, trusted_region=None, sensor_thickness=None, untrusted_rectangle=None, value_range_for_trusted_detector_pixels=None, qy=None, qx=None, overload=None, orgy=None, orgx=None, ny=None, nx=None, minimum_valid_pixel_value=None, direction_of_detector_y_axis=None, direction_of_detector_x_axis=None, detector_name=None, detector_distance=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", detector_distance, "XSDataLength")
		self._detector_distance = detector_distance
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", detector_name, "XSDataString")
		self._detector_name = detector_name
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", direction_of_detector_x_axis, "XSDataVectorDouble")
		self._direction_of_detector_x_axis = direction_of_detector_x_axis
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", direction_of_detector_y_axis, "XSDataVectorDouble")
		self._direction_of_detector_y_axis = direction_of_detector_y_axis
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", minimum_valid_pixel_value, "XSDataInteger")
		self._minimum_valid_pixel_value = minimum_valid_pixel_value
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", nx, "XSDataInteger")
		self._nx = nx
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", ny, "XSDataInteger")
		self._ny = ny
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", orgx, "XSDataDouble")
		self._orgx = orgx
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", orgy, "XSDataDouble")
		self._orgy = orgy
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", overload, "XSDataInteger")
		self._overload = overload
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", qx, "XSDataLength")
		self._qx = qx
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", qy, "XSDataLength")
		self._qy = qy
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", value_range_for_trusted_detector_pixels, "XSDataXDSIntegerRange")
		self._value_range_for_trusted_detector_pixels = value_range_for_trusted_detector_pixels
		if untrusted_rectangle is None:
			self._untrusted_rectangle = []
		else:
			checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", untrusted_rectangle, "list")
			self._untrusted_rectangle = untrusted_rectangle
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", sensor_thickness, "XSDataDouble")
		self._sensor_thickness = sensor_thickness
		checkType("XSDataXDSDetector", "Constructor of XSDataXDSDetector", trusted_region, "XSDataXDSDoubleRange")
		self._trusted_region = trusted_region
	def getDetector_distance(self): return self._detector_distance
	def setDetector_distance(self, detector_distance):
		checkType("XSDataXDSDetector", "setDetector_distance", detector_distance, "XSDataLength")
		self._detector_distance = detector_distance
	def delDetector_distance(self): self._detector_distance = None
	# Properties
	detector_distance = property(getDetector_distance, setDetector_distance, delDetector_distance, "Property for detector_distance")
	def getDetector_name(self): return self._detector_name
	def setDetector_name(self, detector_name):
		checkType("XSDataXDSDetector", "setDetector_name", detector_name, "XSDataString")
		self._detector_name = detector_name
	def delDetector_name(self): self._detector_name = None
	# Properties
	detector_name = property(getDetector_name, setDetector_name, delDetector_name, "Property for detector_name")
	def getDirection_of_detector_x_axis(self): return self._direction_of_detector_x_axis
	def setDirection_of_detector_x_axis(self, direction_of_detector_x_axis):
		checkType("XSDataXDSDetector", "setDirection_of_detector_x_axis", direction_of_detector_x_axis, "XSDataVectorDouble")
		self._direction_of_detector_x_axis = direction_of_detector_x_axis
	def delDirection_of_detector_x_axis(self): self._direction_of_detector_x_axis = None
	# Properties
	direction_of_detector_x_axis = property(getDirection_of_detector_x_axis, setDirection_of_detector_x_axis, delDirection_of_detector_x_axis, "Property for direction_of_detector_x_axis")
	def getDirection_of_detector_y_axis(self): return self._direction_of_detector_y_axis
	def setDirection_of_detector_y_axis(self, direction_of_detector_y_axis):
		checkType("XSDataXDSDetector", "setDirection_of_detector_y_axis", direction_of_detector_y_axis, "XSDataVectorDouble")
		self._direction_of_detector_y_axis = direction_of_detector_y_axis
	def delDirection_of_detector_y_axis(self): self._direction_of_detector_y_axis = None
	# Properties
	direction_of_detector_y_axis = property(getDirection_of_detector_y_axis, setDirection_of_detector_y_axis, delDirection_of_detector_y_axis, "Property for direction_of_detector_y_axis")
	def getMinimum_valid_pixel_value(self): return self._minimum_valid_pixel_value
	def setMinimum_valid_pixel_value(self, minimum_valid_pixel_value):
		checkType("XSDataXDSDetector", "setMinimum_valid_pixel_value", minimum_valid_pixel_value, "XSDataInteger")
		self._minimum_valid_pixel_value = minimum_valid_pixel_value
	def delMinimum_valid_pixel_value(self): self._minimum_valid_pixel_value = None
	# Properties
	minimum_valid_pixel_value = property(getMinimum_valid_pixel_value, setMinimum_valid_pixel_value, delMinimum_valid_pixel_value, "Property for minimum_valid_pixel_value")
	def getNx(self): return self._nx
	def setNx(self, nx):
		checkType("XSDataXDSDetector", "setNx", nx, "XSDataInteger")
		self._nx = nx
	def delNx(self): self._nx = None
	# Properties
	nx = property(getNx, setNx, delNx, "Property for nx")
	def getNy(self): return self._ny
	def setNy(self, ny):
		checkType("XSDataXDSDetector", "setNy", ny, "XSDataInteger")
		self._ny = ny
	def delNy(self): self._ny = None
	# Properties
	ny = property(getNy, setNy, delNy, "Property for ny")
	def getOrgx(self): return self._orgx
	def setOrgx(self, orgx):
		checkType("XSDataXDSDetector", "setOrgx", orgx, "XSDataDouble")
		self._orgx = orgx
	def delOrgx(self): self._orgx = None
	# Properties
	orgx = property(getOrgx, setOrgx, delOrgx, "Property for orgx")
	def getOrgy(self): return self._orgy
	def setOrgy(self, orgy):
		checkType("XSDataXDSDetector", "setOrgy", orgy, "XSDataDouble")
		self._orgy = orgy
	def delOrgy(self): self._orgy = None
	# Properties
	orgy = property(getOrgy, setOrgy, delOrgy, "Property for orgy")
	def getOverload(self): return self._overload
	def setOverload(self, overload):
		checkType("XSDataXDSDetector", "setOverload", overload, "XSDataInteger")
		self._overload = overload
	def delOverload(self): self._overload = None
	# Properties
	overload = property(getOverload, setOverload, delOverload, "Property for overload")
	def getQx(self): return self._qx
	def setQx(self, qx):
		checkType("XSDataXDSDetector", "setQx", qx, "XSDataLength")
		self._qx = qx
	def delQx(self): self._qx = None
	# Properties
	qx = property(getQx, setQx, delQx, "Property for qx")
	def getQy(self): return self._qy
	def setQy(self, qy):
		checkType("XSDataXDSDetector", "setQy", qy, "XSDataLength")
		self._qy = qy
	def delQy(self): self._qy = None
	# Properties
	qy = property(getQy, setQy, delQy, "Property for qy")
	def getValue_range_for_trusted_detector_pixels(self): return self._value_range_for_trusted_detector_pixels
	def setValue_range_for_trusted_detector_pixels(self, value_range_for_trusted_detector_pixels):
		checkType("XSDataXDSDetector", "setValue_range_for_trusted_detector_pixels", value_range_for_trusted_detector_pixels, "XSDataXDSIntegerRange")
		self._value_range_for_trusted_detector_pixels = value_range_for_trusted_detector_pixels
	def delValue_range_for_trusted_detector_pixels(self): self._value_range_for_trusted_detector_pixels = None
	# Properties
	value_range_for_trusted_detector_pixels = property(getValue_range_for_trusted_detector_pixels, setValue_range_for_trusted_detector_pixels, delValue_range_for_trusted_detector_pixels, "Property for value_range_for_trusted_detector_pixels")
	def getUntrusted_rectangle(self): return self._untrusted_rectangle
	def setUntrusted_rectangle(self, untrusted_rectangle):
		checkType("XSDataXDSDetector", "setUntrusted_rectangle", untrusted_rectangle, "list")
		self._untrusted_rectangle = untrusted_rectangle
	def delUntrusted_rectangle(self): self._untrusted_rectangle = None
	# Properties
	untrusted_rectangle = property(getUntrusted_rectangle, setUntrusted_rectangle, delUntrusted_rectangle, "Property for untrusted_rectangle")
	def addUntrusted_rectangle(self, value):
		checkType("XSDataXDSDetector", "setUntrusted_rectangle", value, "XSDataXDSRectangle")
		self._untrusted_rectangle.append(value)
	def insertUntrusted_rectangle(self, index, value):
		checkType("XSDataXDSDetector", "setUntrusted_rectangle", value, "XSDataXDSRectangle")
		self._untrusted_rectangle[index] = value
	def getSensor_thickness(self): return self._sensor_thickness
	def setSensor_thickness(self, sensor_thickness):
		checkType("XSDataXDSDetector", "setSensor_thickness", sensor_thickness, "XSDataDouble")
		self._sensor_thickness = sensor_thickness
	def delSensor_thickness(self): self._sensor_thickness = None
	# Properties
	sensor_thickness = property(getSensor_thickness, setSensor_thickness, delSensor_thickness, "Property for sensor_thickness")
	def getTrusted_region(self): return self._trusted_region
	def setTrusted_region(self, trusted_region):
		checkType("XSDataXDSDetector", "setTrusted_region", trusted_region, "XSDataXDSDoubleRange")
		self._trusted_region = trusted_region
	def delTrusted_region(self): self._trusted_region = None
	# Properties
	trusted_region = property(getTrusted_region, setTrusted_region, delTrusted_region, "Property for trusted_region")
	def export(self, outfile, level, name_='XSDataXDSDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSDetector'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._detector_distance is not None:
			self.detector_distance.export(outfile, level, name_='detector_distance')
		else:
			warnEmptyAttribute("detector_distance", "XSDataLength")
		if self._detector_name is not None:
			self.detector_name.export(outfile, level, name_='detector_name')
		else:
			warnEmptyAttribute("detector_name", "XSDataString")
		if self._direction_of_detector_x_axis is not None:
			self.direction_of_detector_x_axis.export(outfile, level, name_='direction_of_detector_x_axis')
		else:
			warnEmptyAttribute("direction_of_detector_x_axis", "XSDataVectorDouble")
		if self._direction_of_detector_y_axis is not None:
			self.direction_of_detector_y_axis.export(outfile, level, name_='direction_of_detector_y_axis')
		else:
			warnEmptyAttribute("direction_of_detector_y_axis", "XSDataVectorDouble")
		if self._minimum_valid_pixel_value is not None:
			self.minimum_valid_pixel_value.export(outfile, level, name_='minimum_valid_pixel_value')
		else:
			warnEmptyAttribute("minimum_valid_pixel_value", "XSDataInteger")
		if self._nx is not None:
			self.nx.export(outfile, level, name_='nx')
		else:
			warnEmptyAttribute("nx", "XSDataInteger")
		if self._ny is not None:
			self.ny.export(outfile, level, name_='ny')
		else:
			warnEmptyAttribute("ny", "XSDataInteger")
		if self._orgx is not None:
			self.orgx.export(outfile, level, name_='orgx')
		else:
			warnEmptyAttribute("orgx", "XSDataDouble")
		if self._orgy is not None:
			self.orgy.export(outfile, level, name_='orgy')
		else:
			warnEmptyAttribute("orgy", "XSDataDouble")
		if self._overload is not None:
			self.overload.export(outfile, level, name_='overload')
		else:
			warnEmptyAttribute("overload", "XSDataInteger")
		if self._qx is not None:
			self.qx.export(outfile, level, name_='qx')
		else:
			warnEmptyAttribute("qx", "XSDataLength")
		if self._qy is not None:
			self.qy.export(outfile, level, name_='qy')
		else:
			warnEmptyAttribute("qy", "XSDataLength")
		if self._value_range_for_trusted_detector_pixels is not None:
			self.value_range_for_trusted_detector_pixels.export(outfile, level, name_='value_range_for_trusted_detector_pixels')
		for untrusted_rectangle_ in self.getUntrusted_rectangle():
			untrusted_rectangle_.export(outfile, level, name_='untrusted_rectangle')
		if self._sensor_thickness is not None:
			self.sensor_thickness.export(outfile, level, name_='sensor_thickness')
		if self._trusted_region is not None:
			self.trusted_region.export(outfile, level, name_='trusted_region')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector_distance':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setDetector_distance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector_name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setDetector_name(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direction_of_detector_x_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setDirection_of_detector_x_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direction_of_detector_y_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setDirection_of_detector_y_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'minimum_valid_pixel_value':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setMinimum_valid_pixel_value(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nx':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNx(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ny':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'orgx':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setOrgx(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'orgy':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setOrgy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overload':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setOverload(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qx':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setQx(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qy':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setQy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'value_range_for_trusted_detector_pixels':
			obj_ = XSDataXDSIntegerRange()
			obj_.build(child_)
			self.setValue_range_for_trusted_detector_pixels(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'untrusted_rectangle':
			obj_ = XSDataXDSRectangle()
			obj_.build(child_)
			self.untrusted_rectangle.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sensor_thickness':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSensor_thickness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'trusted_region':
			obj_ = XSDataXDSDoubleRange()
			obj_.build(child_)
			self.setTrusted_region(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSDetector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSDetector' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSDetector is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSDetector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDetector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSDetector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSDetector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSDetector

class XSDataXDSImage(XSData):
	def __init__(self, name_template_of_data_frames=None, starting_frame=None, spot_range=None, data_range=None, background_range=None):
		XSData.__init__(self, )
	
	
		if background_range is None:
			self._background_range = []
		else:
			checkType("XSDataXDSImage", "Constructor of XSDataXDSImage", background_range, "list")
			self._background_range = background_range
		if data_range is None:
			self._data_range = []
		else:
			checkType("XSDataXDSImage", "Constructor of XSDataXDSImage", data_range, "list")
			self._data_range = data_range
		if spot_range is None:
			self._spot_range = []
		else:
			checkType("XSDataXDSImage", "Constructor of XSDataXDSImage", spot_range, "list")
			self._spot_range = spot_range
		checkType("XSDataXDSImage", "Constructor of XSDataXDSImage", starting_frame, "XSDataInteger")
		self._starting_frame = starting_frame
		checkType("XSDataXDSImage", "Constructor of XSDataXDSImage", name_template_of_data_frames, "XSDataString")
		self._name_template_of_data_frames = name_template_of_data_frames
	def getBackground_range(self): return self._background_range
	def setBackground_range(self, background_range):
		checkType("XSDataXDSImage", "setBackground_range", background_range, "list")
		self._background_range = background_range
	def delBackground_range(self): self._background_range = None
	# Properties
	background_range = property(getBackground_range, setBackground_range, delBackground_range, "Property for background_range")
	def addBackground_range(self, value):
		checkType("XSDataXDSImage", "setBackground_range", value, "XSDataXDSIntegerRange")
		self._background_range.append(value)
	def insertBackground_range(self, index, value):
		checkType("XSDataXDSImage", "setBackground_range", value, "XSDataXDSIntegerRange")
		self._background_range[index] = value
	def getData_range(self): return self._data_range
	def setData_range(self, data_range):
		checkType("XSDataXDSImage", "setData_range", data_range, "list")
		self._data_range = data_range
	def delData_range(self): self._data_range = None
	# Properties
	data_range = property(getData_range, setData_range, delData_range, "Property for data_range")
	def addData_range(self, value):
		checkType("XSDataXDSImage", "setData_range", value, "XSDataXDSIntegerRange")
		self._data_range.append(value)
	def insertData_range(self, index, value):
		checkType("XSDataXDSImage", "setData_range", value, "XSDataXDSIntegerRange")
		self._data_range[index] = value
	def getSpot_range(self): return self._spot_range
	def setSpot_range(self, spot_range):
		checkType("XSDataXDSImage", "setSpot_range", spot_range, "list")
		self._spot_range = spot_range
	def delSpot_range(self): self._spot_range = None
	# Properties
	spot_range = property(getSpot_range, setSpot_range, delSpot_range, "Property for spot_range")
	def addSpot_range(self, value):
		checkType("XSDataXDSImage", "setSpot_range", value, "XSDataXDSIntegerRange")
		self._spot_range.append(value)
	def insertSpot_range(self, index, value):
		checkType("XSDataXDSImage", "setSpot_range", value, "XSDataXDSIntegerRange")
		self._spot_range[index] = value
	def getStarting_frame(self): return self._starting_frame
	def setStarting_frame(self, starting_frame):
		checkType("XSDataXDSImage", "setStarting_frame", starting_frame, "XSDataInteger")
		self._starting_frame = starting_frame
	def delStarting_frame(self): self._starting_frame = None
	# Properties
	starting_frame = property(getStarting_frame, setStarting_frame, delStarting_frame, "Property for starting_frame")
	def getName_template_of_data_frames(self): return self._name_template_of_data_frames
	def setName_template_of_data_frames(self, name_template_of_data_frames):
		checkType("XSDataXDSImage", "setName_template_of_data_frames", name_template_of_data_frames, "XSDataString")
		self._name_template_of_data_frames = name_template_of_data_frames
	def delName_template_of_data_frames(self): self._name_template_of_data_frames = None
	# Properties
	name_template_of_data_frames = property(getName_template_of_data_frames, setName_template_of_data_frames, delName_template_of_data_frames, "Property for name_template_of_data_frames")
	def export(self, outfile, level, name_='XSDataXDSImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSImage'):
		XSData.exportChildren(self, outfile, level, name_)
		for background_range_ in self.getBackground_range():
			background_range_.export(outfile, level, name_='background_range')
		if self.getBackground_range() == []:
			warnEmptyAttribute("background_range", "XSDataXDSIntegerRange")
		for data_range_ in self.getData_range():
			data_range_.export(outfile, level, name_='data_range')
		if self.getData_range() == []:
			warnEmptyAttribute("data_range", "XSDataXDSIntegerRange")
		for spot_range_ in self.getSpot_range():
			spot_range_.export(outfile, level, name_='spot_range')
		if self.getSpot_range() == []:
			warnEmptyAttribute("spot_range", "XSDataXDSIntegerRange")
		if self._starting_frame is not None:
			self.starting_frame.export(outfile, level, name_='starting_frame')
		else:
			warnEmptyAttribute("starting_frame", "XSDataInteger")
		if self._name_template_of_data_frames is not None:
			self.name_template_of_data_frames.export(outfile, level, name_='name_template_of_data_frames')
		else:
			warnEmptyAttribute("name_template_of_data_frames", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'background_range':
			obj_ = XSDataXDSIntegerRange()
			obj_.build(child_)
			self.background_range.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'data_range':
			obj_ = XSDataXDSIntegerRange()
			obj_.build(child_)
			self.data_range.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spot_range':
			obj_ = XSDataXDSIntegerRange()
			obj_.build(child_)
			self.spot_range.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'starting_frame':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setStarting_frame(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name_template_of_data_frames':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName_template_of_data_frames(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSImage

class XSDataXDSVector(XSData):
	def __init__(self, v3=None, v2=None, v1=None):
		XSData.__init__(self, )
	
	
		checkType("XSDataXDSVector", "Constructor of XSDataXDSVector", v1, "XSDataFloat")
		self._v1 = v1
		checkType("XSDataXDSVector", "Constructor of XSDataXDSVector", v2, "XSDataFloat")
		self._v2 = v2
		checkType("XSDataXDSVector", "Constructor of XSDataXDSVector", v3, "XSDataFloat")
		self._v3 = v3
	def getV1(self): return self._v1
	def setV1(self, v1):
		checkType("XSDataXDSVector", "setV1", v1, "XSDataFloat")
		self._v1 = v1
	def delV1(self): self._v1 = None
	# Properties
	v1 = property(getV1, setV1, delV1, "Property for v1")
	def getV2(self): return self._v2
	def setV2(self, v2):
		checkType("XSDataXDSVector", "setV2", v2, "XSDataFloat")
		self._v2 = v2
	def delV2(self): self._v2 = None
	# Properties
	v2 = property(getV2, setV2, delV2, "Property for v2")
	def getV3(self): return self._v3
	def setV3(self, v3):
		checkType("XSDataXDSVector", "setV3", v3, "XSDataFloat")
		self._v3 = v3
	def delV3(self): self._v3 = None
	# Properties
	v3 = property(getV3, setV3, delV3, "Property for v3")
	def export(self, outfile, level, name_='XSDataXDSVector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXDSVector'):
		XSData.exportChildren(self, outfile, level, name_)
		if self._v1 is not None:
			self.v1.export(outfile, level, name_='v1')
		else:
			warnEmptyAttribute("v1", "XSDataFloat")
		if self._v2 is not None:
			self.v2.export(outfile, level, name_='v2')
		else:
			warnEmptyAttribute("v2", "XSDataFloat")
		if self._v3 is not None:
			self.v3.export(outfile, level, name_='v3')
		else:
			warnEmptyAttribute("v3", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'v1':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setV1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'v2':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setV2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'v3':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setV3(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXDSVector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXDSVector' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXDSVector is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXDSVector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXDSVector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXDSVector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXDSVector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXDSVector

class XSDataInputXDS(XSDataInput):
	def __init__(self, configuration=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
		XSDataInput.__init__(self, configuration)
	
	
		checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", beam, "XSDataXDSBeam")
		self._beam = beam
		checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", crystal, "XSDataXDSCrystal")
		self._crystal = crystal
		checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", detector, "XSDataXDSDetector")
		self._detector = detector
		checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", goniostat, "XSDataXDSGoniostat")
		self._goniostat = goniostat
		checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", image, "XSDataXDSImage")
		self._image = image
		if image_link is None:
			self._image_link = []
		else:
			checkType("XSDataInputXDS", "Constructor of XSDataInputXDS", image_link, "list")
			self._image_link = image_link
	def getBeam(self): return self._beam
	def setBeam(self, beam):
		checkType("XSDataInputXDS", "setBeam", beam, "XSDataXDSBeam")
		self._beam = beam
	def delBeam(self): self._beam = None
	# Properties
	beam = property(getBeam, setBeam, delBeam, "Property for beam")
	def getCrystal(self): return self._crystal
	def setCrystal(self, crystal):
		checkType("XSDataInputXDS", "setCrystal", crystal, "XSDataXDSCrystal")
		self._crystal = crystal
	def delCrystal(self): self._crystal = None
	# Properties
	crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
	def getDetector(self): return self._detector
	def setDetector(self, detector):
		checkType("XSDataInputXDS", "setDetector", detector, "XSDataXDSDetector")
		self._detector = detector
	def delDetector(self): self._detector = None
	# Properties
	detector = property(getDetector, setDetector, delDetector, "Property for detector")
	def getGoniostat(self): return self._goniostat
	def setGoniostat(self, goniostat):
		checkType("XSDataInputXDS", "setGoniostat", goniostat, "XSDataXDSGoniostat")
		self._goniostat = goniostat
	def delGoniostat(self): self._goniostat = None
	# Properties
	goniostat = property(getGoniostat, setGoniostat, delGoniostat, "Property for goniostat")
	def getImage(self): return self._image
	def setImage(self, image):
		checkType("XSDataInputXDS", "setImage", image, "XSDataXDSImage")
		self._image = image
	def delImage(self): self._image = None
	# Properties
	image = property(getImage, setImage, delImage, "Property for image")
	def getImage_link(self): return self._image_link
	def setImage_link(self, image_link):
		checkType("XSDataInputXDS", "setImage_link", image_link, "list")
		self._image_link = image_link
	def delImage_link(self): self._image_link = None
	# Properties
	image_link = property(getImage_link, setImage_link, delImage_link, "Property for image_link")
	def addImage_link(self, value):
		checkType("XSDataInputXDS", "setImage_link", value, "XSDataXDSImageLink")
		self._image_link.append(value)
	def insertImage_link(self, index, value):
		checkType("XSDataInputXDS", "setImage_link", value, "XSDataXDSImageLink")
		self._image_link[index] = value
	def export(self, outfile, level, name_='XSDataInputXDS'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputXDS'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self._beam is not None:
			self.beam.export(outfile, level, name_='beam')
		else:
			warnEmptyAttribute("beam", "XSDataXDSBeam")
		if self._crystal is not None:
			self.crystal.export(outfile, level, name_='crystal')
		if self._detector is not None:
			self.detector.export(outfile, level, name_='detector')
		else:
			warnEmptyAttribute("detector", "XSDataXDSDetector")
		if self._goniostat is not None:
			self.goniostat.export(outfile, level, name_='goniostat')
		else:
			warnEmptyAttribute("goniostat", "XSDataXDSGoniostat")
		if self._image is not None:
			self.image.export(outfile, level, name_='image')
		else:
			warnEmptyAttribute("image", "XSDataXDSImage")
		for image_link_ in self.getImage_link():
			image_link_.export(outfile, level, name_='image_link')
		if self.getImage_link() == []:
			warnEmptyAttribute("image_link", "XSDataXDSImageLink")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beam':
			obj_ = XSDataXDSBeam()
			obj_.build(child_)
			self.setBeam(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal':
			obj_ = XSDataXDSCrystal()
			obj_.build(child_)
			self.setCrystal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector':
			obj_ = XSDataXDSDetector()
			obj_.build(child_)
			self.setDetector(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'goniostat':
			obj_ = XSDataXDSGoniostat()
			obj_.build(child_)
			self.setGoniostat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image':
			obj_ = XSDataXDSImage()
			obj_.build(child_)
			self.setImage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'image_link':
			obj_ = XSDataXDSImageLink()
			obj_.build(child_)
			self.image_link.append(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputXDS" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputXDS' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputXDS is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputXDS.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDS()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputXDS" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDS()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputXDS

class XSDataResultXDS(XSDataResult):
	def __init__(self, status=None):
		XSDataResult.__init__(self, status)
	
	
	def export(self, outfile, level, name_='XSDataResultXDS'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultXDS'):
		XSDataResult.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultXDS" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultXDS' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultXDS is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultXDS.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDS()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultXDS" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDS()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultXDS

class XSDataInputXDSGenerateBackgroundImage(XSDataInputXDS):
	def __init__(self, configuration=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
		XSDataInputXDS.__init__(self, configuration, image_link, image, goniostat, detector, crystal, beam)
	
	
	def export(self, outfile, level, name_='XSDataInputXDSGenerateBackgroundImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputXDSGenerateBackgroundImage'):
		XSDataInputXDS.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataInputXDS.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputXDSGenerateBackgroundImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputXDSGenerateBackgroundImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputXDSGenerateBackgroundImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputXDSGenerateBackgroundImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputXDSGenerateBackgroundImage

class XSDataInputXDSIndexing(XSDataInputXDS):
	def __init__(self, configuration=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
		XSDataInputXDS.__init__(self, configuration, image_link, image, goniostat, detector, crystal, beam)
	
	
	def export(self, outfile, level, name_='XSDataInputXDSIndexing'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputXDSIndexing'):
		XSDataInputXDS.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDataInputXDS.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputXDSIndexing" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputXDSIndexing' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputXDSIndexing is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputXDSIndexing.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSIndexing()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputXDSIndexing" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputXDSIndexing()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputXDSIndexing

class XSDataResultXDSGenerateBackgroundImage(XSDataResultXDS):
	def __init__(self, status=None, xdsBackgroundImage=None):
		XSDataResultXDS.__init__(self, status)
	
	
		checkType("XSDataResultXDSGenerateBackgroundImage", "Constructor of XSDataResultXDSGenerateBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def getXdsBackgroundImage(self): return self._xdsBackgroundImage
	def setXdsBackgroundImage(self, xdsBackgroundImage):
		checkType("XSDataResultXDSGenerateBackgroundImage", "setXdsBackgroundImage", xdsBackgroundImage, "XSDataFile")
		self._xdsBackgroundImage = xdsBackgroundImage
	def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
	# Properties
	xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
	def export(self, outfile, level, name_='XSDataResultXDSGenerateBackgroundImage'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultXDSGenerateBackgroundImage'):
		XSDataResultXDS.exportChildren(self, outfile, level, name_)
		if self._xdsBackgroundImage is not None:
			self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
		else:
			warnEmptyAttribute("xdsBackgroundImage", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xdsBackgroundImage':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setXdsBackgroundImage(obj_)
		XSDataResultXDS.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultXDSGenerateBackgroundImage" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultXDSGenerateBackgroundImage' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultXDSGenerateBackgroundImage.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultXDSGenerateBackgroundImage" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultXDSGenerateBackgroundImage()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultXDSGenerateBackgroundImage



# End of data representation classes.



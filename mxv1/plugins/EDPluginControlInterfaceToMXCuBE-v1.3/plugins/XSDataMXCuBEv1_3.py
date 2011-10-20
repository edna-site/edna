#!/usr/bin/env python

#
# Generated Thu Oct 20 10:56::32 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
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


class XSDataMXCuBEDataSet(object):
	def __init__(self, imageFile=None):
		if imageFile is None:
			self.__imageFile = []
		else:
			checkType("XSDataMXCuBEDataSet", "Constructor of XSDataMXCuBEDataSet", imageFile, "list")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMXCuBEDataSet' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMXCuBEDataSet is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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

class XSDataMXCuBEParameters(XSData):
	def __init__(self, transmission=None, output_file=None, current_osc_start=None, current_energy=None, directory=None, number_passes=None, anomalous=None, phiStart=None, current_wavelength=None, run_number=None, residues=None, current_detdistance=None, number_images=None, inverse_beam=None, processing=None, kappaStart=None, template=None, first_image=None, osc_range=None, comments=None, mad_energies=None, detector_mode=None, sum_images=None, process_directory=None, osc_start=None, overlap=None, prefix=None, mad_4_energy=None, mad_3_energy=None, mad_2_energy=None, mad_1_energy=None, beam_size_y=None, beam_size_x=None, y_beam=None, x_beam=None, resolution_at_corner=None, resolution=None, exposure_time=None, blSampleId=None, sessionId=None):
		XSData.__init__(self, )
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", sessionId, "integer")
		self.__sessionId = sessionId
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", blSampleId, "integer")
		self.__blSampleId = blSampleId
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", exposure_time, "float")
		self.__exposure_time = exposure_time
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", resolution, "float")
		self.__resolution = resolution
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", resolution_at_corner, "float")
		self.__resolution_at_corner = resolution_at_corner
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", x_beam, "float")
		self.__x_beam = x_beam
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", y_beam, "float")
		self.__y_beam = y_beam
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", beam_size_x, "float")
		self.__beam_size_x = beam_size_x
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", beam_size_y, "float")
		self.__beam_size_y = beam_size_y
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", mad_1_energy, "float")
		self.__mad_1_energy = mad_1_energy
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", mad_2_energy, "float")
		self.__mad_2_energy = mad_2_energy
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", mad_3_energy, "float")
		self.__mad_3_energy = mad_3_energy
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", mad_4_energy, "float")
		self.__mad_4_energy = mad_4_energy
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", prefix, "string")
		self.__prefix = prefix
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", overlap, "float")
		self.__overlap = overlap
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", osc_start, "float")
		self.__osc_start = osc_start
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", process_directory, "string")
		self.__process_directory = process_directory
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", sum_images, "float")
		self.__sum_images = sum_images
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", detector_mode, "string")
		self.__detector_mode = detector_mode
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", mad_energies, "string")
		self.__mad_energies = mad_energies
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", comments, "string")
		self.__comments = comments
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", osc_range, "float")
		self.__osc_range = osc_range
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", first_image, "integer")
		self.__first_image = first_image
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", template, "string")
		self.__template = template
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", kappaStart, "float")
		self.__kappaStart = kappaStart
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", processing, "boolean")
		self.__processing = processing
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", inverse_beam, "float")
		self.__inverse_beam = inverse_beam
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", number_images, "integer")
		self.__number_images = number_images
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", current_detdistance, "float")
		self.__current_detdistance = current_detdistance
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", residues, "string")
		self.__residues = residues
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", run_number, "integer")
		self.__run_number = run_number
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", current_wavelength, "float")
		self.__current_wavelength = current_wavelength
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", phiStart, "float")
		self.__phiStart = phiStart
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", anomalous, "boolean")
		self.__anomalous = anomalous
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", number_passes, "integer")
		self.__number_passes = number_passes
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", directory, "string")
		self.__directory = directory
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", current_energy, "float")
		self.__current_energy = current_energy
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", current_osc_start, "float")
		self.__current_osc_start = current_osc_start
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", output_file, "string")
		self.__output_file = output_file
		checkType("XSDataMXCuBEParameters", "Constructor of XSDataMXCuBEParameters", transmission, "float")
		self.__transmission = transmission
	def getSessionId(self): return self.__sessionId
	def setSessionId(self, sessionId):
		checkType("XSDataMXCuBEParameters", "setSessionId", sessionId, "integer")
		self.__sessionId = sessionId
	def delSessionId(self): self.__sessionId = None
	# Properties
	sessionId = property(getSessionId, setSessionId, delSessionId, "Property for sessionId")
	def getBlSampleId(self): return self.__blSampleId
	def setBlSampleId(self, blSampleId):
		checkType("XSDataMXCuBEParameters", "setBlSampleId", blSampleId, "integer")
		self.__blSampleId = blSampleId
	def delBlSampleId(self): self.__blSampleId = None
	# Properties
	blSampleId = property(getBlSampleId, setBlSampleId, delBlSampleId, "Property for blSampleId")
	def getExposure_time(self): return self.__exposure_time
	def setExposure_time(self, exposure_time):
		checkType("XSDataMXCuBEParameters", "setExposure_time", exposure_time, "float")
		self.__exposure_time = exposure_time
	def delExposure_time(self): self.__exposure_time = None
	# Properties
	exposure_time = property(getExposure_time, setExposure_time, delExposure_time, "Property for exposure_time")
	def getResolution(self): return self.__resolution
	def setResolution(self, resolution):
		checkType("XSDataMXCuBEParameters", "setResolution", resolution, "float")
		self.__resolution = resolution
	def delResolution(self): self.__resolution = None
	# Properties
	resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
	def getResolution_at_corner(self): return self.__resolution_at_corner
	def setResolution_at_corner(self, resolution_at_corner):
		checkType("XSDataMXCuBEParameters", "setResolution_at_corner", resolution_at_corner, "float")
		self.__resolution_at_corner = resolution_at_corner
	def delResolution_at_corner(self): self.__resolution_at_corner = None
	# Properties
	resolution_at_corner = property(getResolution_at_corner, setResolution_at_corner, delResolution_at_corner, "Property for resolution_at_corner")
	def getX_beam(self): return self.__x_beam
	def setX_beam(self, x_beam):
		checkType("XSDataMXCuBEParameters", "setX_beam", x_beam, "float")
		self.__x_beam = x_beam
	def delX_beam(self): self.__x_beam = None
	# Properties
	x_beam = property(getX_beam, setX_beam, delX_beam, "Property for x_beam")
	def getY_beam(self): return self.__y_beam
	def setY_beam(self, y_beam):
		checkType("XSDataMXCuBEParameters", "setY_beam", y_beam, "float")
		self.__y_beam = y_beam
	def delY_beam(self): self.__y_beam = None
	# Properties
	y_beam = property(getY_beam, setY_beam, delY_beam, "Property for y_beam")
	def getBeam_size_x(self): return self.__beam_size_x
	def setBeam_size_x(self, beam_size_x):
		checkType("XSDataMXCuBEParameters", "setBeam_size_x", beam_size_x, "float")
		self.__beam_size_x = beam_size_x
	def delBeam_size_x(self): self.__beam_size_x = None
	# Properties
	beam_size_x = property(getBeam_size_x, setBeam_size_x, delBeam_size_x, "Property for beam_size_x")
	def getBeam_size_y(self): return self.__beam_size_y
	def setBeam_size_y(self, beam_size_y):
		checkType("XSDataMXCuBEParameters", "setBeam_size_y", beam_size_y, "float")
		self.__beam_size_y = beam_size_y
	def delBeam_size_y(self): self.__beam_size_y = None
	# Properties
	beam_size_y = property(getBeam_size_y, setBeam_size_y, delBeam_size_y, "Property for beam_size_y")
	def getMad_1_energy(self): return self.__mad_1_energy
	def setMad_1_energy(self, mad_1_energy):
		checkType("XSDataMXCuBEParameters", "setMad_1_energy", mad_1_energy, "float")
		self.__mad_1_energy = mad_1_energy
	def delMad_1_energy(self): self.__mad_1_energy = None
	# Properties
	mad_1_energy = property(getMad_1_energy, setMad_1_energy, delMad_1_energy, "Property for mad_1_energy")
	def getMad_2_energy(self): return self.__mad_2_energy
	def setMad_2_energy(self, mad_2_energy):
		checkType("XSDataMXCuBEParameters", "setMad_2_energy", mad_2_energy, "float")
		self.__mad_2_energy = mad_2_energy
	def delMad_2_energy(self): self.__mad_2_energy = None
	# Properties
	mad_2_energy = property(getMad_2_energy, setMad_2_energy, delMad_2_energy, "Property for mad_2_energy")
	def getMad_3_energy(self): return self.__mad_3_energy
	def setMad_3_energy(self, mad_3_energy):
		checkType("XSDataMXCuBEParameters", "setMad_3_energy", mad_3_energy, "float")
		self.__mad_3_energy = mad_3_energy
	def delMad_3_energy(self): self.__mad_3_energy = None
	# Properties
	mad_3_energy = property(getMad_3_energy, setMad_3_energy, delMad_3_energy, "Property for mad_3_energy")
	def getMad_4_energy(self): return self.__mad_4_energy
	def setMad_4_energy(self, mad_4_energy):
		checkType("XSDataMXCuBEParameters", "setMad_4_energy", mad_4_energy, "float")
		self.__mad_4_energy = mad_4_energy
	def delMad_4_energy(self): self.__mad_4_energy = None
	# Properties
	mad_4_energy = property(getMad_4_energy, setMad_4_energy, delMad_4_energy, "Property for mad_4_energy")
	def getPrefix(self): return self.__prefix
	def setPrefix(self, prefix):
		checkType("XSDataMXCuBEParameters", "setPrefix", prefix, "string")
		self.__prefix = prefix
	def delPrefix(self): self.__prefix = None
	# Properties
	prefix = property(getPrefix, setPrefix, delPrefix, "Property for prefix")
	def getOverlap(self): return self.__overlap
	def setOverlap(self, overlap):
		checkType("XSDataMXCuBEParameters", "setOverlap", overlap, "float")
		self.__overlap = overlap
	def delOverlap(self): self.__overlap = None
	# Properties
	overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
	def getOsc_start(self): return self.__osc_start
	def setOsc_start(self, osc_start):
		checkType("XSDataMXCuBEParameters", "setOsc_start", osc_start, "float")
		self.__osc_start = osc_start
	def delOsc_start(self): self.__osc_start = None
	# Properties
	osc_start = property(getOsc_start, setOsc_start, delOsc_start, "Property for osc_start")
	def getProcess_directory(self): return self.__process_directory
	def setProcess_directory(self, process_directory):
		checkType("XSDataMXCuBEParameters", "setProcess_directory", process_directory, "string")
		self.__process_directory = process_directory
	def delProcess_directory(self): self.__process_directory = None
	# Properties
	process_directory = property(getProcess_directory, setProcess_directory, delProcess_directory, "Property for process_directory")
	def getSum_images(self): return self.__sum_images
	def setSum_images(self, sum_images):
		checkType("XSDataMXCuBEParameters", "setSum_images", sum_images, "float")
		self.__sum_images = sum_images
	def delSum_images(self): self.__sum_images = None
	# Properties
	sum_images = property(getSum_images, setSum_images, delSum_images, "Property for sum_images")
	def getDetector_mode(self): return self.__detector_mode
	def setDetector_mode(self, detector_mode):
		checkType("XSDataMXCuBEParameters", "setDetector_mode", detector_mode, "string")
		self.__detector_mode = detector_mode
	def delDetector_mode(self): self.__detector_mode = None
	# Properties
	detector_mode = property(getDetector_mode, setDetector_mode, delDetector_mode, "Property for detector_mode")
	def getMad_energies(self): return self.__mad_energies
	def setMad_energies(self, mad_energies):
		checkType("XSDataMXCuBEParameters", "setMad_energies", mad_energies, "string")
		self.__mad_energies = mad_energies
	def delMad_energies(self): self.__mad_energies = None
	# Properties
	mad_energies = property(getMad_energies, setMad_energies, delMad_energies, "Property for mad_energies")
	def getComments(self): return self.__comments
	def setComments(self, comments):
		checkType("XSDataMXCuBEParameters", "setComments", comments, "string")
		self.__comments = comments
	def delComments(self): self.__comments = None
	# Properties
	comments = property(getComments, setComments, delComments, "Property for comments")
	def getOsc_range(self): return self.__osc_range
	def setOsc_range(self, osc_range):
		checkType("XSDataMXCuBEParameters", "setOsc_range", osc_range, "float")
		self.__osc_range = osc_range
	def delOsc_range(self): self.__osc_range = None
	# Properties
	osc_range = property(getOsc_range, setOsc_range, delOsc_range, "Property for osc_range")
	def getFirst_image(self): return self.__first_image
	def setFirst_image(self, first_image):
		checkType("XSDataMXCuBEParameters", "setFirst_image", first_image, "integer")
		self.__first_image = first_image
	def delFirst_image(self): self.__first_image = None
	# Properties
	first_image = property(getFirst_image, setFirst_image, delFirst_image, "Property for first_image")
	def getTemplate(self): return self.__template
	def setTemplate(self, template):
		checkType("XSDataMXCuBEParameters", "setTemplate", template, "string")
		self.__template = template
	def delTemplate(self): self.__template = None
	# Properties
	template = property(getTemplate, setTemplate, delTemplate, "Property for template")
	def getKappaStart(self): return self.__kappaStart
	def setKappaStart(self, kappaStart):
		checkType("XSDataMXCuBEParameters", "setKappaStart", kappaStart, "float")
		self.__kappaStart = kappaStart
	def delKappaStart(self): self.__kappaStart = None
	# Properties
	kappaStart = property(getKappaStart, setKappaStart, delKappaStart, "Property for kappaStart")
	def getProcessing(self): return self.__processing
	def setProcessing(self, processing):
		checkType("XSDataMXCuBEParameters", "setProcessing", processing, "boolean")
		self.__processing = processing
	def delProcessing(self): self.__processing = None
	# Properties
	processing = property(getProcessing, setProcessing, delProcessing, "Property for processing")
	def getInverse_beam(self): return self.__inverse_beam
	def setInverse_beam(self, inverse_beam):
		checkType("XSDataMXCuBEParameters", "setInverse_beam", inverse_beam, "float")
		self.__inverse_beam = inverse_beam
	def delInverse_beam(self): self.__inverse_beam = None
	# Properties
	inverse_beam = property(getInverse_beam, setInverse_beam, delInverse_beam, "Property for inverse_beam")
	def getNumber_images(self): return self.__number_images
	def setNumber_images(self, number_images):
		checkType("XSDataMXCuBEParameters", "setNumber_images", number_images, "integer")
		self.__number_images = number_images
	def delNumber_images(self): self.__number_images = None
	# Properties
	number_images = property(getNumber_images, setNumber_images, delNumber_images, "Property for number_images")
	def getCurrent_detdistance(self): return self.__current_detdistance
	def setCurrent_detdistance(self, current_detdistance):
		checkType("XSDataMXCuBEParameters", "setCurrent_detdistance", current_detdistance, "float")
		self.__current_detdistance = current_detdistance
	def delCurrent_detdistance(self): self.__current_detdistance = None
	# Properties
	current_detdistance = property(getCurrent_detdistance, setCurrent_detdistance, delCurrent_detdistance, "Property for current_detdistance")
	def getResidues(self): return self.__residues
	def setResidues(self, residues):
		checkType("XSDataMXCuBEParameters", "setResidues", residues, "string")
		self.__residues = residues
	def delResidues(self): self.__residues = None
	# Properties
	residues = property(getResidues, setResidues, delResidues, "Property for residues")
	def getRun_number(self): return self.__run_number
	def setRun_number(self, run_number):
		checkType("XSDataMXCuBEParameters", "setRun_number", run_number, "integer")
		self.__run_number = run_number
	def delRun_number(self): self.__run_number = None
	# Properties
	run_number = property(getRun_number, setRun_number, delRun_number, "Property for run_number")
	def getCurrent_wavelength(self): return self.__current_wavelength
	def setCurrent_wavelength(self, current_wavelength):
		checkType("XSDataMXCuBEParameters", "setCurrent_wavelength", current_wavelength, "float")
		self.__current_wavelength = current_wavelength
	def delCurrent_wavelength(self): self.__current_wavelength = None
	# Properties
	current_wavelength = property(getCurrent_wavelength, setCurrent_wavelength, delCurrent_wavelength, "Property for current_wavelength")
	def getPhiStart(self): return self.__phiStart
	def setPhiStart(self, phiStart):
		checkType("XSDataMXCuBEParameters", "setPhiStart", phiStart, "float")
		self.__phiStart = phiStart
	def delPhiStart(self): self.__phiStart = None
	# Properties
	phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
	def getAnomalous(self): return self.__anomalous
	def setAnomalous(self, anomalous):
		checkType("XSDataMXCuBEParameters", "setAnomalous", anomalous, "boolean")
		self.__anomalous = anomalous
	def delAnomalous(self): self.__anomalous = None
	# Properties
	anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
	def getNumber_passes(self): return self.__number_passes
	def setNumber_passes(self, number_passes):
		checkType("XSDataMXCuBEParameters", "setNumber_passes", number_passes, "integer")
		self.__number_passes = number_passes
	def delNumber_passes(self): self.__number_passes = None
	# Properties
	number_passes = property(getNumber_passes, setNumber_passes, delNumber_passes, "Property for number_passes")
	def getDirectory(self): return self.__directory
	def setDirectory(self, directory):
		checkType("XSDataMXCuBEParameters", "setDirectory", directory, "string")
		self.__directory = directory
	def delDirectory(self): self.__directory = None
	# Properties
	directory = property(getDirectory, setDirectory, delDirectory, "Property for directory")
	def getCurrent_energy(self): return self.__current_energy
	def setCurrent_energy(self, current_energy):
		checkType("XSDataMXCuBEParameters", "setCurrent_energy", current_energy, "float")
		self.__current_energy = current_energy
	def delCurrent_energy(self): self.__current_energy = None
	# Properties
	current_energy = property(getCurrent_energy, setCurrent_energy, delCurrent_energy, "Property for current_energy")
	def getCurrent_osc_start(self): return self.__current_osc_start
	def setCurrent_osc_start(self, current_osc_start):
		checkType("XSDataMXCuBEParameters", "setCurrent_osc_start", current_osc_start, "float")
		self.__current_osc_start = current_osc_start
	def delCurrent_osc_start(self): self.__current_osc_start = None
	# Properties
	current_osc_start = property(getCurrent_osc_start, setCurrent_osc_start, delCurrent_osc_start, "Property for current_osc_start")
	def getOutput_file(self): return self.__output_file
	def setOutput_file(self, output_file):
		checkType("XSDataMXCuBEParameters", "setOutput_file", output_file, "string")
		self.__output_file = output_file
	def delOutput_file(self): self.__output_file = None
	# Properties
	output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
	def getTransmission(self): return self.__transmission
	def setTransmission(self, transmission):
		checkType("XSDataMXCuBEParameters", "setTransmission", transmission, "float")
		self.__transmission = transmission
	def delTransmission(self): self.__transmission = None
	# Properties
	transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
	def export(self, outfile, level, name_='XSDataMXCuBEParameters'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMXCuBEParameters'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__sessionId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<sessionId>%d</sessionId>\n' % self.__sessionId))
		else:
			warnEmptyAttribute("sessionId", "integer")
		if self.__blSampleId is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<blSampleId>%d</blSampleId>\n' % self.__blSampleId))
		else:
			warnEmptyAttribute("blSampleId", "integer")
		if self.__exposure_time is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<exposure_time>%e</exposure_time>\n' % self.__exposure_time))
		else:
			warnEmptyAttribute("exposure_time", "float")
		if self.__resolution is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolution>%e</resolution>\n' % self.__resolution))
		else:
			warnEmptyAttribute("resolution", "float")
		if self.__resolution_at_corner is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<resolution_at_corner>%e</resolution_at_corner>\n' % self.__resolution_at_corner))
		else:
			warnEmptyAttribute("resolution_at_corner", "float")
		if self.__x_beam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<x_beam>%e</x_beam>\n' % self.__x_beam))
		else:
			warnEmptyAttribute("x_beam", "float")
		if self.__y_beam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<y_beam>%e</y_beam>\n' % self.__y_beam))
		else:
			warnEmptyAttribute("y_beam", "float")
		if self.__beam_size_x is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beam_size_x>%e</beam_size_x>\n' % self.__beam_size_x))
		else:
			warnEmptyAttribute("beam_size_x", "float")
		if self.__beam_size_y is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<beam_size_y>%e</beam_size_y>\n' % self.__beam_size_y))
		else:
			warnEmptyAttribute("beam_size_y", "float")
		if self.__mad_1_energy is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<mad_1_energy>%e</mad_1_energy>\n' % self.__mad_1_energy))
		else:
			warnEmptyAttribute("mad_1_energy", "float")
		if self.__mad_2_energy is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<mad_2_energy>%e</mad_2_energy>\n' % self.__mad_2_energy))
		else:
			warnEmptyAttribute("mad_2_energy", "float")
		if self.__mad_3_energy is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<mad_3_energy>%e</mad_3_energy>\n' % self.__mad_3_energy))
		else:
			warnEmptyAttribute("mad_3_energy", "float")
		if self.__mad_4_energy is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<mad_4_energy>%e</mad_4_energy>\n' % self.__mad_4_energy))
		else:
			warnEmptyAttribute("mad_4_energy", "float")
		if self.__prefix is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<prefix>%s</prefix>\n' % self.__prefix))
		else:
			warnEmptyAttribute("prefix", "string")
		if self.__overlap is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<overlap>%e</overlap>\n' % self.__overlap))
		else:
			warnEmptyAttribute("overlap", "float")
		if self.__osc_start is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<osc_start>%e</osc_start>\n' % self.__osc_start))
		else:
			warnEmptyAttribute("osc_start", "float")
		if self.__process_directory is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<process_directory>%s</process_directory>\n' % self.__process_directory))
		else:
			warnEmptyAttribute("process_directory", "string")
		if self.__sum_images is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<sum_images>%e</sum_images>\n' % self.__sum_images))
		else:
			warnEmptyAttribute("sum_images", "float")
		if self.__detector_mode is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<detector_mode>%s</detector_mode>\n' % self.__detector_mode))
		else:
			warnEmptyAttribute("detector_mode", "string")
		if self.__mad_energies is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<mad_energies>%s</mad_energies>\n' % self.__mad_energies))
		else:
			warnEmptyAttribute("mad_energies", "string")
		if self.__comments is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comments>%s</comments>\n' % self.__comments))
		else:
			warnEmptyAttribute("comments", "string")
		if self.__osc_range is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<osc_range>%e</osc_range>\n' % self.__osc_range))
		else:
			warnEmptyAttribute("osc_range", "float")
		if self.__first_image is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<first_image>%d</first_image>\n' % self.__first_image))
		else:
			warnEmptyAttribute("first_image", "integer")
		if self.__template is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<template>%s</template>\n' % self.__template))
		else:
			warnEmptyAttribute("template", "string")
		if self.__kappaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<kappaStart>%e</kappaStart>\n' % self.__kappaStart))
		else:
			warnEmptyAttribute("kappaStart", "float")
		if self.__processing is not None:
			showIndent(outfile, level)
			if self.__processing:
				outfile.write(unicode('<processing>true</processing>\n'))
			else:
				outfile.write(unicode('<processing>false</processing>\n'))
		else:
			warnEmptyAttribute("processing", "boolean")
		if self.__inverse_beam is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<inverse_beam>%e</inverse_beam>\n' % self.__inverse_beam))
		else:
			warnEmptyAttribute("inverse_beam", "float")
		if self.__number_images is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<number_images>%d</number_images>\n' % self.__number_images))
		else:
			warnEmptyAttribute("number_images", "integer")
		if self.__current_detdistance is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<current_detdistance>%e</current_detdistance>\n' % self.__current_detdistance))
		else:
			warnEmptyAttribute("current_detdistance", "float")
		if self.__residues is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<residues>%s</residues>\n' % self.__residues))
		else:
			warnEmptyAttribute("residues", "string")
		if self.__run_number is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<run_number>%d</run_number>\n' % self.__run_number))
		else:
			warnEmptyAttribute("run_number", "integer")
		if self.__current_wavelength is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<current_wavelength>%e</current_wavelength>\n' % self.__current_wavelength))
		else:
			warnEmptyAttribute("current_wavelength", "float")
		if self.__phiStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<phiStart>%e</phiStart>\n' % self.__phiStart))
		else:
			warnEmptyAttribute("phiStart", "float")
		if self.__anomalous is not None:
			showIndent(outfile, level)
			if self.__anomalous:
				outfile.write(unicode('<anomalous>true</anomalous>\n'))
			else:
				outfile.write(unicode('<anomalous>false</anomalous>\n'))
		else:
			warnEmptyAttribute("anomalous", "boolean")
		if self.__number_passes is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<number_passes>%d</number_passes>\n' % self.__number_passes))
		else:
			warnEmptyAttribute("number_passes", "integer")
		if self.__directory is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<directory>%s</directory>\n' % self.__directory))
		else:
			warnEmptyAttribute("directory", "string")
		if self.__current_energy is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<current_energy>%e</current_energy>\n' % self.__current_energy))
		else:
			warnEmptyAttribute("current_energy", "float")
		if self.__current_osc_start is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<current_osc_start>%e</current_osc_start>\n' % self.__current_osc_start))
		else:
			warnEmptyAttribute("current_osc_start", "float")
		if self.__output_file is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<output_file>%s</output_file>\n' % self.__output_file))
		else:
			warnEmptyAttribute("output_file", "string")
		if self.__transmission is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<transmission>%e</transmission>\n' % self.__transmission))
		else:
			warnEmptyAttribute("transmission", "float")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sessionId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__sessionId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'blSampleId':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__blSampleId = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposure_time':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__exposure_time = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolution = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'resolution_at_corner':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__resolution_at_corner = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x_beam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__x_beam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'y_beam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__y_beam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beam_size_x':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beam_size_x = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beam_size_y':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__beam_size_y = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mad_1_energy':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__mad_1_energy = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mad_2_energy':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__mad_2_energy = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mad_3_energy':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__mad_3_energy = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mad_4_energy':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__mad_4_energy = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'prefix':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__prefix = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'overlap':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__overlap = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'osc_start':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__osc_start = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'process_directory':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__process_directory = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sum_images':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__sum_images = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector_mode':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__detector_mode = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mad_energies':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__mad_energies = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comments':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comments = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'osc_range':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__osc_range = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'first_image':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__first_image = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'template':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__template = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__kappaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'processing':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__processing = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inverse_beam':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__inverse_beam = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'number_images':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__number_images = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'current_detdistance':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__current_detdistance = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'residues':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__residues = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'run_number':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__run_number = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'current_wavelength':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__current_wavelength = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phiStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__phiStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'anomalous':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				if sval_ in ('True', 'true', '1'):
					ival_ = True
				elif sval_ in ('False', 'false', '0'):
					ival_ = False
				else:
					raise ValueError('requires boolean -- %s' % child_.toxml())
				self.__anomalous = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'number_passes':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__number_passes = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'directory':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__directory = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'current_energy':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__current_energy = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'current_osc_start':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__current_osc_start = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output_file':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__output_file = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'transmission':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__transmission = fval_
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMXCuBEParameters" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMXCuBEParameters' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMXCuBEParameters is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMXCuBEParameters.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMXCuBEParameters()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMXCuBEParameters" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMXCuBEParameters()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMXCuBEParameters

class XSDataInputMXCuBE(XSDataInput):
	def __init__(self, configuration=None, dataSet=None, sample=None, outputFileDirectory=None, experimentalCondition=None, diffractionPlan=None, dataCollectionId=None, characterisationInput=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", characterisationInput, "XSDataInputCharacterisation")
		self.__characterisationInput = characterisationInput
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", dataCollectionId, "XSDataInteger")
		self.__dataCollectionId = dataCollectionId
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", diffractionPlan, "XSDataDiffractionPlan")
		self.__diffractionPlan = diffractionPlan
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", experimentalCondition, "XSDataExperimentalCondition")
		self.__experimentalCondition = experimentalCondition
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", outputFileDirectory, "XSDataFile")
		self.__outputFileDirectory = outputFileDirectory
		checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", sample, "XSDataSampleCrystalMM")
		self.__sample = sample
		if dataSet is None:
			self.__dataSet = []
		else:
			checkType("XSDataInputMXCuBE", "Constructor of XSDataInputMXCuBE", dataSet, "list")
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputMXCuBE' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputMXCuBE is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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
	def __init__(self, status=None, htmlPage=None, outputFileDictionary=None, listOfOutputFiles=None, collectionPlan=None, characterisationResult=None, characterisationExecutiveSummary=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", characterisationExecutiveSummary, "XSDataString")
		self.__characterisationExecutiveSummary = characterisationExecutiveSummary
		checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", characterisationResult, "XSDataResultCharacterisation")
		self.__characterisationResult = characterisationResult
		if collectionPlan is None:
			self.__collectionPlan = []
		else:
			checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", collectionPlan, "list")
			self.__collectionPlan = collectionPlan
		checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", listOfOutputFiles, "XSDataString")
		self.__listOfOutputFiles = listOfOutputFiles
		checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", outputFileDictionary, "XSDataDictionary")
		self.__outputFileDictionary = outputFileDictionary
		checkType("XSDataResultMXCuBE", "Constructor of XSDataResultMXCuBE", htmlPage, "XSDataFile")
		self.__htmlPage = htmlPage
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
	def getHtmlPage(self): return self.__htmlPage
	def setHtmlPage(self, htmlPage):
		checkType("XSDataResultMXCuBE", "setHtmlPage", htmlPage, "XSDataFile")
		self.__htmlPage = htmlPage
	def delHtmlPage(self): self.__htmlPage = None
	# Properties
	htmlPage = property(getHtmlPage, setHtmlPage, delHtmlPage, "Property for htmlPage")
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
		if self.__htmlPage is not None:
			self.htmlPage.export(outfile, level, name_='htmlPage')
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'htmlPage':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setHtmlPage(obj_)
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
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultMXCuBE' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultMXCuBE is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
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



#!/usr/bin/env python

#
# Generated Thu Jun 30 09:26::16 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataInterfacev1_2 import XSDataInputInterface
from XSDataInterfacev1_2 import XSDataResultInterface
from XSDataMXv2 import kappa_alignment_response
from XSDataMXv2 import XSDataCollection
from XSDataCommon import XSDataAngle
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataResultCharacterisation




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


class XSDataInputInterfacev2_2(XSDataInputInterface):
	def __init__(self, inputCharacterisation=None, comments=None, shortComments=None, dataCollectionId=None, transmission=None, wavelength=None, beamPosY=None, beamPosX=None, resultsFilePath=None, generatedTemplateFile=None, templateMode=None, beamSizeY=None, beamSizeX=None, beamSize=None, minExposureTimePerImage=None, flux=None, imagePath=None, sample=None, diffractionPlan=None, experimentalCondition=None, phi=None, kappa=None, omega=None, possibleOrientations=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv1ResultCharacterisation_Reference=None, mxv1InputCharacterisation=None):
		XSDataInputInterface.__init__(self, inputCharacterisation, comments, shortComments, dataCollectionId, transmission, wavelength, beamPosY, beamPosX, resultsFilePath, generatedTemplateFile, templateMode, beamSizeY, beamSizeX, beamSize, minExposureTimePerImage, flux, imagePath, sample, diffractionPlan, experimentalCondition)
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", mxv1InputCharacterisation, "XSDataInputCharacterisation")
		self.__mxv1InputCharacterisation = mxv1InputCharacterisation
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", mxv2DataCollection, "XSDataCollection")
		self.__mxv2DataCollection = mxv2DataCollection
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", mxv2DataCollection_Reference, "XSDataCollection")
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", omega, "XSDataAngle")
		self.__omega = omega
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", kappa, "XSDataAngle")
		self.__kappa = kappa
		checkType("XSDataInputInterfacev2_2", "Constructor of XSDataInputInterfacev2_2", phi, "XSDataAngle")
		self.__phi = phi
	def getMxv1InputCharacterisation(self): return self.__mxv1InputCharacterisation
	def setMxv1InputCharacterisation(self, mxv1InputCharacterisation):
		checkType("XSDataInputInterfacev2_2", "setMxv1InputCharacterisation", mxv1InputCharacterisation, "XSDataInputCharacterisation")
		self.__mxv1InputCharacterisation = mxv1InputCharacterisation
	def delMxv1InputCharacterisation(self): self.__mxv1InputCharacterisation = None
	# Properties
	mxv1InputCharacterisation = property(getMxv1InputCharacterisation, setMxv1InputCharacterisation, delMxv1InputCharacterisation, "Property for mxv1InputCharacterisation")
	def getMxv1ResultCharacterisation_Reference(self): return self.__mxv1ResultCharacterisation_Reference
	def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
		checkType("XSDataInputInterfacev2_2", "setMxv1ResultCharacterisation_Reference", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
	def delMxv1ResultCharacterisation_Reference(self): self.__mxv1ResultCharacterisation_Reference = None
	# Properties
	mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
	def getMxv2DataCollection(self): return self.__mxv2DataCollection
	def setMxv2DataCollection(self, mxv2DataCollection):
		checkType("XSDataInputInterfacev2_2", "setMxv2DataCollection", mxv2DataCollection, "XSDataCollection")
		self.__mxv2DataCollection = mxv2DataCollection
	def delMxv2DataCollection(self): self.__mxv2DataCollection = None
	# Properties
	mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
	def getMxv2DataCollection_Reference(self): return self.__mxv2DataCollection_Reference
	def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
		checkType("XSDataInputInterfacev2_2", "setMxv2DataCollection_Reference", mxv2DataCollection_Reference, "XSDataCollection")
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
	def delMxv2DataCollection_Reference(self): self.__mxv2DataCollection_Reference = None
	# Properties
	mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
	def getPossibleOrientations(self): return self.__possibleOrientations
	def setPossibleOrientations(self, possibleOrientations):
		checkType("XSDataInputInterfacev2_2", "setPossibleOrientations", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
	def delPossibleOrientations(self): self.__possibleOrientations = None
	# Properties
	possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
	def getOmega(self): return self.__omega
	def setOmega(self, omega):
		checkType("XSDataInputInterfacev2_2", "setOmega", omega, "XSDataAngle")
		self.__omega = omega
	def delOmega(self): self.__omega = None
	# Properties
	omega = property(getOmega, setOmega, delOmega, "Property for omega")
	def getKappa(self): return self.__kappa
	def setKappa(self, kappa):
		checkType("XSDataInputInterfacev2_2", "setKappa", kappa, "XSDataAngle")
		self.__kappa = kappa
	def delKappa(self): self.__kappa = None
	# Properties
	kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
	def getPhi(self): return self.__phi
	def setPhi(self, phi):
		checkType("XSDataInputInterfacev2_2", "setPhi", phi, "XSDataAngle")
		self.__phi = phi
	def delPhi(self): self.__phi = None
	# Properties
	phi = property(getPhi, setPhi, delPhi, "Property for phi")
	def export(self, outfile, level, name_='XSDataInputInterfacev2_2'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputInterfacev2_2'):
		XSDataInputInterface.exportChildren(self, outfile, level, name_)
		if self.__mxv1InputCharacterisation is not None:
			self.mxv1InputCharacterisation.export(outfile, level, name_='mxv1InputCharacterisation')
		else:
			warnEmptyAttribute("mxv1InputCharacterisation", "XSDataInputCharacterisation")
		if self.__mxv1ResultCharacterisation_Reference is not None:
			self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
		if self.__mxv2DataCollection is not None:
			self.mxv2DataCollection.export(outfile, level, name_='mxv2DataCollection')
		if self.__mxv2DataCollection_Reference is not None:
			self.mxv2DataCollection_Reference.export(outfile, level, name_='mxv2DataCollection_Reference')
		if self.__possibleOrientations is not None:
			self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
		if self.__omega is not None:
			self.omega.export(outfile, level, name_='omega')
		if self.__kappa is not None:
			self.kappa.export(outfile, level, name_='kappa')
		if self.__phi is not None:
			self.phi.export(outfile, level, name_='phi')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv1InputCharacterisation':
			obj_ = XSDataInputCharacterisation()
			obj_.build(child_)
			self.setMxv1InputCharacterisation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv1ResultCharacterisation_Reference':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setMxv1ResultCharacterisation_Reference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv2DataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setMxv2DataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv2DataCollection_Reference':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setMxv2DataCollection_Reference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'possibleOrientations':
			obj_ = kappa_alignment_response()
			obj_.build(child_)
			self.setPossibleOrientations(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omega':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOmega(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappa':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setKappa(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phi':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setPhi(obj_)
		XSDataInputInterface.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputInterfacev2_2" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputInterfacev2_2' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataInputInterfacev2_2 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputInterfacev2_2.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputInterfacev2_2()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputInterfacev2_2" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputInterfacev2_2()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputInterfacev2_2

class XSDataResultInterfacev2_2(XSDataResultInterface):
	def __init__(self, resultControlISPyB=None, resultCharacterisation=None, possibleOrientations=None, suggestedStrategy=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv1ResultCharacterisation_Reference=None, mxv1ResultCharacterisation=None):
		XSDataResultInterface.__init__(self, resultControlISPyB, resultCharacterisation)
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", mxv1ResultCharacterisation, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation = mxv1ResultCharacterisation
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", mxv2DataCollection, "XSDataCollection")
		self.__mxv2DataCollection = mxv2DataCollection
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", mxv2DataCollection_Reference, "XSDataCollection")
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", suggestedStrategy, "XSDataResultStrategy")
		self.__suggestedStrategy = suggestedStrategy
		checkType("XSDataResultInterfacev2_2", "Constructor of XSDataResultInterfacev2_2", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
	def getMxv1ResultCharacterisation(self): return self.__mxv1ResultCharacterisation
	def setMxv1ResultCharacterisation(self, mxv1ResultCharacterisation):
		checkType("XSDataResultInterfacev2_2", "setMxv1ResultCharacterisation", mxv1ResultCharacterisation, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation = mxv1ResultCharacterisation
	def delMxv1ResultCharacterisation(self): self.__mxv1ResultCharacterisation = None
	# Properties
	mxv1ResultCharacterisation = property(getMxv1ResultCharacterisation, setMxv1ResultCharacterisation, delMxv1ResultCharacterisation, "Property for mxv1ResultCharacterisation")
	def getMxv1ResultCharacterisation_Reference(self): return self.__mxv1ResultCharacterisation_Reference
	def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
		checkType("XSDataResultInterfacev2_2", "setMxv1ResultCharacterisation_Reference", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
	def delMxv1ResultCharacterisation_Reference(self): self.__mxv1ResultCharacterisation_Reference = None
	# Properties
	mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
	def getMxv2DataCollection(self): return self.__mxv2DataCollection
	def setMxv2DataCollection(self, mxv2DataCollection):
		checkType("XSDataResultInterfacev2_2", "setMxv2DataCollection", mxv2DataCollection, "XSDataCollection")
		self.__mxv2DataCollection = mxv2DataCollection
	def delMxv2DataCollection(self): self.__mxv2DataCollection = None
	# Properties
	mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
	def getMxv2DataCollection_Reference(self): return self.__mxv2DataCollection_Reference
	def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
		checkType("XSDataResultInterfacev2_2", "setMxv2DataCollection_Reference", mxv2DataCollection_Reference, "XSDataCollection")
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
	def delMxv2DataCollection_Reference(self): self.__mxv2DataCollection_Reference = None
	# Properties
	mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
	def getSuggestedStrategy(self): return self.__suggestedStrategy
	def setSuggestedStrategy(self, suggestedStrategy):
		checkType("XSDataResultInterfacev2_2", "setSuggestedStrategy", suggestedStrategy, "XSDataResultStrategy")
		self.__suggestedStrategy = suggestedStrategy
	def delSuggestedStrategy(self): self.__suggestedStrategy = None
	# Properties
	suggestedStrategy = property(getSuggestedStrategy, setSuggestedStrategy, delSuggestedStrategy, "Property for suggestedStrategy")
	def getPossibleOrientations(self): return self.__possibleOrientations
	def setPossibleOrientations(self, possibleOrientations):
		checkType("XSDataResultInterfacev2_2", "setPossibleOrientations", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
	def delPossibleOrientations(self): self.__possibleOrientations = None
	# Properties
	possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
	def export(self, outfile, level, name_='XSDataResultInterfacev2_2'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultInterfacev2_2'):
		XSDataResultInterface.exportChildren(self, outfile, level, name_)
		if self.__mxv1ResultCharacterisation is not None:
			self.mxv1ResultCharacterisation.export(outfile, level, name_='mxv1ResultCharacterisation')
		else:
			warnEmptyAttribute("mxv1ResultCharacterisation", "XSDataResultCharacterisation")
		if self.__mxv1ResultCharacterisation_Reference is not None:
			self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
		if self.__mxv2DataCollection is not None:
			self.mxv2DataCollection.export(outfile, level, name_='mxv2DataCollection')
		if self.__mxv2DataCollection_Reference is not None:
			self.mxv2DataCollection_Reference.export(outfile, level, name_='mxv2DataCollection_Reference')
		if self.__suggestedStrategy is not None:
			self.suggestedStrategy.export(outfile, level, name_='suggestedStrategy')
		if self.__possibleOrientations is not None:
			self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv1ResultCharacterisation':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setMxv1ResultCharacterisation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv1ResultCharacterisation_Reference':
			obj_ = XSDataResultCharacterisation()
			obj_.build(child_)
			self.setMxv1ResultCharacterisation_Reference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv2DataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setMxv2DataCollection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mxv2DataCollection_Reference':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.setMxv2DataCollection_Reference(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'suggestedStrategy':
			obj_ = XSDataResultStrategy()
			obj_.build(child_)
			self.setSuggestedStrategy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'possibleOrientations':
			obj_ = kappa_alignment_response()
			obj_.build(child_)
			self.setPossibleOrientations(obj_)
		XSDataResultInterface.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultInterfacev2_2" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultInterfacev2_2' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResultInterfacev2_2 is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultInterfacev2_2.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultInterfacev2_2()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultInterfacev2_2" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultInterfacev2_2()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultInterfacev2_2



# End of data representation classes.



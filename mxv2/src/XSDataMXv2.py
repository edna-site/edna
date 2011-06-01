#!/usr/bin/env python

#
# Generated Tue Mar 29 03:09::14 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node

from XSDataCommon import XSData
from XSDataCommon import XSDataDisplacement
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataRotation
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataDate
from XSDataCommon import XSDataUnitVector
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
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
	elif _value is None:
		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
		print(strMessage)
		#raise BaseException(strMessage)


def warnEmptyAttribute(_strName, _strTypeName):
	pass
	#if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
	#		print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer:
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


class possible_orientation:
	def __init__(self, rank=None, trans=None, phi=None, kappa=None, omega=None, v2=None, v1=None):
		self.__v1 = v1
		self.__v2 = v2
		self.__omega = omega
		self.__kappa = kappa
		self.__phi = phi
		self.__trans = trans
		self.__rank = rank
	def getV1(self): return self.__v1
	def setV1(self, v1):
		checkType("possible_orientation", "setV1", v1, "string")
		self.__v1 = v1
	def delV1(self): self.__v1 = None
	# Properties
	v1 = property(getV1, setV1, delV1, "Property for v1")
	def getV2(self): return self.__v2
	def setV2(self, v2):
		checkType("possible_orientation", "setV2", v2, "string")
		self.__v2 = v2
	def delV2(self): self.__v2 = None
	# Properties
	v2 = property(getV2, setV2, delV2, "Property for v2")
	def getOmega(self): return self.__omega
	def setOmega(self, omega):
		checkType("possible_orientation", "setOmega", omega, "double")
		self.__omega = omega
	def delOmega(self): self.__omega = None
	# Properties
	omega = property(getOmega, setOmega, delOmega, "Property for omega")
	def getKappa(self): return self.__kappa
	def setKappa(self, kappa):
		checkType("possible_orientation", "setKappa", kappa, "double")
		self.__kappa = kappa
	def delKappa(self): self.__kappa = None
	# Properties
	kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
	def getPhi(self): return self.__phi
	def setPhi(self, phi):
		checkType("possible_orientation", "setPhi", phi, "double")
		self.__phi = phi
	def delPhi(self): self.__phi = None
	# Properties
	phi = property(getPhi, setPhi, delPhi, "Property for phi")
	def getTrans(self): return self.__trans
	def setTrans(self, trans):
		checkType("possible_orientation", "setTrans", trans, "string")
		self.__trans = trans
	def delTrans(self): self.__trans = None
	# Properties
	trans = property(getTrans, setTrans, delTrans, "Property for trans")
	def getRank(self): return self.__rank
	def setRank(self, rank):
		checkType("possible_orientation", "setRank", rank, "double")
		self.__rank = rank
	def delRank(self): self.__rank = None
	# Properties
	rank = property(getRank, setRank, delRank, "Property for rank")
	def export(self, outfile, level, name_='possible_orientation'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='possible_orientation'):
		pass
		if self.__v1 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<v1>%s</v1>\n' % self.__v1))
		else:
			warnEmptyAttribute("v1", "string")
		if self.__v2 is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<v2>%s</v2>\n' % self.__v2))
		else:
			warnEmptyAttribute("v2", "string")
		if self.__omega is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<omega>%e</omega>\n' % self.__omega))
		else:
			warnEmptyAttribute("omega", "double")
		if self.__kappa is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<kappa>%e</kappa>\n' % self.__kappa))
		else:
			warnEmptyAttribute("kappa", "double")
		if self.__phi is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<phi>%e</phi>\n' % self.__phi))
		else:
			warnEmptyAttribute("phi", "double")
		if self.__trans is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<trans>%s</trans>\n' % self.__trans))
		else:
			warnEmptyAttribute("trans", "string")
		if self.__rank is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<rank>%e</rank>\n' % self.__rank))
		else:
			warnEmptyAttribute("rank", "double")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'v1':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__v1 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'v2':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__v2 = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omega':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__omega = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kappa':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__kappa = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'phi':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__phi = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'trans':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__trans = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rank':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__rank = fval_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="possible_orientation" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='possible_orientation' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return possible_orientation.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = possible_orientation()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="possible_orientation" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = possible_orientation()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class possible_orientation

class status:
	def __init__(self, message=None, code=None):
		self.__code = code
		self.__message = message
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("status", "setCode", code, "status_code")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def getMessage(self): return self.__message
	def setMessage(self, message):
		checkType("status", "setMessage", message, "string")
		self.__message = message
	def delMessage(self): self.__message = None
	# Properties
	message = property(getMessage, setMessage, delMessage, "Property for message")
	def export(self, outfile, level, name_='status'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='status'):
		pass
		if self.__code is not None:
			self.code.export(outfile, level, name_='code')
		else:
			warnEmptyAttribute("code", "status_code")
		if self.__message is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<message>%s</message>\n' % self.__message))
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			obj_ = status_code()
			obj_.build(child_)
			self.setCode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'message':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__message = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="status" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='status' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return status.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = status()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="status" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = status()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class status

class kappa_alignment_response:
	def __init__(self, possible_orientation=None, comment=None, status=None):
		self.__status = status
		self.__comment = comment
		if possible_orientation is None:
			self.__possible_orientation = []
		else:
			self.__possible_orientation = possible_orientation
	def getStatus(self): return self.__status
	def setStatus(self, status):
		checkType("kappa_alignment_response", "setStatus", status, "status")
		self.__status = status
	def delStatus(self): self.__status = None
	# Properties
	status = property(getStatus, setStatus, delStatus, "Property for status")
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("kappa_alignment_response", "setComment", comment, "string")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getPossible_orientation(self): return self.__possible_orientation
	def setPossible_orientation(self, possible_orientation):
		checkType("kappa_alignment_response", "setPossible_orientation", possible_orientation, "list")
		self.__possible_orientation = possible_orientation
	def delPossible_orientation(self): self.__possible_orientation = None
	# Properties
	possible_orientation = property(getPossible_orientation, setPossible_orientation, delPossible_orientation, "Property for possible_orientation")
	def addPossible_orientation(self, value):
		checkType("kappa_alignment_response", "setPossible_orientation", value, "possible_orientation")
		self.__possible_orientation.append(value)
	def insertPossible_orientation(self, index, value):
		checkType("kappa_alignment_response", "setPossible_orientation", value, "possible_orientation")
		self.__possible_orientation[index] = value
	def export(self, outfile, level, name_='kappa_alignment_response'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='kappa_alignment_response'):
		pass
		if self.__status is not None:
			self.status.export(outfile, level, name_='status')
		else:
			warnEmptyAttribute("status", "status")
		if self.__comment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comment>%s</comment>\n' % self.__comment))
		else:
			warnEmptyAttribute("comment", "string")
		for possible_orientation_ in self.getPossible_orientation():
			possible_orientation_.export(outfile, level, name_='possible_orientation')
		if self.getPossible_orientation() == []:
			warnEmptyAttribute("possible_orientation", "possible_orientation")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'status':
			obj_ = status()
			obj_.build(child_)
			self.setStatus(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comment = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'possible_orientation':
			obj_ = possible_orientation()
			obj_.build(child_)
			self.possible_orientation.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="kappa_alignment_response" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='kappa_alignment_response' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return kappa_alignment_response.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = kappa_alignment_response()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="kappa_alignment_response" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = kappa_alignment_response()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class kappa_alignment_response

class status_code:
	def __init__(self, code=None):
		self.__code = code
	def getCode(self): return self.__code
	def setCode(self, code):
		checkType("status_code", "setCode", code, "string")
		self.__code = code
	def delCode(self): self.__code = None
	# Properties
	code = property(getCode, setCode, delCode, "Property for code")
	def export(self, outfile, level, name_='status_code'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='status_code'):
		pass
		if self.__code is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<code>%s</code>\n' % self.__code))
		else:
			warnEmptyAttribute("code", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'code':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__code = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="status_code" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='status_code' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return status_code.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = status_code()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="status_code" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = status_code()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class status_code

class XSBeam(XSData):
	def __init__(self, direction=None, polarisatation=None):
		XSData.__init__(self, )
		self.__polarisatation = polarisatation
		self.__direction = direction
	def getPolarisatation(self): return self.__polarisatation
	def setPolarisatation(self, polarisatation):
		checkType("XSBeam", "setPolarisatation", polarisatation, "XSDataUnitVector")
		self.__polarisatation = polarisatation
	def delPolarisatation(self): self.__polarisatation = None
	# Properties
	polarisatation = property(getPolarisatation, setPolarisatation, delPolarisatation, "Property for polarisatation")
	def getDirection(self): return self.__direction
	def setDirection(self, direction):
		checkType("XSBeam", "setDirection", direction, "XSDataUnitVector")
		self.__direction = direction
	def delDirection(self): self.__direction = None
	# Properties
	direction = property(getDirection, setDirection, delDirection, "Property for direction")
	def export(self, outfile, level, name_='XSBeam'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSBeam'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__polarisatation is not None:
			self.polarisatation.export(outfile, level, name_='polarisatation')
		else:
			warnEmptyAttribute("polarisatation", "XSDataUnitVector")
		if self.__direction is not None:
			self.direction.export(outfile, level, name_='direction')
		else:
			warnEmptyAttribute("direction", "XSDataUnitVector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'polarisatation':
			obj_ = XSDataUnitVector()
			obj_.build(child_)
			self.setPolarisatation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direction':
			obj_ = XSDataUnitVector()
			obj_.build(child_)
			self.setDirection(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSBeam" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSBeam' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSBeam.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSBeam()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSBeam" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSBeam()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSBeam

class XSBeamSetting(XSData):
	def __init__(self, XSBeam=None, wavelength=None):
		XSData.__init__(self, )
		self.__wavelength = wavelength
		self.__XSBeam = XSBeam
	def getWavelength(self): return self.__wavelength
	def setWavelength(self, wavelength):
		checkType("XSBeamSetting", "setWavelength", wavelength, "XSDataWavelength")
		self.__wavelength = wavelength
	def delWavelength(self): self.__wavelength = None
	# Properties
	wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
	def getXSBeam(self): return self.__XSBeam
	def setXSBeam(self, XSBeam):
		checkType("XSBeamSetting", "setXSBeam", XSBeam, "XSBeam")
		self.__XSBeam = XSBeam
	def delXSBeam(self): self.__XSBeam = None
	# Properties
	XSBeam = property(getXSBeam, setXSBeam, delXSBeam, "Property for XSBeam")
	def export(self, outfile, level, name_='XSBeamSetting'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSBeamSetting'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__wavelength is not None:
			self.wavelength.export(outfile, level, name_='wavelength')
		else:
			warnEmptyAttribute("wavelength", "XSDataWavelength")
		if self.__XSBeam is not None:
			self.XSBeam.export(outfile, level, name_='XSBeam')
		else:
			warnEmptyAttribute("XSBeam", "XSBeam")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'wavelength':
			obj_ = XSDataWavelength()
			obj_.build(child_)
			self.setWavelength(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSBeam':
			obj_ = XSBeam()
			obj_.build(child_)
			self.setXSBeam(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSBeamSetting" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSBeamSetting' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSBeamSetting.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSBeamSetting()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSBeamSetting" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSBeamSetting()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSBeamSetting

class XSCalibration(XSData):
	def __init__(self, date=None):
		XSData.__init__(self, )
		self.__date = date
	def getDate(self): return self.__date
	def setDate(self, date):
		checkType("XSCalibration", "setDate", date, "XSDataDate")
		self.__date = date
	def delDate(self): self.__date = None
	# Properties
	date = property(getDate, setDate, delDate, "Property for date")
	def export(self, outfile, level, name_='XSCalibration'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSCalibration'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__date is not None:
			self.date.export(outfile, level, name_='date')
		else:
			warnEmptyAttribute("date", "XSDataDate")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'date':
			obj_ = XSDataDate()
			obj_.build(child_)
			self.setDate(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSCalibration" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSCalibration' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSCalibration.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSCalibration()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSCalibration" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSCalibration()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSCalibration

class XSCalibratedDisplacementAxis(XSData):
	def __init__(self, XSCalibration=None, zerodirection=None):
		XSData.__init__(self, )
		self.__zerodirection = zerodirection
		self.__XSCalibration = XSCalibration
	def getZerodirection(self): return self.__zerodirection
	def setZerodirection(self, zerodirection):
		checkType("XSCalibratedDisplacementAxis", "setZerodirection", zerodirection, "XSDataUnitVector")
		self.__zerodirection = zerodirection
	def delZerodirection(self): self.__zerodirection = None
	# Properties
	zerodirection = property(getZerodirection, setZerodirection, delZerodirection, "Property for zerodirection")
	def getXSCalibration(self): return self.__XSCalibration
	def setXSCalibration(self, XSCalibration):
		checkType("XSCalibratedDisplacementAxis", "setXSCalibration", XSCalibration, "XSCalibration")
		self.__XSCalibration = XSCalibration
	def delXSCalibration(self): self.__XSCalibration = None
	# Properties
	XSCalibration = property(getXSCalibration, setXSCalibration, delXSCalibration, "Property for XSCalibration")
	def export(self, outfile, level, name_='XSCalibratedDisplacementAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSCalibratedDisplacementAxis'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__zerodirection is not None:
			self.zerodirection.export(outfile, level, name_='zerodirection')
		else:
			warnEmptyAttribute("zerodirection", "XSDataUnitVector")
		if self.__XSCalibration is not None:
			self.XSCalibration.export(outfile, level, name_='XSCalibration')
		else:
			warnEmptyAttribute("XSCalibration", "XSCalibration")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'zerodirection':
			obj_ = XSDataUnitVector()
			obj_.build(child_)
			self.setZerodirection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSCalibration':
			obj_ = XSCalibration()
			obj_.build(child_)
			self.setXSCalibration(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSCalibratedDisplacementAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSCalibratedDisplacementAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSCalibratedDisplacementAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSCalibratedDisplacementAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSCalibratedDisplacementAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSCalibratedDisplacementAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSCalibratedDisplacementAxis

class XSDataCollection(XSData):
	def __init__(self, XSSubWedge=None, imagelocation=None):
		XSData.__init__(self, )
		self.__imagelocation = imagelocation
		if XSSubWedge is None:
			self.__XSSubWedge = []
		else:
			self.__XSSubWedge = XSSubWedge
	def getImagelocation(self): return self.__imagelocation
	def setImagelocation(self, imagelocation):
		checkType("XSDataCollection", "setImagelocation", imagelocation, "XSDataString")
		self.__imagelocation = imagelocation
	def delImagelocation(self): self.__imagelocation = None
	# Properties
	imagelocation = property(getImagelocation, setImagelocation, delImagelocation, "Property for imagelocation")
	def getXSSubWedge(self): return self.__XSSubWedge
	def setXSSubWedge(self, XSSubWedge):
		checkType("XSDataCollection", "setXSSubWedge", XSSubWedge, "list")
		self.__XSSubWedge = XSSubWedge
	def delXSSubWedge(self): self.__XSSubWedge = None
	# Properties
	XSSubWedge = property(getXSSubWedge, setXSSubWedge, delXSSubWedge, "Property for XSSubWedge")
	def addXSSubWedge(self, value):
		checkType("XSDataCollection", "setXSSubWedge", value, "XSSubWedge")
		self.__XSSubWedge.append(value)
	def insertXSSubWedge(self, index, value):
		checkType("XSDataCollection", "setXSSubWedge", value, "XSSubWedge")
		self.__XSSubWedge[index] = value
	def export(self, outfile, level, name_='XSDataCollection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataCollection'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__imagelocation is not None:
			self.imagelocation.export(outfile, level, name_='imagelocation')
		else:
			warnEmptyAttribute("imagelocation", "XSDataString")
		for XSSubWedge_ in self.getXSSubWedge():
			XSSubWedge_.export(outfile, level, name_='XSSubWedge')
		if self.getXSSubWedge() == []:
			warnEmptyAttribute("XSSubWedge", "XSSubWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagelocation':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImagelocation(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSSubWedge':
			obj_ = XSSubWedge()
			obj_.build(child_)
			self.XSSubWedge.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataCollection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataCollection' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataCollection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataCollection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataCollection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataCollection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataCollection

class XSDataSpaceGroupType(XSData):
	def __init__(self, iucrstandardsymbol=None, iucrnumber=None):
		XSData.__init__(self, )
		self.__iucrnumber = iucrnumber
		self.__iucrstandardsymbol = iucrstandardsymbol
	def getIucrnumber(self): return self.__iucrnumber
	def setIucrnumber(self, iucrnumber):
		checkType("XSDataSpaceGroupType", "setIucrnumber", iucrnumber, "XSDataInteger")
		self.__iucrnumber = iucrnumber
	def delIucrnumber(self): self.__iucrnumber = None
	# Properties
	iucrnumber = property(getIucrnumber, setIucrnumber, delIucrnumber, "Property for iucrnumber")
	def getIucrstandardsymbol(self): return self.__iucrstandardsymbol
	def setIucrstandardsymbol(self, iucrstandardsymbol):
		checkType("XSDataSpaceGroupType", "setIucrstandardsymbol", iucrstandardsymbol, "XSDataString")
		self.__iucrstandardsymbol = iucrstandardsymbol
	def delIucrstandardsymbol(self): self.__iucrstandardsymbol = None
	# Properties
	iucrstandardsymbol = property(getIucrstandardsymbol, setIucrstandardsymbol, delIucrstandardsymbol, "Property for iucrstandardsymbol")
	def export(self, outfile, level, name_='XSDataSpaceGroupType'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSpaceGroupType'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__iucrnumber is not None:
			self.iucrnumber.export(outfile, level, name_='iucrnumber')
		else:
			warnEmptyAttribute("iucrnumber", "XSDataInteger")
		if self.__iucrstandardsymbol is not None:
			self.iucrstandardsymbol.export(outfile, level, name_='iucrstandardsymbol')
		else:
			warnEmptyAttribute("iucrstandardsymbol", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iucrnumber':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIucrnumber(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iucrstandardsymbol':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setIucrstandardsymbol(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataSpaceGroupType" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataSpaceGroupType' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataSpaceGroupType.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSpaceGroupType()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataSpaceGroupType" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSpaceGroupType()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataSpaceGroupType

class XSDataUnitCell(XSData):
	def __init__(self, edgelengths=None, angles=None):
		XSData.__init__(self, )
		if angles is None:
			self.__angles = []
		else:
			self.__angles = angles
		if edgelengths is None:
			self.__edgelengths = []
		else:
			self.__edgelengths = edgelengths
	def getAngles(self): return self.__angles
	def setAngles(self, angles):
		checkType("XSDataUnitCell", "setAngles", angles, "list")
		self.__angles = angles
	def delAngles(self): self.__angles = None
	# Properties
	angles = property(getAngles, setAngles, delAngles, "Property for angles")
	def addAngles(self, value):
		checkType("XSDataUnitCell", "setAngles", value, "XSDataAngle")
		self.__angles.append(value)
	def insertAngles(self, index, value):
		checkType("XSDataUnitCell", "setAngles", value, "XSDataAngle")
		self.__angles[index] = value
	def getEdgelengths(self): return self.__edgelengths
	def setEdgelengths(self, edgelengths):
		checkType("XSDataUnitCell", "setEdgelengths", edgelengths, "list")
		self.__edgelengths = edgelengths
	def delEdgelengths(self): self.__edgelengths = None
	# Properties
	edgelengths = property(getEdgelengths, setEdgelengths, delEdgelengths, "Property for edgelengths")
	def addEdgelengths(self, value):
		checkType("XSDataUnitCell", "setEdgelengths", value, "XSDataLength")
		self.__edgelengths.append(value)
	def insertEdgelengths(self, index, value):
		checkType("XSDataUnitCell", "setEdgelengths", value, "XSDataLength")
		self.__edgelengths[index] = value
	def export(self, outfile, level, name_='XSDataUnitCell'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataUnitCell'):
		XSData.exportChildren(self, outfile, level, name_)
		for angles_ in self.getAngles():
			angles_.export(outfile, level, name_='angles')
		if self.getAngles() == []:
			warnEmptyAttribute("angles", "XSDataAngle")
		for edgelengths_ in self.getEdgelengths():
			edgelengths_.export(outfile, level, name_='edgelengths')
		if self.getEdgelengths() == []:
			warnEmptyAttribute("edgelengths", "XSDataLength")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angles':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.angles.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'edgelengths':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.edgelengths.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataUnitCell" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataUnitCell' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataUnitCell.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataUnitCell()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataUnitCell" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataUnitCell()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataUnitCell

class XSDataLattice(XSData):
	def __init__(self, representativespacegroup=None, unitcell=None):
		XSData.__init__(self, )
		self.__unitcell = unitcell
		self.__representativespacegroup = representativespacegroup
	def getUnitcell(self): return self.__unitcell
	def setUnitcell(self, unitcell):
		checkType("XSDataLattice", "setUnitcell", unitcell, "XSDataUnitCell")
		self.__unitcell = unitcell
	def delUnitcell(self): self.__unitcell = None
	# Properties
	unitcell = property(getUnitcell, setUnitcell, delUnitcell, "Property for unitcell")
	def getRepresentativespacegroup(self): return self.__representativespacegroup
	def setRepresentativespacegroup(self, representativespacegroup):
		checkType("XSDataLattice", "setRepresentativespacegroup", representativespacegroup, "XSDataSpaceGroupType")
		self.__representativespacegroup = representativespacegroup
	def delRepresentativespacegroup(self): self.__representativespacegroup = None
	# Properties
	representativespacegroup = property(getRepresentativespacegroup, setRepresentativespacegroup, delRepresentativespacegroup, "Property for representativespacegroup")
	def export(self, outfile, level, name_='XSDataLattice'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataLattice'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__unitcell is not None:
			self.unitcell.export(outfile, level, name_='unitcell')
		else:
			warnEmptyAttribute("unitcell", "XSDataUnitCell")
		if self.__representativespacegroup is not None:
			self.representativespacegroup.export(outfile, level, name_='representativespacegroup')
		else:
			warnEmptyAttribute("representativespacegroup", "XSDataSpaceGroupType")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unitcell':
			obj_ = XSDataUnitCell()
			obj_.build(child_)
			self.setUnitcell(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'representativespacegroup':
			obj_ = XSDataSpaceGroupType()
			obj_.build(child_)
			self.setRepresentativespacegroup(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataLattice" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataLattice' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataLattice.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataLattice()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataLattice" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataLattice()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataLattice

class XSDetectorFaceAxisDirection(XSData):
	def __init__(self, direction=None):
		XSData.__init__(self, )
		self.__direction = direction
	def getDirection(self): return self.__direction
	def setDirection(self, direction):
		checkType("XSDetectorFaceAxisDirection", "setDirection", direction, "XSDataUnitVector")
		self.__direction = direction
	def delDirection(self): self.__direction = None
	# Properties
	direction = property(getDirection, setDirection, delDirection, "Property for direction")
	def export(self, outfile, level, name_='XSDetectorFaceAxisDirection'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorFaceAxisDirection'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__direction is not None:
			self.direction.export(outfile, level, name_='direction')
		else:
			warnEmptyAttribute("direction", "XSDataUnitVector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direction':
			obj_ = XSDataUnitVector()
			obj_.build(child_)
			self.setDirection(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorFaceAxisDirection" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorFaceAxisDirection' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorFaceAxisDirection.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceAxisDirection()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorFaceAxisDirection" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceAxisDirection()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorFaceAxisDirection

class XSDetectorFaceAxis(XSData):
	def __init__(self, XSDetectorFaceAxisDirection=None, numberofpixels=None, pixelsize=None, name=None):
		XSData.__init__(self, )
		self.__name = name
		self.__pixelsize = pixelsize
		self.__numberofpixels = numberofpixels
		if XSDetectorFaceAxisDirection is None:
			self.__XSDetectorFaceAxisDirection = []
		else:
			self.__XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
	def getName(self): return self.__name
	def setName(self, name):
		checkType("XSDetectorFaceAxis", "setName", name, "XSDataString")
		self.__name = name
	def delName(self): self.__name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getPixelsize(self): return self.__pixelsize
	def setPixelsize(self, pixelsize):
		checkType("XSDetectorFaceAxis", "setPixelsize", pixelsize, "XSDataDouble")
		self.__pixelsize = pixelsize
	def delPixelsize(self): self.__pixelsize = None
	# Properties
	pixelsize = property(getPixelsize, setPixelsize, delPixelsize, "Property for pixelsize")
	def getNumberofpixels(self): return self.__numberofpixels
	def setNumberofpixels(self, numberofpixels):
		checkType("XSDetectorFaceAxis", "setNumberofpixels", numberofpixels, "XSDataInteger")
		self.__numberofpixels = numberofpixels
	def delNumberofpixels(self): self.__numberofpixels = None
	# Properties
	numberofpixels = property(getNumberofpixels, setNumberofpixels, delNumberofpixels, "Property for numberofpixels")
	def getXSDetectorFaceAxisDirection(self): return self.__XSDetectorFaceAxisDirection
	def setXSDetectorFaceAxisDirection(self, XSDetectorFaceAxisDirection):
		checkType("XSDetectorFaceAxis", "setXSDetectorFaceAxisDirection", XSDetectorFaceAxisDirection, "list")
		self.__XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
	def delXSDetectorFaceAxisDirection(self): self.__XSDetectorFaceAxisDirection = None
	# Properties
	XSDetectorFaceAxisDirection = property(getXSDetectorFaceAxisDirection, setXSDetectorFaceAxisDirection, delXSDetectorFaceAxisDirection, "Property for XSDetectorFaceAxisDirection")
	def addXSDetectorFaceAxisDirection(self, value):
		checkType("XSDetectorFaceAxis", "setXSDetectorFaceAxisDirection", value, "XSDetectorFaceAxisDirection")
		self.__XSDetectorFaceAxisDirection.append(value)
	def insertXSDetectorFaceAxisDirection(self, index, value):
		checkType("XSDetectorFaceAxis", "setXSDetectorFaceAxisDirection", value, "XSDetectorFaceAxisDirection")
		self.__XSDetectorFaceAxisDirection[index] = value
	def export(self, outfile, level, name_='XSDetectorFaceAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorFaceAxis'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__name is not None:
			self.name.export(outfile, level, name_='name')
		else:
			warnEmptyAttribute("name", "XSDataString")
		if self.__pixelsize is not None:
			self.pixelsize.export(outfile, level, name_='pixelsize')
		else:
			warnEmptyAttribute("pixelsize", "XSDataDouble")
		if self.__numberofpixels is not None:
			self.numberofpixels.export(outfile, level, name_='numberofpixels')
		else:
			warnEmptyAttribute("numberofpixels", "XSDataInteger")
		for XSDetectorFaceAxisDirection_ in self.getXSDetectorFaceAxisDirection():
			XSDetectorFaceAxisDirection_.export(outfile, level, name_='XSDetectorFaceAxisDirection')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pixelsize':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPixelsize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberofpixels':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberofpixels(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetectorFaceAxisDirection':
			obj_ = XSDetectorFaceAxisDirection()
			obj_.build(child_)
			self.XSDetectorFaceAxisDirection.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorFaceAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorFaceAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorFaceAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorFaceAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorFaceAxis

class XSDetectorFaceSetting(XSData):
	def __init__(self, XSDetectorFaceAxisDirection=None, detectoraxesorigin=None):
		XSData.__init__(self, )
		self.__detectoraxesorigin = detectoraxesorigin
		if XSDetectorFaceAxisDirection is None:
			self.__XSDetectorFaceAxisDirection = []
		else:
			self.__XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
	def getDetectoraxesorigin(self): return self.__detectoraxesorigin
	def setDetectoraxesorigin(self, detectoraxesorigin):
		checkType("XSDetectorFaceSetting", "setDetectoraxesorigin", detectoraxesorigin, "XSDataVectorDouble")
		self.__detectoraxesorigin = detectoraxesorigin
	def delDetectoraxesorigin(self): self.__detectoraxesorigin = None
	# Properties
	detectoraxesorigin = property(getDetectoraxesorigin, setDetectoraxesorigin, delDetectoraxesorigin, "Property for detectoraxesorigin")
	def getXSDetectorFaceAxisDirection(self): return self.__XSDetectorFaceAxisDirection
	def setXSDetectorFaceAxisDirection(self, XSDetectorFaceAxisDirection):
		checkType("XSDetectorFaceSetting", "setXSDetectorFaceAxisDirection", XSDetectorFaceAxisDirection, "list")
		self.__XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
	def delXSDetectorFaceAxisDirection(self): self.__XSDetectorFaceAxisDirection = None
	# Properties
	XSDetectorFaceAxisDirection = property(getXSDetectorFaceAxisDirection, setXSDetectorFaceAxisDirection, delXSDetectorFaceAxisDirection, "Property for XSDetectorFaceAxisDirection")
	def addXSDetectorFaceAxisDirection(self, value):
		checkType("XSDetectorFaceSetting", "setXSDetectorFaceAxisDirection", value, "XSDetectorFaceAxisDirection")
		self.__XSDetectorFaceAxisDirection.append(value)
	def insertXSDetectorFaceAxisDirection(self, index, value):
		checkType("XSDetectorFaceSetting", "setXSDetectorFaceAxisDirection", value, "XSDetectorFaceAxisDirection")
		self.__XSDetectorFaceAxisDirection[index] = value
	def export(self, outfile, level, name_='XSDetectorFaceSetting'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorFaceSetting'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__detectoraxesorigin is not None:
			self.detectoraxesorigin.export(outfile, level, name_='detectoraxesorigin')
		else:
			warnEmptyAttribute("detectoraxesorigin", "XSDataVectorDouble")
		for XSDetectorFaceAxisDirection_ in self.getXSDetectorFaceAxisDirection():
			XSDetectorFaceAxisDirection_.export(outfile, level, name_='XSDetectorFaceAxisDirection')
		if self.getXSDetectorFaceAxisDirection() == []:
			warnEmptyAttribute("XSDetectorFaceAxisDirection", "XSDetectorFaceAxisDirection")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectoraxesorigin':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setDetectoraxesorigin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetectorFaceAxisDirection':
			obj_ = XSDetectorFaceAxisDirection()
			obj_.build(child_)
			self.XSDetectorFaceAxisDirection.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorFaceSetting" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorFaceSetting' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorFaceSetting.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceSetting()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorFaceSetting" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorFaceSetting()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorFaceSetting

class XSDetectorImageProperties(XSData):
	def __init__(self, format=None, headersizevariable=None, headersize=None, mode=None):
		XSData.__init__(self, )
		self.__mode = mode
		self.__headersize = headersize
		self.__headersizevariable = headersizevariable
		self.__format = format
	def getMode(self): return self.__mode
	def setMode(self, mode):
		checkType("XSDetectorImageProperties", "setMode", mode, "XSDataString")
		self.__mode = mode
	def delMode(self): self.__mode = None
	# Properties
	mode = property(getMode, setMode, delMode, "Property for mode")
	def getHeadersize(self): return self.__headersize
	def setHeadersize(self, headersize):
		checkType("XSDetectorImageProperties", "setHeadersize", headersize, "XSDataInteger")
		self.__headersize = headersize
	def delHeadersize(self): self.__headersize = None
	# Properties
	headersize = property(getHeadersize, setHeadersize, delHeadersize, "Property for headersize")
	def getHeadersizevariable(self): return self.__headersizevariable
	def setHeadersizevariable(self, headersizevariable):
		checkType("XSDetectorImageProperties", "setHeadersizevariable", headersizevariable, "XSDataBoolean")
		self.__headersizevariable = headersizevariable
	def delHeadersizevariable(self): self.__headersizevariable = None
	# Properties
	headersizevariable = property(getHeadersizevariable, setHeadersizevariable, delHeadersizevariable, "Property for headersizevariable")
	def getFormat(self): return self.__format
	def setFormat(self, format):
		checkType("XSDetectorImageProperties", "setFormat", format, "XSDataString")
		self.__format = format
	def delFormat(self): self.__format = None
	# Properties
	format = property(getFormat, setFormat, delFormat, "Property for format")
	def export(self, outfile, level, name_='XSDetectorImageProperties'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorImageProperties'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__mode is not None:
			self.mode.export(outfile, level, name_='mode')
		else:
			warnEmptyAttribute("mode", "XSDataString")
		if self.__headersize is not None:
			self.headersize.export(outfile, level, name_='headersize')
		else:
			warnEmptyAttribute("headersize", "XSDataInteger")
		if self.__headersizevariable is not None:
			self.headersizevariable.export(outfile, level, name_='headersizevariable')
		else:
			warnEmptyAttribute("headersizevariable", "XSDataBoolean")
		if self.__format is not None:
			self.format.export(outfile, level, name_='format')
		else:
			warnEmptyAttribute("format", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'headersize':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setHeadersize(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'headersizevariable':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setHeadersizevariable(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'format':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFormat(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorImageProperties" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorImageProperties' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorImageProperties.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorImageProperties()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorImageProperties" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorImageProperties()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorImageProperties

class XSDiffractionImages(XSData):
	def __init__(self, filename=None):
		XSData.__init__(self, )
		self.__filename = filename
	def getFilename(self): return self.__filename
	def setFilename(self, filename):
		checkType("XSDiffractionImages", "setFilename", filename, "XSDataString")
		self.__filename = filename
	def delFilename(self): self.__filename = None
	# Properties
	filename = property(getFilename, setFilename, delFilename, "Property for filename")
	def export(self, outfile, level, name_='XSDiffractionImages'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDiffractionImages'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__filename is not None:
			self.filename.export(outfile, level, name_='filename')
		else:
			warnEmptyAttribute("filename", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'filename':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setFilename(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDiffractionImages" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDiffractionImages' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDiffractionImages.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDiffractionImages()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDiffractionImages" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDiffractionImages()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDiffractionImages

class XSDisplacementAxis(XSData):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
		XSData.__init__(self, )
		self.__name = name
		if XSCalibratedDisplacementAxis is None:
			self.__XSCalibratedDisplacementAxis = []
		else:
			self.__XSCalibratedDisplacementAxis = XSCalibratedDisplacementAxis
	def getName(self): return self.__name
	def setName(self, name):
		checkType("XSDisplacementAxis", "setName", name, "XSDataString")
		self.__name = name
	def delName(self): self.__name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getXSCalibratedDisplacementAxis(self): return self.__XSCalibratedDisplacementAxis
	def setXSCalibratedDisplacementAxis(self, XSCalibratedDisplacementAxis):
		checkType("XSDisplacementAxis", "setXSCalibratedDisplacementAxis", XSCalibratedDisplacementAxis, "list")
		self.__XSCalibratedDisplacementAxis = XSCalibratedDisplacementAxis
	def delXSCalibratedDisplacementAxis(self): self.__XSCalibratedDisplacementAxis = None
	# Properties
	XSCalibratedDisplacementAxis = property(getXSCalibratedDisplacementAxis, setXSCalibratedDisplacementAxis, delXSCalibratedDisplacementAxis, "Property for XSCalibratedDisplacementAxis")
	def addXSCalibratedDisplacementAxis(self, value):
		checkType("XSDisplacementAxis", "setXSCalibratedDisplacementAxis", value, "XSCalibratedDisplacementAxis")
		self.__XSCalibratedDisplacementAxis.append(value)
	def insertXSCalibratedDisplacementAxis(self, index, value):
		checkType("XSDisplacementAxis", "setXSCalibratedDisplacementAxis", value, "XSCalibratedDisplacementAxis")
		self.__XSCalibratedDisplacementAxis[index] = value
	def export(self, outfile, level, name_='XSDisplacementAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDisplacementAxis'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__name is not None:
			self.name.export(outfile, level, name_='name')
		else:
			warnEmptyAttribute("name", "XSDataString")
		for XSCalibratedDisplacementAxis_ in self.getXSCalibratedDisplacementAxis():
			XSCalibratedDisplacementAxis_.export(outfile, level, name_='XSCalibratedDisplacementAxis')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSCalibratedDisplacementAxis':
			obj_ = XSCalibratedDisplacementAxis()
			obj_.build(child_)
			self.XSCalibratedDisplacementAxis.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDisplacementAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDisplacementAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDisplacementAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDisplacementAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDisplacementAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDisplacementAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDisplacementAxis

class XSDisplacementList(XSData):
	def __init__(self, ):
		XSData.__init__(self, )
	def export(self, outfile, level, name_='XSDisplacementList'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDisplacementList'):
		XSData.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDisplacementList" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDisplacementList' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDisplacementList.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDisplacementList()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDisplacementList" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDisplacementList()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDisplacementList

class XSDisplacementListSetting(XSData):
	def __init__(self, ):
		XSData.__init__(self, )
	def export(self, outfile, level, name_='XSDisplacementListSetting'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDisplacementListSetting'):
		XSData.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDisplacementListSetting" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDisplacementListSetting' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDisplacementListSetting.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDisplacementListSetting()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDisplacementListSetting" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDisplacementListSetting()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDisplacementListSetting

class XSFoundSpot(XSData):
	def __init__(self, intensityesu=None, intensity=None, omega=None, detectorposition=None):
		XSData.__init__(self, )
		if detectorposition is None:
			self.__detectorposition = []
		else:
			self.__detectorposition = detectorposition
		self.__omega = omega
		self.__intensity = intensity
		self.__intensityesu = intensityesu
	def getDetectorposition(self): return self.__detectorposition
	def setDetectorposition(self, detectorposition):
		checkType("XSFoundSpot", "setDetectorposition", detectorposition, "list")
		self.__detectorposition = detectorposition
	def delDetectorposition(self): self.__detectorposition = None
	# Properties
	detectorposition = property(getDetectorposition, setDetectorposition, delDetectorposition, "Property for detectorposition")
	def addDetectorposition(self, value):
		checkType("XSFoundSpot", "setDetectorposition", value, "XSDataDouble")
		self.__detectorposition.append(value)
	def insertDetectorposition(self, index, value):
		checkType("XSFoundSpot", "setDetectorposition", value, "XSDataDouble")
		self.__detectorposition[index] = value
	def getOmega(self): return self.__omega
	def setOmega(self, omega):
		checkType("XSFoundSpot", "setOmega", omega, "XSDataAngle")
		self.__omega = omega
	def delOmega(self): self.__omega = None
	# Properties
	omega = property(getOmega, setOmega, delOmega, "Property for omega")
	def getIntensity(self): return self.__intensity
	def setIntensity(self, intensity):
		checkType("XSFoundSpot", "setIntensity", intensity, "XSDataDouble")
		self.__intensity = intensity
	def delIntensity(self): self.__intensity = None
	# Properties
	intensity = property(getIntensity, setIntensity, delIntensity, "Property for intensity")
	def getIntensityesu(self): return self.__intensityesu
	def setIntensityesu(self, intensityesu):
		checkType("XSFoundSpot", "setIntensityesu", intensityesu, "XSDataDouble")
		self.__intensityesu = intensityesu
	def delIntensityesu(self): self.__intensityesu = None
	# Properties
	intensityesu = property(getIntensityesu, setIntensityesu, delIntensityesu, "Property for intensityesu")
	def export(self, outfile, level, name_='XSFoundSpot'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSFoundSpot'):
		XSData.exportChildren(self, outfile, level, name_)
		for detectorposition_ in self.getDetectorposition():
			detectorposition_.export(outfile, level, name_='detectorposition')
		if self.getDetectorposition() == []:
			warnEmptyAttribute("detectorposition", "XSDataDouble")
		if self.__omega is not None:
			self.omega.export(outfile, level, name_='omega')
		else:
			warnEmptyAttribute("omega", "XSDataAngle")
		if self.__intensity is not None:
			self.intensity.export(outfile, level, name_='intensity')
		else:
			warnEmptyAttribute("intensity", "XSDataDouble")
		if self.__intensityesu is not None:
			self.intensityesu.export(outfile, level, name_='intensityesu')
		else:
			warnEmptyAttribute("intensityesu", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detectorposition':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.detectorposition.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omega':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setOmega(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'intensity':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIntensity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'intensityesu':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setIntensityesu(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSFoundSpot" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSFoundSpot' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSFoundSpot.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSFoundSpot()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSFoundSpot" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSFoundSpot()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSFoundSpot

class XSImageRange(XSData):
	def __init__(self, XSProcessingWedge=None, endimage=None, startimage=None):
		XSData.__init__(self, )
		self.__startimage = startimage
		self.__endimage = endimage
		self.__XSProcessingWedge = XSProcessingWedge
	def getStartimage(self): return self.__startimage
	def setStartimage(self, startimage):
		checkType("XSImageRange", "setStartimage", startimage, "XSDataInteger")
		self.__startimage = startimage
	def delStartimage(self): self.__startimage = None
	# Properties
	startimage = property(getStartimage, setStartimage, delStartimage, "Property for startimage")
	def getEndimage(self): return self.__endimage
	def setEndimage(self, endimage):
		checkType("XSImageRange", "setEndimage", endimage, "XSDataInteger")
		self.__endimage = endimage
	def delEndimage(self): self.__endimage = None
	# Properties
	endimage = property(getEndimage, setEndimage, delEndimage, "Property for endimage")
	def getXSProcessingWedge(self): return self.__XSProcessingWedge
	def setXSProcessingWedge(self, XSProcessingWedge):
		checkType("XSImageRange", "setXSProcessingWedge", XSProcessingWedge, "XSProcessingWedge")
		self.__XSProcessingWedge = XSProcessingWedge
	def delXSProcessingWedge(self): self.__XSProcessingWedge = None
	# Properties
	XSProcessingWedge = property(getXSProcessingWedge, setXSProcessingWedge, delXSProcessingWedge, "Property for XSProcessingWedge")
	def export(self, outfile, level, name_='XSImageRange'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSImageRange'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__startimage is not None:
			self.startimage.export(outfile, level, name_='startimage')
		else:
			warnEmptyAttribute("startimage", "XSDataInteger")
		if self.__endimage is not None:
			self.endimage.export(outfile, level, name_='endimage')
		else:
			warnEmptyAttribute("endimage", "XSDataInteger")
		if self.__XSProcessingWedge is not None:
			self.XSProcessingWedge.export(outfile, level, name_='XSProcessingWedge')
		else:
			warnEmptyAttribute("XSProcessingWedge", "XSProcessingWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'startimage':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setStartimage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'endimage':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setEndimage(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSProcessingWedge':
			obj_ = XSProcessingWedge()
			obj_.build(child_)
			self.setXSProcessingWedge(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSImageRange" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSImageRange' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSImageRange.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSImageRange()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSImageRange" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSImageRange()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSImageRange

class XSIndexingInput(XSData):
	def __init__(self, XSIndexingResult=None, XSSpotSearchOutput=None):
		XSData.__init__(self, )
		if XSSpotSearchOutput is None:
			self.__XSSpotSearchOutput = []
		else:
			self.__XSSpotSearchOutput = XSSpotSearchOutput
		if XSIndexingResult is None:
			self.__XSIndexingResult = []
		else:
			self.__XSIndexingResult = XSIndexingResult
	def getXSSpotSearchOutput(self): return self.__XSSpotSearchOutput
	def setXSSpotSearchOutput(self, XSSpotSearchOutput):
		checkType("XSIndexingInput", "setXSSpotSearchOutput", XSSpotSearchOutput, "list")
		self.__XSSpotSearchOutput = XSSpotSearchOutput
	def delXSSpotSearchOutput(self): self.__XSSpotSearchOutput = None
	# Properties
	XSSpotSearchOutput = property(getXSSpotSearchOutput, setXSSpotSearchOutput, delXSSpotSearchOutput, "Property for XSSpotSearchOutput")
	def addXSSpotSearchOutput(self, value):
		checkType("XSIndexingInput", "setXSSpotSearchOutput", value, "XSSpotSearchOutput")
		self.__XSSpotSearchOutput.append(value)
	def insertXSSpotSearchOutput(self, index, value):
		checkType("XSIndexingInput", "setXSSpotSearchOutput", value, "XSSpotSearchOutput")
		self.__XSSpotSearchOutput[index] = value
	def getXSIndexingResult(self): return self.__XSIndexingResult
	def setXSIndexingResult(self, XSIndexingResult):
		checkType("XSIndexingInput", "setXSIndexingResult", XSIndexingResult, "list")
		self.__XSIndexingResult = XSIndexingResult
	def delXSIndexingResult(self): self.__XSIndexingResult = None
	# Properties
	XSIndexingResult = property(getXSIndexingResult, setXSIndexingResult, delXSIndexingResult, "Property for XSIndexingResult")
	def addXSIndexingResult(self, value):
		checkType("XSIndexingInput", "setXSIndexingResult", value, "XSIndexingResult")
		self.__XSIndexingResult.append(value)
	def insertXSIndexingResult(self, index, value):
		checkType("XSIndexingInput", "setXSIndexingResult", value, "XSIndexingResult")
		self.__XSIndexingResult[index] = value
	def export(self, outfile, level, name_='XSIndexingInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSIndexingInput'):
		XSData.exportChildren(self, outfile, level, name_)
		for XSSpotSearchOutput_ in self.getXSSpotSearchOutput():
			XSSpotSearchOutput_.export(outfile, level, name_='XSSpotSearchOutput')
		if self.getXSSpotSearchOutput() == []:
			warnEmptyAttribute("XSSpotSearchOutput", "XSSpotSearchOutput")
		for XSIndexingResult_ in self.getXSIndexingResult():
			XSIndexingResult_.export(outfile, level, name_='XSIndexingResult')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSSpotSearchOutput':
			obj_ = XSSpotSearchOutput()
			obj_.build(child_)
			self.XSSpotSearchOutput.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSIndexingResult':
			obj_ = XSIndexingResult()
			obj_.build(child_)
			self.XSIndexingResult.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSIndexingInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSIndexingInput' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSIndexingInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSIndexingInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSIndexingInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSIndexingInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSIndexingInput

class XSIndexingOutput(XSData):
	def __init__(self, XSWedge=None, refinedaxisdirection=None, statistics=None):
		XSData.__init__(self, )
		self.__statistics = statistics
		self.__refinedaxisdirection = refinedaxisdirection
		self.__XSWedge = XSWedge
	def getStatistics(self): return self.__statistics
	def setStatistics(self, statistics):
		checkType("XSIndexingOutput", "setStatistics", statistics, "XSStatisticsIndexing")
		self.__statistics = statistics
	def delStatistics(self): self.__statistics = None
	# Properties
	statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
	def getRefinedaxisdirection(self): return self.__refinedaxisdirection
	def setRefinedaxisdirection(self, refinedaxisdirection):
		checkType("XSIndexingOutput", "setRefinedaxisdirection", refinedaxisdirection, "XSDataUnitVector")
		self.__refinedaxisdirection = refinedaxisdirection
	def delRefinedaxisdirection(self): self.__refinedaxisdirection = None
	# Properties
	refinedaxisdirection = property(getRefinedaxisdirection, setRefinedaxisdirection, delRefinedaxisdirection, "Property for refinedaxisdirection")
	def getXSWedge(self): return self.__XSWedge
	def setXSWedge(self, XSWedge):
		checkType("XSIndexingOutput", "setXSWedge", XSWedge, "XSWedge")
		self.__XSWedge = XSWedge
	def delXSWedge(self): self.__XSWedge = None
	# Properties
	XSWedge = property(getXSWedge, setXSWedge, delXSWedge, "Property for XSWedge")
	def export(self, outfile, level, name_='XSIndexingOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSIndexingOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__statistics is not None:
			self.statistics.export(outfile, level, name_='statistics')
		if self.__refinedaxisdirection is not None:
			self.refinedaxisdirection.export(outfile, level, name_='refinedaxisdirection')
		if self.__XSWedge is not None:
			self.XSWedge.export(outfile, level, name_='XSWedge')
		else:
			warnEmptyAttribute("XSWedge", "XSWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statistics':
			obj_ = XSStatisticsIndexing()
			obj_.build(child_)
			self.setStatistics(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refinedaxisdirection':
			obj_ = XSDataUnitVector()
			obj_.build(child_)
			self.setRefinedaxisdirection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSWedge':
			obj_ = XSWedge()
			obj_.build(child_)
			self.setXSWedge(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSIndexingOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSIndexingOutput' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSIndexingOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSIndexingOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSIndexingOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSIndexingOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSIndexingOutput

class XSIndexingSolution(XSData):
	def __init__(self, penalty=None, lattice=None):
		XSData.__init__(self, )
		self.__lattice = lattice
		self.__penalty = penalty
	def getLattice(self): return self.__lattice
	def setLattice(self, lattice):
		checkType("XSIndexingSolution", "setLattice", lattice, "XSDataLattice")
		self.__lattice = lattice
	def delLattice(self): self.__lattice = None
	# Properties
	lattice = property(getLattice, setLattice, delLattice, "Property for lattice")
	def getPenalty(self): return self.__penalty
	def setPenalty(self, penalty):
		checkType("XSIndexingSolution", "setPenalty", penalty, "XSDataDouble")
		self.__penalty = penalty
	def delPenalty(self): self.__penalty = None
	# Properties
	penalty = property(getPenalty, setPenalty, delPenalty, "Property for penalty")
	def export(self, outfile, level, name_='XSIndexingSolution'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSIndexingSolution'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__lattice is not None:
			self.lattice.export(outfile, level, name_='lattice')
		else:
			warnEmptyAttribute("lattice", "XSDataLattice")
		if self.__penalty is not None:
			self.penalty.export(outfile, level, name_='penalty')
		else:
			warnEmptyAttribute("penalty", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lattice':
			obj_ = XSDataLattice()
			obj_.build(child_)
			self.setLattice(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'penalty':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setPenalty(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSIndexingSolution" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSIndexingSolution' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSIndexingSolution.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSIndexingSolution()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSIndexingSolution" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSIndexingSolution()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSIndexingSolution

class XSIndexingResult(XSData):
	def __init__(self, XSIndexingSolution=None, XSIndexingOutput=None, selectedsolution=None):
		XSData.__init__(self, )
		self.__selectedsolution = selectedsolution
		if XSIndexingOutput is None:
			self.__XSIndexingOutput = []
		else:
			self.__XSIndexingOutput = XSIndexingOutput
		if XSIndexingSolution is None:
			self.__XSIndexingSolution = []
		else:
			self.__XSIndexingSolution = XSIndexingSolution
	def getSelectedsolution(self): return self.__selectedsolution
	def setSelectedsolution(self, selectedsolution):
		checkType("XSIndexingResult", "setSelectedsolution", selectedsolution, "XSDataInteger")
		self.__selectedsolution = selectedsolution
	def delSelectedsolution(self): self.__selectedsolution = None
	# Properties
	selectedsolution = property(getSelectedsolution, setSelectedsolution, delSelectedsolution, "Property for selectedsolution")
	def getXSIndexingOutput(self): return self.__XSIndexingOutput
	def setXSIndexingOutput(self, XSIndexingOutput):
		checkType("XSIndexingResult", "setXSIndexingOutput", XSIndexingOutput, "list")
		self.__XSIndexingOutput = XSIndexingOutput
	def delXSIndexingOutput(self): self.__XSIndexingOutput = None
	# Properties
	XSIndexingOutput = property(getXSIndexingOutput, setXSIndexingOutput, delXSIndexingOutput, "Property for XSIndexingOutput")
	def addXSIndexingOutput(self, value):
		checkType("XSIndexingResult", "setXSIndexingOutput", value, "XSIndexingOutput")
		self.__XSIndexingOutput.append(value)
	def insertXSIndexingOutput(self, index, value):
		checkType("XSIndexingResult", "setXSIndexingOutput", value, "XSIndexingOutput")
		self.__XSIndexingOutput[index] = value
	def getXSIndexingSolution(self): return self.__XSIndexingSolution
	def setXSIndexingSolution(self, XSIndexingSolution):
		checkType("XSIndexingResult", "setXSIndexingSolution", XSIndexingSolution, "list")
		self.__XSIndexingSolution = XSIndexingSolution
	def delXSIndexingSolution(self): self.__XSIndexingSolution = None
	# Properties
	XSIndexingSolution = property(getXSIndexingSolution, setXSIndexingSolution, delXSIndexingSolution, "Property for XSIndexingSolution")
	def addXSIndexingSolution(self, value):
		checkType("XSIndexingResult", "setXSIndexingSolution", value, "XSIndexingSolution")
		self.__XSIndexingSolution.append(value)
	def insertXSIndexingSolution(self, index, value):
		checkType("XSIndexingResult", "setXSIndexingSolution", value, "XSIndexingSolution")
		self.__XSIndexingSolution[index] = value
	def export(self, outfile, level, name_='XSIndexingResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSIndexingResult'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__selectedsolution is not None:
			self.selectedsolution.export(outfile, level, name_='selectedsolution')
		else:
			warnEmptyAttribute("selectedsolution", "XSDataInteger")
		for XSIndexingOutput_ in self.getXSIndexingOutput():
			XSIndexingOutput_.export(outfile, level, name_='XSIndexingOutput')
		if self.getXSIndexingOutput() == []:
			warnEmptyAttribute("XSIndexingOutput", "XSIndexingOutput")
		for XSIndexingSolution_ in self.getXSIndexingSolution():
			XSIndexingSolution_.export(outfile, level, name_='XSIndexingSolution')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'selectedsolution':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSelectedsolution(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSIndexingOutput':
			obj_ = XSIndexingOutput()
			obj_.build(child_)
			self.XSIndexingOutput.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSIndexingSolution':
			obj_ = XSIndexingSolution()
			obj_.build(child_)
			self.XSIndexingSolution.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSIndexingResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSIndexingResult' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSIndexingResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSIndexingResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSIndexingResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSIndexingResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSIndexingResult

class XSRotationExposure(XSData):
	def __init__(self, XSGoniostatAxis=None, exposuretime=None, numberimages=None, imagewidth=None):
		XSData.__init__(self, )
		self.__imagewidth = imagewidth
		self.__numberimages = numberimages
		self.__exposuretime = exposuretime
		self.__XSGoniostatAxis = XSGoniostatAxis
	def getImagewidth(self): return self.__imagewidth
	def setImagewidth(self, imagewidth):
		checkType("XSRotationExposure", "setImagewidth", imagewidth, "XSDataAngle")
		self.__imagewidth = imagewidth
	def delImagewidth(self): self.__imagewidth = None
	# Properties
	imagewidth = property(getImagewidth, setImagewidth, delImagewidth, "Property for imagewidth")
	def getNumberimages(self): return self.__numberimages
	def setNumberimages(self, numberimages):
		checkType("XSRotationExposure", "setNumberimages", numberimages, "XSDataInteger")
		self.__numberimages = numberimages
	def delNumberimages(self): self.__numberimages = None
	# Properties
	numberimages = property(getNumberimages, setNumberimages, delNumberimages, "Property for numberimages")
	def getExposuretime(self): return self.__exposuretime
	def setExposuretime(self, exposuretime):
		checkType("XSRotationExposure", "setExposuretime", exposuretime, "XSDataTime")
		self.__exposuretime = exposuretime
	def delExposuretime(self): self.__exposuretime = None
	# Properties
	exposuretime = property(getExposuretime, setExposuretime, delExposuretime, "Property for exposuretime")
	def getXSGoniostatAxis(self): return self.__XSGoniostatAxis
	def setXSGoniostatAxis(self, XSGoniostatAxis):
		checkType("XSRotationExposure", "setXSGoniostatAxis", XSGoniostatAxis, "XSGoniostatAxis")
		self.__XSGoniostatAxis = XSGoniostatAxis
	def delXSGoniostatAxis(self): self.__XSGoniostatAxis = None
	# Properties
	XSGoniostatAxis = property(getXSGoniostatAxis, setXSGoniostatAxis, delXSGoniostatAxis, "Property for XSGoniostatAxis")
	def export(self, outfile, level, name_='XSRotationExposure'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSRotationExposure'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__imagewidth is not None:
			self.imagewidth.export(outfile, level, name_='imagewidth')
		else:
			warnEmptyAttribute("imagewidth", "XSDataAngle")
		if self.__numberimages is not None:
			self.numberimages.export(outfile, level, name_='numberimages')
		else:
			warnEmptyAttribute("numberimages", "XSDataInteger")
		if self.__exposuretime is not None:
			self.exposuretime.export(outfile, level, name_='exposuretime')
		else:
			warnEmptyAttribute("exposuretime", "XSDataTime")
		if self.__XSGoniostatAxis is not None:
			self.XSGoniostatAxis.export(outfile, level, name_='XSGoniostatAxis')
		else:
			warnEmptyAttribute("XSGoniostatAxis", "XSGoniostatAxis")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagewidth':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setImagewidth(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'numberimages':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNumberimages(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'exposuretime':
			obj_ = XSDataTime()
			obj_.build(child_)
			self.setExposuretime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSGoniostatAxis':
			obj_ = XSGoniostatAxis()
			obj_.build(child_)
			self.setXSGoniostatAxis(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSRotationExposure" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSRotationExposure' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSRotationExposure.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSRotationExposure()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSRotationExposure" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSRotationExposure()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSRotationExposure

class XSSample(XSData):
	def __init__(self, XSDataCollection=None, identifier=None):
		XSData.__init__(self, )
		self.__identifier = identifier
		if XSDataCollection is None:
			self.__XSDataCollection = []
		else:
			self.__XSDataCollection = XSDataCollection
	def getIdentifier(self): return self.__identifier
	def setIdentifier(self, identifier):
		checkType("XSSample", "setIdentifier", identifier, "XSDataString")
		self.__identifier = identifier
	def delIdentifier(self): self.__identifier = None
	# Properties
	identifier = property(getIdentifier, setIdentifier, delIdentifier, "Property for identifier")
	def getXSDataCollection(self): return self.__XSDataCollection
	def setXSDataCollection(self, XSDataCollection):
		checkType("XSSample", "setXSDataCollection", XSDataCollection, "list")
		self.__XSDataCollection = XSDataCollection
	def delXSDataCollection(self): self.__XSDataCollection = None
	# Properties
	XSDataCollection = property(getXSDataCollection, setXSDataCollection, delXSDataCollection, "Property for XSDataCollection")
	def addXSDataCollection(self, value):
		checkType("XSSample", "setXSDataCollection", value, "XSDataCollection")
		self.__XSDataCollection.append(value)
	def insertXSDataCollection(self, index, value):
		checkType("XSSample", "setXSDataCollection", value, "XSDataCollection")
		self.__XSDataCollection[index] = value
	def export(self, outfile, level, name_='XSSample'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSSample'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__identifier is not None:
			self.identifier.export(outfile, level, name_='identifier')
		else:
			warnEmptyAttribute("identifier", "XSDataString")
		for XSDataCollection_ in self.getXSDataCollection():
			XSDataCollection_.export(outfile, level, name_='XSDataCollection')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'identifier':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setIdentifier(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDataCollection':
			obj_ = XSDataCollection()
			obj_.build(child_)
			self.XSDataCollection.append(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSSample" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSSample' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSSample.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSSample()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSSample" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSSample()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSSample

class XSWedge(XSData):
	def __init__(self, ednaid=None):
		XSData.__init__(self, )
		self.__ednaid = ednaid
	def getEdnaid(self): return self.__ednaid
	def setEdnaid(self, ednaid):
		checkType("XSWedge", "setEdnaid", ednaid, "XSDataString")
		self.__ednaid = ednaid
	def delEdnaid(self): self.__ednaid = None
	# Properties
	ednaid = property(getEdnaid, setEdnaid, delEdnaid, "Property for ednaid")
	def export(self, outfile, level, name_='XSWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__ednaid is not None:
			self.ednaid.export(outfile, level, name_='ednaid')
		else:
			warnEmptyAttribute("ednaid", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ednaid':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setEdnaid(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSWedge' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSWedge

class XSSpotSearchOutput(XSData):
	def __init__(self, XSWedge=None, spots=None):
		XSData.__init__(self, )
		if spots is None:
			self.__spots = []
		else:
			self.__spots = spots
		self.__XSWedge = XSWedge
	def getSpots(self): return self.__spots
	def setSpots(self, spots):
		checkType("XSSpotSearchOutput", "setSpots", spots, "list")
		self.__spots = spots
	def delSpots(self): self.__spots = None
	# Properties
	spots = property(getSpots, setSpots, delSpots, "Property for spots")
	def addSpots(self, value):
		checkType("XSSpotSearchOutput", "setSpots", value, "XSFoundSpot")
		self.__spots.append(value)
	def insertSpots(self, index, value):
		checkType("XSSpotSearchOutput", "setSpots", value, "XSFoundSpot")
		self.__spots[index] = value
	def getXSWedge(self): return self.__XSWedge
	def setXSWedge(self, XSWedge):
		checkType("XSSpotSearchOutput", "setXSWedge", XSWedge, "XSWedge")
		self.__XSWedge = XSWedge
	def delXSWedge(self): self.__XSWedge = None
	# Properties
	XSWedge = property(getXSWedge, setXSWedge, delXSWedge, "Property for XSWedge")
	def export(self, outfile, level, name_='XSSpotSearchOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSSpotSearchOutput'):
		XSData.exportChildren(self, outfile, level, name_)
		for spots_ in self.getSpots():
			spots_.export(outfile, level, name_='spots')
		if self.__XSWedge is not None:
			self.XSWedge.export(outfile, level, name_='XSWedge')
		else:
			warnEmptyAttribute("XSWedge", "XSWedge")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spots':
			obj_ = XSFoundSpot()
			obj_.build(child_)
			self.spots.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSWedge':
			obj_ = XSWedge()
			obj_.build(child_)
			self.setXSWedge(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSSpotSearchOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSSpotSearchOutput' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSSpotSearchOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSSpotSearchOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSSpotSearchOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSSpotSearchOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSSpotSearchOutput

class XSStatisticsIndexing(XSData):
	def __init__(self, spotsused=None, spotstotal=None, spotdeviationpositional=None, spotdeviationangular=None):
		XSData.__init__(self, )
		self.__spotdeviationangular = spotdeviationangular
		self.__spotdeviationpositional = spotdeviationpositional
		self.__spotstotal = spotstotal
		self.__spotsused = spotsused
	def getSpotdeviationangular(self): return self.__spotdeviationangular
	def setSpotdeviationangular(self, spotdeviationangular):
		checkType("XSStatisticsIndexing", "setSpotdeviationangular", spotdeviationangular, "XSDataAngle")
		self.__spotdeviationangular = spotdeviationangular
	def delSpotdeviationangular(self): self.__spotdeviationangular = None
	# Properties
	spotdeviationangular = property(getSpotdeviationangular, setSpotdeviationangular, delSpotdeviationangular, "Property for spotdeviationangular")
	def getSpotdeviationpositional(self): return self.__spotdeviationpositional
	def setSpotdeviationpositional(self, spotdeviationpositional):
		checkType("XSStatisticsIndexing", "setSpotdeviationpositional", spotdeviationpositional, "XSDataLength")
		self.__spotdeviationpositional = spotdeviationpositional
	def delSpotdeviationpositional(self): self.__spotdeviationpositional = None
	# Properties
	spotdeviationpositional = property(getSpotdeviationpositional, setSpotdeviationpositional, delSpotdeviationpositional, "Property for spotdeviationpositional")
	def getSpotstotal(self): return self.__spotstotal
	def setSpotstotal(self, spotstotal):
		checkType("XSStatisticsIndexing", "setSpotstotal", spotstotal, "XSDataInteger")
		self.__spotstotal = spotstotal
	def delSpotstotal(self): self.__spotstotal = None
	# Properties
	spotstotal = property(getSpotstotal, setSpotstotal, delSpotstotal, "Property for spotstotal")
	def getSpotsused(self): return self.__spotsused
	def setSpotsused(self, spotsused):
		checkType("XSStatisticsIndexing", "setSpotsused", spotsused, "XSDataInteger")
		self.__spotsused = spotsused
	def delSpotsused(self): self.__spotsused = None
	# Properties
	spotsused = property(getSpotsused, setSpotsused, delSpotsused, "Property for spotsused")
	def export(self, outfile, level, name_='XSStatisticsIndexing'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSStatisticsIndexing'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__spotdeviationangular is not None:
			self.spotdeviationangular.export(outfile, level, name_='spotdeviationangular')
		else:
			warnEmptyAttribute("spotdeviationangular", "XSDataAngle")
		if self.__spotdeviationpositional is not None:
			self.spotdeviationpositional.export(outfile, level, name_='spotdeviationpositional')
		else:
			warnEmptyAttribute("spotdeviationpositional", "XSDataLength")
		if self.__spotstotal is not None:
			self.spotstotal.export(outfile, level, name_='spotstotal')
		else:
			warnEmptyAttribute("spotstotal", "XSDataInteger")
		if self.__spotsused is not None:
			self.spotsused.export(outfile, level, name_='spotsused')
		else:
			warnEmptyAttribute("spotsused", "XSDataInteger")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotdeviationangular':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setSpotdeviationangular(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotdeviationpositional':
			obj_ = XSDataLength()
			obj_.build(child_)
			self.setSpotdeviationpositional(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotstotal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpotstotal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spotsused':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSpotsused(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSStatisticsIndexing" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSStatisticsIndexing' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSStatisticsIndexing.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSStatisticsIndexing()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSStatisticsIndexing" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSStatisticsIndexing()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSStatisticsIndexing

class XSSubWedge(XSData):
	def __init__(self, XSRotationExposure=None, XSRotationalGoniostatSetting=None, XSImageRange=None, XSDiffractionImages=None, XSDetectorSetting=None, XSCollectionWedge=None, XSBeamSetting=None, imagefilenametemplate=None):
		XSData.__init__(self, )
		self.__imagefilenametemplate = imagefilenametemplate
		self.__XSBeamSetting = XSBeamSetting
		self.__XSCollectionWedge = XSCollectionWedge
		self.__XSDetectorSetting = XSDetectorSetting
		if XSDiffractionImages is None:
			self.__XSDiffractionImages = []
		else:
			self.__XSDiffractionImages = XSDiffractionImages
		if XSImageRange is None:
			self.__XSImageRange = []
		else:
			self.__XSImageRange = XSImageRange
		self.__XSRotationalGoniostatSetting = XSRotationalGoniostatSetting
		self.__XSRotationExposure = XSRotationExposure
	def getImagefilenametemplate(self): return self.__imagefilenametemplate
	def setImagefilenametemplate(self, imagefilenametemplate):
		checkType("XSSubWedge", "setImagefilenametemplate", imagefilenametemplate, "XSDataString")
		self.__imagefilenametemplate = imagefilenametemplate
	def delImagefilenametemplate(self): self.__imagefilenametemplate = None
	# Properties
	imagefilenametemplate = property(getImagefilenametemplate, setImagefilenametemplate, delImagefilenametemplate, "Property for imagefilenametemplate")
	def getXSBeamSetting(self): return self.__XSBeamSetting
	def setXSBeamSetting(self, XSBeamSetting):
		checkType("XSSubWedge", "setXSBeamSetting", XSBeamSetting, "XSBeamSetting")
		self.__XSBeamSetting = XSBeamSetting
	def delXSBeamSetting(self): self.__XSBeamSetting = None
	# Properties
	XSBeamSetting = property(getXSBeamSetting, setXSBeamSetting, delXSBeamSetting, "Property for XSBeamSetting")
	def getXSCollectionWedge(self): return self.__XSCollectionWedge
	def setXSCollectionWedge(self, XSCollectionWedge):
		checkType("XSSubWedge", "setXSCollectionWedge", XSCollectionWedge, "XSCollectionWedge")
		self.__XSCollectionWedge = XSCollectionWedge
	def delXSCollectionWedge(self): self.__XSCollectionWedge = None
	# Properties
	XSCollectionWedge = property(getXSCollectionWedge, setXSCollectionWedge, delXSCollectionWedge, "Property for XSCollectionWedge")
	def getXSDetectorSetting(self): return self.__XSDetectorSetting
	def setXSDetectorSetting(self, XSDetectorSetting):
		checkType("XSSubWedge", "setXSDetectorSetting", XSDetectorSetting, "XSDetectorSetting")
		self.__XSDetectorSetting = XSDetectorSetting
	def delXSDetectorSetting(self): self.__XSDetectorSetting = None
	# Properties
	XSDetectorSetting = property(getXSDetectorSetting, setXSDetectorSetting, delXSDetectorSetting, "Property for XSDetectorSetting")
	def getXSDiffractionImages(self): return self.__XSDiffractionImages
	def setXSDiffractionImages(self, XSDiffractionImages):
		checkType("XSSubWedge", "setXSDiffractionImages", XSDiffractionImages, "list")
		self.__XSDiffractionImages = XSDiffractionImages
	def delXSDiffractionImages(self): self.__XSDiffractionImages = None
	# Properties
	XSDiffractionImages = property(getXSDiffractionImages, setXSDiffractionImages, delXSDiffractionImages, "Property for XSDiffractionImages")
	def addXSDiffractionImages(self, value):
		checkType("XSSubWedge", "setXSDiffractionImages", value, "XSDiffractionImages")
		self.__XSDiffractionImages.append(value)
	def insertXSDiffractionImages(self, index, value):
		checkType("XSSubWedge", "setXSDiffractionImages", value, "XSDiffractionImages")
		self.__XSDiffractionImages[index] = value
	def getXSImageRange(self): return self.__XSImageRange
	def setXSImageRange(self, XSImageRange):
		checkType("XSSubWedge", "setXSImageRange", XSImageRange, "list")
		self.__XSImageRange = XSImageRange
	def delXSImageRange(self): self.__XSImageRange = None
	# Properties
	XSImageRange = property(getXSImageRange, setXSImageRange, delXSImageRange, "Property for XSImageRange")
	def addXSImageRange(self, value):
		checkType("XSSubWedge", "setXSImageRange", value, "XSImageRange")
		self.__XSImageRange.append(value)
	def insertXSImageRange(self, index, value):
		checkType("XSSubWedge", "setXSImageRange", value, "XSImageRange")
		self.__XSImageRange[index] = value
	def getXSRotationalGoniostatSetting(self): return self.__XSRotationalGoniostatSetting
	def setXSRotationalGoniostatSetting(self, XSRotationalGoniostatSetting):
		checkType("XSSubWedge", "setXSRotationalGoniostatSetting", XSRotationalGoniostatSetting, "XSRotationalGoniostatSetting")
		self.__XSRotationalGoniostatSetting = XSRotationalGoniostatSetting
	def delXSRotationalGoniostatSetting(self): self.__XSRotationalGoniostatSetting = None
	# Properties
	XSRotationalGoniostatSetting = property(getXSRotationalGoniostatSetting, setXSRotationalGoniostatSetting, delXSRotationalGoniostatSetting, "Property for XSRotationalGoniostatSetting")
	def getXSRotationExposure(self): return self.__XSRotationExposure
	def setXSRotationExposure(self, XSRotationExposure):
		checkType("XSSubWedge", "setXSRotationExposure", XSRotationExposure, "XSRotationExposure")
		self.__XSRotationExposure = XSRotationExposure
	def delXSRotationExposure(self): self.__XSRotationExposure = None
	# Properties
	XSRotationExposure = property(getXSRotationExposure, setXSRotationExposure, delXSRotationExposure, "Property for XSRotationExposure")
	def export(self, outfile, level, name_='XSSubWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSSubWedge'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__imagefilenametemplate is not None:
			self.imagefilenametemplate.export(outfile, level, name_='imagefilenametemplate')
		else:
			warnEmptyAttribute("imagefilenametemplate", "XSDataString")
		if self.__XSBeamSetting is not None:
			self.XSBeamSetting.export(outfile, level, name_='XSBeamSetting')
		else:
			warnEmptyAttribute("XSBeamSetting", "XSBeamSetting")
		if self.__XSCollectionWedge is not None:
			self.XSCollectionWedge.export(outfile, level, name_='XSCollectionWedge')
		else:
			warnEmptyAttribute("XSCollectionWedge", "XSCollectionWedge")
		if self.__XSDetectorSetting is not None:
			self.XSDetectorSetting.export(outfile, level, name_='XSDetectorSetting')
		else:
			warnEmptyAttribute("XSDetectorSetting", "XSDetectorSetting")
		for XSDiffractionImages_ in self.getXSDiffractionImages():
			XSDiffractionImages_.export(outfile, level, name_='XSDiffractionImages')
		for XSImageRange_ in self.getXSImageRange():
			XSImageRange_.export(outfile, level, name_='XSImageRange')
		if self.__XSRotationalGoniostatSetting is not None:
			self.XSRotationalGoniostatSetting.export(outfile, level, name_='XSRotationalGoniostatSetting')
		else:
			warnEmptyAttribute("XSRotationalGoniostatSetting", "XSRotationalGoniostatSetting")
		if self.__XSRotationExposure is not None:
			self.XSRotationExposure.export(outfile, level, name_='XSRotationExposure')
		else:
			warnEmptyAttribute("XSRotationExposure", "XSRotationExposure")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'imagefilenametemplate':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setImagefilenametemplate(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSBeamSetting':
			obj_ = XSBeamSetting()
			obj_.build(child_)
			self.setXSBeamSetting(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSCollectionWedge':
			obj_ = XSCollectionWedge()
			obj_.build(child_)
			self.setXSCollectionWedge(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetectorSetting':
			obj_ = XSDetectorSetting()
			obj_.build(child_)
			self.setXSDetectorSetting(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDiffractionImages':
			obj_ = XSDiffractionImages()
			obj_.build(child_)
			self.XSDiffractionImages.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSImageRange':
			obj_ = XSImageRange()
			obj_.build(child_)
			self.XSImageRange.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSRotationalGoniostatSetting':
			obj_ = XSRotationalGoniostatSetting()
			obj_.build(child_)
			self.setXSRotationalGoniostatSetting(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSRotationExposure':
			obj_ = XSRotationExposure()
			obj_.build(child_)
			self.setXSRotationExposure(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSSubWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSSubWedge' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSSubWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSSubWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSSubWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSSubWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSSubWedge

class XSCollectionWedge(XSWedge):
	def __init__(self, ednaid=None):
		XSWedge.__init__(self, ednaid)
	def export(self, outfile, level, name_='XSCollectionWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSCollectionWedge'):
		XSWedge.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSWedge.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSCollectionWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSCollectionWedge' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSCollectionWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSCollectionWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSCollectionWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSCollectionWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSCollectionWedge

class XSDataInputCharacterisationv2_0(XSDataInput):
	def __init__(self, configuration=None, possibleOrientations=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv1ResultCharacterisation_Reference=None, mxv1InputCharacterisation=None):
		XSDataInput.__init__(self, configuration)
		self.__mxv1InputCharacterisation = mxv1InputCharacterisation
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
		self.__mxv2DataCollection = mxv2DataCollection
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
		self.__possibleOrientations = possibleOrientations
	def getMxv1InputCharacterisation(self): return self.__mxv1InputCharacterisation
	def setMxv1InputCharacterisation(self, mxv1InputCharacterisation):
		checkType("XSDataInputCharacterisationv2_0", "setMxv1InputCharacterisation", mxv1InputCharacterisation, "XSDataInputCharacterisation")
		self.__mxv1InputCharacterisation = mxv1InputCharacterisation
	def delMxv1InputCharacterisation(self): self.__mxv1InputCharacterisation = None
	# Properties
	mxv1InputCharacterisation = property(getMxv1InputCharacterisation, setMxv1InputCharacterisation, delMxv1InputCharacterisation, "Property for mxv1InputCharacterisation")
	def getMxv1ResultCharacterisation_Reference(self): return self.__mxv1ResultCharacterisation_Reference
	def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
		checkType("XSDataInputCharacterisationv2_0", "setMxv1ResultCharacterisation_Reference", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
	def delMxv1ResultCharacterisation_Reference(self): self.__mxv1ResultCharacterisation_Reference = None
	# Properties
	mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
	def getMxv2DataCollection(self): return self.__mxv2DataCollection
	def setMxv2DataCollection(self, mxv2DataCollection):
		checkType("XSDataInputCharacterisationv2_0", "setMxv2DataCollection", mxv2DataCollection, "XSDataCollection")
		self.__mxv2DataCollection = mxv2DataCollection
	def delMxv2DataCollection(self): self.__mxv2DataCollection = None
	# Properties
	mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
	def getMxv2DataCollection_Reference(self): return self.__mxv2DataCollection_Reference
	def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
		checkType("XSDataInputCharacterisationv2_0", "setMxv2DataCollection_Reference", mxv2DataCollection_Reference, "XSDataCollection")
		self.__mxv2DataCollection_Reference = mxv2DataCollection_Reference
	def delMxv2DataCollection_Reference(self): self.__mxv2DataCollection_Reference = None
	# Properties
	mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
	def getPossibleOrientations(self): return self.__possibleOrientations
	def setPossibleOrientations(self, possibleOrientations):
		checkType("XSDataInputCharacterisationv2_0", "setPossibleOrientations", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
	def delPossibleOrientations(self): self.__possibleOrientations = None
	# Properties
	possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
	def export(self, outfile, level, name_='XSDataInputCharacterisationv2_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputCharacterisationv2_0'):
		XSDataInput.exportChildren(self, outfile, level, name_)
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
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataInputCharacterisationv2_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataInputCharacterisationv2_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataInputCharacterisationv2_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputCharacterisationv2_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataInputCharacterisationv2_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputCharacterisationv2_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataInputCharacterisationv2_0

class XSDataResultCharacterisationv2_0(XSDataResult):
	def __init__(self, status=None, possibleOrientations=None, suggestedStrategy=None, mxv1ResultCharacterisation_Reference=None, mxv1ResultCharacterisation=None):
		XSDataResult.__init__(self, status)
		self.__mxv1ResultCharacterisation = mxv1ResultCharacterisation
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
		self.__suggestedStrategy = suggestedStrategy
		self.__possibleOrientations = possibleOrientations
	def getMxv1ResultCharacterisation(self): return self.__mxv1ResultCharacterisation
	def setMxv1ResultCharacterisation(self, mxv1ResultCharacterisation):
		checkType("XSDataResultCharacterisationv2_0", "setMxv1ResultCharacterisation", mxv1ResultCharacterisation, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation = mxv1ResultCharacterisation
	def delMxv1ResultCharacterisation(self): self.__mxv1ResultCharacterisation = None
	# Properties
	mxv1ResultCharacterisation = property(getMxv1ResultCharacterisation, setMxv1ResultCharacterisation, delMxv1ResultCharacterisation, "Property for mxv1ResultCharacterisation")
	def getMxv1ResultCharacterisation_Reference(self): return self.__mxv1ResultCharacterisation_Reference
	def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
		checkType("XSDataResultCharacterisationv2_0", "setMxv1ResultCharacterisation_Reference", mxv1ResultCharacterisation_Reference, "XSDataResultCharacterisation")
		self.__mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
	def delMxv1ResultCharacterisation_Reference(self): self.__mxv1ResultCharacterisation_Reference = None
	# Properties
	mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
	def getSuggestedStrategy(self): return self.__suggestedStrategy
	def setSuggestedStrategy(self, suggestedStrategy):
		checkType("XSDataResultCharacterisationv2_0", "setSuggestedStrategy", suggestedStrategy, "XSDataResultStrategy")
		self.__suggestedStrategy = suggestedStrategy
	def delSuggestedStrategy(self): self.__suggestedStrategy = None
	# Properties
	suggestedStrategy = property(getSuggestedStrategy, setSuggestedStrategy, delSuggestedStrategy, "Property for suggestedStrategy")
	def getPossibleOrientations(self): return self.__possibleOrientations
	def setPossibleOrientations(self, possibleOrientations):
		checkType("XSDataResultCharacterisationv2_0", "setPossibleOrientations", possibleOrientations, "kappa_alignment_response")
		self.__possibleOrientations = possibleOrientations
	def delPossibleOrientations(self): self.__possibleOrientations = None
	# Properties
	possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
	def export(self, outfile, level, name_='XSDataResultCharacterisationv2_0'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultCharacterisationv2_0'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__mxv1ResultCharacterisation is not None:
			self.mxv1ResultCharacterisation.export(outfile, level, name_='mxv1ResultCharacterisation')
		else:
			warnEmptyAttribute("mxv1ResultCharacterisation", "XSDataResultCharacterisation")
		if self.__mxv1ResultCharacterisation_Reference is not None:
			self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
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
			nodeName_ == 'suggestedStrategy':
			obj_ = XSDataResultStrategy()
			obj_.build(child_)
			self.setSuggestedStrategy(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'possibleOrientations':
			obj_ = kappa_alignment_response()
			obj_.build(child_)
			self.setPossibleOrientations(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResultCharacterisationv2_0" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResultCharacterisationv2_0' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResultCharacterisationv2_0.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultCharacterisationv2_0()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResultCharacterisationv2_0" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultCharacterisationv2_0()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResultCharacterisationv2_0

class XSDetectorAxis(XSDisplacementAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
		XSDisplacementAxis.__init__(self, XSCalibratedDisplacementAxis, name)
	def export(self, outfile, level, name_='XSDetectorAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorAxis'):
		XSDisplacementAxis.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDisplacementAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorAxis

class XSDetector(XSDisplacementList):
	def __init__(self, XSDetectorAxis=None, XSDetectorFaceAxis=None, profileerror=None, background=None, darkcurrent=None, switchingplatetime=None, readouttime=None, radius=None, shape=None, name=None):
		XSDisplacementList.__init__(self, )
		self.__name = name
		self.__shape = shape
		self.__radius = radius
		self.__readouttime = readouttime
		self.__switchingplatetime = switchingplatetime
		self.__darkcurrent = darkcurrent
		self.__background = background
		self.__profileerror = profileerror
		if XSDetectorFaceAxis is None:
			self.__XSDetectorFaceAxis = []
		else:
			self.__XSDetectorFaceAxis = XSDetectorFaceAxis
		if XSDetectorAxis is None:
			self.__XSDetectorAxis = []
		else:
			self.__XSDetectorAxis = XSDetectorAxis
	def getName(self): return self.__name
	def setName(self, name):
		checkType("XSDetector", "setName", name, "XSDataString")
		self.__name = name
	def delName(self): self.__name = None
	# Properties
	name = property(getName, setName, delName, "Property for name")
	def getShape(self): return self.__shape
	def setShape(self, shape):
		checkType("XSDetector", "setShape", shape, "XSDataString")
		self.__shape = shape
	def delShape(self): self.__shape = None
	# Properties
	shape = property(getShape, setShape, delShape, "Property for shape")
	def getRadius(self): return self.__radius
	def setRadius(self, radius):
		checkType("XSDetector", "setRadius", radius, "XSDataDouble")
		self.__radius = radius
	def delRadius(self): self.__radius = None
	# Properties
	radius = property(getRadius, setRadius, delRadius, "Property for radius")
	def getReadouttime(self): return self.__readouttime
	def setReadouttime(self, readouttime):
		checkType("XSDetector", "setReadouttime", readouttime, "XSDataDouble")
		self.__readouttime = readouttime
	def delReadouttime(self): self.__readouttime = None
	# Properties
	readouttime = property(getReadouttime, setReadouttime, delReadouttime, "Property for readouttime")
	def getSwitchingplatetime(self): return self.__switchingplatetime
	def setSwitchingplatetime(self, switchingplatetime):
		checkType("XSDetector", "setSwitchingplatetime", switchingplatetime, "XSDataDouble")
		self.__switchingplatetime = switchingplatetime
	def delSwitchingplatetime(self): self.__switchingplatetime = None
	# Properties
	switchingplatetime = property(getSwitchingplatetime, setSwitchingplatetime, delSwitchingplatetime, "Property for switchingplatetime")
	def getDarkcurrent(self): return self.__darkcurrent
	def setDarkcurrent(self, darkcurrent):
		checkType("XSDetector", "setDarkcurrent", darkcurrent, "XSDataVectorDouble")
		self.__darkcurrent = darkcurrent
	def delDarkcurrent(self): self.__darkcurrent = None
	# Properties
	darkcurrent = property(getDarkcurrent, setDarkcurrent, delDarkcurrent, "Property for darkcurrent")
	def getBackground(self): return self.__background
	def setBackground(self, background):
		checkType("XSDetector", "setBackground", background, "XSDataDouble")
		self.__background = background
	def delBackground(self): self.__background = None
	# Properties
	background = property(getBackground, setBackground, delBackground, "Property for background")
	def getProfileerror(self): return self.__profileerror
	def setProfileerror(self, profileerror):
		checkType("XSDetector", "setProfileerror", profileerror, "XSDataDouble")
		self.__profileerror = profileerror
	def delProfileerror(self): self.__profileerror = None
	# Properties
	profileerror = property(getProfileerror, setProfileerror, delProfileerror, "Property for profileerror")
	def getXSDetectorFaceAxis(self): return self.__XSDetectorFaceAxis
	def setXSDetectorFaceAxis(self, XSDetectorFaceAxis):
		checkType("XSDetector", "setXSDetectorFaceAxis", XSDetectorFaceAxis, "list")
		self.__XSDetectorFaceAxis = XSDetectorFaceAxis
	def delXSDetectorFaceAxis(self): self.__XSDetectorFaceAxis = None
	# Properties
	XSDetectorFaceAxis = property(getXSDetectorFaceAxis, setXSDetectorFaceAxis, delXSDetectorFaceAxis, "Property for XSDetectorFaceAxis")
	def addXSDetectorFaceAxis(self, value):
		checkType("XSDetector", "setXSDetectorFaceAxis", value, "XSDetectorFaceAxis")
		self.__XSDetectorFaceAxis.append(value)
	def insertXSDetectorFaceAxis(self, index, value):
		checkType("XSDetector", "setXSDetectorFaceAxis", value, "XSDetectorFaceAxis")
		self.__XSDetectorFaceAxis[index] = value
	def getXSDetectorAxis(self): return self.__XSDetectorAxis
	def setXSDetectorAxis(self, XSDetectorAxis):
		checkType("XSDetector", "setXSDetectorAxis", XSDetectorAxis, "list")
		self.__XSDetectorAxis = XSDetectorAxis
	def delXSDetectorAxis(self): self.__XSDetectorAxis = None
	# Properties
	XSDetectorAxis = property(getXSDetectorAxis, setXSDetectorAxis, delXSDetectorAxis, "Property for XSDetectorAxis")
	def addXSDetectorAxis(self, value):
		checkType("XSDetector", "setXSDetectorAxis", value, "XSDetectorAxis")
		self.__XSDetectorAxis.append(value)
	def insertXSDetectorAxis(self, index, value):
		checkType("XSDetector", "setXSDetectorAxis", value, "XSDetectorAxis")
		self.__XSDetectorAxis[index] = value
	def export(self, outfile, level, name_='XSDetector'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetector'):
		XSDisplacementList.exportChildren(self, outfile, level, name_)
		if self.__name is not None:
			self.name.export(outfile, level, name_='name')
		else:
			warnEmptyAttribute("name", "XSDataString")
		if self.__shape is not None:
			self.shape.export(outfile, level, name_='shape')
		else:
			warnEmptyAttribute("shape", "XSDataString")
		if self.__radius is not None:
			self.radius.export(outfile, level, name_='radius')
		else:
			warnEmptyAttribute("radius", "XSDataDouble")
		if self.__readouttime is not None:
			self.readouttime.export(outfile, level, name_='readouttime')
		else:
			warnEmptyAttribute("readouttime", "XSDataDouble")
		if self.__switchingplatetime is not None:
			self.switchingplatetime.export(outfile, level, name_='switchingplatetime')
		else:
			warnEmptyAttribute("switchingplatetime", "XSDataDouble")
		if self.__darkcurrent is not None:
			self.darkcurrent.export(outfile, level, name_='darkcurrent')
		else:
			warnEmptyAttribute("darkcurrent", "XSDataVectorDouble")
		if self.__background is not None:
			self.background.export(outfile, level, name_='background')
		else:
			warnEmptyAttribute("background", "XSDataDouble")
		if self.__profileerror is not None:
			self.profileerror.export(outfile, level, name_='profileerror')
		else:
			warnEmptyAttribute("profileerror", "XSDataDouble")
		for XSDetectorFaceAxis_ in self.getXSDetectorFaceAxis():
			XSDetectorFaceAxis_.export(outfile, level, name_='XSDetectorFaceAxis')
		if self.getXSDetectorFaceAxis() == []:
			warnEmptyAttribute("XSDetectorFaceAxis", "XSDetectorFaceAxis")
		for XSDetectorAxis_ in self.getXSDetectorAxis():
			XSDetectorAxis_.export(outfile, level, name_='XSDetectorAxis')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'name':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setName(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'shape':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setShape(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'radius':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRadius(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'readouttime':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setReadouttime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'switchingplatetime':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setSwitchingplatetime(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'darkcurrent':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setDarkcurrent(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'background':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBackground(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'profileerror':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setProfileerror(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetectorFaceAxis':
			obj_ = XSDetectorFaceAxis()
			obj_.build(child_)
			self.XSDetectorFaceAxis.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetectorAxis':
			obj_ = XSDetectorAxis()
			obj_.build(child_)
			self.XSDetectorAxis.append(obj_)
		XSDisplacementList.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetector" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetector' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetector.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetector()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetector" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetector()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetector

class XSDetectorSetting(XSDisplacementListSetting):
	def __init__(self, XSDetector=None, axissetting=None):
		XSDisplacementListSetting.__init__(self, )
		if axissetting is None:
			self.__axissetting = []
		else:
			self.__axissetting = axissetting
		self.__XSDetector = XSDetector
	def getAxissetting(self): return self.__axissetting
	def setAxissetting(self, axissetting):
		checkType("XSDetectorSetting", "setAxissetting", axissetting, "list")
		self.__axissetting = axissetting
	def delAxissetting(self): self.__axissetting = None
	# Properties
	axissetting = property(getAxissetting, setAxissetting, delAxissetting, "Property for axissetting")
	def addAxissetting(self, value):
		checkType("XSDetectorSetting", "setAxissetting", value, "XSDataDisplacement")
		self.__axissetting.append(value)
	def insertAxissetting(self, index, value):
		checkType("XSDetectorSetting", "setAxissetting", value, "XSDataDisplacement")
		self.__axissetting[index] = value
	def getXSDetector(self): return self.__XSDetector
	def setXSDetector(self, XSDetector):
		checkType("XSDetectorSetting", "setXSDetector", XSDetector, "XSDetector")
		self.__XSDetector = XSDetector
	def delXSDetector(self): self.__XSDetector = None
	# Properties
	XSDetector = property(getXSDetector, setXSDetector, delXSDetector, "Property for XSDetector")
	def export(self, outfile, level, name_='XSDetectorSetting'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorSetting'):
		XSDisplacementListSetting.exportChildren(self, outfile, level, name_)
		for axissetting_ in self.getAxissetting():
			axissetting_.export(outfile, level, name_='axissetting')
		if self.getAxissetting() == []:
			warnEmptyAttribute("axissetting", "XSDataDisplacement")
		if self.__XSDetector is not None:
			self.XSDetector.export(outfile, level, name_='XSDetector')
		else:
			warnEmptyAttribute("XSDetector", "XSDetector")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axissetting':
			obj_ = XSDataDisplacement()
			obj_.build(child_)
			self.axissetting.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSDetector':
			obj_ = XSDetector()
			obj_.build(child_)
			self.setXSDetector(obj_)
		XSDisplacementListSetting.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorSetting" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorSetting' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorSetting.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorSetting()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorSetting" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorSetting()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorSetting

class XSGoniostatAxis(XSDisplacementAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
		XSDisplacementAxis.__init__(self, XSCalibratedDisplacementAxis, name)
		self.__isscannable = isscannable
	def getIsscannable(self): return self.__isscannable
	def setIsscannable(self, isscannable):
		checkType("XSGoniostatAxis", "setIsscannable", isscannable, "XSDataBoolean")
		self.__isscannable = isscannable
	def delIsscannable(self): self.__isscannable = None
	# Properties
	isscannable = property(getIsscannable, setIsscannable, delIsscannable, "Property for isscannable")
	def export(self, outfile, level, name_='XSGoniostatAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSGoniostatAxis'):
		XSDisplacementAxis.exportChildren(self, outfile, level, name_)
		if self.__isscannable is not None:
			self.isscannable.export(outfile, level, name_='isscannable')
		else:
			warnEmptyAttribute("isscannable", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'isscannable':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setIsscannable(obj_)
		XSDisplacementAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSGoniostatAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSGoniostatAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSGoniostatAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSGoniostatAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSGoniostatAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSGoniostatAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSGoniostatAxis

class XSIndexingSolutionSelected(XSIndexingSolution):
	def __init__(self, penalty=None, lattice=None, orientation=None, statistics=None, mosaicityestimated=None, refineddetectorsetting=None):
		XSIndexingSolution.__init__(self, penalty, lattice)
		self.__refineddetectorsetting = refineddetectorsetting
		self.__mosaicityestimated = mosaicityestimated
		self.__statistics = statistics
		self.__orientation = orientation
	def getRefineddetectorsetting(self): return self.__refineddetectorsetting
	def setRefineddetectorsetting(self, refineddetectorsetting):
		checkType("XSIndexingSolutionSelected", "setRefineddetectorsetting", refineddetectorsetting, "XSDetectorFaceSetting")
		self.__refineddetectorsetting = refineddetectorsetting
	def delRefineddetectorsetting(self): self.__refineddetectorsetting = None
	# Properties
	refineddetectorsetting = property(getRefineddetectorsetting, setRefineddetectorsetting, delRefineddetectorsetting, "Property for refineddetectorsetting")
	def getMosaicityestimated(self): return self.__mosaicityestimated
	def setMosaicityestimated(self, mosaicityestimated):
		checkType("XSIndexingSolutionSelected", "setMosaicityestimated", mosaicityestimated, "XSDataDouble")
		self.__mosaicityestimated = mosaicityestimated
	def delMosaicityestimated(self): self.__mosaicityestimated = None
	# Properties
	mosaicityestimated = property(getMosaicityestimated, setMosaicityestimated, delMosaicityestimated, "Property for mosaicityestimated")
	def getStatistics(self): return self.__statistics
	def setStatistics(self, statistics):
		checkType("XSIndexingSolutionSelected", "setStatistics", statistics, "XSStatisticsIndexing")
		self.__statistics = statistics
	def delStatistics(self): self.__statistics = None
	# Properties
	statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
	def getOrientation(self): return self.__orientation
	def setOrientation(self, orientation):
		checkType("XSIndexingSolutionSelected", "setOrientation", orientation, "XSDataRotation")
		self.__orientation = orientation
	def delOrientation(self): self.__orientation = None
	# Properties
	orientation = property(getOrientation, setOrientation, delOrientation, "Property for orientation")
	def export(self, outfile, level, name_='XSIndexingSolutionSelected'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSIndexingSolutionSelected'):
		XSIndexingSolution.exportChildren(self, outfile, level, name_)
		if self.__refineddetectorsetting is not None:
			self.refineddetectorsetting.export(outfile, level, name_='refineddetectorsetting')
		else:
			warnEmptyAttribute("refineddetectorsetting", "XSDetectorFaceSetting")
		if self.__mosaicityestimated is not None:
			self.mosaicityestimated.export(outfile, level, name_='mosaicityestimated')
		else:
			warnEmptyAttribute("mosaicityestimated", "XSDataDouble")
		if self.__statistics is not None:
			self.statistics.export(outfile, level, name_='statistics')
		else:
			warnEmptyAttribute("statistics", "XSStatisticsIndexing")
		if self.__orientation is not None:
			self.orientation.export(outfile, level, name_='orientation')
		else:
			warnEmptyAttribute("orientation", "XSDataRotation")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'refineddetectorsetting':
			obj_ = XSDetectorFaceSetting()
			obj_.build(child_)
			self.setRefineddetectorsetting(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mosaicityestimated':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMosaicityestimated(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'statistics':
			obj_ = XSStatisticsIndexing()
			obj_.build(child_)
			self.setStatistics(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'orientation':
			obj_ = XSDataRotation()
			obj_.build(child_)
			self.setOrientation(obj_)
		XSIndexingSolution.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSIndexingSolutionSelected" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSIndexingSolutionSelected' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSIndexingSolutionSelected.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSIndexingSolutionSelected()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSIndexingSolutionSelected" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSIndexingSolutionSelected()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSIndexingSolutionSelected

class XSProcessingWedge(XSWedge):
	def __init__(self, ednaid=None):
		XSWedge.__init__(self, ednaid)
	def export(self, outfile, level, name_='XSProcessingWedge'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSProcessingWedge'):
		XSWedge.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSWedge.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSProcessingWedge" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSProcessingWedge' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSProcessingWedge.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSProcessingWedge()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSProcessingWedge" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSProcessingWedge()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSProcessingWedge

class XSRotationalGoniostat(XSDisplacementList):
	def __init__(self, XSGoniostatRotatableAxis=None, XSGoniostatBaseAxis=None):
		XSDisplacementList.__init__(self, )
		self.__XSGoniostatBaseAxis = XSGoniostatBaseAxis
		if XSGoniostatRotatableAxis is None:
			self.__XSGoniostatRotatableAxis = []
		else:
			self.__XSGoniostatRotatableAxis = XSGoniostatRotatableAxis
	def getXSGoniostatBaseAxis(self): return self.__XSGoniostatBaseAxis
	def setXSGoniostatBaseAxis(self, XSGoniostatBaseAxis):
		checkType("XSRotationalGoniostat", "setXSGoniostatBaseAxis", XSGoniostatBaseAxis, "XSGoniostatBaseAxis")
		self.__XSGoniostatBaseAxis = XSGoniostatBaseAxis
	def delXSGoniostatBaseAxis(self): self.__XSGoniostatBaseAxis = None
	# Properties
	XSGoniostatBaseAxis = property(getXSGoniostatBaseAxis, setXSGoniostatBaseAxis, delXSGoniostatBaseAxis, "Property for XSGoniostatBaseAxis")
	def getXSGoniostatRotatableAxis(self): return self.__XSGoniostatRotatableAxis
	def setXSGoniostatRotatableAxis(self, XSGoniostatRotatableAxis):
		checkType("XSRotationalGoniostat", "setXSGoniostatRotatableAxis", XSGoniostatRotatableAxis, "list")
		self.__XSGoniostatRotatableAxis = XSGoniostatRotatableAxis
	def delXSGoniostatRotatableAxis(self): self.__XSGoniostatRotatableAxis = None
	# Properties
	XSGoniostatRotatableAxis = property(getXSGoniostatRotatableAxis, setXSGoniostatRotatableAxis, delXSGoniostatRotatableAxis, "Property for XSGoniostatRotatableAxis")
	def addXSGoniostatRotatableAxis(self, value):
		checkType("XSRotationalGoniostat", "setXSGoniostatRotatableAxis", value, "XSGoniostatRotatableAxis")
		self.__XSGoniostatRotatableAxis.append(value)
	def insertXSGoniostatRotatableAxis(self, index, value):
		checkType("XSRotationalGoniostat", "setXSGoniostatRotatableAxis", value, "XSGoniostatRotatableAxis")
		self.__XSGoniostatRotatableAxis[index] = value
	def export(self, outfile, level, name_='XSRotationalGoniostat'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSRotationalGoniostat'):
		XSDisplacementList.exportChildren(self, outfile, level, name_)
		if self.__XSGoniostatBaseAxis is not None:
			self.XSGoniostatBaseAxis.export(outfile, level, name_='XSGoniostatBaseAxis')
		else:
			warnEmptyAttribute("XSGoniostatBaseAxis", "XSGoniostatBaseAxis")
		for XSGoniostatRotatableAxis_ in self.getXSGoniostatRotatableAxis():
			XSGoniostatRotatableAxis_.export(outfile, level, name_='XSGoniostatRotatableAxis')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSGoniostatBaseAxis':
			obj_ = XSGoniostatBaseAxis()
			obj_.build(child_)
			self.setXSGoniostatBaseAxis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSGoniostatRotatableAxis':
			obj_ = XSGoniostatRotatableAxis()
			obj_.build(child_)
			self.XSGoniostatRotatableAxis.append(obj_)
		XSDisplacementList.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSRotationalGoniostat" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSRotationalGoniostat' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSRotationalGoniostat.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSRotationalGoniostat()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSRotationalGoniostat" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSRotationalGoniostat()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSRotationalGoniostat

class XSRotationalGoniostatSetting(XSDisplacementListSetting):
	def __init__(self, XSRotationalGoniostat=None, axissetting=None, baseaxissetting=None):
		XSDisplacementListSetting.__init__(self, )
		self.__baseaxissetting = baseaxissetting
		if axissetting is None:
			self.__axissetting = []
		else:
			self.__axissetting = axissetting
		self.__XSRotationalGoniostat = XSRotationalGoniostat
	def getBaseaxissetting(self): return self.__baseaxissetting
	def setBaseaxissetting(self, baseaxissetting):
		checkType("XSRotationalGoniostatSetting", "setBaseaxissetting", baseaxissetting, "XSDataAngle")
		self.__baseaxissetting = baseaxissetting
	def delBaseaxissetting(self): self.__baseaxissetting = None
	# Properties
	baseaxissetting = property(getBaseaxissetting, setBaseaxissetting, delBaseaxissetting, "Property for baseaxissetting")
	def getAxissetting(self): return self.__axissetting
	def setAxissetting(self, axissetting):
		checkType("XSRotationalGoniostatSetting", "setAxissetting", axissetting, "list")
		self.__axissetting = axissetting
	def delAxissetting(self): self.__axissetting = None
	# Properties
	axissetting = property(getAxissetting, setAxissetting, delAxissetting, "Property for axissetting")
	def addAxissetting(self, value):
		checkType("XSRotationalGoniostatSetting", "setAxissetting", value, "XSDataAngle")
		self.__axissetting.append(value)
	def insertAxissetting(self, index, value):
		checkType("XSRotationalGoniostatSetting", "setAxissetting", value, "XSDataAngle")
		self.__axissetting[index] = value
	def getXSRotationalGoniostat(self): return self.__XSRotationalGoniostat
	def setXSRotationalGoniostat(self, XSRotationalGoniostat):
		checkType("XSRotationalGoniostatSetting", "setXSRotationalGoniostat", XSRotationalGoniostat, "XSRotationalGoniostat")
		self.__XSRotationalGoniostat = XSRotationalGoniostat
	def delXSRotationalGoniostat(self): self.__XSRotationalGoniostat = None
	# Properties
	XSRotationalGoniostat = property(getXSRotationalGoniostat, setXSRotationalGoniostat, delXSRotationalGoniostat, "Property for XSRotationalGoniostat")
	def export(self, outfile, level, name_='XSRotationalGoniostatSetting'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSRotationalGoniostatSetting'):
		XSDisplacementListSetting.exportChildren(self, outfile, level, name_)
		if self.__baseaxissetting is not None:
			self.baseaxissetting.export(outfile, level, name_='baseaxissetting')
		else:
			warnEmptyAttribute("baseaxissetting", "XSDataAngle")
		for axissetting_ in self.getAxissetting():
			axissetting_.export(outfile, level, name_='axissetting')
		if self.__XSRotationalGoniostat is not None:
			self.XSRotationalGoniostat.export(outfile, level, name_='XSRotationalGoniostat')
		else:
			warnEmptyAttribute("XSRotationalGoniostat", "XSRotationalGoniostat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'baseaxissetting':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.setBaseaxissetting(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'axissetting':
			obj_ = XSDataAngle()
			obj_.build(child_)
			self.axissetting.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'XSRotationalGoniostat':
			obj_ = XSRotationalGoniostat()
			obj_.build(child_)
			self.setXSRotationalGoniostat(obj_)
		XSDisplacementListSetting.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSRotationalGoniostatSetting" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSRotationalGoniostatSetting' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSRotationalGoniostatSetting.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSRotationalGoniostatSetting()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSRotationalGoniostatSetting" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSRotationalGoniostatSetting()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSRotationalGoniostatSetting

class XSDetectorRotationAxis(XSDetectorAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
		XSDetectorAxis.__init__(self, XSCalibratedDisplacementAxis, name)
	def export(self, outfile, level, name_='XSDetectorRotationAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorRotationAxis'):
		XSDetectorAxis.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDetectorAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorRotationAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorRotationAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorRotationAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorRotationAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorRotationAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorRotationAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorRotationAxis

class XSDetectorTranslationAxis(XSDetectorAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
		XSDetectorAxis.__init__(self, XSCalibratedDisplacementAxis, name)
	def export(self, outfile, level, name_='XSDetectorTranslationAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDetectorTranslationAxis'):
		XSDetectorAxis.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSDetectorAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDetectorTranslationAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDetectorTranslationAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDetectorTranslationAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDetectorTranslationAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDetectorTranslationAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDetectorTranslationAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDetectorTranslationAxis

class XSGoniostatBaseAxis(XSGoniostatAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
		XSGoniostatAxis.__init__(self, XSCalibratedDisplacementAxis, name, isscannable)
	def export(self, outfile, level, name_='XSGoniostatBaseAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSGoniostatBaseAxis'):
		XSGoniostatAxis.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSGoniostatAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSGoniostatBaseAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSGoniostatBaseAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSGoniostatBaseAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSGoniostatBaseAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSGoniostatBaseAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSGoniostatBaseAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSGoniostatBaseAxis

class XSGoniostatRotatableAxis(XSGoniostatAxis):
	def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
		XSGoniostatAxis.__init__(self, XSCalibratedDisplacementAxis, name, isscannable)
	def export(self, outfile, level, name_='XSGoniostatRotatableAxis'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSGoniostatRotatableAxis'):
		XSGoniostatAxis.exportChildren(self, outfile, level, name_)
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		pass
		XSGoniostatAxis.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSGoniostatRotatableAxis" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSGoniostatRotatableAxis' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return XSGoniostatRotatableAxis.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSGoniostatRotatableAxis()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSGoniostatRotatableAxis" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSGoniostatRotatableAxis()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSGoniostatRotatableAxis



# End of data representation classes.



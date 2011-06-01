#!/usr/bin/env python

#
# Generated Fri Mar 25 10:44::21 2011 by EDGenerateDS.
#

import sys
from xml.dom import minidom
from xml.dom import Node





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


class generated_sweep:
	def __init__(self, rank=None, completeness=None, phi=None, kappa=None, omegaEnd=None, omegaStart=None, strategyID=None):
		self.__strategyID = strategyID
		self.__omegaStart = omegaStart
		self.__omegaEnd = omegaEnd
		self.__kappa = kappa
		self.__phi = phi
		self.__completeness = completeness
		self.__rank = rank
	def getStrategyID(self): return self.__strategyID
	def setStrategyID(self, strategyID):
		checkType("generated_sweep", "setStrategyID", strategyID, "integer")
		self.__strategyID = strategyID
	def delStrategyID(self): self.__strategyID = None
	# Properties
	strategyID = property(getStrategyID, setStrategyID, delStrategyID, "Property for strategyID")
	def getOmegaStart(self): return self.__omegaStart
	def setOmegaStart(self, omegaStart):
		checkType("generated_sweep", "setOmegaStart", omegaStart, "double")
		self.__omegaStart = omegaStart
	def delOmegaStart(self): self.__omegaStart = None
	# Properties
	omegaStart = property(getOmegaStart, setOmegaStart, delOmegaStart, "Property for omegaStart")
	def getOmegaEnd(self): return self.__omegaEnd
	def setOmegaEnd(self, omegaEnd):
		checkType("generated_sweep", "setOmegaEnd", omegaEnd, "double")
		self.__omegaEnd = omegaEnd
	def delOmegaEnd(self): self.__omegaEnd = None
	# Properties
	omegaEnd = property(getOmegaEnd, setOmegaEnd, delOmegaEnd, "Property for omegaEnd")
	def getKappa(self): return self.__kappa
	def setKappa(self, kappa):
		checkType("generated_sweep", "setKappa", kappa, "double")
		self.__kappa = kappa
	def delKappa(self): self.__kappa = None
	# Properties
	kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
	def getPhi(self): return self.__phi
	def setPhi(self, phi):
		checkType("generated_sweep", "setPhi", phi, "double")
		self.__phi = phi
	def delPhi(self): self.__phi = None
	# Properties
	phi = property(getPhi, setPhi, delPhi, "Property for phi")
	def getCompleteness(self): return self.__completeness
	def setCompleteness(self, completeness):
		checkType("generated_sweep", "setCompleteness", completeness, "double")
		self.__completeness = completeness
	def delCompleteness(self): self.__completeness = None
	# Properties
	completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
	def getRank(self): return self.__rank
	def setRank(self, rank):
		checkType("generated_sweep", "setRank", rank, "double")
		self.__rank = rank
	def delRank(self): self.__rank = None
	# Properties
	rank = property(getRank, setRank, delRank, "Property for rank")
	def export(self, outfile, level, name_='generated_sweep'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='generated_sweep'):
		pass
		if self.__strategyID is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<strategyID>%d</strategyID>\n' % self.__strategyID))
		else:
			warnEmptyAttribute("strategyID", "integer")
		if self.__omegaStart is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<omegaStart>%e</omegaStart>\n' % self.__omegaStart))
		else:
			warnEmptyAttribute("omegaStart", "double")
		if self.__omegaEnd is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<omegaEnd>%e</omegaEnd>\n' % self.__omegaEnd))
		else:
			warnEmptyAttribute("omegaEnd", "double")
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
		if self.__completeness is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<completeness>%e</completeness>\n' % self.__completeness))
		else:
			warnEmptyAttribute("completeness", "double")
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
			nodeName_ == 'strategyID':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					ival_ = int(sval_)
				except ValueError:
					raise ValueError('requires integer -- %s' % child_.toxml())
				self.__strategyID = ival_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omegaStart':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__omegaStart = fval_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'omegaEnd':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__omegaEnd = fval_
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
			nodeName_ == 'completeness':
			if child_.firstChild:
				sval_ = child_.firstChild.nodeValue
				try:
					fval_ = float(sval_)
				except ValueError:
					raise ValueError('requires float (or double) -- %s' % child_.toxml())
				self.__completeness = fval_
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
		self.export( oStreamString, 0, name_="generated_sweep" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='generated_sweep' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return generated_sweep.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = generated_sweep()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="generated_sweep" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = generated_sweep()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class generated_sweep

class kappa_alignment:
	def __init__(self, comment=None, close=None, v2=None, v1=None):
		self.__v1 = v1
		self.__v2 = v2
		self.__close = close
		self.__comment = comment
	def getV1(self): return self.__v1
	def setV1(self, v1):
		checkType("kappa_alignment", "setV1", v1, "string")
		self.__v1 = v1
	def delV1(self): self.__v1 = None
	# Properties
	v1 = property(getV1, setV1, delV1, "Property for v1")
	def getV2(self): return self.__v2
	def setV2(self, v2):
		checkType("kappa_alignment", "setV2", v2, "string")
		self.__v2 = v2
	def delV2(self): self.__v2 = None
	# Properties
	v2 = property(getV2, setV2, delV2, "Property for v2")
	def getClose(self): return self.__close
	def setClose(self, close):
		checkType("kappa_alignment", "setClose", close, "string")
		self.__close = close
	def delClose(self): self.__close = None
	# Properties
	close = property(getClose, setClose, delClose, "Property for close")
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("kappa_alignment", "setComment", comment, "string")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def export(self, outfile, level, name_='kappa_alignment'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='kappa_alignment'):
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
		if self.__close is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<close>%s</close>\n' % self.__close))
		else:
			warnEmptyAttribute("close", "string")
		if self.__comment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comment>%s</comment>\n' % self.__comment))
		else:
			warnEmptyAttribute("comment", "string")
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
			nodeName_ == 'close':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__close = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comment = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="kappa_alignment" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='kappa_alignment' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return kappa_alignment.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = kappa_alignment()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="kappa_alignment" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = kappa_alignment()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class kappa_alignment

class kappa_alignment_request:
	def __init__(self, comment=None, desired_orientation=None):
		if desired_orientation is None:
			self.__desired_orientation = []
		else:
			self.__desired_orientation = desired_orientation
		self.__comment = comment
	def getDesired_orientation(self): return self.__desired_orientation
	def setDesired_orientation(self, desired_orientation):
		checkType("kappa_alignment_request", "setDesired_orientation", desired_orientation, "list")
		self.__desired_orientation = desired_orientation
	def delDesired_orientation(self): self.__desired_orientation = None
	# Properties
	desired_orientation = property(getDesired_orientation, setDesired_orientation, delDesired_orientation, "Property for desired_orientation")
	def addDesired_orientation(self, value):
		checkType("kappa_alignment_request", "setDesired_orientation", value, "kappa_alignment")
		self.__desired_orientation.append(value)
	def insertDesired_orientation(self, index, value):
		checkType("kappa_alignment_request", "setDesired_orientation", value, "kappa_alignment")
		self.__desired_orientation[index] = value
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("kappa_alignment_request", "setComment", comment, "string")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def export(self, outfile, level, name_='kappa_alignment_request'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='kappa_alignment_request'):
		pass
		for desired_orientation_ in self.getDesired_orientation():
			desired_orientation_.export(outfile, level, name_='desired_orientation')
		if self.getDesired_orientation() == []:
			warnEmptyAttribute("desired_orientation", "kappa_alignment")
		if self.__comment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comment>%s</comment>\n' % self.__comment))
		else:
			warnEmptyAttribute("comment", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'desired_orientation':
			obj_ = kappa_alignment()
			obj_.build(child_)
			self.desired_orientation.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comment = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="kappa_alignment_request" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='kappa_alignment_request' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return kappa_alignment_request.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = kappa_alignment_request()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="kappa_alignment_request" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = kappa_alignment_request()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class kappa_alignment_request

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

class strategy_request:
	def __init__(self, symmetry=None):
		self.__symmetry = symmetry
	def getSymmetry(self): return self.__symmetry
	def setSymmetry(self, symmetry):
		checkType("strategy_request", "setSymmetry", symmetry, "string")
		self.__symmetry = symmetry
	def delSymmetry(self): self.__symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def export(self, outfile, level, name_='strategy_request'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='strategy_request'):
		pass
		if self.__symmetry is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<symmetry>%s</symmetry>\n' % self.__symmetry))
		else:
			warnEmptyAttribute("symmetry", "string")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__symmetry = value_
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="strategy_request" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='strategy_request' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return strategy_request.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = strategy_request()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="strategy_request" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = strategy_request()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class strategy_request

class kappa_strategy_request:
	def __init__(self, standard_request=None, desired_datum=None, comment=None):
		self.__comment = comment
		if desired_datum is None:
			self.__desired_datum = []
		else:
			self.__desired_datum = desired_datum
		self.__standard_request = standard_request
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("kappa_strategy_request", "setComment", comment, "string")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getDesired_datum(self): return self.__desired_datum
	def setDesired_datum(self, desired_datum):
		checkType("kappa_strategy_request", "setDesired_datum", desired_datum, "list")
		self.__desired_datum = desired_datum
	def delDesired_datum(self): self.__desired_datum = None
	# Properties
	desired_datum = property(getDesired_datum, setDesired_datum, delDesired_datum, "Property for desired_datum")
	def addDesired_datum(self, value):
		checkType("kappa_strategy_request", "setDesired_datum", value, "possible_orientation")
		self.__desired_datum.append(value)
	def insertDesired_datum(self, index, value):
		checkType("kappa_strategy_request", "setDesired_datum", value, "possible_orientation")
		self.__desired_datum[index] = value
	def getStandard_request(self): return self.__standard_request
	def setStandard_request(self, standard_request):
		checkType("kappa_strategy_request", "setStandard_request", standard_request, "strategy_request")
		self.__standard_request = standard_request
	def delStandard_request(self): self.__standard_request = None
	# Properties
	standard_request = property(getStandard_request, setStandard_request, delStandard_request, "Property for standard_request")
	def export(self, outfile, level, name_='kappa_strategy_request'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='kappa_strategy_request'):
		pass
		if self.__comment is not None:
			showIndent(outfile, level)
			outfile.write(unicode('<comment>%s</comment>\n' % self.__comment))
		else:
			warnEmptyAttribute("comment", "string")
		for desired_datum_ in self.getDesired_datum():
			desired_datum_.export(outfile, level, name_='desired_datum')
		if self.getDesired_datum() == []:
			warnEmptyAttribute("desired_datum", "possible_orientation")
		if self.__standard_request is not None:
			self.standard_request.export(outfile, level, name_='standard_request')
		else:
			warnEmptyAttribute("standard_request", "strategy_request")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'comment':
			value_ = ''
			for text__content_ in child_.childNodes:
				if text__content_.nodeValue is not None:
					value_ += text__content_.nodeValue
			self.__comment = value_
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'desired_datum':
			obj_ = possible_orientation()
			obj_.build(child_)
			self.desired_datum.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'standard_request':
			obj_ = strategy_request()
			obj_.build(child_)
			self.setStandard_request(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="kappa_strategy_request" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='kappa_strategy_request' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return kappa_strategy_request.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = kappa_strategy_request()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="kappa_strategy_request" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = kappa_strategy_request()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class kappa_strategy_request

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

class strategy_response:
	def __init__(self, status=None):
		self.__status = status
	def getStatus(self): return self.__status
	def setStatus(self, status):
		checkType("strategy_response", "setStatus", status, "status")
		self.__status = status
	def delStatus(self): self.__status = None
	# Properties
	status = property(getStatus, setStatus, delStatus, "Property for status")
	def export(self, outfile, level, name_='strategy_response'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='strategy_response'):
		pass
		if self.__status is not None:
			self.status.export(outfile, level, name_='status')
		else:
			warnEmptyAttribute("status", "status")
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
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="strategy_response" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='strategy_response' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return strategy_response.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = strategy_response()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="strategy_response" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = strategy_response()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class strategy_response

class kappa_strategy_response:
	def __init__(self, standard_response=None, generated_sweep=None, comment=None, status=None):
		self.__status = status
		self.__comment = comment
		if generated_sweep is None:
			self.__generated_sweep = []
		else:
			self.__generated_sweep = generated_sweep
		self.__standard_response = standard_response
	def getStatus(self): return self.__status
	def setStatus(self, status):
		checkType("kappa_strategy_response", "setStatus", status, "status")
		self.__status = status
	def delStatus(self): self.__status = None
	# Properties
	status = property(getStatus, setStatus, delStatus, "Property for status")
	def getComment(self): return self.__comment
	def setComment(self, comment):
		checkType("kappa_strategy_response", "setComment", comment, "string")
		self.__comment = comment
	def delComment(self): self.__comment = None
	# Properties
	comment = property(getComment, setComment, delComment, "Property for comment")
	def getGenerated_sweep(self): return self.__generated_sweep
	def setGenerated_sweep(self, generated_sweep):
		checkType("kappa_strategy_response", "setGenerated_sweep", generated_sweep, "list")
		self.__generated_sweep = generated_sweep
	def delGenerated_sweep(self): self.__generated_sweep = None
	# Properties
	generated_sweep = property(getGenerated_sweep, setGenerated_sweep, delGenerated_sweep, "Property for generated_sweep")
	def addGenerated_sweep(self, value):
		checkType("kappa_strategy_response", "setGenerated_sweep", value, "generated_sweep")
		self.__generated_sweep.append(value)
	def insertGenerated_sweep(self, index, value):
		checkType("kappa_strategy_response", "setGenerated_sweep", value, "generated_sweep")
		self.__generated_sweep[index] = value
	def getStandard_response(self): return self.__standard_response
	def setStandard_response(self, standard_response):
		checkType("kappa_strategy_response", "setStandard_response", standard_response, "strategy_response")
		self.__standard_response = standard_response
	def delStandard_response(self): self.__standard_response = None
	# Properties
	standard_response = property(getStandard_response, setStandard_response, delStandard_response, "Property for standard_response")
	def export(self, outfile, level, name_='kappa_strategy_response'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='kappa_strategy_response'):
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
		for generated_sweep_ in self.getGenerated_sweep():
			generated_sweep_.export(outfile, level, name_='generated_sweep')
		if self.getGenerated_sweep() == []:
			warnEmptyAttribute("generated_sweep", "generated_sweep")
		if self.__standard_response is not None:
			self.standard_response.export(outfile, level, name_='standard_response')
		else:
			warnEmptyAttribute("standard_response", "strategy_response")
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
			nodeName_ == 'generated_sweep':
			obj_ = generated_sweep()
			obj_.build(child_)
			self.generated_sweep.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'standard_response':
			obj_ = strategy_response()
			obj_.build(child_)
			self.setStandard_response(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="kappa_strategy_response" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def outputFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='kappa_strategy_response' )
		outfile.close()
	#Method for making a copy in a new instance
	def copy( self ):
		return kappa_strategy_response.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = kappa_strategy_response()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="kappa_strategy_response" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = kappa_strategy_response()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class kappa_strategy_response



# End of data representation classes.



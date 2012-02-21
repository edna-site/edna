#!/usr/bin/env python

#
# Generated Thu Feb 16 11:34::27 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
}

try:
	from XSDataCommon import XSDataDouble
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
from XSDataCommon import XSDataDouble
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


class XSDataMatthewsCoeffIn(XSDataInput):
	def __init__(self, configuration=None, symm=None, gamma=None, beta=None, alpha=None, c=None, b=None, a=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", a, "XSDataDouble")
		self.__a = a
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", b, "XSDataDouble")
		self.__b = b
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", c, "XSDataDouble")
		self.__c = c
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", alpha, "XSDataDouble")
		self.__alpha = alpha
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", beta, "XSDataDouble")
		self.__beta = beta
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", gamma, "XSDataDouble")
		self.__gamma = gamma
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", symm, "XSDataString")
		self.__symm = symm
	def getA(self): return self.__a
	def setA(self, a):
		checkType("XSDataMatthewsCoeffIn", "setA", a, "XSDataDouble")
		self.__a = a
	def delA(self): self.__a = None
	# Properties
	a = property(getA, setA, delA, "Property for a")
	def getB(self): return self.__b
	def setB(self, b):
		checkType("XSDataMatthewsCoeffIn", "setB", b, "XSDataDouble")
		self.__b = b
	def delB(self): self.__b = None
	# Properties
	b = property(getB, setB, delB, "Property for b")
	def getC(self): return self.__c
	def setC(self, c):
		checkType("XSDataMatthewsCoeffIn", "setC", c, "XSDataDouble")
		self.__c = c
	def delC(self): self.__c = None
	# Properties
	c = property(getC, setC, delC, "Property for c")
	def getAlpha(self): return self.__alpha
	def setAlpha(self, alpha):
		checkType("XSDataMatthewsCoeffIn", "setAlpha", alpha, "XSDataDouble")
		self.__alpha = alpha
	def delAlpha(self): self.__alpha = None
	# Properties
	alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
	def getBeta(self): return self.__beta
	def setBeta(self, beta):
		checkType("XSDataMatthewsCoeffIn", "setBeta", beta, "XSDataDouble")
		self.__beta = beta
	def delBeta(self): self.__beta = None
	# Properties
	beta = property(getBeta, setBeta, delBeta, "Property for beta")
	def getGamma(self): return self.__gamma
	def setGamma(self, gamma):
		checkType("XSDataMatthewsCoeffIn", "setGamma", gamma, "XSDataDouble")
		self.__gamma = gamma
	def delGamma(self): self.__gamma = None
	# Properties
	gamma = property(getGamma, setGamma, delGamma, "Property for gamma")
	def getSymm(self): return self.__symm
	def setSymm(self, symm):
		checkType("XSDataMatthewsCoeffIn", "setSymm", symm, "XSDataString")
		self.__symm = symm
	def delSymm(self): self.__symm = None
	# Properties
	symm = property(getSymm, setSymm, delSymm, "Property for symm")
	def export(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__a is not None:
			self.a.export(outfile, level, name_='a')
		else:
			warnEmptyAttribute("a", "XSDataDouble")
		if self.__b is not None:
			self.b.export(outfile, level, name_='b')
		else:
			warnEmptyAttribute("b", "XSDataDouble")
		if self.__c is not None:
			self.c.export(outfile, level, name_='c')
		else:
			warnEmptyAttribute("c", "XSDataDouble")
		if self.__alpha is not None:
			self.alpha.export(outfile, level, name_='alpha')
		else:
			warnEmptyAttribute("alpha", "XSDataDouble")
		if self.__beta is not None:
			self.beta.export(outfile, level, name_='beta')
		else:
			warnEmptyAttribute("beta", "XSDataDouble")
		if self.__gamma is not None:
			self.gamma.export(outfile, level, name_='gamma')
		else:
			warnEmptyAttribute("gamma", "XSDataDouble")
		if self.__symm is not None:
			self.symm.export(outfile, level, name_='symm')
		else:
			warnEmptyAttribute("symm", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'a':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'b':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setB(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'c':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setC(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'alpha':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAlpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beta':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gamma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setGamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symm':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymm(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMatthewsCoeffIn' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMatthewsCoeffIn is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMatthewsCoeffIn.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffIn()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffIn()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffIn

class XSDataMatthewsCoeffOut(XSDataResult):
	def __init__(self, status=None, best_sol=None, best_p=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_p, "XSDataDouble")
		self.__best_p = best_p
		checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_sol, "XSDataString")
		self.__best_sol = best_sol
	def getBest_p(self): return self.__best_p
	def setBest_p(self, best_p):
		checkType("XSDataMatthewsCoeffOut", "setBest_p", best_p, "XSDataDouble")
		self.__best_p = best_p
	def delBest_p(self): self.__best_p = None
	# Properties
	best_p = property(getBest_p, setBest_p, delBest_p, "Property for best_p")
	def getBest_sol(self): return self.__best_sol
	def setBest_sol(self, best_sol):
		checkType("XSDataMatthewsCoeffOut", "setBest_sol", best_sol, "XSDataString")
		self.__best_sol = best_sol
	def delBest_sol(self): self.__best_sol = None
	# Properties
	best_sol = property(getBest_sol, setBest_sol, delBest_sol, "Property for best_sol")
	def export(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__best_p is not None:
			self.best_p.export(outfile, level, name_='best_p')
		else:
			warnEmptyAttribute("best_p", "XSDataDouble")
		if self.__best_sol is not None:
			self.best_sol.export(outfile, level, name_='best_sol')
		else:
			warnEmptyAttribute("best_sol", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'best_p':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBest_p(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'best_sol':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBest_sol(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMatthewsCoeffOut' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMatthewsCoeffOut is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMatthewsCoeffOut.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffOut()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffOut()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffOut

class XSDataRBinsIn(XSDataInput):
	def __init__(self, configuration=None, high=None, low=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", low, "XSDataDouble")
		self.__low = low
		checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", high, "XSDataDouble")
		self.__high = high
	def getLow(self): return self.__low
	def setLow(self, low):
		checkType("XSDataRBinsIn", "setLow", low, "XSDataDouble")
		self.__low = low
	def delLow(self): self.__low = None
	# Properties
	low = property(getLow, setLow, delLow, "Property for low")
	def getHigh(self): return self.__high
	def setHigh(self, high):
		checkType("XSDataRBinsIn", "setHigh", high, "XSDataDouble")
		self.__high = high
	def delHigh(self): self.__high = None
	# Properties
	high = property(getHigh, setHigh, delHigh, "Property for high")
	def export(self, outfile, level, name_='XSDataRBinsIn'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRBinsIn'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__low is not None:
			self.low.export(outfile, level, name_='low')
		else:
			warnEmptyAttribute("low", "XSDataDouble")
		if self.__high is not None:
			self.high.export(outfile, level, name_='high')
		else:
			warnEmptyAttribute("high", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'low':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLow(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'high':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setHigh(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRBinsIn" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRBinsIn' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRBinsIn is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRBinsIn.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsIn()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRBinsIn" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsIn()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRBinsIn

class XSDataRBinsOut(XSDataResult):
	def __init__(self, status=None, bins=None):
		XSDataResult.__init__(self, status)
		if bins is None:
			self.__bins = []
		else:
			checkType("XSDataRBinsOut", "Constructor of XSDataRBinsOut", bins, "list")
			self.__bins = bins
	def getBins(self): return self.__bins
	def setBins(self, bins):
		checkType("XSDataRBinsOut", "setBins", bins, "list")
		self.__bins = bins
	def delBins(self): self.__bins = None
	# Properties
	bins = property(getBins, setBins, delBins, "Property for bins")
	def addBins(self, value):
		checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
		self.__bins.append(value)
	def insertBins(self, index, value):
		checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
		self.__bins[index] = value
	def export(self, outfile, level, name_='XSDataRBinsOut'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRBinsOut'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for bins_ in self.getBins():
			bins_.export(outfile, level, name_='bins')
		if self.getBins() == []:
			warnEmptyAttribute("bins", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bins':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.bins.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRBinsOut" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRBinsOut' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRBinsOut is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRBinsOut.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsOut()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRBinsOut" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsOut()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRBinsOut



# End of data representation classes.



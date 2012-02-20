#!/usr/bin/env python

#
# Generated Mon Feb 20 05:53::51 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { "XSDataCommon": "workspace/edna/kernel/datamodel"}

try:
	from XSDataCommon import XSData
	from XSDataCommon import XSDataArray
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataRotation
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataVectorDouble
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
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataRotation
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataVectorDouble




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


class XSDataConfigGnom(XSData):
	def __init__(self, nextjob=None, rad56=None, coef=None, nreal=None, alpha=None, spot2=None, spot1=None, lw2=None, aw2=None, lh2=None, ah2=None, lw1=None, aw1=None, lh1=None, ah1=None, fwhm2=None, fwhm1=None, idet=None, deviat=None, kernel=None, lzrmax=None, lzrmin=None, rmax=None, rmin=None, jobtyp=None, lkern=None, ploerr=None, evaerr=None, plores=None, plonp=None, iscale=None, output=None, nskip2=None, nskip1=None, input2=None, input1=None, expert=None, forfac=None, printer=None):
		XSData.__init__(self,)
		if printer is None:
			self.__printer = []
		else:
			checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", printer, "list")
			self.__printer = printer
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", forfac, "XSDataFile")
		self.__forfac = forfac
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", expert, "XSDataFile")
		self.__expert = expert
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", input1, "XSDataFile")
		self.__input1 = input1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", input2, "XSDataFile")
		self.__input2 = input2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nskip1, "XSDataInteger")
		self.__nskip1 = nskip1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nskip2, "XSDataInteger")
		self.__nskip2 = nskip2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", output, "XSDataFile")
		self.__output = output
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", iscale, "XSDataInteger")
		self.__iscale = iscale
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", plonp, "XSDataBoolean")
		self.__plonp = plonp
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", plores, "XSDataBoolean")
		self.__plores = plores
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", evaerr, "XSDataBoolean")
		self.__evaerr = evaerr
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ploerr, "XSDataBoolean")
		self.__ploerr = ploerr
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lkern, "XSDataBoolean")
		self.__lkern = lkern
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", jobtyp, "XSDataInteger")
		self.__jobtyp = jobtyp
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rmin, "XSDataDouble")
		self.__rmin = rmin
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rmax, "XSDataDouble")
		self.__rmax = rmax
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lzrmin, "XSDataBoolean")
		self.__lzrmin = lzrmin
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lzrmax, "XSDataBoolean")
		self.__lzrmax = lzrmax
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", kernel, "XSDataFile")
		self.__kernel = kernel
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", deviat, "XSDataDouble")
		self.__deviat = deviat
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", idet, "XSDataInteger")
		self.__idet = idet
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", fwhm1, "XSDataDouble")
		self.__fwhm1 = fwhm1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", fwhm2, "XSDataDouble")
		self.__fwhm2 = fwhm2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ah1, "XSDataDouble")
		self.__ah1 = ah1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lh1, "XSDataDouble")
		self.__lh1 = lh1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", aw1, "XSDataDouble")
		self.__aw1 = aw1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lw1, "XSDataDouble")
		self.__lw1 = lw1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", ah2, "XSDataDouble")
		self.__ah2 = ah2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lh2, "XSDataDouble")
		self.__lh2 = lh2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", aw2, "XSDataDouble")
		self.__aw2 = aw2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", lw2, "XSDataDouble")
		self.__lw2 = lw2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", spot1, "XSDataFile")
		self.__spot1 = spot1
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", spot2, "XSDataFile")
		self.__spot2 = spot2
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", alpha, "XSDataDouble")
		self.__alpha = alpha
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nreal, "XSDataInteger")
		self.__nreal = nreal
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", coef, "XSDataDouble")
		self.__coef = coef
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", rad56, "XSDataDouble")
		self.__rad56 = rad56
		checkType("XSDataConfigGnom", "Constructor of XSDataConfigGnom", nextjob, "XSDataBoolean")
		self.__nextjob = nextjob
	def getPrinter(self): return self.__printer
	def setPrinter(self, printer):
		checkType("XSDataConfigGnom", "setPrinter", printer, "list")
		self.__printer = printer
	def delPrinter(self): self.__printer = None
	# Properties
	printer = property(getPrinter, setPrinter, delPrinter, "Property for printer")
	def addPrinter(self, value):
		checkType("XSDataConfigGnom", "setPrinter", value, "XSDataString")
		self.__printer.append(value)
	def insertPrinter(self, index, value):
		checkType("XSDataConfigGnom", "setPrinter", value, "XSDataString")
		self.__printer[index] = value
	def getForfac(self): return self.__forfac
	def setForfac(self, forfac):
		checkType("XSDataConfigGnom", "setForfac", forfac, "XSDataFile")
		self.__forfac = forfac
	def delForfac(self): self.__forfac = None
	# Properties
	forfac = property(getForfac, setForfac, delForfac, "Property for forfac")
	def getExpert(self): return self.__expert
	def setExpert(self, expert):
		checkType("XSDataConfigGnom", "setExpert", expert, "XSDataFile")
		self.__expert = expert
	def delExpert(self): self.__expert = None
	# Properties
	expert = property(getExpert, setExpert, delExpert, "Property for expert")
	def getInput1(self): return self.__input1
	def setInput1(self, input1):
		checkType("XSDataConfigGnom", "setInput1", input1, "XSDataFile")
		self.__input1 = input1
	def delInput1(self): self.__input1 = None
	# Properties
	input1 = property(getInput1, setInput1, delInput1, "Property for input1")
	def getInput2(self): return self.__input2
	def setInput2(self, input2):
		checkType("XSDataConfigGnom", "setInput2", input2, "XSDataFile")
		self.__input2 = input2
	def delInput2(self): self.__input2 = None
	# Properties
	input2 = property(getInput2, setInput2, delInput2, "Property for input2")
	def getNskip1(self): return self.__nskip1
	def setNskip1(self, nskip1):
		checkType("XSDataConfigGnom", "setNskip1", nskip1, "XSDataInteger")
		self.__nskip1 = nskip1
	def delNskip1(self): self.__nskip1 = None
	# Properties
	nskip1 = property(getNskip1, setNskip1, delNskip1, "Property for nskip1")
	def getNskip2(self): return self.__nskip2
	def setNskip2(self, nskip2):
		checkType("XSDataConfigGnom", "setNskip2", nskip2, "XSDataInteger")
		self.__nskip2 = nskip2
	def delNskip2(self): self.__nskip2 = None
	# Properties
	nskip2 = property(getNskip2, setNskip2, delNskip2, "Property for nskip2")
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataConfigGnom", "setOutput", output, "XSDataFile")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def getIscale(self): return self.__iscale
	def setIscale(self, iscale):
		checkType("XSDataConfigGnom", "setIscale", iscale, "XSDataInteger")
		self.__iscale = iscale
	def delIscale(self): self.__iscale = None
	# Properties
	iscale = property(getIscale, setIscale, delIscale, "Property for iscale")
	def getPlonp(self): return self.__plonp
	def setPlonp(self, plonp):
		checkType("XSDataConfigGnom", "setPlonp", plonp, "XSDataBoolean")
		self.__plonp = plonp
	def delPlonp(self): self.__plonp = None
	# Properties
	plonp = property(getPlonp, setPlonp, delPlonp, "Property for plonp")
	def getPlores(self): return self.__plores
	def setPlores(self, plores):
		checkType("XSDataConfigGnom", "setPlores", plores, "XSDataBoolean")
		self.__plores = plores
	def delPlores(self): self.__plores = None
	# Properties
	plores = property(getPlores, setPlores, delPlores, "Property for plores")
	def getEvaerr(self): return self.__evaerr
	def setEvaerr(self, evaerr):
		checkType("XSDataConfigGnom", "setEvaerr", evaerr, "XSDataBoolean")
		self.__evaerr = evaerr
	def delEvaerr(self): self.__evaerr = None
	# Properties
	evaerr = property(getEvaerr, setEvaerr, delEvaerr, "Property for evaerr")
	def getPloerr(self): return self.__ploerr
	def setPloerr(self, ploerr):
		checkType("XSDataConfigGnom", "setPloerr", ploerr, "XSDataBoolean")
		self.__ploerr = ploerr
	def delPloerr(self): self.__ploerr = None
	# Properties
	ploerr = property(getPloerr, setPloerr, delPloerr, "Property for ploerr")
	def getLkern(self): return self.__lkern
	def setLkern(self, lkern):
		checkType("XSDataConfigGnom", "setLkern", lkern, "XSDataBoolean")
		self.__lkern = lkern
	def delLkern(self): self.__lkern = None
	# Properties
	lkern = property(getLkern, setLkern, delLkern, "Property for lkern")
	def getJobtyp(self): return self.__jobtyp
	def setJobtyp(self, jobtyp):
		checkType("XSDataConfigGnom", "setJobtyp", jobtyp, "XSDataInteger")
		self.__jobtyp = jobtyp
	def delJobtyp(self): self.__jobtyp = None
	# Properties
	jobtyp = property(getJobtyp, setJobtyp, delJobtyp, "Property for jobtyp")
	def getRmin(self): return self.__rmin
	def setRmin(self, rmin):
		checkType("XSDataConfigGnom", "setRmin", rmin, "XSDataDouble")
		self.__rmin = rmin
	def delRmin(self): self.__rmin = None
	# Properties
	rmin = property(getRmin, setRmin, delRmin, "Property for rmin")
	def getRmax(self): return self.__rmax
	def setRmax(self, rmax):
		checkType("XSDataConfigGnom", "setRmax", rmax, "XSDataDouble")
		self.__rmax = rmax
	def delRmax(self): self.__rmax = None
	# Properties
	rmax = property(getRmax, setRmax, delRmax, "Property for rmax")
	def getLzrmin(self): return self.__lzrmin
	def setLzrmin(self, lzrmin):
		checkType("XSDataConfigGnom", "setLzrmin", lzrmin, "XSDataBoolean")
		self.__lzrmin = lzrmin
	def delLzrmin(self): self.__lzrmin = None
	# Properties
	lzrmin = property(getLzrmin, setLzrmin, delLzrmin, "Property for lzrmin")
	def getLzrmax(self): return self.__lzrmax
	def setLzrmax(self, lzrmax):
		checkType("XSDataConfigGnom", "setLzrmax", lzrmax, "XSDataBoolean")
		self.__lzrmax = lzrmax
	def delLzrmax(self): self.__lzrmax = None
	# Properties
	lzrmax = property(getLzrmax, setLzrmax, delLzrmax, "Property for lzrmax")
	def getKernel(self): return self.__kernel
	def setKernel(self, kernel):
		checkType("XSDataConfigGnom", "setKernel", kernel, "XSDataFile")
		self.__kernel = kernel
	def delKernel(self): self.__kernel = None
	# Properties
	kernel = property(getKernel, setKernel, delKernel, "Property for kernel")
	def getDeviat(self): return self.__deviat
	def setDeviat(self, deviat):
		checkType("XSDataConfigGnom", "setDeviat", deviat, "XSDataDouble")
		self.__deviat = deviat
	def delDeviat(self): self.__deviat = None
	# Properties
	deviat = property(getDeviat, setDeviat, delDeviat, "Property for deviat")
	def getIdet(self): return self.__idet
	def setIdet(self, idet):
		checkType("XSDataConfigGnom", "setIdet", idet, "XSDataInteger")
		self.__idet = idet
	def delIdet(self): self.__idet = None
	# Properties
	idet = property(getIdet, setIdet, delIdet, "Property for idet")
	def getFwhm1(self): return self.__fwhm1
	def setFwhm1(self, fwhm1):
		checkType("XSDataConfigGnom", "setFwhm1", fwhm1, "XSDataDouble")
		self.__fwhm1 = fwhm1
	def delFwhm1(self): self.__fwhm1 = None
	# Properties
	fwhm1 = property(getFwhm1, setFwhm1, delFwhm1, "Property for fwhm1")
	def getFwhm2(self): return self.__fwhm2
	def setFwhm2(self, fwhm2):
		checkType("XSDataConfigGnom", "setFwhm2", fwhm2, "XSDataDouble")
		self.__fwhm2 = fwhm2
	def delFwhm2(self): self.__fwhm2 = None
	# Properties
	fwhm2 = property(getFwhm2, setFwhm2, delFwhm2, "Property for fwhm2")
	def getAh1(self): return self.__ah1
	def setAh1(self, ah1):
		checkType("XSDataConfigGnom", "setAh1", ah1, "XSDataDouble")
		self.__ah1 = ah1
	def delAh1(self): self.__ah1 = None
	# Properties
	ah1 = property(getAh1, setAh1, delAh1, "Property for ah1")
	def getLh1(self): return self.__lh1
	def setLh1(self, lh1):
		checkType("XSDataConfigGnom", "setLh1", lh1, "XSDataDouble")
		self.__lh1 = lh1
	def delLh1(self): self.__lh1 = None
	# Properties
	lh1 = property(getLh1, setLh1, delLh1, "Property for lh1")
	def getAw1(self): return self.__aw1
	def setAw1(self, aw1):
		checkType("XSDataConfigGnom", "setAw1", aw1, "XSDataDouble")
		self.__aw1 = aw1
	def delAw1(self): self.__aw1 = None
	# Properties
	aw1 = property(getAw1, setAw1, delAw1, "Property for aw1")
	def getLw1(self): return self.__lw1
	def setLw1(self, lw1):
		checkType("XSDataConfigGnom", "setLw1", lw1, "XSDataDouble")
		self.__lw1 = lw1
	def delLw1(self): self.__lw1 = None
	# Properties
	lw1 = property(getLw1, setLw1, delLw1, "Property for lw1")
	def getAh2(self): return self.__ah2
	def setAh2(self, ah2):
		checkType("XSDataConfigGnom", "setAh2", ah2, "XSDataDouble")
		self.__ah2 = ah2
	def delAh2(self): self.__ah2 = None
	# Properties
	ah2 = property(getAh2, setAh2, delAh2, "Property for ah2")
	def getLh2(self): return self.__lh2
	def setLh2(self, lh2):
		checkType("XSDataConfigGnom", "setLh2", lh2, "XSDataDouble")
		self.__lh2 = lh2
	def delLh2(self): self.__lh2 = None
	# Properties
	lh2 = property(getLh2, setLh2, delLh2, "Property for lh2")
	def getAw2(self): return self.__aw2
	def setAw2(self, aw2):
		checkType("XSDataConfigGnom", "setAw2", aw2, "XSDataDouble")
		self.__aw2 = aw2
	def delAw2(self): self.__aw2 = None
	# Properties
	aw2 = property(getAw2, setAw2, delAw2, "Property for aw2")
	def getLw2(self): return self.__lw2
	def setLw2(self, lw2):
		checkType("XSDataConfigGnom", "setLw2", lw2, "XSDataDouble")
		self.__lw2 = lw2
	def delLw2(self): self.__lw2 = None
	# Properties
	lw2 = property(getLw2, setLw2, delLw2, "Property for lw2")
	def getSpot1(self): return self.__spot1
	def setSpot1(self, spot1):
		checkType("XSDataConfigGnom", "setSpot1", spot1, "XSDataFile")
		self.__spot1 = spot1
	def delSpot1(self): self.__spot1 = None
	# Properties
	spot1 = property(getSpot1, setSpot1, delSpot1, "Property for spot1")
	def getSpot2(self): return self.__spot2
	def setSpot2(self, spot2):
		checkType("XSDataConfigGnom", "setSpot2", spot2, "XSDataFile")
		self.__spot2 = spot2
	def delSpot2(self): self.__spot2 = None
	# Properties
	spot2 = property(getSpot2, setSpot2, delSpot2, "Property for spot2")
	def getAlpha(self): return self.__alpha
	def setAlpha(self, alpha):
		checkType("XSDataConfigGnom", "setAlpha", alpha, "XSDataDouble")
		self.__alpha = alpha
	def delAlpha(self): self.__alpha = None
	# Properties
	alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
	def getNreal(self): return self.__nreal
	def setNreal(self, nreal):
		checkType("XSDataConfigGnom", "setNreal", nreal, "XSDataInteger")
		self.__nreal = nreal
	def delNreal(self): self.__nreal = None
	# Properties
	nreal = property(getNreal, setNreal, delNreal, "Property for nreal")
	def getCoef(self): return self.__coef
	def setCoef(self, coef):
		checkType("XSDataConfigGnom", "setCoef", coef, "XSDataDouble")
		self.__coef = coef
	def delCoef(self): self.__coef = None
	# Properties
	coef = property(getCoef, setCoef, delCoef, "Property for coef")
	def getRad56(self): return self.__rad56
	def setRad56(self, rad56):
		checkType("XSDataConfigGnom", "setRad56", rad56, "XSDataDouble")
		self.__rad56 = rad56
	def delRad56(self): self.__rad56 = None
	# Properties
	rad56 = property(getRad56, setRad56, delRad56, "Property for rad56")
	def getNextjob(self): return self.__nextjob
	def setNextjob(self, nextjob):
		checkType("XSDataConfigGnom", "setNextjob", nextjob, "XSDataBoolean")
		self.__nextjob = nextjob
	def delNextjob(self): self.__nextjob = None
	# Properties
	nextjob = property(getNextjob, setNextjob, delNextjob, "Property for nextjob")
	def export(self, outfile, level, name_='XSDataConfigGnom'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataConfigGnom'):
		XSData.exportChildren(self, outfile, level, name_)
		for printer_ in self.getPrinter():
			printer_.export(outfile, level, name_='printer')
		if self.__forfac is not None:
			self.forfac.export(outfile, level, name_='forfac')
		if self.__expert is not None:
			self.expert.export(outfile, level, name_='expert')
		if self.__input1 is not None:
			self.input1.export(outfile, level, name_='input1')
		else:
			warnEmptyAttribute("input1", "XSDataFile")
		if self.__input2 is not None:
			self.input2.export(outfile, level, name_='input2')
		if self.__nskip1 is not None:
			self.nskip1.export(outfile, level, name_='nskip1')
		if self.__nskip2 is not None:
			self.nskip2.export(outfile, level, name_='nskip2')
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		if self.__iscale is not None:
			self.iscale.export(outfile, level, name_='iscale')
		if self.__plonp is not None:
			self.plonp.export(outfile, level, name_='plonp')
		else:
			warnEmptyAttribute("plonp", "XSDataBoolean")
		if self.__plores is not None:
			self.plores.export(outfile, level, name_='plores')
		else:
			warnEmptyAttribute("plores", "XSDataBoolean")
		if self.__evaerr is not None:
			self.evaerr.export(outfile, level, name_='evaerr')
		if self.__ploerr is not None:
			self.ploerr.export(outfile, level, name_='ploerr')
		else:
			warnEmptyAttribute("ploerr", "XSDataBoolean")
		if self.__lkern is not None:
			self.lkern.export(outfile, level, name_='lkern')
		if self.__jobtyp is not None:
			self.jobtyp.export(outfile, level, name_='jobtyp')
		if self.__rmin is not None:
			self.rmin.export(outfile, level, name_='rmin')
		if self.__rmax is not None:
			self.rmax.export(outfile, level, name_='rmax')
		if self.__lzrmin is not None:
			self.lzrmin.export(outfile, level, name_='lzrmin')
		if self.__lzrmax is not None:
			self.lzrmax.export(outfile, level, name_='lzrmax')
		if self.__kernel is not None:
			self.kernel.export(outfile, level, name_='kernel')
		if self.__deviat is not None:
			self.deviat.export(outfile, level, name_='deviat')
		else:
			warnEmptyAttribute("deviat", "XSDataDouble")
		if self.__idet is not None:
			self.idet.export(outfile, level, name_='idet')
		if self.__fwhm1 is not None:
			self.fwhm1.export(outfile, level, name_='fwhm1')
		if self.__fwhm2 is not None:
			self.fwhm2.export(outfile, level, name_='fwhm2')
		if self.__ah1 is not None:
			self.ah1.export(outfile, level, name_='ah1')
		if self.__lh1 is not None:
			self.lh1.export(outfile, level, name_='lh1')
		if self.__aw1 is not None:
			self.aw1.export(outfile, level, name_='aw1')
		if self.__lw1 is not None:
			self.lw1.export(outfile, level, name_='lw1')
		if self.__ah2 is not None:
			self.ah2.export(outfile, level, name_='ah2')
		if self.__lh2 is not None:
			self.lh2.export(outfile, level, name_='lh2')
		if self.__aw2 is not None:
			self.aw2.export(outfile, level, name_='aw2')
		if self.__lw2 is not None:
			self.lw2.export(outfile, level, name_='lw2')
		if self.__spot1 is not None:
			self.spot1.export(outfile, level, name_='spot1')
		if self.__spot2 is not None:
			self.spot2.export(outfile, level, name_='spot2')
		if self.__alpha is not None:
			self.alpha.export(outfile, level, name_='alpha')
		else:
			warnEmptyAttribute("alpha", "XSDataDouble")
		if self.__nreal is not None:
			self.nreal.export(outfile, level, name_='nreal')
		else:
			warnEmptyAttribute("nreal", "XSDataInteger")
		if self.__coef is not None:
			self.coef.export(outfile, level, name_='coef')
		if self.__rad56 is not None:
			self.rad56.export(outfile, level, name_='rad56')
		if self.__nextjob is not None:
			self.nextjob.export(outfile, level, name_='nextjob')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'printer':
			obj_ = XSDataString()
			obj_.build(child_)
			self.printer.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'forfac':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setForfac(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expert':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setExpert(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'input1':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInput1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'input2':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInput2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nskip1':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNskip1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nskip2':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNskip2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iscale':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIscale(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'plonp':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setPlonp(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'plores':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setPlores(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'evaerr':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setEvaerr(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ploerr':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setPloerr(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lkern':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setLkern(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'jobtyp':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setJobtyp(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRmin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rmax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRmax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lzrmin':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setLzrmin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lzrmax':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setLzrmax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'kernel':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setKernel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'deviat':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setDeviat(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'idet':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setIdet(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fwhm1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFwhm1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fwhm2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFwhm2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ah1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAh1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lh1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLh1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aw1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAw1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lw1':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLw1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'ah2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAh2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lh2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLh2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'aw2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAw2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lw2':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLw2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spot1':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSpot1(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'spot2':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSpot2(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'alpha':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAlpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nreal':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setNreal(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'coef':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setCoef(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rad56':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRad56(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'nextjob':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setNextjob(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataConfigGnom")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataConfigGnom')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataConfigGnom is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataConfigGnom.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataConfigGnom()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataConfigGnom")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataConfigGnom()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataConfigGnom

class XSDataSolutionScatteringSettings(XSData):
	def __init__(self, rMaxAbsTol=None, rMaxIntervals=None, rMaxStop=None, rMaxStart=None):
		XSData.__init__(self,)
		checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxStart, "XSDataDouble")
		self.__rMaxStart = rMaxStart
		checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxStop, "XSDataDouble")
		self.__rMaxStop = rMaxStop
		checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxIntervals, "XSDataInteger")
		self.__rMaxIntervals = rMaxIntervals
		checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxAbsTol, "XSDataDouble")
		self.__rMaxAbsTol = rMaxAbsTol
	def getRMaxStart(self): return self.__rMaxStart
	def setRMaxStart(self, rMaxStart):
		checkType("XSDataSolutionScatteringSettings", "setRMaxStart", rMaxStart, "XSDataDouble")
		self.__rMaxStart = rMaxStart
	def delRMaxStart(self): self.__rMaxStart = None
	# Properties
	rMaxStart = property(getRMaxStart, setRMaxStart, delRMaxStart, "Property for rMaxStart")
	def getRMaxStop(self): return self.__rMaxStop
	def setRMaxStop(self, rMaxStop):
		checkType("XSDataSolutionScatteringSettings", "setRMaxStop", rMaxStop, "XSDataDouble")
		self.__rMaxStop = rMaxStop
	def delRMaxStop(self): self.__rMaxStop = None
	# Properties
	rMaxStop = property(getRMaxStop, setRMaxStop, delRMaxStop, "Property for rMaxStop")
	def getRMaxIntervals(self): return self.__rMaxIntervals
	def setRMaxIntervals(self, rMaxIntervals):
		checkType("XSDataSolutionScatteringSettings", "setRMaxIntervals", rMaxIntervals, "XSDataInteger")
		self.__rMaxIntervals = rMaxIntervals
	def delRMaxIntervals(self): self.__rMaxIntervals = None
	# Properties
	rMaxIntervals = property(getRMaxIntervals, setRMaxIntervals, delRMaxIntervals, "Property for rMaxIntervals")
	def getRMaxAbsTol(self): return self.__rMaxAbsTol
	def setRMaxAbsTol(self, rMaxAbsTol):
		checkType("XSDataSolutionScatteringSettings", "setRMaxAbsTol", rMaxAbsTol, "XSDataDouble")
		self.__rMaxAbsTol = rMaxAbsTol
	def delRMaxAbsTol(self): self.__rMaxAbsTol = None
	# Properties
	rMaxAbsTol = property(getRMaxAbsTol, setRMaxAbsTol, delRMaxAbsTol, "Property for rMaxAbsTol")
	def export(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
		XSData.exportChildren(self, outfile, level, name_)
		if self.__rMaxStart is not None:
			self.rMaxStart.export(outfile, level, name_='rMaxStart')
		else:
			warnEmptyAttribute("rMaxStart", "XSDataDouble")
		if self.__rMaxStop is not None:
			self.rMaxStop.export(outfile, level, name_='rMaxStop')
		else:
			warnEmptyAttribute("rMaxStop", "XSDataDouble")
		if self.__rMaxIntervals is not None:
			self.rMaxIntervals.export(outfile, level, name_='rMaxIntervals')
		else:
			warnEmptyAttribute("rMaxIntervals", "XSDataInteger")
		if self.__rMaxAbsTol is not None:
			self.rMaxAbsTol.export(outfile, level, name_='rMaxAbsTol')
		else:
			warnEmptyAttribute("rMaxAbsTol", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMaxStart':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRMaxStart(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMaxStop':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRMaxStop(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMaxIntervals':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setRMaxIntervals(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMaxAbsTol':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRMaxAbsTol(obj_)
		XSData.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataSolutionScatteringSettings")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataSolutionScatteringSettings')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataSolutionScatteringSettings is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataSolutionScatteringSettings.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataSolutionScatteringSettings()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataSolutionScatteringSettings")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataSolutionScatteringSettings()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataSolutionScatteringSettings

class XSDataInputDamaver(XSDataInput):
	def __init__(self, configuration=None, automatic=None, symmetry=None, pdbInputFiles=None):
		XSDataInput.__init__(self, configuration)
		if pdbInputFiles is None:
			self.__pdbInputFiles = []
		else:
			checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", pdbInputFiles, "list")
			self.__pdbInputFiles = pdbInputFiles
		checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", symmetry, "XSDataString")
		self.__symmetry = symmetry
		checkType("XSDataInputDamaver", "Constructor of XSDataInputDamaver", automatic, "XSDataBoolean")
		self.__automatic = automatic
	def getPdbInputFiles(self): return self.__pdbInputFiles
	def setPdbInputFiles(self, pdbInputFiles):
		checkType("XSDataInputDamaver", "setPdbInputFiles", pdbInputFiles, "list")
		self.__pdbInputFiles = pdbInputFiles
	def delPdbInputFiles(self): self.__pdbInputFiles = None
	# Properties
	pdbInputFiles = property(getPdbInputFiles, setPdbInputFiles, delPdbInputFiles, "Property for pdbInputFiles")
	def addPdbInputFiles(self, value):
		checkType("XSDataInputDamaver", "setPdbInputFiles", value, "XSDataFile")
		self.__pdbInputFiles.append(value)
	def insertPdbInputFiles(self, index, value):
		checkType("XSDataInputDamaver", "setPdbInputFiles", value, "XSDataFile")
		self.__pdbInputFiles[index] = value
	def getSymmetry(self): return self.__symmetry
	def setSymmetry(self, symmetry):
		checkType("XSDataInputDamaver", "setSymmetry", symmetry, "XSDataString")
		self.__symmetry = symmetry
	def delSymmetry(self): self.__symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def getAutomatic(self): return self.__automatic
	def setAutomatic(self, automatic):
		checkType("XSDataInputDamaver", "setAutomatic", automatic, "XSDataBoolean")
		self.__automatic = automatic
	def delAutomatic(self): self.__automatic = None
	# Properties
	automatic = property(getAutomatic, setAutomatic, delAutomatic, "Property for automatic")
	def export(self, outfile, level, name_='XSDataInputDamaver'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDamaver'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		for pdbInputFiles_ in self.getPdbInputFiles():
			pdbInputFiles_.export(outfile, level, name_='pdbInputFiles')
		if self.getPdbInputFiles() == []:
			warnEmptyAttribute("pdbInputFiles", "XSDataFile")
		if self.__symmetry is not None:
			self.symmetry.export(outfile, level, name_='symmetry')
		if self.__automatic is not None:
			self.automatic.export(outfile, level, name_='automatic')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbInputFiles':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.pdbInputFiles.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymmetry(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'automatic':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setAutomatic(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputDamaver")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputDamaver')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputDamaver is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputDamaver.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamaver()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputDamaver")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamaver()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputDamaver

class XSDataInputDamfilt(XSDataInput):
	def __init__(self, configuration=None, inputPdbFile=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputDamfilt", "Constructor of XSDataInputDamfilt", inputPdbFile, "XSDataFile")
		self.__inputPdbFile = inputPdbFile
	def getInputPdbFile(self): return self.__inputPdbFile
	def setInputPdbFile(self, inputPdbFile):
		checkType("XSDataInputDamfilt", "setInputPdbFile", inputPdbFile, "XSDataFile")
		self.__inputPdbFile = inputPdbFile
	def delInputPdbFile(self): self.__inputPdbFile = None
	# Properties
	inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
	def export(self, outfile, level, name_='XSDataInputDamfilt'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDamfilt'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputPdbFile is not None:
			self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
		else:
			warnEmptyAttribute("inputPdbFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputPdbFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputDamfilt")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputDamfilt')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputDamfilt is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputDamfilt.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamfilt()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputDamfilt")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamfilt()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputDamfilt

class XSDataInputDammif(XSDataInput):
	def __init__(self, configuration=None, constant=None, chained=None, mode=None, symmetry=None, unit=None, gnomOutputFile=None, expectedParticleShape=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", expectedParticleShape, "XSDataInteger")
		self.__expectedParticleShape = expectedParticleShape
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", gnomOutputFile, "XSDataFile")
		self.__gnomOutputFile = gnomOutputFile
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", unit, "XSDataString")
		self.__unit = unit
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", symmetry, "XSDataString")
		self.__symmetry = symmetry
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", mode, "XSDataString")
		self.__mode = mode
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", chained, "XSDataBoolean")
		self.__chained = chained
		checkType("XSDataInputDammif", "Constructor of XSDataInputDammif", constant, "XSDataDouble")
		self.__constant = constant
	def getExpectedParticleShape(self): return self.__expectedParticleShape
	def setExpectedParticleShape(self, expectedParticleShape):
		checkType("XSDataInputDammif", "setExpectedParticleShape", expectedParticleShape, "XSDataInteger")
		self.__expectedParticleShape = expectedParticleShape
	def delExpectedParticleShape(self): self.__expectedParticleShape = None
	# Properties
	expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
	def getGnomOutputFile(self): return self.__gnomOutputFile
	def setGnomOutputFile(self, gnomOutputFile):
		checkType("XSDataInputDammif", "setGnomOutputFile", gnomOutputFile, "XSDataFile")
		self.__gnomOutputFile = gnomOutputFile
	def delGnomOutputFile(self): self.__gnomOutputFile = None
	# Properties
	gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
	def getUnit(self): return self.__unit
	def setUnit(self, unit):
		checkType("XSDataInputDammif", "setUnit", unit, "XSDataString")
		self.__unit = unit
	def delUnit(self): self.__unit = None
	# Properties
	unit = property(getUnit, setUnit, delUnit, "Property for unit")
	def getSymmetry(self): return self.__symmetry
	def setSymmetry(self, symmetry):
		checkType("XSDataInputDammif", "setSymmetry", symmetry, "XSDataString")
		self.__symmetry = symmetry
	def delSymmetry(self): self.__symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def getMode(self): return self.__mode
	def setMode(self, mode):
		checkType("XSDataInputDammif", "setMode", mode, "XSDataString")
		self.__mode = mode
	def delMode(self): self.__mode = None
	# Properties
	mode = property(getMode, setMode, delMode, "Property for mode")
	def getChained(self): return self.__chained
	def setChained(self, chained):
		checkType("XSDataInputDammif", "setChained", chained, "XSDataBoolean")
		self.__chained = chained
	def delChained(self): self.__chained = None
	# Properties
	chained = property(getChained, setChained, delChained, "Property for chained")
	def getConstant(self): return self.__constant
	def setConstant(self, constant):
		checkType("XSDataInputDammif", "setConstant", constant, "XSDataDouble")
		self.__constant = constant
	def delConstant(self): self.__constant = None
	# Properties
	constant = property(getConstant, setConstant, delConstant, "Property for constant")
	def export(self, outfile, level, name_='XSDataInputDammif'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDammif'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__expectedParticleShape is not None:
			self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
		else:
			warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
		if self.__gnomOutputFile is not None:
			self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
		else:
			warnEmptyAttribute("gnomOutputFile", "XSDataFile")
		if self.__unit is not None:
			self.unit.export(outfile, level, name_='unit')
		if self.__symmetry is not None:
			self.symmetry.export(outfile, level, name_='symmetry')
		else:
			warnEmptyAttribute("symmetry", "XSDataString")
		if self.__mode is not None:
			self.mode.export(outfile, level, name_='mode')
		if self.__chained is not None:
			self.chained.export(outfile, level, name_='chained')
		if self.__constant is not None:
			self.constant.export(outfile, level, name_='constant')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedParticleShape':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setExpectedParticleShape(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gnomOutputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGnomOutputFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unit':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setUnit(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymmetry(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chained':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setChained(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'constant':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setConstant(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputDammif")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputDammif')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputDammif is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputDammif.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDammif()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputDammif")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDammif()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputDammif

class XSDataInputDammin(XSDataInput):
	def __init__(self, configuration=None, mode=None, symmetry=None, pdbInputFile=None, initialDummyAtomModel=None, gnomOutputFile=None, expectedParticleShape=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", expectedParticleShape, "XSDataInteger")
		self.__expectedParticleShape = expectedParticleShape
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", gnomOutputFile, "XSDataFile")
		self.__gnomOutputFile = gnomOutputFile
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", initialDummyAtomModel, "XSDataInteger")
		self.__initialDummyAtomModel = initialDummyAtomModel
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", pdbInputFile, "XSDataFile")
		self.__pdbInputFile = pdbInputFile
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", symmetry, "XSDataString")
		self.__symmetry = symmetry
		checkType("XSDataInputDammin", "Constructor of XSDataInputDammin", mode, "XSDataString")
		self.__mode = mode
	def getExpectedParticleShape(self): return self.__expectedParticleShape
	def setExpectedParticleShape(self, expectedParticleShape):
		checkType("XSDataInputDammin", "setExpectedParticleShape", expectedParticleShape, "XSDataInteger")
		self.__expectedParticleShape = expectedParticleShape
	def delExpectedParticleShape(self): self.__expectedParticleShape = None
	# Properties
	expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
	def getGnomOutputFile(self): return self.__gnomOutputFile
	def setGnomOutputFile(self, gnomOutputFile):
		checkType("XSDataInputDammin", "setGnomOutputFile", gnomOutputFile, "XSDataFile")
		self.__gnomOutputFile = gnomOutputFile
	def delGnomOutputFile(self): self.__gnomOutputFile = None
	# Properties
	gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
	def getInitialDummyAtomModel(self): return self.__initialDummyAtomModel
	def setInitialDummyAtomModel(self, initialDummyAtomModel):
		checkType("XSDataInputDammin", "setInitialDummyAtomModel", initialDummyAtomModel, "XSDataInteger")
		self.__initialDummyAtomModel = initialDummyAtomModel
	def delInitialDummyAtomModel(self): self.__initialDummyAtomModel = None
	# Properties
	initialDummyAtomModel = property(getInitialDummyAtomModel, setInitialDummyAtomModel, delInitialDummyAtomModel, "Property for initialDummyAtomModel")
	def getPdbInputFile(self): return self.__pdbInputFile
	def setPdbInputFile(self, pdbInputFile):
		checkType("XSDataInputDammin", "setPdbInputFile", pdbInputFile, "XSDataFile")
		self.__pdbInputFile = pdbInputFile
	def delPdbInputFile(self): self.__pdbInputFile = None
	# Properties
	pdbInputFile = property(getPdbInputFile, setPdbInputFile, delPdbInputFile, "Property for pdbInputFile")
	def getSymmetry(self): return self.__symmetry
	def setSymmetry(self, symmetry):
		checkType("XSDataInputDammin", "setSymmetry", symmetry, "XSDataString")
		self.__symmetry = symmetry
	def delSymmetry(self): self.__symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def getMode(self): return self.__mode
	def setMode(self, mode):
		checkType("XSDataInputDammin", "setMode", mode, "XSDataString")
		self.__mode = mode
	def delMode(self): self.__mode = None
	# Properties
	mode = property(getMode, setMode, delMode, "Property for mode")
	def export(self, outfile, level, name_='XSDataInputDammin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDammin'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__expectedParticleShape is not None:
			self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
		else:
			warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
		if self.__gnomOutputFile is not None:
			self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
		else:
			warnEmptyAttribute("gnomOutputFile", "XSDataFile")
		if self.__initialDummyAtomModel is not None:
			self.initialDummyAtomModel.export(outfile, level, name_='initialDummyAtomModel')
		else:
			warnEmptyAttribute("initialDummyAtomModel", "XSDataInteger")
		if self.__pdbInputFile is not None:
			self.pdbInputFile.export(outfile, level, name_='pdbInputFile')
		else:
			warnEmptyAttribute("pdbInputFile", "XSDataFile")
		if self.__symmetry is not None:
			self.symmetry.export(outfile, level, name_='symmetry')
		else:
			warnEmptyAttribute("symmetry", "XSDataString")
		if self.__mode is not None:
			self.mode.export(outfile, level, name_='mode')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'expectedParticleShape':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setExpectedParticleShape(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gnomOutputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGnomOutputFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'initialDummyAtomModel':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setInitialDummyAtomModel(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbInputFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbInputFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymmetry(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMode(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputDammin")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputDammin')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputDammin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputDammin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDammin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputDammin")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDammin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputDammin

class XSDataInputDamstart(XSDataInput):
	def __init__(self, configuration=None, inputPdbFile=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputDamstart", "Constructor of XSDataInputDamstart", inputPdbFile, "XSDataFile")
		self.__inputPdbFile = inputPdbFile
	def getInputPdbFile(self): return self.__inputPdbFile
	def setInputPdbFile(self, inputPdbFile):
		checkType("XSDataInputDamstart", "setInputPdbFile", inputPdbFile, "XSDataFile")
		self.__inputPdbFile = inputPdbFile
	def delInputPdbFile(self): self.__inputPdbFile = None
	# Properties
	inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
	def export(self, outfile, level, name_='XSDataInputDamstart'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputDamstart'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__inputPdbFile is not None:
			self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
		else:
			warnEmptyAttribute("inputPdbFile", "XSDataFile")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'inputPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setInputPdbFile(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputDamstart")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputDamstart')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputDamstart is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputDamstart.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamstart()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputDamstart")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputDamstart()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputDamstart

class XSDataInputGnom(XSDataInput):
	"""Input data can be provided either as a list of doubles, as Arrays or as a filename"""
	def __init__(self, configuration=None, mode=None, angularScale=None, experimentalDataFile=None, experimentalDataStdArray=None, experimentalDataStdDev=None, experimentalDataIArray=None, experimentalDataValues=None, experimentalDataQArray=None, experimentalDataQ=None, rMax=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", rMax, "XSDataDouble")
		self.__rMax = rMax
		if experimentalDataQ is None:
			self.__experimentalDataQ = []
		else:
			checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataQ, "list")
			self.__experimentalDataQ = experimentalDataQ
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataQArray, "XSDataArray")
		self.__experimentalDataQArray = experimentalDataQArray
		if experimentalDataValues is None:
			self.__experimentalDataValues = []
		else:
			checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataValues, "list")
			self.__experimentalDataValues = experimentalDataValues
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataIArray, "XSDataArray")
		self.__experimentalDataIArray = experimentalDataIArray
		if experimentalDataStdDev is None:
			self.__experimentalDataStdDev = []
		else:
			checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataStdDev, "list")
			self.__experimentalDataStdDev = experimentalDataStdDev
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataStdArray, "XSDataArray")
		self.__experimentalDataStdArray = experimentalDataStdArray
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", experimentalDataFile, "XSDataFile")
		self.__experimentalDataFile = experimentalDataFile
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", angularScale, "XSDataInteger")
		self.__angularScale = angularScale
		checkType("XSDataInputGnom", "Constructor of XSDataInputGnom", mode, "XSDataString")
		self.__mode = mode
	def getRMax(self): return self.__rMax
	def setRMax(self, rMax):
		checkType("XSDataInputGnom", "setRMax", rMax, "XSDataDouble")
		self.__rMax = rMax
	def delRMax(self): self.__rMax = None
	# Properties
	rMax = property(getRMax, setRMax, delRMax, "Property for rMax")
	def getExperimentalDataQ(self): return self.__experimentalDataQ
	def setExperimentalDataQ(self, experimentalDataQ):
		checkType("XSDataInputGnom", "setExperimentalDataQ", experimentalDataQ, "list")
		self.__experimentalDataQ = experimentalDataQ
	def delExperimentalDataQ(self): self.__experimentalDataQ = None
	# Properties
	experimentalDataQ = property(getExperimentalDataQ, setExperimentalDataQ, delExperimentalDataQ, "Property for experimentalDataQ")
	def addExperimentalDataQ(self, value):
		checkType("XSDataInputGnom", "setExperimentalDataQ", value, "XSDataDouble")
		self.__experimentalDataQ.append(value)
	def insertExperimentalDataQ(self, index, value):
		checkType("XSDataInputGnom", "setExperimentalDataQ", value, "XSDataDouble")
		self.__experimentalDataQ[index] = value
	def getExperimentalDataQArray(self): return self.__experimentalDataQArray
	def setExperimentalDataQArray(self, experimentalDataQArray):
		checkType("XSDataInputGnom", "setExperimentalDataQArray", experimentalDataQArray, "XSDataArray")
		self.__experimentalDataQArray = experimentalDataQArray
	def delExperimentalDataQArray(self): self.__experimentalDataQArray = None
	# Properties
	experimentalDataQArray = property(getExperimentalDataQArray, setExperimentalDataQArray, delExperimentalDataQArray, "Property for experimentalDataQArray")
	def getExperimentalDataValues(self): return self.__experimentalDataValues
	def setExperimentalDataValues(self, experimentalDataValues):
		checkType("XSDataInputGnom", "setExperimentalDataValues", experimentalDataValues, "list")
		self.__experimentalDataValues = experimentalDataValues
	def delExperimentalDataValues(self): self.__experimentalDataValues = None
	# Properties
	experimentalDataValues = property(getExperimentalDataValues, setExperimentalDataValues, delExperimentalDataValues, "Property for experimentalDataValues")
	def addExperimentalDataValues(self, value):
		checkType("XSDataInputGnom", "setExperimentalDataValues", value, "XSDataDouble")
		self.__experimentalDataValues.append(value)
	def insertExperimentalDataValues(self, index, value):
		checkType("XSDataInputGnom", "setExperimentalDataValues", value, "XSDataDouble")
		self.__experimentalDataValues[index] = value
	def getExperimentalDataIArray(self): return self.__experimentalDataIArray
	def setExperimentalDataIArray(self, experimentalDataIArray):
		checkType("XSDataInputGnom", "setExperimentalDataIArray", experimentalDataIArray, "XSDataArray")
		self.__experimentalDataIArray = experimentalDataIArray
	def delExperimentalDataIArray(self): self.__experimentalDataIArray = None
	# Properties
	experimentalDataIArray = property(getExperimentalDataIArray, setExperimentalDataIArray, delExperimentalDataIArray, "Property for experimentalDataIArray")
	def getExperimentalDataStdDev(self): return self.__experimentalDataStdDev
	def setExperimentalDataStdDev(self, experimentalDataStdDev):
		checkType("XSDataInputGnom", "setExperimentalDataStdDev", experimentalDataStdDev, "list")
		self.__experimentalDataStdDev = experimentalDataStdDev
	def delExperimentalDataStdDev(self): self.__experimentalDataStdDev = None
	# Properties
	experimentalDataStdDev = property(getExperimentalDataStdDev, setExperimentalDataStdDev, delExperimentalDataStdDev, "Property for experimentalDataStdDev")
	def addExperimentalDataStdDev(self, value):
		checkType("XSDataInputGnom", "setExperimentalDataStdDev", value, "XSDataDouble")
		self.__experimentalDataStdDev.append(value)
	def insertExperimentalDataStdDev(self, index, value):
		checkType("XSDataInputGnom", "setExperimentalDataStdDev", value, "XSDataDouble")
		self.__experimentalDataStdDev[index] = value
	def getExperimentalDataStdArray(self): return self.__experimentalDataStdArray
	def setExperimentalDataStdArray(self, experimentalDataStdArray):
		checkType("XSDataInputGnom", "setExperimentalDataStdArray", experimentalDataStdArray, "XSDataArray")
		self.__experimentalDataStdArray = experimentalDataStdArray
	def delExperimentalDataStdArray(self): self.__experimentalDataStdArray = None
	# Properties
	experimentalDataStdArray = property(getExperimentalDataStdArray, setExperimentalDataStdArray, delExperimentalDataStdArray, "Property for experimentalDataStdArray")
	def getExperimentalDataFile(self): return self.__experimentalDataFile
	def setExperimentalDataFile(self, experimentalDataFile):
		checkType("XSDataInputGnom", "setExperimentalDataFile", experimentalDataFile, "XSDataFile")
		self.__experimentalDataFile = experimentalDataFile
	def delExperimentalDataFile(self): self.__experimentalDataFile = None
	# Properties
	experimentalDataFile = property(getExperimentalDataFile, setExperimentalDataFile, delExperimentalDataFile, "Property for experimentalDataFile")
	def getAngularScale(self): return self.__angularScale
	def setAngularScale(self, angularScale):
		checkType("XSDataInputGnom", "setAngularScale", angularScale, "XSDataInteger")
		self.__angularScale = angularScale
	def delAngularScale(self): self.__angularScale = None
	# Properties
	angularScale = property(getAngularScale, setAngularScale, delAngularScale, "Property for angularScale")
	def getMode(self): return self.__mode
	def setMode(self, mode):
		checkType("XSDataInputGnom", "setMode", mode, "XSDataString")
		self.__mode = mode
	def delMode(self): self.__mode = None
	# Properties
	mode = property(getMode, setMode, delMode, "Property for mode")
	def export(self, outfile, level, name_='XSDataInputGnom'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputGnom'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__rMax is not None:
			self.rMax.export(outfile, level, name_='rMax')
		else:
			warnEmptyAttribute("rMax", "XSDataDouble")
		for experimentalDataQ_ in self.getExperimentalDataQ():
			experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
		if self.__experimentalDataQArray is not None:
			self.experimentalDataQArray.export(outfile, level, name_='experimentalDataQArray')
		for experimentalDataValues_ in self.getExperimentalDataValues():
			experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
		if self.__experimentalDataIArray is not None:
			self.experimentalDataIArray.export(outfile, level, name_='experimentalDataIArray')
		for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
			experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
		if self.__experimentalDataStdArray is not None:
			self.experimentalDataStdArray.export(outfile, level, name_='experimentalDataStdArray')
		if self.__experimentalDataFile is not None:
			self.experimentalDataFile.export(outfile, level, name_='experimentalDataFile')
		if self.__angularScale is not None:
			self.angularScale.export(outfile, level, name_='angularScale')
		if self.__mode is not None:
			self.mode.export(outfile, level, name_='mode')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRMax(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataQ':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataQ.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataQArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataQArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataValues':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataValues.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataIArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataIArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataStdDev':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataStdDev.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataStdArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataStdArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setExperimentalDataFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angularScale':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setAngularScale(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMode(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputGnom")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputGnom')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputGnom is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputGnom.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputGnom()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputGnom")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputGnom()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputGnom

class XSDataInputSolutionScattering(XSDataInput):
	def __init__(self, configuration=None, qMax=None, qMin=None, plotFit=None, onlyGnom=None, iNbThreads=None, mode=None, symmetry=None, angularUnits=None, rMaxSearchSettings=None, experimentalDataFile=None, experimentalDataStdArray=None, experimentalDataStdDev=None, experimentalDataIArray=None, experimentalDataValues=None, experimentalDataQArray=None, experimentalDataQ=None, title=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", title, "XSDataString")
		self.__title = title
		if experimentalDataQ is None:
			self.__experimentalDataQ = []
		else:
			checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataQ, "list")
			self.__experimentalDataQ = experimentalDataQ
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataQArray, "XSDataArray")
		self.__experimentalDataQArray = experimentalDataQArray
		if experimentalDataValues is None:
			self.__experimentalDataValues = []
		else:
			checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataValues, "list")
			self.__experimentalDataValues = experimentalDataValues
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataIArray, "XSDataArray")
		self.__experimentalDataIArray = experimentalDataIArray
		if experimentalDataStdDev is None:
			self.__experimentalDataStdDev = []
		else:
			checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataStdDev, "list")
			self.__experimentalDataStdDev = experimentalDataStdDev
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataStdArray, "XSDataArray")
		self.__experimentalDataStdArray = experimentalDataStdArray
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataFile, "XSDataFile")
		self.__experimentalDataFile = experimentalDataFile
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", rMaxSearchSettings, "XSDataSolutionScatteringSettings")
		self.__rMaxSearchSettings = rMaxSearchSettings
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", angularUnits, "XSDataInteger")
		self.__angularUnits = angularUnits
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", symmetry, "XSDataString")
		self.__symmetry = symmetry
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", mode, "XSDataString")
		self.__mode = mode
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", iNbThreads, "XSDataInteger")
		self.__iNbThreads = iNbThreads
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", onlyGnom, "XSDataBoolean")
		self.__onlyGnom = onlyGnom
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", plotFit, "XSDataBoolean")
		self.__plotFit = plotFit
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", qMin, "XSDataDouble")
		self.__qMin = qMin
		checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", qMax, "XSDataDouble")
		self.__qMax = qMax
	def getTitle(self): return self.__title
	def setTitle(self, title):
		checkType("XSDataInputSolutionScattering", "setTitle", title, "XSDataString")
		self.__title = title
	def delTitle(self): self.__title = None
	# Properties
	title = property(getTitle, setTitle, delTitle, "Property for title")
	def getExperimentalDataQ(self): return self.__experimentalDataQ
	def setExperimentalDataQ(self, experimentalDataQ):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", experimentalDataQ, "list")
		self.__experimentalDataQ = experimentalDataQ
	def delExperimentalDataQ(self): self.__experimentalDataQ = None
	# Properties
	experimentalDataQ = property(getExperimentalDataQ, setExperimentalDataQ, delExperimentalDataQ, "Property for experimentalDataQ")
	def addExperimentalDataQ(self, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", value, "XSDataDouble")
		self.__experimentalDataQ.append(value)
	def insertExperimentalDataQ(self, index, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", value, "XSDataDouble")
		self.__experimentalDataQ[index] = value
	def getExperimentalDataQArray(self): return self.__experimentalDataQArray
	def setExperimentalDataQArray(self, experimentalDataQArray):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataQArray", experimentalDataQArray, "XSDataArray")
		self.__experimentalDataQArray = experimentalDataQArray
	def delExperimentalDataQArray(self): self.__experimentalDataQArray = None
	# Properties
	experimentalDataQArray = property(getExperimentalDataQArray, setExperimentalDataQArray, delExperimentalDataQArray, "Property for experimentalDataQArray")
	def getExperimentalDataValues(self): return self.__experimentalDataValues
	def setExperimentalDataValues(self, experimentalDataValues):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", experimentalDataValues, "list")
		self.__experimentalDataValues = experimentalDataValues
	def delExperimentalDataValues(self): self.__experimentalDataValues = None
	# Properties
	experimentalDataValues = property(getExperimentalDataValues, setExperimentalDataValues, delExperimentalDataValues, "Property for experimentalDataValues")
	def addExperimentalDataValues(self, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", value, "XSDataDouble")
		self.__experimentalDataValues.append(value)
	def insertExperimentalDataValues(self, index, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", value, "XSDataDouble")
		self.__experimentalDataValues[index] = value
	def getExperimentalDataIArray(self): return self.__experimentalDataIArray
	def setExperimentalDataIArray(self, experimentalDataIArray):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataIArray", experimentalDataIArray, "XSDataArray")
		self.__experimentalDataIArray = experimentalDataIArray
	def delExperimentalDataIArray(self): self.__experimentalDataIArray = None
	# Properties
	experimentalDataIArray = property(getExperimentalDataIArray, setExperimentalDataIArray, delExperimentalDataIArray, "Property for experimentalDataIArray")
	def getExperimentalDataStdDev(self): return self.__experimentalDataStdDev
	def setExperimentalDataStdDev(self, experimentalDataStdDev):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", experimentalDataStdDev, "list")
		self.__experimentalDataStdDev = experimentalDataStdDev
	def delExperimentalDataStdDev(self): self.__experimentalDataStdDev = None
	# Properties
	experimentalDataStdDev = property(getExperimentalDataStdDev, setExperimentalDataStdDev, delExperimentalDataStdDev, "Property for experimentalDataStdDev")
	def addExperimentalDataStdDev(self, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", value, "XSDataDouble")
		self.__experimentalDataStdDev.append(value)
	def insertExperimentalDataStdDev(self, index, value):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", value, "XSDataDouble")
		self.__experimentalDataStdDev[index] = value
	def getExperimentalDataStdArray(self): return self.__experimentalDataStdArray
	def setExperimentalDataStdArray(self, experimentalDataStdArray):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataStdArray", experimentalDataStdArray, "XSDataArray")
		self.__experimentalDataStdArray = experimentalDataStdArray
	def delExperimentalDataStdArray(self): self.__experimentalDataStdArray = None
	# Properties
	experimentalDataStdArray = property(getExperimentalDataStdArray, setExperimentalDataStdArray, delExperimentalDataStdArray, "Property for experimentalDataStdArray")
	def getExperimentalDataFile(self): return self.__experimentalDataFile
	def setExperimentalDataFile(self, experimentalDataFile):
		checkType("XSDataInputSolutionScattering", "setExperimentalDataFile", experimentalDataFile, "XSDataFile")
		self.__experimentalDataFile = experimentalDataFile
	def delExperimentalDataFile(self): self.__experimentalDataFile = None
	# Properties
	experimentalDataFile = property(getExperimentalDataFile, setExperimentalDataFile, delExperimentalDataFile, "Property for experimentalDataFile")
	def getRMaxSearchSettings(self): return self.__rMaxSearchSettings
	def setRMaxSearchSettings(self, rMaxSearchSettings):
		checkType("XSDataInputSolutionScattering", "setRMaxSearchSettings", rMaxSearchSettings, "XSDataSolutionScatteringSettings")
		self.__rMaxSearchSettings = rMaxSearchSettings
	def delRMaxSearchSettings(self): self.__rMaxSearchSettings = None
	# Properties
	rMaxSearchSettings = property(getRMaxSearchSettings, setRMaxSearchSettings, delRMaxSearchSettings, "Property for rMaxSearchSettings")
	def getAngularUnits(self): return self.__angularUnits
	def setAngularUnits(self, angularUnits):
		checkType("XSDataInputSolutionScattering", "setAngularUnits", angularUnits, "XSDataInteger")
		self.__angularUnits = angularUnits
	def delAngularUnits(self): self.__angularUnits = None
	# Properties
	angularUnits = property(getAngularUnits, setAngularUnits, delAngularUnits, "Property for angularUnits")
	def getSymmetry(self): return self.__symmetry
	def setSymmetry(self, symmetry):
		checkType("XSDataInputSolutionScattering", "setSymmetry", symmetry, "XSDataString")
		self.__symmetry = symmetry
	def delSymmetry(self): self.__symmetry = None
	# Properties
	symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
	def getMode(self): return self.__mode
	def setMode(self, mode):
		checkType("XSDataInputSolutionScattering", "setMode", mode, "XSDataString")
		self.__mode = mode
	def delMode(self): self.__mode = None
	# Properties
	mode = property(getMode, setMode, delMode, "Property for mode")
	def getINbThreads(self): return self.__iNbThreads
	def setINbThreads(self, iNbThreads):
		checkType("XSDataInputSolutionScattering", "setINbThreads", iNbThreads, "XSDataInteger")
		self.__iNbThreads = iNbThreads
	def delINbThreads(self): self.__iNbThreads = None
	# Properties
	iNbThreads = property(getINbThreads, setINbThreads, delINbThreads, "Property for iNbThreads")
	def getOnlyGnom(self): return self.__onlyGnom
	def setOnlyGnom(self, onlyGnom):
		checkType("XSDataInputSolutionScattering", "setOnlyGnom", onlyGnom, "XSDataBoolean")
		self.__onlyGnom = onlyGnom
	def delOnlyGnom(self): self.__onlyGnom = None
	# Properties
	onlyGnom = property(getOnlyGnom, setOnlyGnom, delOnlyGnom, "Property for onlyGnom")
	def getPlotFit(self): return self.__plotFit
	def setPlotFit(self, plotFit):
		checkType("XSDataInputSolutionScattering", "setPlotFit", plotFit, "XSDataBoolean")
		self.__plotFit = plotFit
	def delPlotFit(self): self.__plotFit = None
	# Properties
	plotFit = property(getPlotFit, setPlotFit, delPlotFit, "Property for plotFit")
	def getQMin(self): return self.__qMin
	def setQMin(self, qMin):
		checkType("XSDataInputSolutionScattering", "setQMin", qMin, "XSDataDouble")
		self.__qMin = qMin
	def delQMin(self): self.__qMin = None
	# Properties
	qMin = property(getQMin, setQMin, delQMin, "Property for qMin")
	def getQMax(self): return self.__qMax
	def setQMax(self, qMax):
		checkType("XSDataInputSolutionScattering", "setQMax", qMax, "XSDataDouble")
		self.__qMax = qMax
	def delQMax(self): self.__qMax = None
	# Properties
	qMax = property(getQMax, setQMax, delQMax, "Property for qMax")
	def export(self, outfile, level, name_='XSDataInputSolutionScattering'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSolutionScattering'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__title is not None:
			self.title.export(outfile, level, name_='title')
		for experimentalDataQ_ in self.getExperimentalDataQ():
			experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
		if self.__experimentalDataQArray is not None:
			self.experimentalDataQArray.export(outfile, level, name_='experimentalDataQArray')
		for experimentalDataValues_ in self.getExperimentalDataValues():
			experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
		if self.__experimentalDataIArray is not None:
			self.experimentalDataIArray.export(outfile, level, name_='experimentalDataIArray')
		for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
			experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
		if self.__experimentalDataStdArray is not None:
			self.experimentalDataStdArray.export(outfile, level, name_='experimentalDataStdArray')
		if self.__experimentalDataFile is not None:
			self.experimentalDataFile.export(outfile, level, name_='experimentalDataFile')
		if self.__rMaxSearchSettings is not None:
			self.rMaxSearchSettings.export(outfile, level, name_='rMaxSearchSettings')
		if self.__angularUnits is not None:
			self.angularUnits.export(outfile, level, name_='angularUnits')
		if self.__symmetry is not None:
			self.symmetry.export(outfile, level, name_='symmetry')
		if self.__mode is not None:
			self.mode.export(outfile, level, name_='mode')
		if self.__iNbThreads is not None:
			self.iNbThreads.export(outfile, level, name_='iNbThreads')
		if self.__onlyGnom is not None:
			self.onlyGnom.export(outfile, level, name_='onlyGnom')
		if self.__plotFit is not None:
			self.plotFit.export(outfile, level, name_='plotFit')
		if self.__qMin is not None:
			self.qMin.export(outfile, level, name_='qMin')
		if self.__qMax is not None:
			self.qMax.export(outfile, level, name_='qMax')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'title':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setTitle(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataQ':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataQ.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataQArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataQArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataValues':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataValues.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataIArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataIArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataStdDev':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.experimentalDataStdDev.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataStdArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setExperimentalDataStdArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'experimentalDataFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setExperimentalDataFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rMaxSearchSettings':
			obj_ = XSDataSolutionScatteringSettings()
			obj_.build(child_)
			self.setRMaxSearchSettings(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'angularUnits':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setAngularUnits(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symmetry':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymmetry(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'mode':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setMode(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'iNbThreads':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setINbThreads(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'onlyGnom':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setOnlyGnom(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'plotFit':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setPlotFit(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qMin':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setQMin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'qMax':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setQMax(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputSolutionScattering")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputSolutionScattering')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputSolutionScattering is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputSolutionScattering.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSolutionScattering()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputSolutionScattering")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSolutionScattering()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputSolutionScattering

class XSDataInputSupcomb(XSDataInput):
	def __init__(self, configuration=None, backbone=None, enantiomorphs=None, superimposeFile=None, templateFile=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", templateFile, "XSDataFile")
		self.__templateFile = templateFile
		checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", superimposeFile, "XSDataFile")
		self.__superimposeFile = superimposeFile
		checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", enantiomorphs, "XSDataBoolean")
		self.__enantiomorphs = enantiomorphs
		checkType("XSDataInputSupcomb", "Constructor of XSDataInputSupcomb", backbone, "XSDataBoolean")
		self.__backbone = backbone
	def getTemplateFile(self): return self.__templateFile
	def setTemplateFile(self, templateFile):
		checkType("XSDataInputSupcomb", "setTemplateFile", templateFile, "XSDataFile")
		self.__templateFile = templateFile
	def delTemplateFile(self): self.__templateFile = None
	# Properties
	templateFile = property(getTemplateFile, setTemplateFile, delTemplateFile, "Property for templateFile")
	def getSuperimposeFile(self): return self.__superimposeFile
	def setSuperimposeFile(self, superimposeFile):
		checkType("XSDataInputSupcomb", "setSuperimposeFile", superimposeFile, "XSDataFile")
		self.__superimposeFile = superimposeFile
	def delSuperimposeFile(self): self.__superimposeFile = None
	# Properties
	superimposeFile = property(getSuperimposeFile, setSuperimposeFile, delSuperimposeFile, "Property for superimposeFile")
	def getEnantiomorphs(self): return self.__enantiomorphs
	def setEnantiomorphs(self, enantiomorphs):
		checkType("XSDataInputSupcomb", "setEnantiomorphs", enantiomorphs, "XSDataBoolean")
		self.__enantiomorphs = enantiomorphs
	def delEnantiomorphs(self): self.__enantiomorphs = None
	# Properties
	enantiomorphs = property(getEnantiomorphs, setEnantiomorphs, delEnantiomorphs, "Property for enantiomorphs")
	def getBackbone(self): return self.__backbone
	def setBackbone(self, backbone):
		checkType("XSDataInputSupcomb", "setBackbone", backbone, "XSDataBoolean")
		self.__backbone = backbone
	def delBackbone(self): self.__backbone = None
	# Properties
	backbone = property(getBackbone, setBackbone, delBackbone, "Property for backbone")
	def export(self, outfile, level, name_='XSDataInputSupcomb'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataInputSupcomb'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__templateFile is not None:
			self.templateFile.export(outfile, level, name_='templateFile')
		else:
			warnEmptyAttribute("templateFile", "XSDataFile")
		if self.__superimposeFile is not None:
			self.superimposeFile.export(outfile, level, name_='superimposeFile')
		else:
			warnEmptyAttribute("superimposeFile", "XSDataFile")
		if self.__enantiomorphs is not None:
			self.enantiomorphs.export(outfile, level, name_='enantiomorphs')
		if self.__backbone is not None:
			self.backbone.export(outfile, level, name_='backbone')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'templateFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setTemplateFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'superimposeFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setSuperimposeFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'enantiomorphs':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setEnantiomorphs(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'backbone':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setBackbone(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataInputSupcomb")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataInputSupcomb')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataInputSupcomb is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataInputSupcomb.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataInputSupcomb()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataInputSupcomb")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataInputSupcomb()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataInputSupcomb

class XSDataResultDamaver(XSDataResult):
	def __init__(self, status=None, damstartPdbFile=None, damfilterPdbFile=None, damaverPdbFile=None, variationNSD=None, meanNSD=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", meanNSD, "XSDataDouble")
		self.__meanNSD = meanNSD
		checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", variationNSD, "XSDataDouble")
		self.__variationNSD = variationNSD
		checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damaverPdbFile, "XSDataFile")
		self.__damaverPdbFile = damaverPdbFile
		checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damfilterPdbFile, "XSDataFile")
		self.__damfilterPdbFile = damfilterPdbFile
		checkType("XSDataResultDamaver", "Constructor of XSDataResultDamaver", damstartPdbFile, "XSDataFile")
		self.__damstartPdbFile = damstartPdbFile
	def getMeanNSD(self): return self.__meanNSD
	def setMeanNSD(self, meanNSD):
		checkType("XSDataResultDamaver", "setMeanNSD", meanNSD, "XSDataDouble")
		self.__meanNSD = meanNSD
	def delMeanNSD(self): self.__meanNSD = None
	# Properties
	meanNSD = property(getMeanNSD, setMeanNSD, delMeanNSD, "Property for meanNSD")
	def getVariationNSD(self): return self.__variationNSD
	def setVariationNSD(self, variationNSD):
		checkType("XSDataResultDamaver", "setVariationNSD", variationNSD, "XSDataDouble")
		self.__variationNSD = variationNSD
	def delVariationNSD(self): self.__variationNSD = None
	# Properties
	variationNSD = property(getVariationNSD, setVariationNSD, delVariationNSD, "Property for variationNSD")
	def getDamaverPdbFile(self): return self.__damaverPdbFile
	def setDamaverPdbFile(self, damaverPdbFile):
		checkType("XSDataResultDamaver", "setDamaverPdbFile", damaverPdbFile, "XSDataFile")
		self.__damaverPdbFile = damaverPdbFile
	def delDamaverPdbFile(self): self.__damaverPdbFile = None
	# Properties
	damaverPdbFile = property(getDamaverPdbFile, setDamaverPdbFile, delDamaverPdbFile, "Property for damaverPdbFile")
	def getDamfilterPdbFile(self): return self.__damfilterPdbFile
	def setDamfilterPdbFile(self, damfilterPdbFile):
		checkType("XSDataResultDamaver", "setDamfilterPdbFile", damfilterPdbFile, "XSDataFile")
		self.__damfilterPdbFile = damfilterPdbFile
	def delDamfilterPdbFile(self): self.__damfilterPdbFile = None
	# Properties
	damfilterPdbFile = property(getDamfilterPdbFile, setDamfilterPdbFile, delDamfilterPdbFile, "Property for damfilterPdbFile")
	def getDamstartPdbFile(self): return self.__damstartPdbFile
	def setDamstartPdbFile(self, damstartPdbFile):
		checkType("XSDataResultDamaver", "setDamstartPdbFile", damstartPdbFile, "XSDataFile")
		self.__damstartPdbFile = damstartPdbFile
	def delDamstartPdbFile(self): self.__damstartPdbFile = None
	# Properties
	damstartPdbFile = property(getDamstartPdbFile, setDamstartPdbFile, delDamstartPdbFile, "Property for damstartPdbFile")
	def export(self, outfile, level, name_='XSDataResultDamaver'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDamaver'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__meanNSD is not None:
			self.meanNSD.export(outfile, level, name_='meanNSD')
		if self.__variationNSD is not None:
			self.variationNSD.export(outfile, level, name_='variationNSD')
		if self.__damaverPdbFile is not None:
			self.damaverPdbFile.export(outfile, level, name_='damaverPdbFile')
		if self.__damfilterPdbFile is not None:
			self.damfilterPdbFile.export(outfile, level, name_='damfilterPdbFile')
		if self.__damstartPdbFile is not None:
			self.damstartPdbFile.export(outfile, level, name_='damstartPdbFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'meanNSD':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMeanNSD(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'variationNSD':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setVariationNSD(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'damaverPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDamaverPdbFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'damfilterPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDamfilterPdbFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'damstartPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setDamstartPdbFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultDamaver")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultDamaver')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultDamaver is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultDamaver.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamaver()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultDamaver")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamaver()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultDamaver

class XSDataResultDamfilt(XSDataResult):
	def __init__(self, status=None, outputPdbFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDamfilt", "Constructor of XSDataResultDamfilt", outputPdbFile, "XSDataFile")
		self.__outputPdbFile = outputPdbFile
	def getOutputPdbFile(self): return self.__outputPdbFile
	def setOutputPdbFile(self, outputPdbFile):
		checkType("XSDataResultDamfilt", "setOutputPdbFile", outputPdbFile, "XSDataFile")
		self.__outputPdbFile = outputPdbFile
	def delOutputPdbFile(self): self.__outputPdbFile = None
	# Properties
	outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
	def export(self, outfile, level, name_='XSDataResultDamfilt'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDamfilt'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputPdbFile is not None:
			self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputPdbFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultDamfilt")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultDamfilt')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultDamfilt is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultDamfilt.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamfilt()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultDamfilt")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamfilt()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultDamfilt

class XSDataResultDammif(XSDataResult):
	def __init__(self, status=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", fitFile, "XSDataFile")
		self.__fitFile = fitFile
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", rfactor, "XSDataDouble")
		self.__rfactor = rfactor
		checkType("XSDataResultDammif", "Constructor of XSDataResultDammif", chiSqrt, "XSDataDouble")
		self.__chiSqrt = chiSqrt
	def getFitFile(self): return self.__fitFile
	def setFitFile(self, fitFile):
		checkType("XSDataResultDammif", "setFitFile", fitFile, "XSDataFile")
		self.__fitFile = fitFile
	def delFitFile(self): self.__fitFile = None
	# Properties
	fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataResultDammif", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getPdbMoleculeFile(self): return self.__pdbMoleculeFile
	def setPdbMoleculeFile(self, pdbMoleculeFile):
		checkType("XSDataResultDammif", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
	def delPdbMoleculeFile(self): self.__pdbMoleculeFile = None
	# Properties
	pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
	def getPdbSolventFile(self): return self.__pdbSolventFile
	def setPdbSolventFile(self, pdbSolventFile):
		checkType("XSDataResultDammif", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
	def delPdbSolventFile(self): self.__pdbSolventFile = None
	# Properties
	pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
	def getRfactor(self): return self.__rfactor
	def setRfactor(self, rfactor):
		checkType("XSDataResultDammif", "setRfactor", rfactor, "XSDataDouble")
		self.__rfactor = rfactor
	def delRfactor(self): self.__rfactor = None
	# Properties
	rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
	def getChiSqrt(self): return self.__chiSqrt
	def setChiSqrt(self, chiSqrt):
		checkType("XSDataResultDammif", "setChiSqrt", chiSqrt, "XSDataDouble")
		self.__chiSqrt = chiSqrt
	def delChiSqrt(self): self.__chiSqrt = None
	# Properties
	chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
	def export(self, outfile, level, name_='XSDataResultDammif'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDammif'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__fitFile is not None:
			self.fitFile.export(outfile, level, name_='fitFile')
		else:
			warnEmptyAttribute("fitFile", "XSDataFile")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
		if self.__pdbMoleculeFile is not None:
			self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
		else:
			warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
		if self.__pdbSolventFile is not None:
			self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
		else:
			warnEmptyAttribute("pdbSolventFile", "XSDataFile")
		if self.__rfactor is not None:
			self.rfactor.export(outfile, level, name_='rfactor')
		if self.__chiSqrt is not None:
			self.chiSqrt.export(outfile, level, name_='chiSqrt')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fitFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFitFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbMoleculeFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbMoleculeFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbSolventFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbSolventFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rfactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRfactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chiSqrt':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setChiSqrt(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultDammif")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultDammif')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultDammif is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultDammif.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDammif()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultDammif")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDammif()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultDammif

class XSDataResultDammin(XSDataResult):
	def __init__(self, status=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", fitFile, "XSDataFile")
		self.__fitFile = fitFile
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", rfactor, "XSDataDouble")
		self.__rfactor = rfactor
		checkType("XSDataResultDammin", "Constructor of XSDataResultDammin", chiSqrt, "XSDataDouble")
		self.__chiSqrt = chiSqrt
	def getFitFile(self): return self.__fitFile
	def setFitFile(self, fitFile):
		checkType("XSDataResultDammin", "setFitFile", fitFile, "XSDataFile")
		self.__fitFile = fitFile
	def delFitFile(self): self.__fitFile = None
	# Properties
	fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataResultDammin", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getPdbMoleculeFile(self): return self.__pdbMoleculeFile
	def setPdbMoleculeFile(self, pdbMoleculeFile):
		checkType("XSDataResultDammin", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
	def delPdbMoleculeFile(self): self.__pdbMoleculeFile = None
	# Properties
	pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
	def getPdbSolventFile(self): return self.__pdbSolventFile
	def setPdbSolventFile(self, pdbSolventFile):
		checkType("XSDataResultDammin", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
	def delPdbSolventFile(self): self.__pdbSolventFile = None
	# Properties
	pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
	def getRfactor(self): return self.__rfactor
	def setRfactor(self, rfactor):
		checkType("XSDataResultDammin", "setRfactor", rfactor, "XSDataDouble")
		self.__rfactor = rfactor
	def delRfactor(self): self.__rfactor = None
	# Properties
	rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
	def getChiSqrt(self): return self.__chiSqrt
	def setChiSqrt(self, chiSqrt):
		checkType("XSDataResultDammin", "setChiSqrt", chiSqrt, "XSDataDouble")
		self.__chiSqrt = chiSqrt
	def delChiSqrt(self): self.__chiSqrt = None
	# Properties
	chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
	def export(self, outfile, level, name_='XSDataResultDammin'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDammin'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__fitFile is not None:
			self.fitFile.export(outfile, level, name_='fitFile')
		else:
			warnEmptyAttribute("fitFile", "XSDataFile")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
		if self.__pdbMoleculeFile is not None:
			self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
		else:
			warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
		if self.__pdbSolventFile is not None:
			self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
		else:
			warnEmptyAttribute("pdbSolventFile", "XSDataFile")
		if self.__rfactor is not None:
			self.rfactor.export(outfile, level, name_='rfactor')
		if self.__chiSqrt is not None:
			self.chiSqrt.export(outfile, level, name_='chiSqrt')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fitFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFitFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbMoleculeFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbMoleculeFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbSolventFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbSolventFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rfactor':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRfactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'chiSqrt':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setChiSqrt(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultDammin")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultDammin')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultDammin is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultDammin.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDammin()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultDammin")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDammin()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultDammin

class XSDataResultDamstart(XSDataResult):
	def __init__(self, status=None, outputPdbFile=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultDamstart", "Constructor of XSDataResultDamstart", outputPdbFile, "XSDataFile")
		self.__outputPdbFile = outputPdbFile
	def getOutputPdbFile(self): return self.__outputPdbFile
	def setOutputPdbFile(self, outputPdbFile):
		checkType("XSDataResultDamstart", "setOutputPdbFile", outputPdbFile, "XSDataFile")
		self.__outputPdbFile = outputPdbFile
	def delOutputPdbFile(self): self.__outputPdbFile = None
	# Properties
	outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
	def export(self, outfile, level, name_='XSDataResultDamstart'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultDamstart'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputPdbFile is not None:
			self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outputPdbFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutputPdbFile(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultDamstart")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultDamstart')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultDamstart is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultDamstart.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamstart()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultDamstart")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultDamstart()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultDamstart

class XSDataResultGnom(XSDataResult):
	def __init__(self, status=None, radiusOfGyration=None, radiusOfCrossSection=None, arrayErr=None, arrayPr=None, arrayR=None, distributionErr=None, distributionPr=None, distributionR=None, scatteringFitIArray=None, scatteringFitQArray=None, scatteringFitValues=None, scatteringFitQ=None, output=None, fitQuality=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", fitQuality, "XSDataDouble")
		self.__fitQuality = fitQuality
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", output, "XSDataFile")
		self.__output = output
		if scatteringFitQ is None:
			self.__scatteringFitQ = []
		else:
			checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitQ, "list")
			self.__scatteringFitQ = scatteringFitQ
		if scatteringFitValues is None:
			self.__scatteringFitValues = []
		else:
			checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitValues, "list")
			self.__scatteringFitValues = scatteringFitValues
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitQArray, "XSDataArray")
		self.__scatteringFitQArray = scatteringFitQArray
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", scatteringFitIArray, "XSDataArray")
		self.__scatteringFitIArray = scatteringFitIArray
		if distributionR is None:
			self.__distributionR = []
		else:
			checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionR, "list")
			self.__distributionR = distributionR
		if distributionPr is None:
			self.__distributionPr = []
		else:
			checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionPr, "list")
			self.__distributionPr = distributionPr
		if distributionErr is None:
			self.__distributionErr = []
		else:
			checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", distributionErr, "list")
			self.__distributionErr = distributionErr
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayR, "XSDataArray")
		self.__arrayR = arrayR
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayPr, "XSDataArray")
		self.__arrayPr = arrayPr
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", arrayErr, "XSDataArray")
		self.__arrayErr = arrayErr
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", radiusOfCrossSection, "XSDataDouble")
		self.__radiusOfCrossSection = radiusOfCrossSection
		checkType("XSDataResultGnom", "Constructor of XSDataResultGnom", radiusOfGyration, "XSDataDouble")
		self.__radiusOfGyration = radiusOfGyration
	def getFitQuality(self): return self.__fitQuality
	def setFitQuality(self, fitQuality):
		checkType("XSDataResultGnom", "setFitQuality", fitQuality, "XSDataDouble")
		self.__fitQuality = fitQuality
	def delFitQuality(self): self.__fitQuality = None
	# Properties
	fitQuality = property(getFitQuality, setFitQuality, delFitQuality, "Property for fitQuality")
	def getOutput(self): return self.__output
	def setOutput(self, output):
		checkType("XSDataResultGnom", "setOutput", output, "XSDataFile")
		self.__output = output
	def delOutput(self): self.__output = None
	# Properties
	output = property(getOutput, setOutput, delOutput, "Property for output")
	def getScatteringFitQ(self): return self.__scatteringFitQ
	def setScatteringFitQ(self, scatteringFitQ):
		checkType("XSDataResultGnom", "setScatteringFitQ", scatteringFitQ, "list")
		self.__scatteringFitQ = scatteringFitQ
	def delScatteringFitQ(self): self.__scatteringFitQ = None
	# Properties
	scatteringFitQ = property(getScatteringFitQ, setScatteringFitQ, delScatteringFitQ, "Property for scatteringFitQ")
	def addScatteringFitQ(self, value):
		checkType("XSDataResultGnom", "setScatteringFitQ", value, "XSDataDouble")
		self.__scatteringFitQ.append(value)
	def insertScatteringFitQ(self, index, value):
		checkType("XSDataResultGnom", "setScatteringFitQ", value, "XSDataDouble")
		self.__scatteringFitQ[index] = value
	def getScatteringFitValues(self): return self.__scatteringFitValues
	def setScatteringFitValues(self, scatteringFitValues):
		checkType("XSDataResultGnom", "setScatteringFitValues", scatteringFitValues, "list")
		self.__scatteringFitValues = scatteringFitValues
	def delScatteringFitValues(self): self.__scatteringFitValues = None
	# Properties
	scatteringFitValues = property(getScatteringFitValues, setScatteringFitValues, delScatteringFitValues, "Property for scatteringFitValues")
	def addScatteringFitValues(self, value):
		checkType("XSDataResultGnom", "setScatteringFitValues", value, "XSDataDouble")
		self.__scatteringFitValues.append(value)
	def insertScatteringFitValues(self, index, value):
		checkType("XSDataResultGnom", "setScatteringFitValues", value, "XSDataDouble")
		self.__scatteringFitValues[index] = value
	def getScatteringFitQArray(self): return self.__scatteringFitQArray
	def setScatteringFitQArray(self, scatteringFitQArray):
		checkType("XSDataResultGnom", "setScatteringFitQArray", scatteringFitQArray, "XSDataArray")
		self.__scatteringFitQArray = scatteringFitQArray
	def delScatteringFitQArray(self): self.__scatteringFitQArray = None
	# Properties
	scatteringFitQArray = property(getScatteringFitQArray, setScatteringFitQArray, delScatteringFitQArray, "Property for scatteringFitQArray")
	def getScatteringFitIArray(self): return self.__scatteringFitIArray
	def setScatteringFitIArray(self, scatteringFitIArray):
		checkType("XSDataResultGnom", "setScatteringFitIArray", scatteringFitIArray, "XSDataArray")
		self.__scatteringFitIArray = scatteringFitIArray
	def delScatteringFitIArray(self): self.__scatteringFitIArray = None
	# Properties
	scatteringFitIArray = property(getScatteringFitIArray, setScatteringFitIArray, delScatteringFitIArray, "Property for scatteringFitIArray")
	def getDistributionR(self): return self.__distributionR
	def setDistributionR(self, distributionR):
		checkType("XSDataResultGnom", "setDistributionR", distributionR, "list")
		self.__distributionR = distributionR
	def delDistributionR(self): self.__distributionR = None
	# Properties
	distributionR = property(getDistributionR, setDistributionR, delDistributionR, "Property for distributionR")
	def addDistributionR(self, value):
		checkType("XSDataResultGnom", "setDistributionR", value, "XSDataDouble")
		self.__distributionR.append(value)
	def insertDistributionR(self, index, value):
		checkType("XSDataResultGnom", "setDistributionR", value, "XSDataDouble")
		self.__distributionR[index] = value
	def getDistributionPr(self): return self.__distributionPr
	def setDistributionPr(self, distributionPr):
		checkType("XSDataResultGnom", "setDistributionPr", distributionPr, "list")
		self.__distributionPr = distributionPr
	def delDistributionPr(self): self.__distributionPr = None
	# Properties
	distributionPr = property(getDistributionPr, setDistributionPr, delDistributionPr, "Property for distributionPr")
	def addDistributionPr(self, value):
		checkType("XSDataResultGnom", "setDistributionPr", value, "XSDataDouble")
		self.__distributionPr.append(value)
	def insertDistributionPr(self, index, value):
		checkType("XSDataResultGnom", "setDistributionPr", value, "XSDataDouble")
		self.__distributionPr[index] = value
	def getDistributionErr(self): return self.__distributionErr
	def setDistributionErr(self, distributionErr):
		checkType("XSDataResultGnom", "setDistributionErr", distributionErr, "list")
		self.__distributionErr = distributionErr
	def delDistributionErr(self): self.__distributionErr = None
	# Properties
	distributionErr = property(getDistributionErr, setDistributionErr, delDistributionErr, "Property for distributionErr")
	def addDistributionErr(self, value):
		checkType("XSDataResultGnom", "setDistributionErr", value, "XSDataDouble")
		self.__distributionErr.append(value)
	def insertDistributionErr(self, index, value):
		checkType("XSDataResultGnom", "setDistributionErr", value, "XSDataDouble")
		self.__distributionErr[index] = value
	def getArrayR(self): return self.__arrayR
	def setArrayR(self, arrayR):
		checkType("XSDataResultGnom", "setArrayR", arrayR, "XSDataArray")
		self.__arrayR = arrayR
	def delArrayR(self): self.__arrayR = None
	# Properties
	arrayR = property(getArrayR, setArrayR, delArrayR, "Property for arrayR")
	def getArrayPr(self): return self.__arrayPr
	def setArrayPr(self, arrayPr):
		checkType("XSDataResultGnom", "setArrayPr", arrayPr, "XSDataArray")
		self.__arrayPr = arrayPr
	def delArrayPr(self): self.__arrayPr = None
	# Properties
	arrayPr = property(getArrayPr, setArrayPr, delArrayPr, "Property for arrayPr")
	def getArrayErr(self): return self.__arrayErr
	def setArrayErr(self, arrayErr):
		checkType("XSDataResultGnom", "setArrayErr", arrayErr, "XSDataArray")
		self.__arrayErr = arrayErr
	def delArrayErr(self): self.__arrayErr = None
	# Properties
	arrayErr = property(getArrayErr, setArrayErr, delArrayErr, "Property for arrayErr")
	def getRadiusOfCrossSection(self): return self.__radiusOfCrossSection
	def setRadiusOfCrossSection(self, radiusOfCrossSection):
		checkType("XSDataResultGnom", "setRadiusOfCrossSection", radiusOfCrossSection, "XSDataDouble")
		self.__radiusOfCrossSection = radiusOfCrossSection
	def delRadiusOfCrossSection(self): self.__radiusOfCrossSection = None
	# Properties
	radiusOfCrossSection = property(getRadiusOfCrossSection, setRadiusOfCrossSection, delRadiusOfCrossSection, "Property for radiusOfCrossSection")
	def getRadiusOfGyration(self): return self.__radiusOfGyration
	def setRadiusOfGyration(self, radiusOfGyration):
		checkType("XSDataResultGnom", "setRadiusOfGyration", radiusOfGyration, "XSDataDouble")
		self.__radiusOfGyration = radiusOfGyration
	def delRadiusOfGyration(self): self.__radiusOfGyration = None
	# Properties
	radiusOfGyration = property(getRadiusOfGyration, setRadiusOfGyration, delRadiusOfGyration, "Property for radiusOfGyration")
	def export(self, outfile, level, name_='XSDataResultGnom'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultGnom'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__fitQuality is not None:
			self.fitQuality.export(outfile, level, name_='fitQuality')
		else:
			warnEmptyAttribute("fitQuality", "XSDataDouble")
		if self.__output is not None:
			self.output.export(outfile, level, name_='output')
		else:
			warnEmptyAttribute("output", "XSDataFile")
		for scatteringFitQ_ in self.getScatteringFitQ():
			scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
		for scatteringFitValues_ in self.getScatteringFitValues():
			scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
		if self.__scatteringFitQArray is not None:
			self.scatteringFitQArray.export(outfile, level, name_='scatteringFitQArray')
		if self.__scatteringFitIArray is not None:
			self.scatteringFitIArray.export(outfile, level, name_='scatteringFitIArray')
		for distributionR_ in self.getDistributionR():
			distributionR_.export(outfile, level, name_='distributionR')
		for distributionPr_ in self.getDistributionPr():
			distributionPr_.export(outfile, level, name_='distributionPr')
		for distributionErr_ in self.getDistributionErr():
			distributionErr_.export(outfile, level, name_='distributionErr')
		if self.__arrayR is not None:
			self.arrayR.export(outfile, level, name_='arrayR')
		if self.__arrayPr is not None:
			self.arrayPr.export(outfile, level, name_='arrayPr')
		if self.__arrayErr is not None:
			self.arrayErr.export(outfile, level, name_='arrayErr')
		if self.__radiusOfCrossSection is not None:
			self.radiusOfCrossSection.export(outfile, level, name_='radiusOfCrossSection')
		else:
			warnEmptyAttribute("radiusOfCrossSection", "XSDataDouble")
		if self.__radiusOfGyration is not None:
			self.radiusOfGyration.export(outfile, level, name_='radiusOfGyration')
		else:
			warnEmptyAttribute("radiusOfGyration", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fitQuality':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setFitQuality(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setOutput(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitQ':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.scatteringFitQ.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitValues':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.scatteringFitValues.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitQArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setScatteringFitQArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitIArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setScatteringFitIArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distributionR':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.distributionR.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distributionPr':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.distributionPr.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'distributionErr':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.distributionErr.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'arrayR':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setArrayR(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'arrayPr':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setArrayPr(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'arrayErr':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setArrayErr(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'radiusOfCrossSection':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRadiusOfCrossSection(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'radiusOfGyration':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setRadiusOfGyration(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultGnom")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultGnom')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultGnom is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultGnom.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultGnom()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultGnom")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultGnom()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultGnom

class XSDataResultSolutionScattering(XSDataResult):
	def __init__(self, status=None, variationNSD=None, meanNSD=None, scatteringFitIarray=None, scatteringFitQArray=None, scatteringFitValues=None, scatteringFitQ=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, lineProfileFitQuality=None, fitFile=None, corelationFitValues=None):
		XSDataResult.__init__(self, status)
		if corelationFitValues is None:
			self.__corelationFitValues = []
		else:
			checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", corelationFitValues, "list")
			self.__corelationFitValues = corelationFitValues
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", fitFile, "XSDataFile")
		self.__fitFile = fitFile
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", lineProfileFitQuality, "XSDataDouble")
		self.__lineProfileFitQuality = lineProfileFitQuality
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", logFile, "XSDataFile")
		self.__logFile = logFile
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
		if scatteringFitQ is None:
			self.__scatteringFitQ = []
		else:
			checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitQ, "list")
			self.__scatteringFitQ = scatteringFitQ
		if scatteringFitValues is None:
			self.__scatteringFitValues = []
		else:
			checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitValues, "list")
			self.__scatteringFitValues = scatteringFitValues
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitQArray, "XSDataArray")
		self.__scatteringFitQArray = scatteringFitQArray
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitIarray, "XSDataArray")
		self.__scatteringFitIarray = scatteringFitIarray
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", meanNSD, "XSDataDouble")
		self.__meanNSD = meanNSD
		checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", variationNSD, "XSDataDouble")
		self.__variationNSD = variationNSD
	def getCorelationFitValues(self): return self.__corelationFitValues
	def setCorelationFitValues(self, corelationFitValues):
		checkType("XSDataResultSolutionScattering", "setCorelationFitValues", corelationFitValues, "list")
		self.__corelationFitValues = corelationFitValues
	def delCorelationFitValues(self): self.__corelationFitValues = None
	# Properties
	corelationFitValues = property(getCorelationFitValues, setCorelationFitValues, delCorelationFitValues, "Property for corelationFitValues")
	def addCorelationFitValues(self, value):
		checkType("XSDataResultSolutionScattering", "setCorelationFitValues", value, "XSDataDouble")
		self.__corelationFitValues.append(value)
	def insertCorelationFitValues(self, index, value):
		checkType("XSDataResultSolutionScattering", "setCorelationFitValues", value, "XSDataDouble")
		self.__corelationFitValues[index] = value
	def getFitFile(self): return self.__fitFile
	def setFitFile(self, fitFile):
		checkType("XSDataResultSolutionScattering", "setFitFile", fitFile, "XSDataFile")
		self.__fitFile = fitFile
	def delFitFile(self): self.__fitFile = None
	# Properties
	fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
	def getLineProfileFitQuality(self): return self.__lineProfileFitQuality
	def setLineProfileFitQuality(self, lineProfileFitQuality):
		checkType("XSDataResultSolutionScattering", "setLineProfileFitQuality", lineProfileFitQuality, "XSDataDouble")
		self.__lineProfileFitQuality = lineProfileFitQuality
	def delLineProfileFitQuality(self): self.__lineProfileFitQuality = None
	# Properties
	lineProfileFitQuality = property(getLineProfileFitQuality, setLineProfileFitQuality, delLineProfileFitQuality, "Property for lineProfileFitQuality")
	def getLogFile(self): return self.__logFile
	def setLogFile(self, logFile):
		checkType("XSDataResultSolutionScattering", "setLogFile", logFile, "XSDataFile")
		self.__logFile = logFile
	def delLogFile(self): self.__logFile = None
	# Properties
	logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
	def getPdbMoleculeFile(self): return self.__pdbMoleculeFile
	def setPdbMoleculeFile(self, pdbMoleculeFile):
		checkType("XSDataResultSolutionScattering", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
		self.__pdbMoleculeFile = pdbMoleculeFile
	def delPdbMoleculeFile(self): self.__pdbMoleculeFile = None
	# Properties
	pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
	def getPdbSolventFile(self): return self.__pdbSolventFile
	def setPdbSolventFile(self, pdbSolventFile):
		checkType("XSDataResultSolutionScattering", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
		self.__pdbSolventFile = pdbSolventFile
	def delPdbSolventFile(self): self.__pdbSolventFile = None
	# Properties
	pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
	def getScatteringFitQ(self): return self.__scatteringFitQ
	def setScatteringFitQ(self, scatteringFitQ):
		checkType("XSDataResultSolutionScattering", "setScatteringFitQ", scatteringFitQ, "list")
		self.__scatteringFitQ = scatteringFitQ
	def delScatteringFitQ(self): self.__scatteringFitQ = None
	# Properties
	scatteringFitQ = property(getScatteringFitQ, setScatteringFitQ, delScatteringFitQ, "Property for scatteringFitQ")
	def addScatteringFitQ(self, value):
		checkType("XSDataResultSolutionScattering", "setScatteringFitQ", value, "XSDataDouble")
		self.__scatteringFitQ.append(value)
	def insertScatteringFitQ(self, index, value):
		checkType("XSDataResultSolutionScattering", "setScatteringFitQ", value, "XSDataDouble")
		self.__scatteringFitQ[index] = value
	def getScatteringFitValues(self): return self.__scatteringFitValues
	def setScatteringFitValues(self, scatteringFitValues):
		checkType("XSDataResultSolutionScattering", "setScatteringFitValues", scatteringFitValues, "list")
		self.__scatteringFitValues = scatteringFitValues
	def delScatteringFitValues(self): self.__scatteringFitValues = None
	# Properties
	scatteringFitValues = property(getScatteringFitValues, setScatteringFitValues, delScatteringFitValues, "Property for scatteringFitValues")
	def addScatteringFitValues(self, value):
		checkType("XSDataResultSolutionScattering", "setScatteringFitValues", value, "XSDataDouble")
		self.__scatteringFitValues.append(value)
	def insertScatteringFitValues(self, index, value):
		checkType("XSDataResultSolutionScattering", "setScatteringFitValues", value, "XSDataDouble")
		self.__scatteringFitValues[index] = value
	def getScatteringFitQArray(self): return self.__scatteringFitQArray
	def setScatteringFitQArray(self, scatteringFitQArray):
		checkType("XSDataResultSolutionScattering", "setScatteringFitQArray", scatteringFitQArray, "XSDataArray")
		self.__scatteringFitQArray = scatteringFitQArray
	def delScatteringFitQArray(self): self.__scatteringFitQArray = None
	# Properties
	scatteringFitQArray = property(getScatteringFitQArray, setScatteringFitQArray, delScatteringFitQArray, "Property for scatteringFitQArray")
	def getScatteringFitIarray(self): return self.__scatteringFitIarray
	def setScatteringFitIarray(self, scatteringFitIarray):
		checkType("XSDataResultSolutionScattering", "setScatteringFitIarray", scatteringFitIarray, "XSDataArray")
		self.__scatteringFitIarray = scatteringFitIarray
	def delScatteringFitIarray(self): self.__scatteringFitIarray = None
	# Properties
	scatteringFitIarray = property(getScatteringFitIarray, setScatteringFitIarray, delScatteringFitIarray, "Property for scatteringFitIarray")
	def getMeanNSD(self): return self.__meanNSD
	def setMeanNSD(self, meanNSD):
		checkType("XSDataResultSolutionScattering", "setMeanNSD", meanNSD, "XSDataDouble")
		self.__meanNSD = meanNSD
	def delMeanNSD(self): self.__meanNSD = None
	# Properties
	meanNSD = property(getMeanNSD, setMeanNSD, delMeanNSD, "Property for meanNSD")
	def getVariationNSD(self): return self.__variationNSD
	def setVariationNSD(self, variationNSD):
		checkType("XSDataResultSolutionScattering", "setVariationNSD", variationNSD, "XSDataDouble")
		self.__variationNSD = variationNSD
	def delVariationNSD(self): self.__variationNSD = None
	# Properties
	variationNSD = property(getVariationNSD, setVariationNSD, delVariationNSD, "Property for variationNSD")
	def export(self, outfile, level, name_='XSDataResultSolutionScattering'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSolutionScattering'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for corelationFitValues_ in self.getCorelationFitValues():
			corelationFitValues_.export(outfile, level, name_='corelationFitValues')
		if self.__fitFile is not None:
			self.fitFile.export(outfile, level, name_='fitFile')
		else:
			warnEmptyAttribute("fitFile", "XSDataFile")
		if self.__lineProfileFitQuality is not None:
			self.lineProfileFitQuality.export(outfile, level, name_='lineProfileFitQuality')
		else:
			warnEmptyAttribute("lineProfileFitQuality", "XSDataDouble")
		if self.__logFile is not None:
			self.logFile.export(outfile, level, name_='logFile')
		else:
			warnEmptyAttribute("logFile", "XSDataFile")
		if self.__pdbMoleculeFile is not None:
			self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
		else:
			warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
		if self.__pdbSolventFile is not None:
			self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
		else:
			warnEmptyAttribute("pdbSolventFile", "XSDataFile")
		for scatteringFitQ_ in self.getScatteringFitQ():
			scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
		for scatteringFitValues_ in self.getScatteringFitValues():
			scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
		if self.__scatteringFitQArray is not None:
			self.scatteringFitQArray.export(outfile, level, name_='scatteringFitQArray')
		if self.__scatteringFitIarray is not None:
			self.scatteringFitIarray.export(outfile, level, name_='scatteringFitIarray')
		if self.__meanNSD is not None:
			self.meanNSD.export(outfile, level, name_='meanNSD')
		if self.__variationNSD is not None:
			self.variationNSD.export(outfile, level, name_='variationNSD')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'corelationFitValues':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.corelationFitValues.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'fitFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setFitFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'lineProfileFitQuality':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLineProfileFitQuality(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'logFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setLogFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbMoleculeFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbMoleculeFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'pdbSolventFile':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setPdbSolventFile(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitQ':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.scatteringFitQ.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitValues':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.scatteringFitValues.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitQArray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setScatteringFitQArray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'scatteringFitIarray':
			obj_ = XSDataArray()
			obj_.build(child_)
			self.setScatteringFitIarray(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'meanNSD':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setMeanNSD(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'variationNSD':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setVariationNSD(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultSolutionScattering")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultSolutionScattering')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultSolutionScattering is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultSolutionScattering.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSolutionScattering()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultSolutionScattering")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSolutionScattering()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultSolutionScattering

class XSDataResultSupcomb(XSDataResult):
	def __init__(self, status=None, NSD=None, trns=None, rot=None, outputFilename=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", outputFilename, "XSDataFile")
		self.__outputFilename = outputFilename
		checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", rot, "XSDataRotation")
		self.__rot = rot
		checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", trns, "XSDataVectorDouble")
		self.__trns = trns
		checkType("XSDataResultSupcomb", "Constructor of XSDataResultSupcomb", NSD, "XSDataDouble")
		self.__NSD = NSD
	def getOutputFilename(self): return self.__outputFilename
	def setOutputFilename(self, outputFilename):
		checkType("XSDataResultSupcomb", "setOutputFilename", outputFilename, "XSDataFile")
		self.__outputFilename = outputFilename
	def delOutputFilename(self): self.__outputFilename = None
	# Properties
	outputFilename = property(getOutputFilename, setOutputFilename, delOutputFilename, "Property for outputFilename")
	def getRot(self): return self.__rot
	def setRot(self, rot):
		checkType("XSDataResultSupcomb", "setRot", rot, "XSDataRotation")
		self.__rot = rot
	def delRot(self): self.__rot = None
	# Properties
	rot = property(getRot, setRot, delRot, "Property for rot")
	def getTrns(self): return self.__trns
	def setTrns(self, trns):
		checkType("XSDataResultSupcomb", "setTrns", trns, "XSDataVectorDouble")
		self.__trns = trns
	def delTrns(self): self.__trns = None
	# Properties
	trns = property(getTrns, setTrns, delTrns, "Property for trns")
	def getNSD(self): return self.__NSD
	def setNSD(self, NSD):
		checkType("XSDataResultSupcomb", "setNSD", NSD, "XSDataDouble")
		self.__NSD = NSD
	def delNSD(self): self.__NSD = None
	# Properties
	NSD = property(getNSD, setNSD, delNSD, "Property for NSD")
	def export(self, outfile, level, name_='XSDataResultSupcomb'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResultSupcomb'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__outputFilename is not None:
			self.outputFilename.export(outfile, level, name_='outputFilename')
		else:
			warnEmptyAttribute("outputFilename", "XSDataFile")
		if self.__rot is not None:
			self.rot.export(outfile, level, name_='rot')
		else:
			warnEmptyAttribute("rot", "XSDataRotation")
		if self.__trns is not None:
			self.trns.export(outfile, level, name_='trns')
		else:
			warnEmptyAttribute("trns", "XSDataVectorDouble")
		if self.__NSD is not None:
			self.NSD.export(outfile, level, name_='NSD')
		else:
			warnEmptyAttribute("NSD", "XSDataDouble")
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
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rot':
			obj_ = XSDataRotation()
			obj_.build(child_)
			self.setRot(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'trns':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setTrns(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'NSD':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setNSD(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal(self):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export(oStreamString, 0, name_="XSDataResultSupcomb")
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile(self, _outfileName):
		outfile = open(_outfileName, "w")
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export(outfile, 0, name_='XSDataResultSupcomb')
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile(self, _outfileName):
		print("WARNING: Method outputFile in class XSDataResultSupcomb is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy(self):
		return XSDataResultSupcomb.parseString(self.marshal())
	#Static method for parsing a string
	def parseString(_inString):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResultSupcomb()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export(oStreamString, 0, name_="XSDataResultSupcomb")
		oStreamString.close()
		return rootObj
	parseString = staticmethod(parseString)
	#Static method for parsing a file
	def parseFile(_inFilePath):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResultSupcomb()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod(parseFile)
# end class XSDataResultSupcomb



# End of data representation classes.



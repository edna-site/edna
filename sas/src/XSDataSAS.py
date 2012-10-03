#!/usr/bin/env python

#
# Generated Tue Aug 28 04:46::05 2012 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataBoolean
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
from XSDataCommon import XSData
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
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
    if _value != None:
        if _strExpectedType not in (_value.__class__.__name__,)+(_value.__class__.__bases__):
            if (_value.__class__.__name__ == "unicode") and (_strExpectedType == "str"):
                # Accept unicode as expected str
                return
            elif (_value.__class__.__name__ == "int") and (_strExpectedType in ["float", "double"]):
                # Accept int as expected double or float
                return
            else:
                strMessage = "ERROR! %s.%s argument is not %s but %s" % (_strClassName, _strMethodName, _strExpectedType, _value.__class__.__name__)
                print(strMessage)


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
        else:     # category == MixedContainer.CategoryComplex
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


class XSDataSolutionScatteringSettings(XSData):
    def __init__(self, rMaxAbsTol=None, rMaxIntervals=None, rMaxStop=None, rMaxStart=None):
        XSData.__init__(self, )
    
    
        checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxStart, "XSDataDouble")
        self._rMaxStart = rMaxStart
        checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxStop, "XSDataDouble")
        self._rMaxStop = rMaxStop
        checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxIntervals, "XSDataInteger")
        self._rMaxIntervals = rMaxIntervals
        checkType("XSDataSolutionScatteringSettings", "Constructor of XSDataSolutionScatteringSettings", rMaxAbsTol, "XSDataDouble")
        self._rMaxAbsTol = rMaxAbsTol
    def getRMaxStart(self): return self._rMaxStart
    def setRMaxStart(self, rMaxStart):
        checkType("XSDataSolutionScatteringSettings", "setRMaxStart", rMaxStart, "XSDataDouble")
        self._rMaxStart = rMaxStart
    def delRMaxStart(self): self._rMaxStart = None
    # Properties
    rMaxStart = property(getRMaxStart, setRMaxStart, delRMaxStart, "Property for rMaxStart")
    def getRMaxStop(self): return self._rMaxStop
    def setRMaxStop(self, rMaxStop):
        checkType("XSDataSolutionScatteringSettings", "setRMaxStop", rMaxStop, "XSDataDouble")
        self._rMaxStop = rMaxStop
    def delRMaxStop(self): self._rMaxStop = None
    # Properties
    rMaxStop = property(getRMaxStop, setRMaxStop, delRMaxStop, "Property for rMaxStop")
    def getRMaxIntervals(self): return self._rMaxIntervals
    def setRMaxIntervals(self, rMaxIntervals):
        checkType("XSDataSolutionScatteringSettings", "setRMaxIntervals", rMaxIntervals, "XSDataInteger")
        self._rMaxIntervals = rMaxIntervals
    def delRMaxIntervals(self): self._rMaxIntervals = None
    # Properties
    rMaxIntervals = property(getRMaxIntervals, setRMaxIntervals, delRMaxIntervals, "Property for rMaxIntervals")
    def getRMaxAbsTol(self): return self._rMaxAbsTol
    def setRMaxAbsTol(self, rMaxAbsTol):
        checkType("XSDataSolutionScatteringSettings", "setRMaxAbsTol", rMaxAbsTol, "XSDataDouble")
        self._rMaxAbsTol = rMaxAbsTol
    def delRMaxAbsTol(self): self._rMaxAbsTol = None
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
        if self._rMaxStart is not None:
            self.rMaxStart.export(outfile, level, name_='rMaxStart')
        else:
            warnEmptyAttribute("rMaxStart", "XSDataDouble")
        if self._rMaxStop is not None:
            self.rMaxStop.export(outfile, level, name_='rMaxStop')
        else:
            warnEmptyAttribute("rMaxStop", "XSDataDouble")
        if self._rMaxIntervals is not None:
            self.rMaxIntervals.export(outfile, level, name_='rMaxIntervals')
        else:
            warnEmptyAttribute("rMaxIntervals", "XSDataInteger")
        if self._rMaxAbsTol is not None:
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSolutionScatteringSettings" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSolutionScatteringSettings' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSolutionScatteringSettings is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSolutionScatteringSettings.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSolutionScatteringSettings()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSolutionScatteringSettings" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSolutionScatteringSettings()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSolutionScatteringSettings

class XSDataInputSolutionScattering(XSDataInput):
    def __init__(self, configuration=None, qMax=None, qMin=None, plotFit=None, onlyGnom=None, iNbThreads=None, mode=None, symmetry=None, angularUnits=None, rMaxSearchSettings=None, experimentalDataFile=None, experimentalDataStdArray=None, experimentalDataStdDev=None, experimentalDataIArray=None, experimentalDataValues=None, experimentalDataQArray=None, experimentalDataQ=None, title=None):
        XSDataInput.__init__(self, configuration)
    
    
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", title, "XSDataString")
        self._title = title
        if experimentalDataQ is None:
            self._experimentalDataQ = []
        else:
            checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataQ, "list")
            self._experimentalDataQ = experimentalDataQ
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataQArray, "XSDataArray")
        self._experimentalDataQArray = experimentalDataQArray
        if experimentalDataValues is None:
            self._experimentalDataValues = []
        else:
            checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataValues, "list")
            self._experimentalDataValues = experimentalDataValues
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataIArray, "XSDataArray")
        self._experimentalDataIArray = experimentalDataIArray
        if experimentalDataStdDev is None:
            self._experimentalDataStdDev = []
        else:
            checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataStdDev, "list")
            self._experimentalDataStdDev = experimentalDataStdDev
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataStdArray, "XSDataArray")
        self._experimentalDataStdArray = experimentalDataStdArray
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", experimentalDataFile, "XSDataFile")
        self._experimentalDataFile = experimentalDataFile
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", rMaxSearchSettings, "XSDataSolutionScatteringSettings")
        self._rMaxSearchSettings = rMaxSearchSettings
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", angularUnits, "XSDataInteger")
        self._angularUnits = angularUnits
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", symmetry, "XSDataString")
        self._symmetry = symmetry
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", mode, "XSDataString")
        self._mode = mode
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", iNbThreads, "XSDataInteger")
        self._iNbThreads = iNbThreads
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", onlyGnom, "XSDataBoolean")
        self._onlyGnom = onlyGnom
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", plotFit, "XSDataBoolean")
        self._plotFit = plotFit
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", qMin, "XSDataDouble")
        self._qMin = qMin
        checkType("XSDataInputSolutionScattering", "Constructor of XSDataInputSolutionScattering", qMax, "XSDataDouble")
        self._qMax = qMax
    def getTitle(self): return self._title
    def setTitle(self, title):
        checkType("XSDataInputSolutionScattering", "setTitle", title, "XSDataString")
        self._title = title
    def delTitle(self): self._title = None
    # Properties
    title = property(getTitle, setTitle, delTitle, "Property for title")
    def getExperimentalDataQ(self): return self._experimentalDataQ
    def setExperimentalDataQ(self, experimentalDataQ):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", experimentalDataQ, "list")
        self._experimentalDataQ = experimentalDataQ
    def delExperimentalDataQ(self): self._experimentalDataQ = None
    # Properties
    experimentalDataQ = property(getExperimentalDataQ, setExperimentalDataQ, delExperimentalDataQ, "Property for experimentalDataQ")
    def addExperimentalDataQ(self, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", value, "XSDataDouble")
        self._experimentalDataQ.append(value)
    def insertExperimentalDataQ(self, index, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataQ", value, "XSDataDouble")
        self._experimentalDataQ[index] = value
    def getExperimentalDataQArray(self): return self._experimentalDataQArray
    def setExperimentalDataQArray(self, experimentalDataQArray):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataQArray", experimentalDataQArray, "XSDataArray")
        self._experimentalDataQArray = experimentalDataQArray
    def delExperimentalDataQArray(self): self._experimentalDataQArray = None
    # Properties
    experimentalDataQArray = property(getExperimentalDataQArray, setExperimentalDataQArray, delExperimentalDataQArray, "Property for experimentalDataQArray")
    def getExperimentalDataValues(self): return self._experimentalDataValues
    def setExperimentalDataValues(self, experimentalDataValues):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", experimentalDataValues, "list")
        self._experimentalDataValues = experimentalDataValues
    def delExperimentalDataValues(self): self._experimentalDataValues = None
    # Properties
    experimentalDataValues = property(getExperimentalDataValues, setExperimentalDataValues, delExperimentalDataValues, "Property for experimentalDataValues")
    def addExperimentalDataValues(self, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", value, "XSDataDouble")
        self._experimentalDataValues.append(value)
    def insertExperimentalDataValues(self, index, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataValues", value, "XSDataDouble")
        self._experimentalDataValues[index] = value
    def getExperimentalDataIArray(self): return self._experimentalDataIArray
    def setExperimentalDataIArray(self, experimentalDataIArray):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataIArray", experimentalDataIArray, "XSDataArray")
        self._experimentalDataIArray = experimentalDataIArray
    def delExperimentalDataIArray(self): self._experimentalDataIArray = None
    # Properties
    experimentalDataIArray = property(getExperimentalDataIArray, setExperimentalDataIArray, delExperimentalDataIArray, "Property for experimentalDataIArray")
    def getExperimentalDataStdDev(self): return self._experimentalDataStdDev
    def setExperimentalDataStdDev(self, experimentalDataStdDev):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", experimentalDataStdDev, "list")
        self._experimentalDataStdDev = experimentalDataStdDev
    def delExperimentalDataStdDev(self): self._experimentalDataStdDev = None
    # Properties
    experimentalDataStdDev = property(getExperimentalDataStdDev, setExperimentalDataStdDev, delExperimentalDataStdDev, "Property for experimentalDataStdDev")
    def addExperimentalDataStdDev(self, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", value, "XSDataDouble")
        self._experimentalDataStdDev.append(value)
    def insertExperimentalDataStdDev(self, index, value):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataStdDev", value, "XSDataDouble")
        self._experimentalDataStdDev[index] = value
    def getExperimentalDataStdArray(self): return self._experimentalDataStdArray
    def setExperimentalDataStdArray(self, experimentalDataStdArray):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataStdArray", experimentalDataStdArray, "XSDataArray")
        self._experimentalDataStdArray = experimentalDataStdArray
    def delExperimentalDataStdArray(self): self._experimentalDataStdArray = None
    # Properties
    experimentalDataStdArray = property(getExperimentalDataStdArray, setExperimentalDataStdArray, delExperimentalDataStdArray, "Property for experimentalDataStdArray")
    def getExperimentalDataFile(self): return self._experimentalDataFile
    def setExperimentalDataFile(self, experimentalDataFile):
        checkType("XSDataInputSolutionScattering", "setExperimentalDataFile", experimentalDataFile, "XSDataFile")
        self._experimentalDataFile = experimentalDataFile
    def delExperimentalDataFile(self): self._experimentalDataFile = None
    # Properties
    experimentalDataFile = property(getExperimentalDataFile, setExperimentalDataFile, delExperimentalDataFile, "Property for experimentalDataFile")
    def getRMaxSearchSettings(self): return self._rMaxSearchSettings
    def setRMaxSearchSettings(self, rMaxSearchSettings):
        checkType("XSDataInputSolutionScattering", "setRMaxSearchSettings", rMaxSearchSettings, "XSDataSolutionScatteringSettings")
        self._rMaxSearchSettings = rMaxSearchSettings
    def delRMaxSearchSettings(self): self._rMaxSearchSettings = None
    # Properties
    rMaxSearchSettings = property(getRMaxSearchSettings, setRMaxSearchSettings, delRMaxSearchSettings, "Property for rMaxSearchSettings")
    def getAngularUnits(self): return self._angularUnits
    def setAngularUnits(self, angularUnits):
        checkType("XSDataInputSolutionScattering", "setAngularUnits", angularUnits, "XSDataInteger")
        self._angularUnits = angularUnits
    def delAngularUnits(self): self._angularUnits = None
    # Properties
    angularUnits = property(getAngularUnits, setAngularUnits, delAngularUnits, "Property for angularUnits")
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        checkType("XSDataInputSolutionScattering", "setSymmetry", symmetry, "XSDataString")
        self._symmetry = symmetry
    def delSymmetry(self): self._symmetry = None
    # Properties
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    def getMode(self): return self._mode
    def setMode(self, mode):
        checkType("XSDataInputSolutionScattering", "setMode", mode, "XSDataString")
        self._mode = mode
    def delMode(self): self._mode = None
    # Properties
    mode = property(getMode, setMode, delMode, "Property for mode")
    def getINbThreads(self): return self._iNbThreads
    def setINbThreads(self, iNbThreads):
        checkType("XSDataInputSolutionScattering", "setINbThreads", iNbThreads, "XSDataInteger")
        self._iNbThreads = iNbThreads
    def delINbThreads(self): self._iNbThreads = None
    # Properties
    iNbThreads = property(getINbThreads, setINbThreads, delINbThreads, "Property for iNbThreads")
    def getOnlyGnom(self): return self._onlyGnom
    def setOnlyGnom(self, onlyGnom):
        checkType("XSDataInputSolutionScattering", "setOnlyGnom", onlyGnom, "XSDataBoolean")
        self._onlyGnom = onlyGnom
    def delOnlyGnom(self): self._onlyGnom = None
    # Properties
    onlyGnom = property(getOnlyGnom, setOnlyGnom, delOnlyGnom, "Property for onlyGnom")
    def getPlotFit(self): return self._plotFit
    def setPlotFit(self, plotFit):
        checkType("XSDataInputSolutionScattering", "setPlotFit", plotFit, "XSDataBoolean")
        self._plotFit = plotFit
    def delPlotFit(self): self._plotFit = None
    # Properties
    plotFit = property(getPlotFit, setPlotFit, delPlotFit, "Property for plotFit")
    def getQMin(self): return self._qMin
    def setQMin(self, qMin):
        checkType("XSDataInputSolutionScattering", "setQMin", qMin, "XSDataDouble")
        self._qMin = qMin
    def delQMin(self): self._qMin = None
    # Properties
    qMin = property(getQMin, setQMin, delQMin, "Property for qMin")
    def getQMax(self): return self._qMax
    def setQMax(self, qMax):
        checkType("XSDataInputSolutionScattering", "setQMax", qMax, "XSDataDouble")
        self._qMax = qMax
    def delQMax(self): self._qMax = None
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
        if self._title is not None:
            self.title.export(outfile, level, name_='title')
        for experimentalDataQ_ in self.getExperimentalDataQ():
            experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
        if self._experimentalDataQArray is not None:
            self.experimentalDataQArray.export(outfile, level, name_='experimentalDataQArray')
        for experimentalDataValues_ in self.getExperimentalDataValues():
            experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
        if self._experimentalDataIArray is not None:
            self.experimentalDataIArray.export(outfile, level, name_='experimentalDataIArray')
        for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
            experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
        if self._experimentalDataStdArray is not None:
            self.experimentalDataStdArray.export(outfile, level, name_='experimentalDataStdArray')
        if self._experimentalDataFile is not None:
            self.experimentalDataFile.export(outfile, level, name_='experimentalDataFile')
        if self._rMaxSearchSettings is not None:
            self.rMaxSearchSettings.export(outfile, level, name_='rMaxSearchSettings')
        if self._angularUnits is not None:
            self.angularUnits.export(outfile, level, name_='angularUnits')
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
        if self._iNbThreads is not None:
            self.iNbThreads.export(outfile, level, name_='iNbThreads')
        if self._onlyGnom is not None:
            self.onlyGnom.export(outfile, level, name_='onlyGnom')
        if self._plotFit is not None:
            self.plotFit.export(outfile, level, name_='plotFit')
        if self._qMin is not None:
            self.qMin.export(outfile, level, name_='qMin')
        if self._qMax is not None:
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSolutionScattering" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSolutionScattering' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSolutionScattering is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSolutionScattering.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSolutionScattering()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSolutionScattering" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSolutionScattering()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSolutionScattering

class XSDataResultSolutionScattering(XSDataResult):
    def __init__(self, status=None, variationNSD=None, meanNSD=None, scatteringFitIarray=None, scatteringFitQArray=None, scatteringFitValues=None, scatteringFitQ=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, lineProfileFitQuality=None, fitFile=None, corelationFitValues=None):
        XSDataResult.__init__(self, status)
    
    
        if corelationFitValues is None:
            self._corelationFitValues = []
        else:
            checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", corelationFitValues, "list")
            self._corelationFitValues = corelationFitValues
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", fitFile, "XSDataFile")
        self._fitFile = fitFile
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", lineProfileFitQuality, "XSDataDouble")
        self._lineProfileFitQuality = lineProfileFitQuality
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", logFile, "XSDataFile")
        self._logFile = logFile
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
        if scatteringFitQ is None:
            self._scatteringFitQ = []
        else:
            checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitQ, "list")
            self._scatteringFitQ = scatteringFitQ
        if scatteringFitValues is None:
            self._scatteringFitValues = []
        else:
            checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitValues, "list")
            self._scatteringFitValues = scatteringFitValues
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitQArray, "XSDataArray")
        self._scatteringFitQArray = scatteringFitQArray
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", scatteringFitIarray, "XSDataArray")
        self._scatteringFitIarray = scatteringFitIarray
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", meanNSD, "XSDataDouble")
        self._meanNSD = meanNSD
        checkType("XSDataResultSolutionScattering", "Constructor of XSDataResultSolutionScattering", variationNSD, "XSDataDouble")
        self._variationNSD = variationNSD
    def getCorelationFitValues(self): return self._corelationFitValues
    def setCorelationFitValues(self, corelationFitValues):
        checkType("XSDataResultSolutionScattering", "setCorelationFitValues", corelationFitValues, "list")
        self._corelationFitValues = corelationFitValues
    def delCorelationFitValues(self): self._corelationFitValues = None
    # Properties
    corelationFitValues = property(getCorelationFitValues, setCorelationFitValues, delCorelationFitValues, "Property for corelationFitValues")
    def addCorelationFitValues(self, value):
        checkType("XSDataResultSolutionScattering", "setCorelationFitValues", value, "XSDataDouble")
        self._corelationFitValues.append(value)
    def insertCorelationFitValues(self, index, value):
        checkType("XSDataResultSolutionScattering", "setCorelationFitValues", value, "XSDataDouble")
        self._corelationFitValues[index] = value
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        checkType("XSDataResultSolutionScattering", "setFitFile", fitFile, "XSDataFile")
        self._fitFile = fitFile
    def delFitFile(self): self._fitFile = None
    # Properties
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    def getLineProfileFitQuality(self): return self._lineProfileFitQuality
    def setLineProfileFitQuality(self, lineProfileFitQuality):
        checkType("XSDataResultSolutionScattering", "setLineProfileFitQuality", lineProfileFitQuality, "XSDataDouble")
        self._lineProfileFitQuality = lineProfileFitQuality
    def delLineProfileFitQuality(self): self._lineProfileFitQuality = None
    # Properties
    lineProfileFitQuality = property(getLineProfileFitQuality, setLineProfileFitQuality, delLineProfileFitQuality, "Property for lineProfileFitQuality")
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        checkType("XSDataResultSolutionScattering", "setLogFile", logFile, "XSDataFile")
        self._logFile = logFile
    def delLogFile(self): self._logFile = None
    # Properties
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        checkType("XSDataResultSolutionScattering", "setPdbMoleculeFile", pdbMoleculeFile, "XSDataFile")
        self._pdbMoleculeFile = pdbMoleculeFile
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    # Properties
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        checkType("XSDataResultSolutionScattering", "setPdbSolventFile", pdbSolventFile, "XSDataFile")
        self._pdbSolventFile = pdbSolventFile
    def delPdbSolventFile(self): self._pdbSolventFile = None
    # Properties
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    def getScatteringFitQ(self): return self._scatteringFitQ
    def setScatteringFitQ(self, scatteringFitQ):
        checkType("XSDataResultSolutionScattering", "setScatteringFitQ", scatteringFitQ, "list")
        self._scatteringFitQ = scatteringFitQ
    def delScatteringFitQ(self): self._scatteringFitQ = None
    # Properties
    scatteringFitQ = property(getScatteringFitQ, setScatteringFitQ, delScatteringFitQ, "Property for scatteringFitQ")
    def addScatteringFitQ(self, value):
        checkType("XSDataResultSolutionScattering", "setScatteringFitQ", value, "XSDataDouble")
        self._scatteringFitQ.append(value)
    def insertScatteringFitQ(self, index, value):
        checkType("XSDataResultSolutionScattering", "setScatteringFitQ", value, "XSDataDouble")
        self._scatteringFitQ[index] = value
    def getScatteringFitValues(self): return self._scatteringFitValues
    def setScatteringFitValues(self, scatteringFitValues):
        checkType("XSDataResultSolutionScattering", "setScatteringFitValues", scatteringFitValues, "list")
        self._scatteringFitValues = scatteringFitValues
    def delScatteringFitValues(self): self._scatteringFitValues = None
    # Properties
    scatteringFitValues = property(getScatteringFitValues, setScatteringFitValues, delScatteringFitValues, "Property for scatteringFitValues")
    def addScatteringFitValues(self, value):
        checkType("XSDataResultSolutionScattering", "setScatteringFitValues", value, "XSDataDouble")
        self._scatteringFitValues.append(value)
    def insertScatteringFitValues(self, index, value):
        checkType("XSDataResultSolutionScattering", "setScatteringFitValues", value, "XSDataDouble")
        self._scatteringFitValues[index] = value
    def getScatteringFitQArray(self): return self._scatteringFitQArray
    def setScatteringFitQArray(self, scatteringFitQArray):
        checkType("XSDataResultSolutionScattering", "setScatteringFitQArray", scatteringFitQArray, "XSDataArray")
        self._scatteringFitQArray = scatteringFitQArray
    def delScatteringFitQArray(self): self._scatteringFitQArray = None
    # Properties
    scatteringFitQArray = property(getScatteringFitQArray, setScatteringFitQArray, delScatteringFitQArray, "Property for scatteringFitQArray")
    def getScatteringFitIarray(self): return self._scatteringFitIarray
    def setScatteringFitIarray(self, scatteringFitIarray):
        checkType("XSDataResultSolutionScattering", "setScatteringFitIarray", scatteringFitIarray, "XSDataArray")
        self._scatteringFitIarray = scatteringFitIarray
    def delScatteringFitIarray(self): self._scatteringFitIarray = None
    # Properties
    scatteringFitIarray = property(getScatteringFitIarray, setScatteringFitIarray, delScatteringFitIarray, "Property for scatteringFitIarray")
    def getMeanNSD(self): return self._meanNSD
    def setMeanNSD(self, meanNSD):
        checkType("XSDataResultSolutionScattering", "setMeanNSD", meanNSD, "XSDataDouble")
        self._meanNSD = meanNSD
    def delMeanNSD(self): self._meanNSD = None
    # Properties
    meanNSD = property(getMeanNSD, setMeanNSD, delMeanNSD, "Property for meanNSD")
    def getVariationNSD(self): return self._variationNSD
    def setVariationNSD(self, variationNSD):
        checkType("XSDataResultSolutionScattering", "setVariationNSD", variationNSD, "XSDataDouble")
        self._variationNSD = variationNSD
    def delVariationNSD(self): self._variationNSD = None
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
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._lineProfileFitQuality is not None:
            self.lineProfileFitQuality.export(outfile, level, name_='lineProfileFitQuality')
        else:
            warnEmptyAttribute("lineProfileFitQuality", "XSDataDouble")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
        for scatteringFitQ_ in self.getScatteringFitQ():
            scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
        for scatteringFitValues_ in self.getScatteringFitValues():
            scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
        if self._scatteringFitQArray is not None:
            self.scatteringFitQArray.export(outfile, level, name_='scatteringFitQArray')
        if self._scatteringFitIarray is not None:
            self.scatteringFitIarray.export(outfile, level, name_='scatteringFitIarray')
        if self._meanNSD is not None:
            self.meanNSD.export(outfile, level, name_='meanNSD')
        if self._variationNSD is not None:
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
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSolutionScattering" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSolutionScattering' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSolutionScattering is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSolutionScattering.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSolutionScattering()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSolutionScattering" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSolutionScattering()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSolutionScattering



# End of data representation classes.



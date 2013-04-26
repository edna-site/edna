#!/usr/bin/env python

#
# Generated Fri Apr 26 03:16::28 2013 by EDGenerateDS.
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


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    #if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
    #    print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

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



class XSDataInputRdfit(XSDataInput):
    def __init__(self, configuration=None, resultsXmlFile=None, resultsFile=None, bScaleIntensityGleFile=None, bScaleIntensityMtvPlotFile=None, bFactorGlePlotFile=None, bFactorMtvplotFile=None, defaultGama=None, defaultBeta=None, dmin=None, xdsHklFile=None, bestXmlFile=None):
        XSDataInput.__init__(self, configuration)
        if bestXmlFile is None:
            self._bestXmlFile = None
        elif bestXmlFile.__class__.__name__ == "XSDataFile":
            self._bestXmlFile = bestXmlFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'bestXmlFile' is not XSDataFile but %s" % self._bestXmlFile.__class__.__name__
            raise BaseException(strMessage)
        if xdsHklFile is None:
            self._xdsHklFile = []
        elif xdsHklFile.__class__.__name__ == "list":
            self._xdsHklFile = xdsHklFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'xdsHklFile' is not list but %s" % self._xdsHklFile.__class__.__name__
            raise BaseException(strMessage)
        if dmin is None:
            self._dmin = None
        elif dmin.__class__.__name__ == "XSDataDouble":
            self._dmin = dmin
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'dmin' is not XSDataDouble but %s" % self._dmin.__class__.__name__
            raise BaseException(strMessage)
        if defaultBeta is None:
            self._defaultBeta = None
        elif defaultBeta.__class__.__name__ == "XSDataDouble":
            self._defaultBeta = defaultBeta
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'defaultBeta' is not XSDataDouble but %s" % self._defaultBeta.__class__.__name__
            raise BaseException(strMessage)
        if defaultGama is None:
            self._defaultGama = None
        elif defaultGama.__class__.__name__ == "XSDataDouble":
            self._defaultGama = defaultGama
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'defaultGama' is not XSDataDouble but %s" % self._defaultGama.__class__.__name__
            raise BaseException(strMessage)
        if bFactorMtvplotFile is None:
            self._bFactorMtvplotFile = None
        elif bFactorMtvplotFile.__class__.__name__ == "XSDataFile":
            self._bFactorMtvplotFile = bFactorMtvplotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'bFactorMtvplotFile' is not XSDataFile but %s" % self._bFactorMtvplotFile.__class__.__name__
            raise BaseException(strMessage)
        if bFactorGlePlotFile is None:
            self._bFactorGlePlotFile = None
        elif bFactorGlePlotFile.__class__.__name__ == "XSDataFile":
            self._bFactorGlePlotFile = bFactorGlePlotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'bFactorGlePlotFile' is not XSDataFile but %s" % self._bFactorGlePlotFile.__class__.__name__
            raise BaseException(strMessage)
        if bScaleIntensityMtvPlotFile is None:
            self._bScaleIntensityMtvPlotFile = None
        elif bScaleIntensityMtvPlotFile.__class__.__name__ == "XSDataFile":
            self._bScaleIntensityMtvPlotFile = bScaleIntensityMtvPlotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'bScaleIntensityMtvPlotFile' is not XSDataFile but %s" % self._bScaleIntensityMtvPlotFile.__class__.__name__
            raise BaseException(strMessage)
        if bScaleIntensityGleFile is None:
            self._bScaleIntensityGleFile = None
        elif bScaleIntensityGleFile.__class__.__name__ == "XSDataFile":
            self._bScaleIntensityGleFile = bScaleIntensityGleFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'bScaleIntensityGleFile' is not XSDataFile but %s" % self._bScaleIntensityGleFile.__class__.__name__
            raise BaseException(strMessage)
        if resultsFile is None:
            self._resultsFile = None
        elif resultsFile.__class__.__name__ == "XSDataFile":
            self._resultsFile = resultsFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'resultsFile' is not XSDataFile but %s" % self._resultsFile.__class__.__name__
            raise BaseException(strMessage)
        if resultsXmlFile is None:
            self._resultsXmlFile = None
        elif resultsXmlFile.__class__.__name__ == "XSDataFile":
            self._resultsXmlFile = resultsXmlFile
        else:
            strMessage = "ERROR! XSDataInputRdfit constructor argument 'resultsXmlFile' is not XSDataFile but %s" % self._resultsXmlFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bestXmlFile' attribute
    def getBestXmlFile(self): return self._bestXmlFile
    def setBestXmlFile(self, bestXmlFile):
        if bestXmlFile is None:
            self._bestXmlFile = None
        elif bestXmlFile.__class__.__name__ == "XSDataFile":
            self._bestXmlFile = bestXmlFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setBestXmlFile argument is not XSDataFile but %s" % bestXmlFile.__class__.__name__
            raise BaseException(strMessage)
    def delBestXmlFile(self): self._bestXmlFile = None
    bestXmlFile = property(getBestXmlFile, setBestXmlFile, delBestXmlFile, "Property for bestXmlFile")
    # Methods and properties for the 'xdsHklFile' attribute
    def getXdsHklFile(self): return self._xdsHklFile
    def setXdsHklFile(self, xdsHklFile):
        if xdsHklFile is None:
            self._xdsHklFile = []
        elif xdsHklFile.__class__.__name__ == "list":
            self._xdsHklFile = xdsHklFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setXdsHklFile argument is not list but %s" % xdsHklFile.__class__.__name__
            raise BaseException(strMessage)
    def delXdsHklFile(self): self._xdsHklFile = None
    xdsHklFile = property(getXdsHklFile, setXdsHklFile, delXdsHklFile, "Property for xdsHklFile")
    def addXdsHklFile(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputRdfit.addXdsHklFile argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._xdsHklFile.append(value)
        else:
            strMessage = "ERROR! XSDataInputRdfit.addXdsHklFile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXdsHklFile(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputRdfit.insertXdsHklFile argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputRdfit.insertXdsHklFile argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._xdsHklFile[index] = value
        else:
            strMessage = "ERROR! XSDataInputRdfit.addXdsHklFile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dmin' attribute
    def getDmin(self): return self._dmin
    def setDmin(self, dmin):
        if dmin is None:
            self._dmin = None
        elif dmin.__class__.__name__ == "XSDataDouble":
            self._dmin = dmin
        else:
            strMessage = "ERROR! XSDataInputRdfit.setDmin argument is not XSDataDouble but %s" % dmin.__class__.__name__
            raise BaseException(strMessage)
    def delDmin(self): self._dmin = None
    dmin = property(getDmin, setDmin, delDmin, "Property for dmin")
    # Methods and properties for the 'defaultBeta' attribute
    def getDefaultBeta(self): return self._defaultBeta
    def setDefaultBeta(self, defaultBeta):
        if defaultBeta is None:
            self._defaultBeta = None
        elif defaultBeta.__class__.__name__ == "XSDataDouble":
            self._defaultBeta = defaultBeta
        else:
            strMessage = "ERROR! XSDataInputRdfit.setDefaultBeta argument is not XSDataDouble but %s" % defaultBeta.__class__.__name__
            raise BaseException(strMessage)
    def delDefaultBeta(self): self._defaultBeta = None
    defaultBeta = property(getDefaultBeta, setDefaultBeta, delDefaultBeta, "Property for defaultBeta")
    # Methods and properties for the 'defaultGama' attribute
    def getDefaultGama(self): return self._defaultGama
    def setDefaultGama(self, defaultGama):
        if defaultGama is None:
            self._defaultGama = None
        elif defaultGama.__class__.__name__ == "XSDataDouble":
            self._defaultGama = defaultGama
        else:
            strMessage = "ERROR! XSDataInputRdfit.setDefaultGama argument is not XSDataDouble but %s" % defaultGama.__class__.__name__
            raise BaseException(strMessage)
    def delDefaultGama(self): self._defaultGama = None
    defaultGama = property(getDefaultGama, setDefaultGama, delDefaultGama, "Property for defaultGama")
    # Methods and properties for the 'bFactorMtvplotFile' attribute
    def getBFactorMtvplotFile(self): return self._bFactorMtvplotFile
    def setBFactorMtvplotFile(self, bFactorMtvplotFile):
        if bFactorMtvplotFile is None:
            self._bFactorMtvplotFile = None
        elif bFactorMtvplotFile.__class__.__name__ == "XSDataFile":
            self._bFactorMtvplotFile = bFactorMtvplotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setBFactorMtvplotFile argument is not XSDataFile but %s" % bFactorMtvplotFile.__class__.__name__
            raise BaseException(strMessage)
    def delBFactorMtvplotFile(self): self._bFactorMtvplotFile = None
    bFactorMtvplotFile = property(getBFactorMtvplotFile, setBFactorMtvplotFile, delBFactorMtvplotFile, "Property for bFactorMtvplotFile")
    # Methods and properties for the 'bFactorGlePlotFile' attribute
    def getBFactorGlePlotFile(self): return self._bFactorGlePlotFile
    def setBFactorGlePlotFile(self, bFactorGlePlotFile):
        if bFactorGlePlotFile is None:
            self._bFactorGlePlotFile = None
        elif bFactorGlePlotFile.__class__.__name__ == "XSDataFile":
            self._bFactorGlePlotFile = bFactorGlePlotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setBFactorGlePlotFile argument is not XSDataFile but %s" % bFactorGlePlotFile.__class__.__name__
            raise BaseException(strMessage)
    def delBFactorGlePlotFile(self): self._bFactorGlePlotFile = None
    bFactorGlePlotFile = property(getBFactorGlePlotFile, setBFactorGlePlotFile, delBFactorGlePlotFile, "Property for bFactorGlePlotFile")
    # Methods and properties for the 'bScaleIntensityMtvPlotFile' attribute
    def getBScaleIntensityMtvPlotFile(self): return self._bScaleIntensityMtvPlotFile
    def setBScaleIntensityMtvPlotFile(self, bScaleIntensityMtvPlotFile):
        if bScaleIntensityMtvPlotFile is None:
            self._bScaleIntensityMtvPlotFile = None
        elif bScaleIntensityMtvPlotFile.__class__.__name__ == "XSDataFile":
            self._bScaleIntensityMtvPlotFile = bScaleIntensityMtvPlotFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setBScaleIntensityMtvPlotFile argument is not XSDataFile but %s" % bScaleIntensityMtvPlotFile.__class__.__name__
            raise BaseException(strMessage)
    def delBScaleIntensityMtvPlotFile(self): self._bScaleIntensityMtvPlotFile = None
    bScaleIntensityMtvPlotFile = property(getBScaleIntensityMtvPlotFile, setBScaleIntensityMtvPlotFile, delBScaleIntensityMtvPlotFile, "Property for bScaleIntensityMtvPlotFile")
    # Methods and properties for the 'bScaleIntensityGleFile' attribute
    def getBScaleIntensityGleFile(self): return self._bScaleIntensityGleFile
    def setBScaleIntensityGleFile(self, bScaleIntensityGleFile):
        if bScaleIntensityGleFile is None:
            self._bScaleIntensityGleFile = None
        elif bScaleIntensityGleFile.__class__.__name__ == "XSDataFile":
            self._bScaleIntensityGleFile = bScaleIntensityGleFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setBScaleIntensityGleFile argument is not XSDataFile but %s" % bScaleIntensityGleFile.__class__.__name__
            raise BaseException(strMessage)
    def delBScaleIntensityGleFile(self): self._bScaleIntensityGleFile = None
    bScaleIntensityGleFile = property(getBScaleIntensityGleFile, setBScaleIntensityGleFile, delBScaleIntensityGleFile, "Property for bScaleIntensityGleFile")
    # Methods and properties for the 'resultsFile' attribute
    def getResultsFile(self): return self._resultsFile
    def setResultsFile(self, resultsFile):
        if resultsFile is None:
            self._resultsFile = None
        elif resultsFile.__class__.__name__ == "XSDataFile":
            self._resultsFile = resultsFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setResultsFile argument is not XSDataFile but %s" % resultsFile.__class__.__name__
            raise BaseException(strMessage)
    def delResultsFile(self): self._resultsFile = None
    resultsFile = property(getResultsFile, setResultsFile, delResultsFile, "Property for resultsFile")
    # Methods and properties for the 'resultsXmlFile' attribute
    def getResultsXmlFile(self): return self._resultsXmlFile
    def setResultsXmlFile(self, resultsXmlFile):
        if resultsXmlFile is None:
            self._resultsXmlFile = None
        elif resultsXmlFile.__class__.__name__ == "XSDataFile":
            self._resultsXmlFile = resultsXmlFile
        else:
            strMessage = "ERROR! XSDataInputRdfit.setResultsXmlFile argument is not XSDataFile but %s" % resultsXmlFile.__class__.__name__
            raise BaseException(strMessage)
    def delResultsXmlFile(self): self._resultsXmlFile = None
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
    def __init__(self, status=None, htmlPage=None, bFactorPlot=None, scaleIntensityPlot=None, relative_radiation_sensitivity=None, dose_half=None, dose_half_th=None, gama=None, beta=None):
        XSDataResult.__init__(self, status)
        if beta is None:
            self._beta = None
        elif beta.__class__.__name__ == "XSDataDouble":
            self._beta = beta
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'beta' is not XSDataDouble but %s" % self._beta.__class__.__name__
            raise BaseException(strMessage)
        if gama is None:
            self._gama = None
        elif gama.__class__.__name__ == "XSDataDouble":
            self._gama = gama
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'gama' is not XSDataDouble but %s" % self._gama.__class__.__name__
            raise BaseException(strMessage)
        if dose_half_th is None:
            self._dose_half_th = None
        elif dose_half_th.__class__.__name__ == "XSDataDouble":
            self._dose_half_th = dose_half_th
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'dose_half_th' is not XSDataDouble but %s" % self._dose_half_th.__class__.__name__
            raise BaseException(strMessage)
        if dose_half is None:
            self._dose_half = None
        elif dose_half.__class__.__name__ == "XSDataDouble":
            self._dose_half = dose_half
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'dose_half' is not XSDataDouble but %s" % self._dose_half.__class__.__name__
            raise BaseException(strMessage)
        if relative_radiation_sensitivity is None:
            self._relative_radiation_sensitivity = None
        elif relative_radiation_sensitivity.__class__.__name__ == "XSDataDouble":
            self._relative_radiation_sensitivity = relative_radiation_sensitivity
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'relative_radiation_sensitivity' is not XSDataDouble but %s" % self._relative_radiation_sensitivity.__class__.__name__
            raise BaseException(strMessage)
        if scaleIntensityPlot is None:
            self._scaleIntensityPlot = None
        elif scaleIntensityPlot.__class__.__name__ == "XSDataFile":
            self._scaleIntensityPlot = scaleIntensityPlot
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'scaleIntensityPlot' is not XSDataFile but %s" % self._scaleIntensityPlot.__class__.__name__
            raise BaseException(strMessage)
        if bFactorPlot is None:
            self._bFactorPlot = None
        elif bFactorPlot.__class__.__name__ == "XSDataFile":
            self._bFactorPlot = bFactorPlot
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'bFactorPlot' is not XSDataFile but %s" % self._bFactorPlot.__class__.__name__
            raise BaseException(strMessage)
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = "ERROR! XSDataResultRdfit constructor argument 'htmlPage' is not XSDataFile but %s" % self._htmlPage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'beta' attribute
    def getBeta(self): return self._beta
    def setBeta(self, beta):
        if beta is None:
            self._beta = None
        elif beta.__class__.__name__ == "XSDataDouble":
            self._beta = beta
        else:
            strMessage = "ERROR! XSDataResultRdfit.setBeta argument is not XSDataDouble but %s" % beta.__class__.__name__
            raise BaseException(strMessage)
    def delBeta(self): self._beta = None
    beta = property(getBeta, setBeta, delBeta, "Property for beta")
    # Methods and properties for the 'gama' attribute
    def getGama(self): return self._gama
    def setGama(self, gama):
        if gama is None:
            self._gama = None
        elif gama.__class__.__name__ == "XSDataDouble":
            self._gama = gama
        else:
            strMessage = "ERROR! XSDataResultRdfit.setGama argument is not XSDataDouble but %s" % gama.__class__.__name__
            raise BaseException(strMessage)
    def delGama(self): self._gama = None
    gama = property(getGama, setGama, delGama, "Property for gama")
    # Methods and properties for the 'dose_half_th' attribute
    def getDose_half_th(self): return self._dose_half_th
    def setDose_half_th(self, dose_half_th):
        if dose_half_th is None:
            self._dose_half_th = None
        elif dose_half_th.__class__.__name__ == "XSDataDouble":
            self._dose_half_th = dose_half_th
        else:
            strMessage = "ERROR! XSDataResultRdfit.setDose_half_th argument is not XSDataDouble but %s" % dose_half_th.__class__.__name__
            raise BaseException(strMessage)
    def delDose_half_th(self): self._dose_half_th = None
    dose_half_th = property(getDose_half_th, setDose_half_th, delDose_half_th, "Property for dose_half_th")
    # Methods and properties for the 'dose_half' attribute
    def getDose_half(self): return self._dose_half
    def setDose_half(self, dose_half):
        if dose_half is None:
            self._dose_half = None
        elif dose_half.__class__.__name__ == "XSDataDouble":
            self._dose_half = dose_half
        else:
            strMessage = "ERROR! XSDataResultRdfit.setDose_half argument is not XSDataDouble but %s" % dose_half.__class__.__name__
            raise BaseException(strMessage)
    def delDose_half(self): self._dose_half = None
    dose_half = property(getDose_half, setDose_half, delDose_half, "Property for dose_half")
    # Methods and properties for the 'relative_radiation_sensitivity' attribute
    def getRelative_radiation_sensitivity(self): return self._relative_radiation_sensitivity
    def setRelative_radiation_sensitivity(self, relative_radiation_sensitivity):
        if relative_radiation_sensitivity is None:
            self._relative_radiation_sensitivity = None
        elif relative_radiation_sensitivity.__class__.__name__ == "XSDataDouble":
            self._relative_radiation_sensitivity = relative_radiation_sensitivity
        else:
            strMessage = "ERROR! XSDataResultRdfit.setRelative_radiation_sensitivity argument is not XSDataDouble but %s" % relative_radiation_sensitivity.__class__.__name__
            raise BaseException(strMessage)
    def delRelative_radiation_sensitivity(self): self._relative_radiation_sensitivity = None
    relative_radiation_sensitivity = property(getRelative_radiation_sensitivity, setRelative_radiation_sensitivity, delRelative_radiation_sensitivity, "Property for relative_radiation_sensitivity")
    # Methods and properties for the 'scaleIntensityPlot' attribute
    def getScaleIntensityPlot(self): return self._scaleIntensityPlot
    def setScaleIntensityPlot(self, scaleIntensityPlot):
        if scaleIntensityPlot is None:
            self._scaleIntensityPlot = None
        elif scaleIntensityPlot.__class__.__name__ == "XSDataFile":
            self._scaleIntensityPlot = scaleIntensityPlot
        else:
            strMessage = "ERROR! XSDataResultRdfit.setScaleIntensityPlot argument is not XSDataFile but %s" % scaleIntensityPlot.__class__.__name__
            raise BaseException(strMessage)
    def delScaleIntensityPlot(self): self._scaleIntensityPlot = None
    scaleIntensityPlot = property(getScaleIntensityPlot, setScaleIntensityPlot, delScaleIntensityPlot, "Property for scaleIntensityPlot")
    # Methods and properties for the 'bFactorPlot' attribute
    def getBFactorPlot(self): return self._bFactorPlot
    def setBFactorPlot(self, bFactorPlot):
        if bFactorPlot is None:
            self._bFactorPlot = None
        elif bFactorPlot.__class__.__name__ == "XSDataFile":
            self._bFactorPlot = bFactorPlot
        else:
            strMessage = "ERROR! XSDataResultRdfit.setBFactorPlot argument is not XSDataFile but %s" % bFactorPlot.__class__.__name__
            raise BaseException(strMessage)
    def delBFactorPlot(self): self._bFactorPlot = None
    bFactorPlot = property(getBFactorPlot, setBFactorPlot, delBFactorPlot, "Property for bFactorPlot")
    # Methods and properties for the 'htmlPage' attribute
    def getHtmlPage(self): return self._htmlPage
    def setHtmlPage(self, htmlPage):
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = "ERROR! XSDataResultRdfit.setHtmlPage argument is not XSDataFile but %s" % htmlPage.__class__.__name__
            raise BaseException(strMessage)
    def delHtmlPage(self): self._htmlPage = None
    htmlPage = property(getHtmlPage, setHtmlPage, delHtmlPage, "Property for htmlPage")
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
        if self._scaleIntensityPlot is not None:
            self.scaleIntensityPlot.export(outfile, level, name_='scaleIntensityPlot')
        if self._bFactorPlot is not None:
            self.bFactorPlot.export(outfile, level, name_='bFactorPlot')
        if self._htmlPage is not None:
            self.htmlPage.export(outfile, level, name_='htmlPage')
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scaleIntensityPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScaleIntensityPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bFactorPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBFactorPlot(obj_)
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



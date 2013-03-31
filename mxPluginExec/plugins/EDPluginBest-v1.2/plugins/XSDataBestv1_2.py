#!/usr/bin/env python

#
# Generated Tue Feb 12 04:30::05 2013 by EDGenerateDS.
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
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataAbsorbedDoseRate
    from XSDataCommon import XSDataAngularSpeed
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
    from XSDataCommon import XSDataAngle
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataAbsorbedDoseRate
from XSDataCommon import XSDataAngularSpeed
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataAngle




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



class XSDataBestCollectionRun(object):
    def __init__(self, transmission=None, phiWidth=None, phiStart=None, overlaps=None, numberOfImages=None, exposureTime=None, crystalPosition=None, collectionRunNumber=None, action=None):
        if action is None:
            self._action = None
        elif action.__class__.__name__ == "XSDataString":
            self._action = action
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'action' is not XSDataString but %s" % self._action.__class__.__name__
            raise BaseException(strMessage)
        if collectionRunNumber is None:
            self._collectionRunNumber = None
        elif collectionRunNumber.__class__.__name__ == "XSDataInteger":
            self._collectionRunNumber = collectionRunNumber
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'collectionRunNumber' is not XSDataInteger but %s" % self._collectionRunNumber.__class__.__name__
            raise BaseException(strMessage)
        if crystalPosition is None:
            self._crystalPosition = None
        elif crystalPosition.__class__.__name__ == "XSDataInteger":
            self._crystalPosition = crystalPosition
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'crystalPosition' is not XSDataInteger but %s" % self._crystalPosition.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'exposureTime' is not XSDataTime but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'numberOfImages' is not XSDataInteger but %s" % self._numberOfImages.__class__.__name__
            raise BaseException(strMessage)
        if overlaps is None:
            self._overlaps = None
        elif overlaps.__class__.__name__ == "XSDataString":
            self._overlaps = overlaps
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'overlaps' is not XSDataString but %s" % self._overlaps.__class__.__name__
            raise BaseException(strMessage)
        if phiStart is None:
            self._phiStart = None
        elif phiStart.__class__.__name__ == "XSDataAngle":
            self._phiStart = phiStart
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'phiStart' is not XSDataAngle but %s" % self._phiStart.__class__.__name__
            raise BaseException(strMessage)
        if phiWidth is None:
            self._phiWidth = None
        elif phiWidth.__class__.__name__ == "XSDataAngle":
            self._phiWidth = phiWidth
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'phiWidth' is not XSDataAngle but %s" % self._phiWidth.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataBestCollectionRun constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'action' attribute
    def getAction(self): return self._action
    def setAction(self, action):
        if action is None:
            self._action = None
        elif action.__class__.__name__ == "XSDataString":
            self._action = action
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setAction argument is not XSDataString but %s" % action.__class__.__name__
            raise BaseException(strMessage)
    def delAction(self): self._action = None
    action = property(getAction, setAction, delAction, "Property for action")
    # Methods and properties for the 'collectionRunNumber' attribute
    def getCollectionRunNumber(self): return self._collectionRunNumber
    def setCollectionRunNumber(self, collectionRunNumber):
        if collectionRunNumber is None:
            self._collectionRunNumber = None
        elif collectionRunNumber.__class__.__name__ == "XSDataInteger":
            self._collectionRunNumber = collectionRunNumber
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setCollectionRunNumber argument is not XSDataInteger but %s" % collectionRunNumber.__class__.__name__
            raise BaseException(strMessage)
    def delCollectionRunNumber(self): self._collectionRunNumber = None
    collectionRunNumber = property(getCollectionRunNumber, setCollectionRunNumber, delCollectionRunNumber, "Property for collectionRunNumber")
    # Methods and properties for the 'crystalPosition' attribute
    def getCrystalPosition(self): return self._crystalPosition
    def setCrystalPosition(self, crystalPosition):
        if crystalPosition is None:
            self._crystalPosition = None
        elif crystalPosition.__class__.__name__ == "XSDataInteger":
            self._crystalPosition = crystalPosition
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setCrystalPosition argument is not XSDataInteger but %s" % crystalPosition.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalPosition(self): self._crystalPosition = None
    crystalPosition = property(getCrystalPosition, setCrystalPosition, delCrystalPosition, "Property for crystalPosition")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setExposureTime argument is not XSDataTime but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setNumberOfImages argument is not XSDataInteger but %s" % numberOfImages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'overlaps' attribute
    def getOverlaps(self): return self._overlaps
    def setOverlaps(self, overlaps):
        if overlaps is None:
            self._overlaps = None
        elif overlaps.__class__.__name__ == "XSDataString":
            self._overlaps = overlaps
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setOverlaps argument is not XSDataString but %s" % overlaps.__class__.__name__
            raise BaseException(strMessage)
    def delOverlaps(self): self._overlaps = None
    overlaps = property(getOverlaps, setOverlaps, delOverlaps, "Property for overlaps")
    # Methods and properties for the 'phiStart' attribute
    def getPhiStart(self): return self._phiStart
    def setPhiStart(self, phiStart):
        if phiStart is None:
            self._phiStart = None
        elif phiStart.__class__.__name__ == "XSDataAngle":
            self._phiStart = phiStart
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setPhiStart argument is not XSDataAngle but %s" % phiStart.__class__.__name__
            raise BaseException(strMessage)
    def delPhiStart(self): self._phiStart = None
    phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
    # Methods and properties for the 'phiWidth' attribute
    def getPhiWidth(self): return self._phiWidth
    def setPhiWidth(self, phiWidth):
        if phiWidth is None:
            self._phiWidth = None
        elif phiWidth.__class__.__name__ == "XSDataAngle":
            self._phiWidth = phiWidth
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setPhiWidth argument is not XSDataAngle but %s" % phiWidth.__class__.__name__
            raise BaseException(strMessage)
    def delPhiWidth(self): self._phiWidth = None
    phiWidth = property(getPhiWidth, setPhiWidth, delPhiWidth, "Property for phiWidth")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataBestCollectionRun.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    def export(self, outfile, level, name_='XSDataBestCollectionRun'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestCollectionRun'):
        pass
        if self._action is not None:
            self.action.export(outfile, level, name_='action')
        if self._collectionRunNumber is not None:
            self.collectionRunNumber.export(outfile, level, name_='collectionRunNumber')
        else:
            warnEmptyAttribute("collectionRunNumber", "XSDataInteger")
        if self._crystalPosition is not None:
            self.crystalPosition.export(outfile, level, name_='crystalPosition')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        else:
            warnEmptyAttribute("exposureTime", "XSDataTime")
        if self._numberOfImages is not None:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        else:
            warnEmptyAttribute("numberOfImages", "XSDataInteger")
        if self._overlaps is not None:
            self.overlaps.export(outfile, level, name_='overlaps')
        if self._phiStart is not None:
            self.phiStart.export(outfile, level, name_='phiStart')
        else:
            warnEmptyAttribute("phiStart", "XSDataAngle")
        if self._phiWidth is not None:
            self.phiWidth.export(outfile, level, name_='phiWidth')
        else:
            warnEmptyAttribute("phiWidth", "XSDataAngle")
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'action':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setAction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionRunNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setCollectionRunNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalPosition':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setCrystalPosition(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlaps':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOverlaps(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhiStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiWidth':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhiWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestCollectionRun" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestCollectionRun' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestCollectionRun is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestCollectionRun.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestCollectionRun()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestCollectionRun" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestCollectionRun()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestCollectionRun


class XSDataBestResolutionBin(object):
    def __init__(self, redundancy=None, rFriedel=None, rFactor=None, percentageOverload=None, minResolution=None, maxResolution=None, completeness=None, averageSigma=None, averageIntensityOverAverageSigma=None, averageIntensity=None, IOverSigma=None):
        if IOverSigma is None:
            self._IOverSigma = None
        elif IOverSigma.__class__.__name__ == "XSDataDouble":
            self._IOverSigma = IOverSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'IOverSigma' is not XSDataDouble but %s" % self._IOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if averageIntensity is None:
            self._averageIntensity = None
        elif averageIntensity.__class__.__name__ == "XSDataDouble":
            self._averageIntensity = averageIntensity
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'averageIntensity' is not XSDataDouble but %s" % self._averageIntensity.__class__.__name__
            raise BaseException(strMessage)
        if averageIntensityOverAverageSigma is None:
            self._averageIntensityOverAverageSigma = None
        elif averageIntensityOverAverageSigma.__class__.__name__ == "XSDataDouble":
            self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'averageIntensityOverAverageSigma' is not XSDataDouble but %s" % self._averageIntensityOverAverageSigma.__class__.__name__
            raise BaseException(strMessage)
        if averageSigma is None:
            self._averageSigma = None
        elif averageSigma.__class__.__name__ == "XSDataDouble":
            self._averageSigma = averageSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'averageSigma' is not XSDataDouble but %s" % self._averageSigma.__class__.__name__
            raise BaseException(strMessage)
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'completeness' is not XSDataDouble but %s" % self._completeness.__class__.__name__
            raise BaseException(strMessage)
        if maxResolution is None:
            self._maxResolution = None
        elif maxResolution.__class__.__name__ == "XSDataDouble":
            self._maxResolution = maxResolution
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'maxResolution' is not XSDataDouble but %s" % self._maxResolution.__class__.__name__
            raise BaseException(strMessage)
        if minResolution is None:
            self._minResolution = None
        elif minResolution.__class__.__name__ == "XSDataDouble":
            self._minResolution = minResolution
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'minResolution' is not XSDataDouble but %s" % self._minResolution.__class__.__name__
            raise BaseException(strMessage)
        if percentageOverload is None:
            self._percentageOverload = None
        elif percentageOverload.__class__.__name__ == "XSDataDouble":
            self._percentageOverload = percentageOverload
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'percentageOverload' is not XSDataDouble but %s" % self._percentageOverload.__class__.__name__
            raise BaseException(strMessage)
        if rFactor is None:
            self._rFactor = None
        elif rFactor.__class__.__name__ == "XSDataDouble":
            self._rFactor = rFactor
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'rFactor' is not XSDataDouble but %s" % self._rFactor.__class__.__name__
            raise BaseException(strMessage)
        if rFriedel is None:
            self._rFriedel = None
        elif rFriedel.__class__.__name__ == "XSDataDouble":
            self._rFriedel = rFriedel
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'rFriedel' is not XSDataDouble but %s" % self._rFriedel.__class__.__name__
            raise BaseException(strMessage)
        if redundancy is None:
            self._redundancy = None
        elif redundancy.__class__.__name__ == "XSDataDouble":
            self._redundancy = redundancy
        else:
            strMessage = "ERROR! XSDataBestResolutionBin constructor argument 'redundancy' is not XSDataDouble but %s" % self._redundancy.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'IOverSigma' attribute
    def getIOverSigma(self): return self._IOverSigma
    def setIOverSigma(self, IOverSigma):
        if IOverSigma is None:
            self._IOverSigma = None
        elif IOverSigma.__class__.__name__ == "XSDataDouble":
            self._IOverSigma = IOverSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setIOverSigma argument is not XSDataDouble but %s" % IOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delIOverSigma(self): self._IOverSigma = None
    IOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for IOverSigma")
    # Methods and properties for the 'averageIntensity' attribute
    def getAverageIntensity(self): return self._averageIntensity
    def setAverageIntensity(self, averageIntensity):
        if averageIntensity is None:
            self._averageIntensity = None
        elif averageIntensity.__class__.__name__ == "XSDataDouble":
            self._averageIntensity = averageIntensity
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setAverageIntensity argument is not XSDataDouble but %s" % averageIntensity.__class__.__name__
            raise BaseException(strMessage)
    def delAverageIntensity(self): self._averageIntensity = None
    averageIntensity = property(getAverageIntensity, setAverageIntensity, delAverageIntensity, "Property for averageIntensity")
    # Methods and properties for the 'averageIntensityOverAverageSigma' attribute
    def getAverageIntensityOverAverageSigma(self): return self._averageIntensityOverAverageSigma
    def setAverageIntensityOverAverageSigma(self, averageIntensityOverAverageSigma):
        if averageIntensityOverAverageSigma is None:
            self._averageIntensityOverAverageSigma = None
        elif averageIntensityOverAverageSigma.__class__.__name__ == "XSDataDouble":
            self._averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setAverageIntensityOverAverageSigma argument is not XSDataDouble but %s" % averageIntensityOverAverageSigma.__class__.__name__
            raise BaseException(strMessage)
    def delAverageIntensityOverAverageSigma(self): self._averageIntensityOverAverageSigma = None
    averageIntensityOverAverageSigma = property(getAverageIntensityOverAverageSigma, setAverageIntensityOverAverageSigma, delAverageIntensityOverAverageSigma, "Property for averageIntensityOverAverageSigma")
    # Methods and properties for the 'averageSigma' attribute
    def getAverageSigma(self): return self._averageSigma
    def setAverageSigma(self, averageSigma):
        if averageSigma is None:
            self._averageSigma = None
        elif averageSigma.__class__.__name__ == "XSDataDouble":
            self._averageSigma = averageSigma
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setAverageSigma argument is not XSDataDouble but %s" % averageSigma.__class__.__name__
            raise BaseException(strMessage)
    def delAverageSigma(self): self._averageSigma = None
    averageSigma = property(getAverageSigma, setAverageSigma, delAverageSigma, "Property for averageSigma")
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setCompleteness argument is not XSDataDouble but %s" % completeness.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'maxResolution' attribute
    def getMaxResolution(self): return self._maxResolution
    def setMaxResolution(self, maxResolution):
        if maxResolution is None:
            self._maxResolution = None
        elif maxResolution.__class__.__name__ == "XSDataDouble":
            self._maxResolution = maxResolution
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setMaxResolution argument is not XSDataDouble but %s" % maxResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMaxResolution(self): self._maxResolution = None
    maxResolution = property(getMaxResolution, setMaxResolution, delMaxResolution, "Property for maxResolution")
    # Methods and properties for the 'minResolution' attribute
    def getMinResolution(self): return self._minResolution
    def setMinResolution(self, minResolution):
        if minResolution is None:
            self._minResolution = None
        elif minResolution.__class__.__name__ == "XSDataDouble":
            self._minResolution = minResolution
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setMinResolution argument is not XSDataDouble but %s" % minResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMinResolution(self): self._minResolution = None
    minResolution = property(getMinResolution, setMinResolution, delMinResolution, "Property for minResolution")
    # Methods and properties for the 'percentageOverload' attribute
    def getPercentageOverload(self): return self._percentageOverload
    def setPercentageOverload(self, percentageOverload):
        if percentageOverload is None:
            self._percentageOverload = None
        elif percentageOverload.__class__.__name__ == "XSDataDouble":
            self._percentageOverload = percentageOverload
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setPercentageOverload argument is not XSDataDouble but %s" % percentageOverload.__class__.__name__
            raise BaseException(strMessage)
    def delPercentageOverload(self): self._percentageOverload = None
    percentageOverload = property(getPercentageOverload, setPercentageOverload, delPercentageOverload, "Property for percentageOverload")
    # Methods and properties for the 'rFactor' attribute
    def getRFactor(self): return self._rFactor
    def setRFactor(self, rFactor):
        if rFactor is None:
            self._rFactor = None
        elif rFactor.__class__.__name__ == "XSDataDouble":
            self._rFactor = rFactor
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setRFactor argument is not XSDataDouble but %s" % rFactor.__class__.__name__
            raise BaseException(strMessage)
    def delRFactor(self): self._rFactor = None
    rFactor = property(getRFactor, setRFactor, delRFactor, "Property for rFactor")
    # Methods and properties for the 'rFriedel' attribute
    def getRFriedel(self): return self._rFriedel
    def setRFriedel(self, rFriedel):
        if rFriedel is None:
            self._rFriedel = None
        elif rFriedel.__class__.__name__ == "XSDataDouble":
            self._rFriedel = rFriedel
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setRFriedel argument is not XSDataDouble but %s" % rFriedel.__class__.__name__
            raise BaseException(strMessage)
    def delRFriedel(self): self._rFriedel = None
    rFriedel = property(getRFriedel, setRFriedel, delRFriedel, "Property for rFriedel")
    # Methods and properties for the 'redundancy' attribute
    def getRedundancy(self): return self._redundancy
    def setRedundancy(self, redundancy):
        if redundancy is None:
            self._redundancy = None
        elif redundancy.__class__.__name__ == "XSDataDouble":
            self._redundancy = redundancy
        else:
            strMessage = "ERROR! XSDataBestResolutionBin.setRedundancy argument is not XSDataDouble but %s" % redundancy.__class__.__name__
            raise BaseException(strMessage)
    def delRedundancy(self): self._redundancy = None
    redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
    def export(self, outfile, level, name_='XSDataBestResolutionBin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestResolutionBin'):
        pass
        if self._IOverSigma is not None:
            self.IOverSigma.export(outfile, level, name_='IOverSigma')
        else:
            warnEmptyAttribute("IOverSigma", "XSDataDouble")
        if self._averageIntensity is not None:
            self.averageIntensity.export(outfile, level, name_='averageIntensity')
        else:
            warnEmptyAttribute("averageIntensity", "XSDataDouble")
        if self._averageIntensityOverAverageSigma is not None:
            self.averageIntensityOverAverageSigma.export(outfile, level, name_='averageIntensityOverAverageSigma')
        if self._averageSigma is not None:
            self.averageSigma.export(outfile, level, name_='averageSigma')
        else:
            warnEmptyAttribute("averageSigma", "XSDataDouble")
        if self._completeness is not None:
            self.completeness.export(outfile, level, name_='completeness')
        else:
            warnEmptyAttribute("completeness", "XSDataDouble")
        if self._maxResolution is not None:
            self.maxResolution.export(outfile, level, name_='maxResolution')
        else:
            warnEmptyAttribute("maxResolution", "XSDataDouble")
        if self._minResolution is not None:
            self.minResolution.export(outfile, level, name_='minResolution')
        else:
            warnEmptyAttribute("minResolution", "XSDataDouble")
        if self._percentageOverload is not None:
            self.percentageOverload.export(outfile, level, name_='percentageOverload')
        else:
            warnEmptyAttribute("percentageOverload", "XSDataDouble")
        if self._rFactor is not None:
            self.rFactor.export(outfile, level, name_='rFactor')
        else:
            warnEmptyAttribute("rFactor", "XSDataDouble")
        if self._rFriedel is not None:
            self.rFriedel.export(outfile, level, name_='rFriedel')
        if self._redundancy is not None:
            self.redundancy.export(outfile, level, name_='redundancy')
        else:
            warnEmptyAttribute("redundancy", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'IOverSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAverageIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensityOverAverageSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAverageIntensityOverAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMinResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'percentageOverload':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPercentageOverload(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rFriedel':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRFriedel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'redundancy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRedundancy(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestResolutionBin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestResolutionBin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestResolutionBin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestResolutionBin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestResolutionBin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestResolutionBin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestResolutionBin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestResolutionBin


class XSDataBestStatisticalPrediction(object):
    def __init__(self, resolutionBin=None):
        if resolutionBin is None:
            self._resolutionBin = []
        elif resolutionBin.__class__.__name__ == "list":
            self._resolutionBin = resolutionBin
        else:
            strMessage = "ERROR! XSDataBestStatisticalPrediction constructor argument 'resolutionBin' is not list but %s" % self._resolutionBin.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'resolutionBin' attribute
    def getResolutionBin(self): return self._resolutionBin
    def setResolutionBin(self, resolutionBin):
        if resolutionBin is None:
            self._resolutionBin = []
        elif resolutionBin.__class__.__name__ == "list":
            self._resolutionBin = resolutionBin
        else:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.setResolutionBin argument is not list but %s" % resolutionBin.__class__.__name__
            raise BaseException(strMessage)
    def delResolutionBin(self): self._resolutionBin = None
    resolutionBin = property(getResolutionBin, setResolutionBin, delResolutionBin, "Property for resolutionBin")
    def addResolutionBin(self, value):
        if value is None:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.addResolutionBin argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestResolutionBin":
            self._resolutionBin.append(value)
        else:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.addResolutionBin argument is not XSDataBestResolutionBin but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertResolutionBin(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.insertResolutionBin argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.insertResolutionBin argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestResolutionBin":
            self._resolutionBin[index] = value
        else:
            strMessage = "ERROR! XSDataBestStatisticalPrediction.addResolutionBin argument is not XSDataBestResolutionBin but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataBestStatisticalPrediction'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestStatisticalPrediction'):
        pass
        for resolutionBin_ in self.getResolutionBin():
            resolutionBin_.export(outfile, level, name_='resolutionBin')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionBin':
            obj_ = XSDataBestResolutionBin()
            obj_.build(child_)
            self.resolutionBin.append(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestStatisticalPrediction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestStatisticalPrediction' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestStatisticalPrediction is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestStatisticalPrediction.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestStatisticalPrediction()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestStatisticalPrediction" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestStatisticalPrediction()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestStatisticalPrediction


class XSDataBestStrategySummary(object):
    def __init__(self, transmission=None, totalExposureTime=None, totalDataCollectionTime=None, resolutionReasoning=None, resolution=None, redundancy=None, rankingResolution=None, iSigma=None, distance=None, completeness=None):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'completeness' is not XSDataDouble but %s" % self._completeness.__class__.__name__
            raise BaseException(strMessage)
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'distance' is not XSDataLength but %s" % self._distance.__class__.__name__
            raise BaseException(strMessage)
        if iSigma is None:
            self._iSigma = None
        elif iSigma.__class__.__name__ == "XSDataDouble":
            self._iSigma = iSigma
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'iSigma' is not XSDataDouble but %s" % self._iSigma.__class__.__name__
            raise BaseException(strMessage)
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'rankingResolution' is not XSDataDouble but %s" % self._rankingResolution.__class__.__name__
            raise BaseException(strMessage)
        if redundancy is None:
            self._redundancy = None
        elif redundancy.__class__.__name__ == "XSDataDouble":
            self._redundancy = redundancy
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'redundancy' is not XSDataDouble but %s" % self._redundancy.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if resolutionReasoning is None:
            self._resolutionReasoning = None
        elif resolutionReasoning.__class__.__name__ == "XSDataString":
            self._resolutionReasoning = resolutionReasoning
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'resolutionReasoning' is not XSDataString but %s" % self._resolutionReasoning.__class__.__name__
            raise BaseException(strMessage)
        if totalDataCollectionTime is None:
            self._totalDataCollectionTime = None
        elif totalDataCollectionTime.__class__.__name__ == "XSDataTime":
            self._totalDataCollectionTime = totalDataCollectionTime
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'totalDataCollectionTime' is not XSDataTime but %s" % self._totalDataCollectionTime.__class__.__name__
            raise BaseException(strMessage)
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataTime":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'totalExposureTime' is not XSDataTime but %s" % self._totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataBestStrategySummary constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setCompleteness argument is not XSDataDouble but %s" % completeness.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'distance' attribute
    def getDistance(self): return self._distance
    def setDistance(self, distance):
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setDistance argument is not XSDataLength but %s" % distance.__class__.__name__
            raise BaseException(strMessage)
    def delDistance(self): self._distance = None
    distance = property(getDistance, setDistance, delDistance, "Property for distance")
    # Methods and properties for the 'iSigma' attribute
    def getISigma(self): return self._iSigma
    def setISigma(self, iSigma):
        if iSigma is None:
            self._iSigma = None
        elif iSigma.__class__.__name__ == "XSDataDouble":
            self._iSigma = iSigma
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setISigma argument is not XSDataDouble but %s" % iSigma.__class__.__name__
            raise BaseException(strMessage)
    def delISigma(self): self._iSigma = None
    iSigma = property(getISigma, setISigma, delISigma, "Property for iSigma")
    # Methods and properties for the 'rankingResolution' attribute
    def getRankingResolution(self): return self._rankingResolution
    def setRankingResolution(self, rankingResolution):
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setRankingResolution argument is not XSDataDouble but %s" % rankingResolution.__class__.__name__
            raise BaseException(strMessage)
    def delRankingResolution(self): self._rankingResolution = None
    rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
    # Methods and properties for the 'redundancy' attribute
    def getRedundancy(self): return self._redundancy
    def setRedundancy(self, redundancy):
        if redundancy is None:
            self._redundancy = None
        elif redundancy.__class__.__name__ == "XSDataDouble":
            self._redundancy = redundancy
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setRedundancy argument is not XSDataDouble but %s" % redundancy.__class__.__name__
            raise BaseException(strMessage)
    def delRedundancy(self): self._redundancy = None
    redundancy = property(getRedundancy, setRedundancy, delRedundancy, "Property for redundancy")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'resolutionReasoning' attribute
    def getResolutionReasoning(self): return self._resolutionReasoning
    def setResolutionReasoning(self, resolutionReasoning):
        if resolutionReasoning is None:
            self._resolutionReasoning = None
        elif resolutionReasoning.__class__.__name__ == "XSDataString":
            self._resolutionReasoning = resolutionReasoning
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setResolutionReasoning argument is not XSDataString but %s" % resolutionReasoning.__class__.__name__
            raise BaseException(strMessage)
    def delResolutionReasoning(self): self._resolutionReasoning = None
    resolutionReasoning = property(getResolutionReasoning, setResolutionReasoning, delResolutionReasoning, "Property for resolutionReasoning")
    # Methods and properties for the 'totalDataCollectionTime' attribute
    def getTotalDataCollectionTime(self): return self._totalDataCollectionTime
    def setTotalDataCollectionTime(self, totalDataCollectionTime):
        if totalDataCollectionTime is None:
            self._totalDataCollectionTime = None
        elif totalDataCollectionTime.__class__.__name__ == "XSDataTime":
            self._totalDataCollectionTime = totalDataCollectionTime
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setTotalDataCollectionTime argument is not XSDataTime but %s" % totalDataCollectionTime.__class__.__name__
            raise BaseException(strMessage)
    def delTotalDataCollectionTime(self): self._totalDataCollectionTime = None
    totalDataCollectionTime = property(getTotalDataCollectionTime, setTotalDataCollectionTime, delTotalDataCollectionTime, "Property for totalDataCollectionTime")
    # Methods and properties for the 'totalExposureTime' attribute
    def getTotalExposureTime(self): return self._totalExposureTime
    def setTotalExposureTime(self, totalExposureTime):
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataTime":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setTotalExposureTime argument is not XSDataTime but %s" % totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delTotalExposureTime(self): self._totalExposureTime = None
    totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataBestStrategySummary.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    def export(self, outfile, level, name_='XSDataBestStrategySummary'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestStrategySummary'):
        pass
        if self._completeness is not None:
            self.completeness.export(outfile, level, name_='completeness')
        if self._distance is not None:
            self.distance.export(outfile, level, name_='distance')
        else:
            warnEmptyAttribute("distance", "XSDataLength")
        if self._iSigma is not None:
            self.iSigma.export(outfile, level, name_='iSigma')
        if self._rankingResolution is not None:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
        if self._redundancy is not None:
            self.redundancy.export(outfile, level, name_='redundancy')
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        else:
            warnEmptyAttribute("resolution", "XSDataDouble")
        if self._resolutionReasoning is not None:
            self.resolutionReasoning.export(outfile, level, name_='resolutionReasoning')
        if self._totalDataCollectionTime is not None:
            self.totalDataCollectionTime.export(outfile, level, name_='totalDataCollectionTime')
        if self._totalExposureTime is not None:
            self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setISigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRankingResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'redundancy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRedundancy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionReasoning':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setResolutionReasoning(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalDataCollectionTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTotalDataCollectionTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalExposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTotalExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestStrategySummary" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestStrategySummary' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestStrategySummary is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestStrategySummary.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestStrategySummary()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestStrategySummary" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestStrategySummary()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestStrategySummary


class XSDataCrystalScale(object):
    def __init__(self, scale=None, bFactor=None):
        if bFactor is None:
            self._bFactor = None
        elif bFactor.__class__.__name__ == "XSDataDouble":
            self._bFactor = bFactor
        else:
            strMessage = "ERROR! XSDataCrystalScale constructor argument 'bFactor' is not XSDataDouble but %s" % self._bFactor.__class__.__name__
            raise BaseException(strMessage)
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataCrystalScale constructor argument 'scale' is not XSDataDouble but %s" % self._scale.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bFactor' attribute
    def getBFactor(self): return self._bFactor
    def setBFactor(self, bFactor):
        if bFactor is None:
            self._bFactor = None
        elif bFactor.__class__.__name__ == "XSDataDouble":
            self._bFactor = bFactor
        else:
            strMessage = "ERROR! XSDataCrystalScale.setBFactor argument is not XSDataDouble but %s" % bFactor.__class__.__name__
            raise BaseException(strMessage)
    def delBFactor(self): self._bFactor = None
    bFactor = property(getBFactor, setBFactor, delBFactor, "Property for bFactor")
    # Methods and properties for the 'scale' attribute
    def getScale(self): return self._scale
    def setScale(self, scale):
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataCrystalScale.setScale argument is not XSDataDouble but %s" % scale.__class__.__name__
            raise BaseException(strMessage)
    def delScale(self): self._scale = None
    scale = property(getScale, setScale, delScale, "Property for scale")
    def export(self, outfile, level, name_='XSDataCrystalScale'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataCrystalScale'):
        pass
        if self._bFactor is not None:
            self.bFactor.export(outfile, level, name_='bFactor')
        else:
            warnEmptyAttribute("bFactor", "XSDataDouble")
        if self._scale is not None:
            self.scale.export(outfile, level, name_='scale')
        else:
            warnEmptyAttribute("scale", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scale':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setScale(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataCrystalScale" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataCrystalScale' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataCrystalScale is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataCrystalScale.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCrystalScale()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataCrystalScale" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCrystalScale()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataCrystalScale


class XSDataBestCollectionPlan(object):
    def __init__(self, strategySummary=None, statisticalPrediction=None, crystalScale=None, comment=None, collectionRun=None, collectionPlanNumber=None):
        if collectionPlanNumber is None:
            self._collectionPlanNumber = None
        elif collectionPlanNumber.__class__.__name__ == "XSDataInteger":
            self._collectionPlanNumber = collectionPlanNumber
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'collectionPlanNumber' is not XSDataInteger but %s" % self._collectionPlanNumber.__class__.__name__
            raise BaseException(strMessage)
        if collectionRun is None:
            self._collectionRun = []
        elif collectionRun.__class__.__name__ == "list":
            self._collectionRun = collectionRun
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'collectionRun' is not list but %s" % self._collectionRun.__class__.__name__
            raise BaseException(strMessage)
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'comment' is not XSDataString but %s" % self._comment.__class__.__name__
            raise BaseException(strMessage)
        if crystalScale is None:
            self._crystalScale = None
        elif crystalScale.__class__.__name__ == "XSDataCrystalScale":
            self._crystalScale = crystalScale
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'crystalScale' is not XSDataCrystalScale but %s" % self._crystalScale.__class__.__name__
            raise BaseException(strMessage)
        if statisticalPrediction is None:
            self._statisticalPrediction = None
        elif statisticalPrediction.__class__.__name__ == "XSDataBestStatisticalPrediction":
            self._statisticalPrediction = statisticalPrediction
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'statisticalPrediction' is not XSDataBestStatisticalPrediction but %s" % self._statisticalPrediction.__class__.__name__
            raise BaseException(strMessage)
        if strategySummary is None:
            self._strategySummary = None
        elif strategySummary.__class__.__name__ == "XSDataBestStrategySummary":
            self._strategySummary = strategySummary
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan constructor argument 'strategySummary' is not XSDataBestStrategySummary but %s" % self._strategySummary.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'collectionPlanNumber' attribute
    def getCollectionPlanNumber(self): return self._collectionPlanNumber
    def setCollectionPlanNumber(self, collectionPlanNumber):
        if collectionPlanNumber is None:
            self._collectionPlanNumber = None
        elif collectionPlanNumber.__class__.__name__ == "XSDataInteger":
            self._collectionPlanNumber = collectionPlanNumber
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setCollectionPlanNumber argument is not XSDataInteger but %s" % collectionPlanNumber.__class__.__name__
            raise BaseException(strMessage)
    def delCollectionPlanNumber(self): self._collectionPlanNumber = None
    collectionPlanNumber = property(getCollectionPlanNumber, setCollectionPlanNumber, delCollectionPlanNumber, "Property for collectionPlanNumber")
    # Methods and properties for the 'collectionRun' attribute
    def getCollectionRun(self): return self._collectionRun
    def setCollectionRun(self, collectionRun):
        if collectionRun is None:
            self._collectionRun = []
        elif collectionRun.__class__.__name__ == "list":
            self._collectionRun = collectionRun
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setCollectionRun argument is not list but %s" % collectionRun.__class__.__name__
            raise BaseException(strMessage)
    def delCollectionRun(self): self._collectionRun = None
    collectionRun = property(getCollectionRun, setCollectionRun, delCollectionRun, "Property for collectionRun")
    def addCollectionRun(self, value):
        if value is None:
            strMessage = "ERROR! XSDataBestCollectionPlan.addCollectionRun argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestCollectionRun":
            self._collectionRun.append(value)
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.addCollectionRun argument is not XSDataBestCollectionRun but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCollectionRun(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataBestCollectionPlan.insertCollectionRun argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataBestCollectionPlan.insertCollectionRun argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestCollectionRun":
            self._collectionRun[index] = value
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.addCollectionRun argument is not XSDataBestCollectionRun but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'comment' attribute
    def getComment(self): return self._comment
    def setComment(self, comment):
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setComment argument is not XSDataString but %s" % comment.__class__.__name__
            raise BaseException(strMessage)
    def delComment(self): self._comment = None
    comment = property(getComment, setComment, delComment, "Property for comment")
    # Methods and properties for the 'crystalScale' attribute
    def getCrystalScale(self): return self._crystalScale
    def setCrystalScale(self, crystalScale):
        if crystalScale is None:
            self._crystalScale = None
        elif crystalScale.__class__.__name__ == "XSDataCrystalScale":
            self._crystalScale = crystalScale
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setCrystalScale argument is not XSDataCrystalScale but %s" % crystalScale.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalScale(self): self._crystalScale = None
    crystalScale = property(getCrystalScale, setCrystalScale, delCrystalScale, "Property for crystalScale")
    # Methods and properties for the 'statisticalPrediction' attribute
    def getStatisticalPrediction(self): return self._statisticalPrediction
    def setStatisticalPrediction(self, statisticalPrediction):
        if statisticalPrediction is None:
            self._statisticalPrediction = None
        elif statisticalPrediction.__class__.__name__ == "XSDataBestStatisticalPrediction":
            self._statisticalPrediction = statisticalPrediction
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setStatisticalPrediction argument is not XSDataBestStatisticalPrediction but %s" % statisticalPrediction.__class__.__name__
            raise BaseException(strMessage)
    def delStatisticalPrediction(self): self._statisticalPrediction = None
    statisticalPrediction = property(getStatisticalPrediction, setStatisticalPrediction, delStatisticalPrediction, "Property for statisticalPrediction")
    # Methods and properties for the 'strategySummary' attribute
    def getStrategySummary(self): return self._strategySummary
    def setStrategySummary(self, strategySummary):
        if strategySummary is None:
            self._strategySummary = None
        elif strategySummary.__class__.__name__ == "XSDataBestStrategySummary":
            self._strategySummary = strategySummary
        else:
            strMessage = "ERROR! XSDataBestCollectionPlan.setStrategySummary argument is not XSDataBestStrategySummary but %s" % strategySummary.__class__.__name__
            raise BaseException(strMessage)
    def delStrategySummary(self): self._strategySummary = None
    strategySummary = property(getStrategySummary, setStrategySummary, delStrategySummary, "Property for strategySummary")
    def export(self, outfile, level, name_='XSDataBestCollectionPlan'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestCollectionPlan'):
        pass
        if self._collectionPlanNumber is not None:
            self.collectionPlanNumber.export(outfile, level, name_='collectionPlanNumber')
        for collectionRun_ in self.getCollectionRun():
            collectionRun_.export(outfile, level, name_='collectionRun')
        if self._comment is not None:
            self.comment.export(outfile, level, name_='comment')
        if self._crystalScale is not None:
            self.crystalScale.export(outfile, level, name_='crystalScale')
        if self._statisticalPrediction is not None:
            self.statisticalPrediction.export(outfile, level, name_='statisticalPrediction')
        if self._strategySummary is not None:
            self.strategySummary.export(outfile, level, name_='strategySummary')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionPlanNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setCollectionPlanNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionRun':
            obj_ = XSDataBestCollectionRun()
            obj_.build(child_)
            self.collectionRun.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComment(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalScale':
            obj_ = XSDataCrystalScale()
            obj_.build(child_)
            self.setCrystalScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statisticalPrediction':
            obj_ = XSDataBestStatisticalPrediction()
            obj_.build(child_)
            self.setStatisticalPrediction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategySummary':
            obj_ = XSDataBestStrategySummary()
            obj_.build(child_)
            self.setStrategySummary(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestCollectionPlan" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestCollectionPlan' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestCollectionPlan is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestCollectionPlan.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestCollectionPlan()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestCollectionPlan" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestCollectionPlan()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestCollectionPlan


class XSDataBestGlePlot(object):
    def __init__(self, script=None, data=None):
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataFile":
            self._data = data
        else:
            strMessage = "ERROR! XSDataBestGlePlot constructor argument 'data' is not XSDataFile but %s" % self._data.__class__.__name__
            raise BaseException(strMessage)
        if script is None:
            self._script = None
        elif script.__class__.__name__ == "XSDataFile":
            self._script = script
        else:
            strMessage = "ERROR! XSDataBestGlePlot constructor argument 'script' is not XSDataFile but %s" % self._script.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'data' attribute
    def getData(self): return self._data
    def setData(self, data):
        if data is None:
            self._data = None
        elif data.__class__.__name__ == "XSDataFile":
            self._data = data
        else:
            strMessage = "ERROR! XSDataBestGlePlot.setData argument is not XSDataFile but %s" % data.__class__.__name__
            raise BaseException(strMessage)
    def delData(self): self._data = None
    data = property(getData, setData, delData, "Property for data")
    # Methods and properties for the 'script' attribute
    def getScript(self): return self._script
    def setScript(self, script):
        if script is None:
            self._script = None
        elif script.__class__.__name__ == "XSDataFile":
            self._script = script
        else:
            strMessage = "ERROR! XSDataBestGlePlot.setScript argument is not XSDataFile but %s" % script.__class__.__name__
            raise BaseException(strMessage)
    def delScript(self): self._script = None
    script = property(getScript, setScript, delScript, "Property for script")
    def export(self, outfile, level, name_='XSDataBestGlePlot'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBestGlePlot'):
        pass
        if self._data is not None:
            self.data.export(outfile, level, name_='data')
        else:
            warnEmptyAttribute("data", "XSDataFile")
        if self._script is not None:
            self.script.export(outfile, level, name_='script')
        else:
            warnEmptyAttribute("script", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setData(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'script':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScript(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBestGlePlot" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBestGlePlot' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBestGlePlot is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBestGlePlot.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBestGlePlot()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBestGlePlot" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBestGlePlot()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBestGlePlot


class XSDataInputBest(XSDataInput):
    """- anomalousData is deprecated, please use strategyOption instead.

- minTransmission will work only with version v3.4 or higher of Best

- xdsBackgroundFile will only work with version v3.4.1 or higher of Best

- detectorDistanceMin and detectorDistanceMax (in mm) will work only with version v3.4.3 or higher of Best
"""
    def __init__(self, configuration=None, xdsBackgroundImage=None, userDefinedRotationStart=None, userDefinedRotationRange=None, transmission=None, strategyOption=None, radiationDamageModelGamma=None, radiationDamageModelBeta=None, numberOfCrystalPositions=None, minTransmission=None, goniostatMinRotationWidth=None, goniostatMaxRotationSpeed=None, detectorType=None, detectorDistanceMin=None, detectorDistanceMax=None, crystalSusceptibility=None, crystalShape=None, crystalAbsorbedDoseRate=None, complexity=None, bestFileContentPar=None, bestFileContentHKL=None, bestFileContentDat=None, beamMinExposureTime=None, beamMaxExposureTime=None, beamExposureTime=None, anomalousData=None, aimedResolution=None, aimedRedundancy=None, aimedIOverSigma=None, aimedCompleteness=None):
        XSDataInput.__init__(self, configuration)
        if aimedCompleteness is None:
            self._aimedCompleteness = None
        elif aimedCompleteness.__class__.__name__ == "XSDataDouble":
            self._aimedCompleteness = aimedCompleteness
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'aimedCompleteness' is not XSDataDouble but %s" % self._aimedCompleteness.__class__.__name__
            raise BaseException(strMessage)
        if aimedIOverSigma is None:
            self._aimedIOverSigma = None
        elif aimedIOverSigma.__class__.__name__ == "XSDataDouble":
            self._aimedIOverSigma = aimedIOverSigma
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'aimedIOverSigma' is not XSDataDouble but %s" % self._aimedIOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if aimedRedundancy is None:
            self._aimedRedundancy = None
        elif aimedRedundancy.__class__.__name__ == "XSDataDouble":
            self._aimedRedundancy = aimedRedundancy
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'aimedRedundancy' is not XSDataDouble but %s" % self._aimedRedundancy.__class__.__name__
            raise BaseException(strMessage)
        if aimedResolution is None:
            self._aimedResolution = None
        elif aimedResolution.__class__.__name__ == "XSDataDouble":
            self._aimedResolution = aimedResolution
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'aimedResolution' is not XSDataDouble but %s" % self._aimedResolution.__class__.__name__
            raise BaseException(strMessage)
        if anomalousData is None:
            self._anomalousData = None
        elif anomalousData.__class__.__name__ == "XSDataBoolean":
            self._anomalousData = anomalousData
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'anomalousData' is not XSDataBoolean but %s" % self._anomalousData.__class__.__name__
            raise BaseException(strMessage)
        if beamExposureTime is None:
            self._beamExposureTime = None
        elif beamExposureTime.__class__.__name__ == "XSDataTime":
            self._beamExposureTime = beamExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'beamExposureTime' is not XSDataTime but %s" % self._beamExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if beamMaxExposureTime is None:
            self._beamMaxExposureTime = None
        elif beamMaxExposureTime.__class__.__name__ == "XSDataTime":
            self._beamMaxExposureTime = beamMaxExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'beamMaxExposureTime' is not XSDataTime but %s" % self._beamMaxExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if beamMinExposureTime is None:
            self._beamMinExposureTime = None
        elif beamMinExposureTime.__class__.__name__ == "XSDataTime":
            self._beamMinExposureTime = beamMinExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'beamMinExposureTime' is not XSDataTime but %s" % self._beamMinExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if bestFileContentDat is None:
            self._bestFileContentDat = None
        elif bestFileContentDat.__class__.__name__ == "XSDataString":
            self._bestFileContentDat = bestFileContentDat
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'bestFileContentDat' is not XSDataString but %s" % self._bestFileContentDat.__class__.__name__
            raise BaseException(strMessage)
        if bestFileContentHKL is None:
            self._bestFileContentHKL = []
        elif bestFileContentHKL.__class__.__name__ == "list":
            self._bestFileContentHKL = bestFileContentHKL
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'bestFileContentHKL' is not list but %s" % self._bestFileContentHKL.__class__.__name__
            raise BaseException(strMessage)
        if bestFileContentPar is None:
            self._bestFileContentPar = None
        elif bestFileContentPar.__class__.__name__ == "XSDataString":
            self._bestFileContentPar = bestFileContentPar
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'bestFileContentPar' is not XSDataString but %s" % self._bestFileContentPar.__class__.__name__
            raise BaseException(strMessage)
        if complexity is None:
            self._complexity = None
        elif complexity.__class__.__name__ == "XSDataString":
            self._complexity = complexity
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'complexity' is not XSDataString but %s" % self._complexity.__class__.__name__
            raise BaseException(strMessage)
        if crystalAbsorbedDoseRate is None:
            self._crystalAbsorbedDoseRate = None
        elif crystalAbsorbedDoseRate.__class__.__name__ == "XSDataAbsorbedDoseRate":
            self._crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'crystalAbsorbedDoseRate' is not XSDataAbsorbedDoseRate but %s" % self._crystalAbsorbedDoseRate.__class__.__name__
            raise BaseException(strMessage)
        if crystalShape is None:
            self._crystalShape = None
        elif crystalShape.__class__.__name__ == "XSDataDouble":
            self._crystalShape = crystalShape
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'crystalShape' is not XSDataDouble but %s" % self._crystalShape.__class__.__name__
            raise BaseException(strMessage)
        if crystalSusceptibility is None:
            self._crystalSusceptibility = None
        elif crystalSusceptibility.__class__.__name__ == "XSDataDouble":
            self._crystalSusceptibility = crystalSusceptibility
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'crystalSusceptibility' is not XSDataDouble but %s" % self._crystalSusceptibility.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistanceMax is None:
            self._detectorDistanceMax = None
        elif detectorDistanceMax.__class__.__name__ == "XSDataLength":
            self._detectorDistanceMax = detectorDistanceMax
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'detectorDistanceMax' is not XSDataLength but %s" % self._detectorDistanceMax.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistanceMin is None:
            self._detectorDistanceMin = None
        elif detectorDistanceMin.__class__.__name__ == "XSDataLength":
            self._detectorDistanceMin = detectorDistanceMin
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'detectorDistanceMin' is not XSDataLength but %s" % self._detectorDistanceMin.__class__.__name__
            raise BaseException(strMessage)
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'detectorType' is not XSDataString but %s" % self._detectorType.__class__.__name__
            raise BaseException(strMessage)
        if goniostatMaxRotationSpeed is None:
            self._goniostatMaxRotationSpeed = None
        elif goniostatMaxRotationSpeed.__class__.__name__ == "XSDataAngularSpeed":
            self._goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'goniostatMaxRotationSpeed' is not XSDataAngularSpeed but %s" % self._goniostatMaxRotationSpeed.__class__.__name__
            raise BaseException(strMessage)
        if goniostatMinRotationWidth is None:
            self._goniostatMinRotationWidth = None
        elif goniostatMinRotationWidth.__class__.__name__ == "XSDataAngle":
            self._goniostatMinRotationWidth = goniostatMinRotationWidth
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'goniostatMinRotationWidth' is not XSDataAngle but %s" % self._goniostatMinRotationWidth.__class__.__name__
            raise BaseException(strMessage)
        if minTransmission is None:
            self._minTransmission = None
        elif minTransmission.__class__.__name__ == "XSDataDouble":
            self._minTransmission = minTransmission
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'minTransmission' is not XSDataDouble but %s" % self._minTransmission.__class__.__name__
            raise BaseException(strMessage)
        if numberOfCrystalPositions is None:
            self._numberOfCrystalPositions = None
        elif numberOfCrystalPositions.__class__.__name__ == "XSDataInteger":
            self._numberOfCrystalPositions = numberOfCrystalPositions
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'numberOfCrystalPositions' is not XSDataInteger but %s" % self._numberOfCrystalPositions.__class__.__name__
            raise BaseException(strMessage)
        if radiationDamageModelBeta is None:
            self._radiationDamageModelBeta = None
        elif radiationDamageModelBeta.__class__.__name__ == "XSDataDouble":
            self._radiationDamageModelBeta = radiationDamageModelBeta
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'radiationDamageModelBeta' is not XSDataDouble but %s" % self._radiationDamageModelBeta.__class__.__name__
            raise BaseException(strMessage)
        if radiationDamageModelGamma is None:
            self._radiationDamageModelGamma = None
        elif radiationDamageModelGamma.__class__.__name__ == "XSDataDouble":
            self._radiationDamageModelGamma = radiationDamageModelGamma
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'radiationDamageModelGamma' is not XSDataDouble but %s" % self._radiationDamageModelGamma.__class__.__name__
            raise BaseException(strMessage)
        if strategyOption is None:
            self._strategyOption = None
        elif strategyOption.__class__.__name__ == "XSDataString":
            self._strategyOption = strategyOption
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'strategyOption' is not XSDataString but %s" % self._strategyOption.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
        if userDefinedRotationRange is None:
            self._userDefinedRotationRange = None
        elif userDefinedRotationRange.__class__.__name__ == "XSDataAngle":
            self._userDefinedRotationRange = userDefinedRotationRange
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'userDefinedRotationRange' is not XSDataAngle but %s" % self._userDefinedRotationRange.__class__.__name__
            raise BaseException(strMessage)
        if userDefinedRotationStart is None:
            self._userDefinedRotationStart = None
        elif userDefinedRotationStart.__class__.__name__ == "XSDataAngle":
            self._userDefinedRotationStart = userDefinedRotationStart
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'userDefinedRotationStart' is not XSDataAngle but %s" % self._userDefinedRotationStart.__class__.__name__
            raise BaseException(strMessage)
        if xdsBackgroundImage is None:
            self._xdsBackgroundImage = None
        elif xdsBackgroundImage.__class__.__name__ == "XSDataFile":
            self._xdsBackgroundImage = xdsBackgroundImage
        else:
            strMessage = "ERROR! XSDataInputBest constructor argument 'xdsBackgroundImage' is not XSDataFile but %s" % self._xdsBackgroundImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'aimedCompleteness' attribute
    def getAimedCompleteness(self): return self._aimedCompleteness
    def setAimedCompleteness(self, aimedCompleteness):
        if aimedCompleteness is None:
            self._aimedCompleteness = None
        elif aimedCompleteness.__class__.__name__ == "XSDataDouble":
            self._aimedCompleteness = aimedCompleteness
        else:
            strMessage = "ERROR! XSDataInputBest.setAimedCompleteness argument is not XSDataDouble but %s" % aimedCompleteness.__class__.__name__
            raise BaseException(strMessage)
    def delAimedCompleteness(self): self._aimedCompleteness = None
    aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
    # Methods and properties for the 'aimedIOverSigma' attribute
    def getAimedIOverSigma(self): return self._aimedIOverSigma
    def setAimedIOverSigma(self, aimedIOverSigma):
        if aimedIOverSigma is None:
            self._aimedIOverSigma = None
        elif aimedIOverSigma.__class__.__name__ == "XSDataDouble":
            self._aimedIOverSigma = aimedIOverSigma
        else:
            strMessage = "ERROR! XSDataInputBest.setAimedIOverSigma argument is not XSDataDouble but %s" % aimedIOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delAimedIOverSigma(self): self._aimedIOverSigma = None
    aimedIOverSigma = property(getAimedIOverSigma, setAimedIOverSigma, delAimedIOverSigma, "Property for aimedIOverSigma")
    # Methods and properties for the 'aimedRedundancy' attribute
    def getAimedRedundancy(self): return self._aimedRedundancy
    def setAimedRedundancy(self, aimedRedundancy):
        if aimedRedundancy is None:
            self._aimedRedundancy = None
        elif aimedRedundancy.__class__.__name__ == "XSDataDouble":
            self._aimedRedundancy = aimedRedundancy
        else:
            strMessage = "ERROR! XSDataInputBest.setAimedRedundancy argument is not XSDataDouble but %s" % aimedRedundancy.__class__.__name__
            raise BaseException(strMessage)
    def delAimedRedundancy(self): self._aimedRedundancy = None
    aimedRedundancy = property(getAimedRedundancy, setAimedRedundancy, delAimedRedundancy, "Property for aimedRedundancy")
    # Methods and properties for the 'aimedResolution' attribute
    def getAimedResolution(self): return self._aimedResolution
    def setAimedResolution(self, aimedResolution):
        if aimedResolution is None:
            self._aimedResolution = None
        elif aimedResolution.__class__.__name__ == "XSDataDouble":
            self._aimedResolution = aimedResolution
        else:
            strMessage = "ERROR! XSDataInputBest.setAimedResolution argument is not XSDataDouble but %s" % aimedResolution.__class__.__name__
            raise BaseException(strMessage)
    def delAimedResolution(self): self._aimedResolution = None
    aimedResolution = property(getAimedResolution, setAimedResolution, delAimedResolution, "Property for aimedResolution")
    # Methods and properties for the 'anomalousData' attribute
    def getAnomalousData(self): return self._anomalousData
    def setAnomalousData(self, anomalousData):
        if anomalousData is None:
            self._anomalousData = None
        elif anomalousData.__class__.__name__ == "XSDataBoolean":
            self._anomalousData = anomalousData
        else:
            strMessage = "ERROR! XSDataInputBest.setAnomalousData argument is not XSDataBoolean but %s" % anomalousData.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalousData(self): self._anomalousData = None
    anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
    # Methods and properties for the 'beamExposureTime' attribute
    def getBeamExposureTime(self): return self._beamExposureTime
    def setBeamExposureTime(self, beamExposureTime):
        if beamExposureTime is None:
            self._beamExposureTime = None
        elif beamExposureTime.__class__.__name__ == "XSDataTime":
            self._beamExposureTime = beamExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest.setBeamExposureTime argument is not XSDataTime but %s" % beamExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delBeamExposureTime(self): self._beamExposureTime = None
    beamExposureTime = property(getBeamExposureTime, setBeamExposureTime, delBeamExposureTime, "Property for beamExposureTime")
    # Methods and properties for the 'beamMaxExposureTime' attribute
    def getBeamMaxExposureTime(self): return self._beamMaxExposureTime
    def setBeamMaxExposureTime(self, beamMaxExposureTime):
        if beamMaxExposureTime is None:
            self._beamMaxExposureTime = None
        elif beamMaxExposureTime.__class__.__name__ == "XSDataTime":
            self._beamMaxExposureTime = beamMaxExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest.setBeamMaxExposureTime argument is not XSDataTime but %s" % beamMaxExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delBeamMaxExposureTime(self): self._beamMaxExposureTime = None
    beamMaxExposureTime = property(getBeamMaxExposureTime, setBeamMaxExposureTime, delBeamMaxExposureTime, "Property for beamMaxExposureTime")
    # Methods and properties for the 'beamMinExposureTime' attribute
    def getBeamMinExposureTime(self): return self._beamMinExposureTime
    def setBeamMinExposureTime(self, beamMinExposureTime):
        if beamMinExposureTime is None:
            self._beamMinExposureTime = None
        elif beamMinExposureTime.__class__.__name__ == "XSDataTime":
            self._beamMinExposureTime = beamMinExposureTime
        else:
            strMessage = "ERROR! XSDataInputBest.setBeamMinExposureTime argument is not XSDataTime but %s" % beamMinExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delBeamMinExposureTime(self): self._beamMinExposureTime = None
    beamMinExposureTime = property(getBeamMinExposureTime, setBeamMinExposureTime, delBeamMinExposureTime, "Property for beamMinExposureTime")
    # Methods and properties for the 'bestFileContentDat' attribute
    def getBestFileContentDat(self): return self._bestFileContentDat
    def setBestFileContentDat(self, bestFileContentDat):
        if bestFileContentDat is None:
            self._bestFileContentDat = None
        elif bestFileContentDat.__class__.__name__ == "XSDataString":
            self._bestFileContentDat = bestFileContentDat
        else:
            strMessage = "ERROR! XSDataInputBest.setBestFileContentDat argument is not XSDataString but %s" % bestFileContentDat.__class__.__name__
            raise BaseException(strMessage)
    def delBestFileContentDat(self): self._bestFileContentDat = None
    bestFileContentDat = property(getBestFileContentDat, setBestFileContentDat, delBestFileContentDat, "Property for bestFileContentDat")
    # Methods and properties for the 'bestFileContentHKL' attribute
    def getBestFileContentHKL(self): return self._bestFileContentHKL
    def setBestFileContentHKL(self, bestFileContentHKL):
        if bestFileContentHKL is None:
            self._bestFileContentHKL = []
        elif bestFileContentHKL.__class__.__name__ == "list":
            self._bestFileContentHKL = bestFileContentHKL
        else:
            strMessage = "ERROR! XSDataInputBest.setBestFileContentHKL argument is not list but %s" % bestFileContentHKL.__class__.__name__
            raise BaseException(strMessage)
    def delBestFileContentHKL(self): self._bestFileContentHKL = None
    bestFileContentHKL = property(getBestFileContentHKL, setBestFileContentHKL, delBestFileContentHKL, "Property for bestFileContentHKL")
    def addBestFileContentHKL(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBest.addBestFileContentHKL argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._bestFileContentHKL.append(value)
        else:
            strMessage = "ERROR! XSDataInputBest.addBestFileContentHKL argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBestFileContentHKL(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBest.insertBestFileContentHKL argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputBest.insertBestFileContentHKL argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._bestFileContentHKL[index] = value
        else:
            strMessage = "ERROR! XSDataInputBest.addBestFileContentHKL argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bestFileContentPar' attribute
    def getBestFileContentPar(self): return self._bestFileContentPar
    def setBestFileContentPar(self, bestFileContentPar):
        if bestFileContentPar is None:
            self._bestFileContentPar = None
        elif bestFileContentPar.__class__.__name__ == "XSDataString":
            self._bestFileContentPar = bestFileContentPar
        else:
            strMessage = "ERROR! XSDataInputBest.setBestFileContentPar argument is not XSDataString but %s" % bestFileContentPar.__class__.__name__
            raise BaseException(strMessage)
    def delBestFileContentPar(self): self._bestFileContentPar = None
    bestFileContentPar = property(getBestFileContentPar, setBestFileContentPar, delBestFileContentPar, "Property for bestFileContentPar")
    # Methods and properties for the 'complexity' attribute
    def getComplexity(self): return self._complexity
    def setComplexity(self, complexity):
        if complexity is None:
            self._complexity = None
        elif complexity.__class__.__name__ == "XSDataString":
            self._complexity = complexity
        else:
            strMessage = "ERROR! XSDataInputBest.setComplexity argument is not XSDataString but %s" % complexity.__class__.__name__
            raise BaseException(strMessage)
    def delComplexity(self): self._complexity = None
    complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
    # Methods and properties for the 'crystalAbsorbedDoseRate' attribute
    def getCrystalAbsorbedDoseRate(self): return self._crystalAbsorbedDoseRate
    def setCrystalAbsorbedDoseRate(self, crystalAbsorbedDoseRate):
        if crystalAbsorbedDoseRate is None:
            self._crystalAbsorbedDoseRate = None
        elif crystalAbsorbedDoseRate.__class__.__name__ == "XSDataAbsorbedDoseRate":
            self._crystalAbsorbedDoseRate = crystalAbsorbedDoseRate
        else:
            strMessage = "ERROR! XSDataInputBest.setCrystalAbsorbedDoseRate argument is not XSDataAbsorbedDoseRate but %s" % crystalAbsorbedDoseRate.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalAbsorbedDoseRate(self): self._crystalAbsorbedDoseRate = None
    crystalAbsorbedDoseRate = property(getCrystalAbsorbedDoseRate, setCrystalAbsorbedDoseRate, delCrystalAbsorbedDoseRate, "Property for crystalAbsorbedDoseRate")
    # Methods and properties for the 'crystalShape' attribute
    def getCrystalShape(self): return self._crystalShape
    def setCrystalShape(self, crystalShape):
        if crystalShape is None:
            self._crystalShape = None
        elif crystalShape.__class__.__name__ == "XSDataDouble":
            self._crystalShape = crystalShape
        else:
            strMessage = "ERROR! XSDataInputBest.setCrystalShape argument is not XSDataDouble but %s" % crystalShape.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalShape(self): self._crystalShape = None
    crystalShape = property(getCrystalShape, setCrystalShape, delCrystalShape, "Property for crystalShape")
    # Methods and properties for the 'crystalSusceptibility' attribute
    def getCrystalSusceptibility(self): return self._crystalSusceptibility
    def setCrystalSusceptibility(self, crystalSusceptibility):
        if crystalSusceptibility is None:
            self._crystalSusceptibility = None
        elif crystalSusceptibility.__class__.__name__ == "XSDataDouble":
            self._crystalSusceptibility = crystalSusceptibility
        else:
            strMessage = "ERROR! XSDataInputBest.setCrystalSusceptibility argument is not XSDataDouble but %s" % crystalSusceptibility.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalSusceptibility(self): self._crystalSusceptibility = None
    crystalSusceptibility = property(getCrystalSusceptibility, setCrystalSusceptibility, delCrystalSusceptibility, "Property for crystalSusceptibility")
    # Methods and properties for the 'detectorDistanceMax' attribute
    def getDetectorDistanceMax(self): return self._detectorDistanceMax
    def setDetectorDistanceMax(self, detectorDistanceMax):
        if detectorDistanceMax is None:
            self._detectorDistanceMax = None
        elif detectorDistanceMax.__class__.__name__ == "XSDataLength":
            self._detectorDistanceMax = detectorDistanceMax
        else:
            strMessage = "ERROR! XSDataInputBest.setDetectorDistanceMax argument is not XSDataLength but %s" % detectorDistanceMax.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistanceMax(self): self._detectorDistanceMax = None
    detectorDistanceMax = property(getDetectorDistanceMax, setDetectorDistanceMax, delDetectorDistanceMax, "Property for detectorDistanceMax")
    # Methods and properties for the 'detectorDistanceMin' attribute
    def getDetectorDistanceMin(self): return self._detectorDistanceMin
    def setDetectorDistanceMin(self, detectorDistanceMin):
        if detectorDistanceMin is None:
            self._detectorDistanceMin = None
        elif detectorDistanceMin.__class__.__name__ == "XSDataLength":
            self._detectorDistanceMin = detectorDistanceMin
        else:
            strMessage = "ERROR! XSDataInputBest.setDetectorDistanceMin argument is not XSDataLength but %s" % detectorDistanceMin.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistanceMin(self): self._detectorDistanceMin = None
    detectorDistanceMin = property(getDetectorDistanceMin, setDetectorDistanceMin, delDetectorDistanceMin, "Property for detectorDistanceMin")
    # Methods and properties for the 'detectorType' attribute
    def getDetectorType(self): return self._detectorType
    def setDetectorType(self, detectorType):
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputBest.setDetectorType argument is not XSDataString but %s" % detectorType.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorType(self): self._detectorType = None
    detectorType = property(getDetectorType, setDetectorType, delDetectorType, "Property for detectorType")
    # Methods and properties for the 'goniostatMaxRotationSpeed' attribute
    def getGoniostatMaxRotationSpeed(self): return self._goniostatMaxRotationSpeed
    def setGoniostatMaxRotationSpeed(self, goniostatMaxRotationSpeed):
        if goniostatMaxRotationSpeed is None:
            self._goniostatMaxRotationSpeed = None
        elif goniostatMaxRotationSpeed.__class__.__name__ == "XSDataAngularSpeed":
            self._goniostatMaxRotationSpeed = goniostatMaxRotationSpeed
        else:
            strMessage = "ERROR! XSDataInputBest.setGoniostatMaxRotationSpeed argument is not XSDataAngularSpeed but %s" % goniostatMaxRotationSpeed.__class__.__name__
            raise BaseException(strMessage)
    def delGoniostatMaxRotationSpeed(self): self._goniostatMaxRotationSpeed = None
    goniostatMaxRotationSpeed = property(getGoniostatMaxRotationSpeed, setGoniostatMaxRotationSpeed, delGoniostatMaxRotationSpeed, "Property for goniostatMaxRotationSpeed")
    # Methods and properties for the 'goniostatMinRotationWidth' attribute
    def getGoniostatMinRotationWidth(self): return self._goniostatMinRotationWidth
    def setGoniostatMinRotationWidth(self, goniostatMinRotationWidth):
        if goniostatMinRotationWidth is None:
            self._goniostatMinRotationWidth = None
        elif goniostatMinRotationWidth.__class__.__name__ == "XSDataAngle":
            self._goniostatMinRotationWidth = goniostatMinRotationWidth
        else:
            strMessage = "ERROR! XSDataInputBest.setGoniostatMinRotationWidth argument is not XSDataAngle but %s" % goniostatMinRotationWidth.__class__.__name__
            raise BaseException(strMessage)
    def delGoniostatMinRotationWidth(self): self._goniostatMinRotationWidth = None
    goniostatMinRotationWidth = property(getGoniostatMinRotationWidth, setGoniostatMinRotationWidth, delGoniostatMinRotationWidth, "Property for goniostatMinRotationWidth")
    # Methods and properties for the 'minTransmission' attribute
    def getMinTransmission(self): return self._minTransmission
    def setMinTransmission(self, minTransmission):
        if minTransmission is None:
            self._minTransmission = None
        elif minTransmission.__class__.__name__ == "XSDataDouble":
            self._minTransmission = minTransmission
        else:
            strMessage = "ERROR! XSDataInputBest.setMinTransmission argument is not XSDataDouble but %s" % minTransmission.__class__.__name__
            raise BaseException(strMessage)
    def delMinTransmission(self): self._minTransmission = None
    minTransmission = property(getMinTransmission, setMinTransmission, delMinTransmission, "Property for minTransmission")
    # Methods and properties for the 'numberOfCrystalPositions' attribute
    def getNumberOfCrystalPositions(self): return self._numberOfCrystalPositions
    def setNumberOfCrystalPositions(self, numberOfCrystalPositions):
        if numberOfCrystalPositions is None:
            self._numberOfCrystalPositions = None
        elif numberOfCrystalPositions.__class__.__name__ == "XSDataInteger":
            self._numberOfCrystalPositions = numberOfCrystalPositions
        else:
            strMessage = "ERROR! XSDataInputBest.setNumberOfCrystalPositions argument is not XSDataInteger but %s" % numberOfCrystalPositions.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfCrystalPositions(self): self._numberOfCrystalPositions = None
    numberOfCrystalPositions = property(getNumberOfCrystalPositions, setNumberOfCrystalPositions, delNumberOfCrystalPositions, "Property for numberOfCrystalPositions")
    # Methods and properties for the 'radiationDamageModelBeta' attribute
    def getRadiationDamageModelBeta(self): return self._radiationDamageModelBeta
    def setRadiationDamageModelBeta(self, radiationDamageModelBeta):
        if radiationDamageModelBeta is None:
            self._radiationDamageModelBeta = None
        elif radiationDamageModelBeta.__class__.__name__ == "XSDataDouble":
            self._radiationDamageModelBeta = radiationDamageModelBeta
        else:
            strMessage = "ERROR! XSDataInputBest.setRadiationDamageModelBeta argument is not XSDataDouble but %s" % radiationDamageModelBeta.__class__.__name__
            raise BaseException(strMessage)
    def delRadiationDamageModelBeta(self): self._radiationDamageModelBeta = None
    radiationDamageModelBeta = property(getRadiationDamageModelBeta, setRadiationDamageModelBeta, delRadiationDamageModelBeta, "Property for radiationDamageModelBeta")
    # Methods and properties for the 'radiationDamageModelGamma' attribute
    def getRadiationDamageModelGamma(self): return self._radiationDamageModelGamma
    def setRadiationDamageModelGamma(self, radiationDamageModelGamma):
        if radiationDamageModelGamma is None:
            self._radiationDamageModelGamma = None
        elif radiationDamageModelGamma.__class__.__name__ == "XSDataDouble":
            self._radiationDamageModelGamma = radiationDamageModelGamma
        else:
            strMessage = "ERROR! XSDataInputBest.setRadiationDamageModelGamma argument is not XSDataDouble but %s" % radiationDamageModelGamma.__class__.__name__
            raise BaseException(strMessage)
    def delRadiationDamageModelGamma(self): self._radiationDamageModelGamma = None
    radiationDamageModelGamma = property(getRadiationDamageModelGamma, setRadiationDamageModelGamma, delRadiationDamageModelGamma, "Property for radiationDamageModelGamma")
    # Methods and properties for the 'strategyOption' attribute
    def getStrategyOption(self): return self._strategyOption
    def setStrategyOption(self, strategyOption):
        if strategyOption is None:
            self._strategyOption = None
        elif strategyOption.__class__.__name__ == "XSDataString":
            self._strategyOption = strategyOption
        else:
            strMessage = "ERROR! XSDataInputBest.setStrategyOption argument is not XSDataString but %s" % strategyOption.__class__.__name__
            raise BaseException(strMessage)
    def delStrategyOption(self): self._strategyOption = None
    strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataInputBest.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'userDefinedRotationRange' attribute
    def getUserDefinedRotationRange(self): return self._userDefinedRotationRange
    def setUserDefinedRotationRange(self, userDefinedRotationRange):
        if userDefinedRotationRange is None:
            self._userDefinedRotationRange = None
        elif userDefinedRotationRange.__class__.__name__ == "XSDataAngle":
            self._userDefinedRotationRange = userDefinedRotationRange
        else:
            strMessage = "ERROR! XSDataInputBest.setUserDefinedRotationRange argument is not XSDataAngle but %s" % userDefinedRotationRange.__class__.__name__
            raise BaseException(strMessage)
    def delUserDefinedRotationRange(self): self._userDefinedRotationRange = None
    userDefinedRotationRange = property(getUserDefinedRotationRange, setUserDefinedRotationRange, delUserDefinedRotationRange, "Property for userDefinedRotationRange")
    # Methods and properties for the 'userDefinedRotationStart' attribute
    def getUserDefinedRotationStart(self): return self._userDefinedRotationStart
    def setUserDefinedRotationStart(self, userDefinedRotationStart):
        if userDefinedRotationStart is None:
            self._userDefinedRotationStart = None
        elif userDefinedRotationStart.__class__.__name__ == "XSDataAngle":
            self._userDefinedRotationStart = userDefinedRotationStart
        else:
            strMessage = "ERROR! XSDataInputBest.setUserDefinedRotationStart argument is not XSDataAngle but %s" % userDefinedRotationStart.__class__.__name__
            raise BaseException(strMessage)
    def delUserDefinedRotationStart(self): self._userDefinedRotationStart = None
    userDefinedRotationStart = property(getUserDefinedRotationStart, setUserDefinedRotationStart, delUserDefinedRotationStart, "Property for userDefinedRotationStart")
    # Methods and properties for the 'xdsBackgroundImage' attribute
    def getXdsBackgroundImage(self): return self._xdsBackgroundImage
    def setXdsBackgroundImage(self, xdsBackgroundImage):
        if xdsBackgroundImage is None:
            self._xdsBackgroundImage = None
        elif xdsBackgroundImage.__class__.__name__ == "XSDataFile":
            self._xdsBackgroundImage = xdsBackgroundImage
        else:
            strMessage = "ERROR! XSDataInputBest.setXdsBackgroundImage argument is not XSDataFile but %s" % xdsBackgroundImage.__class__.__name__
            raise BaseException(strMessage)
    def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
    xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
    def export(self, outfile, level, name_='XSDataInputBest'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBest'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._aimedCompleteness is not None:
            self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
        if self._aimedIOverSigma is not None:
            self.aimedIOverSigma.export(outfile, level, name_='aimedIOverSigma')
        if self._aimedRedundancy is not None:
            self.aimedRedundancy.export(outfile, level, name_='aimedRedundancy')
        if self._aimedResolution is not None:
            self.aimedResolution.export(outfile, level, name_='aimedResolution')
        if self._anomalousData is not None:
            self.anomalousData.export(outfile, level, name_='anomalousData')
        if self._beamExposureTime is not None:
            self.beamExposureTime.export(outfile, level, name_='beamExposureTime')
        else:
            warnEmptyAttribute("beamExposureTime", "XSDataTime")
        if self._beamMaxExposureTime is not None:
            self.beamMaxExposureTime.export(outfile, level, name_='beamMaxExposureTime')
        if self._beamMinExposureTime is not None:
            self.beamMinExposureTime.export(outfile, level, name_='beamMinExposureTime')
        if self._bestFileContentDat is not None:
            self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
        else:
            warnEmptyAttribute("bestFileContentDat", "XSDataString")
        for bestFileContentHKL_ in self.getBestFileContentHKL():
            bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
        if self.getBestFileContentHKL() == []:
            warnEmptyAttribute("bestFileContentHKL", "XSDataString")
        if self._bestFileContentPar is not None:
            self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
        else:
            warnEmptyAttribute("bestFileContentPar", "XSDataString")
        if self._complexity is not None:
            self.complexity.export(outfile, level, name_='complexity')
        if self._crystalAbsorbedDoseRate is not None:
            self.crystalAbsorbedDoseRate.export(outfile, level, name_='crystalAbsorbedDoseRate')
        if self._crystalShape is not None:
            self.crystalShape.export(outfile, level, name_='crystalShape')
        if self._crystalSusceptibility is not None:
            self.crystalSusceptibility.export(outfile, level, name_='crystalSusceptibility')
        if self._detectorDistanceMax is not None:
            self.detectorDistanceMax.export(outfile, level, name_='detectorDistanceMax')
        if self._detectorDistanceMin is not None:
            self.detectorDistanceMin.export(outfile, level, name_='detectorDistanceMin')
        if self._detectorType is not None:
            self.detectorType.export(outfile, level, name_='detectorType')
        else:
            warnEmptyAttribute("detectorType", "XSDataString")
        if self._goniostatMaxRotationSpeed is not None:
            self.goniostatMaxRotationSpeed.export(outfile, level, name_='goniostatMaxRotationSpeed')
        if self._goniostatMinRotationWidth is not None:
            self.goniostatMinRotationWidth.export(outfile, level, name_='goniostatMinRotationWidth')
        if self._minTransmission is not None:
            self.minTransmission.export(outfile, level, name_='minTransmission')
        if self._numberOfCrystalPositions is not None:
            self.numberOfCrystalPositions.export(outfile, level, name_='numberOfCrystalPositions')
        if self._radiationDamageModelBeta is not None:
            self.radiationDamageModelBeta.export(outfile, level, name_='radiationDamageModelBeta')
        if self._radiationDamageModelGamma is not None:
            self.radiationDamageModelGamma.export(outfile, level, name_='radiationDamageModelGamma')
        if self._strategyOption is not None:
            self.strategyOption.export(outfile, level, name_='strategyOption')
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
        if self._userDefinedRotationRange is not None:
            self.userDefinedRotationRange.export(outfile, level, name_='userDefinedRotationRange')
        if self._userDefinedRotationStart is not None:
            self.userDefinedRotationStart.export(outfile, level, name_='userDefinedRotationStart')
        if self._xdsBackgroundImage is not None:
            self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedCompleteness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedIOverSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedRedundancy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedRedundancy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalousData':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnomalousData(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamExposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setBeamExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamMaxExposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setBeamMaxExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamMinExposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setBeamMinExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentDat':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestFileContentDat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentHKL':
            obj_ = XSDataString()
            obj_.build(child_)
            self.bestFileContentHKL.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentPar':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestFileContentPar(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'complexity':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComplexity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalAbsorbedDoseRate':
            obj_ = XSDataAbsorbedDoseRate()
            obj_.build(child_)
            self.setCrystalAbsorbedDoseRate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalShape':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCrystalShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalSusceptibility':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCrystalSusceptibility(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistanceMax':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistanceMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistanceMin':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistanceMin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorType':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetectorType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostatMaxRotationSpeed':
            obj_ = XSDataAngularSpeed()
            obj_.build(child_)
            self.setGoniostatMaxRotationSpeed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostatMinRotationWidth':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setGoniostatMinRotationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minTransmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMinTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfCrystalPositions':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfCrystalPositions(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiationDamageModelBeta':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiationDamageModelBeta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiationDamageModelGamma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiationDamageModelGamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategyOption':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setStrategyOption(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'userDefinedRotationRange':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setUserDefinedRotationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'userDefinedRotationStart':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setUserDefinedRotationStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xdsBackgroundImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXdsBackgroundImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBest" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBest' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBest is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBest.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBest()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBest" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBest()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBest


class XSDataResultBest(XSDataResult):
    def __init__(self, status=None, pathToPlotMtvFile=None, pathToLogFile=None, glePlot=None, collectionPlan=None):
        XSDataResult.__init__(self, status)
        if collectionPlan is None:
            self._collectionPlan = []
        elif collectionPlan.__class__.__name__ == "list":
            self._collectionPlan = collectionPlan
        else:
            strMessage = "ERROR! XSDataResultBest constructor argument 'collectionPlan' is not list but %s" % self._collectionPlan.__class__.__name__
            raise BaseException(strMessage)
        if glePlot is None:
            self._glePlot = []
        elif glePlot.__class__.__name__ == "list":
            self._glePlot = glePlot
        else:
            strMessage = "ERROR! XSDataResultBest constructor argument 'glePlot' is not list but %s" % self._glePlot.__class__.__name__
            raise BaseException(strMessage)
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataResultBest constructor argument 'pathToLogFile' is not XSDataFile but %s" % self._pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
        if pathToPlotMtvFile is None:
            self._pathToPlotMtvFile = None
        elif pathToPlotMtvFile.__class__.__name__ == "XSDataFile":
            self._pathToPlotMtvFile = pathToPlotMtvFile
        else:
            strMessage = "ERROR! XSDataResultBest constructor argument 'pathToPlotMtvFile' is not XSDataFile but %s" % self._pathToPlotMtvFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'collectionPlan' attribute
    def getCollectionPlan(self): return self._collectionPlan
    def setCollectionPlan(self, collectionPlan):
        if collectionPlan is None:
            self._collectionPlan = []
        elif collectionPlan.__class__.__name__ == "list":
            self._collectionPlan = collectionPlan
        else:
            strMessage = "ERROR! XSDataResultBest.setCollectionPlan argument is not list but %s" % collectionPlan.__class__.__name__
            raise BaseException(strMessage)
    def delCollectionPlan(self): self._collectionPlan = None
    collectionPlan = property(getCollectionPlan, setCollectionPlan, delCollectionPlan, "Property for collectionPlan")
    def addCollectionPlan(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultBest.addCollectionPlan argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestCollectionPlan":
            self._collectionPlan.append(value)
        else:
            strMessage = "ERROR! XSDataResultBest.addCollectionPlan argument is not XSDataBestCollectionPlan but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCollectionPlan(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultBest.insertCollectionPlan argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultBest.insertCollectionPlan argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestCollectionPlan":
            self._collectionPlan[index] = value
        else:
            strMessage = "ERROR! XSDataResultBest.addCollectionPlan argument is not XSDataBestCollectionPlan but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'glePlot' attribute
    def getGlePlot(self): return self._glePlot
    def setGlePlot(self, glePlot):
        if glePlot is None:
            self._glePlot = []
        elif glePlot.__class__.__name__ == "list":
            self._glePlot = glePlot
        else:
            strMessage = "ERROR! XSDataResultBest.setGlePlot argument is not list but %s" % glePlot.__class__.__name__
            raise BaseException(strMessage)
    def delGlePlot(self): self._glePlot = None
    glePlot = property(getGlePlot, setGlePlot, delGlePlot, "Property for glePlot")
    def addGlePlot(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultBest.addGlePlot argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestGlePlot":
            self._glePlot.append(value)
        else:
            strMessage = "ERROR! XSDataResultBest.addGlePlot argument is not XSDataBestGlePlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertGlePlot(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultBest.insertGlePlot argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultBest.insertGlePlot argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataBestGlePlot":
            self._glePlot[index] = value
        else:
            strMessage = "ERROR! XSDataResultBest.addGlePlot argument is not XSDataBestGlePlot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pathToLogFile' attribute
    def getPathToLogFile(self): return self._pathToLogFile
    def setPathToLogFile(self, pathToLogFile):
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataResultBest.setPathToLogFile argument is not XSDataFile but %s" % pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToLogFile(self): self._pathToLogFile = None
    pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
    # Methods and properties for the 'pathToPlotMtvFile' attribute
    def getPathToPlotMtvFile(self): return self._pathToPlotMtvFile
    def setPathToPlotMtvFile(self, pathToPlotMtvFile):
        if pathToPlotMtvFile is None:
            self._pathToPlotMtvFile = None
        elif pathToPlotMtvFile.__class__.__name__ == "XSDataFile":
            self._pathToPlotMtvFile = pathToPlotMtvFile
        else:
            strMessage = "ERROR! XSDataResultBest.setPathToPlotMtvFile argument is not XSDataFile but %s" % pathToPlotMtvFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToPlotMtvFile(self): self._pathToPlotMtvFile = None
    pathToPlotMtvFile = property(getPathToPlotMtvFile, setPathToPlotMtvFile, delPathToPlotMtvFile, "Property for pathToPlotMtvFile")
    def export(self, outfile, level, name_='XSDataResultBest'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBest'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for collectionPlan_ in self.getCollectionPlan():
            collectionPlan_.export(outfile, level, name_='collectionPlan')
        for glePlot_ in self.getGlePlot():
            glePlot_.export(outfile, level, name_='glePlot')
        if self._pathToLogFile is not None:
            self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
        else:
            warnEmptyAttribute("pathToLogFile", "XSDataFile")
        if self._pathToPlotMtvFile is not None:
            self.pathToPlotMtvFile.export(outfile, level, name_='pathToPlotMtvFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionPlan':
            obj_ = XSDataBestCollectionPlan()
            obj_.build(child_)
            self.collectionPlan.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'glePlot':
            obj_ = XSDataBestGlePlot()
            obj_.build(child_)
            self.glePlot.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToLogFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToPlotMtvFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToPlotMtvFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBest" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBest' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBest is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBest.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBest()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBest" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBest()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBest



# End of data representation classes.



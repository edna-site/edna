#!/usr/bin/env python

#
# Generated Fri Feb 15 02:32::29 2013 by EDGenerateDS.
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
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataMatrixDouble
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
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
from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
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



class XSDataCell(object):
    def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_alpha' is not XSDataAngle but %s" % self._angle_alpha.__class__.__name__
            raise BaseException(strMessage)
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_beta' is not XSDataAngle but %s" % self._angle_beta.__class__.__name__
            raise BaseException(strMessage)
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_gamma' is not XSDataAngle but %s" % self._angle_gamma.__class__.__name__
            raise BaseException(strMessage)
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_a' is not XSDataLength but %s" % self._length_a.__class__.__name__
            raise BaseException(strMessage)
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_b' is not XSDataLength but %s" % self._length_b.__class__.__name__
            raise BaseException(strMessage)
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_c' is not XSDataLength but %s" % self._length_c.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angle_alpha' attribute
    def getAngle_alpha(self): return self._angle_alpha
    def setAngle_alpha(self, angle_alpha):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell.setAngle_alpha argument is not XSDataAngle but %s" % angle_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_alpha(self): self._angle_alpha = None
    angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
    # Methods and properties for the 'angle_beta' attribute
    def getAngle_beta(self): return self._angle_beta
    def setAngle_beta(self, angle_beta):
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataCell.setAngle_beta argument is not XSDataAngle but %s" % angle_beta.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_beta(self): self._angle_beta = None
    angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
    # Methods and properties for the 'angle_gamma' attribute
    def getAngle_gamma(self): return self._angle_gamma
    def setAngle_gamma(self, angle_gamma):
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataCell.setAngle_gamma argument is not XSDataAngle but %s" % angle_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_gamma(self): self._angle_gamma = None
    angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
    # Methods and properties for the 'length_a' attribute
    def getLength_a(self): return self._length_a
    def setLength_a(self, length_a):
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataCell.setLength_a argument is not XSDataLength but %s" % length_a.__class__.__name__
            raise BaseException(strMessage)
    def delLength_a(self): self._length_a = None
    length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
    # Methods and properties for the 'length_b' attribute
    def getLength_b(self): return self._length_b
    def setLength_b(self, length_b):
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataCell.setLength_b argument is not XSDataLength but %s" % length_b.__class__.__name__
            raise BaseException(strMessage)
    def delLength_b(self): self._length_b = None
    length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
    # Methods and properties for the 'length_c' attribute
    def getLength_c(self): return self._length_c
    def setLength_c(self, length_c):
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataCell.setLength_c argument is not XSDataLength but %s" % length_c.__class__.__name__
            raise BaseException(strMessage)
    def delLength_c(self): self._length_c = None
    length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
    def export(self, outfile, level, name_='XSDataCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataCell'):
        pass
        if self._angle_alpha is not None:
            self.angle_alpha.export(outfile, level, name_='angle_alpha')
        else:
            warnEmptyAttribute("angle_alpha", "XSDataAngle")
        if self._angle_beta is not None:
            self.angle_beta.export(outfile, level, name_='angle_beta')
        else:
            warnEmptyAttribute("angle_beta", "XSDataAngle")
        if self._angle_gamma is not None:
            self.angle_gamma.export(outfile, level, name_='angle_gamma')
        else:
            warnEmptyAttribute("angle_gamma", "XSDataAngle")
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
            nodeName_ == 'angle_gamma':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_gamma(obj_)
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
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataCell


class XSDataImageQualityIndicators(XSData):
    def __init__(self, totalIntegratedSignal=None, spotTotal=None, signalRangeMin=None, signalRangeMax=None, signalRangeAverage=None, saturationRangeMin=None, saturationRangeMax=None, saturationRangeAverage=None, pctSaturationTop50Peaks=None, method2Res=None, method1Res=None, maxUnitCell=None, inResolutionOvrlSpots=None, inResTotal=None, image=None, iceRings=None, goodBraggCandidates=None, binPopCutOffMethod2Res=None):
        XSData.__init__(self, )
        if binPopCutOffMethod2Res is None:
            self._binPopCutOffMethod2Res = None
        elif binPopCutOffMethod2Res.__class__.__name__ == "XSDataDouble":
            self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'binPopCutOffMethod2Res' is not XSDataDouble but %s" % self._binPopCutOffMethod2Res.__class__.__name__
            raise BaseException(strMessage)
        if goodBraggCandidates is None:
            self._goodBraggCandidates = None
        elif goodBraggCandidates.__class__.__name__ == "XSDataInteger":
            self._goodBraggCandidates = goodBraggCandidates
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'goodBraggCandidates' is not XSDataInteger but %s" % self._goodBraggCandidates.__class__.__name__
            raise BaseException(strMessage)
        if iceRings is None:
            self._iceRings = None
        elif iceRings.__class__.__name__ == "XSDataInteger":
            self._iceRings = iceRings
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'iceRings' is not XSDataInteger but %s" % self._iceRings.__class__.__name__
            raise BaseException(strMessage)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'image' is not XSDataImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if inResTotal is None:
            self._inResTotal = None
        elif inResTotal.__class__.__name__ == "XSDataInteger":
            self._inResTotal = inResTotal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'inResTotal' is not XSDataInteger but %s" % self._inResTotal.__class__.__name__
            raise BaseException(strMessage)
        if inResolutionOvrlSpots is None:
            self._inResolutionOvrlSpots = None
        elif inResolutionOvrlSpots.__class__.__name__ == "XSDataInteger":
            self._inResolutionOvrlSpots = inResolutionOvrlSpots
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'inResolutionOvrlSpots' is not XSDataInteger but %s" % self._inResolutionOvrlSpots.__class__.__name__
            raise BaseException(strMessage)
        if maxUnitCell is None:
            self._maxUnitCell = None
        elif maxUnitCell.__class__.__name__ == "XSDataDouble":
            self._maxUnitCell = maxUnitCell
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'maxUnitCell' is not XSDataDouble but %s" % self._maxUnitCell.__class__.__name__
            raise BaseException(strMessage)
        if method1Res is None:
            self._method1Res = None
        elif method1Res.__class__.__name__ == "XSDataDouble":
            self._method1Res = method1Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'method1Res' is not XSDataDouble but %s" % self._method1Res.__class__.__name__
            raise BaseException(strMessage)
        if method2Res is None:
            self._method2Res = None
        elif method2Res.__class__.__name__ == "XSDataDouble":
            self._method2Res = method2Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'method2Res' is not XSDataDouble but %s" % self._method2Res.__class__.__name__
            raise BaseException(strMessage)
        if pctSaturationTop50Peaks is None:
            self._pctSaturationTop50Peaks = None
        elif pctSaturationTop50Peaks.__class__.__name__ == "XSDataDouble":
            self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'pctSaturationTop50Peaks' is not XSDataDouble but %s" % self._pctSaturationTop50Peaks.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeAverage is None:
            self._saturationRangeAverage = None
        elif saturationRangeAverage.__class__.__name__ == "XSDataDouble":
            self._saturationRangeAverage = saturationRangeAverage
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'saturationRangeAverage' is not XSDataDouble but %s" % self._saturationRangeAverage.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeMax is None:
            self._saturationRangeMax = None
        elif saturationRangeMax.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMax = saturationRangeMax
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'saturationRangeMax' is not XSDataDouble but %s" % self._saturationRangeMax.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeMin is None:
            self._saturationRangeMin = None
        elif saturationRangeMin.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMin = saturationRangeMin
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'saturationRangeMin' is not XSDataDouble but %s" % self._saturationRangeMin.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeAverage is None:
            self._signalRangeAverage = None
        elif signalRangeAverage.__class__.__name__ == "XSDataDouble":
            self._signalRangeAverage = signalRangeAverage
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'signalRangeAverage' is not XSDataDouble but %s" % self._signalRangeAverage.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeMax is None:
            self._signalRangeMax = None
        elif signalRangeMax.__class__.__name__ == "XSDataDouble":
            self._signalRangeMax = signalRangeMax
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'signalRangeMax' is not XSDataDouble but %s" % self._signalRangeMax.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeMin is None:
            self._signalRangeMin = None
        elif signalRangeMin.__class__.__name__ == "XSDataDouble":
            self._signalRangeMin = signalRangeMin
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'signalRangeMin' is not XSDataDouble but %s" % self._signalRangeMin.__class__.__name__
            raise BaseException(strMessage)
        if spotTotal is None:
            self._spotTotal = None
        elif spotTotal.__class__.__name__ == "XSDataInteger":
            self._spotTotal = spotTotal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'spotTotal' is not XSDataInteger but %s" % self._spotTotal.__class__.__name__
            raise BaseException(strMessage)
        if totalIntegratedSignal is None:
            self._totalIntegratedSignal = None
        elif totalIntegratedSignal.__class__.__name__ == "XSDataDouble":
            self._totalIntegratedSignal = totalIntegratedSignal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators constructor argument 'totalIntegratedSignal' is not XSDataDouble but %s" % self._totalIntegratedSignal.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'binPopCutOffMethod2Res' attribute
    def getBinPopCutOffMethod2Res(self): return self._binPopCutOffMethod2Res
    def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res):
        if binPopCutOffMethod2Res is None:
            self._binPopCutOffMethod2Res = None
        elif binPopCutOffMethod2Res.__class__.__name__ == "XSDataDouble":
            self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setBinPopCutOffMethod2Res argument is not XSDataDouble but %s" % binPopCutOffMethod2Res.__class__.__name__
            raise BaseException(strMessage)
    def delBinPopCutOffMethod2Res(self): self._binPopCutOffMethod2Res = None
    binPopCutOffMethod2Res = property(getBinPopCutOffMethod2Res, setBinPopCutOffMethod2Res, delBinPopCutOffMethod2Res, "Property for binPopCutOffMethod2Res")
    # Methods and properties for the 'goodBraggCandidates' attribute
    def getGoodBraggCandidates(self): return self._goodBraggCandidates
    def setGoodBraggCandidates(self, goodBraggCandidates):
        if goodBraggCandidates is None:
            self._goodBraggCandidates = None
        elif goodBraggCandidates.__class__.__name__ == "XSDataInteger":
            self._goodBraggCandidates = goodBraggCandidates
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setGoodBraggCandidates argument is not XSDataInteger but %s" % goodBraggCandidates.__class__.__name__
            raise BaseException(strMessage)
    def delGoodBraggCandidates(self): self._goodBraggCandidates = None
    goodBraggCandidates = property(getGoodBraggCandidates, setGoodBraggCandidates, delGoodBraggCandidates, "Property for goodBraggCandidates")
    # Methods and properties for the 'iceRings' attribute
    def getIceRings(self): return self._iceRings
    def setIceRings(self, iceRings):
        if iceRings is None:
            self._iceRings = None
        elif iceRings.__class__.__name__ == "XSDataInteger":
            self._iceRings = iceRings
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setIceRings argument is not XSDataInteger but %s" % iceRings.__class__.__name__
            raise BaseException(strMessage)
    def delIceRings(self): self._iceRings = None
    iceRings = property(getIceRings, setIceRings, delIceRings, "Property for iceRings")
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setImage argument is not XSDataImage but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'inResTotal' attribute
    def getInResTotal(self): return self._inResTotal
    def setInResTotal(self, inResTotal):
        if inResTotal is None:
            self._inResTotal = None
        elif inResTotal.__class__.__name__ == "XSDataInteger":
            self._inResTotal = inResTotal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setInResTotal argument is not XSDataInteger but %s" % inResTotal.__class__.__name__
            raise BaseException(strMessage)
    def delInResTotal(self): self._inResTotal = None
    inResTotal = property(getInResTotal, setInResTotal, delInResTotal, "Property for inResTotal")
    # Methods and properties for the 'inResolutionOvrlSpots' attribute
    def getInResolutionOvrlSpots(self): return self._inResolutionOvrlSpots
    def setInResolutionOvrlSpots(self, inResolutionOvrlSpots):
        if inResolutionOvrlSpots is None:
            self._inResolutionOvrlSpots = None
        elif inResolutionOvrlSpots.__class__.__name__ == "XSDataInteger":
            self._inResolutionOvrlSpots = inResolutionOvrlSpots
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setInResolutionOvrlSpots argument is not XSDataInteger but %s" % inResolutionOvrlSpots.__class__.__name__
            raise BaseException(strMessage)
    def delInResolutionOvrlSpots(self): self._inResolutionOvrlSpots = None
    inResolutionOvrlSpots = property(getInResolutionOvrlSpots, setInResolutionOvrlSpots, delInResolutionOvrlSpots, "Property for inResolutionOvrlSpots")
    # Methods and properties for the 'maxUnitCell' attribute
    def getMaxUnitCell(self): return self._maxUnitCell
    def setMaxUnitCell(self, maxUnitCell):
        if maxUnitCell is None:
            self._maxUnitCell = None
        elif maxUnitCell.__class__.__name__ == "XSDataDouble":
            self._maxUnitCell = maxUnitCell
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setMaxUnitCell argument is not XSDataDouble but %s" % maxUnitCell.__class__.__name__
            raise BaseException(strMessage)
    def delMaxUnitCell(self): self._maxUnitCell = None
    maxUnitCell = property(getMaxUnitCell, setMaxUnitCell, delMaxUnitCell, "Property for maxUnitCell")
    # Methods and properties for the 'method1Res' attribute
    def getMethod1Res(self): return self._method1Res
    def setMethod1Res(self, method1Res):
        if method1Res is None:
            self._method1Res = None
        elif method1Res.__class__.__name__ == "XSDataDouble":
            self._method1Res = method1Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setMethod1Res argument is not XSDataDouble but %s" % method1Res.__class__.__name__
            raise BaseException(strMessage)
    def delMethod1Res(self): self._method1Res = None
    method1Res = property(getMethod1Res, setMethod1Res, delMethod1Res, "Property for method1Res")
    # Methods and properties for the 'method2Res' attribute
    def getMethod2Res(self): return self._method2Res
    def setMethod2Res(self, method2Res):
        if method2Res is None:
            self._method2Res = None
        elif method2Res.__class__.__name__ == "XSDataDouble":
            self._method2Res = method2Res
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setMethod2Res argument is not XSDataDouble but %s" % method2Res.__class__.__name__
            raise BaseException(strMessage)
    def delMethod2Res(self): self._method2Res = None
    method2Res = property(getMethod2Res, setMethod2Res, delMethod2Res, "Property for method2Res")
    # Methods and properties for the 'pctSaturationTop50Peaks' attribute
    def getPctSaturationTop50Peaks(self): return self._pctSaturationTop50Peaks
    def setPctSaturationTop50Peaks(self, pctSaturationTop50Peaks):
        if pctSaturationTop50Peaks is None:
            self._pctSaturationTop50Peaks = None
        elif pctSaturationTop50Peaks.__class__.__name__ == "XSDataDouble":
            self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setPctSaturationTop50Peaks argument is not XSDataDouble but %s" % pctSaturationTop50Peaks.__class__.__name__
            raise BaseException(strMessage)
    def delPctSaturationTop50Peaks(self): self._pctSaturationTop50Peaks = None
    pctSaturationTop50Peaks = property(getPctSaturationTop50Peaks, setPctSaturationTop50Peaks, delPctSaturationTop50Peaks, "Property for pctSaturationTop50Peaks")
    # Methods and properties for the 'saturationRangeAverage' attribute
    def getSaturationRangeAverage(self): return self._saturationRangeAverage
    def setSaturationRangeAverage(self, saturationRangeAverage):
        if saturationRangeAverage is None:
            self._saturationRangeAverage = None
        elif saturationRangeAverage.__class__.__name__ == "XSDataDouble":
            self._saturationRangeAverage = saturationRangeAverage
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSaturationRangeAverage argument is not XSDataDouble but %s" % saturationRangeAverage.__class__.__name__
            raise BaseException(strMessage)
    def delSaturationRangeAverage(self): self._saturationRangeAverage = None
    saturationRangeAverage = property(getSaturationRangeAverage, setSaturationRangeAverage, delSaturationRangeAverage, "Property for saturationRangeAverage")
    # Methods and properties for the 'saturationRangeMax' attribute
    def getSaturationRangeMax(self): return self._saturationRangeMax
    def setSaturationRangeMax(self, saturationRangeMax):
        if saturationRangeMax is None:
            self._saturationRangeMax = None
        elif saturationRangeMax.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMax = saturationRangeMax
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSaturationRangeMax argument is not XSDataDouble but %s" % saturationRangeMax.__class__.__name__
            raise BaseException(strMessage)
    def delSaturationRangeMax(self): self._saturationRangeMax = None
    saturationRangeMax = property(getSaturationRangeMax, setSaturationRangeMax, delSaturationRangeMax, "Property for saturationRangeMax")
    # Methods and properties for the 'saturationRangeMin' attribute
    def getSaturationRangeMin(self): return self._saturationRangeMin
    def setSaturationRangeMin(self, saturationRangeMin):
        if saturationRangeMin is None:
            self._saturationRangeMin = None
        elif saturationRangeMin.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMin = saturationRangeMin
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSaturationRangeMin argument is not XSDataDouble but %s" % saturationRangeMin.__class__.__name__
            raise BaseException(strMessage)
    def delSaturationRangeMin(self): self._saturationRangeMin = None
    saturationRangeMin = property(getSaturationRangeMin, setSaturationRangeMin, delSaturationRangeMin, "Property for saturationRangeMin")
    # Methods and properties for the 'signalRangeAverage' attribute
    def getSignalRangeAverage(self): return self._signalRangeAverage
    def setSignalRangeAverage(self, signalRangeAverage):
        if signalRangeAverage is None:
            self._signalRangeAverage = None
        elif signalRangeAverage.__class__.__name__ == "XSDataDouble":
            self._signalRangeAverage = signalRangeAverage
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSignalRangeAverage argument is not XSDataDouble but %s" % signalRangeAverage.__class__.__name__
            raise BaseException(strMessage)
    def delSignalRangeAverage(self): self._signalRangeAverage = None
    signalRangeAverage = property(getSignalRangeAverage, setSignalRangeAverage, delSignalRangeAverage, "Property for signalRangeAverage")
    # Methods and properties for the 'signalRangeMax' attribute
    def getSignalRangeMax(self): return self._signalRangeMax
    def setSignalRangeMax(self, signalRangeMax):
        if signalRangeMax is None:
            self._signalRangeMax = None
        elif signalRangeMax.__class__.__name__ == "XSDataDouble":
            self._signalRangeMax = signalRangeMax
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSignalRangeMax argument is not XSDataDouble but %s" % signalRangeMax.__class__.__name__
            raise BaseException(strMessage)
    def delSignalRangeMax(self): self._signalRangeMax = None
    signalRangeMax = property(getSignalRangeMax, setSignalRangeMax, delSignalRangeMax, "Property for signalRangeMax")
    # Methods and properties for the 'signalRangeMin' attribute
    def getSignalRangeMin(self): return self._signalRangeMin
    def setSignalRangeMin(self, signalRangeMin):
        if signalRangeMin is None:
            self._signalRangeMin = None
        elif signalRangeMin.__class__.__name__ == "XSDataDouble":
            self._signalRangeMin = signalRangeMin
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSignalRangeMin argument is not XSDataDouble but %s" % signalRangeMin.__class__.__name__
            raise BaseException(strMessage)
    def delSignalRangeMin(self): self._signalRangeMin = None
    signalRangeMin = property(getSignalRangeMin, setSignalRangeMin, delSignalRangeMin, "Property for signalRangeMin")
    # Methods and properties for the 'spotTotal' attribute
    def getSpotTotal(self): return self._spotTotal
    def setSpotTotal(self, spotTotal):
        if spotTotal is None:
            self._spotTotal = None
        elif spotTotal.__class__.__name__ == "XSDataInteger":
            self._spotTotal = spotTotal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setSpotTotal argument is not XSDataInteger but %s" % spotTotal.__class__.__name__
            raise BaseException(strMessage)
    def delSpotTotal(self): self._spotTotal = None
    spotTotal = property(getSpotTotal, setSpotTotal, delSpotTotal, "Property for spotTotal")
    # Methods and properties for the 'totalIntegratedSignal' attribute
    def getTotalIntegratedSignal(self): return self._totalIntegratedSignal
    def setTotalIntegratedSignal(self, totalIntegratedSignal):
        if totalIntegratedSignal is None:
            self._totalIntegratedSignal = None
        elif totalIntegratedSignal.__class__.__name__ == "XSDataDouble":
            self._totalIntegratedSignal = totalIntegratedSignal
        else:
            strMessage = "ERROR! XSDataImageQualityIndicators.setTotalIntegratedSignal argument is not XSDataDouble but %s" % totalIntegratedSignal.__class__.__name__
            raise BaseException(strMessage)
    def delTotalIntegratedSignal(self): self._totalIntegratedSignal = None
    totalIntegratedSignal = property(getTotalIntegratedSignal, setTotalIntegratedSignal, delTotalIntegratedSignal, "Property for totalIntegratedSignal")
    def export(self, outfile, level, name_='XSDataImageQualityIndicators'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataImageQualityIndicators'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._binPopCutOffMethod2Res is not None:
            self.binPopCutOffMethod2Res.export(outfile, level, name_='binPopCutOffMethod2Res')
        else:
            warnEmptyAttribute("binPopCutOffMethod2Res", "XSDataDouble")
        if self._goodBraggCandidates is not None:
            self.goodBraggCandidates.export(outfile, level, name_='goodBraggCandidates')
        else:
            warnEmptyAttribute("goodBraggCandidates", "XSDataInteger")
        if self._iceRings is not None:
            self.iceRings.export(outfile, level, name_='iceRings')
        else:
            warnEmptyAttribute("iceRings", "XSDataInteger")
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataImage")
        if self._inResTotal is not None:
            self.inResTotal.export(outfile, level, name_='inResTotal')
        else:
            warnEmptyAttribute("inResTotal", "XSDataInteger")
        if self._inResolutionOvrlSpots is not None:
            self.inResolutionOvrlSpots.export(outfile, level, name_='inResolutionOvrlSpots')
        else:
            warnEmptyAttribute("inResolutionOvrlSpots", "XSDataInteger")
        if self._maxUnitCell is not None:
            self.maxUnitCell.export(outfile, level, name_='maxUnitCell')
        if self._method1Res is not None:
            self.method1Res.export(outfile, level, name_='method1Res')
        else:
            warnEmptyAttribute("method1Res", "XSDataDouble")
        if self._method2Res is not None:
            self.method2Res.export(outfile, level, name_='method2Res')
        if self._pctSaturationTop50Peaks is not None:
            self.pctSaturationTop50Peaks.export(outfile, level, name_='pctSaturationTop50Peaks')
        if self._saturationRangeAverage is not None:
            self.saturationRangeAverage.export(outfile, level, name_='saturationRangeAverage')
        if self._saturationRangeMax is not None:
            self.saturationRangeMax.export(outfile, level, name_='saturationRangeMax')
        if self._saturationRangeMin is not None:
            self.saturationRangeMin.export(outfile, level, name_='saturationRangeMin')
        if self._signalRangeAverage is not None:
            self.signalRangeAverage.export(outfile, level, name_='signalRangeAverage')
        if self._signalRangeMax is not None:
            self.signalRangeMax.export(outfile, level, name_='signalRangeMax')
        if self._signalRangeMin is not None:
            self.signalRangeMin.export(outfile, level, name_='signalRangeMin')
        if self._spotTotal is not None:
            self.spotTotal.export(outfile, level, name_='spotTotal')
        else:
            warnEmptyAttribute("spotTotal", "XSDataInteger")
        if self._totalIntegratedSignal is not None:
            self.totalIntegratedSignal.export(outfile, level, name_='totalIntegratedSignal')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'binPopCutOffMethod2Res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBinPopCutOffMethod2Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goodBraggCandidates':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setGoodBraggCandidates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iceRings':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIceRings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inResTotal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setInResTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inResolutionOvrlSpots':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setInResolutionOvrlSpots(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxUnitCell':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'method1Res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMethod1Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'method2Res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMethod2Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pctSaturationTop50Peaks':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPctSaturationTop50Peaks(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'saturationRangeAverage':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSaturationRangeAverage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'saturationRangeMax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSaturationRangeMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'saturationRangeMin':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSaturationRangeMin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'signalRangeAverage':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSignalRangeAverage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'signalRangeMax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSignalRangeMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'signalRangeMin':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSignalRangeMin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotTotal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpotTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalIntegratedSignal':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotalIntegratedSignal(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataImageQualityIndicators" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataImageQualityIndicators' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataImageQualityIndicators is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataImageQualityIndicators.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImageQualityIndicators()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataImageQualityIndicators" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImageQualityIndicators()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataImageQualityIndicators


class XSDataLabelitMosflmScriptsOutput(XSData):
    def __init__(self, uMatrix=None, aMatrix=None):
        XSData.__init__(self, )
        if aMatrix is None:
            self._aMatrix = None
        elif aMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._aMatrix = aMatrix
        else:
            strMessage = "ERROR! XSDataLabelitMosflmScriptsOutput constructor argument 'aMatrix' is not XSDataMatrixDouble but %s" % self._aMatrix.__class__.__name__
            raise BaseException(strMessage)
        if uMatrix is None:
            self._uMatrix = None
        elif uMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._uMatrix = uMatrix
        else:
            strMessage = "ERROR! XSDataLabelitMosflmScriptsOutput constructor argument 'uMatrix' is not XSDataMatrixDouble but %s" % self._uMatrix.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'aMatrix' attribute
    def getAMatrix(self): return self._aMatrix
    def setAMatrix(self, aMatrix):
        if aMatrix is None:
            self._aMatrix = None
        elif aMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._aMatrix = aMatrix
        else:
            strMessage = "ERROR! XSDataLabelitMosflmScriptsOutput.setAMatrix argument is not XSDataMatrixDouble but %s" % aMatrix.__class__.__name__
            raise BaseException(strMessage)
    def delAMatrix(self): self._aMatrix = None
    aMatrix = property(getAMatrix, setAMatrix, delAMatrix, "Property for aMatrix")
    # Methods and properties for the 'uMatrix' attribute
    def getUMatrix(self): return self._uMatrix
    def setUMatrix(self, uMatrix):
        if uMatrix is None:
            self._uMatrix = None
        elif uMatrix.__class__.__name__ == "XSDataMatrixDouble":
            self._uMatrix = uMatrix
        else:
            strMessage = "ERROR! XSDataLabelitMosflmScriptsOutput.setUMatrix argument is not XSDataMatrixDouble but %s" % uMatrix.__class__.__name__
            raise BaseException(strMessage)
    def delUMatrix(self): self._uMatrix = None
    uMatrix = property(getUMatrix, setUMatrix, delUMatrix, "Property for uMatrix")
    def export(self, outfile, level, name_='XSDataLabelitMosflmScriptsOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataLabelitMosflmScriptsOutput'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._aMatrix is not None:
            self.aMatrix.export(outfile, level, name_='aMatrix')
        else:
            warnEmptyAttribute("aMatrix", "XSDataMatrixDouble")
        if self._uMatrix is not None:
            self.uMatrix.export(outfile, level, name_='uMatrix')
        else:
            warnEmptyAttribute("uMatrix", "XSDataMatrixDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aMatrix':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setAMatrix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'uMatrix':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setUMatrix(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataLabelitMosflmScriptsOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataLabelitMosflmScriptsOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataLabelitMosflmScriptsOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataLabelitMosflmScriptsOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitMosflmScriptsOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataLabelitMosflmScriptsOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitMosflmScriptsOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataLabelitMosflmScriptsOutput


class XSDataLabelitScreenSolution(XSData):
    def __init__(self, volume=None, unitCell=None, solutionNumber=None, rmsd=None, numberOfSpots=None, metricFitValue=None, metricFitCode=None, happy=None, crystalSystem=None, bravaisLattice=None):
        XSData.__init__(self, )
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'bravaisLattice' is not XSDataString but %s" % self._bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
        if crystalSystem is None:
            self._crystalSystem = None
        elif crystalSystem.__class__.__name__ == "XSDataString":
            self._crystalSystem = crystalSystem
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'crystalSystem' is not XSDataString but %s" % self._crystalSystem.__class__.__name__
            raise BaseException(strMessage)
        if happy is None:
            self._happy = None
        elif happy.__class__.__name__ == "XSDataBoolean":
            self._happy = happy
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'happy' is not XSDataBoolean but %s" % self._happy.__class__.__name__
            raise BaseException(strMessage)
        if metricFitCode is None:
            self._metricFitCode = None
        elif metricFitCode.__class__.__name__ == "XSDataString":
            self._metricFitCode = metricFitCode
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'metricFitCode' is not XSDataString but %s" % self._metricFitCode.__class__.__name__
            raise BaseException(strMessage)
        if metricFitValue is None:
            self._metricFitValue = None
        elif metricFitValue.__class__.__name__ == "XSDataDouble":
            self._metricFitValue = metricFitValue
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'metricFitValue' is not XSDataDouble but %s" % self._metricFitValue.__class__.__name__
            raise BaseException(strMessage)
        if numberOfSpots is None:
            self._numberOfSpots = None
        elif numberOfSpots.__class__.__name__ == "XSDataInteger":
            self._numberOfSpots = numberOfSpots
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'numberOfSpots' is not XSDataInteger but %s" % self._numberOfSpots.__class__.__name__
            raise BaseException(strMessage)
        if rmsd is None:
            self._rmsd = None
        elif rmsd.__class__.__name__ == "XSDataLength":
            self._rmsd = rmsd
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'rmsd' is not XSDataLength but %s" % self._rmsd.__class__.__name__
            raise BaseException(strMessage)
        if solutionNumber is None:
            self._solutionNumber = None
        elif solutionNumber.__class__.__name__ == "XSDataInteger":
            self._solutionNumber = solutionNumber
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'solutionNumber' is not XSDataInteger but %s" % self._solutionNumber.__class__.__name__
            raise BaseException(strMessage)
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataCell":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'unitCell' is not XSDataCell but %s" % self._unitCell.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataInteger":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution constructor argument 'volume' is not XSDataInteger but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'bravaisLattice' attribute
    def getBravaisLattice(self): return self._bravaisLattice
    def setBravaisLattice(self, bravaisLattice):
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setBravaisLattice argument is not XSDataString but %s" % bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
    def delBravaisLattice(self): self._bravaisLattice = None
    bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
    # Methods and properties for the 'crystalSystem' attribute
    def getCrystalSystem(self): return self._crystalSystem
    def setCrystalSystem(self, crystalSystem):
        if crystalSystem is None:
            self._crystalSystem = None
        elif crystalSystem.__class__.__name__ == "XSDataString":
            self._crystalSystem = crystalSystem
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setCrystalSystem argument is not XSDataString but %s" % crystalSystem.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalSystem(self): self._crystalSystem = None
    crystalSystem = property(getCrystalSystem, setCrystalSystem, delCrystalSystem, "Property for crystalSystem")
    # Methods and properties for the 'happy' attribute
    def getHappy(self): return self._happy
    def setHappy(self, happy):
        if happy is None:
            self._happy = None
        elif happy.__class__.__name__ == "XSDataBoolean":
            self._happy = happy
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setHappy argument is not XSDataBoolean but %s" % happy.__class__.__name__
            raise BaseException(strMessage)
    def delHappy(self): self._happy = None
    happy = property(getHappy, setHappy, delHappy, "Property for happy")
    # Methods and properties for the 'metricFitCode' attribute
    def getMetricFitCode(self): return self._metricFitCode
    def setMetricFitCode(self, metricFitCode):
        if metricFitCode is None:
            self._metricFitCode = None
        elif metricFitCode.__class__.__name__ == "XSDataString":
            self._metricFitCode = metricFitCode
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setMetricFitCode argument is not XSDataString but %s" % metricFitCode.__class__.__name__
            raise BaseException(strMessage)
    def delMetricFitCode(self): self._metricFitCode = None
    metricFitCode = property(getMetricFitCode, setMetricFitCode, delMetricFitCode, "Property for metricFitCode")
    # Methods and properties for the 'metricFitValue' attribute
    def getMetricFitValue(self): return self._metricFitValue
    def setMetricFitValue(self, metricFitValue):
        if metricFitValue is None:
            self._metricFitValue = None
        elif metricFitValue.__class__.__name__ == "XSDataDouble":
            self._metricFitValue = metricFitValue
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setMetricFitValue argument is not XSDataDouble but %s" % metricFitValue.__class__.__name__
            raise BaseException(strMessage)
    def delMetricFitValue(self): self._metricFitValue = None
    metricFitValue = property(getMetricFitValue, setMetricFitValue, delMetricFitValue, "Property for metricFitValue")
    # Methods and properties for the 'numberOfSpots' attribute
    def getNumberOfSpots(self): return self._numberOfSpots
    def setNumberOfSpots(self, numberOfSpots):
        if numberOfSpots is None:
            self._numberOfSpots = None
        elif numberOfSpots.__class__.__name__ == "XSDataInteger":
            self._numberOfSpots = numberOfSpots
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setNumberOfSpots argument is not XSDataInteger but %s" % numberOfSpots.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfSpots(self): self._numberOfSpots = None
    numberOfSpots = property(getNumberOfSpots, setNumberOfSpots, delNumberOfSpots, "Property for numberOfSpots")
    # Methods and properties for the 'rmsd' attribute
    def getRmsd(self): return self._rmsd
    def setRmsd(self, rmsd):
        if rmsd is None:
            self._rmsd = None
        elif rmsd.__class__.__name__ == "XSDataLength":
            self._rmsd = rmsd
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setRmsd argument is not XSDataLength but %s" % rmsd.__class__.__name__
            raise BaseException(strMessage)
    def delRmsd(self): self._rmsd = None
    rmsd = property(getRmsd, setRmsd, delRmsd, "Property for rmsd")
    # Methods and properties for the 'solutionNumber' attribute
    def getSolutionNumber(self): return self._solutionNumber
    def setSolutionNumber(self, solutionNumber):
        if solutionNumber is None:
            self._solutionNumber = None
        elif solutionNumber.__class__.__name__ == "XSDataInteger":
            self._solutionNumber = solutionNumber
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setSolutionNumber argument is not XSDataInteger but %s" % solutionNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSolutionNumber(self): self._solutionNumber = None
    solutionNumber = property(getSolutionNumber, setSolutionNumber, delSolutionNumber, "Property for solutionNumber")
    # Methods and properties for the 'unitCell' attribute
    def getUnitCell(self): return self._unitCell
    def setUnitCell(self, unitCell):
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataCell":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setUnitCell argument is not XSDataCell but %s" % unitCell.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell(self): self._unitCell = None
    unitCell = property(getUnitCell, setUnitCell, delUnitCell, "Property for unitCell")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataInteger":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataLabelitScreenSolution.setVolume argument is not XSDataInteger but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def export(self, outfile, level, name_='XSDataLabelitScreenSolution'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataLabelitScreenSolution'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._bravaisLattice is not None:
            self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
        else:
            warnEmptyAttribute("bravaisLattice", "XSDataString")
        if self._crystalSystem is not None:
            self.crystalSystem.export(outfile, level, name_='crystalSystem')
        else:
            warnEmptyAttribute("crystalSystem", "XSDataString")
        if self._happy is not None:
            self.happy.export(outfile, level, name_='happy')
        else:
            warnEmptyAttribute("happy", "XSDataBoolean")
        if self._metricFitCode is not None:
            self.metricFitCode.export(outfile, level, name_='metricFitCode')
        else:
            warnEmptyAttribute("metricFitCode", "XSDataString")
        if self._metricFitValue is not None:
            self.metricFitValue.export(outfile, level, name_='metricFitValue')
        else:
            warnEmptyAttribute("metricFitValue", "XSDataDouble")
        if self._numberOfSpots is not None:
            self.numberOfSpots.export(outfile, level, name_='numberOfSpots')
        else:
            warnEmptyAttribute("numberOfSpots", "XSDataInteger")
        if self._rmsd is not None:
            self.rmsd.export(outfile, level, name_='rmsd')
        else:
            warnEmptyAttribute("rmsd", "XSDataLength")
        if self._solutionNumber is not None:
            self.solutionNumber.export(outfile, level, name_='solutionNumber')
        else:
            warnEmptyAttribute("solutionNumber", "XSDataInteger")
        if self._unitCell is not None:
            self.unitCell.export(outfile, level, name_='unitCell')
        else:
            warnEmptyAttribute("unitCell", "XSDataCell")
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bravaisLattice':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBravaisLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalSystem':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCrystalSystem(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'happy':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setHappy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'metricFitCode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMetricFitCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'metricFitValue':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMetricFitValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfSpots':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfSpots(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmsd':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRmsd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'solutionNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSolutionNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = XSDataCell()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setVolume(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataLabelitScreenSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataLabelitScreenSolution' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataLabelitScreenSolution is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataLabelitScreenSolution.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitScreenSolution()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataLabelitScreenSolution" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitScreenSolution()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataLabelitScreenSolution


class XSDataLabelitScreenOutput(XSData):
    def __init__(self, selectedSolutionNumber=None, pathToLogFile=None, mosaicity=None, labelitScreenSolution=None, distance=None, beamCentreY=None, beamCentreX=None):
        XSData.__init__(self, )
        if beamCentreX is None:
            self._beamCentreX = None
        elif beamCentreX.__class__.__name__ == "XSDataLength":
            self._beamCentreX = beamCentreX
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'beamCentreX' is not XSDataLength but %s" % self._beamCentreX.__class__.__name__
            raise BaseException(strMessage)
        if beamCentreY is None:
            self._beamCentreY = None
        elif beamCentreY.__class__.__name__ == "XSDataLength":
            self._beamCentreY = beamCentreY
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'beamCentreY' is not XSDataLength but %s" % self._beamCentreY.__class__.__name__
            raise BaseException(strMessage)
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'distance' is not XSDataLength but %s" % self._distance.__class__.__name__
            raise BaseException(strMessage)
        if labelitScreenSolution is None:
            self._labelitScreenSolution = []
        elif labelitScreenSolution.__class__.__name__ == "list":
            self._labelitScreenSolution = labelitScreenSolution
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'labelitScreenSolution' is not list but %s" % self._labelitScreenSolution.__class__.__name__
            raise BaseException(strMessage)
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataAngle":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'mosaicity' is not XSDataAngle but %s" % self._mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'pathToLogFile' is not XSDataFile but %s" % self._pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
        if selectedSolutionNumber is None:
            self._selectedSolutionNumber = None
        elif selectedSolutionNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionNumber = selectedSolutionNumber
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput constructor argument 'selectedSolutionNumber' is not XSDataInteger but %s" % self._selectedSolutionNumber.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'beamCentreX' attribute
    def getBeamCentreX(self): return self._beamCentreX
    def setBeamCentreX(self, beamCentreX):
        if beamCentreX is None:
            self._beamCentreX = None
        elif beamCentreX.__class__.__name__ == "XSDataLength":
            self._beamCentreX = beamCentreX
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setBeamCentreX argument is not XSDataLength but %s" % beamCentreX.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCentreX(self): self._beamCentreX = None
    beamCentreX = property(getBeamCentreX, setBeamCentreX, delBeamCentreX, "Property for beamCentreX")
    # Methods and properties for the 'beamCentreY' attribute
    def getBeamCentreY(self): return self._beamCentreY
    def setBeamCentreY(self, beamCentreY):
        if beamCentreY is None:
            self._beamCentreY = None
        elif beamCentreY.__class__.__name__ == "XSDataLength":
            self._beamCentreY = beamCentreY
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setBeamCentreY argument is not XSDataLength but %s" % beamCentreY.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCentreY(self): self._beamCentreY = None
    beamCentreY = property(getBeamCentreY, setBeamCentreY, delBeamCentreY, "Property for beamCentreY")
    # Methods and properties for the 'distance' attribute
    def getDistance(self): return self._distance
    def setDistance(self, distance):
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setDistance argument is not XSDataLength but %s" % distance.__class__.__name__
            raise BaseException(strMessage)
    def delDistance(self): self._distance = None
    distance = property(getDistance, setDistance, delDistance, "Property for distance")
    # Methods and properties for the 'labelitScreenSolution' attribute
    def getLabelitScreenSolution(self): return self._labelitScreenSolution
    def setLabelitScreenSolution(self, labelitScreenSolution):
        if labelitScreenSolution is None:
            self._labelitScreenSolution = []
        elif labelitScreenSolution.__class__.__name__ == "list":
            self._labelitScreenSolution = labelitScreenSolution
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setLabelitScreenSolution argument is not list but %s" % labelitScreenSolution.__class__.__name__
            raise BaseException(strMessage)
    def delLabelitScreenSolution(self): self._labelitScreenSolution = None
    labelitScreenSolution = property(getLabelitScreenSolution, setLabelitScreenSolution, delLabelitScreenSolution, "Property for labelitScreenSolution")
    def addLabelitScreenSolution(self, value):
        if value is None:
            strMessage = "ERROR! XSDataLabelitScreenOutput.addLabelitScreenSolution argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataLabelitScreenSolution":
            self._labelitScreenSolution.append(value)
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.addLabelitScreenSolution argument is not XSDataLabelitScreenSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertLabelitScreenSolution(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataLabelitScreenOutput.insertLabelitScreenSolution argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataLabelitScreenOutput.insertLabelitScreenSolution argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataLabelitScreenSolution":
            self._labelitScreenSolution[index] = value
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.addLabelitScreenSolution argument is not XSDataLabelitScreenSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mosaicity' attribute
    def getMosaicity(self): return self._mosaicity
    def setMosaicity(self, mosaicity):
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataAngle":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setMosaicity argument is not XSDataAngle but %s" % mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicity(self): self._mosaicity = None
    mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
    # Methods and properties for the 'pathToLogFile' attribute
    def getPathToLogFile(self): return self._pathToLogFile
    def setPathToLogFile(self, pathToLogFile):
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setPathToLogFile argument is not XSDataFile but %s" % pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToLogFile(self): self._pathToLogFile = None
    pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
    # Methods and properties for the 'selectedSolutionNumber' attribute
    def getSelectedSolutionNumber(self): return self._selectedSolutionNumber
    def setSelectedSolutionNumber(self, selectedSolutionNumber):
        if selectedSolutionNumber is None:
            self._selectedSolutionNumber = None
        elif selectedSolutionNumber.__class__.__name__ == "XSDataInteger":
            self._selectedSolutionNumber = selectedSolutionNumber
        else:
            strMessage = "ERROR! XSDataLabelitScreenOutput.setSelectedSolutionNumber argument is not XSDataInteger but %s" % selectedSolutionNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSelectedSolutionNumber(self): self._selectedSolutionNumber = None
    selectedSolutionNumber = property(getSelectedSolutionNumber, setSelectedSolutionNumber, delSelectedSolutionNumber, "Property for selectedSolutionNumber")
    def export(self, outfile, level, name_='XSDataLabelitScreenOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataLabelitScreenOutput'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._beamCentreX is not None:
            self.beamCentreX.export(outfile, level, name_='beamCentreX')
        else:
            warnEmptyAttribute("beamCentreX", "XSDataLength")
        if self._beamCentreY is not None:
            self.beamCentreY.export(outfile, level, name_='beamCentreY')
        else:
            warnEmptyAttribute("beamCentreY", "XSDataLength")
        if self._distance is not None:
            self.distance.export(outfile, level, name_='distance')
        else:
            warnEmptyAttribute("distance", "XSDataLength")
        for labelitScreenSolution_ in self.getLabelitScreenSolution():
            labelitScreenSolution_.export(outfile, level, name_='labelitScreenSolution')
        if self._mosaicity is not None:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        else:
            warnEmptyAttribute("mosaicity", "XSDataAngle")
        if self._pathToLogFile is not None:
            self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
        else:
            warnEmptyAttribute("pathToLogFile", "XSDataFile")
        if self._selectedSolutionNumber is not None:
            self.selectedSolutionNumber.export(outfile, level, name_='selectedSolutionNumber')
        else:
            warnEmptyAttribute("selectedSolutionNumber", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCentreX':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamCentreX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCentreY':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamCentreY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'labelitScreenSolution':
            obj_ = XSDataLabelitScreenSolution()
            obj_.build(child_)
            self.labelitScreenSolution.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToLogFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedSolutionNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSelectedSolutionNumber(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataLabelitScreenOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataLabelitScreenOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataLabelitScreenOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataLabelitScreenOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitScreenOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataLabelitScreenOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLabelitScreenOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataLabelitScreenOutput


class XSDataInputDistlSignalStrength(XSDataInput):
    def __init__(self, configuration=None, referenceImage=None):
        XSDataInput.__init__(self, configuration)
        if referenceImage is None:
            self._referenceImage = None
        elif referenceImage.__class__.__name__ == "XSDataImage":
            self._referenceImage = referenceImage
        else:
            strMessage = "ERROR! XSDataInputDistlSignalStrength constructor argument 'referenceImage' is not XSDataImage but %s" % self._referenceImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'referenceImage' attribute
    def getReferenceImage(self): return self._referenceImage
    def setReferenceImage(self, referenceImage):
        if referenceImage is None:
            self._referenceImage = None
        elif referenceImage.__class__.__name__ == "XSDataImage":
            self._referenceImage = referenceImage
        else:
            strMessage = "ERROR! XSDataInputDistlSignalStrength.setReferenceImage argument is not XSDataImage but %s" % referenceImage.__class__.__name__
            raise BaseException(strMessage)
    def delReferenceImage(self): self._referenceImage = None
    referenceImage = property(getReferenceImage, setReferenceImage, delReferenceImage, "Property for referenceImage")
    def export(self, outfile, level, name_='XSDataInputDistlSignalStrength'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDistlSignalStrength'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._referenceImage is not None:
            self.referenceImage.export(outfile, level, name_='referenceImage')
        else:
            warnEmptyAttribute("referenceImage", "XSDataImage")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'referenceImage':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setReferenceImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDistlSignalStrength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDistlSignalStrength' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDistlSignalStrength is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDistlSignalStrength.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDistlSignalStrength()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDistlSignalStrength" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDistlSignalStrength()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDistlSignalStrength


class XSDataResultDistlSignalStrength(XSDataResult):
    def __init__(self, status=None, imageQualityIndicators=None):
        XSDataResult.__init__(self, status)
        if imageQualityIndicators is None:
            self._imageQualityIndicators = None
        elif imageQualityIndicators.__class__.__name__ == "XSDataImageQualityIndicators":
            self._imageQualityIndicators = imageQualityIndicators
        else:
            strMessage = "ERROR! XSDataResultDistlSignalStrength constructor argument 'imageQualityIndicators' is not XSDataImageQualityIndicators but %s" % self._imageQualityIndicators.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageQualityIndicators' attribute
    def getImageQualityIndicators(self): return self._imageQualityIndicators
    def setImageQualityIndicators(self, imageQualityIndicators):
        if imageQualityIndicators is None:
            self._imageQualityIndicators = None
        elif imageQualityIndicators.__class__.__name__ == "XSDataImageQualityIndicators":
            self._imageQualityIndicators = imageQualityIndicators
        else:
            strMessage = "ERROR! XSDataResultDistlSignalStrength.setImageQualityIndicators argument is not XSDataImageQualityIndicators but %s" % imageQualityIndicators.__class__.__name__
            raise BaseException(strMessage)
    def delImageQualityIndicators(self): self._imageQualityIndicators = None
    imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
    def export(self, outfile, level, name_='XSDataResultDistlSignalStrength'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDistlSignalStrength'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._imageQualityIndicators is not None:
            self.imageQualityIndicators.export(outfile, level, name_='imageQualityIndicators')
        else:
            warnEmptyAttribute("imageQualityIndicators", "XSDataImageQualityIndicators")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageQualityIndicators':
            obj_ = XSDataImageQualityIndicators()
            obj_.build(child_)
            self.setImageQualityIndicators(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDistlSignalStrength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDistlSignalStrength' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDistlSignalStrength is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDistlSignalStrength.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDistlSignalStrength()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDistlSignalStrength" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDistlSignalStrength()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDistlSignalStrength



# End of data representation classes.



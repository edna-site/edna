#!/usr/bin/env python

#
# Generated Tue Dec 10 02:41::54 2013 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
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
from XSDataCommon import XSDataInteger
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



class XSDataImageBackground3D(object):
    def __init__(self, estimate=None, b_cryst=None, b_coef=None, rfactor=None, correlation=None, resolution=None, bfactor=None, scale=None, number=None):
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'number' is not XSDataInteger but %s" % self._number.__class__.__name__
            raise BaseException(strMessage)
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'scale' is not XSDataDouble but %s" % self._scale.__class__.__name__
            raise BaseException(strMessage)
        if bfactor is None:
            self._bfactor = None
        elif bfactor.__class__.__name__ == "XSDataDouble":
            self._bfactor = bfactor
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'bfactor' is not XSDataDouble but %s" % self._bfactor.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if correlation is None:
            self._correlation = None
        elif correlation.__class__.__name__ == "XSDataDouble":
            self._correlation = correlation
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'correlation' is not XSDataDouble but %s" % self._correlation.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if b_coef is None:
            self._b_coef = None
        elif b_coef.__class__.__name__ == "XSDataDouble":
            self._b_coef = b_coef
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'b_coef' is not XSDataDouble but %s" % self._b_coef.__class__.__name__
            raise BaseException(strMessage)
        if b_cryst is None:
            self._b_cryst = None
        elif b_cryst.__class__.__name__ == "XSDataDouble":
            self._b_cryst = b_cryst
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'b_cryst' is not XSDataDouble but %s" % self._b_cryst.__class__.__name__
            raise BaseException(strMessage)
        if estimate is None:
            self._estimate = None
        elif estimate.__class__.__name__ == "XSDataDouble":
            self._estimate = estimate
        else:
            strMessage = "ERROR! XSDataImageBackground3D constructor argument 'estimate' is not XSDataDouble but %s" % self._estimate.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'number' attribute
    def getNumber(self): return self._number
    def setNumber(self, number):
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setNumber argument is not XSDataInteger but %s" % number.__class__.__name__
            raise BaseException(strMessage)
    def delNumber(self): self._number = None
    number = property(getNumber, setNumber, delNumber, "Property for number")
    # Methods and properties for the 'scale' attribute
    def getScale(self): return self._scale
    def setScale(self, scale):
        if scale is None:
            self._scale = None
        elif scale.__class__.__name__ == "XSDataDouble":
            self._scale = scale
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setScale argument is not XSDataDouble but %s" % scale.__class__.__name__
            raise BaseException(strMessage)
    def delScale(self): self._scale = None
    scale = property(getScale, setScale, delScale, "Property for scale")
    # Methods and properties for the 'bfactor' attribute
    def getBfactor(self): return self._bfactor
    def setBfactor(self, bfactor):
        if bfactor is None:
            self._bfactor = None
        elif bfactor.__class__.__name__ == "XSDataDouble":
            self._bfactor = bfactor
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setBfactor argument is not XSDataDouble but %s" % bfactor.__class__.__name__
            raise BaseException(strMessage)
    def delBfactor(self): self._bfactor = None
    bfactor = property(getBfactor, setBfactor, delBfactor, "Property for bfactor")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'correlation' attribute
    def getCorrelation(self): return self._correlation
    def setCorrelation(self, correlation):
        if correlation is None:
            self._correlation = None
        elif correlation.__class__.__name__ == "XSDataDouble":
            self._correlation = correlation
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setCorrelation argument is not XSDataDouble but %s" % correlation.__class__.__name__
            raise BaseException(strMessage)
    def delCorrelation(self): self._correlation = None
    correlation = property(getCorrelation, setCorrelation, delCorrelation, "Property for correlation")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'b_coef' attribute
    def getB_coef(self): return self._b_coef
    def setB_coef(self, b_coef):
        if b_coef is None:
            self._b_coef = None
        elif b_coef.__class__.__name__ == "XSDataDouble":
            self._b_coef = b_coef
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setB_coef argument is not XSDataDouble but %s" % b_coef.__class__.__name__
            raise BaseException(strMessage)
    def delB_coef(self): self._b_coef = None
    b_coef = property(getB_coef, setB_coef, delB_coef, "Property for b_coef")
    # Methods and properties for the 'b_cryst' attribute
    def getB_cryst(self): return self._b_cryst
    def setB_cryst(self, b_cryst):
        if b_cryst is None:
            self._b_cryst = None
        elif b_cryst.__class__.__name__ == "XSDataDouble":
            self._b_cryst = b_cryst
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setB_cryst argument is not XSDataDouble but %s" % b_cryst.__class__.__name__
            raise BaseException(strMessage)
    def delB_cryst(self): self._b_cryst = None
    b_cryst = property(getB_cryst, setB_cryst, delB_cryst, "Property for b_cryst")
    # Methods and properties for the 'estimate' attribute
    def getEstimate(self): return self._estimate
    def setEstimate(self, estimate):
        if estimate is None:
            self._estimate = None
        elif estimate.__class__.__name__ == "XSDataDouble":
            self._estimate = estimate
        else:
            strMessage = "ERROR! XSDataImageBackground3D.setEstimate argument is not XSDataDouble but %s" % estimate.__class__.__name__
            raise BaseException(strMessage)
    def delEstimate(self): self._estimate = None
    estimate = property(getEstimate, setEstimate, delEstimate, "Property for estimate")
    def export(self, outfile, level, name_='XSDataImageBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataImageBackground3D'):
        pass
        if self._number is not None:
            self.number.export(outfile, level, name_='number')
        else:
            warnEmptyAttribute("number", "XSDataInteger")
        if self._scale is not None:
            self.scale.export(outfile, level, name_='scale')
        if self._bfactor is not None:
            self.bfactor.export(outfile, level, name_='bfactor')
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        if self._correlation is not None:
            self.correlation.export(outfile, level, name_='correlation')
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._b_coef is not None:
            self.b_coef.export(outfile, level, name_='b_coef')
        else:
            warnEmptyAttribute("b_coef", "XSDataDouble")
        if self._b_cryst is not None:
            self.b_cryst.export(outfile, level, name_='b_cryst')
        else:
            warnEmptyAttribute("b_cryst", "XSDataDouble")
        if self._estimate is not None:
            self.estimate.export(outfile, level, name_='estimate')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scale':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correlation':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCorrelation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b_coef':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setB_coef(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b_cryst':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setB_cryst(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'estimate':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setEstimate(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataImageBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataImageBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataImageBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataImageBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImageBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataImageBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImageBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataImageBackground3D


class XSDataInputBackground3D(XSDataInput):
    def __init__(self, configuration=None, nameTemplateImage=None, numberImages=None, firstImageNumber=None, startingAngle=None, imageStep=None, oscillationRange=None, orgy=None, orgx=None, fractionPolarization=None, wavelength=None, detectorDistance=None, exposureTime=None, detectorType=None):
        XSDataInput.__init__(self, configuration)
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'detectorType' is not XSDataString but %s" % self._detectorType.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'exposureTime' is not XSDataDouble but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataDouble":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'detectorDistance' is not XSDataDouble but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'wavelength' is not XSDataDouble but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if fractionPolarization is None:
            self._fractionPolarization = None
        elif fractionPolarization.__class__.__name__ == "XSDataDouble":
            self._fractionPolarization = fractionPolarization
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'fractionPolarization' is not XSDataDouble but %s" % self._fractionPolarization.__class__.__name__
            raise BaseException(strMessage)
        if orgx is None:
            self._orgx = None
        elif orgx.__class__.__name__ == "XSDataDouble":
            self._orgx = orgx
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'orgx' is not XSDataDouble but %s" % self._orgx.__class__.__name__
            raise BaseException(strMessage)
        if orgy is None:
            self._orgy = None
        elif orgy.__class__.__name__ == "XSDataDouble":
            self._orgy = orgy
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'orgy' is not XSDataDouble but %s" % self._orgy.__class__.__name__
            raise BaseException(strMessage)
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataDouble":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'oscillationRange' is not XSDataDouble but %s" % self._oscillationRange.__class__.__name__
            raise BaseException(strMessage)
        if imageStep is None:
            self._imageStep = None
        elif imageStep.__class__.__name__ == "XSDataDouble":
            self._imageStep = imageStep
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'imageStep' is not XSDataDouble but %s" % self._imageStep.__class__.__name__
            raise BaseException(strMessage)
        if startingAngle is None:
            self._startingAngle = None
        elif startingAngle.__class__.__name__ == "XSDataDouble":
            self._startingAngle = startingAngle
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'startingAngle' is not XSDataDouble but %s" % self._startingAngle.__class__.__name__
            raise BaseException(strMessage)
        if firstImageNumber is None:
            self._firstImageNumber = None
        elif firstImageNumber.__class__.__name__ == "XSDataInteger":
            self._firstImageNumber = firstImageNumber
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'firstImageNumber' is not XSDataInteger but %s" % self._firstImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if numberImages is None:
            self._numberImages = None
        elif numberImages.__class__.__name__ == "XSDataInteger":
            self._numberImages = numberImages
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'numberImages' is not XSDataInteger but %s" % self._numberImages.__class__.__name__
            raise BaseException(strMessage)
        if nameTemplateImage is None:
            self._nameTemplateImage = None
        elif nameTemplateImage.__class__.__name__ == "XSDataString":
            self._nameTemplateImage = nameTemplateImage
        else:
            strMessage = "ERROR! XSDataInputBackground3D constructor argument 'nameTemplateImage' is not XSDataString but %s" % self._nameTemplateImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detectorType' attribute
    def getDetectorType(self): return self._detectorType
    def setDetectorType(self, detectorType):
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setDetectorType argument is not XSDataString but %s" % detectorType.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorType(self): self._detectorType = None
    detectorType = property(getDetectorType, setDetectorType, delDetectorType, "Property for detectorType")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setExposureTime argument is not XSDataDouble but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataDouble":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setDetectorDistance argument is not XSDataDouble but %s" % detectorDistance.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setWavelength argument is not XSDataDouble but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'fractionPolarization' attribute
    def getFractionPolarization(self): return self._fractionPolarization
    def setFractionPolarization(self, fractionPolarization):
        if fractionPolarization is None:
            self._fractionPolarization = None
        elif fractionPolarization.__class__.__name__ == "XSDataDouble":
            self._fractionPolarization = fractionPolarization
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setFractionPolarization argument is not XSDataDouble but %s" % fractionPolarization.__class__.__name__
            raise BaseException(strMessage)
    def delFractionPolarization(self): self._fractionPolarization = None
    fractionPolarization = property(getFractionPolarization, setFractionPolarization, delFractionPolarization, "Property for fractionPolarization")
    # Methods and properties for the 'orgx' attribute
    def getOrgx(self): return self._orgx
    def setOrgx(self, orgx):
        if orgx is None:
            self._orgx = None
        elif orgx.__class__.__name__ == "XSDataDouble":
            self._orgx = orgx
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setOrgx argument is not XSDataDouble but %s" % orgx.__class__.__name__
            raise BaseException(strMessage)
    def delOrgx(self): self._orgx = None
    orgx = property(getOrgx, setOrgx, delOrgx, "Property for orgx")
    # Methods and properties for the 'orgy' attribute
    def getOrgy(self): return self._orgy
    def setOrgy(self, orgy):
        if orgy is None:
            self._orgy = None
        elif orgy.__class__.__name__ == "XSDataDouble":
            self._orgy = orgy
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setOrgy argument is not XSDataDouble but %s" % orgy.__class__.__name__
            raise BaseException(strMessage)
    def delOrgy(self): self._orgy = None
    orgy = property(getOrgy, setOrgy, delOrgy, "Property for orgy")
    # Methods and properties for the 'oscillationRange' attribute
    def getOscillationRange(self): return self._oscillationRange
    def setOscillationRange(self, oscillationRange):
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataDouble":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setOscillationRange argument is not XSDataDouble but %s" % oscillationRange.__class__.__name__
            raise BaseException(strMessage)
    def delOscillationRange(self): self._oscillationRange = None
    oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
    # Methods and properties for the 'imageStep' attribute
    def getImageStep(self): return self._imageStep
    def setImageStep(self, imageStep):
        if imageStep is None:
            self._imageStep = None
        elif imageStep.__class__.__name__ == "XSDataDouble":
            self._imageStep = imageStep
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setImageStep argument is not XSDataDouble but %s" % imageStep.__class__.__name__
            raise BaseException(strMessage)
    def delImageStep(self): self._imageStep = None
    imageStep = property(getImageStep, setImageStep, delImageStep, "Property for imageStep")
    # Methods and properties for the 'startingAngle' attribute
    def getStartingAngle(self): return self._startingAngle
    def setStartingAngle(self, startingAngle):
        if startingAngle is None:
            self._startingAngle = None
        elif startingAngle.__class__.__name__ == "XSDataDouble":
            self._startingAngle = startingAngle
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setStartingAngle argument is not XSDataDouble but %s" % startingAngle.__class__.__name__
            raise BaseException(strMessage)
    def delStartingAngle(self): self._startingAngle = None
    startingAngle = property(getStartingAngle, setStartingAngle, delStartingAngle, "Property for startingAngle")
    # Methods and properties for the 'firstImageNumber' attribute
    def getFirstImageNumber(self): return self._firstImageNumber
    def setFirstImageNumber(self, firstImageNumber):
        if firstImageNumber is None:
            self._firstImageNumber = None
        elif firstImageNumber.__class__.__name__ == "XSDataInteger":
            self._firstImageNumber = firstImageNumber
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setFirstImageNumber argument is not XSDataInteger but %s" % firstImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delFirstImageNumber(self): self._firstImageNumber = None
    firstImageNumber = property(getFirstImageNumber, setFirstImageNumber, delFirstImageNumber, "Property for firstImageNumber")
    # Methods and properties for the 'numberImages' attribute
    def getNumberImages(self): return self._numberImages
    def setNumberImages(self, numberImages):
        if numberImages is None:
            self._numberImages = None
        elif numberImages.__class__.__name__ == "XSDataInteger":
            self._numberImages = numberImages
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setNumberImages argument is not XSDataInteger but %s" % numberImages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberImages(self): self._numberImages = None
    numberImages = property(getNumberImages, setNumberImages, delNumberImages, "Property for numberImages")
    # Methods and properties for the 'nameTemplateImage' attribute
    def getNameTemplateImage(self): return self._nameTemplateImage
    def setNameTemplateImage(self, nameTemplateImage):
        if nameTemplateImage is None:
            self._nameTemplateImage = None
        elif nameTemplateImage.__class__.__name__ == "XSDataString":
            self._nameTemplateImage = nameTemplateImage
        else:
            strMessage = "ERROR! XSDataInputBackground3D.setNameTemplateImage argument is not XSDataString but %s" % nameTemplateImage.__class__.__name__
            raise BaseException(strMessage)
    def delNameTemplateImage(self): self._nameTemplateImage = None
    nameTemplateImage = property(getNameTemplateImage, setNameTemplateImage, delNameTemplateImage, "Property for nameTemplateImage")
    def export(self, outfile, level, name_='XSDataInputBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputBackground3D'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._detectorType is not None:
            self.detectorType.export(outfile, level, name_='detectorType')
        else:
            warnEmptyAttribute("detectorType", "XSDataString")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        else:
            warnEmptyAttribute("exposureTime", "XSDataDouble")
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_='detectorDistance')
        else:
            warnEmptyAttribute("detectorDistance", "XSDataDouble")
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        else:
            warnEmptyAttribute("wavelength", "XSDataDouble")
        if self._fractionPolarization is not None:
            self.fractionPolarization.export(outfile, level, name_='fractionPolarization')
        if self._orgx is not None:
            self.orgx.export(outfile, level, name_='orgx')
        else:
            warnEmptyAttribute("orgx", "XSDataDouble")
        if self._orgy is not None:
            self.orgy.export(outfile, level, name_='orgy')
        else:
            warnEmptyAttribute("orgy", "XSDataDouble")
        if self._oscillationRange is not None:
            self.oscillationRange.export(outfile, level, name_='oscillationRange')
        else:
            warnEmptyAttribute("oscillationRange", "XSDataDouble")
        if self._imageStep is not None:
            self.imageStep.export(outfile, level, name_='imageStep')
        if self._startingAngle is not None:
            self.startingAngle.export(outfile, level, name_='startingAngle')
        if self._firstImageNumber is not None:
            self.firstImageNumber.export(outfile, level, name_='firstImageNumber')
        else:
            warnEmptyAttribute("firstImageNumber", "XSDataInteger")
        if self._numberImages is not None:
            self.numberImages.export(outfile, level, name_='numberImages')
        else:
            warnEmptyAttribute("numberImages", "XSDataInteger")
        if self._nameTemplateImage is not None:
            self.nameTemplateImage.export(outfile, level, name_='nameTemplateImage')
        else:
            warnEmptyAttribute("nameTemplateImage", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorType':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetectorType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fractionPolarization':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFractionPolarization(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orgx':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOrgx(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orgy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOrgy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationRange':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOscillationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageStep':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setImageStep(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startingAngle':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStartingAngle(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFirstImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberImages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nameTemplateImage':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setNameTemplateImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputBackground3D


class XSDataResultBackground3D(XSDataResult):
    def __init__(self, status=None, imageBackground=None):
        XSDataResult.__init__(self, status)
        if imageBackground is None:
            self._imageBackground = []
        elif imageBackground.__class__.__name__ == "list":
            self._imageBackground = imageBackground
        else:
            strMessage = "ERROR! XSDataResultBackground3D constructor argument 'imageBackground' is not list but %s" % self._imageBackground.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageBackground' attribute
    def getImageBackground(self): return self._imageBackground
    def setImageBackground(self, imageBackground):
        if imageBackground is None:
            self._imageBackground = []
        elif imageBackground.__class__.__name__ == "list":
            self._imageBackground = imageBackground
        else:
            strMessage = "ERROR! XSDataResultBackground3D.setImageBackground argument is not list but %s" % imageBackground.__class__.__name__
            raise BaseException(strMessage)
    def delImageBackground(self): self._imageBackground = None
    imageBackground = property(getImageBackground, setImageBackground, delImageBackground, "Property for imageBackground")
    def addImageBackground(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultBackground3D.addImageBackground argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataImageBackground3D":
            self._imageBackground.append(value)
        else:
            strMessage = "ERROR! XSDataResultBackground3D.addImageBackground argument is not XSDataImageBackground3D but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImageBackground(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultBackground3D.insertImageBackground argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultBackground3D.insertImageBackground argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataImageBackground3D":
            self._imageBackground[index] = value
        else:
            strMessage = "ERROR! XSDataResultBackground3D.addImageBackground argument is not XSDataImageBackground3D but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultBackground3D'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultBackground3D'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for imageBackground_ in self.getImageBackground():
            imageBackground_.export(outfile, level, name_='imageBackground')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageBackground':
            obj_ = XSDataImageBackground3D()
            obj_.build(child_)
            self.imageBackground.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultBackground3D" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultBackground3D' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultBackground3D is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultBackground3D.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBackground3D()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultBackground3D" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBackground3D()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultBackground3D



# End of data representation classes.



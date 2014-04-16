#!/usr/bin/env python

#
# Generated Wed Apr 16 08:26::37 2014 by EDGenerateDS.
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



class XSDataImageDozor(object):
    def __init__(self, score=None, powder_wilson_rfactor=None, powder_wilson_correlation=None, powder_wilson_resolution=None, powder_wilson_bfactor=None, powder_wilson_scale=None, spots_resolution=None, spots_int_aver=None, spots_num_of=None, number=None):
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'number' is not XSDataInteger but %s" % self._number.__class__.__name__
            raise BaseException(strMessage)
        if spots_num_of is None:
            self._spots_num_of = None
        elif spots_num_of.__class__.__name__ == "XSDataInteger":
            self._spots_num_of = spots_num_of
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'spots_num_of' is not XSDataInteger but %s" % self._spots_num_of.__class__.__name__
            raise BaseException(strMessage)
        if spots_int_aver is None:
            self._spots_int_aver = None
        elif spots_int_aver.__class__.__name__ == "XSDataDouble":
            self._spots_int_aver = spots_int_aver
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'spots_int_aver' is not XSDataDouble but %s" % self._spots_int_aver.__class__.__name__
            raise BaseException(strMessage)
        if spots_resolution is None:
            self._spots_resolution = None
        elif spots_resolution.__class__.__name__ == "XSDataDouble":
            self._spots_resolution = spots_resolution
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'spots_resolution' is not XSDataDouble but %s" % self._spots_resolution.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_scale is None:
            self._powder_wilson_scale = None
        elif powder_wilson_scale.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_scale = powder_wilson_scale
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'powder_wilson_scale' is not XSDataDouble but %s" % self._powder_wilson_scale.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_bfactor is None:
            self._powder_wilson_bfactor = None
        elif powder_wilson_bfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_bfactor = powder_wilson_bfactor
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'powder_wilson_bfactor' is not XSDataDouble but %s" % self._powder_wilson_bfactor.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_resolution is None:
            self._powder_wilson_resolution = None
        elif powder_wilson_resolution.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_resolution = powder_wilson_resolution
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'powder_wilson_resolution' is not XSDataDouble but %s" % self._powder_wilson_resolution.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_correlation is None:
            self._powder_wilson_correlation = None
        elif powder_wilson_correlation.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_correlation = powder_wilson_correlation
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'powder_wilson_correlation' is not XSDataDouble but %s" % self._powder_wilson_correlation.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_rfactor is None:
            self._powder_wilson_rfactor = None
        elif powder_wilson_rfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_rfactor = powder_wilson_rfactor
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'powder_wilson_rfactor' is not XSDataDouble but %s" % self._powder_wilson_rfactor.__class__.__name__
            raise BaseException(strMessage)
        if score is None:
            self._score = None
        elif score.__class__.__name__ == "XSDataDouble":
            self._score = score
        else:
            strMessage = "ERROR! XSDataImageDozor constructor argument 'score' is not XSDataDouble but %s" % self._score.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'number' attribute
    def getNumber(self): return self._number
    def setNumber(self, number):
        if number is None:
            self._number = None
        elif number.__class__.__name__ == "XSDataInteger":
            self._number = number
        else:
            strMessage = "ERROR! XSDataImageDozor.setNumber argument is not XSDataInteger but %s" % number.__class__.__name__
            raise BaseException(strMessage)
    def delNumber(self): self._number = None
    number = property(getNumber, setNumber, delNumber, "Property for number")
    # Methods and properties for the 'spots_num_of' attribute
    def getSpots_num_of(self): return self._spots_num_of
    def setSpots_num_of(self, spots_num_of):
        if spots_num_of is None:
            self._spots_num_of = None
        elif spots_num_of.__class__.__name__ == "XSDataInteger":
            self._spots_num_of = spots_num_of
        else:
            strMessage = "ERROR! XSDataImageDozor.setSpots_num_of argument is not XSDataInteger but %s" % spots_num_of.__class__.__name__
            raise BaseException(strMessage)
    def delSpots_num_of(self): self._spots_num_of = None
    spots_num_of = property(getSpots_num_of, setSpots_num_of, delSpots_num_of, "Property for spots_num_of")
    # Methods and properties for the 'spots_int_aver' attribute
    def getSpots_int_aver(self): return self._spots_int_aver
    def setSpots_int_aver(self, spots_int_aver):
        if spots_int_aver is None:
            self._spots_int_aver = None
        elif spots_int_aver.__class__.__name__ == "XSDataDouble":
            self._spots_int_aver = spots_int_aver
        else:
            strMessage = "ERROR! XSDataImageDozor.setSpots_int_aver argument is not XSDataDouble but %s" % spots_int_aver.__class__.__name__
            raise BaseException(strMessage)
    def delSpots_int_aver(self): self._spots_int_aver = None
    spots_int_aver = property(getSpots_int_aver, setSpots_int_aver, delSpots_int_aver, "Property for spots_int_aver")
    # Methods and properties for the 'spots_resolution' attribute
    def getSpots_resolution(self): return self._spots_resolution
    def setSpots_resolution(self, spots_resolution):
        if spots_resolution is None:
            self._spots_resolution = None
        elif spots_resolution.__class__.__name__ == "XSDataDouble":
            self._spots_resolution = spots_resolution
        else:
            strMessage = "ERROR! XSDataImageDozor.setSpots_resolution argument is not XSDataDouble but %s" % spots_resolution.__class__.__name__
            raise BaseException(strMessage)
    def delSpots_resolution(self): self._spots_resolution = None
    spots_resolution = property(getSpots_resolution, setSpots_resolution, delSpots_resolution, "Property for spots_resolution")
    # Methods and properties for the 'powder_wilson_scale' attribute
    def getPowder_wilson_scale(self): return self._powder_wilson_scale
    def setPowder_wilson_scale(self, powder_wilson_scale):
        if powder_wilson_scale is None:
            self._powder_wilson_scale = None
        elif powder_wilson_scale.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_scale = powder_wilson_scale
        else:
            strMessage = "ERROR! XSDataImageDozor.setPowder_wilson_scale argument is not XSDataDouble but %s" % powder_wilson_scale.__class__.__name__
            raise BaseException(strMessage)
    def delPowder_wilson_scale(self): self._powder_wilson_scale = None
    powder_wilson_scale = property(getPowder_wilson_scale, setPowder_wilson_scale, delPowder_wilson_scale, "Property for powder_wilson_scale")
    # Methods and properties for the 'powder_wilson_bfactor' attribute
    def getPowder_wilson_bfactor(self): return self._powder_wilson_bfactor
    def setPowder_wilson_bfactor(self, powder_wilson_bfactor):
        if powder_wilson_bfactor is None:
            self._powder_wilson_bfactor = None
        elif powder_wilson_bfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_bfactor = powder_wilson_bfactor
        else:
            strMessage = "ERROR! XSDataImageDozor.setPowder_wilson_bfactor argument is not XSDataDouble but %s" % powder_wilson_bfactor.__class__.__name__
            raise BaseException(strMessage)
    def delPowder_wilson_bfactor(self): self._powder_wilson_bfactor = None
    powder_wilson_bfactor = property(getPowder_wilson_bfactor, setPowder_wilson_bfactor, delPowder_wilson_bfactor, "Property for powder_wilson_bfactor")
    # Methods and properties for the 'powder_wilson_resolution' attribute
    def getPowder_wilson_resolution(self): return self._powder_wilson_resolution
    def setPowder_wilson_resolution(self, powder_wilson_resolution):
        if powder_wilson_resolution is None:
            self._powder_wilson_resolution = None
        elif powder_wilson_resolution.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_resolution = powder_wilson_resolution
        else:
            strMessage = "ERROR! XSDataImageDozor.setPowder_wilson_resolution argument is not XSDataDouble but %s" % powder_wilson_resolution.__class__.__name__
            raise BaseException(strMessage)
    def delPowder_wilson_resolution(self): self._powder_wilson_resolution = None
    powder_wilson_resolution = property(getPowder_wilson_resolution, setPowder_wilson_resolution, delPowder_wilson_resolution, "Property for powder_wilson_resolution")
    # Methods and properties for the 'powder_wilson_correlation' attribute
    def getPowder_wilson_correlation(self): return self._powder_wilson_correlation
    def setPowder_wilson_correlation(self, powder_wilson_correlation):
        if powder_wilson_correlation is None:
            self._powder_wilson_correlation = None
        elif powder_wilson_correlation.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_correlation = powder_wilson_correlation
        else:
            strMessage = "ERROR! XSDataImageDozor.setPowder_wilson_correlation argument is not XSDataDouble but %s" % powder_wilson_correlation.__class__.__name__
            raise BaseException(strMessage)
    def delPowder_wilson_correlation(self): self._powder_wilson_correlation = None
    powder_wilson_correlation = property(getPowder_wilson_correlation, setPowder_wilson_correlation, delPowder_wilson_correlation, "Property for powder_wilson_correlation")
    # Methods and properties for the 'powder_wilson_rfactor' attribute
    def getPowder_wilson_rfactor(self): return self._powder_wilson_rfactor
    def setPowder_wilson_rfactor(self, powder_wilson_rfactor):
        if powder_wilson_rfactor is None:
            self._powder_wilson_rfactor = None
        elif powder_wilson_rfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_rfactor = powder_wilson_rfactor
        else:
            strMessage = "ERROR! XSDataImageDozor.setPowder_wilson_rfactor argument is not XSDataDouble but %s" % powder_wilson_rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delPowder_wilson_rfactor(self): self._powder_wilson_rfactor = None
    powder_wilson_rfactor = property(getPowder_wilson_rfactor, setPowder_wilson_rfactor, delPowder_wilson_rfactor, "Property for powder_wilson_rfactor")
    # Methods and properties for the 'score' attribute
    def getScore(self): return self._score
    def setScore(self, score):
        if score is None:
            self._score = None
        elif score.__class__.__name__ == "XSDataDouble":
            self._score = score
        else:
            strMessage = "ERROR! XSDataImageDozor.setScore argument is not XSDataDouble but %s" % score.__class__.__name__
            raise BaseException(strMessage)
    def delScore(self): self._score = None
    score = property(getScore, setScore, delScore, "Property for score")
    def export(self, outfile, level, name_='XSDataImageDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataImageDozor'):
        pass
        if self._number is not None:
            self.number.export(outfile, level, name_='number')
        else:
            warnEmptyAttribute("number", "XSDataInteger")
        if self._spots_num_of is not None:
            self.spots_num_of.export(outfile, level, name_='spots_num_of')
        else:
            warnEmptyAttribute("spots_num_of", "XSDataInteger")
        if self._spots_int_aver is not None:
            self.spots_int_aver.export(outfile, level, name_='spots_int_aver')
        else:
            warnEmptyAttribute("spots_int_aver", "XSDataDouble")
        if self._spots_resolution is not None:
            self.spots_resolution.export(outfile, level, name_='spots_resolution')
        if self._powder_wilson_scale is not None:
            self.powder_wilson_scale.export(outfile, level, name_='powder_wilson_scale')
        if self._powder_wilson_bfactor is not None:
            self.powder_wilson_bfactor.export(outfile, level, name_='powder_wilson_bfactor')
        if self._powder_wilson_resolution is not None:
            self.powder_wilson_resolution.export(outfile, level, name_='powder_wilson_resolution')
        if self._powder_wilson_correlation is not None:
            self.powder_wilson_correlation.export(outfile, level, name_='powder_wilson_correlation')
        if self._powder_wilson_rfactor is not None:
            self.powder_wilson_rfactor.export(outfile, level, name_='powder_wilson_rfactor')
        if self._score is not None:
            self.score.export(outfile, level, name_='score')
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
            nodeName_ == 'spots_num_of':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpots_num_of(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spots_int_aver':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSpots_int_aver(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spots_resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSpots_resolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'powder_wilson_scale':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPowder_wilson_scale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'powder_wilson_bfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPowder_wilson_bfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'powder_wilson_resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPowder_wilson_resolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'powder_wilson_correlation':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPowder_wilson_correlation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'powder_wilson_rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPowder_wilson_rfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'score':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setScore(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataImageDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataImageDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataImageDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataImageDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImageDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataImageDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImageDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataImageDozor


class XSDataInputDozor(XSDataInput):
    def __init__(self, configuration=None, nameTemplateImage=None, numberImages=None, firstImageNumber=None, startingAngle=None, imageStep=None, oscillationRange=None, orgy=None, orgx=None, fractionPolarization=None, wavelength=None, detectorDistance=None, spotSize=None, exposureTime=None, detectorType=None):
        XSDataInput.__init__(self, configuration)
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'detectorType' is not XSDataString but %s" % self._detectorType.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'exposureTime' is not XSDataDouble but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if spotSize is None:
            self._spotSize = None
        elif spotSize.__class__.__name__ == "XSDataDouble":
            self._spotSize = spotSize
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'spotSize' is not XSDataDouble but %s" % self._spotSize.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataDouble":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'detectorDistance' is not XSDataDouble but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'wavelength' is not XSDataDouble but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if fractionPolarization is None:
            self._fractionPolarization = None
        elif fractionPolarization.__class__.__name__ == "XSDataDouble":
            self._fractionPolarization = fractionPolarization
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'fractionPolarization' is not XSDataDouble but %s" % self._fractionPolarization.__class__.__name__
            raise BaseException(strMessage)
        if orgx is None:
            self._orgx = None
        elif orgx.__class__.__name__ == "XSDataDouble":
            self._orgx = orgx
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'orgx' is not XSDataDouble but %s" % self._orgx.__class__.__name__
            raise BaseException(strMessage)
        if orgy is None:
            self._orgy = None
        elif orgy.__class__.__name__ == "XSDataDouble":
            self._orgy = orgy
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'orgy' is not XSDataDouble but %s" % self._orgy.__class__.__name__
            raise BaseException(strMessage)
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataDouble":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'oscillationRange' is not XSDataDouble but %s" % self._oscillationRange.__class__.__name__
            raise BaseException(strMessage)
        if imageStep is None:
            self._imageStep = None
        elif imageStep.__class__.__name__ == "XSDataDouble":
            self._imageStep = imageStep
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'imageStep' is not XSDataDouble but %s" % self._imageStep.__class__.__name__
            raise BaseException(strMessage)
        if startingAngle is None:
            self._startingAngle = None
        elif startingAngle.__class__.__name__ == "XSDataDouble":
            self._startingAngle = startingAngle
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'startingAngle' is not XSDataDouble but %s" % self._startingAngle.__class__.__name__
            raise BaseException(strMessage)
        if firstImageNumber is None:
            self._firstImageNumber = None
        elif firstImageNumber.__class__.__name__ == "XSDataInteger":
            self._firstImageNumber = firstImageNumber
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'firstImageNumber' is not XSDataInteger but %s" % self._firstImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if numberImages is None:
            self._numberImages = None
        elif numberImages.__class__.__name__ == "XSDataInteger":
            self._numberImages = numberImages
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'numberImages' is not XSDataInteger but %s" % self._numberImages.__class__.__name__
            raise BaseException(strMessage)
        if nameTemplateImage is None:
            self._nameTemplateImage = None
        elif nameTemplateImage.__class__.__name__ == "XSDataString":
            self._nameTemplateImage = nameTemplateImage
        else:
            strMessage = "ERROR! XSDataInputDozor constructor argument 'nameTemplateImage' is not XSDataString but %s" % self._nameTemplateImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detectorType' attribute
    def getDetectorType(self): return self._detectorType
    def setDetectorType(self, detectorType):
        if detectorType is None:
            self._detectorType = None
        elif detectorType.__class__.__name__ == "XSDataString":
            self._detectorType = detectorType
        else:
            strMessage = "ERROR! XSDataInputDozor.setDetectorType argument is not XSDataString but %s" % detectorType.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setExposureTime argument is not XSDataDouble but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'spotSize' attribute
    def getSpotSize(self): return self._spotSize
    def setSpotSize(self, spotSize):
        if spotSize is None:
            self._spotSize = None
        elif spotSize.__class__.__name__ == "XSDataDouble":
            self._spotSize = spotSize
        else:
            strMessage = "ERROR! XSDataInputDozor.setSpotSize argument is not XSDataDouble but %s" % spotSize.__class__.__name__
            raise BaseException(strMessage)
    def delSpotSize(self): self._spotSize = None
    spotSize = property(getSpotSize, setSpotSize, delSpotSize, "Property for spotSize")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataDouble":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataInputDozor.setDetectorDistance argument is not XSDataDouble but %s" % detectorDistance.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setWavelength argument is not XSDataDouble but %s" % wavelength.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setFractionPolarization argument is not XSDataDouble but %s" % fractionPolarization.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setOrgx argument is not XSDataDouble but %s" % orgx.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setOrgy argument is not XSDataDouble but %s" % orgy.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setOscillationRange argument is not XSDataDouble but %s" % oscillationRange.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setImageStep argument is not XSDataDouble but %s" % imageStep.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setStartingAngle argument is not XSDataDouble but %s" % startingAngle.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setFirstImageNumber argument is not XSDataInteger but %s" % firstImageNumber.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setNumberImages argument is not XSDataInteger but %s" % numberImages.__class__.__name__
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
            strMessage = "ERROR! XSDataInputDozor.setNameTemplateImage argument is not XSDataString but %s" % nameTemplateImage.__class__.__name__
            raise BaseException(strMessage)
    def delNameTemplateImage(self): self._nameTemplateImage = None
    nameTemplateImage = property(getNameTemplateImage, setNameTemplateImage, delNameTemplateImage, "Property for nameTemplateImage")
    def export(self, outfile, level, name_='XSDataInputDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDozor'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._detectorType is not None:
            self.detectorType.export(outfile, level, name_='detectorType')
        else:
            warnEmptyAttribute("detectorType", "XSDataString")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        else:
            warnEmptyAttribute("exposureTime", "XSDataDouble")
        if self._spotSize is not None:
            self.spotSize.export(outfile, level, name_='spotSize')
        else:
            warnEmptyAttribute("spotSize", "XSDataDouble")
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
            nodeName_ == 'spotSize':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSpotSize(obj_)
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
        self.export( oStreamString, 0, name_="XSDataInputDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDozor


class XSDataResultDozor(XSDataResult):
    def __init__(self, status=None, imageDozor=None):
        XSDataResult.__init__(self, status)
        if imageDozor is None:
            self._imageDozor = []
        elif imageDozor.__class__.__name__ == "list":
            self._imageDozor = imageDozor
        else:
            strMessage = "ERROR! XSDataResultDozor constructor argument 'imageDozor' is not list but %s" % self._imageDozor.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageDozor' attribute
    def getImageDozor(self): return self._imageDozor
    def setImageDozor(self, imageDozor):
        if imageDozor is None:
            self._imageDozor = []
        elif imageDozor.__class__.__name__ == "list":
            self._imageDozor = imageDozor
        else:
            strMessage = "ERROR! XSDataResultDozor.setImageDozor argument is not list but %s" % imageDozor.__class__.__name__
            raise BaseException(strMessage)
    def delImageDozor(self): self._imageDozor = None
    imageDozor = property(getImageDozor, setImageDozor, delImageDozor, "Property for imageDozor")
    def addImageDozor(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultDozor.addImageDozor argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataImageDozor":
            self._imageDozor.append(value)
        else:
            strMessage = "ERROR! XSDataResultDozor.addImageDozor argument is not XSDataImageDozor but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImageDozor(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultDozor.insertImageDozor argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultDozor.insertImageDozor argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataImageDozor":
            self._imageDozor[index] = value
        else:
            strMessage = "ERROR! XSDataResultDozor.addImageDozor argument is not XSDataImageDozor but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDozor'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for imageDozor_ in self.getImageDozor():
            imageDozor_.export(outfile, level, name_='imageDozor')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageDozor':
            obj_ = XSDataImageDozor()
            obj_.build(child_)
            self.imageDozor.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDozor



# End of data representation classes.



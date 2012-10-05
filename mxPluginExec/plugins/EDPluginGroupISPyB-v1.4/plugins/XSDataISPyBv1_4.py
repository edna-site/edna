#!/usr/bin/env python

#
# Generated Mon Sep 10 01:27::47 2012 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataAngle
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
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
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime




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



class AutoProc(object):
    def __init__(self, refinedCell_gamma=None, refinedCell_beta=None, refinedCell_alpha=None, refinedCell_c=None, refinedCell_b=None, refinedCell_a=None, spaceGroup=None, autoProcId=None):
        if autoProcId is None:
            self._autoProcId = None
        else:
            self._autoProcId = int(autoProcId)
        self._spaceGroup = str(spaceGroup)
        self._refinedCell_a = str(refinedCell_a)
        self._refinedCell_b = str(refinedCell_b)
        self._refinedCell_c = str(refinedCell_c)
        self._refinedCell_alpha = str(refinedCell_alpha)
        self._refinedCell_beta = str(refinedCell_beta)
        self._refinedCell_gamma = str(refinedCell_gamma)
    # Methods and properties for the 'autoProcId' attribute
    def getAutoProcId(self): return self._autoProcId
    def setAutoProcId(self, autoProcId):
        if autoProcId is None:
            self._autoProcId = None
        else:
            self._autoProcId = int(autoProcId)
    def delAutoProcId(self): self._autoProcId = None
    autoProcId = property(getAutoProcId, setAutoProcId, delAutoProcId, "Property for autoProcId")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        self._spaceGroup = str(spaceGroup)
    def delSpaceGroup(self): self._spaceGroup = None
    spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
    # Methods and properties for the 'refinedCell_a' attribute
    def getRefinedCell_a(self): return self._refinedCell_a
    def setRefinedCell_a(self, refinedCell_a):
        self._refinedCell_a = str(refinedCell_a)
    def delRefinedCell_a(self): self._refinedCell_a = None
    refinedCell_a = property(getRefinedCell_a, setRefinedCell_a, delRefinedCell_a, "Property for refinedCell_a")
    # Methods and properties for the 'refinedCell_b' attribute
    def getRefinedCell_b(self): return self._refinedCell_b
    def setRefinedCell_b(self, refinedCell_b):
        self._refinedCell_b = str(refinedCell_b)
    def delRefinedCell_b(self): self._refinedCell_b = None
    refinedCell_b = property(getRefinedCell_b, setRefinedCell_b, delRefinedCell_b, "Property for refinedCell_b")
    # Methods and properties for the 'refinedCell_c' attribute
    def getRefinedCell_c(self): return self._refinedCell_c
    def setRefinedCell_c(self, refinedCell_c):
        self._refinedCell_c = str(refinedCell_c)
    def delRefinedCell_c(self): self._refinedCell_c = None
    refinedCell_c = property(getRefinedCell_c, setRefinedCell_c, delRefinedCell_c, "Property for refinedCell_c")
    # Methods and properties for the 'refinedCell_alpha' attribute
    def getRefinedCell_alpha(self): return self._refinedCell_alpha
    def setRefinedCell_alpha(self, refinedCell_alpha):
        self._refinedCell_alpha = str(refinedCell_alpha)
    def delRefinedCell_alpha(self): self._refinedCell_alpha = None
    refinedCell_alpha = property(getRefinedCell_alpha, setRefinedCell_alpha, delRefinedCell_alpha, "Property for refinedCell_alpha")
    # Methods and properties for the 'refinedCell_beta' attribute
    def getRefinedCell_beta(self): return self._refinedCell_beta
    def setRefinedCell_beta(self, refinedCell_beta):
        self._refinedCell_beta = str(refinedCell_beta)
    def delRefinedCell_beta(self): self._refinedCell_beta = None
    refinedCell_beta = property(getRefinedCell_beta, setRefinedCell_beta, delRefinedCell_beta, "Property for refinedCell_beta")
    # Methods and properties for the 'refinedCell_gamma' attribute
    def getRefinedCell_gamma(self): return self._refinedCell_gamma
    def setRefinedCell_gamma(self, refinedCell_gamma):
        self._refinedCell_gamma = str(refinedCell_gamma)
    def delRefinedCell_gamma(self): self._refinedCell_gamma = None
    refinedCell_gamma = property(getRefinedCell_gamma, setRefinedCell_gamma, delRefinedCell_gamma, "Property for refinedCell_gamma")
    def export(self, outfile, level, name_='AutoProc'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProc'):
        pass
        if self._autoProcId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcId>%d</autoProcId>\n' % self._autoProcId))
        if self._spaceGroup is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<spaceGroup>%s</spaceGroup>\n' % self._spaceGroup))
        else:
            warnEmptyAttribute("spaceGroup", "string")
        if self._refinedCell_a is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_a>%s</refinedCell_a>\n' % self._refinedCell_a))
        else:
            warnEmptyAttribute("refinedCell_a", "string")
        if self._refinedCell_b is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_b>%s</refinedCell_b>\n' % self._refinedCell_b))
        else:
            warnEmptyAttribute("refinedCell_b", "string")
        if self._refinedCell_c is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_c>%s</refinedCell_c>\n' % self._refinedCell_c))
        else:
            warnEmptyAttribute("refinedCell_c", "string")
        if self._refinedCell_alpha is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_alpha>%s</refinedCell_alpha>\n' % self._refinedCell_alpha))
        else:
            warnEmptyAttribute("refinedCell_alpha", "string")
        if self._refinedCell_beta is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_beta>%s</refinedCell_beta>\n' % self._refinedCell_beta))
        else:
            warnEmptyAttribute("refinedCell_beta", "string")
        if self._refinedCell_gamma is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedCell_gamma>%s</refinedCell_gamma>\n' % self._refinedCell_gamma))
        else:
            warnEmptyAttribute("refinedCell_gamma", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._spaceGroup = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_a':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_a = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_b':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_b = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_c':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_c = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_alpha':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_alpha = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_beta':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_beta = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedCell_gamma':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._refinedCell_gamma = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProc" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProc' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProc is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProc.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProc()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProc" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProc()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProc


class AutoProcContainer(object):
    def __init__(self, AutoProcProgramContainer=None, AutoProcScalingContainer=None, AutoProc=None):
        if AutoProc is None:
            self._AutoProc = None
        elif AutoProc.__class__.__name__ == "AutoProc":
            self._AutoProc = AutoProc
        else:
            strMessage = "ERROR! AutoProcContainer constructor argument 'AutoProc' is not AutoProc but %s" % self._AutoProc.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcScalingContainer is None:
            self._AutoProcScalingContainer = None
        elif AutoProcScalingContainer.__class__.__name__ == "AutoProcScalingContainer":
            self._AutoProcScalingContainer = AutoProcScalingContainer
        else:
            strMessage = "ERROR! AutoProcContainer constructor argument 'AutoProcScalingContainer' is not AutoProcScalingContainer but %s" % self._AutoProcScalingContainer.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcProgramContainer is None:
            self._AutoProcProgramContainer = None
        elif AutoProcProgramContainer.__class__.__name__ == "AutoProcProgramContainer":
            self._AutoProcProgramContainer = AutoProcProgramContainer
        else:
            strMessage = "ERROR! AutoProcContainer constructor argument 'AutoProcProgramContainer' is not AutoProcProgramContainer but %s" % self._AutoProcProgramContainer.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'AutoProc' attribute
    def getAutoProc(self): return self._AutoProc
    def setAutoProc(self, AutoProc):
        if AutoProc is None:
            self._AutoProc = None
        elif AutoProc.__class__.__name__ == "AutoProc":
            self._AutoProc = AutoProc
        else:
            strMessage = "ERROR! AutoProcContainer.setAutoProc argument is not AutoProc but %s" % AutoProc.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProc(self): self._AutoProc = None
    AutoProc = property(getAutoProc, setAutoProc, delAutoProc, "Property for AutoProc")
    # Methods and properties for the 'AutoProcScalingContainer' attribute
    def getAutoProcScalingContainer(self): return self._AutoProcScalingContainer
    def setAutoProcScalingContainer(self, AutoProcScalingContainer):
        if AutoProcScalingContainer is None:
            self._AutoProcScalingContainer = None
        elif AutoProcScalingContainer.__class__.__name__ == "AutoProcScalingContainer":
            self._AutoProcScalingContainer = AutoProcScalingContainer
        else:
            strMessage = "ERROR! AutoProcContainer.setAutoProcScalingContainer argument is not AutoProcScalingContainer but %s" % AutoProcScalingContainer.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcScalingContainer(self): self._AutoProcScalingContainer = None
    AutoProcScalingContainer = property(getAutoProcScalingContainer, setAutoProcScalingContainer, delAutoProcScalingContainer, "Property for AutoProcScalingContainer")
    # Methods and properties for the 'AutoProcProgramContainer' attribute
    def getAutoProcProgramContainer(self): return self._AutoProcProgramContainer
    def setAutoProcProgramContainer(self, AutoProcProgramContainer):
        if AutoProcProgramContainer is None:
            self._AutoProcProgramContainer = None
        elif AutoProcProgramContainer.__class__.__name__ == "AutoProcProgramContainer":
            self._AutoProcProgramContainer = AutoProcProgramContainer
        else:
            strMessage = "ERROR! AutoProcContainer.setAutoProcProgramContainer argument is not AutoProcProgramContainer but %s" % AutoProcProgramContainer.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcProgramContainer(self): self._AutoProcProgramContainer = None
    AutoProcProgramContainer = property(getAutoProcProgramContainer, setAutoProcProgramContainer, delAutoProcProgramContainer, "Property for AutoProcProgramContainer")
    def export(self, outfile, level, name_='AutoProcContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcContainer'):
        pass
        if self._AutoProc is not None:
            self.AutoProc.export(outfile, level, name_='AutoProc')
        else:
            warnEmptyAttribute("AutoProc", "AutoProc")
        if self._AutoProcScalingContainer is not None:
            self.AutoProcScalingContainer.export(outfile, level, name_='AutoProcScalingContainer')
        else:
            warnEmptyAttribute("AutoProcScalingContainer", "AutoProcScalingContainer")
        if self._AutoProcProgramContainer is not None:
            self.AutoProcProgramContainer.export(outfile, level, name_='AutoProcProgramContainer')
        else:
            warnEmptyAttribute("AutoProcProgramContainer", "AutoProcProgramContainer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProc':
            obj_ = AutoProc()
            obj_.build(child_)
            self.setAutoProc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcScalingContainer':
            obj_ = AutoProcScalingContainer()
            obj_.build(child_)
            self.setAutoProcScalingContainer(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcProgramContainer':
            obj_ = AutoProcProgramContainer()
            obj_.build(child_)
            self.setAutoProcProgramContainer(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcContainer


class AutoProcIntegration(object):
    def __init__(self, anomalous=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, beamVectorZ=None, beamVectorY=None, beamVectorX=None, rotationAxisZ=None, rotationAxisY=None, rotationAxisX=None, refinedYbeam=None, refinedXbeam=None, refinedDetectorDistance=None, endImageNumber=None, startImageNumber=None, autoProcIntegrationId=None):
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
        if endImageNumber is None:
            self._endImageNumber = None
        else:
            self._endImageNumber = int(endImageNumber)
        if refinedDetectorDistance is None:
            self._refinedDetectorDistance = None
        else:
            self._refinedDetectorDistance = float(refinedDetectorDistance)
        if refinedXbeam is None:
            self._refinedXbeam = None
        else:
            self._refinedXbeam = float(refinedXbeam)
        if refinedYbeam is None:
            self._refinedYbeam = None
        else:
            self._refinedYbeam = float(refinedYbeam)
        if rotationAxisX is None:
            self._rotationAxisX = None
        else:
            self._rotationAxisX = float(rotationAxisX)
        if rotationAxisY is None:
            self._rotationAxisY = None
        else:
            self._rotationAxisY = float(rotationAxisY)
        if rotationAxisZ is None:
            self._rotationAxisZ = None
        else:
            self._rotationAxisZ = float(rotationAxisZ)
        if beamVectorX is None:
            self._beamVectorX = None
        else:
            self._beamVectorX = float(beamVectorX)
        if beamVectorY is None:
            self._beamVectorY = None
        else:
            self._beamVectorY = float(beamVectorY)
        if beamVectorZ is None:
            self._beamVectorZ = None
        else:
            self._beamVectorZ = float(beamVectorZ)
        if cell_a is None:
            self._cell_a = None
        else:
            self._cell_a = float(cell_a)
        if cell_b is None:
            self._cell_b = None
        else:
            self._cell_b = float(cell_b)
        if cell_c is None:
            self._cell_c = None
        else:
            self._cell_c = float(cell_c)
        if cell_alpha is None:
            self._cell_alpha = None
        else:
            self._cell_alpha = float(cell_alpha)
        if cell_beta is None:
            self._cell_beta = None
        else:
            self._cell_beta = float(cell_beta)
        if cell_gamma is None:
            self._cell_gamma = None
        else:
            self._cell_gamma = float(cell_gamma)
        self._anomalous = bool(anomalous)
    # Methods and properties for the 'autoProcIntegrationId' attribute
    def getAutoProcIntegrationId(self): return self._autoProcIntegrationId
    def setAutoProcIntegrationId(self, autoProcIntegrationId):
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
    def delAutoProcIntegrationId(self): self._autoProcIntegrationId = None
    autoProcIntegrationId = property(getAutoProcIntegrationId, setAutoProcIntegrationId, delAutoProcIntegrationId, "Property for autoProcIntegrationId")
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
    def delStartImageNumber(self): self._startImageNumber = None
    startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
    # Methods and properties for the 'endImageNumber' attribute
    def getEndImageNumber(self): return self._endImageNumber
    def setEndImageNumber(self, endImageNumber):
        if endImageNumber is None:
            self._endImageNumber = None
        else:
            self._endImageNumber = int(endImageNumber)
    def delEndImageNumber(self): self._endImageNumber = None
    endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
    # Methods and properties for the 'refinedDetectorDistance' attribute
    def getRefinedDetectorDistance(self): return self._refinedDetectorDistance
    def setRefinedDetectorDistance(self, refinedDetectorDistance):
        if refinedDetectorDistance is None:
            self._refinedDetectorDistance = None
        else:
            self._refinedDetectorDistance = float(refinedDetectorDistance)
    def delRefinedDetectorDistance(self): self._refinedDetectorDistance = None
    refinedDetectorDistance = property(getRefinedDetectorDistance, setRefinedDetectorDistance, delRefinedDetectorDistance, "Property for refinedDetectorDistance")
    # Methods and properties for the 'refinedXbeam' attribute
    def getRefinedXbeam(self): return self._refinedXbeam
    def setRefinedXbeam(self, refinedXbeam):
        if refinedXbeam is None:
            self._refinedXbeam = None
        else:
            self._refinedXbeam = float(refinedXbeam)
    def delRefinedXbeam(self): self._refinedXbeam = None
    refinedXbeam = property(getRefinedXbeam, setRefinedXbeam, delRefinedXbeam, "Property for refinedXbeam")
    # Methods and properties for the 'refinedYbeam' attribute
    def getRefinedYbeam(self): return self._refinedYbeam
    def setRefinedYbeam(self, refinedYbeam):
        if refinedYbeam is None:
            self._refinedYbeam = None
        else:
            self._refinedYbeam = float(refinedYbeam)
    def delRefinedYbeam(self): self._refinedYbeam = None
    refinedYbeam = property(getRefinedYbeam, setRefinedYbeam, delRefinedYbeam, "Property for refinedYbeam")
    # Methods and properties for the 'rotationAxisX' attribute
    def getRotationAxisX(self): return self._rotationAxisX
    def setRotationAxisX(self, rotationAxisX):
        if rotationAxisX is None:
            self._rotationAxisX = None
        else:
            self._rotationAxisX = float(rotationAxisX)
    def delRotationAxisX(self): self._rotationAxisX = None
    rotationAxisX = property(getRotationAxisX, setRotationAxisX, delRotationAxisX, "Property for rotationAxisX")
    # Methods and properties for the 'rotationAxisY' attribute
    def getRotationAxisY(self): return self._rotationAxisY
    def setRotationAxisY(self, rotationAxisY):
        if rotationAxisY is None:
            self._rotationAxisY = None
        else:
            self._rotationAxisY = float(rotationAxisY)
    def delRotationAxisY(self): self._rotationAxisY = None
    rotationAxisY = property(getRotationAxisY, setRotationAxisY, delRotationAxisY, "Property for rotationAxisY")
    # Methods and properties for the 'rotationAxisZ' attribute
    def getRotationAxisZ(self): return self._rotationAxisZ
    def setRotationAxisZ(self, rotationAxisZ):
        if rotationAxisZ is None:
            self._rotationAxisZ = None
        else:
            self._rotationAxisZ = float(rotationAxisZ)
    def delRotationAxisZ(self): self._rotationAxisZ = None
    rotationAxisZ = property(getRotationAxisZ, setRotationAxisZ, delRotationAxisZ, "Property for rotationAxisZ")
    # Methods and properties for the 'beamVectorX' attribute
    def getBeamVectorX(self): return self._beamVectorX
    def setBeamVectorX(self, beamVectorX):
        if beamVectorX is None:
            self._beamVectorX = None
        else:
            self._beamVectorX = float(beamVectorX)
    def delBeamVectorX(self): self._beamVectorX = None
    beamVectorX = property(getBeamVectorX, setBeamVectorX, delBeamVectorX, "Property for beamVectorX")
    # Methods and properties for the 'beamVectorY' attribute
    def getBeamVectorY(self): return self._beamVectorY
    def setBeamVectorY(self, beamVectorY):
        if beamVectorY is None:
            self._beamVectorY = None
        else:
            self._beamVectorY = float(beamVectorY)
    def delBeamVectorY(self): self._beamVectorY = None
    beamVectorY = property(getBeamVectorY, setBeamVectorY, delBeamVectorY, "Property for beamVectorY")
    # Methods and properties for the 'beamVectorZ' attribute
    def getBeamVectorZ(self): return self._beamVectorZ
    def setBeamVectorZ(self, beamVectorZ):
        if beamVectorZ is None:
            self._beamVectorZ = None
        else:
            self._beamVectorZ = float(beamVectorZ)
    def delBeamVectorZ(self): self._beamVectorZ = None
    beamVectorZ = property(getBeamVectorZ, setBeamVectorZ, delBeamVectorZ, "Property for beamVectorZ")
    # Methods and properties for the 'cell_a' attribute
    def getCell_a(self): return self._cell_a
    def setCell_a(self, cell_a):
        if cell_a is None:
            self._cell_a = None
        else:
            self._cell_a = float(cell_a)
    def delCell_a(self): self._cell_a = None
    cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
    # Methods and properties for the 'cell_b' attribute
    def getCell_b(self): return self._cell_b
    def setCell_b(self, cell_b):
        if cell_b is None:
            self._cell_b = None
        else:
            self._cell_b = float(cell_b)
    def delCell_b(self): self._cell_b = None
    cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
    # Methods and properties for the 'cell_c' attribute
    def getCell_c(self): return self._cell_c
    def setCell_c(self, cell_c):
        if cell_c is None:
            self._cell_c = None
        else:
            self._cell_c = float(cell_c)
    def delCell_c(self): self._cell_c = None
    cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
    # Methods and properties for the 'cell_alpha' attribute
    def getCell_alpha(self): return self._cell_alpha
    def setCell_alpha(self, cell_alpha):
        if cell_alpha is None:
            self._cell_alpha = None
        else:
            self._cell_alpha = float(cell_alpha)
    def delCell_alpha(self): self._cell_alpha = None
    cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
    # Methods and properties for the 'cell_beta' attribute
    def getCell_beta(self): return self._cell_beta
    def setCell_beta(self, cell_beta):
        if cell_beta is None:
            self._cell_beta = None
        else:
            self._cell_beta = float(cell_beta)
    def delCell_beta(self): self._cell_beta = None
    cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
    # Methods and properties for the 'cell_gamma' attribute
    def getCell_gamma(self): return self._cell_gamma
    def setCell_gamma(self, cell_gamma):
        if cell_gamma is None:
            self._cell_gamma = None
        else:
            self._cell_gamma = float(cell_gamma)
    def delCell_gamma(self): self._cell_gamma = None
    cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        self._anomalous = bool(anomalous)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    def export(self, outfile, level, name_='AutoProcIntegration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcIntegration'):
        pass
        if self._autoProcIntegrationId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcIntegrationId>%d</autoProcIntegrationId>\n' % self._autoProcIntegrationId))
        if self._startImageNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self._startImageNumber))
        else:
            warnEmptyAttribute("startImageNumber", "integer")
        if self._endImageNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<endImageNumber>%d</endImageNumber>\n' % self._endImageNumber))
        else:
            warnEmptyAttribute("endImageNumber", "integer")
        if self._refinedDetectorDistance is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedDetectorDistance>%e</refinedDetectorDistance>\n' % self._refinedDetectorDistance))
        else:
            warnEmptyAttribute("refinedDetectorDistance", "float")
        if self._refinedXbeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedXbeam>%e</refinedXbeam>\n' % self._refinedXbeam))
        else:
            warnEmptyAttribute("refinedXbeam", "float")
        if self._refinedYbeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<refinedYbeam>%e</refinedYbeam>\n' % self._refinedYbeam))
        else:
            warnEmptyAttribute("refinedYbeam", "float")
        if self._rotationAxisX is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rotationAxisX>%e</rotationAxisX>\n' % self._rotationAxisX))
        else:
            warnEmptyAttribute("rotationAxisX", "float")
        if self._rotationAxisY is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rotationAxisY>%e</rotationAxisY>\n' % self._rotationAxisY))
        else:
            warnEmptyAttribute("rotationAxisY", "float")
        if self._rotationAxisZ is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rotationAxisZ>%e</rotationAxisZ>\n' % self._rotationAxisZ))
        else:
            warnEmptyAttribute("rotationAxisZ", "float")
        if self._beamVectorX is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamVectorX>%e</beamVectorX>\n' % self._beamVectorX))
        else:
            warnEmptyAttribute("beamVectorX", "float")
        if self._beamVectorY is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamVectorY>%e</beamVectorY>\n' % self._beamVectorY))
        else:
            warnEmptyAttribute("beamVectorY", "float")
        if self._beamVectorZ is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamVectorZ>%e</beamVectorZ>\n' % self._beamVectorZ))
        else:
            warnEmptyAttribute("beamVectorZ", "float")
        if self._cell_a is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_a>%e</cell_a>\n' % self._cell_a))
        else:
            warnEmptyAttribute("cell_a", "float")
        if self._cell_b is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_b>%e</cell_b>\n' % self._cell_b))
        else:
            warnEmptyAttribute("cell_b", "float")
        if self._cell_c is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_c>%e</cell_c>\n' % self._cell_c))
        else:
            warnEmptyAttribute("cell_c", "float")
        if self._cell_alpha is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_alpha>%e</cell_alpha>\n' % self._cell_alpha))
        else:
            warnEmptyAttribute("cell_alpha", "float")
        if self._cell_beta is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_beta>%e</cell_beta>\n' % self._cell_beta))
        else:
            warnEmptyAttribute("cell_beta", "float")
        if self._cell_gamma is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<cell_gamma>%e</cell_gamma>\n' % self._cell_gamma))
        else:
            warnEmptyAttribute("cell_gamma", "float")
        if self._anomalous is not None:
            showIndent(outfile, level)
            if self._anomalous:
                outfile.write(unicode('<anomalous>true</anomalous>\n'))
            else:
                outfile.write(unicode('<anomalous>false</anomalous>\n'))
        else:
            warnEmptyAttribute("anomalous", "boolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcIntegrationId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcIntegrationId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startImageNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._startImageNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endImageNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._endImageNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedDetectorDistance':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._refinedDetectorDistance = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedXbeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._refinedXbeam = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedYbeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._refinedYbeam = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisX':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rotationAxisX = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisY':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rotationAxisY = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisZ':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rotationAxisZ = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamVectorX':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamVectorX = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamVectorY':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamVectorY = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamVectorZ':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamVectorZ = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_a':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_a = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_b':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_b = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_c':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_c = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_alpha':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_alpha = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_beta':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_beta = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_gamma':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._cell_gamma = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('True', 'true', '1'):
                    ival_ = True
                elif sval_ in ('False', 'false', '0'):
                    ival_ = False
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self._anomalous = ival_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcIntegration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcIntegration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcIntegration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcIntegration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcIntegration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcIntegration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcIntegration


class AutoProcIntegrationContainer(object):
    def __init__(self, AutoProcIntegration=None, Image=None):
        if Image is None:
            self._Image = None
        elif Image.__class__.__name__ == "Image":
            self._Image = Image
        else:
            strMessage = "ERROR! AutoProcIntegrationContainer constructor argument 'Image' is not Image but %s" % self._Image.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcIntegration is None:
            self._AutoProcIntegration = None
        elif AutoProcIntegration.__class__.__name__ == "AutoProcIntegration":
            self._AutoProcIntegration = AutoProcIntegration
        else:
            strMessage = "ERROR! AutoProcIntegrationContainer constructor argument 'AutoProcIntegration' is not AutoProcIntegration but %s" % self._AutoProcIntegration.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'Image' attribute
    def getImage(self): return self._Image
    def setImage(self, Image):
        if Image is None:
            self._Image = None
        elif Image.__class__.__name__ == "Image":
            self._Image = Image
        else:
            strMessage = "ERROR! AutoProcIntegrationContainer.setImage argument is not Image but %s" % Image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._Image = None
    Image = property(getImage, setImage, delImage, "Property for Image")
    # Methods and properties for the 'AutoProcIntegration' attribute
    def getAutoProcIntegration(self): return self._AutoProcIntegration
    def setAutoProcIntegration(self, AutoProcIntegration):
        if AutoProcIntegration is None:
            self._AutoProcIntegration = None
        elif AutoProcIntegration.__class__.__name__ == "AutoProcIntegration":
            self._AutoProcIntegration = AutoProcIntegration
        else:
            strMessage = "ERROR! AutoProcIntegrationContainer.setAutoProcIntegration argument is not AutoProcIntegration but %s" % AutoProcIntegration.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcIntegration(self): self._AutoProcIntegration = None
    AutoProcIntegration = property(getAutoProcIntegration, setAutoProcIntegration, delAutoProcIntegration, "Property for AutoProcIntegration")
    def export(self, outfile, level, name_='AutoProcIntegrationContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcIntegrationContainer'):
        pass
        if self._Image is not None:
            self.Image.export(outfile, level, name_='Image')
        else:
            warnEmptyAttribute("Image", "Image")
        if self._AutoProcIntegration is not None:
            self.AutoProcIntegration.export(outfile, level, name_='AutoProcIntegration')
        else:
            warnEmptyAttribute("AutoProcIntegration", "AutoProcIntegration")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Image':
            obj_ = Image()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcIntegration':
            obj_ = AutoProcIntegration()
            obj_.build(child_)
            self.setAutoProcIntegration(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcIntegrationContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcIntegrationContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcIntegrationContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcIntegrationContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcIntegrationContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcIntegrationContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcIntegrationContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcIntegrationContainer


class AutoProcProgram(object):
    def __init__(self, processingEnvironment=None, processingEndTime=None, processingStartTime=None, processingMessage=None, processingStatus=None, processingPrograms=None, processingCommandLine=None, autoProcProgramId=None):
        if autoProcProgramId is None:
            self._autoProcProgramId = None
        else:
            self._autoProcProgramId = int(autoProcProgramId)
        self._processingCommandLine = str(processingCommandLine)
        self._processingPrograms = str(processingPrograms)
        self._processingStatus = bool(processingStatus)
        self._processingMessage = str(processingMessage)
        self._processingStartTime = str(processingStartTime)
        self._processingEndTime = str(processingEndTime)
        self._processingEnvironment = str(processingEnvironment)
    # Methods and properties for the 'autoProcProgramId' attribute
    def getAutoProcProgramId(self): return self._autoProcProgramId
    def setAutoProcProgramId(self, autoProcProgramId):
        if autoProcProgramId is None:
            self._autoProcProgramId = None
        else:
            self._autoProcProgramId = int(autoProcProgramId)
    def delAutoProcProgramId(self): self._autoProcProgramId = None
    autoProcProgramId = property(getAutoProcProgramId, setAutoProcProgramId, delAutoProcProgramId, "Property for autoProcProgramId")
    # Methods and properties for the 'processingCommandLine' attribute
    def getProcessingCommandLine(self): return self._processingCommandLine
    def setProcessingCommandLine(self, processingCommandLine):
        self._processingCommandLine = str(processingCommandLine)
    def delProcessingCommandLine(self): self._processingCommandLine = None
    processingCommandLine = property(getProcessingCommandLine, setProcessingCommandLine, delProcessingCommandLine, "Property for processingCommandLine")
    # Methods and properties for the 'processingPrograms' attribute
    def getProcessingPrograms(self): return self._processingPrograms
    def setProcessingPrograms(self, processingPrograms):
        self._processingPrograms = str(processingPrograms)
    def delProcessingPrograms(self): self._processingPrograms = None
    processingPrograms = property(getProcessingPrograms, setProcessingPrograms, delProcessingPrograms, "Property for processingPrograms")
    # Methods and properties for the 'processingStatus' attribute
    def getProcessingStatus(self): return self._processingStatus
    def setProcessingStatus(self, processingStatus):
        self._processingStatus = bool(processingStatus)
    def delProcessingStatus(self): self._processingStatus = None
    processingStatus = property(getProcessingStatus, setProcessingStatus, delProcessingStatus, "Property for processingStatus")
    # Methods and properties for the 'processingMessage' attribute
    def getProcessingMessage(self): return self._processingMessage
    def setProcessingMessage(self, processingMessage):
        self._processingMessage = str(processingMessage)
    def delProcessingMessage(self): self._processingMessage = None
    processingMessage = property(getProcessingMessage, setProcessingMessage, delProcessingMessage, "Property for processingMessage")
    # Methods and properties for the 'processingStartTime' attribute
    def getProcessingStartTime(self): return self._processingStartTime
    def setProcessingStartTime(self, processingStartTime):
        self._processingStartTime = str(processingStartTime)
    def delProcessingStartTime(self): self._processingStartTime = None
    processingStartTime = property(getProcessingStartTime, setProcessingStartTime, delProcessingStartTime, "Property for processingStartTime")
    # Methods and properties for the 'processingEndTime' attribute
    def getProcessingEndTime(self): return self._processingEndTime
    def setProcessingEndTime(self, processingEndTime):
        self._processingEndTime = str(processingEndTime)
    def delProcessingEndTime(self): self._processingEndTime = None
    processingEndTime = property(getProcessingEndTime, setProcessingEndTime, delProcessingEndTime, "Property for processingEndTime")
    # Methods and properties for the 'processingEnvironment' attribute
    def getProcessingEnvironment(self): return self._processingEnvironment
    def setProcessingEnvironment(self, processingEnvironment):
        self._processingEnvironment = str(processingEnvironment)
    def delProcessingEnvironment(self): self._processingEnvironment = None
    processingEnvironment = property(getProcessingEnvironment, setProcessingEnvironment, delProcessingEnvironment, "Property for processingEnvironment")
    def export(self, outfile, level, name_='AutoProcProgram'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcProgram'):
        pass
        if self._autoProcProgramId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcProgramId>%d</autoProcProgramId>\n' % self._autoProcProgramId))
        if self._processingCommandLine is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingCommandLine>%s</processingCommandLine>\n' % self._processingCommandLine))
        else:
            warnEmptyAttribute("processingCommandLine", "string")
        if self._processingPrograms is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingPrograms>%s</processingPrograms>\n' % self._processingPrograms))
        else:
            warnEmptyAttribute("processingPrograms", "string")
        if self._processingStatus is not None:
            showIndent(outfile, level)
            if self._processingStatus:
                outfile.write(unicode('<processingStatus>true</processingStatus>\n'))
            else:
                outfile.write(unicode('<processingStatus>false</processingStatus>\n'))
        else:
            warnEmptyAttribute("processingStatus", "boolean")
        if self._processingMessage is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingMessage>%s</processingMessage>\n' % self._processingMessage))
        else:
            warnEmptyAttribute("processingMessage", "string")
        if self._processingStartTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingStartTime>%s</processingStartTime>\n' % self._processingStartTime))
        else:
            warnEmptyAttribute("processingStartTime", "string")
        if self._processingEndTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingEndTime>%s</processingEndTime>\n' % self._processingEndTime))
        else:
            warnEmptyAttribute("processingEndTime", "string")
        if self._processingEnvironment is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<processingEnvironment>%s</processingEnvironment>\n' % self._processingEnvironment))
        else:
            warnEmptyAttribute("processingEnvironment", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcProgramId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcProgramId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingCommandLine':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingCommandLine = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingPrograms':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingPrograms = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingStatus':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('True', 'true', '1'):
                    ival_ = True
                elif sval_ in ('False', 'false', '0'):
                    ival_ = False
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self._processingStatus = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingMessage':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingMessage = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingStartTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingStartTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingEndTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingEndTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processingEnvironment':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._processingEnvironment = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcProgram" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcProgram' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcProgram is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcProgram.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcProgram()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcProgram" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcProgram()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcProgram


class AutoProcProgramAttachment(object):
    def __init__(self, recordTimeStamp=None, filePath=None, fileName=None, fileType=None, autoProcProgramAttachmentId=None):
        if autoProcProgramAttachmentId is None:
            self._autoProcProgramAttachmentId = None
        else:
            self._autoProcProgramAttachmentId = int(autoProcProgramAttachmentId)
        self._fileType = str(fileType)
        self._fileName = str(fileName)
        self._filePath = str(filePath)
        self._recordTimeStamp = str(recordTimeStamp)
    # Methods and properties for the 'autoProcProgramAttachmentId' attribute
    def getAutoProcProgramAttachmentId(self): return self._autoProcProgramAttachmentId
    def setAutoProcProgramAttachmentId(self, autoProcProgramAttachmentId):
        if autoProcProgramAttachmentId is None:
            self._autoProcProgramAttachmentId = None
        else:
            self._autoProcProgramAttachmentId = int(autoProcProgramAttachmentId)
    def delAutoProcProgramAttachmentId(self): self._autoProcProgramAttachmentId = None
    autoProcProgramAttachmentId = property(getAutoProcProgramAttachmentId, setAutoProcProgramAttachmentId, delAutoProcProgramAttachmentId, "Property for autoProcProgramAttachmentId")
    # Methods and properties for the 'fileType' attribute
    def getFileType(self): return self._fileType
    def setFileType(self, fileType):
        self._fileType = str(fileType)
    def delFileType(self): self._fileType = None
    fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
    # Methods and properties for the 'fileName' attribute
    def getFileName(self): return self._fileName
    def setFileName(self, fileName):
        self._fileName = str(fileName)
    def delFileName(self): self._fileName = None
    fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
    # Methods and properties for the 'filePath' attribute
    def getFilePath(self): return self._filePath
    def setFilePath(self, filePath):
        self._filePath = str(filePath)
    def delFilePath(self): self._filePath = None
    filePath = property(getFilePath, setFilePath, delFilePath, "Property for filePath")
    # Methods and properties for the 'recordTimeStamp' attribute
    def getRecordTimeStamp(self): return self._recordTimeStamp
    def setRecordTimeStamp(self, recordTimeStamp):
        self._recordTimeStamp = str(recordTimeStamp)
    def delRecordTimeStamp(self): self._recordTimeStamp = None
    recordTimeStamp = property(getRecordTimeStamp, setRecordTimeStamp, delRecordTimeStamp, "Property for recordTimeStamp")
    def export(self, outfile, level, name_='AutoProcProgramAttachment'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcProgramAttachment'):
        pass
        if self._autoProcProgramAttachmentId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcProgramAttachmentId>%d</autoProcProgramAttachmentId>\n' % self._autoProcProgramAttachmentId))
        if self._fileType is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<fileType>%s</fileType>\n' % self._fileType))
        else:
            warnEmptyAttribute("fileType", "string")
        if self._fileName is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<fileName>%s</fileName>\n' % self._fileName))
        else:
            warnEmptyAttribute("fileName", "string")
        if self._filePath is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<filePath>%s</filePath>\n' % self._filePath))
        else:
            warnEmptyAttribute("filePath", "string")
        if self._recordTimeStamp is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<recordTimeStamp>%s</recordTimeStamp>\n' % self._recordTimeStamp))
        else:
            warnEmptyAttribute("recordTimeStamp", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcProgramAttachmentId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcProgramAttachmentId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileType':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._fileType = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileName':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._fileName = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePath':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._filePath = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'recordTimeStamp':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._recordTimeStamp = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcProgramAttachment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcProgramAttachment' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcProgramAttachment is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcProgramAttachment.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcProgramAttachment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcProgramAttachment" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcProgramAttachment()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcProgramAttachment


class AutoProcProgramContainer(object):
    def __init__(self, AutoProcProgramAttachment=None, AutoProcProgram=None):
        if AutoProcProgram is None:
            self._AutoProcProgram = None
        elif AutoProcProgram.__class__.__name__ == "AutoProcProgram":
            self._AutoProcProgram = AutoProcProgram
        else:
            strMessage = "ERROR! AutoProcProgramContainer constructor argument 'AutoProcProgram' is not AutoProcProgram but %s" % self._AutoProcProgram.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcProgramAttachment is None:
            self._AutoProcProgramAttachment = []
        elif AutoProcProgramAttachment.__class__.__name__ == "list":
            self._AutoProcProgramAttachment = AutoProcProgramAttachment
        else:
            strMessage = "ERROR! AutoProcProgramContainer constructor argument 'AutoProcProgramAttachment' is not list but %s" % self._AutoProcProgramAttachment.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'AutoProcProgram' attribute
    def getAutoProcProgram(self): return self._AutoProcProgram
    def setAutoProcProgram(self, AutoProcProgram):
        if AutoProcProgram is None:
            self._AutoProcProgram = None
        elif AutoProcProgram.__class__.__name__ == "AutoProcProgram":
            self._AutoProcProgram = AutoProcProgram
        else:
            strMessage = "ERROR! AutoProcProgramContainer.setAutoProcProgram argument is not AutoProcProgram but %s" % AutoProcProgram.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcProgram(self): self._AutoProcProgram = None
    AutoProcProgram = property(getAutoProcProgram, setAutoProcProgram, delAutoProcProgram, "Property for AutoProcProgram")
    # Methods and properties for the 'AutoProcProgramAttachment' attribute
    def getAutoProcProgramAttachment(self): return self._AutoProcProgramAttachment
    def setAutoProcProgramAttachment(self, AutoProcProgramAttachment):
        if AutoProcProgramAttachment is None:
            self._AutoProcProgramAttachment = []
        elif AutoProcProgramAttachment.__class__.__name__ == "list":
            self._AutoProcProgramAttachment = AutoProcProgramAttachment
        else:
            strMessage = "ERROR! AutoProcProgramContainer.setAutoProcProgramAttachment argument is not list but %s" % AutoProcProgramAttachment.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcProgramAttachment(self): self._AutoProcProgramAttachment = None
    AutoProcProgramAttachment = property(getAutoProcProgramAttachment, setAutoProcProgramAttachment, delAutoProcProgramAttachment, "Property for AutoProcProgramAttachment")
    def addAutoProcProgramAttachment(self, value):
        if value is None:
            strMessage = "ERROR! AutoProcProgramContainer.addAutoProcProgramAttachment argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "AutoProcProgramAttachment":
            self._AutoProcProgramAttachment.append(value)
        else:
            strMessage = "ERROR! AutoProcProgramContainer.addAutoProcProgramAttachment argument is not AutoProcProgramAttachment but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAutoProcProgramAttachment(self, index, value):
        if index is None:
            strMessage = "ERROR! AutoProcProgramContainer.insertAutoProcProgramAttachment argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! AutoProcProgramContainer.insertAutoProcProgramAttachment argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "AutoProcProgramAttachment":
            self._AutoProcProgramAttachment[index] = value
        else:
            strMessage = "ERROR! AutoProcProgramContainer.addAutoProcProgramAttachment argument is not AutoProcProgramAttachment but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='AutoProcProgramContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcProgramContainer'):
        pass
        if self._AutoProcProgram is not None:
            self.AutoProcProgram.export(outfile, level, name_='AutoProcProgram')
        else:
            warnEmptyAttribute("AutoProcProgram", "AutoProcProgram")
        for AutoProcProgramAttachment_ in self.getAutoProcProgramAttachment():
            AutoProcProgramAttachment_.export(outfile, level, name_='AutoProcProgramAttachment')
        if self.getAutoProcProgramAttachment() == []:
            warnEmptyAttribute("AutoProcProgramAttachment", "AutoProcProgramAttachment")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcProgram':
            obj_ = AutoProcProgram()
            obj_.build(child_)
            self.setAutoProcProgram(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcProgramAttachment':
            obj_ = AutoProcProgramAttachment()
            obj_.build(child_)
            self.AutoProcProgramAttachment.append(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcProgramContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcProgramContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcProgramContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcProgramContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcProgramContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcProgramContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcProgramContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcProgramContainer


class AutoProcScaling(object):
    def __init__(self, recordTimeStamp=None, autoProcScalingId=None):
        if autoProcScalingId is None:
            self._autoProcScalingId = None
        else:
            self._autoProcScalingId = int(autoProcScalingId)
        self._recordTimeStamp = str(recordTimeStamp)
    # Methods and properties for the 'autoProcScalingId' attribute
    def getAutoProcScalingId(self): return self._autoProcScalingId
    def setAutoProcScalingId(self, autoProcScalingId):
        if autoProcScalingId is None:
            self._autoProcScalingId = None
        else:
            self._autoProcScalingId = int(autoProcScalingId)
    def delAutoProcScalingId(self): self._autoProcScalingId = None
    autoProcScalingId = property(getAutoProcScalingId, setAutoProcScalingId, delAutoProcScalingId, "Property for autoProcScalingId")
    # Methods and properties for the 'recordTimeStamp' attribute
    def getRecordTimeStamp(self): return self._recordTimeStamp
    def setRecordTimeStamp(self, recordTimeStamp):
        self._recordTimeStamp = str(recordTimeStamp)
    def delRecordTimeStamp(self): self._recordTimeStamp = None
    recordTimeStamp = property(getRecordTimeStamp, setRecordTimeStamp, delRecordTimeStamp, "Property for recordTimeStamp")
    def export(self, outfile, level, name_='AutoProcScaling'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcScaling'):
        pass
        if self._autoProcScalingId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcScalingId>%d</autoProcScalingId>\n' % self._autoProcScalingId))
        if self._recordTimeStamp is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<recordTimeStamp>%s</recordTimeStamp>\n' % self._recordTimeStamp))
        else:
            warnEmptyAttribute("recordTimeStamp", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcScalingId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcScalingId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'recordTimeStamp':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._recordTimeStamp = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcScaling" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcScaling' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcScaling is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcScaling.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcScaling()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcScaling" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcScaling()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcScaling


class AutoProcScalingStatistics(object):
    def __init__(self, ccHalf=None, anomalous=None, recordTimeStamp=None, anomalousMultiplicity=None, anomalousCompleteness=None, multiplicity=None, completeness=None, meanIOverSigI=None, ntotalUniqueObservations=None, nTotalObservations=None, fractionalPartialBias=None, rpimAllIplusIminus=None, rpimWithinIplusIminus=None, rmeasAllIplusIminus=None, rmeasWithinIplusIminus=None, rMerge=None, resolutionLimitHigh=None, resolutionLimitLow=None, comments=None, scalingStatisticsType=None, autoProcScalingStatisticsId=None):
        if autoProcScalingStatisticsId is None:
            self._autoProcScalingStatisticsId = None
        else:
            self._autoProcScalingStatisticsId = int(autoProcScalingStatisticsId)
        self._scalingStatisticsType = str(scalingStatisticsType)
        self._comments = str(comments)
        if resolutionLimitLow is None:
            self._resolutionLimitLow = None
        else:
            self._resolutionLimitLow = float(resolutionLimitLow)
        if resolutionLimitHigh is None:
            self._resolutionLimitHigh = None
        else:
            self._resolutionLimitHigh = float(resolutionLimitHigh)
        if rMerge is None:
            self._rMerge = None
        else:
            self._rMerge = float(rMerge)
        if rmeasWithinIplusIminus is None:
            self._rmeasWithinIplusIminus = None
        else:
            self._rmeasWithinIplusIminus = float(rmeasWithinIplusIminus)
        if rmeasAllIplusIminus is None:
            self._rmeasAllIplusIminus = None
        else:
            self._rmeasAllIplusIminus = float(rmeasAllIplusIminus)
        if rpimWithinIplusIminus is None:
            self._rpimWithinIplusIminus = None
        else:
            self._rpimWithinIplusIminus = float(rpimWithinIplusIminus)
        if rpimAllIplusIminus is None:
            self._rpimAllIplusIminus = None
        else:
            self._rpimAllIplusIminus = float(rpimAllIplusIminus)
        if fractionalPartialBias is None:
            self._fractionalPartialBias = None
        else:
            self._fractionalPartialBias = float(fractionalPartialBias)
        if nTotalObservations is None:
            self._nTotalObservations = None
        else:
            self._nTotalObservations = int(nTotalObservations)
        if ntotalUniqueObservations is None:
            self._ntotalUniqueObservations = None
        else:
            self._ntotalUniqueObservations = int(ntotalUniqueObservations)
        if meanIOverSigI is None:
            self._meanIOverSigI = None
        else:
            self._meanIOverSigI = float(meanIOverSigI)
        if completeness is None:
            self._completeness = None
        else:
            self._completeness = float(completeness)
        if multiplicity is None:
            self._multiplicity = None
        else:
            self._multiplicity = float(multiplicity)
        if anomalousCompleteness is None:
            self._anomalousCompleteness = None
        else:
            self._anomalousCompleteness = float(anomalousCompleteness)
        if anomalousMultiplicity is None:
            self._anomalousMultiplicity = None
        else:
            self._anomalousMultiplicity = float(anomalousMultiplicity)
        self._recordTimeStamp = str(recordTimeStamp)
        self._anomalous = bool(anomalous)
        if ccHalf is None:
            self._ccHalf = None
        else:
            self._ccHalf = float(ccHalf)
    # Methods and properties for the 'autoProcScalingStatisticsId' attribute
    def getAutoProcScalingStatisticsId(self): return self._autoProcScalingStatisticsId
    def setAutoProcScalingStatisticsId(self, autoProcScalingStatisticsId):
        if autoProcScalingStatisticsId is None:
            self._autoProcScalingStatisticsId = None
        else:
            self._autoProcScalingStatisticsId = int(autoProcScalingStatisticsId)
    def delAutoProcScalingStatisticsId(self): self._autoProcScalingStatisticsId = None
    autoProcScalingStatisticsId = property(getAutoProcScalingStatisticsId, setAutoProcScalingStatisticsId, delAutoProcScalingStatisticsId, "Property for autoProcScalingStatisticsId")
    # Methods and properties for the 'scalingStatisticsType' attribute
    def getScalingStatisticsType(self): return self._scalingStatisticsType
    def setScalingStatisticsType(self, scalingStatisticsType):
        self._scalingStatisticsType = str(scalingStatisticsType)
    def delScalingStatisticsType(self): self._scalingStatisticsType = None
    scalingStatisticsType = property(getScalingStatisticsType, setScalingStatisticsType, delScalingStatisticsType, "Property for scalingStatisticsType")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        self._comments = str(comments)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'resolutionLimitLow' attribute
    def getResolutionLimitLow(self): return self._resolutionLimitLow
    def setResolutionLimitLow(self, resolutionLimitLow):
        if resolutionLimitLow is None:
            self._resolutionLimitLow = None
        else:
            self._resolutionLimitLow = float(resolutionLimitLow)
    def delResolutionLimitLow(self): self._resolutionLimitLow = None
    resolutionLimitLow = property(getResolutionLimitLow, setResolutionLimitLow, delResolutionLimitLow, "Property for resolutionLimitLow")
    # Methods and properties for the 'resolutionLimitHigh' attribute
    def getResolutionLimitHigh(self): return self._resolutionLimitHigh
    def setResolutionLimitHigh(self, resolutionLimitHigh):
        if resolutionLimitHigh is None:
            self._resolutionLimitHigh = None
        else:
            self._resolutionLimitHigh = float(resolutionLimitHigh)
    def delResolutionLimitHigh(self): self._resolutionLimitHigh = None
    resolutionLimitHigh = property(getResolutionLimitHigh, setResolutionLimitHigh, delResolutionLimitHigh, "Property for resolutionLimitHigh")
    # Methods and properties for the 'rMerge' attribute
    def getRMerge(self): return self._rMerge
    def setRMerge(self, rMerge):
        if rMerge is None:
            self._rMerge = None
        else:
            self._rMerge = float(rMerge)
    def delRMerge(self): self._rMerge = None
    rMerge = property(getRMerge, setRMerge, delRMerge, "Property for rMerge")
    # Methods and properties for the 'rmeasWithinIplusIminus' attribute
    def getRmeasWithinIplusIminus(self): return self._rmeasWithinIplusIminus
    def setRmeasWithinIplusIminus(self, rmeasWithinIplusIminus):
        if rmeasWithinIplusIminus is None:
            self._rmeasWithinIplusIminus = None
        else:
            self._rmeasWithinIplusIminus = float(rmeasWithinIplusIminus)
    def delRmeasWithinIplusIminus(self): self._rmeasWithinIplusIminus = None
    rmeasWithinIplusIminus = property(getRmeasWithinIplusIminus, setRmeasWithinIplusIminus, delRmeasWithinIplusIminus, "Property for rmeasWithinIplusIminus")
    # Methods and properties for the 'rmeasAllIplusIminus' attribute
    def getRmeasAllIplusIminus(self): return self._rmeasAllIplusIminus
    def setRmeasAllIplusIminus(self, rmeasAllIplusIminus):
        if rmeasAllIplusIminus is None:
            self._rmeasAllIplusIminus = None
        else:
            self._rmeasAllIplusIminus = float(rmeasAllIplusIminus)
    def delRmeasAllIplusIminus(self): self._rmeasAllIplusIminus = None
    rmeasAllIplusIminus = property(getRmeasAllIplusIminus, setRmeasAllIplusIminus, delRmeasAllIplusIminus, "Property for rmeasAllIplusIminus")
    # Methods and properties for the 'rpimWithinIplusIminus' attribute
    def getRpimWithinIplusIminus(self): return self._rpimWithinIplusIminus
    def setRpimWithinIplusIminus(self, rpimWithinIplusIminus):
        if rpimWithinIplusIminus is None:
            self._rpimWithinIplusIminus = None
        else:
            self._rpimWithinIplusIminus = float(rpimWithinIplusIminus)
    def delRpimWithinIplusIminus(self): self._rpimWithinIplusIminus = None
    rpimWithinIplusIminus = property(getRpimWithinIplusIminus, setRpimWithinIplusIminus, delRpimWithinIplusIminus, "Property for rpimWithinIplusIminus")
    # Methods and properties for the 'rpimAllIplusIminus' attribute
    def getRpimAllIplusIminus(self): return self._rpimAllIplusIminus
    def setRpimAllIplusIminus(self, rpimAllIplusIminus):
        if rpimAllIplusIminus is None:
            self._rpimAllIplusIminus = None
        else:
            self._rpimAllIplusIminus = float(rpimAllIplusIminus)
    def delRpimAllIplusIminus(self): self._rpimAllIplusIminus = None
    rpimAllIplusIminus = property(getRpimAllIplusIminus, setRpimAllIplusIminus, delRpimAllIplusIminus, "Property for rpimAllIplusIminus")
    # Methods and properties for the 'fractionalPartialBias' attribute
    def getFractionalPartialBias(self): return self._fractionalPartialBias
    def setFractionalPartialBias(self, fractionalPartialBias):
        if fractionalPartialBias is None:
            self._fractionalPartialBias = None
        else:
            self._fractionalPartialBias = float(fractionalPartialBias)
    def delFractionalPartialBias(self): self._fractionalPartialBias = None
    fractionalPartialBias = property(getFractionalPartialBias, setFractionalPartialBias, delFractionalPartialBias, "Property for fractionalPartialBias")
    # Methods and properties for the 'nTotalObservations' attribute
    def getNTotalObservations(self): return self._nTotalObservations
    def setNTotalObservations(self, nTotalObservations):
        if nTotalObservations is None:
            self._nTotalObservations = None
        else:
            self._nTotalObservations = int(nTotalObservations)
    def delNTotalObservations(self): self._nTotalObservations = None
    nTotalObservations = property(getNTotalObservations, setNTotalObservations, delNTotalObservations, "Property for nTotalObservations")
    # Methods and properties for the 'ntotalUniqueObservations' attribute
    def getNtotalUniqueObservations(self): return self._ntotalUniqueObservations
    def setNtotalUniqueObservations(self, ntotalUniqueObservations):
        if ntotalUniqueObservations is None:
            self._ntotalUniqueObservations = None
        else:
            self._ntotalUniqueObservations = int(ntotalUniqueObservations)
    def delNtotalUniqueObservations(self): self._ntotalUniqueObservations = None
    ntotalUniqueObservations = property(getNtotalUniqueObservations, setNtotalUniqueObservations, delNtotalUniqueObservations, "Property for ntotalUniqueObservations")
    # Methods and properties for the 'meanIOverSigI' attribute
    def getMeanIOverSigI(self): return self._meanIOverSigI
    def setMeanIOverSigI(self, meanIOverSigI):
        if meanIOverSigI is None:
            self._meanIOverSigI = None
        else:
            self._meanIOverSigI = float(meanIOverSigI)
    def delMeanIOverSigI(self): self._meanIOverSigI = None
    meanIOverSigI = property(getMeanIOverSigI, setMeanIOverSigI, delMeanIOverSigI, "Property for meanIOverSigI")
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        else:
            self._completeness = float(completeness)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        else:
            self._multiplicity = float(multiplicity)
    def delMultiplicity(self): self._multiplicity = None
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    # Methods and properties for the 'anomalousCompleteness' attribute
    def getAnomalousCompleteness(self): return self._anomalousCompleteness
    def setAnomalousCompleteness(self, anomalousCompleteness):
        if anomalousCompleteness is None:
            self._anomalousCompleteness = None
        else:
            self._anomalousCompleteness = float(anomalousCompleteness)
    def delAnomalousCompleteness(self): self._anomalousCompleteness = None
    anomalousCompleteness = property(getAnomalousCompleteness, setAnomalousCompleteness, delAnomalousCompleteness, "Property for anomalousCompleteness")
    # Methods and properties for the 'anomalousMultiplicity' attribute
    def getAnomalousMultiplicity(self): return self._anomalousMultiplicity
    def setAnomalousMultiplicity(self, anomalousMultiplicity):
        if anomalousMultiplicity is None:
            self._anomalousMultiplicity = None
        else:
            self._anomalousMultiplicity = float(anomalousMultiplicity)
    def delAnomalousMultiplicity(self): self._anomalousMultiplicity = None
    anomalousMultiplicity = property(getAnomalousMultiplicity, setAnomalousMultiplicity, delAnomalousMultiplicity, "Property for anomalousMultiplicity")
    # Methods and properties for the 'recordTimeStamp' attribute
    def getRecordTimeStamp(self): return self._recordTimeStamp
    def setRecordTimeStamp(self, recordTimeStamp):
        self._recordTimeStamp = str(recordTimeStamp)
    def delRecordTimeStamp(self): self._recordTimeStamp = None
    recordTimeStamp = property(getRecordTimeStamp, setRecordTimeStamp, delRecordTimeStamp, "Property for recordTimeStamp")
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        self._anomalous = bool(anomalous)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    # Methods and properties for the 'ccHalf' attribute
    def getCcHalf(self): return self._ccHalf
    def setCcHalf(self, ccHalf):
        if ccHalf is None:
            self._ccHalf = None
        else:
            self._ccHalf = float(ccHalf)
    def delCcHalf(self): self._ccHalf = None
    ccHalf = property(getCcHalf, setCcHalf, delCcHalf, "Property for ccHalf")
    def export(self, outfile, level, name_='AutoProcScalingStatistics'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcScalingStatistics'):
        pass
        if self._autoProcScalingStatisticsId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcScalingStatisticsId>%d</autoProcScalingStatisticsId>\n' % self._autoProcScalingStatisticsId))
        if self._scalingStatisticsType is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<scalingStatisticsType>%s</scalingStatisticsType>\n' % self._scalingStatisticsType))
        else:
            warnEmptyAttribute("scalingStatisticsType", "string")
        if self._comments is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
        else:
            warnEmptyAttribute("comments", "string")
        if self._resolutionLimitLow is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolutionLimitLow>%e</resolutionLimitLow>\n' % self._resolutionLimitLow))
        else:
            warnEmptyAttribute("resolutionLimitLow", "float")
        if self._resolutionLimitHigh is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolutionLimitHigh>%e</resolutionLimitHigh>\n' % self._resolutionLimitHigh))
        else:
            warnEmptyAttribute("resolutionLimitHigh", "float")
        if self._rMerge is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rMerge>%e</rMerge>\n' % self._rMerge))
        else:
            warnEmptyAttribute("rMerge", "float")
        if self._rmeasWithinIplusIminus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rmeasWithinIplusIminus>%e</rmeasWithinIplusIminus>\n' % self._rmeasWithinIplusIminus))
        else:
            warnEmptyAttribute("rmeasWithinIplusIminus", "float")
        if self._rmeasAllIplusIminus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rmeasAllIplusIminus>%e</rmeasAllIplusIminus>\n' % self._rmeasAllIplusIminus))
        else:
            warnEmptyAttribute("rmeasAllIplusIminus", "float")
        if self._rpimWithinIplusIminus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rpimWithinIplusIminus>%e</rpimWithinIplusIminus>\n' % self._rpimWithinIplusIminus))
        else:
            warnEmptyAttribute("rpimWithinIplusIminus", "float")
        if self._rpimAllIplusIminus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rpimAllIplusIminus>%e</rpimAllIplusIminus>\n' % self._rpimAllIplusIminus))
        else:
            warnEmptyAttribute("rpimAllIplusIminus", "float")
        if self._fractionalPartialBias is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<fractionalPartialBias>%e</fractionalPartialBias>\n' % self._fractionalPartialBias))
        else:
            warnEmptyAttribute("fractionalPartialBias", "float")
        if self._nTotalObservations is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<nTotalObservations>%d</nTotalObservations>\n' % self._nTotalObservations))
        else:
            warnEmptyAttribute("nTotalObservations", "integer")
        if self._ntotalUniqueObservations is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ntotalUniqueObservations>%d</ntotalUniqueObservations>\n' % self._ntotalUniqueObservations))
        else:
            warnEmptyAttribute("ntotalUniqueObservations", "integer")
        if self._meanIOverSigI is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<meanIOverSigI>%e</meanIOverSigI>\n' % self._meanIOverSigI))
        else:
            warnEmptyAttribute("meanIOverSigI", "float")
        if self._completeness is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<completeness>%e</completeness>\n' % self._completeness))
        else:
            warnEmptyAttribute("completeness", "float")
        if self._multiplicity is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<multiplicity>%e</multiplicity>\n' % self._multiplicity))
        else:
            warnEmptyAttribute("multiplicity", "float")
        if self._anomalousCompleteness is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<anomalousCompleteness>%e</anomalousCompleteness>\n' % self._anomalousCompleteness))
        else:
            warnEmptyAttribute("anomalousCompleteness", "float")
        if self._anomalousMultiplicity is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<anomalousMultiplicity>%e</anomalousMultiplicity>\n' % self._anomalousMultiplicity))
        else:
            warnEmptyAttribute("anomalousMultiplicity", "float")
        if self._recordTimeStamp is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<recordTimeStamp>%s</recordTimeStamp>\n' % self._recordTimeStamp))
        else:
            warnEmptyAttribute("recordTimeStamp", "string")
        if self._anomalous is not None:
            showIndent(outfile, level)
            if self._anomalous:
                outfile.write(unicode('<anomalous>true</anomalous>\n'))
            else:
                outfile.write(unicode('<anomalous>false</anomalous>\n'))
        else:
            warnEmptyAttribute("anomalous", "boolean")
        if self._ccHalf is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ccHalf>%e</ccHalf>\n' % self._ccHalf))
        else:
            warnEmptyAttribute("ccHalf", "float")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcScalingStatisticsId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcScalingStatisticsId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scalingStatisticsType':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._scalingStatisticsType = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._comments = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionLimitLow':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolutionLimitLow = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionLimitHigh':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolutionLimitHigh = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMerge':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rMerge = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmeasWithinIplusIminus':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rmeasWithinIplusIminus = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmeasAllIplusIminus':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rmeasAllIplusIminus = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rpimWithinIplusIminus':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rpimWithinIplusIminus = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rpimAllIplusIminus':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rpimAllIplusIminus = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fractionalPartialBias':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._fractionalPartialBias = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nTotalObservations':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._nTotalObservations = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ntotalUniqueObservations':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._ntotalUniqueObservations = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'meanIOverSigI':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._meanIOverSigI = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._completeness = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._multiplicity = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalousCompleteness':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._anomalousCompleteness = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalousMultiplicity':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._anomalousMultiplicity = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'recordTimeStamp':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._recordTimeStamp = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('True', 'true', '1'):
                    ival_ = True
                elif sval_ in ('False', 'false', '0'):
                    ival_ = False
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self._anomalous = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ccHalf':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ccHalf = fval_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcScalingStatistics" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcScalingStatistics' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcScalingStatistics is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcScalingStatistics.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcScalingStatistics()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcScalingStatistics" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcScalingStatistics()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcScalingStatistics


class AutoProcScalingContainer(object):
    def __init__(self, AutoProcIntegrationContainer=None, AutoProcScalingStatistics=None, AutoProcScaling=None):
        if AutoProcScaling is None:
            self._AutoProcScaling = None
        elif AutoProcScaling.__class__.__name__ == "AutoProcScaling":
            self._AutoProcScaling = AutoProcScaling
        else:
            strMessage = "ERROR! AutoProcScalingContainer constructor argument 'AutoProcScaling' is not AutoProcScaling but %s" % self._AutoProcScaling.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcScalingStatistics is None:
            self._AutoProcScalingStatistics = []
        elif AutoProcScalingStatistics.__class__.__name__ == "list":
            self._AutoProcScalingStatistics = AutoProcScalingStatistics
        else:
            strMessage = "ERROR! AutoProcScalingContainer constructor argument 'AutoProcScalingStatistics' is not list but %s" % self._AutoProcScalingStatistics.__class__.__name__
            raise BaseException(strMessage)
        if AutoProcIntegrationContainer is None:
            self._AutoProcIntegrationContainer = None
        elif AutoProcIntegrationContainer.__class__.__name__ == "AutoProcIntegrationContainer":
            self._AutoProcIntegrationContainer = AutoProcIntegrationContainer
        else:
            strMessage = "ERROR! AutoProcScalingContainer constructor argument 'AutoProcIntegrationContainer' is not AutoProcIntegrationContainer but %s" % self._AutoProcIntegrationContainer.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'AutoProcScaling' attribute
    def getAutoProcScaling(self): return self._AutoProcScaling
    def setAutoProcScaling(self, AutoProcScaling):
        if AutoProcScaling is None:
            self._AutoProcScaling = None
        elif AutoProcScaling.__class__.__name__ == "AutoProcScaling":
            self._AutoProcScaling = AutoProcScaling
        else:
            strMessage = "ERROR! AutoProcScalingContainer.setAutoProcScaling argument is not AutoProcScaling but %s" % AutoProcScaling.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcScaling(self): self._AutoProcScaling = None
    AutoProcScaling = property(getAutoProcScaling, setAutoProcScaling, delAutoProcScaling, "Property for AutoProcScaling")
    # Methods and properties for the 'AutoProcScalingStatistics' attribute
    def getAutoProcScalingStatistics(self): return self._AutoProcScalingStatistics
    def setAutoProcScalingStatistics(self, AutoProcScalingStatistics):
        if AutoProcScalingStatistics is None:
            self._AutoProcScalingStatistics = []
        elif AutoProcScalingStatistics.__class__.__name__ == "list":
            self._AutoProcScalingStatistics = AutoProcScalingStatistics
        else:
            strMessage = "ERROR! AutoProcScalingContainer.setAutoProcScalingStatistics argument is not list but %s" % AutoProcScalingStatistics.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcScalingStatistics(self): self._AutoProcScalingStatistics = None
    AutoProcScalingStatistics = property(getAutoProcScalingStatistics, setAutoProcScalingStatistics, delAutoProcScalingStatistics, "Property for AutoProcScalingStatistics")
    def addAutoProcScalingStatistics(self, value):
        if value is None:
            strMessage = "ERROR! AutoProcScalingContainer.addAutoProcScalingStatistics argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "AutoProcScalingStatistics":
            self._AutoProcScalingStatistics.append(value)
        else:
            strMessage = "ERROR! AutoProcScalingContainer.addAutoProcScalingStatistics argument is not AutoProcScalingStatistics but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAutoProcScalingStatistics(self, index, value):
        if index is None:
            strMessage = "ERROR! AutoProcScalingContainer.insertAutoProcScalingStatistics argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! AutoProcScalingContainer.insertAutoProcScalingStatistics argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "AutoProcScalingStatistics":
            self._AutoProcScalingStatistics[index] = value
        else:
            strMessage = "ERROR! AutoProcScalingContainer.addAutoProcScalingStatistics argument is not AutoProcScalingStatistics but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'AutoProcIntegrationContainer' attribute
    def getAutoProcIntegrationContainer(self): return self._AutoProcIntegrationContainer
    def setAutoProcIntegrationContainer(self, AutoProcIntegrationContainer):
        if AutoProcIntegrationContainer is None:
            self._AutoProcIntegrationContainer = None
        elif AutoProcIntegrationContainer.__class__.__name__ == "AutoProcIntegrationContainer":
            self._AutoProcIntegrationContainer = AutoProcIntegrationContainer
        else:
            strMessage = "ERROR! AutoProcScalingContainer.setAutoProcIntegrationContainer argument is not AutoProcIntegrationContainer but %s" % AutoProcIntegrationContainer.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcIntegrationContainer(self): self._AutoProcIntegrationContainer = None
    AutoProcIntegrationContainer = property(getAutoProcIntegrationContainer, setAutoProcIntegrationContainer, delAutoProcIntegrationContainer, "Property for AutoProcIntegrationContainer")
    def export(self, outfile, level, name_='AutoProcScalingContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcScalingContainer'):
        pass
        if self._AutoProcScaling is not None:
            self.AutoProcScaling.export(outfile, level, name_='AutoProcScaling')
        else:
            warnEmptyAttribute("AutoProcScaling", "AutoProcScaling")
        for AutoProcScalingStatistics_ in self.getAutoProcScalingStatistics():
            AutoProcScalingStatistics_.export(outfile, level, name_='AutoProcScalingStatistics')
        if self.getAutoProcScalingStatistics() == []:
            warnEmptyAttribute("AutoProcScalingStatistics", "AutoProcScalingStatistics")
        if self._AutoProcIntegrationContainer is not None:
            self.AutoProcIntegrationContainer.export(outfile, level, name_='AutoProcIntegrationContainer')
        else:
            warnEmptyAttribute("AutoProcIntegrationContainer", "AutoProcIntegrationContainer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcScaling':
            obj_ = AutoProcScaling()
            obj_.build(child_)
            self.setAutoProcScaling(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcScalingStatistics':
            obj_ = AutoProcScalingStatistics()
            obj_.build(child_)
            self.AutoProcScalingStatistics.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcIntegrationContainer':
            obj_ = AutoProcIntegrationContainer()
            obj_.build(child_)
            self.setAutoProcIntegrationContainer(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcScalingContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcScalingContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcScalingContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcScalingContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcScalingContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcScalingContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcScalingContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcScalingContainer


class AutoProcStatus(object):
    def __init__(self, bltimeStamp=None, comments=None, status=None, step=None, autoProcIntegrationId=None, autoProcStatusId=None):
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
        self._step = str(step)
        self._status = str(status)
        self._comments = str(comments)
        self._bltimeStamp = str(bltimeStamp)
    # Methods and properties for the 'autoProcStatusId' attribute
    def getAutoProcStatusId(self): return self._autoProcStatusId
    def setAutoProcStatusId(self, autoProcStatusId):
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
    def delAutoProcStatusId(self): self._autoProcStatusId = None
    autoProcStatusId = property(getAutoProcStatusId, setAutoProcStatusId, delAutoProcStatusId, "Property for autoProcStatusId")
    # Methods and properties for the 'autoProcIntegrationId' attribute
    def getAutoProcIntegrationId(self): return self._autoProcIntegrationId
    def setAutoProcIntegrationId(self, autoProcIntegrationId):
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
    def delAutoProcIntegrationId(self): self._autoProcIntegrationId = None
    autoProcIntegrationId = property(getAutoProcIntegrationId, setAutoProcIntegrationId, delAutoProcIntegrationId, "Property for autoProcIntegrationId")
    # Methods and properties for the 'step' attribute
    def getStep(self): return self._step
    def setStep(self, step):
        self._step = str(step)
    def delStep(self): self._step = None
    step = property(getStep, setStep, delStep, "Property for step")
    # Methods and properties for the 'status' attribute
    def getStatus(self): return self._status
    def setStatus(self, status):
        self._status = str(status)
    def delStatus(self): self._status = None
    status = property(getStatus, setStatus, delStatus, "Property for status")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        self._comments = str(comments)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'bltimeStamp' attribute
    def getBltimeStamp(self): return self._bltimeStamp
    def setBltimeStamp(self, bltimeStamp):
        self._bltimeStamp = str(bltimeStamp)
    def delBltimeStamp(self): self._bltimeStamp = None
    bltimeStamp = property(getBltimeStamp, setBltimeStamp, delBltimeStamp, "Property for bltimeStamp")
    def export(self, outfile, level, name_='AutoProcStatus'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='AutoProcStatus'):
        pass
        if self._autoProcStatusId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcStatusId>%d</autoProcStatusId>\n' % self._autoProcStatusId))
        if self._autoProcIntegrationId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcIntegrationId>%d</autoProcIntegrationId>\n' % self._autoProcIntegrationId))
        else:
            warnEmptyAttribute("autoProcIntegrationId", "integer")
        if self._step is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<step>%s</step>\n' % self._step))
        else:
            warnEmptyAttribute("step", "string")
        if self._status is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<status>%s</status>\n' % self._status))
        else:
            warnEmptyAttribute("status", "string")
        if self._comments is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
        else:
            warnEmptyAttribute("comments", "string")
        if self._bltimeStamp is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<bltimeStamp>%s</bltimeStamp>\n' % self._bltimeStamp))
        else:
            warnEmptyAttribute("bltimeStamp", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcStatusId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcStatusId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcIntegrationId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcIntegrationId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'step':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._step = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'status':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._status = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._comments = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bltimeStamp':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._bltimeStamp = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="AutoProcStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='AutoProcStatus' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class AutoProcStatus is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return AutoProcStatus.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = AutoProcStatus()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="AutoProcStatus" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = AutoProcStatus()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class AutoProcStatus


class Image(object):
    def __init__(self, dataCollectionId=None):
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    def export(self, outfile, level, name_='Image'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='Image'):
        pass
        if self._dataCollectionId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
        else:
            warnEmptyAttribute("dataCollectionId", "integer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionId = ival_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="Image" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='Image' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class Image is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return Image.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = Image()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="Image" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = Image()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class Image


class XSDataISPyBDataCollection(object):
    def __init__(self, ybeam=None, xtalSnapshotFullPath4=None, xtalSnapshotFullPath3=None, xtalSnapshotFullPath2=None, xtalSnapshotFullPath1=None, xbeam=None, wavelength=None, undulatorGap3=None, undulatorGap2=None, undulatorGap1=None, transmission=None, synchrotronMode=None, startTime=None, strategySubWedgeOrigId=None, startImageNumber=None, slitGapHorizontal=None, slitGapVertical=None, runStatus=None, rotationAxis=None, resolutionAtCorner=None, resolution=None, printableForReport=None, phiStart=None, overlap=None, omegaStart=None, numberOfPasses=None, numberOfImages=None, kappaStart=None, imageSuffix=None, imagePrefix=None, imageDirectory=None, flux=None, fileTemplate=None, exposureTime=None, endTime=None, detectorMode=None, detectorDistance=None, detector2theta=None, dataCollectionNumber=None, dataCollectionId=None, comments=None, centeringMethod=None, beamSizeAtSampleY=None, beamSizeAtSampleX=None, beamShape=None, axisStart=None, axisRange=None, axisEnd=None, averageTemperature=None, actualCenteringPosition=None):
        self._actualCenteringPosition = str(actualCenteringPosition)
        if averageTemperature is None:
            self._averageTemperature = None
        else:
            self._averageTemperature = float(averageTemperature)
        if axisEnd is None:
            self._axisEnd = None
        else:
            self._axisEnd = float(axisEnd)
        if axisRange is None:
            self._axisRange = None
        else:
            self._axisRange = float(axisRange)
        if axisStart is None:
            self._axisStart = None
        else:
            self._axisStart = float(axisStart)
        self._beamShape = str(beamShape)
        if beamSizeAtSampleX is None:
            self._beamSizeAtSampleX = None
        else:
            self._beamSizeAtSampleX = float(beamSizeAtSampleX)
        if beamSizeAtSampleY is None:
            self._beamSizeAtSampleY = None
        else:
            self._beamSizeAtSampleY = float(beamSizeAtSampleY)
        self._centeringMethod = str(centeringMethod)
        self._comments = str(comments)
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
        if dataCollectionNumber is None:
            self._dataCollectionNumber = None
        else:
            self._dataCollectionNumber = int(dataCollectionNumber)
        if detector2theta is None:
            self._detector2theta = None
        else:
            self._detector2theta = float(detector2theta)
        if detectorDistance is None:
            self._detectorDistance = None
        else:
            self._detectorDistance = float(detectorDistance)
        self._detectorMode = str(detectorMode)
        self._endTime = str(endTime)
        if exposureTime is None:
            self._exposureTime = None
        else:
            self._exposureTime = float(exposureTime)
        self._fileTemplate = str(fileTemplate)
        if flux is None:
            self._flux = None
        else:
            self._flux = float(flux)
        self._imageDirectory = str(imageDirectory)
        self._imagePrefix = str(imagePrefix)
        self._imageSuffix = str(imageSuffix)
        if kappaStart is None:
            self._kappaStart = None
        else:
            self._kappaStart = float(kappaStart)
        if numberOfImages is None:
            self._numberOfImages = None
        else:
            self._numberOfImages = int(numberOfImages)
        if numberOfPasses is None:
            self._numberOfPasses = None
        else:
            self._numberOfPasses = int(numberOfPasses)
        if omegaStart is None:
            self._omegaStart = None
        else:
            self._omegaStart = float(omegaStart)
        if overlap is None:
            self._overlap = None
        else:
            self._overlap = float(overlap)
        if phiStart is None:
            self._phiStart = None
        else:
            self._phiStart = float(phiStart)
        self._printableForReport = bool(printableForReport)
        if resolution is None:
            self._resolution = None
        else:
            self._resolution = float(resolution)
        if resolutionAtCorner is None:
            self._resolutionAtCorner = None
        else:
            self._resolutionAtCorner = float(resolutionAtCorner)
        self._rotationAxis = str(rotationAxis)
        self._runStatus = str(runStatus)
        if slitGapVertical is None:
            self._slitGapVertical = None
        else:
            self._slitGapVertical = float(slitGapVertical)
        if slitGapHorizontal is None:
            self._slitGapHorizontal = None
        else:
            self._slitGapHorizontal = float(slitGapHorizontal)
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
        if strategySubWedgeOrigId is None:
            self._strategySubWedgeOrigId = None
        else:
            self._strategySubWedgeOrigId = int(strategySubWedgeOrigId)
        self._startTime = str(startTime)
        self._synchrotronMode = str(synchrotronMode)
        if transmission is None:
            self._transmission = None
        else:
            self._transmission = float(transmission)
        if undulatorGap1 is None:
            self._undulatorGap1 = None
        else:
            self._undulatorGap1 = float(undulatorGap1)
        if undulatorGap2 is None:
            self._undulatorGap2 = None
        else:
            self._undulatorGap2 = float(undulatorGap2)
        if undulatorGap3 is None:
            self._undulatorGap3 = None
        else:
            self._undulatorGap3 = float(undulatorGap3)
        if wavelength is None:
            self._wavelength = None
        else:
            self._wavelength = float(wavelength)
        if xbeam is None:
            self._xbeam = None
        else:
            self._xbeam = float(xbeam)
        self._xtalSnapshotFullPath1 = str(xtalSnapshotFullPath1)
        self._xtalSnapshotFullPath2 = str(xtalSnapshotFullPath2)
        self._xtalSnapshotFullPath3 = str(xtalSnapshotFullPath3)
        self._xtalSnapshotFullPath4 = str(xtalSnapshotFullPath4)
        if ybeam is None:
            self._ybeam = None
        else:
            self._ybeam = float(ybeam)
    # Methods and properties for the 'actualCenteringPosition' attribute
    def getActualCenteringPosition(self): return self._actualCenteringPosition
    def setActualCenteringPosition(self, actualCenteringPosition):
        self._actualCenteringPosition = str(actualCenteringPosition)
    def delActualCenteringPosition(self): self._actualCenteringPosition = None
    actualCenteringPosition = property(getActualCenteringPosition, setActualCenteringPosition, delActualCenteringPosition, "Property for actualCenteringPosition")
    # Methods and properties for the 'averageTemperature' attribute
    def getAverageTemperature(self): return self._averageTemperature
    def setAverageTemperature(self, averageTemperature):
        if averageTemperature is None:
            self._averageTemperature = None
        else:
            self._averageTemperature = float(averageTemperature)
    def delAverageTemperature(self): self._averageTemperature = None
    averageTemperature = property(getAverageTemperature, setAverageTemperature, delAverageTemperature, "Property for averageTemperature")
    # Methods and properties for the 'axisEnd' attribute
    def getAxisEnd(self): return self._axisEnd
    def setAxisEnd(self, axisEnd):
        if axisEnd is None:
            self._axisEnd = None
        else:
            self._axisEnd = float(axisEnd)
    def delAxisEnd(self): self._axisEnd = None
    axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
    # Methods and properties for the 'axisRange' attribute
    def getAxisRange(self): return self._axisRange
    def setAxisRange(self, axisRange):
        if axisRange is None:
            self._axisRange = None
        else:
            self._axisRange = float(axisRange)
    def delAxisRange(self): self._axisRange = None
    axisRange = property(getAxisRange, setAxisRange, delAxisRange, "Property for axisRange")
    # Methods and properties for the 'axisStart' attribute
    def getAxisStart(self): return self._axisStart
    def setAxisStart(self, axisStart):
        if axisStart is None:
            self._axisStart = None
        else:
            self._axisStart = float(axisStart)
    def delAxisStart(self): self._axisStart = None
    axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
    # Methods and properties for the 'beamShape' attribute
    def getBeamShape(self): return self._beamShape
    def setBeamShape(self, beamShape):
        self._beamShape = str(beamShape)
    def delBeamShape(self): self._beamShape = None
    beamShape = property(getBeamShape, setBeamShape, delBeamShape, "Property for beamShape")
    # Methods and properties for the 'beamSizeAtSampleX' attribute
    def getBeamSizeAtSampleX(self): return self._beamSizeAtSampleX
    def setBeamSizeAtSampleX(self, beamSizeAtSampleX):
        if beamSizeAtSampleX is None:
            self._beamSizeAtSampleX = None
        else:
            self._beamSizeAtSampleX = float(beamSizeAtSampleX)
    def delBeamSizeAtSampleX(self): self._beamSizeAtSampleX = None
    beamSizeAtSampleX = property(getBeamSizeAtSampleX, setBeamSizeAtSampleX, delBeamSizeAtSampleX, "Property for beamSizeAtSampleX")
    # Methods and properties for the 'beamSizeAtSampleY' attribute
    def getBeamSizeAtSampleY(self): return self._beamSizeAtSampleY
    def setBeamSizeAtSampleY(self, beamSizeAtSampleY):
        if beamSizeAtSampleY is None:
            self._beamSizeAtSampleY = None
        else:
            self._beamSizeAtSampleY = float(beamSizeAtSampleY)
    def delBeamSizeAtSampleY(self): self._beamSizeAtSampleY = None
    beamSizeAtSampleY = property(getBeamSizeAtSampleY, setBeamSizeAtSampleY, delBeamSizeAtSampleY, "Property for beamSizeAtSampleY")
    # Methods and properties for the 'centeringMethod' attribute
    def getCenteringMethod(self): return self._centeringMethod
    def setCenteringMethod(self, centeringMethod):
        self._centeringMethod = str(centeringMethod)
    def delCenteringMethod(self): self._centeringMethod = None
    centeringMethod = property(getCenteringMethod, setCenteringMethod, delCenteringMethod, "Property for centeringMethod")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        self._comments = str(comments)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'dataCollectionNumber' attribute
    def getDataCollectionNumber(self): return self._dataCollectionNumber
    def setDataCollectionNumber(self, dataCollectionNumber):
        if dataCollectionNumber is None:
            self._dataCollectionNumber = None
        else:
            self._dataCollectionNumber = int(dataCollectionNumber)
    def delDataCollectionNumber(self): self._dataCollectionNumber = None
    dataCollectionNumber = property(getDataCollectionNumber, setDataCollectionNumber, delDataCollectionNumber, "Property for dataCollectionNumber")
    # Methods and properties for the 'detector2theta' attribute
    def getDetector2theta(self): return self._detector2theta
    def setDetector2theta(self, detector2theta):
        if detector2theta is None:
            self._detector2theta = None
        else:
            self._detector2theta = float(detector2theta)
    def delDetector2theta(self): self._detector2theta = None
    detector2theta = property(getDetector2theta, setDetector2theta, delDetector2theta, "Property for detector2theta")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        else:
            self._detectorDistance = float(detectorDistance)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'detectorMode' attribute
    def getDetectorMode(self): return self._detectorMode
    def setDetectorMode(self, detectorMode):
        self._detectorMode = str(detectorMode)
    def delDetectorMode(self): self._detectorMode = None
    detectorMode = property(getDetectorMode, setDetectorMode, delDetectorMode, "Property for detectorMode")
    # Methods and properties for the 'endTime' attribute
    def getEndTime(self): return self._endTime
    def setEndTime(self, endTime):
        self._endTime = str(endTime)
    def delEndTime(self): self._endTime = None
    endTime = property(getEndTime, setEndTime, delEndTime, "Property for endTime")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        else:
            self._exposureTime = float(exposureTime)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'fileTemplate' attribute
    def getFileTemplate(self): return self._fileTemplate
    def setFileTemplate(self, fileTemplate):
        self._fileTemplate = str(fileTemplate)
    def delFileTemplate(self): self._fileTemplate = None
    fileTemplate = property(getFileTemplate, setFileTemplate, delFileTemplate, "Property for fileTemplate")
    # Methods and properties for the 'flux' attribute
    def getFlux(self): return self._flux
    def setFlux(self, flux):
        if flux is None:
            self._flux = None
        else:
            self._flux = float(flux)
    def delFlux(self): self._flux = None
    flux = property(getFlux, setFlux, delFlux, "Property for flux")
    # Methods and properties for the 'imageDirectory' attribute
    def getImageDirectory(self): return self._imageDirectory
    def setImageDirectory(self, imageDirectory):
        self._imageDirectory = str(imageDirectory)
    def delImageDirectory(self): self._imageDirectory = None
    imageDirectory = property(getImageDirectory, setImageDirectory, delImageDirectory, "Property for imageDirectory")
    # Methods and properties for the 'imagePrefix' attribute
    def getImagePrefix(self): return self._imagePrefix
    def setImagePrefix(self, imagePrefix):
        self._imagePrefix = str(imagePrefix)
    def delImagePrefix(self): self._imagePrefix = None
    imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
    # Methods and properties for the 'imageSuffix' attribute
    def getImageSuffix(self): return self._imageSuffix
    def setImageSuffix(self, imageSuffix):
        self._imageSuffix = str(imageSuffix)
    def delImageSuffix(self): self._imageSuffix = None
    imageSuffix = property(getImageSuffix, setImageSuffix, delImageSuffix, "Property for imageSuffix")
    # Methods and properties for the 'kappaStart' attribute
    def getKappaStart(self): return self._kappaStart
    def setKappaStart(self, kappaStart):
        if kappaStart is None:
            self._kappaStart = None
        else:
            self._kappaStart = float(kappaStart)
    def delKappaStart(self): self._kappaStart = None
    kappaStart = property(getKappaStart, setKappaStart, delKappaStart, "Property for kappaStart")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        else:
            self._numberOfImages = int(numberOfImages)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'numberOfPasses' attribute
    def getNumberOfPasses(self): return self._numberOfPasses
    def setNumberOfPasses(self, numberOfPasses):
        if numberOfPasses is None:
            self._numberOfPasses = None
        else:
            self._numberOfPasses = int(numberOfPasses)
    def delNumberOfPasses(self): self._numberOfPasses = None
    numberOfPasses = property(getNumberOfPasses, setNumberOfPasses, delNumberOfPasses, "Property for numberOfPasses")
    # Methods and properties for the 'omegaStart' attribute
    def getOmegaStart(self): return self._omegaStart
    def setOmegaStart(self, omegaStart):
        if omegaStart is None:
            self._omegaStart = None
        else:
            self._omegaStart = float(omegaStart)
    def delOmegaStart(self): self._omegaStart = None
    omegaStart = property(getOmegaStart, setOmegaStart, delOmegaStart, "Property for omegaStart")
    # Methods and properties for the 'overlap' attribute
    def getOverlap(self): return self._overlap
    def setOverlap(self, overlap):
        if overlap is None:
            self._overlap = None
        else:
            self._overlap = float(overlap)
    def delOverlap(self): self._overlap = None
    overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
    # Methods and properties for the 'phiStart' attribute
    def getPhiStart(self): return self._phiStart
    def setPhiStart(self, phiStart):
        if phiStart is None:
            self._phiStart = None
        else:
            self._phiStart = float(phiStart)
    def delPhiStart(self): self._phiStart = None
    phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
    # Methods and properties for the 'printableForReport' attribute
    def getPrintableForReport(self): return self._printableForReport
    def setPrintableForReport(self, printableForReport):
        self._printableForReport = bool(printableForReport)
    def delPrintableForReport(self): self._printableForReport = None
    printableForReport = property(getPrintableForReport, setPrintableForReport, delPrintableForReport, "Property for printableForReport")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        else:
            self._resolution = float(resolution)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'resolutionAtCorner' attribute
    def getResolutionAtCorner(self): return self._resolutionAtCorner
    def setResolutionAtCorner(self, resolutionAtCorner):
        if resolutionAtCorner is None:
            self._resolutionAtCorner = None
        else:
            self._resolutionAtCorner = float(resolutionAtCorner)
    def delResolutionAtCorner(self): self._resolutionAtCorner = None
    resolutionAtCorner = property(getResolutionAtCorner, setResolutionAtCorner, delResolutionAtCorner, "Property for resolutionAtCorner")
    # Methods and properties for the 'rotationAxis' attribute
    def getRotationAxis(self): return self._rotationAxis
    def setRotationAxis(self, rotationAxis):
        self._rotationAxis = str(rotationAxis)
    def delRotationAxis(self): self._rotationAxis = None
    rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
    # Methods and properties for the 'runStatus' attribute
    def getRunStatus(self): return self._runStatus
    def setRunStatus(self, runStatus):
        self._runStatus = str(runStatus)
    def delRunStatus(self): self._runStatus = None
    runStatus = property(getRunStatus, setRunStatus, delRunStatus, "Property for runStatus")
    # Methods and properties for the 'slitGapVertical' attribute
    def getSlitGapVertical(self): return self._slitGapVertical
    def setSlitGapVertical(self, slitGapVertical):
        if slitGapVertical is None:
            self._slitGapVertical = None
        else:
            self._slitGapVertical = float(slitGapVertical)
    def delSlitGapVertical(self): self._slitGapVertical = None
    slitGapVertical = property(getSlitGapVertical, setSlitGapVertical, delSlitGapVertical, "Property for slitGapVertical")
    # Methods and properties for the 'slitGapHorizontal' attribute
    def getSlitGapHorizontal(self): return self._slitGapHorizontal
    def setSlitGapHorizontal(self, slitGapHorizontal):
        if slitGapHorizontal is None:
            self._slitGapHorizontal = None
        else:
            self._slitGapHorizontal = float(slitGapHorizontal)
    def delSlitGapHorizontal(self): self._slitGapHorizontal = None
    slitGapHorizontal = property(getSlitGapHorizontal, setSlitGapHorizontal, delSlitGapHorizontal, "Property for slitGapHorizontal")
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
    def delStartImageNumber(self): self._startImageNumber = None
    startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
    # Methods and properties for the 'strategySubWedgeOrigId' attribute
    def getStrategySubWedgeOrigId(self): return self._strategySubWedgeOrigId
    def setStrategySubWedgeOrigId(self, strategySubWedgeOrigId):
        if strategySubWedgeOrigId is None:
            self._strategySubWedgeOrigId = None
        else:
            self._strategySubWedgeOrigId = int(strategySubWedgeOrigId)
    def delStrategySubWedgeOrigId(self): self._strategySubWedgeOrigId = None
    strategySubWedgeOrigId = property(getStrategySubWedgeOrigId, setStrategySubWedgeOrigId, delStrategySubWedgeOrigId, "Property for strategySubWedgeOrigId")
    # Methods and properties for the 'startTime' attribute
    def getStartTime(self): return self._startTime
    def setStartTime(self, startTime):
        self._startTime = str(startTime)
    def delStartTime(self): self._startTime = None
    startTime = property(getStartTime, setStartTime, delStartTime, "Property for startTime")
    # Methods and properties for the 'synchrotronMode' attribute
    def getSynchrotronMode(self): return self._synchrotronMode
    def setSynchrotronMode(self, synchrotronMode):
        self._synchrotronMode = str(synchrotronMode)
    def delSynchrotronMode(self): self._synchrotronMode = None
    synchrotronMode = property(getSynchrotronMode, setSynchrotronMode, delSynchrotronMode, "Property for synchrotronMode")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        else:
            self._transmission = float(transmission)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'undulatorGap1' attribute
    def getUndulatorGap1(self): return self._undulatorGap1
    def setUndulatorGap1(self, undulatorGap1):
        if undulatorGap1 is None:
            self._undulatorGap1 = None
        else:
            self._undulatorGap1 = float(undulatorGap1)
    def delUndulatorGap1(self): self._undulatorGap1 = None
    undulatorGap1 = property(getUndulatorGap1, setUndulatorGap1, delUndulatorGap1, "Property for undulatorGap1")
    # Methods and properties for the 'undulatorGap2' attribute
    def getUndulatorGap2(self): return self._undulatorGap2
    def setUndulatorGap2(self, undulatorGap2):
        if undulatorGap2 is None:
            self._undulatorGap2 = None
        else:
            self._undulatorGap2 = float(undulatorGap2)
    def delUndulatorGap2(self): self._undulatorGap2 = None
    undulatorGap2 = property(getUndulatorGap2, setUndulatorGap2, delUndulatorGap2, "Property for undulatorGap2")
    # Methods and properties for the 'undulatorGap3' attribute
    def getUndulatorGap3(self): return self._undulatorGap3
    def setUndulatorGap3(self, undulatorGap3):
        if undulatorGap3 is None:
            self._undulatorGap3 = None
        else:
            self._undulatorGap3 = float(undulatorGap3)
    def delUndulatorGap3(self): self._undulatorGap3 = None
    undulatorGap3 = property(getUndulatorGap3, setUndulatorGap3, delUndulatorGap3, "Property for undulatorGap3")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        else:
            self._wavelength = float(wavelength)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'xbeam' attribute
    def getXbeam(self): return self._xbeam
    def setXbeam(self, xbeam):
        if xbeam is None:
            self._xbeam = None
        else:
            self._xbeam = float(xbeam)
    def delXbeam(self): self._xbeam = None
    xbeam = property(getXbeam, setXbeam, delXbeam, "Property for xbeam")
    # Methods and properties for the 'xtalSnapshotFullPath1' attribute
    def getXtalSnapshotFullPath1(self): return self._xtalSnapshotFullPath1
    def setXtalSnapshotFullPath1(self, xtalSnapshotFullPath1):
        self._xtalSnapshotFullPath1 = str(xtalSnapshotFullPath1)
    def delXtalSnapshotFullPath1(self): self._xtalSnapshotFullPath1 = None
    xtalSnapshotFullPath1 = property(getXtalSnapshotFullPath1, setXtalSnapshotFullPath1, delXtalSnapshotFullPath1, "Property for xtalSnapshotFullPath1")
    # Methods and properties for the 'xtalSnapshotFullPath2' attribute
    def getXtalSnapshotFullPath2(self): return self._xtalSnapshotFullPath2
    def setXtalSnapshotFullPath2(self, xtalSnapshotFullPath2):
        self._xtalSnapshotFullPath2 = str(xtalSnapshotFullPath2)
    def delXtalSnapshotFullPath2(self): self._xtalSnapshotFullPath2 = None
    xtalSnapshotFullPath2 = property(getXtalSnapshotFullPath2, setXtalSnapshotFullPath2, delXtalSnapshotFullPath2, "Property for xtalSnapshotFullPath2")
    # Methods and properties for the 'xtalSnapshotFullPath3' attribute
    def getXtalSnapshotFullPath3(self): return self._xtalSnapshotFullPath3
    def setXtalSnapshotFullPath3(self, xtalSnapshotFullPath3):
        self._xtalSnapshotFullPath3 = str(xtalSnapshotFullPath3)
    def delXtalSnapshotFullPath3(self): self._xtalSnapshotFullPath3 = None
    xtalSnapshotFullPath3 = property(getXtalSnapshotFullPath3, setXtalSnapshotFullPath3, delXtalSnapshotFullPath3, "Property for xtalSnapshotFullPath3")
    # Methods and properties for the 'xtalSnapshotFullPath4' attribute
    def getXtalSnapshotFullPath4(self): return self._xtalSnapshotFullPath4
    def setXtalSnapshotFullPath4(self, xtalSnapshotFullPath4):
        self._xtalSnapshotFullPath4 = str(xtalSnapshotFullPath4)
    def delXtalSnapshotFullPath4(self): self._xtalSnapshotFullPath4 = None
    xtalSnapshotFullPath4 = property(getXtalSnapshotFullPath4, setXtalSnapshotFullPath4, delXtalSnapshotFullPath4, "Property for xtalSnapshotFullPath4")
    # Methods and properties for the 'ybeam' attribute
    def getYbeam(self): return self._ybeam
    def setYbeam(self, ybeam):
        if ybeam is None:
            self._ybeam = None
        else:
            self._ybeam = float(ybeam)
    def delYbeam(self): self._ybeam = None
    ybeam = property(getYbeam, setYbeam, delYbeam, "Property for ybeam")
    def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
        pass
        if self._actualCenteringPosition is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<actualCenteringPosition>%s</actualCenteringPosition>\n' % self._actualCenteringPosition))
        else:
            warnEmptyAttribute("actualCenteringPosition", "string")
        if self._averageTemperature is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<averageTemperature>%e</averageTemperature>\n' % self._averageTemperature))
        else:
            warnEmptyAttribute("averageTemperature", "float")
        if self._axisEnd is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisEnd>%e</axisEnd>\n' % self._axisEnd))
        else:
            warnEmptyAttribute("axisEnd", "float")
        if self._axisRange is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisRange>%e</axisRange>\n' % self._axisRange))
        else:
            warnEmptyAttribute("axisRange", "float")
        if self._axisStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisStart>%e</axisStart>\n' % self._axisStart))
        else:
            warnEmptyAttribute("axisStart", "float")
        if self._beamShape is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamShape>%s</beamShape>\n' % self._beamShape))
        else:
            warnEmptyAttribute("beamShape", "string")
        if self._beamSizeAtSampleX is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamSizeAtSampleX>%e</beamSizeAtSampleX>\n' % self._beamSizeAtSampleX))
        else:
            warnEmptyAttribute("beamSizeAtSampleX", "float")
        if self._beamSizeAtSampleY is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamSizeAtSampleY>%e</beamSizeAtSampleY>\n' % self._beamSizeAtSampleY))
        else:
            warnEmptyAttribute("beamSizeAtSampleY", "float")
        if self._centeringMethod is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<centeringMethod>%s</centeringMethod>\n' % self._centeringMethod))
        else:
            warnEmptyAttribute("centeringMethod", "string")
        if self._comments is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
        else:
            warnEmptyAttribute("comments", "string")
        if self._dataCollectionId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
        else:
            warnEmptyAttribute("dataCollectionId", "integer")
        if self._dataCollectionNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionNumber>%d</dataCollectionNumber>\n' % self._dataCollectionNumber))
        else:
            warnEmptyAttribute("dataCollectionNumber", "integer")
        if self._detector2theta is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detector2theta>%e</detector2theta>\n' % self._detector2theta))
        else:
            warnEmptyAttribute("detector2theta", "float")
        if self._detectorDistance is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detectorDistance>%e</detectorDistance>\n' % self._detectorDistance))
        else:
            warnEmptyAttribute("detectorDistance", "float")
        if self._detectorMode is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detectorMode>%s</detectorMode>\n' % self._detectorMode))
        else:
            warnEmptyAttribute("detectorMode", "string")
        if self._endTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<endTime>%s</endTime>\n' % self._endTime))
        else:
            warnEmptyAttribute("endTime", "string")
        if self._exposureTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<exposureTime>%e</exposureTime>\n' % self._exposureTime))
        else:
            warnEmptyAttribute("exposureTime", "float")
        if self._fileTemplate is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<fileTemplate>%s</fileTemplate>\n' % self._fileTemplate))
        else:
            warnEmptyAttribute("fileTemplate", "string")
        if self._flux is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<flux>%e</flux>\n' % self._flux))
        else:
            warnEmptyAttribute("flux", "float")
        if self._imageDirectory is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imageDirectory>%s</imageDirectory>\n' % self._imageDirectory))
        else:
            warnEmptyAttribute("imageDirectory", "string")
        if self._imagePrefix is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imagePrefix>%s</imagePrefix>\n' % self._imagePrefix))
        else:
            warnEmptyAttribute("imagePrefix", "string")
        if self._imageSuffix is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imageSuffix>%s</imageSuffix>\n' % self._imageSuffix))
        else:
            warnEmptyAttribute("imageSuffix", "string")
        if self._kappaStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<kappaStart>%e</kappaStart>\n' % self._kappaStart))
        else:
            warnEmptyAttribute("kappaStart", "float")
        if self._numberOfImages is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<numberOfImages>%d</numberOfImages>\n' % self._numberOfImages))
        else:
            warnEmptyAttribute("numberOfImages", "integer")
        if self._numberOfPasses is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<numberOfPasses>%d</numberOfPasses>\n' % self._numberOfPasses))
        else:
            warnEmptyAttribute("numberOfPasses", "integer")
        if self._omegaStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<omegaStart>%e</omegaStart>\n' % self._omegaStart))
        else:
            warnEmptyAttribute("omegaStart", "float")
        if self._overlap is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<overlap>%e</overlap>\n' % self._overlap))
        else:
            warnEmptyAttribute("overlap", "float")
        if self._phiStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<phiStart>%e</phiStart>\n' % self._phiStart))
        else:
            warnEmptyAttribute("phiStart", "float")
        if self._printableForReport is not None:
            showIndent(outfile, level)
            if self._printableForReport:
                outfile.write(unicode('<printableForReport>true</printableForReport>\n'))
            else:
                outfile.write(unicode('<printableForReport>false</printableForReport>\n'))
        else:
            warnEmptyAttribute("printableForReport", "boolean")
        if self._resolution is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolution>%e</resolution>\n' % self._resolution))
        else:
            warnEmptyAttribute("resolution", "float")
        if self._resolutionAtCorner is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolutionAtCorner>%e</resolutionAtCorner>\n' % self._resolutionAtCorner))
        else:
            warnEmptyAttribute("resolutionAtCorner", "float")
        if self._rotationAxis is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rotationAxis>%s</rotationAxis>\n' % self._rotationAxis))
        else:
            warnEmptyAttribute("rotationAxis", "string")
        if self._runStatus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<runStatus>%s</runStatus>\n' % self._runStatus))
        else:
            warnEmptyAttribute("runStatus", "string")
        if self._slitGapVertical is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<slitGapVertical>%e</slitGapVertical>\n' % self._slitGapVertical))
        else:
            warnEmptyAttribute("slitGapVertical", "float")
        if self._slitGapHorizontal is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<slitGapHorizontal>%e</slitGapHorizontal>\n' % self._slitGapHorizontal))
        else:
            warnEmptyAttribute("slitGapHorizontal", "float")
        if self._startImageNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self._startImageNumber))
        else:
            warnEmptyAttribute("startImageNumber", "integer")
        if self._strategySubWedgeOrigId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<strategySubWedgeOrigId>%d</strategySubWedgeOrigId>\n' % self._strategySubWedgeOrigId))
        if self._startTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<startTime>%s</startTime>\n' % self._startTime))
        else:
            warnEmptyAttribute("startTime", "string")
        if self._synchrotronMode is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<synchrotronMode>%s</synchrotronMode>\n' % self._synchrotronMode))
        else:
            warnEmptyAttribute("synchrotronMode", "string")
        if self._transmission is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<transmission>%e</transmission>\n' % self._transmission))
        else:
            warnEmptyAttribute("transmission", "float")
        if self._undulatorGap1 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap1>%e</undulatorGap1>\n' % self._undulatorGap1))
        else:
            warnEmptyAttribute("undulatorGap1", "float")
        if self._undulatorGap2 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap2>%e</undulatorGap2>\n' % self._undulatorGap2))
        else:
            warnEmptyAttribute("undulatorGap2", "float")
        if self._undulatorGap3 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap3>%e</undulatorGap3>\n' % self._undulatorGap3))
        else:
            warnEmptyAttribute("undulatorGap3", "float")
        if self._wavelength is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<wavelength>%e</wavelength>\n' % self._wavelength))
        else:
            warnEmptyAttribute("wavelength", "float")
        if self._xbeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xbeam>%e</xbeam>\n' % self._xbeam))
        else:
            warnEmptyAttribute("xbeam", "float")
        if self._xtalSnapshotFullPath1 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath1>%s</xtalSnapshotFullPath1>\n' % self._xtalSnapshotFullPath1))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath1", "string")
        if self._xtalSnapshotFullPath2 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath2>%s</xtalSnapshotFullPath2>\n' % self._xtalSnapshotFullPath2))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath2", "string")
        if self._xtalSnapshotFullPath3 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath3>%s</xtalSnapshotFullPath3>\n' % self._xtalSnapshotFullPath3))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath3", "string")
        if self._xtalSnapshotFullPath4 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath4>%s</xtalSnapshotFullPath4>\n' % self._xtalSnapshotFullPath4))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath4", "string")
        if self._ybeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ybeam>%e</ybeam>\n' % self._ybeam))
        else:
            warnEmptyAttribute("ybeam", "float")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'actualCenteringPosition':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._actualCenteringPosition = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageTemperature':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._averageTemperature = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisEnd':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisEnd = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisRange':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisRange = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShape':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._beamShape = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeAtSampleX':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamSizeAtSampleX = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeAtSampleY':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamSizeAtSampleY = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'centeringMethod':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._centeringMethod = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._comments = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector2theta':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._detector2theta = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._detectorDistance = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorMode':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._detectorMode = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._endTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._exposureTime = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileTemplate':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._fileTemplate = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._flux = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageDirectory':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imageDirectory = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePrefix':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imagePrefix = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageSuffix':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imageSuffix = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappaStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._kappaStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._numberOfImages = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfPasses':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._numberOfPasses = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omegaStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._omegaStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlap':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._overlap = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._phiStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'printableForReport':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('True', 'true', '1'):
                    ival_ = True
                elif sval_ in ('False', 'false', '0'):
                    ival_ = False
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self._printableForReport = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolution = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionAtCorner':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolutionAtCorner = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxis':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._rotationAxis = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'runStatus':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._runStatus = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitGapVertical':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._slitGapVertical = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitGapHorizontal':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._slitGapHorizontal = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startImageNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._startImageNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategySubWedgeOrigId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._strategySubWedgeOrigId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._startTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'synchrotronMode':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._synchrotronMode = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._transmission = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap3 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._wavelength = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xbeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._xbeam = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath1':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath1 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath2':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath2 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath3':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath3 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath4':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath4 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ybeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ybeam = fval_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBDataCollection


class XSDataISPyBDiffractionPlan(XSData):
    def __init__(self, numberOfPositions=None, kappaStrategyOption=None, strategyOption=None, requiredResolution=None, requiredMultiplicity=None, requiredCompleteness=None, forcedSpaceGroup=None, estimateRadiationDamage=None, complexity=None, anomalousData=None, aimedResolution=None, aimedMultiplicity=None, aimedIOverSigmaAtHighestResolution=None, aimedCompleteness=None, comments=None, preferredBeamSizeY=None, preferredBeamSizeX=None, anomalousScatterer=None, radiationSensitivity=None, screeningResolution=None, maximalResolution=None, oscillationRange=None, exposureTime=None, minimalResolution=None, observedResolution=None, experimentKind=None, xmlDocumentId=None, diffractionPlanId=None):
        XSData.__init__(self, )
        if diffractionPlanId is None:
            self._diffractionPlanId = None
        elif diffractionPlanId.__class__.__name__ == "XSDataInteger":
            self._diffractionPlanId = diffractionPlanId
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'diffractionPlanId' is not XSDataInteger but %s" % self._diffractionPlanId.__class__.__name__
            raise BaseException(strMessage)
        if xmlDocumentId is None:
            self._xmlDocumentId = None
        elif xmlDocumentId.__class__.__name__ == "XSDataInteger":
            self._xmlDocumentId = xmlDocumentId
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'xmlDocumentId' is not XSDataInteger but %s" % self._xmlDocumentId.__class__.__name__
            raise BaseException(strMessage)
        if experimentKind is None:
            self._experimentKind = None
        elif experimentKind.__class__.__name__ == "XSDataString":
            self._experimentKind = experimentKind
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'experimentKind' is not XSDataString but %s" % self._experimentKind.__class__.__name__
            raise BaseException(strMessage)
        if observedResolution is None:
            self._observedResolution = None
        elif observedResolution.__class__.__name__ == "XSDataDouble":
            self._observedResolution = observedResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'observedResolution' is not XSDataDouble but %s" % self._observedResolution.__class__.__name__
            raise BaseException(strMessage)
        if minimalResolution is None:
            self._minimalResolution = None
        elif minimalResolution.__class__.__name__ == "XSDataDouble":
            self._minimalResolution = minimalResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'minimalResolution' is not XSDataDouble but %s" % self._minimalResolution.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'exposureTime' is not XSDataDouble but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataDouble":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'oscillationRange' is not XSDataDouble but %s" % self._oscillationRange.__class__.__name__
            raise BaseException(strMessage)
        if maximalResolution is None:
            self._maximalResolution = None
        elif maximalResolution.__class__.__name__ == "XSDataDouble":
            self._maximalResolution = maximalResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'maximalResolution' is not XSDataDouble but %s" % self._maximalResolution.__class__.__name__
            raise BaseException(strMessage)
        if screeningResolution is None:
            self._screeningResolution = None
        elif screeningResolution.__class__.__name__ == "XSDataDouble":
            self._screeningResolution = screeningResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'screeningResolution' is not XSDataDouble but %s" % self._screeningResolution.__class__.__name__
            raise BaseException(strMessage)
        if radiationSensitivity is None:
            self._radiationSensitivity = None
        elif radiationSensitivity.__class__.__name__ == "XSDataDouble":
            self._radiationSensitivity = radiationSensitivity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'radiationSensitivity' is not XSDataDouble but %s" % self._radiationSensitivity.__class__.__name__
            raise BaseException(strMessage)
        if anomalousScatterer is None:
            self._anomalousScatterer = None
        elif anomalousScatterer.__class__.__name__ == "XSDataString":
            self._anomalousScatterer = anomalousScatterer
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'anomalousScatterer' is not XSDataString but %s" % self._anomalousScatterer.__class__.__name__
            raise BaseException(strMessage)
        if preferredBeamSizeX is None:
            self._preferredBeamSizeX = None
        elif preferredBeamSizeX.__class__.__name__ == "XSDataDouble":
            self._preferredBeamSizeX = preferredBeamSizeX
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'preferredBeamSizeX' is not XSDataDouble but %s" % self._preferredBeamSizeX.__class__.__name__
            raise BaseException(strMessage)
        if preferredBeamSizeY is None:
            self._preferredBeamSizeY = None
        elif preferredBeamSizeY.__class__.__name__ == "XSDataDouble":
            self._preferredBeamSizeY = preferredBeamSizeY
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'preferredBeamSizeY' is not XSDataDouble but %s" % self._preferredBeamSizeY.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if aimedCompleteness is None:
            self._aimedCompleteness = None
        elif aimedCompleteness.__class__.__name__ == "XSDataDouble":
            self._aimedCompleteness = aimedCompleteness
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'aimedCompleteness' is not XSDataDouble but %s" % self._aimedCompleteness.__class__.__name__
            raise BaseException(strMessage)
        if aimedIOverSigmaAtHighestResolution is None:
            self._aimedIOverSigmaAtHighestResolution = None
        elif aimedIOverSigmaAtHighestResolution.__class__.__name__ == "XSDataDouble":
            self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'aimedIOverSigmaAtHighestResolution' is not XSDataDouble but %s" % self._aimedIOverSigmaAtHighestResolution.__class__.__name__
            raise BaseException(strMessage)
        if aimedMultiplicity is None:
            self._aimedMultiplicity = None
        elif aimedMultiplicity.__class__.__name__ == "XSDataDouble":
            self._aimedMultiplicity = aimedMultiplicity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'aimedMultiplicity' is not XSDataDouble but %s" % self._aimedMultiplicity.__class__.__name__
            raise BaseException(strMessage)
        if aimedResolution is None:
            self._aimedResolution = None
        elif aimedResolution.__class__.__name__ == "XSDataDouble":
            self._aimedResolution = aimedResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'aimedResolution' is not XSDataDouble but %s" % self._aimedResolution.__class__.__name__
            raise BaseException(strMessage)
        if anomalousData is None:
            self._anomalousData = None
        elif anomalousData.__class__.__name__ == "XSDataBoolean":
            self._anomalousData = anomalousData
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'anomalousData' is not XSDataBoolean but %s" % self._anomalousData.__class__.__name__
            raise BaseException(strMessage)
        if complexity is None:
            self._complexity = None
        elif complexity.__class__.__name__ == "XSDataString":
            self._complexity = complexity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'complexity' is not XSDataString but %s" % self._complexity.__class__.__name__
            raise BaseException(strMessage)
        if estimateRadiationDamage is None:
            self._estimateRadiationDamage = None
        elif estimateRadiationDamage.__class__.__name__ == "XSDataBoolean":
            self._estimateRadiationDamage = estimateRadiationDamage
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'estimateRadiationDamage' is not XSDataBoolean but %s" % self._estimateRadiationDamage.__class__.__name__
            raise BaseException(strMessage)
        if forcedSpaceGroup is None:
            self._forcedSpaceGroup = None
        elif forcedSpaceGroup.__class__.__name__ == "XSDataString":
            self._forcedSpaceGroup = forcedSpaceGroup
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'forcedSpaceGroup' is not XSDataString but %s" % self._forcedSpaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if requiredCompleteness is None:
            self._requiredCompleteness = None
        elif requiredCompleteness.__class__.__name__ == "XSDataDouble":
            self._requiredCompleteness = requiredCompleteness
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'requiredCompleteness' is not XSDataDouble but %s" % self._requiredCompleteness.__class__.__name__
            raise BaseException(strMessage)
        if requiredMultiplicity is None:
            self._requiredMultiplicity = None
        elif requiredMultiplicity.__class__.__name__ == "XSDataDouble":
            self._requiredMultiplicity = requiredMultiplicity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'requiredMultiplicity' is not XSDataDouble but %s" % self._requiredMultiplicity.__class__.__name__
            raise BaseException(strMessage)
        if requiredResolution is None:
            self._requiredResolution = None
        elif requiredResolution.__class__.__name__ == "XSDataDouble":
            self._requiredResolution = requiredResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'requiredResolution' is not XSDataDouble but %s" % self._requiredResolution.__class__.__name__
            raise BaseException(strMessage)
        if strategyOption is None:
            self._strategyOption = None
        elif strategyOption.__class__.__name__ == "XSDataString":
            self._strategyOption = strategyOption
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'strategyOption' is not XSDataString but %s" % self._strategyOption.__class__.__name__
            raise BaseException(strMessage)
        if kappaStrategyOption is None:
            self._kappaStrategyOption = None
        elif kappaStrategyOption.__class__.__name__ == "XSDataString":
            self._kappaStrategyOption = kappaStrategyOption
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'kappaStrategyOption' is not XSDataString but %s" % self._kappaStrategyOption.__class__.__name__
            raise BaseException(strMessage)
        if numberOfPositions is None:
            self._numberOfPositions = None
        elif numberOfPositions.__class__.__name__ == "XSDataInteger":
            self._numberOfPositions = numberOfPositions
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan constructor argument 'numberOfPositions' is not XSDataInteger but %s" % self._numberOfPositions.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'diffractionPlanId' attribute
    def getDiffractionPlanId(self): return self._diffractionPlanId
    def setDiffractionPlanId(self, diffractionPlanId):
        if diffractionPlanId is None:
            self._diffractionPlanId = None
        elif diffractionPlanId.__class__.__name__ == "XSDataInteger":
            self._diffractionPlanId = diffractionPlanId
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setDiffractionPlanId argument is not XSDataInteger but %s" % diffractionPlanId.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionPlanId(self): self._diffractionPlanId = None
    diffractionPlanId = property(getDiffractionPlanId, setDiffractionPlanId, delDiffractionPlanId, "Property for diffractionPlanId")
    # Methods and properties for the 'xmlDocumentId' attribute
    def getXmlDocumentId(self): return self._xmlDocumentId
    def setXmlDocumentId(self, xmlDocumentId):
        if xmlDocumentId is None:
            self._xmlDocumentId = None
        elif xmlDocumentId.__class__.__name__ == "XSDataInteger":
            self._xmlDocumentId = xmlDocumentId
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setXmlDocumentId argument is not XSDataInteger but %s" % xmlDocumentId.__class__.__name__
            raise BaseException(strMessage)
    def delXmlDocumentId(self): self._xmlDocumentId = None
    xmlDocumentId = property(getXmlDocumentId, setXmlDocumentId, delXmlDocumentId, "Property for xmlDocumentId")
    # Methods and properties for the 'experimentKind' attribute
    def getExperimentKind(self): return self._experimentKind
    def setExperimentKind(self, experimentKind):
        if experimentKind is None:
            self._experimentKind = None
        elif experimentKind.__class__.__name__ == "XSDataString":
            self._experimentKind = experimentKind
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setExperimentKind argument is not XSDataString but %s" % experimentKind.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentKind(self): self._experimentKind = None
    experimentKind = property(getExperimentKind, setExperimentKind, delExperimentKind, "Property for experimentKind")
    # Methods and properties for the 'observedResolution' attribute
    def getObservedResolution(self): return self._observedResolution
    def setObservedResolution(self, observedResolution):
        if observedResolution is None:
            self._observedResolution = None
        elif observedResolution.__class__.__name__ == "XSDataDouble":
            self._observedResolution = observedResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setObservedResolution argument is not XSDataDouble but %s" % observedResolution.__class__.__name__
            raise BaseException(strMessage)
    def delObservedResolution(self): self._observedResolution = None
    observedResolution = property(getObservedResolution, setObservedResolution, delObservedResolution, "Property for observedResolution")
    # Methods and properties for the 'minimalResolution' attribute
    def getMinimalResolution(self): return self._minimalResolution
    def setMinimalResolution(self, minimalResolution):
        if minimalResolution is None:
            self._minimalResolution = None
        elif minimalResolution.__class__.__name__ == "XSDataDouble":
            self._minimalResolution = minimalResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setMinimalResolution argument is not XSDataDouble but %s" % minimalResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMinimalResolution(self): self._minimalResolution = None
    minimalResolution = property(getMinimalResolution, setMinimalResolution, delMinimalResolution, "Property for minimalResolution")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setExposureTime argument is not XSDataDouble but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'oscillationRange' attribute
    def getOscillationRange(self): return self._oscillationRange
    def setOscillationRange(self, oscillationRange):
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataDouble":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setOscillationRange argument is not XSDataDouble but %s" % oscillationRange.__class__.__name__
            raise BaseException(strMessage)
    def delOscillationRange(self): self._oscillationRange = None
    oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
    # Methods and properties for the 'maximalResolution' attribute
    def getMaximalResolution(self): return self._maximalResolution
    def setMaximalResolution(self, maximalResolution):
        if maximalResolution is None:
            self._maximalResolution = None
        elif maximalResolution.__class__.__name__ == "XSDataDouble":
            self._maximalResolution = maximalResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setMaximalResolution argument is not XSDataDouble but %s" % maximalResolution.__class__.__name__
            raise BaseException(strMessage)
    def delMaximalResolution(self): self._maximalResolution = None
    maximalResolution = property(getMaximalResolution, setMaximalResolution, delMaximalResolution, "Property for maximalResolution")
    # Methods and properties for the 'screeningResolution' attribute
    def getScreeningResolution(self): return self._screeningResolution
    def setScreeningResolution(self, screeningResolution):
        if screeningResolution is None:
            self._screeningResolution = None
        elif screeningResolution.__class__.__name__ == "XSDataDouble":
            self._screeningResolution = screeningResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setScreeningResolution argument is not XSDataDouble but %s" % screeningResolution.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningResolution(self): self._screeningResolution = None
    screeningResolution = property(getScreeningResolution, setScreeningResolution, delScreeningResolution, "Property for screeningResolution")
    # Methods and properties for the 'radiationSensitivity' attribute
    def getRadiationSensitivity(self): return self._radiationSensitivity
    def setRadiationSensitivity(self, radiationSensitivity):
        if radiationSensitivity is None:
            self._radiationSensitivity = None
        elif radiationSensitivity.__class__.__name__ == "XSDataDouble":
            self._radiationSensitivity = radiationSensitivity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setRadiationSensitivity argument is not XSDataDouble but %s" % radiationSensitivity.__class__.__name__
            raise BaseException(strMessage)
    def delRadiationSensitivity(self): self._radiationSensitivity = None
    radiationSensitivity = property(getRadiationSensitivity, setRadiationSensitivity, delRadiationSensitivity, "Property for radiationSensitivity")
    # Methods and properties for the 'anomalousScatterer' attribute
    def getAnomalousScatterer(self): return self._anomalousScatterer
    def setAnomalousScatterer(self, anomalousScatterer):
        if anomalousScatterer is None:
            self._anomalousScatterer = None
        elif anomalousScatterer.__class__.__name__ == "XSDataString":
            self._anomalousScatterer = anomalousScatterer
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAnomalousScatterer argument is not XSDataString but %s" % anomalousScatterer.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalousScatterer(self): self._anomalousScatterer = None
    anomalousScatterer = property(getAnomalousScatterer, setAnomalousScatterer, delAnomalousScatterer, "Property for anomalousScatterer")
    # Methods and properties for the 'preferredBeamSizeX' attribute
    def getPreferredBeamSizeX(self): return self._preferredBeamSizeX
    def setPreferredBeamSizeX(self, preferredBeamSizeX):
        if preferredBeamSizeX is None:
            self._preferredBeamSizeX = None
        elif preferredBeamSizeX.__class__.__name__ == "XSDataDouble":
            self._preferredBeamSizeX = preferredBeamSizeX
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setPreferredBeamSizeX argument is not XSDataDouble but %s" % preferredBeamSizeX.__class__.__name__
            raise BaseException(strMessage)
    def delPreferredBeamSizeX(self): self._preferredBeamSizeX = None
    preferredBeamSizeX = property(getPreferredBeamSizeX, setPreferredBeamSizeX, delPreferredBeamSizeX, "Property for preferredBeamSizeX")
    # Methods and properties for the 'preferredBeamSizeY' attribute
    def getPreferredBeamSizeY(self): return self._preferredBeamSizeY
    def setPreferredBeamSizeY(self, preferredBeamSizeY):
        if preferredBeamSizeY is None:
            self._preferredBeamSizeY = None
        elif preferredBeamSizeY.__class__.__name__ == "XSDataDouble":
            self._preferredBeamSizeY = preferredBeamSizeY
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setPreferredBeamSizeY argument is not XSDataDouble but %s" % preferredBeamSizeY.__class__.__name__
            raise BaseException(strMessage)
    def delPreferredBeamSizeY(self): self._preferredBeamSizeY = None
    preferredBeamSizeY = property(getPreferredBeamSizeY, setPreferredBeamSizeY, delPreferredBeamSizeY, "Property for preferredBeamSizeY")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'aimedCompleteness' attribute
    def getAimedCompleteness(self): return self._aimedCompleteness
    def setAimedCompleteness(self, aimedCompleteness):
        if aimedCompleteness is None:
            self._aimedCompleteness = None
        elif aimedCompleteness.__class__.__name__ == "XSDataDouble":
            self._aimedCompleteness = aimedCompleteness
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAimedCompleteness argument is not XSDataDouble but %s" % aimedCompleteness.__class__.__name__
            raise BaseException(strMessage)
    def delAimedCompleteness(self): self._aimedCompleteness = None
    aimedCompleteness = property(getAimedCompleteness, setAimedCompleteness, delAimedCompleteness, "Property for aimedCompleteness")
    # Methods and properties for the 'aimedIOverSigmaAtHighestResolution' attribute
    def getAimedIOverSigmaAtHighestResolution(self): return self._aimedIOverSigmaAtHighestResolution
    def setAimedIOverSigmaAtHighestResolution(self, aimedIOverSigmaAtHighestResolution):
        if aimedIOverSigmaAtHighestResolution is None:
            self._aimedIOverSigmaAtHighestResolution = None
        elif aimedIOverSigmaAtHighestResolution.__class__.__name__ == "XSDataDouble":
            self._aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAimedIOverSigmaAtHighestResolution argument is not XSDataDouble but %s" % aimedIOverSigmaAtHighestResolution.__class__.__name__
            raise BaseException(strMessage)
    def delAimedIOverSigmaAtHighestResolution(self): self._aimedIOverSigmaAtHighestResolution = None
    aimedIOverSigmaAtHighestResolution = property(getAimedIOverSigmaAtHighestResolution, setAimedIOverSigmaAtHighestResolution, delAimedIOverSigmaAtHighestResolution, "Property for aimedIOverSigmaAtHighestResolution")
    # Methods and properties for the 'aimedMultiplicity' attribute
    def getAimedMultiplicity(self): return self._aimedMultiplicity
    def setAimedMultiplicity(self, aimedMultiplicity):
        if aimedMultiplicity is None:
            self._aimedMultiplicity = None
        elif aimedMultiplicity.__class__.__name__ == "XSDataDouble":
            self._aimedMultiplicity = aimedMultiplicity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAimedMultiplicity argument is not XSDataDouble but %s" % aimedMultiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delAimedMultiplicity(self): self._aimedMultiplicity = None
    aimedMultiplicity = property(getAimedMultiplicity, setAimedMultiplicity, delAimedMultiplicity, "Property for aimedMultiplicity")
    # Methods and properties for the 'aimedResolution' attribute
    def getAimedResolution(self): return self._aimedResolution
    def setAimedResolution(self, aimedResolution):
        if aimedResolution is None:
            self._aimedResolution = None
        elif aimedResolution.__class__.__name__ == "XSDataDouble":
            self._aimedResolution = aimedResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAimedResolution argument is not XSDataDouble but %s" % aimedResolution.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setAnomalousData argument is not XSDataBoolean but %s" % anomalousData.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalousData(self): self._anomalousData = None
    anomalousData = property(getAnomalousData, setAnomalousData, delAnomalousData, "Property for anomalousData")
    # Methods and properties for the 'complexity' attribute
    def getComplexity(self): return self._complexity
    def setComplexity(self, complexity):
        if complexity is None:
            self._complexity = None
        elif complexity.__class__.__name__ == "XSDataString":
            self._complexity = complexity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setComplexity argument is not XSDataString but %s" % complexity.__class__.__name__
            raise BaseException(strMessage)
    def delComplexity(self): self._complexity = None
    complexity = property(getComplexity, setComplexity, delComplexity, "Property for complexity")
    # Methods and properties for the 'estimateRadiationDamage' attribute
    def getEstimateRadiationDamage(self): return self._estimateRadiationDamage
    def setEstimateRadiationDamage(self, estimateRadiationDamage):
        if estimateRadiationDamage is None:
            self._estimateRadiationDamage = None
        elif estimateRadiationDamage.__class__.__name__ == "XSDataBoolean":
            self._estimateRadiationDamage = estimateRadiationDamage
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setEstimateRadiationDamage argument is not XSDataBoolean but %s" % estimateRadiationDamage.__class__.__name__
            raise BaseException(strMessage)
    def delEstimateRadiationDamage(self): self._estimateRadiationDamage = None
    estimateRadiationDamage = property(getEstimateRadiationDamage, setEstimateRadiationDamage, delEstimateRadiationDamage, "Property for estimateRadiationDamage")
    # Methods and properties for the 'forcedSpaceGroup' attribute
    def getForcedSpaceGroup(self): return self._forcedSpaceGroup
    def setForcedSpaceGroup(self, forcedSpaceGroup):
        if forcedSpaceGroup is None:
            self._forcedSpaceGroup = None
        elif forcedSpaceGroup.__class__.__name__ == "XSDataString":
            self._forcedSpaceGroup = forcedSpaceGroup
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setForcedSpaceGroup argument is not XSDataString but %s" % forcedSpaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delForcedSpaceGroup(self): self._forcedSpaceGroup = None
    forcedSpaceGroup = property(getForcedSpaceGroup, setForcedSpaceGroup, delForcedSpaceGroup, "Property for forcedSpaceGroup")
    # Methods and properties for the 'requiredCompleteness' attribute
    def getRequiredCompleteness(self): return self._requiredCompleteness
    def setRequiredCompleteness(self, requiredCompleteness):
        if requiredCompleteness is None:
            self._requiredCompleteness = None
        elif requiredCompleteness.__class__.__name__ == "XSDataDouble":
            self._requiredCompleteness = requiredCompleteness
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setRequiredCompleteness argument is not XSDataDouble but %s" % requiredCompleteness.__class__.__name__
            raise BaseException(strMessage)
    def delRequiredCompleteness(self): self._requiredCompleteness = None
    requiredCompleteness = property(getRequiredCompleteness, setRequiredCompleteness, delRequiredCompleteness, "Property for requiredCompleteness")
    # Methods and properties for the 'requiredMultiplicity' attribute
    def getRequiredMultiplicity(self): return self._requiredMultiplicity
    def setRequiredMultiplicity(self, requiredMultiplicity):
        if requiredMultiplicity is None:
            self._requiredMultiplicity = None
        elif requiredMultiplicity.__class__.__name__ == "XSDataDouble":
            self._requiredMultiplicity = requiredMultiplicity
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setRequiredMultiplicity argument is not XSDataDouble but %s" % requiredMultiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delRequiredMultiplicity(self): self._requiredMultiplicity = None
    requiredMultiplicity = property(getRequiredMultiplicity, setRequiredMultiplicity, delRequiredMultiplicity, "Property for requiredMultiplicity")
    # Methods and properties for the 'requiredResolution' attribute
    def getRequiredResolution(self): return self._requiredResolution
    def setRequiredResolution(self, requiredResolution):
        if requiredResolution is None:
            self._requiredResolution = None
        elif requiredResolution.__class__.__name__ == "XSDataDouble":
            self._requiredResolution = requiredResolution
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setRequiredResolution argument is not XSDataDouble but %s" % requiredResolution.__class__.__name__
            raise BaseException(strMessage)
    def delRequiredResolution(self): self._requiredResolution = None
    requiredResolution = property(getRequiredResolution, setRequiredResolution, delRequiredResolution, "Property for requiredResolution")
    # Methods and properties for the 'strategyOption' attribute
    def getStrategyOption(self): return self._strategyOption
    def setStrategyOption(self, strategyOption):
        if strategyOption is None:
            self._strategyOption = None
        elif strategyOption.__class__.__name__ == "XSDataString":
            self._strategyOption = strategyOption
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setStrategyOption argument is not XSDataString but %s" % strategyOption.__class__.__name__
            raise BaseException(strMessage)
    def delStrategyOption(self): self._strategyOption = None
    strategyOption = property(getStrategyOption, setStrategyOption, delStrategyOption, "Property for strategyOption")
    # Methods and properties for the 'kappaStrategyOption' attribute
    def getKappaStrategyOption(self): return self._kappaStrategyOption
    def setKappaStrategyOption(self, kappaStrategyOption):
        if kappaStrategyOption is None:
            self._kappaStrategyOption = None
        elif kappaStrategyOption.__class__.__name__ == "XSDataString":
            self._kappaStrategyOption = kappaStrategyOption
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setKappaStrategyOption argument is not XSDataString but %s" % kappaStrategyOption.__class__.__name__
            raise BaseException(strMessage)
    def delKappaStrategyOption(self): self._kappaStrategyOption = None
    kappaStrategyOption = property(getKappaStrategyOption, setKappaStrategyOption, delKappaStrategyOption, "Property for kappaStrategyOption")
    # Methods and properties for the 'numberOfPositions' attribute
    def getNumberOfPositions(self): return self._numberOfPositions
    def setNumberOfPositions(self, numberOfPositions):
        if numberOfPositions is None:
            self._numberOfPositions = None
        elif numberOfPositions.__class__.__name__ == "XSDataInteger":
            self._numberOfPositions = numberOfPositions
        else:
            strMessage = "ERROR! XSDataISPyBDiffractionPlan.setNumberOfPositions argument is not XSDataInteger but %s" % numberOfPositions.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfPositions(self): self._numberOfPositions = None
    numberOfPositions = property(getNumberOfPositions, setNumberOfPositions, delNumberOfPositions, "Property for numberOfPositions")
    def export(self, outfile, level, name_='XSDataISPyBDiffractionPlan'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBDiffractionPlan'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._diffractionPlanId is not None:
            self.diffractionPlanId.export(outfile, level, name_='diffractionPlanId')
        if self._xmlDocumentId is not None:
            self.xmlDocumentId.export(outfile, level, name_='xmlDocumentId')
        if self._experimentKind is not None:
            self.experimentKind.export(outfile, level, name_='experimentKind')
        if self._observedResolution is not None:
            self.observedResolution.export(outfile, level, name_='observedResolution')
        if self._minimalResolution is not None:
            self.minimalResolution.export(outfile, level, name_='minimalResolution')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self._oscillationRange is not None:
            self.oscillationRange.export(outfile, level, name_='oscillationRange')
        if self._maximalResolution is not None:
            self.maximalResolution.export(outfile, level, name_='maximalResolution')
        if self._screeningResolution is not None:
            self.screeningResolution.export(outfile, level, name_='screeningResolution')
        if self._radiationSensitivity is not None:
            self.radiationSensitivity.export(outfile, level, name_='radiationSensitivity')
        if self._anomalousScatterer is not None:
            self.anomalousScatterer.export(outfile, level, name_='anomalousScatterer')
        if self._preferredBeamSizeX is not None:
            self.preferredBeamSizeX.export(outfile, level, name_='preferredBeamSizeX')
        if self._preferredBeamSizeY is not None:
            self.preferredBeamSizeY.export(outfile, level, name_='preferredBeamSizeY')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._aimedCompleteness is not None:
            self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
        if self._aimedIOverSigmaAtHighestResolution is not None:
            self.aimedIOverSigmaAtHighestResolution.export(outfile, level, name_='aimedIOverSigmaAtHighestResolution')
        if self._aimedMultiplicity is not None:
            self.aimedMultiplicity.export(outfile, level, name_='aimedMultiplicity')
        if self._aimedResolution is not None:
            self.aimedResolution.export(outfile, level, name_='aimedResolution')
        if self._anomalousData is not None:
            self.anomalousData.export(outfile, level, name_='anomalousData')
        if self._complexity is not None:
            self.complexity.export(outfile, level, name_='complexity')
        if self._estimateRadiationDamage is not None:
            self.estimateRadiationDamage.export(outfile, level, name_='estimateRadiationDamage')
        if self._forcedSpaceGroup is not None:
            self.forcedSpaceGroup.export(outfile, level, name_='forcedSpaceGroup')
        if self._requiredCompleteness is not None:
            self.requiredCompleteness.export(outfile, level, name_='requiredCompleteness')
        if self._requiredMultiplicity is not None:
            self.requiredMultiplicity.export(outfile, level, name_='requiredMultiplicity')
        if self._requiredResolution is not None:
            self.requiredResolution.export(outfile, level, name_='requiredResolution')
        if self._strategyOption is not None:
            self.strategyOption.export(outfile, level, name_='strategyOption')
        if self._kappaStrategyOption is not None:
            self.kappaStrategyOption.export(outfile, level, name_='kappaStrategyOption')
        if self._numberOfPositions is not None:
            self.numberOfPositions.export(outfile, level, name_='numberOfPositions')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlanId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDiffractionPlanId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmlDocumentId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setXmlDocumentId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentKind':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setExperimentKind(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'observedResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setObservedResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimalResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMinimalResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationRange':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOscillationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maximalResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaximalResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setScreeningResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiationSensitivity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiationSensitivity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalousScatterer':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setAnomalousScatterer(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preferredBeamSizeX':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPreferredBeamSizeX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preferredBeamSizeY':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPreferredBeamSizeY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedCompleteness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedIOverSigmaAtHighestResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedIOverSigmaAtHighestResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedMultiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAimedMultiplicity(obj_)
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
            nodeName_ == 'complexity':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComplexity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'estimateRadiationDamage':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setEstimateRadiationDamage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedSpaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setForcedSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredCompleteness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRequiredCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredMultiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRequiredMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRequiredResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategyOption':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setStrategyOption(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappaStrategyOption':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setKappaStrategyOption(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfPositions':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfPositions(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBDiffractionPlan" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBDiffractionPlan' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBDiffractionPlan is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBDiffractionPlan.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDiffractionPlan()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBDiffractionPlan" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDiffractionPlan()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBDiffractionPlan


class XSDataISPyBImage(XSData):
    def __init__(self, temperature=None, synchrotronCurrent=None, measuredIntensity=None, machineMessage=None, jpegThumbnailFileFullPath=None, jpegFileFullPath=None, imageNumber=None, imageId=None, cumulativeIntensity=None, comments=None, fileName=None, fileLocation=None):
        XSData.__init__(self, )
        if fileLocation is None:
            self._fileLocation = None
        elif fileLocation.__class__.__name__ == "XSDataString":
            self._fileLocation = fileLocation
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'fileLocation' is not XSDataString but %s" % self._fileLocation.__class__.__name__
            raise BaseException(strMessage)
        if fileName is None:
            self._fileName = None
        elif fileName.__class__.__name__ == "XSDataString":
            self._fileName = fileName
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'fileName' is not XSDataString but %s" % self._fileName.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if cumulativeIntensity is None:
            self._cumulativeIntensity = None
        elif cumulativeIntensity.__class__.__name__ == "XSDataDouble":
            self._cumulativeIntensity = cumulativeIntensity
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'cumulativeIntensity' is not XSDataDouble but %s" % self._cumulativeIntensity.__class__.__name__
            raise BaseException(strMessage)
        if imageId is None:
            self._imageId = None
        elif imageId.__class__.__name__ == "XSDataInteger":
            self._imageId = imageId
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'imageId' is not XSDataInteger but %s" % self._imageId.__class__.__name__
            raise BaseException(strMessage)
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'imageNumber' is not XSDataInteger but %s" % self._imageNumber.__class__.__name__
            raise BaseException(strMessage)
        if jpegFileFullPath is None:
            self._jpegFileFullPath = None
        elif jpegFileFullPath.__class__.__name__ == "XSDataString":
            self._jpegFileFullPath = jpegFileFullPath
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'jpegFileFullPath' is not XSDataString but %s" % self._jpegFileFullPath.__class__.__name__
            raise BaseException(strMessage)
        if jpegThumbnailFileFullPath is None:
            self._jpegThumbnailFileFullPath = None
        elif jpegThumbnailFileFullPath.__class__.__name__ == "XSDataString":
            self._jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'jpegThumbnailFileFullPath' is not XSDataString but %s" % self._jpegThumbnailFileFullPath.__class__.__name__
            raise BaseException(strMessage)
        if machineMessage is None:
            self._machineMessage = None
        elif machineMessage.__class__.__name__ == "XSDataString":
            self._machineMessage = machineMessage
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'machineMessage' is not XSDataString but %s" % self._machineMessage.__class__.__name__
            raise BaseException(strMessage)
        if measuredIntensity is None:
            self._measuredIntensity = None
        elif measuredIntensity.__class__.__name__ == "XSDataDouble":
            self._measuredIntensity = measuredIntensity
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'measuredIntensity' is not XSDataDouble but %s" % self._measuredIntensity.__class__.__name__
            raise BaseException(strMessage)
        if synchrotronCurrent is None:
            self._synchrotronCurrent = None
        elif synchrotronCurrent.__class__.__name__ == "XSDataDouble":
            self._synchrotronCurrent = synchrotronCurrent
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'synchrotronCurrent' is not XSDataDouble but %s" % self._synchrotronCurrent.__class__.__name__
            raise BaseException(strMessage)
        if temperature is None:
            self._temperature = None
        elif temperature.__class__.__name__ == "XSDataDouble":
            self._temperature = temperature
        else:
            strMessage = "ERROR! XSDataISPyBImage constructor argument 'temperature' is not XSDataDouble but %s" % self._temperature.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fileLocation' attribute
    def getFileLocation(self): return self._fileLocation
    def setFileLocation(self, fileLocation):
        if fileLocation is None:
            self._fileLocation = None
        elif fileLocation.__class__.__name__ == "XSDataString":
            self._fileLocation = fileLocation
        else:
            strMessage = "ERROR! XSDataISPyBImage.setFileLocation argument is not XSDataString but %s" % fileLocation.__class__.__name__
            raise BaseException(strMessage)
    def delFileLocation(self): self._fileLocation = None
    fileLocation = property(getFileLocation, setFileLocation, delFileLocation, "Property for fileLocation")
    # Methods and properties for the 'fileName' attribute
    def getFileName(self): return self._fileName
    def setFileName(self, fileName):
        if fileName is None:
            self._fileName = None
        elif fileName.__class__.__name__ == "XSDataString":
            self._fileName = fileName
        else:
            strMessage = "ERROR! XSDataISPyBImage.setFileName argument is not XSDataString but %s" % fileName.__class__.__name__
            raise BaseException(strMessage)
    def delFileName(self): self._fileName = None
    fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBImage.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'cumulativeIntensity' attribute
    def getCumulativeIntensity(self): return self._cumulativeIntensity
    def setCumulativeIntensity(self, cumulativeIntensity):
        if cumulativeIntensity is None:
            self._cumulativeIntensity = None
        elif cumulativeIntensity.__class__.__name__ == "XSDataDouble":
            self._cumulativeIntensity = cumulativeIntensity
        else:
            strMessage = "ERROR! XSDataISPyBImage.setCumulativeIntensity argument is not XSDataDouble but %s" % cumulativeIntensity.__class__.__name__
            raise BaseException(strMessage)
    def delCumulativeIntensity(self): self._cumulativeIntensity = None
    cumulativeIntensity = property(getCumulativeIntensity, setCumulativeIntensity, delCumulativeIntensity, "Property for cumulativeIntensity")
    # Methods and properties for the 'imageId' attribute
    def getImageId(self): return self._imageId
    def setImageId(self, imageId):
        if imageId is None:
            self._imageId = None
        elif imageId.__class__.__name__ == "XSDataInteger":
            self._imageId = imageId
        else:
            strMessage = "ERROR! XSDataISPyBImage.setImageId argument is not XSDataInteger but %s" % imageId.__class__.__name__
            raise BaseException(strMessage)
    def delImageId(self): self._imageId = None
    imageId = property(getImageId, setImageId, delImageId, "Property for imageId")
    # Methods and properties for the 'imageNumber' attribute
    def getImageNumber(self): return self._imageNumber
    def setImageNumber(self, imageNumber):
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataISPyBImage.setImageNumber argument is not XSDataInteger but %s" % imageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delImageNumber(self): self._imageNumber = None
    imageNumber = property(getImageNumber, setImageNumber, delImageNumber, "Property for imageNumber")
    # Methods and properties for the 'jpegFileFullPath' attribute
    def getJpegFileFullPath(self): return self._jpegFileFullPath
    def setJpegFileFullPath(self, jpegFileFullPath):
        if jpegFileFullPath is None:
            self._jpegFileFullPath = None
        elif jpegFileFullPath.__class__.__name__ == "XSDataString":
            self._jpegFileFullPath = jpegFileFullPath
        else:
            strMessage = "ERROR! XSDataISPyBImage.setJpegFileFullPath argument is not XSDataString but %s" % jpegFileFullPath.__class__.__name__
            raise BaseException(strMessage)
    def delJpegFileFullPath(self): self._jpegFileFullPath = None
    jpegFileFullPath = property(getJpegFileFullPath, setJpegFileFullPath, delJpegFileFullPath, "Property for jpegFileFullPath")
    # Methods and properties for the 'jpegThumbnailFileFullPath' attribute
    def getJpegThumbnailFileFullPath(self): return self._jpegThumbnailFileFullPath
    def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath):
        if jpegThumbnailFileFullPath is None:
            self._jpegThumbnailFileFullPath = None
        elif jpegThumbnailFileFullPath.__class__.__name__ == "XSDataString":
            self._jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
        else:
            strMessage = "ERROR! XSDataISPyBImage.setJpegThumbnailFileFullPath argument is not XSDataString but %s" % jpegThumbnailFileFullPath.__class__.__name__
            raise BaseException(strMessage)
    def delJpegThumbnailFileFullPath(self): self._jpegThumbnailFileFullPath = None
    jpegThumbnailFileFullPath = property(getJpegThumbnailFileFullPath, setJpegThumbnailFileFullPath, delJpegThumbnailFileFullPath, "Property for jpegThumbnailFileFullPath")
    # Methods and properties for the 'machineMessage' attribute
    def getMachineMessage(self): return self._machineMessage
    def setMachineMessage(self, machineMessage):
        if machineMessage is None:
            self._machineMessage = None
        elif machineMessage.__class__.__name__ == "XSDataString":
            self._machineMessage = machineMessage
        else:
            strMessage = "ERROR! XSDataISPyBImage.setMachineMessage argument is not XSDataString but %s" % machineMessage.__class__.__name__
            raise BaseException(strMessage)
    def delMachineMessage(self): self._machineMessage = None
    machineMessage = property(getMachineMessage, setMachineMessage, delMachineMessage, "Property for machineMessage")
    # Methods and properties for the 'measuredIntensity' attribute
    def getMeasuredIntensity(self): return self._measuredIntensity
    def setMeasuredIntensity(self, measuredIntensity):
        if measuredIntensity is None:
            self._measuredIntensity = None
        elif measuredIntensity.__class__.__name__ == "XSDataDouble":
            self._measuredIntensity = measuredIntensity
        else:
            strMessage = "ERROR! XSDataISPyBImage.setMeasuredIntensity argument is not XSDataDouble but %s" % measuredIntensity.__class__.__name__
            raise BaseException(strMessage)
    def delMeasuredIntensity(self): self._measuredIntensity = None
    measuredIntensity = property(getMeasuredIntensity, setMeasuredIntensity, delMeasuredIntensity, "Property for measuredIntensity")
    # Methods and properties for the 'synchrotronCurrent' attribute
    def getSynchrotronCurrent(self): return self._synchrotronCurrent
    def setSynchrotronCurrent(self, synchrotronCurrent):
        if synchrotronCurrent is None:
            self._synchrotronCurrent = None
        elif synchrotronCurrent.__class__.__name__ == "XSDataDouble":
            self._synchrotronCurrent = synchrotronCurrent
        else:
            strMessage = "ERROR! XSDataISPyBImage.setSynchrotronCurrent argument is not XSDataDouble but %s" % synchrotronCurrent.__class__.__name__
            raise BaseException(strMessage)
    def delSynchrotronCurrent(self): self._synchrotronCurrent = None
    synchrotronCurrent = property(getSynchrotronCurrent, setSynchrotronCurrent, delSynchrotronCurrent, "Property for synchrotronCurrent")
    # Methods and properties for the 'temperature' attribute
    def getTemperature(self): return self._temperature
    def setTemperature(self, temperature):
        if temperature is None:
            self._temperature = None
        elif temperature.__class__.__name__ == "XSDataDouble":
            self._temperature = temperature
        else:
            strMessage = "ERROR! XSDataISPyBImage.setTemperature argument is not XSDataDouble but %s" % temperature.__class__.__name__
            raise BaseException(strMessage)
    def delTemperature(self): self._temperature = None
    temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
    def export(self, outfile, level, name_='XSDataISPyBImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBImage'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._fileLocation is not None:
            self.fileLocation.export(outfile, level, name_='fileLocation')
        else:
            warnEmptyAttribute("fileLocation", "XSDataString")
        if self._fileName is not None:
            self.fileName.export(outfile, level, name_='fileName')
        else:
            warnEmptyAttribute("fileName", "XSDataString")
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._cumulativeIntensity is not None:
            self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
        if self._imageId is not None:
            self.imageId.export(outfile, level, name_='imageId')
        if self._imageNumber is not None:
            self.imageNumber.export(outfile, level, name_='imageNumber')
        if self._jpegFileFullPath is not None:
            self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
        if self._jpegThumbnailFileFullPath is not None:
            self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
        if self._machineMessage is not None:
            self.machineMessage.export(outfile, level, name_='machineMessage')
        if self._measuredIntensity is not None:
            self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
        if self._synchrotronCurrent is not None:
            self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
        if self._temperature is not None:
            self.temperature.export(outfile, level, name_='temperature')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileLocation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFileLocation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileName':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cumulativeIntensity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCumulativeIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jpegFileFullPath':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setJpegFileFullPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jpegThumbnailFileFullPath':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setJpegThumbnailFileFullPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineMessage':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMachineMessage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'measuredIntensity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMeasuredIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'synchrotronCurrent':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSynchrotronCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'temperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTemperature(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBImage


class XSDataISPyBImageQualityIndicators(XSData):
    def __init__(self, totalIntegratedSignal=None, spotTotal=None, signalRangeMin=None, signalRangeMax=None, signalRangeAverage=None, saturationRangeMin=None, saturationRangeMax=None, saturationRangeAverage=None, pctSaturationTop50Peaks=None, method2Res=None, method1Res=None, maxUnitCell=None, inResolutionOvrlSpots=None, inResTotal=None, image=None, iceRings=None, goodBraggCandidates=None, binPopCutOffMethod2Res=None):
        XSData.__init__(self, )
        if binPopCutOffMethod2Res is None:
            self._binPopCutOffMethod2Res = None
        elif binPopCutOffMethod2Res.__class__.__name__ == "XSDataDouble":
            self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'binPopCutOffMethod2Res' is not XSDataDouble but %s" % self._binPopCutOffMethod2Res.__class__.__name__
            raise BaseException(strMessage)
        if goodBraggCandidates is None:
            self._goodBraggCandidates = None
        elif goodBraggCandidates.__class__.__name__ == "XSDataInteger":
            self._goodBraggCandidates = goodBraggCandidates
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'goodBraggCandidates' is not XSDataInteger but %s" % self._goodBraggCandidates.__class__.__name__
            raise BaseException(strMessage)
        if iceRings is None:
            self._iceRings = None
        elif iceRings.__class__.__name__ == "XSDataInteger":
            self._iceRings = iceRings
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'iceRings' is not XSDataInteger but %s" % self._iceRings.__class__.__name__
            raise BaseException(strMessage)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'image' is not XSDataImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if inResTotal is None:
            self._inResTotal = None
        elif inResTotal.__class__.__name__ == "XSDataInteger":
            self._inResTotal = inResTotal
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'inResTotal' is not XSDataInteger but %s" % self._inResTotal.__class__.__name__
            raise BaseException(strMessage)
        if inResolutionOvrlSpots is None:
            self._inResolutionOvrlSpots = None
        elif inResolutionOvrlSpots.__class__.__name__ == "XSDataInteger":
            self._inResolutionOvrlSpots = inResolutionOvrlSpots
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'inResolutionOvrlSpots' is not XSDataInteger but %s" % self._inResolutionOvrlSpots.__class__.__name__
            raise BaseException(strMessage)
        if maxUnitCell is None:
            self._maxUnitCell = None
        elif maxUnitCell.__class__.__name__ == "XSDataDouble":
            self._maxUnitCell = maxUnitCell
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'maxUnitCell' is not XSDataDouble but %s" % self._maxUnitCell.__class__.__name__
            raise BaseException(strMessage)
        if method1Res is None:
            self._method1Res = None
        elif method1Res.__class__.__name__ == "XSDataDouble":
            self._method1Res = method1Res
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'method1Res' is not XSDataDouble but %s" % self._method1Res.__class__.__name__
            raise BaseException(strMessage)
        if method2Res is None:
            self._method2Res = None
        elif method2Res.__class__.__name__ == "XSDataDouble":
            self._method2Res = method2Res
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'method2Res' is not XSDataDouble but %s" % self._method2Res.__class__.__name__
            raise BaseException(strMessage)
        if pctSaturationTop50Peaks is None:
            self._pctSaturationTop50Peaks = None
        elif pctSaturationTop50Peaks.__class__.__name__ == "XSDataDouble":
            self._pctSaturationTop50Peaks = pctSaturationTop50Peaks
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'pctSaturationTop50Peaks' is not XSDataDouble but %s" % self._pctSaturationTop50Peaks.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeAverage is None:
            self._saturationRangeAverage = None
        elif saturationRangeAverage.__class__.__name__ == "XSDataDouble":
            self._saturationRangeAverage = saturationRangeAverage
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'saturationRangeAverage' is not XSDataDouble but %s" % self._saturationRangeAverage.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeMax is None:
            self._saturationRangeMax = None
        elif saturationRangeMax.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMax = saturationRangeMax
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'saturationRangeMax' is not XSDataDouble but %s" % self._saturationRangeMax.__class__.__name__
            raise BaseException(strMessage)
        if saturationRangeMin is None:
            self._saturationRangeMin = None
        elif saturationRangeMin.__class__.__name__ == "XSDataDouble":
            self._saturationRangeMin = saturationRangeMin
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'saturationRangeMin' is not XSDataDouble but %s" % self._saturationRangeMin.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeAverage is None:
            self._signalRangeAverage = None
        elif signalRangeAverage.__class__.__name__ == "XSDataDouble":
            self._signalRangeAverage = signalRangeAverage
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'signalRangeAverage' is not XSDataDouble but %s" % self._signalRangeAverage.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeMax is None:
            self._signalRangeMax = None
        elif signalRangeMax.__class__.__name__ == "XSDataDouble":
            self._signalRangeMax = signalRangeMax
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'signalRangeMax' is not XSDataDouble but %s" % self._signalRangeMax.__class__.__name__
            raise BaseException(strMessage)
        if signalRangeMin is None:
            self._signalRangeMin = None
        elif signalRangeMin.__class__.__name__ == "XSDataDouble":
            self._signalRangeMin = signalRangeMin
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'signalRangeMin' is not XSDataDouble but %s" % self._signalRangeMin.__class__.__name__
            raise BaseException(strMessage)
        if spotTotal is None:
            self._spotTotal = None
        elif spotTotal.__class__.__name__ == "XSDataInteger":
            self._spotTotal = spotTotal
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'spotTotal' is not XSDataInteger but %s" % self._spotTotal.__class__.__name__
            raise BaseException(strMessage)
        if totalIntegratedSignal is None:
            self._totalIntegratedSignal = None
        elif totalIntegratedSignal.__class__.__name__ == "XSDataDouble":
            self._totalIntegratedSignal = totalIntegratedSignal
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators constructor argument 'totalIntegratedSignal' is not XSDataDouble but %s" % self._totalIntegratedSignal.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'binPopCutOffMethod2Res' attribute
    def getBinPopCutOffMethod2Res(self): return self._binPopCutOffMethod2Res
    def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res):
        if binPopCutOffMethod2Res is None:
            self._binPopCutOffMethod2Res = None
        elif binPopCutOffMethod2Res.__class__.__name__ == "XSDataDouble":
            self._binPopCutOffMethod2Res = binPopCutOffMethod2Res
        else:
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setBinPopCutOffMethod2Res argument is not XSDataDouble but %s" % binPopCutOffMethod2Res.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setGoodBraggCandidates argument is not XSDataInteger but %s" % goodBraggCandidates.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setIceRings argument is not XSDataInteger but %s" % iceRings.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setImage argument is not XSDataImage but %s" % image.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setInResTotal argument is not XSDataInteger but %s" % inResTotal.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setInResolutionOvrlSpots argument is not XSDataInteger but %s" % inResolutionOvrlSpots.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setMaxUnitCell argument is not XSDataDouble but %s" % maxUnitCell.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setMethod1Res argument is not XSDataDouble but %s" % method1Res.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setMethod2Res argument is not XSDataDouble but %s" % method2Res.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setPctSaturationTop50Peaks argument is not XSDataDouble but %s" % pctSaturationTop50Peaks.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSaturationRangeAverage argument is not XSDataDouble but %s" % saturationRangeAverage.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSaturationRangeMax argument is not XSDataDouble but %s" % saturationRangeMax.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSaturationRangeMin argument is not XSDataDouble but %s" % saturationRangeMin.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSignalRangeAverage argument is not XSDataDouble but %s" % signalRangeAverage.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSignalRangeMax argument is not XSDataDouble but %s" % signalRangeMax.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSignalRangeMin argument is not XSDataDouble but %s" % signalRangeMin.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setSpotTotal argument is not XSDataInteger but %s" % spotTotal.__class__.__name__
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
            strMessage = "ERROR! XSDataISPyBImageQualityIndicators.setTotalIntegratedSignal argument is not XSDataDouble but %s" % totalIntegratedSignal.__class__.__name__
            raise BaseException(strMessage)
    def delTotalIntegratedSignal(self): self._totalIntegratedSignal = None
    totalIntegratedSignal = property(getTotalIntegratedSignal, setTotalIntegratedSignal, delTotalIntegratedSignal, "Property for totalIntegratedSignal")
    def export(self, outfile, level, name_='XSDataISPyBImageQualityIndicators'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBImageQualityIndicators'):
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
        else:
            warnEmptyAttribute("maxUnitCell", "XSDataDouble")
        if self._method1Res is not None:
            self.method1Res.export(outfile, level, name_='method1Res')
        else:
            warnEmptyAttribute("method1Res", "XSDataDouble")
        if self._method2Res is not None:
            self.method2Res.export(outfile, level, name_='method2Res')
        else:
            warnEmptyAttribute("method2Res", "XSDataDouble")
        if self._pctSaturationTop50Peaks is not None:
            self.pctSaturationTop50Peaks.export(outfile, level, name_='pctSaturationTop50Peaks')
        else:
            warnEmptyAttribute("pctSaturationTop50Peaks", "XSDataDouble")
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
        self.export( oStreamString, 0, name_="XSDataISPyBImageQualityIndicators" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBImageQualityIndicators' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBImageQualityIndicators is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBImageQualityIndicators.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImageQualityIndicators()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBImageQualityIndicators" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImageQualityIndicators()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBImageQualityIndicators


class XSDataISPyBScreening(XSData):
    def __init__(self, xmlSampleInformation=None, shortComments=None, comments=None, programVersion=None, timeStamp=None, diffractionplanId=None, dataCollectionId=None, screeningId=None):
        XSData.__init__(self, )
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'screeningId' is not XSDataInteger but %s" % self._screeningId.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if diffractionplanId is None:
            self._diffractionplanId = None
        elif diffractionplanId.__class__.__name__ == "XSDataInteger":
            self._diffractionplanId = diffractionplanId
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'diffractionplanId' is not XSDataInteger but %s" % self._diffractionplanId.__class__.__name__
            raise BaseException(strMessage)
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataString":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'timeStamp' is not XSDataString but %s" % self._timeStamp.__class__.__name__
            raise BaseException(strMessage)
        if programVersion is None:
            self._programVersion = None
        elif programVersion.__class__.__name__ == "XSDataString":
            self._programVersion = programVersion
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'programVersion' is not XSDataString but %s" % self._programVersion.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if shortComments is None:
            self._shortComments = None
        elif shortComments.__class__.__name__ == "XSDataString":
            self._shortComments = shortComments
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'shortComments' is not XSDataString but %s" % self._shortComments.__class__.__name__
            raise BaseException(strMessage)
        if xmlSampleInformation is None:
            self._xmlSampleInformation = None
        elif xmlSampleInformation.__class__.__name__ == "XSDataString":
            self._xmlSampleInformation = xmlSampleInformation
        else:
            strMessage = "ERROR! XSDataISPyBScreening constructor argument 'xmlSampleInformation' is not XSDataString but %s" % self._xmlSampleInformation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningId' attribute
    def getScreeningId(self): return self._screeningId
    def setScreeningId(self, screeningId):
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setScreeningId argument is not XSDataInteger but %s" % screeningId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningId(self): self._screeningId = None
    screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'diffractionplanId' attribute
    def getDiffractionplanId(self): return self._diffractionplanId
    def setDiffractionplanId(self, diffractionplanId):
        if diffractionplanId is None:
            self._diffractionplanId = None
        elif diffractionplanId.__class__.__name__ == "XSDataInteger":
            self._diffractionplanId = diffractionplanId
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setDiffractionplanId argument is not XSDataInteger but %s" % diffractionplanId.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionplanId(self): self._diffractionplanId = None
    diffractionplanId = property(getDiffractionplanId, setDiffractionplanId, delDiffractionplanId, "Property for diffractionplanId")
    # Methods and properties for the 'timeStamp' attribute
    def getTimeStamp(self): return self._timeStamp
    def setTimeStamp(self, timeStamp):
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataString":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setTimeStamp argument is not XSDataString but %s" % timeStamp.__class__.__name__
            raise BaseException(strMessage)
    def delTimeStamp(self): self._timeStamp = None
    timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
    # Methods and properties for the 'programVersion' attribute
    def getProgramVersion(self): return self._programVersion
    def setProgramVersion(self, programVersion):
        if programVersion is None:
            self._programVersion = None
        elif programVersion.__class__.__name__ == "XSDataString":
            self._programVersion = programVersion
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setProgramVersion argument is not XSDataString but %s" % programVersion.__class__.__name__
            raise BaseException(strMessage)
    def delProgramVersion(self): self._programVersion = None
    programVersion = property(getProgramVersion, setProgramVersion, delProgramVersion, "Property for programVersion")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'shortComments' attribute
    def getShortComments(self): return self._shortComments
    def setShortComments(self, shortComments):
        if shortComments is None:
            self._shortComments = None
        elif shortComments.__class__.__name__ == "XSDataString":
            self._shortComments = shortComments
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setShortComments argument is not XSDataString but %s" % shortComments.__class__.__name__
            raise BaseException(strMessage)
    def delShortComments(self): self._shortComments = None
    shortComments = property(getShortComments, setShortComments, delShortComments, "Property for shortComments")
    # Methods and properties for the 'xmlSampleInformation' attribute
    def getXmlSampleInformation(self): return self._xmlSampleInformation
    def setXmlSampleInformation(self, xmlSampleInformation):
        if xmlSampleInformation is None:
            self._xmlSampleInformation = None
        elif xmlSampleInformation.__class__.__name__ == "XSDataString":
            self._xmlSampleInformation = xmlSampleInformation
        else:
            strMessage = "ERROR! XSDataISPyBScreening.setXmlSampleInformation argument is not XSDataString but %s" % xmlSampleInformation.__class__.__name__
            raise BaseException(strMessage)
    def delXmlSampleInformation(self): self._xmlSampleInformation = None
    xmlSampleInformation = property(getXmlSampleInformation, setXmlSampleInformation, delXmlSampleInformation, "Property for xmlSampleInformation")
    def export(self, outfile, level, name_='XSDataISPyBScreening'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreening'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningId is not None:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        else:
            warnEmptyAttribute("dataCollectionId", "XSDataInteger")
        if self._diffractionplanId is not None:
            self.diffractionplanId.export(outfile, level, name_='diffractionplanId')
        else:
            warnEmptyAttribute("diffractionplanId", "XSDataInteger")
        if self._timeStamp is not None:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        else:
            warnEmptyAttribute("timeStamp", "XSDataString")
        if self._programVersion is not None:
            self.programVersion.export(outfile, level, name_='programVersion')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._shortComments is not None:
            self.shortComments.export(outfile, level, name_='shortComments')
        if self._xmlSampleInformation is not None:
            self.xmlSampleInformation.export(outfile, level, name_='xmlSampleInformation')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionplanId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDiffractionplanId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setTimeStamp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'programVersion':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProgramVersion(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shortComments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setShortComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmlSampleInformation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setXmlSampleInformation(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreening" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreening' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreening is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreening.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreening()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreening" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreening()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreening


class XSDataISPyBScreeningFile(XSData):
    def __init__(self, timeStamp=None, description=None, filePath=None, fileName=None, fileType=None, screeningId=None, screeningFileId=None):
        XSData.__init__(self, )
        if screeningFileId is None:
            self._screeningFileId = None
        elif screeningFileId.__class__.__name__ == "XSDataInteger":
            self._screeningFileId = screeningFileId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'screeningFileId' is not XSDataInteger but %s" % self._screeningFileId.__class__.__name__
            raise BaseException(strMessage)
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'screeningId' is not XSDataInteger but %s" % self._screeningId.__class__.__name__
            raise BaseException(strMessage)
        if fileType is None:
            self._fileType = None
        elif fileType.__class__.__name__ == "XSDataString":
            self._fileType = fileType
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'fileType' is not XSDataString but %s" % self._fileType.__class__.__name__
            raise BaseException(strMessage)
        if fileName is None:
            self._fileName = None
        elif fileName.__class__.__name__ == "XSDataString":
            self._fileName = fileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'fileName' is not XSDataString but %s" % self._fileName.__class__.__name__
            raise BaseException(strMessage)
        if filePath is None:
            self._filePath = None
        elif filePath.__class__.__name__ == "XSDataString":
            self._filePath = filePath
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'filePath' is not XSDataString but %s" % self._filePath.__class__.__name__
            raise BaseException(strMessage)
        if description is None:
            self._description = None
        elif description.__class__.__name__ == "XSDataString":
            self._description = description
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'description' is not XSDataString but %s" % self._description.__class__.__name__
            raise BaseException(strMessage)
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataString":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile constructor argument 'timeStamp' is not XSDataString but %s" % self._timeStamp.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningFileId' attribute
    def getScreeningFileId(self): return self._screeningFileId
    def setScreeningFileId(self, screeningFileId):
        if screeningFileId is None:
            self._screeningFileId = None
        elif screeningFileId.__class__.__name__ == "XSDataInteger":
            self._screeningFileId = screeningFileId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setScreeningFileId argument is not XSDataInteger but %s" % screeningFileId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningFileId(self): self._screeningFileId = None
    screeningFileId = property(getScreeningFileId, setScreeningFileId, delScreeningFileId, "Property for screeningFileId")
    # Methods and properties for the 'screeningId' attribute
    def getScreeningId(self): return self._screeningId
    def setScreeningId(self, screeningId):
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setScreeningId argument is not XSDataInteger but %s" % screeningId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningId(self): self._screeningId = None
    screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
    # Methods and properties for the 'fileType' attribute
    def getFileType(self): return self._fileType
    def setFileType(self, fileType):
        if fileType is None:
            self._fileType = None
        elif fileType.__class__.__name__ == "XSDataString":
            self._fileType = fileType
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setFileType argument is not XSDataString but %s" % fileType.__class__.__name__
            raise BaseException(strMessage)
    def delFileType(self): self._fileType = None
    fileType = property(getFileType, setFileType, delFileType, "Property for fileType")
    # Methods and properties for the 'fileName' attribute
    def getFileName(self): return self._fileName
    def setFileName(self, fileName):
        if fileName is None:
            self._fileName = None
        elif fileName.__class__.__name__ == "XSDataString":
            self._fileName = fileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setFileName argument is not XSDataString but %s" % fileName.__class__.__name__
            raise BaseException(strMessage)
    def delFileName(self): self._fileName = None
    fileName = property(getFileName, setFileName, delFileName, "Property for fileName")
    # Methods and properties for the 'filePath' attribute
    def getFilePath(self): return self._filePath
    def setFilePath(self, filePath):
        if filePath is None:
            self._filePath = None
        elif filePath.__class__.__name__ == "XSDataString":
            self._filePath = filePath
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setFilePath argument is not XSDataString but %s" % filePath.__class__.__name__
            raise BaseException(strMessage)
    def delFilePath(self): self._filePath = None
    filePath = property(getFilePath, setFilePath, delFilePath, "Property for filePath")
    # Methods and properties for the 'description' attribute
    def getDescription(self): return self._description
    def setDescription(self, description):
        if description is None:
            self._description = None
        elif description.__class__.__name__ == "XSDataString":
            self._description = description
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setDescription argument is not XSDataString but %s" % description.__class__.__name__
            raise BaseException(strMessage)
    def delDescription(self): self._description = None
    description = property(getDescription, setDescription, delDescription, "Property for description")
    # Methods and properties for the 'timeStamp' attribute
    def getTimeStamp(self): return self._timeStamp
    def setTimeStamp(self, timeStamp):
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataString":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreeningFile.setTimeStamp argument is not XSDataString but %s" % timeStamp.__class__.__name__
            raise BaseException(strMessage)
    def delTimeStamp(self): self._timeStamp = None
    timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
    def export(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningFileId is not None:
            self.screeningFileId.export(outfile, level, name_='screeningFileId')
        if self._screeningId is not None:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self._fileType is not None:
            self.fileType.export(outfile, level, name_='fileType')
        if self._fileName is not None:
            self.fileName.export(outfile, level, name_='fileName')
        else:
            warnEmptyAttribute("fileName", "XSDataString")
        if self._filePath is not None:
            self.filePath.export(outfile, level, name_='filePath')
        else:
            warnEmptyAttribute("filePath", "XSDataString")
        if self._description is not None:
            self.description.export(outfile, level, name_='description')
        if self._timeStamp is not None:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        else:
            warnEmptyAttribute("timeStamp", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningFileId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningFileId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileType':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFileType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileName':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePath':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'description':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDescription(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setTimeStamp(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningFile


class XSDataISPyBScreeningOutput(XSData):
    def __init__(self, rFriedel=None, totalNumberOfImages=None, totalRotationRange=None, totalExposureTime=None, doseTotal=None, program=None, rankingResolution=None, mosaicityEstimated=None, strategySuccess=None, indexingSuccess=None, diffractionRings=None, iOverSigma=None, mosaicity=None, numSpotsRejected=None, numSpotsUsed=None, numSpotsFound=None, beamShiftY=None, beamShiftX=None, spotDeviationTheta=None, spotDeviationR=None, resolutionObtained=None, rejectedReflections=None, statusDescription=None, screeningId=None, screeningOutputId=None):
        XSData.__init__(self, )
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'screeningOutputId' is not XSDataInteger but %s" % self._screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'screeningId' is not XSDataInteger but %s" % self._screeningId.__class__.__name__
            raise BaseException(strMessage)
        if statusDescription is None:
            self._statusDescription = None
        elif statusDescription.__class__.__name__ == "XSDataString":
            self._statusDescription = statusDescription
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'statusDescription' is not XSDataString but %s" % self._statusDescription.__class__.__name__
            raise BaseException(strMessage)
        if rejectedReflections is None:
            self._rejectedReflections = None
        elif rejectedReflections.__class__.__name__ == "XSDataInteger":
            self._rejectedReflections = rejectedReflections
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'rejectedReflections' is not XSDataInteger but %s" % self._rejectedReflections.__class__.__name__
            raise BaseException(strMessage)
        if resolutionObtained is None:
            self._resolutionObtained = None
        elif resolutionObtained.__class__.__name__ == "XSDataDouble":
            self._resolutionObtained = resolutionObtained
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'resolutionObtained' is not XSDataDouble but %s" % self._resolutionObtained.__class__.__name__
            raise BaseException(strMessage)
        if spotDeviationR is None:
            self._spotDeviationR = None
        elif spotDeviationR.__class__.__name__ == "XSDataLength":
            self._spotDeviationR = spotDeviationR
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'spotDeviationR' is not XSDataLength but %s" % self._spotDeviationR.__class__.__name__
            raise BaseException(strMessage)
        if spotDeviationTheta is None:
            self._spotDeviationTheta = None
        elif spotDeviationTheta.__class__.__name__ == "XSDataAngle":
            self._spotDeviationTheta = spotDeviationTheta
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'spotDeviationTheta' is not XSDataAngle but %s" % self._spotDeviationTheta.__class__.__name__
            raise BaseException(strMessage)
        if beamShiftX is None:
            self._beamShiftX = None
        elif beamShiftX.__class__.__name__ == "XSDataLength":
            self._beamShiftX = beamShiftX
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'beamShiftX' is not XSDataLength but %s" % self._beamShiftX.__class__.__name__
            raise BaseException(strMessage)
        if beamShiftY is None:
            self._beamShiftY = None
        elif beamShiftY.__class__.__name__ == "XSDataLength":
            self._beamShiftY = beamShiftY
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'beamShiftY' is not XSDataLength but %s" % self._beamShiftY.__class__.__name__
            raise BaseException(strMessage)
        if numSpotsFound is None:
            self._numSpotsFound = None
        elif numSpotsFound.__class__.__name__ == "XSDataInteger":
            self._numSpotsFound = numSpotsFound
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'numSpotsFound' is not XSDataInteger but %s" % self._numSpotsFound.__class__.__name__
            raise BaseException(strMessage)
        if numSpotsUsed is None:
            self._numSpotsUsed = None
        elif numSpotsUsed.__class__.__name__ == "XSDataInteger":
            self._numSpotsUsed = numSpotsUsed
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'numSpotsUsed' is not XSDataInteger but %s" % self._numSpotsUsed.__class__.__name__
            raise BaseException(strMessage)
        if numSpotsRejected is None:
            self._numSpotsRejected = None
        elif numSpotsRejected.__class__.__name__ == "XSDataInteger":
            self._numSpotsRejected = numSpotsRejected
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'numSpotsRejected' is not XSDataInteger but %s" % self._numSpotsRejected.__class__.__name__
            raise BaseException(strMessage)
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataDouble":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'mosaicity' is not XSDataDouble but %s" % self._mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if iOverSigma is None:
            self._iOverSigma = None
        elif iOverSigma.__class__.__name__ == "XSDataDouble":
            self._iOverSigma = iOverSigma
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'iOverSigma' is not XSDataDouble but %s" % self._iOverSigma.__class__.__name__
            raise BaseException(strMessage)
        if diffractionRings is None:
            self._diffractionRings = None
        elif diffractionRings.__class__.__name__ == "XSDataBoolean":
            self._diffractionRings = diffractionRings
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'diffractionRings' is not XSDataBoolean but %s" % self._diffractionRings.__class__.__name__
            raise BaseException(strMessage)
        if indexingSuccess is None:
            self._indexingSuccess = None
        elif indexingSuccess.__class__.__name__ == "XSDataBoolean":
            self._indexingSuccess = indexingSuccess
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'indexingSuccess' is not XSDataBoolean but %s" % self._indexingSuccess.__class__.__name__
            raise BaseException(strMessage)
        if strategySuccess is None:
            self._strategySuccess = None
        elif strategySuccess.__class__.__name__ == "XSDataBoolean":
            self._strategySuccess = strategySuccess
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'strategySuccess' is not XSDataBoolean but %s" % self._strategySuccess.__class__.__name__
            raise BaseException(strMessage)
        if mosaicityEstimated is None:
            self._mosaicityEstimated = None
        elif mosaicityEstimated.__class__.__name__ == "XSDataBoolean":
            self._mosaicityEstimated = mosaicityEstimated
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'mosaicityEstimated' is not XSDataBoolean but %s" % self._mosaicityEstimated.__class__.__name__
            raise BaseException(strMessage)
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'rankingResolution' is not XSDataDouble but %s" % self._rankingResolution.__class__.__name__
            raise BaseException(strMessage)
        if program is None:
            self._program = None
        elif program.__class__.__name__ == "XSDataString":
            self._program = program
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'program' is not XSDataString but %s" % self._program.__class__.__name__
            raise BaseException(strMessage)
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'doseTotal' is not XSDataDouble but %s" % self._doseTotal.__class__.__name__
            raise BaseException(strMessage)
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataDouble":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'totalExposureTime' is not XSDataDouble but %s" % self._totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if totalRotationRange is None:
            self._totalRotationRange = None
        elif totalRotationRange.__class__.__name__ == "XSDataDouble":
            self._totalRotationRange = totalRotationRange
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'totalRotationRange' is not XSDataDouble but %s" % self._totalRotationRange.__class__.__name__
            raise BaseException(strMessage)
        if totalNumberOfImages is None:
            self._totalNumberOfImages = None
        elif totalNumberOfImages.__class__.__name__ == "XSDataInteger":
            self._totalNumberOfImages = totalNumberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'totalNumberOfImages' is not XSDataInteger but %s" % self._totalNumberOfImages.__class__.__name__
            raise BaseException(strMessage)
        if rFriedel is None:
            self._rFriedel = None
        elif rFriedel.__class__.__name__ == "XSDataDouble":
            self._rFriedel = rFriedel
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput constructor argument 'rFriedel' is not XSDataDouble but %s" % self._rFriedel.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningOutputId' attribute
    def getScreeningOutputId(self): return self._screeningOutputId
    def setScreeningOutputId(self, screeningOutputId):
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setScreeningOutputId argument is not XSDataInteger but %s" % screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputId(self): self._screeningOutputId = None
    screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
    # Methods and properties for the 'screeningId' attribute
    def getScreeningId(self): return self._screeningId
    def setScreeningId(self, screeningId):
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setScreeningId argument is not XSDataInteger but %s" % screeningId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningId(self): self._screeningId = None
    screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
    # Methods and properties for the 'statusDescription' attribute
    def getStatusDescription(self): return self._statusDescription
    def setStatusDescription(self, statusDescription):
        if statusDescription is None:
            self._statusDescription = None
        elif statusDescription.__class__.__name__ == "XSDataString":
            self._statusDescription = statusDescription
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setStatusDescription argument is not XSDataString but %s" % statusDescription.__class__.__name__
            raise BaseException(strMessage)
    def delStatusDescription(self): self._statusDescription = None
    statusDescription = property(getStatusDescription, setStatusDescription, delStatusDescription, "Property for statusDescription")
    # Methods and properties for the 'rejectedReflections' attribute
    def getRejectedReflections(self): return self._rejectedReflections
    def setRejectedReflections(self, rejectedReflections):
        if rejectedReflections is None:
            self._rejectedReflections = None
        elif rejectedReflections.__class__.__name__ == "XSDataInteger":
            self._rejectedReflections = rejectedReflections
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setRejectedReflections argument is not XSDataInteger but %s" % rejectedReflections.__class__.__name__
            raise BaseException(strMessage)
    def delRejectedReflections(self): self._rejectedReflections = None
    rejectedReflections = property(getRejectedReflections, setRejectedReflections, delRejectedReflections, "Property for rejectedReflections")
    # Methods and properties for the 'resolutionObtained' attribute
    def getResolutionObtained(self): return self._resolutionObtained
    def setResolutionObtained(self, resolutionObtained):
        if resolutionObtained is None:
            self._resolutionObtained = None
        elif resolutionObtained.__class__.__name__ == "XSDataDouble":
            self._resolutionObtained = resolutionObtained
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setResolutionObtained argument is not XSDataDouble but %s" % resolutionObtained.__class__.__name__
            raise BaseException(strMessage)
    def delResolutionObtained(self): self._resolutionObtained = None
    resolutionObtained = property(getResolutionObtained, setResolutionObtained, delResolutionObtained, "Property for resolutionObtained")
    # Methods and properties for the 'spotDeviationR' attribute
    def getSpotDeviationR(self): return self._spotDeviationR
    def setSpotDeviationR(self, spotDeviationR):
        if spotDeviationR is None:
            self._spotDeviationR = None
        elif spotDeviationR.__class__.__name__ == "XSDataLength":
            self._spotDeviationR = spotDeviationR
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setSpotDeviationR argument is not XSDataLength but %s" % spotDeviationR.__class__.__name__
            raise BaseException(strMessage)
    def delSpotDeviationR(self): self._spotDeviationR = None
    spotDeviationR = property(getSpotDeviationR, setSpotDeviationR, delSpotDeviationR, "Property for spotDeviationR")
    # Methods and properties for the 'spotDeviationTheta' attribute
    def getSpotDeviationTheta(self): return self._spotDeviationTheta
    def setSpotDeviationTheta(self, spotDeviationTheta):
        if spotDeviationTheta is None:
            self._spotDeviationTheta = None
        elif spotDeviationTheta.__class__.__name__ == "XSDataAngle":
            self._spotDeviationTheta = spotDeviationTheta
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setSpotDeviationTheta argument is not XSDataAngle but %s" % spotDeviationTheta.__class__.__name__
            raise BaseException(strMessage)
    def delSpotDeviationTheta(self): self._spotDeviationTheta = None
    spotDeviationTheta = property(getSpotDeviationTheta, setSpotDeviationTheta, delSpotDeviationTheta, "Property for spotDeviationTheta")
    # Methods and properties for the 'beamShiftX' attribute
    def getBeamShiftX(self): return self._beamShiftX
    def setBeamShiftX(self, beamShiftX):
        if beamShiftX is None:
            self._beamShiftX = None
        elif beamShiftX.__class__.__name__ == "XSDataLength":
            self._beamShiftX = beamShiftX
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setBeamShiftX argument is not XSDataLength but %s" % beamShiftX.__class__.__name__
            raise BaseException(strMessage)
    def delBeamShiftX(self): self._beamShiftX = None
    beamShiftX = property(getBeamShiftX, setBeamShiftX, delBeamShiftX, "Property for beamShiftX")
    # Methods and properties for the 'beamShiftY' attribute
    def getBeamShiftY(self): return self._beamShiftY
    def setBeamShiftY(self, beamShiftY):
        if beamShiftY is None:
            self._beamShiftY = None
        elif beamShiftY.__class__.__name__ == "XSDataLength":
            self._beamShiftY = beamShiftY
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setBeamShiftY argument is not XSDataLength but %s" % beamShiftY.__class__.__name__
            raise BaseException(strMessage)
    def delBeamShiftY(self): self._beamShiftY = None
    beamShiftY = property(getBeamShiftY, setBeamShiftY, delBeamShiftY, "Property for beamShiftY")
    # Methods and properties for the 'numSpotsFound' attribute
    def getNumSpotsFound(self): return self._numSpotsFound
    def setNumSpotsFound(self, numSpotsFound):
        if numSpotsFound is None:
            self._numSpotsFound = None
        elif numSpotsFound.__class__.__name__ == "XSDataInteger":
            self._numSpotsFound = numSpotsFound
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setNumSpotsFound argument is not XSDataInteger but %s" % numSpotsFound.__class__.__name__
            raise BaseException(strMessage)
    def delNumSpotsFound(self): self._numSpotsFound = None
    numSpotsFound = property(getNumSpotsFound, setNumSpotsFound, delNumSpotsFound, "Property for numSpotsFound")
    # Methods and properties for the 'numSpotsUsed' attribute
    def getNumSpotsUsed(self): return self._numSpotsUsed
    def setNumSpotsUsed(self, numSpotsUsed):
        if numSpotsUsed is None:
            self._numSpotsUsed = None
        elif numSpotsUsed.__class__.__name__ == "XSDataInteger":
            self._numSpotsUsed = numSpotsUsed
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setNumSpotsUsed argument is not XSDataInteger but %s" % numSpotsUsed.__class__.__name__
            raise BaseException(strMessage)
    def delNumSpotsUsed(self): self._numSpotsUsed = None
    numSpotsUsed = property(getNumSpotsUsed, setNumSpotsUsed, delNumSpotsUsed, "Property for numSpotsUsed")
    # Methods and properties for the 'numSpotsRejected' attribute
    def getNumSpotsRejected(self): return self._numSpotsRejected
    def setNumSpotsRejected(self, numSpotsRejected):
        if numSpotsRejected is None:
            self._numSpotsRejected = None
        elif numSpotsRejected.__class__.__name__ == "XSDataInteger":
            self._numSpotsRejected = numSpotsRejected
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setNumSpotsRejected argument is not XSDataInteger but %s" % numSpotsRejected.__class__.__name__
            raise BaseException(strMessage)
    def delNumSpotsRejected(self): self._numSpotsRejected = None
    numSpotsRejected = property(getNumSpotsRejected, setNumSpotsRejected, delNumSpotsRejected, "Property for numSpotsRejected")
    # Methods and properties for the 'mosaicity' attribute
    def getMosaicity(self): return self._mosaicity
    def setMosaicity(self, mosaicity):
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataDouble":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setMosaicity argument is not XSDataDouble but %s" % mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicity(self): self._mosaicity = None
    mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
    # Methods and properties for the 'iOverSigma' attribute
    def getIOverSigma(self): return self._iOverSigma
    def setIOverSigma(self, iOverSigma):
        if iOverSigma is None:
            self._iOverSigma = None
        elif iOverSigma.__class__.__name__ == "XSDataDouble":
            self._iOverSigma = iOverSigma
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setIOverSigma argument is not XSDataDouble but %s" % iOverSigma.__class__.__name__
            raise BaseException(strMessage)
    def delIOverSigma(self): self._iOverSigma = None
    iOverSigma = property(getIOverSigma, setIOverSigma, delIOverSigma, "Property for iOverSigma")
    # Methods and properties for the 'diffractionRings' attribute
    def getDiffractionRings(self): return self._diffractionRings
    def setDiffractionRings(self, diffractionRings):
        if diffractionRings is None:
            self._diffractionRings = None
        elif diffractionRings.__class__.__name__ == "XSDataBoolean":
            self._diffractionRings = diffractionRings
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setDiffractionRings argument is not XSDataBoolean but %s" % diffractionRings.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionRings(self): self._diffractionRings = None
    diffractionRings = property(getDiffractionRings, setDiffractionRings, delDiffractionRings, "Property for diffractionRings")
    # Methods and properties for the 'indexingSuccess' attribute
    def getIndexingSuccess(self): return self._indexingSuccess
    def setIndexingSuccess(self, indexingSuccess):
        if indexingSuccess is None:
            self._indexingSuccess = None
        elif indexingSuccess.__class__.__name__ == "XSDataBoolean":
            self._indexingSuccess = indexingSuccess
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setIndexingSuccess argument is not XSDataBoolean but %s" % indexingSuccess.__class__.__name__
            raise BaseException(strMessage)
    def delIndexingSuccess(self): self._indexingSuccess = None
    indexingSuccess = property(getIndexingSuccess, setIndexingSuccess, delIndexingSuccess, "Property for indexingSuccess")
    # Methods and properties for the 'strategySuccess' attribute
    def getStrategySuccess(self): return self._strategySuccess
    def setStrategySuccess(self, strategySuccess):
        if strategySuccess is None:
            self._strategySuccess = None
        elif strategySuccess.__class__.__name__ == "XSDataBoolean":
            self._strategySuccess = strategySuccess
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setStrategySuccess argument is not XSDataBoolean but %s" % strategySuccess.__class__.__name__
            raise BaseException(strMessage)
    def delStrategySuccess(self): self._strategySuccess = None
    strategySuccess = property(getStrategySuccess, setStrategySuccess, delStrategySuccess, "Property for strategySuccess")
    # Methods and properties for the 'mosaicityEstimated' attribute
    def getMosaicityEstimated(self): return self._mosaicityEstimated
    def setMosaicityEstimated(self, mosaicityEstimated):
        if mosaicityEstimated is None:
            self._mosaicityEstimated = None
        elif mosaicityEstimated.__class__.__name__ == "XSDataBoolean":
            self._mosaicityEstimated = mosaicityEstimated
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setMosaicityEstimated argument is not XSDataBoolean but %s" % mosaicityEstimated.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicityEstimated(self): self._mosaicityEstimated = None
    mosaicityEstimated = property(getMosaicityEstimated, setMosaicityEstimated, delMosaicityEstimated, "Property for mosaicityEstimated")
    # Methods and properties for the 'rankingResolution' attribute
    def getRankingResolution(self): return self._rankingResolution
    def setRankingResolution(self, rankingResolution):
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setRankingResolution argument is not XSDataDouble but %s" % rankingResolution.__class__.__name__
            raise BaseException(strMessage)
    def delRankingResolution(self): self._rankingResolution = None
    rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
    # Methods and properties for the 'program' attribute
    def getProgram(self): return self._program
    def setProgram(self, program):
        if program is None:
            self._program = None
        elif program.__class__.__name__ == "XSDataString":
            self._program = program
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setProgram argument is not XSDataString but %s" % program.__class__.__name__
            raise BaseException(strMessage)
    def delProgram(self): self._program = None
    program = property(getProgram, setProgram, delProgram, "Property for program")
    # Methods and properties for the 'doseTotal' attribute
    def getDoseTotal(self): return self._doseTotal
    def setDoseTotal(self, doseTotal):
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setDoseTotal argument is not XSDataDouble but %s" % doseTotal.__class__.__name__
            raise BaseException(strMessage)
    def delDoseTotal(self): self._doseTotal = None
    doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
    # Methods and properties for the 'totalExposureTime' attribute
    def getTotalExposureTime(self): return self._totalExposureTime
    def setTotalExposureTime(self, totalExposureTime):
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataDouble":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setTotalExposureTime argument is not XSDataDouble but %s" % totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delTotalExposureTime(self): self._totalExposureTime = None
    totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
    # Methods and properties for the 'totalRotationRange' attribute
    def getTotalRotationRange(self): return self._totalRotationRange
    def setTotalRotationRange(self, totalRotationRange):
        if totalRotationRange is None:
            self._totalRotationRange = None
        elif totalRotationRange.__class__.__name__ == "XSDataDouble":
            self._totalRotationRange = totalRotationRange
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setTotalRotationRange argument is not XSDataDouble but %s" % totalRotationRange.__class__.__name__
            raise BaseException(strMessage)
    def delTotalRotationRange(self): self._totalRotationRange = None
    totalRotationRange = property(getTotalRotationRange, setTotalRotationRange, delTotalRotationRange, "Property for totalRotationRange")
    # Methods and properties for the 'totalNumberOfImages' attribute
    def getTotalNumberOfImages(self): return self._totalNumberOfImages
    def setTotalNumberOfImages(self, totalNumberOfImages):
        if totalNumberOfImages is None:
            self._totalNumberOfImages = None
        elif totalNumberOfImages.__class__.__name__ == "XSDataInteger":
            self._totalNumberOfImages = totalNumberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setTotalNumberOfImages argument is not XSDataInteger but %s" % totalNumberOfImages.__class__.__name__
            raise BaseException(strMessage)
    def delTotalNumberOfImages(self): self._totalNumberOfImages = None
    totalNumberOfImages = property(getTotalNumberOfImages, setTotalNumberOfImages, delTotalNumberOfImages, "Property for totalNumberOfImages")
    # Methods and properties for the 'rFriedel' attribute
    def getRFriedel(self): return self._rFriedel
    def setRFriedel(self, rFriedel):
        if rFriedel is None:
            self._rFriedel = None
        elif rFriedel.__class__.__name__ == "XSDataDouble":
            self._rFriedel = rFriedel
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutput.setRFriedel argument is not XSDataDouble but %s" % rFriedel.__class__.__name__
            raise BaseException(strMessage)
    def delRFriedel(self): self._rFriedel = None
    rFriedel = property(getRFriedel, setRFriedel, delRFriedel, "Property for rFriedel")
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningOutputId is not None:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self._screeningId is not None:
            self.screeningId.export(outfile, level, name_='screeningId')
        else:
            warnEmptyAttribute("screeningId", "XSDataInteger")
        if self._statusDescription is not None:
            self.statusDescription.export(outfile, level, name_='statusDescription')
        if self._rejectedReflections is not None:
            self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
        if self._resolutionObtained is not None:
            self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
        if self._spotDeviationR is not None:
            self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
        if self._spotDeviationTheta is not None:
            self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
        if self._beamShiftX is not None:
            self.beamShiftX.export(outfile, level, name_='beamShiftX')
        if self._beamShiftY is not None:
            self.beamShiftY.export(outfile, level, name_='beamShiftY')
        if self._numSpotsFound is not None:
            self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
        if self._numSpotsUsed is not None:
            self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
        if self._numSpotsRejected is not None:
            self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
        if self._mosaicity is not None:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self._iOverSigma is not None:
            self.iOverSigma.export(outfile, level, name_='iOverSigma')
        if self._diffractionRings is not None:
            self.diffractionRings.export(outfile, level, name_='diffractionRings')
        if self._indexingSuccess is not None:
            self.indexingSuccess.export(outfile, level, name_='indexingSuccess')
        else:
            warnEmptyAttribute("indexingSuccess", "XSDataBoolean")
        if self._strategySuccess is not None:
            self.strategySuccess.export(outfile, level, name_='strategySuccess')
        else:
            warnEmptyAttribute("strategySuccess", "XSDataBoolean")
        if self._mosaicityEstimated is not None:
            self.mosaicityEstimated.export(outfile, level, name_='mosaicityEstimated')
        if self._rankingResolution is not None:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
        if self._program is not None:
            self.program.export(outfile, level, name_='program')
        if self._doseTotal is not None:
            self.doseTotal.export(outfile, level, name_='doseTotal')
        if self._totalExposureTime is not None:
            self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
        if self._totalRotationRange is not None:
            self.totalRotationRange.export(outfile, level, name_='totalRotationRange')
        if self._totalNumberOfImages is not None:
            self.totalNumberOfImages.export(outfile, level, name_='totalNumberOfImages')
        if self._rFriedel is not None:
            self.rFriedel.export(outfile, level, name_='rFriedel')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statusDescription':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setStatusDescription(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rejectedReflections':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRejectedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionObtained':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolutionObtained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationR':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setSpotDeviationR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationTheta':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setSpotDeviationTheta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShiftX':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamShiftX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShiftY':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamShiftY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsFound':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumSpotsFound(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumSpotsUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsRejected':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumSpotsRejected(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iOverSigma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionRings':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDiffractionRings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'indexingSuccess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setIndexingSuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategySuccess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setStrategySuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityEstimated':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setMosaicityEstimated(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRankingResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'program':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProgram(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseTotal':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalExposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotalExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalRotationRange':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotalRotationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalNumberOfImages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setTotalNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rFriedel':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRFriedel(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutput


class XSDataISPyBScreeningOutputLattice(XSData):
    def __init__(self, labelitIndexing=None, timeStamp=None, unitCell_gamma=None, unitCell_c=None, unitCell_beta=None, unitCell_b=None, unitCell_alpha=None, unitCell_a=None, rawOrientationMatrix_c_z=None, rawOrientationMatrix_c_y=None, rawOrientationMatrix_c_x=None, rawOrientationMatrix_b_z=None, rawOrientationMatrix_b_y=None, rawOrientationMatrix_b_x=None, rawOrientationMatrix_a_z=None, rawOrientationMatrix_a_y=None, rawOrientationMatrix_a_x=None, bravaisLattice=None, pointGroup=None, spaceGroup=None, screeningOutputId=None, screeningOutputLatticeId=None):
        XSData.__init__(self, )
        if screeningOutputLatticeId is None:
            self._screeningOutputLatticeId = None
        elif screeningOutputLatticeId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputLatticeId = screeningOutputLatticeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'screeningOutputLatticeId' is not XSDataInteger but %s" % self._screeningOutputLatticeId.__class__.__name__
            raise BaseException(strMessage)
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'screeningOutputId' is not XSDataInteger but %s" % self._screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if pointGroup is None:
            self._pointGroup = None
        elif pointGroup.__class__.__name__ == "XSDataString":
            self._pointGroup = pointGroup
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'pointGroup' is not XSDataString but %s" % self._pointGroup.__class__.__name__
            raise BaseException(strMessage)
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'bravaisLattice' is not XSDataString but %s" % self._bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_a_x is None:
            self._rawOrientationMatrix_a_x = None
        elif rawOrientationMatrix_a_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_a_x' is not XSDataDouble but %s" % self._rawOrientationMatrix_a_x.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_a_y is None:
            self._rawOrientationMatrix_a_y = None
        elif rawOrientationMatrix_a_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_a_y' is not XSDataDouble but %s" % self._rawOrientationMatrix_a_y.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_a_z is None:
            self._rawOrientationMatrix_a_z = None
        elif rawOrientationMatrix_a_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_a_z' is not XSDataDouble but %s" % self._rawOrientationMatrix_a_z.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_b_x is None:
            self._rawOrientationMatrix_b_x = None
        elif rawOrientationMatrix_b_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_b_x' is not XSDataDouble but %s" % self._rawOrientationMatrix_b_x.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_b_y is None:
            self._rawOrientationMatrix_b_y = None
        elif rawOrientationMatrix_b_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_b_y' is not XSDataDouble but %s" % self._rawOrientationMatrix_b_y.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_b_z is None:
            self._rawOrientationMatrix_b_z = None
        elif rawOrientationMatrix_b_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_b_z' is not XSDataDouble but %s" % self._rawOrientationMatrix_b_z.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_c_x is None:
            self._rawOrientationMatrix_c_x = None
        elif rawOrientationMatrix_c_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_c_x' is not XSDataDouble but %s" % self._rawOrientationMatrix_c_x.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_c_y is None:
            self._rawOrientationMatrix_c_y = None
        elif rawOrientationMatrix_c_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_c_y' is not XSDataDouble but %s" % self._rawOrientationMatrix_c_y.__class__.__name__
            raise BaseException(strMessage)
        if rawOrientationMatrix_c_z is None:
            self._rawOrientationMatrix_c_z = None
        elif rawOrientationMatrix_c_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'rawOrientationMatrix_c_z' is not XSDataDouble but %s" % self._rawOrientationMatrix_c_z.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_a is None:
            self._unitCell_a = None
        elif unitCell_a.__class__.__name__ == "XSDataLength":
            self._unitCell_a = unitCell_a
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_a' is not XSDataLength but %s" % self._unitCell_a.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_alpha is None:
            self._unitCell_alpha = None
        elif unitCell_alpha.__class__.__name__ == "XSDataAngle":
            self._unitCell_alpha = unitCell_alpha
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_alpha' is not XSDataAngle but %s" % self._unitCell_alpha.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_b is None:
            self._unitCell_b = None
        elif unitCell_b.__class__.__name__ == "XSDataLength":
            self._unitCell_b = unitCell_b
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_b' is not XSDataLength but %s" % self._unitCell_b.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_beta is None:
            self._unitCell_beta = None
        elif unitCell_beta.__class__.__name__ == "XSDataAngle":
            self._unitCell_beta = unitCell_beta
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_beta' is not XSDataAngle but %s" % self._unitCell_beta.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_c is None:
            self._unitCell_c = None
        elif unitCell_c.__class__.__name__ == "XSDataLength":
            self._unitCell_c = unitCell_c
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_c' is not XSDataLength but %s" % self._unitCell_c.__class__.__name__
            raise BaseException(strMessage)
        if unitCell_gamma is None:
            self._unitCell_gamma = None
        elif unitCell_gamma.__class__.__name__ == "XSDataAngle":
            self._unitCell_gamma = unitCell_gamma
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'unitCell_gamma' is not XSDataAngle but %s" % self._unitCell_gamma.__class__.__name__
            raise BaseException(strMessage)
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataLength":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'timeStamp' is not XSDataLength but %s" % self._timeStamp.__class__.__name__
            raise BaseException(strMessage)
        if labelitIndexing is None:
            self._labelitIndexing = None
        elif labelitIndexing.__class__.__name__ == "XSDataBoolean":
            self._labelitIndexing = labelitIndexing
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice constructor argument 'labelitIndexing' is not XSDataBoolean but %s" % self._labelitIndexing.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningOutputLatticeId' attribute
    def getScreeningOutputLatticeId(self): return self._screeningOutputLatticeId
    def setScreeningOutputLatticeId(self, screeningOutputLatticeId):
        if screeningOutputLatticeId is None:
            self._screeningOutputLatticeId = None
        elif screeningOutputLatticeId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputLatticeId = screeningOutputLatticeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setScreeningOutputLatticeId argument is not XSDataInteger but %s" % screeningOutputLatticeId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputLatticeId(self): self._screeningOutputLatticeId = None
    screeningOutputLatticeId = property(getScreeningOutputLatticeId, setScreeningOutputLatticeId, delScreeningOutputLatticeId, "Property for screeningOutputLatticeId")
    # Methods and properties for the 'screeningOutputId' attribute
    def getScreeningOutputId(self): return self._screeningOutputId
    def setScreeningOutputId(self, screeningOutputId):
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setScreeningOutputId argument is not XSDataInteger but %s" % screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputId(self): self._screeningOutputId = None
    screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpaceGroup(self): self._spaceGroup = None
    spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
    # Methods and properties for the 'pointGroup' attribute
    def getPointGroup(self): return self._pointGroup
    def setPointGroup(self, pointGroup):
        if pointGroup is None:
            self._pointGroup = None
        elif pointGroup.__class__.__name__ == "XSDataString":
            self._pointGroup = pointGroup
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setPointGroup argument is not XSDataString but %s" % pointGroup.__class__.__name__
            raise BaseException(strMessage)
    def delPointGroup(self): self._pointGroup = None
    pointGroup = property(getPointGroup, setPointGroup, delPointGroup, "Property for pointGroup")
    # Methods and properties for the 'bravaisLattice' attribute
    def getBravaisLattice(self): return self._bravaisLattice
    def setBravaisLattice(self, bravaisLattice):
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setBravaisLattice argument is not XSDataString but %s" % bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
    def delBravaisLattice(self): self._bravaisLattice = None
    bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
    # Methods and properties for the 'rawOrientationMatrix_a_x' attribute
    def getRawOrientationMatrix_a_x(self): return self._rawOrientationMatrix_a_x
    def setRawOrientationMatrix_a_x(self, rawOrientationMatrix_a_x):
        if rawOrientationMatrix_a_x is None:
            self._rawOrientationMatrix_a_x = None
        elif rawOrientationMatrix_a_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_a_x argument is not XSDataDouble but %s" % rawOrientationMatrix_a_x.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_a_x(self): self._rawOrientationMatrix_a_x = None
    rawOrientationMatrix_a_x = property(getRawOrientationMatrix_a_x, setRawOrientationMatrix_a_x, delRawOrientationMatrix_a_x, "Property for rawOrientationMatrix_a_x")
    # Methods and properties for the 'rawOrientationMatrix_a_y' attribute
    def getRawOrientationMatrix_a_y(self): return self._rawOrientationMatrix_a_y
    def setRawOrientationMatrix_a_y(self, rawOrientationMatrix_a_y):
        if rawOrientationMatrix_a_y is None:
            self._rawOrientationMatrix_a_y = None
        elif rawOrientationMatrix_a_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_a_y argument is not XSDataDouble but %s" % rawOrientationMatrix_a_y.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_a_y(self): self._rawOrientationMatrix_a_y = None
    rawOrientationMatrix_a_y = property(getRawOrientationMatrix_a_y, setRawOrientationMatrix_a_y, delRawOrientationMatrix_a_y, "Property for rawOrientationMatrix_a_y")
    # Methods and properties for the 'rawOrientationMatrix_a_z' attribute
    def getRawOrientationMatrix_a_z(self): return self._rawOrientationMatrix_a_z
    def setRawOrientationMatrix_a_z(self, rawOrientationMatrix_a_z):
        if rawOrientationMatrix_a_z is None:
            self._rawOrientationMatrix_a_z = None
        elif rawOrientationMatrix_a_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_a_z argument is not XSDataDouble but %s" % rawOrientationMatrix_a_z.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_a_z(self): self._rawOrientationMatrix_a_z = None
    rawOrientationMatrix_a_z = property(getRawOrientationMatrix_a_z, setRawOrientationMatrix_a_z, delRawOrientationMatrix_a_z, "Property for rawOrientationMatrix_a_z")
    # Methods and properties for the 'rawOrientationMatrix_b_x' attribute
    def getRawOrientationMatrix_b_x(self): return self._rawOrientationMatrix_b_x
    def setRawOrientationMatrix_b_x(self, rawOrientationMatrix_b_x):
        if rawOrientationMatrix_b_x is None:
            self._rawOrientationMatrix_b_x = None
        elif rawOrientationMatrix_b_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_b_x argument is not XSDataDouble but %s" % rawOrientationMatrix_b_x.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_b_x(self): self._rawOrientationMatrix_b_x = None
    rawOrientationMatrix_b_x = property(getRawOrientationMatrix_b_x, setRawOrientationMatrix_b_x, delRawOrientationMatrix_b_x, "Property for rawOrientationMatrix_b_x")
    # Methods and properties for the 'rawOrientationMatrix_b_y' attribute
    def getRawOrientationMatrix_b_y(self): return self._rawOrientationMatrix_b_y
    def setRawOrientationMatrix_b_y(self, rawOrientationMatrix_b_y):
        if rawOrientationMatrix_b_y is None:
            self._rawOrientationMatrix_b_y = None
        elif rawOrientationMatrix_b_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_b_y argument is not XSDataDouble but %s" % rawOrientationMatrix_b_y.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_b_y(self): self._rawOrientationMatrix_b_y = None
    rawOrientationMatrix_b_y = property(getRawOrientationMatrix_b_y, setRawOrientationMatrix_b_y, delRawOrientationMatrix_b_y, "Property for rawOrientationMatrix_b_y")
    # Methods and properties for the 'rawOrientationMatrix_b_z' attribute
    def getRawOrientationMatrix_b_z(self): return self._rawOrientationMatrix_b_z
    def setRawOrientationMatrix_b_z(self, rawOrientationMatrix_b_z):
        if rawOrientationMatrix_b_z is None:
            self._rawOrientationMatrix_b_z = None
        elif rawOrientationMatrix_b_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_b_z argument is not XSDataDouble but %s" % rawOrientationMatrix_b_z.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_b_z(self): self._rawOrientationMatrix_b_z = None
    rawOrientationMatrix_b_z = property(getRawOrientationMatrix_b_z, setRawOrientationMatrix_b_z, delRawOrientationMatrix_b_z, "Property for rawOrientationMatrix_b_z")
    # Methods and properties for the 'rawOrientationMatrix_c_x' attribute
    def getRawOrientationMatrix_c_x(self): return self._rawOrientationMatrix_c_x
    def setRawOrientationMatrix_c_x(self, rawOrientationMatrix_c_x):
        if rawOrientationMatrix_c_x is None:
            self._rawOrientationMatrix_c_x = None
        elif rawOrientationMatrix_c_x.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_c_x argument is not XSDataDouble but %s" % rawOrientationMatrix_c_x.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_c_x(self): self._rawOrientationMatrix_c_x = None
    rawOrientationMatrix_c_x = property(getRawOrientationMatrix_c_x, setRawOrientationMatrix_c_x, delRawOrientationMatrix_c_x, "Property for rawOrientationMatrix_c_x")
    # Methods and properties for the 'rawOrientationMatrix_c_y' attribute
    def getRawOrientationMatrix_c_y(self): return self._rawOrientationMatrix_c_y
    def setRawOrientationMatrix_c_y(self, rawOrientationMatrix_c_y):
        if rawOrientationMatrix_c_y is None:
            self._rawOrientationMatrix_c_y = None
        elif rawOrientationMatrix_c_y.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_c_y argument is not XSDataDouble but %s" % rawOrientationMatrix_c_y.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_c_y(self): self._rawOrientationMatrix_c_y = None
    rawOrientationMatrix_c_y = property(getRawOrientationMatrix_c_y, setRawOrientationMatrix_c_y, delRawOrientationMatrix_c_y, "Property for rawOrientationMatrix_c_y")
    # Methods and properties for the 'rawOrientationMatrix_c_z' attribute
    def getRawOrientationMatrix_c_z(self): return self._rawOrientationMatrix_c_z
    def setRawOrientationMatrix_c_z(self, rawOrientationMatrix_c_z):
        if rawOrientationMatrix_c_z is None:
            self._rawOrientationMatrix_c_z = None
        elif rawOrientationMatrix_c_z.__class__.__name__ == "XSDataDouble":
            self._rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setRawOrientationMatrix_c_z argument is not XSDataDouble but %s" % rawOrientationMatrix_c_z.__class__.__name__
            raise BaseException(strMessage)
    def delRawOrientationMatrix_c_z(self): self._rawOrientationMatrix_c_z = None
    rawOrientationMatrix_c_z = property(getRawOrientationMatrix_c_z, setRawOrientationMatrix_c_z, delRawOrientationMatrix_c_z, "Property for rawOrientationMatrix_c_z")
    # Methods and properties for the 'unitCell_a' attribute
    def getUnitCell_a(self): return self._unitCell_a
    def setUnitCell_a(self, unitCell_a):
        if unitCell_a is None:
            self._unitCell_a = None
        elif unitCell_a.__class__.__name__ == "XSDataLength":
            self._unitCell_a = unitCell_a
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_a argument is not XSDataLength but %s" % unitCell_a.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_a(self): self._unitCell_a = None
    unitCell_a = property(getUnitCell_a, setUnitCell_a, delUnitCell_a, "Property for unitCell_a")
    # Methods and properties for the 'unitCell_alpha' attribute
    def getUnitCell_alpha(self): return self._unitCell_alpha
    def setUnitCell_alpha(self, unitCell_alpha):
        if unitCell_alpha is None:
            self._unitCell_alpha = None
        elif unitCell_alpha.__class__.__name__ == "XSDataAngle":
            self._unitCell_alpha = unitCell_alpha
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_alpha argument is not XSDataAngle but %s" % unitCell_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_alpha(self): self._unitCell_alpha = None
    unitCell_alpha = property(getUnitCell_alpha, setUnitCell_alpha, delUnitCell_alpha, "Property for unitCell_alpha")
    # Methods and properties for the 'unitCell_b' attribute
    def getUnitCell_b(self): return self._unitCell_b
    def setUnitCell_b(self, unitCell_b):
        if unitCell_b is None:
            self._unitCell_b = None
        elif unitCell_b.__class__.__name__ == "XSDataLength":
            self._unitCell_b = unitCell_b
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_b argument is not XSDataLength but %s" % unitCell_b.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_b(self): self._unitCell_b = None
    unitCell_b = property(getUnitCell_b, setUnitCell_b, delUnitCell_b, "Property for unitCell_b")
    # Methods and properties for the 'unitCell_beta' attribute
    def getUnitCell_beta(self): return self._unitCell_beta
    def setUnitCell_beta(self, unitCell_beta):
        if unitCell_beta is None:
            self._unitCell_beta = None
        elif unitCell_beta.__class__.__name__ == "XSDataAngle":
            self._unitCell_beta = unitCell_beta
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_beta argument is not XSDataAngle but %s" % unitCell_beta.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_beta(self): self._unitCell_beta = None
    unitCell_beta = property(getUnitCell_beta, setUnitCell_beta, delUnitCell_beta, "Property for unitCell_beta")
    # Methods and properties for the 'unitCell_c' attribute
    def getUnitCell_c(self): return self._unitCell_c
    def setUnitCell_c(self, unitCell_c):
        if unitCell_c is None:
            self._unitCell_c = None
        elif unitCell_c.__class__.__name__ == "XSDataLength":
            self._unitCell_c = unitCell_c
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_c argument is not XSDataLength but %s" % unitCell_c.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_c(self): self._unitCell_c = None
    unitCell_c = property(getUnitCell_c, setUnitCell_c, delUnitCell_c, "Property for unitCell_c")
    # Methods and properties for the 'unitCell_gamma' attribute
    def getUnitCell_gamma(self): return self._unitCell_gamma
    def setUnitCell_gamma(self, unitCell_gamma):
        if unitCell_gamma is None:
            self._unitCell_gamma = None
        elif unitCell_gamma.__class__.__name__ == "XSDataAngle":
            self._unitCell_gamma = unitCell_gamma
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setUnitCell_gamma argument is not XSDataAngle but %s" % unitCell_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell_gamma(self): self._unitCell_gamma = None
    unitCell_gamma = property(getUnitCell_gamma, setUnitCell_gamma, delUnitCell_gamma, "Property for unitCell_gamma")
    # Methods and properties for the 'timeStamp' attribute
    def getTimeStamp(self): return self._timeStamp
    def setTimeStamp(self, timeStamp):
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataLength":
            self._timeStamp = timeStamp
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setTimeStamp argument is not XSDataLength but %s" % timeStamp.__class__.__name__
            raise BaseException(strMessage)
    def delTimeStamp(self): self._timeStamp = None
    timeStamp = property(getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp")
    # Methods and properties for the 'labelitIndexing' attribute
    def getLabelitIndexing(self): return self._labelitIndexing
    def setLabelitIndexing(self, labelitIndexing):
        if labelitIndexing is None:
            self._labelitIndexing = None
        elif labelitIndexing.__class__.__name__ == "XSDataBoolean":
            self._labelitIndexing = labelitIndexing
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputLattice.setLabelitIndexing argument is not XSDataBoolean but %s" % labelitIndexing.__class__.__name__
            raise BaseException(strMessage)
    def delLabelitIndexing(self): self._labelitIndexing = None
    labelitIndexing = property(getLabelitIndexing, setLabelitIndexing, delLabelitIndexing, "Property for labelitIndexing")
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningOutputLatticeId is not None:
            self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
        if self._screeningOutputId is not None:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        else:
            warnEmptyAttribute("screeningOutputId", "XSDataInteger")
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self._pointGroup is not None:
            self.pointGroup.export(outfile, level, name_='pointGroup')
        if self._bravaisLattice is not None:
            self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
        if self._rawOrientationMatrix_a_x is not None:
            self.rawOrientationMatrix_a_x.export(outfile, level, name_='rawOrientationMatrix_a_x')
        if self._rawOrientationMatrix_a_y is not None:
            self.rawOrientationMatrix_a_y.export(outfile, level, name_='rawOrientationMatrix_a_y')
        if self._rawOrientationMatrix_a_z is not None:
            self.rawOrientationMatrix_a_z.export(outfile, level, name_='rawOrientationMatrix_a_z')
        if self._rawOrientationMatrix_b_x is not None:
            self.rawOrientationMatrix_b_x.export(outfile, level, name_='rawOrientationMatrix_b_x')
        if self._rawOrientationMatrix_b_y is not None:
            self.rawOrientationMatrix_b_y.export(outfile, level, name_='rawOrientationMatrix_b_y')
        if self._rawOrientationMatrix_b_z is not None:
            self.rawOrientationMatrix_b_z.export(outfile, level, name_='rawOrientationMatrix_b_z')
        if self._rawOrientationMatrix_c_x is not None:
            self.rawOrientationMatrix_c_x.export(outfile, level, name_='rawOrientationMatrix_c_x')
        if self._rawOrientationMatrix_c_y is not None:
            self.rawOrientationMatrix_c_y.export(outfile, level, name_='rawOrientationMatrix_c_y')
        if self._rawOrientationMatrix_c_z is not None:
            self.rawOrientationMatrix_c_z.export(outfile, level, name_='rawOrientationMatrix_c_z')
        if self._unitCell_a is not None:
            self.unitCell_a.export(outfile, level, name_='unitCell_a')
        else:
            warnEmptyAttribute("unitCell_a", "XSDataLength")
        if self._unitCell_alpha is not None:
            self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
        else:
            warnEmptyAttribute("unitCell_alpha", "XSDataAngle")
        if self._unitCell_b is not None:
            self.unitCell_b.export(outfile, level, name_='unitCell_b')
        else:
            warnEmptyAttribute("unitCell_b", "XSDataLength")
        if self._unitCell_beta is not None:
            self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
        else:
            warnEmptyAttribute("unitCell_beta", "XSDataAngle")
        if self._unitCell_c is not None:
            self.unitCell_c.export(outfile, level, name_='unitCell_c')
        else:
            warnEmptyAttribute("unitCell_c", "XSDataLength")
        if self._unitCell_gamma is not None:
            self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
        else:
            warnEmptyAttribute("unitCell_gamma", "XSDataAngle")
        if self._timeStamp is not None:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        else:
            warnEmptyAttribute("timeStamp", "XSDataLength")
        if self._labelitIndexing is not None:
            self.labelitIndexing.export(outfile, level, name_='labelitIndexing')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLatticeId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningOutputLatticeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPointGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bravaisLattice':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBravaisLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_x':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_y':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_z':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_x':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_y':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_z':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_x':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_y':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_z':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_a':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setUnitCell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_alpha':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setUnitCell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_b':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setUnitCell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_beta':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setUnitCell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_c':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setUnitCell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_gamma':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setUnitCell_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setTimeStamp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'labelitIndexing':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLabelitIndexing(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutputLattice' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningOutputLattice is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningOutputLattice.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputLattice()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputLattice()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutputLattice


class XSDataISPyBScreeningOutputContainer(XSData):
    def __init__(self, screeningStrategyContainer=None, screeningOutputLattice=None, screeningOutput=None):
        XSData.__init__(self, )
        if screeningOutput is None:
            self._screeningOutput = None
        elif screeningOutput.__class__.__name__ == "XSDataISPyBScreeningOutput":
            self._screeningOutput = screeningOutput
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer constructor argument 'screeningOutput' is not XSDataISPyBScreeningOutput but %s" % self._screeningOutput.__class__.__name__
            raise BaseException(strMessage)
        if screeningOutputLattice is None:
            self._screeningOutputLattice = []
        elif screeningOutputLattice.__class__.__name__ == "list":
            self._screeningOutputLattice = screeningOutputLattice
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer constructor argument 'screeningOutputLattice' is not list but %s" % self._screeningOutputLattice.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyContainer is None:
            self._screeningStrategyContainer = []
        elif screeningStrategyContainer.__class__.__name__ == "list":
            self._screeningStrategyContainer = screeningStrategyContainer
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer constructor argument 'screeningStrategyContainer' is not list but %s" % self._screeningStrategyContainer.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningOutput' attribute
    def getScreeningOutput(self): return self._screeningOutput
    def setScreeningOutput(self, screeningOutput):
        if screeningOutput is None:
            self._screeningOutput = None
        elif screeningOutput.__class__.__name__ == "XSDataISPyBScreeningOutput":
            self._screeningOutput = screeningOutput
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.setScreeningOutput argument is not XSDataISPyBScreeningOutput but %s" % screeningOutput.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutput(self): self._screeningOutput = None
    screeningOutput = property(getScreeningOutput, setScreeningOutput, delScreeningOutput, "Property for screeningOutput")
    # Methods and properties for the 'screeningOutputLattice' attribute
    def getScreeningOutputLattice(self): return self._screeningOutputLattice
    def setScreeningOutputLattice(self, screeningOutputLattice):
        if screeningOutputLattice is None:
            self._screeningOutputLattice = []
        elif screeningOutputLattice.__class__.__name__ == "list":
            self._screeningOutputLattice = screeningOutputLattice
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.setScreeningOutputLattice argument is not list but %s" % screeningOutputLattice.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputLattice(self): self._screeningOutputLattice = None
    screeningOutputLattice = property(getScreeningOutputLattice, setScreeningOutputLattice, delScreeningOutputLattice, "Property for screeningOutputLattice")
    def addScreeningOutputLattice(self, value):
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningOutputLattice argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningOutputLattice":
            self._screeningOutputLattice.append(value)
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningOutputLattice argument is not XSDataISPyBScreeningOutputLattice but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningOutputLattice(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.insertScreeningOutputLattice argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.insertScreeningOutputLattice argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningOutputLattice":
            self._screeningOutputLattice[index] = value
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningOutputLattice argument is not XSDataISPyBScreeningOutputLattice but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategyContainer' attribute
    def getScreeningStrategyContainer(self): return self._screeningStrategyContainer
    def setScreeningStrategyContainer(self, screeningStrategyContainer):
        if screeningStrategyContainer is None:
            self._screeningStrategyContainer = []
        elif screeningStrategyContainer.__class__.__name__ == "list":
            self._screeningStrategyContainer = screeningStrategyContainer
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.setScreeningStrategyContainer argument is not list but %s" % screeningStrategyContainer.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyContainer(self): self._screeningStrategyContainer = None
    screeningStrategyContainer = property(getScreeningStrategyContainer, setScreeningStrategyContainer, delScreeningStrategyContainer, "Property for screeningStrategyContainer")
    def addScreeningStrategyContainer(self, value):
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningStrategyContainer argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategyContainer":
            self._screeningStrategyContainer.append(value)
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningStrategyContainer argument is not XSDataISPyBScreeningStrategyContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningStrategyContainer(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.insertScreeningStrategyContainer argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.insertScreeningStrategyContainer argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategyContainer":
            self._screeningStrategyContainer[index] = value
        else:
            strMessage = "ERROR! XSDataISPyBScreeningOutputContainer.addScreeningStrategyContainer argument is not XSDataISPyBScreeningStrategyContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningOutput is not None:
            self.screeningOutput.export(outfile, level, name_='screeningOutput')
        else:
            warnEmptyAttribute("screeningOutput", "XSDataISPyBScreeningOutput")
        for screeningOutputLattice_ in self.getScreeningOutputLattice():
            screeningOutputLattice_.export(outfile, level, name_='screeningOutputLattice')
        for screeningStrategyContainer_ in self.getScreeningStrategyContainer():
            screeningStrategyContainer_.export(outfile, level, name_='screeningStrategyContainer')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutput':
            obj_ = XSDataISPyBScreeningOutput()
            obj_.build(child_)
            self.setScreeningOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLattice':
            obj_ = XSDataISPyBScreeningOutputLattice()
            obj_.build(child_)
            self.screeningOutputLattice.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyContainer':
            obj_ = XSDataISPyBScreeningStrategyContainer()
            obj_.build(child_)
            self.screeningStrategyContainer.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutputContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningOutputContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningOutputContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningOutputContainer


class XSDataISPyBScreeningRank(XSData):
    def __init__(self, rankInformation=None, rankValue=None, screeningId=None, screeningRankSetId=None, screeningRankId=None):
        XSData.__init__(self, )
        if screeningRankId is None:
            self._screeningRankId = None
        elif screeningRankId.__class__.__name__ == "XSDataInteger":
            self._screeningRankId = screeningRankId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank constructor argument 'screeningRankId' is not XSDataInteger but %s" % self._screeningRankId.__class__.__name__
            raise BaseException(strMessage)
        if screeningRankSetId is None:
            self._screeningRankSetId = None
        elif screeningRankSetId.__class__.__name__ == "XSDataInteger":
            self._screeningRankSetId = screeningRankSetId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank constructor argument 'screeningRankSetId' is not XSDataInteger but %s" % self._screeningRankSetId.__class__.__name__
            raise BaseException(strMessage)
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank constructor argument 'screeningId' is not XSDataInteger but %s" % self._screeningId.__class__.__name__
            raise BaseException(strMessage)
        if rankValue is None:
            self._rankValue = None
        elif rankValue.__class__.__name__ == "XSDataDouble":
            self._rankValue = rankValue
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank constructor argument 'rankValue' is not XSDataDouble but %s" % self._rankValue.__class__.__name__
            raise BaseException(strMessage)
        if rankInformation is None:
            self._rankInformation = None
        elif rankInformation.__class__.__name__ == "XSDataString":
            self._rankInformation = rankInformation
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank constructor argument 'rankInformation' is not XSDataString but %s" % self._rankInformation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningRankId' attribute
    def getScreeningRankId(self): return self._screeningRankId
    def setScreeningRankId(self, screeningRankId):
        if screeningRankId is None:
            self._screeningRankId = None
        elif screeningRankId.__class__.__name__ == "XSDataInteger":
            self._screeningRankId = screeningRankId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank.setScreeningRankId argument is not XSDataInteger but %s" % screeningRankId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningRankId(self): self._screeningRankId = None
    screeningRankId = property(getScreeningRankId, setScreeningRankId, delScreeningRankId, "Property for screeningRankId")
    # Methods and properties for the 'screeningRankSetId' attribute
    def getScreeningRankSetId(self): return self._screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId):
        if screeningRankSetId is None:
            self._screeningRankSetId = None
        elif screeningRankSetId.__class__.__name__ == "XSDataInteger":
            self._screeningRankSetId = screeningRankSetId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank.setScreeningRankSetId argument is not XSDataInteger but %s" % screeningRankSetId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningRankSetId(self): self._screeningRankSetId = None
    screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
    # Methods and properties for the 'screeningId' attribute
    def getScreeningId(self): return self._screeningId
    def setScreeningId(self, screeningId):
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank.setScreeningId argument is not XSDataInteger but %s" % screeningId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningId(self): self._screeningId = None
    screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
    # Methods and properties for the 'rankValue' attribute
    def getRankValue(self): return self._rankValue
    def setRankValue(self, rankValue):
        if rankValue is None:
            self._rankValue = None
        elif rankValue.__class__.__name__ == "XSDataDouble":
            self._rankValue = rankValue
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank.setRankValue argument is not XSDataDouble but %s" % rankValue.__class__.__name__
            raise BaseException(strMessage)
    def delRankValue(self): self._rankValue = None
    rankValue = property(getRankValue, setRankValue, delRankValue, "Property for rankValue")
    # Methods and properties for the 'rankInformation' attribute
    def getRankInformation(self): return self._rankInformation
    def setRankInformation(self, rankInformation):
        if rankInformation is None:
            self._rankInformation = None
        elif rankInformation.__class__.__name__ == "XSDataString":
            self._rankInformation = rankInformation
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRank.setRankInformation argument is not XSDataString but %s" % rankInformation.__class__.__name__
            raise BaseException(strMessage)
    def delRankInformation(self): self._rankInformation = None
    rankInformation = property(getRankInformation, setRankInformation, delRankInformation, "Property for rankInformation")
    def export(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningRankId is not None:
            self.screeningRankId.export(outfile, level, name_='screeningRankId')
        if self._screeningRankSetId is not None:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        else:
            warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
        if self._screeningId is not None:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self._rankValue is not None:
            self.rankValue.export(outfile, level, name_='rankValue')
        else:
            warnEmptyAttribute("rankValue", "XSDataDouble")
        if self._rankInformation is not None:
            self.rankInformation.export(outfile, level, name_='rankInformation')
        else:
            warnEmptyAttribute("rankInformation", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningRankId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankValue':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRankValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankInformation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRankInformation(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningRank' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningRank is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningRank.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRank()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRank()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRank


class XSDataISPyBScreeningRankSet(XSData):
    def __init__(self, rankingSummaryFileName=None, rankingProjectFileName=None, rankEngine=None, screeningRankSetId=None):
        XSData.__init__(self, )
        if screeningRankSetId is None:
            self._screeningRankSetId = None
        elif screeningRankSetId.__class__.__name__ == "XSDataInteger":
            self._screeningRankSetId = screeningRankSetId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet constructor argument 'screeningRankSetId' is not XSDataInteger but %s" % self._screeningRankSetId.__class__.__name__
            raise BaseException(strMessage)
        if rankEngine is None:
            self._rankEngine = None
        elif rankEngine.__class__.__name__ == "XSDataString":
            self._rankEngine = rankEngine
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet constructor argument 'rankEngine' is not XSDataString but %s" % self._rankEngine.__class__.__name__
            raise BaseException(strMessage)
        if rankingProjectFileName is None:
            self._rankingProjectFileName = None
        elif rankingProjectFileName.__class__.__name__ == "XSDataString":
            self._rankingProjectFileName = rankingProjectFileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet constructor argument 'rankingProjectFileName' is not XSDataString but %s" % self._rankingProjectFileName.__class__.__name__
            raise BaseException(strMessage)
        if rankingSummaryFileName is None:
            self._rankingSummaryFileName = None
        elif rankingSummaryFileName.__class__.__name__ == "XSDataString":
            self._rankingSummaryFileName = rankingSummaryFileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet constructor argument 'rankingSummaryFileName' is not XSDataString but %s" % self._rankingSummaryFileName.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningRankSetId' attribute
    def getScreeningRankSetId(self): return self._screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId):
        if screeningRankSetId is None:
            self._screeningRankSetId = None
        elif screeningRankSetId.__class__.__name__ == "XSDataInteger":
            self._screeningRankSetId = screeningRankSetId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet.setScreeningRankSetId argument is not XSDataInteger but %s" % screeningRankSetId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningRankSetId(self): self._screeningRankSetId = None
    screeningRankSetId = property(getScreeningRankSetId, setScreeningRankSetId, delScreeningRankSetId, "Property for screeningRankSetId")
    # Methods and properties for the 'rankEngine' attribute
    def getRankEngine(self): return self._rankEngine
    def setRankEngine(self, rankEngine):
        if rankEngine is None:
            self._rankEngine = None
        elif rankEngine.__class__.__name__ == "XSDataString":
            self._rankEngine = rankEngine
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet.setRankEngine argument is not XSDataString but %s" % rankEngine.__class__.__name__
            raise BaseException(strMessage)
    def delRankEngine(self): self._rankEngine = None
    rankEngine = property(getRankEngine, setRankEngine, delRankEngine, "Property for rankEngine")
    # Methods and properties for the 'rankingProjectFileName' attribute
    def getRankingProjectFileName(self): return self._rankingProjectFileName
    def setRankingProjectFileName(self, rankingProjectFileName):
        if rankingProjectFileName is None:
            self._rankingProjectFileName = None
        elif rankingProjectFileName.__class__.__name__ == "XSDataString":
            self._rankingProjectFileName = rankingProjectFileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet.setRankingProjectFileName argument is not XSDataString but %s" % rankingProjectFileName.__class__.__name__
            raise BaseException(strMessage)
    def delRankingProjectFileName(self): self._rankingProjectFileName = None
    rankingProjectFileName = property(getRankingProjectFileName, setRankingProjectFileName, delRankingProjectFileName, "Property for rankingProjectFileName")
    # Methods and properties for the 'rankingSummaryFileName' attribute
    def getRankingSummaryFileName(self): return self._rankingSummaryFileName
    def setRankingSummaryFileName(self, rankingSummaryFileName):
        if rankingSummaryFileName is None:
            self._rankingSummaryFileName = None
        elif rankingSummaryFileName.__class__.__name__ == "XSDataString":
            self._rankingSummaryFileName = rankingSummaryFileName
        else:
            strMessage = "ERROR! XSDataISPyBScreeningRankSet.setRankingSummaryFileName argument is not XSDataString but %s" % rankingSummaryFileName.__class__.__name__
            raise BaseException(strMessage)
    def delRankingSummaryFileName(self): self._rankingSummaryFileName = None
    rankingSummaryFileName = property(getRankingSummaryFileName, setRankingSummaryFileName, delRankingSummaryFileName, "Property for rankingSummaryFileName")
    def export(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningRankSetId is not None:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        else:
            warnEmptyAttribute("screeningRankSetId", "XSDataInteger")
        if self._rankEngine is not None:
            self.rankEngine.export(outfile, level, name_='rankEngine')
        else:
            warnEmptyAttribute("rankEngine", "XSDataString")
        if self._rankingProjectFileName is not None:
            self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
        else:
            warnEmptyAttribute("rankingProjectFileName", "XSDataString")
        if self._rankingSummaryFileName is not None:
            self.rankingSummaryFileName.export(outfile, level, name_='rankingSummaryFileName')
        else:
            warnEmptyAttribute("rankingSummaryFileName", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankEngine':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRankEngine(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingProjectFileName':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRankingProjectFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingSummaryFileName':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRankingSummaryFileName(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningRankSet' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningRankSet is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningRankSet.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRankSet()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRankSet()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningRankSet


class XSDataISPyBScreeningStrategy(XSData):
    def __init__(self, transmission=None, rankingResolution=None, program=None, anomalous=None, multiplicity=None, completeness=None, resolution=None, exposureTime=None, rotation=None, phiEnd=None, phiStart=None, screeningOutputId=None, screeningStrategyId=None):
        XSData.__init__(self, )
        if screeningStrategyId is None:
            self._screeningStrategyId = None
        elif screeningStrategyId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyId = screeningStrategyId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'screeningStrategyId' is not XSDataInteger but %s" % self._screeningStrategyId.__class__.__name__
            raise BaseException(strMessage)
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'screeningOutputId' is not XSDataInteger but %s" % self._screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
        if phiStart is None:
            self._phiStart = None
        elif phiStart.__class__.__name__ == "XSDataDouble":
            self._phiStart = phiStart
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'phiStart' is not XSDataDouble but %s" % self._phiStart.__class__.__name__
            raise BaseException(strMessage)
        if phiEnd is None:
            self._phiEnd = None
        elif phiEnd.__class__.__name__ == "XSDataDouble":
            self._phiEnd = phiEnd
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'phiEnd' is not XSDataDouble but %s" % self._phiEnd.__class__.__name__
            raise BaseException(strMessage)
        if rotation is None:
            self._rotation = None
        elif rotation.__class__.__name__ == "XSDataDouble":
            self._rotation = rotation
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'rotation' is not XSDataDouble but %s" % self._rotation.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'exposureTime' is not XSDataDouble but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'completeness' is not XSDataDouble but %s" % self._completeness.__class__.__name__
            raise BaseException(strMessage)
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'multiplicity' is not XSDataDouble but %s" % self._multiplicity.__class__.__name__
            raise BaseException(strMessage)
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'anomalous' is not XSDataBoolean but %s" % self._anomalous.__class__.__name__
            raise BaseException(strMessage)
        if program is None:
            self._program = None
        elif program.__class__.__name__ == "XSDataString":
            self._program = program
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'program' is not XSDataString but %s" % self._program.__class__.__name__
            raise BaseException(strMessage)
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'rankingResolution' is not XSDataDouble but %s" % self._rankingResolution.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategyId' attribute
    def getScreeningStrategyId(self): return self._screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId):
        if screeningStrategyId is None:
            self._screeningStrategyId = None
        elif screeningStrategyId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyId = screeningStrategyId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setScreeningStrategyId argument is not XSDataInteger but %s" % screeningStrategyId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyId(self): self._screeningStrategyId = None
    screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
    # Methods and properties for the 'screeningOutputId' attribute
    def getScreeningOutputId(self): return self._screeningOutputId
    def setScreeningOutputId(self, screeningOutputId):
        if screeningOutputId is None:
            self._screeningOutputId = None
        elif screeningOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningOutputId = screeningOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setScreeningOutputId argument is not XSDataInteger but %s" % screeningOutputId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputId(self): self._screeningOutputId = None
    screeningOutputId = property(getScreeningOutputId, setScreeningOutputId, delScreeningOutputId, "Property for screeningOutputId")
    # Methods and properties for the 'phiStart' attribute
    def getPhiStart(self): return self._phiStart
    def setPhiStart(self, phiStart):
        if phiStart is None:
            self._phiStart = None
        elif phiStart.__class__.__name__ == "XSDataDouble":
            self._phiStart = phiStart
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setPhiStart argument is not XSDataDouble but %s" % phiStart.__class__.__name__
            raise BaseException(strMessage)
    def delPhiStart(self): self._phiStart = None
    phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
    # Methods and properties for the 'phiEnd' attribute
    def getPhiEnd(self): return self._phiEnd
    def setPhiEnd(self, phiEnd):
        if phiEnd is None:
            self._phiEnd = None
        elif phiEnd.__class__.__name__ == "XSDataDouble":
            self._phiEnd = phiEnd
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setPhiEnd argument is not XSDataDouble but %s" % phiEnd.__class__.__name__
            raise BaseException(strMessage)
    def delPhiEnd(self): self._phiEnd = None
    phiEnd = property(getPhiEnd, setPhiEnd, delPhiEnd, "Property for phiEnd")
    # Methods and properties for the 'rotation' attribute
    def getRotation(self): return self._rotation
    def setRotation(self, rotation):
        if rotation is None:
            self._rotation = None
        elif rotation.__class__.__name__ == "XSDataDouble":
            self._rotation = rotation
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setRotation argument is not XSDataDouble but %s" % rotation.__class__.__name__
            raise BaseException(strMessage)
    def delRotation(self): self._rotation = None
    rotation = property(getRotation, setRotation, delRotation, "Property for rotation")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataDouble":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setExposureTime argument is not XSDataDouble but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setCompleteness argument is not XSDataDouble but %s" % completeness.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setMultiplicity argument is not XSDataDouble but %s" % multiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delMultiplicity(self): self._multiplicity = None
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setAnomalous argument is not XSDataBoolean but %s" % anomalous.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    # Methods and properties for the 'program' attribute
    def getProgram(self): return self._program
    def setProgram(self, program):
        if program is None:
            self._program = None
        elif program.__class__.__name__ == "XSDataString":
            self._program = program
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setProgram argument is not XSDataString but %s" % program.__class__.__name__
            raise BaseException(strMessage)
    def delProgram(self): self._program = None
    program = property(getProgram, setProgram, delProgram, "Property for program")
    # Methods and properties for the 'rankingResolution' attribute
    def getRankingResolution(self): return self._rankingResolution
    def setRankingResolution(self, rankingResolution):
        if rankingResolution is None:
            self._rankingResolution = None
        elif rankingResolution.__class__.__name__ == "XSDataDouble":
            self._rankingResolution = rankingResolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setRankingResolution argument is not XSDataDouble but %s" % rankingResolution.__class__.__name__
            raise BaseException(strMessage)
    def delRankingResolution(self): self._rankingResolution = None
    rankingResolution = property(getRankingResolution, setRankingResolution, delRankingResolution, "Property for rankingResolution")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategy.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningStrategyId is not None:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        if self._screeningOutputId is not None:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        else:
            warnEmptyAttribute("screeningOutputId", "XSDataInteger")
        if self._phiStart is not None:
            self.phiStart.export(outfile, level, name_='phiStart')
        if self._phiEnd is not None:
            self.phiEnd.export(outfile, level, name_='phiEnd')
        if self._rotation is not None:
            self.rotation.export(outfile, level, name_='rotation')
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        if self._completeness is not None:
            self.completeness.export(outfile, level, name_='completeness')
        if self._multiplicity is not None:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self._anomalous is not None:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self._program is not None:
            self.program.export(outfile, level, name_='program')
        if self._rankingResolution is not None:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPhiStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiEnd':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPhiEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotation':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRotation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'program':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProgram(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRankingResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategy' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategy is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningStrategy.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategy()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategy()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategy


class XSDataISPyBScreeningStrategySubWedge(XSData):
    def __init__(self, comments=None, numberOfImages=None, doseTotal=None, multiplicity=None, completeness=None, oscillationRange=None, transmission=None, exposureTime=None, axisEnd=None, axisStart=None, rotationAxis=None, subWedgeNumber=None, screeningStrategyWedgeId=None, screeningStrategySubWedgeId=None):
        XSData.__init__(self, )
        if screeningStrategySubWedgeId is None:
            self._screeningStrategySubWedgeId = None
        elif screeningStrategySubWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategySubWedgeId = screeningStrategySubWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'screeningStrategySubWedgeId' is not XSDataInteger but %s" % self._screeningStrategySubWedgeId.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyWedgeId is None:
            self._screeningStrategyWedgeId = None
        elif screeningStrategyWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyWedgeId = screeningStrategyWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'screeningStrategyWedgeId' is not XSDataInteger but %s" % self._screeningStrategyWedgeId.__class__.__name__
            raise BaseException(strMessage)
        if subWedgeNumber is None:
            self._subWedgeNumber = None
        elif subWedgeNumber.__class__.__name__ == "XSDataInteger":
            self._subWedgeNumber = subWedgeNumber
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'subWedgeNumber' is not XSDataInteger but %s" % self._subWedgeNumber.__class__.__name__
            raise BaseException(strMessage)
        if rotationAxis is None:
            self._rotationAxis = None
        elif rotationAxis.__class__.__name__ == "XSDataString":
            self._rotationAxis = rotationAxis
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'rotationAxis' is not XSDataString but %s" % self._rotationAxis.__class__.__name__
            raise BaseException(strMessage)
        if axisStart is None:
            self._axisStart = None
        elif axisStart.__class__.__name__ == "XSDataAngle":
            self._axisStart = axisStart
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'axisStart' is not XSDataAngle but %s" % self._axisStart.__class__.__name__
            raise BaseException(strMessage)
        if axisEnd is None:
            self._axisEnd = None
        elif axisEnd.__class__.__name__ == "XSDataAngle":
            self._axisEnd = axisEnd
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'axisEnd' is not XSDataAngle but %s" % self._axisEnd.__class__.__name__
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'exposureTime' is not XSDataTime but %s" % self._exposureTime.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataAngle":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'oscillationRange' is not XSDataAngle but %s" % self._oscillationRange.__class__.__name__
            raise BaseException(strMessage)
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'completeness' is not XSDataDouble but %s" % self._completeness.__class__.__name__
            raise BaseException(strMessage)
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'multiplicity' is not XSDataDouble but %s" % self._multiplicity.__class__.__name__
            raise BaseException(strMessage)
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'doseTotal' is not XSDataDouble but %s" % self._doseTotal.__class__.__name__
            raise BaseException(strMessage)
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'numberOfImages' is not XSDataInteger but %s" % self._numberOfImages.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategySubWedgeId' attribute
    def getScreeningStrategySubWedgeId(self): return self._screeningStrategySubWedgeId
    def setScreeningStrategySubWedgeId(self, screeningStrategySubWedgeId):
        if screeningStrategySubWedgeId is None:
            self._screeningStrategySubWedgeId = None
        elif screeningStrategySubWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategySubWedgeId = screeningStrategySubWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setScreeningStrategySubWedgeId argument is not XSDataInteger but %s" % screeningStrategySubWedgeId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategySubWedgeId(self): self._screeningStrategySubWedgeId = None
    screeningStrategySubWedgeId = property(getScreeningStrategySubWedgeId, setScreeningStrategySubWedgeId, delScreeningStrategySubWedgeId, "Property for screeningStrategySubWedgeId")
    # Methods and properties for the 'screeningStrategyWedgeId' attribute
    def getScreeningStrategyWedgeId(self): return self._screeningStrategyWedgeId
    def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
        if screeningStrategyWedgeId is None:
            self._screeningStrategyWedgeId = None
        elif screeningStrategyWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyWedgeId = screeningStrategyWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setScreeningStrategyWedgeId argument is not XSDataInteger but %s" % screeningStrategyWedgeId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyWedgeId(self): self._screeningStrategyWedgeId = None
    screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
    # Methods and properties for the 'subWedgeNumber' attribute
    def getSubWedgeNumber(self): return self._subWedgeNumber
    def setSubWedgeNumber(self, subWedgeNumber):
        if subWedgeNumber is None:
            self._subWedgeNumber = None
        elif subWedgeNumber.__class__.__name__ == "XSDataInteger":
            self._subWedgeNumber = subWedgeNumber
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setSubWedgeNumber argument is not XSDataInteger but %s" % subWedgeNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSubWedgeNumber(self): self._subWedgeNumber = None
    subWedgeNumber = property(getSubWedgeNumber, setSubWedgeNumber, delSubWedgeNumber, "Property for subWedgeNumber")
    # Methods and properties for the 'rotationAxis' attribute
    def getRotationAxis(self): return self._rotationAxis
    def setRotationAxis(self, rotationAxis):
        if rotationAxis is None:
            self._rotationAxis = None
        elif rotationAxis.__class__.__name__ == "XSDataString":
            self._rotationAxis = rotationAxis
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setRotationAxis argument is not XSDataString but %s" % rotationAxis.__class__.__name__
            raise BaseException(strMessage)
    def delRotationAxis(self): self._rotationAxis = None
    rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
    # Methods and properties for the 'axisStart' attribute
    def getAxisStart(self): return self._axisStart
    def setAxisStart(self, axisStart):
        if axisStart is None:
            self._axisStart = None
        elif axisStart.__class__.__name__ == "XSDataAngle":
            self._axisStart = axisStart
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setAxisStart argument is not XSDataAngle but %s" % axisStart.__class__.__name__
            raise BaseException(strMessage)
    def delAxisStart(self): self._axisStart = None
    axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
    # Methods and properties for the 'axisEnd' attribute
    def getAxisEnd(self): return self._axisEnd
    def setAxisEnd(self, axisEnd):
        if axisEnd is None:
            self._axisEnd = None
        elif axisEnd.__class__.__name__ == "XSDataAngle":
            self._axisEnd = axisEnd
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setAxisEnd argument is not XSDataAngle but %s" % axisEnd.__class__.__name__
            raise BaseException(strMessage)
    def delAxisEnd(self): self._axisEnd = None
    axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setExposureTime argument is not XSDataTime but %s" % exposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'oscillationRange' attribute
    def getOscillationRange(self): return self._oscillationRange
    def setOscillationRange(self, oscillationRange):
        if oscillationRange is None:
            self._oscillationRange = None
        elif oscillationRange.__class__.__name__ == "XSDataAngle":
            self._oscillationRange = oscillationRange
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setOscillationRange argument is not XSDataAngle but %s" % oscillationRange.__class__.__name__
            raise BaseException(strMessage)
    def delOscillationRange(self): self._oscillationRange = None
    oscillationRange = property(getOscillationRange, setOscillationRange, delOscillationRange, "Property for oscillationRange")
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setCompleteness argument is not XSDataDouble but %s" % completeness.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setMultiplicity argument is not XSDataDouble but %s" % multiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delMultiplicity(self): self._multiplicity = None
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    # Methods and properties for the 'doseTotal' attribute
    def getDoseTotal(self): return self._doseTotal
    def setDoseTotal(self, doseTotal):
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setDoseTotal argument is not XSDataDouble but %s" % doseTotal.__class__.__name__
            raise BaseException(strMessage)
    def delDoseTotal(self): self._doseTotal = None
    doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setNumberOfImages argument is not XSDataInteger but %s" % numberOfImages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategySubWedge.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningStrategySubWedgeId is not None:
            self.screeningStrategySubWedgeId.export(outfile, level, name_='screeningStrategySubWedgeId')
        if self._screeningStrategyWedgeId is not None:
            self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
        else:
            warnEmptyAttribute("screeningStrategyWedgeId", "XSDataInteger")
        if self._subWedgeNumber is not None:
            self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
        else:
            warnEmptyAttribute("subWedgeNumber", "XSDataInteger")
        if self._rotationAxis is not None:
            self.rotationAxis.export(outfile, level, name_='rotationAxis')
        if self._axisStart is not None:
            self.axisStart.export(outfile, level, name_='axisStart')
        else:
            warnEmptyAttribute("axisStart", "XSDataAngle")
        if self._axisEnd is not None:
            self.axisEnd.export(outfile, level, name_='axisEnd')
        else:
            warnEmptyAttribute("axisEnd", "XSDataAngle")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        else:
            warnEmptyAttribute("exposureTime", "XSDataTime")
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
        if self._oscillationRange is not None:
            self.oscillationRange.export(outfile, level, name_='oscillationRange')
        else:
            warnEmptyAttribute("oscillationRange", "XSDataAngle")
        if self._completeness is not None:
            self.completeness.export(outfile, level, name_='completeness')
        if self._multiplicity is not None:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self._doseTotal is not None:
            self.doseTotal.export(outfile, level, name_='doseTotal')
        if self._numberOfImages is not None:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        else:
            warnEmptyAttribute("numberOfImages", "XSDataInteger")
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategySubWedgeId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategySubWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategyWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedgeNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSubWedgeNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxis':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRotationAxis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisStart':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAxisStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisEnd':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAxisEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationRange':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOscillationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseTotal':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategySubWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategySubWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategySubWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningStrategySubWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategySubWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategySubWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategySubWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategySubWedge


class XSDataISPyBScreeningStrategyWedge(XSData):
    def __init__(self, wavelength=None, comments=None, kappa=None, phi=None, numberOfImages=None, doseTotal=None, multiplicity=None, completeness=None, resolution=None, wedgeNumber=None, screeningStrategyOutputId=None, screeningStrategyId=None, screeningStrategyWedgeId=None):
        XSData.__init__(self, )
        if screeningStrategyWedgeId is None:
            self._screeningStrategyWedgeId = None
        elif screeningStrategyWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyWedgeId = screeningStrategyWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'screeningStrategyWedgeId' is not XSDataInteger but %s" % self._screeningStrategyWedgeId.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyId is None:
            self._screeningStrategyId = None
        elif screeningStrategyId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyId = screeningStrategyId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'screeningStrategyId' is not XSDataInteger but %s" % self._screeningStrategyId.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyOutputId is None:
            self._screeningStrategyOutputId = None
        elif screeningStrategyOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyOutputId = screeningStrategyOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'screeningStrategyOutputId' is not XSDataInteger but %s" % self._screeningStrategyOutputId.__class__.__name__
            raise BaseException(strMessage)
        if wedgeNumber is None:
            self._wedgeNumber = None
        elif wedgeNumber.__class__.__name__ == "XSDataInteger":
            self._wedgeNumber = wedgeNumber
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'wedgeNumber' is not XSDataInteger but %s" % self._wedgeNumber.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'completeness' is not XSDataDouble but %s" % self._completeness.__class__.__name__
            raise BaseException(strMessage)
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'multiplicity' is not XSDataDouble but %s" % self._multiplicity.__class__.__name__
            raise BaseException(strMessage)
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'doseTotal' is not XSDataDouble but %s" % self._doseTotal.__class__.__name__
            raise BaseException(strMessage)
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'numberOfImages' is not XSDataInteger but %s" % self._numberOfImages.__class__.__name__
            raise BaseException(strMessage)
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'phi' is not XSDataDouble but %s" % self._phi.__class__.__name__
            raise BaseException(strMessage)
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'kappa' is not XSDataDouble but %s" % self._kappa.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge constructor argument 'wavelength' is not XSDataDouble but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategyWedgeId' attribute
    def getScreeningStrategyWedgeId(self): return self._screeningStrategyWedgeId
    def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId):
        if screeningStrategyWedgeId is None:
            self._screeningStrategyWedgeId = None
        elif screeningStrategyWedgeId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyWedgeId = screeningStrategyWedgeId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setScreeningStrategyWedgeId argument is not XSDataInteger but %s" % screeningStrategyWedgeId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyWedgeId(self): self._screeningStrategyWedgeId = None
    screeningStrategyWedgeId = property(getScreeningStrategyWedgeId, setScreeningStrategyWedgeId, delScreeningStrategyWedgeId, "Property for screeningStrategyWedgeId")
    # Methods and properties for the 'screeningStrategyId' attribute
    def getScreeningStrategyId(self): return self._screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId):
        if screeningStrategyId is None:
            self._screeningStrategyId = None
        elif screeningStrategyId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyId = screeningStrategyId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setScreeningStrategyId argument is not XSDataInteger but %s" % screeningStrategyId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyId(self): self._screeningStrategyId = None
    screeningStrategyId = property(getScreeningStrategyId, setScreeningStrategyId, delScreeningStrategyId, "Property for screeningStrategyId")
    # Methods and properties for the 'screeningStrategyOutputId' attribute
    def getScreeningStrategyOutputId(self): return self._screeningStrategyOutputId
    def setScreeningStrategyOutputId(self, screeningStrategyOutputId):
        if screeningStrategyOutputId is None:
            self._screeningStrategyOutputId = None
        elif screeningStrategyOutputId.__class__.__name__ == "XSDataInteger":
            self._screeningStrategyOutputId = screeningStrategyOutputId
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setScreeningStrategyOutputId argument is not XSDataInteger but %s" % screeningStrategyOutputId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyOutputId(self): self._screeningStrategyOutputId = None
    screeningStrategyOutputId = property(getScreeningStrategyOutputId, setScreeningStrategyOutputId, delScreeningStrategyOutputId, "Property for screeningStrategyOutputId")
    # Methods and properties for the 'wedgeNumber' attribute
    def getWedgeNumber(self): return self._wedgeNumber
    def setWedgeNumber(self, wedgeNumber):
        if wedgeNumber is None:
            self._wedgeNumber = None
        elif wedgeNumber.__class__.__name__ == "XSDataInteger":
            self._wedgeNumber = wedgeNumber
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setWedgeNumber argument is not XSDataInteger but %s" % wedgeNumber.__class__.__name__
            raise BaseException(strMessage)
    def delWedgeNumber(self): self._wedgeNumber = None
    wedgeNumber = property(getWedgeNumber, setWedgeNumber, delWedgeNumber, "Property for wedgeNumber")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'completeness' attribute
    def getCompleteness(self): return self._completeness
    def setCompleteness(self, completeness):
        if completeness is None:
            self._completeness = None
        elif completeness.__class__.__name__ == "XSDataDouble":
            self._completeness = completeness
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setCompleteness argument is not XSDataDouble but %s" % completeness.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness(self): self._completeness = None
    completeness = property(getCompleteness, setCompleteness, delCompleteness, "Property for completeness")
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setMultiplicity argument is not XSDataDouble but %s" % multiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delMultiplicity(self): self._multiplicity = None
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    # Methods and properties for the 'doseTotal' attribute
    def getDoseTotal(self): return self._doseTotal
    def setDoseTotal(self, doseTotal):
        if doseTotal is None:
            self._doseTotal = None
        elif doseTotal.__class__.__name__ == "XSDataDouble":
            self._doseTotal = doseTotal
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setDoseTotal argument is not XSDataDouble but %s" % doseTotal.__class__.__name__
            raise BaseException(strMessage)
    def delDoseTotal(self): self._doseTotal = None
    doseTotal = property(getDoseTotal, setDoseTotal, delDoseTotal, "Property for doseTotal")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataInteger":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setNumberOfImages argument is not XSDataInteger but %s" % numberOfImages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setPhi argument is not XSDataDouble but %s" % phi.__class__.__name__
            raise BaseException(strMessage)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setKappa argument is not XSDataDouble but %s" % kappa.__class__.__name__
            raise BaseException(strMessage)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedge.setWavelength argument is not XSDataDouble but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningStrategyWedgeId is not None:
            self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
        if self._screeningStrategyId is not None:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        else:
            warnEmptyAttribute("screeningStrategyId", "XSDataInteger")
        if self._screeningStrategyOutputId is not None:
            self.screeningStrategyOutputId.export(outfile, level, name_='screeningStrategyOutputId')
        else:
            warnEmptyAttribute("screeningStrategyOutputId", "XSDataInteger")
        if self._wedgeNumber is not None:
            self.wedgeNumber.export(outfile, level, name_='wedgeNumber')
        else:
            warnEmptyAttribute("wedgeNumber", "XSDataInteger")
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        else:
            warnEmptyAttribute("resolution", "XSDataDouble")
        if self._completeness is not None:
            self.completeness.export(outfile, level, name_='completeness')
        else:
            warnEmptyAttribute("completeness", "XSDataDouble")
        if self._multiplicity is not None:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        else:
            warnEmptyAttribute("multiplicity", "XSDataDouble")
        if self._doseTotal is not None:
            self.doseTotal.export(outfile, level, name_='doseTotal')
        if self._numberOfImages is not None:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        else:
            warnEmptyAttribute("numberOfImages", "XSDataInteger")
        if self._phi is not None:
            self.phi.export(outfile, level, name_='phi')
        if self._kappa is not None:
            self.kappa.export(outfile, level, name_='kappa')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategyWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyOutputId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningStrategyOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wedgeNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setWedgeNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseTotal':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPhi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setWavelength(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningStrategyWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyWedge


class XSDataISPyBScreeningStrategyWedgeContainer(XSData):
    def __init__(self, screeningStrategyWedge=None, screeningStrategySubWedge=None):
        XSData.__init__(self, )
        if screeningStrategySubWedge is None:
            self._screeningStrategySubWedge = []
        elif screeningStrategySubWedge.__class__.__name__ == "list":
            self._screeningStrategySubWedge = screeningStrategySubWedge
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer constructor argument 'screeningStrategySubWedge' is not list but %s" % self._screeningStrategySubWedge.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyWedge is None:
            self._screeningStrategyWedge = None
        elif screeningStrategyWedge.__class__.__name__ == "XSDataISPyBScreeningStrategyWedge":
            self._screeningStrategyWedge = screeningStrategyWedge
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer constructor argument 'screeningStrategyWedge' is not XSDataISPyBScreeningStrategyWedge but %s" % self._screeningStrategyWedge.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategySubWedge' attribute
    def getScreeningStrategySubWedge(self): return self._screeningStrategySubWedge
    def setScreeningStrategySubWedge(self, screeningStrategySubWedge):
        if screeningStrategySubWedge is None:
            self._screeningStrategySubWedge = []
        elif screeningStrategySubWedge.__class__.__name__ == "list":
            self._screeningStrategySubWedge = screeningStrategySubWedge
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.setScreeningStrategySubWedge argument is not list but %s" % screeningStrategySubWedge.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategySubWedge(self): self._screeningStrategySubWedge = None
    screeningStrategySubWedge = property(getScreeningStrategySubWedge, setScreeningStrategySubWedge, delScreeningStrategySubWedge, "Property for screeningStrategySubWedge")
    def addScreeningStrategySubWedge(self, value):
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.addScreeningStrategySubWedge argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategySubWedge":
            self._screeningStrategySubWedge.append(value)
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.addScreeningStrategySubWedge argument is not XSDataISPyBScreeningStrategySubWedge but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningStrategySubWedge(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.insertScreeningStrategySubWedge argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.insertScreeningStrategySubWedge argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategySubWedge":
            self._screeningStrategySubWedge[index] = value
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.addScreeningStrategySubWedge argument is not XSDataISPyBScreeningStrategySubWedge but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategyWedge' attribute
    def getScreeningStrategyWedge(self): return self._screeningStrategyWedge
    def setScreeningStrategyWedge(self, screeningStrategyWedge):
        if screeningStrategyWedge is None:
            self._screeningStrategyWedge = None
        elif screeningStrategyWedge.__class__.__name__ == "XSDataISPyBScreeningStrategyWedge":
            self._screeningStrategyWedge = screeningStrategyWedge
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyWedgeContainer.setScreeningStrategyWedge argument is not XSDataISPyBScreeningStrategyWedge but %s" % screeningStrategyWedge.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyWedge(self): self._screeningStrategyWedge = None
    screeningStrategyWedge = property(getScreeningStrategyWedge, setScreeningStrategyWedge, delScreeningStrategyWedge, "Property for screeningStrategyWedge")
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        XSData.exportChildren(self, outfile, level, name_)
        for screeningStrategySubWedge_ in self.getScreeningStrategySubWedge():
            screeningStrategySubWedge_.export(outfile, level, name_='screeningStrategySubWedge')
        if self._screeningStrategyWedge is not None:
            self.screeningStrategyWedge.export(outfile, level, name_='screeningStrategyWedge')
        else:
            warnEmptyAttribute("screeningStrategyWedge", "XSDataISPyBScreeningStrategyWedge")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategySubWedge':
            obj_ = XSDataISPyBScreeningStrategySubWedge()
            obj_.build(child_)
            self.screeningStrategySubWedge.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedge':
            obj_ = XSDataISPyBScreeningStrategyWedge()
            obj_.build(child_)
            self.setScreeningStrategyWedge(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedgeContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedgeContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyWedgeContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningStrategyWedgeContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedgeContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedgeContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedgeContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyWedgeContainer


class XSDataISPyBScreeningStrategyContainer(XSData):
    def __init__(self, screeningStrategyWedgeContainer=None, screeningStrategy=None):
        XSData.__init__(self, )
        if screeningStrategy is None:
            self._screeningStrategy = None
        elif screeningStrategy.__class__.__name__ == "XSDataISPyBScreeningStrategy":
            self._screeningStrategy = screeningStrategy
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer constructor argument 'screeningStrategy' is not XSDataISPyBScreeningStrategy but %s" % self._screeningStrategy.__class__.__name__
            raise BaseException(strMessage)
        if screeningStrategyWedgeContainer is None:
            self._screeningStrategyWedgeContainer = []
        elif screeningStrategyWedgeContainer.__class__.__name__ == "list":
            self._screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer constructor argument 'screeningStrategyWedgeContainer' is not list but %s" % self._screeningStrategyWedgeContainer.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningStrategy' attribute
    def getScreeningStrategy(self): return self._screeningStrategy
    def setScreeningStrategy(self, screeningStrategy):
        if screeningStrategy is None:
            self._screeningStrategy = None
        elif screeningStrategy.__class__.__name__ == "XSDataISPyBScreeningStrategy":
            self._screeningStrategy = screeningStrategy
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.setScreeningStrategy argument is not XSDataISPyBScreeningStrategy but %s" % screeningStrategy.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategy(self): self._screeningStrategy = None
    screeningStrategy = property(getScreeningStrategy, setScreeningStrategy, delScreeningStrategy, "Property for screeningStrategy")
    # Methods and properties for the 'screeningStrategyWedgeContainer' attribute
    def getScreeningStrategyWedgeContainer(self): return self._screeningStrategyWedgeContainer
    def setScreeningStrategyWedgeContainer(self, screeningStrategyWedgeContainer):
        if screeningStrategyWedgeContainer is None:
            self._screeningStrategyWedgeContainer = []
        elif screeningStrategyWedgeContainer.__class__.__name__ == "list":
            self._screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.setScreeningStrategyWedgeContainer argument is not list but %s" % screeningStrategyWedgeContainer.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningStrategyWedgeContainer(self): self._screeningStrategyWedgeContainer = None
    screeningStrategyWedgeContainer = property(getScreeningStrategyWedgeContainer, setScreeningStrategyWedgeContainer, delScreeningStrategyWedgeContainer, "Property for screeningStrategyWedgeContainer")
    def addScreeningStrategyWedgeContainer(self, value):
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.addScreeningStrategyWedgeContainer argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategyWedgeContainer":
            self._screeningStrategyWedgeContainer.append(value)
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.addScreeningStrategyWedgeContainer argument is not XSDataISPyBScreeningStrategyWedgeContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningStrategyWedgeContainer(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.insertScreeningStrategyWedgeContainer argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.insertScreeningStrategyWedgeContainer argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningStrategyWedgeContainer":
            self._screeningStrategyWedgeContainer[index] = value
        else:
            strMessage = "ERROR! XSDataISPyBScreeningStrategyContainer.addScreeningStrategyWedgeContainer argument is not XSDataISPyBScreeningStrategyWedgeContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._screeningStrategy is not None:
            self.screeningStrategy.export(outfile, level, name_='screeningStrategy')
        else:
            warnEmptyAttribute("screeningStrategy", "XSDataISPyBScreeningStrategy")
        for screeningStrategyWedgeContainer_ in self.getScreeningStrategyWedgeContainer():
            screeningStrategyWedgeContainer_.export(outfile, level, name_='screeningStrategyWedgeContainer')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategy':
            obj_ = XSDataISPyBScreeningStrategy()
            obj_.build(child_)
            self.setScreeningStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeContainer':
            obj_ = XSDataISPyBScreeningStrategyWedgeContainer()
            obj_.build(child_)
            self.screeningStrategyWedgeContainer.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyContainer' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBScreeningStrategyContainer is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBScreeningStrategyContainer.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyContainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyContainer" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyContainer()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBScreeningStrategyContainer


class XSDataInputISPyBStoreScreening(XSDataInput):
    def __init__(self, configuration=None, screeningRankSet=None, screeningRank=None, screeningOutputContainer=None, screening=None, image=None, file=None, diffractionPlan=None):
        XSDataInput.__init__(self, configuration)
        if diffractionPlan is None:
            self._diffractionPlan = None
        elif diffractionPlan.__class__.__name__ == "XSDataISPyBDiffractionPlan":
            self._diffractionPlan = diffractionPlan
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'diffractionPlan' is not XSDataISPyBDiffractionPlan but %s" % self._diffractionPlan.__class__.__name__
            raise BaseException(strMessage)
        if file is None:
            self._file = []
        elif file.__class__.__name__ == "list":
            self._file = file
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'file' is not list but %s" % self._file.__class__.__name__
            raise BaseException(strMessage)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataISPyBImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'image' is not XSDataISPyBImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if screening is None:
            self._screening = None
        elif screening.__class__.__name__ == "XSDataISPyBScreening":
            self._screening = screening
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'screening' is not XSDataISPyBScreening but %s" % self._screening.__class__.__name__
            raise BaseException(strMessage)
        if screeningOutputContainer is None:
            self._screeningOutputContainer = []
        elif screeningOutputContainer.__class__.__name__ == "list":
            self._screeningOutputContainer = screeningOutputContainer
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'screeningOutputContainer' is not list but %s" % self._screeningOutputContainer.__class__.__name__
            raise BaseException(strMessage)
        if screeningRank is None:
            self._screeningRank = []
        elif screeningRank.__class__.__name__ == "list":
            self._screeningRank = screeningRank
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'screeningRank' is not list but %s" % self._screeningRank.__class__.__name__
            raise BaseException(strMessage)
        if screeningRankSet is None:
            self._screeningRankSet = None
        elif screeningRankSet.__class__.__name__ == "XSDataISPyBScreeningRankSet":
            self._screeningRankSet = screeningRankSet
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening constructor argument 'screeningRankSet' is not XSDataISPyBScreeningRankSet but %s" % self._screeningRankSet.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'diffractionPlan' attribute
    def getDiffractionPlan(self): return self._diffractionPlan
    def setDiffractionPlan(self, diffractionPlan):
        if diffractionPlan is None:
            self._diffractionPlan = None
        elif diffractionPlan.__class__.__name__ == "XSDataISPyBDiffractionPlan":
            self._diffractionPlan = diffractionPlan
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setDiffractionPlan argument is not XSDataISPyBDiffractionPlan but %s" % diffractionPlan.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionPlan(self): self._diffractionPlan = None
    diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
    # Methods and properties for the 'file' attribute
    def getFile(self): return self._file
    def setFile(self, file):
        if file is None:
            self._file = []
        elif file.__class__.__name__ == "list":
            self._file = file
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setFile argument is not list but %s" % file.__class__.__name__
            raise BaseException(strMessage)
    def delFile(self): self._file = None
    file = property(getFile, setFile, delFile, "Property for file")
    def addFile(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addFile argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningFile":
            self._file.append(value)
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addFile argument is not XSDataISPyBScreeningFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFile(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertFile argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertFile argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningFile":
            self._file[index] = value
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addFile argument is not XSDataISPyBScreeningFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataISPyBImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setImage argument is not XSDataISPyBImage but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'screening' attribute
    def getScreening(self): return self._screening
    def setScreening(self, screening):
        if screening is None:
            self._screening = None
        elif screening.__class__.__name__ == "XSDataISPyBScreening":
            self._screening = screening
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setScreening argument is not XSDataISPyBScreening but %s" % screening.__class__.__name__
            raise BaseException(strMessage)
    def delScreening(self): self._screening = None
    screening = property(getScreening, setScreening, delScreening, "Property for screening")
    # Methods and properties for the 'screeningOutputContainer' attribute
    def getScreeningOutputContainer(self): return self._screeningOutputContainer
    def setScreeningOutputContainer(self, screeningOutputContainer):
        if screeningOutputContainer is None:
            self._screeningOutputContainer = []
        elif screeningOutputContainer.__class__.__name__ == "list":
            self._screeningOutputContainer = screeningOutputContainer
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setScreeningOutputContainer argument is not list but %s" % screeningOutputContainer.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningOutputContainer(self): self._screeningOutputContainer = None
    screeningOutputContainer = property(getScreeningOutputContainer, setScreeningOutputContainer, delScreeningOutputContainer, "Property for screeningOutputContainer")
    def addScreeningOutputContainer(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningOutputContainer argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningOutputContainer":
            self._screeningOutputContainer.append(value)
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningOutputContainer argument is not XSDataISPyBScreeningOutputContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningOutputContainer(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertScreeningOutputContainer argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertScreeningOutputContainer argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningOutputContainer":
            self._screeningOutputContainer[index] = value
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningOutputContainer argument is not XSDataISPyBScreeningOutputContainer but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningRank' attribute
    def getScreeningRank(self): return self._screeningRank
    def setScreeningRank(self, screeningRank):
        if screeningRank is None:
            self._screeningRank = []
        elif screeningRank.__class__.__name__ == "list":
            self._screeningRank = screeningRank
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setScreeningRank argument is not list but %s" % screeningRank.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningRank(self): self._screeningRank = None
    screeningRank = property(getScreeningRank, setScreeningRank, delScreeningRank, "Property for screeningRank")
    def addScreeningRank(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningRank argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningRank":
            self._screeningRank.append(value)
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningRank argument is not XSDataISPyBScreeningRank but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScreeningRank(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertScreeningRank argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.insertScreeningRank argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataISPyBScreeningRank":
            self._screeningRank[index] = value
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.addScreeningRank argument is not XSDataISPyBScreeningRank but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningRankSet' attribute
    def getScreeningRankSet(self): return self._screeningRankSet
    def setScreeningRankSet(self, screeningRankSet):
        if screeningRankSet is None:
            self._screeningRankSet = None
        elif screeningRankSet.__class__.__name__ == "XSDataISPyBScreeningRankSet":
            self._screeningRankSet = screeningRankSet
        else:
            strMessage = "ERROR! XSDataInputISPyBStoreScreening.setScreeningRankSet argument is not XSDataISPyBScreeningRankSet but %s" % screeningRankSet.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningRankSet(self): self._screeningRankSet = None
    screeningRankSet = property(getScreeningRankSet, setScreeningRankSet, delScreeningRankSet, "Property for screeningRankSet")
    def export(self, outfile, level, name_='XSDataInputISPyBStoreScreening'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputISPyBStoreScreening'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._diffractionPlan is not None:
            self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        for file_ in self.getFile():
            file_.export(outfile, level, name_='file')
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        if self._screening is not None:
            self.screening.export(outfile, level, name_='screening')
        for screeningOutputContainer_ in self.getScreeningOutputContainer():
            screeningOutputContainer_.export(outfile, level, name_='screeningOutputContainer')
        for screeningRank_ in self.getScreeningRank():
            screeningRank_.export(outfile, level, name_='screeningRank')
        if self._screeningRankSet is not None:
            self.screeningRankSet.export(outfile, level, name_='screeningRankSet')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataISPyBDiffractionPlan()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'file':
            obj_ = XSDataISPyBScreeningFile()
            obj_.build(child_)
            self.file.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataISPyBImage()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screening':
            obj_ = XSDataISPyBScreening()
            obj_.build(child_)
            self.setScreening(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputContainer':
            obj_ = XSDataISPyBScreeningOutputContainer()
            obj_.build(child_)
            self.screeningOutputContainer.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRank':
            obj_ = XSDataISPyBScreeningRank()
            obj_.build(child_)
            self.screeningRank.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSet':
            obj_ = XSDataISPyBScreeningRankSet()
            obj_.build(child_)
            self.setScreeningRankSet(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputISPyBStoreScreening" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputISPyBStoreScreening' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputISPyBStoreScreening is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputISPyBStoreScreening.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputISPyBStoreScreening()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputISPyBStoreScreening" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputISPyBStoreScreening()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputISPyBStoreScreening


class XSDataInputRetrieveDataCollection(XSDataInput):
    def __init__(self, configuration=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputRetrieveDataCollection constructor argument 'image' is not XSDataImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputRetrieveDataCollection.setImage argument is not XSDataImage but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def export(self, outfile, level, name_='XSDataInputRetrieveDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputRetrieveDataCollection'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataImage")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputRetrieveDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputRetrieveDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputRetrieveDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputRetrieveDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputRetrieveDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputRetrieveDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputRetrieveDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputRetrieveDataCollection


class XSDataInputStoreAutoProc(XSDataInput):
    def __init__(self, configuration=None, AutoProcContainer=None):
        XSDataInput.__init__(self, configuration)
        if AutoProcContainer is None:
            self._AutoProcContainer = None
        elif AutoProcContainer.__class__.__name__ == "AutoProcContainer":
            self._AutoProcContainer = AutoProcContainer
        else:
            strMessage = "ERROR! XSDataInputStoreAutoProc constructor argument 'AutoProcContainer' is not AutoProcContainer but %s" % self._AutoProcContainer.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'AutoProcContainer' attribute
    def getAutoProcContainer(self): return self._AutoProcContainer
    def setAutoProcContainer(self, AutoProcContainer):
        if AutoProcContainer is None:
            self._AutoProcContainer = None
        elif AutoProcContainer.__class__.__name__ == "AutoProcContainer":
            self._AutoProcContainer = AutoProcContainer
        else:
            strMessage = "ERROR! XSDataInputStoreAutoProc.setAutoProcContainer argument is not AutoProcContainer but %s" % AutoProcContainer.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcContainer(self): self._AutoProcContainer = None
    AutoProcContainer = property(getAutoProcContainer, setAutoProcContainer, delAutoProcContainer, "Property for AutoProcContainer")
    def export(self, outfile, level, name_='XSDataInputStoreAutoProc'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStoreAutoProc'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._AutoProcContainer is not None:
            self.AutoProcContainer.export(outfile, level, name_='AutoProcContainer')
        else:
            warnEmptyAttribute("AutoProcContainer", "AutoProcContainer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcContainer':
            obj_ = AutoProcContainer()
            obj_.build(child_)
            self.setAutoProcContainer(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStoreAutoProc" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStoreAutoProc' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStoreAutoProc is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStoreAutoProc.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreAutoProc()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStoreAutoProc" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreAutoProc()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStoreAutoProc


class XSDataInputStoreAutoProcStatus(XSDataInput):
    def __init__(self, configuration=None, AutoProcStatus=None, autoProcStatusId=None, autoProcIntegrationId=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
        if AutoProcStatus is None:
            self._AutoProcStatus = None
        elif AutoProcStatus.__class__.__name__ == "AutoProcStatus":
            self._AutoProcStatus = AutoProcStatus
        else:
            strMessage = "ERROR! XSDataInputStoreAutoProcStatus constructor argument 'AutoProcStatus' is not AutoProcStatus but %s" % self._AutoProcStatus.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'autoProcIntegrationId' attribute
    def getAutoProcIntegrationId(self): return self._autoProcIntegrationId
    def setAutoProcIntegrationId(self, autoProcIntegrationId):
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
    def delAutoProcIntegrationId(self): self._autoProcIntegrationId = None
    autoProcIntegrationId = property(getAutoProcIntegrationId, setAutoProcIntegrationId, delAutoProcIntegrationId, "Property for autoProcIntegrationId")
    # Methods and properties for the 'autoProcStatusId' attribute
    def getAutoProcStatusId(self): return self._autoProcStatusId
    def setAutoProcStatusId(self, autoProcStatusId):
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
    def delAutoProcStatusId(self): self._autoProcStatusId = None
    autoProcStatusId = property(getAutoProcStatusId, setAutoProcStatusId, delAutoProcStatusId, "Property for autoProcStatusId")
    # Methods and properties for the 'AutoProcStatus' attribute
    def getAutoProcStatus(self): return self._AutoProcStatus
    def setAutoProcStatus(self, AutoProcStatus):
        if AutoProcStatus is None:
            self._AutoProcStatus = None
        elif AutoProcStatus.__class__.__name__ == "AutoProcStatus":
            self._AutoProcStatus = AutoProcStatus
        else:
            strMessage = "ERROR! XSDataInputStoreAutoProcStatus.setAutoProcStatus argument is not AutoProcStatus but %s" % AutoProcStatus.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcStatus(self): self._AutoProcStatus = None
    AutoProcStatus = property(getAutoProcStatus, setAutoProcStatus, delAutoProcStatus, "Property for AutoProcStatus")
    def export(self, outfile, level, name_='XSDataInputStoreAutoProcStatus'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStoreAutoProcStatus'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
        if self._autoProcIntegrationId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcIntegrationId>%d</autoProcIntegrationId>\n' % self._autoProcIntegrationId))
        if self._autoProcStatusId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcStatusId>%d</autoProcStatusId>\n' % self._autoProcStatusId))
        if self._AutoProcStatus is not None:
            self.AutoProcStatus.export(outfile, level, name_='AutoProcStatus')
        else:
            warnEmptyAttribute("AutoProcStatus", "AutoProcStatus")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcIntegrationId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcIntegrationId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcStatusId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcStatusId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AutoProcStatus':
            obj_ = AutoProcStatus()
            obj_.build(child_)
            self.setAutoProcStatus(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStoreAutoProcStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStoreAutoProcStatus' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStoreAutoProcStatus is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStoreAutoProcStatus.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreAutoProcStatus()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStoreAutoProcStatus" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreAutoProcStatus()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStoreAutoProcStatus


class XSDataInputStoreDataCollection(XSDataInput):
    def __init__(self, configuration=None, dataCollection=None):
        XSDataInput.__init__(self, configuration)
        if dataCollection is None:
            self._dataCollection = None
        elif dataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._dataCollection = dataCollection
        else:
            strMessage = "ERROR! XSDataInputStoreDataCollection constructor argument 'dataCollection' is not XSDataISPyBDataCollection but %s" % self._dataCollection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollection' attribute
    def getDataCollection(self): return self._dataCollection
    def setDataCollection(self, dataCollection):
        if dataCollection is None:
            self._dataCollection = None
        elif dataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._dataCollection = dataCollection
        else:
            strMessage = "ERROR! XSDataInputStoreDataCollection.setDataCollection argument is not XSDataISPyBDataCollection but %s" % dataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollection(self): self._dataCollection = None
    dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
    def export(self, outfile, level, name_='XSDataInputStoreDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStoreDataCollection'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollection is not None:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        else:
            warnEmptyAttribute("dataCollection", "XSDataISPyBDataCollection")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataISPyBDataCollection()
            obj_.build(child_)
            self.setDataCollection(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStoreDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStoreDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStoreDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStoreDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStoreDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStoreDataCollection


class XSDataInputStoreImageQualityIndicators(XSDataInput):
    def __init__(self, configuration=None, imageQualityIndicators=None):
        XSDataInput.__init__(self, configuration)
        if imageQualityIndicators is None:
            self._imageQualityIndicators = None
        elif imageQualityIndicators.__class__.__name__ == "XSDataISPyBImageQualityIndicators":
            self._imageQualityIndicators = imageQualityIndicators
        else:
            strMessage = "ERROR! XSDataInputStoreImageQualityIndicators constructor argument 'imageQualityIndicators' is not XSDataISPyBImageQualityIndicators but %s" % self._imageQualityIndicators.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageQualityIndicators' attribute
    def getImageQualityIndicators(self): return self._imageQualityIndicators
    def setImageQualityIndicators(self, imageQualityIndicators):
        if imageQualityIndicators is None:
            self._imageQualityIndicators = None
        elif imageQualityIndicators.__class__.__name__ == "XSDataISPyBImageQualityIndicators":
            self._imageQualityIndicators = imageQualityIndicators
        else:
            strMessage = "ERROR! XSDataInputStoreImageQualityIndicators.setImageQualityIndicators argument is not XSDataISPyBImageQualityIndicators but %s" % imageQualityIndicators.__class__.__name__
            raise BaseException(strMessage)
    def delImageQualityIndicators(self): self._imageQualityIndicators = None
    imageQualityIndicators = property(getImageQualityIndicators, setImageQualityIndicators, delImageQualityIndicators, "Property for imageQualityIndicators")
    def export(self, outfile, level, name_='XSDataInputStoreImageQualityIndicators'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputStoreImageQualityIndicators'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._imageQualityIndicators is not None:
            self.imageQualityIndicators.export(outfile, level, name_='imageQualityIndicators')
        else:
            warnEmptyAttribute("imageQualityIndicators", "XSDataISPyBImageQualityIndicators")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageQualityIndicators':
            obj_ = XSDataISPyBImageQualityIndicators()
            obj_.build(child_)
            self.setImageQualityIndicators(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputStoreImageQualityIndicators" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputStoreImageQualityIndicators' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputStoreImageQualityIndicators is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputStoreImageQualityIndicators.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreImageQualityIndicators()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputStoreImageQualityIndicators" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStoreImageQualityIndicators()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputStoreImageQualityIndicators


class XSDataResultISPyBStoreScreening(XSDataResult):
    def __init__(self, status=None, screeningId=None):
        XSDataResult.__init__(self, status)
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataResultISPyBStoreScreening constructor argument 'screeningId' is not XSDataInteger but %s" % self._screeningId.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'screeningId' attribute
    def getScreeningId(self): return self._screeningId
    def setScreeningId(self, screeningId):
        if screeningId is None:
            self._screeningId = None
        elif screeningId.__class__.__name__ == "XSDataInteger":
            self._screeningId = screeningId
        else:
            strMessage = "ERROR! XSDataResultISPyBStoreScreening.setScreeningId argument is not XSDataInteger but %s" % screeningId.__class__.__name__
            raise BaseException(strMessage)
    def delScreeningId(self): self._screeningId = None
    screeningId = property(getScreeningId, setScreeningId, delScreeningId, "Property for screeningId")
    def export(self, outfile, level, name_='XSDataResultISPyBStoreScreening'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultISPyBStoreScreening'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._screeningId is not None:
            self.screeningId.export(outfile, level, name_='screeningId')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setScreeningId(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultISPyBStoreScreening" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultISPyBStoreScreening' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultISPyBStoreScreening is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultISPyBStoreScreening.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultISPyBStoreScreening()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultISPyBStoreScreening" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultISPyBStoreScreening()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultISPyBStoreScreening


class XSDataResultRetrieveDataCollection(XSDataResult):
    def __init__(self, status=None, dataCollection=None):
        XSDataResult.__init__(self, status)
        if dataCollection is None:
            self._dataCollection = None
        elif dataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._dataCollection = dataCollection
        else:
            strMessage = "ERROR! XSDataResultRetrieveDataCollection constructor argument 'dataCollection' is not XSDataISPyBDataCollection but %s" % self._dataCollection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollection' attribute
    def getDataCollection(self): return self._dataCollection
    def setDataCollection(self, dataCollection):
        if dataCollection is None:
            self._dataCollection = None
        elif dataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._dataCollection = dataCollection
        else:
            strMessage = "ERROR! XSDataResultRetrieveDataCollection.setDataCollection argument is not XSDataISPyBDataCollection but %s" % dataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollection(self): self._dataCollection = None
    dataCollection = property(getDataCollection, setDataCollection, delDataCollection, "Property for dataCollection")
    def export(self, outfile, level, name_='XSDataResultRetrieveDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultRetrieveDataCollection'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._dataCollection is not None:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        else:
            warnEmptyAttribute("dataCollection", "XSDataISPyBDataCollection")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataISPyBDataCollection()
            obj_.build(child_)
            self.setDataCollection(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultRetrieveDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultRetrieveDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultRetrieveDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultRetrieveDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultRetrieveDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultRetrieveDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultRetrieveDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultRetrieveDataCollection


class XSDataResultStoreAutoProc(XSDataResult):
    def __init__(self, status=None, autoProcId=None):
        XSDataResult.__init__(self, status)
        if autoProcId is None:
            self._autoProcId = None
        elif autoProcId.__class__.__name__ == "XSDataInteger":
            self._autoProcId = autoProcId
        else:
            strMessage = "ERROR! XSDataResultStoreAutoProc constructor argument 'autoProcId' is not XSDataInteger but %s" % self._autoProcId.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'autoProcId' attribute
    def getAutoProcId(self): return self._autoProcId
    def setAutoProcId(self, autoProcId):
        if autoProcId is None:
            self._autoProcId = None
        elif autoProcId.__class__.__name__ == "XSDataInteger":
            self._autoProcId = autoProcId
        else:
            strMessage = "ERROR! XSDataResultStoreAutoProc.setAutoProcId argument is not XSDataInteger but %s" % autoProcId.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcId(self): self._autoProcId = None
    autoProcId = property(getAutoProcId, setAutoProcId, delAutoProcId, "Property for autoProcId")
    def export(self, outfile, level, name_='XSDataResultStoreAutoProc'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStoreAutoProc'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._autoProcId is not None:
            self.autoProcId.export(outfile, level, name_='autoProcId')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setAutoProcId(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStoreAutoProc" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStoreAutoProc' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStoreAutoProc is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStoreAutoProc.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreAutoProc()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStoreAutoProc" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreAutoProc()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStoreAutoProc


class XSDataResultStoreAutoProcStatus(XSDataResult):
    def __init__(self, status=None, autoProcStatusId=None, autoProcIntegrationId=None):
        XSDataResult.__init__(self, status)
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
    # Methods and properties for the 'autoProcIntegrationId' attribute
    def getAutoProcIntegrationId(self): return self._autoProcIntegrationId
    def setAutoProcIntegrationId(self, autoProcIntegrationId):
        if autoProcIntegrationId is None:
            self._autoProcIntegrationId = None
        else:
            self._autoProcIntegrationId = int(autoProcIntegrationId)
    def delAutoProcIntegrationId(self): self._autoProcIntegrationId = None
    autoProcIntegrationId = property(getAutoProcIntegrationId, setAutoProcIntegrationId, delAutoProcIntegrationId, "Property for autoProcIntegrationId")
    # Methods and properties for the 'autoProcStatusId' attribute
    def getAutoProcStatusId(self): return self._autoProcStatusId
    def setAutoProcStatusId(self, autoProcStatusId):
        if autoProcStatusId is None:
            self._autoProcStatusId = None
        else:
            self._autoProcStatusId = int(autoProcStatusId)
    def delAutoProcStatusId(self): self._autoProcStatusId = None
    autoProcStatusId = property(getAutoProcStatusId, setAutoProcStatusId, delAutoProcStatusId, "Property for autoProcStatusId")
    def export(self, outfile, level, name_='XSDataResultStoreAutoProcStatus'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStoreAutoProcStatus'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._autoProcIntegrationId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcIntegrationId>%d</autoProcIntegrationId>\n' % self._autoProcIntegrationId))
        else:
            warnEmptyAttribute("autoProcIntegrationId", "integer")
        if self._autoProcStatusId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<autoProcStatusId>%d</autoProcStatusId>\n' % self._autoProcStatusId))
        else:
            warnEmptyAttribute("autoProcStatusId", "integer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcIntegrationId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcIntegrationId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcStatusId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._autoProcStatusId = ival_
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStoreAutoProcStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStoreAutoProcStatus' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStoreAutoProcStatus is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStoreAutoProcStatus.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreAutoProcStatus()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStoreAutoProcStatus" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreAutoProcStatus()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStoreAutoProcStatus


class XSDataResultStoreDataCollection(XSDataResult):
    def __init__(self, status=None, dataCollectionId=None):
        XSDataResult.__init__(self, status)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataResultStoreDataCollection constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataResultStoreDataCollection.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    def export(self, outfile, level, name_='XSDataResultStoreDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStoreDataCollection'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStoreDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStoreDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStoreDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStoreDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStoreDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStoreDataCollection


class XSDataResultStoreImageQualityIndicators(XSDataResult):
    def __init__(self, status=None, imageQualityIndicatorsId=None):
        XSDataResult.__init__(self, status)
        if imageQualityIndicatorsId is None:
            self._imageQualityIndicatorsId = None
        elif imageQualityIndicatorsId.__class__.__name__ == "XSDataInteger":
            self._imageQualityIndicatorsId = imageQualityIndicatorsId
        else:
            strMessage = "ERROR! XSDataResultStoreImageQualityIndicators constructor argument 'imageQualityIndicatorsId' is not XSDataInteger but %s" % self._imageQualityIndicatorsId.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageQualityIndicatorsId' attribute
    def getImageQualityIndicatorsId(self): return self._imageQualityIndicatorsId
    def setImageQualityIndicatorsId(self, imageQualityIndicatorsId):
        if imageQualityIndicatorsId is None:
            self._imageQualityIndicatorsId = None
        elif imageQualityIndicatorsId.__class__.__name__ == "XSDataInteger":
            self._imageQualityIndicatorsId = imageQualityIndicatorsId
        else:
            strMessage = "ERROR! XSDataResultStoreImageQualityIndicators.setImageQualityIndicatorsId argument is not XSDataInteger but %s" % imageQualityIndicatorsId.__class__.__name__
            raise BaseException(strMessage)
    def delImageQualityIndicatorsId(self): self._imageQualityIndicatorsId = None
    imageQualityIndicatorsId = property(getImageQualityIndicatorsId, setImageQualityIndicatorsId, delImageQualityIndicatorsId, "Property for imageQualityIndicatorsId")
    def export(self, outfile, level, name_='XSDataResultStoreImageQualityIndicators'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultStoreImageQualityIndicators'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._imageQualityIndicatorsId is not None:
            self.imageQualityIndicatorsId.export(outfile, level, name_='imageQualityIndicatorsId')
        else:
            warnEmptyAttribute("imageQualityIndicatorsId", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageQualityIndicatorsId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageQualityIndicatorsId(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultStoreImageQualityIndicators" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultStoreImageQualityIndicators' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultStoreImageQualityIndicators is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultStoreImageQualityIndicators.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreImageQualityIndicators()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultStoreImageQualityIndicators" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStoreImageQualityIndicators()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultStoreImageQualityIndicators



# End of data representation classes.



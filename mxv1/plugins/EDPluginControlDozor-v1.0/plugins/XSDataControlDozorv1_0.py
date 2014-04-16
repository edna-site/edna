#!/usr/bin/env python

#
# Generated Wed Apr 16 09:08::35 2014 by EDGenerateDS.
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
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
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
from XSDataCommon import XSDataInteger
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



class XSDataControlImageDozor(object):
    def __init__(self, score=None, powder_wilson_rfactor=None, powder_wilson_correlation=None, powder_wilson_resolution=None, powder_wilson_bfactor=None, powder_wilson_scale=None, spots_resolution=None, spots_int_aver=None, spots_num_of=None, image=None):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'image' is not XSDataFile but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if spots_num_of is None:
            self._spots_num_of = None
        elif spots_num_of.__class__.__name__ == "XSDataInteger":
            self._spots_num_of = spots_num_of
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'spots_num_of' is not XSDataInteger but %s" % self._spots_num_of.__class__.__name__
            raise BaseException(strMessage)
        if spots_int_aver is None:
            self._spots_int_aver = None
        elif spots_int_aver.__class__.__name__ == "XSDataDouble":
            self._spots_int_aver = spots_int_aver
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'spots_int_aver' is not XSDataDouble but %s" % self._spots_int_aver.__class__.__name__
            raise BaseException(strMessage)
        if spots_resolution is None:
            self._spots_resolution = None
        elif spots_resolution.__class__.__name__ == "XSDataDouble":
            self._spots_resolution = spots_resolution
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'spots_resolution' is not XSDataDouble but %s" % self._spots_resolution.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_scale is None:
            self._powder_wilson_scale = None
        elif powder_wilson_scale.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_scale = powder_wilson_scale
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'powder_wilson_scale' is not XSDataDouble but %s" % self._powder_wilson_scale.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_bfactor is None:
            self._powder_wilson_bfactor = None
        elif powder_wilson_bfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_bfactor = powder_wilson_bfactor
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'powder_wilson_bfactor' is not XSDataDouble but %s" % self._powder_wilson_bfactor.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_resolution is None:
            self._powder_wilson_resolution = None
        elif powder_wilson_resolution.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_resolution = powder_wilson_resolution
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'powder_wilson_resolution' is not XSDataDouble but %s" % self._powder_wilson_resolution.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_correlation is None:
            self._powder_wilson_correlation = None
        elif powder_wilson_correlation.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_correlation = powder_wilson_correlation
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'powder_wilson_correlation' is not XSDataDouble but %s" % self._powder_wilson_correlation.__class__.__name__
            raise BaseException(strMessage)
        if powder_wilson_rfactor is None:
            self._powder_wilson_rfactor = None
        elif powder_wilson_rfactor.__class__.__name__ == "XSDataDouble":
            self._powder_wilson_rfactor = powder_wilson_rfactor
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'powder_wilson_rfactor' is not XSDataDouble but %s" % self._powder_wilson_rfactor.__class__.__name__
            raise BaseException(strMessage)
        if score is None:
            self._score = None
        elif score.__class__.__name__ == "XSDataDouble":
            self._score = score
        else:
            strMessage = "ERROR! XSDataControlImageDozor constructor argument 'score' is not XSDataDouble but %s" % self._score.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataControlImageDozor.setImage argument is not XSDataFile but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'spots_num_of' attribute
    def getSpots_num_of(self): return self._spots_num_of
    def setSpots_num_of(self, spots_num_of):
        if spots_num_of is None:
            self._spots_num_of = None
        elif spots_num_of.__class__.__name__ == "XSDataInteger":
            self._spots_num_of = spots_num_of
        else:
            strMessage = "ERROR! XSDataControlImageDozor.setSpots_num_of argument is not XSDataInteger but %s" % spots_num_of.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setSpots_int_aver argument is not XSDataDouble but %s" % spots_int_aver.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setSpots_resolution argument is not XSDataDouble but %s" % spots_resolution.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setPowder_wilson_scale argument is not XSDataDouble but %s" % powder_wilson_scale.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setPowder_wilson_bfactor argument is not XSDataDouble but %s" % powder_wilson_bfactor.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setPowder_wilson_resolution argument is not XSDataDouble but %s" % powder_wilson_resolution.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setPowder_wilson_correlation argument is not XSDataDouble but %s" % powder_wilson_correlation.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setPowder_wilson_rfactor argument is not XSDataDouble but %s" % powder_wilson_rfactor.__class__.__name__
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
            strMessage = "ERROR! XSDataControlImageDozor.setScore argument is not XSDataDouble but %s" % score.__class__.__name__
            raise BaseException(strMessage)
    def delScore(self): self._score = None
    score = property(getScore, setScore, delScore, "Property for score")
    def export(self, outfile, level, name_='XSDataControlImageDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataControlImageDozor'):
        pass
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataFile")
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
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setImage(obj_)
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
        self.export( oStreamString, 0, name_="XSDataControlImageDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataControlImageDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataControlImageDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataControlImageDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataControlImageDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataControlImageDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataControlImageDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataControlImageDozor


class XSDataInputControlDozor(XSDataInput):
    def __init__(self, configuration=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputControlDozor constructor argument 'image' is not list but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputControlDozor.setImage argument is not list but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def addImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputControlDozor.addImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image.append(value)
        else:
            strMessage = "ERROR! XSDataInputControlDozor.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputControlDozor.insertImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputControlDozor.insertImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image[index] = value
        else:
            strMessage = "ERROR! XSDataInputControlDozor.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputControlDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlDozor'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getImage() == []:
            warnEmptyAttribute("image", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.image.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlDozor


class XSDataResultControlDozor(XSDataResult):
    def __init__(self, status=None, imageDozor=None):
        XSDataResult.__init__(self, status)
        if imageDozor is None:
            self._imageDozor = []
        elif imageDozor.__class__.__name__ == "list":
            self._imageDozor = imageDozor
        else:
            strMessage = "ERROR! XSDataResultControlDozor constructor argument 'imageDozor' is not list but %s" % self._imageDozor.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageDozor' attribute
    def getImageDozor(self): return self._imageDozor
    def setImageDozor(self, imageDozor):
        if imageDozor is None:
            self._imageDozor = []
        elif imageDozor.__class__.__name__ == "list":
            self._imageDozor = imageDozor
        else:
            strMessage = "ERROR! XSDataResultControlDozor.setImageDozor argument is not list but %s" % imageDozor.__class__.__name__
            raise BaseException(strMessage)
    def delImageDozor(self): self._imageDozor = None
    imageDozor = property(getImageDozor, setImageDozor, delImageDozor, "Property for imageDozor")
    def addImageDozor(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultControlDozor.addImageDozor argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataControlImageDozor":
            self._imageDozor.append(value)
        else:
            strMessage = "ERROR! XSDataResultControlDozor.addImageDozor argument is not XSDataControlImageDozor but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImageDozor(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultControlDozor.insertImageDozor argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultControlDozor.insertImageDozor argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataControlImageDozor":
            self._imageDozor[index] = value
        else:
            strMessage = "ERROR! XSDataResultControlDozor.addImageDozor argument is not XSDataControlImageDozor but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultControlDozor'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlDozor'):
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
            obj_ = XSDataControlImageDozor()
            obj_.build(child_)
            self.imageDozor.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultControlDozor" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlDozor' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlDozor is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlDozor.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlDozor()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlDozor" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlDozor()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlDozor



# End of data representation classes.



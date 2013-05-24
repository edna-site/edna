#!/usr/bin/env python

#
# Generated Fri May 24 03:23::12 2013 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataInterfacev1_2": "mxv1/plugins/EDPluginGroupInterface-v1.2/datamodel", \
 "XSDataInterfacev1_2": "mxv1/plugins/EDPluginGroupInterface-v1.2/datamodel", \
 "XSDataMXv2": "mxv2/datamodel", \
 "XSDataMXv2": "mxv2/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv2": "mxv2/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataInterfacev1_2 import XSDataInputInterface
    from XSDataInterfacev1_2 import XSDataResultInterface
    from XSDataMXv2 import kappa_alignment_response
    from XSDataMXv2 import XSDataCollection
    from XSDataMXv1 import XSDataInputCharacterisation
    from XSDataMXv1 import XSDataResultStrategy
    from XSDataMXv1 import XSDataResultCharacterisation
    from XSDataMXv2 import XSDataResultCharacterisationv2_0
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
from XSDataInterfacev1_2 import XSDataInputInterface
from XSDataInterfacev1_2 import XSDataResultInterface
from XSDataMXv2 import kappa_alignment_response
from XSDataMXv2 import XSDataCollection
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv2 import XSDataResultCharacterisationv2_0
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



class XSDataInputInterfacev2_2(XSDataInputInterface):
    def __init__(self, inputCharacterisation=None, comments=None, shortComments=None, dataCollectionId=None, transmission=None, wavelength=None, beamPosY=None, beamPosX=None, resultsFilePath=None, generatedTemplateFile=None, templateMode=None, beamSizeY=None, beamSizeX=None, beamSize=None, minExposureTimePerImage=None, flux=None, imagePath=None, sample=None, diffractionPlan=None, experimentalCondition=None, phi=None, kappa=None, omega=None, possibleOrientations=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv1ResultCharacterisation_Reference=None, mxv1InputCharacterisation=None):
        XSDataInputInterface.__init__(self, inputCharacterisation, comments, shortComments, dataCollectionId, transmission, wavelength, beamPosY, beamPosX, resultsFilePath, generatedTemplateFile, templateMode, beamSizeY, beamSizeX, beamSize, minExposureTimePerImage, flux, imagePath, sample, diffractionPlan, experimentalCondition)
        if mxv1InputCharacterisation is None:
            self._mxv1InputCharacterisation = None
        elif mxv1InputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._mxv1InputCharacterisation = mxv1InputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'mxv1InputCharacterisation' is not XSDataInputCharacterisation but %s" % self._mxv1InputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'mxv1ResultCharacterisation_Reference' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'mxv2DataCollection' is not XSDataCollection but %s" % self._mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'mxv2DataCollection_Reference' is not XSDataCollection but %s" % self._mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'possibleOrientations' is not kappa_alignment_response but %s" % self._possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'omega' is not XSDataAngle but %s" % self._omega.__class__.__name__
            raise BaseException(strMessage)
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataAngle":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'kappa' is not XSDataAngle but %s" % self._kappa.__class__.__name__
            raise BaseException(strMessage)
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataAngle":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2 constructor argument 'phi' is not XSDataAngle but %s" % self._phi.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mxv1InputCharacterisation' attribute
    def getMxv1InputCharacterisation(self): return self._mxv1InputCharacterisation
    def setMxv1InputCharacterisation(self, mxv1InputCharacterisation):
        if mxv1InputCharacterisation is None:
            self._mxv1InputCharacterisation = None
        elif mxv1InputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._mxv1InputCharacterisation = mxv1InputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setMxv1InputCharacterisation argument is not XSDataInputCharacterisation but %s" % mxv1InputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1InputCharacterisation(self): self._mxv1InputCharacterisation = None
    mxv1InputCharacterisation = property(getMxv1InputCharacterisation, setMxv1InputCharacterisation, delMxv1InputCharacterisation, "Property for mxv1InputCharacterisation")
    # Methods and properties for the 'mxv1ResultCharacterisation_Reference' attribute
    def getMxv1ResultCharacterisation_Reference(self): return self._mxv1ResultCharacterisation_Reference
    def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setMxv1ResultCharacterisation_Reference argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation_Reference(self): self._mxv1ResultCharacterisation_Reference = None
    mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
    # Methods and properties for the 'mxv2DataCollection' attribute
    def getMxv2DataCollection(self): return self._mxv2DataCollection
    def setMxv2DataCollection(self, mxv2DataCollection):
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setMxv2DataCollection argument is not XSDataCollection but %s" % mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection(self): self._mxv2DataCollection = None
    mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
    # Methods and properties for the 'mxv2DataCollection_Reference' attribute
    def getMxv2DataCollection_Reference(self): return self._mxv2DataCollection_Reference
    def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setMxv2DataCollection_Reference argument is not XSDataCollection but %s" % mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection_Reference(self): self._mxv2DataCollection_Reference = None
    mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
    # Methods and properties for the 'possibleOrientations' attribute
    def getPossibleOrientations(self): return self._possibleOrientations
    def setPossibleOrientations(self, possibleOrientations):
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setPossibleOrientations argument is not kappa_alignment_response but %s" % possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    def delPossibleOrientations(self): self._possibleOrientations = None
    possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
    # Methods and properties for the 'omega' attribute
    def getOmega(self): return self._omega
    def setOmega(self, omega):
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setOmega argument is not XSDataAngle but %s" % omega.__class__.__name__
            raise BaseException(strMessage)
    def delOmega(self): self._omega = None
    omega = property(getOmega, setOmega, delOmega, "Property for omega")
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataAngle":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setKappa argument is not XSDataAngle but %s" % kappa.__class__.__name__
            raise BaseException(strMessage)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataAngle":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataInputInterfacev2_2.setPhi argument is not XSDataAngle but %s" % phi.__class__.__name__
            raise BaseException(strMessage)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    def export(self, outfile, level, name_='XSDataInputInterfacev2_2'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputInterfacev2_2'):
        XSDataInputInterface.exportChildren(self, outfile, level, name_)
        if self._mxv1InputCharacterisation is not None:
            self.mxv1InputCharacterisation.export(outfile, level, name_='mxv1InputCharacterisation')
        else:
            warnEmptyAttribute("mxv1InputCharacterisation", "XSDataInputCharacterisation")
        if self._mxv1ResultCharacterisation_Reference is not None:
            self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
        if self._mxv2DataCollection is not None:
            self.mxv2DataCollection.export(outfile, level, name_='mxv2DataCollection')
        if self._mxv2DataCollection_Reference is not None:
            self.mxv2DataCollection_Reference.export(outfile, level, name_='mxv2DataCollection_Reference')
        if self._possibleOrientations is not None:
            self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
        if self._omega is not None:
            self.omega.export(outfile, level, name_='omega')
        if self._kappa is not None:
            self.kappa.export(outfile, level, name_='kappa')
        if self._phi is not None:
            self.phi.export(outfile, level, name_='phi')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1InputCharacterisation':
            obj_ = XSDataInputCharacterisation()
            obj_.build(child_)
            self.setMxv1InputCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation_Reference':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection_Reference':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possibleOrientations':
            obj_ = kappa_alignment_response()
            obj_.build(child_)
            self.setPossibleOrientations(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omega':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOmega(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhi(obj_)
        XSDataInputInterface.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputInterfacev2_2" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputInterfacev2_2' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputInterfacev2_2 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputInterfacev2_2.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterfacev2_2()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputInterfacev2_2" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterfacev2_2()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputInterfacev2_2


class XSDataResultInterfacev2_2(XSDataResultInterface):
    def __init__(self, resultControlISPyB=None, resultCharacterisation=None, possibleOrientations=None, suggestedStrategy=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv2ResultCharacterisation=None, mxv1ResultCharacterisation_Reference=None, mxv1ResultCharacterisation=None):
        XSDataResultInterface.__init__(self, resultControlISPyB, resultCharacterisation)
        if mxv1ResultCharacterisation is None:
            self._mxv1ResultCharacterisation = None
        elif mxv1ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation = mxv1ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'mxv1ResultCharacterisation' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'mxv1ResultCharacterisation_Reference' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
        if mxv2ResultCharacterisation is None:
            self._mxv2ResultCharacterisation = None
        elif mxv2ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisationv2_0":
            self._mxv2ResultCharacterisation = mxv2ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'mxv2ResultCharacterisation' is not XSDataResultCharacterisationv2_0 but %s" % self._mxv2ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'mxv2DataCollection' is not XSDataCollection but %s" % self._mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'mxv2DataCollection_Reference' is not XSDataCollection but %s" % self._mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
        if suggestedStrategy is None:
            self._suggestedStrategy = None
        elif suggestedStrategy.__class__.__name__ == "XSDataResultStrategy":
            self._suggestedStrategy = suggestedStrategy
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'suggestedStrategy' is not XSDataResultStrategy but %s" % self._suggestedStrategy.__class__.__name__
            raise BaseException(strMessage)
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2 constructor argument 'possibleOrientations' is not kappa_alignment_response but %s" % self._possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mxv1ResultCharacterisation' attribute
    def getMxv1ResultCharacterisation(self): return self._mxv1ResultCharacterisation
    def setMxv1ResultCharacterisation(self, mxv1ResultCharacterisation):
        if mxv1ResultCharacterisation is None:
            self._mxv1ResultCharacterisation = None
        elif mxv1ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation = mxv1ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setMxv1ResultCharacterisation argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation(self): self._mxv1ResultCharacterisation = None
    mxv1ResultCharacterisation = property(getMxv1ResultCharacterisation, setMxv1ResultCharacterisation, delMxv1ResultCharacterisation, "Property for mxv1ResultCharacterisation")
    # Methods and properties for the 'mxv1ResultCharacterisation_Reference' attribute
    def getMxv1ResultCharacterisation_Reference(self): return self._mxv1ResultCharacterisation_Reference
    def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setMxv1ResultCharacterisation_Reference argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation_Reference(self): self._mxv1ResultCharacterisation_Reference = None
    mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
    # Methods and properties for the 'mxv2ResultCharacterisation' attribute
    def getMxv2ResultCharacterisation(self): return self._mxv2ResultCharacterisation
    def setMxv2ResultCharacterisation(self, mxv2ResultCharacterisation):
        if mxv2ResultCharacterisation is None:
            self._mxv2ResultCharacterisation = None
        elif mxv2ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisationv2_0":
            self._mxv2ResultCharacterisation = mxv2ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setMxv2ResultCharacterisation argument is not XSDataResultCharacterisationv2_0 but %s" % mxv2ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2ResultCharacterisation(self): self._mxv2ResultCharacterisation = None
    mxv2ResultCharacterisation = property(getMxv2ResultCharacterisation, setMxv2ResultCharacterisation, delMxv2ResultCharacterisation, "Property for mxv2ResultCharacterisation")
    # Methods and properties for the 'mxv2DataCollection' attribute
    def getMxv2DataCollection(self): return self._mxv2DataCollection
    def setMxv2DataCollection(self, mxv2DataCollection):
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setMxv2DataCollection argument is not XSDataCollection but %s" % mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection(self): self._mxv2DataCollection = None
    mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
    # Methods and properties for the 'mxv2DataCollection_Reference' attribute
    def getMxv2DataCollection_Reference(self): return self._mxv2DataCollection_Reference
    def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setMxv2DataCollection_Reference argument is not XSDataCollection but %s" % mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection_Reference(self): self._mxv2DataCollection_Reference = None
    mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
    # Methods and properties for the 'suggestedStrategy' attribute
    def getSuggestedStrategy(self): return self._suggestedStrategy
    def setSuggestedStrategy(self, suggestedStrategy):
        if suggestedStrategy is None:
            self._suggestedStrategy = None
        elif suggestedStrategy.__class__.__name__ == "XSDataResultStrategy":
            self._suggestedStrategy = suggestedStrategy
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setSuggestedStrategy argument is not XSDataResultStrategy but %s" % suggestedStrategy.__class__.__name__
            raise BaseException(strMessage)
    def delSuggestedStrategy(self): self._suggestedStrategy = None
    suggestedStrategy = property(getSuggestedStrategy, setSuggestedStrategy, delSuggestedStrategy, "Property for suggestedStrategy")
    # Methods and properties for the 'possibleOrientations' attribute
    def getPossibleOrientations(self): return self._possibleOrientations
    def setPossibleOrientations(self, possibleOrientations):
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataResultInterfacev2_2.setPossibleOrientations argument is not kappa_alignment_response but %s" % possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    def delPossibleOrientations(self): self._possibleOrientations = None
    possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
    def export(self, outfile, level, name_='XSDataResultInterfacev2_2'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultInterfacev2_2'):
        XSDataResultInterface.exportChildren(self, outfile, level, name_)
        if self._mxv1ResultCharacterisation is not None:
            self.mxv1ResultCharacterisation.export(outfile, level, name_='mxv1ResultCharacterisation')
        else:
            warnEmptyAttribute("mxv1ResultCharacterisation", "XSDataResultCharacterisation")
        if self._mxv1ResultCharacterisation_Reference is not None:
            self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
        if self._mxv2ResultCharacterisation is not None:
            self.mxv2ResultCharacterisation.export(outfile, level, name_='mxv2ResultCharacterisation')
        if self._mxv2DataCollection is not None:
            self.mxv2DataCollection.export(outfile, level, name_='mxv2DataCollection')
        if self._mxv2DataCollection_Reference is not None:
            self.mxv2DataCollection_Reference.export(outfile, level, name_='mxv2DataCollection_Reference')
        if self._suggestedStrategy is not None:
            self.suggestedStrategy.export(outfile, level, name_='suggestedStrategy')
        if self._possibleOrientations is not None:
            self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation_Reference':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2ResultCharacterisation':
            obj_ = XSDataResultCharacterisationv2_0()
            obj_.build(child_)
            self.setMxv2ResultCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection_Reference':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'suggestedStrategy':
            obj_ = XSDataResultStrategy()
            obj_.build(child_)
            self.setSuggestedStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possibleOrientations':
            obj_ = kappa_alignment_response()
            obj_.build(child_)
            self.setPossibleOrientations(obj_)
        XSDataResultInterface.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultInterfacev2_2" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultInterfacev2_2' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultInterfacev2_2 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultInterfacev2_2.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterfacev2_2()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultInterfacev2_2" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterfacev2_2()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultInterfacev2_2



# End of data representation classes.



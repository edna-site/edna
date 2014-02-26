#!/usr/bin/env python

#
# Generated Wed Feb 26 10:18::17 2014 by EDGenerateDS.
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
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
}

try:
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataFloat
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataString
    from XSDataMXv1 import XSDataDiffractionPlan
    from XSDataMXv1 import XSDataExperimentalCondition
    from XSDataMXv1 import XSDataInputCharacterisation
    from XSDataMXv1 import XSDataResultCharacterisation
    from XSDataMXv1 import XSDataResultControlISPyB
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
    from XSDataCommon import XSDataWavelength
    from XSDataMXv1 import XSDataSampleCrystalMM
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
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataResultControlISPyB
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength
from XSDataMXv1 import XSDataSampleCrystalMM




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



class XSDataInputInterface(object):
    def __init__(self, inputCharacterisation=None, comments=None, shortComments=None, dataCollectionId=None, transmission=None, wavelength=None, beamPosY=None, beamPosX=None, resultsFilePath=None, generatedTemplateFile=None, templateMode=None, beamSizeY=None, beamSizeX=None, beamSize=None, minExposureTimePerImage=None, flux=None, imagePath=None, sample=None, diffractionPlan=None, experimentalCondition=None):
        if experimentalCondition is None:
            self._experimentalCondition = None
        elif experimentalCondition.__class__.__name__ == "XSDataExperimentalCondition":
            self._experimentalCondition = experimentalCondition
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'experimentalCondition' is not XSDataExperimentalCondition but %s" % self._experimentalCondition.__class__.__name__
            raise BaseException(strMessage)
        if diffractionPlan is None:
            self._diffractionPlan = None
        elif diffractionPlan.__class__.__name__ == "XSDataDiffractionPlan":
            self._diffractionPlan = diffractionPlan
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'diffractionPlan' is not XSDataDiffractionPlan but %s" % self._diffractionPlan.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataSampleCrystalMM":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'sample' is not XSDataSampleCrystalMM but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if imagePath is None:
            self._imagePath = []
        elif imagePath.__class__.__name__ == "list":
            self._imagePath = imagePath
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'imagePath' is not list but %s" % self._imagePath.__class__.__name__
            raise BaseException(strMessage)
        if flux is None:
            self._flux = None
        elif flux.__class__.__name__ == "XSDataFloat":
            self._flux = flux
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'flux' is not XSDataFloat but %s" % self._flux.__class__.__name__
            raise BaseException(strMessage)
        if minExposureTimePerImage is None:
            self._minExposureTimePerImage = None
        elif minExposureTimePerImage.__class__.__name__ == "XSDataTime":
            self._minExposureTimePerImage = minExposureTimePerImage
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'minExposureTimePerImage' is not XSDataTime but %s" % self._minExposureTimePerImage.__class__.__name__
            raise BaseException(strMessage)
        if beamSize is None:
            self._beamSize = None
        elif beamSize.__class__.__name__ == "XSDataLength":
            self._beamSize = beamSize
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'beamSize' is not XSDataLength but %s" % self._beamSize.__class__.__name__
            raise BaseException(strMessage)
        if beamSizeX is None:
            self._beamSizeX = None
        elif beamSizeX.__class__.__name__ == "XSDataLength":
            self._beamSizeX = beamSizeX
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'beamSizeX' is not XSDataLength but %s" % self._beamSizeX.__class__.__name__
            raise BaseException(strMessage)
        if beamSizeY is None:
            self._beamSizeY = None
        elif beamSizeY.__class__.__name__ == "XSDataLength":
            self._beamSizeY = beamSizeY
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'beamSizeY' is not XSDataLength but %s" % self._beamSizeY.__class__.__name__
            raise BaseException(strMessage)
        if templateMode is None:
            self._templateMode = None
        elif templateMode.__class__.__name__ == "XSDataBoolean":
            self._templateMode = templateMode
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'templateMode' is not XSDataBoolean but %s" % self._templateMode.__class__.__name__
            raise BaseException(strMessage)
        if generatedTemplateFile is None:
            self._generatedTemplateFile = None
        elif generatedTemplateFile.__class__.__name__ == "XSDataFile":
            self._generatedTemplateFile = generatedTemplateFile
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'generatedTemplateFile' is not XSDataFile but %s" % self._generatedTemplateFile.__class__.__name__
            raise BaseException(strMessage)
        if resultsFilePath is None:
            self._resultsFilePath = None
        elif resultsFilePath.__class__.__name__ == "XSDataFile":
            self._resultsFilePath = resultsFilePath
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'resultsFilePath' is not XSDataFile but %s" % self._resultsFilePath.__class__.__name__
            raise BaseException(strMessage)
        if beamPosX is None:
            self._beamPosX = None
        elif beamPosX.__class__.__name__ == "XSDataFloat":
            self._beamPosX = beamPosX
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'beamPosX' is not XSDataFloat but %s" % self._beamPosX.__class__.__name__
            raise BaseException(strMessage)
        if beamPosY is None:
            self._beamPosY = None
        elif beamPosY.__class__.__name__ == "XSDataFloat":
            self._beamPosY = beamPosY
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'beamPosY' is not XSDataFloat but %s" % self._beamPosY.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if shortComments is None:
            self._shortComments = None
        elif shortComments.__class__.__name__ == "XSDataString":
            self._shortComments = shortComments
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'shortComments' is not XSDataString but %s" % self._shortComments.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if inputCharacterisation is None:
            self._inputCharacterisation = None
        elif inputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._inputCharacterisation = inputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputInterface constructor argument 'inputCharacterisation' is not XSDataInputCharacterisation but %s" % self._inputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'experimentalCondition' attribute
    def getExperimentalCondition(self): return self._experimentalCondition
    def setExperimentalCondition(self, experimentalCondition):
        if experimentalCondition is None:
            self._experimentalCondition = None
        elif experimentalCondition.__class__.__name__ == "XSDataExperimentalCondition":
            self._experimentalCondition = experimentalCondition
        else:
            strMessage = "ERROR! XSDataInputInterface.setExperimentalCondition argument is not XSDataExperimentalCondition but %s" % experimentalCondition.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalCondition(self): self._experimentalCondition = None
    experimentalCondition = property(getExperimentalCondition, setExperimentalCondition, delExperimentalCondition, "Property for experimentalCondition")
    # Methods and properties for the 'diffractionPlan' attribute
    def getDiffractionPlan(self): return self._diffractionPlan
    def setDiffractionPlan(self, diffractionPlan):
        if diffractionPlan is None:
            self._diffractionPlan = None
        elif diffractionPlan.__class__.__name__ == "XSDataDiffractionPlan":
            self._diffractionPlan = diffractionPlan
        else:
            strMessage = "ERROR! XSDataInputInterface.setDiffractionPlan argument is not XSDataDiffractionPlan but %s" % diffractionPlan.__class__.__name__
            raise BaseException(strMessage)
    def delDiffractionPlan(self): self._diffractionPlan = None
    diffractionPlan = property(getDiffractionPlan, setDiffractionPlan, delDiffractionPlan, "Property for diffractionPlan")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataSampleCrystalMM":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputInterface.setSample argument is not XSDataSampleCrystalMM but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'imagePath' attribute
    def getImagePath(self): return self._imagePath
    def setImagePath(self, imagePath):
        if imagePath is None:
            self._imagePath = []
        elif imagePath.__class__.__name__ == "list":
            self._imagePath = imagePath
        else:
            strMessage = "ERROR! XSDataInputInterface.setImagePath argument is not list but %s" % imagePath.__class__.__name__
            raise BaseException(strMessage)
    def delImagePath(self): self._imagePath = None
    imagePath = property(getImagePath, setImagePath, delImagePath, "Property for imagePath")
    def addImagePath(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputInterface.addImagePath argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._imagePath.append(value)
        else:
            strMessage = "ERROR! XSDataInputInterface.addImagePath argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImagePath(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputInterface.insertImagePath argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputInterface.insertImagePath argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._imagePath[index] = value
        else:
            strMessage = "ERROR! XSDataInputInterface.addImagePath argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'flux' attribute
    def getFlux(self): return self._flux
    def setFlux(self, flux):
        if flux is None:
            self._flux = None
        elif flux.__class__.__name__ == "XSDataFloat":
            self._flux = flux
        else:
            strMessage = "ERROR! XSDataInputInterface.setFlux argument is not XSDataFloat but %s" % flux.__class__.__name__
            raise BaseException(strMessage)
    def delFlux(self): self._flux = None
    flux = property(getFlux, setFlux, delFlux, "Property for flux")
    # Methods and properties for the 'minExposureTimePerImage' attribute
    def getMinExposureTimePerImage(self): return self._minExposureTimePerImage
    def setMinExposureTimePerImage(self, minExposureTimePerImage):
        if minExposureTimePerImage is None:
            self._minExposureTimePerImage = None
        elif minExposureTimePerImage.__class__.__name__ == "XSDataTime":
            self._minExposureTimePerImage = minExposureTimePerImage
        else:
            strMessage = "ERROR! XSDataInputInterface.setMinExposureTimePerImage argument is not XSDataTime but %s" % minExposureTimePerImage.__class__.__name__
            raise BaseException(strMessage)
    def delMinExposureTimePerImage(self): self._minExposureTimePerImage = None
    minExposureTimePerImage = property(getMinExposureTimePerImage, setMinExposureTimePerImage, delMinExposureTimePerImage, "Property for minExposureTimePerImage")
    # Methods and properties for the 'beamSize' attribute
    def getBeamSize(self): return self._beamSize
    def setBeamSize(self, beamSize):
        if beamSize is None:
            self._beamSize = None
        elif beamSize.__class__.__name__ == "XSDataLength":
            self._beamSize = beamSize
        else:
            strMessage = "ERROR! XSDataInputInterface.setBeamSize argument is not XSDataLength but %s" % beamSize.__class__.__name__
            raise BaseException(strMessage)
    def delBeamSize(self): self._beamSize = None
    beamSize = property(getBeamSize, setBeamSize, delBeamSize, "Property for beamSize")
    # Methods and properties for the 'beamSizeX' attribute
    def getBeamSizeX(self): return self._beamSizeX
    def setBeamSizeX(self, beamSizeX):
        if beamSizeX is None:
            self._beamSizeX = None
        elif beamSizeX.__class__.__name__ == "XSDataLength":
            self._beamSizeX = beamSizeX
        else:
            strMessage = "ERROR! XSDataInputInterface.setBeamSizeX argument is not XSDataLength but %s" % beamSizeX.__class__.__name__
            raise BaseException(strMessage)
    def delBeamSizeX(self): self._beamSizeX = None
    beamSizeX = property(getBeamSizeX, setBeamSizeX, delBeamSizeX, "Property for beamSizeX")
    # Methods and properties for the 'beamSizeY' attribute
    def getBeamSizeY(self): return self._beamSizeY
    def setBeamSizeY(self, beamSizeY):
        if beamSizeY is None:
            self._beamSizeY = None
        elif beamSizeY.__class__.__name__ == "XSDataLength":
            self._beamSizeY = beamSizeY
        else:
            strMessage = "ERROR! XSDataInputInterface.setBeamSizeY argument is not XSDataLength but %s" % beamSizeY.__class__.__name__
            raise BaseException(strMessage)
    def delBeamSizeY(self): self._beamSizeY = None
    beamSizeY = property(getBeamSizeY, setBeamSizeY, delBeamSizeY, "Property for beamSizeY")
    # Methods and properties for the 'templateMode' attribute
    def getTemplateMode(self): return self._templateMode
    def setTemplateMode(self, templateMode):
        if templateMode is None:
            self._templateMode = None
        elif templateMode.__class__.__name__ == "XSDataBoolean":
            self._templateMode = templateMode
        else:
            strMessage = "ERROR! XSDataInputInterface.setTemplateMode argument is not XSDataBoolean but %s" % templateMode.__class__.__name__
            raise BaseException(strMessage)
    def delTemplateMode(self): self._templateMode = None
    templateMode = property(getTemplateMode, setTemplateMode, delTemplateMode, "Property for templateMode")
    # Methods and properties for the 'generatedTemplateFile' attribute
    def getGeneratedTemplateFile(self): return self._generatedTemplateFile
    def setGeneratedTemplateFile(self, generatedTemplateFile):
        if generatedTemplateFile is None:
            self._generatedTemplateFile = None
        elif generatedTemplateFile.__class__.__name__ == "XSDataFile":
            self._generatedTemplateFile = generatedTemplateFile
        else:
            strMessage = "ERROR! XSDataInputInterface.setGeneratedTemplateFile argument is not XSDataFile but %s" % generatedTemplateFile.__class__.__name__
            raise BaseException(strMessage)
    def delGeneratedTemplateFile(self): self._generatedTemplateFile = None
    generatedTemplateFile = property(getGeneratedTemplateFile, setGeneratedTemplateFile, delGeneratedTemplateFile, "Property for generatedTemplateFile")
    # Methods and properties for the 'resultsFilePath' attribute
    def getResultsFilePath(self): return self._resultsFilePath
    def setResultsFilePath(self, resultsFilePath):
        if resultsFilePath is None:
            self._resultsFilePath = None
        elif resultsFilePath.__class__.__name__ == "XSDataFile":
            self._resultsFilePath = resultsFilePath
        else:
            strMessage = "ERROR! XSDataInputInterface.setResultsFilePath argument is not XSDataFile but %s" % resultsFilePath.__class__.__name__
            raise BaseException(strMessage)
    def delResultsFilePath(self): self._resultsFilePath = None
    resultsFilePath = property(getResultsFilePath, setResultsFilePath, delResultsFilePath, "Property for resultsFilePath")
    # Methods and properties for the 'beamPosX' attribute
    def getBeamPosX(self): return self._beamPosX
    def setBeamPosX(self, beamPosX):
        if beamPosX is None:
            self._beamPosX = None
        elif beamPosX.__class__.__name__ == "XSDataFloat":
            self._beamPosX = beamPosX
        else:
            strMessage = "ERROR! XSDataInputInterface.setBeamPosX argument is not XSDataFloat but %s" % beamPosX.__class__.__name__
            raise BaseException(strMessage)
    def delBeamPosX(self): self._beamPosX = None
    beamPosX = property(getBeamPosX, setBeamPosX, delBeamPosX, "Property for beamPosX")
    # Methods and properties for the 'beamPosY' attribute
    def getBeamPosY(self): return self._beamPosY
    def setBeamPosY(self, beamPosY):
        if beamPosY is None:
            self._beamPosY = None
        elif beamPosY.__class__.__name__ == "XSDataFloat":
            self._beamPosY = beamPosY
        else:
            strMessage = "ERROR! XSDataInputInterface.setBeamPosY argument is not XSDataFloat but %s" % beamPosY.__class__.__name__
            raise BaseException(strMessage)
    def delBeamPosY(self): self._beamPosY = None
    beamPosY = property(getBeamPosY, setBeamPosY, delBeamPosY, "Property for beamPosY")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputInterface.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataInputInterface.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputInterface.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'shortComments' attribute
    def getShortComments(self): return self._shortComments
    def setShortComments(self, shortComments):
        if shortComments is None:
            self._shortComments = None
        elif shortComments.__class__.__name__ == "XSDataString":
            self._shortComments = shortComments
        else:
            strMessage = "ERROR! XSDataInputInterface.setShortComments argument is not XSDataString but %s" % shortComments.__class__.__name__
            raise BaseException(strMessage)
    def delShortComments(self): self._shortComments = None
    shortComments = property(getShortComments, setShortComments, delShortComments, "Property for shortComments")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataInputInterface.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'inputCharacterisation' attribute
    def getInputCharacterisation(self): return self._inputCharacterisation
    def setInputCharacterisation(self, inputCharacterisation):
        if inputCharacterisation is None:
            self._inputCharacterisation = None
        elif inputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._inputCharacterisation = inputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputInterface.setInputCharacterisation argument is not XSDataInputCharacterisation but %s" % inputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delInputCharacterisation(self): self._inputCharacterisation = None
    inputCharacterisation = property(getInputCharacterisation, setInputCharacterisation, delInputCharacterisation, "Property for inputCharacterisation")
    def export(self, outfile, level, name_='XSDataInputInterface'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputInterface'):
        pass
        if self._experimentalCondition is not None:
            self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        if self._diffractionPlan is not None:
            self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        for imagePath_ in self.getImagePath():
            imagePath_.export(outfile, level, name_='imagePath')
        if self._flux is not None:
            self.flux.export(outfile, level, name_='flux')
        if self._minExposureTimePerImage is not None:
            self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
        if self._beamSize is not None:
            self.beamSize.export(outfile, level, name_='beamSize')
        if self._beamSizeX is not None:
            self.beamSizeX.export(outfile, level, name_='beamSizeX')
        if self._beamSizeY is not None:
            self.beamSizeY.export(outfile, level, name_='beamSizeY')
        if self._templateMode is not None:
            self.templateMode.export(outfile, level, name_='templateMode')
        if self._generatedTemplateFile is not None:
            self.generatedTemplateFile.export(outfile, level, name_='generatedTemplateFile')
        if self._resultsFilePath is not None:
            self.resultsFilePath.export(outfile, level, name_='resultsFilePath')
        if self._beamPosX is not None:
            self.beamPosX.export(outfile, level, name_='beamPosX')
        if self._beamPosY is not None:
            self.beamPosY.export(outfile, level, name_='beamPosY')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self._shortComments is not None:
            self.shortComments.export(outfile, level, name_='shortComments')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._inputCharacterisation is not None:
            self.inputCharacterisation.export(outfile, level, name_='inputCharacterisation')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataDiffractionPlan()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSampleCrystalMM()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePath':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.imagePath.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setFlux(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposureTimePerImage':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setMinExposureTimePerImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSize':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeX':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamSizeX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeY':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setBeamSizeY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'templateMode':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setTemplateMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'generatedTemplateFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGeneratedTemplateFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultsFilePath':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setResultsFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPosX':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setBeamPosX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPosY':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setBeamPosY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shortComments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setShortComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCharacterisation':
            obj_ = XSDataInputCharacterisation()
            obj_.build(child_)
            self.setInputCharacterisation(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputInterface" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputInterface' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputInterface is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputInterface.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterface()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputInterface" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterface()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputInterface


class XSDataResultInterface(object):
    def __init__(self, resultControlISPyB=None, resultCharacterisation=None):
        if resultCharacterisation is None:
            self._resultCharacterisation = None
        elif resultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._resultCharacterisation = resultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterface constructor argument 'resultCharacterisation' is not XSDataResultCharacterisation but %s" % self._resultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if resultControlISPyB is None:
            self._resultControlISPyB = None
        elif resultControlISPyB.__class__.__name__ == "XSDataResultControlISPyB":
            self._resultControlISPyB = resultControlISPyB
        else:
            strMessage = "ERROR! XSDataResultInterface constructor argument 'resultControlISPyB' is not XSDataResultControlISPyB but %s" % self._resultControlISPyB.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'resultCharacterisation' attribute
    def getResultCharacterisation(self): return self._resultCharacterisation
    def setResultCharacterisation(self, resultCharacterisation):
        if resultCharacterisation is None:
            self._resultCharacterisation = None
        elif resultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._resultCharacterisation = resultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultInterface.setResultCharacterisation argument is not XSDataResultCharacterisation but %s" % resultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delResultCharacterisation(self): self._resultCharacterisation = None
    resultCharacterisation = property(getResultCharacterisation, setResultCharacterisation, delResultCharacterisation, "Property for resultCharacterisation")
    # Methods and properties for the 'resultControlISPyB' attribute
    def getResultControlISPyB(self): return self._resultControlISPyB
    def setResultControlISPyB(self, resultControlISPyB):
        if resultControlISPyB is None:
            self._resultControlISPyB = None
        elif resultControlISPyB.__class__.__name__ == "XSDataResultControlISPyB":
            self._resultControlISPyB = resultControlISPyB
        else:
            strMessage = "ERROR! XSDataResultInterface.setResultControlISPyB argument is not XSDataResultControlISPyB but %s" % resultControlISPyB.__class__.__name__
            raise BaseException(strMessage)
    def delResultControlISPyB(self): self._resultControlISPyB = None
    resultControlISPyB = property(getResultControlISPyB, setResultControlISPyB, delResultControlISPyB, "Property for resultControlISPyB")
    def export(self, outfile, level, name_='XSDataResultInterface'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultInterface'):
        pass
        if self._resultCharacterisation is not None:
            self.resultCharacterisation.export(outfile, level, name_='resultCharacterisation')
        if self._resultControlISPyB is not None:
            self.resultControlISPyB.export(outfile, level, name_='resultControlISPyB')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultCharacterisation':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setResultCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultControlISPyB':
            obj_ = XSDataResultControlISPyB()
            obj_.build(child_)
            self.setResultControlISPyB(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultInterface" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultInterface' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultInterface is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultInterface.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterface()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultInterface" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterface()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultInterface



# End of data representation classes.



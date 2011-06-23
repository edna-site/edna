# coding: utf8
# 
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Jérôme Kieffer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
ReImplementation of the Reprocess script: Process one file  
( by ricardo.fernandes@esrf.fr)
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, sys
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsProcessOneFilev1_0, XSDataResultBioSaxsProcessOneFilev1_0, \
                            XSDataString, XSDataFile, XSDataImage, XSDataInteger, \
                            XSDataInputBioSaxsNormalizev1_0, XSDataInputBioSaxsAzimutIntv1_0


class EDPluginControlBioSaxsProcessOneFilev1_0(EDPluginControl):
    """
    Control plugin that does what was in the Reprocess function in the original program 
    
    """

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsProcessOneFilev1_0)
        self.__strControlledPluginNomalize = "EDPluginBioSaxsNormalizev1_1"
        self.__strControlledPluginIntegrate = "EDPluginBioSaxsAzimutIntv1_1"
        self.__edPluginNormalize = None
        self.__edPluginIntegrate = None


        self.xsdInputData = None
        self.strDetector = None
        self.strOperation = None
        self.strDirectory = None
        self.strRawDir = None
        self.str1dDir = None
        self.str2dDir = None
        self.strMiscDir = None
        self.strPrefix = None
        self.specStatus = None
        self.specVersion = None
        self.specAbort = None
        self.beamCenterX = None
        self.pixelSizeX = None
        self.pixelSizeY = None
        self.beamCenterY = None
        self.beamStopDiode = None
        self.strCode = None
        self.strComments = None
        self.fConcentration = None
        self.bKeepOriginal = True
        self.machineCurrent = None
        self.wavelength = None
        self.iRunNumber = None
        self.maskFile = None
        self.normalisation = None
        self.bIsOnline = False
        self.listFrames = []
        self.iRawImageSize = 1024
        self.normalizedImage = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image provided")

#    rawImageSize : XSDataInteger
#//    logFile : XSDataFile optional
#    normalizedImage : XSDataImage
#    integratedImage : XSDataImage
#    integratedCurve : XSDataFile
#    correctedImage : XSDataImage



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginNormalize = self.loadPlugin(self.__strControlledPluginNomalize)
        self.__edPluginIntegrate = self.loadPlugin(self.__strControlledPluginIntegrate)

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.process")
        self.__edPluginNormalize.connectSUCCESS(self.doSuccessNomalize)
        self.__edPluginNormalize.connectFAILURE(self.doFailureNomalize)
        xsd = XSDataInputBioSaxsNormalizev1_0()
        xsd.rawImage = self.dataInput.rawImage
        xsd.normalizedImage = self.dataInput.normalizedImage
        xsd.rawImageSize = XSDataInteger(self.iRawImageSize)

        xsd.detector = self.dataInput.detector
        xsd.detectorDistance = self.dataInput.detectorDistance
        xsd.pixelSize_1 = self.dataInput.pixelSize_1
        xsd.pixelSize_2 = self.dataInput.pixelSize_2
        xsd.beamCenter_1 = self.dataInput.beamCenter_1
        xsd.beamCenter_2 = self.dataInput.beamCenter_2
        xsd.beamStopDiode = self.dataInput.beamStopDiode
        xsd.wavelength = self.dataInput.wavelength
        xsd.machineCurrent = self.dataInput.machineCurrent
        xsd.maskFile = self.dataInput.maskFile
        xsd.normalizationFactor = self.dataInput.normalizationFactor
        xsd.sampleConcentration = self.dataInput.sampleConcentration
        xsd.sampleComments = self.dataInput.sampleComments
        xsd.sampleCode = self.dataInput.sampleCode
        xsd.logFile = self.dataInput.logFile

        self.__edPluginNormalize.dataInput = xsd
        self.__edPluginNormalize.executeSynchronous()

        self.__edPluginIntegrate.connectSUCCESS(self.doSuccessIntegrate)
        self.__edPluginIntegrate.connectFAILURE(self.doFailureIntegrate)
        xsd = XSDataInputBioSaxsAzimutIntv1_0()
        xsd.normalizedImage = self.dataInput.normalizedImage
        xsd.normalizedImageSize = XSDataInteger(self.iRawImageSize)
        xsd.integratedImage = self.dataInput.integratedImage
        xsd.integratedCurve = self.dataInput.integratedCurve

        xsd.detector = self.dataInput.detector
        xsd.detectorDistance = self.dataInput.detectorDistance
        xsd.pixelSize_1 = self.dataInput.pixelSize_1
        xsd.pixelSize_2 = self.dataInput.pixelSize_2
        xsd.beamCenter_1 = self.dataInput.beamCenter_1
        xsd.beamCenter_2 = self.dataInput.beamCenter_2
        xsd.beamStopDiode = self.dataInput.beamStopDiode
        xsd.wavelength = self.dataInput.wavelength
        xsd.machineCurrent = self.dataInput.machineCurrent
        xsd.maskFile = self.dataInput.maskFile
        xsd.normalizationFactor = self.dataInput.normalizationFactor
        xsd.sampleConcentration = self.dataInput.sampleConcentration
        xsd.sampleComments = self.dataInput.sampleComments
        xsd.sampleCode = self.dataInput.sampleCode
        xsd.logFile = self.dataInput.logFile

        self.__edPluginIntegrate.dataInput = xsd
        self.__edPluginIntegrate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsProcessOneFilev1_0()

        xsDataResult.normalizedImage = XSDataImage()
        xsDataResult.integratedImage = XSDataImage()
        xsDataResult.outputCurve = XSDataFile()
        self.setDataOutput(xsDataResult)


    def doSuccessNomalize(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.doSuccessNomalize")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsProcessOneFilev1_0.doSuccessNomalize")


    def doFailureNomalize(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.doFailureNomalize")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsProcessOneFilev1_0.doFailureNomalize")

    def doSuccessIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.doSuccessIntegrate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlBioSaxsProcessOneFilev1_0.doSuccessIntegrate")


    def doFailureIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginControlBioSaxsProcessOneFilev1_0.doFailureIntegrate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlBioSaxsProcessOneFilev1_0.doFailureIntegrate")

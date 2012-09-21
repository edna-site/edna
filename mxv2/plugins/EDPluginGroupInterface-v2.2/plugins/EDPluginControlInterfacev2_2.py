#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlInterfacev2_2.py 3504 2011-06-27 09:18:44Z svensson $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Olof Svensson", "Karl Levik"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, shutil

from EDUtilsImage       import EDUtilsImage
from EDUtilsFile        import EDUtilsFile
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDMessage          import EDMessage
from EDConfiguration    import EDConfiguration
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsImage import EDUtilsImage


from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataAngularSpeed
from XSDataCommon import XSDataFlux
from XSDataCommon import XSDataWavelength

EDFactoryPluginStatic.loadModule("XSDataMXv1")
EDFactoryPluginStatic.loadModule("XSDataMXv2")
EDFactoryPluginStatic.loadModule("XSDataInterfacev1_2")
EDFactoryPluginStatic.loadModule("EDHandlerESRFPyarchv1_0")
EDFactoryPluginStatic.loadModule("XSDataSimpleHTMLPagev1_0")

import XSDataMXv1
import XSDataMXv2

from XSDataInterfacev2_2 import XSDataInputInterfacev2_2
from XSDataInterfacev2_2 import XSDataResultInterfacev2_2

from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from XSDataSimpleHTMLPagev1_0 import XSDataInputSimpleHTMLPage

class EDPluginControlInterfacev2_2(EDPluginControl):
    """
    This is the common class to all plugins managing user interfaces
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)

        self.setXSDataInputClass(XSDataInputInterfacev2_2)

        self.setXSDataInputClass(XSDataMXv1.XSDataExperimentalCondition, "experimentalCondition")
        self.setXSDataInputClass(XSDataMXv1.XSDataDiffractionPlan, "diffractionPlan")
        self.setXSDataInputClass(XSDataMXv1.XSDataSampleCrystalMM, "sample")
        self.setXSDataInputClass(XSDataString, "imagePaths")
        self.setXSDataInputClass(XSDataFloat, "flux")
        self.setXSDataInputClass(XSDataFloat, "minExposureTimePerImage")
        self.setXSDataInputClass(XSDataFloat, "beamSize")
        self.setXSDataInputClass(XSDataFloat, "beamSizeX")
        self.setXSDataInputClass(XSDataFloat, "beamSizeY")
        self.setXSDataInputClass(XSDataBoolean, "templateMode")
        self.setXSDataInputClass(XSDataString, "generatedTemplateFile")
        self.setXSDataInputClass(XSDataString, "generatedTemplateFileMXv2")
        self.setXSDataInputClass(XSDataString, "resultsFilePath")
        self.setXSDataInputClass(XSDataFloat, "beamPosX")
        self.setXSDataInputClass(XSDataFloat, "beamPosY")
        self.setXSDataInputClass(XSDataDouble, "wavelength")
        self.setXSDataInputClass(XSDataDouble, "transmission")
        self.setXSDataInputClass(XSDataInteger, "dataCollectionId")
        self.setXSDataInputClass(XSDataString, "shortComments")
        self.setXSDataInputClass(XSDataString, "comments")
        self.setXSDataInputClass(XSDataMXv1.XSDataInputCharacterisation, "inputCharacterisation")
        self.setXSDataInputClass(XSDataMXv2.XSDataCollection, "mxv2DataCollection")

        self.strEDPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev1_1"
        strEDPluginControlCharacterisationName = None
        self.strEDPluginControlCharForReorientationName = "EDPluginControlCharForReorientationv2_0"
        self.strEDPluginControlCharAtNewOrientationName = "EDPluginControlCharAtNewOrientationv2_0"
        self.strEDPluginControlISPyBName = "EDPluginControlISPyBv1_4"

        self.edPluginControlSubWedgeAssemble = None
        self.edPluginControlCharacterisationv2 = None
        self.edPluginControlISPyB = None

        self.pyListImagePaths = None
        self.xsDataInputCharacterisation = None
        self.xsDataInputCharacterisationv2_0 = None
        self.xsDataCollectionMXv2 = None
        self.strComplexity = "none"

        self.listImagePaths = []
        self.fFlux = None
        self.fMaxExposureTimePerDataCollection = 10000 # s, default prototype value
        self.fMinExposureTimePerImage = None
        self.fBeamSizeX = None
        self.fBeamSizeY = None
        self.bTemplateMode = False
        self.strGeneratedTemplateFile = None
        self.strGeneratedTemplateFileMXv2 = None
        self.strResultsFilePath = None
        self.strForcedSpaceGroup = None
        self.bAnomalousData = False
        self.fBeamPosX = None
        self.fBeamPosY = None
        self.fMinOscillationWidth = None
        self.fMaxOscillationSpeed = None
        self.fWavelength = None
        self.fTransmission = None
        self.strStrategyOption = None
        self.listKappaStrategyOption = []
        self.iDataCollectionId = None
        self.strShortComments = None
        self.strComments = None
        self.strStatusMessage = None

        self.xsDataExperimentalCodition = None
        self.xsDataSample = None
        self.xsDataDiffractionPlan = None
        
        self.mxv1InputCharacterisation = None
        self.mxv1ResultCharacterisation_Reference = None
        self.mxv2DataCollection = None
        self.mxv2DataCollection_Reference = None
        self.mxv2PossibleOrientations = None
        
        self.fKappa = None
        self.fOmega = None
        self.fPhi = None
        self.strCreateSimpleHTMLPageForISPyB = None
        self.strPluginExecSimpleHTMLName = "EDPluginExecSimpleHTMLPagev1_0"
        self.edPluginExecSimpleHTML = None        



    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.configure")
        pluginConfiguration = self.getConfiguration()

        if (pluginConfiguration is None):
            EDVerbose.DEBUG("No plugin configuration found for EDPluginControlInterfacev2_2.")
        else:
            if (self.getControlledPluginName("subWedgeAssemblePlugin") is not None):
                self.strEDPluginControlSubWedgeAssembleName = self.getControlledPluginName("subWedgeAssemblePlugin")
            if (self.getControlledPluginName("characterisationPlugin") is not None):
                self.strEDPluginControlCharacterisationName = self.getControlledPluginName("characterisationPlugin")
            if (self.getControlledPluginName("ispybPlugin") is not None):
                self.strEDPluginControlISPyBName = self.getControlledPluginName("ispybPlugin")

            bUseISPyBPlugin = EDConfiguration.getStringParamValue(pluginConfiguration, "useISPyBPlugin")
            if (bUseISPyBPlugin.lower() != "true"):
                self.strEDPluginControlISPyBName = None


    def preProcess(self, _edPlugin=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.preProcess...")

        self.listImagePaths = []

        # Check if XSDataInputInterface is given as input
        if self.hasDataInput():
            xsDataInputInterface = self.getDataInput()

            if xsDataInputInterface.getExperimentalCondition():
                self.xsDataExperimentalCodition = xsDataInputInterface.getExperimentalCondition()
                if self.xsDataExperimentalCodition.getGoniostat():
                    if self.xsDataExperimentalCodition.getGoniostat().getMinOscillationWidth():
                        self.fMinOscillationWidth = self.xsDataExperimentalCodition.getGoniostat().getMinOscillationWidth().getValue()
                    if self.xsDataExperimentalCodition.getGoniostat().getMaxOscillationSpeed():
                        self.fMaxOscillationSpeed = self.xsDataExperimentalCodition.getGoniostat().getMaxOscillationSpeed().getValue()


            self.xsDataSample = xsDataInputInterface.getSample()

            self.xsDataDiffractionPlan = self.getDataInput().getDiffractionPlan()
            if self.xsDataDiffractionPlan:
                if self.xsDataDiffractionPlan.getForcedSpaceGroup():
                    self.strForcedSpaceGroup = self.xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
                if self.xsDataDiffractionPlan.getMaxExposureTimePerDataCollection():
                    self.fMaxExposureTimePerDataCollection = self.xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue()
                if self.xsDataDiffractionPlan.getAnomalousData():
                    self.bAnomalousData = self.xsDataDiffractionPlan.getAnomalousData().getValue()
                if self.xsDataDiffractionPlan.getStrategyOption():
                    self.strStrategyOption = self.xsDataDiffractionPlan.getStrategyOption().getValue()
                if self.xsDataDiffractionPlan.getKappaStrategyOption():
                    self.listKappaStrategyOption = self.xsDataDiffractionPlan.getKappaStrategyOption()
                if self.xsDataDiffractionPlan.getComplexity():
                    self.strComplexity = self.xsDataDiffractionPlan.getComplexity().getValue()
                if self.fMinOscillationWidth == None:
                    if self.xsDataDiffractionPlan.getGoniostatMinOscillationWidth():
                        self.fMinOscillationWidth = self.xsDataDiffractionPlan.getGoniostatMinOscillationWidth().getValue()
                if self.fMaxOscillationSpeed == None:
                    if self.xsDataDiffractionPlan.getGoniostatMaxOscillationSpeed():
                        self.fMaxOscillationSpeed = self.xsDataDiffractionPlan.getGoniostatMaxOscillationSpeed().getValue()


            self.xsDataSample = xsDataInputInterface.getSample()

            if xsDataInputInterface.getImagePath():
                for xsDataFile in xsDataInputInterface.getImagePath():
                    self.listImagePaths.append(xsDataFile.getPath())

            if xsDataInputInterface.getFlux():
                self.fFlux = xsDataInputInterface.getFlux().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getFlux() != None:
                        self.fFlux = self.xsDataExperimentalCodition.getBeam().getFlux().getValue()

            if xsDataInputInterface.getMinExposureTimePerImage():
                self.fMinExposureTimePerImage = xsDataInputInterface.getMinExposureTimePerImage().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getMinExposureTimePerImage() != None:
                        self.fMinExposureTimePerImage = self.xsDataExperimentalCodition.getBeam().getMinExposureTimePerImage().getValue()
            if self.fMinExposureTimePerImage == None and xsDataInputInterface.getDiffractionPlan():
                if xsDataInputInterface.getDiffractionPlan().getMinExposureTimePerImage() != None:
                    self.fMinExposureTimePerImage = xsDataInputInterface.getdiffractionPlan().getMinExposureTimePerImage().getValue()

            if self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getSize() != None:
                        self.fBeamSizeX = self.xsDataExperimentalCodition.getBeam().getSize().getX().getValue()
                        self.fBeamSizeY = self.xsDataExperimentalCodition.getBeam().getSize().getY().getValue()

            if xsDataInputInterface.getBeamSize():
                self.fBeamSizeX = xsDataInputInterface.getBeamSize().getValue()
                self.fBeamSizeY = xsDataInputInterface.getBeamSize().getValue()

            if xsDataInputInterface.getBeamSizeX():
                self.fBeamSizeX = xsDataInputInterface.getBeamSizeX().getValue()

            if xsDataInputInterface.getBeamSizeY():
                self.fBeamSizeY = xsDataInputInterface.getBeamSizeY().getValue()

            if xsDataInputInterface.getTemplateMode():
                self.bTemplateMode = xsDataInputInterface.getTemplateMode().getValue()

            if xsDataInputInterface.getBeamPosX():
                self.fBeamPosX = xsDataInputInterface.getBeamPosX().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getDetector() != None:
                    if self.xsDataExperimentalCodition.getDetector().getBeamPositionX() != None:
                        self.fBeamPosX = self.xsDataExperimentalCodition.getDetector().getBeamPositionX().getValue()

            if xsDataInputInterface.getBeamPosY():
                self.fBeamPosY = xsDataInputInterface.getBeamPosY().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getDetector() != None:
                    if self.xsDataExperimentalCodition.getDetector().getBeamPositionY() != None:
                        self.fBeamPosY = self.xsDataExperimentalCodition.getDetector().getBeamPositionY().getValue()

            if xsDataInputInterface.getWavelength():
                self.fWavelength = xsDataInputInterface.getWavelength().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getWavelength() != None:
                        self.fWavelength = self.xsDataExperimentalCodition.getBeam().getWavelength().getValue()

            if xsDataInputInterface.getTransmission():
                self.fTransmission = xsDataInputInterface.getTransmission().getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getTransmission() != None:
                        self.fTransmission = self.xsDataExperimentalCodition.getBeam().getTransmission().getValue()

            if xsDataInputInterface.getGeneratedTemplateFile():
                self.strGeneratedTemplateFile = xsDataInputInterface.getGeneratedTemplateFile().getPath().getValue()

            if xsDataInputInterface.getResultsFilePath():
                self.strResultsFilePath = xsDataInputInterface.getResultsFilePath().getPath().getValue()

            if xsDataInputInterface.getDataCollectionId():
                self.iDataCollectionId = xsDataInputInterface.getDataCollectionId().getValue()

            if xsDataInputInterface.getShortComments():
                self.strShortComments = xsDataInputInterface.getShortComments().getValue()

            if xsDataInputInterface.getComments():
                self.strComments = xsDataInputInterface.getComments().getValue()

            if xsDataInputInterface.getInputCharacterisation():
                self.xsDataInputCharacterisation = xsDataInputInterface.getInputCharacterisation()

            if xsDataInputInterface.getDataCollectionId():
                self.iDataCollectionId = xsDataInputInterface.getDataCollectionId().getValue()

            if xsDataInputInterface.getMxv1InputCharacterisation():
                self.mxv1InputCharacterisation = xsDataInputInterface.getMxv1InputCharacterisation()
                
            if xsDataInputInterface.getMxv1ResultCharacterisation_Reference():
                self.mxv1ResultCharacterisation_Reference = xsDataInputInterface.getMxv1ResultCharacterisation_Reference()
            
            if xsDataInputInterface.getMxv2DataCollection():
                self.mxv2DataCollection = xsDataInputInterface.getMxv2DataCollection()
                
            if xsDataInputInterface.getMxv2DataCollection_Reference():                
                self.mxv2DataCollection_Reference = xsDataInputInterface.getMxv2DataCollection()
                
            if xsDataInputInterface.getPossibleOrientations():
                self.mxv2PossibleOrientations = xsDataInputInterface.getPossibleOrientations()
                
            if xsDataInputInterface.getKappa():
                self.fKappa = xsDataInputInterface.getKappa().getValue()

            if xsDataInputInterface.getOmega():
                self.fOmega = xsDataInputInterface.getOmega().getValue()

            if xsDataInputInterface.getPhi():
                self.fPhi = xsDataInputInterface.getPhi().getValue()

        else:

            if self.hasDataInput("experimentalCondition"):
                self.xsDataExperimentalCodition = self.getDataInput("experimentalCondition")[0]
                if self.xsDataExperimentalCodition.getGoniostat():
                    if self.xsDataExperimentalCodition.getGoniostat().getMinOscillationWidth():
                        self.fMinOscillationWidth = self.xsDataExperimentalCodition.getGoniostat().getMinOscillationWidth().getValue()
                    if self.xsDataExperimentalCodition.getGoniostat().getMaxOscillationSpeed():
                        self.fMaxOscillationSpeed = self.xsDataExperimentalCodition.getGoniostat().getMaxOscillationSpeed().getValue()


            if self.hasDataInput("sample"):
                self.xsDataSample = self.getDataInput("sample")[0]

            if (self.hasDataInput("diffractionPlan")):
                if self.xsDataDiffractionPlan is None:
                    self.xsDataDiffractionPlan = XSDataMXv1.XSDataDiffractionPlan()
                xsDataDiffractionPlans = self.getDataInput("diffractionPlan")
                if (not xsDataDiffractionPlans[0] is None):
                    self.xsDataDiffractionPlan = xsDataDiffractionPlans[0]
                    if self.xsDataDiffractionPlan.getForcedSpaceGroup():
                        self.strForcedSpaceGroup = self.xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
                    if self.xsDataDiffractionPlan.getMaxExposureTimePerDataCollection():
                        self.fMaxExposureTimePerDataCollection = self.xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue()
                    if self.xsDataDiffractionPlan.getAnomalousData():
                        self.bAnomalousData = self.xsDataDiffractionPlan.getAnomalousData().getValue()
                    if self.xsDataDiffractionPlan.getStrategyOption():
                        self.strStrategyOption = self.xsDataDiffractionPlan.getStrategyOption().getValue()
                    if self.xsDataDiffractionPlan.getKappaStrategyOption():
                        self.listKappaStrategyOption = self.xsDataDiffractionPlan.getKappaStrategyOption()
                    if self.xsDataDiffractionPlan.getComplexity():
                        self.strComplexity = self.xsDataDiffractionPlan.getComplexity().getValue()
                    if self.fMinOscillationWidth == None:
                        if self.xsDataDiffractionPlan.getGoniostatMinOscillationWidth():
                            self.fMinOscillationWidth = self.xsDataDiffractionPlan.getGoniostatMinOscillationWidth().getValue()
                    if self.fMaxOscillationSpeed == None:
                        if self.xsDataDiffractionPlan.getGoniostatMaxOscillationSpeed():
                            self.fMaxOscillationSpeed = self.xsDataDiffractionPlan.getGoniostatMaxOscillationSpeed().getValue()


            if self.hasDataInput("sample"):
                self.xsDataSample = self.getDataInput("sample")[0]

            if self.hasDataInput("imagePaths"):
                for strImagePath in self.getDataInput("imagePaths"):
                    self.listImagePaths.append(strImagePath)

            if self.hasDataInput("flux"):
                self.fFlux = self.getDataInput("flux")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getFlux() != None:
                        self.fFlux = self.xsDataExperimentalCodition.getBeam().getFlux().getValue()

            if self.hasDataInput("minExposureTimePerImage"):
                self.fMinExposureTimePerImage = self.getDataInput("minExposureTimePerImage")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getMinExposureTimePerImage() != None:
                        self.fMinExposureTimePerImage = self.xsDataExperimentalCodition.getBeam().getMinExposureTimePerImage().getValue()
            if self.fMinExposureTimePerImage == None and self.hasDataInput("diffractionPlan"):
                if self.getDataInput("diffractionPlan")[0].getMinExposureTimePerImage() != None:
                    self.fMinExposureTimePerImage = self.getDataInput("diffractionPlan")[0].getMinExposureTimePerImage().getValue()

            if self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getSize() != None:
                        self.fBeamSizeX = self.xsDataExperimentalCodition.getBeam().getSize().getX().getValue()
                        self.fBeamSizeY = self.xsDataExperimentalCodition.getBeam().getSize().getY().getValue()

            if self.hasDataInput("beamSize"):
                self.fBeamSizeX = self.getDataInput("beamSize")[0].getValue()
                self.fBeamSizeY = self.getDataInput("beamSize")[0].getValue()

            if self.hasDataInput("beamSizeX"):
                self.fBeamSizeX = self.getDataInput("beamSizeX")[0].getValue()

            if self.hasDataInput("beamSizeY"):
                self.fBeamSizeY = self.getDataInput("beamSizeY")[0].getValue()

            if self.hasDataInput("templateMode"):
                self.bTemplateMode = self.getDataInput("templateMode")[0].getValue()

            if (self.hasDataInput("beamPosX")):
                self.fBeamPosX = self.getDataInput("beamPosX")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getDetector() != None:
                    if self.xsDataExperimentalCodition.getDetector().getBeamPositionX() != None:
                        self.fBeamPosX = self.xsDataExperimentalCodition.getDetector().getBeamPositionX().getValue()

            if (self.hasDataInput("beamPosY")):
                self.fBeamPosY = self.getDataInput("beamPosY")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getDetector() != None:
                    if self.xsDataExperimentalCodition.getDetector().getBeamPositionY() != None:
                        self.fBeamPosY = self.xsDataExperimentalCodition.getDetector().getBeamPositionY().getValue()

            if (self.hasDataInput("wavelength")):
                self.fWavelength = self.getDataInput("wavelength")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getWavelength() != None:
                        self.fWavelength = self.xsDataExperimentalCodition.getBeam().getWavelength().getValue()

            if (self.hasDataInput("transmission")):
                self.fTransmission = self.getDataInput("transmission")[0].getValue()
            elif self.xsDataExperimentalCodition != None:
                if self.xsDataExperimentalCodition.getBeam() != None:
                    if self.xsDataExperimentalCodition.getBeam().getTransmission() != None:
                        self.fTransmission = self.xsDataExperimentalCodition.getBeam().getTransmission().getValue()

            if self.hasDataInput("generatedTemplateFile"):
                self.strGeneratedTemplateFile = self.getDataInput("generatedTemplateFile")[0].getValue()

            if self.hasDataInput("resultsFilePath"):
                self.strResultsFilePath = self.getDataInput("resultsFilePath")[0].getValue()

            if self.hasDataInput("dataCollectionId"):
                self.iDataCollectionId = self.getDataInput("dataCollectionId")[0].getValue()

            if self.hasDataInput("shortComments"):
                self.strShortComments = self.getDataInput("shortComments")[0].getValue()

            if self.hasDataInput("comments"):
                self.strComments = self.getDataInput("comments")[0].getValue()

            if self.hasDataInput("inputCharacterisation"):
                self.xsDataInputCharacterisation = self.getDataInput("inputCharacterisation")[0]
                
            if (self.hasDataInput("mxv2DataCollection")):
                self.xsDataCollectionMXv2 = self.getDataInput("mxv2DataCollection")[0]

        # Check if XML data is given as input :
        if (self.xsDataInputCharacterisation is None):
            self.edPluginControlSubWedgeAssemble = self.loadPlugin(self.strEDPluginControlSubWedgeAssembleName, "SubWedgeAssemble")

        if self.mxv2DataCollection_Reference is None:
            self.strEDPluginControlCharacterisationName = self.strEDPluginControlCharForReorientationName
        else:
            self.strEDPluginControlCharacterisationName = self.strEDPluginControlCharAtNewOrientationName
        self.screen("Using plugin %s" % self.strEDPluginControlCharacterisationName)
        self.edPluginControlCharacterisationv2 = self.loadPlugin(self.strEDPluginControlCharacterisationName, "Characterisation")

        if (self.strEDPluginControlISPyBName is not None):
            self.edPluginControlISPyB = self.loadPlugin(self.strEDPluginControlISPyBName, "ISPyB")

        self.xsDataInputCharacterisationv2_0 = XSDataMXv2.XSDataInputCharacterisationv2_0()
        # Check if we should create simple HTML and store to ISPyB
        self.strCreateSimpleHTMLPageForISPyB = self.getStringConfigurationParameterValue("createSimpleHTMLPageForISPyB")
        if self.strCreateSimpleHTMLPageForISPyB == "True":
            self.edPluginExecSimpleHTML = self.loadPlugin(self.strPluginExecSimpleHTMLName, "SimpleHTML")



    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.process...")

        if (self.edPluginControlSubWedgeAssemble is not None):
            if(self.bTemplateMode == True):
                self.edPluginControlSubWedgeAssemble.connectSUCCESS(self.generateTemplateFile)
            else:
                self.edPluginControlSubWedgeAssemble.connectSUCCESS(self.doSubWedgeAssembleSUCCESS)
            self.edPluginControlSubWedgeAssemble.connectFAILURE(self.doSubWedgeAssembleFAILURE)

        if(self.edPluginControlCharacterisationv2 is not None):
            self.edPluginControlCharacterisationv2.connectSUCCESS(self.doSuccessActionCharacterisation)
            self.edPluginControlCharacterisationv2.connectFAILURE(self.doFailureActionCharacterisation)

        if (self.edPluginControlISPyB is not None):
            self.edPluginControlISPyB.connectSUCCESS(self.doSuccessActionISPyB)
            self.edPluginControlISPyB.connectFAILURE(self.doFailureActionISPyB)

        if (self.mxv1InputCharacterisation is None):
            self.createInputCharacterisationFromImageHeaders(self.edPluginControlSubWedgeAssemble)
        else:
            self.runCharacterisationPlugin(self.edPluginControlCharacterisationv2)


    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.finallyProcess...")

        if (not self.edPluginControlCharacterisationv2 is None):
            if (self.edPluginControlCharacterisationv2.hasDataOutput()):
                self.setDataOutput(self.edPluginControlCharacterisationv2.getDataOutput().getMxv1ResultCharacterisation(), "characterisation")
                self.setDataOutput(self.edPluginControlCharacterisationv2.getDataOutput(), "resultCharacterisationv2_0")
        if (not self.edPluginControlISPyB is None):
            if (self.edPluginControlISPyB.hasDataOutput()):
                self.setDataOutput(self.edPluginControlISPyB.getDataOutput(), "ISPyB")
        xsDataResultInterface = XSDataResultInterfacev2_2()
        if self.edPluginControlCharacterisationv2:
            if self.edPluginControlCharacterisationv2.getDataOutput():
                xsDataResultInterface.setMxv1ResultCharacterisation(self.edPluginControlCharacterisationv2.getDataOutput().getMxv1ResultCharacterisation())
                xsDataResultInterface.setMxv1ResultCharacterisation_Reference(self.edPluginControlCharacterisationv2.getDataOutput().getMxv1ResultCharacterisation_Reference())
                xsDataResultInterface.setMxv2DataCollection(self.mxv2DataCollection)
                if self.mxv2DataCollection_Reference:
                    xsDataResultInterface.setMxv2DataCollection_Reference(self.mxv2DataCollection_Reference)
                else:
                    xsDataResultInterface.setMxv2DataCollection_Reference(self.mxv2DataCollection)
                xsDataResultInterface.setSuggestedStrategy(self.edPluginControlCharacterisationv2.getDataOutput().getSuggestedStrategy())
                xsDataResultInterface.setPossibleOrientations(self.edPluginControlCharacterisationv2.getDataOutput().getPossibleOrientations())
        if self.edPluginControlISPyB:
            xsDataResultInterface.setResultControlISPyB(self.edPluginControlISPyB.getDataOutput())
        self.setDataOutput(xsDataResultInterface)


    def createInputCharacterisationFromImageHeaders(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.createInputCharacterisationFromImageHeaders")
        xsDataInputSubWedgeAssemble = XSDataMXv1.XSDataInputSubWedgeAssemble()
        for xsDataStringImagePath in self.listImagePaths:
            xsDataFile = XSDataFile()
            xsDataFile.setPath(xsDataStringImagePath)
            xsDataInputSubWedgeAssemble.addFile(xsDataFile)
        _edPlugin.setDataInput(xsDataInputSubWedgeAssemble)
        _edPlugin.executeSynchronous()


    def runCharacterisationPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.runCharacterisationPlugin")
        if self.xsDataInputCharacterisationv2_0.getMxv1InputCharacterisation() is None:
            self.xsDataInputCharacterisationv2_0.setMxv1InputCharacterisation(self.mxv1InputCharacterisation)
        self.xsDataInputCharacterisationv2_0.setMxv1ResultCharacterisation_Reference(self.mxv1ResultCharacterisation_Reference)
        if self.mxv2DataCollection is None:
            if (self.fKappa is not None) and (self.fOmega is not None) and (self.fPhi is not None):
                self.mxv2DataCollection = self.generateMXv2DataCollection()
            else:
                self.screen("No kappa strategy calculated due to one or several missing kappa angles (phi, kappa and/or omega)")
        self.xsDataInputCharacterisationv2_0.setMxv2DataCollection(self.mxv2DataCollection)
        if self.mxv2DataCollection_Reference:
            self.xsDataInputCharacterisationv2_0.setMxv2DataCollection_Reference(self.mxv2DataCollection_Reference)
        else:
            self.xsDataInputCharacterisationv2_0.setMxv2DataCollection_Reference(self.mxv2DataCollection)
        self.xsDataInputCharacterisationv2_0.setPossibleOrientations(self.mxv2PossibleOrientations)

        self.edPluginControlCharacterisationv2.setDataInput(self.xsDataInputCharacterisationv2_0)
        self.edPluginControlCharacterisationv2.executeSynchronous()


    def storeResultsInISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.storeResultsInISPyB")
        if (self.edPluginControlISPyB is not None):
            # Execute the ISPyB control plugin
            xsDataInputControlISPyB = XSDataMXv1.XSDataInputControlISPyB()
            xsDataInputControlISPyB.setCharacterisationResult(self.edPluginControlCharacterisationv2.getDataOutput().getMxv1ResultCharacterisation())
            if (not self.iDataCollectionId is None):
                xsDataInputControlISPyB.setDataCollectionId(XSDataInteger(self.iDataCollectionId))
            if (not self.strShortComments is None):
                self.edPluginControlISPyB.setDataInput(XSDataString(self.strShortComments), "shortComments")
            if (not self.strComments is None):
                self.edPluginControlISPyB.setDataInput(XSDataString(self.strComments), "comments")
            if (not self.strStatusMessage is None):
                self.edPluginControlISPyB.setDataInput(XSDataString(self.strStatusMessage), "statusMessage")
            self.edPluginControlISPyB.setDataInput(xsDataInputControlISPyB)
            self.edPluginControlISPyB.executeSynchronous()


    def createMXv1InputCharacterisationFromSubWedges(self):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.createMXv1InputCharacterisationFromSubWedges")
        xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput()
        xsDataInputCharacterisation = XSDataMXv1.XSDataInputCharacterisation()
        xsDataCollection = XSDataMXv1.XSDataCollection()
        # Default exposure time (for the moment, this value should be
        # possible to read from the command line)
        if self.xsDataDiffractionPlan is None:
            self.xsDataDiffractionPlan = XSDataMXv1.XSDataDiffractionPlan()
        if (not xsDataResultSubWedgeAssemble is None):
            pyListSubWedge = xsDataResultSubWedgeAssemble.getSubWedge()
            xsDataCollection.setSubWedge(pyListSubWedge)
            for xsDataSubWedge in pyListSubWedge:
                if (self.strComplexity is not None):
                    self.xsDataDiffractionPlan.setComplexity(XSDataString(self.strComplexity))
                if (self.fFlux is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(XSDataFlux(self.fFlux))
                if (self.fBeamSizeX is not None) and (self.fBeamSizeY is not None):
                    xsDataSize = XSDataSize()
                    xsDataSize.setX(XSDataLength(self.fBeamSizeX))
                    xsDataSize.setY(XSDataLength(self.fBeamSizeY))
                    xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataSize)
                if (self.fBeamPosX is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionX(XSDataLength(self.fBeamPosX))
                if (self.fBeamPosY is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionY(XSDataLength(self.fBeamPosY))
                if (self.fMinExposureTimePerImage is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(XSDataTime(self.fMinExposureTimePerImage))
                if (self.fTransmission is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setTransmission(XSDataDouble(self.fTransmission))
                if (self.fWavelength is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setWavelength(XSDataWavelength(self.fWavelength))
                if self.fMinOscillationWidth != None:
                    xsDataSubWedge.getExperimentalCondition().getGoniostat().setMinOscillationWidth(XSDataAngle(self.fMinOscillationWidth))
                if self.fMaxOscillationSpeed != None:
                    xsDataSubWedge.getExperimentalCondition().getGoniostat().setMaxOscillationSpeed(XSDataAngularSpeed(self.fMaxOscillationSpeed))
        if (self.strForcedSpaceGroup is not None):
            self.xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString(self.strForcedSpaceGroup))
        self.xsDataDiffractionPlan.setAnomalousData(XSDataBoolean(self.bAnomalousData))
        self.xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(self.fMaxExposureTimePerDataCollection))
        if (self.strStrategyOption is not None):
            self.xsDataDiffractionPlan.setStrategyOption(XSDataString(self.strStrategyOption))
        if (self.listKappaStrategyOption is not None):
            self.xsDataDiffractionPlan.setKappaStrategyOption(self.listKappaStrategyOption)
        xsDataCollection.setDiffractionPlan(self.xsDataDiffractionPlan)
        if self.xsDataSample is not None:
            xsDataCollection.setSample(XSDataMXv1.XSDataSampleCrystalMM.parseString(self.xsDataSample.marshal()))
        xsDataInputCharacterisation.setDataCollection(xsDataCollection)
        self.xsDataInputCharacterisationv2_0.setMxv1InputCharacterisation(xsDataInputCharacterisation)


    def generateTemplateFile(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.generateTemplateFile")
        self.createMXv1InputCharacterisationFromSubWedges()
        if(self.strGeneratedTemplateFile is None):
            EDVerbose.screen("No argument for command line --generateTemplate key word found!")
        elif (self.xsDataInputCharacterisation is None):
            EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.strGeneratedTemplateFile)
        else:
            EDVerbose.screen("Generating xml template input file for edna: " + self.strGeneratedTemplateFile + "...")
            self.xsDataInputCharacterisation.exportToFile(self.strGeneratedTemplateFile)
        if self.strGeneratedTemplateFileMXv2 is not None:
            if(self.strGeneratedTemplateFileMXv2 is None):
                EDVerbose.screen("No argument for command line --generateTemplateMXv2 key word found!")
            elif (self.xsDataInputCharacterisation is None):
                EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.__strGeneratedTemplateFileMXv2)
            else:
                EDVerbose.screen("Generating MXv2 xml template input file: " + self.strGeneratedTemplateFileMXv2 + "...")
                xsDC_v2 = self.generateMXv2DataCollection()
                xsDC_v2.outputFile(self.strGeneratedTemplateFileMXv2)
                
                
    def generateMXv2DataCollection(self):
        # TEMP: generates the file to be read in
        ##PARAMS
        calibDate = '2009-12-10'
        omegaR = (0, 0, 1)
        kappaR = (0, 0.707106781187, 0.707106781187)
        phiR = (0, 0, 1)
        beamD = (1, 0, 0)
        polarisationP = (0, 1, 0)
        exposuretime = 1.0
        imagewidth = 1.0
        numberimages = 1
        wavelength = 1.0
        OmegaV = self.fOmega
        KappaV = self.fKappa
        PhiV = self.fPhi
        imgFnames = []
        for xsDataImage in self.listImagePaths:
            imgFnames.append(xsDataImage.getValue())
        xsDataCollectionv2 = self.generateDataCollectionDescriptorForSubWedge(calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames)
        return xsDataCollectionv2
    

    def doSubWedgeAssembleSUCCESS(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doSubWedgeAssembleSUCCESS")
        self.createMXv1InputCharacterisationFromSubWedges()
        self.runCharacterisationPlugin(_edPlugin)

    def doSubWedgeAssembleFAILURE(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doSubWedgeAssembleFAILURE")
        EDVerbose.screen("Execution of " + self.strEDPluginControlSubWedgeAssembleName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.setFailure()

    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doFailureActionCharacterisation")
        self.retrieveFailureMessages(self.edPluginControlCharacterisationv2, "EDPluginControlInterfacev2_2.doSuccessActionISPyB")
        if _edPlugin.hasDataOutput("statusMessage"):
            self.strStatusMessage = _edPlugin.getDataOutput("statusMessage")[0].getValue()
        self.generateExecutiveSummary(self)
        self.setFailure()

    def doSuccessActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doSuccessActionCharacterisation")
        # Store the results if requested
        if (self.strResultsFilePath is not None):
            xsDataCharacterisationResultv2_0 = _edPlugin.getDataOutput()
            if (xsDataCharacterisationResultv2_0 is not None):
                xsDataCharacterisationResultv2_0.exportToFile(self.strResultsFilePath)
        if _edPlugin.hasDataOutput("statusMessage"):
            self.strStatusMessage = _edPlugin.getDataOutput("statusMessage")[0].getValue()
        self.storeResultsInISPyB(_edPlugin)

    def doSuccessActionISPyB(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.edPluginControlISPyB, "EDPluginControlInterfacev2_2.doSuccessActionISPyB")
        if self.strCreateSimpleHTMLPageForISPyB == "True":
            # Copy the files to PyArch
            xsDataResultCharacterisation = self.edPluginControlCharacterisationv2.getDataOutput().getMxv1ResultCharacterisation()
            strPathToDNAFileDirectory = self.createDNAFileDirectoryPath(xsDataResultCharacterisation)
            if self.createDNAFileDirectory(strPathToDNAFileDirectory):
                self.copyFilesToPyArch(xsDataResultCharacterisation, strPathToDNAFileDirectory)
            strPyArchPathToDNAFileDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(strPathToDNAFileDirectory)
            if self.createDNAFileDirectory(strPyArchPathToDNAFileDirectory):
                self.copyFilesToPyArch(xsDataResultCharacterisation, strPyArchPathToDNAFileDirectory)
            # Execute plugin which creates a simple HTML page
            xsDataInputSimpleHTMLPage = XSDataInputSimpleHTMLPage()
            xsDataInputSimpleHTMLPage.setCharacterisationResult(xsDataResultCharacterisation)
            self.edPluginExecSimpleHTML.setDataInput(xsDataInputSimpleHTMLPage)
            self.executePluginSynchronous(self.edPluginExecSimpleHTML)
        

    def doFailureActionISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.doFailureActionISpyB...")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def generateExecutiveSummary(self, _edPlugin=None):
        """
        Prints the executive summary from the plugin
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_2.generateExecutiveSummary")
        if (self.edPluginControlSubWedgeAssemble is not None):
            if self.edPluginControlSubWedgeAssemble.getListExecutiveSummaryLines() != []:
                self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlSubWedgeAssembleName)
                self.appendExecutiveSummary(self.edPluginControlSubWedgeAssemble)
        if (self.edPluginControlCharacterisationv2 is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlCharacterisationName)
            self.appendExecutiveSummary(self.edPluginControlCharacterisationv2)
        if (self.edPluginControlISPyB is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlISPyBName)
            self.appendExecutiveSummary(self.edPluginControlISPyB)
        self.verboseScreenExecutiveSummary()


    def generateDataCollectionDescriptorForSubWedge(self, calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames):
        ##CONTAINER
        xsDC_v2 = XSDataMXv2.XSDataCollection()

        ##GonioCalib
        calib = XSDataMXv2.XSCalibration()
        cdate = XSDataMXv2.XSDataDate()
        cdate.setValue(calibDate)
        calib.setDate(cdate)
        #OmegaCalib
        omegacal = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(omegaR[0])
        zdir.setV2(omegaR[1])
        zdir.setV3(omegaR[2])
        omegacal.setZerodirection(zdir)
        omegacal.setXSCalibration(calib)
        #KappaCalib
        kappacal = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(kappaR[0])
        zdir.setV2(kappaR[1])
        zdir.setV3(kappaR[2])
        kappacal.setZerodirection(zdir)
        kappacal.setXSCalibration(calib)
        #PhiCalib
        phical = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(phiR[0])
        zdir.setV2(phiR[1])
        zdir.setV3(phiR[2])
        phical.setZerodirection(zdir)
        phical.setXSCalibration(calib)

        ##goni
        actgonio = XSDataMXv2.XSRotationalGoniostat()
        #omega
        omega = XSDataMXv2.XSGoniostatBaseAxis()
        omega.setName(XSDataMXv2.XSDataString('Omega'))
        omega.setIsscannable(XSDataMXv2.XSDataBoolean(1))
        omega.addXSCalibratedDisplacementAxis(omegacal)
        actgonio.setXSGoniostatBaseAxis(omega)
        #kappa
        kappa = XSDataMXv2.XSGoniostatRotatableAxis()
        kappa.setName(XSDataMXv2.XSDataString('Kappa'))
        kappa.setIsscannable(XSDataMXv2.XSDataBoolean(0))
        kappa.addXSCalibratedDisplacementAxis(kappacal)
        actgonio.addXSGoniostatRotatableAxis(kappa)
        #phi
        phi = XSDataMXv2.XSGoniostatRotatableAxis()
        phi.setName(XSDataMXv2.XSDataString('Phi'))
        phi.setIsscannable(XSDataMXv2.XSDataBoolean(0))
        phi.addXSCalibratedDisplacementAxis(phical)
        actgonio.addXSGoniostatRotatableAxis(phi)

        ##beam
        beam = XSDataMXv2.XSBeam()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(polarisationP[0])
        zdir.setV2(polarisationP[1])
        zdir.setV3(polarisationP[2])
        beam.setPolarisatation(zdir)
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(beamD[0])
        zdir.setV2(beamD[1])
        zdir.setV3(beamD[2])
        beam.setDirection(zdir)

        ##detector
        detector = XSDataMXv2.XSDetector()
        detector.setName(XSDataMXv2.XSDataString('detector'))
        ###detector.set

        ##SUBWEDGE
        sw = XSDataMXv2.XSSubWedge()
        # template
        sw.setImagefilenametemplate(XSDataMXv2.XSDataString(EDUtilsImage.getTemplate(imgFnames[0], "#")))
        # images
        for imgFname in imgFnames:
            img = XSDataMXv2.XSDiffractionImages()
            img.setFilename(XSDataMXv2.XSDataString(imgFname))
            sw.addXSDiffractionImages(img)
        #RotationExposure
        rotexp = XSDataMXv2.XSRotationExposure()
        rotexp.setExposuretime(XSDataMXv2.XSDataTime(exposuretime))
        rotexp.setImagewidth(XSDataMXv2.XSDataAngle(imagewidth))
        rotexp.setNumberimages(XSDataMXv2.XSDataInteger(numberimages))
        rotexp.setXSGoniostatAxis(omega)
        sw.setXSRotationExposure(rotexp)
        #Beamsetting
        beams = XSDataMXv2.XSBeamSetting()
        w = XSDataMXv2.XSDataWavelength()
        w.setValue(wavelength)
        beams.setWavelength(w)
        beams.setXSBeam(beam)
        sw.setXSBeamSetting(beams)
        #RotationalGonioSetting
        rotgset = XSDataMXv2.XSRotationalGoniostatSetting()
        rotgset.setXSRotationalGoniostat(actgonio)
        oang = XSDataMXv2.XSDataAngle()
        oang.setValue(OmegaV)
        rotgset.setBaseaxissetting(oang)
        kang = XSDataMXv2.XSDataAngle()
        kang.setValue(KappaV)
        rotgset.addAxissetting(kang)
        pang = XSDataMXv2.XSDataAngle()
        pang.setValue(PhiV)
        rotgset.addAxissetting(pang)
        sw.setXSRotationalGoniostatSetting(rotgset)
        #DetectorSetting TODOTODO
        detset = XSDataMXv2.XSDetectorSetting()
        #axissetting=(XSDataMXv2.XSDataAngle().setValue(KappaV),XSDataMXv2.XSDataAngle().setValue(PhiV))
        #detset.setAxissetting(axissetting)

        xsDC_v2.addXSSubWedge(sw)

        return xsDC_v2


        #xsDataResultSubWedgeAssemble = self.__edPluginControlSubWedgeAssemble.getDataOutput()
        #imgFname = xsDataResultSubWedgeAssemble.getSubWedge()[0].getImage()[0].getPath().getValue()
        #self.xsDC_v2.outputFile(os.path.dirname(imgFname) + '/edna_' + EDUtilsImage.getTemplate(imgFname, "#") + '_auto')


#    def createInputCharacterisationFromSubWedges(self):
#        #selecting the old result from the new complex outputList
#        #xsDataResultSubWedgeAssembleList = self.edPluginControlSubWedgeAssemble.getDataOutput()
#        #xsDataResultSubWedgeAssemble = xsDataResultSubWedgeAssembleList[0]
#
#        xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput("mxv1Assemble")[0]
#
#        self.xsDataInputCharacterisationOLD = XSDataInputCharacterisation()
#        xsDataCollection = XSDataCollection()
#        # Default exposure time (for the moment, this value should be
#        # possible to read from the command line)
#        xsDataDiffractionPlan = XSDataDiffractionPlan()
#        listSubWedge = xsDataResultSubWedgeAssemble.getSubWedge()
#        for xsDataSubWedge in listSubWedge:
#            if (self.strComplexity is not None):
#                xsDataDiffractionPlan.setComplexity(XSDataString(self.strComplexity))
#            if (self.fFlux is not None):
#                xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(XSDataFloat(self.fFlux))
#            if (self.fBeamSize is not None):
#                xsDataSize = XSDataSize()
#                xsDataSize.setX(XSDataLength(self.fBeamSize))
#                xsDataSize.setY(XSDataLength(self.fBeamSize))
#                xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataSize)
#            if (self.fMinExposureTimePerImage is not None):
#                xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(XSDataFloat(self.fMinExposureTimePerImage))
#        if (self.strForcedSpaceGroup is not None):
#            xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString(self.strForcedSpaceGroup))
#        xsDataDiffractionPlan.setAnomalousData(XSDataBoolean(self.bAnomalousData))
#        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(self.fMaxExposureTimePerDataCollection))
#        xsDataCollection.setSubWedge(listSubWedge)
#        xsDataCollection.setDiffractionPlan(xsDataDiffractionPlan)
#        self.xsDataInputCharacterisationOLD.setDataCollection(xsDataCollection)
#
#        self.xsDataInputCharacterisation = []
#        self.xsDataInputCharacterisation.add(self.xsDataInputCharacterisationOLD)
#
#        # TODO: complete the new multi-input Characteristaion
#        # by the second output element (DataCollection_mxv2) of SubWedge
#        self.xsDataInputCharacterisation.add(self.edPluginControlSubWedgeAssemble.getDataOutput("mxv2DataCollection")[0])


    def createDNAFileDirectoryPath(self, _xsDataResultCharacterisation):
        """
        This method creates a "DNA" style directory path, i.e. in the same directory were the 
        images are located a new directory is created with the following convention:
        
          dnafiles_prefix_runNumber
        
        The path to this directory is returned if the directory was successfully created.
        """
        # First extract all reference image directory paths and names
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        listImageDirectoryPath = []
        listImagePrefix = []
        for xsDataSubWedge in xsDataCollection.getSubWedge():
            for xsDataImage in xsDataSubWedge.getImage():
                strImagePath = xsDataImage.getPath().getValue()
                listImageDirectoryPath.append(os.path.dirname(strImagePath))
                listImagePrefix.append(EDUtilsImage.getPrefix(strImagePath))
        # TODO: Check that all paths and prefixes are the same
        strImageDirectory = listImageDirectoryPath[0]
        strPrefix = listImagePrefix[0]
        # Remove any "ref-" or "postref-" from the prefix in order to make it fully
        # compatitble with DNA standards:
        if (strPrefix is not None):
            if (strPrefix.startswith("ref-")):
                strPrefix = strPrefix[4:]
            elif (strPrefix.startswith("postref-")):
                strPrefix = strPrefix[8:]
        strDNAFileDirectoryPath = os.path.join(strImageDirectory, "%s_dnafiles" % strPrefix)
        return strDNAFileDirectoryPath
    
    def createDNAFileDirectory(self, _strDNAFileDirectoryPath):
        """
        Create a "DNA-files" directory - if possible.
        """
        bSuccess = False
        if (_strDNAFileDirectoryPath is not None):
            if (os.path.exists(_strDNAFileDirectoryPath)):
                self.warning("Removing existing DNA files directory: %s" % _strDNAFileDirectoryPath)
                if (os.access(_strDNAFileDirectoryPath, os.W_OK)):
                    shutil.rmtree(_strDNAFileDirectoryPath)
                else:
                    self.warning("Cannot remove existing DNA files directory!")
            if (_strDNAFileDirectoryPath is not None):
                # Check if directory one level up is writeable
                strDNAFileBaseDirectory = os.path.split(_strDNAFileDirectoryPath)[0]
                if (os.access(strDNAFileBaseDirectory, os.W_OK)):
                    self.DEBUG("Creating DNA files directory: %s" % _strDNAFileDirectoryPath)
                    os.mkdir(_strDNAFileDirectoryPath)
                    bSuccess = True
                else:
                    self.warning("Cannot create DNA files directory: %s" % _strDNAFileDirectoryPath)
        return bSuccess    
    
    def copyFilesToPyArch(self, _xsDataResultCharacterisation, _strPathToLogFileDirectory=None):
        """
        This method copies files from characterisation to pyarch
        """
        # Start with the prediction images
        xsDataIndexingResult = _xsDataResultCharacterisation.getIndexingResult()
        xsDataGeneratePredictionResult = xsDataIndexingResult.getPredictionResult()
        listXSDataImagePrediction = xsDataGeneratePredictionResult.getPredictionImage()
        for xsDataImagePrediction in listXSDataImagePrediction:
            strPredictionImagePath = xsDataImagePrediction.getPath().getValue()
            if (_strPathToLogFileDirectory is not None):
                strPredictionImageFileName = EDUtilsFile.getBaseName(strPredictionImagePath)
                strNewPredictionImagePath = os.path.join(_strPathToLogFileDirectory, strPredictionImageFileName)
                EDUtilsFile.copyFile(strPredictionImagePath, strNewPredictionImagePath)
        # Best log file
        strPathToBESTLogFile = None
        strPathToExecutiveSummary = None
        if _xsDataResultCharacterisation.getStrategyResult().getBestLogFile() != None:
            strPathToBESTLogFile = _xsDataResultCharacterisation.getStrategyResult().getBestLogFile().getPath().getValue()
        if strPathToBESTLogFile is not None:
            if (_strPathToLogFileDirectory is not None):
                strNewBestLogPath = os.path.join(_strPathToLogFileDirectory, "best.log")
                EDUtilsFile.copyFile(strPathToBESTLogFile, strNewBestLogPath)
        if (strPathToExecutiveSummary is not None):
            if (_strPathToLogFileDirectory is not None):
                strExecutiveSummaryFileName = EDUtilsFile.getBaseName(strPathToExecutiveSummary)
                strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, strExecutiveSummaryFileName)
                EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)
                # Copy also the executive summary file to "dna_log.txt"...
                strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, "dna_log.txt")
                EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)



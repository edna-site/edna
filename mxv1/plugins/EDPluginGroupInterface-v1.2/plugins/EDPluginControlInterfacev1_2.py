#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Marie-Francoise Incardona (incardon@esrf.fr)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Karl Levik"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDMessage          import EDMessage
from EDConfiguration    import EDConfiguration


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

from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataSampleCrystalMM
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataInputControlISPyB

from XSDataInterfacev1_2 import XSDataInputInterface
from XSDataInterfacev1_2 import XSDataResultInterface

class EDPluginControlInterfacev1_2(EDPluginControl):
    """
    This is the common class to all plugins managing user interfaces
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)

        self.setXSDataInputClass(XSDataInputInterface)

        self.setXSDataInputClass(XSDataExperimentalCondition, "experimentalCondition")
        self.setXSDataInputClass(XSDataDiffractionPlan, "diffractionPlan")
        self.setXSDataInputClass(XSDataSampleCrystalMM, "sample")
        self.setXSDataInputClass(XSDataString, "imagePaths")
        self.setXSDataInputClass(XSDataFloat, "flux")
        self.setXSDataInputClass(XSDataFloat, "minExposureTimePerImage")
        self.setXSDataInputClass(XSDataFloat, "beamSize")
        self.setXSDataInputClass(XSDataFloat, "beamSizeX")
        self.setXSDataInputClass(XSDataFloat, "beamSizeY")
        self.setXSDataInputClass(XSDataBoolean, "templateMode")
        self.setXSDataInputClass(XSDataString, "generatedTemplateFile")
        self.setXSDataInputClass(XSDataString, "resultsFilePath")
        self.setXSDataInputClass(XSDataFloat, "beamPosX")
        self.setXSDataInputClass(XSDataFloat, "beamPosY")
        self.setXSDataInputClass(XSDataDouble, "wavelength")
        self.setXSDataInputClass(XSDataDouble, "transmission")
        self.setXSDataInputClass(XSDataInteger, "dataCollectionId")
        self.setXSDataInputClass(XSDataString, "shortComments")
        self.setXSDataInputClass(XSDataString, "comments")
        self.setXSDataInputClass(XSDataInputCharacterisation, "inputCharacterisation")

        self.strEDPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev1_1"
        self.strEDPluginControlCharacterisationName = "EDPluginControlCharacterisationv1_3"
        self.strEDPluginControlISPyBName = "EDPluginControlISPyBv1_1"

        self.edPluginControlSubWedgeAssemble = None
        self.edPluginControlCharacterisation = None
        self.edPluginControlISPyB = None

        self.pyListImagePaths = None
        self.xsDataInputCharacterisation = None
        self.strComplexity = "none"

        self.listImagePaths = []
        self.fFlux = None
        self.fMaxExposureTimePerDataCollection = 10000 # s, default prototype value
        self.fMinExposureTimePerImage = None
        self.fBeamSizeX = None
        self.fBeamSizeY = None
        self.bTemplateMode = False
        self.strGeneratedTemplateFile = None
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
        self.iDataCollectionId = None
        self.strShortComments = None
        self.strComments = None
        self.strStatusMessage = None

        self.xsDataExperimentalCodition = None
        self.xsDataSample = None
        self.xsDataDiffractionPlan = None


    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.configure")
        if (self.getControlledPluginName("subWedgeAssemblePlugin") is not None):
            self.strEDPluginControlSubWedgeAssembleName = self.getControlledPluginName("subWedgeAssemblePlugin")
        if (self.getControlledPluginName("characterisationPlugin") is not None):
            self.strEDPluginControlCharacterisationName = self.getControlledPluginName("characterisationPlugin")
        if (self.getControlledPluginName("ispybPlugin") is not None):
            self.strEDPluginControlISPyBName = self.getControlledPluginName("ispybPlugin")

        bUseISPyBPlugin = self.config.get("useISPyBPlugin")
        if not bUseISPyBPlugin:
            self.DEBUG("EDPluginControlInterfacev1_2 configured to not use ISPyB")
            self.strEDPluginControlISPyBName = None


    def preProcess(self, _edPlugin=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.preProcess...")

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
                    self.xsDataDiffractionPlan = XSDataDiffractionPlan()
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

        # Check if XML data is given as input :
        if (self.xsDataInputCharacterisation is None):
            self.edPluginControlSubWedgeAssemble = self.loadPlugin(self.strEDPluginControlSubWedgeAssembleName, "SubWedgeAssemble")

        self.edPluginControlCharacterisation = self.loadPlugin(self.strEDPluginControlCharacterisationName, "Characterisation")

        if (self.strEDPluginControlISPyBName is not None):
            self.edPluginControlISPyB = self.loadPlugin(self.strEDPluginControlISPyBName, "ISPyB")


    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.process...")

        if (self.edPluginControlSubWedgeAssemble is not None):
            if(self.bTemplateMode == True):
                self.edPluginControlSubWedgeAssemble.connectSUCCESS(self.generateTemplateFile)
            else:
                self.edPluginControlSubWedgeAssemble.connectSUCCESS(self.doSubWedgeAssembleSUCCESS)
            self.edPluginControlSubWedgeAssemble.connectFAILURE(self.doSubWedgeAssembleFAILURE)

        if(self.edPluginControlCharacterisation is not None):
            self.edPluginControlCharacterisation.connectSUCCESS(self.doSuccessActionCharacterisation)
            self.edPluginControlCharacterisation.connectFAILURE(self.doFailureActionCharacterisation)

        if (self.edPluginControlISPyB is not None):
            self.edPluginControlISPyB.connectSUCCESS(self.doSuccessActionISPyB)
            self.edPluginControlISPyB.connectFAILURE(self.doFailureActionISPyB)

        if (self.xsDataInputCharacterisation is None):
            self.createInputCharacterisationFromImageHeaders(self.edPluginControlSubWedgeAssemble)
        else:
            self.runCharacterisationPlugin(self.edPluginControlCharacterisation)


    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.finallyProcess...")

        if (not self.edPluginControlCharacterisation is None):
            if (self.edPluginControlCharacterisation.hasDataOutput()):
                self.setDataOutput(self.edPluginControlCharacterisation.getDataOutput(), "characterisation")
        if (not self.edPluginControlISPyB is None):
            if (self.edPluginControlISPyB.hasDataOutput()):
                self.setDataOutput(self.edPluginControlISPyB.getDataOutput(), "ISPyB")
        if self.hasDataInput():
            xsDataResultInterface = XSDataResultInterface()
            if self.edPluginControlCharacterisation:
                xsDataResultInterface.setResultCharacterisation(self.edPluginControlCharacterisation.getDataOutput())
            if self.edPluginControlISPyB:
                xsDataResultInterface.setResultControlISPyB(self.edPluginControlISPyB.getDataOutput())
            self.setDataOutput(xsDataResultInterface)


    def createInputCharacterisationFromImageHeaders(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.createInputCharacterisationFromImageHeaders")
        xsDataInputSubWedgeAssemble = XSDataInputSubWedgeAssemble()
        for xsDataStringImagePath in self.listImagePaths:
            xsDataFile = XSDataFile()
            xsDataFile.setPath(xsDataStringImagePath)
            xsDataInputSubWedgeAssemble.addFile(xsDataFile)
        _edPlugin.setDataInput(xsDataInputSubWedgeAssemble)
        _edPlugin.executeSynchronous()


    def runCharacterisationPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.runCharacterisationPlugin")
        self.edPluginControlCharacterisation.setDataInput(self.xsDataInputCharacterisation)
        self.edPluginControlCharacterisation.executeSynchronous()


    def storeResultsInISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.storeResultsInISPyB")
        if (self.edPluginControlISPyB is not None):
            # Execute the ISPyB control plugin
            xsDataInputControlISPyB = XSDataInputControlISPyB()
            xsDataInputControlISPyB.setCharacterisationResult(self.edPluginControlCharacterisation.getDataOutput())
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


    def createInputCharacterisationFromSubWedges(self):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.createInputCharacterisationFromSubWedges")
        xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput()
        self.xsDataInputCharacterisation = XSDataInputCharacterisation()
        xsDataCollection = XSDataCollection()
        # Default exposure time (for the moment, this value should be
        # possible to read from the command line)
        if self.xsDataDiffractionPlan is None:
            self.xsDataDiffractionPlan = XSDataDiffractionPlan()
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
        xsDataCollection.setDiffractionPlan(self.xsDataDiffractionPlan)
        if self.xsDataSample is not None:
            xsDataCollection.setSample(XSDataSampleCrystalMM.parseString(self.xsDataSample.marshal()))
        self.xsDataInputCharacterisation.setDataCollection(xsDataCollection)


    def generateTemplateFile(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.generateTemplateFile")
        self.createInputCharacterisationFromSubWedges()
        if(self.strGeneratedTemplateFile is None):
            EDVerbose.screen("No argument for command line --generateTemplate key word found!")
        elif (self.xsDataInputCharacterisation is None):
            EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.strGeneratedTemplateFile)
        else:
            EDVerbose.screen("Generating xml template input file for edna: " + self.strGeneratedTemplateFile + "...")
            self.xsDataInputCharacterisation.exportToFile(self.strGeneratedTemplateFile)


    def doSubWedgeAssembleSUCCESS(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doSubWedgeAssembleSUCCESS")
        self.createInputCharacterisationFromSubWedges()
        self.runCharacterisationPlugin(_edPlugin)

    def doSubWedgeAssembleFAILURE(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doSubWedgeAssembleFAILURE")
        EDVerbose.screen("Execution of " + self.strEDPluginControlSubWedgeAssembleName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.setFailure()

    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doFailureActionCharacterisation")
        self.retrieveFailureMessages(self.edPluginControlCharacterisation, "EDPluginControlInterfacev1_2.doSuccessActionISPyB")
        if _edPlugin.hasDataOutput("statusMessage"):
            self.strStatusMessage = _edPlugin.getDataOutput("statusMessage")[0].getValue()
        self.generateExecutiveSummary(self)
        self.storeResultsInISPyB(_edPlugin)
        self.setFailure()

    def doSuccessActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doSuccessActionCharacterisation")
        # Store the results if requested
        if (self.strResultsFilePath is not None):
            xsDataCharacterisationResult = _edPlugin.getDataOutput()
            if (xsDataCharacterisationResult is not None):
                xsDataCharacterisationResult.exportToFile(self.strResultsFilePath)
        if _edPlugin.hasDataOutput("statusMessage"):
            self.strStatusMessage = _edPlugin.getDataOutput("statusMessage")[0].getValue()
        self.storeResultsInISPyB(_edPlugin)

    def doSuccessActionISPyB(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.edPluginControlISPyB, "EDPluginControlInterfacev1_2.doSuccessActionISPyB")

    def doFailureActionISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.doFailureActionISpyB...")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def generateExecutiveSummary(self, _edPlugin=None):
        """
        Prints the executive summary from the plugin
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev1_2.generateExecutiveSummary")
        if (self.edPluginControlSubWedgeAssemble is not None):
            if self.edPluginControlSubWedgeAssemble.getListExecutiveSummaryLines() != []:
                self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlSubWedgeAssembleName)
                self.appendExecutiveSummary(self.edPluginControlSubWedgeAssemble)
        if (self.edPluginControlCharacterisation is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlCharacterisationName)
            self.appendExecutiveSummary(self.edPluginControlCharacterisation)
        if (self.edPluginControlISPyB is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.strEDPluginControlISPyBName)
            self.appendExecutiveSummary(self.edPluginControlISPyB)
        self.verboseScreenExecutiveSummary()

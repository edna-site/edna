#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlInterfacev1_2.py 1949 2010-08-23 14:51:38Z svensson $"
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
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDUtilsImage       import EDUtilsImage

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataLength

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataInputControlISPyB

from XSDataMXv2 import XSDataCollection as XSDataCollection_v2
from XSDataMXv2 import XSSubWedge as XSSubWedge_v2
from XSDataMXv2 import XSDiffractionImages as XSDiffractionImages_v2
from XSDataMXv2 import XSRotationExposure as XSRotationExposure_v2
from XSDataMXv2 import XSBeamSetting as XSBeamSetting_v2
import XSDataMXv2


class EDPluginControlInterfacev2_0(EDPluginControl):
    """
    This plugin is an enhancement of EDPluginControlInterfacev1_2
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)

        self.setXSDataInputClass(XSDataDiffractionPlan, "diffractionPlan")
        self.setXSDataInputClass(XSDataString, "imagePaths")
        self.setXSDataInputClass(XSDataFloat, "flux")
        self.setXSDataInputClass(XSDataFloat, "minExposureTimePerImage")
        self.setXSDataInputClass(XSDataFloat, "beamSize")
        self.setXSDataInputClass(XSDataBoolean, "templateMode")
        self.setXSDataInputClass(XSDataString, "generatedTemplateFile")
        self.setXSDataInputClass(XSDataString, "generatedTemplateFileMXv2")
        self.setXSDataInputClass(XSDataString, "resultsFilePath")
        self.setXSDataInputClass(XSDataFloat, "beamPosX")
        self.setXSDataInputClass(XSDataFloat, "beamPosY")
        self.setXSDataInputClass(XSDataDouble, "transmission")
        self.setXSDataInputClass(XSDataInteger, "dataCollectionId")
        self.setXSDataInputClass(XSDataString, "shortComments")
        self.setXSDataInputClass(XSDataString, "comments")
        self.setXSDataInputClass(XSDataInputCharacterisation, "inputCharacterisation")
        self.setXSDataInputClass(XSDataMXv2.XSDataCollection, "mxv2DataCollection")

        self.__strEDPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev1_1"
        self.__strEDPluginControlCharacterisationName = "EDPluginControlCharForReorientationv2_0"
        self.__strEDPluginControlISPyBName = "EDPluginControlISPyBv1_1"

        self.__edPluginControlSubWedgeAssemble = None
        self.__edPluginControlCharacterisation = None
        self.__edPluginControlISPyB = None

        self.__pyListImagePaths = None
        self.__xsDataInputCharacterisation = None
        self.__xsDataCollectionMXv2 = None
        self.__strComplexity = "none"

        self.__listImagePaths = []
        self.__fFlux = None
        self.__fMaxExposureTimePerDataCollection = 10000 # s, default prototype value
        self.__fMinExposureTimePerImage = None
        self.__fBeamSize = None
        self.__bTemplateMode = False
        self.__strGeneratedTemplateFile = None
        self.__strGeneratedTemplateFileMXv2 = None
        self.__strResultsFilePath = None
        self.__strForcedSpaceGroup = None
        self.__bAnomalousData = False
        self.__fBeamPosX = None
        self.__fBeamPosY = None
        self.__fTransmission = None
        self.__strStrategyOption = None
        self.__iDataCollectionId = None
        self.__strShortComments = None
        self.__strComments = None


    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.configure")
        pluginConfiguration = self.getConfiguration()
        strUseISPyBPlugin = "false"

        if (pluginConfiguration is None):
            EDVerbose.DEBUG("No plugin configuration found for EDPluginControlInterfacev2_0.")
        else:
            if (self.getControlledPluginName("subWedgeAssemblePlugin") is not None):
                self.__strEDPluginControlSubWedgeAssembleName = self.getControlledPluginName("subWedgeAssemblePlugin")
            if (self.getControlledPluginName("characterisationPlugin") is not None):
                self.__strEDPluginControlCharacterisationName = self.getControlledPluginName("characterisationPlugin")
            if (self.getControlledPluginName("ispybPlugin") is not None):
                self.__strEDPluginControlISPyBName = self.getControlledPluginName("ispybPlugin")
            strUseISPyBPlugin = EDConfiguration.getStringParamValue(pluginConfiguration, "useISPyBPlugin")

        if (strUseISPyBPlugin.lower() != "true"):
            self.__strEDPluginControlISPyBName = None


    def preProcess(self, _edPlugin=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.preProcess...")

        self.__listImagePaths = []

        if (self.hasDataInput("diffractionPlan")):
            xsDataDiffractionPlan = XSDataDiffractionPlan()
            xsDataDiffractionPlans = self.getDataInput("diffractionPlan")
            if (not xsDataDiffractionPlans[0] is None):
                xsDataDiffractionPlan = xsDataDiffractionPlans[0]
                if (not xsDataDiffractionPlan.getForcedSpaceGroup() is None):
                    self.__strForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
                if (not xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is None):
                    self.__fMaxExposureTimePerDataCollection = xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue()
                if (not xsDataDiffractionPlan.getAnomalousData() is None):
                    self.__bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()
                if (not xsDataDiffractionPlan.getStrategyOption() is None):
                    self.__strStrategyOption = xsDataDiffractionPlan.getStrategyOption().getValue()
                if (not xsDataDiffractionPlan.getComplexity() is None):
                    self.__strComplexity = xsDataDiffractionPlan.getComplexity().getValue()

        if (self.hasDataInput("imagePaths")):
            for strImagePath in self.getDataInput("imagePaths"):
                self.__listImagePaths.append(strImagePath)
        if (self.hasDataInput("flux")):
            self.__fFlux = self.getDataInput("flux")[0].getValue()
        if (self.hasDataInput("minExposureTimePerImage")):
            self.__fMinExposureTimePerImage = self.getDataInput("minExposureTimePerImage")[0].getValue()
        if (self.hasDataInput("beamSize")):
            self.__fBeamSize = self.getDataInput("beamSize")[0].getValue()
        if (self.hasDataInput("templateMode")):
            self.__bTemplateMode = self.getDataInput("templateMode")[0].getValue()
        if (self.hasDataInput("generatedTemplateFile")):
            self.__strGeneratedTemplateFile = self.getDataInput("generatedTemplateFile")[0].getValue()
        if (self.hasDataInput("generatedTemplateFileMXv2")):
            self.__strGeneratedTemplateFileMXv2 = self.getDataInput("generatedTemplateFileMXv2")[0].getValue()
        if (self.hasDataInput("resultsFilePath")):
            self.__strResultsFilePath = self.getDataInput("resultsFilePath")[0].getValue()
        if (self.hasDataInput("beamPosX")):
            self.__fBeamPosX = self.getDataInput("beamPosX")[0].getValue()
        if (self.hasDataInput("beamPosY")):
            self.__fBeamPosY = self.getDataInput("beamPosY")[0].getValue()
        if (self.hasDataInput("transmission")):
            self.__fTransmission = self.getDataInput("transmission")[0].getValue()
        if (self.hasDataInput("dataCollectionId")):
            self.__iDataCollectionId = self.getDataInput("dataCollectionId")[0].getValue()
        if (self.hasDataInput("shortComments")):
            self.__strShortComments = self.getDataInput("shortComments")[0].getValue()
        if (self.hasDataInput("comments")):
            self.__strComments = self.getDataInput("comments")[0].getValue()
        if (self.hasDataInput("inputCharacterisation")):
            self.__xsDataInputCharacterisation = self.getDataInput("inputCharacterisation")[0]
        if (self.hasDataInput("mxv2DataCollection")):
            self.__xsDataCollectionMXv2 = self.getDataInput("mxv2DataCollection")[0]

        # Check if XML data is given as input :
        if (self.__xsDataInputCharacterisation is None):
            self.__edPluginControlSubWedgeAssemble = self.loadPlugin(self.__strEDPluginControlSubWedgeAssembleName, "SubWedgeAssemble")

        self.__edPluginControlCharacterisation = self.loadPlugin(self.__strEDPluginControlCharacterisationName, "Characterisation")

        if (self.__strEDPluginControlISPyBName is not None):
            self.__edPluginControlISPyB = self.loadPlugin(self.__strEDPluginControlISPyBName, "ISPyB")


    def process(self, _edPlugin=None):
        """
        """
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.process...")

        if (self.__edPluginControlSubWedgeAssemble is not None):
            if(self.__bTemplateMode == True):
                self.__edPluginControlSubWedgeAssemble.connectSUCCESS(self.generateTemplateFile)
            else:
                self.__edPluginControlSubWedgeAssemble.connectSUCCESS(self.doSubWedgeAssembleSUCCESS)
            self.__edPluginControlSubWedgeAssemble.connectFAILURE(self.doSubWedgeAssembleFAILURE)

        if(self.__edPluginControlCharacterisation is not None):
            self.__edPluginControlCharacterisation.connectSUCCESS(self.doSuccessActionCharacterisation)
            self.__edPluginControlCharacterisation.connectFAILURE(self.doFailureActionCharacterisation)

        if (self.__edPluginControlISPyB is not None):
            self.__edPluginControlISPyB.connectSUCCESS(self.doSuccessActionISPyB)
            self.__edPluginControlISPyB.connectFAILURE(self.doFailureActionISPyB)

        if (self.__xsDataInputCharacterisation is None):
            self.createInputCharacterisationFromImageHeaders(self.__edPluginControlSubWedgeAssemble)
        else:
            self.runCharacterisationPlugin(self.__edPluginControlCharacterisation)


    def postProcess(self, _edPlugin=None):
        """
        """
        EDPluginControl.postProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.postProcess...")

        if (not self.__edPluginControlCharacterisation is None):
            if (self.__edPluginControlCharacterisation.hasDataOutput()):
                self.setDataOutput(self.__edPluginControlCharacterisation.getDataOutput(), "resultCharacterisationv2_0")
        if (not self.__edPluginControlISPyB is None):
            if (self.__edPluginControlISPyB.hasDataOutput()):
                self.setDataOutput(self.__edPluginControlISPyB.getDataOutput(), "ISPyB")


    def createInputCharacterisationFromImageHeaders(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.createInputCharacterisationFromImageHeaders")
        xsDataInputSubWedgeAssemble = XSDataInputSubWedgeAssemble()
        for xsDataStringImagePath in self.__listImagePaths:
            xsDataFile = XSDataFile()
            xsDataFile.setPath(xsDataStringImagePath)
            xsDataInputSubWedgeAssemble.addFile(xsDataFile)
        _edPlugin.setDataInput(xsDataInputSubWedgeAssemble)
        _edPlugin.executeSynchronous()


    def runCharacterisationPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.runCharacterisationPlugin")
        self.__edPluginControlCharacterisation.setDataInput(self.__xsDataInputCharacterisation, "mxv1InputCharacterisation")
        if self.__xsDataCollectionMXv2 != None:
            self.__edPluginControlCharacterisation.setDataInput(self.__xsDataCollectionMXv2, "mxv2DataCollection")
        self.__edPluginControlCharacterisation.executeSynchronous()


    def storeResultsInISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.storeResultsInISPyB")
        if (self.__edPluginControlISPyB is not None):
            # Execute the ISPyB control plugin
            xsDataInputControlISPyB = XSDataInputControlISPyB()
            xsDataInputControlISPyB.setCharacterisationResult(self.__edPluginControlCharacterisation.getDataOutput())
            if (not self.__iDataCollectionId is None):
                xsDataInputControlISPyB.setDataCollectionId(XSDataInteger(self.__iDataCollectionId))
            if (not self.__strShortComments is None):
                self.__edPluginControlISPyB.setDataInput(XSDataString(self.__strShortComments), "shortComments")
            if (not self.__strComments is None):
                self.__edPluginControlISPyB.setDataInput(XSDataString(self.__strComments), "comments")
            self.__edPluginControlISPyB.setDataInput(xsDataInputControlISPyB)
            self.__edPluginControlISPyB.executeSynchronous()


    def createInputCharacterisationFromSubWedges(self):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.createInputCharacterisationFromSubWedges")
        xsDataResultSubWedgeAssemble = self.__edPluginControlSubWedgeAssemble.getDataOutput()
        self.__xsDataInputCharacterisation = XSDataInputCharacterisation()
        xsDataCollection = XSDataCollection()
        # Default exposure time (for the moment, this value should be
        # possible to read from the command line)
        xsDataDiffractionPlan = XSDataDiffractionPlan()
        if (not xsDataResultSubWedgeAssemble is None):
            pyListSubWedge = xsDataResultSubWedgeAssemble.getSubWedge()
            xsDataCollection.setSubWedge(pyListSubWedge)
            for xsDataSubWedge in pyListSubWedge:
                if (self.__strComplexity is not None):
                    xsDataDiffractionPlan.setComplexity(XSDataString(self.__strComplexity))
                if (self.__fFlux is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(XSDataFloat(self.__fFlux))
                if (self.__fBeamSize is not None):
                    xsDataSize = XSDataSize()
                    xsDataSize.setX(XSDataLength(self.__fBeamSize))
                    xsDataSize.setY(XSDataLength(self.__fBeamSize))
                    xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataSize)
                if (self.__fBeamPosX is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionX(XSDataLength(self.__fBeamPosX))
                if (self.__fBeamPosY is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionY(XSDataLength(self.__fBeamPosY))
                if (self.__fMinExposureTimePerImage is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(XSDataFloat(self.__fMinExposureTimePerImage))
                if (self.__fTransmission is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setTransmission(XSDataDouble(self.__fTransmission))
        if (self.__strForcedSpaceGroup is not None):
            xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString(self.__strForcedSpaceGroup))
        xsDataDiffractionPlan.setAnomalousData(XSDataBoolean(self.__bAnomalousData))
        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(self.__fMaxExposureTimePerDataCollection))
        if (self.__strStrategyOption is not None):
            xsDataDiffractionPlan.setStrategyOption(XSDataString(self.__strStrategyOption))
        xsDataCollection.setDiffractionPlan(xsDataDiffractionPlan)
        self.__xsDataInputCharacterisation.setDataCollection(xsDataCollection)


    def generateTemplateFile(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.generateTemplateFile")
        self.createInputCharacterisationFromSubWedges()
        if self.__strGeneratedTemplateFile is not None:
            if(self.__strGeneratedTemplateFile is None):
                EDVerbose.screen("No argument for command line --generateTemplate key word found!")
            elif (self.__xsDataInputCharacterisation is None):
                EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.__strGeneratedTemplateFile)
            else:
                EDVerbose.screen("Generating MXv1 xml template input file: " + self.__strGeneratedTemplateFile + "...")
                self.__xsDataInputCharacterisation.outputFile(self.__strGeneratedTemplateFile)
        if self.__strGeneratedTemplateFileMXv2 is not None:
            if(self.__strGeneratedTemplateFileMXv2 is None):
                EDVerbose.screen("No argument for command line --generateTemplateMXv2 key word found!")
            elif (self.__xsDataInputCharacterisation is None):
                EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.__strGeneratedTemplateFileMXv2)
            else:
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
                OmegaV = 0.0
                KappaV = 90.0
                PhiV = 40.0
                imgFnames = []
                xsDataResultSubWedgeAssemble = self.__edPluginControlSubWedgeAssemble.getDataOutput()
                for xsDataImage in xsDataResultSubWedgeAssemble.getSubWedge()[0].getImage():
                    imgFnames.append(xsDataImage.getPath().getValue())
                xsDC_v2 = self.generateDataCollectionDescriptorForSubWedge(calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames)
                EDVerbose.screen("Generating MXv2 xml template input file: " + self.__strGeneratedTemplateFileMXv2 + "...")
                xsDC_v2.outputFile(self.__strGeneratedTemplateFileMXv2)


    def doSubWedgeAssembleSUCCESS(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSubWedgeAssembleSUCCESS")
        self.createInputCharacterisationFromSubWedges()
        self.runCharacterisationPlugin(_edPlugin)

    def doSubWedgeAssembleFAILURE(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSubWedgeAssembleFAILURE")
        EDVerbose.screen("Execution of " + self.__strEDPluginControlSubWedgeAssembleName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.setFailure()

    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doFailureActionCharacterisation")
        self.retrieveFailureMessages(self.__edPluginControlCharacterisation, "EDPluginControlInterfacev2_0.doSuccessActionISPyB")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def doSuccessActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSuccessActionCharacterisation")
        # Store the results if requested
        if (self.__strResultsFilePath is not None):
            xsDataCharacterisationResult = _edPlugin.getDataOutput()
            if (xsDataCharacterisationResult is not None):
                xsDataCharacterisationResult.outputFile(self.__strResultsFilePath)
        self.storeResultsInISPyB(_edPlugin)

    def doSuccessActionISPyB(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.__edPluginControlISPyB, "EDPluginControlInterfacev2_0.doSuccessActionISPyB")

    def doFailureActionISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doFailureActionISpyB...")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def generateExecutiveSummary(self, _edPlugin=None):
        """
        Prints the executive summary from the plugin
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.generateExecutiveSummary")
        if (self.__edPluginControlSubWedgeAssemble is not None):
            if self.__edPluginControlSubWedgeAssemble.getListExecutiveSummaryLines() != []:
                self.addExecutiveSummaryLine("Summary of plugin %s:" % self.__strEDPluginControlSubWedgeAssembleName)
                self.appendExecutiveSummary(self.__edPluginControlSubWedgeAssemble)
        if (self.__edPluginControlCharacterisation is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.__strEDPluginControlCharacterisationName)
            self.appendExecutiveSummary(self.__edPluginControlCharacterisation)
        if (self.__edPluginControlISPyB is not None):
            self.addExecutiveSummaryLine("Summary of plugin %s:" % self.__strEDPluginControlISPyBName)
            self.appendExecutiveSummary(self.__edPluginControlISPyB)
        self.verboseScreenExecutiveSummary()



    def generateDataCollectionDescriptorForSubWedge(self, calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames):
        ##CONTAINER
        xsDC_v2 = XSDataCollection_v2()

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
        sw = XSSubWedge_v2()
        # template
        sw.setImagefilenametemplate(XSDataMXv2.XSDataString(EDUtilsImage.getTemplate(imgFnames[0], "#")))
        # images
        for imgFname in imgFnames:
            img = XSDiffractionImages_v2()
            img.setFilename(XSDataMXv2.XSDataString(imgFname))
            sw.addXSDiffractionImages(img)
        #RotationExposure
        rotexp = XSRotationExposure_v2()
        rotexp.setExposuretime(XSDataMXv2.XSDataTime(exposuretime))
        rotexp.setImagewidth(XSDataMXv2.XSDataAngle(imagewidth))
        rotexp.setNumberimages(XSDataMXv2.XSDataInteger(numberimages))
        rotexp.setXSGoniostatAxis(omega)
        sw.setXSRotationExposure(rotexp)
        #Beamsetting
        beams = XSBeamSetting_v2()
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




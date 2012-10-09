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

        self.strEDPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev1_1"
        self.strEDPluginControlCharacterisationName = "EDPluginControlCharForReorientationv2_0"
        self.strEDPluginControlISPyBName = "EDPluginControlISPyBv1_1"

        self.edPluginControlSubWedgeAssemble = None
        self.edPluginControlCharacterisation = None
        self.edPluginControlISPyB = None

        self.pyListImagePaths = None
        self.xsDataInputCharacterisation = None
        self.xsDataCollectionMXv2 = None
        self.strComplexity = "none"

        self.listImagePaths = []
        self.fFlux = None
        self.fMaxExposureTimePerDataCollection = 10000 # s, default prototype value
        self.fMinExposureTimePerImage = None
        self.fBeamSize = None
        self.bTemplateMode = False
        self.strGeneratedTemplateFile = None
        self.strGeneratedTemplateFileMXv2 = None
        self.strResultsFilePath = None
        self.strForcedSpaceGroup = None
        self.bAnomalousData = False
        self.fBeamPosX = None
        self.fBeamPosY = None
        self.fTransmission = None
        self.strStrategyOption = None
        self.iDataCollectionId = None
        self.strShortComments = None
        self.strComments = None


    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.configure")
        if (self.getControlledPluginName("subWedgeAssemblePlugin") is not None):
            self.strEDPluginControlSubWedgeAssembleName = self.getControlledPluginName("subWedgeAssemblePlugin")
        if (self.getControlledPluginName("characterisationPlugin") is not None):
            self.strEDPluginControlCharacterisationName = self.getControlledPluginName("characterisationPlugin")
        if (self.getControlledPluginName("ispybPlugin") is not None):
            self.strEDPluginControlISPyBName = self.getControlledPluginName("ispybPlugin")
        bUseISPyBPlugin = self.config.get("useISPyBPlugin", False)
        if not bUseISPyBPlugin:
            self.strEDPluginControlISPyBName = None


    def preProcess(self, _edPlugin=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.preProcess...")

        self.listImagePaths = []

        if (self.hasDataInput("diffractionPlan")):
            xsDataDiffractionPlan = XSDataDiffractionPlan()
            xsDataDiffractionPlans = self.getDataInput("diffractionPlan")
            if (not xsDataDiffractionPlans[0] is None):
                xsDataDiffractionPlan = xsDataDiffractionPlans[0]
                if (not xsDataDiffractionPlan.getForcedSpaceGroup() is None):
                    self.strForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
                if (not xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is None):
                    self.fMaxExposureTimePerDataCollection = xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue()
                if (not xsDataDiffractionPlan.getAnomalousData() is None):
                    self.bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()
                if (not xsDataDiffractionPlan.getStrategyOption() is None):
                    self.strStrategyOption = xsDataDiffractionPlan.getStrategyOption().getValue()
                if (not xsDataDiffractionPlan.getComplexity() is None):
                    self.strComplexity = xsDataDiffractionPlan.getComplexity().getValue()

        if (self.hasDataInput("imagePaths")):
            for strImagePath in self.getDataInput("imagePaths"):
                self.listImagePaths.append(strImagePath)
        if (self.hasDataInput("flux")):
            self.fFlux = self.getDataInput("flux")[0].getValue()
        if (self.hasDataInput("minExposureTimePerImage")):
            self.fMinExposureTimePerImage = self.getDataInput("minExposureTimePerImage")[0].getValue()
        if (self.hasDataInput("beamSize")):
            self.fBeamSize = self.getDataInput("beamSize")[0].getValue()
        if (self.hasDataInput("templateMode")):
            self.bTemplateMode = self.getDataInput("templateMode")[0].getValue()
        if (self.hasDataInput("generatedTemplateFile")):
            self.strGeneratedTemplateFile = self.getDataInput("generatedTemplateFile")[0].getValue()
        if (self.hasDataInput("generatedTemplateFileMXv2")):
            self.strGeneratedTemplateFileMXv2 = self.getDataInput("generatedTemplateFileMXv2")[0].getValue()
        if (self.hasDataInput("resultsFilePath")):
            self.strResultsFilePath = self.getDataInput("resultsFilePath")[0].getValue()
        if (self.hasDataInput("beamPosX")):
            self.fBeamPosX = self.getDataInput("beamPosX")[0].getValue()
        if (self.hasDataInput("beamPosY")):
            self.fBeamPosY = self.getDataInput("beamPosY")[0].getValue()
        if (self.hasDataInput("transmission")):
            self.fTransmission = self.getDataInput("transmission")[0].getValue()
        if (self.hasDataInput("dataCollectionId")):
            self.iDataCollectionId = self.getDataInput("dataCollectionId")[0].getValue()
        if (self.hasDataInput("shortComments")):
            self.strShortComments = self.getDataInput("shortComments")[0].getValue()
        if (self.hasDataInput("comments")):
            self.strComments = self.getDataInput("comments")[0].getValue()
        if (self.hasDataInput("inputCharacterisation")):
            self.xsDataInputCharacterisation = self.getDataInput("inputCharacterisation")[0]
        if (self.hasDataInput("mxv2DataCollection")):
            self.xsDataCollectionMXv2 = self.getDataInput("mxv2DataCollection")[0]

        # Check if XML data is given as input :
        if (self.xsDataInputCharacterisation is None):
            self.edPluginControlSubWedgeAssemble = self.loadPlugin(self.strEDPluginControlSubWedgeAssembleName, "SubWedgeAssemble")

        self.edPluginControlCharacterisation = self.loadPlugin(self.strEDPluginControlCharacterisationName, "Characterisation")

        if (self.strEDPluginControlISPyBName is not None):
            self.edPluginControlISPyB = self.loadPlugin(self.strEDPluginControlISPyBName, "ISPyB")


    def process(self, _edPlugin=None):
        """
        """
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.process...")

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


    def postProcess(self, _edPlugin=None):
        """
        """
        EDPluginControl.postProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.postProcess...")

        if (not self.edPluginControlCharacterisation is None):
            if (self.edPluginControlCharacterisation.hasDataOutput()):
                self.setDataOutput(self.edPluginControlCharacterisation.getDataOutput(), "resultCharacterisationv2_0")
        if (not self.edPluginControlISPyB is None):
            if (self.edPluginControlISPyB.hasDataOutput()):
                self.setDataOutput(self.edPluginControlISPyB.getDataOutput(), "ISPyB")


    def createInputCharacterisationFromImageHeaders(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.createInputCharacterisationFromImageHeaders")
        xsDataInputSubWedgeAssemble = XSDataInputSubWedgeAssemble()
        for xsDataStringImagePath in self.listImagePaths:
            xsDataFile = XSDataFile()
            xsDataFile.setPath(xsDataStringImagePath)
            xsDataInputSubWedgeAssemble.addFile(xsDataFile)
        _edPlugin.setDataInput(xsDataInputSubWedgeAssemble)
        _edPlugin.executeSynchronous()


    def runCharacterisationPlugin(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.runCharacterisationPlugin")
        self.edPluginControlCharacterisation.setDataInput(self.xsDataInputCharacterisation, "mxv1InputCharacterisation")
        if self.xsDataCollectionMXv2 != None:
            self.edPluginControlCharacterisation.setDataInput(self.xsDataCollectionMXv2, "mxv2DataCollection")
        self.edPluginControlCharacterisation.executeSynchronous()


    def storeResultsInISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.storeResultsInISPyB")
        if (self.edPluginControlISPyB is not None):
            # Execute the ISPyB control plugin
            xsDataInputControlISPyB = XSDataInputControlISPyB()
            xsDataInputControlISPyB.setCharacterisationResult(self.edPluginControlCharacterisation.getDataOutput().getMxv1ResultCharacterisation())
            if (not self.iDataCollectionId is None):
                xsDataInputControlISPyB.setDataCollectionId(XSDataInteger(self.iDataCollectionId))
            if (not self.strShortComments is None):
                self.edPluginControlISPyB.setDataInput(XSDataString(self.strShortComments), "shortComments")
            if (not self.strComments is None):
                self.edPluginControlISPyB.setDataInput(XSDataString(self.strComments), "comments")
            self.edPluginControlISPyB.setDataInput(xsDataInputControlISPyB)
            self.edPluginControlISPyB.executeSynchronous()


    def createInputCharacterisationFromSubWedges(self):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.createInputCharacterisationFromSubWedges")
        xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput()
        self.xsDataInputCharacterisation = XSDataInputCharacterisation()
        xsDataCollection = XSDataCollection()
        # Default exposure time (for the moment, this value should be
        # possible to read from the command line)
        xsDataDiffractionPlan = XSDataDiffractionPlan()
        if (not xsDataResultSubWedgeAssemble is None):
            pyListSubWedge = xsDataResultSubWedgeAssemble.getSubWedge()
            xsDataCollection.setSubWedge(pyListSubWedge)
            for xsDataSubWedge in pyListSubWedge:
                if (self.strComplexity is not None):
                    xsDataDiffractionPlan.setComplexity(XSDataString(self.strComplexity))
                if (self.fFlux is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(XSDataFloat(self.fFlux))
                if (self.fBeamSize is not None):
                    xsDataSize = XSDataSize()
                    xsDataSize.setX(XSDataLength(self.fBeamSize))
                    xsDataSize.setY(XSDataLength(self.fBeamSize))
                    xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataSize)
                if (self.fBeamPosX is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionX(XSDataLength(self.fBeamPosX))
                if (self.fBeamPosY is not None):
                    xsDataSubWedge.getExperimentalCondition().getDetector().setBeamPositionY(XSDataLength(self.fBeamPosY))
                if (self.fMinExposureTimePerImage is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(XSDataFloat(self.fMinExposureTimePerImage))
                if (self.fTransmission is not None):
                    xsDataSubWedge.getExperimentalCondition().getBeam().setTransmission(XSDataDouble(self.fTransmission))
        if (self.strForcedSpaceGroup is not None):
            xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString(self.strForcedSpaceGroup))
        xsDataDiffractionPlan.setAnomalousData(XSDataBoolean(self.bAnomalousData))
        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(self.fMaxExposureTimePerDataCollection))
        if (self.strStrategyOption is not None):
            xsDataDiffractionPlan.setStrategyOption(XSDataString(self.strStrategyOption))
        xsDataCollection.setDiffractionPlan(xsDataDiffractionPlan)
        self.xsDataInputCharacterisation.setDataCollection(xsDataCollection)


    def generateTemplateFile(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.generateTemplateFile")
        self.createInputCharacterisationFromSubWedges()
        if self.strGeneratedTemplateFile is not None:
            if(self.strGeneratedTemplateFile is None):
                EDVerbose.screen("No argument for command line --generateTemplate key word found!")
            elif (self.xsDataInputCharacterisation is None):
                EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.strGeneratedTemplateFile)
            else:
                EDVerbose.screen("Generating MXv1 xml template input file: " + self.strGeneratedTemplateFile + "...")
                self.xsDataInputCharacterisation.outputFile(self.strGeneratedTemplateFile)
        if self.strGeneratedTemplateFileMXv2 is not None:
            if(self.strGeneratedTemplateFileMXv2 is None):
                EDVerbose.screen("No argument for command line --generateTemplateMXv2 key word found!")
            elif (self.xsDataInputCharacterisation is None):
                EDVerbose.screen("ERROR! Cannot generate template file %s, please check the log files." % self.strGeneratedTemplateFileMXv2)
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
                xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput()
                for xsDataImage in xsDataResultSubWedgeAssemble.getSubWedge()[0].getImage():
                    imgFnames.append(xsDataImage.getPath().getValue())
                xsDC_v2 = self.generateDataCollectionDescriptorForSubWedge(calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames)
                EDVerbose.screen("Generating MXv2 xml template input file: " + self.strGeneratedTemplateFileMXv2 + "...")
                xsDC_v2.outputFile(self.strGeneratedTemplateFileMXv2)


    def doSubWedgeAssembleSUCCESS(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSubWedgeAssembleSUCCESS")
        self.createInputCharacterisationFromSubWedges()
        self.runCharacterisationPlugin(_edPlugin)

    def doSubWedgeAssembleFAILURE(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSubWedgeAssembleFAILURE")
        EDVerbose.screen("Execution of " + self.strEDPluginControlSubWedgeAssembleName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.setFailure()

    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doFailureActionCharacterisation")
        self.retrieveFailureMessages(self.edPluginControlCharacterisation, "EDPluginControlInterfacev2_0.doSuccessActionISPyB")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def doSuccessActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSuccessActionCharacterisation")
        # Store the results if requested
        if (self.strResultsFilePath is not None):
            xsDataCharacterisationResult = _edPlugin.getDataOutput()
            if (xsDataCharacterisationResult is not None):
                xsDataCharacterisationResult.outputFile(self.strResultsFilePath)
        self.storeResultsInISPyB(_edPlugin)

    def doSuccessActionISPyB(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.edPluginControlISPyB, "EDPluginControlInterfacev2_0.doSuccessActionISPyB")

    def doFailureActionISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.doFailureActionISpyB...")
        self.generateExecutiveSummary(self)
        self.setFailure()

    def generateExecutiveSummary(self, _edPlugin=None):
        """
        Prints the executive summary from the plugin
        """
        EDVerbose.DEBUG("EDPluginControlInterfacev2_0.generateExecutiveSummary")
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


        #xsDataResultSubWedgeAssemble = self.edPluginControlSubWedgeAssemble.getDataOutput()
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




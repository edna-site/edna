#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBStoreScreening
from XSDataISPyBv1_4 import XSDataResultISPyBStoreScreening


class EDPluginISPyBStoreScreeningv1_4(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBStoreScreening)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForBLSampleWebServiceWsdl = None
        self.strToolsForScreeningEDNAWebServiceWsdl = None
        self.iScreeningId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForBLSampleWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForBLSampleWebServiceWsdl")
        if self.strToolsForBLSampleWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_4.configure: No toolsForBLSampleWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForScreeningEDNAWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForScreeningEDNAWebServiceWsdl")
        if self.strToolsForScreeningEDNAWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_4.configure: No toolsForScreeningEDNAWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.process")
        xsDataInputISPyBStoreScreening = self.getDataInput()
        httpAuthenticatedToolsForAutoprocessingWebService1 = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForBLSampleWebServiceWsdl = Client(self.strToolsForBLSampleWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService1)
        httpAuthenticatedToolsForAutoprocessingWebService2 = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForScreeningEDNAWebServiceWsdl = Client(self.strToolsForScreeningEDNAWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService2)
        self.bContinue = True
        # DiffractionPlan
        xsDataISPyBDiffractionPlan = xsDataInputISPyBStoreScreening.diffractionPlan
        iDiffractionPlanId = self.storeOrUpdateDiffractionPlan(clientToolsForBLSampleWebServiceWsdl, xsDataISPyBDiffractionPlan)
        if iDiffractionPlanId is None:
            self.ERROR("Couldn't create entry for diffraction plan in ISPyB!")
            self.setFailure()
            self.bContinue = False
        # Screening
        xsDataISPyBScreening = xsDataInputISPyBStoreScreening.screening
        self.iScreeningId = self.storeOrUpdateScreening(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreening)
        if self.iScreeningId is None:
            self.ERROR("Couldn't create entry for screening in ISPyB!")
            self.setFailure()
            self.bContinue = False
        # Screening Input
        xsDataISPyBScreeningInput = xsDataInputISPyBStoreScreening.screeningInput
        iScreeningInputId = self.storeOrUpdateScreeningInput(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningInput, self.iScreeningId, iDiffractionPlanId)
        if iScreeningInputId is None:
            self.ERROR("Couldn't create entry for screening in ISPyB!")
            self.setFailure()
            self.bContinue = False
        # Screening Output Container
        for xsDataISPyBScreeningOutputContainer in xsDataInputISPyBStoreScreening.screeningOutputContainer:
            xsDataISPyBScreeningOutput = xsDataISPyBScreeningOutputContainer.screeningOutput
            iScreeningOutputId = self.storeOrUpdateScreeningOutput(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningOutput, self.iScreeningId)
            if iScreeningOutputId is None:
                self.ERROR("Couldn't create entry for screening in ISPyB!")
                self.setFailure()
                self.bContinue = False
            for xsDataISPyBScreeningOutputLattice in xsDataISPyBScreeningOutputContainer.screeningOutputLattice:
                iScreeningOutputLatticeId = self.storeOrUpdateScreeningOutputLattice(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningOutputLattice, iScreeningOutputId)
                if iScreeningOutputLatticeId is None:
                    self.ERROR("Couldn't create entry for screening lattice in ISPyB!")
                    self.setFailure()
                    self.bContinue = False
            for xsDataISPyBScreeningStrategyContainer in xsDataISPyBScreeningOutputContainer.screeningStrategyContainer:
                xsDataISPyBScreeningStrategy = xsDataISPyBScreeningStrategyContainer.screeningStrategy
                iScreeningStrategyId = self.storeOrUpdateScreeningStrategy(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningStrategy, iScreeningOutputId)
                if iScreeningStrategyId is None:
                    self.ERROR("Couldn't create entry for screening strategy in ISPyB!")
                    self.setFailure()
                    self.bContinue = False
                for xsDataISPyBScreeningStrategyWedgeContainer in xsDataISPyBScreeningStrategyContainer.screeningStrategyWedgeContainer:
                    xsDataISPyBScreeningStrategyWedge = xsDataISPyBScreeningStrategyWedgeContainer.screeningStrategyWedge
                    iScreeningStrategyWedgeId = self.storeOrUpdateScreeningStrategyWedge(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningStrategyWedge, iScreeningStrategyId)
                    if iScreeningStrategyWedgeId is None:
                        self.ERROR("Couldn't create entry for screening strategy in ISPyB!")
                        self.setFailure()
                        self.bContinue = False
                    for xsDataISPyBScreeningStrategySubWedge in xsDataISPyBScreeningStrategyWedgeContainer.screeningStrategySubWedge:
                        iScreeningStrategySubWedgeId = self.storeOrUpdateScreeningStrategySubWedge(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreeningStrategySubWedge, iScreeningStrategyWedgeId)
                        if iScreeningStrategySubWedgeId is None:
                            self.ERROR("Couldn't create entry for screening strategy in ISPyB!")
                            self.setFailure()
                            self.bContinue = False
                        
                    
            


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.postProcess")
        xsDataResultISPyBStoreScreening = XSDataResultISPyBStoreScreening()
        if self.iScreeningId is not None:
            xsDataResultISPyBStoreScreening.screeningId = XSDataInteger(self.iScreeningId)
        self.setDataOutput(xsDataResultISPyBStoreScreening)


    def getValue(self, _oValue, _oDefaultValue):
        if _oValue is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _oValue
        return oReturnValue

    
    def getXSValue(self, _xsData, _oDefaultValue):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _xsData.value
        if type(oReturnValue) == bool:
            if oReturnValue:
                oReturnValue = "1"
            else:
                oReturnValue = "0"
        return oReturnValue

    
    def getDateValue(self, _strValue, _strFormat, _oDefaultValue):
        if _strValue is None:
            oReturnValue = _oDefaultValue
        else:
            try:
                oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
            except:
                oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
        return oReturnValue
    
    def storeOrUpdateDiffractionPlan(self, _clientToolsForBLSampleWebServiceWsdl, _xsDataISPyBDiffractionPlan):
        """Creates an entry in ISPyB for the DiffractionPlan table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeDiffractionPlan")
        iDiffractionPlanId = self.getXSValue(_xsDataISPyBDiffractionPlan.diffractionPlanId, 0)
        iXmlDocumentId = self.getXSValue(_xsDataISPyBDiffractionPlan.xmlDocumentId, 0)
        strExperimentKind = self.getXSValue(_xsDataISPyBDiffractionPlan.experimentKind, "OSC")
        fObservedResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.observedResolution, -1.0)
        fMinimalResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.minimalResolution, -1.0)
        fExposureTime = self.getXSValue(_xsDataISPyBDiffractionPlan.exposureTime, -1.0)
        fOscillationRange = self.getXSValue(_xsDataISPyBDiffractionPlan.oscillationRange, -1.0)
        fMaximalResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.maximalResolution, -1.0)
        fScreeningResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.screeningResolution, -1.0)
        fRadiationSensitivity = self.getXSValue(_xsDataISPyBDiffractionPlan.radiationSensitivity, -1.0)
        strAnomalousScatterer = self.getXSValue(_xsDataISPyBDiffractionPlan.anomalousScatterer, "")
        fPreferredBeamSizeX = self.getXSValue(_xsDataISPyBDiffractionPlan.preferredBeamSizeX, -1.0)
        fPreferredBeamSizeY = self.getXSValue(_xsDataISPyBDiffractionPlan.preferredBeamSizeY, -1.0)
        strComments = self.getXSValue(_xsDataISPyBDiffractionPlan.comments, "")
        fAimedCompleteness = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedCompleteness, -1.0)
        fAimedIOverSigmaAtHighestResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedIOverSigmaAtHighestResolution, -1.0)
        fAimedMultiplicity = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedMultiplicity, -1.0)
        fAimedResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedResolution, -1.0)
        bAnomalousData = self.getXSValue(_xsDataISPyBDiffractionPlan.anomalousData, False)
        strComplexity = self.getXSValue(_xsDataISPyBDiffractionPlan.complexity, "")
        bEstimateRadiationDamage = self.getXSValue(_xsDataISPyBDiffractionPlan.estimateRadiationDamage, False)
        strForcedSpaceGroup = self.getXSValue(_xsDataISPyBDiffractionPlan.forcedSpaceGroup, "")
        fRequiredCompleteness = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredCompleteness, -1.0)
        fRequiredMultiplicity = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredMultiplicity, -1.0)
        fRequiredResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredResolution, -1.0)
        strStrategyOption = self.getXSValue(_xsDataISPyBDiffractionPlan.strategyOption, "")
        strKappaStrategyOption = self.getXSValue(_xsDataISPyBDiffractionPlan.kappaStrategyOption, "")
        iNumberOfPositions = self.getXSValue(_xsDataISPyBDiffractionPlan.numberOfPositions, -1)
        iDiffractionPlanId = _clientToolsForBLSampleWebServiceWsdl.service.storeOrUpdateDiffractionPlan(
            iDiffractionPlanId, \
            iXmlDocumentId, \
            strExperimentKind, \
            fObservedResolution, \
            fMinimalResolution, \
            fExposureTime, \
            fOscillationRange, \
            fMaximalResolution, \
            fScreeningResolution, \
            fRadiationSensitivity, \
            strAnomalousScatterer, \
            fPreferredBeamSizeX, \
            fPreferredBeamSizeY, \
            strComments, \
            fAimedCompleteness, \
            fAimedIOverSigmaAtHighestResolution, \
            fAimedMultiplicity, \
            fAimedResolution, \
            bAnomalousData, \
            strComplexity, \
            bEstimateRadiationDamage, \
            strForcedSpaceGroup, \
            fRequiredCompleteness, \
            fRequiredMultiplicity, \
            fRequiredResolution, \
            strStrategyOption, \
            strKappaStrategyOption, \
            iNumberOfPositions, \
            )
        self.DEBUG("DiffractionPlanId: %d" % iDiffractionPlanId)
        return iDiffractionPlanId


    def storeOrUpdateScreening(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreening):
        """Creates an entry in ISPyB for the Screening table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreening")
        iScreeningId = self.getXSValue(_xsDataISPyBScreening.screeningId, 0)
        iDataCollectionId = self.getXSValue(_xsDataISPyBScreening.dataCollectionId, 0)
        strTimeStamp = DateTime(datetime.datetime.now())
        strProgramVersion = self.getXSValue(_xsDataISPyBScreening.programVersion, "")
        strComments = self.getXSValue(_xsDataISPyBScreening.comments, "")
        strShortComments = self.getXSValue(_xsDataISPyBScreening.shortComments, "")
        iScreeningId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreening(
            iScreeningId, \
            iDataCollectionId, \
            strTimeStamp, \
            strProgramVersion, \
            strComments, \
            strShortComments, \
            )
        self.DEBUG("ScreeningId: %d" % iScreeningId)
        return iScreeningId



    def storeOrUpdateScreeningOutput(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningOutput, _iScreeningId):
        """Creates an entry in ISPyB for the ScreeningOutput table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningOutput")
        iScreeningOutputId = self.getXSValue(_xsDataISPyBScreeningOutput.screeningOutputId, 0)
        iScreeningId = _iScreeningId
        strStatusDescription = self.getXSValue(_xsDataISPyBScreeningOutput.statusDescription, "")
        iRejectedReflections = self.getXSValue(_xsDataISPyBScreeningOutput.rejectedReflections, 0)
        fResolutionObtained = self.getXSValue(_xsDataISPyBScreeningOutput.resolutionObtained, -1.0)
        fSpotDeviationR = self.getXSValue(_xsDataISPyBScreeningOutput.spotDeviationR, -1.0)
        fSpotDeviationTheta = self.getXSValue(_xsDataISPyBScreeningOutput.spotDeviationTheta, -1.0)
        fBeamShiftX = self.getXSValue(_xsDataISPyBScreeningOutput.beamShiftX, -1.0)
        fBeamShiftY = self.getXSValue(_xsDataISPyBScreeningOutput.beamShiftY, -1.0)
        iNumSpotsFound = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsFound, 0)
        iNumSpotsUsed = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsUsed, 0)
        iNumSpotsRejected = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsRejected, 0)
        fMosaicity = self.getXSValue(_xsDataISPyBScreeningOutput.mosaicity, -1.0)
        fIOverSigma = self.getXSValue(_xsDataISPyBScreeningOutput.iOverSigma, -1.0)
        bDiffractionRings = self.getXSValue(_xsDataISPyBScreeningOutput.diffractionRings, False)
        bScreeningSuccess = self.getXSValue(_xsDataISPyBScreeningOutput.screeningSuccess, False)
        bMosaicityEstimated = self.getXSValue(_xsDataISPyBScreeningOutput.mosaicityEstimated, False)
        iScreeningOutputId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningOutput(
            iScreeningOutputId, \
            iScreeningId, \
            strStatusDescription, \
            iRejectedReflections, \
            fResolutionObtained, \
            fSpotDeviationR, \
            fSpotDeviationTheta, \
            fBeamShiftX, \
            fBeamShiftY, \
            iNumSpotsFound, \
            iNumSpotsUsed, \
            iNumSpotsRejected, \
            fMosaicity, \
            fIOverSigma, \
            bDiffractionRings, \
            bScreeningSuccess, \
            bMosaicityEstimated, \
            )
        self.DEBUG("ScreeningOutputId: %d" % iScreeningOutputId)
        return iScreeningOutputId

    def storeOrUpdateScreeningOutputLattice(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningOutputLattice, _iScreeningOutputId):
        """Creates an entry in ISPyB for the ScreeningOutputLattice table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningOutputLattice")
        iScreeningOutputLatticeId = self.getXSValue(_xsDataISPyBScreeningOutputLattice.screeningOutputLatticeId, 0)
        iScreeningOutputId = _iScreeningOutputId
        strSpaceGroup = self.getXSValue(_xsDataISPyBScreeningOutputLattice.spaceGroup, "")
        strPointGroup = self.getXSValue(_xsDataISPyBScreeningOutputLattice.pointGroup, "")
        strBravaisLattice = self.getXSValue(_xsDataISPyBScreeningOutputLattice.bravaisLattice, "")
        fRawOrientationMatrix_a_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_x, -1.0)
        fRawOrientationMatrix_a_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_y, -1.0)
        fRawOrientationMatrix_a_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_z, -1.0)
        fRawOrientationMatrix_b_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_x, -1.0)
        fRawOrientationMatrix_b_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_y, -1.0)
        fRawOrientationMatrix_b_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_z, -1.0)
        fRawOrientationMatrix_c_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_x, -1.0)
        fRawOrientationMatrix_c_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_y, -1.0)
        fRawOrientationMatrix_c_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_z, -1.0)
        fUnitCell_a = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_a, -1.0)
        fUnitCell_alpha = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_alpha, -1.0)
        fUnitCell_b = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_b, -1.0)
        fUnitCell_beta = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_beta, -1.0)
        fUnitCell_c = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_c, -1.0)
        fUnitCell_gamma = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_gamma, -1.0)
        strTimeStamp = DateTime(datetime.datetime.now())
        iScreeningOutputLatticeId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningOutputLattice(
            iScreeningOutputLatticeId, \
            iScreeningOutputId, \
            strSpaceGroup, \
            strPointGroup, \
            strBravaisLattice, \
            fRawOrientationMatrix_a_x, \
            fRawOrientationMatrix_a_y, \
            fRawOrientationMatrix_a_z, \
            fRawOrientationMatrix_b_x, \
            fRawOrientationMatrix_b_y, \
            fRawOrientationMatrix_b_z, \
            fRawOrientationMatrix_c_x, \
            fRawOrientationMatrix_c_y, \
            fRawOrientationMatrix_c_z, \
            fUnitCell_a, \
            fUnitCell_alpha, \
            fUnitCell_b, \
            fUnitCell_beta, \
            fUnitCell_c, \
            fUnitCell_gamma, \
            strTimeStamp, \
            )
        self.DEBUG("ScreeningOutputLatticeId: %d" % iScreeningOutputLatticeId)
        return iScreeningOutputLatticeId

    def storeOrUpdateScreeningStrategy(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningStrategy, _iScreeningOutputId):
        """Creates an entry in ISPyB for the ScreeningStrategy table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningStrategy")
        iScreeningStrategyId = self.getXSValue(_xsDataISPyBScreeningStrategy.screeningStrategyId, 0)
        iScreeningOutputId = _iScreeningOutputId
        fPhiStart = self.getXSValue(_xsDataISPyBScreeningStrategy.phiStart, -1.0)
        fPhiEnd = self.getXSValue(_xsDataISPyBScreeningStrategy.phiEnd, -1.0)
        fRotation = self.getXSValue(_xsDataISPyBScreeningStrategy.rotation, -1.0)
        fExposureTime = self.getXSValue(_xsDataISPyBScreeningStrategy.exposureTime, -1.0)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategy.resolution, -1.0)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategy.completeness, -1.0)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategy.multiplicity, -1.0)
        bAnomalous = self.getXSValue(_xsDataISPyBScreeningStrategy.anomalous, False)
        strProgram = self.getXSValue(_xsDataISPyBScreeningStrategy.program, "")
        fRankingResolution = self.getXSValue(_xsDataISPyBScreeningStrategy.rankingResolution, -1.0)
        fTransmission = self.getXSValue(_xsDataISPyBScreeningStrategy.transmission, -1.0)
        iScreeningStrategyId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningStrategy(
            iScreeningStrategyId, \
            iScreeningOutputId, \
            fPhiStart, \
            fPhiEnd, \
            fRotation, \
            fExposureTime, \
            fResolution, \
            fCompleteness, \
            fMultiplicity, \
            bAnomalous, \
            strProgram, \
            fRankingResolution, \
            fTransmission, \
            )
        self.DEBUG("ScreeningStrategyId: %d" % iScreeningStrategyId)
        return iScreeningStrategyId

    def storeOrUpdateScreeningStrategyWedge(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningStrategyWedge, _iScreeningStrategyId):
        """Creates an entry in ISPyB for the ScreeningStrategyWedge table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningStrategyWedge")
        iScreeningStrategyWedgeId = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.screeningStrategyWedgeId, 0)
        iScreeningStrategyId = _iScreeningStrategyId
        iWedgeNumber = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.wedgeNumber, 0)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.resolution, -1.0)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.completeness, -1.0)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.multiplicity, -1.0)
        fDoseTotal = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.doseTotal, -1.0)
        iNumberOfImages = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.numberOfImages, 0)
        fPhi = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.phi, -1.0)
        fKappa = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.kappa, -1.0)
        iScreeningStrategyWedgeId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningStrategyWedge(
            iScreeningStrategyWedgeId, \
            iScreeningStrategyId, \
            iWedgeNumber, \
            fResolution, \
            fCompleteness, \
            fMultiplicity, \
            fDoseTotal, \
            iNumberOfImages, \
            fPhi, \
            fKappa, \
            )
        self.DEBUG("ScreeningStrategyWedgeId: %d" % iScreeningStrategyWedgeId)
        return iScreeningStrategyWedgeId

    def storeOrUpdateScreeningStrategySubWedge(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningStrategySubWedge, _iScreeningStrategyWedgeId):
        """Creates an entry in ISPyB for the ScreeningStrategySubWedge table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningStrategySubWedge")
        iScreeningStrategySubWedgeId = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.screeningStrategySubWedgeId, 0)
        iScreeningStrategyWedgeId = _iScreeningStrategyWedgeId
        iSubWedgeNumber = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.subWedgeNumber, 0)
        strRotationAxis = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.rotationAxis, "")
        fAxisStart = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.axisStart, -1.0)
        fAxisEnd = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.axisEnd, -1.0)
        fExposureTime = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.exposureTime, -1.0)
        fTransmission = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.transmission, -1.0)
        fOscillationRange = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.oscillationRange, -1.0)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.completeness, -1.0)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.multiplicity, -1.0)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.resolution, -1.0)
        fDoseTotal = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.doseTotal, -1.0)
        iNumberOfImages = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.numberOfImages, 0)
        iScreeningStrategySubWedgeId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningStrategySubWedge(
            iScreeningStrategySubWedgeId, \
            iScreeningStrategyWedgeId, \
            iSubWedgeNumber, \
            strRotationAxis, \
            fAxisStart, \
            fAxisEnd, \
            fExposureTime, \
            fTransmission, \
            fOscillationRange, \
            fCompleteness, \
            fMultiplicity, \
            fResolution, \
            fDoseTotal, \
            iNumberOfImages, \
            )
        self.DEBUG("ScreeningStrategySubWedgeId: %d" % iScreeningStrategySubWedgeId)
        return iScreeningStrategySubWedgeId

    def storeOrUpdateScreeningInput(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreeningInput, _iScreeningId, _iDiffractionPlanId):
        """Creates an entry in ISPyB for the ScreeningInput table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_4.storeScreeningInput")
        iScreeningInputId = self.getXSValue(_xsDataISPyBScreeningInput.screeningInputId, 0)
        iScreeningId = _iScreeningId
        iDiffractionPlanId = _iDiffractionPlanId
        fBeamX = self.getXSValue(_xsDataISPyBScreeningInput.beamX, 9999.0)
        fBeamY = self.getXSValue(_xsDataISPyBScreeningInput.beamY, 9999.0)
        fRmsErrorLimits = self.getXSValue(_xsDataISPyBScreeningInput.rmsErrorLimits, -1.0)
        fMinimumFractionIndexed = self.getXSValue(_xsDataISPyBScreeningInput.minimumFractionIndexed, -1.0)
        fMaximumFractionRejected = self.getXSValue(_xsDataISPyBScreeningInput.maximumFractionRejected, -1.0)
        fMinimumSignalToNoise = self.getXSValue(_xsDataISPyBScreeningInput.minimumSignalToNoise, -1.0)
        strXmlSampleInformation = self.getXSValue(_xsDataISPyBScreeningInput.xmlSampleInformation, "")
        iScreeningInputId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreeningInput(
            iScreeningInputId, \
            iScreeningId, \
            iDiffractionPlanId, \
            fBeamX, \
            fBeamY, \
            fRmsErrorLimits, \
            fMinimumFractionIndexed, \
            fMaximumFractionRejected, \
            fMinimumSignalToNoise, \
            strXmlSampleInformation, \
            )
        self.DEBUG("ScreeningInputId: %d" % iScreeningInputId)
        return iScreeningInputId



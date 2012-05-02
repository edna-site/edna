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
        iDiffractionPlanId = self.getXSValue(_xsDataISPyBDiffractionPlan.diffractionPlanId, None)
        iXmlDocumentId = self.getXSValue(_xsDataISPyBDiffractionPlan.xmlDocumentId, None)
        strExperimentKind = self.getXSValue(_xsDataISPyBDiffractionPlan.experimentKind, None)
        fObservedResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.observedResolution, None)
        fMinimalResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.minimalResolution, None)
        fExposureTime = self.getXSValue(_xsDataISPyBDiffractionPlan.exposureTime, None)
        fOscillationRange = self.getXSValue(_xsDataISPyBDiffractionPlan.oscillationRange, None)
        fMaximalResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.maximalResolution, None)
        fScreeningResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.screeningResolution, None)
        fRadiationSensitivity = self.getXSValue(_xsDataISPyBDiffractionPlan.radiationSensitivity, None)
        strAnomalousScatterer = self.getXSValue(_xsDataISPyBDiffractionPlan.anomalousScatterer, None)
        fPreferredBeamSizeX = self.getXSValue(_xsDataISPyBDiffractionPlan.preferredBeamSizeX, None)
        fPreferredBeamSizeY = self.getXSValue(_xsDataISPyBDiffractionPlan.preferredBeamSizeY, None)
        strComments = self.getXSValue(_xsDataISPyBDiffractionPlan.comments, None)
        fAimedCompleteness = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedCompleteness, None)
        fAimedIOverSigmaAtHighestResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedIOverSigmaAtHighestResolution, None)
        fAimedMultiplicity = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedMultiplicity, None)
        fAimedResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.aimedResolution, None)
        bAnomalousData = self.getXSValue(_xsDataISPyBDiffractionPlan.anomalousData, False)
        strComplexity = self.getXSValue(_xsDataISPyBDiffractionPlan.complexity, None)
        bEstimateRadiationDamage = self.getXSValue(_xsDataISPyBDiffractionPlan.estimateRadiationDamage, False)
        strForcedSpaceGroup = self.getXSValue(_xsDataISPyBDiffractionPlan.forcedSpaceGroup, None)
        fRequiredCompleteness = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredCompleteness, None)
        fRequiredMultiplicity = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredMultiplicity, None)
        fRequiredResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.requiredResolution, None)
        strStrategyOption = self.getXSValue(_xsDataISPyBDiffractionPlan.strategyOption, None)
        strKappaStrategyOption = self.getXSValue(_xsDataISPyBDiffractionPlan.kappaStrategyOption, None)
        iNumberOfPositions = self.getXSValue(_xsDataISPyBDiffractionPlan.numberOfPositions, None)
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
        iScreeningId = self.getXSValue(_xsDataISPyBScreening.screeningId, None)
        iDataCollectionId = self.getXSValue(_xsDataISPyBScreening.dataCollectionId, None)
        strTimeStamp = DateTime(datetime.datetime.now())
        strProgramVersion = self.getXSValue(_xsDataISPyBScreening.programVersion, None)
        strComments = self.getXSValue(_xsDataISPyBScreening.comments, None)
        strShortComments = self.getXSValue(_xsDataISPyBScreening.shortComments, None)
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
        iScreeningOutputId = self.getXSValue(_xsDataISPyBScreeningOutput.screeningOutputId, None)
        iScreeningId = _iScreeningId
        strStatusDescription = self.getXSValue(_xsDataISPyBScreeningOutput.statusDescription, None)
        iRejectedReflections = self.getXSValue(_xsDataISPyBScreeningOutput.rejectedReflections, None)
        fResolutionObtained = self.getXSValue(_xsDataISPyBScreeningOutput.resolutionObtained, None)
        fSpotDeviationR = self.getXSValue(_xsDataISPyBScreeningOutput.spotDeviationR, None)
        fSpotDeviationTheta = self.getXSValue(_xsDataISPyBScreeningOutput.spotDeviationTheta, None)
        fBeamShiftX = self.getXSValue(_xsDataISPyBScreeningOutput.beamShiftX, None)
        fBeamShiftY = self.getXSValue(_xsDataISPyBScreeningOutput.beamShiftY, None)
        iNumSpotsFound = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsFound, None)
        iNumSpotsUsed = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsUsed, None)
        iNumSpotsRejected = self.getXSValue(_xsDataISPyBScreeningOutput.numSpotsRejected, None)
        fMosaicity = self.getXSValue(_xsDataISPyBScreeningOutput.mosaicity, None)
        fIOverSigma = self.getXSValue(_xsDataISPyBScreeningOutput.iOverSigma, None)
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
        iScreeningOutputLatticeId = self.getXSValue(_xsDataISPyBScreeningOutputLattice.screeningOutputLatticeId, None)
        iScreeningOutputId = _iScreeningOutputId
        strSpaceGroup = self.getXSValue(_xsDataISPyBScreeningOutputLattice.spaceGroup, None)
        strPointGroup = self.getXSValue(_xsDataISPyBScreeningOutputLattice.pointGroup, None)
        strBravaisLattice = self.getXSValue(_xsDataISPyBScreeningOutputLattice.bravaisLattice, None)
        fRawOrientationMatrix_a_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_x, None)
        fRawOrientationMatrix_a_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_y, None)
        fRawOrientationMatrix_a_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_a_z, None)
        fRawOrientationMatrix_b_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_x, None)
        fRawOrientationMatrix_b_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_y, None)
        fRawOrientationMatrix_b_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_b_z, None)
        fRawOrientationMatrix_c_x = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_x, None)
        fRawOrientationMatrix_c_y = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_y, None)
        fRawOrientationMatrix_c_z = self.getXSValue(_xsDataISPyBScreeningOutputLattice.rawOrientationMatrix_c_z, None)
        fUnitCell_a = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_a, None)
        fUnitCell_alpha = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_alpha, None)
        fUnitCell_b = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_b, None)
        fUnitCell_beta = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_beta, None)
        fUnitCell_c = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_c, None)
        fUnitCell_gamma = self.getXSValue(_xsDataISPyBScreeningOutputLattice.unitCell_gamma, None)
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
        iScreeningStrategyId = self.getXSValue(_xsDataISPyBScreeningStrategy.screeningStrategyId, None)
        iScreeningOutputId = _iScreeningOutputId
        fPhiStart = self.getXSValue(_xsDataISPyBScreeningStrategy.phiStart, None)
        fPhiEnd = self.getXSValue(_xsDataISPyBScreeningStrategy.phiEnd, None)
        fRotation = self.getXSValue(_xsDataISPyBScreeningStrategy.rotation, None)
        fExposureTime = self.getXSValue(_xsDataISPyBScreeningStrategy.exposureTime, None)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategy.resolution, None)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategy.completeness, None)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategy.multiplicity, None)
        bAnomalous = self.getXSValue(_xsDataISPyBScreeningStrategy.anomalous, False)
        strProgram = self.getXSValue(_xsDataISPyBScreeningStrategy.program, None)
        fRankingResolution = self.getXSValue(_xsDataISPyBScreeningStrategy.rankingResolution, None)
        fTransmission = self.getXSValue(_xsDataISPyBScreeningStrategy.transmission, None)
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
        iScreeningStrategyWedgeId = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.screeningStrategyWedgeId, None)
        iScreeningStrategyId = _iScreeningStrategyId
        iWedgeNumber = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.wedgeNumber, None)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.resolution, None)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.completeness, None)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.multiplicity, None)
        fDoseTotal = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.doseTotal, None)
        iNumberOfImages = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.numberOfImages, None)
        fPhi = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.phi, None)
        fKappa = self.getXSValue(_xsDataISPyBScreeningStrategyWedge.kappa, None)
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
        iScreeningStrategySubWedgeId = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.screeningStrategySubWedgeId, None)
        iScreeningStrategyWedgeId = _iScreeningStrategyWedgeId
        iSubWedgeNumber = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.subWedgeNumber, None)
        strRotationAxis = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.rotationAxis, None)
        fAxisStart = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.axisStart, None)
        fAxisEnd = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.axisEnd, None)
        fExposureTime = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.exposureTime, None)
        fTransmission = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.transmission, None)
        fOscillationRange = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.oscillationRange, None)
        fCompleteness = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.completeness, None)
        fMultiplicity = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.multiplicity, None)
        fResolution = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.resolution, None)
        fDoseTotal = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.doseTotal, None)
        iNumberOfImages = self.getXSValue(_xsDataISPyBScreeningStrategySubWedge.numberOfImages, None)
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
        iScreeningInputId = self.getXSValue(_xsDataISPyBScreeningInput.screeningInputId, None)
        iScreeningId = _iScreeningId
        iDiffractionPlanId = _iDiffractionPlanId
        fBeamX = self.getXSValue(_xsDataISPyBScreeningInput.beamX, None)
        fBeamY = self.getXSValue(_xsDataISPyBScreeningInput.beamY, None)
        fRmsErrorLimits = self.getXSValue(_xsDataISPyBScreeningInput.rmsErrorLimits, None)
        fMinimumFractionIndexed = self.getXSValue(_xsDataISPyBScreeningInput.minimumFractionIndexed, None)
        fMaximumFractionRejected = self.getXSValue(_xsDataISPyBScreeningInput.maximumFractionRejected, None)
        fMinimumSignalToNoise = self.getXSValue(_xsDataISPyBScreeningInput.minimumSignalToNoise, None)
        strXmlSampleInformation = self.getXSValue(_xsDataISPyBScreeningInput.xmlSampleInformation, None)
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



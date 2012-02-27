#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011      European Synchrotron Radiation Facility
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

from XSDataISPyBv1_3 import XSDataInputISPyBStoreScreening
from XSDataISPyBv1_3 import XSDataResultISPyBStoreScreening


class EDPluginISPyBStoreScreeningv1_3(EDPluginExec):
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
        self.iDiffractionPlanId = None
        self.iScreeningId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_3.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_3.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForBLSampleWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForBLSampleWebServiceWsdl")
        if self.strToolsForBLSampleWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_3.configure: No toolsForBLSampleWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForScreeningEDNAWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForScreeningEDNAWebServiceWsdl")
        if self.strToolsForBLSampleWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_3.configure: No toolsForScreeningEDNAWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreScreeningv1_3.process")
        xsDataInputISPyBStoreScreening = self.getDataInput()
        httpAuthenticatedToolsForAutoprocessingWebService1 = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForBLSampleWebServiceWsdl = Client(self.strToolsForBLSampleWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService1)
        httpAuthenticatedToolsForAutoprocessingWebService2 = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForScreeningEDNAWebServiceWsdl = Client(self.strToolsForScreeningEDNAWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService2)
        self.bContinue = True
        # DiffractionPlan
        xsDataISPyBDiffractionPlan = xsDataInputISPyBStoreScreening.diffractionPlan
        self.iDiffractionPlanId = self.storeOrUpdateDiffractionPlan(clientToolsForBLSampleWebServiceWsdl, xsDataISPyBDiffractionPlan)
        if self.iDiffractionPlanId is None:
            self.ERROR("Couldn't create entry for diffraction plan in ISPyB!")
            self.setFailure()
            self.bContinue = False
        # Screening
        xsDataISPyBScreening = xsDataInputISPyBStoreScreening.screening
        self.iScreeningId = self.storeOrUpdateScreeningRequest(clientToolsForScreeningEDNAWebServiceWsdl, xsDataISPyBScreening)
        if self.iScreeningId is None:
            self.ERROR("Couldn't create entry for screening in ISPyB!")
            self.setFailure()
            self.bContinue = False
            


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreScreeningv1_3.postProcess")
        xsDataResultISPyBStoreScreening = XSDataResultISPyBStoreScreening()
        if self.iDiffractionPlanId is not None:
            xsDataResultISPyBStoreScreening.diffractionPlanId = XSDataInteger(self.iDiffractionPlanId)
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
        if oReturnValue.__class__.__name__ == 'unicode':
            oReturnValue = str(oReturnValue)
        print oReturnValue.__class__.__name__
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
        """Creates an entry in the ISPyB AutoProcProgram table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_3.storeOrUpdateDiffractionPlan")
        print _xsDataISPyBDiffractionPlan.marshal()
        iDiffractionPlanId = self.getXSValue(_xsDataISPyBDiffractionPlan.diffractionPlanId, 0)
        iXmlDocumentId     = self.getXSValue(_xsDataISPyBDiffractionPlan.xmlDocumentId, 0)
        strExperimentKind  = self.getXSValue(_xsDataISPyBDiffractionPlan.experimentKind, "OSC")
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
        iNumberOfPositions = self.getXSValue(_xsDataISPyBDiffractionPlan.numberOfPositions, 1)
        iDifftactionPlanId = _clientToolsForBLSampleWebServiceWsdl.service.storeOrUpdateDiffractionPlan(
                in0 = iDiffractionPlanId, \
                in1 = iXmlDocumentId, \
                in2 = strExperimentKind, \
                in3 = fObservedResolution, \
                in4 = fMinimalResolution, \
                in5 = fExposureTime, \
                in6 = fOscillationRange, \
                in7 = fMaximalResolution, \
                in8 = fScreeningResolution, \
                in9 = fRadiationSensitivity, \
                in10 = strAnomalousScatterer, \
                in11 = fPreferredBeamSizeX, \
                in12 = fPreferredBeamSizeY, \
                in13 = strComments, \
                in14 = fAimedCompleteness, \
                in15 = fAimedIOverSigmaAtHighestResolution, \
                in16 = fAimedMultiplicity, \
                in17 = fAimedResolution, \
                in18 = bAnomalousData, \
                in19 = strComplexity, \
                in20 = bEstimateRadiationDamage, \
                in21 = strForcedSpaceGroup, \
                in22 = fRequiredCompleteness, \
                in23 = fRequiredMultiplicity, \
                in24 = fRequiredResolution, \
                in25 = strStrategyOption, \
                in26 = strKappaStrategyOption, \
                in27 = iNumberOfPositions                
                )
        self.DEBUG("iDiffractionPlanId: %r" % iDifftactionPlanId)
        return iDifftactionPlanId

    def storeOrUpdateScreeningRequest(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyBScreening):
        """Creates an entry in the ISPyB Screening table"""
        self.DEBUG("EDPluginISPyBStoreScreeningv1_3.storestoreOrUpdateScreeningRequest")
        iScreeningId      = self.getXSValue(_xsDataISPyBScreening.screeningId, 0) # integer
        iDataCollectionId = self.getXSValue(_xsDataISPyBScreening.dataCollectionId, 0)
        recordTimeStamp   = DateTime(datetime.datetime.now())
        programVersion    = self.getXSValue(_xsDataISPyBScreening.programVersion, "EDNA MXv1")
        comments          = self.getXSValue(_xsDataISPyBScreening.comments, None)
        shortComments     = self.getXSValue(_xsDataISPyBScreening.shortComments, None)
        iScreeningId      = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdateScreening(
                in0 = iScreeningId, \
                in1 = iDataCollectionId, \
                in2 = recordTimeStamp, \
                in3 = programVersion, \
                in4 = comments, \
                in5 = shortComments)
        self.DEBUG("ScreeningId: %r" % iScreeningId)
        return iScreeningId


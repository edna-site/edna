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
        iDiffractionPlanId = self.getXSValue(_xsDataISPyBDiffractionPlan.diffractionPlanId, 0)
        iXmlDocumentId     = self.getXSValue(_xsDataISPyBDiffractionPlan.xmlDocumentId, 0)
        strExperimentKind  = self.getXSValue(_xsDataISPyBDiffractionPlan.experimentKind, "Test")
        fObservedResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.observedResolution, 9999.0)
        fMinimalResolution = self.getXSValue(_xsDataISPyBDiffractionPlan.minimalResolution, 9999.0)
#        exposureTime : XSDataDouble optional
#        oscillationRange : XSDataDouble optional
#        maximalResolution : XSDataDouble optional
#        screeningResolution : XSDataDouble optional
#        radiationSensitivity : XSDataDouble optional
#        anomalousScatterer : XSDataString optional
#        preferredBeamSizeX : XSDataDouble optional
#        preferredBeamSizeY : XSDataDouble optional
#        comments : XSDataString optional
#        aimedCompleteness : XSDataDouble optional
#        aimedIOverSigmaAtHighestResolution : XSDataDouble optional
#        aimedMultiplicity : XSDataDouble optional
#        aimedResolution : XSDataDouble optional
#        anomalousData : XSDataBoolean optional
#        complexity : XSDataString optional
#        estimateRadiationDamage : XSDataBoolean optional
#        forcedSpaceGroup : XSDataString optional
#        requiredCompleteness : XSDataDouble optional
#        requiredMultiplicity : XSDataDouble optional
#        requiredResolution : XSDataDouble optional
#        strategyOption : XSDataString optional
#        kappaStrategyOption : XSDataString optional
#        numberOfPositions : XSDataInteger optional
#        
#        strProcessingCommandLine = self.getValue(_xsDataAutoProcProgram.getProcessingCommandLine(), "")
#        strProcessingPrograms    = self.getValue(_xsDataAutoProcProgram.getProcessingPrograms(), "")
#        bProcessingStatus        = self.getValue(_xsDataAutoProcProgram.getProcessingStatus(), True)
#        strProcessingMessage     = self.getValue(_xsDataAutoProcProgram.getProcessingMessage(), "")
#        processingStartTime      = self.getDateValue(_xsDataAutoProcProgram.getProcessingStartTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        processingEndTime        = self.getDateValue(_xsDataAutoProcProgram.getProcessingEndTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        strProcessingEnvironment = self.getValue(_xsDataAutoProcProgram.getProcessingEnvironment(), "")
#        recordTimeStamp          = DateTime(datetime.datetime.now())
        iDifftactionPlanId = _clientToolsForBLSampleWebServiceWsdl.service.storeOrUpdateDiffractionPlan(
                in0 = iDiffractionPlanId, \
                in1 = iXmlDocumentId, \
                in2 = None, \
                in3 = None, \
                in4 = None, \
                in5 = None, \
                in6 = None, \
                in7 = None, \
                in8 = None, \
                in9 = None, \
                in10 = None, \
                in11 = None, \
                in12 = None, \
                in13 = None, \
                in14 = None, \
                in15 = None, \
                in16 = None, \
                in17 = None, \
                in18 = None, \
                in19 = None, \
                in20 = None, \
                in21 = None, \
                in22 = None, \
                in23 = None, \
                in24 = None, \
                in25 = None, \
                in26 = None, \
                in27 = None                
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


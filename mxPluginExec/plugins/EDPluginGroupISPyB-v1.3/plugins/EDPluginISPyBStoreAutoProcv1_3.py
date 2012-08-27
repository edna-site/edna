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
__date__ = "20120712"
__status__ = "deprecated"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_3 import XSDataInputStoreAutoProc
from XSDataISPyBv1_3 import XSDataResultStoreAutoProc


class EDPluginISPyBStoreAutoProcv1_3(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreAutoProc)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForAutoprocessingWebServiceWsdl = None
        self.iAutoProcId = None
        self.iAutoProcProgramId = None
        self.bContinue = True
        self.iAutoProcScaling_has_IntId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_3.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_3.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_3.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_3.process")
        xsDataInputStoreAutoProc = self.getDataInput()
        xsDataAutoProcContainer = xsDataInputStoreAutoProc.getAutoProcContainer()
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService)
        xsDataAutoProcScalingContainer = xsDataAutoProcContainer.getAutoProcScalingContainer()
        xsDataAutoProcProgram = xsDataAutoProcContainer.getAutoProcProgramContainer().getAutoProcProgram()
        # AutoProcProgram
        self.iAutoProcProgramId = self.storeAutoProcProgram(clientToolsForAutoprocessingWebService, xsDataAutoProcProgram)
        if self.iAutoProcProgramId is None:
            self.ERROR("Couldn't create entry for AutoProcProgram in ISPyB!")
            self.setFailure()
            self.bContinue = False
        else:
            listAutoProcProgramAttachment = xsDataAutoProcContainer.getAutoProcProgramContainer().getAutoProcProgramAttachment()
            for xsDataAutoProcProgramAttachment in listAutoProcProgramAttachment:
                self.storeAutoProcProgramAttachment(clientToolsForAutoprocessingWebService, xsDataAutoProcProgramAttachment)
            if xsDataAutoProcProgram.getProcessingStatus() == False:
                self.bContinue = False
        if self.bContinue:
            # AutoProcIntegration
            xsDataAutoProcIntegrationContainer = xsDataAutoProcScalingContainer.getAutoProcIntegrationContainer()
            self.iAutoProcIntegrationId = self.storeAutoProcIntegration(clientToolsForAutoprocessingWebService, xsDataAutoProcIntegrationContainer)
            if self.iAutoProcIntegrationId is None:
                self.WARNING("Couldn't create entry for AutoProcIntegration in ISPyB!")
        if self.bContinue:
            # AutoProc
            xsDataAutoProc = xsDataAutoProcContainer.getAutoProc()
            self.iAutoProcId = self.storeAutoProc(clientToolsForAutoprocessingWebService, xsDataAutoProc)
            if self.iAutoProcId is None:
                self.ERROR("Couldn't create entry for AutoProc in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScaling
            xsDataAutoProcScaling = xsDataAutoProcScalingContainer.getAutoProcScaling()
            self.iAutoProcScalingId = self.storeAutoProcScaling(clientToolsForAutoprocessingWebService, xsDataAutoProcScaling)
            if self.iAutoProcScalingId is None:
                self.ERROR("Couldn't create entry for AutoProcScaling in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScaling_has_IntId
            self.iAutoProcScaling_has_IntId = self.storeAutoProcScaling_has_IntId(clientToolsForAutoprocessingWebService)
            if self.iAutoProcScaling_has_IntId is None:
                self.ERROR("Couldn't create entry for AutoProcScaling_has_IntId in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScalingStatistics
            for xsDataAutoProcScalingStatistics in xsDataAutoProcScalingContainer.getAutoProcScalingStatistics():
                iAutoProcScalingStatisticsId = self.storeAutoProcScalingStatistics(clientToolsForAutoprocessingWebService, xsDataAutoProcScalingStatistics)
                if iAutoProcScalingStatisticsId is None:
                    self.ERROR("Couldn't create entry for AutoProcScalingStatistics in ISPyB!")
                    self.setFailure()
                    self.bContinue = False
            


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_3.postProcess")
        xsDataResultStoreAutoProc = XSDataResultStoreAutoProc()
        if self.iAutoProcId is not None:
            xsDataResultStoreAutoProc.setAutoProcId(XSDataInteger(self.iAutoProcId))
        self.setDataOutput(xsDataResultStoreAutoProc)


    def getValue(self, _oValue, _oDefaultValue):
        if _oValue is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _oValue
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
    

    def storeAutoProcProgram(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgram):
        """Creates an entry in the ISPyB AutoProcProgram table"""
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_3.storeAutoProcProgram")
        strProcessingCommandLine = self.getValue(_xsDataAutoProcProgram.getProcessingCommandLine(), "")
        strProcessingPrograms    = self.getValue(_xsDataAutoProcProgram.getProcessingPrograms(), "")
        bProcessingStatus        = self.getValue(_xsDataAutoProcProgram.getProcessingStatus(), True)
        strProcessingMessage     = self.getValue(_xsDataAutoProcProgram.getProcessingMessage(), "")
        processingStartTime      = self.getDateValue(_xsDataAutoProcProgram.getProcessingStartTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        processingEndTime        = self.getDateValue(_xsDataAutoProcProgram.getProcessingEndTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        strProcessingEnvironment = self.getValue(_xsDataAutoProcProgram.getProcessingEnvironment(), "")
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcProgramId = _clientToolsForAutoprocessingWebService.service.storeAutoProcProgram(
                in0 = strProcessingCommandLine, \
                in1 = strProcessingPrograms, \
                in2 = bProcessingStatus, \
                in3 = strProcessingMessage, \
                in4 = processingStartTime, \
                in5 = processingEndTime, \
                in6 = strProcessingEnvironment, \
                in7 = recordTimeStamp
                )
        self.DEBUG("AutoProcProgramId: %r" % iAutoProcProgramId)
        return iAutoProcProgramId


    def storeAutoProcProgramAttachment(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgramAttachment):
        """Creates an entry in the ISPyB AutoProcProgramAttachment table"""
        iAutoProcProgramId = self.iAutoProcProgramId
        strFileType = self.getValue(_xsDataAutoProcProgramAttachment.getFileType(), "")
        strFileName = self.getValue(_xsDataAutoProcProgramAttachment.getFileName(), "")
        strFilePath = self.getValue(_xsDataAutoProcProgramAttachment.getFilePath(), "")
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcProgramAttachmentId = _clientToolsForAutoprocessingWebService.service.storeAutoProcProgramAttachment(
                in0 = strFileType, \
                in1 = strFileName, \
                in2 = strFilePath, \
                in3 = recordTimeStamp, \
                in4 = iAutoProcProgramId
                )
        self.DEBUG("AutoProcProgramAttachmentId: %r" % iAutoProcProgramAttachmentId)
        return iAutoProcProgramAttachmentId


    def storeAutoProcIntegration(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcIntegrationContainer):
        """Creates an entry in the ISPyB AutoProcIntegration table"""
        xsDataProcIntegration = _xsDataAutoProcIntegrationContainer.getAutoProcIntegration()
        iAutoProcProgramId = self.iAutoProcProgramId
        iStartImageNumber  = self.getValue(xsDataProcIntegration.getStartImageNumber(), 9999)
        iEndImageNumber    = self.getValue(xsDataProcIntegration.getEndImageNumber(), 9999)
        fRefinedDetectorDistance = self.getValue(xsDataProcIntegration.getRefinedDetectorDistance(), -1.0)
        fRefinedXbeam      = self.getValue(xsDataProcIntegration.getRefinedXbeam(), -1.0)
        fRefinedYbeam      = self.getValue(xsDataProcIntegration.getRefinedYbeam(), -1.0)
        fRotationAxisX     = self.getValue(xsDataProcIntegration.getRotationAxisX(), -1.0)
        fRotationAxisY     = self.getValue(xsDataProcIntegration.getRotationAxisY(), -1.0)
        fRotationAxisZ     = self.getValue(xsDataProcIntegration.getRotationAxisZ(), -1.0)
        fBeamVectorX       = self.getValue(xsDataProcIntegration.getBeamVectorX(), -1.0)
        fBeamVectorY       = self.getValue(xsDataProcIntegration.getBeamVectorY(), -1.0)
        fBeamVectorZ       = self.getValue(xsDataProcIntegration.getBeamVectorZ(), -1.0)
        fCellA             = self.getValue(xsDataProcIntegration.getCell_a(), -1.0)
        fCellB             = self.getValue(xsDataProcIntegration.getCell_b(), -1.0)
        fCellC             = self.getValue(xsDataProcIntegration.getCell_c(), -1.0)
        fCellAlpha         = self.getValue(xsDataProcIntegration.getCell_alpha(), -1.0)
        fCellBeta          = self.getValue(xsDataProcIntegration.getCell_beta(), -1.0)
        fCellGamma         = self.getValue(xsDataProcIntegration.getCell_gamma(), -1.0)
        bAnomalous         = self.getValue(xsDataProcIntegration.getAnomalous(), False)
        iDataCollectionId = _xsDataAutoProcIntegrationContainer.getImage().getDataCollectionId()        
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeAutoProcIntegration(
                in0 = iAutoProcProgramId, \
                in1 = iStartImageNumber, \
                in2 = iEndImageNumber, \
                in3 = fRefinedDetectorDistance, \
                in4 = fRefinedXbeam, \
                in5 = fRefinedYbeam, \
                in6 = fRotationAxisX, \
                in7 = fRotationAxisY, \
                in8 = fRotationAxisZ, \
                in9 = fBeamVectorX, \
                in10 = fBeamVectorY, \
                in11 = fBeamVectorZ, \
                in12 = fCellA, \
                in13 = fCellB, \
                in14 = fCellC, \
                in15 = fCellAlpha, \
                in16 = fCellBeta, \
                in17 = fCellGamma, \
                in18 = recordTimeStamp, \
                in19 = bAnomalous, \
                in20 = iDataCollectionId \
                )
        self.DEBUG("AutoProcProgramIntegrationId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


    def storeAutoProc(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProc):
        """Creates an entry in the ISPyB AutoProc table"""
        iAutoProcProgramId = self.iAutoProcProgramId
        strSpaceGroup = self.getValue(_xsDataAutoProc.getSpaceGroup(), "")
        fRefinedCellA = self.getValue(_xsDataAutoProc.getRefinedCell_a(), -1)
        fRefinedCellB = self.getValue(_xsDataAutoProc.getRefinedCell_b(), -1)
        fRefinedCellC = self.getValue(_xsDataAutoProc.getRefinedCell_c(), -1)
        fRefinedCellAlpha =self.getValue( _xsDataAutoProc.getRefinedCell_alpha(), -1)
        fRefinedCellBeta = self.getValue(_xsDataAutoProc.getRefinedCell_beta(), -1)
        fRefinedCellGamma = self.getValue(_xsDataAutoProc.getRefinedCell_gamma(), -1)
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcId = _clientToolsForAutoprocessingWebService.service.storeAutoProc(
                in0 = iAutoProcProgramId, \
                in1 = strSpaceGroup, \
                in2 = fRefinedCellA, \
                in3 = fRefinedCellB, \
                in4 = fRefinedCellC, \
                in5 = fRefinedCellAlpha, \
                in6 = fRefinedCellBeta, \
                in7 = fRefinedCellGamma, \
                in8 = recordTimeStamp \
                )
        self.DEBUG("AutoProcId: %r" % iAutoProcId)
        return iAutoProcId
    
    
    def storeAutoProcScaling(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScaling):
        """Creates an entry in the ISPyB AutoProcScaling table"""
        iAutoProcId = self.iAutoProcId
        recordTimeStamp = self.getDateValue(_xsDataAutoProcScaling.getRecordTimeStamp(), "%Y-%m-%d %H:%M:%S", DateTime(datetime.datetime.now()))
        iAutoProcScalingId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScaling(
                in0 = iAutoProcId, \
                in1 = recordTimeStamp \
                )
        self.DEBUG("AutoProcScalingId: %r" % iAutoProcScalingId)
        return iAutoProcScalingId
        
    
    
    def storeAutoProcScalingStatistics(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScalingStatistics):
        """Creates an entry in the ISPyB AutoProcScalingStatistics table"""
        strScalingStatisticsType = _xsDataAutoProcScalingStatistics.getScalingStatisticsType()
        strComments = ""
        fResolutionLimitLow = self.getValue(_xsDataAutoProcScalingStatistics.getResolutionLimitLow(), -1.0)
        fResolutionLimitHigh = self.getValue(_xsDataAutoProcScalingStatistics.getResolutionLimitHigh(), -1.0)
        fRmerge = self.getValue(_xsDataAutoProcScalingStatistics.getRMerge(), -1.0)
        fRmeasWithinIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRmeasWithinIplusIminus(), -1.0)
        fRmeasAllIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRmeasAllIplusIminus(), -1.0)
        fRpimWithinIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRpimWithinIplusIminus(), -1.0)
        fRpimAllIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRpimAllIplusIminus(), -1.0)
        fFractionalPartialBias = self.getValue(_xsDataAutoProcScalingStatistics.getFractionalPartialBias(), -1.0)
        iNtotalObservations = int(self.getValue(_xsDataAutoProcScalingStatistics.getNTotalObservations(), 0))
        iNtotalUniqueObservations = self.getValue(_xsDataAutoProcScalingStatistics.getNtotalUniqueObservations(), 0)
        fMeanIoverSigI = self.getValue(_xsDataAutoProcScalingStatistics.getMeanIOverSigI(), -1.0)
        fCompleteness = self.getValue(_xsDataAutoProcScalingStatistics.getCompleteness(), -1.0)
        fMultiplicity = self.getValue(_xsDataAutoProcScalingStatistics.getMultiplicity(), -1.0)
        fAnomalousCompleteness = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalousCompleteness(), -1.0)
        fAnomalousMultiplicity = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalousMultiplicity(), -1.0)
        recordTimeStamp = DateTime(datetime.datetime.now())
        bAnomalous = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalous(), False)
        iAutoProcScalingId = self.iAutoProcScalingId
        iAutoProcScalingStatisticsId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScalingStatistic(
                in0 = strScalingStatisticsType, \
                in1 = strComments, \
                in2 = fResolutionLimitLow, \
                in3 = fResolutionLimitHigh, \
                in4 = fRmerge, \
                in5 = fRmeasWithinIplusIminus, \
                in6 = fRmeasAllIplusIminus, \
                in7 = fRpimWithinIplusIminus, \
                in8 = fRpimAllIplusIminus, \
                in9 = fFractionalPartialBias, \
                in10 = iNtotalObservations, \
                in11 = iNtotalUniqueObservations, \
                in12 = fMeanIoverSigI, \
                in13 = fCompleteness, \
                in14 = fMultiplicity, \
                in15 = fAnomalousCompleteness, \
                in16 = fAnomalousMultiplicity, \
                in17 = recordTimeStamp, \
                in18 = bAnomalous, \
                in19 = iAutoProcScalingId \
                )
        self.DEBUG("AutoProcScalingStatisticsId: %r" % iAutoProcScalingStatisticsId)
        return iAutoProcScalingStatisticsId


    def storeAutoProcScaling_has_IntId(self, _clientToolsForAutoprocessingWebService):
        """Creates an entry in the ISPyB storeAutoProcScaling_has_IntId table"""
        iAutoProcIntegrationId = self.iAutoProcIntegrationId
        iAutoProcScalingId = self.iAutoProcScalingId
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcScaling_has_intId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScalingHasInt(                                                                                                          
                in0 = iAutoProcIntegrationId, \
                in1 = iAutoProcScalingId, \
                in2 = recordTimeStamp \
                )
        self.DEBUG("AutoProcScaling_has_IntId: %r" % iAutoProcScaling_has_intId)
        return iAutoProcScaling_has_intId
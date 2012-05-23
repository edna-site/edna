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

from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc


class EDPluginISPyBStoreAutoProcv1_4(EDPluginExec):
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
            self.ERROR("EDPluginISPyBStoreAutoProcv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.process")
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
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.postProcess")
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
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.storeAutoProcProgram")
        strProcessingCommandLine = self.getValue(_xsDataAutoProcProgram.getProcessingCommandLine(), None)
        strProcessingPrograms    = self.getValue(_xsDataAutoProcProgram.getProcessingPrograms(), None)
        bProcessingStatus        = self.getValue(_xsDataAutoProcProgram.getProcessingStatus(), True)
        strProcessingMessage     = self.getValue(_xsDataAutoProcProgram.getProcessingMessage(), None)
        processingStartTime      = self.getDateValue(_xsDataAutoProcProgram.getProcessingStartTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        processingEndTime        = self.getDateValue(_xsDataAutoProcProgram.getProcessingEndTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        strProcessingEnvironment = self.getValue(_xsDataAutoProcProgram.getProcessingEnvironment(), None)
        recordTimeStamp          = self.getDateValue(None,  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        iAutoProcProgramId = _clientToolsForAutoprocessingWebService.service.storeAutoProcProgram(
                strProcessingCommandLine, \
                strProcessingPrograms, \
                bProcessingStatus, \
                strProcessingMessage, \
                processingStartTime, \
                processingEndTime, \
                strProcessingEnvironment, \
                recordTimeStamp
                )
        self.DEBUG("AutoProcProgramId: %r" % iAutoProcProgramId)
        return iAutoProcProgramId


    def storeAutoProcProgramAttachment(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgramAttachment):
        """Creates an entry in the ISPyB AutoProcProgramAttachment table"""
        iAutoProcProgramId = self.iAutoProcProgramId
        strFileType = self.getValue(_xsDataAutoProcProgramAttachment.getFileType(), None)
        strFileName = self.getValue(_xsDataAutoProcProgramAttachment.getFileName(), None)
        strFilePath = self.getValue(_xsDataAutoProcProgramAttachment.getFilePath(), None)
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcProgramAttachmentId = _clientToolsForAutoprocessingWebService.service.storeAutoProcProgramAttachment(
                strFileType, \
                strFileName, \
                strFilePath, \
                recordTimeStamp, \
                iAutoProcProgramId
                )
        self.DEBUG("AutoProcProgramAttachmentId: %r" % iAutoProcProgramAttachmentId)
        return iAutoProcProgramAttachmentId


    def storeAutoProcIntegration(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcIntegrationContainer):
        """Creates an entry in the ISPyB AutoProcIntegration table"""
        xsDataProcIntegration = _xsDataAutoProcIntegrationContainer.getAutoProcIntegration()
        iAutoProcProgramId = self.iAutoProcProgramId
        iStartImageNumber  = self.getValue(xsDataProcIntegration.getStartImageNumber(), None)
        iEndImageNumber    = self.getValue(xsDataProcIntegration.getEndImageNumber(), None)
        fRefinedDetectorDistance = self.getValue(xsDataProcIntegration.getRefinedDetectorDistance(), None)
        fRefinedXbeam      = self.getValue(xsDataProcIntegration.getRefinedXbeam(), None)
        fRefinedYbeam      = self.getValue(xsDataProcIntegration.getRefinedYbeam(), None)
        fRotationAxisX     = self.getValue(xsDataProcIntegration.getRotationAxisX(), None)
        fRotationAxisY     = self.getValue(xsDataProcIntegration.getRotationAxisY(), None)
        fRotationAxisZ     = self.getValue(xsDataProcIntegration.getRotationAxisZ(), None)
        fBeamVectorX       = self.getValue(xsDataProcIntegration.getBeamVectorX(), None)
        fBeamVectorY       = self.getValue(xsDataProcIntegration.getBeamVectorY(), None)
        fBeamVectorZ       = self.getValue(xsDataProcIntegration.getBeamVectorZ(), None)
        fCellA             = self.getValue(xsDataProcIntegration.getCell_a(), None)
        fCellB             = self.getValue(xsDataProcIntegration.getCell_b(), None)
        fCellC             = self.getValue(xsDataProcIntegration.getCell_c(), None)
        fCellAlpha         = self.getValue(xsDataProcIntegration.getCell_alpha(), None)
        fCellBeta          = self.getValue(xsDataProcIntegration.getCell_beta(), None)
        fCellGamma         = self.getValue(xsDataProcIntegration.getCell_gamma(), None)
        bAnomalous         = self.getValue(xsDataProcIntegration.getAnomalous(), False)
        iDataCollectionId = _xsDataAutoProcIntegrationContainer.getImage().getDataCollectionId()        
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeAutoProcIntegration(
                iAutoProcProgramId, \
                iStartImageNumber, \
                iEndImageNumber, \
                fRefinedDetectorDistance, \
                fRefinedXbeam, \
                fRefinedYbeam, \
                fRotationAxisX, \
                fRotationAxisY, \
                fRotationAxisZ, \
                fBeamVectorX, \
                fBeamVectorY, \
                fBeamVectorZ, \
                fCellA, \
                fCellB, \
                fCellC, \
                fCellAlpha, \
                fCellBeta, \
                fCellGamma, \
                recordTimeStamp, \
                bAnomalous, \
                iDataCollectionId \
                )
        self.DEBUG("AutoProcProgramIntegrationId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


    def storeAutoProc(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProc):
        """Creates an entry in the ISPyB AutoProc table"""
        iAutoProcProgramId = self.iAutoProcProgramId
        strSpaceGroup = self.getValue(_xsDataAutoProc.getSpaceGroup(), None)
        fRefinedCellA = self.getValue(_xsDataAutoProc.getRefinedCell_a(), None)
        fRefinedCellB = self.getValue(_xsDataAutoProc.getRefinedCell_b(), None)
        fRefinedCellC = self.getValue(_xsDataAutoProc.getRefinedCell_c(), None)
        fRefinedCellAlpha =self.getValue( _xsDataAutoProc.getRefinedCell_alpha(), None)
        fRefinedCellBeta = self.getValue(_xsDataAutoProc.getRefinedCell_beta(), None)
        fRefinedCellGamma = self.getValue(_xsDataAutoProc.getRefinedCell_gamma(), None)
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcId = _clientToolsForAutoprocessingWebService.service.storeAutoProc(
                iAutoProcProgramId, \
                strSpaceGroup, \
                fRefinedCellA, \
                fRefinedCellB, \
                fRefinedCellC, \
                fRefinedCellAlpha, \
                fRefinedCellBeta, \
                fRefinedCellGamma, \
                recordTimeStamp \
                )
        self.DEBUG("AutoProcId: %r" % iAutoProcId)
        return iAutoProcId
    
    
    def storeAutoProcScaling(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScaling):
        """Creates an entry in the ISPyB AutoProcScaling table"""
        iAutoProcId = self.iAutoProcId
        recordTimeStamp = self.getDateValue(_xsDataAutoProcScaling.getRecordTimeStamp(), "%Y-%m-%d %H:%M:%S", DateTime(datetime.datetime.now()))
        iAutoProcScalingId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScaling(
                iAutoProcId, \
                recordTimeStamp \
                )
        self.DEBUG("AutoProcScalingId: %r" % iAutoProcScalingId)
        return iAutoProcScalingId
        
    
    
    def storeAutoProcScalingStatistics(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScalingStatistics):
        """Creates an entry in the ISPyB AutoProcScalingStatistics table"""
        strScalingStatisticsType = _xsDataAutoProcScalingStatistics.getScalingStatisticsType()
        strComments = ""
        fResolutionLimitLow = self.getValue(_xsDataAutoProcScalingStatistics.getResolutionLimitLow(), None)
        fResolutionLimitHigh = self.getValue(_xsDataAutoProcScalingStatistics.getResolutionLimitHigh(), None)
        fRmerge = self.getValue(_xsDataAutoProcScalingStatistics.getRMerge(), None)
        fRmeasWithinIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRmeasWithinIplusIminus(), None)
        fRmeasAllIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRmeasAllIplusIminus(), None)
        fRpimWithinIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRpimWithinIplusIminus(), None)
        fRpimAllIplusIminus = self.getValue(_xsDataAutoProcScalingStatistics.getRpimAllIplusIminus(), None)
        fFractionalPartialBias = self.getValue(_xsDataAutoProcScalingStatistics.getFractionalPartialBias(), None)
        iNtotalObservations = self.getValue(_xsDataAutoProcScalingStatistics.getNTotalObservations(), None)
        iNtotalUniqueObservations = self.getValue(_xsDataAutoProcScalingStatistics.getNtotalUniqueObservations(), None)
        fMeanIoverSigI = self.getValue(_xsDataAutoProcScalingStatistics.getMeanIOverSigI(), None)
        fCompleteness = self.getValue(_xsDataAutoProcScalingStatistics.getCompleteness(), None)
        fMultiplicity = self.getValue(_xsDataAutoProcScalingStatistics.getMultiplicity(), None)
        fAnomalousCompleteness = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalousCompleteness(), None)
        fAnomalousMultiplicity = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalousMultiplicity(), None)
        recordTimeStamp = DateTime(datetime.datetime.now())
        bAnomalous = self.getValue(_xsDataAutoProcScalingStatistics.getAnomalous(), False)
        iAutoProcScalingId = self.iAutoProcScalingId
        iAutoProcScalingStatisticsId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScalingStatistics(
                strScalingStatisticsType, \
                strComments, \
                fResolutionLimitLow, \
                fResolutionLimitHigh, \
                fRmerge, \
                fRmeasWithinIplusIminus, \
                fRmeasAllIplusIminus, \
                fRpimWithinIplusIminus, \
                fRpimAllIplusIminus, \
                fFractionalPartialBias, \
                iNtotalObservations, \
                iNtotalUniqueObservations, \
                fMeanIoverSigI, \
                fCompleteness, \
                fMultiplicity, \
                fAnomalousCompleteness, \
                fAnomalousMultiplicity, \
                recordTimeStamp, \
                bAnomalous, \
                iAutoProcScalingId \
                )
        self.DEBUG("AutoProcScalingStatisticsId: %r" % iAutoProcScalingStatisticsId)
        return iAutoProcScalingStatisticsId


    def storeAutoProcScaling_has_IntId(self, _clientToolsForAutoprocessingWebService):
        """Creates an entry in the ISPyB storeAutoProcScaling_has_IntId table"""
        iAutoProcIntegrationId = self.iAutoProcIntegrationId
        iAutoProcScalingId = self.iAutoProcScalingId
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcScaling_has_intId = _clientToolsForAutoprocessingWebService.service.storeAutoProcScalingHasInt(                                                                                                          
                iAutoProcIntegrationId, \
                iAutoProcScalingId, \
                recordTimeStamp \
                )
        self.DEBUG("AutoProcScaling_has_IntId: %r" % iAutoProcScaling_has_intId)
        return iAutoProcScaling_has_intId
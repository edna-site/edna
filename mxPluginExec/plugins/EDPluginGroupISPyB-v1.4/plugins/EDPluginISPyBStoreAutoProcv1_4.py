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
__status__ = "production"

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
        self.iAutoProcScalingHasIntId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreAutoProcv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.config.get("toolsForAutoprocessingWebServiceWsdl")
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
        self.iAutoProcProgramId = self.storeOrUpdateAutoProcProgram(clientToolsForAutoprocessingWebService, xsDataAutoProcProgram)
        if self.iAutoProcProgramId is None:
            self.ERROR("Couldn't create entry for AutoProcProgram in ISPyB!")
            self.setFailure()
            self.bContinue = False
        else:
            listAutoProcProgramAttachment = xsDataAutoProcContainer.getAutoProcProgramContainer().getAutoProcProgramAttachment()
            for xsDataAutoProcProgramAttachment in listAutoProcProgramAttachment:
                self.storeOrUpdateAutoProcProgramAttachment(clientToolsForAutoprocessingWebService, xsDataAutoProcProgramAttachment)
            if (xsDataAutoProcProgram.getProcessingStatus() == False) or (xsDataAutoProcScalingContainer is None):
                self.bContinue = False
        if self.bContinue:
            # AutoProcIntegration
            xsDataAutoProcIntegrationContainer = xsDataAutoProcScalingContainer.getAutoProcIntegrationContainer()
            self.iAutoProcIntegrationId = self.storeOrUpdateAutoProcIntegration(clientToolsForAutoprocessingWebService, xsDataAutoProcIntegrationContainer)
            if self.iAutoProcIntegrationId is None:
                self.WARNING("Couldn't create entry for AutoProcIntegration in ISPyB!")
        if self.bContinue:
            # AutoProc
            xsDataAutoProc = xsDataAutoProcContainer.getAutoProc()
            self.iAutoProcId = self.storeOrUpdateAutoProc(clientToolsForAutoprocessingWebService, xsDataAutoProc)
            if self.iAutoProcId is None:
                self.ERROR("Couldn't create entry for AutoProc in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScaling
            xsDataAutoProcScaling = xsDataAutoProcScalingContainer.getAutoProcScaling()
            self.iAutoProcScalingId = self.storeOrUpdateAutoProcScaling(clientToolsForAutoprocessingWebService, xsDataAutoProcScaling)
            if self.iAutoProcScalingId is None:
                self.ERROR("Couldn't create entry for AutoProcScaling in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScalingHasIntId
            self.iAutoProcScalingHasIntId = self.storeOrUpdateAutoProcScalingHasIntId(clientToolsForAutoprocessingWebService)
            if self.iAutoProcScalingHasIntId is None:
                self.ERROR("Couldn't create entry for AutoProcScalingHasIntId in ISPyB!")
                self.setFailure()
                self.bContinue = False
        if self.bContinue:
            # AutoProcScalingStatistics
            for xsDataAutoProcScalingStatistics in xsDataAutoProcScalingContainer.getAutoProcScalingStatistics():
                iAutoProcScalingStatisticsId = self.storeOrUpdateAutoProcScalingStatistics(clientToolsForAutoprocessingWebService, xsDataAutoProcScalingStatistics)
                if iAutoProcScalingStatisticsId is None:
                    self.ERROR("Couldn't create entry for AutoProcScalingStatistics in ISPyB!")
                    self.setFailure()
                    self.bContinue = False
            


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.postProcess")
        xsDataResultStoreAutoProc = XSDataResultStoreAutoProc()
        if self.iAutoProcId is not None:
            xsDataResultStoreAutoProc.setAutoProcId(XSDataInteger(self.iAutoProcId))
        self.setDataOutput(xsDataResultStoreAutoProc)


    def getXSValue(self, _xsData, _oDefaultValue=None, _iMaxStringLength=255):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _xsData
        if type(oReturnValue) == bool:
            if oReturnValue:
                oReturnValue = "1"
            else:
                oReturnValue = "0"
        elif (type(oReturnValue) == str) or (type(oReturnValue) == unicode):
            if len(oReturnValue) > _iMaxStringLength:
                strOldString = oReturnValue
                oReturnValue = oReturnValue[0:_iMaxStringLength-3]+"..."
                self.warning("String truncated to %d characters for ISPyB! Original string: %s" % (_iMaxStringLength, strOldString))
                self.warning("Truncated string: %s" % oReturnValue)
        return oReturnValue

    
    def getDateValue(self, _strValue, _strFormat, _oDefaultValue):
        if _strValue is None or _strValue == "None":
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
        return oReturnValue
    

    def storeOrUpdateAutoProcProgram(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgram):
        """Creates an entry in the ISPyB AutoProcProgram table"""
        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.storeOrUpdateAutoProcProgram")
        iAutoProcProgramId       = self.getXSValue(_xsDataAutoProcProgram.getAutoProcProgramId())
        strProcessingCommandLine = self.getXSValue(_xsDataAutoProcProgram.getProcessingCommandLine())
        strProcessingPrograms    = self.getXSValue(_xsDataAutoProcProgram.getProcessingPrograms())
        bProcessingStatus        = self.getXSValue(_xsDataAutoProcProgram.getProcessingStatus(), True)
        strProcessingMessage     = self.getXSValue(_xsDataAutoProcProgram.getProcessingMessage())
        processingStartTime      = self.getDateValue(_xsDataAutoProcProgram.getProcessingStartTime(),  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        processingEndTime        = self.getDateValue(_xsDataAutoProcProgram.getProcessingEndTime(),    "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        strProcessingEnvironment = self.getXSValue(_xsDataAutoProcProgram.getProcessingEnvironment())
        recordTimeStamp          = self.getDateValue(None,  "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
        iAutoProcProgramId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcProgram(
                arg0 = iAutoProcProgramId, \
                processingCommandLine = strProcessingCommandLine, \
                processingPrograms = strProcessingPrograms, \
                processingStatus = bProcessingStatus, \
                processingMessage = strProcessingMessage, \
                processingStartTime = processingStartTime, \
                processingEndTime = processingEndTime, \
                processingEnvironment = strProcessingEnvironment, \
                recordTimeStamp = recordTimeStamp
                )
        self.DEBUG("AutoProcProgramId: %r" % iAutoProcProgramId)
        return iAutoProcProgramId


    def storeOrUpdateAutoProcProgramAttachment(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgramAttachment):
        """Creates an entry in the ISPyB AutoProcProgramAttachment table"""
        iAutoProcProgramAttachmentId = self.getXSValue(_xsDataAutoProcProgramAttachment.getAutoProcProgramAttachmentId())
        strFileType = self.getXSValue(_xsDataAutoProcProgramAttachment.getFileType())
        strFileName = self.getXSValue(_xsDataAutoProcProgramAttachment.getFileName())
        strFilePath = self.getXSValue(_xsDataAutoProcProgramAttachment.getFilePath())
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcProgramId = self.iAutoProcProgramId
        iAutoProcProgramAttachmentId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcProgramAttachment(
                arg0 = iAutoProcProgramAttachmentId, \
                fileType = strFileType, \
                fileName = strFileName, \
                filePath = strFilePath, \
                recordTimeStamp = recordTimeStamp, \
                autoProcProgramId = iAutoProcProgramId
                )
        self.DEBUG("AutoProcProgramAttachmentId: %r" % iAutoProcProgramAttachmentId)
        return iAutoProcProgramAttachmentId


    def storeOrUpdateAutoProcIntegration(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcIntegrationContainer):
        """Creates an entry in the ISPyB AutoProcIntegration table"""
        xsDataProcIntegration = _xsDataAutoProcIntegrationContainer.getAutoProcIntegration()
        iAutoProcIntegrationId = self.getXSValue(xsDataProcIntegration.getAutoProcIntegrationId())
        iAutoProcProgramId = self.iAutoProcProgramId
        iStartImageNumber  = self.getXSValue(xsDataProcIntegration.getStartImageNumber())
        iEndImageNumber    = self.getXSValue(xsDataProcIntegration.getEndImageNumber())
        fRefinedDetectorDistance = self.getXSValue(xsDataProcIntegration.getRefinedDetectorDistance())
        fRefinedXbeam      = self.getXSValue(xsDataProcIntegration.getRefinedXbeam())
        fRefinedYbeam      = self.getXSValue(xsDataProcIntegration.getRefinedYbeam())
        fRotationAxisX     = self.getXSValue(xsDataProcIntegration.getRotationAxisX())
        fRotationAxisY     = self.getXSValue(xsDataProcIntegration.getRotationAxisY())
        fRotationAxisZ     = self.getXSValue(xsDataProcIntegration.getRotationAxisZ())
        fBeamVectorX       = self.getXSValue(xsDataProcIntegration.getBeamVectorX())
        fBeamVectorY       = self.getXSValue(xsDataProcIntegration.getBeamVectorY())
        fBeamVectorZ       = self.getXSValue(xsDataProcIntegration.getBeamVectorZ())
        fCellA             = self.getXSValue(xsDataProcIntegration.getCell_a())
        fCellB             = self.getXSValue(xsDataProcIntegration.getCell_b())
        fCellC             = self.getXSValue(xsDataProcIntegration.getCell_c())
        fCellAlpha         = self.getXSValue(xsDataProcIntegration.getCell_alpha())
        fCellBeta          = self.getXSValue(xsDataProcIntegration.getCell_beta())
        fCellGamma         = self.getXSValue(xsDataProcIntegration.getCell_gamma())
        bAnomalous         = self.getXSValue(xsDataProcIntegration.getAnomalous(), False)
        iDataCollectionId = _xsDataAutoProcIntegrationContainer.getImage().getDataCollectionId()        
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcIntegration(
                arg0 = iAutoProcIntegrationId, \
                autoProcProgramId = iAutoProcProgramId, \
                startImageNumber = iStartImageNumber, \
                endImageNumber = iEndImageNumber, \
                refinedDetectorDistance = fRefinedDetectorDistance, \
                refinedXbeam = fRefinedXbeam, \
                refinedYbeam = fRefinedYbeam, \
                rotationAxisX = fRotationAxisX, \
                rotationAxisY = fRotationAxisY, \
                rotationAxisZ = fRotationAxisZ, \
                beamVectorX = fBeamVectorX, \
                beamVectorY = fBeamVectorY, \
                beamVectorZ = fBeamVectorZ, \
                cellA = fCellA, \
                cellB = fCellB, \
                cellC = fCellC, \
                cellAlpha = fCellAlpha, \
                cellBeta = fCellBeta, \
                cellGamma = fCellGamma, \
                recordTimeStamp= recordTimeStamp, \
                anomalous = bAnomalous, \
                dataCollectionId = iDataCollectionId \
                )
        self.DEBUG("AutoProcProgramIntegrationId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


    def storeOrUpdateAutoProc(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProc):
        """Creates an entry in the ISPyB AutoProc table"""
        iAutoProcId = self.getXSValue(_xsDataAutoProc.getAutoProcId())
        iAutoProcProgramId = self.iAutoProcProgramId
        strSpaceGroup = self.getXSValue(_xsDataAutoProc.getSpaceGroup())
        fRefinedCellA = self.getXSValue(_xsDataAutoProc.getRefinedCell_a())
        fRefinedCellB = self.getXSValue(_xsDataAutoProc.getRefinedCell_b())
        fRefinedCellC = self.getXSValue(_xsDataAutoProc.getRefinedCell_c())
        fRefinedCellAlpha =self.getXSValue( _xsDataAutoProc.getRefinedCell_alpha())
        fRefinedCellBeta = self.getXSValue(_xsDataAutoProc.getRefinedCell_beta())
        fRefinedCellGamma = self.getXSValue(_xsDataAutoProc.getRefinedCell_gamma())
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProc(
                arg0 = iAutoProcId, \
                autoProcProgramId = iAutoProcProgramId, \
                spaceGroup = strSpaceGroup, \
                refinedCellA = fRefinedCellA, \
                refinedCellB = fRefinedCellB, \
                refinedCellC = fRefinedCellC, \
                refinedCellAlpha = fRefinedCellAlpha, \
                refinedCellBeta = fRefinedCellBeta, \
                refinedCellGamma = fRefinedCellGamma, \
                recordTimeStamp = recordTimeStamp \
                )
        self.DEBUG("AutoProcId: %r" % iAutoProcId)
        return iAutoProcId
    
    
    def storeOrUpdateAutoProcScaling(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScaling):
        """Creates an entry in the ISPyB AutoProcScaling table"""
        iAutoProcScalingId = self.getXSValue(_xsDataAutoProcScaling.getAutoProcScalingId())
        iAutoProcId = self.iAutoProcId
        recordTimeStamp = self.getDateValue(_xsDataAutoProcScaling.getRecordTimeStamp(), "%Y-%m-%d %H:%M:%S", DateTime(datetime.datetime.now()))
        iAutoProcScalingId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcScaling(
                arg0 = iAutoProcScalingId, \
                autoProcId = iAutoProcId, \
                recordTimeStamp = recordTimeStamp \
                )
        self.DEBUG("AutoProcScalingId: %r" % iAutoProcScalingId)
        return iAutoProcScalingId
        
    
    
    def storeOrUpdateAutoProcScalingStatistics(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcScalingStatistics):
        """Creates an entry in the ISPyB AutoProcScalingStatistics table"""
        iAutoProcScalingStatisticsId = self.getXSValue(_xsDataAutoProcScalingStatistics.getAutoProcScalingStatisticsId())
        strScalingStatisticsType = self.getXSValue(_xsDataAutoProcScalingStatistics.getScalingStatisticsType())
        strComments = self.getXSValue(_xsDataAutoProcScalingStatistics.getComments())
        fResolutionLimitLow = self.getXSValue(_xsDataAutoProcScalingStatistics.getResolutionLimitLow())
        fResolutionLimitHigh = self.getXSValue(_xsDataAutoProcScalingStatistics.getResolutionLimitHigh())
        fRmerge = self.getXSValue(_xsDataAutoProcScalingStatistics.getRMerge())
        fRmeasWithinIplusIminus = self.getXSValue(_xsDataAutoProcScalingStatistics.getRmeasWithinIplusIminus())
        fRmeasAllIplusIminus = self.getXSValue(_xsDataAutoProcScalingStatistics.getRmeasAllIplusIminus())
        fRpimWithinIplusIminus = self.getXSValue(_xsDataAutoProcScalingStatistics.getRpimWithinIplusIminus())
        fRpimAllIplusIminus = self.getXSValue(_xsDataAutoProcScalingStatistics.getRpimAllIplusIminus())
        fFractionalPartialBias = self.getXSValue(_xsDataAutoProcScalingStatistics.getFractionalPartialBias())
        iNtotalObservations = self.getXSValue(_xsDataAutoProcScalingStatistics.getNTotalObservations())
        iNtotalUniqueObservations = self.getXSValue(_xsDataAutoProcScalingStatistics.getNtotalUniqueObservations())
        fMeanIoverSigI = self.getXSValue(_xsDataAutoProcScalingStatistics.getMeanIOverSigI())
        fCompleteness = self.getXSValue(_xsDataAutoProcScalingStatistics.getCompleteness())
        fMultiplicity = self.getXSValue(_xsDataAutoProcScalingStatistics.getMultiplicity())
        fAnomalousCompleteness = self.getXSValue(_xsDataAutoProcScalingStatistics.getAnomalousCompleteness())
        fAnomalousMultiplicity = self.getXSValue(_xsDataAutoProcScalingStatistics.getAnomalousMultiplicity())
        recordTimeStamp = DateTime(datetime.datetime.now())
        bAnomalous = self.getXSValue(_xsDataAutoProcScalingStatistics.getAnomalous(), False)
        iAutoProcScalingId = self.iAutoProcScalingId
        fCcHalf = self.getXSValue(_xsDataAutoProcScalingStatistics.getCcHalf())
        iAutoProcScalingStatisticsId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcScalingStatistics(
                arg0 = iAutoProcScalingStatisticsId, \
                scalingStatisticsType = strScalingStatisticsType, \
                comments = strComments, \
                resolutionLimitLow = fResolutionLimitLow, \
                resolutionLimitHigh = fResolutionLimitHigh, \
                rmerge = fRmerge, \
                rmeasWithinIplusIminus = fRmeasWithinIplusIminus, \
                rmeasAllIplusIminus = fRmeasAllIplusIminus, \
                rpimWithinIplusIminus = fRpimWithinIplusIminus, \
                rpimAllIplusIminus = fRpimAllIplusIminus, \
                fractionalPartialBias = fFractionalPartialBias, \
                nTotalObservations = iNtotalObservations, \
                nTotalUniqueObservations = iNtotalUniqueObservations, \
                meanIoverSigI = fMeanIoverSigI, \
                completeness = fCompleteness, \
                multiplicity = fMultiplicity, \
                anomalousCompleteness = fAnomalousCompleteness, \
                anomalousMultiplicity = fAnomalousMultiplicity, \
                recordTimeStamp = recordTimeStamp, \
                anomalous = bAnomalous, \
                autoProcScalingId = iAutoProcScalingId, \
                ccHalf = fCcHalf, \
                )
        self.DEBUG("AutoProcScalingStatisticsId: %r" % iAutoProcScalingStatisticsId)
        return iAutoProcScalingStatisticsId


    def storeOrUpdateAutoProcScalingHasIntId(self, _clientToolsForAutoprocessingWebService):
        """Creates an entry in the ISPyB storeOrUpdateAutoProcScalingHasIntId table"""
        iAutoProcIntegrationId = self.iAutoProcIntegrationId
        iAutoProcScalingId = self.iAutoProcScalingId
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcScalingHasIntId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcScalingHasInt(
                arg0 = None, \
                autoProcIntegrationId = iAutoProcIntegrationId, \
                autoProcScalingId = iAutoProcScalingId, \
                recordTimeStamp = recordTimeStamp \
                )
        self.DEBUG("AutoProcScalingHasIntId: %r" % iAutoProcScalingHasIntId)
        return iAutoProcScalingHasIntId

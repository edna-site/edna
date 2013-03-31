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

from XSDataISPyBv1_4 import XSDataInputStoreAutoProcStatus
from XSDataISPyBv1_4 import XSDataResultStoreAutoProcStatus


class EDPluginISPyBStoreAutoProcStatusv1_4(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreAutoProcStatus)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForAutoprocessingWebServiceWsdl = None
        self.iAutoProcIntegrationId = None
        self.iAutoProcStatusId = None
        
        
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreAutoProcStatusv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreAutoProcStatusv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.config.get("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreAutoProcStatusv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcStatusv1_4.process")
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService)
        xsDataInputStoreAutoProcStatus = self.getDataInput()
        if xsDataInputStoreAutoProcStatus.dataCollectionId is not None:
            iDataCollectionId = xsDataInputStoreAutoProcStatus.dataCollectionId
        if xsDataInputStoreAutoProcStatus.autoProcIntegrationId is not None:
            self.iAutoProcIntegrationId = xsDataInputStoreAutoProcStatus.autoProcIntegrationId
        if xsDataInputStoreAutoProcStatus.autoProcStatusId is not None:
            self.iAutoProcStatusId = xsDataInputStoreAutoProcStatus.autoProcStatusId
        # If autoProcIntegrationId is not given a dataCollectionId must be present:
        if (self.iAutoProcIntegrationId is None) and (iDataCollectionId is None):
            strErrorMessage = "Either data collection id or auto proc integration id must be given as input!"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
        else:
            if self.iAutoProcIntegrationId is None:
                # If no autoProcessingId is given create a dummy entry in the integration table
                self.iAutoProcIntegrationId = self.storeOrUpdateAutoProcIntegration(clientToolsForAutoprocessingWebService, 
                                                                               _iDataCollectionId = iDataCollectionId)
            # Store the AutoProcStatus
            self.iAutoProcStatusId = self.storeOrUpdateAutoProcStatus(clientToolsForAutoprocessingWebService, \
                                                                 _xsDataAutoProcStatus = xsDataInputStoreAutoProcStatus.getAutoProcStatus(), \
                                                                 _iAutoProcIntegrationId = self.iAutoProcIntegrationId, \
                                                                 _iAutoProcStatusId = self.iAutoProcStatusId)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcStatusv1_4.postProcess")
        xsDataResultStoreAutoProcStatus = XSDataResultStoreAutoProcStatus()
        xsDataResultStoreAutoProcStatus.setAutoProcIntegrationId(self.iAutoProcIntegrationId)
        xsDataResultStoreAutoProcStatus.setAutoProcStatusId(self.iAutoProcStatusId)
        self.setDataOutput(xsDataResultStoreAutoProcStatus)
            
                
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
                
            
    def storeOrUpdateAutoProcIntegration(self, _clientToolsForAutoprocessingWebService, \
                                         _iAutoProcIntegrationId=None, _iDataCollectionId=None):
        """Creates or updates an entry in the ISPyB AutoProcIntegration table"""
        recordTimeStamp          = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcIntegration(
                arg0 = _iAutoProcIntegrationId, \
                recordTimeStamp= recordTimeStamp, \
                dataCollectionId = _iDataCollectionId \
                )
        self.DEBUG("AutoProcProgramIntegrationId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


    def storeOrUpdateAutoProcStatus(self, _clientToolsForAutoprocessingWebService, \
                                    _xsDataAutoProcStatus, _iAutoProcIntegrationId, _iAutoProcStatusId=None):
        """Creates or updates an entry in the ISPyB AutoProcIntegration table"""
        strStep = self.getXSValue(_xsDataAutoProcStatus.getStep())
        strStatus = self.getXSValue(_xsDataAutoProcStatus.getStatus())
        strComments = self.getXSValue(_xsDataAutoProcStatus.getComments(), _iMaxStringLength=1024)
        strBltimeStamp = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcStatus(
                arg0 = _iAutoProcStatusId, \
                autoProcIntegrationId = _iAutoProcIntegrationId, \
                step = strStep, \
                status = strStatus, \
                comments = strComments, \
                bltimeStamp = strBltimeStamp, \
                )
        self.DEBUG("AutoProcProgramStatusId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


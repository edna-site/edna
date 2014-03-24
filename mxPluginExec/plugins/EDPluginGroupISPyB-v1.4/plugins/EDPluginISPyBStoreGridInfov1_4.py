#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2014 European Synchrotron Radiation Facility
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
__date__ = "20140324"
__status__ = "production"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBStoreGridInfo
from XSDataISPyBv1_4 import XSDataResultISPyBStoreGridInfo


class EDPluginISPyBStoreGridInfov1_4(EDPluginExec):
    """
    Plugin to store workflow status in an ISPyB database using web services
    """

    def __init__(self):
        """
        Init plugin
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBStoreGridInfo)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.iGridInfoId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreGridInfov1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreGridInfov1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreGridInfov1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
                
    def getXSValue(self, _xsData, _oDefaultValue=None, _iMaxStringLength=255):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _xsData.value
        if type(oReturnValue) == bool:
            if oReturnValue:
                oReturnValue = "1"
            else:
                oReturnValue = "0"
        elif (type(oReturnValue) == str) or (type(oReturnValue) == unicode):
            if len(oReturnValue) > _iMaxStringLength:
                strOldString = oReturnValue
                oReturnValue = oReturnValue[0:_iMaxStringLength - 3] + "..."
                self.warning("String truncated to %d characters for ISPyB! Original string: %s" % (_iMaxStringLength, strOldString))
                self.warning("Truncated string: %s" % oReturnValue)
        return oReturnValue

    
    def getDateValue(self, _strValue, _strFormat, _oDefaultValue):
        if _strValue is None or _strValue == "None":
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
        return oReturnValue

    def process(self, _edObject=None):
        """
        Uses ToolsForCollectionWebService for storing the workflow status
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreGridInfov1_4.process")
        # First get the image ID
        xsDataInputGridInfo = self.getDataInput()

        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        gridInfoWS3VO = clientToolsForCollectionWebService.factory.create('gridInfoWS3VO')
        gridInfoWS3VO.gridInfoId = self.getXSValue(xsDataInputGridInfo.gridInfoId)
        gridInfoWS3VO.workflowMeshId = self.getXSValue(xsDataInputGridInfo.workflowMeshId)
        gridInfoWS3VO.dx_mm = self.getXSValue(xsDataInputGridInfo.dx_mm)
        gridInfoWS3VO.dy_mm = self.getXSValue(xsDataInputGridInfo.dy_mm)
        gridInfoWS3VO.xOffset = self.getXSValue(xsDataInputGridInfo.xOffset)
        gridInfoWS3VO.yOffset = self.getXSValue(xsDataInputGridInfo.yOffset)
        gridInfoWS3VO.steps_x = self.getXSValue(xsDataInputGridInfo.steps_x)
        gridInfoWS3VO.steps_y = self.getXSValue(xsDataInputGridInfo.steps_y)
        gridInfoWS3VO.meshAngle = self.getXSValue(xsDataInputGridInfo.meshAngle)
#        print gridInfoWS3VO
        self.iGridInfoId = clientToolsForCollectionWebService.service.storeOrUpdateGridInfo(gridInfoWS3VO)
        self.DEBUG("EDPluginISPyBStoreGridInfov1_4.process: WorkflowId=%d" % self.iGridInfoId)
            
             



    def finallyProcess(self, _edObject=None):
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreGridInfov1_4.finallyProcess")
        xsDataResultISPyBStoreGridInfo = XSDataResultISPyBStoreGridInfo()
        if self.iGridInfoId is not None:
            xsDataResultISPyBStoreGridInfo.gridInfoId = XSDataInteger(self.iGridInfoId)
        self.setDataOutput(xsDataResultISPyBStoreGridInfo)

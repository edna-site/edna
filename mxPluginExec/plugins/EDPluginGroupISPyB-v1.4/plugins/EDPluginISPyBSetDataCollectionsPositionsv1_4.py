#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2013 European Synchrotron Radiation Facility
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
__date__ = "20130705"
__status__ = "production"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBSetDataCollectionsPositions
from XSDataISPyBv1_4 import XSDataResultISPyBSetDataCollectionsPositions


class EDPluginISPyBSetDataCollectionsPositionsv1_4(EDPluginExec):
    """
    Plugin to store sample position (for grid scans)
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBSetDataCollectionsPositions)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.iDataCollectionId  = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBSetDataCollectionsPositionsv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBSetDataCollectionsPositionsv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBSetDataCollectionsPositionsv1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Uses ToolsForCollectionWebService for storing the workflow status
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBSetDataCollectionsPositionsv1_4.process")
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        # Loop over all positions
        listDataCollectionPosition = []
        for xsDataDataCollectionPosition in self.dataInput.dataCollectionPosition:
            dataCollectionPosition = clientToolsForCollectionWebService.factory.create('dataCollectionPosition')
            # Get the workflow ID and status
            dataCollectionPosition.fileName = os.path.basename(xsDataDataCollectionPosition.fileName.path.value)
            dataCollectionPosition.fileLocation = os.path.dirname(xsDataDataCollectionPosition.fileName.path.value)
            dataCollectionPosition.startPosition = self.createMotorPosition3VO(clientToolsForCollectionWebService, 
                                                                               xsDataDataCollectionPosition.startPosition)
            if xsDataDataCollectionPosition.endPosition is not None:
                dataCollectionPosition.endPosition = self.createMotorPosition3VO(clientToolsForCollectionWebService, 
                                                                                 xsDataDataCollectionPosition.endPosition)
            else:
                endMotorPosition3VO = None
            listDataCollectionPosition.append(dataCollectionPosition)
        self.listDataCollectionId = clientToolsForCollectionWebService.service.setDataCollectionsPositions(
                                    listDataCollectionPosition = listDataCollectionPosition)
        self.DEBUG("EDPluginISPyBSetDataCollectionsPositionsv1_4.process: DataCollectionId=%r" % self.listDataCollectionId)
            
             



    def finallyProcess(self, _edObject=None):
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBSetDataCollectionsPositionsv1_4.finallyProcess")
        xsDataResultISPyBSetDataCollectionsPositions = XSDataResultISPyBSetDataCollectionsPositions()
        for dataCollectionId in self.listDataCollectionId:
            xsDataResultISPyBSetDataCollectionsPositions.addDataCollectionId(XSDataInteger(dataCollectionId))
        self.setDataOutput(xsDataResultISPyBSetDataCollectionsPositions)


    def createMotorPosition3VO(self, _clientToolsForCollectionWebService, _xsDataPosition):
        position3VO = _clientToolsForCollectionWebService.factory.create('motorPosition3VO')
        position3VO.gridIndexY = _xsDataPosition.gridIndexY.value
        position3VO.gridIndexZ = _xsDataPosition.gridIndexZ.value
        position3VO.kappa      = _xsDataPosition.kappa.value
        position3VO.omega      = _xsDataPosition.omega.value
        position3VO.phi        = _xsDataPosition.phi.value
        position3VO.phiX       = _xsDataPosition.phiX.value
        position3VO.phiY       = _xsDataPosition.phiY.value
        position3VO.phiZ       = _xsDataPosition.phiZ.value
        position3VO.sampX      = _xsDataPosition.sampX.value
        position3VO.sampY      = _xsDataPosition.sampY.value
        return position3VO

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
from suds.sax.date import Date

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputStoreImageQualityIndicators
from XSDataISPyBv1_4 import XSDataResultStoreImageQualityIndicators


class EDPluginISPyBStoreImageQualityIndicatorsv1_4(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreImageQualityIndicators)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForAutoprocessingWebServiceWsdl = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.iImageQualityIndicatorsId = None
        self.iAutoProcProgramId = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
        self.iAutoProcProgramId = self.getIntegerConfigurationParameterValue("autoProcProgramId")
        if self.iAutoProcProgramId is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No autoProcProgramId found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        First uses the ImageService to find the imageId.
        Then uses ToolsForCollectionWebService for storing the image quality indicators.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.process")
        # First get the image ID
        xsDataImageQualityIndicators = self.getDataInput().getImageQualityIndicators()
        strPathToImage = xsDataImageQualityIndicators.getImage().getPath().getValue()
        strDirName = os.path.dirname(strPathToImage)+os.sep
        strFileName = os.path.basename(strPathToImage)
        if strDirName.endswith(os.sep):
            strDirName = strDirName[:-1]
        self.DEBUG("Looking for ISPyB imageId for dir %s name %s" % (strDirName, strFileName))
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        iDataCollectionId = clientToolsForCollectionWebService.service.findDataCollectionFromFileLocationAndFileName(
                strDirName, \
                strFileName, \
                )
        print iDataCollectionId
        
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService)
        iImageId = 0
        iAutoProcProgramId = self.iAutoProcProgramId
        iSpotTotal = xsDataImageQualityIndicators.getSpotTotal().getValue()
        iInResTotal = xsDataImageQualityIndicators.getInResTotal().getValue()
        iGoodBraggCandidates = xsDataImageQualityIndicators.getGoodBraggCandidates().getValue()
        iIceRings = xsDataImageQualityIndicators.getIceRings().getValue()
        fMethod1res = xsDataImageQualityIndicators.getMethod1Res().getValue()
        fMethod2res = xsDataImageQualityIndicators.getMethod2Res().getValue()
        fMaxUnitCell = xsDataImageQualityIndicators.getMaxUnitCell().getValue()
        fPctSaturationTop50peaks = xsDataImageQualityIndicators.getPctSaturationTop50Peaks().getValue()
        iInResolutionOvrlSpots = xsDataImageQualityIndicators.getInResolutionOvrlSpots().getValue()
        fBinPopCutOffMethod2res = xsDataImageQualityIndicators.getBinPopCutOffMethod2Res().getValue()
        providedDate = Date(datetime.datetime.now())
        self.iImageQualityIndicatorsId = clientToolsForAutoprocessingWebService.service.storeImageQualityIndicators(
                strDirName, \
                strFileName, \
                iImageId, \
                iAutoProcProgramId, \
                iSpotTotal, \
                iInResTotal, \
                iGoodBraggCandidates, \
                iIceRings, \
                fMethod1res, \
                fMethod2res, \
                fMaxUnitCell, \
                fPctSaturationTop50peaks, \
                iInResolutionOvrlSpots, \
                fBinPopCutOffMethod2res, \
                providedDate)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.process: imageQualityIndicatorsId=%d" % self.iImageQualityIndicatorsId)
            
             



    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.postProcess")
        xsDataResultStoreImageQualityIndicators = XSDataResultStoreImageQualityIndicators()
        if self.iImageQualityIndicatorsId is not None:
            xsDataResultStoreImageQualityIndicators.setImageQualityIndicatorsId(XSDataInteger(self.iImageQualityIndicatorsId))
        self.setDataOutput(xsDataResultStoreImageQualityIndicators)

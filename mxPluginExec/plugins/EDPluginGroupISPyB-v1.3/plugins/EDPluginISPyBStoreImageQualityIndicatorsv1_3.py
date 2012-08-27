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
from suds.sax.date import Date

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_3 import XSDataInputStoreImageQualityIndicators
from XSDataISPyBv1_3 import XSDataResultStoreImageQualityIndicators


class EDPluginISPyBStoreImageQualityIndicatorsv1_3(EDPluginExec):
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
        self.strImageServiceWdsl = None
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
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_3.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_3.configure: No pass word found in configuration!")
            self.setFailure()
        self.strImageServiceWdsl = self.getStringConfigurationParameterValue("imageServiceWdsl")
        if self.strImageServiceWdsl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_3.configure: No imageServiceWdsl found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_3.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
        self.iAutoProcProgramId = self.getIntegerConfigurationParameterValue("autoProcProgramId")
        if self.iAutoProcProgramId is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_3.configure: No autoProcProgramId found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        First uses the ImageService to find the imageId.
        Then uses ToolsForCollectionWebService for storing the image quality indicators.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_3.process")
        # First get the image ID
        xsDataImageQualityIndicators = self.getDataInput().getImageQualityIndicators()
        strPathToImage = xsDataImageQualityIndicators.getImage().getPath().getValue()
        strDirName = os.path.dirname(strPathToImage)+os.sep
        strFileName = os.path.basename(strPathToImage)
        if strDirName.endswith(os.sep):
            strDirName = strDirName[:-1]
        self.DEBUG("Looking for ISPyB imageId for dir %s name %s" % (strDirName, strFileName))
        httpAuthenticatedImageService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientImageService = Client(self.strImageServiceWdsl, transport=httpAuthenticatedImageService)
        iImageId = clientImageService.service.findImageIdFromFileLocationAndFileName(strDirName, strFileName)
        # Then store the image quality indicators
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_3.process: iImageId = %d" % iImageId)
        if iImageId > 0:
            httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
            clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
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
            self.iImageQualityIndicatorsId = clientToolsForCollectionWebService.service.storeImageQualityIndicators(
                    in0 = strDirName, \
                    in1 = strFileName, \
                    in2 = iImageId, \
                    in3 = iAutoProcProgramId, \
                    in4 = iSpotTotal, \
                    in5 = iInResTotal, \
                    in6 = iGoodBraggCandidates, \
                    in7 = iIceRings, \
                    in8 = fMethod1res, \
                    in9 = fMethod2res, \
                    in10= fMaxUnitCell, \
                    in11= fPctSaturationTop50peaks, \
                    in12= iInResolutionOvrlSpots, \
                    in13= fBinPopCutOffMethod2res, \
                    in14= providedDate)
            
             



    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_3.postProcess")
        xsDataResultStoreImageQualityIndicators = XSDataResultStoreImageQualityIndicators()
        if self.iImageQualityIndicatorsId is not None:
            xsDataResultStoreImageQualityIndicators.setImageQualityIndicatorsId(XSDataInteger(self.iImageQualityIndicatorsId))
        self.setDataOutput(xsDataResultStoreImageQualityIndicators)

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
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.config.get("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
        strAutoProcProgramId = self.config.get("autoProcProgramId")
        if strAutoProcProgramId is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No autoProcProgramId found in configuration!")
            self.setFailure()
        else:
            self.iAutoProcProgramId = int(strAutoProcProgramId)
                
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
        First uses the ImageService to find the imageId.
        Then uses ToolsForCollectionWebService for storing the image quality indicators.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.process")
        # First get the image ID
        xsDataImageQualityIndicators = self.getDataInput().getImageQualityIndicators()
        strPathToImage = xsDataImageQualityIndicators.getImage().getPath().getValue()
        strDirName = os.path.dirname(strPathToImage)
        strFileName = os.path.basename(strPathToImage)
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService)
        iImageId = 0
        iAutoProcProgramId = self.iAutoProcProgramId
        iSpotTotal = self.getXSValue(xsDataImageQualityIndicators.spotTotal)
        iInResTotal = self.getXSValue(xsDataImageQualityIndicators.inResTotal)
        iGoodBraggCandidates = self.getXSValue(xsDataImageQualityIndicators.goodBraggCandidates)
        iIceRings = self.getXSValue(xsDataImageQualityIndicators.iceRings)
        fMethod1res = self.getXSValue(xsDataImageQualityIndicators.method1Res)
        fMethod2res = self.getXSValue(xsDataImageQualityIndicators.method2Res)
        fMaxUnitCell = self.getXSValue(xsDataImageQualityIndicators.maxUnitCell)
        fPctSaturationTop50peaks = self.getXSValue(xsDataImageQualityIndicators.pctSaturationTop50Peaks)
        iInResolutionOvrlSpots = self.getXSValue(xsDataImageQualityIndicators.inResolutionOvrlSpots)
        fBinPopCutOffMethod2res = self.getXSValue(xsDataImageQualityIndicators.binPopCutOffMethod2Res)
        fTotalIntegratedSignal = self.getXSValue(xsDataImageQualityIndicators.totalIntegratedSignal)
        fBackground3D_score = self.getXSValue(xsDataImageQualityIndicators.background3D_score)

        providedDate = DateTime(datetime.datetime.now())
        self.iImageQualityIndicatorsId = clientToolsForAutoprocessingWebService.service.storeOrUpdateImageQualityIndicatorsForFileName(
                fileLocation=strDirName, \
                fileName=strFileName, \
                imageId=iImageId, \
                autoProcProgramId=iAutoProcProgramId, \
                spotTotal=iSpotTotal, \
                inResTotal=iInResTotal, \
                goodBraggCandidates=iGoodBraggCandidates, \
                iceRings=iIceRings, \
                method1Res=fMethod1res, \
                method2Res=fMethod2res, \
                maxUnitCell=fMaxUnitCell, \
                pctSaturationTop50Peaks=fPctSaturationTop50peaks, \
                inResolutionOvrlSpots=iInResolutionOvrlSpots, \
                binPopCutOffMethod2Res=fBinPopCutOffMethod2res, \
                totalIntegratedSignal=fTotalIntegratedSignal, \
                background3D_score=fBackground3D_score)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.process: imageQualityIndicatorsId=%r" % self.iImageQualityIndicatorsId)
            
             



    def finallyProcess(self, _edObject=None):
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreImageQualityIndicatorsv1_4.finallyProcess")
        xsDataResultStoreImageQualityIndicators = XSDataResultStoreImageQualityIndicators()
        if self.iImageQualityIndicatorsId is not None:
            xsDataResultStoreImageQualityIndicators.setImageQualityIndicatorsId(XSDataInteger(self.iImageQualityIndicatorsId))
        self.setDataOutput(xsDataResultStoreImageQualityIndicators)

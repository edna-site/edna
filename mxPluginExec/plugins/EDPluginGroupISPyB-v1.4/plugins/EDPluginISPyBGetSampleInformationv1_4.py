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

import pprint

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

from XSDataISPyBv1_4 import XSDataISPyBDiffractionPlan
from XSDataISPyBv1_4 import XSDataInputGetSampleInformation
from XSDataISPyBv1_4 import XSDataResultGetSampleInformation


class EDPluginISPyBGetSampleInformationv1_4(EDPluginExec):
    """
    Plugin to store workflow status in an ISPyB database using web services
    """

    def __init__(self):
        """
        Init plugin
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputGetSampleInformation)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForBLSampleWebServiceWsdl = None
        self.xsDataResultISPyBGetSampleInformation = XSDataResultGetSampleInformation()
        self.setDataOutput(self.xsDataResultISPyBGetSampleInformation)
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.config.get("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBGetSampleInformationv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.config.get("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBGetSampleInformationv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForBLSampleWebServiceWsdl = self.config.get("toolsForBLSampleWebServiceWsdl")
        if self.strToolsForBLSampleWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBGetSampleInformationv1_4.configure: No toolsForBLSampleWebServiceWsdl found in configuration!")
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
        self.DEBUG("EDPluginISPyBGetSampleInformationv1_4.process")
        # First get the image ID
        xsDataInputGetSampleInformation = self.getDataInput()
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForBLSampleWebServiceWsdl = Client(self.strToolsForBLSampleWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        iSampleId = self.getXSValue(xsDataInputGetSampleInformation.sampleId)
        sampleInfo = clientToolsForBLSampleWebServiceWsdl.service.getSampleInformation(iSampleId)
        self.DEBUG("Sample info from ISPyB: %r" % sampleInfo)
        if sampleInfo is not None:
            if "code" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.code = XSDataString(sampleInfo.code)
            if "cellA" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellA = XSDataDouble(sampleInfo.cellA)
            if "cellB" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellB = XSDataDouble(sampleInfo.cellB)
            if "cellC" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellC = XSDataDouble(sampleInfo.cellC)
            if "cellAlpha" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellAlpha = XSDataDouble(sampleInfo.cellAlpha)
            if "cellBeta" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellBeta = XSDataDouble(sampleInfo.cellBeta)
            if "cellGamma" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.cellGamma = XSDataDouble(sampleInfo.cellGamma)
            if "containerSampleChangerLocation" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.containerSampleChangerLocation = XSDataString(sampleInfo.containerSampleChangerLocation)
            if "crystalSpaceGroup" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.crystalSpaceGroup = XSDataString(sampleInfo.crystalSpaceGroup)
            if "experimentType" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.experimentType = XSDataString(sampleInfo.experimentType)
            if "holderLength" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.holderLength = XSDataDouble(sampleInfo.holderLength)
            if "minimalResolution" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.minimalResolution = XSDataDouble(sampleInfo.minimalResolution)
            if "proteinAcronym" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.proteinAcronym = XSDataString(sampleInfo.proteinAcronym)
            if "sampleId" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.sampleId = XSDataInteger(sampleInfo.sampleId)
            if "sampleLocation" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.sampleLocation = XSDataString(sampleInfo.sampleLocation)
            if "sampleName" in sampleInfo:
                self.xsDataResultISPyBGetSampleInformation.sampleName = XSDataString(sampleInfo.sampleName)
            if "diffractionPlan" in sampleInfo:
                xsDataISPyBDiffractionPlan = XSDataISPyBDiffractionPlan()
                if "aimedCompleteness" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.aimedCompleteness = XSDataDouble(sampleInfo.diffractionPlan.aimedCompleteness)
                if "aimedIOverSigmaAtHighestResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.aimedIOverSigmaAtHighestResolution = XSDataDouble(sampleInfo.diffractionPlan.aimedIOverSigmaAtHighestResolution)
                if "aimedMultiplicity" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.aimedMultiplicity = XSDataDouble(sampleInfo.diffractionPlan.aimedMultiplicity)
                if "aimedResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.aimedResolution = XSDataDouble(sampleInfo.diffractionPlan.aimedResolution)
                if "anomalousData" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.anomalousData = XSDataBoolean(sampleInfo.diffractionPlan.anomalousData)
                if "comments" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.comments = XSDataString(sampleInfo.diffractionPlan.comments)
                if "complexity" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.complexity = XSDataString(sampleInfo.diffractionPlan.complexity)
                if "diffractionPlanId" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.diffractionPlanId = XSDataInteger(sampleInfo.diffractionPlan.diffractionPlanId)
                if "estimateRadiationDamage" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.estimateRadiationDamage = XSDataBoolean(sampleInfo.diffractionPlan.estimateRadiationDamage)
                if "experimentKind" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.experimentKind = XSDataString(sampleInfo.diffractionPlan.experimentKind)
                if "exposureTime" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.exposureTime = XSDataDouble(sampleInfo.diffractionPlan.exposureTime)
                if "forcedSpaceGroup" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.forcedSpaceGroup = XSDataString(sampleInfo.diffractionPlan.forcedSpaceGroup)
                if "kappaStrategyOption" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.kappaStrategyOption = XSDataString(sampleInfo.diffractionPlan.kappaStrategyOption)
                if "maxDimAccrossSpindleAxis" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.maxDimAccrossSpindleAxis = XSDataDouble(sampleInfo.diffractionPlan.maxDimAccrossSpindleAxis)
                if "maximalResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.maximalResolution = XSDataDouble(sampleInfo.diffractionPlan.maximalResolution)
                if "minDimAccrossSpindleAxis" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.minDimAccrossSpindleAxis = XSDataDouble(sampleInfo.diffractionPlan.minDimAccrossSpindleAxis)
                if "minimalResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.minimalResolution = XSDataDouble(sampleInfo.diffractionPlan.minimalResolution)
                if "numberOfPositions" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.numberOfPositions = XSDataInteger(sampleInfo.diffractionPlan.numberOfPositions)
                if "observedResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.observedResolution = XSDataDouble(sampleInfo.diffractionPlan.observedResolution)
                if "oscillationRange" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.oscillationRange = XSDataDouble(sampleInfo.diffractionPlan.oscillationRange)
                if "preferredBeamSizeX" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.preferredBeamSizeX = XSDataDouble(sampleInfo.diffractionPlan.preferredBeamSizeX)
                if "preferredBeamSizeY" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.preferredBeamSizeY = XSDataDouble(sampleInfo.diffractionPlan.preferredBeamSizeY)
                if "radiationSensitivity" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.radiationSensitivity = XSDataDouble(sampleInfo.diffractionPlan.radiationSensitivity)
                if "radiationSensitivityBeta" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.radiationSensitivityBeta = XSDataDouble(sampleInfo.diffractionPlan.radiationSensitivityBeta)
                if "radiationSensitivityGamma" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.radiationSensitivityGamma = XSDataDouble(sampleInfo.diffractionPlan.radiationSensitivityGamma)
                if "requiredCompleteness" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.requiredCompleteness = XSDataDouble(sampleInfo.diffractionPlan.requiredCompleteness)
                if "requiredMultiplicity" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.requiredMultiplicity = XSDataDouble(sampleInfo.diffractionPlan.requiredMultiplicity)
                if "requiredResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.requiredResolution = XSDataDouble(sampleInfo.diffractionPlan.requiredResolution)
                if "screeningResolution" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.screeningResolution = XSDataDouble(sampleInfo.diffractionPlan.screeningResolution)
                if "anomalousScatterer" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.anomalousScatterer = XSDataString(sampleInfo.diffractionPlan.anomalousScatterer)
                if "strategyOption" in sampleInfo.diffractionPlan:
                    xsDataISPyBDiffractionPlan.strategyOption = XSDataString(sampleInfo.diffractionPlan.strategyOption)
                self.xsDataResultISPyBGetSampleInformation.diffractionPlan = xsDataISPyBDiffractionPlan
        self.DEBUG("EDPluginISPyBGetSampleInformationv1_4.process: result=%s" % pprint.pformat(self.xsDataResultISPyBGetSampleInformation))
            
             



    def finallyProcess(self, _edObject=None):
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBGetSampleInformationv1_4.finallyProcess")
        self.setDataOutput(self.xsDataResultISPyBGetSampleInformation)

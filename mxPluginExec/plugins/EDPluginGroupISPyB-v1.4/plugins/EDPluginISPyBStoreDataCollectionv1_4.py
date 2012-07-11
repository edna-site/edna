#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
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


__author__ = "Thomas Boeglin"
__contact__ = "thomas.boeglin@esrf.fr"
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

from XSDataISPyBv1_4 import XSDataInputStoreDataCollection
from XSDataISPyBv1_4 import XSDataResultStoreDataCollection

class EDPluginISPyBStoreDataCollectionv1_4(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreDataCollection)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.bContinue = True

    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()


    def process(self, _edObject=None):
        """
        Stores the contents of the DataCollectionContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_4.process")
        xsDataInputStoreDataCollection = self.getDataInput()
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)

        # DataCollectionProgram
        self.iDataCollectionId = self.storeDataCollectionProgram(clientToolsForCollectionWebService, xsDataInputStoreDataCollection)
        if self.iDataCollectionId is None:
            self.ERROR("Couldn't create entry for DataCollectionId in ISPyB!")
            self.setFailure()
            self.bContinue = False


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_4.postProcess")
        xsDataResultStoreDataCollection = XSDataResultStoreDataCollection()
        if self.iDataCollectionId is not None:
            xsDataResultStoreDataCollection.setDataCollectionId(XSDataInteger(self.iDataCollectionId))
        self.setDataOutput(xsDataResultStoreDataCollection)


    def getValue(self, _oValue, _oDefaultValue=None):
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


    def storeDataCollectionProgram(self, _clientToolsForCollectionWebService, _xsDataInputStoreDataCollection):
        """Creates an entry in the ISPyB DataCollectionProgram table"""
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_4.storeDataCollectionProgram")

        dataCollection = _xsDataInputStoreDataCollection.getDataCollection()
        dataCollectionWS3VO =_clientToolsForCollectionWebService.factory.create('dataCollectionWS3VO')

        dataCollectionWS3VO.dataCollectionId = self.getValue(dataCollection.getDataCollectionId(), 0) # integer
        dataCollectionWS3VO.blSampleId = self.getValue(dataCollection.getBlSampleId(), 0) # integer
        dataCollectionWS3VO.sessionId = self.getValue(dataCollection.getSessionId()) # integer
        dataCollectionWS3VO.experimentType = self.getValue(dataCollection.getExperimentType()) # string
        dataCollectionWS3VO.dataCollectionNumber = self.getValue(dataCollection.getDataCollectionNumber()) # integer
        dataCollectionWS3VO.startTime = DateTime(self.getValue(dataCollection.getStartDate())) # string
        dataCollectionWS3VO.endTime = DateTime(self.getValue(dataCollection.getEndDate())) # string
        dataCollectionWS3VO.runStatus = self.getValue(dataCollection.getRunStatus()) # string
        dataCollectionWS3VO.rotationAxis = self.getValue(dataCollection.getRotationAxis()) # string
        dataCollectionWS3VO.phiStart = self.getValue(dataCollection.getPhiStart()) # float
        dataCollectionWS3VO.kappaStart = self.getValue(dataCollection.getKappaStart()) # float
        dataCollectionWS3VO.omegaStart = self.getValue(dataCollection.getOmegaStart()) # float
        dataCollectionWS3VO.axisStart = self.getValue(dataCollection.getAxisStart()) # float
        dataCollectionWS3VO.axisEnd = self.getValue(dataCollection.getAxisEnd()) # float
        dataCollectionWS3VO.axisRange = self.getValue(dataCollection.getAxisRange()) # float
        dataCollectionWS3VO.overlap = self.getValue(dataCollection.getOverlap()) # float
        dataCollectionWS3VO.numberOfImages = self.getValue(dataCollection.getNumberOfImages()) # integer
        dataCollectionWS3VO.startImageNumber = self.getValue(dataCollection.getStartImageNumber()) # integer
        dataCollectionWS3VO.numberOfPasses = self.getValue(dataCollection.getNumberOfPasses()) # integer
        dataCollectionWS3VO.exposureTime = self.getValue(dataCollection.getExposureTime()) # float
        dataCollectionWS3VO.imageDirectory = self.getValue(dataCollection.getImageDirectory()) # string
        dataCollectionWS3VO.imagePrefix = self.getValue(dataCollection.getImagePrefix()) # string
        dataCollectionWS3VO.imageSuffix = self.getValue(dataCollection.getImageSuffix()) # string
        dataCollectionWS3VO.fileTemplate = self.getValue(dataCollection.getFileTemplate()) # string
        dataCollectionWS3VO.wavelength = self.getValue(dataCollection.getWavelength()) # float
        dataCollectionWS3VO.resolution = self.getValue(dataCollection.getResolution()) # float
        dataCollectionWS3VO.resolutionAtCorner = self.getValue(dataCollection.getResolutionAtCorner()) # float
        dataCollectionWS3VO.detectorDistance = self.getValue(dataCollection.getDetectorDistance()) # float
        dataCollectionWS3VO.detector2theta = self.getValue(dataCollection.getDetector2theta()) # float
        dataCollectionWS3VO.detectorMode = self.getValue(dataCollection.getDetectorMode()) # string
        dataCollectionWS3VO.undulatorGap1 = self.getValue(dataCollection.getUndulatorGap1()) # float
        dataCollectionWS3VO.undulatorGap2 = self.getValue(dataCollection.getUndulatorGap2()) # float
        dataCollectionWS3VO.undulatorGap3 = self.getValue(dataCollection.getUndulatorGap3()) # float
        dataCollectionWS3VO.xbeam = self.getValue(dataCollection.getXbeam()) # float
        dataCollectionWS3VO.ybeam = self.getValue(dataCollection.getYbeam()) # float
        dataCollectionWS3VO.crystalClass = self.getValue(dataCollection.getCrystalClass()) # string
        dataCollectionWS3VO.slitGapVertical = self.getValue(dataCollection.getSlitGapVertical()) # float
        dataCollectionWS3VO.slitGapHorizontal = self.getValue(dataCollection.getSlitGapHorizontal()) # float
        dataCollectionWS3VO.beamSizeAtSampleX = self.getValue(dataCollection.getBeamSizeAtSampleX()) # float
        dataCollectionWS3VO.beamSizeAtSampleY = self.getValue(dataCollection.getBeamSizeAtSampleY()) # float
        dataCollectionWS3VO.transmission = self.getValue(dataCollection.getTransmission()) # float
        dataCollectionWS3VO.synchrotronMode = self.getValue(dataCollection.getSynchrotronMode()) # string
        dataCollectionWS3VO.centeringMethod = self.getValue(dataCollection.getCenteringMethod()) # string
        dataCollectionWS3VO.averageTemperature = self.getValue(dataCollection.getAverageTemperature()) # float
        dataCollectionWS3VO.comments = self.getValue(dataCollection.getComments()) # string
        #printableForReport = str(self.getValue(dataCollection.getPrintableForReport())).lower() # boolean
        if self.getValue(dataCollection.getPrintableForReport()):
            dataCollectionWS3VO.printableForReport = 1
        else:
            dataCollectionWS3VO.printableForReport = 0
        dataCollectionWS3VO.xtalSnapshotFullPath1 = self.getValue(dataCollection.getXtalSnapshotFullPath1()) # string
        dataCollectionWS3VO.xtalSnapshotFullPath2 = self.getValue(dataCollection.getXtalSnapshotFullPath2()) # string
        dataCollectionWS3VO.xtalSnapshotFullPath3 = self.getValue(dataCollection.getXtalSnapshotFullPath3()) # string
        dataCollectionWS3VO.xtalSnapshotFullPath4 = self.getValue(dataCollection.getXtalSnapshotFullPath4()) # string
        dataCollectionWS3VO.beamShape = self.getValue(dataCollection.getBeamShape()) # string

        iDataCollectionId = _clientToolsForCollectionWebService.service.storeOrUpdateDataCollection(dataCollection=dataCollectionWS3VO)

        self.DEBUG("DataCollectionProgramId: %r" % iDataCollectionId)
        return iDataCollectionId


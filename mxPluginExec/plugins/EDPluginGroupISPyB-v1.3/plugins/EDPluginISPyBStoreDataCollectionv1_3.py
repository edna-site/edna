#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011      European Synchrotron Radiation Facility
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

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataISPyBv1_3 import XSDataInputStoreDataCollection

class EDPluginISPyBStoreDataCollectionv1_3(EDPluginExec):
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
        self.strToolsForMXCubeWebServiceWsdl = None
        self.bContinue = True

    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = self.getStringConfigurationParameterValue("userName")
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_3.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = self.getStringConfigurationParameterValue("passWord")
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_3.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForMXCubeWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForMXCubeWebServiceWsdl")
        if self.strToolsForMXCubeWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_3.configure: No toolsForMXCubeWebServiceWsdl found in configuration!")
            self.setFailure()


    def process(self, _edObject=None):
        """
        Stores the contents of the DataCollectionContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.process")
        xsDataInputStoreDataCollection = self.getDataInput()
        httpAuthenticatedToolsForMXCubeWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForMXCubeWebService = Client(self.strToolsForMXCubeWebServiceWsdl, transport=httpAuthenticatedToolsForMXCubeWebService)

        # DataCollectionProgram
        self.iDataCollectionId = self.storeDataCollectionProgram(clientToolsForMXCubeWebService, xsDataInputStoreDataCollection)
        if self.iDataCollectionId is None:
            self.ERROR("Couldn't create entry for DataCollectionId in ISPyB!")
            self.setFailure()
            self.bContinue = False


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.postProcess")
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


    def storeDataCollectionProgram(self, _clientToolsForMXCubeWebService, _xsDataInputStoreDataCollection):
        """Creates an entry in the ISPyB DataCollectionProgram table"""
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.storeDataCollectionProgram")

        updateOrStoreDataCollectionRequest = _xsDataInputStoreDataCollection.getUpdateOrStoreDataCollectionRequest()

        dataCollectionId = self.getValue(updateOrStoreDataCollectionRequest.getDataCollectionId(), 0) # integer
        blSampleId = self.getValue(updateOrStoreDataCollectionRequest.getBlSampleId(), 0) # integer
        sessionId = self.getValue(updateOrStoreDataCollectionRequest.getSessionId()) # integer
        experimentType = self.getValue(updateOrStoreDataCollectionRequest.getExperimentType()) # string
        dataCollectionNumber = self.getValue(updateOrStoreDataCollectionRequest.getDataCollectionNumber()) # integer
        startDate = self.getValue(updateOrStoreDataCollectionRequest.getStartDate()) # string
        endDate = self.getValue(updateOrStoreDataCollectionRequest.getEndDate()) # string
        runStatus = self.getValue(updateOrStoreDataCollectionRequest.getRunStatus()) # string
        rotationAxis = self.getValue(updateOrStoreDataCollectionRequest.getRotationAxis()) # string
        phiStart = self.getValue(updateOrStoreDataCollectionRequest.getPhiStart()) # float
        kappaStart = self.getValue(updateOrStoreDataCollectionRequest.getKappaStart()) # float
        omegaStart = self.getValue(updateOrStoreDataCollectionRequest.getOmegaStart()) # float
        axisStart = self.getValue(updateOrStoreDataCollectionRequest.getAxisStart()) # float
        axisEnd = self.getValue(updateOrStoreDataCollectionRequest.getAxisEnd()) # float
        axisRange = self.getValue(updateOrStoreDataCollectionRequest.getAxisRange()) # float
        overlap = self.getValue(updateOrStoreDataCollectionRequest.getOverlap()) # float
        numberOfImages = self.getValue(updateOrStoreDataCollectionRequest.getNumberOfImages()) # integer
        startImageNumber = self.getValue(updateOrStoreDataCollectionRequest.getStartImageNumber()) # integer
        numberOfPasses = self.getValue(updateOrStoreDataCollectionRequest.getNumberOfPasses()) # integer
        exposureTime = self.getValue(updateOrStoreDataCollectionRequest.getExposureTime()) # float
        imageDirectory = self.getValue(updateOrStoreDataCollectionRequest.getImageDirectory()) # string
        imagePrefix = self.getValue(updateOrStoreDataCollectionRequest.getImagePrefix()) # string
        imageSuffix = self.getValue(updateOrStoreDataCollectionRequest.getImageSuffix()) # string
        fileTemplate = self.getValue(updateOrStoreDataCollectionRequest.getFileTemplate()) # string
        wavelength = self.getValue(updateOrStoreDataCollectionRequest.getWavelength()) # float
        resolution = self.getValue(updateOrStoreDataCollectionRequest.getResolution()) # float
        resolutionAtCorner = self.getValue(updateOrStoreDataCollectionRequest.getResolutionAtCorner()) # float
        detectorDistance = self.getValue(updateOrStoreDataCollectionRequest.getDetectorDistance()) # float
        detector2theta = self.getValue(updateOrStoreDataCollectionRequest.getDetector2theta()) # float
        detectorMode = self.getValue(updateOrStoreDataCollectionRequest.getDetectorMode()) # string
        undulatorGap1 = self.getValue(updateOrStoreDataCollectionRequest.getUndulatorGap1()) # float
        undulatorGap2 = self.getValue(updateOrStoreDataCollectionRequest.getUndulatorGap2()) # float
        undulatorGap3 = self.getValue(updateOrStoreDataCollectionRequest.getUndulatorGap3()) # float
        xbeam = self.getValue(updateOrStoreDataCollectionRequest.getXbeam()) # float
        ybeam = self.getValue(updateOrStoreDataCollectionRequest.getYbeam()) # float
        crystalClass = self.getValue(updateOrStoreDataCollectionRequest.getCrystalClass()) # string
        slitGapVertical = self.getValue(updateOrStoreDataCollectionRequest.getSlitGapVertical()) # float
        slitGapHorizontal = self.getValue(updateOrStoreDataCollectionRequest.getSlitGapHorizontal()) # float
        beamSizeAtSampleX = self.getValue(updateOrStoreDataCollectionRequest.getBeamSizeAtSampleX()) # float
        beamSizeAtSampleY = self.getValue(updateOrStoreDataCollectionRequest.getBeamSizeAtSampleY()) # float
        transmission = self.getValue(updateOrStoreDataCollectionRequest.getTransmission()) # float
        synchrotronMode = self.getValue(updateOrStoreDataCollectionRequest.getSynchrotronMode()) # string
        centeringMethod = self.getValue(updateOrStoreDataCollectionRequest.getCenteringMethod()) # string
        averageTemperature = self.getValue(updateOrStoreDataCollectionRequest.getAverageTemperature()) # float
        comments = self.getValue(updateOrStoreDataCollectionRequest.getComments()) # string
        printableForReport = self.getValue(updateOrStoreDataCollectionRequest.getPrintableForReport()) # boolean
        xtalSnapshotFullPath1 = self.getValue(updateOrStoreDataCollectionRequest.getXtalSnapshotFullPath1()) # string
        xtalSnapshotFullPath2 = self.getValue(updateOrStoreDataCollectionRequest.getXtalSnapshotFullPath2()) # string
        xtalSnapshotFullPath3 = self.getValue(updateOrStoreDataCollectionRequest.getXtalSnapshotFullPath3()) # string
        xtalSnapshotFullPath4 = self.getValue(updateOrStoreDataCollectionRequest.getXtalSnapshotFullPath4()) # string
        beamShape = self.getValue(updateOrStoreDataCollectionRequest.getBeamShape()) # string

        iDataCollectionId = _clientToolsForMXCubeWebService.service.updateOrStoreDataCollectionRequest(dataCollectionId, blSampleId, sessionId,
                                                                           experimentType, dataCollectionNumber, startDate,
                                                                           endDate, runStatus, rotationAxis,
                                                                           phiStart, kappaStart, omegaStart,
                                                                           axisStart, axisEnd, axisRange,
                                                                           overlap, numberOfImages, startImageNumber,
                                                                           numberOfPasses, exposureTime, imageDirectory,
                                                                           imagePrefix, imageSuffix, fileTemplate,
                                                                           wavelength, resolution, resolutionAtCorner,
                                                                           detectorDistance, detector2theta, detectorMode,
                                                                           undulatorGap1, undulatorGap2, undulatorGap3,
                                                                           xbeam, ybeam, crystalClass,
                                                                           slitGapVertical, slitGapHorizontal, beamSizeAtSampleX,
                                                                           beamSizeAtSampleY, transmission, synchrotronMode,
                                                                           centeringMethod, averageTemperature, comments,
                                                                           printableForReport, xtalSnapshotFullPath1, xtalSnapshotFullPath2,
                                                                           xtalSnapshotFullPath3, xtalSnapshotFullPath4, beamShape)







#        strProcessingCommandLine = self.getValue(updateOrStoreDataCollectionRequest.getProcessingCommandLine(), "")
#        strProcessingPrograms = self.getValue(updateOrStoreDataCollectionRequest.getProcessingPrograms(), "")
#        bProcessingStatus = self.getValue(updateOrStoreDataCollectionRequest.getProcessingStatus(), True)
#        strProcessingMessage = self.getValue(updateOrStoreDataCollectionRequest.getProcessingMessage(), "")
#        processingStartTime = self.getDateValue(updateOrStoreDataCollectionRequest.getProcessingStartTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        processingEndTime = self.getDateValue(updateOrStoreDataCollectionRequest.getProcessingEndTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        strProcessingEnvironment = self.getValue(updateOrStoreDataCollectionRequest.getProcessingEnvironment(), "")
#        recordTimeStamp = DateTime(datetime.datetime.now())
#        iDataCollectionProgramId = _clientToolsForMXCubeWebService.service.storeDataCollectionProgram(
#                in0=strProcessingCommandLine, \
#                in1=strProcessingPrograms, \
#                in2=bProcessingStatus, \
#                in3=strProcessingMessage, \
#                in4=processingStartTime, \
#                in5=processingEndTime, \
#                in6=strProcessingEnvironment, \
#                in7=recordTimeStamp
#                )
        self.DEBUG("DataCollectionProgramId: %r" % iDataCollectionProgramId)
        return iDataCollectionProgramId


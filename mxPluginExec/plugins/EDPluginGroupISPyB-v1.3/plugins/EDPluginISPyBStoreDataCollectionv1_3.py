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

from XSDataISPyBv1_3 import UpdateOrStoreDataCollectionRequest

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


    def getValue(self, _oValue, _oDefaultValue):
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


    def storeDataCollectionProgram(self, _clientToolsForMXCubeWebService, _xsDataDataCollectionProgram):
        """Creates an entry in the ISPyB DataCollectionProgram table"""
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.storeDataCollectionProgram")

        

        dataCollectionId = self.getValue(_xsDataDataCollectionProgram.getDataCollectionId()) # integer
	blSampleId = self.getValue(_xsDataDataCollectionProgram.getBlSampleId()) # integer
	sessionId = self.getValue(_xsDataDataCollectionProgram.getSessionId()) # integer
	experimentType = self.getValue(_xsDataDataCollectionProgram.getExperimentType()) # string
	dataCollectionNumber = self.getValue(_xsDataDataCollectionProgram.getDataCollectionNumber()) # integer
	startDate = self.getValue(_xsDataDataCollectionProgram.getStartDate()) # string
	endDate = self.getValue(_xsDataDataCollectionProgram.getEndDate()) # string
	runStatus = self.getValue(_xsDataDataCollectionProgram.getRunStatus()) # string
	rotationAxis = self.getValue(_xsDataDataCollectionProgram.getRotationAxis()) # string
	phiStart = self.getValue(_xsDataDataCollectionProgram.getPhiStart()) # float
	kappaStart = self.getValue(_xsDataDataCollectionProgram.getKappaStart()) # float
	omegaStart = self.getValue(_xsDataDataCollectionProgram.getOmegaStart()) # float
	axisStart = self.getValue(_xsDataDataCollectionProgram.getAxisStart()) # float
	axisEnd = self.getValue(_xsDataDataCollectionProgram.getAxisEnd()) # float
	axisRange = self.getValue(_xsDataDataCollectionProgram.getAxisRange()) # float
	overlap = self.getValue(_xsDataDataCollectionProgram.getOverlap()) # float
	numberOfImages = self.getValue(_xsDataDataCollectionProgram.getNumberOfImages()) # integer
	startImageNumber = self.getValue(_xsDataDataCollectionProgram.getStartImageNumber()) # integer
	numberOfPasses = self.getValue(_xsDataDataCollectionProgram.getNumberOfPasses()) # integer
	exposureTime = self.getValue(_xsDataDataCollectionProgram.getExposureTime()) # float
	imageDirectory = self.getValue(_xsDataDataCollectionProgram.getImageDirectory()) # string
	imagePrefix = self.getValue(_xsDataDataCollectionProgram.getImagePrefix()) # string
	imageSuffix = self.getValue(_xsDataDataCollectionProgram.getImageSuffix()) # string
	fileTemplate = self.getValue(_xsDataDataCollectionProgram.getFileTemplate()) # string
	wavelength = self.getValue(_xsDataDataCollectionProgram.getWavelength()) # float
	resolution = self.getValue(_xsDataDataCollectionProgram.getResolution()) # float
	resolutionAtCorner = self.getValue(_xsDataDataCollectionProgram.getResolutionAtCorner()) # float
	detectorDistance = self.getValue(_xsDataDataCollectionProgram.getDetectorDistance()) # float
	detector2theta = self.getValue(_xsDataDataCollectionProgram.getDetector2theta()) # float
	detectorMode = self.getValue(_xsDataDataCollectionProgram.getDetectorMode()) # string
	undulatorGap1 = self.getValue(_xsDataDataCollectionProgram.getUndulatorGap1()) # float
	undulatorGap2 = self.getValue(_xsDataDataCollectionProgram.getUndulatorGap2()) # float
	undulatorGap3 = self.getValue(_xsDataDataCollectionProgram.getUndulatorGap3()) # float
	xbeam = self.getValue(_xsDataDataCollectionProgram.getXbeam()) # float
	ybeam = self.getValue(_xsDataDataCollectionProgram.getYbeam()) # float
	crystalClass = self.getValue(_xsDataDataCollectionProgram.getCrystalClass()) # string
	slitGapVertical = self.getValue(_xsDataDataCollectionProgram.getSlitGapVertical()) # float
	slitGapHorizontal = self.getValue(_xsDataDataCollectionProgram.getSlitGapHorizontal()) # float
	beamSizeAtSampleX = self.getValue(_xsDataDataCollectionProgram.getBeamSizeAtSampleX()) # float
	beamSizeAtSampleY = self.getValue(_xsDataDataCollectionProgram.getBeamSizeAtSampleY()) # float
	transmission = self.getValue(_xsDataDataCollectionProgram.getTransmission()) # float
	synchrotronMode = self.getValue(_xsDataDataCollectionProgram.getSynchrotronMode()) # string
	centeringMethod = self.getValue(_xsDataDataCollectionProgram.getCenteringMethod()) # string
	averageTemperature = self.getValue(_xsDataDataCollectionProgram.getAverageTemperature()) # float
	comments = self.getValue(_xsDataDataCollectionProgram.getComments()) # string
	printableForReport = self.getValue(_xsDataDataCollectionProgram.getPrintableForReport()) # boolean
	xtalSnapshotFullPath1 = self.getValue(_xsDataDataCollectionProgram.getXtalSnapshotFullPath1()) # string
	xtalSnapshotFullPath2 = self.getValue(_xsDataDataCollectionProgram.getXtalSnapshotFullPath2()) # string
	xtalSnapshotFullPath3 = self.getValue(_xsDataDataCollectionProgram.getXtalSnapshotFullPath3()) # string
	xtalSnapshotFullPath4 = self.getValue(_xsDataDataCollectionProgram.getXtalSnapshotFullPath4()) # string
        beamShape = self.getValue(_xsDataDataCollectionProgram.getBeamShape()) # string

        _clientToolsForMXCubeWebService.service.storeDataCollectionProgram(dataCollectionId, blSampleId, sessionId,
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







#        strProcessingCommandLine = self.getValue(_xsDataDataCollectionProgram.getProcessingCommandLine(), "")
#        strProcessingPrograms = self.getValue(_xsDataDataCollectionProgram.getProcessingPrograms(), "")
#        bProcessingStatus = self.getValue(_xsDataDataCollectionProgram.getProcessingStatus(), True)
#        strProcessingMessage = self.getValue(_xsDataDataCollectionProgram.getProcessingMessage(), "")
#        processingStartTime = self.getDateValue(_xsDataDataCollectionProgram.getProcessingStartTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        processingEndTime = self.getDateValue(_xsDataDataCollectionProgram.getProcessingEndTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
#        strProcessingEnvironment = self.getValue(_xsDataDataCollectionProgram.getProcessingEnvironment(), "")
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


    def storeDataCollectionProgramAttachment(self, _clientToolsForMXCubeWebService, _xsDataDataCollectionProgramAttachment):
        """Creates an entry in the ISPyB DataCollectionProgramAttachment table"""
        iDataCollectionProgramId = self.iDataCollectionProgramId
        strFileType = self.getValue(_xsDataDataCollectionProgramAttachment.getFileType(), "")
        strFileName = self.getValue(_xsDataDataCollectionProgramAttachment.getFileName(), "")
        strFilePath = self.getValue(_xsDataDataCollectionProgramAttachment.getFilePath(), "")
        recordTimeStamp = DateTime(datetime.datetime.now())
        iDataCollectionProgramAttachmentId = _clientToolsForMXCubeWebService.service.storeDataCollectionProgramAttachment(
                in0=strFileType, \
                in1=strFileName, \
                in2=strFilePath, \
                in3=recordTimeStamp, \
                in4=iDataCollectionProgramId
                )
        self.DEBUG("DataCollectionProgramAttachmentId: %r" % iDataCollectionProgramAttachmentId)
        return iDataCollectionProgramAttachmentId


    def storeDataCollectionIntegration(self, _clientToolsForMXCubeWebService, _xsDataDataCollectionIntegrationContainer):
        """Creates an entry in the ISPyB DataCollectionIntegration table"""
        xsDataProcIntegration = _xsDataDataCollectionIntegrationContainer.getDataCollectionIntegration()
        iDataCollectionProgramId = self.iDataCollectionProgramId
        iStartImageNumber = self.getValue(xsDataProcIntegration.getStartImageNumber(), 9999)
        iEndImageNumber = self.getValue(xsDataProcIntegration.getEndImageNumber(), 9999)
        fRefinedDetectorDistance = self.getValue(xsDataProcIntegration.getRefinedDetectorDistance(), -1.0)
        fRefinedXbeam = self.getValue(xsDataProcIntegration.getRefinedXbeam(), -1.0)
        fRefinedYbeam = self.getValue(xsDataProcIntegration.getRefinedYbeam(), -1.0)
        fRotationAxisX = self.getValue(xsDataProcIntegration.getRotationAxisX(), -1.0)
        fRotationAxisY = self.getValue(xsDataProcIntegration.getRotationAxisY(), -1.0)
        fRotationAxisZ = self.getValue(xsDataProcIntegration.getRotationAxisZ(), -1.0)
        fBeamVectorX = self.getValue(xsDataProcIntegration.getBeamVectorX(), -1.0)
        fBeamVectorY = self.getValue(xsDataProcIntegration.getBeamVectorY(), -1.0)
        fBeamVectorZ = self.getValue(xsDataProcIntegration.getBeamVectorZ(), -1.0)
        fCellA = self.getValue(xsDataProcIntegration.getCell_a(), -1.0)
        fCellB = self.getValue(xsDataProcIntegration.getCell_b(), -1.0)
        fCellC = self.getValue(xsDataProcIntegration.getCell_c(), -1.0)
        fCellAlpha = self.getValue(xsDataProcIntegration.getCell_alpha(), -1.0)
        fCellBeta = self.getValue(xsDataProcIntegration.getCell_beta(), -1.0)
        fCellGamma = self.getValue(xsDataProcIntegration.getCell_gamma(), -1.0)
        iDataCollectionId = _xsDataDataCollectionIntegrationContainer.getImage().getDataCollectionId()
        recordTimeStamp = DateTime(datetime.datetime.now())
        iDataCollectionIntegrationId = _clientToolsForMXCubeWebService.service.storeDataCollectionIntegration(
                in0=iDataCollectionProgramId, \
                in1=iStartImageNumber, \
                in2=iEndImageNumber, \
                in3=fRefinedDetectorDistance, \
                in4=fRefinedXbeam, \
                in5=fRefinedYbeam, \
                in6=fRotationAxisX, \
                in7=fRotationAxisY, \
                in8=fRotationAxisZ, \
                in9=fBeamVectorX, \
                in10=fBeamVectorY, \
                in11=fBeamVectorZ, \
                in12=fCellA, \
                in13=fCellB, \
                in14=fCellC, \
                in15=fCellAlpha, \
                in16=fCellBeta, \
                in17=fCellGamma, \
                in18=recordTimeStamp, \
                in19=iDataCollectionId \
                )
        self.DEBUG("DataCollectionProgramIntegrationId: %r" % iDataCollectionIntegrationId)
        return iDataCollectionIntegrationId


    def storeDataCollection(self, _clientToolsForMXCubeWebService, _xsDataDataCollection):
        """Creates an entry in the ISPyB DataCollection table"""
        iDataCollectionProgramId = self.iDataCollectionProgramId
        strSpaceGroup = self.getValue(_xsDataDataCollection.getSpaceGroup(), "")
        fRefinedCellA = self.getValue(_xsDataDataCollection.getRefinedCell_a(), -1)
        fRefinedCellB = self.getValue(_xsDataDataCollection.getRefinedCell_b(), -1)
        fRefinedCellC = self.getValue(_xsDataDataCollection.getRefinedCell_c(), -1)
        fRefinedCellAlpha = self.getValue(_xsDataDataCollection.getRefinedCell_alpha(), -1)
        fRefinedCellBeta = self.getValue(_xsDataDataCollection.getRefinedCell_beta(), -1)
        fRefinedCellGamma = self.getValue(_xsDataDataCollection.getRefinedCell_gamma(), -1)
        recordTimeStamp = DateTime(datetime.datetime.now())
        iDataCollectionId = _clientToolsForMXCubeWebService.service.storeDataCollection(
                in0=iDataCollectionProgramId, \
                in1=strSpaceGroup, \
                in2=fRefinedCellA, \
                in3=fRefinedCellB, \
                in4=fRefinedCellC, \
                in5=fRefinedCellAlpha, \
                in6=fRefinedCellBeta, \
                in7=fRefinedCellGamma, \
                in8=recordTimeStamp \
                )
        self.DEBUG("DataCollectionId: %r" % iDataCollectionId)
        return iDataCollectionId


    def storeDataCollectionScaling(self, _clientToolsForMXCubeWebService, _xsDataDataCollectionScaling):
        """Creates an entry in the ISPyB DataCollectionScaling table"""
        iDataCollectionId = self.iDataCollectionId
        recordTimeStamp = self.getDateValue(_xsDataDataCollectionScaling.getRecordTimeStamp(), "%Y-%m-%d %H:%M:%S", DateTime(datetime.datetime.now()))
        iDataCollectionScalingId = _clientToolsForMXCubeWebService.service.storeDataCollectionScaling(
                in0=iDataCollectionId, \
                in1=recordTimeStamp \
                )
        self.DEBUG("DataCollectionScalingId: %r" % iDataCollectionScalingId)
        return iDataCollectionScalingId



    def storeDataCollectionScalingStatistics(self, _clientToolsForMXCubeWebService, _xsDataDataCollectionScalingStatistics):
        """Creates an entry in the ISPyB DataCollectionScalingStatistics table"""
        strScalingStatisticsType = _xsDataDataCollectionScalingStatistics.getScalingStatisticsType()
        strComments = ""
        fResolutionLimitLow = self.getValue(_xsDataDataCollectionScalingStatistics.getResolutionLimitLow(), -1.0)
        fResolutionLimitHigh = self.getValue(_xsDataDataCollectionScalingStatistics.getResolutionLimitHigh(), -1.0)
        fRmerge = self.getValue(_xsDataDataCollectionScalingStatistics.getRMerge(), -1.0)
        fRmeasWithinIplusIminus = self.getValue(_xsDataDataCollectionScalingStatistics.getRmeasWithinIplusIminus(), -1.0)
        fRmeasAllIplusIminus = self.getValue(_xsDataDataCollectionScalingStatistics.getRmeasAllIplusIminus(), -1.0)
        fRpimWithinIplusIminus = self.getValue(_xsDataDataCollectionScalingStatistics.getRpimWithinIplusIminus(), -1.0)
        fRpimAllIplusIminus = self.getValue(_xsDataDataCollectionScalingStatistics.getRpimAllIplusIminus(), -1.0)
        fFractionalPartialBias = self.getValue(_xsDataDataCollectionScalingStatistics.getFractionalPartialBias(), -1.0)
        iNtotalObservations = int(self.getValue(_xsDataDataCollectionScalingStatistics.getNTotalObservations(), 0))
        iNtotalUniqueObservations = self.getValue(_xsDataDataCollectionScalingStatistics.getNtotalUniqueObservations(), 0)
        fMeanIoverSigI = self.getValue(_xsDataDataCollectionScalingStatistics.getMeanIOverSigI(), -1.0)
        fCompleteness = self.getValue(_xsDataDataCollectionScalingStatistics.getCompleteness(), -1.0)
        fMultiplicity = self.getValue(_xsDataDataCollectionScalingStatistics.getMultiplicity(), -1.0)
        fAnomalousCompleteness = self.getValue(_xsDataDataCollectionScalingStatistics.getAnomalousCompleteness(), -1.0)
        fAnomalousMultiplicity = self.getValue(_xsDataDataCollectionScalingStatistics.getAnomalousMultiplicity(), -1.0)
        recordTimeStamp = DateTime(datetime.datetime.now())
        iDataCollectionScalingId = self.iDataCollectionScalingId
        iDataCollectionScalingStatisticsId = _clientToolsForMXCubeWebService.service.storeDataCollectionScalingStatistic(
                in0=strScalingStatisticsType, \
                in1=strComments, \
                in2=fResolutionLimitLow, \
                in3=fResolutionLimitHigh, \
                in4=fRmerge, \
                in5=fRmeasWithinIplusIminus, \
                in6=fRmeasAllIplusIminus, \
                in7=fRpimWithinIplusIminus, \
                in8=fRpimAllIplusIminus, \
                in9=fFractionalPartialBias, \
                in10=iNtotalObservations, \
                in11=iNtotalUniqueObservations, \
                in12=fMeanIoverSigI, \
                in13=fCompleteness, \
                in14=fMultiplicity, \
                in15=fAnomalousCompleteness, \
                in16=fAnomalousMultiplicity, \
                in17=recordTimeStamp, \
                in18=iDataCollectionScalingId \
                )
        self.DEBUG("DataCollectionScalingStatisticsId: %r" % iDataCollectionScalingStatisticsId)
        return iDataCollectionScalingStatisticsId


    def storeDataCollectionScaling_has_IntId(self, _clientToolsForMXCubeWebService):
        """Creates an entry in the ISPyB storeDataCollectionScaling_has_IntId table"""
        iDataCollectionIntegrationId = self.iDataCollectionIntegrationId
        iDataCollectionScalingId = self.iDataCollectionScalingId
        recordTimeStamp = DateTime(datetime.datetime.now())
        iDataCollectionScaling_has_intId = _clientToolsForMXCubeWebService.service.storeDataCollectionScalingHasInt(
                in0=iDataCollectionIntegrationId, \
                in1=iDataCollectionScalingId, \
                in2=recordTimeStamp \
                )
        self.DEBUG("DataCollectionScaling_has_IntId: %r" % iDataCollectionScaling_has_intId)
        return iDataCollectionScaling_has_intId

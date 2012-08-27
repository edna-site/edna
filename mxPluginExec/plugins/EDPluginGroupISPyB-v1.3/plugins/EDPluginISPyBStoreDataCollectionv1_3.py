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
__status__ = "deprecated"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_3 import XSDataInputStoreDataCollection
from XSDataISPyBv1_3 import XSDataResultStoreDataCollection

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
        self.strToolsForCollectionWebServiceWsdl = None
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
        self.strToolsForCollectionWebServiceWsdl = self.getStringConfigurationParameterValue("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreDataCollectionv1_3.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()


    def process(self, _edObject=None):
        """
        Stores the contents of the DataCollectionContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.process")
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


    def storeDataCollectionProgram(self, _clientToolsForCollectionWebService, _xsDataInputStoreDataCollection):
        """Creates an entry in the ISPyB DataCollectionProgram table"""
        self.DEBUG("EDPluginISPyBStoreDataCollectionv1_3.storeDataCollectionProgram")

        dataCollection = _xsDataInputStoreDataCollection.getDataCollection()

        dataCollectionId = self.getValue(dataCollection.getDataCollectionId(), 0) # integer
        blSampleId = self.getValue(dataCollection.getBlSampleId(), 0) # integer
        sessionId = self.getValue(dataCollection.getSessionId()) # integer
        experimentType = self.getValue(dataCollection.getExperimentType()) # string
        dataCollectionNumber = self.getValue(dataCollection.getDataCollectionNumber()) # integer
        startDate = DateTime(self.getValue(dataCollection.getStartDate())) # string
        endDate = DateTime(self.getValue(dataCollection.getEndDate())) # string
        runStatus = self.getValue(dataCollection.getRunStatus()) # string
        rotationAxis = self.getValue(dataCollection.getRotationAxis()) # string
        phiStart = self.getValue(dataCollection.getPhiStart()) # float
        kappaStart = self.getValue(dataCollection.getKappaStart()) # float
        omegaStart = self.getValue(dataCollection.getOmegaStart()) # float
        axisStart = self.getValue(dataCollection.getAxisStart()) # float
        axisEnd = self.getValue(dataCollection.getAxisEnd()) # float
        axisRange = self.getValue(dataCollection.getAxisRange()) # float
        overlap = self.getValue(dataCollection.getOverlap()) # float
        numberOfImages = self.getValue(dataCollection.getNumberOfImages()) # integer
        startImageNumber = self.getValue(dataCollection.getStartImageNumber()) # integer
        numberOfPasses = self.getValue(dataCollection.getNumberOfPasses()) # integer
        exposureTime = self.getValue(dataCollection.getExposureTime()) # float
        imageDirectory = self.getValue(dataCollection.getImageDirectory()) # string
        imagePrefix = self.getValue(dataCollection.getImagePrefix()) # string
        imageSuffix = self.getValue(dataCollection.getImageSuffix()) # string
        fileTemplate = self.getValue(dataCollection.getFileTemplate()) # string
        wavelength = self.getValue(dataCollection.getWavelength()) # float
        resolution = self.getValue(dataCollection.getResolution()) # float
        resolutionAtCorner = self.getValue(dataCollection.getResolutionAtCorner()) # float
        detectorDistance = self.getValue(dataCollection.getDetectorDistance()) # float
        detector2theta = self.getValue(dataCollection.getDetector2theta()) # float
        detectorMode = self.getValue(dataCollection.getDetectorMode()) # string
        undulatorGap1 = self.getValue(dataCollection.getUndulatorGap1()) # float
        undulatorGap2 = self.getValue(dataCollection.getUndulatorGap2()) # float
        undulatorGap3 = self.getValue(dataCollection.getUndulatorGap3()) # float
        xbeam = self.getValue(dataCollection.getXbeam()) # float
        ybeam = self.getValue(dataCollection.getYbeam()) # float
        crystalClass = self.getValue(dataCollection.getCrystalClass()) # string
        slitGapVertical = self.getValue(dataCollection.getSlitGapVertical()) # float
        slitGapHorizontal = self.getValue(dataCollection.getSlitGapHorizontal()) # float
        beamSizeAtSampleX = self.getValue(dataCollection.getBeamSizeAtSampleX()) # float
        beamSizeAtSampleY = self.getValue(dataCollection.getBeamSizeAtSampleY()) # float
        transmission = self.getValue(dataCollection.getTransmission()) # float
        synchrotronMode = self.getValue(dataCollection.getSynchrotronMode()) # string
        centeringMethod = self.getValue(dataCollection.getCenteringMethod()) # string
        averageTemperature = self.getValue(dataCollection.getAverageTemperature()) # float
        comments = self.getValue(dataCollection.getComments()) # string
        #printableForReport = str(self.getValue(dataCollection.getPrintableForReport())).lower() # boolean
        if self.getValue(dataCollection.getPrintableForReport()):
            printableForReport = 1
        else:
            printableForReport = 0
        xtalSnapshotFullPath1 = self.getValue(dataCollection.getXtalSnapshotFullPath1()) # string
        xtalSnapshotFullPath2 = self.getValue(dataCollection.getXtalSnapshotFullPath2()) # string
        xtalSnapshotFullPath3 = self.getValue(dataCollection.getXtalSnapshotFullPath3()) # string
        xtalSnapshotFullPath4 = self.getValue(dataCollection.getXtalSnapshotFullPath4()) # string
        beamShape = self.getValue(dataCollection.getBeamShape()) # string

        dcargs = dict(in1=dataCollectionId,
                      in2=blSampleId,
                      in3=sessionId,
                      in4=experimentType,
                      in5=dataCollectionNumber,
                      in6=startDate,
                      in7=endDate,
                      in8=runStatus,
                      in9=rotationAxis,
                      in10=phiStart,
                      in11=kappaStart,
                      in12=omegaStart,
                      in13=axisStart,
                      in14=axisEnd,
                      in15=axisRange,
                      in16=overlap,
                      in17=numberOfImages,
                      in18=startImageNumber,
                      in19=numberOfPasses,
                      in20=exposureTime,
                      in21=imageDirectory,
                      in22=imagePrefix,
                      in23=imageSuffix,
                      in24=fileTemplate,
                      in25=wavelength,
                      in26=resolution,
                      in27=resolutionAtCorner,
                      in28=detectorDistance,
                      in29=detector2theta,
                      in30=detectorMode,
                      in31=undulatorGap1,
                      in32=undulatorGap2,
                      in33=undulatorGap3,
                      in34=xbeam,
                      in35=ybeam,
                      in36=crystalClass,
                      in37=slitGapVertical,
                      in38=slitGapHorizontal,
                      in39=beamSizeAtSampleX,
                      in40=beamSizeAtSampleY,
                      in41=transmission,
                      in42=synchrotronMode,
                      in43=centeringMethod,
                      in44=averageTemperature,
                      in45=comments,
                      in46=printableForReport,
                      in47=xtalSnapshotFullPath1,
                      in48=xtalSnapshotFullPath2,
                      in49=xtalSnapshotFullPath3,
                      in50=xtalSnapshotFullPath4,
                      in51=beamShape)
        
        ks = dcargs.keys()
        ks.sort()
#        for k in ks:
#            print '%s=%s (type %s)'%(k,dcargs[k], type(dcargs[k]))

        iDataCollectionId = _clientToolsForCollectionWebService.service.storeOrUpdateDataCollection(in0=dataCollectionId,
                                                                                                in1=blSampleId,
                                                                                                in2=sessionId,
                                                                                                in3=experimentType,
                                                                                                in4=dataCollectionNumber,
                                                                                                in5=startDate,
                                                                                                in6=endDate,
                                                                                                in7=runStatus,
                                                                                                in8=rotationAxis,
                                                                                                in9=phiStart,
                                                                                                in10=kappaStart,
                                                                                                in11=omegaStart,
                                                                                                in12=axisStart,
                                                                                                in13=axisEnd,
                                                                                                in14=axisRange,
                                                                                                in15=overlap,
                                                                                                in16=numberOfImages,
                                                                                                in17=startImageNumber,
                                                                                                in18=numberOfPasses,
                                                                                                in19=exposureTime,
                                                                                                in20=imageDirectory,
                                                                                                in21=imagePrefix,
                                                                                                in22=imageSuffix,
                                                                                                in23=fileTemplate,
                                                                                                in24=wavelength,
                                                                                                in25=resolution,
                                                                                                in26=resolutionAtCorner,
                                                                                                in27=detectorDistance,
                                                                                                in28=detector2theta,
                                                                                                in29=detectorMode,
                                                                                                in30=undulatorGap1,
                                                                                                in31=undulatorGap2,
                                                                                                in32=undulatorGap3,
                                                                                                in33=xbeam,
                                                                                                in34=ybeam,
                                                                                                in35=crystalClass,
                                                                                                in36=slitGapVertical,
                                                                                                in37=slitGapHorizontal,
                                                                                                in38=beamSizeAtSampleX,
                                                                                                in39=beamSizeAtSampleY,
                                                                                                in40=transmission,
                                                                                                in41=synchrotronMode,
                                                                                                in42=centeringMethod,
                                                                                                in43=averageTemperature,
                                                                                                in44=comments,
                                                                                                in45=printableForReport,
                                                                                                in46=xtalSnapshotFullPath1,
                                                                                                in47=xtalSnapshotFullPath2,
                                                                                                in48=xtalSnapshotFullPath3,
                                                                                                in49=xtalSnapshotFullPath4,
                                                                                                in50=beamShape)
        self.DEBUG("DataCollectionProgramId: %r" % iDataCollectionId)
        return iDataCollectionId


#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os
from EDVerbose             import EDVerbose
from EDPluginControl       import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDMessage             import EDMessage
from XSDataCommon          import XSDataFile, XSDataLength, XSDataString, XSDataInteger, XSDataAngle, XSDataBoolean, XSDataDouble
from XSDataDiffractionCTv1 import XSDataInputPowderIntegration
from XSDataDiffractionCTv1 import XSDataResultPowderIntegration
from EDUtilsUnit           import EDUtilsUnit
EDFactoryPluginStatic.loadModule("XSDataSPDv1_0")
from XSDataSPDv1_0 import XSDataInputSPDCake, XSDataResultSPDCake



class EDPluginControlDCTPowderIntegrationv1_1(EDPluginControl):
    """
    This is the plugin-control for Diffraction CT for doing the azimuthal integration of images
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputPowderIntegration)
        self.m_edStringControlledPluginName = "EDPluginSPDCakev1_5"
        self.m_edPluginPowderIntegration = None
        self.xsDataResultPowderIntegration = XSDataResultPowderIntegration()



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        """
        The pre-process of ED Plugin Control DiffractionCT Powder Integration consists in preparing the input data for SPD Cake. 
        and declares the execution plugin as EDPluginFit2DCacke
        """
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.preProcess")
        # Load the execution plugin
        self.m_edPluginPowderIntegration = self.loadPlugin(self.m_edStringControlledPluginName)
        #Retrive its'datamodel

        xsDataInputSPDCake = XSDataInputSPDCake()

        instrumentParameters = self.getDataInput().getInstrumentParameters()
        imageParameters = self.getDataInput().getImageParameters()

        xsDataInputSPDCake.setInputFile(self.getDataInput().getImageFile())

        xsDataInputSPDCake.setWavelength(instrumentParameters.get_diffrn_radiation_wavelength())

        xsDataInputSPDCake.setSampleToDetectorDistance(instrumentParameters.get_pd_instr_dist_spec_detc())


        xsDataInputSPDCake.setAngleOfTilt(imageParameters.get_pd_instr_special_details_tilt_angle())
        xsDataInputSPDCake.setTiltRotation(imageParameters.get_pd_instr_special_details_tilt_rotation())

        xsDataInputSPDCake.setDarkCurrentImageFile(imageParameters.get_file_correction_image_dark_current())
        xsDataInputSPDCake.setFlatFieldImageFile(imageParameters.get_file_correction_image_flat_field())
        xsDataInputSPDCake.setSpatialDistortionFile(imageParameters.get_file_correction_spline_spatial_distortion())

#        EDVerbose.screen("imageParameters.get_array_element_size_1: %s" % imageParameters.get_array_element_size_1().marshal())
        xsDataInputSPDCake.setBeamCentreInPixelsX(XSDataDouble(\
                            EDUtilsUnit.getSIValue(imageParameters.get_diffrn_detector_element_center_1()) / \
                            EDUtilsUnit.getSIValue(imageParameters.get_array_element_size_1())))
        xsDataInputSPDCake.setBeamCentreInPixelsY(XSDataDouble(\
                            EDUtilsUnit.getSIValue(imageParameters.get_diffrn_detector_element_center_2()) / \
                            EDUtilsUnit.getSIValue(imageParameters.get_array_element_size_2())))
        xsDataInputSPDCake.setPixelSizeX(imageParameters.get_array_element_size_1())
                            #imageParameters.get_diffrn_detector_element_center_1())
        xsDataInputSPDCake.setPixelSizeY(imageParameters.get_array_element_size_2())
                            #imageParameters.get_diffrn_detector_element_center_1())

        xsDataInputSPDCake.setBufferSizeX(XSDataInteger(2048))
        xsDataInputSPDCake.setBufferSizeY(XSDataInteger(2048))
        xsDataInputSPDCake.setStartAzimuth(XSDataAngle(0))
        xsDataInputSPDCake.setStopAzimuth(XSDataAngle(360))
        xsDataInputSPDCake.setStepAzimuth(XSDataAngle(360))
        xsDataInputSPDCake.setOutputDirCake(self.getDataInput().getDestinationDir())
        xsDataInputSPDCake.setDeleteCorImg(XSDataBoolean(True))

        try:
            self.m_edPluginPowderIntegration.setDataInput(xsDataInputSPDCake)
        except Exception, error:
           # This exception handling needs to be rethought, see bug #43.
            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlDCTPowderIntegrationv1_1.preProcess: Unexpected error in SPD handler: ", error)
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage



    def process(self, _edObject=None):
        """ Does the job"""
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.process")
        self.m_edPluginPowderIntegration.connectSUCCESS(self.doSuccessExecPowderIntegration)
        self.m_edPluginPowderIntegration.connectFAILURE(self.doFailureExecPowderIntegration)
        self.m_edPluginPowderIntegration.executeSynchronous()


    def postProcess(self, _edObject=None):
        """The post processing of DCT powder integration is mainly to integrate the metadata concerning instrument geometry to the output CIF file"""
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.postProcess")
#        try:
#            xsDataPathToCakedFile = self.m_edPluginPowderIntegration.getDataOutput().getResultFile()
#        except Exception, error:
#            # This exception handling needs to be rethought, see bug #43.
#            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlDCTPowderIntegrationv1_1.postProcess: Unexpected error in SPD handler: ", error)
#            EDVerbose.error(errorMessage)
#            self.addErrorMessage(errorMessage)
#            raise RuntimeError, errorMessage

        self.setDataOutput(self.xsDataResultPowderIntegration)



    def doSuccessExecPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.doSuccessExecPowderIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDCTPowderIntegrationv1_1.doSuccessExecPowderIntegration")
#        EDVerbose.DEBUG(self.m_edPluginPowderIntegration.getDataOutput().mashal())
        self.xsDataResultPowderIntegration.setIntegratedIntensities(self.m_edPluginPowderIntegration.getDataOutput().getCakedFile())

    def doFailureExecPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDCTPowderIntegrationv1_1.doFailureExecPowderIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDCTPowderIntegrationv1_1.doFailureExecPowderIntegration")
        self.setFailure()

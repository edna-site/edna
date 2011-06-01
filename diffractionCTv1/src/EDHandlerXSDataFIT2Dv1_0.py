# coding: utf8
#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id: EDHandlerXSDataBestv10.py 698 2009-05-11 10:43:08Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:  Jérøme Kieffer (jerome.kieffer@esrf.fr)    
#                        Olof Svensson (svensson@esrf.fr) 
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


from EDObject                    import EDObject
from EDFactoryPluginStatic       import EDFactoryPluginStatic
from XSDataCommon import XSDataLength , XSDataInteger, XSDataString
EDFactoryPluginStatic.loadModule("XSDataFIT2Dv1_0")
from XSDataFIT2Dv1_0 import XSDataInputFIT2DCake
EDFactoryPluginStatic.loadModule("XSDataDiffractionCTv1")
from XSDataDiffractionCTv1          import XSDataResultPowderIntegration


class EDHandlerXSDataFIT2Dv1_0(EDObject):
    """
    """
    def getXSDataInputFIT2DCake(self, _xsDataInputPowderIntegration):
        """
        """

        xsDataInputFIT2DCake = XSDataInputFIT2DCake()

        imageFile = _xsDataInputPowderIntegration.getImageFile()
        instrumentParameters = _xsDataInputPowderIntegration.getInstrumentParameters()
        imageParameters = _xsDataInputPowderIntegration.getImageParameters()

        xsDataInputFIT2DCake.setInputFile(imageFile)

        xsDataInputFIT2DCake.setWavelength(instrumentParameters.get_diffrn_radiation_wavelength())
        xsDataInputFIT2DCake.setSampleToDetectorDistance(instrumentParameters.get_pd_instr_dist_spec_detc())

        xsDataInputFIT2DCake.setAngleOfTilt(imageParameters.get_pd_instr_special_details_tilt_angle())
        xsDataInputFIT2DCake.setTiltRotation(imageParameters.get_pd_instr_special_details_tilt_rotation())

        xsDataInputFIT2DCake.setDarkCurrentImageFile(imageParameters.get_file_correction_image_dark_current())
        xsDataInputFIT2DCake.setFlatFieldImageFile(imageParameters.get_file_correction_image_flat_field())
        xsDataInputFIT2DCake.setSpatialDistortionFile(imageParameters.get_file_correction_spline_spatial_distortion())

        fBeamCentreInMillimetersX = imageParameters.get_diffrn_detector_element_center_1().getValue()
        fBeamCentreInMillimetersY = imageParameters.get_diffrn_detector_element_center_2().getValue()
        fPixelSizeInMetersX = imageParameters.get_array_element_size_1().getValue()
        fPixelSizeInMetersY = imageParameters.get_array_element_size_2().getValue()
        xsDataInputFIT2DCake.setBeamCentreInPixelsX(XSDataLength(fBeamCentreInMillimetersX / fPixelSizeInMetersX / 1000))
        xsDataInputFIT2DCake.setBeamCentreInPixelsY(XSDataLength(fBeamCentreInMillimetersY / fPixelSizeInMetersX / 1000))
        xsDataInputFIT2DCake.setPixelSizeX(XSDataLength(fPixelSizeInMetersX * 1000))
        xsDataInputFIT2DCake.setPixelSizeY(XSDataLength(fPixelSizeInMetersY * 1000))

        xsDataInputFIT2DCake.setBufferSizeX(XSDataInteger(2048))
        xsDataInputFIT2DCake.setBufferSizeY(XSDataInteger(2048))
        xsDataInputFIT2DCake.setOutputFileType(XSDataString("CHIPLOT"))

        return xsDataInputFIT2DCake



    def getXSDataResultPowderIntegration(self, _xsDataResultFIT2DCake):
        """
        """
        xsDataResultPowderIntegration = XSDataResultPowderIntegration()
        xsDataResultPowderIntegration.setIntegratedIntensities(_xsDataResultFIT2DCake.getResultFile())

        return xsDataResultPowderIntegration

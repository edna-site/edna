#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

import os
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDUtilsFile        import EDUtilsFile

from XSDataDiffractionCTv1 import XSDataInputDiffractionCT
from XSDataDiffractionCTv1 import XSDataResultDiffractionCT
from XSDataDiffractionCTv1 import XSDataInputReadHeader
from XSDataDiffractionCTv1 import XSDataFile
from XSDataDiffractionCTv1 import XSDataDiffractionCTImage
from XSDataDiffractionCTv1 import XSDataDiffractionCTInstrument
from XSDataDiffractionCTv1 import XSDataAngle
from XSDataDiffractionCTv1 import XSDataLength
from XSDataDiffractionCTv1 import XSDataWavelength
from XSDataDiffractionCTv1 import XSDataFlux
from XSDataDiffractionCTv1 import XSDataString
from XSDataDiffractionCTv1 import XSDataDouble
from XSDataDiffractionCTv1 import XSDataInputPowderIntegration
from XSDataDiffractionCTv1 import XSDataInputWriteSinogram


class EDPluginControlDiffractionCTv1_0(EDPluginControl):
    """
    This is the EDNA control plug-in for diffraction contrast tomography. 
    It is  intented to run 2D integration provided by Fit2D for example and ....
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputDiffractionCT)
        self.m_strControlledPluginReadHeader = "EDPluginControlDCTReadHeaderv1_0"
        self.m_edPluginReadHeader = None
        self.m_strControlledPluginPowderIntegration = "EDPluginControlDCTPowderIntegrationv1_0"
        self.m_edPluginPowderIntegration = None
        self.m_xsDataDiffractionCTInstrument = None
        self.m_xsDataDiffractionCTImage = None
        self.m_xsDataFileInputImage = None
        self.m_edPluginControlledPluginWriteSinogram = None
        self.m_strControlledPluginWriteSinogram = "EDPluginDCTWriteSinogramv1_0"
        self.m_xsDataFileInputPowderDiffraction = None
        self.m_xsDataResultDiffractionCT = None
        self.m_edPluginWriteSinogram = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "No path to input image")
        self.checkMandatoryParameters(self.getDataInput().getDestinationDirectory(), "No path to destination directory")
        self.checkMandatoryParameters(self.getDataInput().getSinogramFileNamePrefix(), "No sinogram prefix given")
        self.checkMandatoryParameters(self.getDataInput().getPowderDiffractionSubdirectory(), "No subdirectory prefix for powder diffraction patterns")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.preProcess")
        # Load the execution plugin
        self.m_edPluginReadHeader = self.loadPlugin(self.m_strControlledPluginReadHeader)
        self.m_edPluginPowderIntegration = self.loadPlugin(self.m_strControlledPluginPowderIntegration)
        self.m_edPluginWriteSinogram = self.loadPlugin(self.m_strControlledPluginWriteSinogram)
        # Set the input data for the read header plugin
        xsDataInputReadHeader = XSDataInputReadHeader()
        xsdataStringPathToImage = self.getDataInput().getImage().getPath()
        self.m_xsDataFileInputImage = XSDataFile()
        self.m_xsDataFileInputImage.setPath(xsdataStringPathToImage)
        xsDataInputReadHeader.setInputFile(self.m_xsDataFileInputImage)
        self.m_edPluginReadHeader.setDataInput(xsDataInputReadHeader)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.process")
        self.m_edPluginReadHeader.connectSUCCESS(self.doSuccessReadHeader)
        self.m_edPluginReadHeader.connectFAILURE(self.doFailureReadHeader)
        self.m_edPluginPowderIntegration.connectSUCCESS(self.doSuccessPowderIntegration)
        self.m_edPluginPowderIntegration.connectFAILURE(self.doFailurePowderIntegration)
        self.m_edPluginWriteSinogram.connectSUCCESS(self.doSuccessWriteSinogram)
        self.m_edPluginWriteSinogram.connectFAILURE(self.doFailureWriteSinogram)

        self.m_edPluginReadHeader.executeSynchronous()





    def postProcess(self, _edObject=None):

        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.postProcess")
        self.setDataOutput(self.m_xsDataResultDiffractionCT)


    def doSuccessReadHeader(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doSuccessReadHeader")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doSuccessReadHeader")
        # Translate dictionary to image and instrument objects
        xsDataInputPowderIntegration = XSDataInputPowderIntegration()
        self.m_xsDataDiffractionCTInstrument = XSDataDiffractionCTInstrument()
        self.m_xsDataDiffractionCTImage = XSDataDiffractionCTImage()
        xsDataDictionaryHeader = self.m_edPluginReadHeader.getDataOutput().getDictionary()
        for xsDataKeyValuePair in xsDataDictionaryHeader.getKeyValuePair():
            strKey = str(xsDataKeyValuePair.getKey().getValue())
            strValue = str(xsDataKeyValuePair.getValue().getValue())
            if (strKey == "_diffrn_radiation_wavelength"):
                self.m_xsDataDiffractionCTInstrument.set_diffrn_radiation_wavelength(XSDataWavelength(float(strValue)))
            elif (strKey == "_pd_instr_dist_spec/detc"):
                self.m_xsDataDiffractionCTInstrument.set_pd_instr_dist_spec_detc(XSDataLength(float(strValue)))
            elif (strKey == "_pd_meas_2theta_range_max"):
                self.m_xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_max(XSDataAngle(float(strValue)))
            elif (strKey == "_pd_meas_2theta_range_min"):
                self.m_xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_min(XSDataAngle(float(strValue)))
            elif (strKey == "_pd_meas_2theta_range_inc"):
                self.m_xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_inc(XSDataAngle(float(strValue)))
            elif (strKey == "_synchrotron_photon-flux"):
                self.m_xsDataDiffractionCTInstrument.set_synchrotron_photon_flux(XSDataFlux(float(strValue)))
            elif (strKey == "_synchrotron_ring-intensity"):
                self.m_xsDataDiffractionCTInstrument.set_synchrotron_ring_intensity(XSDataDouble(float(strValue)))
            elif (strKey == "_tomo_scan_ampl"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_scan_ampl(XSDataAngle(float(strValue)))
            elif (strKey == "_tomo_scan_type"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_scan_type(XSDataString(strValue))
            elif (strKey == "_tomo_spec_displ_rotation"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation(XSDataAngle(float(strValue)))
            elif (strKey == "_tomo_spec_displ_rotation_inc"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation_inc(XSDataAngle(float(strValue)))
            elif (strKey == "_tomo_spec_displ_x"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_x(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_x_inc"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_inc(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_x_max"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_max(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_x_min"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_min(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_z"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_z(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_z_inc"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_inc(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_z_max"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_max(XSDataLength(float(strValue)))
            elif (strKey == "_tomo_spec_displ_z_min"):
                self.m_xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_min(XSDataLength(float(strValue)))
            elif (strKey == "_pd_instr_special_details_tilt_angle"):
                self.m_xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_angle(XSDataAngle(float(strValue)))
            elif (strKey == "_pd_instr_special_details_tilt_rotation"):
                self.m_xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_rotation(XSDataAngle(float(strValue)))
            elif (strKey == "_array_element_size[1]"):
                self.m_xsDataDiffractionCTImage.set_array_element_size_1(XSDataLength(float(strValue)))
            elif (strKey == "_array_element_size[2]"):
                self.m_xsDataDiffractionCTImage.set_array_element_size_2(XSDataLength(float(strValue)))
            elif (strKey == "_diffrn_detector_element.center[1]"):
                self.m_xsDataDiffractionCTImage.set_diffrn_detector_element_center_1(XSDataLength(float(strValue)))
            elif (strKey == "_diffrn_detector_element.center[2]"):
                self.m_xsDataDiffractionCTImage.set_diffrn_detector_element_center_2(XSDataLength(float(strValue)))

## Here the tricky case of lists ....                 
#            elif strKey.startswith("_pd_sum_2theta_range_max"):
#                if strKey.find("[")>0:
#                    pyintIndex = int(strKey.split("[")[1].split("]")[0]) - 1 #gets the int that is between []
#                else:
#                    pyintIndex = 0
#                while len(self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_max()) < pyintIndex + 1:
#                    self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_max().append(None)
#                self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_max()[pyintIndex] = XSDataAngle(float(strValue))
#            elif strKey.startswith("_pd_sum_2theta_range_min"):
#                if strKey.find("[")>0:
#                    pyintIndex = int(strKey.split("[")[1].split("]")[0]) - 1 #gets the int that is between []
#                else:
#                    pyintIndex = 0
#                while len(self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_min()) < pyintIndex + 1:
#                    self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_min().append(None)
#                self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_min()[pyintIndex] = XSDataAngle(float(strValue))
##end  Seems OK 20091023                              
            elif (strKey == "_file_correction_image_dark-current"):
                xsDataFileDark = XSDataFile()
                xsDataFileDark.setPath(XSDataString(strValue))
                self.m_xsDataDiffractionCTImage.set_file_correction_image_dark_current(xsDataFileDark)
            elif (strKey == "_file_correction_image_flat-field"):
                xsDataFileFlat = XSDataFile()
                xsDataFileFlat.setPath(XSDataString(strValue))
                self.m_xsDataDiffractionCTImage.set_file_correction_image_flat_field(xsDataFileFlat)
            elif (strKey == "_file_correction_image-mask"):
                xsDataFileMask = XSDataFile()
                xsDataFileMask.setPath(XSDataString(strValue))
                self.m_xsDataDiffractionCTImage.set_file_correction_image_mask(xsDataFileMask)
            elif (strKey == "_file_correction_spline_spatial-distortion"):
                xsDataFileSpatialDist = XSDataFile()
                xsDataFileSpatialDist.setPath(XSDataString(strValue))
                self.m_xsDataDiffractionCTImage.set_file_correction_spline_spatial_distortion(xsDataFileSpatialDist)
        xsDataInputPowderIntegration.setImageParameters(self.m_xsDataDiffractionCTImage)
        xsDataInputPowderIntegration.setInstrumentParameters(self.m_xsDataDiffractionCTInstrument)
        xsDataInputPowderIntegration.setImageFile(self.m_xsDataFileInputImage)
        self.m_edPluginPowderIntegration.setDataInput(xsDataInputPowderIntegration)
        self.m_edPluginPowderIntegration.executeSynchronous()


    def doFailureReadHeader(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doFailureReadHeader")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doFailureReadHeader")


    def doSuccessPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doSuccessPowderIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doSuccessPowderIntegration")
        self.m_xsDataResultDiffractionCT = XSDataResultDiffractionCT()
        # Copy file to final destination and add path to result object
        xsDataFileIntegratedIntensities = self.m_edPluginPowderIntegration.getDataOutput().getIntegratedIntensities()
        EDVerbose.DEBUG("Path to cif: " + xsDataFileIntegratedIntensities.getPath().getValue())
        EDVerbose.DEBUG("%s" % xsDataFileIntegratedIntensities)
        if (xsDataFileIntegratedIntensities is not None):
            strOutputFilePath = xsDataFileIntegratedIntensities.getPath().getValue()

            strDestinationDirectory = self.getDataInput().getDestinationDirectory().getPath().getValue()
            strPowderDiffractionSubdirectory = self.getDataInput().getPowderDiffractionSubdirectory().getValue()

            if not     os.path.isdir(strDestinationDirectory):
                        os.mkdir(strDestinationDirectory)

            if self.m_xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() in  ["flat", "spiral"]:
#                pyintLineNumber = int( abs(   float( self.cif[ "_tomo_spec_displ_rotation" ] ) / float( self.cif[ "_tomo_spec_displ_rotation_inc" ] ) ) )
                pyintLineNumber = int(abs(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation().getValue()) / self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation_inc().getValue())
            elif self.m_xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
#                pyintLineNumber = int( abs( ( float( self.cif[ "_tomo_spec_displ_z" ]) - float ( self.cif [ "_tomo_spec_displ_z_min" ] ) ) / float( self.cif["_tomo_spec_displ_z_inc"] ) ) )
                pyintLineNumber = int(abs(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z().getValue() - self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min().getValue()) / self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_inc().getValue())
            else:
                pyintLineNumber = None

            if  pyintLineNumber is not None:
                pystrDestinationSubDir = "%s%04i" % (strPowderDiffractionSubdirectory, pyintLineNumber)
                strDestinationDirectoryWithSub = os.path.join(strDestinationDirectory, pystrDestinationSubDir)
                strDestinationFilePath = os.path.join(strDestinationDirectoryWithSub , os.path.basename(strOutputFilePath))
                if not os.path.isdir(os.path.join(strDestinationDirectoryWithSub)):
                    os.mkdir(strDestinationDirectoryWithSub)
                EDVerbose.DEBUG("Full path should be now: %s" % strDestinationFilePath)
            else:
                EDVerbose.DEBUG("No modification of the output directory: I was not able to determine on which line of the sinogram I am.")
                strDestinationFilePath = os.path.abspath(os.path.join(strDestinationDirectory, EDUtilsFile.getBaseName(strOutputFilePath)))

            EDUtilsFile.copyFile(strOutputFilePath, strDestinationFilePath)
            xsDataFileDestination = XSDataFile()
            xsDataFileDestination.setPath(XSDataString(strDestinationFilePath))
            self.m_xsDataResultDiffractionCT.setIntegratedIntensities(xsDataFileDestination)
            xsDataPathSinogramDirectory = XSDataFile()
            xsDataPathSinogramDirectory.setPath(XSDataString(strDestinationDirectory))

            xsDataInputWriteSinogram = XSDataInputWriteSinogram()
            xsDataInputWriteSinogram.setSinogramDirectory(xsDataPathSinogramDirectory)
            xsDataInputWriteSinogram.setIntegratedIntensities(xsDataFileDestination)
            xsDataInputWriteSinogram.setSinogramFileNamePrefix(self.getDataInput().getSinogramFileNamePrefix())
            self.m_edPluginWriteSinogram.setDataInput(xsDataInputWriteSinogram)
            self.m_edPluginWriteSinogram.executeSynchronous()

    def doFailurePowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doFailurePowderIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doFailurePowderIntegration")

    def doSuccessWriteSinogram(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doSuccessWriteSinogram")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doSuccessWriteSinogram")
        xsDataResultWriteSinogram = self.m_edPluginWriteSinogram.getDataOutput()
        if (xsDataResultWriteSinogram is not None):
            self.m_xsDataResultDiffractionCT.setSinogramFile(xsDataResultWriteSinogram.getSinogramFile())

    def doFailureWriteSinogram(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDiffractionCTv1_0.doFailureWriteSinogram")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_0.doFailureWriteSinogram")

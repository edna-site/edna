# coding: utf8
#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
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


__author__ = "Jérôme Kieffer"
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"


import os
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsUnit            import EDUtilsUnit
from EDConfiguration        import EDConfiguration
from XSDataDiffractionCTv1  import XSDataInputDiffractionCT
from XSDataDiffractionCTv1  import XSDataResultDiffractionCT
from XSDataDiffractionCTv1  import XSDataInputReadHeader
from XSDataDiffractionCTv1  import XSDataDiffractionCTImage
from XSDataDiffractionCTv1  import XSDataDiffractionCTInstrument
from XSDataCommon           import XSDataLength, XSDataWavelength, XSDataFlux, \
                                    XSDataString, XSDataDouble, XSDataAngle, \
                                    XSDataInteger, XSDataFile, XSPluginItem
from XSDataDiffractionCTv1  import XSDataInputPowderIntegration
EDFactoryPluginStatic.loadModule("XSDataHDF5v1_0")
from XSDataHDF5v1_0 import XSDataInputHDF5MapSpectra, XSDataSpectrum, XSDataMeshScan
EDFactoryPluginStatic.loadModule("EDPluginExportAsciiPowderv1_0")
from XSDataEDFv1_0 import XSDataInput1DPowderEDF
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile

class EDPluginControlDiffractionCTv1_2(EDPluginControl):
    """
    This is the EDNA control plug-in for diffraction contrast tomography. 
    It is  intented to run 2D integration provided by SPD for example and create a sinogram as a 3D array in HDF5....
    """
    CONF_INPUT_IMAGE_SIZE = "inputImageSize"

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputDiffractionCT)
        self.strControlledPluginReadHeader = "EDPluginControlDCTReadHeaderv1_0"
        self.strControlledPluginPowderIntegration = "EDPluginControlDCTPowderIntegrationv1_1"
        self.strControlledPluginHDF5MapSpectra = "EDPluginHDF5MapOfSpectrav10"
        self.strControlledPluginExportAsciiPowder = "EDPluginExportAsciiPowderv1_0"
        self.strControlledPluginWait = "EDPluginWaitFile"

        self.edPluginPowderIntegration = None
        self.xsDataDiffractionCTInstrument = None
        self.xsDataDiffractionCTImage = None
        self.xsDataFileInputImage = None
        self.xsDataFileInputPowderDiffraction = None
        self.xsDataResultDiffractionCT = None
        self.edPluginHDF5MapSpectra = None
        self.edPluginExportAsciiPowder = None

        self.xsdForceImageParam = None
        self.xsdForceScanParam = None
        self.powderDiffractionFormat = "edf" #default output format
        self.iImageSize = 100 #Default value

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "No path to input image")
        self.checkMandatoryParameters(self.getDataInput().getDestinationDirectory(), "No path to destination directory")
        self.checkMandatoryParameters(self.getDataInput().getSinogramFileNamePrefix(), "No sinogram prefix given")
        self.checkMandatoryParameters(self.getDataInput().getPowderDiffractionSubdirectory(), "No subdirectory prefix for powder diffraction patterns")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.preProcess")
        # Load the execution plugin
        self.edPluginPowderIntegration = self.loadPlugin(self.strControlledPluginPowderIntegration)
        self.edPluginHDF5MapSpectra = self.loadPlugin(self.strControlledPluginHDF5MapSpectra)
        self.edPluginExportAsciiPowder = self.loadPlugin(self.strControlledPluginExportAsciiPowder)
        sdi = self.getDataInput()
        self.xsDataFileInputImage = self.getDataInput().getImage()
        self.xsdForceImageParam = sdi.getOverrideImageParam()
        self.xsdForceScanParam = sdi.getOverrideScanParam()
        if sdi.getPowderDiffractionFormat() is not None:
            self.powderDiffractionFormat = sdi.getPowderDiffractionFormat().getValue()


    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters
         - Excpected image size
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            EDVerbose.warning("EDPluginControlDiffractionCTv1_2.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()
        strImageSize = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginControlDiffractionCTv1_2.CONF_INPUT_IMAGE_SIZE)
        if(strImageSize == None):
            EDVerbose.WARNING("EDPluginControlDiffractionCTv1_2.configure: No configuration parameter found for: %s, using default value: %s " % (\
                         EDPluginControlDiffractionCTv1_2.CONF_INPUT_IMAGE_SIZE, self.iImageSize))
        else:
            self.iImageSize = int(strImageSize)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.process")
#===============================================================================
# Wait File
#===============================================================================
        edPluginWaitFile = self.loadPlugin(self.strControlledPluginWait)
        xsdin = XSDataInputWaitFile()
        xsdin.setExpectedFile(self.xsDataFileInputImage)
        xsdin.setExpectedSize(XSDataInteger(self.iImageSize))
        edPluginWaitFile.setDataInput(xsdin)
        edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        edPluginWaitFile.executeSynchronous()

#===============================================================================
# #ReadHeader
#===============================================================================

        edPluginReadHeader = self.loadPlugin(self.strControlledPluginReadHeader)
        # Set the input data for the read header plugin
        xsDataInputReadHeader = XSDataInputReadHeader()

        xsDataInputReadHeader.setInputFile(self.xsDataFileInputImage)
        edPluginReadHeader.setDataInput(xsDataInputReadHeader)

        edPluginReadHeader.connectSUCCESS(self.doSuccessReadHeader)
        edPluginReadHeader.connectFAILURE(self.doFailureReadHeader)

        edPluginReadHeader.executeSynchronous()

################################################################################
# Powder Integration
################################################################################

        self.edPluginPowderIntegration.connectSUCCESS(self.doSuccessPowderIntegration)
        self.edPluginPowderIntegration.connectFAILURE(self.doFailurePowderIntegration)
        self.edPluginPowderIntegration.executeSynchronous()


        self.edPluginHDF5MapSpectra.connectSUCCESS(self.doSuccessWriteSinogram)
        self.edPluginHDF5MapSpectra.connectFAILURE(self.doFailureWriteSinogram)
        self.edPluginHDF5MapSpectra.execute()

        self.edPluginExportAsciiPowder.connectSUCCESS(self.doSuccessExportAsciiPowder)
        self.edPluginExportAsciiPowder.connectFAILURE(self.doFailureExportAsciiPowder)
        self.edPluginExportAsciiPowder.execute()


    def postProcess(self, _edObject=None):

        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.postProcess")
        self.synchronizePlugins()
        self.setDataOutput(self.xsDataResultDiffractionCT)


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doSuccessWaitFile")


    def doFailureWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doFailureWaitFile")
        EDVerbose.ERROR("Failure in WaitFile of %s " % _edPlugin.getDataInput().marshal())
        self.setFailure()

    def doSuccessReadHeader(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doSuccessReadHeader")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doSuccessReadHeader")
        # Translate dictionary to image and instrument objects
        xsDataInputPowderIntegration = XSDataInputPowderIntegration()
        self.xsDataDiffractionCTInstrument = XSDataDiffractionCTInstrument()
        self.xsDataDiffractionCTImage = XSDataDiffractionCTImage()
        xsdOut = _edPlugin.getDataOutput()
        if xsdOut is None:
            strErr = "EDPluginControlDiffractionCTv1_2.doSuccessReadHeader: xsdataResult is None"
            EDVerbose.ERROR(strErr)
            self.setFailure()
            raise RuntimeError(strErr)
        xsDataDictionaryHeader = xsdOut.getDictionary()
        for xsDataKeyValuePair in xsDataDictionaryHeader.getKeyValuePair():
            strKey = str(xsDataKeyValuePair.getKey().getValue())
            lstValue = xsDataKeyValuePair.getValue().getValue().split()
            if len(lstValue) == 2:
                strValue = lstValue[0]
                strUnit = lstValue[1]
            else:
                strValue = xsDataKeyValuePair.getValue().getValue()
                strUnit = None

            if (strKey == "_diffrn_radiation_wavelength"):
                xsd = EDUtilsUnit.toXSD(XSDataWavelength, strValue)
                self.xsDataDiffractionCTInstrument.set_diffrn_radiation_wavelength(xsd)
            elif (strKey == "_pd_instr_dist_spec/detc"):
                xsd = EDUtilsUnit.toXSD(XSDataLength, strValue)
                self.xsDataDiffractionCTInstrument.set_pd_instr_dist_spec_detc(xsd)
            elif (strKey == "_pd_meas_2theta_range_max"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_max(xsd)
            elif (strKey == "_pd_meas_2theta_range_min"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_min(xsd)
            elif (strKey == "_pd_meas_2theta_range_inc"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_inc(xsd)
            elif (strKey == "_synchrotron_photon-flux"):
                self.xsDataDiffractionCTInstrument.set_synchrotron_photon_flux(XSDataFlux(float(strValue)))
            elif (strKey == "_synchrotron_ring-intensity"):
                self.xsDataDiffractionCTInstrument.set_synchrotron_ring_intensity(XSDataDouble(float(strValue)))
            elif (strKey == "_tomo_scan_ampl"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_scan_ampl(xsd)
            elif (strKey == "_tomo_scan_type"):
                self.xsDataDiffractionCTInstrument.set_tomo_scan_type(XSDataString(strValue))
            elif (strKey == "_tomo_spec_displ_rotation"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation(xsd)
            elif (strKey == "_tomo_spec_displ_rotation_inc"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation_inc(xsd)
            elif (strKey == "_tomo_spec_displ_x"):
                xsd = EDUtilsUnit.toXSD(XSDataLength, strValue)
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x(xsd)
            elif (strKey == "_tomo_spec_displ_x_inc"):
                xsd = EDUtilsUnit.toXSD(XSDataLength, strValue)
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_inc(xsd)
            elif (strKey == "_tomo_spec_displ_x_max"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_max(xsd)
            elif (strKey == "_tomo_spec_displ_x_min"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_min(xsd)
            elif (strKey == "_tomo_spec_displ_z"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z(xsd)
            elif (strKey == "_tomo_spec_displ_z_inc"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_inc(xsd)
            elif (strKey == "_tomo_spec_displ_z_max"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_max(xsd)
            elif (strKey == "_tomo_spec_displ_z_min"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_min(xsd)
            elif (strKey == "_pd_instr_special_details_tilt_angle"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_angle(xsd)
            elif (strKey == "_pd_instr_special_details_tilt_rotation"):
                xsd = XSDataAngle(float(strValue))
                if strUnit is None: strUnit = "deg"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_rotation(xsd)
            elif (strKey == "_array_element_size[1]"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "m"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_array_element_size_1(xsd)
            elif (strKey == "_array_element_size[2]"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "m"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_array_element_size_2(xsd)
            elif (strKey == "_diffrn_detector_element.center[1]"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_diffrn_detector_element_center_1(xsd)
            elif (strKey == "_diffrn_detector_element.center[2]"):
                xsd = XSDataLength(float(strValue))
                if strUnit is None: strUnit = "mm"
                xsd.setUnit(XSDataString(strUnit))
                self.xsDataDiffractionCTImage.set_diffrn_detector_element_center_2(xsd)
            elif (strKey == "_file_correction_image_dark-current"):
                    xsDataFileDark = XSDataFile()
                    xsDataFileDark.setPath(XSDataString(strValue))
                    self.xsDataDiffractionCTImage.set_file_correction_image_dark_current(xsDataFileDark)
            elif (strKey == "_file_correction_image_flat-field"):
                xsDataFileFlat = XSDataFile()
                xsDataFileFlat.setPath(XSDataString(strValue))
                self.xsDataDiffractionCTImage.set_file_correction_image_flat_field(xsDataFileFlat)
            elif (strKey == "_file_correction_image-mask"):
                xsDataFileMask = XSDataFile()
                xsDataFileMask.setPath(XSDataString(strValue))
                self.xsDataDiffractionCTImage.set_file_correction_image_mask(xsDataFileMask)
            elif (strKey == "_file_correction_spline_spatial-distortion"):
                xsDataFileSpatialDist = XSDataFile()
                xsDataFileSpatialDist.setPath(XSDataString(strValue))
                self.xsDataDiffractionCTImage.set_file_correction_spline_spatial_distortion(xsDataFileSpatialDist)

        if self.xsdForceImageParam is not None:
            self.forceImageParam(self.xsdForceImageParam)

        if self.xsdForceScanParam is not None:
            self.forceScanParam(self.xsdForceScanParam)


        xsDataInputPowderIntegration.setImageParameters(self.xsDataDiffractionCTImage)
        xsDataInputPowderIntegration.setInstrumentParameters(self.xsDataDiffractionCTInstrument)
        xsDataInputPowderIntegration.setImageFile(self.xsDataFileInputImage)


# Set the destination directory for output  XRPD file

        strDestinationDirectory = os.path.join(self.getDataInput().getDestinationDirectory().getPath().getValue(), \
                                               self.getDataInput().getPowderDiffractionSubdirectory().getValue())

        if self.xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() in  ["flat", "spiral"]:
            pyintLineNumber = int(abs(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation().getValue()) / self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation_inc().getValue())
        elif self.xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
            pyintLineNumber = int(abs(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z().getValue() - self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min().getValue()) / self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_inc().getValue())
        else:
            pyintLineNumber = None
        try:
            strDestinationDirectory = "%s%04i" % (strDestinationDirectory, pyintLineNumber)
        except TypeError:
            pass #if pyintLineNumber is none: do not add suffix


        xsDataInputPowderIntegration.setDestinationDir(XSDataFile(XSDataString(strDestinationDirectory)))
        self.edPluginPowderIntegration.setDataInput(xsDataInputPowderIntegration)


    def doFailureReadHeader(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doFailureReadHeader")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doFailureReadHeader")
        self.setFailure()

    def doSuccessPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doSuccessPowderIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doSuccessPowderIntegration")

        self.xsDataResultDiffractionCT = XSDataResultDiffractionCT()

        xsDataFileIntegratedIntensities = _edPlugin.getDataOutput().getIntegratedIntensities()
        if (xsDataFileIntegratedIntensities is not None):
#            EDVerbose.DEBUG(self.edPluginPowderIntegration.getDataOutput().mashal())
            xsdPathFileIntegratedIntensities = xsDataFileIntegratedIntensities.getPath()

            if self.powderDiffractionFormat == "edf":
                self.xsDataResultDiffractionCT.setIntegratedIntensities(xsDataFileIntegratedIntensities)
            else:
                xsdInput1DPowderEDF = XSDataInput1DPowderEDF()
                xsdInput1DPowderEDF.setEdfFile(xsDataFileIntegratedIntensities)
                xsdOutFile = XSDataFile()
                xsdOutFile.setPath(XSDataString(os.path.splitext(xsdPathFileIntegratedIntensities.getValue())[0] + "." + self.powderDiffractionFormat))
                xsdInput1DPowderEDF.setOutputFile(xsdOutFile)
                xsdInput1DPowderEDF.setOutputFormat(XSDataString(self.powderDiffractionFormat))

                self.edPluginExportAsciiPowder.setDataInput(xsdInput1DPowderEDF)



            xsDataInputHDF5MapSpectra = XSDataInputHDF5MapSpectra()

            xsDataMesh = XSDataMeshScan()

            xsDataSpectrum = XSDataSpectrum()
            xsDataSpectrum.setPath(xsdPathFileIntegratedIntensities)
            strDestinationFile = os.path.join(self.getDataInput().getDestinationDirectory().getPath().getValue(), \
                                              self.getDataInput().getSinogramFileNamePrefix().getValue() + ".h5")


            xsDataPathSinogram = XSDataFile()
            xsDataPathSinogram.setPath(XSDataString(strDestinationFile))
            xsDataInputHDF5MapSpectra.setHDF5File(xsDataPathSinogram)

            xsDataInputHDF5MapSpectra.setInternalHDF5Path(XSDataString("RawDCT"))


            if self.xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() in  ["flat", "spiral"]:
                xsDataSpectrum.setFastMotorPosition(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x())
                xsDataMesh.setFastMotorStart(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min())
                xsDataMesh.setFastMotorStop(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max())
                xsSteps = XSDataInteger(int(round(\
                         (self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max().getValue() - \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min().getValue()) / \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_inc().getValue() \
                                                  )))
                xsDataMesh.setFastMotorSteps(xsSteps)
                xsDataMesh.setSlowMotorStart(XSDataDouble(0.0))
                xsDataMesh.setSlowMotorStop(self.xsDataDiffractionCTInstrument.get_tomo_scan_ampl())
                xsSteps = XSDataInteger(int(round(\
                                self.xsDataDiffractionCTInstrument.get_tomo_scan_ampl().getValue() / \
                                self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation_inc().getValue())))
                xsDataMesh.setSlowMotorSteps(xsSteps)
                xsDataSpectrum.setSlowMotorPosition(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation())

            elif self.xsDataDiffractionCTInstrument.get_tomo_scan_type().getValue().lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
                xsDataSpectrum.setFastMotorPosition(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x())
                xsDataSpectrum.setSlowMotorPosition(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z())
                xsSteps = XSDataInteger(int(round(\
                         (self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max().getValue() - \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min().getValue()) / \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_inc().getValue() \
                                                  )))

                xsDataMesh.setFastMotorSteps(xsSteps)
                xsDataMesh.setFastMotorStop(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max())
                xsDataMesh.setFastMotorStart(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min())

                xsSteps = XSDataInteger(int(round(\
                         (self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_max().getValue() - \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min().getValue()) / \
                           self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_inc().getValue() \
                                                  )))
                xsDataMesh.setSlowMotorSteps(xsSteps)
                xsDataMesh.setSlowMotorStop(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_max())
                xsDataMesh.setSlowMotorStart(self.xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min())
            xsDataSpectrum.setMeshScan(xsDataMesh)
            xsDataInputHDF5MapSpectra.setInputSpectrumFile([xsDataSpectrum])


            self.edPluginHDF5MapSpectra.setDataInput(xsDataInputHDF5MapSpectra)


    def doFailurePowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doFailurePowderIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doFailurePowderIntegration")
        self.setFailure()

    def doSuccessWriteSinogram(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doSuccessWriteSinogram")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doSuccessWriteSinogram")
        xsDataResultWriteSinogram = self.edPluginHDF5MapSpectra.getDataOutput()
        if (xsDataResultWriteSinogram is not None):
            self.xsDataResultDiffractionCT.setSinogramFile([xsDataResultWriteSinogram.getHDF5File()])

    def doFailureWriteSinogram(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doFailureWriteSinogram")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doFailureWriteSinogram")
        self.setFailure()

    def doSuccessExportAsciiPowder(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doSuccessExportAsciiPowder")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doSuccessExportAsciiPowder")
        xsDataResultExport1DPower = _edPlugin.getDataOutput()
        if (xsDataResultExport1DPower is not None):
            self.xsDataResultDiffractionCT.setIntegratedIntensities(xsDataResultExport1DPower.getOutputFile())

    def doFailureExportAsciiPowder(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDiffractionCTv1_2.doFailureExportAsciiPowder")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDiffractionCTv1_2.doFailureExportAsciiPowder")
        self.setFailure()


    def forceImageParam(self, xsdForceImageParam):
        """
        Helper function to override self.xsDataDiffractionCTImage with the contents of xsdForceImageParam
        @param xsDataDiffractionCTImage: instance of  XSDataDiffractionCTImage
        @return: None
        """
        if xsdForceImageParam.get_array_element_size_1() is not None:
            self.xsDataDiffractionCTImage.set_array_element_size_1(xsdForceImageParam.get_array_element_size_1())
        if xsdForceImageParam.get_array_element_size_2() is not None:
            self.xsDataDiffractionCTImage.set_array_element_size_2(xsdForceImageParam.get_array_element_size_2())
        if xsdForceImageParam.get_diffrn_detector_element_center_1() is not None:
            self.xsDataDiffractionCTImage.set_diffrn_detector_element_center_1(xsdForceImageParam.get_diffrn_detector_element_center_1())
        if xsdForceImageParam.get_diffrn_detector_element_center_2() is not None:
            self.xsDataDiffractionCTImage.set_diffrn_detector_element_center_2(xsdForceImageParam.get_diffrn_detector_element_center_2())
        if xsdForceImageParam.get_file_correction_image_dark_current() is not None:
            self.xsDataDiffractionCTImage.set_file_correction_image_dark_current(xsdForceImageParam.get_file_correction_image_dark_current())
        if xsdForceImageParam.get_file_correction_image_flat_field() is not None:
            self.xsDataDiffractionCTImage.set_file_correction_image_flat_field(xsdForceImageParam.get_file_correction_image_flat_field())
        if xsdForceImageParam.get_file_correction_image_mask() is not None:
            self.xsDataDiffractionCTImage.set_file_correction_image_mask(xsdForceImageParam.get_file_correction_image_mask())
        if xsdForceImageParam.get_file_correction_spline_spatial_distortion() is not None:
            self.xsDataDiffractionCTImage.set_file_correction_spline_spatial_distortion(xsdForceImageParam.get_file_correction_spline_spatial_distortion())
        if xsdForceImageParam.get_pd_instr_special_details_tilt_angle() is not None:
            self.xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_angle(xsdForceImageParam.get_pd_instr_special_details_tilt_angle())
        if xsdForceImageParam.get_pd_instr_special_details_tilt_rotation() is not None:
            self.xsDataDiffractionCTImage.set_pd_instr_special_details_tilt_rotation(xsdForceImageParam.get_pd_instr_special_details_tilt_rotation())


    def forceScanParam(self, xsdForceScanParam):
        """
        Helper function to override self.xsDataDiffractionCTInstrument with the contents of xsdForceScanParam
        @param xsdForceScanParam: instance of  XSDataDiffractionCTInstrument
        @return: None
        """
        if xsdForceScanParam.get_diffrn_radiation_wavelength() is not None:
            self.xsDataDiffractionCTInstrument.set_diffrn_radiation_wavelength(xsdForceScanParam.get_diffrn_radiation_wavelength())
        if xsdForceScanParam.get_pd_instr_dist_spec_detc() is not None:
            self.xsDataDiffractionCTInstrument.set_pd_instr_dist_spec_detc(xsdForceScanParam.get_pd_instr_dist_spec_detc())
        if xsdForceScanParam.get_pd_meas_2theta_range_inc() is not None:
            self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_inc(xsdForceScanParam.get_pd_meas_2theta_range_inc())
        if xsdForceScanParam.get_pd_meas_2theta_range_max() is not None:
            self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_max(xsdForceScanParam.get_pd_meas_2theta_range_max())
        if xsdForceScanParam.get_pd_meas_2theta_range_min() is not None:
            self.xsDataDiffractionCTInstrument.set_pd_meas_2theta_range_min(xsdForceScanParam.get_pd_meas_2theta_range_min())
        if xsdForceScanParam.get_synchrotron_photon_flux() is not None:
            self.xsDataDiffractionCTInstrument.set_synchrotron_photon_flux(xsdForceScanParam.get_synchrotron_photon_flux())
        if xsdForceScanParam.get_synchrotron_ring_intensity() is not None:
            self.xsDataDiffractionCTInstrument.set_synchrotron_ring_intensity(xsdForceScanParam.get_synchrotron_ring_intensity())
        if xsdForceScanParam.get_tomo_scan_ampl() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_scan_ampl(xsdForceScanParam.get_tomo_scan_ampl())
        if xsdForceScanParam.get_tomo_scan_type() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_scan_type(xsdForceScanParam.get_tomo_scan_type())
        if xsdForceScanParam.get_tomo_spec_displ_rotation() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation(xsdForceScanParam.get_tomo_spec_displ_rotation())
        if xsdForceScanParam.get_tomo_spec_displ_rotation_inc() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_rotation_inc(xsdForceScanParam.get_tomo_spec_displ_rotation_inc())
        if xsdForceScanParam.get_tomo_spec_displ_x_min() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_min(xsdForceScanParam.get_tomo_spec_displ_x_min())
        if xsdForceScanParam.get_tomo_spec_displ_x_max() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_max(xsdForceScanParam.get_tomo_spec_displ_x_max())
        if xsdForceScanParam.get_tomo_spec_displ_x_inc() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x_inc(xsdForceScanParam.get_tomo_spec_displ_x_inc())
        if xsdForceScanParam.get_tomo_spec_displ_x() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_x(xsdForceScanParam.get_tomo_spec_displ_x())
        if xsdForceScanParam.get_tomo_spec_displ_z() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z(xsdForceScanParam.get_tomo_spec_displ_z())
        if xsdForceScanParam.get_tomo_spec_displ_z_inc() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_inc(xsdForceScanParam.get_tomo_spec_displ_z_inc())
        if xsdForceScanParam.get_tomo_spec_displ_z_max() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_max(xsdForceScanParam.get_tomo_spec_displ_z_max())
        if xsdForceScanParam.get_tomo_spec_displ_z_min() is not None:
            self.xsDataDiffractionCTInstrument.set_tomo_spec_displ_z_min(xsdForceScanParam.get_tomo_spec_displ_z_min())



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
from EDVerbose             import EDVerbose
from EDPluginControl       import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDMessage             import EDMessage
from XSDataCommon          import XSDataFile, XSDataString
from XSDataDiffractionCTv1 import XSDataInputPowderIntegration
from XSDataDiffractionCTv1 import XSDataResultPowderIntegration
from CIFfile               import CIF


class EDPluginControlDCTPowderIntegrationv1_0(EDPluginControl):
    """
    This is the plugin-control for Diffraction Contrast Tomography for doing the azimutal integration  of 
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputPowderIntegration)
#        self.m_edStringControlledPluginName = "EDPluginFIT2DCakev1_0"
        self.m_edStringControlledPluginName = "EDPluginFIT2DCakev1_1"
        self.m_edPluginPowderIntegration = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        """
        The pre-process of ED Plugin Control Diffraction CT Powder Integration consists in preparing the input data for Fit2D Cake. 
        and declares the execution plugin as EDPluginFit2DCacke
        """
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.preProcess")
        # Load the execution plugin
        self.m_edPluginPowderIntegration = self.loadPlugin(self.m_edStringControlledPluginName)
        # Use the FIT2D handler
        EDFactoryPluginStatic.loadModule("EDHandlerXSDataFIT2Dv1_0")
        from EDHandlerXSDataFIT2Dv1_0 import EDHandlerXSDataFIT2Dv1_0
        edHandlerXSDataFIT2Dv1_0 = EDHandlerXSDataFIT2Dv1_0()
        try:
            xsDataInputFIT2DCake = edHandlerXSDataFIT2Dv1_0.getXSDataInputFIT2DCake(self.getDataInput())
            self.m_edPluginPowderIntegration.setDataInput(xsDataInputFIT2DCake)
        except Exception, error:
            # This exception handling needs to be rethought, see bug #43.
            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlDCTPowderIntegrationv1_0.preProcess: Unexpected error in FIT2D handler: ", error)
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage



    def process(self, _edObject=None):
        """ Does the job"""
        EDPluginControl.process(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.process")
        self.m_edPluginPowderIntegration.connectSUCCESS(self.doSuccessExecPowderIntegration)
        self.m_edPluginPowderIntegration.connectFAILURE(self.doFailureExecPowderIntegration)
        self.m_edPluginPowderIntegration.executeSynchronous()


    def postProcess(self, _edObject=None):
        """The post processing of DCT powder integration is mainly to integrate the metadata concerning instrument geometry to the output CIF file"""
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.postProcess")
        # Create result object
        from EDHandlerXSDataFIT2Dv1_0 import EDHandlerXSDataFIT2Dv1_0
        edHandlerXSDataFIT2Dv1_0 = EDHandlerXSDataFIT2Dv1_0()
        try:
            xsDataResultPowderDiffraction = edHandlerXSDataFIT2Dv1_0.getXSDataResultPowderIntegration(self.m_edPluginPowderIntegration.getDataOutput())
            self.setDataOutput(xsDataResultPowderDiffraction)
        except Exception, error:
            # This exception handling needs to be rethought, see bug #43.
            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlDCTPowderIntegrationv1_0.postProcess: Unexpected error in FIT2D handler: ", error)
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage

        # Here we read the output file written in CIF format (OK 20091023) 
        edStringPathToCHIFile = self.getDataOutput().getIntegratedIntensities().getPath().getValue()


        cifPowderData = CIF()
#        cifPowderData.loadCIF(edStringPathToCIFFile) 
        cifPowderData.loadCHIPLOT(edStringPathToCHIFile)

        # Add CIF instrumentation keywords

        self.m_xsDataDiffractionCTInstrument = self.getDataInput().getInstrumentParameters()

        if (not cifPowderData.exists("_diffrn_radiation_wavelength"))  and (self.m_xsDataDiffractionCTInstrument.get_diffrn_radiation_wavelength() is not None) :
             cifPowderData[" _diffrn_radiation_wavelength" ] = str(self.m_xsDataDiffractionCTInstrument.get_diffrn_radiation_wavelength().getValue())
        if (not cifPowderData.exists("_pd_meas_2theta_range_max")) and (self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_max() is not None) :
            cifPowderData[ "_pd_meas_2theta_range_max" ] = str(self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_max().getValue())
        if (not cifPowderData.exists("_pd_meas_2theta_range_min")) and (self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_min() is not None) :
            cifPowderData[ "_pd_meas_2theta_range_min" ] = str(self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_min().getValue())
        if (not cifPowderData.exists("_pd_meas_2theta_range_inc")) and (self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_inc() is not None):
            cifPowderData[ "_pd_meas_2theta_range_inc" ] = str(self.m_xsDataDiffractionCTInstrument.get_pd_meas_2theta_range_inc().getValue())
        if (not cifPowderData.exists("_pd_instr_dist_spec/detc")) and (self.m_xsDataDiffractionCTInstrument.get_pd_instr_dist_spec_detc() is not None) :
            cifPowderData[ "_pd_instr_dist_spec/detc"] = str(self.m_xsDataDiffractionCTInstrument.get_pd_instr_dist_spec_detc().getValue())
        if (not cifPowderData.exists("_synchrotron_photon-flux")) and (self.m_xsDataDiffractionCTInstrument.get_synchrotron_photon_flux() is not None) :
            cifPowderData[ "_synchrotron_photon-flux" ] = str(self.m_xsDataDiffractionCTInstrument.get_synchrotron_photon_flux().getValue())
        if (not cifPowderData.exists("_synchrotron_ring-intensity")) and (self.m_xsDataDiffractionCTInstrument.get_synchrotron_ring_intensity() is not None) :
            cifPowderData[ "_synchrotron_ring-intensity" ] = str(self.m_xsDataDiffractionCTInstrument.get_synchrotron_ring_intensity().getValue())
        if (not cifPowderData.exists("_tomo_scan_ampl")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_scan_ampl() is not None) :
            cifPowderData[ "_tomo_scan_ampl" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_scan_ampl ().getValue())
        if (not cifPowderData.exists("_tomo_scan_type")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_scan_type() is not None) :
            cifPowderData[ "_tomo_scan_type" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_scan_type ().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_rotation")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation() is not None) :
            cifPowderData[ "_tomo_spec_displ_rotation" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_rotation_inc")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation_inc () is not None) :
            cifPowderData[ "_tomo_spec_displ_rotation_inc" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_rotation_inc ().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_x")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x () is not None) :
            cifPowderData[ "_tomo_spec_displ_x" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_x_inc")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_inc () is not None) :
            cifPowderData[ "_tomo_spec_displ_x_inc" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_inc().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_x_max")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max () is not None) :
            cifPowderData[ "_tomo_spec_displ_x_max" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_max().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_x_min")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min () is not None) :
            cifPowderData[ "_tomo_spec_displ_x_min" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_x_min().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_z")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z() is not None) :
            cifPowderData[ "_tomo_spec_displ_z" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_z_inc")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_inc () is not None) :
            cifPowderData[ "_tomo_spec_displ_z_inc" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_inc().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_z_max")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_max () is not None) :
            cifPowderData[ "_tomo_spec_displ_z_max" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_max().getValue())
        if (not cifPowderData.exists("_tomo_spec_displ_z_min")) and (self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min() is not None) :
            cifPowderData[ "_tomo_spec_displ_z_min" ] = str(self.m_xsDataDiffractionCTInstrument.get_tomo_spec_displ_z_min().getValue())
#        #Now the tricky case of loops ... 
#        loop_pd_sum_2theta_range_max = []
#        loop_pd_sum_2theta_range_min = []
#        pyintPosToPop = -1
#        if self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_max() is not None :
#            if cifPowderData.exists("_pd_sum_2theta_range_max"):
#                pylist_pd_sum_2theta_range_max.append(cifPowderData[ "_pd_sum_2theta_range_max"])
#                cifPowderData.pop("_pd_sum_2theta_range_max")
#            elif cifPowderData.existsInLoop("_pd_sum_2theta_range_max"):
#                for pylistOneLoop in cifPowderData[ "loop_" ]:
#                    if pylistOneLoop[0].find("_pd_sum_2theta_range_max") >= 0:
#                        for pydictOneKeyPair in pylistOneLoop[1]:
#                            loop_pd_sum_2theta_range_max.append(pydictOneKeyPair [ "_pd_sum_2theta_range_max"])
#            for i in self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_max():
#                loop_pd_sum_2theta_range_max.append(str(i.getValue()))
#
#        if self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_min() is not None :
#            if cifPowderData.exists("_pd_sum_2theta_range_min"):
#                pylist_pd_sum_2theta_range_min.append(cifPowderData[ "_pd_sum_2theta_range_min"])
#                cifPowderData.pop("_pd_sum_2theta_range_min")
#            elif cifPowderData.existsInLoop("_pd_sum_2theta_range_min"):
#                pyIndex = -1
#                for pylistOneLoop in cifPowderData[ "loop_" ]:
#                    pyIndex += 1
#                    if pylistOneLoop[0].find("_pd_sum_2theta_range_min") >= 0:
#                        pyintPosToPop = pyIndex
#                        for pydictOneKeyPair in pylistOneLoop[1]:
#                            loop_pd_sum_2theta_range_min.append(pydictOneKeyPair [ "_pd_sum_2theta_range_min"])
#
#            for i in self.m_xsDataDiffractionCTInstrument.get_pd_sum_2theta_range_min():
#                loop_pd_sum_2theta_range_min.append(str(i.getValue()))
#        if len(loop_pd_sum_2theta_range_max) != len(loop_pd_sum_2theta_range_min):
#            print "there must be an error :\nloop_pd_sum_2theta_range_min=%s\nloop_pd_sum_2theta_range_max" % (loop_pd_sum_2theta_range_min, loop_pd_sum_2theta_range_max)
#        if len(loop_pd_sum_2theta_range_max) == 1:
#            cifPowderData[ "_pd_sum_2theta_range_min"] = loop_pd_sum_2theta_range_min [0]
#            cifPowderData[ "_pd_sum_2theta_range_max"] = loop_pd_sum_2theta_range_max [0]
#        elif len(loop_pd_sum_2theta_range_max) > 1:
#            cifloop = []
#            for pyIndex in range(len(loop_pd_sum_2theta_range_max)):
#                cifloop.append({"_pd_sum_2theta_range_max":loop_pd_sum_2theta_range_max[pyIndex], "_pd_sum_2theta_range_min": loop_pd_sum_2theta_range_min[pyIndex] })
#            if pyintPosToPop >= 0:
#                cifPowderData[ "loop_" ][pyintPosToPop] = [["_pd_sum_2theta_range_min", "_pd_sum_2theta_range_max"], cifloop]
#            else:
#                cifPowderData[ "loop_" ].insert(0, [["_pd_sum_2theta_range_min", "_pd_sum_2theta_range_max"], cifloop])
        #And finally we write the CIF file 

        edStringPathToCIFFile = os.path.splitext(edStringPathToCHIFile)[0] + ".cif"
        cifPowderData.saveCIF(edStringPathToCIFFile)
        xsDataFilePathToCIF = XSDataFile()
        xsDataFilePathToCIF.setPath(XSDataString(edStringPathToCIFFile))
        self.xsDataResultPowderIntegration.setIntegratedIntensities(xsDataFilePathToCIF)
        self.setDataOutput(self.xsDataResultPowderIntegration)



    def doSuccessExecPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.doSuccessExecPowderIntegration")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDCTPowderIntegrationv1_0.doSuccessExecPowderIntegration")
        # Create some output data
        self.xsDataResultPowderIntegration = XSDataResultPowderIntegration()
        self.setDataOutput(self.xsDataResultPowderIntegration)


    def doFailureExecPowderIntegration(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDCTPowderIntegrationv1_0.doFailureExecPowderIntegration")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDCTPowderIntegrationv1_0.doFailureExecPowderIntegration")

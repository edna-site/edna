#
#    Project: EDNA mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
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

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20120712"
__status__ = "production"


from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsPath import EDUtilsPath

from XSDataXDSv1_0 import XSDataInputXDS
from XSDataXDSv1_0 import XSDataResultXDS

import os as PyOs

class EDPluginXDSv1_0(EDPluginExecProcessScript):


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setRequiredToHaveConfiguration(True)
        self.__strXDSInput = None
        self.__listJob = None
        self.__strImageLinkSubDirectory = "img"
        self.__strPathToXGeoCorr = None
        self.__strPathToYGeoCorr = None


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.__strPathToXGeoCorr = self.config.get("x-geo_corr", None)
        self.__strPathToYGeoCorr = self.config.get("y-geo_corr", None)



    def preProcess(self, _oedObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXDSv1_0.preProcess")
        self.createImageLinks()
        self.generateXDSCommands()
        self.writeInputXDSFile()


    def process(self, _oedObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginXDSv1_0.process")
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginXDSv1_0"):
             raise ExectuteAbstractPluginError


    def postProcess(self, _oedObject=None):
        EDPluginExecProcessScript.postProcess(self, _oedObject)
        self.dataOutput = XSDataResultXDS()

    def checkParameters(self):
        """
        Checks the mandatory parameters for all XDS plugins
        """
        self.DEBUG("EDPluginXDSv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getBeam(), "beam")
        self.checkMandatoryParameters(self.getDataInput().getDetector(), "detector")
        self.checkMandatoryParameters(self.getDataInput().getGoniostat(), "goniostat")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "image")


    def addJob(self, _pyStrJob):
        if (self.__listJob is None):
            self.__listJob = []
        self.__listJob.append(_pyStrJob)


    def addInputLine(self, _strInputLine):
        if (self.__strXDSInput is None):
            self.__strXDSInput = ""
        self.__strXDSInput += _strInputLine + "\n"


    def generateXDSCommands(self):
        """
        This method creates a list of XDS commands given a valid
        XSDataXDSInput as self.getDataInput()
        """
        self.DEBUG("EDPluginXDSv1_0.generateXDSCommands")
        self.__strXDSInput = ""

        xsDataXDSInput = self.getDataInput()

        # Detecor related input

        xsDataXDSDetector = xsDataXDSInput.getDetector()

        if (self.__listJob is None):
            raise "RuntimeException", "No jobs given to XDS!"

        pyStrJobLine = "JOB"
        for pyStrJob in self.__listJob:
            pyStrJobLine += " %s" % (pyStrJob)

        self.addInputLine(pyStrJobLine)

        self.addInputLine("DETECTOR=%s   MINIMUM_VALID_PIXEL_VALUE=%d    OVERLOAD=%d" % \
                           (xsDataXDSDetector.getDetector_name().getValue(),
                             xsDataXDSDetector.getMinimum_valid_pixel_value().getValue(),
                             xsDataXDSDetector.getOverload().getValue()))

        for xsDataXDSRectangle in xsDataXDSDetector.getUntrusted_rectangle():
            self.addInputLine("UNTRUSTED_RECTANGLE=%4d %4d %4d %4d" % (\
                              xsDataXDSRectangle.getX1().getValue(),
                              xsDataXDSRectangle.getX2().getValue(),
                              xsDataXDSRectangle.getY1().getValue(),
                              xsDataXDSRectangle.getY2().getValue()))

        if xsDataXDSDetector.getTrusted_region():
            self.addInputLine("TRUSTED_REGION=%f %f" % (\
                              xsDataXDSDetector.getTrusted_region().getLower().getValue(),
                              xsDataXDSDetector.getTrusted_region().getUpper().getValue()))

        if xsDataXDSDetector.getSensor_thickness():
            self.addInputLine("SENSOR_THICKNESS=%f" % xsDataXDSDetector.getSensor_thickness().getValue())

        if self.__strPathToXGeoCorr and self.__strPathToYGeoCorr:
            self.addInputLine("X-GEO_CORR=%s" % self.__strPathToXGeoCorr)
            self.addInputLine("Y-GEO_CORR=%s" % self.__strPathToYGeoCorr)

        self.addInputLine("DETECTOR_DISTANCE=%f" % (xsDataXDSDetector.getDetector_distance().getValue()))

        self.addInputLine("DIRECTION_OF_DETECTOR_X-AXIS= %8f %8f %8f" % \
                           (xsDataXDSDetector.getDirection_of_detector_x_axis().getV1(),
                             xsDataXDSDetector.getDirection_of_detector_x_axis().getV2(),
                             xsDataXDSDetector.getDirection_of_detector_x_axis().getV3()))

        self.addInputLine("DIRECTION_OF_DETECTOR_Y-AXIS= %8f %8f %8f" % \
                           (xsDataXDSDetector.getDirection_of_detector_y_axis().getV1(),
                             xsDataXDSDetector.getDirection_of_detector_y_axis().getV2(),
                             xsDataXDSDetector.getDirection_of_detector_y_axis().getV3()))

        self.addInputLine("NX=%d   NY=%d  QX=%8f  QY=%8f" % \
                           (xsDataXDSDetector.getNx().getValue(),
                             xsDataXDSDetector.getNy().getValue(),
                             xsDataXDSDetector.getQx().getValue(),
                             xsDataXDSDetector.getQy().getValue()))

        self.addInputLine("ORGX=%8f  ORGY=%8f" % \
                           (xsDataXDSDetector.getOrgx().getValue(),
                             xsDataXDSDetector.getOrgy().getValue()))

        self.addInputLine("VALUE_RANGE_FOR_TRUSTED_DETECTOR_PIXELS=%d  %d" % \
                           (xsDataXDSDetector.getValue_range_for_trusted_detector_pixels().getLower().getValue(),
                             xsDataXDSDetector.getValue_range_for_trusted_detector_pixels().getUpper().getValue()))

        # Image related input

        xsDataXDSImage = xsDataXDSInput.getImage()

        xsDataXSDIntegerRangeBackgroundList = xsDataXDSImage.getBackground_range()
        for xsDataXSDIntegerRangeBackground in xsDataXSDIntegerRangeBackgroundList:
            self.addInputLine("BACKGROUND_RANGE= %4d %4d" % \
                               (xsDataXSDIntegerRangeBackground.getLower().getValue(),
                                 xsDataXSDIntegerRangeBackground.getUpper().getValue()))

        xsDataXSDIntegerRangeDataList = xsDataXDSImage.getData_range()
        for xsDataXSDIntegerRangeData in xsDataXSDIntegerRangeDataList:
            self.addInputLine("DATA_RANGE= %4d %4d" % \
                               (xsDataXSDIntegerRangeData.getLower().getValue(),
                                 xsDataXSDIntegerRangeData.getUpper().getValue()))

        xsDataXSDIntegerRangeSpotList = xsDataXDSImage.getSpot_range()
        for xsDataXSDIntegerRangeSpot in xsDataXSDIntegerRangeSpotList:
            self.addInputLine("SPOT_RANGE= %4d %4d" % \
                               (xsDataXSDIntegerRangeSpot.getLower().getValue(),
                                 xsDataXSDIntegerRangeSpot.getUpper().getValue()))

        pyStrTemplate = xsDataXDSImage.getName_template_of_data_frames().getValue()
        pyStrTemplatePath = PyOs.path.join(self.__strImageLinkSubDirectory, pyStrTemplate)
        self.addInputLine("NAME_TEMPLATE_OF_DATA_FRAMES= %s" % (pyStrTemplatePath))

        self.addInputLine("STARTING_FRAME= %d" % \
                           (xsDataXDSImage.getStarting_frame().getValue()))

        # Beam related input

        xsDataXDSBeam = xsDataXDSInput.getBeam()

        xsDataFloatFractionOfPolarization = xsDataXDSBeam.getFraction_of_polarization()
        if (xsDataFloatFractionOfPolarization is not None):
            self.addInputLine("FRACTION_OF_POLARIZATION= %8f" % \
                               (xsDataFloatFractionOfPolarization.getValue()))

        self.addInputLine("INCIDENT_BEAM_DIRECTION=   %8f %8f %8f" % \
                           (xsDataXDSBeam.getIncident_beam_direction().getV1(),
                             xsDataXDSBeam.getIncident_beam_direction().getV2(),
                             xsDataXDSBeam.getIncident_beam_direction().getV3()))

        self.addInputLine("POLARIZATION_PLANE_NORMAL= %8f %8f %8f" % \
                           (xsDataXDSBeam.getPolarization_plane_normal().getV1(),
                             xsDataXDSBeam.getPolarization_plane_normal().getV2(),
                             xsDataXDSBeam.getPolarization_plane_normal().getV3()))

        self.addInputLine("X-RAY_WAVELENGTH= %8f" % (xsDataXDSBeam.getX_ray_wavelength().getValue()))

        # Goniostat related input

        xsDataXDSGoniostat = xsDataXDSInput.getGoniostat()

        self.addInputLine("OSCILLATION_RANGE= %8f" % (xsDataXDSGoniostat.getOscillation_range().getValue()))

        self.addInputLine("STARTING_ANGLE= %8f" % (xsDataXDSGoniostat.getStarting_angle().getValue()))

        self.addInputLine("ROTATION_AXIS= %8f %8f %8f" % \
                           (xsDataXDSGoniostat.getRotation_axis().getV1(),
                             xsDataXDSGoniostat.getRotation_axis().getV2(),
                             xsDataXDSGoniostat.getRotation_axis().getV3()))

        # Crystal related input

        xsDataXDSCrystal = xsDataXDSInput.getCrystal()

        #xsDataStringFriedelsLaw = xsDataXDSCrystal.getFriedels_law()
        #if ( xsDataStringFriedelsLaw is not None ):
        #    self.addInputLine( "FRIEDEL'S_LAW= %s" % ( xsDataStringFriedelsLaw.getValue() ) )

        if xsDataXDSCrystal:
            self.addInputLine("SPACE_GROUP_NUMBER= %d" % (xsDataXDSCrystal.getSpace_group_number().getValue()))

            xsDataIntegerStrongPixel = xsDataXDSCrystal.getStrong_pixel()
            if (xsDataIntegerStrongPixel is not None):
                self.addInputLine("STRONG_PIXEL= %s" % (xsDataIntegerStrongPixel.getValue()))

            xsDataCell = xsDataXDSCrystal.getUnit_cell_constants()
            self.addInputLine("UNIT_CELL_CONSTANTS= %8f %8f %8f %8f %8f %8f" % \
                               (xsDataCell.getLength_a().getValue(),
                                 xsDataCell.getLength_b().getValue(),
                                 xsDataCell.getLength_c().getValue(),
                                 xsDataCell.getAngle_alpha().getValue(),
                                 xsDataCell.getAngle_beta().getValue(),
                                 xsDataCell.getAngle_gamma().getValue()))
        else:
            self.addInputLine("SPACE_GROUP_NUMBER= 0")
            self.addInputLine("UNIT_CELL_CONSTANTS= 0 0 0 0 0 0")



    def writeInputXDSFile(self):
        self.writeProcessFile("XDS.INP", self.__strXDSInput)


    def createImageLinks(self):
        xsDataXDSInput = self.getDataInput()
        xsDataXDSImageLinkList = xsDataXDSInput.getImage_link()
        self.addListCommandPreExecution("rm -rf %s" % (self.__strImageLinkSubDirectory))
        self.addListCommandPreExecution("mkdir -p %s" % (self.__strImageLinkSubDirectory))

        for xsDataXDSImageLink in xsDataXDSImageLinkList:
            pyStrSourcePath = xsDataXDSImageLink.getSource().getPath().getValue()
            pyStrTarget = xsDataXDSImageLink.getTarget().getValue()
            pyStrTargetPath = PyOs.path.join(self.__strImageLinkSubDirectory, pyStrTarget)
            self.addListCommandPreExecution("ln -s %s %s" % (pyStrSourcePath, pyStrTargetPath))

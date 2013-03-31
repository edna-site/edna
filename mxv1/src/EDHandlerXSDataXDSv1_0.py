#
#    Project: The EDNA Prototype
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    Contributors:      Olof Svensson (svensson@esrf.fr) 


__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataVectorDouble

from XSDataMXv1 import XSDataCell
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataResultControlXDSGenerateBackgroundImage

EDFactoryPluginStatic.loadModule("XSDataXDSv1_0")
from XSDataXDSv1_0 import XSDataInputXDSGenerateBackgroundImage
from XSDataXDSv1_0 import XSDataXDSDetector
from XSDataXDSv1_0 import XSDataVectorDouble
from XSDataXDSv1_0 import XSDataXDSBeam
from XSDataXDSv1_0 import XSDataXDSImage
from XSDataXDSv1_0 import XSDataXDSGoniostat
from XSDataXDSv1_0 import XSDataXDSIntegerRange
from XSDataXDSv1_0 import XSDataXDSDoubleRange
from XSDataXDSv1_0 import XSDataXDSCrystal
from XSDataXDSv1_0 import XSDataXDSImageLink
from XSDataXDSv1_0 import XSDataXDSRectangle



class EDHandlerXSDataXDSv1_0:


    @staticmethod
    def generateXSDataInputXDS(_xsDataCollection):

        xsDataCollection = _xsDataCollection
        xsDataExperimentalCondition = _xsDataCollection.getSubWedge()[0].getExperimentalCondition()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()

        xsDataInputXDS = XSDataInputXDSGenerateBackgroundImage()

        xsDataBeam = xsDataExperimentalCondition.getBeam()
        xsDataDetector = xsDataExperimentalCondition.getDetector()
        xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()

        dWavelength = xsDataBeam.getWavelength().getValue()
        dDistance = xsDataDetector.getDistance().getValue()
        dBeamPositionX = xsDataDetector.getBeamPositionX().getValue()
        dBeamPositionY = xsDataDetector.getBeamPositionY().getValue()

        # Start with the detector

        xsDataXDSDetector = EDHandlerXSDataXDSv1_0.getXSDataXDSDetector(xsDataDetector)
        xsDataInputXDS.setDetector(xsDataXDSDetector)

        # Then the beam 

        xsDataXDSBeam = XSDataXDSBeam()

        xsDataVectorDoubleIncidentBeam = XSDataVectorDouble()
        xsDataVectorDoubleIncidentBeam.setV1(0.0)
        xsDataVectorDoubleIncidentBeam.setV2(0.0)
        xsDataVectorDoubleIncidentBeam.setV3(1.0)
        xsDataXDSBeam.setIncident_beam_direction(xsDataVectorDoubleIncidentBeam)

        xsDataVectorDoublePolarizationPlaneNormal = XSDataVectorDouble()
        xsDataVectorDoublePolarizationPlaneNormal.setV1(0.0)
        xsDataVectorDoublePolarizationPlaneNormal.setV2(1.0)
        xsDataVectorDoublePolarizationPlaneNormal.setV3(0.0)
        xsDataXDSBeam.setPolarization_plane_normal(xsDataVectorDoublePolarizationPlaneNormal)

        xsDataXDSBeam.setX_ray_wavelength(XSDataWavelength(dWavelength))

        xsDataInputXDS.setBeam(xsDataXDSBeam)

        # Then the goniostat

        xsDataXDSGoniostat = XSDataXDSGoniostat()

        xsDataVectorDoubleRotationAxis = XSDataVectorDouble()
        xsDataVectorDoubleRotationAxis.setV1(1.0)
        xsDataVectorDoubleRotationAxis.setV2(0.0)
        xsDataVectorDoubleRotationAxis.setV3(0.0)
        xsDataXDSGoniostat.setRotation_axis(xsDataVectorDoubleRotationAxis)

        xsDataXDSGoniostat.setOscillation_range(xsDataGoniostat.getOscillationWidth())

        xsDataXDSGoniostat.setStarting_angle(xsDataGoniostat.getRotationAxisStart())

        xsDataInputXDS.setGoniostat(xsDataXDSGoniostat)

#        # Then the Crystal
#
#        xsDataXDSCrystal = XSDataXDSCrystal()
#
#        xsDataXDSCrystal.setFriedels_law(XSDataString("FALSE"))
#
##        if ( xsDataCrystal is not None ):
##            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
##            if ( xsDataSpaceGroup is not None ):
##                xsDataStringName = xsDataSpaceGroup.getName()
##                if ( xsDataStringName is not None ):
##                    xsDataInputXDS.setSymmetry( XSDataString( xsDataStringName.getValue() ) )      
#        xsDataXDSCrystal.setSpace_group_number(XSDataInteger(0))
#
#        xsDataXDSCrystal.setStrong_pixel(XSDataInteger(8))
#
#        xsDataCell = XSDataCell()
#        xsDataCell.setLength_a(XSDataLength(0.0))
#        xsDataCell.setLength_b(XSDataLength(0.0))
#        xsDataCell.setLength_c(XSDataLength(0.0))
#        xsDataCell.setAngle_alpha(XSDataAngle(0.0))
#        xsDataCell.setAngle_beta(XSDataAngle(0.0))
#        xsDataCell.setAngle_gamma(XSDataAngle(0.0))
#        xsDataXDSCrystal.setUnit_cell_constants(xsDataCell)
#
#        xsDataInputXDS.setCrystal(xsDataXDSCrystal)

        # Finaly the images

        xsDataXDSImage = XSDataXDSImage()

        xsDataSubWedgeFirst = xsDataSubWedgeList[0]
        xsDataImageFirst = xsDataSubWedgeFirst.getImage()[0]
        pyStrPath = xsDataImageFirst.getPath().getValue()
        pyStrFileName = EDUtilsFile.getBaseName(pyStrPath)
        pyStrDirectory = EDUtilsPath.getFolderName(pyStrPath)

        pyStrPrefix = EDUtilsImage.getPrefix(pyStrFileName)
        pyStrSuffix = EDUtilsImage.getSuffix(pyStrFileName)
        pyStrXDSTemplate = "%s_xdslink_?????.%s" % (pyStrPrefix, pyStrSuffix)

        xsDataXDSImage.setName_template_of_data_frames(XSDataString(pyStrXDSTemplate))

        iXDSLowestImageNumberGlobal = 1
        xsDataXDSImage.setStarting_frame(XSDataInteger(iXDSLowestImageNumberGlobal))

        # First we have to find the smallest goniostat rotation axis start:
        fGonioStatOscillationStartMin = None
        for xsDataSubWedge in xsDataSubWedgeList:
            xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()
            fGonioStatOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
            if (fGonioStatOscillationStartMin is None):
                fGonioStatOscillationStartMin = fGonioStatOscillationStart
            elif (fGonioStatOscillationStartMin > fGonioStatOscillationStart):
                fGonioStatOscillationStartMin = fGonioStatOscillationStart

        # Loop through the list of sub wedges 

        for xsDataSubWedge in xsDataSubWedgeList:

            xsDataImageList = xsDataSubWedge.getImage()
            xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()
            fGonioStatOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
            fGonioStatOscillationRange = xsDataGoniostat.getOscillationWidth().getValue()

            # First find the lowest and highest image numbers
            iLowestImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                if (iLowestImageNumber is None):
                    iLowestImageNumber = iImageNumber
                elif (iImageNumber < iLowestImageNumber):
                    iLowestImageNumber = iImageNumber

            # Loop through the list of images
            iLowestXDSImageNumber = None
            iHighestXDSImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                fImageOscillationStart = fGonioStatOscillationStart + (iImageNumber - iLowestImageNumber) * fGonioStatOscillationRange
                iXDSImageNumber = iXDSLowestImageNumberGlobal + int((fImageOscillationStart - fGonioStatOscillationStartMin) / fGonioStatOscillationRange)
                #print iXDSImageNumber, fImageOscillationStart, fGonioStatOscillationStartMin, fGonioStatOscillationRange
                pyStrSourcePath = xsDataImage.getPath()
                pyStrTarget = "%s_xdslink_%05d.%s" % (pyStrPrefix, iXDSImageNumber, pyStrSuffix)
                xsDataXDSImageLink = XSDataXDSImageLink()
                xsDataFileSource = XSDataFile()
                xsDataFileSource.setPath(pyStrSourcePath)
                xsDataXDSImageLink.setSource(xsDataFileSource)
                xsDataXDSImageLink.setTarget(XSDataString(pyStrTarget))
                xsDataInputXDS.addImage_link(xsDataXDSImageLink)
                if (iLowestXDSImageNumber is None):
                    iLowestXDSImageNumber = iXDSImageNumber
                elif (iLowestXDSImageNumber > iXDSImageNumber):
                    iLowestXDSImageNumber = iXDSImageNumber
                if (iHighestXDSImageNumber is None):
                    iHighestXDSImageNumber = iXDSImageNumber
                elif (iHighestXDSImageNumber < iXDSImageNumber):
                    iHighestXDSImageNumber = iXDSImageNumber
            xsDataXDSIntegerRange = XSDataXDSIntegerRange()
            xsDataXDSIntegerRange.setLower(XSDataInteger(iLowestXDSImageNumber))
            xsDataXDSIntegerRange.setUpper(XSDataInteger(iHighestXDSImageNumber))

            xsDataXDSImage.addBackground_range(xsDataXDSIntegerRange)
            xsDataXDSImage.addData_range(xsDataXDSIntegerRange)
            xsDataXDSImage.addSpot_range(xsDataXDSIntegerRange)

        xsDataInputXDS.setImage(xsDataXDSImage)

        return xsDataInputXDS


    @staticmethod
    def generateXSDataResultXDSGenerateBackgroundImage(_xsDataResultXDSGeneratePredictionImage):
        xsDataResultControlXDSGenerateBackgroundImage = XSDataResultControlXDSGenerateBackgroundImage()
        xsDataResultControlXDSGenerateBackgroundImage.setXdsBackgroundImage(_xsDataResultXDSGeneratePredictionImage.getXdsBackgroundImage())
        return xsDataResultControlXDSGenerateBackgroundImage




    @staticmethod
    def getXSDataXDSDetector(_xsDataDetector):
        EDFactoryPluginStatic.loadModule("XSDataXDSv1_0")
        from XSDataXDSv1_0 import XSDataXDSDetector
        from XSDataXDSv1_0 import XSDataXDSIntegerRange
        xsDataXDSDetector = XSDataXDSDetector()
        strDetectorType = _xsDataDetector.getType().getValue()
        if ((strDetectorType == "q4")      or \
             (strDetectorType == "q4-2x")   or \
             (strDetectorType == "q210")    or \
             (strDetectorType == "q210-2x") or \
             (strDetectorType == "q315")    or \
             (strDetectorType == "q315-2x")):
            xsDataXDSDetector.setDetector_name(XSDataString("ADSC"))
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(1))
            xsDataXDSDetector.setOverload(XSDataInteger(65535))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(6000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)
#        elif ( strDetectorType == "mar165") or \
#               strDetectorType == "mar225") ):
#            xsDataXDSDetector.setType( XSDataString( "MARCCD" ) )
        elif strDetectorType == "pilatus6m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 487, 495, 0, 2528], \
                [ 981, 989, 0, 2528], \
                [1475, 1483, 0, 2528], \
                [1969, 1977, 0, 2528], \
                [   0, 2464, 195, 213], \
                [   0, 2464, 407, 425], \
                [   0, 2464, 619, 637], \
                [   0, 2464, 831, 849], \
                [   0, 2464, 1043, 1061], \
                [   0, 2464, 1255, 1273], \
                [   0, 2464, 1467, 1485], \
                [   0, 2464, 1679, 1697], \
                [   0, 2464, 1891, 1909], \
                [   0, 2464, 2103, 2121], \
                [   0, 2464, 2315, 2333]]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))
        elif strDetectorType == "pilatus2m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 487, 495, 0, 1680], \
                [ 981, 989, 0, 1680], \
                [   0, 1476, 195, 213], \
                [   0, 1476, 407, 425], \
                [   0, 1476, 619, 637], \
                [   0, 1476, 831, 849], \
                [   0, 1476, 1043, 1061], \
                [   0, 1476, 1255, 1273], \
                [   0, 1476, 1467, 1485]]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))
        else:
            # This is a temporary solution for the exception problem pointed out in bug #43.
            # Instead of raising an exception with a known type we send the error message as a string.
            pyStrErrorMessage = "EDHandlerXSDataXDSv1_0.getXSDataXDSDetector: Unknown detector type : " + strDetectorType
            raise Exception, pyStrErrorMessage

        xsDataXDSDetector.setNx(_xsDataDetector.getNumberPixelX())
        xsDataXDSDetector.setNy(_xsDataDetector.getNumberPixelY())
        xsDataXDSDetector.setQx(_xsDataDetector.getPixelSizeX())
        xsDataXDSDetector.setQy(_xsDataDetector.getPixelSizeY())
        xsDataXDSDetector.setDetector_distance(_xsDataDetector.getDistance())

        fOrgx = _xsDataDetector.getBeamPositionY().getValue() / _xsDataDetector.getPixelSizeY().getValue()
        fOrgy = _xsDataDetector.getBeamPositionX().getValue() / _xsDataDetector.getPixelSizeX().getValue()
        xsDataXDSDetector.setOrgx(XSDataDouble(fOrgx))
        xsDataXDSDetector.setOrgy(XSDataDouble(fOrgy))
        xsDataVectorDoubleXAxis = XSDataVectorDouble()

        xsDataVectorDoubleXAxis.setV1(1.0)
        xsDataVectorDoubleXAxis.setV2(0.0)
        xsDataVectorDoubleXAxis.setV3(0.0)
        xsDataXDSDetector.setDirection_of_detector_x_axis(xsDataVectorDoubleXAxis)

        xsDataVectorDoubleYAxis = XSDataVectorDouble()
        xsDataVectorDoubleYAxis.setV1(0.0)
        xsDataVectorDoubleYAxis.setV2(1.0)
        xsDataVectorDoubleYAxis.setV3(0.0)
        xsDataXDSDetector.setDirection_of_detector_y_axis(xsDataVectorDoubleYAxis)


        return xsDataXDSDetector

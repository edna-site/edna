#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2014 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Michael Hellmig" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import struct

from EDVerbose      import EDVerbose
from EDMessage      import EDMessage
from EDUtilsImage   import EDUtilsImage

from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger

from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataBeam
from XSDataMXv1 import XSDataGoniostat
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataResultReadImageHeader



class EDPluginExecReadImageHeaderMARCCDv10(EDPluginExec):


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputReadImageHeader)
        self.__xsDataResultReadImageHeader = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderMARCCDv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderMARCCDv10.process")
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFile = xsDataInputReadImageHeader.getImage()
        strPath = xsDataFile.getPath().getValue()
        dictMARCCDHeader = self.readHeaderMarccd(strPath)
        if (dictMARCCDHeader is None):
            strErrorMessage = "EDPluginExecReadImageHeaderMARCCDv10.process : Cannot read header : %s" % strPath
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataDetector = XSDataDetector()

            iNoPixelsX = int(dictMARCCDHeader[ "nslow"   ])
            iNoPixelsY = int(dictMARCCDHeader[ "nfast"   ])
            xsDataDetector.setNumberPixelX(XSDataInteger(iNoPixelsX))
            xsDataDetector.setNumberPixelY(XSDataInteger(iNoPixelsY))
            fPixelSizeX = float(dictMARCCDHeader[ "pixelsize_x"   ]) / 1000.0
            xsDataDetector.setPixelSizeX(XSDataLength(fPixelSizeX))
            fPixelSizeY = float(dictMARCCDHeader[ "pixelsize_y"   ]) / 1000.0
            xsDataDetector.setPixelSizeY(XSDataLength(fPixelSizeY))
            fBeamPositionX = float(dictMARCCDHeader[ "beam_x" ]) / 1000.0
            fBeamPositionY = float(dictMARCCDHeader[ "beam_y" ]) / 1000.0
            # Fix for bug 397 - check if the beam position is close to the centre of the image
            fTwoTheta = float(dictMARCCDHeader[ "end_twotheta"   ]) / 1000.0
            xsDataDetector.setTwoTheta(XSDataAngle(fTwoTheta))
            if (abs(fTwoTheta) < 0.1):
                if (abs(fBeamPositionX / (fPixelSizeX / 1000.0) - iNoPixelsX / 2.0) > (2 * iNoPixelsX)):
                    fBeamPositionX = fBeamPositionX * fPixelSizeX / 1000.0
                    fBeamPositionY = fBeamPositionY * fPixelSizeY / 1000.0
            xsDataDetector.setBeamPositionX(XSDataLength(fBeamPositionX))
            xsDataDetector.setBeamPositionY(XSDataLength(fBeamPositionY))
            fDistance = float(dictMARCCDHeader[ "xtal_to_detector"   ]) / 1000.0
            if (abs(fDistance) < 0.1):
                fDistanceStart = float(dictMARCCDHeader[ "start_xtal_to_detector"   ]) / 1000.0
                fDistanceEnd = float(dictMARCCDHeader[ "end_xtal_to_detector"   ]) / 1000.0
                if (abs(fDistanceStart - fDistanceEnd) < 0.1):
                    fDistance = fDistanceStart
                else:
                    # Somethings very wrong with the distances...
                    strErrorMessage = "EDPluginExecReadImageHeaderMARCCDv10.process : Inconsistency in MAR CCD image header: start_xtal_to_detector = %d, end_xtal_to_detector = %d" % \
                                                                           (fDistanceStart, fDistanceEnd)
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
            xsDataDetector.setDistance(XSDataLength(fDistance))
            xsDataDetector.setNumberBytesInHeader(XSDataInteger(float(dictMARCCDHeader[ "header_size"   ])))
            # xsDataDetector.setSerialNumber(        XSDataInteger(  dictMARCCDHeader[ "DETECTOR_SN"   ] ) ) )
            # xsDataDetector.setBin(                 XSDataString(   dictMARCCDHeader[ "BIN" ] ) ) )
            # xsDataDetector.setDataType(            XSDataString(   dictMARCCDHeader[ "TYPE" ] ) ) )
            # xsDataDetector.setByteOrder(           XSDataString(   dictMARCCDHeader[ "BYTE_ORDER" ] ) ) )
            xsDataDetector.setImageSaturation(XSDataInteger(int(dictMARCCDHeader[ "saturation_level" ])))
            # Determine type of detector...
            if (iNoPixelsX == 2048 and iNoPixelsY == 2048):
                xsDataDetector.setName(XSDataString("MAR CCD 165"))
                xsDataDetector.setType(XSDataString("mar165"))
            elif (iNoPixelsX == 3072 and iNoPixelsY == 3072):
                xsDataDetector.setName(XSDataString("MAR CCD 225"))
                xsDataDetector.setType(XSDataString("mar225"))
            elif (iNoPixelsX == 4096 and iNoPixelsY == 4096):
                xsDataDetector.setName(XSDataString("MAR CCD 325"))
                xsDataDetector.setType(XSDataString("mar325"))
            else:
                strErrorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginExecReadImageHeaderMARCCDv10.process", "Unknown detector type")
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

            xsDataExperimentalCondition.setDetector(xsDataDetector)

            # Beam object

            xsDataBeam = XSDataBeam()
            xsDataBeam.setWavelength(XSDataWavelength(float(dictMARCCDHeader[ "source_wavelength" ]) / 100000.0))
            xsDataBeam.setExposureTime(XSDataTime(float(dictMARCCDHeader[ "exposure_time" ]) / 1000.0))
            xsDataExperimentalCondition.setBeam(xsDataBeam)

            # Goniostat object
            xsDataGoniostat = XSDataGoniostat()
            fRotationAxisStart = float(dictMARCCDHeader[ "start_phi" ]) / 1000.0
            fOscillationWidth = float(dictMARCCDHeader[ "rotation_range" ]) / 1000.0
            xsDataGoniostat.setRotationAxisStart(XSDataAngle(fRotationAxisStart))
            xsDataGoniostat.setRotationAxisEnd(XSDataAngle(fRotationAxisStart + fOscillationWidth))
            xsDataGoniostat.setOscillationWidth(XSDataAngle(fOscillationWidth))
            xsDataExperimentalCondition.setGoniostat(xsDataGoniostat)

            # Create the image object
            xsDataImage = XSDataImage()
            xsDataImage.setPath(XSDataString(strPath))
            strTimeStamp = dictMARCCDHeader[ "acquire_timestamp" ]
            xsDataImage.setDate(XSDataString(strTimeStamp))
            iImageNumber = EDUtilsImage.getImageNumber(strPath)
            xsDataImage.setNumber(XSDataInteger(iImageNumber))

            xsDataSubWedge = XSDataSubWedge()
            xsDataSubWedge.setExperimentalCondition(xsDataExperimentalCondition)
            xsDataSubWedge.addImage(xsDataImage)

            self.__xsDataResultReadImageHeader = XSDataResultReadImageHeader()
            self.__xsDataResultReadImageHeader.setSubWedge(xsDataSubWedge)



    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderMARCCDv10.postProcess")
        if (self.__xsDataResultReadImageHeader is not None):
            self.setDataOutput(self.__xsDataResultReadImageHeader)


    def readHeaderMarccd(self, _strFileName):
        """
        Returns an dictionary with the contents of a MAR CCD image header.
        """
        #
        #  Created by Krister Larsson on 08/11/5.
        #  Modified by Olof Svensson 20090401
        #
        strUint32 = 'I'
        strChar = 's'
        # strInt16 = 'H'
        strInt32 = 'i'

        iMAXIMAGES = 9

        pyListHeader = [
        # File/header format parameters (256bytes)
        [strUint32, 'header_type'],
        [strChar, 'header_name', 16],
        [strUint32, 'header_major_version'],
        [strUint32, 'header_minor_version'],
        [strUint32, 'header_byte_order'],
        [strUint32, 'data_byte_order'],
        [strUint32, 'header_size'],
        [strUint32, 'frame_type'],
        [strUint32, 'magic_number'],
        [strUint32, 'compression_type'],
        [strUint32, 'compression1'],
        [strUint32, 'compression2'],
        [strUint32, 'compression3'],
        [strUint32, 'compression4'],
        [strUint32, 'compression5'],
        [strUint32, 'compression6'],
        [strUint32, 'nheaders'],
        [strUint32, 'nfast'],
        [strUint32, 'nslow'],
        [strUint32, 'depth'],
        [strUint32, 'record_length'],
        [strUint32, 'signif_bits'],
        [strUint32, 'data_type'],
        [strUint32, 'saturated_value'],
        [strUint32, 'sequence'],
        [strUint32, 'nimages'],
        [strUint32, 'origin'],
        [strUint32, 'orientation'],
        [strUint32, 'view_direction'],
        [strUint32, 'overflow_direction'],
        [strUint32, 'over_8_bits'],
        [strUint32, 'over_16_bits'],
        [strUint32, 'multiplexed'],
        [strUint32, 'nfastimages'],
        [strUint32, 'nslowimages'],
        [strUint32, 'darkcurrent_applied'],
        [strUint32, 'bias_applied'],
        [strUint32, 'flatfield_applied'],
        [strUint32, 'distortion_applied'],
        [strUint32, 'original_header_type'],
        [strUint32, 'file_saved'],
        [strUint32, 'n_valid_pixels'],
        [strUint32, 'defectmap_applied'],
        [strUint32, 'subimage_nfast'],
        [strUint32, 'subimage_nslow'],
        [strUint32, 'subimage_origin_fast'],
        [strUint32, 'subimage_origin_slow'],
        [strUint32, 'readout_pattern'],
        [strUint32, 'saturation_level'],
        [strUint32, 'orientation_code'],
        [strUint32, 'frameshift_multiplexed'],
        [strUint32, 'precsan_nfast'],
        [strUint32, 'prescan_nslow'],
        [strUint32, 'postscan_nfast'],
        [strUint32, 'postscan_nslow'],
        [strUint32, 'prepost_trimmed'],
        [strChar, 'reserve1', 20],
        # Data statistics (128 bytes)
        [strUint32, 'total_counts', 2],
        [strUint32, 'special_counts1', 2],
        [strUint32, 'special_counts2', 2],
        [strUint32, 'min'],
        [strUint32, 'max'],
        [strUint32, 'mean'],
        [strUint32, 'rms'],
        [strUint32, 'n_zeros'],
        [strUint32, 'n_saturated'],
        [strUint32, 'stats_uptodate'],
        [strUint32, 'pixel_noise', iMAXIMAGES],
        [strChar, 'reserve2', (19 - iMAXIMAGES) * 4 ],

        # More statistics (256 bytes)
        # [uint16,'percentile',128],
        # Percentile is substituted by Sample changer info
        [strChar, 'barcode', 16],
        [strUint32, 'barcode_angle'],
        [strUint32, 'barcode_status'],
        [strChar, 'reserve2a', 232],
        # Goniostat parameters (128 bytes)
        [strInt32, 'xtal_to_detector'],
        [strInt32, 'beam_x'],
        [strInt32, 'beam_y'],
        [strInt32, 'integration_time'],
        [strInt32, 'exposure_time'],
        [strInt32, 'readout_time'],
        [strInt32, 'nreads'],
        [strInt32, 'start_twotheta'],
        [strInt32, 'start_omega'],
        [strInt32, 'start_chi'],
        [strInt32, 'start_kappa'],
        [strInt32, 'start_phi'],
        [strInt32, 'start_delta'],
        [strInt32, 'start_gamma'],
        [strInt32, 'start_xtal_to_detector'],
        [strInt32, 'end_twotheta'],
        [strInt32, 'end_omega'],
        [strInt32, 'end_chi'],
        [strInt32, 'end_kappa'],
        [strInt32, 'end_phi'],
        [strInt32, 'end_delta'],
        [strInt32, 'end_gamma'],
        [strInt32, 'end_xtal_to_detector'],
        [strInt32, 'rotation_axis'],
        [strInt32, 'rotation_range'],
        [strInt32, 'detector_rotx'],
        [strInt32, 'detector_roty'],
        [strInt32, 'detector_rotz'],
        [strInt32, 'total_dose'],
        [strChar, 'reserve3', 12],
        # Detector parameters (128 bytes)
        [strInt32, 'detector_type'],
        [strInt32, 'pixelsize_x'],
        [strInt32, 'pixelsize_y'],
        [strInt32, 'mean_bias'],
        [strInt32, 'photons_per_100adu'],
        [strInt32, 'measured_bias', iMAXIMAGES],
        [strInt32, 'measured_temperature', iMAXIMAGES],
        [strInt32, 'measured_pressure', iMAXIMAGES],
        # X-ray source and optics parameters (128 bytes)
        [strInt32, 'source_type'],
        [strInt32, 'source_dx'],
        [strInt32, 'source_dy'],
        [strInt32, 'source_wavelength'],
        [strInt32, 'source_power'],
        [strInt32, 'source_voltage'],
        [strInt32, 'source_current'],
        [strInt32, 'source_bias'],
        [strInt32, 'source_polarization_x'],
        [strInt32, 'source_polarization_y'],
        [strInt32, 'source_intensity_0'],
        [strInt32, 'source_intensity_1'],
        [strChar, 'reserve_source', 8],
        [strInt32, 'optics_type'],
        [strInt32, 'optics_dx'],
        [strInt32, 'optics_dy'],
        [strInt32, 'optics_wavelength'],
        [strInt32, 'optics_dispersion'],
        [strInt32, 'optics_crossfire_x'],
        [strInt32, 'optics_crossfire_y'],
        [strInt32, 'optics_angle'],
        [strInt32, 'optics_polarization_x'],
        [strInt32, 'optics_polarization_y'],
        [strChar, 'reserve_optics', 16],
        [strChar, 'reserve5', 16],
        # File parameters
        [strChar, 'filetitle', 128],
        [strChar, 'filepath', 128],
        [strChar, 'filename', 64],
        [strChar, 'acquire_timestamp', 32],
        [strChar, 'header_timestamp', 32],
        [strChar, 'save_timestamp', 32],
        [strChar, 'file_comment', 512],
        [strChar, 'reserve6', 96],
        [strChar, 'dataset_comments', 512],
        [strChar, 'user_data', 512]
        ]

        pyFile = None
        dictMarccd = None
        try:
            pyFile = open(_strFileName, "rb")
        except:
            EDVerbose.warning("EDPluginExecReadImageHeaderMARCCDv10.readHeaderMarccd: couldn't open file: " + _strFileName)
        if (pyFile is not None):
            EDVerbose.DEBUG("EDPluginExecReadImageHeaderMARCCDv10.readHeaderMarccd: Reading header from image " + _strFileName)
            dictMarccd = {}
            # Move to marccd part of header
            pyFile.seek(1024)
            for pyListRow in pyListHeader:
                if len(pyListRow) == 3:
                    strFormat = str(pyListRow[2]) + str(pyListRow[0])
                else:
                    strFormat = pyListRow[0]
                strKeyword = pyListRow[1]
                iReadSize = struct.calcsize(strFormat)
                pyRawData = pyFile.read(iReadSize)
                strValue = struct.unpack(strFormat, pyRawData)
                if len(strValue) == 1:
                    strValue = strValue[0]
                if pyListRow[0] == strChar:
                    strValue = strValue.strip('\x00')
                dictMarccd[strKeyword] = strValue
            pyFile.close()

        return dictMarccd


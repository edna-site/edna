#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose    import EDVerbose
from EDPlugin     import EDPlugin
from EDPluginExec import EDPluginExec
from EDUtilsImage import EDUtilsImage
from EDMessage    import EDMessage

from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger

from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataBeam
from XSDataMXv1 import XSDataGoniostat
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataResultReadImageHeader


class EDPluginExecReadImageHeaderADSCv10(EDPluginExec):

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
        EDVerbose.DEBUG("*** EDPluginExecReadImageHeaderADSCv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("*** EDPluginExecReadImageHeaderADSCv10.process")
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFile = xsDataInputReadImageHeader.getImage()
        strPath = xsDataFile.getPath().getValue()
        strAbsolutePath = os.path.abspath(strPath)
        dictHeader = self.readHeaderADSC(strPath)
        if (dictHeader is None):
            strErrorMessage = "EDPluginExecReadImageHeaderADSCv10.process : error when reading header from %s" % strAbsolutePath
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataDetector = XSDataDetector()

            xsDataDetector.setBeamPositionX(XSDataLength(float(dictHeader[ "BEAM_CENTER_X" ])))
            xsDataDetector.setBeamPositionY(XSDataLength(float(dictHeader[ "BEAM_CENTER_Y" ])))
            xsDataDetector.setDistance(XSDataLength(float(dictHeader[ "DISTANCE"   ])))
            fPixelSize = float(dictHeader[ "PIXEL_SIZE"   ])
            xsDataDetector.setPixelSizeX(XSDataLength(fPixelSize))
            xsDataDetector.setPixelSizeY(XSDataLength(fPixelSize))
            if "TWOTHETA" in dictHeader.keys():
                xsDataDetector.setTwoTheta(XSDataAngle(float(dictHeader[ "TWOTHETA"   ])))
            xsDataDetector.setNumberBytesInHeader(XSDataInteger(float(dictHeader[ "HEADER_BYTES"   ])))
            xsDataDetector.setSerialNumber(XSDataString(dictHeader[ "DETECTOR_SN"   ]))
            xsDataDetector.setNumberPixelX(XSDataInteger(int(dictHeader[ "SIZE1"   ])))
            xsDataDetector.setNumberPixelY(XSDataInteger(int(dictHeader[ "SIZE2"   ])))
            xsDataDetector.setBin(XSDataString(dictHeader[ "BIN" ]))
            xsDataDetector.setDataType(XSDataString(dictHeader[ "TYPE" ]))
            xsDataDetector.setByteOrder(XSDataString(dictHeader[ "BYTE_ORDER" ]))
            if "CCD_IMAGE_SATURATION" in dictHeader.keys():
                xsDataDetector.setImageSaturation(XSDataInteger(int(dictHeader[ "CCD_IMAGE_SATURATION" ])))

            # Determine type of detector...
            iNoPixelsX = xsDataDetector.getNumberPixelX().getValue()
            iNoPixelsY = xsDataDetector.getNumberPixelY().getValue()
            if (iNoPixelsX == 2304 and iNoPixelsY == 2304):
                xsDataDetector.setName(XSDataString("ADSC Q4"))
                xsDataDetector.setType(XSDataString("q4"))
            elif (iNoPixelsX == 1152 and iNoPixelsY == 1152):
                xsDataDetector.setName(XSDataString("ADSC Q4 bin 2x2"))
                xsDataDetector.setType(XSDataString("q4-2x"))
            elif (iNoPixelsX == 4096 and iNoPixelsY == 4096):
                xsDataDetector.setName(XSDataString("ADSC Q210"))
                xsDataDetector.setType(XSDataString("q210"))
            elif (iNoPixelsX == 2048 and iNoPixelsY == 2048):
                xsDataDetector.setName(XSDataString("ADSC Q210 bin 2x2"))
                xsDataDetector.setType(XSDataString("q210-2x"))
            elif (iNoPixelsX == 6144 and iNoPixelsY == 6144):
                xsDataDetector.setName(XSDataString("ADSC Q315"))
                xsDataDetector.setType(XSDataString("q315"))
            elif (iNoPixelsX == 3072 and iNoPixelsY == 3072):
                xsDataDetector.setName(XSDataString("ADSC Q315 bin 2x2"))
                xsDataDetector.setType(XSDataString("q315-2x"))
            else:
                strErrorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginExecReadImageHeaderADSCv10.process", "Unknown detector type")
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

            xsDataExperimentalCondition.setDetector(xsDataDetector)

            # Beam object

            xsDataBeam = XSDataBeam()
            xsDataBeam.setWavelength(XSDataWavelength(float(dictHeader[ "WAVELENGTH" ])))
            xsDataBeam.setExposureTime(XSDataTime(float(dictHeader[ "TIME" ])))
            xsDataExperimentalCondition.setBeam(xsDataBeam)

            # Goniostat object
            xsDataGoniostat = XSDataGoniostat()
            fRotationAxisStart = float(dictHeader[ "OSC_START" ])
            fOscillationWidth = float(dictHeader[ "OSC_RANGE" ])
            xsDataGoniostat.setRotationAxisStart(XSDataAngle(fRotationAxisStart))
            xsDataGoniostat.setRotationAxisEnd(XSDataAngle(fRotationAxisStart + fOscillationWidth))
            xsDataGoniostat.setOscillationWidth(XSDataAngle(fOscillationWidth))
            strRotationAxis = None
            if ("AXIS" in dictHeader.keys()):
                strRotationAxis = dictHeader[ "AXIS" ]
            elif ("OSC_AXIS" in dictHeader.keys()):
                strRotationAxis = dictHeader[ "OSC_AXIS" ]
            else:
                strErrorMessage = "EDPluginExecReadImageHeaderADSCv10.process : Neither AXIS nor OSC_AXIS header item found."
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            xsDataGoniostat.setRotationAxis(XSDataString(strRotationAxis))
            xsDataExperimentalCondition.setGoniostat(xsDataGoniostat)

            # Create the image object
            xsDataImage = XSDataImage()
            xsDataImage.setPath(XSDataString(strAbsolutePath))
            xsDataImage.setDate(XSDataString(dictHeader[ "DATE" ]))
            strFileName = os.path.basename(strPath)
            iImageNumber = EDUtilsImage.getImageNumber(strFileName)
            xsDataImage.setNumber(XSDataInteger(iImageNumber))

            xsDataSubWedge = XSDataSubWedge()
            xsDataSubWedge.setExperimentalCondition(xsDataExperimentalCondition)
            xsDataSubWedge.addImage(xsDataImage)

            self.__xsDataResultReadImageHeader = XSDataResultReadImageHeader()
            self.__xsDataResultReadImageHeader.setSubWedge(xsDataSubWedge)



    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecReadImageHeaderADSCv10.postProcess")
        if (self.__xsDataResultReadImageHeader is not None):
            self.setDataOutput(self.__xsDataResultReadImageHeader)


    def readHeaderADSC(self, _strImageFileName):
        """
        This method reads the header from an ADSC image and returns a dictionary.
        Ideally this method should be a part of another (exec) plugin.
        """
        pyFile = None
        dictionary = None
        try:
            pyFile = open(_strImageFileName, "r")
        except:
            EDVerbose.warning("**** EDPluginExecReadImageHeaderADSCv10.readHeaderADSC: couldn't open file: " + _strImageFileName)

        if (pyFile != None):
            EDVerbose.DEBUG("EDPluginExecReadImageHeaderADSCv10.readHeaderADSC: Reading header from image " + _strImageFileName)
            pyFile.seek(0, 0)
            strLine = pyFile.readline()
            if strLine[0] == "{":
                dictionary = {}
                strLine = pyFile.readline()
                while strLine[0] != "}" :
                    listSplit = strLine.split("=")
                    strKeyword = listSplit[0]
                    listSplitValue = listSplit[1].split(";")
                    strValue = listSplitValue[0]
                    dictionary[strKeyword] = strValue
                    strLine = pyFile.readline()
            pyFile.close()

        return dictionary

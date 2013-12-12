#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginExecReadImageHeaderMARCCDv10.py 1513 2010-05-11 13:29:05Z svensson $"
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



class EDPluginExecReadImageHeaderPilatus6Mv10(EDPluginExec):


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
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderPilatus6Mv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderPilatus6Mv10.process")
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFile = xsDataInputReadImageHeader.getImage()
        strPath = xsDataFile.getPath().getValue()
        dictPilatus6MHeader = self.readHeaderPilatus6M(strPath)
        if (dictPilatus6MHeader is None):
            strErrorMessage = "EDPluginExecReadImageHeaderPilatus6Mv10.process : Cannot read header : %s" % strPath
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataDetector = XSDataDetector()

            iNoPixelsX = 2463
            iNoPixelsY = 2527
            xsDataDetector.setNumberPixelX(XSDataInteger(iNoPixelsX))
            xsDataDetector.setNumberPixelY(XSDataInteger(iNoPixelsY))
            # Pixel size
            listPixelSizeXY = dictPilatus6MHeader[ "Pixel_size"   ].split(" ")
            fPixelSizeX = float(listPixelSizeXY[0]) * 1000
            xsDataDetector.setPixelSizeX(XSDataLength(fPixelSizeX))
            fPixelSizeY = float(listPixelSizeXY[3]) * 1000
            xsDataDetector.setPixelSizeY(XSDataLength(fPixelSizeY))
            # Beam position
            listBeamPosition = dictPilatus6MHeader["Beam_xy"].replace("(", " ").replace(")", " ").replace(",", " ").split()
            fBeamPositionX = float(listBeamPosition[1]) * fPixelSizeX
            fBeamPositionY = float(listBeamPosition[0]) * fPixelSizeY
            xsDataDetector.setBeamPositionX(XSDataLength(fBeamPositionX))
            xsDataDetector.setBeamPositionY(XSDataLength(fBeamPositionY))
            fDistance = float(dictPilatus6MHeader[ "Detector_distance" ].split(" ")[0]) * 1000
            xsDataDetector.setDistance(XSDataLength(fDistance))
#            xsDataDetector.setNumberBytesInHeader(XSDataInteger(float(dictPilatus6MHeader[ "header_size"   ])))
            xsDataDetector.setSerialNumber(XSDataString(dictPilatus6MHeader[ "Detector:"   ]))
#            #xsDataDetector.setBin(                 XSDataString(   dictPilatus6MHeader[ "BIN" ] ) ) )
#            #xsDataDetector.setDataType(            XSDataString(   dictPilatus6MHeader[ "TYPE" ] ) ) )
#            #xsDataDetector.setByteOrder(           XSDataString(   dictPilatus6MHeader[ "BYTE_ORDER" ] ) ) )
#            xsDataDetector.setImageSaturation(XSDataInteger(int(dictPilatus6MHeader[ "saturation_level" ])))
            xsDataDetector.setName(XSDataString("PILATUS 6M"))
            xsDataDetector.setType(XSDataString("pilatus6m"))
            xsDataExperimentalCondition.setDetector(xsDataDetector)

            # Beam object

            xsDataBeam = XSDataBeam()
            xsDataBeam.setWavelength(XSDataWavelength(float(dictPilatus6MHeader[ "Wavelength" ].split(" ")[0])))
            xsDataBeam.setExposureTime(XSDataTime(float(dictPilatus6MHeader[ "Exposure_time" ].split(" ")[0])))
            xsDataExperimentalCondition.setBeam(xsDataBeam)

            # Goniostat object
            xsDataGoniostat = XSDataGoniostat()
            fRotationAxisStart = float(dictPilatus6MHeader[ "Start_angle" ].split(" ")[0])
            fOscillationWidth = float(dictPilatus6MHeader[ "Angle_increment" ].split(" ")[0])
            xsDataGoniostat.setRotationAxisStart(XSDataAngle(fRotationAxisStart))
            xsDataGoniostat.setRotationAxisEnd(XSDataAngle(fRotationAxisStart + fOscillationWidth))
            xsDataGoniostat.setOscillationWidth(XSDataAngle(fOscillationWidth))
            xsDataExperimentalCondition.setGoniostat(xsDataGoniostat)
#
            # Create the image object
            xsDataImage = XSDataImage()
            xsDataImage.setPath(XSDataString(strPath))
            if "DateTime" in dictPilatus6MHeader:
                strTimeStamp = dictPilatus6MHeader[ "DateTime" ]
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
        EDVerbose.DEBUG("EDPluginExecReadImageHeaderPilatus6Mv10.postProcess")
        if (self.__xsDataResultReadImageHeader is not None):
            self.setDataOutput(self.__xsDataResultReadImageHeader)


    def readHeaderPilatus6M(self, _strImageFileName):
        """
        Returns an dictionary with the contents of a Pilatus 6M CBF image header.
        """
        dictPilatus6M = None
        pyFile = None
        try:
            pyFile = open(_strImageFileName, "r")
        except:
            EDVerbose.ERROR("EDPluginExecReadImageHeaderPilatus6Mv10.readHeaderPilauts6M: couldn't open file: " + _strImageFileName)
            self.setFailure()
        if (pyFile != None):
            EDVerbose.DEBUG("EDPluginExecReadImageHeaderPilatus6Mv10.readHeaderPilauts6M: Reading header from image " + _strImageFileName)
            pyFile.seek(0, 0)
            bContinue = True
            iMax = 60
            iIndex = 0
            while bContinue:
                strLine = pyFile.readline()
                iIndex += 1
                if (strLine.find("_array_data.header_contents") != -1):
                    dictPilatus6M = {}
                if (strLine.find("_array_data.data") != -1) or iIndex > iMax:
                    bContinue = False
                if (dictPilatus6M != None) and (strLine[0] == "#"):
                    # Check for date
                    strTmp = strLine[2:].replace("\r\n", "")
                    if strLine[6] == "/" and strLine[10] == "/":
                        dictPilatus6M["DateTime"] = strTmp
                    else:
                        strKey = strTmp.split(" ")[0]
                        strValue = strTmp.replace(strKey, "")[1:]
                        dictPilatus6M[strKey] = strValue
            pyFile.close()
        return dictPilatus6M


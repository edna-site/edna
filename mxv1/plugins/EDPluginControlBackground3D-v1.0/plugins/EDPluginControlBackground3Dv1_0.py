# coding: utf8
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDPluginControl import EDPluginControl
from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataBackground3Dv1_0")
from XSDataBackground3Dv1_0 import XSDataInputBackground3D

from XSDataMXv1 import XSDataInputReadImageHeader

from XSDataControlBackground3Dv1_0 import XSDataInputControlBackground3D
from XSDataControlBackground3Dv1_0 import XSDataResultControlBackground3D
from XSDataControlBackground3Dv1_0 import XSDataControlImageBackground3D


class EDPluginControlBackground3Dv1_0(EDPluginControl):
    """
    This plugin runs the Background3D program written by Sasha Popov
    """
    

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlBackground3D)
        self.setDataOutput(XSDataResultControlBackground3D())
        self.strEDPluginControlReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.edPluginControlReadImageHeader = None
        self.strEDPluginBackground3DName = "EDPluginBackground3Dv1_0"
        self.edPluginBackground3D = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlBackground3Dv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    
    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlBackground3Dv1_0.preProcess")
        self.edPluginControlReadImageHeader = self.loadPlugin(self.strEDPluginControlReadImageHeaderName, "SubWedgeAssemble")
        self.edPluginBackground3D = self.loadPlugin(self.strEDPluginBackground3DName, "Background3D")
        


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlBackground3Dv1_0.process")
        xsDataResultControlBackground3D = XSDataResultControlBackground3D()
        for xsDataFile in self.dataInput.image:
            edPluginControlReadImageHeader = self.loadPlugin(self.strEDPluginControlReadImageHeaderName)
            xsDataInputReadImageHeader = XSDataInputReadImageHeader()
            xsDataInputReadImageHeader.image = xsDataFile
            edPluginControlReadImageHeader.dataInput = xsDataInputReadImageHeader
            edPluginControlReadImageHeader.executeSynchronous()
            subWedge = edPluginControlReadImageHeader.dataOutput.subWedge
            xsDataInputBackground3D = XSDataInputBackground3D()
            beam = subWedge.experimentalCondition.beam
            detector = subWedge.experimentalCondition.detector
            goniostat = subWedge.experimentalCondition.goniostat
            xsDataInputBackground3D.detectorType = detector.type
            xsDataInputBackground3D.exposureTime = XSDataDouble(beam.exposureTime.value)
            xsDataInputBackground3D.detectorDistance = XSDataDouble(detector.distance.value)
            xsDataInputBackground3D.wavelength = XSDataDouble(beam.wavelength.value)
#            xsDataInputBackground3D.fractionPolatization : XSDataDouble optional
            orgx = detector.beamPositionY.value / detector.pixelSizeY.value
            orgy = detector.beamPositionX.value / detector.pixelSizeX.value
            xsDataInputBackground3D.orgx = XSDataDouble(orgx)
            xsDataInputBackground3D.orgy = XSDataDouble(orgy)
            xsDataInputBackground3D.oscillationRange = XSDataDouble(goniostat.oscillationWidth.value)
#            xsDataInputBackground3D.imageStep : XSDataDouble optional
            xsDataInputBackground3D.startingAngle = XSDataDouble(goniostat.rotationAxisStart.value)
            xsDataInputBackground3D.firstImageNumber = subWedge.image[0].number
            xsDataInputBackground3D.numberImages = XSDataInteger(1)
            strFileName = subWedge.image[0].path.value
            strPrefix = EDUtilsImage.getPrefix(strFileName)
            strSuffix = EDUtilsImage.getSuffix(strFileName)
            strXDSTemplate = "%s_????.%s" % (strPrefix, strSuffix)
            xsDataInputBackground3D.nameTemplateImage = XSDataString(os.path.join(os.path.dirname(strFileName), strXDSTemplate))
            edPluginBackground3D = self.loadPlugin(self.strEDPluginBackground3DName, "Background3D")
            edPluginBackground3D.dataInput = xsDataInputBackground3D
            edPluginBackground3D.executeSynchronous()
            if edPluginBackground3D.dataOutput.imageBackground != []:
                xsDataResultBackground3D = edPluginBackground3D.dataOutput.imageBackground[0]
                xsDataControlImageBackground3D = XSDataControlImageBackground3D()
                xsDataControlImageBackground3D.image = xsDataFile
                xsDataControlImageBackground3D.scale = xsDataResultBackground3D.scale
                xsDataControlImageBackground3D.bfactor = xsDataResultBackground3D.bfactor
                xsDataControlImageBackground3D.resolution = xsDataResultBackground3D.resolution
                xsDataControlImageBackground3D.correlation = xsDataResultBackground3D.correlation
                xsDataControlImageBackground3D.rfactor = xsDataResultBackground3D.rfactor
                xsDataControlImageBackground3D.b_coef = xsDataResultBackground3D.b_coef
                xsDataControlImageBackground3D.b_cryst = xsDataResultBackground3D.b_cryst
                xsDataControlImageBackground3D.estimate = xsDataResultBackground3D.estimate
                xsDataResultControlBackground3D.addImageBackground(xsDataControlImageBackground3D)
        self.dataOutput = xsDataResultControlBackground3D

     

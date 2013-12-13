# coding: utf8
#
#    Project: MX Plugin Exec
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

import os, time

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsTable              import EDUtilsTable
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

EDFactoryPluginStatic.loadModule("markupv1_7")
import markupv1_7

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataDnaTables import dna_tables

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString

from XSDataBackground3Dv1_0 import XSDataInputBackground3D
from XSDataBackground3Dv1_0 import XSDataResultBackground3D
from XSDataBackground3Dv1_0 import XSDataImageBackground3D

class EDPluginBackground3Dv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the Background3D program written by Sasha Popov
    """
    

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputBackground3D)
        self.setDataOutput(XSDataResultBackground3D())
        self.strImageLinkSubDirectory = "img"
        self.defaultFractionPolarization = 0.99
        self.defaultImageStep = 1
        self.startingAngle = 0.0

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBackground3Dv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    
    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginBackground3Dv1_0.preProcess")
        xsDataInputBackground3D = self.getDataInput()
        self.setScriptCommandline("background.dat")
        strCommands = self.generateCommands(xsDataInputBackground3D)
        self.createImageLinks(xsDataInputBackground3D)
        EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), "background.dat"), strCommands)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginBackground3Dv1_0.postProcess")
        self.dataOutput = self.parseOutput(os.path.join(self.getWorkingDirectory(),
                                                        self.getScriptLogFileName()))


    
    def generateCommands(self, _xsDataInputBackground3D):
        """
        This method creates the input file for background3D
        """
        self.DEBUG("EDPluginBackground3Dv1_0.generateCommands")
        strCommandText = None
        if _xsDataInputBackground3D is not None:
            strCommandText = "job single\n"
            strCommandText += "detector %s\n" % _xsDataInputBackground3D.detectorType.value
            strCommandText += "exposure %.3f\n" % _xsDataInputBackground3D.exposureTime.value
            strCommandText += "detector_distance %.3f\n" % _xsDataInputBackground3D.detectorDistance.value
            strCommandText += "X-ray_wavelength %.3f\n" % _xsDataInputBackground3D.wavelength.value
            if _xsDataInputBackground3D.fractionPolarization is None:
                fractionPolarization = self.defaultFractionPolarization
            else:
                fractionPolarization = _xsDataInputBackground3D.fractionPolarization.value
            strCommandText += "fraction_polarization %.3f\n" % fractionPolarization
            strCommandText += "pixel_min -1\n"
            strCommandText += "pixel_max 64000\n"
            strCommandText += "ix_min 1\n"
            strCommandText += "ix_max 1321\n"
            strCommandText += "iy_min 1198\n"
            strCommandText += "iy_max 1304\n"
            strCommandText += "orgx %.1f\n" % _xsDataInputBackground3D.orgx.value
            strCommandText += "orgy %.1f\n" % _xsDataInputBackground3D.orgy.value
            strCommandText += "oscillation_range %.3f\n" % _xsDataInputBackground3D.oscillationRange.value
            if _xsDataInputBackground3D.imageStep is None:
                imageStep = self.defaultImageStep
            else:
                imageStep = _xsDataInputBackground3D.imageStep.value
            strCommandText += "image_step %.3f\n" % imageStep
            if _xsDataInputBackground3D.startingAngle is None:
                startingAngle = self.defaultStartingAngle
            else:
                startingAngle = _xsDataInputBackground3D.startingAngle.value
            strCommandText += "starting_angle %.3f\n" % startingAngle
            strCommandText += "first_image_number %d\n" % _xsDataInputBackground3D.firstImageNumber.value
            strCommandText += "number_images %d\n" % _xsDataInputBackground3D.numberImages.value
            strCommandText += "name_template_image %s\n" % os.path.join(self.strImageLinkSubDirectory,
                                                                        os.path.basename(_xsDataInputBackground3D.nameTemplateImage.value))
            strCommandText += "end\n"
        return strCommandText
    

    def createImageLinks(self, _xsDataInputBackground3D):
        self.addListCommandPreExecution("rm -rf %s" % (self.strImageLinkSubDirectory))
        self.addListCommandPreExecution("mkdir -p %s" % (self.strImageLinkSubDirectory))
        strTemplate = os.path.basename(_xsDataInputBackground3D.nameTemplateImage.value)
        strTemplatePrefix, strTemplateSuffix = strTemplate.split("????")
        for index in range(_xsDataInputBackground3D.numberImages.value):
            iImageNo = _xsDataInputBackground3D.firstImageNumber.value + index
            strImageName = strTemplatePrefix + "%04d" % iImageNo + strTemplateSuffix
            strSourcePath = os.path.join(os.path.dirname(_xsDataInputBackground3D.nameTemplateImage.value),
                                           strImageName)
            strTargetPath = os.path.join(self.strImageLinkSubDirectory,
                                       strImageName)
            self.addListCommandPreExecution("ln -s %s %s" % (strSourcePath, strTargetPath))

        
        
  
        
    def parseOutput(self, _strFileName):
        """
        This method parses the output of background3D
        """
        xsDataResultBackground3D = XSDataResultBackground3D()
        strOutput = EDUtilsFile.readFile(_strFileName)
        # Skip the four first lines
        listOutput = strOutput.split("\n")[4:]
        for strLine in listOutput:
            xsDataImageBackground3D = XSDataImageBackground3D()
            # Remove empty strings ""
            listLine = filter(None, strLine.split(" "))
            if listLine != []:
                xsDataImageBackground3D.number = XSDataInteger(listLine[0])
                if listLine[1].startswith("-"):
                    xsDataImageBackground3D.b_coef = self.parseDouble(listLine[4])
                    xsDataImageBackground3D.b_cryst = self.parseDouble(listLine[5])
                    xsDataImageBackground3D.estimate = self.parseDouble(listLine[6])
                else:
                    xsDataImageBackground3D.scale = self.parseDouble(listLine[1])
                    xsDataImageBackground3D.bfactor = self.parseDouble(listLine[2])
                    xsDataImageBackground3D.resolution = self.parseDouble(listLine[3])
                    xsDataImageBackground3D.correlation = self.parseDouble(listLine[4])
                    xsDataImageBackground3D.rfactor = self.parseDouble(listLine[5])
                    xsDataImageBackground3D.b_coef = self.parseDouble(listLine[6])
                    xsDataImageBackground3D.b_cryst = self.parseDouble(listLine[7])
                    xsDataImageBackground3D.estimate = self.parseDouble(listLine[8])
                xsDataResultBackground3D.addImageBackground(xsDataImageBackground3D)
        return xsDataResultBackground3D
        
    def parseDouble(self, _strValue):
        returnValue = None
        try:
            returnValue = XSDataDouble(_strValue)
        except BaseException as ex:
            self.warning("Error when trying to parse '" + _strValue + "': %r" % ex)
        return returnValue

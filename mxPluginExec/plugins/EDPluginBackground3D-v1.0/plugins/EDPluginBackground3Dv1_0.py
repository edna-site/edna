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

from XSDataBackground3Dv1_0 import XSDataInputBackground3D
from XSDataBackground3Dv1_0 import XSDataResultBackground3D

class EDPluginBackground3Dv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the Background3D program written by Sasha Popov
    """
    

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputBackground3D)
        self.setDataOutput(XSDataResultBackground3D())


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    
    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.preProcess")
        xsDataInputBackground3D = self.getDataInput()
        self.setScriptCommandline(self.generateCommands(xsDataInputBackground3D))

        
        
    
    def generateCommands(self, _xsDataInputBackground3D):
        """
        This method creates the input file for background3D
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.generateCommands")
        strCommandText = None
        if _xsDataInputBackground3D is not None:
            strCommandText = "detector %s\n" % _xsDataInputBackground3D.detectorType.value
            strCommandText += "exposure %.3f\n" % _xsDataInputBackground3D.exposureTime.value
            strCommandText += "detector_distance %.3f\n" % _xsDataInputBackground3D.detectorDistance.value
            strCommandText += "X-ray_wavelength %.3f\n" % _xsDataInputBackground3D.wavelength.value
            strCommandText += "fraction_polarization %.3f\n" % _xsDataInputBackground3D.fractionPolatization.value
            strCommandText += "orgx %.1f\n" % _xsDataInputBackground3D.orgx.value
            strCommandText += "orgy %.1f\n" % _xsDataInputBackground3D.orgy.value
            strCommandText += "oscillation_range %.3f\n" % _xsDataInputBackground3D.oscillationRange.value
            strCommandText += "image_step %.3f\n" % _xsDataInputBackground3D.imageStep.value
            strCommandText += "starting_angle %.3f\n" % _xsDataInputBackground3D.startingAngle.value
            strCommandText += "first_image_number %d\n" % _xsDataInputBackground3D.firstImageNumber.value
            strCommandText += "number_images %d\n" % _xsDataInputBackground3D.numberImages.value
            strCommandText += "name_template_image %s\n" % _xsDataInputBackground3D.nameTemplateImage.value
        return strCommandText
    

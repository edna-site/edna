#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2010-2014 ESRF
#
#    Principal author:        Olof Svensson
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
__copyright__ = "Copyrigth (c) 2010 ESRF"

import os

from EDPluginControl import EDPluginControl

from XSDataPyarchThumbnailGeneratorv1_0 import XSDataInputPyarchThumbnailGenerator
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataInputPyarchThumbnailGeneratorParallel
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataResultPyarchThumbnailGeneratorParallel



class EDPluginControlPyarchThumbnailGeneratorParallelv1_0(EDPluginControl):
    """
    This control plugin runs the EDPluginControlPyarchThumbnailGeneratorv1_0 in parallel for many images
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputPyarchThumbnailGeneratorParallel)
        self.strControlThumbnailPluginName = "EDPluginControlPyarchThumbnailGeneratorv1_0"
        self.xsDataResult = XSDataResultPyarchThumbnailGeneratorParallel()
        self.setDataOutput(self.xsDataResult)
        



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorParallelv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDiffractionImage(), "No diffraction image file path")



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorParallelv1_0.preProcess")
        # Check that the input image exists and is of the expected type
        strPathToDiffractionImage = self.getDataInput().getDiffractionImage()[0].getPath().getValue()
        strImageFileNameExtension = os.path.splitext(strPathToDiffractionImage)[1]
        if not strImageFileNameExtension in [".img", ".marccd", ".mccd", ".cbf"]:
            self.error("Unknown image file name extension for pyarch thumbnail generator: %s" % strPathToDiffractionImage)
            self.setFailure()
            


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorParallelv1_0.process")
        listPlugins = []
        for xsDataFile in self.dataInput.diffractionImage:
            edPluginControlThumbnail = self.loadPlugin(self.strControlThumbnailPluginName)
            xsDataInputPyarchThumbnailGenerator = XSDataInputPyarchThumbnailGenerator()
            xsDataInputPyarchThumbnailGenerator.diffractionImage = xsDataFile
            xsDataInputPyarchThumbnailGenerator.forcedOutputDirectory = self.dataInput.forcedOutputDirectory
            xsDataInputPyarchThumbnailGenerator.waitForFileTimeOut = self.dataInput.waitForFileTimeOut
            edPluginControlThumbnail.dataInput = xsDataInputPyarchThumbnailGenerator
            listPlugins.append(edPluginControlThumbnail)
            edPluginControlThumbnail.execute()
        for edPlugin in listPlugins:
            edPlugin.synchronize()
            self.dataOutput.addPathToJPEGImage(edPlugin.dataOutput.pathToJPEGImage)
            self.dataOutput.addPathToThumbImage(edPlugin.dataOutput.pathToThumbImage)


        

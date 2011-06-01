#
#    Project: ExecPlugins / Saxs Group / SaxsAdd
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010 ESRF
#
#    Principal author:       Jerome Kieffer
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


"""
Execution plugin for Sacs Add:

Add two images (taking into account variances ...)

"""


__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010 - ESRF"

import os
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataSaxsv1_0 import XSDataInputSaxsAddv1_0, XSDataImage
from XSDataSaxsv1_0 import XSDataResultSaxsAddv1_0 , XSDataString

class EDPluginExecSaxsAddv1_0(EDPluginExecProcessScript):
    """
    Execution plugin for Sacs Add:
    multiply and add constant to images (or set of images)

    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsAddv1_0)
        self.inputImages = []
        self.outputImage = None
        self.options = None




    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsAddv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImage(), "InputImages is None")
        if len(self.getDataInput().getInputImage()) != 2:
            self.checkMandatoryParameters(None, "There should be exactly 2 input images")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsAddv1_0.preProcess")
        xsdIn = self.getDataInput()
        for oneXSDimage in xsdIn.getInputImage():
            self.inputImages.append(oneXSDimage.getPath().getValue())
            if not os.path.isfile(self.inputImages[-1]):
                EDVerbose.WARNING("Input file %s does not exist ... try to go on anyway" % self.inputImages[-1])
                self.inputImages[-1] = "="
        if xsdIn.getOutputImage() is not None:
            self.outputImage = xsdIn.getOutputImage().getPath().getValue()
        if xsdIn.getOptions() is not None:
            self.options = xsdIn.getOptions().getValue()

        #Create the command line to run the program
        self.generateSaxsAddCommand()



    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsAddv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSaxsAddv1_0()
        if self.outputImage is None:
            self.outputImage = "output.edf"
        if os.path.isfile(self.outputImage):
            xsdFile = XSDataImage()
            xsdFile.setPath(XSDataString(os.path.abspath(self.outputImage)))
            xsDataResult.setOutputImage(xsdFile)

        self.setDataOutput(xsDataResult)


    def generateSaxsAddCommand(self):
        """
        Generation of the command line.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsAddv1_0.generateSaxsAddCommand")

        if self.options is None:
            strOptions = ""
        else:
            strOptions = self.options

        if len(self.inputImages) == 2:
            strOptions += " %s %s " % tuple(self.inputImages)
        else:
            strOptions += " = = "


        if self.outputImage is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.outputImage

        EDVerbose.DEBUG("saxs_add " + strOptions)
        self.setScriptCommandline(strOptions)


#
#    Project: ExecPlugins / Saxs Group / SaxsMac
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
Execution plugin for Sacs Mac:
multiply and add constant to images (or set of images)

"""


__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010 - ESRF"

import os
from EDVerbose                  import EDVerbose
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from XSDataCommon               import XSDataImage, XSDataString
from XSDataSaxsv1_0             import XSDataInputSaxsMacv1_0, XSDataResultSaxsMacv1_0

class EDPluginExecSaxsMacv1_0(EDPluginExecProcessScript):
    """
    Execution plugin for Sacs Mac:
    multiply and add constant to images (or set of images)

    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsMacv1_0)
        self.inputImage = None
        self.outputImage = None
        self.multConst = None
        self.addConst = None
        self.firstImage = None
        self.lastImage = None
        self.increment = None
        self.dummy = None
        self.options = None




    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsMacv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        # there are no mandatory parameters ....

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsMacv1_0.preProcess")
        xsdIn = self.getDataInput()
        if xsdIn.getInputImage() is not None:
            self.inputImage = xsdIn.getInputImage().getPath().getValue()
            if not os.path.isfile(self.inputImage) and "%" not in self.inputImage:
                EDVerbose.WARNING("Input file %s does not exist ... try to go on anyway" % self.inputImage)
                self.inputImage = None
        if xsdIn.getOutputImage() is not None:
            self.outputImage = xsdIn.getOutputImage().getPath().getValue()
        if xsdIn.getFirstImage() is not None:
            self.firstImage = xsdIn.getFirstImage().getValue()
        if xsdIn.getLastImage() is not None:
            self.lastImage = xsdIn.getLastImage().getValue()
        if xsdIn.getOptions() is not None:
            self.options = xsdIn.getOptions().getValue()
        if xsdIn.getDummy() is not None:
            self.dummy = xsdIn.getDummy().getValue()
        if xsdIn.getIncrement() is not None:
            self.increment = xsdIn.getIncrement().getValue()
        if xsdIn.getAddConst() is not None:
            self.addConst = xsdIn.getAddConst().getValue()
        if xsdIn.getMultConst() is not None:
            self.multConst = xsdIn.getMultConst().getValue()
        #Create the command line to run the program
        self.generateSaxsMacCommand()



    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsMacv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSaxsMacv1_0()
        if self.outputImage is None:
            self.outputImage = "output.edf"
        if os.path.isfile(self.outputImage):
            xsdFile = XSDataImage()
            xsdFile.setPath(XSDataString(os.path.abspath(self.outputImage)))
            xsDataResult.setOutputImage(xsdFile)

        self.setDataOutput(xsDataResult)


    def generateSaxsMacCommand(self):
        """
        Generation of the command line.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsMacv1_0.generateSaxsMacCommand")

#        if self.options is not None and \
#            self.inputImage is not None and\
#            self.outputImage is not None and\
#            self.multConst is None and\
#             self.addConst is None:
#            strOptions = "%s %s %s" % (self.options, self.inputImage, self.outputImage)
#
#        else:
        if self.options is None:
            strOptions = ""
        else:
            strOptions = self.options

        if self.inputImage is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.inputImage

        if self.outputImage is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.outputImage

        if self.firstImage is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.firstImage
        if self.lastImage is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.lastImage
        if self.increment is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.increment
        if self.dummy is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.dummy

        strOptions += " = = " #for the image dimensions.

        if self.multConst is None :
            strOptions += " ="
        else:
            strOptions += " %s" % self.multConst

        if self.addConst is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.addConst





        EDVerbose.DEBUG("saxs_mac " + strOptions)
        self.setScriptCommandline(strOptions)


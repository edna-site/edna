#
#    Project: ExecPlugins / Saxs Group / SaxsCurves
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
Execution plugin for Sacs Curves:

Convert an image into an ascii file (spec like) radius 

"""


__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010 - ESRF"

import os
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataSaxsv1_0 import XSDataInputSaxsCurvesv1_0, XSDataFile
from XSDataSaxsv1_0 import XSDataResultSaxsCurvesv1_0 , XSDataString

class EDPluginExecSaxsCurvesv1_0(EDPluginExecProcessScript):
    """
    Execution plugin for Sacs Curves:
    multiply and add constant to images (or set of images)
 
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsCurvesv1_0)
        self.inputImage = None
        self.outputDataFile = None
        self.options = None
        self.headerMarker = "#"
        self.extraHeader = []





    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsCurvesv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#        self.checkMandatoryParameters(self.getDataInput().getInputImage(), "InputImages is None")
#        if len(self.getDataInput().getInputImage()) != 2:
#            self.checkMandatoryParameters(None, "There should be exactly 2 input images")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsCurvesv1_0.preProcess")
        xsdIn = self.getDataInput()
        if  xsdIn.getInputImage() is not None:
            self.inputImage = xsdIn.getInputImage().getPath().getValue()
            if not os.path.isfile(self.inputImage):
                EDVerbose.WARNING("Input file %s does not exist ... try to go on anyway" % self.inputImage)
                self.inputImage = "="
        if xsdIn.getOutputDataFile() is not None:
            self.outputDataFile = xsdIn.getOutputDataFile().getPath().getValue()
        if xsdIn.getOptions() is not None:
            self.options = xsdIn.getOptions().getValue()
        for oneHeader in  xsdIn.getExtraHeaders():
            self.extraHeader.append(oneHeader.getValue())
        if xsdIn.getHeaderMarker() is not None:
            self.headerMarker = xsdIn.getHeaderMarker().getValue()


        #Create the command line to run the program
        self.generateSaxsCurvesCommand()



    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsCurvesv1_0.postProcess")

        #Append the headers is needed
        if self.extraHeader != []:
            datalines = open(self.outputDataFile, "rb").readlines()
            datafile = open(self.outputDataFile, "w")
            for oneLine in self.extraHeader:
                datafile.write(self.headerMarker + oneLine.strip() + os.linesep)
            for oneLine in datalines:
                datafile.write(oneLine.strip() + os.linesep)
            datafile.close()
        # Create some output data
        xsDataResult = XSDataResultSaxsCurvesv1_0()
        if self.outputDataFile is None:
            self.outputDataFile = "output.edf"
        if os.path.isfile(self.outputDataFile):
            xsdFile = XSDataFile()
            xsdFile.setPath(XSDataString(os.path.abspath(self.outputDataFile)))
            xsDataResult.setOutputDataFile(xsdFile)

        self.setDataOutput(xsDataResult)


    def generateSaxsCurvesCommand(self):
        """
        Generation of the command line.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsCurvesv1_0.generateSaxsCurvesCommand")

        if self.headerMarker != "#":
            strOptions = " -hdml '%s'" % self.headerMarker
        else:
            strOptions = ""
        if self.options is not None:

            strOptions += " %s" % self.options

        if (self.outputDataFile is not None)  and (self.options is not None):
            if  ("-ext" not  in self.options)  and not self.outputDataFile.endswith(".txt"):
                strOptions += " -ext %s" % os.path.splitext(self.outputDataFile)[1]

        if self.inputImage is not None :
            strOptions += " %s" % self.inputImage
        else:
            strOptions += " ="


        if self.outputDataFile is None:
            strOptions += " ="
        else:
            strOptions += " %s" % self.outputDataFile

        EDVerbose.DEBUG("saxs_curves " + strOptions)
        self.setScriptCommandline(strOptions)


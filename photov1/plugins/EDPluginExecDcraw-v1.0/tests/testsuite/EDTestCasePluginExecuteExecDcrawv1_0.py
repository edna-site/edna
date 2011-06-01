#
#    Project: Photo-v1.0
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

import os, sys

from EDVerbose                      import EDVerbose
from EDAssert                       import EDAssert
from EDTestCasePluginExecute        import EDTestCasePluginExecute
from XSDataPhotov1                  import XSDataInputExecDcrawv1, XSDataResultExecDcrawv1
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
import  Image, ImageChops


class EDTestCasePluginExecuteExecDcrawv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Dcrawv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDcrawv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Dcraw.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDcraw_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDcraw_reference.xml"))
        self.inputFile = None
        self.outputFile = None
        self.xsDataResultReference = None

    def preProcess(self):
       """
       PreProcess of the execution test: download a set of images  from http://www.edna-site.org
       """
       EDTestCasePluginExecute.preProcess(self)

       xsDataInput = XSDataInputExecDcrawv1.parseString(self.readAndParseFile(self.getDataInputFile()))
       self.inputFile = xsDataInput.getRawImagePath().getPath().getValue()

       self.xsDataResultReference = XSDataResultExecDcrawv1.parseString(self.readAndParseFile(self.getReferenceDataOutputFile()))
       self.outputFile = self.xsDataResultReference.getOutputPath().getPath().getValue()

       self.loadTestImage([os.path.basename(self.inputFile), os.path.basename(self.outputFile) ])

       if not os.path.isdir(os.path.dirname(self.outputFile)):
           os.makedirs(os.path.dirname(self.outputFile))
       if os.path.isfile(self.outputFile):
           EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.outputFile)
           os.remove(self.outputFile)


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
################################################################################
# Compare XSDataResults
################################################################################
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")

        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(self.xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")
################################################################################
# Compare image Files
################################################################################
        outputData = Image.open(self.outputFile)
        referenceData = Image.open(os.path.join(self.getTestsDataImagesHome(), os.path.basename(self.outputFile)))
        delta = ImageChops.difference(outputData, referenceData)
        deltaColor = delta.getextrema()
        i = 0
        for color in deltaColor:
            EDAssert.lowerThan(color[1], 12, "Maximum tone variation is %s for channel %s" % (color[1], "RGBA"[i]))
            i += 1
#Nota the factor 12 is necessary between 32/64 bits computers, More important than CPU brand  

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testDcrawv1_0instance = EDTestCasePluginExecuteControlDcrawv1_0("EDTestCasePluginExecuteExecDcrawv1_0")
    testDcrawv1_0instance.execute()

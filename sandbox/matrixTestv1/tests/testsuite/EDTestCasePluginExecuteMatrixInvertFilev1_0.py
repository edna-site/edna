#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer, jerome.kieffer@esrf.fr
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

__author__ = "Jerome Kieffer, jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataMatrixv1                      import XSDataInputMatrixInvertFile, XSDataResultMatrixInvertFile
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_r5080")

import numpy
import fabio.openimage
from fabio.openimage import openimage
import  ImageChops

class EDTestCasePluginExecuteMatrixInvertFilev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin MatrixInvertFilev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginControlMatrixInvertFilev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MatrixInvertFile.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMatrixInvertFile_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMatrixInvertFile_reference.xml"))
    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and delete any output file
        """
        EDTestCasePluginExecute.preProcess(self)

        xsDataInput = XSDataInputMatrixInvertFile.parseString(self.readAndParseFile(self.getDataInputFile()))
        self.inputFile = xsDataInput.getInputMatrixFile().getPath().getValue()

        self.xsDataResultReference = XSDataResultMatrixInvertFile.parseString(self.readAndParseFile(self.getReferenceDataOutputFile()))
        self.outputFile = self.xsDataResultReference.getOutputMatrixFile().getPath().getValue()

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
        xsDataResultReference = XSDataResultMatrixInvertFile.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), _strComment="XSDataResult output are the same")

################################################################################
# Check that  outputData * inputData - Id = 0
################################################################################
        outputData = openimage(self.outputFile).data
        size = outputData.shape[0]
        inputData = openimage(self.inputFile).data
        EDAssert.arraySimilar(numpy.matrix(outputData) * numpy.matrix(inputData), numpy.identity(size), _fAbsMaxDelta=2e-4, _strComment="output x input = Id ")


################################################################################
# Compare image Files
################################################################################
        referenceData = openimage(os.path.join(self.getTestsDataImagesHome(), os.path.basename(self.outputFile))).data
        EDAssert.arraySimilar(referenceData, outputData, _fAbsMaxDelta=1e-5, _strComment="images are the same")



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testMatrixInvertFilev1_0instance = EDTestCasePluginExecuteMatrixInvertFilev1_0("EDTestCasePluginExecuteMatrixInvertFilev1_0")
    testMatrixInvertFilev1_0instance.execute()

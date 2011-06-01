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
from XSDataMatrixv1                      import XSDataResultWriteMatrix, XSDataInputWriteMatrix
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_r5080")



class EDTestCasePluginExecuteExecMatrixWritev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin MatrixWritev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecMatrixWritev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MatrixWrite.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMatrixWrite_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMatrixWrite_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and delete any output file
        """
        EDTestCasePluginExecute.preProcess(self)

        xsDataInput = XSDataInputWriteMatrix.parseString(self.readAndParseFile(self.getDataInputFile()))
        self.inputFile = xsDataInput.getOutputFile().getPath().getValue()

        self.xsDataResultReference = XSDataResultWriteMatrix.parseString(self.readAndParseFile(self.getReferenceDataOutputFile()))
        self.outputFile = self.xsDataResultReference.getOutputFile().getPath().getValue()

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
        xsDataResultReference = XSDataResultWriteMatrix.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testMatrixWritev1_0instance = EDTestCasePluginExecuteControlMatrixWritev1_0("EDTestCasePluginExecuteExecMatrixWritev1_0")
    testMatrixWritev1_0instance.execute()

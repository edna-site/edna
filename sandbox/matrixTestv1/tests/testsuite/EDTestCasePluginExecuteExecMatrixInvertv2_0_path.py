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

import os, sys, tempfile
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataMatrixv1                      import XSDataResultMatrixInvertv2, XSDataInputMatrixInvertv2
from EDFactoryPluginStatic               import EDFactoryPluginStatic
from EDShare                             import EDShare
from EDUtilsPlatform                     import EDUtilsPlatform


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)

if "USER" not in os.environ:
    os.environ["USER"] = "tester"
destDir = os.path.join(tempfile.gettempdir(), "edna-%s" % os.environ["USER"])
EDShare.initialize(destDir)


class EDTestCasePluginExecuteExecMatrixInvertv2_0_path(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin MatrixInvertv2_0 (Using shared arrays via HDF5)
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecMatrixInvertv2_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MatrixInvert.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMatrixInvertv2_path.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMatrixInvertv2_path.xml"))
        self.inputFile = None
        self.outputFile = None

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and delete any output file
        """
        EDTestCasePluginExecute.preProcess(self)

        xsDataInput = XSDataInputMatrixInvertv2.parseString(self.readAndParseFile(self.getDataInputFile()))
        self.inputFile = xsDataInput.getInputMatrix().getPath().getValue()

        self.xsDataResultReference = XSDataResultMatrixInvertv2.parseString(self.readAndParseFile(self.getReferenceDataOutputFile()))
        self.outputFile = self.xsDataResultReference.getOutputMatrix().getPath().getValue()

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
        strExpectedOutput = self.readAndParseFile(self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultMatrixInvertv2.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), _fStrSimilar=0.99, _strComment="XSDataResult output are the same")
        output = fabio.open(self.outputFile).data
        ref = fabio.open(os.path.join(self.getTestsDataImagesHome(), "inverted.edf")).data
        EDAssert.arraySimilar(output , ref, "arrays are the same", 1e-4)


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testMatrixInvertv2_0instance = EDTestCasePluginExecuteExecMatrixInvertv2_0_path("EDTestCasePluginExecuteExecMatrixInvertv2_0_path")
    testMatrixInvertv2_0instance.execute()

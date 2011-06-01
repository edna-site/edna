#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
__copyright__ = "ESRF"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataSaxsv1_0                      import XSDataResultSaxsAddMetadatav1_0



class EDTestCasePluginExecuteExecSaxsAddMetadatav1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SaxsAddMetadatav1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSaxsAddMetadatav1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SaxsAddMetadata.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSaxsAddMetadata_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSaxsAddMetadata_reference.xml"))
        self.testImage = "saxsAddMetadata.edf"
        self.refImage = "saxsDelMetadata.edf"
        self.testOutput = os.path.join(self.getTestsDataImagesHome(), self.testImage)
        self.refOutput = os.path.join(self.getTestsDataImagesHome(), self.refImage)

    def preProcess(self):
        """
        PreProcess of the execution test:remove existing image and download a fresh one from http://www.edna-site.org
        """
        EDTestCasePluginExecute.preProcess(self)

        if os.path.isfile(self.testOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.testOutput)
            os.remove(self.testOutput)

        if os.path.isfile(self.refOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.refOutput)
            os.remove(self.refOutput)

        self.loadTestImage([self.testImage, self.refImage])


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())

        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultSaxsAddMetadatav1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


        outputData = str(open(self.testOutput, "rb").read()[:8196])
        referenceData = str(open(self.refOutput, "rb").read()[:8196])
        EDAssert.strAlmostEqual(outputData, referenceData, "Same headers")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

    def postProcess(self):
        if os.path.isfile(self.testOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.testOutput)
            os.remove(self.testOutput)

        if os.path.isfile(self.refOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.refOutput)
            os.remove(self.refOutput)





if __name__ == '__main__':

    testSaxsAddMetadatav1_0instance = EDTestCasePluginExecuteControlSaxsAddMetadatav1_0("EDTestCasePluginExecuteExecSaxsAddMetadatav1_0")
    testSaxsAddMetadatav1_0instance.execute()

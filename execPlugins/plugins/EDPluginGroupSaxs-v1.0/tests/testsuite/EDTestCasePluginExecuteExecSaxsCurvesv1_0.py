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

import os#, distutils.util, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataSaxsv1_0                      import XSDataResultSaxsCurvesv1_0

class EDTestCasePluginExecuteExecSaxsCurvesv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SaxsCurvesv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSaxsCurvesv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SaxsCurves.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSaxsCurves_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSaxsCurves_reference.xml"))
    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "bsa_013_08.ang", "bsa_013_08.dat" ])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultSaxsCurvesv1_0.parseString(strExpectedOutput)
        self.refOutput = xsDataResultReference.getOutputDataFile().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % self.refOutput)
        if not os.path.isdir(os.path.dirname(self.refOutput)):
            os.makedirs(os.path.dirname(self.refOutput))
        if os.path.isfile(self.refOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.refOutput)
            os.remove(self.refOutput)


    def testExecute(self):
        """
        """
        self.run()

        plugin = self.getPlugin()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultSaxsCurvesv1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


        outputData = open(xsDataResultObtained.getOutputDataFile().getPath().getValue(), "rb").read()
        referenceData = open(os.path.join(self.getTestsDataImagesHome(), "bsa_013_08.dat"), "rb").read()

        EDVerbose.DEBUG("Expected= %s" % os.path.join(self.getTestsDataImagesHome(), "bsa_013_08.dat"))
        EDVerbose.DEBUG("Obtained= %s" % xsDataResultObtained.getOutputDataFile().getPath().getValue())

        EDAssert.strAlmostEqual(outputData, referenceData, _strComment="Curves are the same", _strExcluded="bsa_013_08")



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edtestSaxsCurvesv1_0 = EDTestCasePluginExecuteExecSaxsCurvesv1_0("EDTestCasePluginExecuteExecSaxsCurvesv1_0")
    edtestSaxsCurvesv1_0.execute()

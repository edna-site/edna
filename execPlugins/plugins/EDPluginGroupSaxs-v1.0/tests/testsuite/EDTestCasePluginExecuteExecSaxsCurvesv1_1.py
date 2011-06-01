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
from EDFactoryPluginStatic import EDFactoryPluginStatic
# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

class EDTestCasePluginExecuteExecSaxsCurvesv1_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SaxsCurvesv1_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSaxsCurvesv1_1")
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


        outputData = os.linesep.join([ i.strip() for i in open(xsDataResultObtained.getOutputDataFile().getPath().getValue(), "rb") if not i.startswith("#")])
        referenceData = os.linesep.join([ i.strip() for i in open(os.path.join(self.getTestsDataImagesHome(), "bsa_013_08.dat"), "rb") if not i.startswith("#")])

#        EDVerbose.DEBUG("Expected= %s" % os.path.join(self.getTestsDataImagesHome(), "bsa_013_08.dat"))
#        EDVerbose.DEBUG("Obtained= %s" % xsDataResultObtained.getOutputDataFile().getPath().getValue())

        EDAssert.strAlmostEqual(outputData, referenceData, _strComment="Curves are the same",)



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edtestSaxsCurvesv1_1 = EDTestCasePluginExecuteExecSaxsCurvesv1_1("EDTestCasePluginExecuteExecSaxsCurvesv1_1")
    edtestSaxsCurvesv1_1.execute()

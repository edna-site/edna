#
#    Project: SAXS
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 - ESRF
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

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataSaxsv1_0                      import XSDataResultSaxsAnglev1_0
from EDFactoryPluginStatic      import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")

import fabio.openimage
from fabio.openimage import openimage


class EDTestCasePluginExecuteExecSaxsAnglev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SaxsAnglev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSaxsAnglev1_0")
#
# Commented out so that the default configuration is taken for the test, not the one specific for the tests.
#
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SaxsAngle.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSaxsAngle_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSaxsAngle_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "Moke-2th10-tilt0-rot0.%s" % i for i in ("edf", "azim")])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultSaxsAnglev1_0.parseString(strExpectedOutput)
        self.refOutput = xsDataResultReference.getRegroupedDataFile().getPath().getValue()
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
        xsDataResultReference = XSDataResultSaxsAnglev1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


        outputData = openimage(xsDataResultObtained.getRegroupedDataFile().getPath().getValue()).data
        referenceData = openimage(os.path.join(self.getTestsDataImagesHome(), "Moke-2th10-tilt0-rot0.azim")).data
        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.4, _fScaledMaxDelta=0.5, _strComment="Images are the same")



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testSaxsAnglev1_0instance = EDTestCasePluginExecuteExecSaxsAnglev1_0("EDTestCasePluginExecuteExecSaxsAnglev1_0")
    testSaxsAnglev1_0instance.execute()

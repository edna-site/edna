#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataExecCommandLine               import XSDataInputExecCommandLine
from XSDataExecCommandLine               import XSDataResultExecCommandLine



class EDTestCasePluginExecuteExecCommandLinev10(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin CommandLinev10
    """

    def __init__(self, _edStringTestName=None):
        """
        Constructor of the test
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecCommandLinev10")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_CommandLine.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCommandLine_fromStdout_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultCommandLine_fromStdout_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"


    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "test_region1_dark_1_0041.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultExecCommandLine.parseString(strExpectedOutput)
        outputFileName = xsDataResultReference.getOutputFilename().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)
        outputDirName = os.path.dirname(outputFileName)
        if not os.path.isdir(outputDirName):
            os.makedirs(outputDirName, int("777", 8))



    def testExecute(self):
        """
        execute the execution test 
        """
        self.run()
        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultExecCommandLine.parseString(strExpectedOutput)
        xsDataResultObtained = XSDataResultExecCommandLine.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal())



##############################################################################

    def process(self):
        """
        run the test
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    testCommandLinev10instance = EDTestCasePluginExecuteExecCommandLinev10("EDTestCasePluginExecuteExecCommandLinev10")
    testCommandLinev10instance.execute()

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

import os, shutil
from EDUtilsTest                        import EDUtilsTest
from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from XSDataExecCommandLine              import XSDataInputExecCommandLine
from XSDataExecCommandLine              import XSDataResultExecCommandLine
from EDTestCasePluginExecute            import EDTestCasePluginExecute

class EDTestCasePluginExecuteExecCommandLinev10_fireAndForget(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin CommandLinev10
    """

    def __init__(self, _edStringTestName=None):
        """
        constructor of the test
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecCommandLinev10")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_CommandLine.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCommandLine_fireAndForget_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultCommandLine_fireAndForget_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"


    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "test_region1_dark_1_0040.edf"])

        xsDataInputReference = XSDataInputExecCommandLine.parseString(self.readAndParseFile (self.getDataInputFile()))
        strInputFile = xsDataInputReference.getInputFileName().getPath().getValue()
        if not(os.path.isdir(os.path.dirname(strInputFile))):
            os.makedirs(os.path.dirname(strInputFile), int("777", 8))
        EDVerbose.DEBUG("temporary filename is :" + strInputFile)
        shutil.copy(os.path.join(EDUtilsTest.getTestsDataHome(), "images", "test_region1_dark_1_0040.edf"), strInputFile)
        strInputXML = self.readAndParseFile (self.getDataInputFile())
        xsDataInputReference = XSDataInputExecCommandLine.parseString(strInputXML)
        outputFileName = xsDataInputReference.getInputFileName().getPath().getValue() + ".gz"
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)



    def testExecute(self):
        """
        execute the execution test 
        """
        EDVerbose.DEBUG("Timeout seems to be: %s" % self.getPlugin().getTimeOut())

        self.run()
#        plugin = self.getPlugin()
#        EDVerbose.DEBUG("Timeout seems to be: %s" % self.getPlugin().getTimeOut())
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
        Execution test
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    testCommandLinev10instance = EDTestCasePluginExecuteExecCommandLinev10_fireAndForget("EDTestCasePluginExecuteExecCommandLinev10_fireAndForget")
    testCommandLinev10instance.execute()

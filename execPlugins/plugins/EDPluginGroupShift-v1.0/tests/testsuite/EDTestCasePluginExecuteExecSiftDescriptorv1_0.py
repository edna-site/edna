#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
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
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataShiftv1_0 import XSDataResultSiftDescriptor

class EDTestCasePluginExecuteExecSiftDescriptorv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SiftDescriptorv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSiftDescriptorv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SiftDescriptor.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSiftDescriptor_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSiftDescriptor_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "FullFieldXAS_00.jpg" ])


    def testExecute(self):
        """
        """
        self.run()

        plugin = self.getPlugin()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultSiftDescriptor.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), _strExcluded="EDTestCasePluginExecuteExecSiftDescriptorv1_0", _fRelError=0.0, _fAbsError=0.3, _strComment="XML out are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testSiftDescriptorv1_0instance = EDTestCasePluginExecuteControlSiftDescriptorv1_0("EDTestCasePluginExecuteExecSiftDescriptorv1_0")
    testSiftDescriptorv1_0instance.execute()

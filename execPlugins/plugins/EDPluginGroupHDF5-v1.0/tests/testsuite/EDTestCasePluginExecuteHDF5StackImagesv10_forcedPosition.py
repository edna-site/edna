#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF Grenoble
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
__copyright__ = "ESRF Grenoble"

import os

from EDVerbose                              import EDVerbose
from EDAssert                               import EDAssert
from EDTestCasePluginExecute                import EDTestCasePluginExecute
from XSDataHDF5v1_0                         import XSDataInputHDF5StackImages
from XSDataHDF5v1_0                         import XSDataResultHDF5StackImages
from EDTestCasePluginExecuteHDF5StackImagesv10 import EDTestCasePluginExecuteHDF5StackImagesv10

class EDTestCasePluginExecuteHDF5StackImagesv10_forcedPosition(EDTestCasePluginExecuteHDF5StackImagesv10):
    """
    Those are all execution tests for the EDNA Exec plugin HDF5StackImagesv10
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecuteHDF5StackImagesv10.__init__(self, "EDTestCasePluginExecuteHDF5StackImagesv10_forcedPosition")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
                                               "XSConfiguration_HDF5StackImages.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputHDF5StackImages_reference_ForcedPosition.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultHDF5StackImages_reference.xml"))
    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/edna-$USER/stack.h5 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "test_region1_dark_1_0040.edf",
                            "test_region1_dark_1_0041.edf",
                            "test_region1_dark_1_0042.edf",
                            "test_region1_dark_1_0043.edf",
                            "test_region1_dark_1_0044.edf"])
        strExpectedOutput = self.readAndParseFile (self.getDataInputFile())
        xsDataResultReference = XSDataInputHDF5StackImages.parseString(strExpectedOutput)

if __name__ == '__main__':

    testHDF5StackImagesv10instance = EDTestCasePluginExecuteHDF5StackImagesv10_forcedPosition("EDTestCasePluginExecuteHDF5StackImagesv10_forcedPosition")
    testHDF5StackImagesv10instance.execute()

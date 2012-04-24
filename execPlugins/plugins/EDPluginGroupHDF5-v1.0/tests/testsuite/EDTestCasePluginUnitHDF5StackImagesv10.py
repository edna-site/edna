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

import os, time

from EDVerbose                      import EDVerbose
from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDPluginHDF5StackImagesv10     import EDPluginHDF5StackImagesv10
from EDAssert                       import EDAssert
from XSDataHDF5v1_0 import XSDataInputHDF5StackImages
from XSDataCommon import XSDataString, XSDataImage, XSDataFile

class EDTestCasePluginUnitHDF5StackImagesv10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin HDF5StackImagesv10
    we test mainly the static methods f the class
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginHDF5StackImagesv10")
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputHDF5StackImages_reference.xml")



    def testCheckParameters(self):
        xsDataInput = XSDataInputHDF5StackImages(HDF5File=XSDataFile(),
                                                 internalHDF5Path=XSDataString(),
                                                 inputImageFile=[XSDataImage()])
        edPluginExecHDF5StackImages = self.createPlugin()
        edPluginExecHDF5StackImages.setDataInput(xsDataInput)
        edPluginExecHDF5StackImages.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)

if __name__ == '__main__':

    edTestCasePluginUnitHDF5StackImagesv10 = EDTestCasePluginUnitHDF5StackImagesv10("EDTestCasePluginUnitHDF5StackImagesv10")
    edTestCasePluginUnitHDF5StackImagesv10.execute()

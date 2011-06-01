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
from EDPluginHDF5MapOfSpectrav10    import EDPluginHDF5MapOfSpectrav10
from EDAssert                       import EDAssert

class EDTestCasePluginUnitHDF5MapSpectrav10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin HDF5MapOfSpectrav10
    we test mainly the static methods f the class
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginHDF5MapOfSpectrav10")
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputHDF5MapOfSpectra_reference.xml")



    def testCheckParameters(self):
        xsDataInput = self.readAndParseFile(self.strReferenceInputFile)
        edPluginExecHDF5MapOfSpectra = self.createPlugin()
        edPluginExecHDF5MapOfSpectra.setDataInput(xsDataInput)
        edPluginExecHDF5MapOfSpectra.checkParameters()


    def process(self):
        self.addTestMethod(self.testCheckParameters)

if __name__ == '__main__':

    edTestCasePluginUnitHDF5MapOfSpectrav10 = EDTestCasePluginUnitHDF5MapSpectrav10("EDTestCasePluginUnitHDF5MapSpectrav10")
    edTestCasePluginUnitHDF5MapOfSpectrav10.execute()

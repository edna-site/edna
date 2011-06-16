#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble

#    Principal author:       Jerome Kieffer, jerome.kieffer@esrf.fr
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

__author__ = "Jerome Kieffer, jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataMatrixv1 import XSDataInputMatrixInvertFile
from XSDataCommon import XSDataFile

class EDTestCasePluginUnitMatrixInvertFilev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin MatrixInvertFilev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginControlMatrixInvertFilev1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputMatrixInvertFile()
        xsDataInput.setInputMatrixFile(XSDataFile())
        xsDataInput.setOutputMatrixFile(XSDataFile())
        edPluginExecMatrixInvertFile = self.createPlugin()
        edPluginExecMatrixInvertFile.setDataInput(xsDataInput)
        edPluginExecMatrixInvertFile.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecMatrixInvertFilev1_0 = EDTestCasePluginUnitMatrixInvertFilev1_0("EDTestCasePluginUnitMatrixInvertFilev1_0")
    edTestCasePluginUnitExecMatrixInvertFilev1_0.execute()

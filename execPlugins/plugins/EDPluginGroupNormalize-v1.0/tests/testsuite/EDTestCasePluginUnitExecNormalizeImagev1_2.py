#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble, France

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
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataNormalizeImage import XSDataInputNormalize, XSDataImageExt
from XSDataCommon import XSDataFile, XSDataString

class EDTestCasePluginUnitExecNormalizeImagev1_2(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin NormalizeImagev1_2
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecNormalizeImagev1_2")


    def testCheckParameters(self):
        xsDataInput = XSDataInputNormalize()
        xsDataInput.setData([XSDataImageExt()])
        edPluginExecNormalizeImage = self.createPlugin()
        edPluginExecNormalizeImage.setDataInput(xsDataInput)
        edPluginExecNormalizeImage.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecNormalizeImagev1_2 = EDTestCasePluginUnitExecNormalizeImagev1_2("EDTestCasePluginUnitExecNormalizeImagev1_2")
    edTestCasePluginUnitExecNormalizeImagev1_2.execute()

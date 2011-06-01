#
#    Project: execPlugins / Saxs Group / saxs_mac
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF

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
__copyright__ = "2010 ESRF"

from EDVerbose            import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataSaxsv1_0 import XSDataInputSaxsAddv1_0, XSDataImage, XSDataString

class EDTestCasePluginUnitExecSaxsAddv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin SaxsAddv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsAddv1_0: init")
        EDTestCasePluginUnit.__init__(self, "EDPluginExecSaxsAddv1_0")


    def testCheckParameters(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsAddv1_0: testCheckParameters")
        xsDataInput = XSDataInputSaxsAddv1_0()
        image1 = XSDataImage()
        image2 = XSDataImage()
        image1.setPath(XSDataString("image1"))
        image2.setPath(XSDataString("image2"))
        xsDataInput.setInputImage([image1, image2])
        edPluginExecSaxsAdd = self.createPlugin()
        edPluginExecSaxsAdd.setDataInput(xsDataInput)
        edPluginExecSaxsAdd.checkParameters()



    def process(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsAddv1_0: process")
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecSaxsAddv1_0 = EDTestCasePluginUnitExecSaxsAddv1_0("EDTestCasePluginUnitExecSaxsAddv1_0")
    edTestCasePluginUnitExecSaxsAddv1_0.execute()

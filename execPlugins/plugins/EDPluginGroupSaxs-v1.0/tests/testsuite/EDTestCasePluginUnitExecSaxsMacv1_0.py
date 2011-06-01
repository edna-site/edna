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
from XSDataSaxsv1_0 import XSDataInputSaxsMacv1_0

class EDTestCasePluginUnitExecSaxsMacv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin SaxsMacv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsMacv1_0: init")
        EDTestCasePluginUnit.__init__(self, "EDPluginExecSaxsMacv1_0")


    def testCheckParameters(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsMacv1_0: testCheckParameters")
        xsDataInput = XSDataInputSaxsMacv1_0()
        edPluginExecSaxsMac = self.createPlugin()
        edPluginExecSaxsMac.setDataInput(xsDataInput)
        edPluginExecSaxsMac.checkParameters()



    def process(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsMacv1_0: process")
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecSaxsMacv1_0 = EDTestCasePluginUnitExecSaxsMacv1_0("EDTestCasePluginUnitExecSaxsMacv1_0")
    edTestCasePluginUnitExecSaxsMacv1_0.execute()

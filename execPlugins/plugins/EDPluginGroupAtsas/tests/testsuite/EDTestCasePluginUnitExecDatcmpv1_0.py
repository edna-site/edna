# coding: utf8
#
#    Project: ExecPlugins/GroupAtsas
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataAtsas import XSDataInputDatcmp, XSDataFile

class EDTestCasePluginUnitExecDatcmpv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Datcmpv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecDatcmpv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputDatcmp(inputCurve=[XSDataFile(), XSDataFile()])
        edPluginExecDatcmp = self.createPlugin()
        edPluginExecDatcmp.setDataInput(xsDataInput)
        edPluginExecDatcmp.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecDatcmpv1_0 = EDTestCasePluginUnitExecDatcmpv1_0("EDTestCasePluginUnitExecDatcmpv1_0")
    edTestCasePluginUnitExecDatcmpv1_0.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 - ESRF
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
__copyright__ = "ESRF"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginUnitGroupSaxsv1_0(EDTestSuite):
    """
    This is the test suite Unit for EDNA Group Saxsv1_0 
    It will run subsequently all unit tests .     
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsAddv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsAnglev1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsCurvesv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsMacv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsDelMetadatav1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSaxsAddMetadatav1_0")





if __name__ == '__main__':

    edTestSuitePluginUnitGroupSaxsv1_0 = EDTestSuitePluginUnitGroupSaxsv1_0("EDTestSuitePluginExecSaxsAnglev1_0")
    edTestSuitePluginUnitGroupSaxsv1_0.execute()


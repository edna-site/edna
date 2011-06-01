# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2011 - ESRF
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
__contat__ = "Jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginExecuteGroupSaxsv1_0(EDTestSuite):
    """
    This is the test suite for EDNA plugin SaxsAnglev1_0 
    It will run subsequently all unit tests and execution tests.     
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsAddv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsAnglev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsCurvesv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsCurvesv1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsMacv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsDelMetadatav1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSaxsAddMetadatav1_0")



if __name__ == '__main__':

    edTestSuitePluginExecuteGroupSaxsv1_0 = EDTestSuitePluginExecuteGroupSaxsv1_0("EDTestSuitePluginExecuteGroupSaxsv1_0")
    edTestSuitePluginExecuteGroupSaxsv1_0.execute()


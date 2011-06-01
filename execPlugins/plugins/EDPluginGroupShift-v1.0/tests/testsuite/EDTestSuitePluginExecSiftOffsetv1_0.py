#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
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

__author__="Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginExecSiftOffsetv1_0(EDTestSuite):
    """
    This is the test suite for EDNA plugin SiftOffsetv1_0 
    It will run subsequently all unit tests and execution tests.     
    """        

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitExecSiftOffsetv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSiftOffsetv1_0")
        


if __name__ == '__main__':

    edTestSuitePluginExecSiftOffsetv1_0 = EDTestSuitePluginExecSiftOffsetv1_0("EDTestSuitePluginExecSiftOffsetv1_0")
    edTestSuitePluginExecSiftOffsetv1_0.execute()


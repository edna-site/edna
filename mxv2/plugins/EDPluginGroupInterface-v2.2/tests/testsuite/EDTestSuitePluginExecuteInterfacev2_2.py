#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteInterfacev1_2.py 1554 2010-05-24 15:22:06Z levik $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite                                  import EDTestSuite

class EDTestSuitePluginExecuteInterfacev2_2(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteInterfacev2_2")
        self.addTestCaseFromName("EDTestCasePluginExecuteInterfacev2_2_kappaCELL")
        self.addTestCaseFromName("EDTestCasePluginExecuteInterfacev2_2_kappaCELL_2")
        self.addTestCaseFromName("EDTestCasePluginExecuteInterfacev2_2_charAtNewOrientation")

if __name__ == '__main__':

    edTestSuitePluginExecuteInterfacev2_2 = EDTestSuitePluginExecuteInterfacev2_2("EDTestSuitePluginExecuteInterfacev2_2")
    edTestSuitePluginExecuteInterfacev2_2.execute()


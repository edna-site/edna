#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginUnitControlGridScreeningv1_0(EDTestSuite):
    """
    This is the unit test suite for EDNA plugin GridScreeningv1_0 
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitControlGridScreeningv1_0")



if __name__ == '__main__':

    edTestSuitePluginUnitControlGridScreeningv1_0 = EDTestSuitePluginUnitControlGridScreeningv1_0("EDTestSuitePluginUnitControlGridScreeningv1_0")
    edTestSuitePluginUnitControlGridScreeningv1_0.execute()


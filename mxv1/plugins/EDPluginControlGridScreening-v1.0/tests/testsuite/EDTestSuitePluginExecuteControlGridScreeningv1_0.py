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

class EDTestSuitePluginExecuteControlGridScreeningv1_0(EDTestSuite):
    """
    This is the execute test suite for EDNA plugin GridScreeningv1_0 
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_fewSpots")
        #self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_bestBFactorFailed")
        #self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_iceRings")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_indexingError")
        #self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_integrationError")
        #self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_meshImage")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators")



if __name__ == '__main__':

    edTestSuitePluginExecuteControlGridScreeningv1_0 = EDTestSuitePluginExecuteControlGridScreeningv1_0("EDTestSuitePluginExecuteControlGridScreeningv1_0")
    edTestSuitePluginExecuteControlGridScreeningv1_0.execute()


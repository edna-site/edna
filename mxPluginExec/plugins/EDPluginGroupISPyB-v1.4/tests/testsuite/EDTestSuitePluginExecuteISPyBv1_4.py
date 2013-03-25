#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite                                          import EDTestSuite


class EDTestSuitePluginExecuteISPyBv1_4(EDTestSuite):

    def process(self):
        """
        Adds the plugin execute test cases 
        """
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreAutoProcv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreAutoProcv1_4_failedProcessing")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4_withIntegrationId")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBRetrieveDataCollectionv1_4")
#        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreDataCollectionv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreScreeningv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreScreeningv1_4_withoutDataCollectionId")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBStoreWorkflowv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBUpdateDataCollectionGroupWorkflowIdv1_4")
        self.addTestCaseFromName("EDTestCasePluginExecuteISPyBGroupDataCollectionsv1_4")

##############################################################################
if __name__ == '__main__':
    edTestSuitePluginExecuteISPyBv1_4 = EDTestSuitePluginExecuteISPyBv1_4("EDTestSuitePluginExecuteISPyBv1_4")
    edTestSuitePluginExecuteISPyBv1_4.execute()

##############################################################################

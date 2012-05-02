#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteMXv1(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlIndexingIndicatorsv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlImageQualityIndicatorsv1_1")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlIndexingv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlGeneratePredictionv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlIntegrationv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlStrategyv1_2")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlCharacterisationv1_2")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlGridScreeningv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteReadImageHeaderv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlInterfacev1_2")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteExecEvaluationIndexingv10")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteExecOutputHTMLv1_0")


if __name__ == '__main__':

    edTestSuitePluginExecuteMXv1 = EDTestSuitePluginExecuteMXv1("EDTestSuitePluginExecuteMXv1")
    edTestSuitePluginExecuteMXv1.execute()


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


from EDTestSuite           import EDTestSuite


class EDTestSuitePluginUnitMXv1(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCaseEDHandlerMOSFLMv10")
        self.addTestCaseFromName("EDTestCaseEDHandlerLabelitv10")
        self.addTestCaseFromName("EDTestCaseEDHandlerRaddosev10")
        self.addTestCaseFromName("EDTestCaseEDHandlerBestv1_2")
        self.addTestCaseFromName("EDTestCaseEDHandlerESRFPyarchv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitControlIndexingIndicatorsv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlIndexingv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlIntegrationv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlStrategyv1_2")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlCharacterisationv1_3")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlGridScreeningv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginUnitReadImageHeaderv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlInterfaceToMXCuBEv1_3")
        self.addTestSuiteFromName("EDTestSuitePluginUnitExecEvaluationIndexingv10")


if __name__ == '__main__':

    edTestSuitePluginUnitMXv1 = EDTestSuitePluginUnitMXv1("EDTestSuitePluginUnitMXv1")
    edTestSuitePluginUnitMXv1.execute()


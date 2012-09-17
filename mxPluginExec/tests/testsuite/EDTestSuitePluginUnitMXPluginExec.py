#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDTestSuite           import EDTestSuite


class EDTestSuitePluginUnitMXPluginExec(EDTestSuite):


    def process(self):
        self.addTestSuiteFromName("EDTestSuitePluginUnitBestv1_2")
        self.addTestSuiteFromName("EDTestSuitePluginUnitISPyBv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitISPyBv1_1")
        self.addTestSuiteFromName("EDTestSuitePluginUnitISPyBv1_2")
        self.addTestSuiteFromName("EDTestSuitePluginUnitLabelitv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitMOSFLMv10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitRaddosev10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitSTACv2_0")
        self.addTestSuiteFromName("EDTestSuitePluginUnitXDSv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginUnitXDSv1_1")



if __name__ == '__main__':

    edTestSuitePluginUnitMXPluginExec = EDTestSuitePluginUnitMXPluginExec("EDTestSuitePluginUnitMXPluginExec")
    edTestSuitePluginUnitMXPluginExec.execute()


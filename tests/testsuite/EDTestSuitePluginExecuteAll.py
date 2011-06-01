#
#    Project: EDNA
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuiteMXv1PluginExecute.py 698 2009-05-11 10:43:08Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
#                            Jerome Kieffer (jerome.kieffer@esrf.fr)
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


from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteAll(EDTestSuite):


    def process(self):
        self.addTestSuiteFromName("EDTestSuiteKernelExecute")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteMXAll")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteExecPlugins")
        self.addTestSuiteFromName("EDTestSuiteExecuteBioSaxsv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginsExecuteMatrix")


if __name__ == '__main__':

    edTestSuitePluginExecuteAll = EDTestSuitePluginExecuteAll("EDTestSuitePluginExecuteAll")
    edTestSuitePluginExecuteAll.execute()


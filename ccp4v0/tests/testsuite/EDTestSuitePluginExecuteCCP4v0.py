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
#                            Jerome Kieffer (kieffer@esrf.fr)
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


from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteCCP4v0(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecPDBSETUnitCellv10")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCopyUnitCellMTZtoPDBv10")



if __name__ == '__main__':

    edTestSuitePluginExecute = EDTestSuitePluginExecuteCCP4v0("EDTestSuitePluginExecuteCCP4v0")
    edTestSuitePluginExecute.execute()


#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteControlCharacterisationv2_0.py 1920 2010-08-18 15:13:00Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

from EDTestSuite                                         import EDTestSuite


class EDTestSuitePluginExecuteControlCharForReorientationv2_0(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCharForReorientationv2_0_noKAPPA_")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Anomalous")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Anomalous_singleXML")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlCharForReorientationv2_0_workflow")
        


if __name__ == '__main__':

    edTestSuitePluginExecuteControlCharForReorientationv2_0= EDTestSuitePluginExecuteControlCharForReorientationv2_0("EDTestSuitePluginExecuteControlCharForReorientationv2_0")
    edTestSuitePluginExecuteControlCharForReorientationv2_0.execute()


#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteMXv1.py 1938 2010-08-23 09:45:08Z svensson $"
#
#    Copyright (C) 2010 Diamond Light Source, CCP4
#
#    Principal authors: Graeme Winter (graeme.winter@diamond.ac.uk)
#                       Ronan Keegan (ronan.keegan@stfc.ac.uk)
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


__authors__ = ['Graeme Winter', 'Ronan Keegan']
__contact__ = "graeme.winter@diamond.ac.uk"
__license__ = "LGPL+"
__copyright__ = "Diamond Light Source and CCP4"

from EDTestSuite import EDTestSuite

class EDTestSuitePluginExecuteDimplev0(EDTestSuite):
    def process(self):
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLECopySpaceGroupPDBtoMTZv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLECopyUnitCellMTZtoPDBv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLEDIMPLESv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLEPipelineCalcDiffMapv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLEPrepareMTZFileForRefinementv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginControlDIMPLERefmacRigidBodyPhaserv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLECADv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLECheckValidHKLv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLECheckValidXYZv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEFREERFLAGv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEMTZDUMPv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEPDBDUMPv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEPDBListv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEPDBSETv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEPHASERv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLERefmacMonomerCheckv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEREFMACRestrainedRefinementv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEREFMACRigidBodyv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEREINDEXv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLETRUNCATEv10")
        self.addTestSuiteFromName(
            "EDTestSuitePluginExecDIMPLEUNIQUEv10")

if __name__ == '__main__':

    edTestSuitePluginExecuteDimplev0 = EDTestSuitePluginExecuteDimplev0(
        "EDTestSuitePluginExecuteDimplev0")
    edTestSuitePluginExecuteDimplev0.execute()


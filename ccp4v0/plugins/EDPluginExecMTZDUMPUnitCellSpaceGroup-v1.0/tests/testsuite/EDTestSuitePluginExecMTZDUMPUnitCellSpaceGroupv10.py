#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4/ESRF
#
#    Principal author:       Mark
#                        Jerome Kieffer (kieffer@esrf.fr)
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

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginExecMTZDUMPUnitCellSpaceGroupv10(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecMTZDUMPUnitCellSpaceGroupv10")


if __name__ == '__main__':

    edTestSuitePluginExecMTZDUMPUnitCellSpaceGroupv10 = EDTestSuitePluginExecMTZDUMPUnitCellSpaceGroupv10("EDTestSuitePluginExecMTZDUMPUnitCellSpaceGroupv10")
    edTestSuitePluginExecMTZDUMPUnitCellSpaceGroupv10.execute()


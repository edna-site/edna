#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4/ESRF
#
#    Principal author:      Jerome Kieffer (kieffer@esrf.fr)
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

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute




class EDTestCasePluginExecuteExecMTZDUMPUnitCellSpaceGroupv10(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecMTZDUMPUnitCellSpaceGroupv10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputMTZDUMPUnitCellSpaceGroup_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultMTZDUMPUnitCellSpaceGroup_reference.xml"))





if __name__ == '__main__':

    testMTZDUMPUnitCellSpaceGroupv10instance = EDTestCasePluginExecuteExecMTZDUMPUnitCellSpaceGroupv10("EDTestCasePluginExecuteExecMTZDUMPUnitCellSpaceGroupv10")
    testMTZDUMPUnitCellSpaceGroupv10instance.execute()

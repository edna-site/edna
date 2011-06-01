#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4
#
#    Principal author:       Mark
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

from EDImportLib                         import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataCCP4v0                        import XSDataResultPDBSETUnitCell


class EDTestCasePluginExecuteExecPDBSETUnitCellv10(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecPDBSETUnitCellv10")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputPDBSETUnitCell_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultPDBSETUnitCell_reference.xml"))


if __name__ == '__main__':

    testPDBSETUnitCellv10instance = EDTestCasePluginExecuteControlPDBSETUnitCellv10("EDTestCasePluginExecuteControlPDBSETUnitCellv10")
    testPDBSETUnitCellv10instance.execute()

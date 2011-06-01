#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4 2010 / ESRF
#
#    Principal author:       Mark Basham
#                            Jerome Kieffer (kieffer@esrf.fr)
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
from XSDataCCP4v0                        import XSDataResultCopyUnitCellMTZtoPDB

class EDTestCasePluginExecuteControlCopyUnitCellMTZtoPDBv10(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlCopyUnitCellMTZtoPDBv10")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCopyUnitCellMTZtoPDB_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultCopyUnitCellMTZtoPDB_reference.xml"))




if __name__ == '__main__':

    edTestCasePluginExecuteControlUnitCellMTZtoPDB = EDTestCasePluginExecuteControlCopyUnitCellMTZtoPDBv10("EDTestCasePluginExecuteControlCopyUnitCellMTZtoPDBv10")
    edTestCasePluginExecuteControlUnitCellMTZtoPDB.execute()

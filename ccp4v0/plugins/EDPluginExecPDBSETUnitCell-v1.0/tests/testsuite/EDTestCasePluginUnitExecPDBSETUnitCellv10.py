#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4/ESRF

#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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

from EDVerbose import EDVerbose
from EDUtilsTest import EDUtilsTest
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataCCP4v0 import XSDataInputPDBSETUnitCell


class EDTestCasePluginUnitExecPDBSETUnitCellv10(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecPDBSETUnitCellv10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputPDBSETUnitCell_reference.xml")


    def testCheckParameters(self):
        pyStrXMLInput = EDUtilsTest.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecPDBSETUnitCell = self.createPlugin()
        edPluginExecPDBSETUnitCell.setDataInput(pyStrXMLInput)
        edPluginExecPDBSETUnitCell.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecPDBSETUnitCellv10 = EDTestCasePluginUnitExecPDBSETUnitCellv10("EDTestCasePluginUnitExecPDBSETUnitCellv10")
    edTestCasePluginUnitExecPDBSETUnitCellv10.execute()

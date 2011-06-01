#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4/ESRF
#
#    Principal author:  Mark
#                       Jerome Kieffer (kieffer@esrf.fr) 
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
from EDUtilsFile import EDUtilsFile
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataCCP4v0 import XSDataInputMTZDUMPUnitCellSpaceGroup

class EDTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10(EDTestCasePluginUnit):

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecMTZDUMPUnitCellSpaceGroupv10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputMTZDUMPUnitCellSpaceGroup_reference.xml")


    def testCheckParameters(self):
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecMTZDUMPUnitCellSpaceGroup = self.createPlugin()
        edPluginExecMTZDUMPUnitCellSpaceGroup.setDataInput(pyStrXMLInput)
        edPluginExecMTZDUMPUnitCellSpaceGroup.checkParameters()


    def testGenerateMTZDUMPCommands(self):
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecMTZDUMPUnitCellSpaceGroup = self.createPlugin()
        edPluginExecMTZDUMPUnitCellSpaceGroup.setDataInput(pyStrXMLInput)
        edPluginExecMTZDUMPUnitCellSpaceGroup.generateMTZDUMPCommands()


    def testParseMTZDUMPLog(self):
        pyStrLogFilePath = os.path.join(self.getPluginTestsDataHome(), "mtzdump.log")
        pyStrLog = EDUtilsFile.readFile(pyStrLogFilePath)
        edPluginExecMTZDUMPUnitCellSpaceGroup = self.createPlugin()
        xsDataResult = edPluginExecMTZDUMPUnitCellSpaceGroup.parseMTZDUMPLog(pyStrLog)

    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testGenerateMTZDUMPCommands)
        self.addTestMethod(self.testParseMTZDUMPLog)



if __name__ == '__main__':

    edTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10 = EDTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10("EDTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10")
    edTestCasePluginUnitExecMTZDUMPUnitCellSpaceGroupv10.execute()

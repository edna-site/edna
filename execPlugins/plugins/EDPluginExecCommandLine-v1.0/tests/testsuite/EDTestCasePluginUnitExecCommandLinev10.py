#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France

#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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

__author__ = "Jerome Kieffer (Jerome.Kieffer@ESRF.eu)"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataExecCommandLine  import XSDataInputExecCommandLine

class EDTestCasePluginUnitExecCommandLinev10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin CommandLinev10
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecCommandLinev10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputCommandLine_fireAndForget_reference.xml")

    def testCheckParameters(self):
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecCommandLine = self.createPlugin()
        edPluginExecCommandLine.setDataInput(pyStrXMLInput)
        edPluginExecCommandLine.checkParameters()




    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitExecCommandLinev10 = EDTestCasePluginUnitExecCommandLinev10("EDTestCasePluginUnitExecCommandLinev10")
    edTestCasePluginUnitExecCommandLinev10.execute()

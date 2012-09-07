#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:       irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute

from XSDataCommon                    import XSDataString


class EDTestCasePluginExecuteExecDamstartv0_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Damstartv0_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDamstartv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Damstart.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDamstart_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDamstart_reference.xml"))


    def testExecute(self):
        """
        """
        inputPdbPath = XSDataString()

        # Add path to the input data file
        inputPdbName = self.getPlugin().getDataInput().getInputPdbFile().getPath().getValue()
        inputPdbPath.setValue(os.path.join(self.getPluginTestsDataHome(), inputPdbName))
        self.getPlugin().getDataInput().getInputPdbFile().setPath(inputPdbPath)

        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testDamstartv0_1instance = EDTestCasePluginExecuteExecDamstartv0_1("EDTestCasePluginExecuteExecDamstartv0_1")
    testDamstartv0_1instance.execute()

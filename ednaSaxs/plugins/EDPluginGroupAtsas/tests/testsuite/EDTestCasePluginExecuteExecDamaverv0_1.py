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

from XSDataCommon import XSDataString

class EDTestCasePluginExecuteExecDamaverv0_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Damaverv0_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDamaverv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Damaver.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDamaver_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDamaver_reference.xml"))


    def testExecute(self):
        """
        """
        # Add path to the input data file
        for pdbInputFile in self.getPlugin().getDataInput().getPdbInputFiles():
            dataInputName = pdbInputFile.getPath().getValue()
            pdbInputFile.setPath(XSDataString(os.path.join(self.getPluginTestsDataHome(), dataInputName)))

        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testDamaverv0_1instance = EDTestCasePluginExecuteExecDamaverv0_1("EDTestCasePluginExecuteExecDamaverv0_1")
    testDamaverv0_1instance.execute()

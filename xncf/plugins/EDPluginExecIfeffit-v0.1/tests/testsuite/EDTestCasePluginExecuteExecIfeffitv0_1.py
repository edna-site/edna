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

from XSDataIfeffit                    import XSDataString


class EDTestCasePluginExecuteExecIfeffitv0_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Ifeffitv0_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecIfeffitv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Ifeffit.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputIfeffit_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultIfeffit_reference.xml"))


    def testExecute(self):
        """
        """
        scriptPath = XSDataString()

        # Add path to the input data file
        scriptName = self.getPlugin().getDataInput().getScriptFile().getPath().getValue()
        scriptPath.setValue(os.path.join(self.getPluginTestsDataHome(), scriptName))
        self.getPlugin().getDataInput().getScriptFile().setPath(scriptPath)

        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testIfeffitv0_1instance = EDTestCasePluginExecuteExecIfeffitv0_1("EDTestCasePluginExecuteExecIfeffitv0_1")
    testIfeffitv0_1instance.execute()

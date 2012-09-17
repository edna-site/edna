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


class EDTestCasePluginExecuteExecSupcombv0_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Supcombv0_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSupcombv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Supcomb.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSupcomb_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSupcomb_reference.xml"))


    def testExecute(self):
        """
        """
        templateInputPath = XSDataString()
        supimposeInputPath = XSDataString()

        # Add path to the input data file
        templateInputName = self.getPlugin().getDataInput().getTemplateFile().getPath().getValue()
        templateInputPath.setValue(os.path.join(self.getPluginTestsDataHome(), templateInputName))
        self.getPlugin().getDataInput().getTemplateFile().setPath(templateInputPath)

        supimposeInputName = self.getPlugin().getDataInput().getSuperimposeFile().getPath().getValue()
        supimposeInputPath.setValue(os.path.join(self.getPluginTestsDataHome(), supimposeInputName))
        self.getPlugin().getDataInput().getSuperimposeFile().setPath(supimposeInputPath)

        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testSupcombv0_1instance = EDTestCasePluginExecuteExecSupcombv0_1("EDTestCasePluginExecuteExecSupcombv0_1")
    testSupcombv0_1instance.execute()

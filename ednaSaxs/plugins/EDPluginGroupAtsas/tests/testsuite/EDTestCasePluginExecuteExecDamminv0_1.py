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


class EDTestCasePluginExecuteExecDamminv0_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Damminv0_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDamminv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Dammin.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDammin_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDammin_reference.xml"))


    def testExecute(self):
        """
        """

        # Add path to the input data file
        #dataGnomInputName = self.getPlugin().getDataInput().getGnomOutputFile().getPath().getValue()
        #dataGnomInputPath.setValue(os.path.join(self.getPluginTestsDataHome(), dataGnomInputName))
        #self.getPlugin().getDataInput().getGnomOutputFile().setPath(dataGnomInputPath)
        #self.getPlugin().getDataInput().getPdbInputFile().setPath(dataInputPath)
        self.writeFullPath(self.getPlugin().getDataInput().getGnomOutputFile())
        self.writeFullPath(self.getPlugin().getDataInput().getPdbInputFile())
        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

    def writeFullPath(self, xsDataFile):
        """
        Add path to the data file directory 
        """
        dataInputPath = XSDataString()
        dataInputName = xsDataFile.getPath().getValue()
        dataInputPath.setValue(os.path.join(self.getPluginTestsDataHome(), dataInputName))
        xsDataFile.setPath(dataInputPath)



if __name__ == '__main__':

    testDamminv0_1instance = EDTestCasePluginExecuteExecDamminv0_1("EDTestCasePluginExecuteExecDamminv0_1")
    testDamminv0_1instance.execute()

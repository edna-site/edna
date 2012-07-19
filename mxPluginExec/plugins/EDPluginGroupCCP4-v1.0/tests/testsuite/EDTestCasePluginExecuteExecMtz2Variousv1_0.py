# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecMtz2Variousv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Mtz2Variousv1_0
    """
    
    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecMtz2Variousv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Mtz2Variousv1_0.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMtz2Various_reference.xml"))
#        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
#                                                     "XSDataResultMtz2Variousv1_0_reference.xml"))
                 
                 
    def preProcess(self, _edObject = None):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["process_1_1.mtz"])
        
    def testExecute(self):
        self.run()
        

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        

if __name__ == '__main__':

    testMtz2Variousv1_0instance = EDTestCasePluginExecuteControlMtz2Variousv1_0("EDTestCasePluginExecuteExecMtz2Variousv1_0")
    testMtz2Variousv1_0instance.execute()

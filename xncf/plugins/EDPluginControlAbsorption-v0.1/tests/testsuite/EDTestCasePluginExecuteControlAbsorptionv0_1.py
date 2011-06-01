#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source
#
#    Principal author:       Irakli Sikharulidze
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

__author__="Irakli Sikharulidze"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteControlAbsorptionv0_1(EDTestCasePluginExecute):
    

    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlAbsorptionv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Absorption.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputAbsorption_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultAbsorption_reference.xml"))
                 
        
    def testExecute(self):
        """
        """ 
        self.run()
        


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        
        

if __name__ == '__main__':

    edTestCasePluginExecuteControlAbsorptionv0_1 = EDTestCasePluginExecuteControlAbsorptionv0_1("EDTestCasePluginExecuteControlAbsorptionv0_1")
    edTestCasePluginExecuteControlAbsorptionv0_1.execute()

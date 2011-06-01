#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source

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

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataAbsCalc import XSDataInputAbsCalc

class EDTestCasePluginUnitExecAbsCalcv0_1(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin AbsCalcv0_1
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecAbsCalcv0_1")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputAbsCalc()
        edPluginExecAbsCalc = self.createPlugin()
        edPluginExecAbsCalc.setDataInput(xsDataInput)
        edPluginExecAbsCalc.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecAbsCalcv0_1 = EDTestCasePluginUnitExecAbsCalcv0_1("EDTestCasePluginUnitExecAbsCalcv0_1")
    edTestCasePluginUnitExecAbsCalcv0_1.execute()

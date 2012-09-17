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


from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCCP4v1_0 import XSDataInputMtz2Various

class EDTestCasePluginUnitExecMtz2Variousv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Mtz2Variousv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecMtz2Variousv1_0")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputMtz2Various()
        edPluginExecMtz2Variousv1_0 = self.createPlugin()
        edPluginExecMtz2Variousv1_0.setDataInput(xsDataInput)
        edPluginExecMtz2Variousv1_0.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecMtz2Variousv1_0 = EDTestCasePluginUnitExecMtz2Variousv1_0("EDTestCasePluginUnitExecMtz2Variousv1_0")
    edTestCasePluginUnitExecMtz2Variousv1_0.execute()

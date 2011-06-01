#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source
#
#    Principal author:        Irakli Sikharulidze
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

from XSDataAbsCalc import XSDataInputAbsorption

class EDTestCasePluginUnitControlAbsorptionv0_1(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlAbsorptionv0_1")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputAbsorption()
        edPluginExecAbsorption = self.createPlugin()
        edPluginExecAbsorption.setDataInput(xsDataInput)
        edPluginExecAbsorption.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    


if __name__ == '__main__':

    EDTestCasePluginUnitControlAbsorptionv0_1 = EDTestCasePluginUnitControlAbsorptionv0_1("EDTestCasePluginUnitControlAbsorptionv0_1")
    EDTestCasePluginUnitControlAbsorptionv0_1.execute()

#
#    Project: DIMPLE
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source and CCP4
#
#    Principal authors: Graeme Winter (graeme.winter@diamond.ac.uk)
#                       Ronan Keegan (ronan.keegan@stfc.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the Lesser GNU General Public License as published by
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

__author__= ['Graeme Winter', 'Ronan Keegan']
__license__ = 'LGPLv3+'
__copyright__ = '2010 Diamond Light Source, CCP4'

from EDImportLib import EDVerbose

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCCP4DIMPLE import CCP4DataInputCAD

class EDTestCasePluginUnitExecDIMPLECADv10(EDTestCasePluginUnit):
    '''Currently no unit tests for this plugin.'''

    def __init__(self, _edStringTestName = None):
        EDTestCasePluginUnit.__init__(self, 'EDPluginExecDIMPLECADv10')
              
    def testCheckParameters(self):
        xsDataInput = CCP4DataInputCAD()
        edPluginExecDIMPLECAD = self.createPlugin()
        edPluginExecDIMPLECAD.setDataInput(xsDataInput)
        edPluginExecDIMPLECAD.checkParameters()
        
        return
    
    def process(self):
        pass

if __name__ == '__main__':
    
    test_inhstance = EDTestCasePluginUnitExecDIMPLECADv10(
        'EDTestCasePluginUnitExecDIMPLECADv10')
    test_instance.execute()

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

import os

from EDImportLib import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataCCP4DIMPLE import CCP4DataInputPDBDUMP

class EDTestCasePluginUnitExecDIMPLEPDBDUMPv10( EDTestCasePluginUnit ):
    """Those are all units tests for the EDNA Exec plugin
    DIMPLEPDBDUMPv10."""

    def __init__( self, _edStringTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecDIMPLEPDBDUMPv10")
              
    def testReadUnitCell(self):
        '''Test reading of the unit cell.'''
        xyzin = os.path.join(self.getPluginTestsDataHome(),
                             'insulin.pdb')
        
        edPluginExecDIMPLEPDBDUMP = self.createPlugin()
        edPluginExecDIMPLEPDBDUMP.set_xyzin(xyzin)
        edPluginExecDIMPLEPDBDUMP.parse_pdb_get_unit_cell_symmetry()
        unit_cell = edPluginExecDIMPLEPDBDUMP.get_unit_cell_constants()

        assert(int(round(unit_cell[0])) == 78)
        assert(int(round(unit_cell[1])) == 78)
        assert(int(round(unit_cell[2])) == 78)
        assert(int(round(unit_cell[3])) == 90)
        assert(int(round(unit_cell[4])) == 90)
        assert(int(round(unit_cell[5])) == 90)
        
        return

    def testReadSpaceGroup(self):
        '''Test reading of the space group.'''
        xyzin = os.path.join(self.getPluginTestsDataHome(),
                             'insulin.pdb')
        
        edPluginExecDIMPLEPDBDUMP = self.createPlugin()
        edPluginExecDIMPLEPDBDUMP.set_xyzin(xyzin)
        edPluginExecDIMPLEPDBDUMP.parse_pdb_get_unit_cell_symmetry()
        space_group_name = edPluginExecDIMPLEPDBDUMP.get_space_group_name()

        assert(space_group_name == 'I 21 3')

        return

    def testReadSequence(self):
        '''Test reading of the amino acid sequence from SEQRES records.'''
        xyzin = os.path.join(self.getPluginTestsDataHome(),
                                      'insulin.pdb')
        
        edPluginExecDIMPLEPDBDUMP = self.createPlugin()
        edPluginExecDIMPLEPDBDUMP.set_xyzin(xyzin)
        edPluginExecDIMPLEPDBDUMP.parse_pdb_get_sequence()
        sequence = edPluginExecDIMPLEPDBDUMP.get_amino_acid_sequence()

        assert(len(sequence) > 10 and len(sequence) < 100)
        
        return
    
    def process(self):
        self.addTestMethod(self.testReadUnitCell)
        self.addTestMethod(self.testReadSpaceGroup)
        self.addTestMethod(self.testReadSequence)
        return
    
if __name__ == '__main__':

    test_plugin = EDTestCasePluginUnitExecDIMPLEPDBDUMPv10(
        "EDTestCasePluginUnitExecDIMPLEPDBDUMPv10")
    test_plugin.execute()

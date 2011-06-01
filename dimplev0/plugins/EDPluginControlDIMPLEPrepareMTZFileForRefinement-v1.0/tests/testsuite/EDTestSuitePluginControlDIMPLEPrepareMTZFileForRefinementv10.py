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

from EDImportLib  import EDCompiler
from EDTestSuite  import EDTestSuite

class EDTestSuitePluginControlDIMPLEPrepareMTZFileForRefinementv10(
    EDTestSuite):

    def process(self):
        self.addTestCaseFromName('EDTestCasePluginUnitControlDIMPLEPrepareMTZFileForRefinementv10')
        self.addTestCaseFromName('EDTestCasePluginExecuteControlDIMPLEPrepareMTZFileForRefinementv10')
        
if __name__ == '__main__':

    EDCompiler.accelerator()

    test_instance = EDTestSuitePluginControlDIMPLEPrepareMTZFileForRefinementv10(
        'EDTestSuitePluginControlDIMPLEPrepareMTZFileForRefinementv10')
    test_instance.execute()


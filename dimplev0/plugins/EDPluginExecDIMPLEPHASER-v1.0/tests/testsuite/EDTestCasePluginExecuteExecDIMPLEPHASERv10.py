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

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecDIMPLEPHASERv10(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin DIMPLEPHASERv10
    """
    
    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDIMPLEPHASERv10")

        self.setConfigurationFile( self.getRefConfigFile() )
        
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDIMPLEPHASER_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDIMPLEPHASER_reference.xml"))
                 
        
    def testExecute(self):
        """
        """ 
        self.run()
        

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        

if __name__ == '__main__':

    testDIMPLEPHASERv10instance = EDTestCasePluginExecuteControlDIMPLEPHASERv10("EDTestCasePluginExecuteExecDIMPLEPHASERv10")
    testDIMPLEPHASERv10instance.execute()

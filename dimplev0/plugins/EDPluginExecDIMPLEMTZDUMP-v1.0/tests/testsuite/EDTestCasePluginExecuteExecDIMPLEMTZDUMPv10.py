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

from EDImportLib                         import EDVerbose

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsPath                         import EDUtilsPath

from XSDataCCP4DIMPLE import CCP4DataResultMTZDUMP
from XSDataCCP4DIMPLE import CCP4UnitCell


class EDTestCasePluginExecuteExecDIMPLEMTZDUMPv10( EDTestCasePluginExecute ):
    """
    Those are all execution tests for the EDNA Exec plugin DIMPLEMTZDUMPv10
    """
    
    def __init__( self, _edStringTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__( self, "EDPluginExecDIMPLEMTZDUMPv10" )

        self.setConfigurationFile( self.getRefConfigFile() )
        
        self.setDataInputFile( EDUtilsPath.mergePath( self.getPluginTestsDataHome(), \
                                                      "XSDataInputDIMPLEMTZDUMP_reference.xml" ) )
        
        self.setReferenceDataOutputFile( EDUtilsPath.mergePath( self.getPluginTestsDataHome(), \
                                                                "XSDataResultDIMPLEMTZDUMP_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"
        
        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0        
                 
        
    def testExecute( self ):
        """
        """ 
        self.run()
        
        # Checks that there are no error messages
        
        plugin = self.getPlugin()

        EDVerbose.DEBUG("Checking error messages...")
        EDAssert.equal( self.m_iNoErrorMessages, self.getErrorMessages().getNumberObjects() )
            
        EDVerbose.DEBUG("Checking warning messages...")
        EDAssert.equal( self.m_iNoWarningMessages, self.getWarningMessages().getNumberObjects() )

        # Define a test which will test the XML reference output file (which you got when you run the plugin last time) with the data output file, which you will get when you
        # the plugin again, to see if you get the same result. If so, this will mean that the plugin works fine and gives you the correct result. You can customise the test so
        # that you test specific values, as in the code listed below where the value A of the unit cell is checked.
        
        #ccp4DataResultMTZDUMP = CCP4DataResultMTZDUMP(self.getReferenceDataOutputFile())
        #dataOutput = plugin.getDataOutput()
        #EDAssert.equal(ccp4DataResultMTZDUMP.getUnitCell().getA(),dataOutput.getUnitCell().getA())
        


##############################################################################

    def process( self ):
        """
        """
        self.addTestMethod( self.testExecute )

        
        
##############################################################################


if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()
    
    testDIMPLEMTZDUMPv10instance = EDTestCasePluginExecuteControlDIMPLEMTZDUMPv10( "EDTestCasePluginExecuteExecDIMPLEMTZDUMPv10" )
    testDIMPLEMTZDUMPv10instance.execute()

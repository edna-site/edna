#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS 2010
#
#    Principal author:       Mark Basham
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
__author__="Mark Basham"
__license__ = "GPLv3+"
__copyright__ = "DLS 2010"

from EDImportLib                         import EDVerbose

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsPath                         import EDUtilsPath




class EDTestCasePluginExecuteExecTomographyv10( EDTestCasePluginExecute ):
    """
    Those are all execution tests for the EDNA Exec plugin Tomographyv10
    """
    
    def __init__( self, _edStringTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__( self, "EDPluginExecTomographyv10" )

        self.setConfigurationFile( EDUtilsPath.mergePath( self.getPluginTestsDataHome(),
                                                          "XSConfiguration_Tomography.xml" ) )
        
        self.setDataInputFile( EDUtilsPath.mergePath( self.getPluginTestsDataHome(), \
                                                      "XSDataInputTomography_reference.xml" ) )
        
        self.setReferenceDataOutputFile( EDUtilsPath.mergePath( self.getPluginTestsDataHome(), \
                                                                "XSDataResultTomography_reference.xml"))

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



##############################################################################

    def process( self ):
        """
        """
        self.addTestMethod( self.testExecute )

        
        
##############################################################################


if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()
    
    testTomographyv10instance = EDTestCasePluginExecuteControlTomographyv10( "EDTestCasePluginExecuteExecTomographyv10" )
    testTomographyv10instance.execute()

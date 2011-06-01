#
#    Project: The EDNA Archive Project
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 Diamond Light Source
#                            Chilton, Didcot, UK
#
#    Principal author:       Mark Basham (mark.basham@diamond.ac.uk)
#
#    Contributing authors:   Olof Svensson (svensson@esrf.fr) 
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


from EDImportLib                         import EDCompiler
from EDImportLib                         import EDVerbose
from EDImportLib                         import EDString
from EDImportLib                         import EDDiskExplorer
from EDImportLib                         import EDDict
from EDImportLib                         import EDDictionary
from EDImportLib                         import EDList

from EDUtilsFile                         import EDUtilsFile
from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest

#from EDPluginDLSArchiverv01 import EDPluginDLSArchiver

class EDTestCasePluginExecUnitICATIngesterv10( EDTestCasePluginUnit ):
    """
    """
    
    def __init__( self, _oalStringTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__( self, "EDPluginExecICATIngesterv10", "EDPluginExecICATIngester-v1.0", _oalStringTestName )
        self.m_edStringReferenceDataInputFile  = EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginExecICATIngester_reference.xml")
                    
            
    def testSetDataInput( self ):
        """
        This method test the setDataInput method of the Labelit plugin by providing an XML string
        and then retriving an XSDataInputLabelit object.
        """
        #Create the plugin instance
        edPluginExecICATIngester = self.createPlugin()
        # create an object which contains the test information
        edStringInputExecICATIngesterv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile )
        # gives the data to the plugin
        edPluginExecICATIngester.setDataInput( edStringInputExecICATIngesterv10XML )
        # get the data from the plugin
        xsDataInputPluginExecICATIngester = edPluginExecICATIngester.getDataInput()
        # get the string of the path
        edStringPath = EDString( xsDataInputPluginExecICATIngester.getXmlIngestFileName().getPath().getValue() )
        # create the test path 
        edStringPathReference = EDString( "/tmp/xmlingest/" )
        # Actualy test the data.
        EDAssert.equal( edStringPathReference, edStringPath )

        
    def testGenerateExecutiveSummary( self ):
        """
        This method tests the generateExecutiveSummary of the Labelit plugin.
        It contains no assert call so the contents of the executive summary is not tested.
        """
        edPluginExecICATIngester = self.createPlugin()
        
    def testMakeExernalCall(self):
        """
        This method should test that an external call has sucsesfully been made
        """
        
        
        
    
 

##############################################################################
 
    def process( self ):
        """
        """
        self.addTestMethod( self.testSetDataInput )
        self.addTestMethod( self.testGenerateExecutiveSummary )
        
        
##############################################################################


if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()
    
    edTestCasePluginExecUnitICATIngesterv10 = EDTestCasePluginExecUnitICATIngesterv10( "EDTestCasePluginExecUnitICATIngesterv10" )
    edTestCasePluginExecUnitICATIngesterv10.execute()


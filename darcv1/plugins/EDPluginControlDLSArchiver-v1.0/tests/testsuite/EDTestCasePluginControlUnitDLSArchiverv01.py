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

class EDTestCasePluginControlUnitDLSArchiverv01( EDTestCasePluginUnit ):
    """
    """
    
    def __init__( self, _oalStringTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__( self, "EDPluginControlDLSArchiverv10", "EDPluginControlDLSArchiver-v1.0", _oalStringTestName )
        self.m_edStringReferenceDataInputFile  = EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginControlDLSArchiverv10_reference.xml")
                    
            
    def testSetDataInput( self ):
        """
        This method test the setDataInput method of the Labelit plugin by providing an XML string
        and then retriving an XSDataInputLabelit object.
        """
        #Create the plugin instance
        edPluginControlDLSArchiver = self.createPlugin()
        # create an object which contains the test information
        edStringInputPluginControlDLSArchiverv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile )
        # gives the data to the plugin
        edPluginControlDLSArchiver.setDataInput( edStringInputPluginControlDLSArchiverv10XML )
        # get the data from the plugin
        xsDataInputPluginControlDLSArchiver = edPluginControlDLSArchiver.getDataInput()
        # get the string of the path
        edStringPath = EDString( xsDataInputPluginControlDLSArchiver.getDropZonePath().getPath().getValue() )
        # create the test path 
        edStringPathReference = EDString( "../data/test/ingest/" )
        # Actually test the data.
        EDAssert.equal( edStringPath, edStringPathReference)
        
        #check out that the list is getting read in properly
        #FIXME, add in some proper test code here
        print xsDataInputPluginControlDLSArchiver.getDropZonePath().getPath().getValue()
        print xsDataInputPluginControlDLSArchiver.getIgnoreList()[1].getValue()
        

    def testGenerateExecutiveSummary( self ):
        """
        This method tests the generateExecutiveSummary of the Labelit plugin.
        It contains no assert call so the contents of the executive summary is not tested.
        """
        edPluginControlDLSArchiver = self.createPlugin()
    
 

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
    
    edTestCasePluginControlUnitDLSArchiverv01 = EDTestCasePluginControlUnitDLSArchiverv01( "EDTestCasePluginControlUnitDLSArchiverv01" )
    edTestCasePluginControlUnitDLSArchiverv01.execute()


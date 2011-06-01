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

import os.path

class EDTestCasePluginExecUnitSRBRegisterv10( EDTestCasePluginUnit ):
    """
    """
    
    def __init__( self, _oalStringTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__( self, "EDPluginExecSRBRegisterv10", "EDPluginExecSRBRegister-v1.0", _oalStringTestName )
        self.m_edStringReferenceDataInputFile  = EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginExecSRBRegister_reference.xml")
        self.m_edStringReferenceDataInputFile2  = EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginExecSRBRegister_reference2.xml")
        self.m_edStringReferenceDataInputFile3  = EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginExecSRBRegister_reference3.xml")
            
    def testSetDataInput( self ):
        """
        This method test the setDataInput method of the SRBRegister plugin by providing an XML string
        and then retriving an XSDataInputLabelit object.  It checks both inputs
        """
        #Create the plugin instance
        edPluginExecSRBRegister = self.createPlugin()
        # create an object which contains the test information
        edStringInputExecSRBRegisterv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile )
        # gives the data to the plugin
        edPluginExecSRBRegister.setDataInput( edStringInputExecSRBRegisterv10XML )
        # get the data from the plugin
        xsDataInputPluginExecSRBRegister = edPluginExecSRBRegister.getDataInput()
        # get the string of the path
        edStringPath = EDString( xsDataInputPluginExecSRBRegister.getSrbDropFileName().getPath().getValue() )
        # create the test path 
        edStringPathReference = EDString( "../data/out/test2.drop" )
        # Actually test the data.
        EDAssert.equal( edStringPathReference, edStringPath )
        
        # test the reading of the other data
        edStringPath = EDString( xsDataInputPluginExecSRBRegister.getXmlIngestFileName().getPath().getValue() )
        # create the test path 
        edStringPathReference = EDString( "../data/create-ds.xml" )
        # Actually test the data.
        EDAssert.equal( edStringPathReference, edStringPath )

        
    def testGenerateExecutiveSummary( self ):
        """
        This method tests the generateExecutiveSummary of the SRBRegister plugin.
        It contains no assert call so the contents of the executive summary is not tested.
        """
        edPluginControlDLSArchiver = self.createPlugin()
    
    
    def testFileNameExtraction( self ):
        """
        This method should test to make sure that the plugin is extracting the correct file 
        list from the xml ingest file
        """
        
        try :
            os.rename("../data/create-ds.xml.icat","../data/create-ds.xml")
        except :
            print "nothing to delete"     
            
        # Create the plugin instance
        edPluginExecSRBRegister = self.createPlugin()
        # Read in the data from the XML 
        edStringInputExecSRBRegisterv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile )

        # gives the data to the plugin
        edPluginExecSRBRegister.setDataInput( edStringInputExecSRBRegisterv10XML )
        
        edPluginExecSRBRegister.openXMLTree()
        
        edFilelist = edPluginExecSRBRegister.processFileList()
        
        # assert that the filelist is correct
        edTestlist = ["EDPluginExecSRBRegisterv10_output.xml\n"]
        
        EDAssert.equal(edFilelist,edTestlist)
        


    def testDropFileCreation( self ):
        """
        This test will check to make sure the dropfile is created correctly and saved properly
        """
        
        try :
            os.remove("../data/out/test2.drop")
        except :
            print "nothing to delete"
        
        try :
            os.rename("../data/create-ds.xml.icat","../data/create-ds.xml")
        except :
            print "nothing to delete"          
        
        # Create the plugin instance
        edPluginExecSRBRegister = self.createPlugin()
        # Read in the data from the XML, for the big xml 
        edStringInputExecSRBRegisterv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile )

        # gives the data to the plugin
        edPluginExecSRBRegister.setDataInput( edStringInputExecSRBRegisterv10XML )
        
        # call the method
        edPluginExecSRBRegister.createDropFile();
        
        # finalise the process
        edPluginExecSRBRegister.moveGeneratedFiles()
        
        # check that the file has been created
        EDAssert.equal(True, os.path.isfile("../data/out/test2.drop"))
        EDAssert.equal(True, os.path.isfile("../data/create-ds.xml.icat"))


    def testIgnoreFile(self):
        
        # Create the plugin instance
        edPluginExecSRBRegister = self.createPlugin()
        # Read in the data from the XML, for the big xml 
        edStringInputExecSRBRegisterv10XML  = EDUtilsTest.readAndParseFile( self.m_edStringReferenceDataInputFile3)
        
        # gives the data to the plugin
        edPluginExecSRBRegister.setDataInput( edStringInputExecSRBRegisterv10XML )
        
        # first load the tree
        edPluginExecSRBRegister.openXMLTree()
        
        edPluginExecSRBRegister.checkAgainstIgnoreList()
        
        EDAssert.equal(False,edPluginExecSRBRegister.forArchiving)


##############################################################################
 
    def process( self ):
        """
        """
        self.addTestMethod( self.testSetDataInput )
        self.addTestMethod( self.testGenerateExecutiveSummary )
        self.addTestMethod( self.testFileNameExtraction )
        self.addTestMethod( self.testDropFileCreation )
        self.addTestMethod( self.testIgnoreFile )
        
##############################################################################


if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()
    
    edTestCasePluginExecUnitSRBRegisterv10 = EDTestCasePluginExecUnitSRBRegisterv10( "EDTestCasePluginExecUnitSRBRegisterv10" )
    edTestCasePluginExecUnitSRBRegisterv10.execute()


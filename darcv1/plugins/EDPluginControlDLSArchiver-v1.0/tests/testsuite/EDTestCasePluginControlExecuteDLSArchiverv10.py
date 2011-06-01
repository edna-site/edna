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


from EDImportLib                      import EDCompiler
from EDImportLib                      import EDVerbose
from EDImportLib                      import EDString
from EDImportLib                      import EDDiskExplorer

from EDTestCasePluginExecute import EDTestCasePluginExecute
from EDAssert import EDAssert


class EDTestCasePluginControlExecuteDLSArchiverv10( EDTestCasePluginExecute ):
    """
    """
    
    def __init__( self, _oalStringTestName = None):
        """
        """       
        EDTestCasePluginExecute.__init__( self, "EDPluginControlDLSArchiverv10", "EDPluginControlDLSArchiver-v1.0", _oalStringTestName )
        self.setConfigurationFile( self.getRefConfigFile() )
        self.setDataInputFile( EDDiskExplorer.mergePath( self.getPluginTestsDataHome(), "XSDataInputPluginControlDLSArchiverv10_reference.xml" ) )
        
        
    def testExecute( self ):
        """
        """ 
        self.run()
        



##############################################################################

    def process( self ):
        """
        """
        self.addTestMethod( self.testExecute )

        
        
##############################################################################


if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()
    
    edTestCasePluginControlExecuteDLSArchiverv10 = EDTestCasePluginControlExecuteDLSArchiverv10( "EDTestCasePluginControlExecuteDLSArchiverv10" )
    edTestCasePluginControlExecuteDLSArchiverv10.execute()
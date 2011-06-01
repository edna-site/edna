#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS 2010
#
#    Principal author:        Mark Basham
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


from EDImportLib import EDVerbose

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataTomo import XSDataInputTomography

class EDTestCasePluginUnitControlTomographyv10( EDTestCasePluginUnit ):
    """
    """

    def __init__( self, _edStringTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__( self, "EDPluginExecTomographyv10", "EDPluginControlTomography-v1.0", _edStringTestName )
              

    def testCheckParameters( self ):
        xsDataInput = XSDataInputTomography()
        edPluginExecTomography = self.createPlugin()
        edPluginExecTomography.setDataInput( xsDataInput )
        edPluginExecTomography.checkParameters()
        
    
    
    def process( self ):
        self.addTestMethod( self.testCheckParameters )

    

##############################################################################


if __name__ == '__main__':

    EDTestCasePluginUnitControlTomographyv10 = EDTestCasePluginUnitControlTomographyv10( "EDTestCasePluginUnitControlTomographyv10" )
    EDTestCasePluginUnitControlTomographyv10.execute()

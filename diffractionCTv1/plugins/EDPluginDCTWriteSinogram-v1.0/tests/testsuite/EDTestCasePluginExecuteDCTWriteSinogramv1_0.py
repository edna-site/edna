#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

import os
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsPath                         import EDUtilsPath

from XSDataDiffractionCTv1 import XSDataString 
from XSDataDiffractionCTv1 import XSDataFile

class EDTestCasePluginExecuteDCTWriteSinogramv1_0( EDTestCasePluginExecute ):
    """
    """
    
    def __init__( self, _edStringTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__( self, "EDPluginDCTWriteSinogramv1_0" )

        self.setDataInputFile( os.path.abspath(os.path.join( self.getPluginTestsDataHome(), \
                                                      "XSDataInputWriteSinogram_reference.xml" ) ))
        
        self.setReferenceDataOutputFile( os.path.abspath(os.path.join( self.getPluginTestsDataHome(), \
                                                                "XSDataResultWriteSinogram_reference.xml")))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"
       
    def testExecute( self ):
        """
        """ 
        self.run()
        
        # Checks that there are no error messages
        
        plugin = self.getPlugin()




##############################################################################

    def process( self ):
        """
        """
        self.addTestMethod( self.testExecute )

        
        
##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteDCTWriteSinogramv1_0 = EDTestCasePluginExecuteDCTWriteSinogramv1_0( "EDTestCasePluginExecuteDCTWriteSinogramv1_0" )
    edTestCasePluginExecuteDCTWriteSinogramv1_0.execute()

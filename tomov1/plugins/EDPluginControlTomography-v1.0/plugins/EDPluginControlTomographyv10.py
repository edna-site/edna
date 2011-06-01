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

__author__="Mark Basham"
__license__ = "GPLv3+"
__copyright__ = "DLS 2010"

from EDImportLib import EDVerbose

from EDPluginControl import EDPluginControl

from XSDataTomo import XSDataInputTomography
from XSDataTomo import XSDataResultTomography

class EDPluginControlTomographyv10( EDPluginControl ):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """
    

    def __init__( self ):
        """
        """
        EDPluginControl.__init__( self )
        self.setXSDataInputClass( XSDataInputTomography )
        self.m_edStringControlledPluginName = "EDPluginExecTomographyv10"
        self.m_edPluginExecTemplate = None


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.checkParameters")
        self.checkMandatoryParameters( self.getDataInput(), "Data Input is None" )

    
    def preProcess( self, _edObject = None ):
        EDPluginControl.preProcess( self )
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.preProcess")
        # Load the execution plugin
        self.m_edPluginExecTemplate = self.loadPlugin( self.m_edStringControlledPluginName ) 

        
    def process( self, _edObject = None ):
        EDPluginControl.process( self )
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.process")
        self.m_edPluginExecTemplate.connectSUCCESS( self.doSuccessExecTemplate )
        self.m_edPluginExecTemplate.connectFAILURE( self.doFailureExecTemplate )
        self.m_edPluginExecTemplate.executeSynchronous()

    
    def postProcess( self, _edObject = None ):
        EDPluginControl.postProcess( self )
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.postProcess")
        # Create some output data
        xsDataResult = XSDataResultTomography()
        self.setDataOutput( xsDataResult )
    

    def doSuccessExecTemplate( self,  _edPlugin = None ):
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.doSuccessExecTemplate" )
        self.retrieveSuccessMessages( _edPlugin, "EDPluginControlTomographyv10.doSuccessExecTemplate" )


    def doFailureExecTemplate( self,  _edPlugin = None ):
        EDVerbose.DEBUG( "*** EDPluginControlTomographyv10.doFailureExecTemplate" )
        self.retrieveFailureMessages( _edPlugin, "EDPluginControlTomographyv10.doFailureExecTemplate" )

#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

from EDVerbose    import EDVerbose
from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile


class EDPluginExecCreateDNAFilesDirectoryv1_0( EDPluginExec ):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """


    def __init__( self ):
        """
        """
        EDPluginExec.__init__( self )
        self.setXSDataInputClass( XSDataFile, "dnaFilesParentDirectory" )


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "EDPluginExecCreateDNAFilesDirectoryv1_0.checkParameters" )
        self.checkMandatoryParameters( self.getDataInput(), "Data Input is None" )


    def preProcess( self, _edObject=None ):
        EDPluginExec.preProcess( self )
        EDVerbose.DEBUG( "EDPluginExecCreateDNAFilesDirectoryv1_0.postProcess" )


    def process( self, _edObject=None ):
        EDPluginExec.process( self )
        EDVerbose.DEBUG( "EDPluginExecCreateDNAFilesDirectoryv1_0.process" )


    def postProcess( self, _edObject=None ):
        EDPluginExec.postProcess( self )
        EDVerbose.DEBUG( "EDPluginExecCreateDNAFilesDirectoryv1_0.postProcess" )
        # Create some output data
        xsDataResult = < xsDataResultName > ()
        self.setDataOutput( xsDataResult )


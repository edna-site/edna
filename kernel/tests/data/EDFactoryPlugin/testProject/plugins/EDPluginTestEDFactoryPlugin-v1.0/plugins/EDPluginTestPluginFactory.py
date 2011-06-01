#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author: Karl Levik (karl.levik@diamond.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

from EDPlugin import EDPlugin

from XSDataCommon import XSDataString

class EDPluginTestPluginFactory( EDPlugin ):

    def __init__( self ):
        EDPlugin.__init__( self )
        self.setXSDataInputClass( XSDataString )
        self.setXSDataInputClass( XSDataString, "value1" )
        self.setXSDataInputClass( XSDataString, "value2" )

    def getTestValue( self ):
        return "TestReturnValue"

    def process( self, _edPlugin=None ):
        pyListKeyValues = self.getListOfDataInputKeys()
        for pyStrKey in pyListKeyValues:
            if ( pyStrKey == self.getDefaultInputDataKey() ):
                self.setDataOutput( self.getDataInput( pyStrKey ) )
            else:
                self.setDataOutput( self.getDataInput( pyStrKey ), pyStrKey )


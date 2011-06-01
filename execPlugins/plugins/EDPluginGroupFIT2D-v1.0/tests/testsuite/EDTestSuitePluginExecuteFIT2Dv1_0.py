#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 INSTITUTE_LINE_1
#                            INSTITUTE_LINE_2
#
#    Principal author:       PRINCIPAL_AUTHOR
#
#    Contributing author:    CONTRIBUTING_AUTHOR
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

from EDTestSuite import EDTestSuite

class EDTestSuitePluginExecuteFIT2Dv1_0( EDTestSuite ):
        

    def process( self ):
        """
        """
        self.addTestCaseFromName( "EDTestCasePluginExecuteFIT2DCakev1_0" )
        self.addTestCaseFromName( "EDTestCasePluginExecuteFIT2DCakev1_1" )
        self.addTestCaseFromName( "EDTestCasePluginExecuteFIT2DCakev1_1withCIFOutput" )


##############################################################################
if __name__ == '__main__':

    EDTestSuitePluginExecuteFIT2Dv1_0 = EDTestSuitePluginExecuteFIT2Dv1_0( "EDTestSuitePluginExecuteFIT2Dv1_0" )
    EDTestSuitePluginExecuteFIT2Dv1_0.execute()

##############################################################################
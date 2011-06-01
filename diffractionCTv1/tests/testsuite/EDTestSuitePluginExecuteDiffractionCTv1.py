#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteMXPluginExec.py 923 2009-10-27 13:35:32Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteDiffractionCTv1(EDTestSuite):


    def process(self):
        """
        """
        # Test as well the execPlugins
#        self.addTestSuiteFromName( "EDTestSuitePluginExecuteExecPlugins" )        
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlDCTReadHeaderv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlDCTPowderIntegrationv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteDCTWriteSinogramv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteControlDiffractionCTv1_0")



##############################################################################
if __name__ == '__main__':

    edTestSuitePluginExecuteDiffractionCTv1 = EDTestSuitePluginExecuteDiffractionCTv1("EDTestSuitePluginExecuteDiffractionCTv1")
    edTestSuitePluginExecuteDiffractionCTv1.execute()

##############################################################################

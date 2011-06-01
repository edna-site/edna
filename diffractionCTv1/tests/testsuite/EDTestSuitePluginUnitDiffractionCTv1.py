# coding: utf8
#
#    Project: DiffractionCT
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Jérôme Kieffer 
#                            Olof Svensson (svensson@esrf.fr) 
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published
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


from EDTestSuite           import EDTestSuite


class EDTestSuitePluginUnitDiffractionCTv1(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCaseEDHandlerFIT2Dv1_0")
        # Test as well the execPlugins
        self.addTestSuiteFromName("EDTestSuitePluginUnitExecPlugins")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlDCTReadHeaderv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlDCTPowderIntegrationv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginUnitControlDiffractionCTv1_0")



##############################################################################
if __name__ == '__main__':


    edTestSuitePluginUnitDiffractionCTv1 = EDTestSuitePluginUnitDiffractionCTv1("EDTestSuitePluginUnitDiffractionCTv1")
    edTestSuitePluginUnitDiffractionCTv1.execute()

##############################################################################

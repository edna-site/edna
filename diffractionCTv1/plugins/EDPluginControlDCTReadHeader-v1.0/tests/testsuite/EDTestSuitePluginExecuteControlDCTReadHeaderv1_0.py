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

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginExecuteControlDCTReadHeaderv1_0(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginExecuteControlDCTReadHeaderv1_0")


if __name__ == '__main__':

    edTestSuitePluginExecuteControlDCTReadHeaderv1_0 = EDTestSuitePluginExecuteControlDCTReadHeaderv1_0("EDTestSuitePlugin<basName>DCTReadHeaderv1_0")
    edTestSuitePluginExecuteControlDCTReadHeaderv1_0.execute()


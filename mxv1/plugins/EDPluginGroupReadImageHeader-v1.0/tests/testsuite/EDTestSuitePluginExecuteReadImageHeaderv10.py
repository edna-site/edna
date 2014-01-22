#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2014 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteReadImageHeaderv10(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecutePluginExecReadImageHeaderADSCv10")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginExecReadImageHeaderPilatus2Mv10")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginExecReadImageHeaderPilatus6Mv10")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_MARCCD")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_Pilatus2M")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_Pilatus6M")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile")
        self.addTestCaseFromName("EDTestCasePluginExecutePluginControlReadImageHeaderv10_failure")

if __name__ == '__main__':

    edTestSuitePluginExecuteReadImageHeaderv10 = EDTestSuitePluginExecute("EDTestSuitePluginExecuteReadImageHeaderv10")
    edTestSuitePluginExecuteReadImageHeaderv10.execute()


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



import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName="EDPluginExecReadImageHeaderMARCCDv10"):
        EDTestCasePluginExecute.__init__(self, _strTestName)
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputReadImageHeader_MARCCD_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultReadImageHeader_MARCCD_reference.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-screentest-crystal1_1_001.mccd" ])


    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10 = EDTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10("EDTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10")
    edTestCasePluginExecutePluginExecReadImageHeaderMARCCDv10.execute()

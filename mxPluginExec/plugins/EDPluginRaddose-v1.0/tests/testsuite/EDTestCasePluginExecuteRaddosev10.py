#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDAssert                         import EDAssert
from EDTestCasePluginExecute          import EDTestCasePluginExecute



class EDTestCasePluginExecuteRaddosev10(EDTestCasePluginExecute):

    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginRaddosev10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataRaddosev10Input_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataRaddosev10Output_reference.xml"))


    def testExecute(self):
        self.run()

        if self.getPlugin().findStringInLog("version 2"):
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataRaddosev10Output_reference_Raddosev2.xml"))

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())

        from XSDataRaddosev10 import XSDataRaddoseOutput
        xsDataOutputExpected = XSDataRaddoseOutput.parseString(strExpectedOutput)
        xsDataOutputObtained = self.getPlugin().getDataOutput()

        EDAssert.equal(xsDataOutputExpected.marshal(), xsDataOutputObtained.marshal())


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edTestCasePluginExecuteRaddosev10 = EDTestCasePluginExecuteRaddosev10("EDTestCasePluginExecuteRaddosev10")
    edTestCasePluginExecuteRaddosev10.execute()

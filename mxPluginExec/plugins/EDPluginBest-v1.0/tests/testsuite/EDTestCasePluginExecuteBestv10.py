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
__status__ = "deprecated"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteBestv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBestv10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataBestv10Input_reference.xml"))


    def testExecute(self):
        self.run()

        edPlugin = self.getPlugin()

        strBestVersion = self.getPlugin().getStringVersion()

        if strBestVersion.find("3.1.0") != -1 :
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataBestv10Output_reference.xml"))
        elif strBestVersion.find("3.2.0") != -1 :
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataBestv10Output_reference_BESTv320.xml"))

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile(self.getReferenceDataOutputFile())

        from XSDataBestv10 import XSDataBestOutput
        xsDataOutputExpected = XSDataBestOutput.parseString(strExpectedOutput)
        xsDataOutputObtained = edPlugin.getDataOutput()

        EDAssert.equal(xsDataOutputExpected.marshal(), xsDataOutputObtained.marshal())



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBestv10 = EDTestCasePluginExecuteBestv10("EDTestCasePluginExecuteBestv10")
    edTestCasePluginExecuteBestv10.execute()

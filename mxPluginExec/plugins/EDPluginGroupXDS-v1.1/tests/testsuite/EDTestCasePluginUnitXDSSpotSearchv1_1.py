#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#                            Sandor Brockhauser (brockhauser@embl-grnoble.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

__authors__ = ["Olof Svensson", "Sandor Brockhauser", "Gleb Bourenkov"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDUtilsTest                    import EDUtilsTest
from EDUtilsPath                    import EDUtilsPath

from XSDataXDSv1_1 import XSDataInputXDSSpotSearch

class EDTestCasePluginUnitXDSSpotSearchv1_1(EDTestCasePluginUnit):

    def __init__(self, _pyStrTestName="EDPluginXDSSpotSearchv1_1"):
        """
        Set up paths, reference files etc.
        """
        EDTestCasePluginUnit.__init__(self, _pyStrTestName)
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSSpotSearch_reference.xml")


    def testCheckParameters(self):
        edPluginXDSSpotSearchv1_1 = self.createPlugin()
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        xsDataInputXDSSpotSearch = XSDataInputXDSSpotSearch.parseString(pyStrXMLInput)
        edPluginXDSSpotSearchv1_1.setDataInput(xsDataInputXDSSpotSearch)
        edPluginXDSSpotSearchv1_1.checkParameters()


    def testCreateXDSInput(self):
        edPluginXDSSpotSearchv1_1 = self.createPlugin()
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        xsDataInputXDSSpotSearch = XSDataInputXDSSpotSearch.parseString(pyStrXMLInput)
        edPluginXDSSpotSearchv1_1.setDataInput(xsDataInputXDSSpotSearch)
        #edPluginXDSSpotSearchv1_1.configure()
        edPluginXDSSpotSearchv1_1.createXDSInput()
        print edPluginXDSSpotSearchv1_1.m_pyStrXDSInput


    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testCreateXDSInput)



if __name__ == '__main__':
    edTestCasePluginUnitXDSSpotSearchv1_1 = EDTestCasePluginUnitXDSSpotSearchv1_1("EDTestCasePluginUnitXDSSpotSearchv1_1")
    edTestCasePluginUnitXDSSpotSearchv1_1.execute()

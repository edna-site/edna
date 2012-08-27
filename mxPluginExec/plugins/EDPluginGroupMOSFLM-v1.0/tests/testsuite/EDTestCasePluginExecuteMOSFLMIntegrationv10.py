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
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDAssert import EDAssert
from EDTestCasePluginExecuteMOSFLMv10 import EDTestCasePluginExecuteMOSFLMv10

from XSDataMOSFLMv10 import XSDataMOSFLMOutputIntegration


class EDTestCasePluginExecuteMOSFLMIntegrationv10(EDTestCasePluginExecuteMOSFLMv10):


    def __init__(self, _strTestName="EDPluginMOSFLMIntegrationv10"):
        EDTestCasePluginExecuteMOSFLMv10.__init__(self, _strTestName)

        self.setDataInputFile(os.path.join(self.strExecutionTestDataInputHome, "XSDataMOSFLMInputIntegration_reference.xml"))
        # We don't use the setReferenceDataOutputFile method because the automatic testing of the 
        # expected versus obtained is problematic due to different results on different architectures
        self.__strReferenceDataOutputFile = os.path.join(self.strExecutionTestDataResultHome, "XSDataMOSFLMOutputIntegration_reference.xml")




    def testExecute(self):
        self.run()
        # Compare results
        strXMLExpected = self.readAndParseFile(self.__strReferenceDataOutputFile)
        xsDataObtained = self.getPlugin().getDataOutput()
        xsDataExpected = XSDataMOSFLMOutputIntegration.parseString(strXMLExpected)
        # Remove the bestFileHKL part which creates problem...
        xsDataObtained.setBestfileHKL(None)
        xsDataExpected.setBestfileHKL(None)
        EDAssert.strAlmostEqual(xsDataExpected.marshal(), xsDataObtained.marshal(), "(MOSFLM integration result comparison - expected versus obtained)", 0.1, 5000)



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteMOSFLMIntegrationv10 = EDTestCasePluginExecuteMOSFLMIntegrationv10("EDTestCasePluginExecuteMOSFLMIntegrationv10")
    edTestCasePluginExecuteMOSFLMIntegrationv10.execute()

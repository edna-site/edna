#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:  Marie-Francoise Incardona (incardon@esrf.fr)
#                           Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Karl Levik", "Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "karl.levik@diamond.ac.uk"
__license__ = "LGPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

import os.path

from EDAssert                         import EDAssert
from EDTestCasePluginExecute          import EDTestCasePluginExecute


from XSDataISPyBv10                   import XSDataResultISPyB
from XSDataCommon                     import XSDataString

class EDTestCasePluginExecuteISPyBv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginISPyBv10", "EDPluginGroupISPyB-v1.0", _strTestName)

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv10Input_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultISPyB_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

    def testHttpPost(self):
        """
        A test for whether the httpPost method can send a request to the dbserver and receive a response
        """
        edPluginISPyB = self.createPlugin()
        xsPluginItemISPyB = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginISPyB.setConfiguration(xsPluginItemISPyB)
        edPluginISPyB.configure()

        edStringXML = '<?xml version="1.0" encoding="UTF-8"?><Proposal><code>nt</code><number>20</number></Proposal>'
        edStringResponse = edPluginISPyB.httpPost(edPluginISPyB.getDbserverHost(), edPluginISPyB.getDbserverPort(), \
                                                  '/proposal_request', edStringXML)
        if edStringResponse != None:
            self.DEBUG("*** EDTestCasePluginExecuteISPyBv10.testHttpPost response: " + edStringResponse)

        EDAssert.equal(edStringResponse != None, True)


    def testExecute(self):
        """
        Runs the plugin and then compares expected output with obtained output to verify that it executed correctly. 
        """
        self.run()

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile(self.m_edObtainedOutputDataFile)
        xsDataResultISPyBObtained = XSDataResultISPyB.parseString(strObtainedOutput)
        xsDataResultStatusListObtained = xsDataResultISPyBObtained.getResultStatus()

        self.DEBUG("Checking obtained result...")
        for xsDataResultStatusObtained in xsDataResultStatusListObtained:
            EDAssert.equal(xsDataResultStatusObtained.getCode().getValue(), "ok")


    def process(self):
        """
        Adds the plugin execute test methods
        """
        #self.addTestMethod( self.testHttpPost )
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteISPyBv10 = EDTestCasePluginExecuteISPyBv10("EDTestCasePluginExecuteISPyBv10")
    edTestCasePluginExecuteISPyBv10.execute()

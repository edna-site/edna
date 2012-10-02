#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest
from EDVerbose import EDVerbose

from XSDataMXv1 import XSDataIntegrationResult

class EDTestCasePluginUnitControlIntegrationv10(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlIntegrationv10", "EDPluginControlIntegration-v1.0", _edStringTestName)
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataIntegrationInput_reference.xml")


    def testConfigureOK(self):
        edPluginControlIntegrationv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlIntegrationv10.setConfiguration(xsPluginItemGood01)
        edPluginControlIntegrationv10.configure()
        self.cleanUp(edPluginControlIntegrationv10)



    def testSetDataInput(self):
        edPluginControlIntegrationv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlIntegrationv10.setConfiguration(xsPluginItemGood01)
        edPluginControlIntegrationv10.configure()
        xmlInputReference = self.readAndParseFile(self.strReferenceInputFile)
        from XSDataMXv1 import XSDataIntegrationInput
        xsDataIntegrationInputReference = XSDataIntegrationInput.parseString(xmlInputReference)
        edPluginControlIntegrationv10.setDataInput(xmlInputReference)
        xsDataIntegrationv10Input = edPluginControlIntegrationv10.getDataInput()
        EDAssert.equal(xsDataIntegrationInputReference.marshal(), xsDataIntegrationv10Input.marshal())
        self.cleanUp(edPluginControlIntegrationv10)


    def testGenerateIntegrationShortSummary(self):
        edPluginControlIntegrationv10 = self.createPlugin()
        strReferenceOutputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataIntegrationResult_reference.xml")
        strXML = self.readAndParseFile(strReferenceOutputFile)
        xsDataIntegrationResult = XSDataIntegrationResult.parseString(strXML)
        edPluginControlIntegrationv10.generateIntegrationShortSummary(xsDataIntegrationResult)
        for strLine in edPluginControlIntegrationv10.getDataOutput("integrationShortSummary")[0].getValue().split("\n"):
            EDVerbose.unitTest(strLine)


    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataInput)
        self.addTestMethod(self.testGenerateIntegrationShortSummary)



if __name__ == '__main__':

    edTestCasePluginUnitControlIntegrationv10 = EDTestCasePluginUnitControlIntegrationv10("EDTestCasePluginUnitControlIntegrationv10")
    edTestCasePluginUnitControlIntegrationv10.execute()


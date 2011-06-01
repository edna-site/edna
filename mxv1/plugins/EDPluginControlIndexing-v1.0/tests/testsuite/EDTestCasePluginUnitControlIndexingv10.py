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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit

from XSDataMXv1 import XSDataIndexingInput

class EDTestCasePluginUnitControlIndexingv10(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlIndexingv10")
        self.__strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataIndexingInput_reference.xml")


    def testConfigureOK(self):
        edPluginControlIndexingv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlIndexingv10.setConfiguration(xsPluginItemGood01)
        edPluginControlIndexingv10.configure()


    def testSetDataInput(self):
        edPluginControlIndexingv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlIndexingv10.setConfiguration(xsPluginItemGood01)
        edPluginControlIndexingv10.configure()

        xmlInput = self.readAndParseFile(self.__strReferenceInputFile)
        edPluginControlIndexingv10.setDataInput(xmlInput)

        xsDataIndexingv01Input = edPluginControlIndexingv10.getDataInput()

        xsDataIndexingInputReference = XSDataIndexingInput.parseString(xmlInput)
        EDAssert.equal(xsDataIndexingInputReference.marshal(), xsDataIndexingv01Input.marshal())

        self.cleanUp(edPluginControlIndexingv10)



    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataInput)




if __name__ == '__main__':

    edTestCasePluginUnitControlIndexingv10 = EDTestCasePluginUnitControlIndexingv10("EDTestCasePluginUnitControlIndexingv10")
    edTestCasePluginUnitControlIndexingv10.execute()


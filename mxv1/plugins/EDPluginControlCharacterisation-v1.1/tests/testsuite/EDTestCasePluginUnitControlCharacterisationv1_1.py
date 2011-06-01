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
from EDUtilsFile                         import EDUtilsFile


class EDTestCasePluginUnitControlCharacterisationv1_1(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlCharacterisationv1_1", "EDPluginControlCharacterisation-v0.1", _edStringTestName)
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference.xml")


    def testConfigureOK(self):
        edPluginControlCharacterisationv1_1 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlCharacterisationv1_1.setConfiguration(xsPluginItemGood01)
        edPluginControlCharacterisationv1_1.configure()


    def testSetDataInput(self):
        edPluginControlCharacterisationv1_1 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlCharacterisationv1_1.setConfiguration(xsPluginItemGood01)
        edPluginControlCharacterisationv1_1.configure()

        edStringXMLInput = self.readAndParseFile(self.strReferenceInputFile)
        edPluginControlCharacterisationv1_1.setDataInput(edStringXMLInput)
        from XSDataMXv1 import XSDataInputCharacterisation
        xsDataInputCharacterisationReference = XSDataInputCharacterisation.parseString(edStringXMLInput)

        xsDataInputCharacterisationv11 = edPluginControlCharacterisationv1_1.getDataInput()
        EDAssert.equal(xsDataInputCharacterisationReference.marshal(), xsDataInputCharacterisationv11.marshal())



    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataInput)




if __name__ == '__main__':

    edTestCasePluginUnitControlCharacterisationv1_1 = EDTestCasePluginUnitControlCharacterisationv1_1("EDTestCasePluginUnitControlCharacterisationv1_1")
    edTestCasePluginUnitControlCharacterisationv1_1.execute()


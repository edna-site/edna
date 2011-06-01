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


class EDTestCasePluginUnitControlCharacterisationv10(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlCharacterisationv10", "EDPluginControlCharacterisation-v0.1", _edStringTestName)
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataCollection_reference.xml")


    def testConfigureOK(self):
        edPluginControlCharacterisationv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlCharacterisationv10.setConfiguration(xsPluginItemGood01)
        edPluginControlCharacterisationv10.configure()


    def testSetDataInput(self):
        edPluginControlCharacterisationv10 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginControlCharacterisationv10.setConfiguration(xsPluginItemGood01)
        edPluginControlCharacterisationv10.configure()

        edStringXMLInput = self.readAndParseFile(self.strReferenceInputFile)
        edPluginControlCharacterisationv10.setDataInput(edStringXMLInput)
        from XSDataMXv1 import XSDataCollection
        xsDataCollectionReference = XSDataCollection.parseString(edStringXMLInput)

        xsDataCharacterisationv10Input = edPluginControlCharacterisationv10.getDataInput()
        EDAssert.equal(xsDataCollectionReference.marshal(), xsDataCharacterisationv10Input.marshal())



    def process(self):
        self.addTestMethod(self.testConfigureOK)
        self.addTestMethod(self.testSetDataInput)




if __name__ == '__main__':

    edTestCasePluginUnitControlCharacterisationv10 = EDTestCasePluginUnitControlCharacterisationv10("EDTestCasePluginUnitControlCharacterisationv10")
    edTestCasePluginUnitControlCharacterisationv10.execute()


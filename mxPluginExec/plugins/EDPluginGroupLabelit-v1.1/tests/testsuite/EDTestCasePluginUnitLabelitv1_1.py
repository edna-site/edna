#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDAssert    import EDAssert
from EDUtilsTest import EDUtilsTest
from EDUtilsFile import EDUtilsFile

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataLabelitv1_1 import XSDataImage

class EDTestCasePluginUnitLabelitv1_1(EDTestCasePluginUnit):


    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginLabelitIndexingv1_1")
        self.__strReferenceInputFile1 = os.path.join(self.getPluginTestsDataHome(), "XSDataImage_1_reference.xml")
        self.__strReferenceInputFile2 = os.path.join(self.getPluginTestsDataHome(), "XSDataImage_2_reference.xml")


    def testSetDataInput(self):
        """
        This method test the setDataInput method of the Labelit plugin by providing an XML string
        and then retriving an XSDataInputLabelit object.
        """
        edPluginLabelitv1_1 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginLabelitv1_1.setConfiguration(xsPluginItemGood01)
        edPluginLabelitv1_1.setScriptExecutable("cat")
        edPluginLabelitv1_1.configure()
        xmlInput1 = self.readAndParseFile(self.__strReferenceInputFile1)
        edPluginLabelitv1_1.setDataInput(xmlInput1, "referenceImage")
        xmlInput2 = self.readAndParseFile(self.__strReferenceInputFile2)
        edPluginLabelitv1_1.setDataInput(xmlInput2, "referenceImage")
        xsDataImageReference1 = XSDataImage.parseString(xmlInput1)
        xsDataImageReference2 = XSDataImage.parseString(xmlInput2)
        xsDataImage1 = edPluginLabelitv1_1.getDataInput("referenceImage")[0]
        xsDataImage2 = edPluginLabelitv1_1.getDataInput("referenceImage")[1]
        EDAssert.equal(xsDataImageReference1.marshal(), xsDataImage1.marshal())
        EDAssert.equal(xsDataImageReference2.marshal(), xsDataImage2.marshal())



    def testInitaliseLabelitCommandLine(self):
        """
        This method tests the initaliseLabelitCommandLine method of the Labelit plugin.
        """
        edPluginLabelitv1_1 = self.createPlugin()
        xmlInput1 = EDUtilsFile.readFile(self.__strReferenceInputFile1)
        edPluginLabelitv1_1.setDataInput(xmlInput1, "referenceImage")
        xmlInput2 = EDUtilsFile.readFile(self.__strReferenceInputFile2)
        edPluginLabelitv1_1.setDataInput(xmlInput2, "referenceImage")
        edPluginLabelitv1_1.initaliseLabelitCommandLine()
        strScriptCommandLine = edPluginLabelitv1_1.getScriptCommandline()
        strCommandLineExpected = "--index_only ${EDNA_TESTIMAGES}/images/ref-testscale_1_001.img ${EDNA_TESTIMAGES}/images/ref-testscale_1_002.img"
        EDAssert.equal(strCommandLineExpected, strScriptCommandLine)



    def process(self):
        self.addTestMethod(self.testSetDataInput)
        self.addTestMethod(self.testInitaliseLabelitCommandLine)


if __name__ == '__main__':

    EDTestCasePluginUnitLabelitv1_1 = EDTestCasePluginUnitLabelitv1_1("EDTestCasePluginUnitLabelitv1_1")
    EDTestCasePluginUnitLabelitv1_1.execute()


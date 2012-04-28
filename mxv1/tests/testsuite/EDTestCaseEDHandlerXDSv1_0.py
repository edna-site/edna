#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
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

from EDTestCase import EDTestCase
from EDUtilsTest import EDUtilsTest
from EDUtilsPath import EDUtilsPath
from EDAssert import EDAssert

class EDTestCaseEDHandlerXDSv1_0(EDTestCase):
    """
    """

    def __init__(self, _pyStrTestName=None):
        """
        """
        EDTestCase.__init__(self, _pyStrTestName)
        pyStrMXv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        pyStrDataDir = "EDHandlerXDSv1_0"
        self.m_pyStrDataPath = os.path.join(pyStrMXv1DataHome, pyStrDataDir)


    def testGenerateXSDataInputXDSIndexing(self):
        pyStrFilename = "XSDataIndexingInput_reference.xml"
        pyStrPath = os.path.join(self.m_pyStrDataPath, pyStrFilename)
        pyStrXMLIndexingInput = self.readAndParseFile(pyStrPath)
        from XSDataMXv1 import XSDataIndexingInput
        xsDataIndexingInput = XSDataIndexingInput.parseString(pyStrXMLIndexingInput)

        from EDHandlerXSDataXDSv1_0 import EDHandlerXSDataXDSv1_0
        xsDataInputXDSIndexing = EDHandlerXSDataXDSv1_0.generateXSDataInputXDSIndexing(xsDataIndexingInput)

        xsDataInputXDSIndexing.exportToFile("XSDataInputXDSIndexing_reference.xml")

        pyStrReferenceFilename = "XSDataInputXDSIndexing_reference.xml"
        pyStrReferencePath = os.path.join(self.m_pyStrDataPath, pyStrReferenceFilename)
        xsDataInputXDSIndexing.exportToFile("XSDataInputXDSIndexing.xml")
        pyStrXMLInputXDSIndexingReference = self.readAndParseFile(pyStrReferencePath)
        EDAssert.equal(pyStrXMLInputXDSIndexingReference, xsDataInputXDSIndexing.marshal())


    def process(self):
        """
        """
        self.addTestMethod(self.testGenerateXSDataInputXDSIndexing)


##############################################################################


if __name__ == '__main__':

    edTestCaseEDHandlerXDSv1_0 = EDTestCaseEDHandlerXDSv1_0("EDTestCaseEDHandlerXDSv1_0")
    edTestCaseEDHandlerXDSv1_0.execute()


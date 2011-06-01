# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr)
#
#    Contribution from: Jérôme Kieffer (jerome.kieffer@esrf.eu)
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

__authors__ = [ "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This is the test case for the EDUtilsFile static class.
"""


import os, tempfile

from EDTestCase     import EDTestCase
from EDVerbose      import EDVerbose
from EDAssert       import EDAssert
from EDUtilsFile    import EDUtilsFile

class EDTestCaseEDUtilsFile(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDUtilsFile")


    def testReadFileAndParseVariables(self):
        # Test 1 - just with environment variables in a file
        os.environ["TEST_XSCONFIGURATION1"] = "TEST1"
        os.environ["TEST_XSCONFIGURATION2"] = "TEST2"
        strTest1 = "This is a test: ${TEST_XSCONFIGURATION1}, another test ${TEST_XSCONFIGURATION2}"
        (fd, strFileName1) = tempfile.mkstemp(prefix="EDTestCaseEDUtilsFile-", suffix=".xml", text=True)
        os.close(fd)
        EDUtilsFile.writeFile(strFileName1, strTest1)
        strReference1 = "This is a test: TEST1, another test TEST2"
        strResult1 = EDUtilsFile.readFileAndParseVariables(strFileName1)
        EDAssert.equal(strReference1, strResult1, "Just with environment variables in a file")
        EDUtilsFile.deleteFile(strFileName1)
        # Test 2 - with a file and a dictionary
        strTest2 = "This is a second test: ${TEST_XSCONFIGURATION1}, ${EDNA_VARIABLE}, another test ${TEST_XSCONFIGURATION2} and another ${EDNA_VARIABLE2}."
        dictTest = { "${EDNA_VARIABLE}" : "EDNA1", "${EDNA_VARIABLE2}" : "EDNA2"}
        (fd, strFileName2) = tempfile.mkstemp(prefix="EDTestCaseEDUtilsFile-", suffix=".xml", text=True)
        os.close(fd)
        EDUtilsFile.writeFile(strFileName2, strTest2)
        strReference2 = "This is a second test: TEST1, EDNA1, another test TEST2 and another EDNA2."
        strResult2 = EDUtilsFile.readFileAndParseVariables(strFileName2, dictTest)
        EDAssert.equal(strReference2, strResult2, "with a file and a dictionary")
        EDUtilsFile.deleteFile(strFileName2)


    def process(self):
        self.addTestMethod(self.testReadFileAndParseVariables)


if __name__ == '__main__':

    edTestCaseEDUtilsFile = EDTestCaseEDUtilsFile("EDTestCaseEDUtilsFile")
    edTestCaseEDUtilsFile.execute()

# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr)
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

"""
This is the test case for the EDUtilsFile static class.
"""


import os, tempfile

from EDTestCase     import EDTestCase
from EDVerbose      import EDVerbose
from EDAssert       import EDAssert
from EDUtilsFile    import EDUtilsFile
from EDUtilsPath    import EDUtilsPath

class EDTestCaseEDUtilsPath(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDUtilsPath")


    def testGetEdnaUserTempFolder(self):
        # Test that we can access the user temp folder
        strUserTempFolder = EDUtilsPath.getEdnaUserTempFolder()
        EDAssert.equal(True, os.path.exists(strUserTempFolder), "Checking that user temp folder exists")
        # Test if we can write to the temp folder
        strTest = "This is a test string."
        strPathTestFile = os.path.join(strUserTempFolder, "EDTestCaseEDUtilsPath_testFile.txt")
        EDUtilsFile.writeFile(strPathTestFile, strTest)
        EDAssert.equal(True, os.path.exists(strPathTestFile), "Checking that new temp file exists")
        # Delete the test file
        os.remove(strPathTestFile)
        
        


    def process(self):
        self.addTestMethod(self.testGetEdnaUserTempFolder)


if __name__ == '__main__':

    edTestCaseEDUtilsPath = EDTestCaseEDUtilsPath("EDTestCaseEDUtilsPath")
    edTestCaseEDUtilsPath.execute()

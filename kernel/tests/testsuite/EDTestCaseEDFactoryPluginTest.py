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



from EDTestCase          import EDTestCase
from EDAssert            import EDAssert
from EDFactoryPluginTest import EDFactoryPluginTest
from EDUtilsPath         import EDUtilsPath

class EDTestCaseEDFactoryPluginTest(EDTestCase):

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDFactoryPluginTest")


    def testGetProjectRootDirectory(self):
        edFactoryPluginTest = EDFactoryPluginTest()
        strEdnaHome = EDUtilsPath.getEdnaHome()
        strTestProjectRootDirectoryReference = EDUtilsPath.appendListOfPaths(strEdnaHome, [ "kernel", "tests", "data", "EDFactoryPlugin", "testProject" ])
        strTestProjectRootDirectory1 = edFactoryPluginTest.getProjectRootDirectory("EDTestCasePluginUnitTestPluginFactory")
        EDAssert.equal(strTestProjectRootDirectoryReference, strTestProjectRootDirectory1)
        strTestProjectRootDirectory2 = edFactoryPluginTest.getProjectRootDirectory("EDTestSuitePluginUnitTestProject")
        EDAssert.equal(strTestProjectRootDirectoryReference, strTestProjectRootDirectory2)



    def process(self):
        self.addTestMethod(self.testGetProjectRootDirectory)



if __name__ == '__main__':

    edTestCaseEDFactoryPluginTest = EDTestCaseEDFactoryPluginTest("EDTestCaseEDFactoryPluginTest")
    edTestCaseEDFactoryPluginTest.execute()

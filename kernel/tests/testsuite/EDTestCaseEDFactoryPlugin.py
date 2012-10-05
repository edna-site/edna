#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestCase import EDTestCase
from EDAssert import EDAssert
from EDFactoryPlugin import EDFactoryPlugin
from EDUtilsPath import EDUtilsPath

class EDTestCaseEDFactoryPlugin(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        self.__edConfiguration = None


    def testGetProjectRootDirectory(self):
        edFactoryPlugin = EDFactoryPlugin()
        strEdnaHome = EDUtilsPath.getEdnaHome()
        strTestProjectRootDirectoryReference = EDUtilsPath.appendListOfPaths(strEdnaHome, [ "kernel", "tests", "data", "EDFactoryPlugin", "testProject" ])
        strTestProjectRootDirectory1 = edFactoryPlugin.getProjectRootDirectory("EDPluginTestPluginFactory")
        EDAssert.equal(strTestProjectRootDirectoryReference, strTestProjectRootDirectory1)
        strTestProjectRootDirectory2 = edFactoryPlugin.getProjectRootDirectory("XSDataTestProject")
        EDAssert.equal(strTestProjectRootDirectoryReference, strTestProjectRootDirectory2)
        strTestProjectRootDirectory3 = edFactoryPlugin.getProjectRootDirectory("PluginThatNotExists")
        EDAssert.equal(None, strTestProjectRootDirectory3)


    def testGetProjectName(self):
        edFactoryPlugin = EDFactoryPlugin()
        strProjectName = edFactoryPlugin.getProjectName("EDPluginTestPluginFactory")
        EDAssert.equal("testProject", strProjectName)


    def testLoadPlugin(self):
        edFactoryPlugin = EDFactoryPlugin()
        edPluginTest = edFactoryPlugin.loadPlugin("EDPluginTestPluginFactory")
        EDAssert.equal("TestReturnValue", edPluginTest.getTestValue())


    def testSaveModuleDictionaryToDisk(self):
        edFactoryPlugin = EDFactoryPlugin()
        edPluginTest = edFactoryPlugin.loadPlugin("EDPluginTestPluginFactory")
        edFactoryPlugin.saveModuleDictionaryToDisk("testDictionary.xml")



    def testLoadModuleDictionaryFromDisk(self):
        edFactoryPlugin = EDFactoryPlugin()
        edFactoryPlugin.loadModuleDictionaryFromDisk("testDictionary.xml")






    def process(self):
        """
        """
        self.addTestMethod(self.testGetProjectRootDirectory)
        self.addTestMethod(self.testGetProjectName)
        self.addTestMethod(self.testLoadPlugin)
        self.addTestMethod(self.testSaveModuleDictionaryToDisk)
        self.addTestMethod(self.testLoadModuleDictionaryFromDisk)




if __name__ == '__main__':

    edTestCaseEDFactoryPlugin = EDTestCaseEDFactoryPlugin("EDTestCaseEDFactoryPlugin")
    edTestCaseEDFactoryPlugin.execute()

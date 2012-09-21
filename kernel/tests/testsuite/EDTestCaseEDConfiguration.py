#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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


"""
This is the test case for the EDConfiguration class.
"""

import os

from EDAssert                import EDAssert
from EDConfiguration         import EDConfiguration
from EDConfigurationStatic   import EDConfigurationStatic
from EDUtilsTest             import EDUtilsTest
from EDUtilsPath             import EDUtilsPath
from EDTestCase              import EDTestCase

from XSDataCommon import XSPluginItem

class EDTestCaseEDConfiguration(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDConfiguration")
        strKernelDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDConfiguration"
        self.strDataPath = EDUtilsPath.mergePath(strKernelDataHome, strDataDir)
        self.strEdnaSiteOrig = EDUtilsPath.getEdnaSite()
        

    def preProcess(self):
        """Set EDNA_SITE to TestSite for these tests"""
        EDUtilsPath.setEdnaSite("TestSite") 


    def testAddConfigFile(self):
        # Tests adding a config file
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        # Load the config file again, this time the cache should be used
        edConfiguration.addConfigurationFile(strPath)

    
    def testGetXSConfigurationItem1(self):
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        xsDataPluginItem = edConfiguration.getXSConfigurationItem("indexingMosflm")
        EDAssert.equal(True, xsDataPluginItem is not None, "Obtanied configuration for indexingMosflm")

    def testGetXSConfigurationItem2(self):
        edConfiguration = EDConfiguration()
        xsDataPluginItem1 = edConfiguration.getXSConfigurationItem("EDPluginTestPluginFactory")
        EDAssert.equal(True, xsDataPluginItem1 is not None, "Obtanied configuration for EDPluginTestPluginFactory")
        xsDataPluginItem2 = edConfiguration.getXSConfigurationItem("EDPluginTestPluginFactoryImport1")
        EDAssert.equal(True, xsDataPluginItem2 is not None, "Obtanied imported configuration for EDPluginTestPluginFactoryImport1")
        xsDataPluginItem3 = edConfiguration.getXSConfigurationItem("EDPluginTestPluginFactoryImport2")
        EDAssert.equal(True, xsDataPluginItem3 is not None, "Obtanied imported configuration for EDPluginTestPluginFactoryImport2")
        
        
    def testSetXSConfigurationItem(self):
        xsPluginItem = XSPluginItem()
        xsPluginItem.name = "EDPluginTestSetConfig"
        edConfiguration = EDConfiguration()
        edConfiguration.setXSConfigurationItem(xsPluginItem)
        xsDataPluginItem = edConfiguration.getXSConfigurationItem("EDPluginTestSetConfig")
        EDAssert.equal(True, xsDataPluginItem is not None, "Obtanied set configuration")


    def testGetPathToProjectConfigurationFile(self):
        edConfiguration = EDConfiguration()
        strPathToConfigurationFile1 = edConfiguration.getPathToProjectConfigurationFile("EDPluginTestPluginFactory")
        strPathToConfigurationFileReference1 = EDUtilsPath.appendListOfPaths(EDUtilsPath.getEdnaHome(),
                                                                                  [ "kernel", "tests", "data", "EDFactoryPlugin", \
                                                                                   "testProject", "conf", "XSConfiguration_TestSite.xml" ])
        EDAssert.equal(strPathToConfigurationFileReference1, strPathToConfigurationFile1)
        EDUtilsPath.setEdnaSite("NonexistingTestSite")
        strPathToConfigurationFile2 = edConfiguration.getPathToProjectConfigurationFile("EDPluginTestPluginFactory")
        strPathToConfigurationFileReference2 = None
        EDAssert.equal(strPathToConfigurationFileReference2, strPathToConfigurationFile2)


    def testStaticEDConfiguration(self):
        # This test make sure that changing an instatiation of EDConfiguration does not change the
        # corresponding plugin configuration for EDConfigurationStatic
        strPathToTestConfigFile = os.path.join(self.strDataPath, "XSConfiguration_testNonStatic.xml")
        edConfiguration = EDConfiguration(strPathToTestConfigFile)
        strParam1 = edConfiguration.getStringValue("EDPluginTestPluginFactory", "testItemName")
        EDUtilsPath.setEdnaSite("TestStaticConfiguration") 
        strParam2 = EDConfigurationStatic.getStringValue("EDPluginTestPluginFactory", "testItemName")
        EDAssert.equal(False, strParam1 == strParam2, "Static config is not equal to local config")
        

    def finallyProcess(self):
        """Restores EDNA_SITE"""
        EDUtilsPath.setEdnaSite(self.strEdnaSiteOrig) 

         

    def testGetPluginListSize(self):
        """
        Testing the retrieved XSPluginList size from configuration
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        iPluginListSize = edConfiguration.getPluginListSize()
        EDAssert.equal(1, iPluginListSize)


    def testGetPluginItem(self):
        """
        Testing Plugin indexingMosflm Configuration
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        xsPluginItem = edConfiguration.getXSConfigurationItem("indexingMosflm")
        EDAssert.equal("indexingMosflm", xsPluginItem.getName())

        paramList = xsPluginItem.getXSParamList()
        paramItems = paramList.getXSParamItem()

        EDAssert.equal("workingDir", paramItems[0].getName())
        EDAssert.equal("/path/to/working/dir", paramItems[0].getValue())
        EDAssert.equal("number", paramItems[1].getName())
        EDAssert.equal("3", paramItems[1].getValue())


    def testGetPluginItemError(self):
        """
        Testing the retrieval of an absent plugin
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        xsPluginItem = edConfiguration.getXSConfigurationItem("toto")
        EDAssert.equal(None, xsPluginItem, "Non-existing configuration item should be None")


    def testGetParamItem(self):
        """
        Testing the XSParamItem inside an XSPluginItem
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        strValue = edConfiguration.getStringValue("indexingMosflm", "workingDir")
        EDAssert.equal("/path/to/working/dir", strValue)


    def testGetParamValue(self):
        """
        Testing the XSParamItem Value convertion from string to different formats
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        xsPluginItem = edConfiguration.getXSConfigurationItem("indexingMosflm")
        EDAssert.equal("/path/to/working/dir", edConfiguration.getStringParamValue(xsPluginItem, "workingDir"))
        EDAssert.equal("/path/to/working/dir", EDConfiguration.getStringParamValue(xsPluginItem, "workingDir"))
        EDAssert.equal(3, edConfiguration.getIntegerParamValue(xsPluginItem, "number"))
        EDAssert.equal(3, EDConfiguration.getIntegerParamValue(xsPluginItem, "number"))


    def process(self):
        self.addTestMethod(self.testAddConfigFile)
        self.addTestMethod(self.testGetXSConfigurationItem1)
        self.addTestMethod(self.testGetXSConfigurationItem2)
        self.addTestMethod(self.testSetXSConfigurationItem)
        self.addTestMethod(self.testGetPathToProjectConfigurationFile)
        self.addTestMethod(self.testStaticEDConfiguration)
        self.addTestMethod(self.testGetPluginListSize)
        self.addTestMethod(self.testGetPluginItem)
        self.addTestMethod(self.testGetPluginItemError)
        self.addTestMethod(self.testGetParamItem)
        self.addTestMethod(self.testGetParamValue)


if __name__ == '__main__':

    edTestCaseEDConfiguration = EDTestCaseEDConfiguration("EDTestCaseEDConfiguration")
    edTestCaseEDConfiguration.execute()

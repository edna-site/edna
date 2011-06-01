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

"""
This is the test case for the EDConfiguration class.
"""

import os

from EDAssert                import EDAssert
from EDConfiguration         import EDConfiguration
from EDUtilsTest             import EDUtilsTest
from EDUtilsPath             import EDUtilsPath
from EDTestCase              import EDTestCase


class EDTestCaseEDConfiguration(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDConfiguration")
        self.__edConfiguration = None
        strKernelDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDConfiguration"
        self.___strDataPath = EDUtilsPath.mergePath(strKernelDataHome, strDataDir)


    def preProcess(self):
        """
        Constructs the utilitary EDConfiguration class
        """
        #Loads py module directly using xml configuration file
        self.___edConfiguration = EDConfiguration(os.path.join(self.___strDataPath, "XSConfiguration.xml"))
        self.___edConfiguration.load()


    def testGetPluginList(self):
        """
        Testing the retrieved XSPluginList from configuration
        """
        edPluginList = self.___edConfiguration.getPluginList()
        EDAssert.equal(2, self.___edConfiguration.getPluginListSize())


    def testGetPluginItem(self):
        """
        Testing Plugin indexingMosflm Configuration
        """
        xsPluginItem = self.___edConfiguration.getPluginItem("indexingMosflm")
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
        EDAssert.equal(None, self.___edConfiguration.getPluginItem("toto"))


    def testGetParamItem(self):
        """
        Testing the XSParamItem inside an XSPluginItem
        """
        xsPluginItem = self.___edConfiguration.getPluginItem("indexingMosflm")
        xsParamItem = self.___edConfiguration.getParamItem(xsPluginItem, "workingDir")
        EDAssert.equal("workingDir", xsParamItem.getName())


    def testGetParamValue(self):
        """
        Testing the XSParamItem Value convertion from string to different formats
        """
        xsPluginItem = self.___edConfiguration.getPluginItem("indexingMosflm")
        EDAssert.equal("/path/to/working/dir", self.___edConfiguration.getStringParamValue(xsPluginItem, "workingDir"))
        EDAssert.equal("/path/to/working/dir", EDConfiguration.getStringParamValue(xsPluginItem, "workingDir"))
        EDAssert.equal(3, self.___edConfiguration.getIntegerParamValue(xsPluginItem, "number"))
        EDAssert.equal(3, EDConfiguration.getIntegerParamValue(xsPluginItem, "number"))


    def testGetOptionItem(self):
        """
        Testing the XSOptionItem inside an XSPluginItem
        """
        xsPluginItem = self.___edConfiguration.getPluginItem("indexing")
        xsOptionItemMosflm = self.___edConfiguration.getOptionItem(xsPluginItem, "indexingMosflm")
        EDAssert.equal(True, xsOptionItemMosflm.getEnabled())

        xsOptionItemXds = self.___edConfiguration.getOptionItem(xsPluginItem, "indexingXds")
        EDAssert.equal(False, xsOptionItemXds.getEnabled())

        xsOptionItemLabelit = self.___edConfiguration.getOptionItem(xsPluginItem, "indexingLabelit")
        EDAssert.equal(False, xsOptionItemLabelit.getEnabled())


    def process(self):
        self.addTestMethod(self.testGetPluginList)
        self.addTestMethod(self.testGetPluginItem)
        self.addTestMethod(self.testGetPluginItemError)
        self.addTestMethod(self.testGetParamItem)
        self.addTestMethod(self.testGetParamValue)
        self.addTestMethod(self.testGetOptionItem)


if __name__ == '__main__':

    edTestCaseEDConfiguration = EDTestCaseEDConfiguration("EDTestCaseEDConfiguration")
    edTestCaseEDConfiguration.execute()

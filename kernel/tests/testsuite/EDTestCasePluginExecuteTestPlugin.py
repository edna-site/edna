#
#    Project: the EDNA kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

__author__ = ["Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath




class EDTestCasePluginExecuteTestPlugin(EDTestCasePluginExecute):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginTestPluginFactory")
        strModuleLocation = EDUtilsTest.getFactoryPluginTest().getModuleLocation("EDPluginTestPluginFactory")
        strRootDirectory = EDUtilsPath.appendListOfPaths(strModuleLocation, [ "..", "tests", "data" ])
        # Default input
        self.setDataInputFile(os.path.join(strRootDirectory, "XSDataInputString_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(strRootDirectory, "XSDataResultString_reference.xml"))
        # Named input
        self.setDataInputFile(os.path.join(strRootDirectory, "XSDataInputString_reference.xml"), "value1")
        self.setReferenceDataOutputFile(os.path.join(strRootDirectory, "XSDataResultString_reference.xml"), "value1")
        # List input
        self.setDataInputFile(os.path.join(strRootDirectory, "XSDataInputString_reference.xml"), "value2")
        self.setDataInputFile(os.path.join(strRootDirectory, "XSDataInputString_reference.xml"), "value2")
        self.setDataInputFile(os.path.join(strRootDirectory, "XSDataInputString_reference.xml"), "value2")
        self.setReferenceDataOutputFile(os.path.join(strRootDirectory, "XSDataResultString_reference.xml"), "value2")
        self.setReferenceDataOutputFile(os.path.join(strRootDirectory, "XSDataResultString_reference.xml"), "value2")
        self.setReferenceDataOutputFile(os.path.join(strRootDirectory, "XSDataResultString_reference.xml"), "value2")




    def testExecute(self):
        self.run()





    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edTestCasePluginExecuteTestPlugin = EDTestCasePluginExecuteTestPlugin("EDTestCasePluginExecuteTestPlugin")
    edTestCasePluginExecuteTestPlugin.execute()

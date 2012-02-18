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


from __future__ import with_statement
__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDAssert   import EDAssert
from EDPlugin   import EDPlugin
from EDTestCase import EDTestCase

from XSDataCommon import XSDataString
from XSDataCommon import XSDataResult



class EDTestCaseEDPlugin(EDTestCase):
    """
    This is the test case for the plugin base class EDPlugin.
    """

    def testSetDataInput(self):
        """
        Test the setDataInput method with different inputs
        """
        # Test 1: default input with XML
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString)
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest.marshal())
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataInput().marshal(), "Test 1: default input with XML")
        # Test 2: default input with object
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString)
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest)
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataInput().marshal(), "Test 2: default input with object")
        # Test 3: named input with XML
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest.marshal(), "testData")
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataInput("testData")[0].marshal(), "Test 3: named input with XML")
        # Test 4: named input with object
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest, "testData")
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataInput("testData")[0].marshal(), "Test 4: named input with object")
        # Test 4: several inputs with the same name, XML input
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest1 = XSDataString("Test1")
        xsDataStringTest2 = XSDataString("Test2")
        edPlugin.setDataInput(xsDataStringTest1.marshal(), "testData")
        edPlugin.setDataInput(xsDataStringTest2.marshal(), "testData")
        pyListDataInput = edPlugin.getDataInput("testData")
        EDAssert.equal(xsDataStringTest1.marshal(), pyListDataInput[0].marshal(), "Test 4: several inputs with the same name, XML input, 1")
        EDAssert.equal(xsDataStringTest2.marshal(), pyListDataInput[1].marshal(), "Test 4: several inputs with the same name, XML input, 2")
        # Test 5: several inputs with the same name, object input
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest1 = XSDataString("Test1")
        xsDataStringTest2 = XSDataString("Test2")
        edPlugin.setDataInput(xsDataStringTest1, "testData")
        edPlugin.setDataInput(xsDataStringTest2, "testData")
        pyListDataInput = edPlugin.getDataInput("testData")
        EDAssert.equal(xsDataStringTest1.marshal(), pyListDataInput[0].marshal(), "Test 5: several inputs with the same name, object input, 1")
        EDAssert.equal(xsDataStringTest2.marshal(), pyListDataInput[1].marshal(), "Test 5: several inputs with the same name, object input, 2")
        # Test 6: test of delDataInput
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString)
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest.marshal())
        edPlugin.delDataInput()
        EDAssert.equal(None, edPlugin.getDataInput(), "Test 6: test of delDataInput")


    def testSetDataOutput(self):
        """
        Test the setDataOutput method with different arguments
        """
        # Test 1: default output
        edPlugin = EDPlugin()
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataOutput(xsDataStringTest)
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataOutput().marshal(), "Test 1: default output")
        # Test 2: named output
        edPlugin = EDPlugin()
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataOutput(xsDataStringTest, "testData")
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.getDataOutput("testData")[0].marshal(), "Test 2: named output")
        # Test 3: several inputs with the same name
        edPlugin = EDPlugin()
        xsDataStringTest1 = XSDataString("Test1")
        xsDataStringTest2 = XSDataString("Test2")
        edPlugin.setDataOutput(xsDataStringTest1, "testData")
        edPlugin.setDataOutput(xsDataStringTest2, "testData")
        pyListDataOutput = edPlugin.getDataOutput("testData")
        EDAssert.equal(xsDataStringTest1.marshal(), pyListDataOutput[0].marshal(), "Test 3: several inputs with the same name, 1")
        EDAssert.equal(xsDataStringTest2.marshal(), pyListDataOutput[1].marshal(), "Test 3: several inputs with the same name, 2")
        # Test 6: test of delDataOutput
        edPlugin = EDPlugin()
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataOutput(xsDataStringTest.marshal())
        edPlugin.delDataOutput()
        EDAssert.equal(None, edPlugin.getDataOutput(), "Test 6: test of delDataOutput")


    def testWriteDataInput(self):
        # Test 1: default input with XML
        edPlugin = EDPlugin()
        edPlugin.configure()
        edPlugin.setXSDataInputClass(XSDataString)
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest.marshal())
        edPlugin.writeDataInput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_dataInput.xml")), "Test 1: default input with XML")
        # Test 2: named input with XML
        edPlugin = EDPlugin()
        edPlugin.configure()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataInput(xsDataStringTest.marshal(), "testData")
        edPlugin.writeDataInput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_0_dataInput.xml")), "Test 2: named input with XML")
        # Test 3: several inputs with the same name, XML input
        edPlugin = EDPlugin()
        edPlugin.configure()
        edPlugin.setXSDataInputClass(XSDataString, "testData")
        xsDataStringTest1 = XSDataString("Test1")
        xsDataStringTest2 = XSDataString("Test2")
        edPlugin.setDataInput(xsDataStringTest1.marshal(), "testData")
        edPlugin.setDataInput(xsDataStringTest2.marshal(), "testData")
        edPlugin.writeDataInput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_0_dataInput.xml")), "Test 3: several inputs with the same name, XML input, 1")
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_1_dataInput.xml")), "Test 3: several inputs with the same name, XML input, 2")


    def testWriteDataOutput(self):
        # Test 1: default Output with XML
        edPlugin = EDPlugin()
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataOutput(xsDataStringTest)
        edPlugin.writeDataOutput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_dataOutput.xml")), "Test 1: default Output with XML")
        # Test 2: named Output with XML
        edPlugin = EDPlugin()
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test")
        edPlugin.setDataOutput(xsDataStringTest, "testData")
        edPlugin.writeDataOutput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_0_dataOutput.xml")), "Test 2: named Output with XML")
        # Test 3: several Outputs with the same name, XML Output
        edPlugin = EDPlugin()
        edPlugin.configure()
        xsDataStringTest1 = XSDataString("Test1")
        xsDataStringTest2 = XSDataString("Test2")
        edPlugin.setDataOutput(xsDataStringTest1, "testData")
        edPlugin.setDataOutput(xsDataStringTest2, "testData")
        edPlugin.writeDataOutput()
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_0_dataOutput.xml")), "Test 3: several Outputs with the same name, XML Output, 1")
        EDAssert.equal(True, os.path.exists(os.path.join(edPlugin.getWorkingDirectory(), "_testData_1_dataOutput.xml")), "Test 3: several Outputs with the same name, XML Output, 2")


    def testDataInputOutputProperties(self):
        # Test dataInput property with XSDataObject
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString)
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test1")
        edPlugin.dataInput = xsDataStringTest
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.dataInput.marshal(), "Test dataInput property with XSDataObject")
        # Test dataInput property with XML
        edPlugin = EDPlugin()
        edPlugin.setXSDataInputClass(XSDataString)
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test1")
        edPlugin.dataInput = xsDataStringTest.marshal()
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.dataInput.marshal(), "Test dataInput property with XML")
        # Test dataOutput property with XSDataObject
        edPlugin = EDPlugin()
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test1")
        edPlugin.dataOutput = xsDataStringTest
        EDAssert.equal(xsDataStringTest.marshal(), edPlugin.dataOutput.marshal(), "Test dataOutput property with XSDataObject")


    def testWarningIfNoOutputData(self):
        # Test warning in case of no output data
        edPlugin = EDPlugin()
        edPlugin.configure()
        edPlugin.executeSynchronous()
        xsDataResultReference = XSDataResult()
        listOfWarningMessages = edPlugin.getListOfWarningMessages()
        EDAssert.equal(1, len(listOfWarningMessages), "Test warning in case of no output data, no warning messages = 1")
        EDAssert.equal(xsDataResultReference.marshal(), edPlugin.dataOutput.marshal(), "Test warning in case of no output data, default XSDataResult")
        # Test warning in case of named output data
        edPlugin = EDPlugin()
        edPlugin.configure()
        xsDataStringTest = XSDataString("Test1")
        edPlugin.setDataOutput(xsDataStringTest, "test")
        edPlugin.executeSynchronous()
        xsDataResultReference = XSDataResult()
        listOfWarningMessages = edPlugin.getListOfWarningMessages()
        EDAssert.equal(0, len(listOfWarningMessages), "Test warning in case of named output data, no warning messages = 0")


    def testCreateBaseName(self):
        # Test 1 : naming of working directory
        edPlugin = EDPlugin()
        edPlugin.setBaseName("EDPlugin_testCreateBaseName")
        edPlugin.configure()
        strWorkingDir = edPlugin.getWorkingDirectory()
        EDAssert.equal(True, os.path.exists(strWorkingDir), "Test 1 : naming of working directory")


    def testWithSingleThread(self):
        edPlugin = EDPlugin()
        with edPlugin.locked():
            edPlugin.screen("test of with singleThread")


    def process(self):
        """
        """
        self.addTestMethod(self.testSetDataInput)
        self.addTestMethod(self.testSetDataOutput)
        self.addTestMethod(self.testWriteDataInput)
        self.addTestMethod(self.testWriteDataOutput)
        self.addTestMethod(self.testDataInputOutputProperties)
        self.addTestMethod(self.testWarningIfNoOutputData)
        self.addTestMethod(self.testCreateBaseName)
        self.addTestMethod(self.testWithSingleThread)




if __name__ == '__main__':

    EDTestCaseEDPlugin = EDTestCaseEDPlugin("TestCase EDPluginExecProcessScript")
    EDTestCaseEDPlugin.execute()

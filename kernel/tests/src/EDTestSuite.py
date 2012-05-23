# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (Jerome.kieffer@esrf.fr)
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

"""
EDNA test suite module ...

a TestSuite is a sequence of EDTestCase and/or EDTestSuite

"""

__authors__ = "Marie-Francoise Incardona, Olof Svensson, Jerome Kieffer"
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"

from EDVerbose          import EDVerbose
from EDTest             import EDTest
from EDUtilsTest        import EDUtilsTest


class EDTestSuite(EDTest):
    """
    A test suite can contain a list of test cases and/or other test suites.
    At the end of the execution of a test suite a summary is written containing:
    - The number of test suites in the test suite(if any)
    - If there are test suites not executed a list of these
    - The total number of test cases not executed due to e.g. missing configuration file and a list of these
    - The total number of test cases ending with success
    - The total number of test cases ending with failure
    - If there are test methods ending with failure a list of the test cases, test methods and the failures.
    - The total number of test methods ending with success
    - The total number of test methods ending with failure
    """


    def __init__(self, _strTestSuiteName=None):
        EDTest.__init__(self, _strTestSuiteName)
        self.__listTestCase = []
        self.__listTestSuite = []
        self.__bTopLevel = True
        self.__iNumberTestSuite = 0
        self.__iNumberTestMethodSuccess = 0
        self.__iNumberTestMethodFailure = 0
        self.__iNumberTestCaseSuccess = 0
        self.__iNumberTestCaseFailure = 0
        self.__dictTestCaseFailureMessages = {}
        self.__dictTestCaseNotExecuted = {}
        self.__dictTestSuiteNotExecuted = {}


    def addTestCaseFromName(self, _strTestCaseName):
        """
        This method adds a test case give it's name to the test suite. If the test case
        cannot be loaded an error message is issued and it's name is added to the list of not
        executed test cases.
        @return: NumberTestCaseFailure
        @rtype: integer 
        """
        edTestCase = None
        exceptionObject = None
        try:
            edTestCase = EDUtilsTest.getFactoryPluginTest().loadPlugin(_strTestCaseName)
        except ImportError, exceptionObject:
            strWarningMessage = "Could not create the test case: %s, reason: %s" % (_strTestCaseName, exceptionObject)
            EDVerbose.WARNING(strWarningMessage)
            self.__dictTestCaseNotExecuted[_strTestCaseName] = "%s : %s" % (self.getClassName(), strWarningMessage)
        if edTestCase is None:
            if exceptionObject is None:
                EDVerbose.error("EDTestSuite.addTestCaseFromName: Could not create the test case: " + _strTestCaseName)
                self.__dictTestCaseNotExecuted[_strTestCaseName] = "%s : Could not create the test case" % self.getClassName()
        else:
            edTestCase.setTestSuiteName(self.getClassName())
            self.__listTestCase.append(edTestCase)


    def addTestSuiteFromName(self, _strTestSuiteName):
        """
        This method adds a test suite give it's name to the test suite. If the test case
        cannot be loaded an error message is issued and it's name is added to the list of not
        executed test suites.
        @return: NumberTestCaseFailure
        @rtype: integer 
        """
        edTestSuite = None
        exceptionObject = None
        try:
            edTestSuite = EDUtilsTest.getFactoryPluginTest().loadPlugin(_strTestSuiteName)
        except ImportError, exceptionObject:
            strWarningMessage = "Could not create the test suite: %s, reason: %s" % (_strTestSuiteName, exceptionObject)
            EDVerbose.WARNING(strWarningMessage)
            self.__dictTestCaseNotExecuted[_strTestSuiteName] = "%s : %s" % (self.getClassName(), strWarningMessage)
        if edTestSuite is None:
            if exceptionObject is None:
                EDVerbose.error("EDTestSuitePluginUnit.addTestSuiteFromName: Could not create test suite: " + _strTestSuiteName)
                self.__dictTestSuiteNotExecuted[_strTestSuiteName] = "%s : Could not create the test suite" % self.getClassName()
        else:
            self.__listTestSuite.append(edTestSuite)



    def processKernel(self):
        """
        This method executes the test suite.
        """
        EDVerbose.DEBUG("Execution: EDTestSuite.processKernel()")
        EDVerbose.screen("")
        EDVerbose.screen("")
        EDVerbose.unitTest("###################################################################")
        EDVerbose.unitTest("STARTING::" + self.getTestName())
        EDVerbose.unitTest("###################################################################")
        self.setTimeInit()
        for edTestCase in self.__listTestCase:
            edTestCase.execute()
            if edTestCase.isExecuted():
                self.__iNumberTestMethodSuccess += edTestCase.getNumberTestMethodSuccess()
                if edTestCase.getNumberTestMethodFailure() == 0:
                    self.__iNumberTestCaseSuccess += 1
                else:
                    self.__iNumberTestCaseFailure += 1
                    self.__iNumberTestMethodFailure += edTestCase.getNumberTestMethodFailure()
                    self.__dictTestCaseFailureMessages[edTestCase.getClassName()] = edTestCase.getMethodFailureMessages()
            else:
                self.__dictTestCaseNotExecuted[edTestCase.getClassName()] = edTestCase.getReasonForNotBeingExectuted()
            EDVerbose.screen()
        for edTestSuite in self.__listTestSuite:
            edTestSuite.execute()
            self.__iNumberTestSuite += 1
            self.__iNumberTestMethodSuccess += edTestSuite.getNumberTestMethodSuccess()
            self.__iNumberTestMethodFailure += edTestSuite.getNumberTestMethodFailure()
            self.__iNumberTestCaseSuccess += edTestSuite.getNumberTestCaseSuccess()
            self.__iNumberTestCaseFailure += edTestSuite.getNumberTestCaseFailure()
            self.extendDictionary(self.__dictTestCaseNotExecuted, edTestSuite.getDictTestCaseNotExecuted())
            self.extendDictionary(self.__dictTestSuiteNotExecuted, edTestSuite.getDictTestSuiteNotExecuted())
            self.extendDictionary(self.__dictTestCaseFailureMessages, edTestSuite.getDictTestCaseFailureMessages())
        self.setTimeEnd()



    def postProcess(self):
        """
        This method writes out the results of the test suite.
        """
        EDVerbose.screen()
        EDVerbose.screen()
        EDVerbose.unitTest("###################################################################")
        strResult = None
        if self.__iNumberTestCaseFailure == 0 and self.__iNumberTestMethodFailure == 0:
            strResult = "SUCCESS"
        else:
            strResult = "FAILURE"
        EDVerbose.unitTest("Result for %s : %s" % (self.getTestName(), strResult))
        EDVerbose.unitTest()
        if self.__iNumberTestSuite > 0:
            EDVerbose.unitTest(" Number of executed test suites in this test suite : %d" % self.__iNumberTestSuite)
            EDVerbose.unitTest()
        if self.__dictTestSuiteNotExecuted != {}:
            EDVerbose.unitTest()
            EDVerbose.unitTest("OBS! The following test suites were not executed due to errors:")
            EDVerbose.unitTest()
            for strTestSuiteName in self.__dictTestSuiteNotExecuted.keys():
                EDVerbose.unitTest("  %s : %s" % (self.__dictTestSuiteNotExecuted[strTestSuiteName], strTestSuiteName))
            EDVerbose.unitTest()
        if self.__dictTestCaseNotExecuted != {}:
            EDVerbose.unitTest()
            EDVerbose.unitTest("OBS! The following test cases not executed due to errors:")
            EDVerbose.unitTest()
            for strTestCaseName in self.__dictTestCaseNotExecuted.keys():
                EDVerbose.unitTest("  %s :" % strTestCaseName)
                EDVerbose.unitTest("      %s" % self.__dictTestCaseNotExecuted[strTestCaseName])
                EDVerbose.unitTest()
            EDVerbose.unitTest("           Total number of test cases NOT EXECUTED : %d" % len(self.__dictTestCaseNotExecuted))
        EDVerbose.unitTest()
        if self.__iNumberTestCaseSuccess != 0 or self.__iNumberTestCaseFailure != 0:
            EDVerbose.unitTest("  Total number of test cases executed with SUCCESS : %d" % self.__iNumberTestCaseSuccess)
            EDVerbose.unitTest("  Total number of test cases executed with FAILURE : %d" % self.__iNumberTestCaseFailure)
            EDVerbose.unitTest()
        if self.__dictTestCaseFailureMessages != {}:
            EDVerbose.unitTest("")
            EDVerbose.unitTest("OBS! The following test methods ended with failure:")
            EDVerbose.unitTest("")
            for strTestCaseName in self.__dictTestCaseFailureMessages.keys():
                EDVerbose.unitTest("  %s :" % strTestCaseName)
                for strMethodName in self.__dictTestCaseFailureMessages[strTestCaseName].keys():
                    EDVerbose.unitTest("    %s :" % strMethodName.split(".")[1])
                    EDVerbose.unitTest("       %s" % self.__dictTestCaseFailureMessages[strTestCaseName][strMethodName])
                EDVerbose.unitTest("")
            EDVerbose.unitTest("")
        if self.__iNumberTestMethodSuccess != 0 or self.__iNumberTestMethodFailure != 0:
            EDVerbose.unitTest("Total number of test methods executed with SUCCESS : %d" % self.__iNumberTestMethodSuccess)
            EDVerbose.unitTest("Total number of test methods executed with FAILURE : %d" % self.__iNumberTestMethodFailure)
        EDVerbose.unitTest()
        EDVerbose.unitTest("                                           Runtime : %.3f [s]" % self.getRunTime())
        EDVerbose.unitTest("###################################################################")


    def extendDictionary(self, _dictBase, _dictExtend):
        """
        Helper function for "extending" a dictionary. Example:
        >>> a={"a":1, "b": 2}
        >>> b={"c":3, "d": 4}
        >>> extendDictionary(a,b)
        >>>a
        {"a":1, "b": 2, "c":3, "d": 4}
        
        @param _dictBase: The dictionary to be extended
        @type _dictBase: dict
        
        @param _dictExtend: The dictionary that will extend _dictBase
        @type _dictExtend: dict 
        """
        for key in _dictExtend.keys():
            _dictBase[key] = _dictExtend[key]


    def getNumberTestCaseFailure(self):
        """
        Total number of test cases ended with failure.
        @return: NumberTestCaseFailure
        @rtype: integer 
        """
        return self.__iNumberTestCaseFailure


    def getNumberTestCaseSuccess(self):
        """
        Total number of test cases ended with success.
        @return: NumberTestCaseSuccess
        @rtype: integer 
        """
        return self.__iNumberTestCaseSuccess


    def getNumberTestMethodFailure(self):
        """
        Total number of test methods ending with failure.
        @return: NumberTestMethodFailure
        @rtype: integer 
        """
        return self.__iNumberTestMethodFailure


    def getNumberTestMethodSuccess(self):
        """
        Total number of test methods ending with success.
        @return: NumberTestMethodSuccess
        @rtype: integer 
        """
        return self.__iNumberTestMethodSuccess



    def getDictTestCaseFailureMessages(self):
        """
        Returns a dictionary containing:
            Key   : Test case name with failed test method(s)
            Value : Dictionary with method names (keys) and error messages (values).
        @return: TestCaseFailureMessages
        @rtype: dict
        """
        return self.__dictTestCaseFailureMessages


    def getDictTestCaseNotExecuted(self):
        """
        Returns a dictionary containing:
            Key   : Test case name
            Value : Description of why the test case was not executed
        @return: TestCaseNotExecuted
        @rtype: dict
        """
        return self.__dictTestCaseNotExecuted


    def getDictTestSuiteNotExecuted(self):
        """
        Returns a dictionary containing:
            Key   : Test suite name
            Value : Description of why the test suite was not executed
        @return: TestCaseNotExecuted
        @rtype: list
        """
        return self.__dictTestSuiteNotExecuted



# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (jerome.kieffer@esrf.fr)
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
EDNA test Case module ...

a TestCase is a single test, either an unit test or an execution test.
"""

__authors__ = "Marie-Francoise Incardona, Olof Svensson, Jerome Kieffer"
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"

from EDTest            import EDTest
from EDVerbose         import EDVerbose
from EDUtilsTest       import EDUtilsTest
from EDUtilsPath       import EDUtilsPath


class EDTestCase(EDTest):
    """
    Test case class
    """

    def __init__(self, _strTestName=None):
        EDTest.__init__(self, _strTestName)
        self.__strTestSuiteName = None
        self.__strTestsHome = None
        self.__strTestsDataHome = None
        self.__strTestsDataImagesHome = None
        self.__strReasonForNotBeingExecuted = ""
        self.__bIsExecuted = False
        self.__iNumberTestMethodSuccess = 0
        self.__iNumberTestMethodFailure = 0
        self.__dictMethodFailureMessages = {}


    def processKernel(self):
        """
        Executes the test case.
        """
        EDVerbose.DEBUG("EDTestCase.processKernel")
        EDVerbose.screen()
        EDVerbose.unitTest("===================================================================")
        if self.getTestSuiteName() is not None:
            EDVerbose.unitTest("TEST SUITE : %s" % self.getTestSuiteName())
        EDVerbose.unitTest("TEST CASE  : %s" % self.getClassName())
        EDVerbose.unitTest(" ")
        if self.__strReasonForNotBeingExecuted == "":
            self.setTimeInit()
            iNumberMethods = self.getNumberOfTests()
            EDVerbose.unitTest("Total number of tests : %d" % iNumberMethods)
            EDVerbose.unitTest()
            iTestCaseNumber = 0
            if self.getListTest() == []:
                self.__strReasonForNotBeingExecuted = "No test methods!"
            else:
                for pyTestMethod in self.getListTest():
                    iTestCaseNumber = iTestCaseNumber + 1
                    strMethodName = EDUtilsTest.patchMethodName(pyTestMethod)
                    EDVerbose.unitTest("-------------------------------------------------------------------")
                    EDVerbose.unitTest("Test case method : %s" % strMethodName)
                    EDVerbose.unitTest()
                    try:
                        pyTestMethod()
                        self.__iNumberTestMethodSuccess += 1
                        EDVerbose.unitTest("%s executed with SUCCESS" % strMethodName)
                        EDVerbose.unitTest()

                    except AssertionError, pyException:
                        self.__dictMethodFailureMessages[strMethodName] = str(pyException)
                        self.__iNumberTestMethodFailure += 1
                        EDVerbose.unitTest("Assertion Error Raised!")
                        EDVerbose.unitTest("%s executed with FAILURE" % strMethodName)
                        EDVerbose.unitTest()

                    except Exception, pyException:
                        self.__dictMethodFailureMessages[strMethodName] = str(pyException)
                        self.__iNumberTestMethodFailure += 1
                        EDVerbose.unitTest("Unexpected Error!")
                        EDVerbose.unitTest("%s executed with FAILURE" % strMethodName)
                        EDVerbose.unitTest()
                        EDVerbose.writeErrorTrace()
                        EDVerbose.unitTest()
                self.__bIsExecuted = True
                self.setTimeEnd()



    def postProcess(self):
        """
        Writes out a summary of the test case.
        """
        if self.__bIsExecuted:
            EDVerbose.unitTest("-------------------------------------------------------------------")
            EDVerbose.unitTest("Result for %s" % self.getClassName())
            EDVerbose.unitTest()
            EDVerbose.unitTest("Total number of test methods     : %d" % self.getNumberOfTests())
            EDVerbose.unitTest("Number of SUCCESS                : %d" % self.__iNumberTestMethodSuccess)
            EDVerbose.unitTest("Number of FAILURE                : %d" % self.__iNumberTestMethodFailure)
            if self.__dictMethodFailureMessages != {}:
                EDVerbose.unitTest("")
                EDVerbose.unitTest("List of test methods ending with failure:")
                for strMethodName in self.__dictMethodFailureMessages:
                    EDVerbose.unitTest("  %s :" % strMethodName.split(".")[1])
                    EDVerbose.unitTest("     %s" % self.__dictMethodFailureMessages[strMethodName])
            EDVerbose.unitTest()
            EDVerbose.unitTest("Runtime                          : %.3f [s]" % self.getRunTime())
            EDVerbose.unitTest("===================================================================")
        else:
            EDVerbose.unitTest()
            EDVerbose.unitTest("Test case %s not executed :" % self.getClassName())
            EDVerbose.unitTest(self.__strReasonForNotBeingExecuted)
            EDVerbose.unitTest()
            EDVerbose.unitTest("===================================================================")


    def getMethodFailureMessages(self):
        """
        This method returns a dictionary with the failure messages:
          Key   : Name of the test method
          Value : Failure message
        @return: MethodFailureMessages
        @rtype: dict
        """
        return self.__dictMethodFailureMessages


    def setTestSuiteName(self, _strTestSuiteName):
        """
        Used by EDTestSuite: Sets the name of the test suite invoking the test case.
        @param _strTestSuiteName: TestSuiteName
        @type _strTestSuiteName: string
        """
        self.__strTestSuiteName = _strTestSuiteName



    def getTestSuiteName(self):
        """
        Returns the name of the test suite invoking the test case.
        None if not inviked by a test suite.
        @return: TestSuiteName
        @rtype: string
        """
        return self.__strTestSuiteName


    def setReasonForNotBeingExectuted(self, _strValue):
        """
        Sets a string describing why the test case shouldn't be executed.
        For example : missing configuration file.
        If the string is not empty, the test case is not executed.
        @param _strValue: ReasonForNotBeingExecuted
        @type _strValue: string
        """
        self.__strReasonForNotBeingExecuted = _strValue


    def getReasonForNotBeingExectuted(self):
        """
        Returns a string describing why the test case shouldn't be executed.
        For example : missing configuration file.
        If the string is not empty, the test case is not executed.
        @return: ReasonForNotBeingExecuted
        @rtype: string
        """
        return self.__strReasonForNotBeingExecuted


    def getTestsHome(self):
        """
        Returns the Test home directory
        @return: TestsHome
        @rtype: string
        """
        return EDUtilsPath.EDNA_TESTS


    def getTestsDataHome(self):
        """
        Returns the Test data home directory
        @return: TestsDataHome
        @rtype: string
        """
        return EDUtilsPath.EDNA_TESTDATA


    def getTestsDataImagesHome(self):
        """
        Returns the Test data home directory
        @return: TestsDataImagesHome
        @rtype: string
        """
        return EDUtilsPath.EDNA_TESTIMAGES



    def getNumberTestMethodSuccess(self):
        """
        The number of successful test methods.
        @return: NumberTestMethodSuccess
        @rtype: integer
        """
        return self.__iNumberTestMethodSuccess


    def getNumberTestMethodFailure(self):
        """
        The number of test methods executed with failure.
        @return: NumberTestMethodFailure
        @rtype: integer
        """
        return self.__iNumberTestMethodFailure


    def isExecuted(self):
        """
        Returns True if the test case was executed.
        @return: IsExecuted
        @rtype: boolean
        """
        return self.__bIsExecuted

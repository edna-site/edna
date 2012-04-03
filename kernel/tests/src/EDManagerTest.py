#coding: utf8
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
#                       Jérôme Kieffer (kieffer@esrf.fr)
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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

from __future__ import with_statement

__authors__ = [ "Olof Svensson, Jerome Kieffer" ]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"
__doc__ = """
 EDManagerTest stores all information comming from tests 
 Static class for storing all test information / results.
"""

import time

from EDVerbose          import EDVerbose
from EDObject           import EDObject



class EDManagerTest(EDObject):
    """
    Static class for storing all test information / results.
    """
    __listTest = []
    __listTestTotal = []
    __semaphore = EDObject()
    __edTestRunning = None
    __iCumulativeTotalTest = 0
    __iCumulativeTotalTestMethod = 0
    __iCumulativeTotalTestSuccess = 0
    __iCumulativeTotalTestFailure = 0
    __pyStrReport = None


    @classmethod
    def synchronizeOn(cls):
        """
        Locks the EDManagerTest class
        """
        cls.__semaphore.synchronizeOn()


    @classmethod
    def synchronizeOff(cls):
        """
        Unlocks the EDManagerTest class
        """
        cls.__semaphore.synchronizeOff()


    @classmethod
    def create(cls):
        """
        Create
        """
        cls.__iCumulativeTotalTest += cls.getNumberTest()
        cls.__iCumulativeTotalTestMethod += cls.getNumberTestMethod()
        cls.__iCumulativeTotalTestSuccess += cls.getNumberTestSuccess()
        cls.__iCumulativeTotalTestFailure += cls.getNumberTestFailure()
        with cls.__semaphore:
            for edTest in cls.__listTest:
                cls.__listTestTotal.append(edTest)
            del cls.__listTest
            cls.__listTest = []


    @classmethod
    def outputScreen(cls):
        with cls.__semaphore:
            strMessage = ""
            strMessage += "\n  ===============================================================================\n"
            strMessage += "  Final Report\n"
            strMessage += "                            Date: %s\n" % time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime())
            strMessage += "           Total Cumulated Tests: [ %d ]\n" % cls.__iCumulativeTotalTest
            strMessage += "    Total Cumulated Test SUCCESS: [ %d ]\n" % cls.__iCumulativeTotalTestSuccess
            strMessage += "   Total Cumulated Test FAILLURE: [ %d ]\n" % cls.__iCumulativeTotalTestFailure
            strMessage += "    Total Cumulated Test Methods: [ %d ]\n" % cls.__iCumulativeTotalTestMethod
            strMessage += "  -------------------------------------------------------------------------------\n"
            strFailedTests = ""
            for edTest in cls.__listTestTotal:
                strMessage += edTest.outputString()
                if (not edTest.isSuccess()):
                    strFailedTests += edTest.outputString()
            strMessage += "\n  ===============================================================================\n"
            if (strFailedTests != ""):
                strMessage += "  Failed tests:\n"
                strMessage += strFailedTests
            cls.__pyStrReport = strMessage
            EDVerbose.screen(cls.__pyStrReport)
        cls.synchronizeOff()


    @classmethod
    def getNumberTestCumulative(cls):
        return cls.__iCumulativeTotalTest


    @classmethod
    def getNumberTestMethodCumulative(cls):
        return cls.__iCumulativeTotalTestMethod


    @classmethod
    def getNumberTestSuccessCumulative(cls):
        return cls.__iCumulativeTotalTestSuccess


    @classmethod
    def getNumberTestFailureCumulative(cls):
        return cls.__iCumulativeTotalTestFailure


    @classmethod
    def addInformationTest(cls, _edInformationTest):
        with cls.__semaphore:
            cls.__edTestRunning = _edInformationTest
            cls.__listTest.append(_edInformationTest)


    @classmethod
    def addInformationTestMethod(cls, _edInformationTest):
        with cls.__semaphore:
            if (cls.__edTestRunning is not None):
                cls.__edTestRunning.addInformationTest(_edInformationTest)


    @classmethod
    def getNumberTest(cls):
        with cls.__semaphore:
            iNumberTestTotal = len(cls.__listTest)
        return iNumberTestTotal


    @classmethod
    def getNumberTestMethod(cls):
        with cls.__semaphore:
            iNumberTestTotal = 0
            for edTest in cls.__listTest:
                iNumberTestTotal += edTest.getNumberTestMethod()
        return iNumberTestTotal


    @classmethod
    def getNumberTestSuccess(cls):
        with cls.__semaphore:
            iNumberTestTotal = 0
            for edTest in cls.__listTest:
                if (edTest.isSuccess()):
                    iNumberTestTotal += 1
        return iNumberTestTotal


    @classmethod
    def getNumberTestFailure(cls):
        with cls.__semaphore:
            iNumberTestTotal = 0
            for edTest in cls.__listTest:
                if (not edTest.isSuccess()):
                    iNumberTestTotal += 1
        return iNumberTestTotal


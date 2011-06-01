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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

"""
 EDManagerTest stores all information comming from tests 
 Static class for storing all test information / results.
 
"""

__authors__ = [ "Olof Svensson, Jerome Kieffer" ]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import sys, time

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


    @staticmethod
    def synchronizeOn():
        """
        Locks the EDManagerTest class
        """
        EDManagerTest.__semaphore.synchronizeOn()


    @staticmethod
    def synchronizeOff():
        """
        Unlocks the EDManagerTest class
        """

        EDManagerTest.__semaphore.synchronizeOff()


    @staticmethod
    def create():
        """
        Create
        """
        EDManagerTest.__iCumulativeTotalTest += EDManagerTest.getNumberTest()
        EDManagerTest.__iCumulativeTotalTestMethod += EDManagerTest.getNumberTestMethod()
        EDManagerTest.__iCumulativeTotalTestSuccess += EDManagerTest.getNumberTestSuccess()
        EDManagerTest.__iCumulativeTotalTestFailure += EDManagerTest.getNumberTestFailure()
        EDManagerTest.synchronizeOn()
        for edTest in EDManagerTest.__listTest:
            EDManagerTest.__listTestTotal.append(edTest)
        del EDManagerTest.__listTest
        EDManagerTest.__listTest = []
        EDManagerTest.synchronizeOff()


    @staticmethod
    def outputScreen():
        EDManagerTest.synchronizeOn()
        strMessage = ""
        strMessage += "\n  ===============================================================================\n"
        strMessage += "  Final Report\n"
        strMessage += "                            Date: %s\n" % time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime())
        strMessage += "           Total Cumulated Tests: [ %d ]\n" % EDManagerTest.__iCumulativeTotalTest
        strMessage += "    Total Cumulated Test SUCCESS: [ %d ]\n" % EDManagerTest.__iCumulativeTotalTestSuccess
        strMessage += "   Total Cumulated Test FAILLURE: [ %d ]\n" % EDManagerTest.__iCumulativeTotalTestFailure
        strMessage += "    Total Cumulated Test Methods: [ %d ]\n" % EDManagerTest.__iCumulativeTotalTestMethod
        strMessage += "  -------------------------------------------------------------------------------\n"
        strFailedTests = ""
        for edTest in EDManagerTest.__listTestTotal:
            strMessage += edTest.outputString()
            if (not edTest.isSuccess()):
                strFailedTests += edTest.outputString()
        strMessage += "\n  ===============================================================================\n"
        if (strFailedTests != ""):
            strMessage += "  Failed tests:\n"
            strMessage += strFailedTests
        EDManagerTest.__pyStrReport = strMessage
        EDVerbose.screen(EDManagerTest.__pyStrReport)
        EDManagerTest.synchronizeOff()


    @staticmethod
    def getNumberTestCumulative():
        return EDManagerTest.__iCumulativeTotalTest


    @staticmethod
    def getNumberTestMethodCumulative():
        return EDManagerTest.__iCumulativeTotalTestMethod


    @staticmethod
    def getNumberTestSuccessCumulative():
        return EDManagerTest.__iCumulativeTotalTestSuccess


    @staticmethod
    def getNumberTestFailureCumulative():
        return EDManagerTest.__iCumulativeTotalTestFailure


    @staticmethod
    def addInformationTest(_edInformationTest):
        EDManagerTest.synchronizeOn()
        EDManagerTest.__edTestRunning = _edInformationTest
        EDManagerTest.__listTest.append(_edInformationTest)
        EDManagerTest.synchronizeOff()


    @staticmethod
    def addInformationTestMethod(_edInformationTest):
        EDManagerTest.synchronizeOn()
        if (EDManagerTest.__edTestRunning is not None):
            EDManagerTest.__edTestRunning.addInformationTest(_edInformationTest)
        EDManagerTest.synchronizeOff()


    @staticmethod
    def getNumberTest():
        EDManagerTest.synchronizeOn()
        iNumberTestTotal = len(EDManagerTest.__listTest)
        EDManagerTest.synchronizeOff()
        return iNumberTestTotal


    @staticmethod
    def getNumberTestMethod():
        EDManagerTest.synchronizeOn()
        iNumberTestTotal = 0
        for edTest in EDManagerTest.__listTest:
            iNumberTestTotal += edTest.getNumberTestMethod()
        EDManagerTest.synchronizeOff()
        return iNumberTestTotal


    @staticmethod
    def getNumberTestSuccess():
        EDManagerTest.synchronizeOn()
        iNumberTestTotal = 0
        for edTest in EDManagerTest.__listTest:
            if (edTest.isSuccess()):
                iNumberTestTotal += 1
        EDManagerTest.synchronizeOff()
        return iNumberTestTotal


    @staticmethod
    def getNumberTestFailure():
        EDManagerTest.synchronizeOn()
        iNumberTestTotal = 0
        for edTest in EDManagerTest.__listTest:
            if (not edTest.isSuccess()):
                iNumberTestTotal += 1
        EDManagerTest.synchronizeOff()
        return iNumberTestTotal


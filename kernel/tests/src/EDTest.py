# coding: utf8
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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

"""
EDNA Test class, Parent class for all plugin test cases
"""

__authors__ = "Olof Svensson, Jerome Kieffer"
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120212"

from EDObject          import  EDObject
from EDVerbose         import  EDVerbose


class EDTest(EDObject):
    """
    Parent class for plugin test cases
    """
    def __init__(self, _strTestName="Test"):
        EDObject.__init__(self)
        if _strTestName is None:
            self.__strTestName = self.getClassName()
        else:
            self.__strTestName = _strTestName
        self.__listTest = []
        self.__bIsVerbose = False
        self.__bIsDebug = False
        self.__bIsAssert = False
        self.__bIsLogFile = False
        self.__bIsProfile = False


    def getTestName(self):
        """
        getter for TestName
        @return: test name
        @rtype: string
        """
        return self.__strTestName


    def setTestName(self, _strTestName):
        """
        Setter for test name
        @param _strTestName: name of the test
        @type _strTestName: string
        """
        self.__strTestName = _strTestName

    def addTestMethod(self, _pyClassMethod):
        """
        Add a method to the list of tests
        """
        self.__listTest.append(_pyClassMethod)


    def getNumberOfTests(self):
        """
        getter for the number of tests 
        @rtype: integer
        @return: number of tests 
        """
        return len(self.__listTest)


    def getListTest(self):
        """
        getter for the list of tests 
        @rtype: list 
        @return: list of tests 
        """
        return self.__listTest


    def executeKernel(self):
        EDVerbose.DEBUG("EDTest.executeKernel")
        self.preProcess()
        self.process()
        self.processKernel()
        self.postProcess()


    def execute(self):
        EDVerbose.DEBUG("EDTest.execute()")
        self.executeKernel()


    def preProcess(self):
        """
        to be overwritten
        """
        EDVerbose.DEBUG("EDTest.preProcess()")


    def process(self):
        """
        to be overridden
        """
        EDVerbose.DEBUG("EDTest.process()")


    def postProcess(self):
        """
        to be overridden
        """
        EDVerbose.DEBUG("EDTest.postProcess()")


    def processKernel(self):
        """
        to be overridden
        """
        EDVerbose.DEBUG("EDTest.processKernel()")

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

from __future__ import with_statement
__authors__ = ["Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"
__doc__ = """
EDInformationTest: Information for the test cases.
"""


from EDObject          import EDObject

class EDInformationTest(EDObject):
    """
    Information for the test cases.
    """
    def __init__(self, _pyStrNameTest="Test", _iNumberTest=0):
        EDObject.__init__(self)
        self.__strNameTest = _pyStrNameTest
        self.__strException = None
        self.__iNumberTest = _iNumberTest
        self.__bSuccess = True
        self.__listTest = []
        self.setTimeInit()


    def isSuccess(self):
        bSuccess = True
        if (self.__bSuccess):
            for edTest in self.__listTest:
                if (not edTest.isSuccess()):
                    bSuccess = False
        else:
            bSuccess = False
        return bSuccess


    def getTestNumber(self):
        return self.__iNumberTest


    def getTestName(self):
        return self.__strNameTest


    def setTerminate(self, _bSuccess=True):
        self.__bSuccess = _bSuccess
        self.setTimeEnd()


    def setFailure(self):
        self.__bSuccess = False


    def setSuccess(self):
        self.__bSuccess = True


    def addInformationTest(self, _edInformationTest):
        self.__listTest.append(_edInformationTest)


    def setException(self, _pyStr):
        self.__strException = _pyStr
        self.setFailure()


    def getException(self):
        return self.__strException


    def getNumberTestMethod(self):
        return len(self.__listTest)


    def outputString(self, _strSpacing="  "):
        fTime = self.getRunTime()
        bSuccess = self.isSuccess()
        with self.locked():
            strMessage = _strSpacing
            if (bSuccess):
                strMessage += "[SUCCESS]"
            else:
                strMessage += "[FAILURE]"
            strMessage += " [ %d ][ %s ][ %.3f s ]\n" % (self.__iNumberTest, self.__strNameTest, fTime)
            if ((not bSuccess) and (self.__strException is not None)):
                strMessage += _strSpacing + "          [Exception]: " + str(self.__strException) + "\n"

            for edTest in self.__listTest:
                strMessage += edTest.outputString("            ")
        return strMessage

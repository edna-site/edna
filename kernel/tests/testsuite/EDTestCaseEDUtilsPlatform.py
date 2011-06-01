#    coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseParallelExecute.py 2128 2010-10-04 16:39:42Z kieffer $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (kieffer@esrf.fr)
# 
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

__authors__ = ["Jérôme Kieffer"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, math, distutils.util
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDUtilsPlatform                     import EDUtilsPlatform



class EDTestCaseEDUtilsPlatform(EDTestCase):
    """
    Unit & execution test for the EDUtilsPlatform static class
    """

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDUtilsPlatform")


    def unitTestName(self):
        """
        Test os.name
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsPlatform.unitTestName")
        if os.name != "java":
            EDAssert.equal(os.name, EDUtilsPlatform.name, "os.name equivalent")
        else:
            EDAssert.equal(True, EDUtilsPlatform.name in ["posix", "nt"], "os.name equivalent")


    def unitTestLineSep(self):
        """
        Test os.linesep
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsPlatform.unitTestLineSep")
        EDAssert.equal(os.linesep, EDUtilsPlatform.linesep, "os.linesep equivalent")


    def unitTestSep(self):
        """
        Test os.sep
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsPlatform.unitTestSep")
        EDAssert.equal(os.sep, EDUtilsPlatform.sep, "os.sep equivalent")


    def unitTestArchSize(self):
        """
        Test architecture and size
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsPlatform.unitTestArchSize")
        if EDUtilsPlatform.size == 64:
            EDAssert.equal(distutils.util.get_platform(), EDUtilsPlatform.getPythonPlatform(), "distutil.util.get_platform")
        else:
            EDAssert.equal(distutils.util.get_platform(), EDUtilsPlatform.getSystemPlatform(), "distutil.util.get_platform")


    def unitTestEscapedLineSep(self):
        """
        Test architecture and size
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsPlatform.unitTestEscapedLineSep")
        if EDUtilsPlatform.name == "posix":
            EDAssert.equal("\\n", EDUtilsPlatform.escapedLinesep, "escapedLineSep")
        else:
            EDAssert.equal("\\r\\n", EDUtilsPlatform.escapedLinesep, "escapedLineSep")


    def process(self):
        self.addTestMethod(self.unitTestName)
        self.addTestMethod(self.unitTestLineSep)
        self.addTestMethod(self.unitTestSep)
        self.addTestMethod(self.unitTestArchSize)
        self.addTestMethod(self.unitTestEscapedLineSep)

if __name__ == '__main__':

    edTestCaseEDUtils = EDTestCaseEDUtilsUnit("EDTestCaseEDUtilsUnit")
    edTestCaseEDUtils.execute()

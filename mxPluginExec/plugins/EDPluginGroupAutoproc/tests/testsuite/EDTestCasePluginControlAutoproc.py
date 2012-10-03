# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       <author>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__="<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginControlAutoproc(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SolveContent
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginControlAutoproc")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SolveContent.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataAutoprocInput_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataAutoproc_reference.xml"))

    def testExecute(self):
        """
        """
        self.run()

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

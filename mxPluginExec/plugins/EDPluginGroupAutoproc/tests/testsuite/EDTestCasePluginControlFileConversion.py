# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
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

__author__="Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginControlFileConversion(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin SolveContent
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginControlFileConversion")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataFileConversionInput_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataFileConversionOutput_reference.xml"))

    def testExecute(self):
        """
        """
        self.run()

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

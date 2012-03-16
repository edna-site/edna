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
from XSDataAutoproc import XSDataMinimalXDSOut


class EDTestCasePluginExecuteExecMinimalXds(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin MinimalXds
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecMinimalXds")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMinimalXds_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMinimalXds_reference.xml"))


    def testExecute(self):
        """
        """
        self.run()

        plugin = self.getPlugin()
        output = plugin.dataOutput
        reference = XSDataMinimalXDSOut.parseFile(self.getReferenceDataOutputFile())

        EDAssert.equal(output.succeeded.value,
                       reference.succeeded.value,
                       "'succeeded' values match")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testMinimalXdsinstance = EDTestCasePluginExecuteControlMinimalXds("EDTestCasePluginExecuteExecMinimalXds")
    testMinimalXdsinstance.execute()

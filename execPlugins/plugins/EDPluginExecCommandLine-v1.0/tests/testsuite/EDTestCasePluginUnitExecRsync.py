#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France

#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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

__author__ = "Jerome Kieffer (Jerome.Kieffer@ESRF.eu)"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataExecCommandLine  import XSDataInputRsync, XSDataResultRsync, XSDataFile, XSDataString

class EDTestCasePluginUnitExecRsync(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Rsync
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecRsync")

    def testCheckParameters(self):
        xsd = XSDataInputRsync(destination=XSDataFile(), source=XSDataFile(), options=XSDataString())
        edPluginExecCommandLine = self.createPlugin()
        edPluginExecCommandLine.setDataInput(xsd)
        edPluginExecCommandLine.checkParameters()




    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitExecRsync = EDTestCasePluginUnitExecRsync("EDTestCasePluginUnitExecRsync")
    edTestCasePluginUnitExecRsync.execute()

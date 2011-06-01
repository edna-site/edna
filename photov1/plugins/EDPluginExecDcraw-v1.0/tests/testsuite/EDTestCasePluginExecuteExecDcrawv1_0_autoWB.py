#
#    Project: Photo-v1.0
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

import os
from EDTestCasePluginExecuteExecDcrawv1_0 import EDTestCasePluginExecuteExecDcrawv1_0

class EDTestCasePluginExecuteExecDcrawv1_0_autoWB(EDTestCasePluginExecuteExecDcrawv1_0):
    """
    Those are all execution tests for the EDNA Exec plugin Dcrawv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecuteExecDcrawv1_0.__init__(self, "EDPluginExecDcrawv1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDcraw_reference_autoWB.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDcraw_reference_autoWB.xml"))

if __name__ == '__main__':

    testDcrawv1_0instance = EDTestCasePluginExecuteExecDcrawv1_0_autoWB("EDTestCasePluginExecuteExecDcrawv1_0_autoWB")
    testDcrawv1_0instance.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
__copyright__ = "ESRF"

import os

from EDVerbose                                  import EDVerbose
from EDAssert                                   import EDAssert
from EDTestCasePluginExecuteWaitFile            import EDTestCasePluginExecuteWaitFile


class EDTestCasePluginExecuteWaitFile_timeout(EDTestCasePluginExecuteWaitFile):
    """
    Those are all execution tests for the EDNA Exec plugin WaitFile
    """

    def __init__(self, _strTestName=None):
        """
        """

        EDTestCasePluginExecuteWaitFile.__init__(self, "EDPluginWaitFile")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
                                               "XSConfiguration_WaitFile.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputWaitFile_timeout.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultWaitFile_timeout.xml"))
        tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(tmpdir):
            os.mkdir(tmpdir)
        filename = os.path.join(tmpdir, "sizeIsTen")
        if os.path.isfile(filename):
            os.remove(filename)
        open(filename, "w").write("0" * 10)

if __name__ == '__main__':

    testWaitFileinstance = EDTestCasePluginExecuteControlWaitFile_timeout("EDTestCasePluginExecuteWaitFile_timeout")
    testWaitFileinstance.execute()

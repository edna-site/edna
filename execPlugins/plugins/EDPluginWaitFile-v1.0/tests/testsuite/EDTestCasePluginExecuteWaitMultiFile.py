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

import os, threading

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteWaitMultiFile(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin WaitMultiFile
    """

    def __init__(self, _strTestName=None):
        """
        """

        EDTestCasePluginExecute.__init__(self, "EDPluginWaitMultiFile")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_WaitMultiFile.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputWaitMultiFile_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultWaitMultiFile_reference.xml"))
        self.tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(self.tmpdir):
            os.mkdir(self.tmpdir)
        for i in range(1, 7):
            filename = os.path.join(self.tmpdir, "File%isizeIsTen" % i)
            if os.path.isfile(filename):
                os.remove(filename)
        t = threading.Timer(2, self.createFiles)
        t.start()


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

        # Checking obtained results
        xsDataResult = plugin.getDataOutput()
        ref = self.readAndParseFile(self.getReferenceDataOutputFile())
        obt = xsDataResult.marshal()
#        EDVerbose.DEBUG("Reference: %s" % ref)
#        EDVerbose.DEBUG("Obtained: %s" % obt)
        EDAssert.equal(ref, obt, "XML object comparison")

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

    def createFiles(self,):
        for i in range(1, 7):
            filename = os.path.join(self.tmpdir, "File%isizeIsTen" % i)
            open(filename, "w").write("0" * 10)


if __name__ == '__main__':

    testWaitMultiFileinstance = EDTestCasePluginExecuteControlWaitMultiFile("EDTestCasePluginExecuteWaitMultiFile")
    testWaitMultiFileinstance.execute()

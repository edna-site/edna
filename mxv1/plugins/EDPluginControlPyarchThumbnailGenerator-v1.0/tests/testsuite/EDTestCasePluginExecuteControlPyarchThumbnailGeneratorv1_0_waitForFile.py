#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Copyrigth (c) 2010 ESRF
#
#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "Copyrigth (c) 2010 ESRF"

import os, tempfile, shutil

from threading import Timer

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0             import EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0

class EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile(EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0):


    def __init__(self):
        EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0.__init__(self)
        strTmpDir = tempfile.mkdtemp(prefix="EDPluginControlPyarchThumbnailGeneratorv1_0_")
        os.environ["EDNA_TMP_DIR"] = strTmpDir
        self.strInputDataFile = os.path.join(self.getTestsDataImagesHome(), "FAE_1_1_00001.cbf")
        self.strInputDataFileNew = os.path.join(strTmpDir, "FAE_1_1_00001.cbf")


    def copyFile(self):
        shutil.copyfile(self.strInputDataFile, self.strInputDataFileNew)


    def testExecute(self):
        # Start a timer for copying the file
        pyTimer = Timer(5, self.copyFile)
        pyTimer.start()
        self.run()
        pyTimer.cancel()


    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile = EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile("EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile")
    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile.execute()

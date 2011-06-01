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

import os

from threading import Timer

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0             import EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0

class EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile(EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0):


    def __init__(self):
        EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0.__init__(self)
        self.__strInputDataFile = os.path.join(self.getTestsDataImagesHome(), "FAE_1_1_00001.cbf")
        self.__strInputDataFileNew = os.path.join(self.getTestsDataImagesHome(), "FAE_1_1_00001.cbf.renamed")


    def moveFileBack(self):
        os.rename(self.__strInputDataFileNew, self.__strInputDataFile)


    def testExecute(self):
        os.rename(self.__strInputDataFile, self.__strInputDataFileNew)
        # Start a timer for copying the file
        pyTimer = Timer(5, self.moveFileBack)
        pyTimer.start()
        self.run()
        pyTimer.cancel()


    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile = EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile("EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile")
    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0_waitForFile.execute()

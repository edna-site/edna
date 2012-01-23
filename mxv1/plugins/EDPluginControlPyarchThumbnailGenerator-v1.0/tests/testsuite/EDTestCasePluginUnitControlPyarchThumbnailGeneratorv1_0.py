#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Copyrigth (c) 2010 ESRF
#
#    Principal author:        Olof Svensson
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

from EDAssert import EDAssert
from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCommon import XSDataInput

class EDTestCasePluginUnitControlPyarchThumbnailGeneratorv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlPyarchThumbnailGeneratorv1_0")


    def testCheckParameters(self):
        strInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputPyarchThumbnailGenerator_reference.xml")
        strXML = self.readAndParseFile(strInputFile)
        edPluginExecPyarchThumbnailGenerator = self.createPlugin()
        edPluginExecPyarchThumbnailGenerator.setDataInput(strXML)
        edPluginExecPyarchThumbnailGenerator.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlPyarchThumbnailGeneratorv1_0 = EDTestCasePluginUnitControlPyarchThumbnailGeneratorv1_0("EDTestCasePluginUnitControlPyarchThumbnailGeneratorv1_0")
    EDTestCasePluginUnitControlPyarchThumbnailGeneratorv1_0.execute()

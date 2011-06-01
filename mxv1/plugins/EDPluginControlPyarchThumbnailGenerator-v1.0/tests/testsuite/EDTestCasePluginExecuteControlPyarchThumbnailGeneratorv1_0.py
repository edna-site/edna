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

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlPyarchThumbnailGeneratorv1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \

                                           "XSDataInputPyarchThumbnailGenerator_reference.xml"))
    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "FAE_1_1_00001.cbf" ])


    def readAndParseFile(self, _strFileName):
        """
        Reads a file and parses potential existing environment variables such as:
        - EDNA_WORKING_DIR
        Returns the content of this file as a string
        """
        strXML = EDTestCasePluginExecute.readAndParseFile(self, _strFileName)
        self.getPlugin().configure()
        if (self.getPlugin().getWorkingDirectory() is not None):
            strXML = strXML.replace("${EDNA_WORKING_DIR}" , self.getPlugin().getWorkingDirectory())
        return strXML

    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0 = EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0("EDTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0")
    edTestCasePluginExecuteControlPyarchThumbnailGeneratorv1_0.execute()

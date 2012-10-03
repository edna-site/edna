# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) EMBL + ESRF + DLS
#
#    Principal author:       Al, Irakli, Alun, Jerome, Olof, Peter and Claudio
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

__author__ = "Al, Irakli, Alun, Jerome, Olof, Peter and Claudio"
__license__ = "GPLv3+"
__copyright__ = "EMBL + ESRF + DLS"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataEdnaSaxs import XSDataInputAutoRg as XSDataInput
from XSDataEdnaSaxs import XSDataResultAutoRg as XSDataResult

class EDTestCasePluginExecuteExecAutoRgv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin AutoRgv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecAutoRgv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_AutoRg.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputAutoRg_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultAutoRg_reference.xml"))

    def preProcess(self):
        """
        Download reference 1D curves
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["autosubtracted.dat"])

    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

################################################################################
# Compare XSDataResults
################################################################################

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResult.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testAutoRgv1_0instance = EDTestCasePluginExecuteControlAutoRgv1_0("EDTestCasePluginExecuteExecAutoRgv1_0")
    testAutoRgv1_0instance.execute()

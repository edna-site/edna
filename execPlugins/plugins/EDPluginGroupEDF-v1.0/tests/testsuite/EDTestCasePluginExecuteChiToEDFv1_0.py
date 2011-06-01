#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteChiToEDFv1_0(EDTestCasePluginExecute):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginChiToEDFv1_0")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputChiToEDF_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultChiToEDF_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.chi" ])

    def testExecute(self):
        """
        """
        self.run()
        # Checks that there are no error messages

        plugin = self.getPlugin()

        EDVerbose.DEBUG("Checking error messages...")
        EDAssert.equal(self.m_iNoErrorMessages, self.getErrorMessages().getNumberObjects())

        EDVerbose.DEBUG("Checking warning messages...")
        EDAssert.equal(self.m_iNoWarningMessages, self.getWarningMessages().getNumberObjects())

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")

        from XSDataEDFv1_0 import XSDataResultChiToEDF
        xsDataResultChiToEDFReference = XSDataResultChiToEDF.parseString(strExpectedOutput)
        xsDataResultChiToEDFObtained = XSDataResultChiToEDF.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultChiToEDFReference.marshal(), xsDataResultChiToEDFObtained.marshal())

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

if __name__ == '__main__':

    edTestCasePluginExecuteChiToEDFv1_0 = EDTestCasePluginExecuteChiToEDFv1_0()
    edTestCasePluginExecuteChiToEDFv1_0.execute()

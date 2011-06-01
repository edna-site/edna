#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author: Jerome Kieffer (kieffer@esrf.fr)
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
from EDVerbose                  import EDVerbose
from EDAssert                   import EDAssert
from EDTestCasePluginExecute    import EDTestCasePluginExecute




class EDTestCasePluginExecuteEDFReadHeaderv1_0(EDTestCasePluginExecute):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginEDFReadHeaderv1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputEDFReadHeader_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultEDFReadHeader_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"
        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0


    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.edf" ])


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

        from XSDataEDFv1_0 import XSDataResultEDFReadHeader
        xsDataResultEDFReadHeaderReference = XSDataResultEDFReadHeader.parseString(strExpectedOutput)
        xsDataResultEDFReadHeaderObtained = XSDataResultEDFReadHeader.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultEDFReadHeaderReference.marshal(), xsDataResultEDFReadHeaderObtained.marshal())


##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteEDFReadHeaderv1_0 = EDTestCasePluginExecuteEDFReadHeaderv1_0()
    edTestCasePluginExecuteEDFReadHeaderv1_0.execute()

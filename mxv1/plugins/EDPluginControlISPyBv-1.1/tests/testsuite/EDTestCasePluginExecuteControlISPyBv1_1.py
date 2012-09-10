#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
#                            Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Olof Svensson, Karl Levik"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from EDTestCasePluginExecute            import EDTestCasePluginExecute
from EDUtilsPath                        import EDUtilsPath
from EDUtilsTest                        import EDUtilsTest
from XSDataMXv1                         import XSDataResultControlISPyB


class EDTestCasePluginExecuteControlISPyBv1_1(EDTestCasePluginExecute):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginControlISPyBv1_1")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputControlISPyB_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultControlISPyB_reference.xml"))



    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages
        plugin = self.getPlugin()

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")

        xsDataResultReference = XSDataResultControlISPyB.parseString(strExpectedOutput)
        xsDataResultObtained = XSDataResultControlISPyB.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal())


##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    edTestCasePluginExecuteControlISPyBv1_1 = EDTestCasePluginExecuteControlISPyBv1_1("EDTestCasePluginExecuteControlISPyBv1_1")
    edTestCasePluginExecuteControlISPyBv1_1.execute()

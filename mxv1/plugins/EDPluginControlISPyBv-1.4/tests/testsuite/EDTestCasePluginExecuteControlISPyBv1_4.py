#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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
from XSDataMXv1                         import XSDataResultControlISPyB


class EDTestCasePluginExecuteControlISPyBv1_4(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlISPyBv1_4")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputControlISPyB_reference.xml"))




    def testExecute(self):
        self.run()

        # Checks that there are no error messages
        plugin = self.getPlugin()

        # Checks the expected result
        EDVerbose.DEBUG("Checking obtained result...")

        xsDataResultControlISPyB = plugin.dataOutput
        bExistScreeningId = False
        if xsDataResultControlISPyB.screeningId is not None:
            bExistScreeningId = True
        EDAssert.equal(True, bExistScreeningId, "Screening id generated")


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':
    edTestCasePluginExecuteControlISPyBv1_4 = EDTestCasePluginExecuteControlISPyBv1_4("EDTestCasePluginExecuteControlISPyBv1_4")
    edTestCasePluginExecuteControlISPyBv1_4.execute()

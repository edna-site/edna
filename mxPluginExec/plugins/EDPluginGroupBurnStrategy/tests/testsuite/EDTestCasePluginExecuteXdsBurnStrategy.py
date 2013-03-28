#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20130328"
__status__ = "production"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteXdsBurnStrategy(EDTestCasePluginExecute):


    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlXdsBurnStrategy")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputXdsBurnStrategy_reference.xml"))


    def testExecute(self):
        self.run()
        # Check that we have result HKL file
        xsDataOutput = self.getPlugin().dataOutput
        EDAssert.equal(True, os.path.exists(xsDataOutput.xds_hkl.value), "XDS HKL file is present")


    def process(self):
        self.addTestMethod(self.testExecute)


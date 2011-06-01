#
#    Project: FullField XANES
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
#
#    Principal author:        Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"
__date__ = "2011/05/12"

from EDVerbose                  import EDVerbose
from EDTestCasePluginUnit       import EDTestCasePluginUnit
from XSDataCommon               import XSDataInteger, XSDataFile, XSDataString
from XSDataFullFieldXAS         import XSDataInputFullFieldXAS

class EDTestCasePluginUnitControlFullFieldXASv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlFullFieldXASv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputFullFieldXAS(index=XSDataInteger(0), HDF5File=XSDataFile(), internalHDF5Path=XSDataString())
        edPluginExecFullFieldXAS = self.createPlugin()
        edPluginExecFullFieldXAS.setDataInput(xsDataInput)
        edPluginExecFullFieldXAS.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlFullFieldXASv1_0 = EDTestCasePluginUnitControlFullFieldXASv1_0("EDTestCasePluginUnitControlFullFieldXASv1_0")
    EDTestCasePluginUnitControlFullFieldXASv1_0.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
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
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"


from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataFullFieldXAS import XSDataInputAlignStack, XSDataFile, XSDataString

class EDTestCasePluginUnitControlAlignStackv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlAlignStackv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputAlignStack()
        xsDataInput.setHDF5File(XSDataFile())
        xsDataInput.setInternalHDF5Path(XSDataString())
        edPluginExecAlignStack = self.createPlugin()

        edPluginExecAlignStack.setDataInput(xsDataInput)
        edPluginExecAlignStack.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlAlignStackv1_0 = EDTestCasePluginUnitControlAlignStackv1_0("EDTestCasePluginUnitControlAlignStackv1_0")
    EDTestCasePluginUnitControlAlignStackv1_0.execute()

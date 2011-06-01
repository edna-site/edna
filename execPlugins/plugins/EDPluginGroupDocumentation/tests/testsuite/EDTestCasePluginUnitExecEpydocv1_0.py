# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF"

from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataCommon           import XSDataFile, XSDataString
from XSDataDocumentation    import XSDataInputEpydoc

class EDTestCasePluginUnitExecEpydocv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Epydocv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecEpydocv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputEpydoc()
        xsDataInput.setDocPath(XSDataFile())
        xsDataInput.setSources([XSDataFile()])
        edPluginExecEpydoc = self.createPlugin()
        edPluginExecEpydoc.setDataInput(xsDataInput)
        edPluginExecEpydoc.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecEpydocv1_0 = EDTestCasePluginUnitExecEpydocv1_0("EDTestCasePluginUnitExecEpydocv1_0")
    edTestCasePluginUnitExecEpydocv1_0.execute()

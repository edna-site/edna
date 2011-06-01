#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
from XSDataCommon import XSDataInteger, XSDataString

#    Principal author:       jerome Kieffer
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

__author__="jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataCommon import XSDataString,XSDataDouble,XSDataInteger
from XSDataPeakSearchv1_0 import XSDataInputPeakSearch

class EDTestCasePluginUnitExecPeakSearchv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin PeakSearchv1_0
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecPeakSearchv1_0")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputPeakSearch()
        xsDataInput.setThreshold([XSDataDouble(1.0)])
        xsDataInput.setIndexMax(XSDataInteger(10))
        xsDataInput.setIndexMin(XSDataInteger(0))
        xsDataInput.setStem(XSDataString())
        edPluginExecPeakSearch = self.createPlugin()
        edPluginExecPeakSearch.setDataInput(xsDataInput)
        edPluginExecPeakSearch.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecPeakSearchv1_0 = EDTestCasePluginUnitExecPeakSearchv1_0("EDTestCasePluginUnitExecPeakSearchv1_0")
    edTestCasePluginUnitExecPeakSearchv1_0.execute()

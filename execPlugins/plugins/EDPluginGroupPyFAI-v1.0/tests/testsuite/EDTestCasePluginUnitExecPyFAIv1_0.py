# coding: utf8
#
#    Project: Python Fast Azimuthal Integration
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#
#    Principal author:       Jerome Kieffer <jerome.kieffer@esrf.fr>
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

__author__="Jerome Kieffer <jerome.kieffer@esrf.fr>"
__license__ = "GPLv3+"
__copyright__ = "2012 European Synchrotron Radiation Facility"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataPyFAIv1_0 import XSDataInputPyFAI

class EDTestCasePluginUnitExecPyFAIv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin PyFAIv1_0
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecPyFAIv1_0")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputPyFAI()
        edPluginExecPyFAIv1_0 = self.createPlugin()
        edPluginExecPyFAIv1_0.setDataInput(xsDataInput)
        edPluginExecPyFAIv1_0.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecPyFAIv1_0 = EDTestCasePluginUnitExecPyFAIv1_0("EDTestCasePluginUnitExecPyFAIv1_0")
    edTestCasePluginUnitExecPyFAIv1_0.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF

#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataMXv1 import XSDataIndexingResult

class EDTestCasePluginUnitExecEvaluationIndexingv10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin EvaluationIndexingv10
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecEvaluationIndexingv10")
        self.strPathToDataInputFile = os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataIndexingResult_reference.xml")


    def testCheckParameters(self):
        strXMLInput = self.readAndParseFile(self.strPathToDataInputFile)
        xsDataInput = XSDataIndexingResult.parseString(strXMLInput)
        edPluginExecEvaluationIndexing = self.createPlugin()
        edPluginExecEvaluationIndexing.setDataInput(xsDataInput, "indexingResult")
        edPluginExecEvaluationIndexing.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecEvaluationIndexingv10 = EDTestCasePluginUnitExecEvaluationIndexingv10("EDTestCasePluginUnitExecEvaluationIndexingv10")
    edTestCasePluginUnitExecEvaluationIndexingv10.execute()

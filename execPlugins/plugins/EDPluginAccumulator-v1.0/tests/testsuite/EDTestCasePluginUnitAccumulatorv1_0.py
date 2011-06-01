#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF

#    Principal author:       Jerome Kieffer
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
__copyright__ = "ESRF"

from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataAccumulatorv1_0  import XSDataInputAccumulator, XSDataBoolean
from EDAssert               import EDAssert

class EDTestCasePluginUnitAccumulatorv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Accumulatorv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginAccumulatorv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputAccumulator()
        edPluginAccumulator = self.createPlugin()
        edPluginAccumulator.setDataInput(xsDataInput)
        edPluginAccumulator.checkParameters()

    def testFlush(self):
        xsDataInput = XSDataInputAccumulator()
        xsDataInput.setFlush(XSDataBoolean(True))
        edPluginAccumulator = self.createPlugin()
        edPluginAccumulator.emptyItems()
        edPluginAccumulator.emptyQueries()
        edPluginAccumulator.addItem("data1")
        edPluginAccumulator.addItem("data2")
        edPluginAccumulator.addItem("data3")
        edPluginAccumulator.addItem("data4")
        edPluginAccumulator.addItem("data3")
        EDAssert.equal(edPluginAccumulator.getItems(), ["data1", "data2", "data3", "data4", "data3"], "Artificial item feed")
        edPluginAccumulator.setDataInput(xsDataInput)
        edPluginAccumulator.checkParameters()
        edPluginAccumulator.preProcess()
        edPluginAccumulator.process()
        edPluginAccumulator.postProcess()
        EDAssert.equal(edPluginAccumulator.getItems(), [], "Empty item list after Flush")
        if "query" in  edPluginAccumulator.getDataOutput().__dict__:
#            print "Old datamodel"
            myQuery = edPluginAccumulator.getDataOutput().__dict__["query"][0].__dict__['item']
        else:
            myQuery = edPluginAccumulator.getDataOutput().__dict__["_XSDataResultAccumulator__query"][0].__dict__['_XSDataQuery__item']
        EDAssert.equal(len(myQuery), 5, "We expect 5 items as output")




    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testFlush)


if __name__ == '__main__':

    edTestCasePluginUnitAccumulatorv1_0 = EDTestCasePluginUnitAccumulatorv1_0("EDTestCasePluginUnitAccumulatorv1_0")
    edTestCasePluginUnitAccumulatorv1_0.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
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

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsFile                         import EDUtilsFile
from XSDataAccumulatorv1_0               import XSDataResultAccumulator


class EDTestCasePluginExecuteAccumulatorv1_0_NoRemove(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Accumulatorv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginAccumulatorv1_0")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
                                               "XSConfiguration_Accumulator.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputAccumulator_NoRemove.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultAccumulator_NoRemove.xml"))


    def testExecute(self):
        """
        """
        plugin = self.getPlugin()
        plugin.emptyItems()
        plugin.emptyQueries()
        plugin.addItem("data1")
        plugin.addItem("data2")
        plugin.addItem("data3")
        plugin.addItem("data4")
        plugin.addItem("data5")
        self.run()
        # Checking obtained results
#        print plugin.getDataInput().marshal()
#        print plugin.getDataOutput().marshal()
        xsDataResult = plugin.getDataOutput()
        strXMLRef = XSDataResultAccumulator.parseString(EDUtilsFile.readFile(self.getReferenceDataOutputFile())).marshal()
        EDAssert.equal(xsDataResult.marshal(), strXMLRef, "XML results are conform")
#        print plugin.getItems()
        EDAssert.equal(plugin.getItems(), ['data1', 'data2', 'data3', 'data4', 'data5'], "Remaining items are the same")
        plugin.emptyItems()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testAccumulatorv1_0instance = EDTestCasePluginExecuteControlAccumulatorv1_0("EDTestCasePluginExecuteAccumulatorv1_0_NoRemove")
    testAccumulatorv1_0instance.execute()

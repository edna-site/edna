#
# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2010, ESRF, Grenoble"

import os, sys

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteExecMeasureOffsetv1_0             import EDTestCasePluginExecuteExecMeasureOffsetv1_0
from XSDataShiftv1_0    import XSDataInputMeasureOffset, XSDataResultMeasureOffset


class EDTestCasePluginExecuteExecMeasureOffsetv1_0_array(EDTestCasePluginExecuteExecMeasureOffsetv1_0):
    """
    Those are all execution tests for the EDNA Exec plugin MeasureOffsetv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecuteExecMeasureOffsetv1_0.__init__(self, "EDPluginExecMeasureOffsetv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MeasureOffset.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMeasureOffset_array.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMeasureOffset_reference.xml"))
        self.im1 = "rhodo_f1_datanorm_0000.edf"
        self.im2 = "rhodo_f1_datanorm_0001.edf"



if __name__ == '__main__':

    testMeasureOffsetv1_0instance = EDTestCasePluginExecuteExecMeasureOffsetv1_0_array("EDTestCasePluginExecuteExecMeasureOffsetv1_0_array")
    testMeasureOffsetv1_0instance.execute()

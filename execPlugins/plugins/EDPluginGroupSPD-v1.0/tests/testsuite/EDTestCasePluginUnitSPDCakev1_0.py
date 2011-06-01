#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsTest import EDUtilsTest
from XSDataSPDv1_0 import XSDataInputSPDCake

class EDTestCasePluginUnitSPDCakev1_0(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginSPDCakev1_0")
        edStringPluginTestDataHome = self.getPluginTestsDataHome()
        self.m_edStringReferenceInputFileName = os.path.join(edStringPluginTestDataHome, "XSDataInputSPDCake_reference.xml")


    def testCheckParameters(self):
        edPluginSPD = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(edStringXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.checkParameters()


    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitSPDCakev1_0 = EDTestCasePluginUnitExecSPDv10("EDTestCasePluginUnitSPDCakev1_0")
    edTestCasePluginUnitSPDCakev1_0.execute()

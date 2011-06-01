#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 INSTITUTE_LINE_1
#                            INSTITUTE_LINE_2
#
#    Principal author:       PRINCIPAL_AUTHOR
#
#    Contributing author:    CONTRIBUTING_AUTHOR
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

import os
from EDImportLib            import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from EDUtilsTest            import EDUtilsTest
from XSDataFIT2Dv1_0        import XSDataInputFIT2DCake

class EDTestCasePluginUnitFIT2DCakev1_0(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginFIT2DCakev1_0")
        edStringPluginTestDataHome = self.getPluginTestsDataHome()
        self.m_edStringReferenceInputFileName = os.path.join(edStringPluginTestDataHome, "XSDataInputFIT2DCake_reference.xml")


    def testCheckParameters(self):
        edPluginFIT2D = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputFIT2DCake = XSDataInputFIT2DCake.parseString(edStringXMLInput)
        edPluginFIT2D.setDataInput(xsDataInputFIT2DCake)
        edPluginFIT2D.checkParameters()


    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitFIT2DCakev1_0 = EDTestCasePluginUnitExecFIT2Dv10("EDTestCasePluginUnitFIT2DCakev1_0")
    edTestCasePluginUnitFIT2DCakev1_0.execute()

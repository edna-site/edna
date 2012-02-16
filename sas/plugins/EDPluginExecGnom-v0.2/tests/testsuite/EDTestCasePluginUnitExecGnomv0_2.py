# coding: utf8
#
#    Project: solution Scattering
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 DLS
#                  2012 ESRF
#    Principal author:       irakli
#                            Jérôme Kieffer
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

__authors__ = ["irakli", "Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "2011 DLS, 2012 ESRF"

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataSAS import XSDataInputGnom
from XSDataCommon import XSDataDouble

class EDTestCasePluginUnitExecGnomv0_2(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Gnomv0_2
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecGnomv0_2")
        #self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputGnom_reference.xml")



    def testCheckParameters(self):
        xsDataInput = XSDataInputGnom()
        edPluginExecGnom = self.createPlugin()
        xsDataInput.rMax = XSDataDouble()
        xsDataInput.experimentalDataQ = [XSDataDouble()]
        xsDataInput.experimentalDataValues = [XSDataDouble()]
        edPluginExecGnom.setDataInput(xsDataInput)
        edPluginExecGnom.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecGnomv0_2 = EDTestCasePluginUnitExecGnomv0_2("EDTestCasePluginUnitExecGnomv0_2")
    edTestCasePluginUnitExecGnomv0_2.execute()

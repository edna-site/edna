#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlGridScreeningv1_0 import EDTestCasePluginExecuteControlGridScreeningv1_0




class EDTestCasePluginExecuteControlGridScreeningv1_0_integrationError(EDTestCasePluginExecuteControlGridScreeningv1_0):
    """
    Test of characterisation error messages.
    """

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlGridScreeningv1_0.__init__(self, "EDTestCasePluginExecuteControlGridScreeningv1_0_integrationError")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputGridScreening_integrationError.xml"))
        self.setNoExpectedWarningMessages(0)
        self.setNoExpectedErrorMessages(1)


    def preProcess(self):
        EDTestCasePluginExecuteControlGridScreeningv1_0.preProcess(self)
        self.loadTestImage([ "integrationError_2_001.img" ])


#    def testExecute(self):
#        EDTestCasePluginExecuteControlGridScreeningv1_0.testExecute(self)
#
#        edPlugin = self.getPlugin()
#        strStatusMessage = None
#        if edPlugin.hasDataOutput("statusMessage"):
#            strStatusMessage = edPlugin.getDataOutput("statusMessage")[0].getValue()
#        EDAssert.equal(True, strStatusMessage.find("Integration FAILURE") != -1, "Status message contains 'Integration FAILURE'")



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlGridScreeningv1_0_integrationError = EDTestCasePluginExecuteControlGridScreeningv1_0_integrationError("EDTestCasePluginExecuteControlGridScreeningv1_0_integrationError")
    edTestCasePluginExecuteControlGridScreeningv1_0_integrationError.execute()

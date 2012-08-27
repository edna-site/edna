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




class EDTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators(EDTestCasePluginExecuteControlGridScreeningv1_0):
    """
    Test of characterisation error messages.
    """

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlGridScreeningv1_0.__init__(self, "EDTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputGridScreening_onlyImageQualityIndicators.xml"))
        self.setNoExpectedWarningMessages(0)
        self.setNoExpectedErrorMessages(0)


    def preProcess(self):
        EDTestCasePluginExecuteControlGridScreeningv1_0.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img" ])


    def testExecute(self):
        EDTestCasePluginExecuteControlGridScreeningv1_0.testExecute(self)

        edPlugin = self.getPlugin()
        # Check that we have the image quality indicators
        xsDataResult = edPlugin.getDataOutput()
        EDAssert.equal(False, xsDataResult.getImageQualityIndicators() is None, "Result contains image quality indicators")
        # Check that we don't have the indexing result
        EDAssert.equal(True, xsDataResult.getMosaicity() is None, "Result doesn't contain the mosaicity estimation")



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators = EDTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators("EDTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators")
    edTestCasePluginExecuteControlGridScreeningv1_0_onlyImageQualityIndicators.execute()

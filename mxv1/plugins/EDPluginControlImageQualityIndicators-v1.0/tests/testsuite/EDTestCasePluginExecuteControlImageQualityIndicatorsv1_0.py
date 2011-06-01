#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
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

from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlImageQualityIndicatorsv1_0(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlImageQualityIndicatorsv1_0")
        self.setRequiredPluginConfiguration("EDPluginLabelitDistlv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataImage_1_reference.xml"), "referenceImage")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataImage_2_reference.xml"), "referenceImage")
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataImageQualityIndicators_1_reference.xml"), "imageQualityIndicators")
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataImageQualityIndicators_2_reference.xml"), "imageQualityIndicators")


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':
    edTestCasePluginExecuteControlGeneratePredictionv10 = EDTestCasePluginExecuteControlImageQualityIndicatorsv1_0("EDTestCasePluginExecuteControlImageQualityIndicatorsv1_0")
    edTestCasePluginExecuteControlGeneratePredictionv10.execute()

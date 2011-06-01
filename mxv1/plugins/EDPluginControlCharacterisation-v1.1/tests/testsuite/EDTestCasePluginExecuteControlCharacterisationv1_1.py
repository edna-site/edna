#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlCharacterisationv1_1(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlCharacterisationv1_1")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIntegrationv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMGeneratePredictionv10")
        self.setRequiredPluginConfiguration("EDPluginBestv1_1")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference.xml"))
        self.setNoExpectedErrorMessages(0)
        self.setNoExpectedWarningMessages(0)


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()


        # Checks the expected result

        plugin = self.getPlugin()
        xsDataResultCharacterisation = plugin.getDataOutput()

        # There should be indexing results, integration results and strategy results
        EDAssert.equal(True, xsDataResultCharacterisation.getIndexingResult()    is not None)
        EDAssert.equal(True, xsDataResultCharacterisation.getIntegrationResult() is not None)
        EDAssert.equal(True, xsDataResultCharacterisation.getStrategyResult()    is not None)



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv1_1 = EDTestCasePluginExecuteControlCharacterisationv1_1("EDTestCasePluginExecuteControlCharacterisationv1_1")
    edTestCasePluginExecuteControlCharacterisationv1_1.execute()

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

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath




class EDTestCasePluginExecuteControlInducedRadiationProcessv10_withBonly(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlInducedRadiationProcessv10")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference_withBonly.xml"))



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

    edTestCasePluginExecuteControlInducedRadiationProcessv10_withBonly = EDTestCasePluginExecuteControlInducedRadiationProcessv10_withBonly("EDTestCasePluginExecuteControlInducedRadiationProcessv10_withBonly")
    edTestCasePluginExecuteControlInducedRadiationProcessv10_withBonly.execute()

#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlCharacterisationv2_0.py 1939 2010-08-23 10:07:58Z svensson $"
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




class EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlCharForReorientationv2_0", "EDPluginControlCharacterisation-v1.0", _strTestName)

        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIntegrationv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMGeneratePredictionv10")
        self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")
        self.setRequiredPluginConfiguration("EDPluginSTACAlignmentv2_0")
        self.setRequiredPluginConfiguration("EDPluginSTACOrientationv2_0")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_reference_KAPPA_Cell.xml") , "mxv1InputCharacterisation")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "mxv2_XSDataCollection_reference.xml") , "mxv2DataCollection")

        #self.setReferenceDataOutputFile( os.path.join( self.getPluginTestsDataHome(), "XSDataResultCharacterisation_reference.xml"))



    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        # Checks the expected result

        xsDataResultCharacterisationv2_0 = plugin.getDataOutput()

        EDAssert.equal(True, xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation_Reference()    is not None)
        EDAssert.equal(True, xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()    is not None)
        EDAssert.equal(True, xsDataResultCharacterisationv2_0.getSuggestedStrategy()    is not None)
        EDAssert.equal(True, xsDataResultCharacterisationv2_0.getPossibleOrientations()    is not None)

        xsDataResultCharacterisation = xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()

        # There should be indexing results, integration results and strategy results
        EDAssert.equal(True, xsDataResultCharacterisation.getIndexingResult()    is not None)
        EDAssert.equal(True, xsDataResultCharacterisation.getIntegrationResult() is not None)
        EDAssert.equal(True, xsDataResultCharacterisation.getStrategyResult()    is not None)



    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell = EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell("EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell")
    EDTestCasePluginExecuteControlCharForReorientationv2_0_KAPPA_Cell.execute()

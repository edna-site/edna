#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteInterfacev2_0.py 1555 2010-05-25 07:27:29Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr),
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

__authors__ = [ "Karl Levik", "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "karl.levik@diamond.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDAssert                   import EDAssert
from XSDataCommon               import XSDataString
from XSDataCommon               import XSDataInteger
from XSDataCommon               import XSDataFloat
from XSDataCommon               import XSDataBoolean


class EDTestCasePluginExecuteInterfacev2_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlInterfacev2_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIntegrationv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMGeneratePredictionv10")
        self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        #self.setRequiredPluginConfiguration("EDPluginBestv2_0")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)

        strImageName1 = "ref-testscale_1_001.img"
        strImageName2 = "ref-testscale_1_002.img"

        self.loadTestImage([ strImageName1, strImageName2 ])

        edPlugin = self.getPlugin()
        edPlugin.setDataInput(XSDataString(os.path.join(self.getTestsDataImagesHome(), strImageName1)), "imagePaths")
        edPlugin.setDataInput(XSDataString(os.path.join(self.getTestsDataImagesHome(), strImageName2)), "imagePaths")
        edPlugin.setDataInput(XSDataInteger(1), "dataCollectionId")
        edPlugin.setDataInput(XSDataString("EDNA test characterisation"), "comments")
        edPlugin.setDataInput(XSDataString("Test"), "shortComments")


    def testExecute(self):
        self.run()
        edPlugin = self.getPlugin()
        EDAssert.equal(edPlugin.hasDataOutput("resultCharacterisationv2_0"), True)

        if (edPlugin.hasDataOutput("resultCharacterisationv2_0")):
            xsDataResultCharacterisationv2_0 = edPlugin.getDataOutput("resultCharacterisationv2_0")[0]
            xsDataResultCharacterisation = xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()
            EDAssert.equal(xsDataResultCharacterisation.getDataCollection() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getIndexingResult() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getIntegrationResult() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getStrategyResult() != None, True)


    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteInterfacev2_0 = EDTestCasePluginExecuteInterfacev2_0("EDTestCasePluginExecuteInterfacev2_0")
    edTestCasePluginExecuteInterfacev2_0.execute()

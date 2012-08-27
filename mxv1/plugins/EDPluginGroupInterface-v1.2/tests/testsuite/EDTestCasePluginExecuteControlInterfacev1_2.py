#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
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
from EDUtilsPath                import EDUtilsPath
from XSDataCommon               import XSDataString
from XSDataCommon               import XSDataInteger
from XSDataCommon               import XSDataFloat
from XSDataCommon               import XSDataBoolean


class EDTestCasePluginExecuteControlInterfacev1_2(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlInterfacev1_2")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIntegrationv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMGeneratePredictionv10")
        self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        #self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)

        strImageName1 = "ref-testscale_1_001.img"
        strImageName2 = "ref-testscale_1_002.img"

        self.loadTestImage([ strImageName1, strImageName2 ])

        edPlugin = self.getPlugin()
        edPlugin.setDataInput(XSDataString(os.path.join(self.getTestsDataImagesHome(), strImageName1)), "imagePaths")
        edPlugin.setDataInput(XSDataString(os.path.join(self.getTestsDataImagesHome(), strImageName2)), "imagePaths")
        if EDUtilsPath.getEdnaSite().startswith("ESRF"):
            edPlugin.setDataInput(XSDataInteger(772751), "dataCollectionId")
        else:
            edPlugin.setDataInput(XSDataInteger(1), "dataCollectionId")
        edPlugin.setDataInput(XSDataString("EDNA test characterisation"), "comments")
        edPlugin.setDataInput(XSDataString("Test"), "shortComments")


    def testExecute(self):
        self.run()
        edPlugin = self.getPlugin()
        EDAssert.equal(edPlugin.hasDataOutput("characterisation"), True)

        if (edPlugin.hasDataOutput("characterisation")):
            xsDataResultCharacterisation = edPlugin.getDataOutput("characterisation")[0]
            EDAssert.equal(xsDataResultCharacterisation.getDataCollection() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getIndexingResult() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getIntegrationResult() != None, True)
            EDAssert.equal(xsDataResultCharacterisation.getStrategyResult() != None, True)


    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteControlInterfacev1_2 = EDTestCasePluginExecuteControlInterfacev1_2("EDTestCasePluginExecuteControlInterfacev1_2")
    edTestCasePluginExecuteControlInterfacev1_2.execute()

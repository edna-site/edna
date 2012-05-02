#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:  Marie-Francoise Incardona (incardon@esrf.fr)
#                           Olof Svensson (svensson@esrf.fr) 
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

import os.path
from EDVerbose                      import EDVerbose
from EDAssert                       import EDAssert
from EDUtilsFile                    import EDUtilsFile
from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDUtilsTest                    import EDUtilsTest

from XSDataCommon                   import XSDataInteger
from XSDataCommon                   import XSDataDouble
from XSDataCommon                   import XSDataString
from XSDataCommon                   import XSDataBoolean
from XSDataCommon                   import XSData
from XSDataISPyBv1_1                import XSDataInputISPyB
from XSDataISPyBv1_1                import XSDataISPyBImage
from XSDataISPyBv1_1                import XSDataISPyBScreening
from XSDataISPyBv1_1                import XSDataISPyBScreeningInput
from XSDataISPyBv1_1                import XSDataISPyBScreeningOutput
from XSDataISPyBv1_1                import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_1                import XSDataISPyBScreeningRank
from XSDataISPyBv1_1                import XSDataISPyBScreeningRankSet
from XSDataISPyBv1_1                import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_1                import XSDataResultISPyB
from XSDataISPyBv1_1                import XSDatadbstatus
from XSDataISPyBv1_1                import XSDataISPyBScreeningOutputContainer

class EDTestCasePluginUnitISPyBv1_1(EDTestCasePluginUnit):

    def __init__(self, _pyStrTestName=None):
       """
       Set up paths, reference files etc.
       """
       EDTestCasePluginUnit.__init__(self, "EDPluginISPyBv1_1", "EDPluginGroupISPyB-v1.1", _pyStrTestName)

       self.m_edStrDataPath = self.getPluginTestsDataHome()
       self.m_edObtainedInputFile = "XSDataInputISPyBv1_1.xml"
       self.m_edReferenceInputFile = os.path.join(self.m_edStrDataPath, "XSDataISPyBv1_1Input_reference.xml")

    def preProcess(self):
        """
        Delete old obtained files.
        """
        EDTestCasePluginUnit.preProcess(self)
        EDUtilsFile.deleteFile(self.m_edObtainedInputFile)

    def testConfigureOK(self):
        """
        A test for the configure method of the plugin
        """
        edPluginISPyB = self.createPlugin()
        xsPluginItemISPyB = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginISPyB.setConfiguration(xsPluginItemISPyB)
        edPluginISPyB.configure()
        EDAssert.equal("localhost", edPluginISPyB.getDbserverHost())
        EDAssert.equal(9090, edPluginISPyB.getDbserverPort())
        self.cleanUp(edPluginISPyB)

    def testSetDataModelInput(self):
        """
        A test for whether we can obtain the expected XML by setting a certain input for the plugin. 
        """
        edPluginISPyB = self.createPlugin()
        xsPluginItemISPyB = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginISPyB.setConfiguration(xsPluginItemISPyB)
        edPluginISPyB.configure()

        xsDataInputISPyB = XSDataInputISPyB()

        xsDataISPyBImage = XSDataISPyBImage()
        xsDataISPyBImage.setFileName(XSDataString("test.img"))
        xsDataISPyBImage.setFileLocation(XSDataString("/tmp"))

        xsDataISPyBScreening = XSDataISPyBScreening()
#        xsDataISPyBScreening.setDataCollectionId( XSDataInteger ( 1 ) )
        xsDataISPyBScreening.setProgramVersion(XSDataString("EDNA Prototype"))

        xsDataISPyBScreeningInput = XSDataISPyBScreeningInput()
        xsDataISPyBScreeningInput.setBeamX(XSDataDouble(10.4))
        xsDataISPyBScreeningInput.setBeamY(XSDataDouble(2.31))
        xsDataISPyBScreeningInput.setRmsErrorLimits(XSDataDouble(0.8))
        xsDataISPyBScreeningInput.setMinimumFractionIndexed(XSDataDouble(0.4))
        xsDataISPyBScreeningInput.setMaximumFractionRejected(XSDataDouble(0.45))
        xsDataISPyBScreeningInput.setMinimumSignalToNoise(XSDataDouble(0.56))

        xsDataISPyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("It's just fine."))
        xsDataISPyBScreeningOutput.setMosaicity(XSDataDouble(0.25))
        xsDataISPyBScreeningOutput.setBeamShiftX(XSDataDouble (0.141))
        xsDataISPyBScreeningOutput.setBeamShiftY(XSDataDouble (0.156))

        xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()
        xsDataISPyBScreeningOutputLattice.setSpaceGroup(XSDataString("P222"))

        xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
        xsDataISPyBScreeningStrategy.setPhiStart(XSDataDouble(0))
        xsDataISPyBScreeningStrategy.setPhiEnd(XSDataDouble(20))
        xsDataISPyBScreeningStrategy.setRotation(XSDataDouble(1))
        xsDataISPyBScreeningStrategy.setProgram(XSDataString("EDNA"))
        xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(1))

        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningOutputContainer.setScreeningOutput(xsDataISPyBScreeningOutput)
        xsDataISPyBScreeningOutputContainer.getScreeningOutputLattice().append(xsDataISPyBScreeningOutputLattice)
        xsDataISPyBScreeningOutputContainer.getScreeningStrategy().append(xsDataISPyBScreeningStrategy)

        xsDataISPyBScreeningRank = XSDataISPyBScreeningRank()
        xsDataISPyBScreeningRank.setRankValue(XSDataDouble(1.4))
        xsDataISPyBScreeningRank.setRankInformation(XSDataString("This is the only one"))

        xsDataISPyBScreeningRankSet = XSDataISPyBScreeningRankSet()
        xsDataISPyBScreeningRankSet.setRankEngine(XSDataString("ISPyB"))

        xsDataInputISPyB.setImage(xsDataISPyBImage)
        xsDataInputISPyB.setScreening(xsDataISPyBScreening)
        xsDataInputISPyB.getScreeningInput().append(xsDataISPyBScreeningInput)
        xsDataInputISPyB.getScreeningOutputContainer().append(xsDataISPyBScreeningOutputContainer)
        xsDataInputISPyB.getScreeningRank().append(xsDataISPyBScreeningRank)
        xsDataInputISPyB.setScreeningRankSet(xsDataISPyBScreeningRankSet)
        xsDataInputISPyB.outputFile(self.m_edObtainedInputFile)

        pyStrExpectedInput = self.readAndParseFile (self.m_edReferenceInputFile)
        xsDataScreeningExpected = XSDataInputISPyB.parseString(pyStrExpectedInput)
        pyStrExpectedXML = xsDataScreeningExpected.marshal()

        pyStrObtainedInput = self.readAndParseFile (self.m_edObtainedInputFile)
        xsDataScreeningObtained = XSDataInputISPyB.parseString(pyStrObtainedInput)
        pyStrObtainedXML = xsDataScreeningObtained.marshal()

        EDAssert.equal(pyStrExpectedXML, pyStrObtainedXML)
        self.cleanUp(edPluginISPyB)

    def process(self):
       """
       List of test methods
       """
       EDVerbose.DEBUG("*** EDTestCasePluginUnitISPyBv1_1.process")
       self.addTestMethod(self.testConfigureOK)
       self.addTestMethod(self.testSetDataModelInput)

if __name__ == '__main__':
    edTestCasePluginUnitISPyBv1_1 = EDTestCasePluginUnitISPyBv1_1("EDTestCasePluginUnitISPyBv1_1")
    edTestCasePluginUnitISPyBv1_1.execute()

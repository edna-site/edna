#
#    Project: mxPluginExec
#             http://www.edna-site.org
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


from EDAssert                       import EDAssert
from EDUtilsFile                    import EDUtilsFile
from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDUtilsTest                    import EDUtilsTest

from XSDataCommon                   import XSDataInteger
from XSDataCommon                   import XSDataFloat
from XSDataCommon                   import XSDataString
from XSDataCommon                   import XSDataBoolean
from XSDataCommon                   import XSData
from XSDataISPyBv10                 import XSDataInputISPyB
from XSDataISPyBv10                 import XSDataISPyBImage
from XSDataISPyBv10                 import XSDataISPyBScreening
from XSDataISPyBv10                 import XSDataISPyBScreeningInput
from XSDataISPyBv10                 import XSDataISPyBScreeningOutput
from XSDataISPyBv10                 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv10                 import XSDataISPyBScreeningRank
from XSDataISPyBv10                 import XSDataISPyBScreeningRankSet
from XSDataISPyBv10                 import XSDataISPyBScreeningStrategy
from XSDataISPyBv10                 import XSDataResultISPyB
from XSDataISPyBv10                 import XSDatadbstatus

class EDTestCasePluginUnitISPyBv10(EDTestCasePluginUnit):

    def __init__(self, _strTestName=None):
       """
       Set up paths, reference files etc.
       """
       EDTestCasePluginUnit.__init__(self, "EDPluginISPyBv10", "EDPluginGroupISPyB-v1.0", _strTestName)

       self.m_edStrDataPath = self.getPluginTestsDataHome()
       self.m_edObtainedInputFile = "XSDataInputISPyBv10.xml"
       self.m_edReferenceInputFile = os.path.join(self.m_edStrDataPath, "XSDataISPyBv10Input_reference.xml")

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
        xsDataISPyBScreeningInput.setBeamX(XSDataFloat(10.4))
        xsDataISPyBScreeningInput.setBeamY(XSDataFloat(2.31))
        xsDataISPyBScreeningInput.setRmsErrorLimits(XSDataFloat(0.8))
        xsDataISPyBScreeningInput.setMinimumFractionIndexed(XSDataFloat(0.4))
        xsDataISPyBScreeningInput.setMaximumFractionRejected(XSDataFloat(0.45))
        xsDataISPyBScreeningInput.setMinimumSignalToNoise(XSDataFloat(0.56))

        xsDataISPyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("It's just fine."))
        xsDataISPyBScreeningOutput.setMosaicity(XSDataFloat(0.25))
        xsDataISPyBScreeningOutput.setBeamShiftX(XSDataFloat (0.141))
        xsDataISPyBScreeningOutput.setBeamShiftY(XSDataFloat (0.156))

        xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()
        xsDataISPyBScreeningOutputLattice.setSpaceGroup(XSDataString("P222"))

        xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
        xsDataISPyBScreeningStrategy.setPhiStart(XSDataFloat(0))
        xsDataISPyBScreeningStrategy.setPhiEnd(XSDataFloat(20))
        xsDataISPyBScreeningStrategy.setRotation(XSDataFloat(1))
        xsDataISPyBScreeningStrategy.setProgram(XSDataString("EDNA"))
        xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(1))

        xsDataInputISPyB.setImage(xsDataISPyBImage)
        xsDataInputISPyB.setScreening(xsDataISPyBScreening)
        xsDataInputISPyB.setScreeningInput(xsDataISPyBScreeningInput)
        xsDataInputISPyB.setScreeningOutput(xsDataISPyBScreeningOutput)
        xsDataInputISPyB.setScreeningOutputLattice(xsDataISPyBScreeningOutputLattice)
        xsDataInputISPyB.setScreeningStrategy(xsDataISPyBScreeningStrategy)

        xsDataInputISPyB.outputFile(self.m_edObtainedInputFile)

        strExpectedInput = self.readAndParseFile (self.m_edReferenceInputFile)
        strObtainedInput = self.readAndParseFile (self.m_edObtainedInputFile)
        xsDataScreeningExpected = XSDataInputISPyB.parseString(strExpectedInput)
        xsDataScreeningObtained = XSDataInputISPyB.parseString(strObtainedInput)
        pyStrExpectedXML = xsDataScreeningExpected.marshal()
        pyStrObtainedXML = xsDataScreeningObtained.marshal()
        EDAssert.equal(pyStrExpectedXML, pyStrObtainedXML)

        self.cleanUp(edPluginISPyB)

    def process(self):
       """
       List of test methods
       """
       self.DEBUG("*** EDTestCasePluginUnitISPyBv10.process")
       self.addTestMethod(self.testConfigureOK)
       self.addTestMethod(self.testSetDataModelInput)

if __name__ == '__main__':
    # JIT compiler accelerator
    edTestCasePluginUnitISPyBv10 = EDTestCasePluginUnitISPyBv10("EDTestCasePluginUnitISPyBv10")
    edTestCasePluginUnitISPyBv10.execute()

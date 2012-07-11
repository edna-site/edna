#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source
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

__author__ = "Karl Levik, Marie-Francoise Incardona, Olof Svensson"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"
__date__ = "20120712"
__status__ = "production"

import os.path


from EDAssert                       import EDAssert
from EDUtilsFile                    import EDUtilsFile
from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDUtilsTest                    import EDUtilsTest

from XSDataCommon                   import XSDataInteger
from XSDataCommon                   import XSDataDouble
from XSDataCommon                   import XSDataString
from XSDataCommon                   import XSDataBoolean
from XSDataCommon                   import XSData
from XSDataISPyBv1_2                import XSDataInputISPyB
from XSDataISPyBv1_2                import XSDataISPyBImage
from XSDataISPyBv1_2                import XSDataISPyBScreening
from XSDataISPyBv1_2                import XSDataISPyBScreeningInput
from XSDataISPyBv1_2                import XSDataISPyBScreeningOutput
from XSDataISPyBv1_2                import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_2                import XSDataISPyBScreeningRank
from XSDataISPyBv1_2                import XSDataISPyBScreeningRankSet
from XSDataISPyBv1_2                import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_2                import XSDataISPyBScreeningStrategyContainer
from XSDataISPyBv1_2                import XSDataISPyBScreeningStrategyWedge
from XSDataISPyBv1_2                import XSDataISPyBScreeningStrategySubWedge
from XSDataISPyBv1_2                import XSDataISPyBScreeningStrategyWedgeContainer
from XSDataISPyBv1_2                import XSDataISPyBScreeningFile
from XSDataISPyBv1_2                import XSDataISPyBv1_2
from XSDataISPyBv1_2                import XSDataResultISPyB
from XSDataISPyBv1_2                import XSDatadbstatus
from XSDataISPyBv1_2                import XSDataISPyBScreeningOutputContainer

class EDTestCasePluginUnitISPyBv1_2(EDTestCasePluginUnit):

    def __init__(self, _strTestName=None):
       """
       Set up paths, reference files etc.
       """
       EDTestCasePluginUnit.__init__(self, "EDPluginISPyBv1_2", "EDPluginGroupISPyB-v1.1", _strTestName)

       self.__strDataPath = self.getPluginTestsDataHome()
       self.__strObtainedInputFile = "XSDataInputISPyBv1_2.xml"

       self.__strObtainedScreening = "XSDataISPyBScreening.xml"
       self.__strObtainedScreeningInput = "XSDataISPyBScreeningInput.xml"
       self.__strObtainedScreeningOutputContainer = "XSDataISPyBScreeningOutputContainer.xml"
       self.__strObtainedScreeningRank = "XSDataISPyBScreeningRank.xml"
       self.__strObtainedScreeningRankSet = "XSDataISPyBScreeningRankSet.xml"
       self.__strObtainedScreeningFile = "XSDataISPyBScreeningFile.xml"

       self.__strReferenceInputScreening = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screening.xml")
       self.__strReferenceInputScreeningInput = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screeningInput.xml")
       self.__strReferenceInputScreeningOutputContainer = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screeningOutputContainer.xml")
       self.__strReferenceInputScreeningRank = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screeningRank.xml")
       self.__strReferenceInputScreeningRankSet = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screeningRankSet.xml")
       self.__strReferenceInputScreeningFile = os.path.join(self.__strDataPath, "XSDataISPyBv1_2Input_reference_screeningFile.xml")

       self.__strReferenceInputFile = os.path.join(self.__strDataPath, "XSDataISPyBv1_2_UnitTest_reference.xml")

    def preProcess(self):
        """
        Delete old obtained files.
        """
        EDTestCasePluginUnit.preProcess(self)
        EDUtilsFile.deleteFile(self.__strObtainedInputFile)

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

        # Create XSDataISPyB objects

        xsDataISPyBImage = XSDataISPyBImage()
        xsDataISPyBImage.setFileName(XSDataString("test.img"))
        xsDataISPyBImage.setFileLocation(XSDataString("/tmp"))

        xsDataISPyBScreening = XSDataISPyBScreening()
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

        xsDataISPyBScreeningStrategyWedge = XSDataISPyBScreeningStrategyWedge()
        xsDataISPyBScreeningStrategyWedge.setWedgeNumber(XSDataInteger(1))
        xsDataISPyBScreeningStrategyWedge.setResolution(XSDataDouble(2.1))
        xsDataISPyBScreeningStrategyWedge.setCompleteness(XSDataDouble(90))
        xsDataISPyBScreeningStrategyWedge.setMultiplicity(XSDataDouble(1.5))
        xsDataISPyBScreeningStrategyWedge.setDoseTotal(XSDataDouble(40.5))
        xsDataISPyBScreeningStrategyWedge.setNumberOfImages(XSDataInteger(130))

        xsDataISPyBScreeningStrategySubWedge = XSDataISPyBScreeningStrategySubWedge()
        xsDataISPyBScreeningStrategySubWedge.setSubWedgeNumber(XSDataInteger(1))
        xsDataISPyBScreeningStrategySubWedge.setRotationAxis(XSDataString("Omega"))
        xsDataISPyBScreeningStrategySubWedge.setAxisStart(XSDataDouble(0.0))
        xsDataISPyBScreeningStrategySubWedge.setAxisEnd(XSDataDouble(90.0))
        xsDataISPyBScreeningStrategySubWedge.setExposureTime(XSDataDouble(0.5))
        xsDataISPyBScreeningStrategySubWedge.setTransmission(XSDataDouble(100.0))
        xsDataISPyBScreeningStrategySubWedge.setNumberOfImages(XSDataInteger(130))

        xsDataISPyBScreeningStrategyWedgeContainer = XSDataISPyBScreeningStrategyWedgeContainer()
        xsDataISPyBScreeningStrategyWedgeContainer.setScreeningStrategyWedge(xsDataISPyBScreeningStrategyWedge)
        xsDataISPyBScreeningStrategyWedgeContainer.getScreeningStrategySubWedge().append(xsDataISPyBScreeningStrategySubWedge)

        xsDataISPyBScreeningStrategyContainer = XSDataISPyBScreeningStrategyContainer()
        xsDataISPyBScreeningStrategyContainer.setScreeningStrategy(xsDataISPyBScreeningStrategy)
        xsDataISPyBScreeningStrategyContainer.getScreeningStrategyWedgeContainer().append(xsDataISPyBScreeningStrategyWedgeContainer)

        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningOutputContainer.setScreeningOutput(xsDataISPyBScreeningOutput)
        xsDataISPyBScreeningOutputContainer.getScreeningOutputLattice().append(xsDataISPyBScreeningOutputLattice)
        xsDataISPyBScreeningOutputContainer.getScreeningStrategyContainer().append(xsDataISPyBScreeningStrategyContainer)

        xsDataISPyBScreeningRank = XSDataISPyBScreeningRank()
        xsDataISPyBScreeningRank.setRankValue(XSDataDouble(1.4))
        xsDataISPyBScreeningRank.setRankInformation(XSDataString("This is the only one"))

        xsDataISPyBScreeningRankSet = XSDataISPyBScreeningRankSet()
        xsDataISPyBScreeningRankSet.setRankEngine(XSDataString("ISPyB"))

        xsDataISPyBScreeningFile = XSDataISPyBScreeningFile()
        xsDataISPyBScreeningFile.setFileType(XSDataString("log"))
        xsDataISPyBScreeningFile.setDescription(XSDataString("Output log file"))

        # Write XSDataISPyB objects to files
        xsDataISPyBScreening.outputFile(self.__strObtainedScreening)
        xsDataISPyBScreeningInput.outputFile(self.__strObtainedScreeningInput)
        xsDataISPyBScreeningOutputContainer.outputFile(self.__strObtainedScreeningOutputContainer)
        xsDataISPyBScreeningRank.outputFile(self.__strObtainedScreeningRank)
        xsDataISPyBScreeningRankSet.outputFile(self.__strObtainedScreeningRankSet)
        xsDataISPyBScreeningFile.outputFile(self.__strObtainedScreeningFile)

        # Compare screening
        strInputScreeningExpected = self.readAndParseFile(self.__strReferenceInputScreening)
        xsDataScreeningExpected = XSDataInputISPyB.parseString(strInputScreeningExpected)
        strXMLScreeningExpected = xsDataScreeningExpected.marshal()

        strScreeningObtained = self.readAndParseFile(self.__strObtainedScreening)
        xsDataScreeningObtained = XSDataInputISPyB.parseString(strScreeningObtained)
        strXMLScreeningObtained = xsDataScreeningObtained.marshal()

        EDAssert.equal(strXMLScreeningExpected, strXMLScreeningObtained)

        #Compare screeningInput
        strInputScreeningInputExpected = self.readAndParseFile(self.__strReferenceInputScreeningInput)
        xsDataScreeningInputExpected = XSDataInputISPyB.parseString(strInputScreeningInputExpected)
        strXMLScreeningInputExpected = xsDataScreeningInputExpected.marshal()

        strScreeningInputObtained = self.readAndParseFile(self.__strObtainedScreeningInput)
        xsDataScreeningInputObtained = XSDataInputISPyB.parseString(strScreeningInputObtained)
        strXMLScreeningInputObtained = xsDataScreeningInputObtained.marshal()

        EDAssert.equal(strXMLScreeningInputExpected, strXMLScreeningInputObtained)

        #Compare screeningOutputContainer
        strInputScreeningOutputContainerExpected = self.readAndParseFile(self.__strReferenceInputScreeningOutputContainer)
        xsDataScreeningOutputContainerExpected = XSDataInputISPyB.parseString(strInputScreeningOutputContainerExpected)
        strXMLScreeningOutputContainerExpected = xsDataScreeningOutputContainerExpected.marshal()

        strScreeningOutputContainerObtained = self.readAndParseFile(self.__strObtainedScreeningOutputContainer)
        xsDataScreeningOutputContainerObtained = XSDataInputISPyB.parseString(strScreeningOutputContainerObtained)
        strXMLScreeningOutputContainerObtained = xsDataScreeningOutputContainerObtained.marshal()

        EDAssert.equal(strXMLScreeningOutputContainerExpected, strXMLScreeningOutputContainerObtained)

        #Compare screeningRank
        strInputScreeningRankExpected = self.readAndParseFile(self.__strReferenceInputScreeningRank)
        xsDataScreeningRankExpected = XSDataInputISPyB.parseString(strInputScreeningRankExpected)
        strXMLScreeningRankExpected = xsDataScreeningRankExpected.marshal()

        strScreeningRankObtained = self.readAndParseFile(self.__strObtainedScreeningRank)
        xsDataScreeningRankObtained = XSDataInputISPyB.parseString(strScreeningRankObtained)
        strXMLScreeningRankObtained = xsDataScreeningRankObtained.marshal()

        EDAssert.equal(strXMLScreeningRankExpected, strXMLScreeningRankObtained)

        #Compare screeningRankSet
        strInputScreeningRankSetExpected = self.readAndParseFile(self.__strReferenceInputScreeningRankSet)
        xsDataScreeningRankSetExpected = XSDataInputISPyB.parseString(strInputScreeningRankSetExpected)
        strXMLScreeningRankSetExpected = xsDataScreeningRankSetExpected.marshal()

        strScreeningRankSetObtained = self.readAndParseFile(self.__strObtainedScreeningRankSet)
        xsDataScreeningRankSetObtained = XSDataInputISPyB.parseString(strScreeningRankSetObtained)
        strXMLScreeningRankSetObtained = xsDataScreeningRankSetObtained.marshal()

        EDAssert.equal(strXMLScreeningRankSetExpected, strXMLScreeningRankSetObtained)

        #Compare screeningFile
        strInputScreeningFileExpected = self.readAndParseFile(self.__strReferenceInputScreeningFile)
        xsDataScreeningFileExpected = XSDataInputISPyB.parseString(strInputScreeningFileExpected)
        strXMLScreeningFileExpected = xsDataScreeningFileExpected.marshal()

        strScreeningFileObtained = self.readAndParseFile(self.__strObtainedScreeningFile)
        xsDataScreeningFileObtained = XSDataInputISPyB.parseString(strScreeningFileObtained)
        strXMLScreeningFileObtained = xsDataScreeningFileObtained.marshal()

        EDAssert.equal(strXMLScreeningFileExpected, strXMLScreeningFileObtained)

        self.cleanUp(edPluginISPyB)

    def process(self):
       """
       List of test methods
       """
       self.DEBUG("*** EDTestCasePluginUnitISPyBv1_2.process")
       self.addTestMethod(self.testConfigureOK)
       self.addTestMethod(self.testSetDataModelInput)

if __name__ == '__main__':
    edTestCasePluginUnitISPyBv1_2 = EDTestCasePluginUnitISPyBv1_2("EDTestCasePluginUnitISPyBv1_2")
    edTestCasePluginUnitISPyBv1_2.execute()

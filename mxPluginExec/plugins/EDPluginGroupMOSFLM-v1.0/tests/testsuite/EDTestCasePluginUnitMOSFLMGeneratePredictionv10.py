#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDAssert             import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataWavelength


class EDTestCasePluginUnitMOSFLMGeneratePredictionv10(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginMOSFLMGeneratePredictionv10", "EDPluginGroupMOSFLM-v1.0", _edStringTestName)

        strDataImageDir = "images"
        self.strDataImagePath = os.path.join(self.getTestsDataHome(), strDataImageDir)

        stringPluginTestDataHome = self.getPluginTestsDataHome()
        self.strUnitTestDataHome = os.path.join(stringPluginTestDataHome, "unitTest")

        self.strReferenceInputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMv10InputGeneratePrediction_reference.xml")
        self.strReferenceDataOutputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMOutputGeneratePrediction_reference.xml")



    def generateDataMOSFLMInputGeneratePrediction(self):
        """
        """
        from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
        xsDataMOSFLMBeamPosition = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeamPosition.setX(XSDataLength(102.5))
        xsDataMOSFLMBeamPosition.setY(XSDataLength(104.7))

        from XSDataMOSFLMv10 import XSDataMOSFLMDetector
        xsDataMOSFLMDetector = XSDataMOSFLMDetector()
        xsDataMOSFLMDetector.setType(XSDataString("ADSC"))

        from XSDataMOSFLMv10 import XSDataMOSFLMImage
        xsDataMOSFLMImage1 = XSDataMOSFLMImage()
        xsDataMOSFLMImage1.setNumber(XSDataInteger(1))
        xsDataMOSFLMImage1.setRotationAxisStart(XSDataAngle(0.0))
        xsDataMOSFLMImage1.setRotationAxisEnd(XSDataAngle(1.0))

        from XSDataMOSFLMv10 import XSDataMOSFLMInputGeneratePrediction
        xsDataMOSFLMInputGeneratePrediction = XSDataMOSFLMInputGeneratePrediction()
        xsDataMOSFLMInputGeneratePrediction.setDistance(XSDataLength(198.4))
        xsDataMOSFLMInputGeneratePrediction.setWavelength(XSDataWavelength(0.9340))
        xsDataMOSFLMInputGeneratePrediction.setBeam(xsDataMOSFLMBeamPosition)
        xsDataMOSFLMInputGeneratePrediction.setDetector(xsDataMOSFLMDetector)
        xsDataMOSFLMInputGeneratePrediction.setDirectory(XSDataString(self.strDataImagePath))
        xsDataMOSFLMInputGeneratePrediction.setTemplate(XSDataString("ref-testscale_1_###.img"))
        xsDataMOSFLMInputGeneratePrediction.setImage(xsDataMOSFLMImage1)

        return xsDataMOSFLMInputGeneratePrediction


    def testGenerateMOSFLMCommands(self):
        """
        """
        pluginGeneratePrediction = self.createPlugin()
        pluginGeneratePrediction.setScriptExecutable("cat")
        pluginGeneratePrediction.configure()
        xsDataMOSFLMInputGeneratePrediction = self.generateDataMOSFLMInputGeneratePrediction()
        pluginGeneratePrediction.setDataInput(xsDataMOSFLMInputGeneratePrediction)
        pluginGeneratePrediction.generateMOSFLMCommands()
        listCommandsReference = ['WAVELENGTH 0.934', 'DISTANCE 198.4', 'BEAM 102.5 104.7', 'DETECTOR ADSC', 'DIRECTORY ' + self.strDataImagePath, 'TEMPLATE ref-testscale_1_###.img', 'XGUI ON', 'IMAGE 1 PHI 0.000000 TO 1.000000', 'GO', 'PREDICT_SPOTS', 'CREATE_IMAGE PREDICTION ON BINARY TRUE FILENAME ' + pluginGeneratePrediction.getPredictionImageFileName(), 'RETURN', 'EXIT']
        listCommands = pluginGeneratePrediction.getListCommandExecution()
        #print listCommandsReference
        #print listCommands
        EDAssert.equal(listCommandsReference, listCommands)

        self.cleanUp(pluginGeneratePrediction)

    def testCreateDataMOSFLMOutputGeneratePrediction(self):
        """
        """
        pluginGeneratePrediction = self.createPlugin()
        pluginGeneratePrediction.setScriptExecutable("cat")
        pluginGeneratePrediction.configure()
        pluginGeneratePrediction.setPredictionImageFileName("prediction.jpg")
        stringBaseName = pluginGeneratePrediction.getBaseName()
        stringNewmatFile = os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMv10_autoindexMat_ok.txt")
        pluginGeneratePrediction.setNewmatFileName(stringNewmatFile)
        from XSDataMOSFLMv10 import XSDataMOSFLMInputGeneratePrediction
        xsDataMOSFLMInputGeneratePrediction = XSDataMOSFLMInputGeneratePrediction.parseFile(os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMInputGeneratePrediction_reference.xml"))
        pluginGeneratePrediction.setDataInput(xsDataMOSFLMInputGeneratePrediction)
        xsDataMOSFLMOutputGeneratePrediction = pluginGeneratePrediction.createDataMOSFLMOutputGeneratePrediction()
        stringImagePath = xsDataMOSFLMOutputGeneratePrediction.getPredictionImage().getPath().getValue()
        stringReferenceXML = self.readAndParseFile(self.strReferenceDataOutputFile)
        from XSDataMOSFLMv10 import XSDataMOSFLMOutputGeneratePrediction
        xsDataMOSFLMOutputGeneratePredictionReference = XSDataMOSFLMOutputGeneratePrediction.parseString(stringReferenceXML)
        xsDataImage = xsDataMOSFLMOutputGeneratePredictionReference.getPredictionImage()
        xsDataImage.setPath(XSDataString(stringImagePath))
        xsDataMOSFLMOutputGeneratePredictionReference.setPredictionImage(xsDataImage)
        # Replace path to log file since it cannot be determined by the unit test
        xsDataMOSFLMOutputGeneratePrediction.setPathToLogFile(XSDataFile(XSDataString("MOSFLMGeneratePredictionv10.log")))        
        EDAssert.equal(xsDataMOSFLMOutputGeneratePredictionReference.marshal(), xsDataMOSFLMOutputGeneratePrediction.marshal())

        self.cleanUp(pluginGeneratePrediction)


    def testGetImageFileNameFromTemplate(self):
        pluginGeneratePrediction = self.createPlugin()
        EDAssert.equal("ref-test_1_001", pluginGeneratePrediction.getImageFileNameFromTemplate("ref-test_1_###.img", 1))
        EDAssert.equal("ref-test_1_099", pluginGeneratePrediction.getImageFileNameFromTemplate("ref-test_1_###.img", 99))
        EDAssert.equal("ref-test_1_999", pluginGeneratePrediction.getImageFileNameFromTemplate("ref-test_1_###.img", 999))
        EDAssert.equal("ref-test_1_9999", pluginGeneratePrediction.getImageFileNameFromTemplate("ref-test_1_####.img", 9999))
        EDAssert.equal("12345.001", pluginGeneratePrediction.getImageFileNameFromTemplate("12345.###", 1))


    def process(self):
        self.addTestMethod(self.testGenerateMOSFLMCommands)
        self.addTestMethod(self.testCreateDataMOSFLMOutputGeneratePrediction)
        self.addTestMethod(self.testGetImageFileNameFromTemplate)




if __name__ == '__main__':

    edTestCasePluginUnitMOSFLMGeneratePredictionv10 = EDTestCasePluginUnitMOSFLMGeneratePredictionv10("EDTestCasePluginUnitMOSFLMGeneratePredictionv10")
    edTestCasePluginUnitMOSFLMGeneratePredictionv10.execute()

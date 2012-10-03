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
from EDConfiguration import EDConfiguration

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataMatrixDouble

from XSDataMOSFLMv10 import XSDataCell
from XSDataMOSFLMv10 import XSDataMOSFLMNewmat
from XSDataMOSFLMv10 import XSDataMOSFLMMissettingsAngles
from XSDataMOSFLMv10 import XSDataMOSFLMInput
from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
from XSDataMOSFLMv10 import XSDataMOSFLMDetector


class EDTestCasePluginUnitMOSFLMv10(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginMOSFLMv10", "EDPluginGroupMOSFLM-v1.0", _strTestName)
        strPluginTestDataHome = self.getPluginTestsDataHome()
        self.strUnitTestDataHome = os.path.join(strPluginTestDataHome, "unitTest")



    def getReferenceDataMOSFLMNewmat(self):

        xsDataMOSFLMNewmat = XSDataMOSFLMNewmat()

        XSDataMatrixDoubleA = XSDataMatrixDouble()
        XSDataMatrixDoubleA.setM11(-0.00826416)
        XSDataMatrixDoubleA.setM12(0.00885073)
        XSDataMatrixDoubleA.setM13(0.00937013)
        XSDataMatrixDoubleA.setM21(0.00126554)
        XSDataMatrixDoubleA.setM22(0.01251971)
        XSDataMatrixDoubleA.setM23(-0.00845341)
        XSDataMatrixDoubleA.setM31(-0.01484956)
        XSDataMatrixDoubleA.setM32(-0.00385867)
        XSDataMatrixDoubleA.setM33(-0.00593515)
        xsDataMOSFLMNewmat.setAMatrix(XSDataMatrixDoubleA)

        xsDataMOSFLMMissettingsAngles = XSDataMOSFLMMissettingsAngles()
        xsDataMOSFLMMissettingsAngles.setPhix(XSDataAngle(1.000))
        xsDataMOSFLMMissettingsAngles.setPhiy(XSDataAngle(2.000))
        xsDataMOSFLMMissettingsAngles.setPhiz(XSDataAngle(3.000))
        xsDataMOSFLMNewmat.setMissettingAngles(xsDataMOSFLMMissettingsAngles)

        XSDataMatrixDoubleU = XSDataMatrixDouble()
        XSDataMatrixDoubleU.setM11(-0.4849475)
        XSDataMatrixDoubleU.setM12(0.5598049)
        XSDataMatrixDoubleU.setM13(0.6718960)
        XSDataMatrixDoubleU.setM21(0.0742629)
        XSDataMatrixDoubleU.setM22(0.7918670)
        XSDataMatrixDoubleU.setM23(-0.6061614)
        XSDataMatrixDoubleU.setM31(-0.8713845)
        XSDataMatrixDoubleU.setM32(-0.2440595)
        XSDataMatrixDoubleU.setM33(-0.4255866)
        xsDataMOSFLMNewmat.setUMatrix(XSDataMatrixDoubleU)

        xsDataCellRefined = XSDataCell()
        xsDataCellRefined.setLength_a(XSDataLength(54.8079))
        xsDataCellRefined.setLength_b(XSDataLength(59.0751))
        xsDataCellRefined.setLength_c(XSDataLength(66.9736))
        xsDataCellRefined.setAngle_alpha(XSDataAngle(91.0000))
        xsDataCellRefined.setAngle_beta(XSDataAngle(92.0000))
        xsDataCellRefined.setAngle_gamma(XSDataAngle(93.0000))
        xsDataMOSFLMNewmat.setRefinedCell(xsDataCellRefined)

        return xsDataMOSFLMNewmat


    def testGetDataMOSFLMNewmat(self):
        edPluginMOSFLMv10 = self.createPlugin()
        edPluginMOSFLMv10.setScriptExecutable("cat")
        edPluginMOSFLMv10.configure()
        strFilename = os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMv10_autoindexMat_test.txt")
        xsDataMOSFLMNewmat = edPluginMOSFLMv10.getDataMOSFLMNewmat(strFilename)
        xsDataMOSFLMNewmatReference = self.getReferenceDataMOSFLMNewmat()
        EDAssert.equal(xsDataMOSFLMNewmatReference.marshal(), xsDataMOSFLMNewmat.marshal(), "MOSFLM newmat")
        self.cleanUp(edPluginMOSFLMv10)


    def testWriteDataMOSFLMNewmat(self):
        edPluginMOSFLMv10 = self.createPlugin()
        edPluginMOSFLMv10.setScriptExecutable("cat")
        edPluginMOSFLMv10.configure()
        xsDataMOSFLMNewmatReference = self.getReferenceDataMOSFLMNewmat()
        strNewmatFilename = edPluginMOSFLMv10.getScriptBaseName() + "_testWriteDataMOSFLMNewmat.mat"
        edPluginMOSFLMv10.writeDataMOSFLMNewmat(xsDataMOSFLMNewmatReference, strNewmatFilename)
        self.cleanUp(edPluginMOSFLMv10)


    def testGenerateMOSFLMCommands(self):
        xsDataMOSFLMInput = XSDataMOSFLMInput()
        xsDataMOSFLMBeam = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeam.setX(XSDataLength(1.0))
        xsDataMOSFLMBeam.setY(XSDataLength(2.0))
        xsDataMOSFLMInput.setBeam(xsDataMOSFLMBeam)
        xsDataMOSFLMDetector = XSDataMOSFLMDetector()
        xsDataMOSFLMDetector.setType(XSDataString("ADSC"))
        xsDataMOSFLMInput.setDetector(xsDataMOSFLMDetector)
        xsDataMOSFLMInput.setDirectory(XSDataString("/tmp"))
        xsDataMOSFLMInput.setTemplate(XSDataString("testdata_1_###.img"))
        xsDataMOSFLMInput.setWavelength(XSDataWavelength(1.1111))
        xsDataMOSFLMInput.setDistance(XSDataLength(222.22))
        edPluginMOSFLMv10 = self.createPlugin()
        edPluginMOSFLMv10.setScriptExecutable("cat")
        edPluginMOSFLMv10.configure()
        edPluginMOSFLMv10.setXSDataInputClass(XSDataMOSFLMInput)
        edPluginMOSFLMv10.setDataInput(xsDataMOSFLMInput)
        edPluginMOSFLMv10.generateMOSFLMCommands()
        edListCommands = edPluginMOSFLMv10.getListCommandExecution()
        edListCommandsReference = ['WAVELENGTH 1.1111', 'DISTANCE 222.22', 'BEAM 1.0 2.0', 'DETECTOR ADSC', 'DIRECTORY /tmp', 'TEMPLATE testdata_1_###.img']
        EDAssert.equal(edListCommandsReference, edListCommands, "MOSFLM commands")
        self.cleanUp(edPluginMOSFLMv10)


    def testReversephiConfiguration(self):
        strPathToTestConfigFile = os.path.join(self.strUnitTestDataHome, "XSConfiguration_reversephi.xml")
        edConfiguration = EDConfiguration(strPathToTestConfigFile)
        xsPluginItem = edConfiguration.getXSConfigurationItem("EDPluginMOSFLMv10")
        xsDataMOSFLMInput = XSDataMOSFLMInput()
        xsDataMOSFLMBeam = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeam.setX(XSDataLength(1.0))
        xsDataMOSFLMBeam.setY(XSDataLength(2.0))
        xsDataMOSFLMInput.setBeam(xsDataMOSFLMBeam)
        xsDataMOSFLMDetector = XSDataMOSFLMDetector()
        xsDataMOSFLMDetector.setType(XSDataString("ADSC"))
        xsDataMOSFLMInput.setDetector(xsDataMOSFLMDetector)
        xsDataMOSFLMInput.setDirectory(XSDataString("/tmp"))
        xsDataMOSFLMInput.setTemplate(XSDataString("testdata_1_###.img"))
        xsDataMOSFLMInput.setWavelength(XSDataWavelength(1.1111))
        xsDataMOSFLMInput.setDistance(XSDataLength(222.22))
        edPluginMOSFLMv10 = self.createPlugin()
        edPluginMOSFLMv10.setScriptExecutable("cat")
        edPluginMOSFLMv10.setConfiguration(xsPluginItem)
        edPluginMOSFLMv10.configure()
        edPluginMOSFLMv10.setXSDataInputClass(XSDataMOSFLMInput)
        edPluginMOSFLMv10.setDataInput(xsDataMOSFLMInput)
        edPluginMOSFLMv10.generateMOSFLMCommands()
        edListCommands = edPluginMOSFLMv10.getListCommandExecution()
        edListCommandsReference = ['WAVELENGTH 1.1111', 'DISTANCE 222.22', 'BEAM 1.0 2.0', 'DETECTOR ADSC', 'DIRECTORY /tmp', 'TEMPLATE testdata_1_###.img', 'DETECTOR REVERSEPHI']
        EDAssert.equal(edListCommandsReference, edListCommands, "MOSFLM commands with reversephi configured")


    def testRasterConfiguration(self):
        strPathToTestConfigFile = os.path.join(self.strUnitTestDataHome, "XSConfiguration_raster.xml")
        edConfiguration = EDConfiguration(strPathToTestConfigFile)
        xsPluginItem = edConfiguration.getXSConfigurationItem("EDPluginMOSFLMv10")
        xsDataMOSFLMInput = XSDataMOSFLMInput()
        xsDataMOSFLMBeam = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeam.setX(XSDataLength(1.0))
        xsDataMOSFLMBeam.setY(XSDataLength(2.0))
        xsDataMOSFLMInput.setBeam(xsDataMOSFLMBeam)
        xsDataMOSFLMDetector = XSDataMOSFLMDetector()
        xsDataMOSFLMDetector.setType(XSDataString("ADSC"))
        xsDataMOSFLMInput.setDetector(xsDataMOSFLMDetector)
        xsDataMOSFLMInput.setDirectory(XSDataString("/tmp"))
        xsDataMOSFLMInput.setTemplate(XSDataString("testdata_1_###.img"))
        xsDataMOSFLMInput.setWavelength(XSDataWavelength(1.1111))
        xsDataMOSFLMInput.setDistance(XSDataLength(222.22))
        edPluginMOSFLMv10 = self.createPlugin()
        edPluginMOSFLMv10.setScriptExecutable("cat")
        edPluginMOSFLMv10.setConfiguration(xsPluginItem)
        edPluginMOSFLMv10.configure()
        edPluginMOSFLMv10.setXSDataInputClass(XSDataMOSFLMInput)
        edPluginMOSFLMv10.setDataInput(xsDataMOSFLMInput)
        edPluginMOSFLMv10.generateMOSFLMCommands()
        edListCommands = edPluginMOSFLMv10.getListCommandExecution()
        edListCommandsReference = ['WAVELENGTH 1.1111', 'DISTANCE 222.22', 'BEAM 1.0 2.0', 'DETECTOR ADSC', 'DIRECTORY /tmp', 'TEMPLATE testdata_1_###.img', 'RASTER 15 15 3 3 3']
        EDAssert.equal(edListCommandsReference, edListCommands, "MOSFLM commands with ratser configured")

    
    def process(self):
        self.addTestMethod(self.testGetDataMOSFLMNewmat)
        self.addTestMethod(self.testWriteDataMOSFLMNewmat)
        self.addTestMethod(self.testGenerateMOSFLMCommands)
        self.addTestMethod(self.testReversephiConfiguration)
        self.addTestMethod(self.testRasterConfiguration)





if __name__ == '__main__':

    edTestCasePluginUnitMOSFLMv10 = EDTestCasePluginUnitMOSFLMv10("EDTestCasePluginUnitMOSFLMv10")
    edTestCasePluginUnitMOSFLMv10.execute()

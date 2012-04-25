#
#    Project: mxPluginExec
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

import os, shutil

from EDAssert             import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsPath          import EDUtilsPath

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataWavelength

from XSDataMOSFLMv10 import XSDataMOSFLMOutputIndexing

class EDTestCasePluginUnitMOSFLMIndexingv10(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginMOSFLMIndexingv10")

        strDataImageDir = "images"
        self.strDataImagePath = os.path.join(self.getTestsDataHome(), strDataImageDir)

        strPluginTestDataHome = self.getPluginTestsDataHome()
        self.strUnitTestDataHome = os.path.join(strPluginTestDataHome, "unitTest")

        self.strReferenceDataInputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMInputIndexing_reference.xml")
        self.strReferenceDataOutputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMOutputIndexing_reference.xml")




    def generateDataMOSFLMInputIndexing(self):
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

        from XSDataMOSFLMv10 import XSDataMOSFLMImage
        xsDataMOSFLMImage2 = XSDataMOSFLMImage()
        xsDataMOSFLMImage2.setNumber(XSDataInteger(2))
        xsDataMOSFLMImage2.setRotationAxisStart(XSDataAngle(90.0))
        xsDataMOSFLMImage2.setRotationAxisEnd(XSDataAngle(91.0))

        from XSDataMOSFLMv10 import XSDataMOSFLMInputIndexing
        xsDataMOSFLMInputIndexing = XSDataMOSFLMInputIndexing()
        xsDataMOSFLMInputIndexing.setDistance(XSDataLength(198.4))
        xsDataMOSFLMInputIndexing.setWavelength(XSDataWavelength(0.9340))
        xsDataMOSFLMInputIndexing.setBeam(xsDataMOSFLMBeamPosition)
        xsDataMOSFLMInputIndexing.setDetector(xsDataMOSFLMDetector)
        xsDataMOSFLMInputIndexing.setDirectory(XSDataString(self.strDataImagePath))
        xsDataMOSFLMInputIndexing.setTemplate(XSDataString("ref-testscale_1_###.img"))
        xsDataMOSFLMInputIndexing.addImage(xsDataMOSFLMImage1)
        xsDataMOSFLMInputIndexing.addImage(xsDataMOSFLMImage2)

        return xsDataMOSFLMInputIndexing


    def testGenerateMOSFLMCommands(self):
        """
        """
        pluginIndexing = self.createPlugin()
        pluginIndexing.setScriptExecutable("cat")
        pluginIndexing.configure()
        xsDataMOSFLMInputIndexing = self.generateDataMOSFLMInputIndexing()
        pluginIndexing.setDataInput(xsDataMOSFLMInputIndexing)
        pluginIndexing.generateMOSFLMCommands()
        listCommandsReference = ['WAVELENGTH 0.934', 'DISTANCE 198.4', 'BEAM 102.5 104.7', 'DETECTOR ADSC', 'DIRECTORY ' + self.strDataImagePath, 'TEMPLATE ref-testscale_1_###.img', 'NEWMAT ' + pluginIndexing.getNewmatFileName(), 'AUTOINDEX DPS REFINE IMAGE 1 PHI 0.0 1.0', 'AUTOINDEX DPS REFINE IMAGE 2 PHI 90.0 91.0', 'GO', 'MOSAIC ESTIMATE 1', 'GO', 'MOSAIC ESTIMATE 2', 'GO']
        listCommands = pluginIndexing.getListCommandExecution()
        EDAssert.equal(listCommandsReference, listCommands)
        self.cleanUp(pluginIndexing)


    def testCreateDataMOSFLMOutputIndexing(self):
        """
        """
        pluginIndexing = self.createPlugin()
        pluginIndexing.setScriptExecutable("cat")
        pluginIndexing.configure()
        strBaseName = pluginIndexing.getBaseName()
        shutil.copyfile(os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMIndexingv10_outputDnaTables_ok.xml"), os.path.join(pluginIndexing.getWorkingDirectory(), strBaseName + "_dnaTables.xml"))
        strNewmatFile = os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMv10_autoindexMat_ok.txt")
        pluginIndexing.setNewmatFileName(strNewmatFile)
        xsDataMOSFLMOutputIndexing = pluginIndexing.createDataMOSFLMOutputIndexing()
        strReferenceXML = self.readAndParseFile(self.strReferenceDataOutputFile)
        xsDataMOSFLMOutputIndexingReference = XSDataMOSFLMOutputIndexing.parseString(strReferenceXML)
        #print len( strReferenceXML )
        #print len( xsDataMOSFLMOutputIndexing.marshal() )
        EDAssert.equal(xsDataMOSFLMOutputIndexingReference.marshal(), xsDataMOSFLMOutputIndexing.marshal())
        self.cleanUp(pluginIndexing)


    def testGenerateExecutiveSummary(self):
        """
        """
        pluginIndexing = self.createPlugin()
        pluginIndexing.setScriptExecutable("cat")
        pluginIndexing.configure()
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIndexing
        from XSDataMOSFLMv10 import XSDataMOSFLMOutputIndexing
        strMOSFLMInputIndexingXML = self.readAndParseFile(self.strReferenceDataInputFile)
        strMOSFLMOutputIndexingXML = self.readAndParseFile(self.strReferenceDataOutputFile)
        xsDataMOSFLMInputIndexing = XSDataMOSFLMInputIndexing.parseString(strMOSFLMInputIndexingXML)
        xsDataMOSFLMOutputIndexing = XSDataMOSFLMOutputIndexing.parseString(strMOSFLMOutputIndexingXML)
        pluginIndexing.setDataInput(xsDataMOSFLMInputIndexing)
        pluginIndexing.setDataOutput(xsDataMOSFLMOutputIndexing)
        pluginIndexing.generateExecutiveSummary(pluginIndexing)
        pluginIndexing.verboseScreenExecutiveSummary()
        self.cleanUp(pluginIndexing)

    def process(self):
        """
        """
        self.addTestMethod(self.testGenerateMOSFLMCommands)
        self.addTestMethod(self.testCreateDataMOSFLMOutputIndexing)
        self.addTestMethod(self.testGenerateExecutiveSummary)



if __name__ == '__main__':

    edTestCasePluginUnitMOSFLMIndexingv10 = EDTestCasePluginUnitMOSFLMIndexingv10("EDTestCasePluginUnitMOSFLMIndexingv10")
    edTestCasePluginUnitMOSFLMIndexingv10.execute()

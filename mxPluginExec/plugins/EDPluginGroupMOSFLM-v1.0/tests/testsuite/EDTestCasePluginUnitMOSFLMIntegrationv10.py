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

from EDVerbose            import EDVerbose
from EDAssert             import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsPath          import EDUtilsPath
from EDConfiguration import EDConfiguration

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from XSDataMOSFLMv10 import XSDataMOSFLMOutputIntegration
class EDTestCasePluginUnitMOSFLMIntegrationv10(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginMOSFLMIntegrationv10", "EDPluginGroupMOSFLM-v1.0", _strTestName)

        strPluginTestDataHome = self.getPluginTestsDataHome()
        self.strUnitTestDataHome = os.path.join(strPluginTestDataHome, "unitTest")

        self.strReferenceDataInputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMInputIntegration_reference.xml")
        self.strReferenceDataOutputFile = os.path.join(self.strUnitTestDataHome, "XSDataMOSFLMOutputIntegration_reference.xml")

        strDataImageDir = "images"
        self.strDataImagePath = os.path.join(self.getTestsDataHome(), strDataImageDir)


    def preProcess(self):
        EDVerbose.DEBUG ("*** EDTestCaseEDPluginMOSFLMIntegrationv10.preProcess")



    def testGenerateMOSFLMIntegrationCommands(self):
        strPathToTestConfigFile = os.path.join(self.strUnitTestDataHome, "XSConfiguration_unitTest.xml")
        edConfiguration = EDConfiguration(strPathToTestConfigFile)
        edConfiguration.load()
        xsPluginItem = edConfiguration.getPluginItem("EDPluginMOSFLMIntegrationv10")
        pluginIntegration = self.createPlugin()
        pluginIntegration.setScriptExecutable("cat")
        pluginIntegration.setConfiguration(xsPluginItem)
        pluginIntegration.configure()
        strXMLInputData = self.readAndParseFile (self.strReferenceDataInputFile)
        pluginIntegration.setDataInput(strXMLInputData)
        pluginIntegration.generateMOSFLMCommands()
        listCommandExecution = pluginIntegration.getListCommandExecution()
        listCommandReference = ['WAVELENGTH 0.934', 'DISTANCE 198.440994', 'BEAM 102.478996 104.8862', 'DETECTOR ADSC', 'DIRECTORY ' + self.strDataImagePath, 'TEMPLATE ref-testscale_1_###.img', 'SYMMETRY P222', 'MATRIX ' + pluginIntegration.getScriptBaseName() + '_matrix.mat', 'MOSAIC 0.75', 'HKLOUT process_1_1.mtz', 'PROCESS 1 TO 1 START 0.000000 ANGLE 1.000000', 'BEST ON', 'GO', 'BEST OFF']
        EDAssert.equal(listCommandReference, listCommandExecution)


    def testCreateDataMOSFLMOutputIntegration(self):
        pluginIntegration = self.createPlugin()
        pluginIntegration.setScriptExecutable("cat")
        pluginIntegration.configure()
        strBaseName = pluginIntegration.getBaseName()
        shutil.copyfile(os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMIntegrationv10_bestfileDat_ok.txt"), os.path.join (pluginIntegration.getWorkingDirectory(), "bestfile.dat"))
        shutil.copyfile(os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMIntegrationv10_bestfilePar_ok.txt"), os.path.join (pluginIntegration.getWorkingDirectory(), "bestfile.par"))
        shutil.copyfile(os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMIntegrationv10_bestfileHKL_ok.txt"), os.path.join (pluginIntegration.getWorkingDirectory(), "bestfile.hkl"))
        shutil.copyfile(os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMIntegrationv10_outputDnaTables_ok.xml"), os.path.join(pluginIntegration.getWorkingDirectory(), strBaseName + "_dnaTables.xml"))
        strMatrixFile = os.path.join(self.strUnitTestDataHome, "EDPluginMOSFLMv10_autoindexMat_ok.txt")
        pluginIntegration.setMatrixFileName(strMatrixFile)
        xsDataMOSFLMIntegrationOutput = pluginIntegration.createDataMOSFLMOutputIntegration()
        # Fix problem with absolute path by replacing it with a fixed one
        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString("/tmp/EDPluginMOSFLMIntegrationv10_process_1_1.mtz"))
        xsDataMOSFLMIntegrationOutput.setGeneratedMTZFile(xsDataFile)
        strReferenceXML = self.readAndParseFile(self.strReferenceDataOutputFile)
        xsDataMOSFLMIntegrationOutputReference = XSDataMOSFLMOutputIntegration.parseString(strReferenceXML)
        EDAssert.equal(xsDataMOSFLMIntegrationOutputReference.marshal(), xsDataMOSFLMIntegrationOutput.marshal())


    def testGenerateExecutiveSummary(self):
        pluginIntegration = self.createPlugin()
        pluginIntegration.setScriptExecutable("cat")
        pluginIntegration.configure()
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIntegration
        strMOSFLMInputIntegrationXML = self.readAndParseFile(self.strReferenceDataInputFile)
        strMOSFLMOutputIntegrationXML = self.readAndParseFile(self.strReferenceDataOutputFile)
        xsDataMOSFLMInputIntegration = XSDataMOSFLMInputIntegration.parseString(strMOSFLMInputIntegrationXML)
        xsDataMOSFLMOutputIntegration = XSDataMOSFLMOutputIntegration.parseString(strMOSFLMOutputIntegrationXML)
        pluginIntegration.setDataInput(xsDataMOSFLMInputIntegration)
        pluginIntegration.setDataOutput(xsDataMOSFLMOutputIntegration)
        pluginIntegration.generateExecutiveSummary(pluginIntegration)
        pluginIntegration.verboseScreenExecutiveSummary()
        self.cleanUp(pluginIntegration)



    def process(self):
        self.addTestMethod(self.testGenerateMOSFLMIntegrationCommands)
        self.addTestMethod(self.testCreateDataMOSFLMOutputIntegration)
        self.addTestMethod(self.testGenerateExecutiveSummary)






if __name__ == '__main__':

    edTestCasePluginUnitMOSFLMIntegrationv10 = EDTestCasePluginUnitMOSFLMIntegrationv10("EDTestCasePluginUnitMOSFLMIntegrationv10")
    edTestCasePluginUnitMOSFLMIntegrationv10.execute()

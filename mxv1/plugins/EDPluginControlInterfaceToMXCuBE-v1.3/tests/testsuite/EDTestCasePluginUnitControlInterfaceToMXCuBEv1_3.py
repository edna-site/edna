#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import shutil

from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsPath                         import EDUtilsPath

from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataMXCuBEv1_3 import XSDataResultCharacterisation


class EDTestCasePluginUnitControlInterfaceToMXCuBEv1_3(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlInterfaceToMXCuBEv1_3")
        self.strDataPath = self.getPluginTestsDataHome()


    def preProcess(self):
        EDTestCasePluginUnit.preProcess(self)
        self.loadTestImage(["EDPluginMOSFLMGeneratePredictionv10-01_image.jpg",
                             "EDPluginMOSFLMGeneratePredictionv10-02_image.jpg" ])


    def testCreateDNAFileDirectoryPath(self):
        pluginMXCuBE = self.createPlugin()
        pluginMXCuBE.configure()
        strResultCharacterisationFileName = "XSDataResultCharacterisation_reference.xml"
        strPathToReferenceFile = os.path.join(self.getPluginTestsDataHome(),
                                                          strResultCharacterisationFileName)
        strXML = self.readAndParseFile(strPathToReferenceFile)
        xsDataResultCharacterisation = XSDataResultCharacterisation.parseString(strXML)
        strDNAFileDirectoryPath = pluginMXCuBE.createDNAFileDirectoryPath(xsDataResultCharacterisation)
        strDNAFileDirectoryPathExpected = os.path.join(EDUtilsPath.getEdnaHome(), "tests", "data", "images", "testscale_1_dnafiles")
        EDAssert.equal(strDNAFileDirectoryPathExpected, strDNAFileDirectoryPath)


    def testCreateOutputFileDictionary(self):
        strPathToCCP4iResult = os.path.join(self.getPluginTestsDataHome(),
                                                        "XSDataResultCCP4i_reference.xml")
        strXML = self.readAndParseFile(strPathToCCP4iResult)
        EDFactoryPluginStatic.loadModule("XSDataCCP4iv1_1")
        from XSDataCCP4iv1_1 import XSDataResultCCP4i
        xsDataResultCCP4i = XSDataResultCCP4i.parseString(strXML)
        xsDataStringListOfOutputFiles = xsDataResultCCP4i.getListOfOutputFiles()
        pluginMXCuBE = self.createPlugin()
        pluginMXCuBE.configure()
        strResultCharacterisationFileName = "XSDataResultCharacterisation_reference.xml"
        strPathToReferenceFile = os.path.join(self.getPluginTestsDataHome(),
                                                          strResultCharacterisationFileName)
        strXML = self.readAndParseFile(strPathToReferenceFile)
        xsDataResultCharacterisation = XSDataResultCharacterisation.parseString(strXML)
        strDNAFileDirectoryPath = pluginMXCuBE.createDNAFileDirectoryPath(xsDataResultCharacterisation)
        pluginMXCuBE.createDNAFileDirectory(strDNAFileDirectoryPath)
        xsDataDictionary = pluginMXCuBE.createOutputFileDictionary(xsDataResultCharacterisation, strDNAFileDirectoryPath)
        EDAssert.equal(False, xsDataDictionary is None)
        shutil.rmtree(strDNAFileDirectoryPath)


    def testSplitHeadDirectory(self):
        pluginMXCuBE = self.createPlugin()
        EDAssert.equal([None, None], pluginMXCuBE.splitHeadDirectory("/"))
        EDAssert.equal(["data", None], pluginMXCuBE.splitHeadDirectory("/data"))
        EDAssert.equal(["data", "visitor"], pluginMXCuBE.splitHeadDirectory("/data/visitor"))
        EDAssert.equal(["data", "visitor/mx415/id14eh2/20100212"], pluginMXCuBE.splitHeadDirectory("/data/visitor/mx415/id14eh2/20100212"))

    def testCreatePyArchDNAFilePath(self):
        pluginMXCuBE = self.createPlugin()
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/"))
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/data"))
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/data/visitor"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415", pluginMXCuBE.createPyArchDNAFilePath("/data/visitor/mx415/id14eh2"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212", pluginMXCuBE.createPyArchDNAFilePath("/data/visitor/mx415/id14eh2/20100212"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1", pluginMXCuBE.createPyArchDNAFilePath("/data/visitor/mx415/id14eh2/20100212/1"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1/2", pluginMXCuBE.createPyArchDNAFilePath("/data/visitor/mx415/id14eh2/20100212/1/2"))
        # Test with inhouse account...
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/"))
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/data"))
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2"))
        EDAssert.equal(None, pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2/inhouse"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232", pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2/inhouse/opid232"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525", pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2/inhouse/opid232/20100525"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1", pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2/inhouse/opid232/20100525/1"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1/2", pluginMXCuBE.createPyArchDNAFilePath("/data/id23eh2/inhouse/opid232/20100525/1/2"))



    def process(self):
        self.addTestMethod(self.testCreateDNAFileDirectoryPath)
        self.addTestMethod(self.testCreateOutputFileDictionary)
        self.addTestMethod(self.testSplitHeadDirectory)
        self.addTestMethod(self.testCreatePyArchDNAFilePath)




if __name__ == '__main__':

    edTestCasePluginUnitControlInterfaceToMXCuBEv1_3 = EDTestCasePluginUnitControlInterfaceToMXCuBEv1_3("EDTestCasePluginUnitControlInterfaceToMXCuBEv1_3")
    edTestCasePluginUnitControlInterfaceToMXCuBEv1_3.execute()


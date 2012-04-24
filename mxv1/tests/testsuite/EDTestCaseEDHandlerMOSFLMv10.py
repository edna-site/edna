#
#    Project: EDNA MXv1
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
Test case for EDHandlerMOSFLMv10.
"""

import os

from EDAssert      import EDAssert
from EDTestCase    import EDTestCase
from EDUtilsTest   import EDUtilsTest
from EDUtilsPath   import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDTestCaseEDHandlerMOSFLMv10(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        strMXv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerMOSFLMv10"
        self.m_strDataPath = os.path.join(strMXv1DataHome, strDataDir)


    def testGenerateXSDataMOSFLMInputIndexing(self):
        strFilename = "XSDataIndexingInput_reference.xml"
        strPath = os.path.join(self.m_strDataPath, strFilename)
        strXMLIndexingInput = EDUtilsTest.readAndParseFile(strPath)
        from XSDataMXv1 import XSDataIndexingInput
        xsDataIndexingInput = XSDataIndexingInput.parseString(strXMLIndexingInput)
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        xsDataMOSFLMInputIndexing = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(xsDataIndexingInput)
        xsDataMOSFLMInputIndexing.exportToFile("XSDataMOSFLMInputIndexing_reference.xml")
        strReferenceFilename = "XSDataMOSFLMInputIndexing_reference.xml"
        strReferencePath = os.path.join(self.m_strDataPath, strReferenceFilename)
        strXMLMOSFLMInputIndexingReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIndexing
        xsDataMOSFLMInputIndexingReference = XSDataMOSFLMInputIndexing.parseString(strXMLMOSFLMInputIndexingReference)
        EDAssert.equal(xsDataMOSFLMInputIndexingReference.marshal(), xsDataMOSFLMInputIndexing.marshal())


    def testGenerateXSDataIndexingResult(self):
        strFilename = "XSDataMOSFLMOutputIndexing_reference.xml"
        strPath = os.path.join(self.m_strDataPath, strFilename)
        strXMLMOSFLMOutputIndexing = EDUtilsTest.readAndParseFile(strPath)
        from XSDataMOSFLMv10 import XSDataMOSFLMOutputIndexing
        xsDataMOSFLMOutputIndexing = XSDataMOSFLMOutputIndexing.parseString(strXMLMOSFLMOutputIndexing)
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        xsDataIndexingResult = EDHandlerXSDataMOSFLMv10.generateXSDataIndexingResult(xsDataMOSFLMOutputIndexing)
        strReferenceFilename = "XSDataIndexingResult_reference.xml"
        strReferencePath = os.path.join(self.m_strDataPath, strReferenceFilename)
        strXMLIndexingOutputReference = EDUtilsTest.readAndParseFile(strReferencePath)
        from XSDataMXv1 import  XSDataIndexingResult
        xsdataIndexingResultReference = XSDataIndexingResult.parseString(strXMLIndexingOutputReference)
        EDAssert.equal(xsdataIndexingResultReference.marshal(), xsDataIndexingResult.marshal())


    def testGenerateXSDataMOSFLMInputIntegration(self):
        strFilename = "XSDataIntegrationInput_reference.xml"
        strPath = os.path.join(self.m_strDataPath, strFilename)
        strXMLIntegrationInput = EDUtilsTest.readAndParseFile(strPath)
        from XSDataMXv1 import XSDataIntegrationInput
        xsDataIntegrationInput = XSDataIntegrationInput.parseString(strXMLIntegrationInput)
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        xsDataMOSFLMInputIntegration = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIntegration(xsDataIntegrationInput)
        strReferenceFilename = "XSDataMOSFLMInputIntegration_reference.xml"
        strReferencePath = os.path.join(self.m_strDataPath, strReferenceFilename)
        strXMLIntegrationInputReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIntegration
        xsDataMOSFLMInputIntegrationReference = XSDataMOSFLMInputIntegration.parseString(strXMLIntegrationInputReference)
        EDAssert.equal(xsDataMOSFLMInputIntegrationReference.marshal(), xsDataMOSFLMInputIntegration.marshal())


    def testGenerateXSDataIntegrationSubWedgeResult(self):
        strFilename = "XSDataMOSFLMOutputIntegration_reference.xml"
        strPath = os.path.join(self.m_strDataPath, strFilename)
        strXMLMOSFLMOutputIntegration = EDUtilsTest.readAndParseFile(strPath)
        from XSDataMOSFLMv10 import XSDataMOSFLMOutputIntegration
        xsDataMOSFLMOutputIntegration = XSDataMOSFLMOutputIntegration.parseString(strXMLMOSFLMOutputIntegration)
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        xsDataIntegrationSubWedgeResult = EDHandlerXSDataMOSFLMv10.generateXSDataIntegrationSubWedgeResult(xsDataMOSFLMOutputIntegration)
        strReferenceFilename = "XSDataIntegrationSubWedgeResult_reference.xml"
        strReferencePath = os.path.join(self.m_strDataPath, strReferenceFilename)
        strXMLIntegrationSubWedgeReference = EDUtilsTest.readAndParseFile(strReferencePath)
        from XSDataMXv1 import XSDataIntegrationSubWedgeResult
        xsDataIntegrationSubWedgeResult = XSDataIntegrationSubWedgeResult.parseString(strXMLIntegrationSubWedgeReference)
        EDAssert.equal(xsDataIntegrationSubWedgeResult.marshal(), xsDataIntegrationSubWedgeResult.marshal())



    def process(self):
        self.addTestMethod(self.testGenerateXSDataMOSFLMInputIndexing)
        self.addTestMethod(self.testGenerateXSDataIndexingResult)
        self.addTestMethod(self.testGenerateXSDataMOSFLMInputIntegration)
        self.addTestMethod(self.testGenerateXSDataIntegrationSubWedgeResult)



##############################################################################


if __name__ == '__main__':
    edTestCaseEDHandlerMOSFLMv10 = EDTestCaseEDHandlerMOSFLMv10("EDTestCaseEDHandlerMOSFLMv10")
    edTestCaseEDHandlerMOSFLMv10.execute()

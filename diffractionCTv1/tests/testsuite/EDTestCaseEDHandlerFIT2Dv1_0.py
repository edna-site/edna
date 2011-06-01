#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseEDHandlerLabelitv10.py 745 2009-05-29 10:26:40Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDUtilsFile                         import EDUtilsFile
from EDTestCase                          import EDTestCase
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath
from EDApplication                       import EDApplication


class EDTestCaseEDHandlerFIT2Dv1_0(EDTestCase):

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        strDiffractionCTv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerFIT2Dv1_0"
        self.m_strDataPath = os.path.abspath(os.path.join(strDiffractionCTv1DataHome, strDataDir))
        self.m_strReferenceOutputFile = os.path.abspath(os.path.join(self.m_strDataPath, "XSDataResultFIT2DCake_reference.xml"))



    def testGenerateXSDataInputFIT2DCake(self):
        strReferenceInputFile = os.path.join(self.m_strDataPath, "XSDataInputPowderDiffraction_reference.xml")
        strXMLInput = EDUtilsTest.readAndParseFile(strReferenceInputFile)
        EDApplication.loadModule("XSDataDiffractionCTv1")
        from XSDataDiffractionCTv1 import XSDataInputPowderIntegration
        xsDataInputPowderIntegration = XSDataInputPowderIntegration.parseString(strXMLInput)
        from EDHandlerXSDataFIT2Dv1_0 import EDHandlerXSDataFIT2Dv1_0
        edHandlerXSDataFIT2Dv1_0 = EDHandlerXSDataFIT2Dv1_0()
        xsDataInputFIT2DCake = edHandlerXSDataFIT2Dv1_0.getXSDataInputFIT2DCake(xsDataInputPowderIntegration)
        strReferencePath = os.path.join(self.m_strDataPath, "XSDataInputFIT2DCake_reference.xml")
        strXMLInputReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDApplication.loadModule("XSDataFIT2Dv1_0")
        from XSDataFIT2Dv1_0 import XSDataInputFIT2DCake
        xsDataInputFIT2DCakeReference = XSDataInputFIT2DCake.parseString(strXMLInputReference)
        EDAssert.equal(xsDataInputFIT2DCakeReference.marshal(), xsDataInputFIT2DCake.marshal())



    def testGenerateXSDataResultPowderIntegration(self):
        strReferenceInputFile = os.path.join(self.m_strDataPath, "XSDataResultFIT2DCake_reference.xml")
        strXMLInput = EDUtilsTest.readAndParseFile(strReferenceInputFile)
        EDApplication.loadModule("XSDataFIT2Dv1_0")
        from XSDataFIT2Dv1_0 import XSDataResultFIT2DCake
        xsDataResultFIT2DCake = XSDataResultFIT2DCake.parseString(strXMLInput)
        from EDHandlerXSDataFIT2Dv1_0 import EDHandlerXSDataFIT2Dv1_0
        edHandlerXSDataFIT2Dv1_0 = EDHandlerXSDataFIT2Dv1_0()
        xsDataResultPowderDiffraction = edHandlerXSDataFIT2Dv1_0.getXSDataResultPowderIntegration(xsDataResultFIT2DCake)
        strReferencePath = os.path.join(self.m_strDataPath, "XSDataResultPowderIntegration_reference.xml")
        strXMLResultReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDApplication.loadModule("XSDataDiffractionCTv1")
        from XSDataDiffractionCTv1 import XSDataResultPowderIntegration
        xsDataResultPowderIntegrationReference = XSDataResultPowderIntegration.parseString(strXMLResultReference)
        EDAssert.equal(xsDataResultPowderIntegrationReference.marshal(), xsDataResultPowderDiffraction.marshal())




    def process(self):
        self.addTestMethod(self.testGenerateXSDataInputFIT2DCake)
        self.addTestMethod(self.testGenerateXSDataResultPowderIntegration)



if __name__ == '__main__':

    edTestCaseEDHandlerLabelitv10 = EDTestCaseEDHandlerLabelitv10("EDTestCaseEDHandlerLabelitv10")
    edTestCaseEDHandlerLabelitv10.execute()


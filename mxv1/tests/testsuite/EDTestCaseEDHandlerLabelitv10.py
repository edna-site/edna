#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
#
#    Contributors:           Marie-Francoise Incardona (incardon@esrf.fr)
#                            Karl Levik (karl.levik@diamond.ac.uk)
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCase                          import EDTestCase
from EDUtilsTest                         import EDUtilsTest
from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDTestCaseEDHandlerLabelitv10(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        strMXv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerLabelitv10"
        self.strDataPath = os.path.join(strMXv1DataHome, strDataDir)
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataInputLabelit_reference.xml")
        self.strReferenceOutputFile = os.path.join(self.strDataPath, "XSDataResultLabelit_reference.xml")


    def testGenerateXSDataInputLabelit(self, _strFileNameXSDataIndexingInput_reference,
                                              _strFileNameXSDataLabelitInput_reference):
        """
        This method is testing the generation of the XSDataInputLabelit object given a XSDataIndexingInput object.
        """
        strPath = os.path.join(self.strDataPath, _strFileNameXSDataIndexingInput_reference)
        strXMLIndexingInput = EDUtilsTest.readAndParseFile(strPath)
        from XSDataMXv1 import XSDataIndexingInput
        xsDataIndexingInput = XSDataIndexingInput.parseString(strXMLIndexingInput)
        from EDHandlerXSDataLabelitv10 import EDHandlerXSDataLabelitv10
        xsDataInputLabelit = EDHandlerXSDataLabelitv10.generateXSDataInputLabelit(xsDataIndexingInput)
        strReferencePath = os.path.join(self.strDataPath, _strFileNameXSDataLabelitInput_reference)
        strXMLInputLabelitReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDFactoryPluginStatic.loadModule("XSDataLabelitv10")
        from XSDataLabelitv10 import XSDataInputLabelit
        xsDataInputLabelitReference = XSDataInputLabelit.parseString(strXMLInputLabelitReference)
        EDAssert.equal(xsDataInputLabelitReference.marshal(), xsDataInputLabelit.marshal())


    def testGenerateXSDataInputLabelit_reference(self):
        """
        This method tests the generation of an XSDataInputLabelit object given two reference 
        images collected more than 4 degrees apart.
        """
        self.testGenerateXSDataInputLabelit("XSDataIndexingInput_reference.xml",
                                             "XSDataInputLabelit_reference.xml")


    def testGenerateXSDataInputLabelit_oneImage(self):
        """
        This method tests the generation of an XSDataInputLabelit object given one reference image.
        """
        self.testGenerateXSDataInputLabelit("XSDataIndexingInput_oneImage.xml",
                                             "XSDataInputLabelit_oneImage.xml")


    def testGenerateXSDataInputLabelit_twoImagesLessThan4degrees(self):
        """
        This method tests the generation of an XSDataInputLabelit object given two reference 
        images collected less than 4 degrees apart.
        """
        self.testGenerateXSDataInputLabelit("XSDataIndexingInput_twoImagesLessThan4degrees.xml",
                                             "XSDataInputLabelit_oneImage.xml")


    def testGenerateXSDataIndexingResult(self):
        """
        This method tests the generation of an XSDataIndexingResult object given an XSDataResultLabelit object.
        """
        strPath = os.path.join(self.strDataPath, self.strReferenceOutputFile)
        strXMLResultLabelit = EDUtilsTest.readAndParseFile(strPath)
        EDFactoryPluginStatic.loadModule("XSDataLabelitv10")
        from XSDataLabelitv10 import XSDataResultLabelit
        xsDataResultLabelit = XSDataResultLabelit.parseString(strXMLResultLabelit)
        from EDHandlerXSDataLabelitv10 import EDHandlerXSDataLabelitv10
        xsDataIndexingResult = EDHandlerXSDataLabelitv10.generateXSDataIndexingResult(xsDataResultLabelit)
        strReferencePath = os.path.join(self.strDataPath, "XSDataIndexingResult_reference.xml")
        strIndexingResultReferenceXML = EDUtilsTest.readAndParseFile(strReferencePath)
        from XSDataMXv1 import XSDataIndexingResult
        xsDataIndexingResultReference = XSDataIndexingResult.parseString(strIndexingResultReferenceXML)
        EDAssert.equal(xsDataIndexingResultReference.marshal(), xsDataIndexingResult.marshal())



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testGenerateXSDataInputLabelit_reference)
        self.addTestMethod(self.testGenerateXSDataInputLabelit_oneImage)
        self.addTestMethod(self.testGenerateXSDataInputLabelit_twoImagesLessThan4degrees)
        self.addTestMethod(self.testGenerateXSDataIndexingResult)



if __name__ == '__main__':

    edTestCaseEDHandlerLabelitv10 = EDTestCaseEDHandlerLabelitv10("EDTestCaseEDHandlerLabelitv10")
    edTestCaseEDHandlerLabelitv10.execute()


#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseEDHandlerLabelitv10.py 1525 2010-05-12 12:54:17Z svensson $"
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


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCase                          import EDTestCase
from EDUtilsTest                         import EDUtilsTest
from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDTestCaseEDHandlerBestv1_2(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        strMXv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerBestv1_2"
        self.strDataPath = os.path.join(strMXv1DataHome, strDataDir)
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataInputStrategy_reference.xml")
        self.strReferenceOutputFile = os.path.join(self.strDataPath, "XSDataResultBestv1_2_reference.xml")


    def testGenerateXSDataInputBestv1_2(self, _strFileNameXSDataInputStrategy_reference, _strFileNameXSDataInputBest_reference):
        """
        This method is testing the generation of the XSDataInputBest object given a XSDataIndexingStrategy object.
        """
        strReferenceInputFile = os.path.join(self.strDataPath, _strFileNameXSDataInputStrategy_reference)
        strPath = os.path.join(self.strDataPath, strReferenceInputFile)
        from XSDataMXv1 import XSDataInputStrategy
        xsDataInputStrategy = XSDataInputStrategy.parseFile(strPath)
        from EDHandlerXSDataBestv1_2 import EDHandlerXSDataBestv1_2
        edHandlerXSDataBestv1_2 = EDHandlerXSDataBestv1_2()
        xsDataInputBestv1_2 = edHandlerXSDataBestv1_2.getXSDataInputBest(xsDataInputStrategy)
        strReferencePath = os.path.join(self.strDataPath, _strFileNameXSDataInputBest_reference)
        strXMLInputBestReference = EDUtilsTest.readAndParseFile(strReferencePath)
        EDFactoryPluginStatic.loadModule("XSDataBestv1_2")
        from XSDataBestv1_2 import XSDataInputBest
        xsDataInputBestReference = XSDataInputBest.parseString(strXMLInputBestReference)
        EDAssert.equal(xsDataInputBestReference.marshal(), xsDataInputBestv1_2.marshal())


    def testGenerateXSDataInputBestv1_2_reference(self):
        """
        Test with minimal information in the diffraction plan
        """
        self.testGenerateXSDataInputBestv1_2("XSDataInputStrategy_reference.xml", "XSDataInputBest_reference.xml")


    def testGenerateXSDataInputBestv1_2_diffractionPlan(self):
        """
        Test with more information in the diffraction plan + information in beam and goniostat
        """
        self.testGenerateXSDataInputBestv1_2("XSDataInputStrategy_diffractionPlan.xml", "XSDataInputBest_diffractionPlan.xml")


    def testGenerateXSDataInputBestv1_2_onlyDiffractionPlan(self):
        """
        Test with more information in the diffraction plan + information in beam and goniostat
        """
        self.testGenerateXSDataInputBestv1_2("XSDataInputStrategy_onlyDiffractionPlan.xml", "XSDataInputBest_onlyDiffractionPlan.xml")


    def testGenerateXSDataInputBestv1_2_withZeroTransmission(self):
        """
        Test with more information in the diffraction plan + information in beam and goniostat
        """
        self.testGenerateXSDataInputBestv1_2("XSDataInputStrategy_withZeroTransmission.xml", "XSDataInputBest_withZeroTransmission.xml")


    def process(self):
        self.addTestMethod(self.testGenerateXSDataInputBestv1_2_reference)
        self.addTestMethod(self.testGenerateXSDataInputBestv1_2_diffractionPlan)
        self.addTestMethod(self.testGenerateXSDataInputBestv1_2_onlyDiffractionPlan)
        self.addTestMethod(self.testGenerateXSDataInputBestv1_2_withZeroTransmission)



if __name__ == '__main__':

    edTestCaseEDHandlerBestv1_2 = EDTestCaseEDHandlerBestv1_2("EDTestCaseEDHandlerBestv1_2")
    edTestCaseEDHandlerBestv1_2.execute()


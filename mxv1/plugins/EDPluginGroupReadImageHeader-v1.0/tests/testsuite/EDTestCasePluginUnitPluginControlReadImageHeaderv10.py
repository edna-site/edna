#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2014 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Michael Hellmig (michael.hellmig@bessy.de)
# 							 Marie-Francoise Incardona (incardon@esrf.fr)
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import shutil
import tempfile


from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsPath                         import EDUtilsPath
from EDUtilsFile                         import EDUtilsFile

class EDTestCasePluginUnitPluginControlReadImageHeaderv10(EDTestCasePluginUnit):


    def __init__(self, _strTestName="EDPluginControlReadImageHeaderv10"):
        EDTestCasePluginUnit.__init__(self, _strTestName)


    def testDetermineImageType(self):
        edPluginControlReadImageHeaderv10 = self.createPlugin()
        # Test 1 : ADSC 
        self.loadTestImage([ "testscale_1_001.img" ])
        strImage1 = os.path.join(self.getTestsDataImagesHome(), "testscale_1_001.img")
        strType1 = edPluginControlReadImageHeaderv10.determineImageType(strImage1)
        EDAssert.equal(strType1, "ADSC", "ADSC")
        # Test 2 : MAR CCD with .mccd suffix
        self.loadTestImage([ "ref-screentest-crystal1_1_001.mccd" ])
        strImage2 = os.path.join(self.getTestsDataImagesHome(), "ref-screentest-crystal1_1_001.mccd")
        strType2 = edPluginControlReadImageHeaderv10.determineImageType(strImage2)
        EDAssert.equal(strType2, "MARCCD", "MARCCD 1")
        # Test 3 : MAR CCD with .marccd suffix - copied from ref-screentest-crystal1_1_001.mccd
        strImage3 = tempfile.mktemp(suffix="_1_001.marccd", prefix="ref-screentest-crystal1_")
        shutil.copyfile(strImage2, strImage3)
        strType3 = edPluginControlReadImageHeaderv10.determineImageType(strImage3)
        EDAssert.equal(strType3, "MARCCD", "MARCCD 2")
        os.remove(strImage3)
        # Test 4 : Pilatus 2M CBF image
        self.loadTestImage([ "ref-2m_RNASE_1_0001.cbf" ])
        strImage1 = os.path.join(self.getTestsDataImagesHome(), "ref-2m_RNASE_1_0001.cbf")
        strType1 = edPluginControlReadImageHeaderv10.determineImageType(strImage1)
        EDAssert.equal(strType1, "Pilatus2M", "Pilatus2M")
        # Test 5 : Pilatus 6M CBF image
        self.loadTestImage([ "FAE_1_1_00001.cbf" ])
        strImage1 = os.path.join(self.getTestsDataImagesHome(), "FAE_1_1_00001.cbf")
        strType1 = edPluginControlReadImageHeaderv10.determineImageType(strImage1)
        EDAssert.equal(strType1, "Pilatus6M", "Pilatus6M")
        # Test 6 : Unknown image - created by the test
        strImage4 = tempfile.mktemp(suffix="_1_001.unknown", prefix="zeroes_")
        EDUtilsFile.writeFile(strImage4, "Dummy text string for EDTestCasePluginUnitPluginControlReadImageHeaderv10.testDetermineImageType")
        strType4 = edPluginControlReadImageHeaderv10.determineImageType(strImage4)
        EDAssert.equal(True, edPluginControlReadImageHeaderv10.isFailure(), "Not recognized format")
        os.remove(strImage4)


    def testDetermineExecReadImageHeaderPluginName(self):
        edPluginControlReadImageHeaderv10 = self.createPlugin()
        # Test 1 : ADSC 
        strType1 = "ADSC"
        strPluginName1 = edPluginControlReadImageHeaderv10.determineExecReadImageHeaderPluginName(strType1)
        EDAssert.equal(strPluginName1, "EDPluginExecReadImageHeaderADSCv10")
        # Test 2 : MAR CCD 
        strType2 = "MARCCD"
        strPluginName2 = edPluginControlReadImageHeaderv10.determineExecReadImageHeaderPluginName(strType2)
        EDAssert.equal(strPluginName2, "EDPluginExecReadImageHeaderMARCCDv10")
        # Test 3 : UNKNOWN 
        strType3 = "UNKNOWN"
        strPluginName3 = edPluginControlReadImageHeaderv10.determineExecReadImageHeaderPluginName(strType3)
        EDAssert.equal(True, edPluginControlReadImageHeaderv10.isFailure())





    def process(self):
        """
        """
        self.addTestMethod(self.testDetermineImageType)
        self.addTestMethod(self.testDetermineExecReadImageHeaderPluginName)


if __name__ == '__main__':

    edTestCasePluginUnitPluginControlReadImageHeaderv10 = EDTestCasePluginUnitPluginControlReadImageHeaderv10("EDTestCasePluginUnitPluginControlReadImageHeaderv10")
    edTestCasePluginUnitPluginControlReadImageHeaderv10.execute()


#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from EDTestCasePluginExecute            import EDTestCasePluginExecute
#from EDUtilsTest                        import EDUtilsTest
from XSDataDiffractionCTv1              import XSDataResultDiffractionCT
import EDFfileCompleter
from CIFfile import CIF
import os

class EDTestCasePluginExecuteControlDiffractionCTv1_0(EDTestCasePluginExecute):
    """
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginControlDiffractionCTv1_0", "EDPluginControlDCTPowderIntegration-v1.0", _strTestName)

        self.setDataInputFile(os.path.abspath(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputDiffractionCT_reference.xml")))

        self.setReferenceDataOutputFile(os.path.abspath(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultDiffractionCT_reference.xml")))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"



    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.edf", "flats0001.edf", "darks0001.edf", "frelon_spline_file_to_correct_SPD.spline" ])
        strPathToCifHeaders = (os.path.abspath(os.path.join(self.getPluginTestsDataHome(), "default_headers.cif")))
        cifDictDefaultHeaders = CIF()
        cifDictDefaultHeaders.loadCIF(strPathToCifHeaders)
        strImageDir = self.getTestsDataImagesHome()
        strPathToInputImage = os.path.abspath(os.path.join(strImageDir, "diff6105.edf"))
        strPathToDarkImage = os.path.abspath(os.path.join(strImageDir, "darks0001.edf"))
        strPathToFlatImage = os.path.abspath(os.path.join(strImageDir, "flats0001.edf"))
        strPathToSplineFile = os.path.abspath(os.path.join(strImageDir, "frelon_spline_file_to_correct_SPD.spline"))
        cifDictDefaultHeaders[ "_file_correction_image_dark-current" ] = strPathToDarkImage
        cifDictDefaultHeaders[ "_file_correction_image_flat-field" ] = strPathToFlatImage
        cifDictDefaultHeaders[ "_file_correction_spline_spatial-distortion" ] = strPathToSplineFile

        strPathToTestImage = os.path.abspath(os.path.join(strImageDir, "test.edf"))
        strPathToTestCif = os.path.abspath(os.path.join(strImageDir, "test.cif"))
        if os.path.isfile(strPathToTestImage):
            os.remove(strPathToTestImage)
        EDFfileCompleter.edf_keywords_completion(strPathToInputImage, cifDictDefaultHeaders, strPathToTestImage)
        cifDictDefaultHeaders.saveCIF(strPathToTestCif)


    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = plugin.getDataOutput().marshal() # EDUtilsTest.readAndParseFile ( self.m_edObtainedOutputDataFile )    
        EDVerbose.DEBUG("Checking obtained result...")


        xsDataResultReference = XSDataResultDiffractionCT.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()# XSDataResultDiffractionCT.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal())



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteControlDiffractionCTv1_0 = EDTestCasePluginExecuteControlDiffractionCTv1_0("EDTestCasePluginExecuteControlDiffractionCTv1_0")
    edTestCasePluginExecuteControlDiffractionCTv1_0.execute()

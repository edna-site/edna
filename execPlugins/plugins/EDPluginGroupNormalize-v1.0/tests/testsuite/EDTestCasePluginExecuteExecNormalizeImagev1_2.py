#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDUtilsArray                       import EDUtilsArray
from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from EDTestCasePluginExecute            import EDTestCasePluginExecute
from XSDataNormalizeImage               import XSDataResultNormalize
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")



class EDTestCasePluginExecuteExecNormalizeImagev1_2(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin NormalizeImagev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecNormalizeImagev1_2")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_NormalizeImage.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputNormalizeImage_reference_array.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultNormalizeImage_array.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "normaliseImageDark10.edf", "normaliseImageDark15.edf", "normaliseImageDark2.edf", "normaliseImageDark3.edf", "normaliseImageData10.edf", "normaliseImageData15.edf", "normaliseImageFlat2.edf", "normaliseImageFlat3.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        xsDataResultReference = XSDataResultNormalize.parseString(strExpectedOutput)
#        outputFileName = xsDataResultReference.getThumbnailPath().getPath().getValue()
#        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
#        if os.path.isfile(outputFileName):
#            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
#            os.remove(outputFileName)



    def testExecute(self):
        """
        """
        self.run()
#        plugin = self.getPlugin()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultNormalize.parseString(strExpectedOutput)
        xsDataResultObtained = XSDataResultNormalize.parseString(strObtainedOutput)

        #EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "Result XML are the same")

        npaReference = EDUtilsArray.getArray(xsDataResultReference.output)
        npaObtained = EDUtilsArray.getArray(xsDataResultObtained.output)
        EDAssert.arraySimilar(npaReference, npaObtained, "Arrays are the same", _fAbsMaxDelta=1e-6)
        EDAssert.equal(npaReference.dtype, npaObtained.dtype, "Datatypes are the same")
#        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        xsDataResultReference = XSDataResultExecThumbnail.parseString(strExpectedOutput)
#        outputFileName = xsDataResultReference.getThumbnailPath().getPath().getValue()
#        outputImage = Image.open(outputFileName)
#
#        referenceFileName = os.path.join(self.getPluginTestsDataHome(), os.path.basename(outputFileName))
#        referenceImage = Image.open(referenceFileName)
#



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testNormalizeImagev1_0instance = EDTestCasePluginExecuteExecNormalizeImagev1_2("EDTestCasePluginExecuteExecNormalizeImagev1_2")
    testNormalizeImagev1_0instance.execute()

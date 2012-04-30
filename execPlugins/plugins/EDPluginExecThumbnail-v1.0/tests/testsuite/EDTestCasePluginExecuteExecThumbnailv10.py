#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@esrf.eu)
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"

import os, sys
from EDVerbose                  import EDVerbose
from EDAssert                   import EDAssert
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataExecThumbnail        import XSDataInputExecThumbnail
from XSDataExecThumbnail        import XSDataResultExecThumbnail
from EDUtilsPath                import EDUtilsPath

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")

import numpy
import Image

class EDTestCasePluginExecuteExecThumbnailv10(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Thumbnailv10
    """

    def __init__(self):
        """
        Constructor of the Class Execute Test Plugin Exec fro thumbnails
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecThumbnailv10")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_Thumbnail.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputThumbnail_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultThumbnail_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0


    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)

        xsDataInput = XSDataInputExecThumbnail.parseString(self.readAndParseFile (self.getDataInputFile()))
        self.loadTestImage([ os.path.basename(xsDataInput.getInputImagePath().getPath().getValue())])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultExecThumbnail.parseString(strExpectedOutput)
        outputFileName = xsDataResultReference.getThumbnailPath().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)


    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultExecThumbnail.parseString(strExpectedOutput)
        xsDataResultObtained = XSDataResultExecThumbnail.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XML are the same")

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultExecThumbnail.parseString(strExpectedOutput)
        outputFileName = xsDataResultReference.getThumbnailPath().getPath().getValue()
        outputImage = Image.open(outputFileName)

        self.loadTestImage([os.path.basename(outputFileName)])
        referenceFileName = os.path.join(EDUtilsPath.EDNA_TESTIMAGES, os.path.basename(outputFileName))
        referenceImage = Image.open(referenceFileName)

        EDAssert.arraySimilar(numpy.asarray(outputImage), numpy.asarray(referenceImage), _strComment="Images are the same", _fAbsMaxDelta=5)
##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################
#
#
if __name__ == '__main__':
    testThumbnailv10instance = EDTestCasePluginExecuteExecThumbnailv10()
    testThumbnailv10instance.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer kieffer@esrf.fr
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
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, subprocess
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataExecVideo                     import XSDataInputExecVideo
from XSDataExecVideo                     import XSDataResultExecVideo



class EDTestCasePluginExecuteExecVideov10(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Videov10
    """

    def __init__(self):
        """
        """
        self.EXCLUDED = ["Playing", "Software:", "ID_FILENAME", "ID_CLIP_INFO_VALUE0", "load"]
        EDTestCasePluginExecute.__init__(self, "EDPluginExecVideov10")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                                          "XSConfiguration_Video.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputVideo_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultVideo_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"


    def preProcess(self):
        """
        PreProcess of the execution test: download a set of JPEG files from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/example-msmpeg4v2.avi 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "sample1_%04i.jpg" % i for i in range(50, 101)])
        edStringExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultExecVideo.parseString(edStringExpectedOutput)
        outputFileName = xsDataResultReference.getVideoPath().getPath().getValue()
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

        edStringExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        edStringObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultExecVideo.parseString(edStringExpectedOutput)
        xsDataResultObtained = XSDataResultExecVideo.parseString(edStringObtainedOutput)

        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")

################################################################################
# Identification of the video by its size
################################################################################

        edStringExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultExecVideo.parseString(edStringExpectedOutput)
        outputFileName = xsDataResultReference.getVideoPath().getPath().getValue()
        outputVideoSize = os.stat(outputFileName)[6]


        referenceFileName = os.path.join(self.getPluginTestsDataHome(), os.path.basename(outputFileName))
        referenceVideoSize = os.stat(referenceFileName)[6]

        EDAssert.equal(outputVideoSize, referenceVideoSize, "Identification of the video file by its size")
################################################################################
# Identification of the video by mplayer
################################################################################
        outputVideoLog = subprocess.Popen("mplayer  -identify -vo null -ao null -frames 0 2>/dev/null " + outputFileName, stdout=subprocess.PIPE, shell=True).stdout.readlines()
        outputVideoSummary = ""

        for oneLine in outputVideoLog:
            if oneLine.strip() != "":
                if not oneLine.split()[0].split("=")[0] in self.EXCLUDED:
                    outputVideoSummary += oneLine

        referenceVideoLog = subprocess.Popen("mplayer  -identify -vo null -ao null -frames 0 2>/dev/null " + referenceFileName, stdout=subprocess.PIPE, shell=True).stdout.readlines()
        referenceVideoSummary = ""
        for oneLine in referenceVideoLog:
            if oneLine.strip() != "":
                if not oneLine.split()[0].split("=")[0] in self.EXCLUDED:
                    referenceVideoSummary += oneLine

        EDAssert.strAlmostEqual(outputVideoSummary, referenceVideoSummary, "Identification of the video by mplayer", _lstExcluded="edna")
#########################outputVideoSummary#####################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    testVideov10instance = EDTestCasePluginExecuteControlVideov10()
    testVideov10instance.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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


import os

from EDVerbose                  import EDVerbose
from XSDataExecVideo            import XSDataInputExecVideo
from XSDataExecVideo            import XSDataResultExecVideo
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from XSDataCommon               import XSDataFile
from XSDataCommon               import XSDataString


class EDPluginExecVideov10(EDPluginExecProcessScript):
    """
    This is an execution plugin arround mencoder to create a video from a set of images
    """

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputExecVideo)
#       Initialization of instance variable to their default
        self.fps = 25
        self.pyListInputImages = []
        self.bitrate = 800
        self.codec = "msmpeg4v2"
        self.videoFile = ""

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecVideov10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImagePath(), "inputImage list  is None")
        for oneXSDataFile in self.getDataInput().getInputImagePath():
            self.checkMandatoryParameters(oneXSDataFile.getPath().getValue(), "input Image does not exist" + oneXSDataFile.marshal())


    def preProcess(self, _edObject=None):
        """
        Extract the input data and runs the method generateMencoderCommands 
        """
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecVideov10.preProcess")

        for oneXSDataFile in self.getDataInput().getInputImagePath():
            inputFilename = oneXSDataFile.getPath().getValue()
            if not os.path.isfile(inputFilename):
                EDVerbose.ERROR("The input file provided is not a valid file: " + inputFilename)
                raise
            else:
                self.pyListInputImages.append(inputFilename)
        EDVerbose.DEBUG("*** input Images= %s" % self.pyListInputImages)

        if self.getDataInput().getVideoFPS() is not None:
            self.fps = self.getDataInput().getVideoFPS().getValue()

        if self.getDataInput().getVideoFPS() is not None:
            self.bitrate = int(self.getDataInput().getVideoBitRate().getValue())

        if self.getDataInput().getVideoFPS() is not None:
            self.codec = self.getDataInput().getVideoCodec().getValue()

        EDVerbose.DEBUG("*** FPS = %.1f\t BitRate = %i\tCodec= %s" % (self.fps, self.bitrate, self.codec))

        if self.getDataInput().getOutputPath() is not None:
            strOutputPath = self.getDataInput().getOutputPath().getPath().getValue()
            #Create structure of the destination directories ...
            if strOutputPath.endswith(os.sep) and not os.path.isdir(strOutputPath):
                os.makedirs(strOutputPath, int("777", 8))
            elif not os.path.isdir(os.path.dirname(strOutputPath)):
                os.makedirs(os.path.dirname(strOutputPath), int("777", 8))
            if os.path.isdir(strOutputPath):
                strDirname = strOutputPath
                strFilename = os.path.splitext(os.path.basename(self.pyListInputImages[0]))[0] + ".avi"
                if os.path.isfile(os.path.join(strDirname, strFilename)):
                    __, self.videoFile = tempfile.mkstemp(suffix=".avi", prefix=os.path.splitext(os.path.basename(self.pyListInputImages))[0] + "-", dir=strDirname)
                else:
                    self.videoFile = os.path.join(strDirname, strFilename)
            else:
                self.videoFile = strOutputPath
        else:
            self.videoFile = os.path.splitext(self.pyListInputImages)[0] + ".avi"
            if os.path.isfile(self.videoFile):
                self.videoFile = os.path.join(self.getWorkingDirectory(), "video.avi")
        EDVerbose.DEBUG("Output Video File: " + self.videoFile)
        self.generateMencoderCommands()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecVideov10.postProcess")
        # Create some output data
        xsDataResult = XSDataResultExecVideo()
        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(self.videoFile))
        xsDataResult.setVideoPath(xsDataFile)
        xsDataResult.setVideoPath(xsDataFile)
        xsDataResult.setVideoCodec(XSDataString(self.codec))
        self.setDataOutput(xsDataResult)

    def generateMencoderCommands(self):
        EDVerbose.DEBUG("EDPluginExecVideov10.generateMencoderCommands")
        pyStrOptions = "-ovc lavc -lavcopts vcodec=%s:vbitrate=%s -mf fps=%s -o %s " % (self.codec, self.bitrate, self.fps, self.videoFile)
        pyStrImageList = "mf://"
        for i in self.pyListInputImages:
            pyStrImageList += "%s," % i
        self.setScriptCommandline(pyStrOptions + pyStrImageList[:-1])

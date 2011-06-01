#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010 ESRF
#
#    Principal author:        Olof Svensson
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
from EDFactoryPluginStatic import EDFactoryPluginStatic

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "Copyrigth (c) 2010 ESRF"

import os, tempfile

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataInputPyarchThumbnailGenerator
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataResultPyarchThumbnailGenerator

EDFactoryPluginStatic.loadModule("XSDataExecThumbnail")
from XSDataExecThumbnail import XSDataInputExecThumbnail

EDFactoryPluginStatic.loadModule("EDPluginWaitFile")
from EDPluginWaitFile import EDPluginWaitFile
from XSDataWaitFilev1_0 import XSDataInputWaitFile


class EDPluginControlPyarchThumbnailGeneratorv1_0(EDPluginControl):
    """
    This control plugin uses EDPluginExecThumbnailv10 for creating two JPEG images from
    a diffraction image: one 1024x1024 (imagename.jpeg) and one 256x256 (imagename.thumb.jpeg).    
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputPyarchThumbnailGenerator)
        self.__strExecThumbnailPluginName = "EDPluginExecThumbnailv10"
        self.__edPluginExecThumbnail = None
        self.__strWaitFilePluginName = "EDPluginWaitFile"
        self.__edPluginWaitFile = None
        self.strOutputPath = None
        self.strOutputPathWithoutExtension = None
        self.__xsDataFilePathToThumbnail = None
        self.__xsDataFilePathToThumbnail2 = None
        self.__iExpectedSize = 1000000



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDiffractionImage(), "No diffraction image file path")



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.preProcess")
        # Check that the input image exists and is of the expected type
        strPathToDiffractionImage = self.getDataInput().getDiffractionImage().getPath().getValue()
        strImageFileNameExtension = os.path.splitext(strPathToDiffractionImage)[1]
        if not strImageFileNameExtension in [".img", ".marccd", ".mccd", ".cbf"]:
            print strImageFileNameExtension
            EDVerbose.error("Unknown image file name extension for pyarch thumbnail generator: %s" % strPathToDiffractionImage)
            self.setFailure()
        else:
            # Load the waitFile plugin
            xsDataInputWaitFile = XSDataInputWaitFile()
            xsDataInputWaitFile.setExpectedSize(XSDataInteger(self.__iExpectedSize))
            xsDataInputWaitFile.setExpectedFile(self.getDataInput().getDiffractionImage())
            if self.getDataInput().getWaitForFileTimeOut():
                xsDataInputWaitFile.setTimeOut(self.getDataInput().getWaitForFileTimeOut())
            self.__edPluginWaitFile = EDPluginWaitFile()
            self.__edPluginWaitFile.setDataInput(xsDataInputWaitFile)
            # Load the execution plugin
            self.__edPluginExecThumbnail = self.loadPlugin(self.__strExecThumbnailPluginName)
            xsDataInputExecThumbnail = XSDataInputExecThumbnail()
            xsDataInputExecThumbnail.setInputImagePath(self.getDataInput().getDiffractionImage())
            xsDataInputExecThumbnail.setLevelsInvert(XSDataBoolean(True))
            xsDataInputExecThumbnail.setLevelsMin(XSDataDoubleWithUnit(0.0))
            xsDataDoubleWithUnitLevelsMax = XSDataDoubleWithUnit(99.95)
            xsDataDoubleWithUnitLevelsMax.setUnit(XSDataString("%"))
            xsDataInputExecThumbnail.setLevelsMax(xsDataDoubleWithUnitLevelsMax)
            xsDataInputExecThumbnail.setFilterDilatation([XSDataInteger(4)])
            xsDataInputExecThumbnail.setLevelsColorize(XSDataBoolean(False))
            xsDataInputExecThumbnail.setThumbHeight(XSDataInteger(1024))
            xsDataInputExecThumbnail.setThumbWidth(XSDataInteger(1024))
            xsDataInputExecThumbnail.setKeepRatio(XSDataBoolean(False))
            # Output path
            strImageNameWithoutExt = os.path.basename(os.path.splitext(strPathToDiffractionImage)[0])
            strImageDirname = os.path.dirname(strPathToDiffractionImage)
            if self.getDataInput().getForcedOutputDirectory():
                strForcedOutputDirectory = self.getDataInput().getForcedOutputDirectory().getPath().getValue()
                if not os.access(strForcedOutputDirectory, os.W_OK):
                    EDVerbose.error("Cannot write to forced output directory : %s" % strForcedOutputDirectory)
                    self.setFailure()
                else:
                    self.strOutputPathWithoutExtension = os.path.join(strForcedOutputDirectory, strImageNameWithoutExt)
            else:
                # Try to store in the ESRF pyarch directory
                strOutputDirname = self.createPyarchFilePath(strImageDirname)
                # Check that output pyarch path exists and is writeable:
                bIsOk = False
                if strOutputDirname:
                    if not os.path.exists(strOutputDirname):
                        # Try to create the directory
                        try:
                            os.makedirs(strOutputDirname)
                            bIsOk = True
                        except BaseException, e:
                            EDVerbose.WARNING("Couldn't create the directory %s" % strOutputDirname)
                    elif os.access(strOutputDirname, os.W_OK):
                        bIsOk = True
                if not bIsOk:
                    EDVerbose.warning("Cannot write to pyarch directory: %s" % strOutputDirname)
                    strOutputDirname = tempfile.mkdtemp("", "EDPluginPyarchThumbnailv10_", "/tmp")
                    EDVerbose.warning("Writing thumbnail images to: %s" % strOutputDirname)
                self.strOutputPathWithoutExtension = os.path.join(strOutputDirname, strImageNameWithoutExt)
            self.strOutputPath = os.path.join(self.strOutputPathWithoutExtension + ".jpeg")
            xsDataInputExecThumbnail.setOutputPath(XSDataFile(XSDataString(self.strOutputPath)))
            self.__edPluginExecThumbnail.setDataInput(xsDataInputExecThumbnail)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.process")
        if self.__edPluginExecThumbnail and self.__edPluginWaitFile:
            self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
            self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
            self.__edPluginWaitFile.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPyarchThumbnailGenerator()
        if self.__xsDataFilePathToThumbnail:
            xsDataResult.setPathToJPEGImage(self.__xsDataFilePathToThumbnail)
        if self.__xsDataFilePathToThumbnail2:
            xsDataResult.setPathToThumbImage(self.__xsDataFilePathToThumbnail2)
        self.setDataOutput(xsDataResult)


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlID29CreateThumbnailv1_0.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlID29CreateThumbnailv1_0.doSuccessWaitFile")
        # Check that the image is really there
        # The image is here - make the first thumbnail
        if not self.__edPluginWaitFile.getDataOutput().getTimedOut().getValue():
            self.__edPluginExecThumbnail.connectSUCCESS(self.doSuccessExecThumbnail)
            self.__edPluginExecThumbnail.connectFAILURE(self.doFailureExecThumbnail)
            self.__edPluginExecThumbnail.executeSynchronous()
        else:
            EDVerbose.error("Time-out while waiting for image!")
            self.setFailure()


    def doFailureWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlID29CreateThumbnailv1_0.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlID29CreateThumbnailv1_0.doFailureWaitFile")
        # To be removed if failure of the exec plugin shouldn't make the control plugin to fail:
        self.setFailure()


    def doSuccessExecThumbnail(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail")
        # Retrieve the output path
        self.__xsDataFilePathToThumbnail = self.__edPluginExecThumbnail.getDataOutput().getThumbnailPath()
        # Run the plugin again, this time with the first thumbnail as input
        self.__edPluginExecThumbnail2 = self.loadPlugin(self.__strExecThumbnailPluginName)
        xsDataInputExecThumbnail = XSDataInputExecThumbnail()
        xsDataInputExecThumbnail.setInputImagePath(self.__edPluginExecThumbnail.getDataOutput().getThumbnailPath())
        xsDataInputExecThumbnail.setThumbHeight(XSDataInteger(256))
        xsDataInputExecThumbnail.setThumbWidth(XSDataInteger(256))
        xsDataInputExecThumbnail.setKeepRatio(XSDataBoolean(False))
        xsDataInputExecThumbnail.setOutputPath(XSDataFile(XSDataString(self.strOutputPathWithoutExtension + ".thumb.jpeg")))
        self.__edPluginExecThumbnail2.setDataInput(xsDataInputExecThumbnail)
        self.__edPluginExecThumbnail2.connectSUCCESS(self.doSuccessExecThumbnail2)
        self.__edPluginExecThumbnail2.connectFAILURE(self.doFailureExecThumbnail2)
        self.__edPluginExecThumbnail2.executeSynchronous()



    def doFailureExecThumbnail(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail")
        # To be removed if failure of the exec plugin shouldn't make the control plugin to fail:
        self.setFailure()


    def doSuccessExecThumbnail2(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail2")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail2")
        self.__xsDataFilePathToThumbnail2 = self.__edPluginExecThumbnail2.getDataOutput().getThumbnailPath()


    def doFailureExecThumbnail2(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail2")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail2")
        # To be removed if failure of the exec plugin shouldn't make the control plugin to fail:
        self.setFailure()


    def createPyarchFilePath(self, _strDNAFileDirectoryPath):
        """
        This method translates from a "visitor" path to a "pyarch" path:
        /data/visitor/mx415/id14eh1/20100209 -> /data/pyarch/id14eh1/mx415/20100209
        """
        strPyarchDNAFilePath = None
        listOfDirectories = _strDNAFileDirectoryPath.split(os.sep)
        listBeamlines = ["id14eh1", "id14eh2", "id14eh3", "id14eh4", "id23eh1", "id23eh2", "id29"]
        # Check that we have at least four levels of directories:
        if (len(listOfDirectories) > 4):
            strDataDirectory = listOfDirectories[ 1 ]
            strSecondDirectory = listOfDirectories[ 2 ]
            strProposal = None
            strBeamline = None
            if ((strDataDirectory == "data") and (strSecondDirectory == "visitor")):
                strProposal = listOfDirectories[ 3 ]
                strBeamline = listOfDirectories[ 4 ]
            elif ((strDataDirectory == "data") and (strSecondDirectory in listBeamlines)):
                strBeamline = strSecondDirectory
                strProposal = listOfDirectories[ 4 ]
            if (strProposal != None) and (strBeamline != None):
                strPyarchDNAFilePath = os.path.join(os.sep, "data")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, "pyarch")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strBeamline)
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strProposal)
                for strDirectory in listOfDirectories[ 5: ]:
                    strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strDirectory)
        if (strPyarchDNAFilePath is None):
            EDVerbose.WARNING("EDPluginControlPyarchThumbnailGeneratorv1_0.createPyArchFilePath: path not converted for pyarch: %s " % _strDNAFileDirectoryPath)
        return strPyarchDNAFilePath


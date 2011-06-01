# coding: utf8
#
#    Project: Photo-v1.0
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

import os, shutil
from EDVerbose                  import EDVerbose
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from XSDataPhotov1              import XSDataInputExecDcrawv1, XSDataResultExecDcrawv1
from XSDataCommon               import XSDataString, XSDataFile

class EDPluginExecDcrawv1_0(EDPluginExecProcessScript):
    """
    Plugin Exec to wrap dcraw
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputExecDcrawv1)

        self.__strRawFile = None
        self.__strOutputType = "ppm"
        self.__strOutputFile = None
        self.__bExportTiff = False
        self.__bExtracThumbnail = False
        self.__bWBAuto = False
        self.__bWBCamera = True
        self.__bLevelCamera = False
        self.__iInterpolate = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDcrawv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getRawImagePath(), "No Raw file provided")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDcrawv1_0.preProcess")
        self.__strRawFile = self.getDataInput().getRawImagePath().getPath().getValue()
        if self.getDataInput().getOutputPath() is not None:
            self.__strOutputFile = self.getDataInput().getOutputPath().getPath().getValue()
        if self.getDataInput().getExtractThumbnail() is not None:
            self.__bExtracThumbnail = (self.getDataInput().getExtractThumbnail().getValue() in [1, "true", "True", "TRUE", True])
########################################################################
# This option is incompatible with all others
########################################################################
        if self.__bExtracThumbnail is True:
            self.__bWBCamera = False
            self.__strOutputType = None #we cannot know what find of thumbnail is saved, can be jpeg, tiff or nothing !
        else:
            if  self.getDataInput().getExportTiff() is not None:
                self.__bExportTiff = (self.getDataInput().getExportTiff().getValue() in [1, "true", "True", "TRUE", True])
                if self.__bExportTiff:
                    self.__strOutputType = "tiff"
            if self.getDataInput().getWhiteBalanceAuto() is not None:
                self.__bWBAuto = (self.getDataInput().getWhiteBalanceAuto().getValue() in [1, "true", "True", "TRUE", True])
                if self.__bWBAuto is True: self.__bWBCamera = False
            if self.getDataInput().getWhiteBalanceFromCamera() is not None:
                self.__bWBCamera = (self.getDataInput().getWhiteBalanceFromCamera().getValue() in [1, "true", "True", "TRUE", True])
            if self.getDataInput().getLevelsFromCamera() is not None:
                self.__bLevelCamera = (self.getDataInput().getLevelsFromCamera().getValue()  in [1, "true", "True", "TRUE", True])
            if self.getDataInput().getInterpolationQuality() is not None:
                self.__iInterpolate = self.getDataInput().getInterpolationQuality().getValue()
        self.generateDcrawCommand()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDcrawv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultExecDcrawv1()
        xsdFile = XSDataFile()
        if self.__strOutputFile is not None:
            shutil.copyfile(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()), self.__strOutputFile)
            xsdFile.setPath(XSDataString(self.__strOutputFile))
        else:
            xsdFile.setPath(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())))
        xsDataResult.setOutputPath(xsdFile)
        if self.__strOutputType is not None:
            xsDataResult.setOutputFileType(XSDataString(self.__strOutputType))
        self.setDataOutput(xsDataResult)

    def generateDcrawCommand(self):
        strOptions = "-c" #export to stdout
        if self.__bExtracThumbnail is True:
            strOptions += " -e"
        if self.__bExportTiff is True:
             strOptions += " -T"
        if self.__bWBAuto is True:
            strOptions += " -a"
        if self.__bWBCamera is True:
            strOptions += " -w"
        if self.__bLevelCamera is True:
            strOptions += " -W"
        if self.__iInterpolate is not None:
            strOptions += " -q %s" % self.__iInterpolate
        strOptions += " %s" % self.__strRawFile

        EDVerbose.DEBUG("DCRaw Command LineOption is: %s" % strOptions)
        self.setScriptCommandline(strOptions)

#
#    Project: EDNA Exec Plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr)
#                            Jerome Kieffer (kieffer@esrf.fr)
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
import os, random
from EDVerbose    import EDVerbose
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from EDMessage       import EDMessage
from EDConfiguration import EDConfiguration
from EDUtilsFile     import EDUtilsFile
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataFIT2Dv1_0 import XSDataInputFIT2DCake
from XSDataFIT2Dv1_0 import XSDataResultFIT2DCake



class EDPluginFIT2DCakev1_0(EDPluginExecProcessScript):
    """
    The purpose of this plugin is to use FIT2D to do "cake" integration,
    i.e. azimutal integration of powder diffraction images. 
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputFIT2DCake)
        self.m_strOutputFilePath = None
        self.m_strCONF_PATH_TO_XVFB = "pathToXvfb"
        self.m_strPathToXvfb = None
        self.m_strCONF_ARGUMENTS_FOR_XVFB = "argumentsForXvfb"
        self.m_strArgumentsForXvfb = None
        self.addCompatibleVersion("PROGRAM  FIT2D  Version: V15.095")


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputFile(), "inputFile is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_0.preProcess")
        # Check that the input data and correction images are present
        xsDataInputFIT2DCake = self.getDataInput()
        pyStrPathToInputFile = xsDataInputFIT2DCake.getInputFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToInputFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToInputFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToDarkCurrentImageFile = xsDataInputFIT2DCake.getDarkCurrentImageFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToDarkCurrentImageFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToDarkCurrentImageFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToFlatFieldImageFile = xsDataInputFIT2DCake.getFlatFieldImageFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToFlatFieldImageFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToFlatFieldImageFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToSpatialDistortionFile = xsDataInputFIT2DCake.getSpatialDistortionFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToSpatialDistortionFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToSpatialDistortionFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        # Get path to Xvfb program
        pluginConfiguration = self.getConfiguration()
        if(pluginConfiguration is not None):
            self.m_strPathToXvfb = EDConfiguration.getStringParamValue(pluginConfiguration, self.m_strCONF_PATH_TO_XVFB)
            self.m_strArgumentsForXvfb = EDConfiguration.getStringParamValue(pluginConfiguration, self.m_strCONF_ARGUMENTS_FOR_XVFB)
        if (self.m_strPathToXvfb is None):
            strErrorMessage = EDMessage.ERROR_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 % (self.getPluginName() + ".preProcess", self.m_strCONF_PATH_TO_XVFB)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage

        self.generateFIT2DCommands()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_0.postProcess")
        # Create the output data
        xsDataResultFIT2DCake = XSDataResultFIT2DCake()
        if (self.m_strOutputFilePath is not None):
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.m_strOutputFilePath))
            xsDataResultFIT2DCake.setResultFile(xsDataFile)
        self.setDataOutput(xsDataResultFIT2DCake)


    def generateFIT2DCommands(self):
        """
        This method creates the FIT2D macro file for caking.
        """
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_0.generateFIT2DCommands")

#This is a patch of JKR preventing the system to re-use an existing display number 
        pyListOfDisplay = []
        if os.path.isdir("/tmp/.X11-unix"):
            for pystrOneLine in os.listdir("/tmp/.X11-unix"):
                if pystrOneLine[1:].isdigit():
                    pyListOfDisplay.append(int(pystrOneLine[1:]))
        else: #We do it in the ugly way
            pyfileout = os.popen("ps -ax -o cmd  | grep X")
            for pystrOneLine in pyfileout.readlines():
                for pyword in pystrOneLine.split():
                    if pyword[ 0 ] == ":":
                        if pyword[ 1: ].isdigit():
                            pyListOfDisplay.append(int(pyword[ 1: ]))
            pyfileout.close()

        iDisplayNumber = random.randrange(10, 1000)
        while  iDisplayNumber in  pyListOfDisplay:
            iDisplayNumber = random.randrange(10, 1000)

        EDVerbose.DEBUG("I selected for you the free display number %i. The list of occupied ones is: %s" % (iDisplayNumber, pyListOfDisplay))

        self.addListCommandPreExecution("rm -rf $HOME/.fit2d.ref")

        if (self.m_strArgumentsForXvfb is None):
            self.addListCommandPreExecution(self.m_strPathToXvfb + " :%d > Xvfb.log 2>&1 &" % iDisplayNumber)
        else:
            self.addListCommandPreExecution(self.m_strPathToXvfb + " " + self.m_strArgumentsForXvfb + " :%d > Xvfb.log 2>&1 &" % iDisplayNumber)

        self.addListCommandPreExecution("pid=$!")
        self.addListCommandPreExecution("export DISPLAY=:%d" % iDisplayNumber)

        self.addListCommandPostExecution("kill $pid > kill.log 2>&1 ")
        self.addListCommandPostExecution("sync")

        xsDataInputFIT2DCake = self.getDataInput()

        strMacroFileName = self.getBaseName() + ".fit2d"
        strOutputFileType = xsDataInputFIT2DCake.getOutputFileType().getValue()

        # Determine the image file name without path and suffix
        strInputImageFilePath = xsDataInputFIT2DCake.getInputFile().getPath().getValue()
        strInputFileNameWithoutSuffix = os.path.splitext(EDUtilsFile.getBaseName(strInputImageFilePath))[0]

        strOutputFileSuffix = "data"
        if  strOutputFileType == "PowderCIF":
             strOutputFileSuffix = "cif"
        elif  strOutputFileType == "CHIPLOT" :
             strOutputFileSuffix = "chi"

        strOutputFileName = strInputFileNameWithoutSuffix + "." + strOutputFileSuffix
        self.m_strOutputFilePath = os.path.join(self.getWorkingDirectory(), strOutputFileName)

        self.setScriptCommandline(" -dim%dx%d -mac%s" % (xsDataInputFIT2DCake.getBufferSizeX().getValue(), \
                                                           xsDataInputFIT2DCake.getBufferSizeY().getValue(), \
                                                           strMacroFileName))

        strMacro = "I ACCEPT\n"
        strMacro += "POWDER DIFFRACTION (2-D)\n"
        strMacro += "INPUT\n"
        strMacro += "%s\n" % strInputImageFilePath
        strMacro += "DARK CURRENT\n"
        if (xsDataInputFIT2DCake.getDarkCurrentImageFile() is None):
            strMacro += "NO\n"
        else:
            strMacro += "YES\n"
            strMacro += "DC FILE\n"
            strMacro += xsDataInputFIT2DCake.getDarkCurrentImageFile().getPath().getValue() + "\n"
        strMacro += "FLAT-FIELD\n"
        if (xsDataInputFIT2DCake.getFlatFieldImageFile() is None):
            strMacro += "NO\n"
        else:
            strMacro += "YES\n"
            strMacro += "FF FILE\n"
            strMacro += xsDataInputFIT2DCake.getFlatFieldImageFile().getPath().getValue() + "\n"
        strMacro += "FF SCALE\n"
        strMacro += "NO\n"
        strMacro += "FF MULTIPLIER\n"
        strMacro += "1.0\n"
        strMacro += "SPATIAL DIS.\n"
        if (xsDataInputFIT2DCake.getSpatialDistortionFile() is None):
            strMacro += "NO\n"
        else:
            strMacro += "YES\n"
            strMacro += "SD FILE\n"
            strMacro += xsDataInputFIT2DCake.getSpatialDistortionFile().getPath().getValue() + "\n"
        strMacro += "O.K.\n"
        strMacro += "CAKE\n"
        strMacro += "GRAPHICAL COORDINATE\n"
        strMacro += "           1\n"
        strMacro += " 1.0E+00\n"
        strMacro += " 1.0E+00\n"
        strMacro += "           0\n"
        strMacro += "           0\n"
        strMacro += "           1\n"
        strMacro += " 2.0E00\n"
        strMacro += " 2.0E00\n"
        strMacro += "           1\n"
        strMacro += " 3.0E00\n"
        strMacro += " 3.0E00\n"
        strMacro += "INTEGRATE\n"
#        strMacro += "X-PIXEL SIZE\n"
#        strMacro += "%f\n" % xsDataInputFIT2DCake.getPixelSizeX().getValue()
#        strMacro += "Y-PIXEL SIZE\n"
#        strMacro += "%f\n" % xsDataInputFIT2DCake.getPixelSizeY().getValue()
        strMacro += "DISTANCE\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getSampleToDetectorDistance().getValue()
        strMacro += "WAVELENGTH\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getWavelength().getValue()
        strMacro += "X-BEAM CENTRE\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getBeamCentreInPixelsX().getValue()
        strMacro += "Y-BEAM CENTRE\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getBeamCentreInPixelsY().getValue()
        strMacro += "TILT ROTATION\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getTiltRotation().getValue()
        strMacro += "ANGLE OF TILT\n"
        strMacro += "%f\n" % xsDataInputFIT2DCake.getAngleOfTilt().getValue()
        strMacro += "O.K.\n"
        strMacro += "START AZIMUTH\n"
        strMacro += "0.0\n"
        strMacro += "END AZIMUTH\n"
        strMacro += "360.0\n"
        strMacro += "INNER RADIUS\n"
        strMacro += "100.0\n"
        strMacro += "OUTER RADIUS\n"
        strMacro += "1500.0\n"
        strMacro += "SCAN TYPE\n"
        strMacro += "2-THETA\n"
        strMacro += "1 DEGREE AZ\n"
        strMacro += "NO\n"
        strMacro += "AZIMUTH BINS\n"
        strMacro += "1\n"
        strMacro += "RADIAL BINS\n"
        strMacro += "2048\n"
        strMacro += "CONSERVE INT.\n"
        strMacro += "NO\n"
        strMacro += "POLARISATION\n"
        strMacro += "NO\n"
        strMacro += "GEOMETRY COR.\n"
        strMacro += "YES\n"
        strMacro += "O.K.\n"
        strMacro += "EXIT\n"
        strMacro += "OUTPUT\n"
        strMacro += "%s\n" % strOutputFileType
        strMacro += "FILE NAME\n"
        strMacro += "%s\n" % strOutputFileName
        strMacro += "O.K.\n"
        strMacro += "EXCHANGE\n"
        strMacro += "EXIT\n"
        strMacro += "EXIT FIT2d\n"
        strMacro += "YES\n"

        self.writeProcessFile(strMacroFileName, strMacro)

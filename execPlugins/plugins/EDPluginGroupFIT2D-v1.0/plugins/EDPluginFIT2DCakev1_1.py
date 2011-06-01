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

import os, shutil
from EDVerbose      import EDVerbose
from XSDataCommon   import XSDataInput
from XSDataCommon   import XSDataResult
from XSDataCommon   import XSDataFile
from XSDataCommon   import XSDataString
from EDMessage      import EDMessage
from EDConfiguration import EDConfiguration
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataFIT2Dv1_0 import XSDataInputFIT2DCake
from XSDataFIT2Dv1_0 import XSDataResultFIT2DCake


# Use the EDF image header reader plugin for localising the EdfFile module
from EDApplication import EDApplication
EDApplication.loadModule("EDPluginEDFReadHeaderv1_0")
import  EdfFile as EDF
import  CIFfile
import  numpy as NP


class EDPluginFIT2DCakev1_1(EDPluginExecProcessScript):
    """
    The purpose of this plugin is to use FIT2D to do "cake" integration,
    i.e. azimutal integration of powder diffraction images.
    version 1.1 correspond to the first trial to get rid of the null-X-server  
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputFIT2DCake)
        self.m_strOutputFilePath = None
        self.addCompatibleVersion("PROGRAM  FIT2D  Version: V15.095")


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputFile(), "inputFile is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_1.preProcess")
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

# Rev 946
##Generate the image cleaned from the background and flatfield
#        edfImage=EDF.EdfFile(pyStrPathToInputFile)
#        npArrayImage=edfImage.GetData(0).astype("float32")
#        edfDark=EDF.EdfFile(pyStrPathToDarkCurrentImageFile)
#        Md=edfDark.GetData(0).astype("float32")
#        edfFlat=EDF.EdfFile( pyStrPathToFlatFieldImageFile )
#        Mf=edfFlat.GetData(0).astype("float32")
#        npaTmp = NP.zeros_like(npArrayImage)
#        npaNum = NP.maximum(npArrayImage-Md,NP.zeros_like(npArrayImage))
#        npaDen = NP.maximum(Mf-Md,NP.ones_like(npArrayImage))
#        npaTmp += NP.max( npaDen )
#        npaRes = npaTmp * npaNum / npaDen
#        
#        edfOutfile=EDF.EdfFile(os.path.join( self.getWorkingDirectory(),  "CleanedImage.edf") )
#        edfOutfile.WriteImage(edfImage.GetHeader(0), npaRes.astype("uint16"), Append=0)
##End Generate cleaned image
#Generate the image cleaned from the background and flatfield
        edfImage = EDF.EdfFile(pyStrPathToInputFile)
        npArrayImage = edfImage.GetData(0).astype("float32")
        edfDark = EDF.EdfFile(pyStrPathToDarkCurrentImageFile)
        Md = edfDark.GetData(0).astype("float32")
        edfFlat = EDF.EdfFile(pyStrPathToFlatFieldImageFile)
        Mf = edfFlat.GetData(0).astype("float32")
        #npaTmp = NP.zeros_like(npArrayImage)
        npaNum = npArrayImage - Md
        npaDen = Mf
#        npaTmp += NP.max( npaDen )
        npaRes = npaNum / npaDen

        edfOutfile = EDF.EdfFile(os.path.join(self.getWorkingDirectory(), "CleanedImage.edf"))
        edfOutfile.WriteImage(edfImage.GetHeader(0), npaRes.astype("float32"), Append=0)
#End Generate cleaned image
        self.generateFIT2DCommands()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_1.postProcess")
        #Remove the temporary data file
        os.remove(os.path.join(self.getWorkingDirectory(), "CleanedImage.edf"))
        os.remove(os.path.join(self.getWorkingDirectory(), "spline"))
        # Create the output data
        xsDataResultFIT2DCake = XSDataResultFIT2DCake()
        if (self.m_strOutputFilePath is not None):
            if os.path.splitext(self.m_strOutputFilePath)[1].lower() == ".cif" :
############read CHI plot file and convert it in cif cile if needed
                cif = CIFfile.CIF()
                cif.loadCHIPLOT(os.path.splitext(self.m_strOutputFilePath)[0] + ".chi")
                cif["_diffrn_radiation_wavelength"] = str(self.getDataInput().getWavelength().getValue())
                cif["_pd_instr_dist_spec/detc"] = str(self.getDataInput().getSampleToDetectorDistance().getValue())
                cif.saveCIF(self.m_strOutputFilePath)
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.m_strOutputFilePath))
            xsDataResultFIT2DCake.setResultFile(xsDataFile)
        self.setDataOutput(xsDataResultFIT2DCake)


    def generateFIT2DCommands(self):
        """
        This method creates the FIT2D macro file for caking.
        """
        EDVerbose.DEBUG("*** EDPluginFIT2DCakev1_1.generateFIT2DCommands")


        self.addListCommandPreExecution("rm -rf $HOME/.fit2d.ref")
        self.addListCommandPostExecution("sync")

        xsDataInputFIT2DCake = self.getDataInput()

        strMacroFileName = self.getBaseName() + ".fit2d"
        strOutputFileType = (xsDataInputFIT2DCake.getOutputFileType().getValue())

        # Determine the image file name without path and suffix
        strInputImageFilePath = xsDataInputFIT2DCake.getInputFile().getPath().getValue()
        strInputFileNameWithoutSuffix = os.path.splitext(os.path.basename(strInputImageFilePath))[0]

        strOutputFileSuffix = "data"
        if (strOutputFileType == "PowderCIF"):
             strOutputFileSuffix = "cif"
             strTmpOutputFileName = strInputFileNameWithoutSuffix + ".chi"

        elif (strOutputFileType == "CHIPLOT"):
             strOutputFileSuffix = "chi"
             strTmpOutputFileName = strInputFileNameWithoutSuffix + ".chi"

        strOutputFileName = strInputFileNameWithoutSuffix + "." + strOutputFileSuffix
        self.m_strOutputFilePath = os.path.join(self.getWorkingDirectory(), strOutputFileName)

        self.setScriptCommandline(" -nogr -key -dim%dx%d -mac%s" % (xsDataInputFIT2DCake.getBufferSizeX().getValue(), \
                                                           xsDataInputFIT2DCake.getBufferSizeY().getValue(), \
                                                            strMacroFileName))

        strMacro = "INPUT DATA\n"
        strMacro += "KLORA\n"
        strMacro += "CleanedImage.edf\n"
        strMacro += "1\nFIT\nPOWDER DIFFRACTION\nYES\n"
# Beam Center 
        strMacro += "%f\n" % xsDataInputFIT2DCake.getBeamCentreInPixelsX().getValue()
        strMacro += "%f\n" % xsDataInputFIT2DCake.getBeamCentreInPixelsY().getValue()
# size of the pixel in micorns (not needed as it will be re read afterwards)
        if xsDataInputFIT2DCake.getPixelSizeX() is not None:
             strMacro += "%f\n" % xsDataInputFIT2DCake.getPixelSizeX().getValue()
             strMacro += "%f\n" % xsDataInputFIT2DCake.getPixelSizeY().getValue()
        else:
             strMacro += "50\n50\n"
#Distance to detector
        strMacro += "%f\n" % xsDataInputFIT2DCake.getSampleToDetectorDistance().getValue()
#TILT PLANE ROTATION ANGLE (DEGREES)
        strMacro += "%f\n" % xsDataInputFIT2DCake.getTiltRotation().getValue()
#DETECTOR TILT ANGLE (DEGREES) (Range: -180.0000 to 180.0000)
        strMacro += "%f\n" % xsDataInputFIT2DCake.getAngleOfTilt().getValue()
#CORRECT FOR X-RAY BEAM POLARISATION [YES]:No
#BEAM POLARISATION (AT SAMPLE) (Range: -1.000000 to 1.000000)
# [0.990000]:0.99
        strMacro += "NO\n"
#TYPE OF LORENTZIAN CORRECTION TO APPLY
# [PARTIAL POWDER (2-THETA SCAN)]:None
        strMacro += "NO\n"
#PRODUCE EQUAL ANGLE PIXEL SCAN [YES]:yes
        strMacro += "YES\n"
#2 THETA SCAN ANGULAR PIXEL STEP (DEGREES)
# (Range: 1.000000E-03 to 10000.00) [3.600000E-02]:0.05
        strMacro += "0.05\n"
#TAKE ACCOUNT OF SPATIAL DISTORTION [NO]:yes
#Name of file for spatial distortion interpolation function
#FILE NAME []:spline
        if (xsDataInputFIT2DCake.getSpatialDistortionFile() is None):
             strMacro += "NO\n"
        else:
            strMacro += "YES\nspline\n"
            shutil.copyfile(xsDataInputFIT2DCake.getSpatialDistortionFile().getPath().getValue(), os.path.join(self.getWorkingDirectory(), "spline"))
#OVER-LOADED PIXEL VALUE (Range: 0.0 to 1.700000E+38)
# [99999.50]:65000
        strMacro += "65000\n"
#NUMBER OF ROWS OF DISTORTION FUNCTIONS TO CALCULATED IN A BLOCK
# (Range: 2 to 1001) [500]:
        strMacro += "500\n"
#SAVE DATA IN "POWDER DIFFRACTION STANDARD" FORMAT [YES]:no
#Fit sub-menu: ENTER COMMAND [EXIT]:exit
#Main menu: ENTER COMMAND [EXCHANGE]:no
#Main menu: ENTER COMMAND [OUTPUT DATA]:exchange
#Main menu: ENTER COMMAND [IMAGE]:output data
#FILE FORMAT [FIT2D STANDARD FORMAT]:chiplot
        strMacro += "NO\nEXIT\nNO\nEXCHANGE\nOUTPUT DATA\nCHIPLOT\n"
#Enter name of output file
#FILE NAME [output.chi]:output-non.chi
        strMacro += "%s\n" % strTmpOutputFileName
#OUTPUT ROWS [YES]:yes
#NUMBER OF ROW TO OUTPUT (Range: 1 to 1) [1]:1
#Main menu: ENTER COMMAND [INPUT DATA]:exit
#CONFIRM EXIT [NO]:yes
        strMacro += "YES\n1\nEXIT\nYES\n"


        self.writeProcessFile(strMacroFileName, strMacro)

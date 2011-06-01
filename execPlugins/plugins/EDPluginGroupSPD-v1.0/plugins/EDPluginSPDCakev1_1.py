# coding: utf8
#
#    Project: EDNA Exec Plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal authors:      Jérôme Kieffer (jerome.kieffer@esrf.eu)
#                            
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

"""
This is an alernative to the very first implementation of the SPD plugin for azimuthal integration.
It is no more used, just here for demonstration purpose

"""
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose      import  EDVerbose
from XSDataCommon   import  XSDataFile
from XSDataCommon   import  XSDataString
from EDMessage      import  EDMessage
from EDUtilsFile    import  EDUtilsFile
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataSPDv1_0  import  XSDataInputSPDCake
from XSDataSPDv1_0  import  XSDataResultSPDCake
from EDUtilsPlatform   import EDUtilsPlatform

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)
try:
    import numpy
except:
    EDVerbose.ERROR("Error in loading numpy, Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecThumbnailv10 \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")

from fabio.openimage import openimage

class EDPluginSPDCakev1_1(EDPluginExecProcessScript):
    """
    The purpose of this plugin is to use SPD to do "cake" azimuthal integration,
    i.e. azimutal integration of powder diffraction images. 
    
    The version 1.0 of EDPluginSPDCake will just call spd as strand alone version of the program, so this implementation is far from being optimal in performances.
    
    Few tips and tricks about SPD ...
  * When doing azimuthal integration, spd keeps the first axis in length (meter of detector) and not in 2Theta as expected (or Fit2D does). 
    This is why there is a numpy transformation with ArcTan in the post process with a subsequent rebinning.
  * This version includes a full 2pi azimuthal integration from SPD. This is the main difference with plugin v1_0  
  * Last but not least, there is currently NO tilt, only spline distortion of the image  
    
    """


    def __init__(self):
        """
        Constructor of the plugin: just do some simple initialization 
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSPDCake)
        self.m_strOutputFilePath = None
        self.outputDir = None
        self.addCompatibleVersion("spd version SPD = 1.1 SAXS = 2.436 EDF = 2.163")
        self.addCompatibleVersion("spd version SPD = 1.2 SAXS = 2.436 EDF = 2.171")


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginSPDCakev1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputFile(), "inputFile is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginSPDCakev1_1.preProcess")
        # Check that the input data and correction images are present
        xsDataInputSPDCake = self.getDataInput()
        pyStrPathToInputFile = xsDataInputSPDCake.getInputFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToInputFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToInputFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToDarkCurrentImageFile = xsDataInputSPDCake.getDarkCurrentImageFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToDarkCurrentImageFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToDarkCurrentImageFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToFlatFieldImageFile = xsDataInputSPDCake.getFlatFieldImageFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToFlatFieldImageFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToFlatFieldImageFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        pyStrPathToSpatialDistortionFile = xsDataInputSPDCake.getSpatialDistortionFile().getPath().getValue()
        if (not os.path.exists(pyStrPathToSpatialDistortionFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToSpatialDistortionFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage

        if xsDataInputSPDCake.getOutputDir() is not None:
            self.outputDir = xsDataInputSPDCake.getOutputDir().getPath().getValue()
            if not os.path.isdir(self.outputDir):
                os.makedirs(self.outputDir)

        self.generateSPDCommand()



    def postProcess(self, _edObject=None):

        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginSPDCakev1_1.postProcess")


        xsDataInputSPDCake = self.getDataInput()
        strOutputFileType = xsDataInputSPDCake.getOutputFileType().getValue()
        # Determine the image file name without path and suffix
        strInputImageFilePath = xsDataInputSPDCake.getInputFile().getPath().getValue()
        strInputFileNameWithoutSuffix = os.path.splitext(EDUtilsFile.getBaseName(strInputImageFilePath))[0]

        self.strOutputFileSuffix = "data"
        if (strOutputFileType == "PowderCIF"):
            self.strOutputFileSuffix = "cif"
        elif (strOutputFileType == "CHIPLOT"):
            self.strOutputFileSuffix = "chi"

        strOutputFileName = strInputFileNameWithoutSuffix + "." + self.strOutputFileSuffix
        if self.outputDir is None:
            self.m_strOutputFilePath = os.path.join(self.getWorkingDirectory(), strOutputFileName)
        else:
            self.m_strOutputFilePath = os.path.join(self.outputDir, strOutputFileName)
        PyStrCakeFilePrefix = os.path.splitext(os.path.split(strInputImageFilePath)[1])[0]


        ################################################################
        ####  Do some manipulation of the  output image  ##############
        ################################################################
        EDFCakeFile = openimage(os.path.join(self.getWorkingDirectory(), PyStrCakeFilePrefix + ".azim.edf"))
        npaData = EDFCakeFile.data
        pydHeader = EDFCakeFile.header

        pyfPixSize = float(pydHeader["PSize_1"].split()[0])
        pyfDist = float(pydHeader["SampleDistance"].split()[0])
        EDVerbose.DEBUG("Calculation done with PixSize=%s, distance= %s" % (pydHeader["PSize_1"], pydHeader["SampleDistance"]))
        pyiNbAzimBin, pyiLength = npaData.shape
        nplInt = npaData.reshape((pyiLength))
        nplTth = numpy.degrees(numpy.arctan(numpy.linspace(0.5 * pyfPixSize / pyfDist, (pyiLength - 0.5) * pyfPixSize / pyfDist  , pyiLength,)))

        #for the description of the +0.5 term, please refer to http://www.esrf.fr/computing/scientific/SAXS/doc/SaxsKeywords/SaxsKeywords.pdf page 23

        ######################################Debugging#######################
        f = open(os.path.join(self.getWorkingDirectory(), "original.dat"), "w")
        for i in range(pyiLength):
            f.write("%f\t%f\n" % (nplTth[i], nplInt[i]))
        f.close()
        ##############################end Debugging############################
        XRPD = lambda tth: numpy.interp(tth, nplTth, nplInt, left=0, right=0)
        pyfTthMin = nplTth[0]
        pyfTthMax = nplTth[-1]
        pyfStep = (pyfTthMax - pyfTthMin) / (pyiLength - 1)
                ########### Remove large files to prevent disk saturation when not in debug mode ###################
        if not EDVerbose.isVerboseDebug():
            os.remove(os.path.join(self.getWorkingDirectory(), PyStrCakeFilePrefix + ".cor.edf"))
            os.remove(os.path.join(self.getWorkingDirectory(), PyStrCakeFilePrefix + ".azim.edf"))



#        # Create the output data
        xsDataResultSPDCake = XSDataResultSPDCake()
        if (self.m_strOutputFilePath is not None):

            if (strOutputFileType == "PowderCIF"):
                    import CIFfile
                    cif = CIFfile.CIF()
                    cif[ "_audit_creation_method"    ] = 'From 2-D detector using SPD and CIFfile'
                    cif[ "_pd_meas_2theta_range_inc" ] = str(pyfStep)
                    cif[ "_pd_meas_2theta_range_max" ] = str(pyfTthMax)
                    cif[ "_pd_meas_2theta_range_min" ] = str(pyfTthMin)
                    cif[ "_pd_meas_number_of_points" ] = str(pyiLength)
                    cif[ "_pd_meas_scan_method"      ] = "fixed"
                    cif[ "_pd_spec_description"      ] = pydHeader["title"]
                    cif["_diffrn_radiation_wavelength"] = str(self.getDataInput().getWavelength().getValue())
                    cif["_pd_instr_dist_spec/detc"] = str(self.getDataInput().getSampleToDetectorDistance().getValue())
                    oneloop = []
                    #range( pyiLength ):
                    for i in numpy.linspace(pyfTthMin, pyfTthMax, pyiLength):
                        oneloop.append({ "_pd_meas_intensity_total" : str(XRPD(i)) })
                    cif["loop_"] = [ [ ["_pd_meas_intensity_total"], oneloop ] ]
                    cif.saveCIF(self.m_strOutputFilePath)

            elif (strOutputFileType == "CHIPLOT"):
                f = open(os.path.join(self.getWorkingDirectory(), self.m_strOutputFilePath), "w")
                f.write(pydHeader["title"] + ": Angular Profile\nTwo-Theta Angle (degrees)\nIntensity (normalised)\n%i\n" % pyiLength)
                for i in numpy.linspace(pyfTthMin, pyfTthMax, pyiLength):
                    f.write("%f\t%f\n" % (i, XRPD(i)))
                f.close()

            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.m_strOutputFilePath))
            xsDataResultSPDCake.setCakedFile(xsDataFile)
        self.setDataOutput(xsDataResultSPDCake)

    def generateSPDCommand(self):
        """
        This method creates the SPD command line for caking.
        """

        EDVerbose.DEBUG("EDPluginSPDCakev1_1.generateSPDLine")
        xsDataInputSPDCake = self.getDataInput()



        maxXdist = max(abs(xsDataInputSPDCake.getBeamCentreInPixelsX().getValue()), \
                        abs(xsDataInputSPDCake.getBufferSizeX().getValue() - \
                             xsDataInputSPDCake.getBeamCentreInPixelsX().getValue()))*\
                              xsDataInputSPDCake.getPixelSizeX().getValue()
        maxYdist = max(abs(xsDataInputSPDCake.getBeamCentreInPixelsY().getValue()), \
                        abs(xsDataInputSPDCake.getBufferSizeY().getValue() - \
                            xsDataInputSPDCake.getBeamCentreInPixelsY().getValue()))*\
                             xsDataInputSPDCake.getPixelSizeY().getValue()
        pyiMaxRadius = int (numpy.sqrt(maxXdist ** 2 + maxYdist ** 2) / \
                             min(xsDataInputSPDCake.getPixelSizeX().getValue() , \
                                  xsDataInputSPDCake.getPixelSizeY().getValue()))


        strMacro = " do_distortion=2"
        strMacro += " verbose=2"
        strMacro += " src_ext=edf azim_ext=azim.edf cor_ext=cor.edf"
        strMacro += " azim_int=1 azim_pass=1"
        strMacro += " off_1=0 off_2=0"
        strMacro += " wvl=%e" % (xsDataInputSPDCake.getWavelength().getValue()*1e-10)
        strMacro += " cen_1=%e cen_2=%e" % \
            (xsDataInputSPDCake.getBeamCentreInPixelsX().getValue(), xsDataInputSPDCake.getBeamCentreInPixelsY().getValue())
        strMacro += " dis=%e" % (xsDataInputSPDCake.getSampleToDetectorDistance().getValue()*1e-3)
        strMacro += " pix_1=%e pix_2=%e" % \
            (1e-3 * xsDataInputSPDCake.getPixelSizeX().getValue() , 1e-3 * xsDataInputSPDCake.getPixelSizeY().getValue())
        strMacro += " azim_a0=0   azim_a_num=1 azim_da=360"
        strMacro += " azim_r0=0 azim_r_num=%i" % pyiMaxRadius
        if not xsDataInputSPDCake.getSpatialDistortionFile()  is None :
            strMacro += " distortion_file=%s" % xsDataInputSPDCake.getSpatialDistortionFile().getPath().getValue()
        if not xsDataInputSPDCake.getDarkCurrentImageFile()   is None :
            strMacro += " dark_file=%s" % xsDataInputSPDCake.getDarkCurrentImageFile().getPath().getValue()
        if not xsDataInputSPDCake.getFlatFieldImageFile()     is None :
            strMacro += " flood_file=%s" % xsDataInputSPDCake.getFlatFieldImageFile().getPath().getValue()
#Last but not least: the name of the image !
        strMacro += " %s" % xsDataInputSPDCake.getInputFile().getPath().getValue()
        EDVerbose.DEBUG("SPD Command line:\n" + strMacro)
        self.setScriptCommandline(strMacro)

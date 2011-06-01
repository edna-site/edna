# coding: utf8
#
#    Project: EDNA Exec Plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal authors:      Jérôme Kieffer (jerome.kieffer@esrf.fr)
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
SPD Execution plugin for EDNA for doing image correction (distortion / intensity correction) an subsequent cacking
It implements parallelization, tries to keep track of former calculation to optimize the execution 
by preventing SPD to re-calculate the look-up table
"""
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import math, os, shutil, threading, time
from SPDworker              import SPDworker
from EDVerbose              import  EDVerbose
from EDPluginSPDCorrectv10  import  EDPluginSPDCorrectv10
from EDUtilsPath            import  EDUtilsPath
from XSDataSPDv1_0          import  XSDataResultSPDCake, XSDataInputSPDCake
from XSDataCommon           import  XSDataString, XSDataFile
from EDUtilsUnit            import  EDUtilsUnit
from EDUtilsPlatform        import  EDUtilsPlatform
from EDFactoryPluginStatic  import  EDFactoryPluginStatic
################################################################################
# AutoBuilder for Numpy, PIL, scipy and Fabio 
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("fabio.openimage", fabioPath)
EDFactoryPluginStatic.preImport("fabio.edfimage", fabioPath)
EDFactoryPluginStatic.preImport("fabio.fit2dmaskimage", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)

try:
    from fabio.openimage import openimage
    import fabio.edfimage
    import fabio.fit2dmaskimage
except ImportError:
    EDVerbose.ERROR("Error in loading Fabio\n\
    Please re-run the test suite for EDTestSuiteSPD \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


class EDPluginSPDCakev1_5(EDPluginSPDCorrectv10):
    """
    The purpose of this plugin is to use SPD to do "cake" azimuthal integration,
    i.e. azimuthal integration of powder diffraction images. 

    Most of the code is in EDPluginSPDCorrectv10
    """
    __dictMask = {} #dictionary containing the input mask and the output (corrected and tilted mask) 
    __semaphore = threading.Semaphore()

    def __init__(self):
        """
        Constructor of the plugin: just do some simple initialization 
        """
        self.bDeleteCorImg = False
        EDPluginSPDCorrectv10.__init__(self)
        if self.getClassName() == "EDPluginSPDCakev1_5":
            self.setXSDataInputClass(XSDataInputSPDCake)
        self.bCorrectTiltMask = False


    def preProcess(self, _edObject=None):
        """
        Preprocess methods for the EDPluginSPDCakev1_5 :
        - tilts the mask if needed 
        """
        EDPluginSPDCorrectv10.preProcess(self, _edObject)
        self.DEBUG("EDPluginSPDCakev1_5.preProcess")
        if ("MaskFile" in self.dictGeometry) and  (self.dictGeometry["MaskFile"] not in EDPluginSPDCakev1_5.__dictMask):
            self.correctMask()


    def postProcess(self, _edObject=None):
        """
        postProcess of the plugin EDPluginSPDCakev1_5.py:
        - convert to HDF if needed (to be implemented)
        - convert to chiplot or xye or cif if needed
        - move images (if needed) or delete .cor image 
        - set result XML   
        """
        EDPluginSPDCorrectv10.postProcess(self)
        self.DEBUG("EDPluginSPDCakev1_5.postProcess")

        if not os.path.isdir(self.dictGeometry["OutputDirCake"]):
            os.makedirs(self.dictGeometry["OutputDirCake"])



        strInputImagePathNoSfx = os.path.splitext(os.path.basename(self.pathToInputFile))[0]
        strSpdoutCake = strInputImagePathNoSfx + self.dictGeometry["OutputFileType"]

        strOutputCakeFilePath = os.path.join(self.dictGeometry["OutputDirCake"], strSpdoutCake)
        xsDataResultSPD = XSDataResultSPDCake()


        if not self.getFireAndForget():
            strTempFilePath = None
            if "corrected" in self.dictRes:
                strSpdoutCor = self.dictRes["corrected"]
            if "regrouped" in self.dictRes:
                strTempFilePath = self.dictRes["regrouped"]

            if self.dictGeometry["OutputFileType"].lower() in [".hdf5", ".nexus", ".h5", ".nx"]:
                self.WARNING("HDF5/Nexus output is not yet implemented in the SPD plugin.")

            if strTempFilePath is None:
                self.WARNING("Cannot copy output to %s as there is not input: %s " % (strOutputCakeFilePath, self.dictRes))
            elif os.path.exists(strOutputCakeFilePath):
                self.WARNING("Destination file exists, I will leave result file in %s." % strTempFilePath)
                strOutputCakeFilePath = strTempFilePath
            else:
                shutil.move(strTempFilePath, strOutputCakeFilePath)

            strOutputCorFilePath = os.path.join(self.dictGeometry["OutputDir"], os.path.split(strSpdoutCor)[1])
            if self.bDeleteCorImg:
                if os.path.isfile(strSpdoutCor):
                    os.remove(strSpdoutCor)
                else:
                    self.WARNING("Corrected file vanished before removal %s" % strSpdoutCor)
            else:
                strTempFilePathCor = os.path.join(self.getWorkingDirectory(), strSpdoutCor)
                if self.dictGeometry["OutputFileType"].lower() in [".hdf5", ".nexus", ".h5", ".nx"]:
                    self.WARNING("HDF5/Nexus output is not yet implemented in the SPD plugin.")
                elif self.dictGeometry["OutputFileType"].lower() not in [".edf", ".azim", ".cor"] :
                    self.WARNING("Output file format %s is not yet implemented in the SPD plugin." % self.dictGeometry["OutputFileType"])

                if os.path.exists(strOutputCorFilePath):
                    self.WARNING("Destination file exists, I will leave result file in %s." % strTempFilePathCor)
                    strOutputCorFilePath = os.path.abspath(strTempFilePathCor)
                else:

                    shutil.move(strTempFilePath, strOutputCorFilePath)
                xsDataFileCorr = XSDataFile()
                xsDataFileCorr.setPath(XSDataString(strOutputCorFilePath))
                xsDataResultSPD.setcorrectedFile(xsDataFileCorr)
#        # Create the output data
        xsDataFileCake = XSDataFile()
        xsDataFileCake.setPath(XSDataString(strOutputCakeFilePath))
        xsDataResultSPD.setCakedFile(xsDataFileCake)

        self.setDataOutput(xsDataResultSPD)


    def getInputParameter(self):
        """
        Read all the input parameters and store them in instance variables called  self.dictGeometry and  self.pathToInputFile
        """
        self.DEBUG("EDPluginSPDCakev1_5.getInputParameter")
        EDPluginSPDCorrectv10.getInputParameter(self)
        if self.xsDataInputSPD.getStartAzimuth() is not None:
            if self.xsDataInputSPD.getStartAzimuth().getUnit() is not None:
                self.dictGeometry["StartAzimuth"] = EDUtilsUnit.getValue(self.xsDataInputSPD.getStartAzimuth(), "deg")
            else:
                self.WARNING("You did not specify the StartAzimuth Unit, Falling back to Deg (not Rad)")
                self.dictGeometry["StartAzimuth"] = self.xsDataInputSPD.getStartAzimuth().getValue()
        if self.xsDataInputSPD.getStopAzimuth() is not None:
            if self.xsDataInputSPD.getStopAzimuth().getUnit() is not None:
                self.dictGeometry["StopAzimuth"] = EDUtilsUnit.getValue(self.xsDataInputSPD.getStopAzimuth(), "deg")
            else:
                self.WARNING("You did not specify the StopAzimuth Unit, Falling back to Deg (not Rad)")
                self.dictGeometry["StopAzimuth"] = self.xsDataInputSPD.getStopAzimuth().getValue()
        if self.xsDataInputSPD.getStepAzimuth() is not None:
            if self.xsDataInputSPD.getStepAzimuth().getUnit() is not None:
                self.dictGeometry["StepAzimuth"] = EDUtilsUnit.getValue(self.xsDataInputSPD.getStepAzimuth(), "deg")
            else:
                self.WARNING("You did not specify the StepAzimuth Unit, Falling back to Deg (not Rad)")
                self.dictGeometry["StepAzimuth"] = self.xsDataInputSPD.getStepAzimuth().getValue()
        if self.xsDataInputSPD.getInnerRadius() is not None:
            self.dictGeometry["InnerRadius"] = self.xsDataInputSPD.getInnerRadius().getValue()
        if self.xsDataInputSPD.getOuterRadius() is not None:
            self.dictGeometry["OuterRadius"] = self.xsDataInputSPD.getOuterRadius().getValue()
        if self.xsDataInputSPD.getOutputDirCake() is not None:
            self.dictGeometry["OutputDirCake"] = self.xsDataInputSPD.getOutputDirCake().getPath().getValue()
            EDUtilsPath.createFolder(self.dictGeometry["OutputDirCake"])
            if self.dictGeometry["OutputDirCake"] != self.dictGeometry["OutputDir"]:
                self.setFireAndForget(False)
        else:
            self.dictGeometry["OutputDirCake"] = self.dictGeometry["OutputDir"]
        if self.xsDataInputSPD.getMaskFile() is not None:
            self.dictGeometry["MaskFile"] = self.xsDataInputSPD.getMaskFile().getPath().getValue()
            if not os.path.isfile(self.dictGeometry["MaskFile"]):
                self.ERROR("Mask file %s does not exist " % self.dictGeometry["MaskFile"])
                self.dictGeometry.pop("MaskFile")
        if self.xsDataInputSPD.getIntensityScaleFactor() is not None:
            self.dictGeometry["IntensityScaleFactor"] = self.xsDataInputSPD.getIntensityScaleFactor().getValue()

        if self.xsDataInputSPD.getDeleteCorImg() is not None:
            self.bDeleteCorImg = (self.xsDataInputSPD.getDeleteCorImg().getValue() in ["1", 1, "true", "True", True])
        if self.bDeleteCorImg:
            self.setFireAndForget(False)
        if self.xsDataInputSPD.getCorrectTiltMask() is not None:
            self.bCorrectTiltMask = bool(self.xsDataInputSPD.getCorrectTiltMask().getValue())


    def generateSPDCommand(self):
        """
        This method creates the SPD command line for image correction.
        """
        EDPluginSPDCorrectv10.generateSPDCommand(self)
        self.DEBUG("EDPluginSPDCackev1_5.generateSPDCommand")
        lstCmdLineOption = [self.getSPDConfig()]
        lstCmdLineOption.append("cor_ext=.cor azim_int=1 azim_pass=0")
        if self.dictGeometry.has_key("OutputFileType") and (self.getClassName() == "EDPluginSPDCakev1_5"):
            if self.dictGeometry["OutputFileType"].startswith("."):
                lstCmdLineOption.append("azim_ext=%s" % self.dictGeometry["OutputFileType"])
            else:
                lstCmdLineOption.append("azim_ext=.%s" % self.dictGeometry["OutputFileType"])
        pixelSize = min(self.dictGeometry["PixelSizeX"], self.dictGeometry["PixelSizeY"])
        if "InnerRadius" in self.dictGeometry:
            lstCmdLineOption.append("azim_r0=%s" % (self.dictGeometry["InnerRadius"] * pixelSize))
        if "OuterRadius" in self.dictGeometry:
            lstCmdLineOption.append("azim_r_num=%s" % ((self.dictGeometry["OuterRadius"] - self.dictGeometry["InnerRadius"])))
        else:
            if ("BeamCenterX" in self.dictGeometry) and\
               ("BeamCenterY" in self.dictGeometry) and\
               ("BufferSizeX" in self.dictGeometry) and\
               ("BufferSizeY" in self.dictGeometry) and\
               ("PixelSizeX" in self.dictGeometry) and\
               ("PixelSizeY" in self.dictGeometry):
                maxXdist = max(abs(self.dictGeometry["BeamCenterX"]), abs(self.dictGeometry["BufferSizeX"] - self.dictGeometry["BeamCenterX"])) * self.dictGeometry["PixelSizeX"]
                maxYdist = max(abs(self.dictGeometry["BeamCenterY"]), abs(self.dictGeometry["BufferSizeY"] - self.dictGeometry["BeamCenterY"])) * self.dictGeometry["PixelSizeY"]
                MaxRadius = int(math.sqrt(maxXdist ** 2 + maxYdist ** 2) / min(self.dictGeometry["PixelSizeX"], self.dictGeometry["PixelSizeY"]))
                lstCmdLineOption.append("azim_r_num=%s" % MaxRadius)

        if "StartAzimuth" in self.dictGeometry:
            lstCmdLineOption.append("azim_a0=%s" % self.dictGeometry["StartAzimuth"])
        if "StepAzimuth" in self.dictGeometry:
            lstCmdLineOption.append("azim_da=%s" % self.dictGeometry["StepAzimuth"])
        if "StopAzimuth" in self.dictGeometry:
            lstCmdLineOption.append("azim_a_num=%s" % int(round((self.dictGeometry["StopAzimuth"] - self.dictGeometry["StartAzimuth"]) / self.dictGeometry["StepAzimuth"])))
        if "MaskFile" in self.dictGeometry:
            if self.dictGeometry["MaskFile"] in EDPluginSPDCakev1_5.__dictMask:
                lstCmdLineOption.append('mask_file=%s' % os.path.abspath(EDPluginSPDCakev1_5.__dictMask[self.dictGeometry["MaskFile"]]))
            else:
                lstCmdLineOption.append('mask_file=%s' % os.path.abspath(self.dictGeometry["MaskFile"]))
        if "IntensityScaleFactor" in self.dictGeometry:
            lstCmdLineOption.append("ave_scf=%s" % self.dictGeometry["IntensityScaleFactor"])
        strCmdLineOption = " ".join(lstCmdLineOption)
        self.DEBUG("SPD Command line:\n" + strCmdLineOption)
        self.setSPDConfig(strCmdLineOption)


    def correctMask(self):
        """
        Apply spline and tilt correction to the mask if provided in fit2d format.
        """
        self.DEBUG("EDPluginSPDCakev1_5.correctMask")
        EDPluginSPDCakev1_5.__semaphore.acquire()
        t0 = time.time()
#        self.screen("%s: preCalc Mask file is in %s" % (self.getId(), self.dictGeometry["MaskFile"]))
        if (self.dictGeometry["MaskFile"] not in EDPluginSPDCakev1_5.__dictMask):
            strUnCorrectedEdfMask = self.dictGeometry["MaskFile"]
            unCorrectedMask = openimage(strUnCorrectedEdfMask)
            basename = os.path.join(self.getSPDCommonDirectory(), os.path.splitext(os.path.basename(strUnCorrectedEdfMask))[0])

            if self.bCorrectTiltMask:
                if not isinstance(unCorrectedMask, fabio.edfimage.edfimage):
                    strUnCorrectedEdfMask = os.path.join(self.getSPDCommonDirectory(),
                                                         os.path.splitext(os.path.basename(self.dictGeometry["MaskFile"]))[0] + ".edf")
                    unCorrectedEdfMask = fabio.edfimage.edfimage(header={}, data=unCorrectedMask.data.astype("float32"))
                    unCorrectedEdfMask.write(strUnCorrectedEdfMask)

                imgConfig = self.getSPDConfig()
                mskConfig = " ".join([i for i in imgConfig.split() \
                                    if not (i.startswith("mask_file=") or i.startswith("azim_")\
                                    or i.startswith("flood_file=") or i.startswith("dark_file="))] + ["do_dark=0", "dummy=1"])
                worker = SPDworker()
                worker.setExecutable(self.getExecutable())
                worker.setLogFilename(os.path.join(self.getSPDCommonDirectory(), "worker-mask.log"))
                worker.initialize(mskConfig)
                worker.setTimeOut(self.getTimeOut())
                dictLog = worker.process("outdir=%s/ %s" % (self.getSPDCommonDirectory(), strUnCorrectedEdfMask))
                for oneLog in dictLog:
                    self.DEBUG("EDPluginSPDCakev1_5.correctMask %s: %s" % (oneLog, dictLog[oneLog]))
                worker.kill(gentle=True)
                worker = None
                npaCorrected = -(openimage(basename + ".cor").data + 0.5).astype("int8")
            else:
                npaCorrected = -(unCorrectedMask.data).astype("int8")
            strCorrectedMask = basename + ".msk"
            fabio.edfimage.edfimage(data=npaCorrected, header={"Dummy":"-1"}).write(strCorrectedMask)
            EDPluginSPDCakev1_5.__dictMask[self.dictGeometry["MaskFile"]] = strCorrectedMask

        EDPluginSPDCakev1_5.__semaphore.release()
        newConfig = []
        for key in self.getSPDConfig().split():
            if key.startswith("mask_file="):
                newConfig.append('mask_file=%s' % os.path.abspath(EDPluginSPDCakev1_5.__dictMask[self.dictGeometry["MaskFile"]]))
            else:
                newConfig.append(key)
        self.setSPDConfig(" ".join(newConfig))
#        self.worker.setConfig(self.getSPDConfig())
        self.DEBUG("%s updating mask %s took %.3fs " % (self.getId(), self.dictGeometry["MaskFile"], time.time() - t0))


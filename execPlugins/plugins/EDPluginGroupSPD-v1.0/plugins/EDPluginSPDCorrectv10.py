# coding: utf8
#
#    Project: EDNA Exec Plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 ESRF
#
#    Principal authors:      Jérôme Kieffer (kieffer@esrf.fr)
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
SPD Execution plugin for EDNA for doing image correction (distortion / intensity correction)
It implements parallelization, tries to keep track of former calculation to optimize the execution 
by preventing SPD to re-clculate the look-up table
"""

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, tempfile, threading, shutil, time

from spline                     import Spline
from SPDworker                  import SPDworker
from EDVerbose                  import  EDVerbose
from EDUtilsPath                import  EDUtilsPath
from EDFactoryPluginStatic      import  EDFactoryPluginStatic
from XSDataCommon               import  XSDataFile
from XSDataCommon               import  XSDataString
from EDMessage                  import  EDMessage
from EDConfiguration            import  EDConfiguration
from EDPluginExecProcess        import  EDPluginExecProcess
from EDUtilsParallel            import  EDUtilsParallel
from EDUtilsUnit                import  EDUtilsUnit
from EDUtilsPlatform           import EDUtilsPlatform
from XSDataSPDv1_0              import  XSDataInputSPD
from XSDataSPDv1_0              import  XSDataResultSPD
from XSDataCommon               import XSPluginItem


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)

try:
    import fabio
except ImportError:
    EDVerbose.ERROR("Error in loading Fabio\n\
    Please re-run the test suite for EDTestSuiteSPD \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")



CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE = "execProcessScriptExecutable"
CONF_EXEC_MAX_MAX_NUMBER_OF_WORKERS = "maxNumberOfWorkers"
CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING = "version"

class EDPluginSPDCorrectv10(EDPluginExecProcess):
    """
    The purpose of this execution plugin is to use SPD to do 2D image correction using a spline and/or a tilt,
    
    Few tips and tricks about SPD ...
  * the tilt implementation is done in python and applied to the orthonormmal spline distortion of the image.     
    """
    __listOfWorker = []        #a dictionary containing the current setup
    __iNumberOfWorker = 0      # the max lenth of  __listOfWorker
    __bInitialized = False     #a boolean to tell if it is initialized     
    __strSPDDir = None         # a temporary directory common for SPD
    __lockTilt = threading.Semaphore()
    __lockWorker = threading.Semaphore()

    def __init__(self):
        """
        Constructor of the plugin: just do some simple initialization 
        """
        EDPluginExecProcess.__init__(self)
#        self.DEBUG(self.getBaseName())
        if self.getClassName() == "EDPluginSPDCorrectv10":
            self.setXSDataInputClass(XSDataInputSPD)
        self.dictGeometry = {}
        self.dictRes = {}
        self.xsDataInputSPD = None
        self.pathToInputFile = None
        self._SPDconfig = None
        self.worker = None
        self.workerID = None
        self._listCompatibleVersions = []
        self._strConfigExecutable = None
        self.bTimeOut = False

        self._iConfigNumberOfWorker = 0
        self._bFireAndForget = False
        self.strCurrentVersion = None
        self.addCompatibleVersion("spd version SPD = 1.2 SAXS = 2.436 EDF = 2.171")


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginSPDCorrectv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputFile(), "inputFile is None")


    def preProcess(self, _edObject=None):
        """
        Preprocess methods for the EDPluginSPDCorrectv10 :
        - Reads input parameters
        - Creates the displacement matrix if the the detector is tilted
        - create the configuration for SPD
        - selects the worker (SPD program under control)
        """
        EDPluginExecProcess.preProcess(self)
        self.DEBUG("EDPluginSPDCorrectv10.preProcess")
        # Check that the input data and correction images are present
        self.getInputParameter()
        if "SpatialDistortionFile" in self.dictGeometry:
            splineDM = Spline()
            splineDM.read(self.dictGeometry["SpatialDistortionFile"])
            self.dictGeometry["PixelSizeX"], self.dictGeometry["PixelSizeY"] = splineDM.getPixelSize()
        else:
            splineDM = None
        if self.dictGeometry["AngleOfTilt"] != 0:
            EDPluginSPDCorrectv10.__lockTilt.acquire()
            if splineDM == None:
                edfFile = fabio.open(self.pathToInputFile)
                data = edfFile.data
                size = data.shape
                splineDM = splineDM.zeros(xmin=0.0, ymin=0.0, xmax=size[0], ymax=size[1])
                if ("PixelSizeX" in self.dictGeometry) and ("PixelSizeY" in self.dictGeometry):
                    splineDM.setPixelSize = (self.dictGeometry["PixelSizeX"], self.dictGeometry["PixelSizeY"])

            strtmp = os.path.join(self.getSPDCommonDirectory(), os.path.basename(os.path.splitext(self.dictGeometry["SpatialDistortionFile"])[0]))

            if not(os.path.isfile (strtmp + "-tilted-x.edf") and os.path.isfile (strtmp + "-tilted-y.edf")):
#                self.DEBUG("preProcess: \t EDPluginSPDCorrectv10.__lock.acquire(), currently: %i" % EDPluginSPDCorrectv10.__lock._Semaphore__value)

                if not(os.path.isfile (strtmp + "-tilted-x.edf") and os.path.isfile (strtmp + "-tilted-y.edf")):
                    #The second test is just here to gain some time as the global semaphore could be in use elsewhere 
                    self.createDisplacementMatrix(splineDM)

            self.dictGeometry["DistortionFileX"] = strtmp + "-tilted-x.edf"
            self.dictGeometry["DistortionFileY"] = strtmp + "-tilted-y.edf"
            EDPluginSPDCorrectv10.__lockTilt.release()
        self.generateSPDCommand()



    def process(self, _edObject=None):
        """
        Processing of one image: send the image to process to the good worker
        """
        self.DEBUG("EDPluginSPDCorrectv1_0.process starting")
        self.chooseWorker()
        self.synchronizeOn()
        self.DEBUG(self.getBaseName() + ": Processing")
        if self.isVerboseDebug():
            self.DEBUG("EDPluginSPDCorrectv1_0.process worker number: %s " % self.workerID)
            self.DEBUG("EDPluginSPDCorrectv1_0.process Logs will be in %s" % self.worker.getLogFilename())

        if self._bFireAndForget:
            if self.dictGeometry["OutputDir"].endswith("/"):
                strCmdLine = "outdir=%s %s" % (self.dictGeometry["OutputDir"], self.pathToInputFile)
            else:
                strCmdLine = " outdir=%s/ %s" % (self.dictGeometry["OutputDir"], self.pathToInputFile)
        else:
            strCmdLine = self.pathToInputFile
        self.dictRes = self.worker.process(strCmdLine)
        if (self.dictRes["timeout"] == True):
            self.DEBUG(" EDPluginSPDCorrectv1_0.process ========================================= TIMEOUT ================")
            errorMessage = 'EDPluginSPDCorrectv1_0.process called as %s-%s : TIMEOUT!' % (self.getClassName(), self.getId())
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage
        if (self.dictRes["error"] == True):
            self.DEBUG("EDPluginSPDCorrectv1_0.process ========================================= Execution Error! ================")
            errorMessage = 'EDPluginSPDCorrectv1_0.process called as %s-%s : Execution Error !' % (self.getClassName(), self.getId())
#            for mesg in self.dictRes:
#                self.error("%s: %s" % (mesg, self.dictRes[mesg]))
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError(errorMessage)
#        self.DEBUG("dictRes= %s" % self.dictRes)
        self.DEBUG("EDPluginSPDCorrectv1_0.process finished ")
        self.synchronizeOff()


    def postProcess(self, _edObject=None):
        """
        postProcess of the plugin EDPluginSPDCorrectv10.py:
        - convert to HDF if needed (to be implemented)
        - move images (if needed)
        - set result XML   
        """
        EDPluginExecProcess.postProcess(self)
        self.DEBUG("EDPluginSPDCorrectv10.postProcess")
        EDUtilsPath.createFolder(self.dictGeometry["OutputDir"])

        if self.getClassName() == "EDPluginSPDCorrectv10":



            strInputImagePathNoSfx = os.path.splitext(os.path.basename(self.pathToInputFile))[0]
            destFileBaseName = strInputImagePathNoSfx + self.dictGeometry["OutputFileType"]
            strOutputFilePath = os.path.join(self.dictGeometry["OutputDir"], destFileBaseName)
            if not self._bFireAndForget:
                if "corrected" in self.dictRes:
                    strTempFilePath = self.dictRes["corrected"]
                else:
                    strTempFilePath = os.path.join(self.getWorkingDirectory(), destFileBaseName)
                if self.dictGeometry["OutputFileType"].lower() in [".hdf5", ".nexus", ".h5", ".nx"]:
                    self.WARNING("HDF5/Nexus output is not yet implemented in the SPD plugin.")
                if os.path.exists(strOutputFilePath):
                    self.WARNING("Destination file exists, I will leave result file in %s." % strTempFilePath)
                    strOutputFilePath = strTempFilePath
                else:
                    shutil.move(strTempFilePath, strOutputFilePath)
    #        # Create the output data
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(strOutputFilePath))

            xsDataResultSPD = XSDataResultSPD()
            xsDataResultSPD.setCorrectedFile(xsDataFile)
            self.setDataOutput(xsDataResultSPD)



    def getInputParameter(self, _edObject=None):
        """
        Read all the input parameters and store them in instance variables called  self.dictGeometry and  self.pathToInputFile
        """
        self.DEBUG("EDPluginSPDCorrectv10.getInputParameter")
        self.xsDataInputSPD = self.getDataInput()
        self.pathToInputFile = self.xsDataInputSPD.getInputFile().getPath().getValue()
        if not os.path.isfile(self.pathToInputFile):
            edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", self.pathToInputFile)
            self.error(edStringErrorMessage)
            self.addErrorMessage(edStringErrorMessage)
            raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getDarkCurrentImageFile() is not None:
            pathToDarkCurrentImageFile = self.xsDataInputSPD.getDarkCurrentImageFile().getPath().getValue()
            if os.path.isfile(pathToDarkCurrentImageFile):
                self.dictGeometry["DarkCurrentImageFile"] = pathToDarkCurrentImageFile
            else:
                edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pathToDarkCurrentImageFile)
                self.error(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getFlatFieldImageFile() is not None:
            pathToFlatFieldImageFile = self.xsDataInputSPD.getFlatFieldImageFile().getPath().getValue()
            if os.path.isfile(pathToFlatFieldImageFile):
                self.dictGeometry["FlatFieldImageFile"] = pathToFlatFieldImageFile
            else:
                edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pathToFlatFieldImageFile)
                self.error(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getSpatialDistortionFile() is not None:
            pathToSpatialDistortionFile = self.xsDataInputSPD.getSpatialDistortionFile().getPath().getValue()
            if os.path.isfile(pathToSpatialDistortionFile):
                self.dictGeometry["SpatialDistortionFile"] = pathToSpatialDistortionFile
            else:
                edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pathToSpatialDistortionFile)
                self.error(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getAngleOfTilt() is not None:
            if self.xsDataInputSPD.getAngleOfTilt().getUnit() is not None:
                self.dictGeometry["AngleOfTilt"] = EDUtilsUnit.getValue(self.xsDataInputSPD.getAngleOfTilt(), "deg")
            else: #Fall-back by default to deg
                self.WARNING("You did not specify the AngleOfTilt unit ... I Guess it is deg")
                self.dictGeometry["AngleOfTilt"] = self.xsDataInputSPD.getAngleOfTilt().getValue()
        else:
            self.dictGeometry["AngleOfTilt"] = 0

        if self.xsDataInputSPD.getTiltRotation() is not None:
            if self.xsDataInputSPD.getTiltRotation().getUnit() is not None:
                self.dictGeometry["TiltRotation"] = EDUtilsUnit.getValue(self.xsDataInputSPD.getTiltRotation(), "deg")
            else: #Fall-back by default to deg
                self.WARNING("You did not specify the TiltRotation unit ... I Guess it is deg")
                self.dictGeometry["TiltRotation"] = self.xsDataInputSPD.getTiltRotation().getValue()
        else:
            self.dictGeometry["TiltRotation"] = 0
        if self.xsDataInputSPD.getBeamCentreInPixelsX() is not None:
            self.dictGeometry["BeamCenterX"] = self.xsDataInputSPD.getBeamCentreInPixelsX().getValue()
        if self.xsDataInputSPD.getBeamCentreInPixelsY() is not None:
            self.dictGeometry["BeamCenterY"] = self.xsDataInputSPD.getBeamCentreInPixelsY().getValue()
        if self.xsDataInputSPD.getBufferSizeX() is not None:
            self.dictGeometry["BufferSizeX"] = self.xsDataInputSPD.getBufferSizeX().getValue()
        if self.xsDataInputSPD.getBufferSizeY() is not None:
            self.dictGeometry["BufferSizeY"] = self.xsDataInputSPD.getBufferSizeY().getValue()


        if self.xsDataInputSPD.getDistortionFileX() is not None:
            pathToDistortionFileX = self.xsDataInputSPD.getDistortionFileX().getPath().getValue()
            if os.path.isfile(pathToDistortionFileX):
                self.dictGeometry["DistortionFileX"] = pathToDistortionFileX
            else:
                edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pathToDistortionFileX)
                self.error(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getDistortionFileY() is not None:
            pathToDistortionFileY = self.xsDataInputSPD.getDistortionFileY().getPath().getValue()
            if os.path.isfile(pathToDistortionFileY):
                self.dictGeometry["DistortionFileY"] = pathToDistortionFileY
            else:
                edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pathToDistortionFileY)
                self.error(edStringErrorMessage)
                self.addErrorMessage(edStringErrorMessage)
                raise RuntimeError, edStringErrorMessage
        if self.xsDataInputSPD.getPixelSizeX() is not None:
            self.dictGeometry["PixelSizeX"] = EDUtilsUnit.getSIValue(self.xsDataInputSPD.getPixelSizeX())
        if self.xsDataInputSPD.getPixelSizeY() is not None:
            self.dictGeometry["PixelSizeY"] = EDUtilsUnit.getSIValue(self.xsDataInputSPD.getPixelSizeY())
        if self.xsDataInputSPD.getSampleToDetectorDistance() is not None:
            self.dictGeometry["SampleToDetectorDistance"] = EDUtilsUnit.getSIValue(self.xsDataInputSPD.getSampleToDetectorDistance())

        if self.xsDataInputSPD.getWavelength() is not None:
            if self.xsDataInputSPD.getWavelength().getUnit() is not None:
                self.dictGeometry["Wavelength"] = EDUtilsUnit.getSIValue(self.xsDataInputSPD.getWavelength())
            else: #Fall-back to Angsrom
                self.WARNING("You did not specify the wavelength unit ... I Guess it is Angstrom")
                self.dictGeometry["Wavelength"] = self.xsDataInputSPD.getWavelength().getValue()*1e-10
        if self.xsDataInputSPD.getOutputFileType() is not None:
            self.dictGeometry["OutputFileType"] = self.xsDataInputSPD.getOutputFileType().getValue()
            if not  self.dictGeometry["OutputFileType"].startswith("."):
                self.dictGeometry["OutputFileType"] = "." + self.dictGeometry["OutputFileType"]
        else:
            self.dictGeometry["OutputFileType"] = ".edf"
        if self.xsDataInputSPD.getOutputDir() is not None:
            tmpdir = self.xsDataInputSPD.getOutputDir().getPath().getValue()
            if os.path.isdir(tmpdir):
                self.dictGeometry["OutputDir"] = tmpdir
                if tmpdir != os.path.dirname(self.pathToInputFile):
                    self._bFireAndForget = True
            else:
                self.WARNING("The destination directory %s does not exist, using working directory instead %s" % (tmpdir, self.getWorkingDirectory()))
                self.dictGeometry["OutputDir"] = self.getWorkingDirectory()
        else:
            self.dictGeometry["OutputDir"] = os.path.dirname(self.pathToInputFile)
        if self.dictGeometry["OutputDir"] == os.path.dirname(self.pathToInputFile) and \
           not (self.pathToInputFile.endswith(self.dictGeometry["OutputFileType"])) and \
           not (self.dictGeometry["OutputFileType"].lower()  in [".h5", ".chi", ".nx", ".nexus", ".cif"]) :
            self.bFireAndForget = True




    def createDisplacementMatrix(self, splineDM):
        """
        generate the displacement matrix for SPD
        
        @param splineDM: displacement matrix of a non tilted detector.
        @type splineDM: instance of class Spline
        """
        splineDM.spline2array()
        tilted = splineDM.tilt((self.dictGeometry["BeamCenterX"], self.dictGeometry["BeamCenterY"]), \
                                self.dictGeometry["AngleOfTilt"], self.dictGeometry["TiltRotation"], self.dictGeometry["SampleToDetectorDistance"])
        strtmp = os.path.join(self.getSPDCommonDirectory(), os.path.splitext(os.path.basename(self.dictGeometry["SpatialDistortionFile"]))[0])
        tilted.writeEDF(strtmp + "-tilted")


    def generateSPDCommand(self):
        """
        This method creates the SPD command line for image correction.
        """
        self.DEBUG(" EDPluginSPDCorrectv10.generateSPDCommand")
        lstCmdLineOption = ["off_1=0 off_2=0"]
        if self.isVerboseDebug() is True:
            lstCmdLineOption.append("verbose=2")
        else:
            lstCmdLineOption.append("verbose=0")
        lstCmdLineOption.append('src_ext=%s' % (os.path.splitext(self.xsDataInputSPD.getInputFile().getPath().getValue())[1]))
        if ("OutputFileType" in self.dictGeometry) and (self.getClassName() == "EDPluginSPDCorrectv10"):
            if self.dictGeometry["OutputFileType"].startswith("."):
                lstCmdLineOption.append("cor_ext=%s" % self.dictGeometry["OutputFileType"])
            else:
                lstCmdLineOption.append("cor_ext=.%s" % self.dictGeometry["OutputFileType"])
        if "Wavelength" in self.dictGeometry:
            lstCmdLineOption.append("wvl=%e" % (self.dictGeometry["Wavelength"]))
        if ("BeamCenterX" in self.dictGeometry) and ("BeamCenterY" in self.dictGeometry):
            lstCmdLineOption.append("cen_1=%e cen_2=%e" % (self.dictGeometry["BeamCenterX"], self.dictGeometry["BeamCenterY"]))
        if ("SampleToDetectorDistance" in self.dictGeometry):
            lstCmdLineOption.append("dis=%e" % (self.dictGeometry["SampleToDetectorDistance"]))
        if ("PixelSizeX" in self.dictGeometry) and ("PixelSizeY" in self.dictGeometry):
            lstCmdLineOption.append("pix_1=%e pix_2=%e" % (self.dictGeometry["PixelSizeX"] , self.dictGeometry["PixelSizeY"]))
        if ("DistortionFileX" in self.dictGeometry) and ("DistortionFileY" in self.dictGeometry):
            lstCmdLineOption.append('do_distortion=2 xfile=%s yfile=%s' % (self.dictGeometry["DistortionFileX"], self.dictGeometry["DistortionFileY"]))
        elif ("SpatialDistortionFile" in self.dictGeometry):
            lstCmdLineOption.append('do_distortion=2 distortion_file=%s' % self.dictGeometry["SpatialDistortionFile"])
        else:
            lstCmdLineOption.append("do_distortion=0")
        if ("DarkCurrentImageFile" in self.dictGeometry):
            lstCmdLineOption.append('dark_file=%s' % self.dictGeometry["DarkCurrentImageFile"])
        else:
            lstCmdLineOption.append("do_dark=0")
        if ("FlatFieldImageFile" in self.dictGeometry) :
            lstCmdLineOption.append('flood_file=%s' % self.dictGeometry["FlatFieldImageFile"])
        strCmdLineOption = " ".join(lstCmdLineOption)
#        for i in lstCmdLineOption: self.screen(i)
        if "EDPluginSPDCorrectv10" in self.getName():
            self.DEBUG("SPD Command line:\n" + strCmdLineOption)
        self.setSPDConfig(strCmdLineOption)


    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters
         - Script executable to be invoked
         - number of worker 
         - The 3rd party executable installed version
        """
        EDPluginExecProcess.configure(self)
        self.DEBUG(" EDPluginSPDCorrect.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            self.WARNING("EDPluginSPDCorrect.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()
        if (self.getExecutable() is None):
            edStringScriptExecutable = EDConfiguration.getStringParamValue(xsPluginItem, CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE)
            if(edStringScriptExecutable == None):
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginSPDCorrect.process', self.getClassName(), "Configuration parameter missing: " \
                                                               + CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE)
                self.error(errorMessage)
                self.addErrorMessage(errorMessage)
                raise RuntimeError, errorMessage
            else:
                # Check that the executable file exists
                if not os.path.isfile(edStringScriptExecutable):
                    errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginSPDCorrect.process', self.getClassName(), "Cannot find configured " \
                                                                   + CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE + " : " + edStringScriptExecutable)
                    self.error(errorMessage)
                    self.addErrorMessage(errorMessage)
                    raise RuntimeError, errorMessage
                else:
                    self.setExecutable(edStringScriptExecutable)
        edStringConfigSetupNbWorker = EDConfiguration.getStringParamValue(xsPluginItem, CONF_EXEC_MAX_MAX_NUMBER_OF_WORKERS)
        if(edStringConfigSetupNbWorker == None):
            self.DEBUG("EDPluginSPDCorrect.configure: No configuration parameter found for: " + CONF_EXEC_MAX_MAX_NUMBER_OF_WORKERS + ", NO default value!")
        else:
            self._iConfigNumberOfWorker = int(edStringConfigSetupNbWorker)
        edStringVersion = EDConfiguration.getStringParamValue(xsPluginItem, CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING)
        if(edStringVersion == None):
            self.DEBUG("EDPluginSPDCorrect.configure: No configuration parameter found for: " + CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING + ", NO default value!")
        else:
            self.setStringVersion(edStringVersion)


    def chooseWorker(self):
        """
        selects the worker and sets self.worker
        """
#        self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s" % self.getId())
        if EDPluginSPDCorrectv10.__iNumberOfWorker == 0:
            EDPluginSPDCorrectv10.__iNumberOfWorker = EDUtilsParallel.detectNumberOfCPUs(self._iConfigNumberOfWorker)
        self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s nb of workers = %s lockWorker=%s" % (self.getId(), EDPluginSPDCorrectv10.__iNumberOfWorker, EDPluginSPDCorrectv10.__lockWorker._Semaphore__value))
#        self.DEBUG("chooseWorker: \t EDPluginSPDCorrectv10.__lock.acquire(), currently: %i" % EDPluginSPDCorrectv10.__lock._Semaphore__value)
        EDPluginSPDCorrectv10.__lockWorker.acquire()
        for oneWorker in EDPluginSPDCorrectv10.__listOfWorker :
            self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s Status of worker %i: %s" % (self.getId(), oneWorker.pid, oneWorker.getStatus()))
            if (oneWorker.getConfig() == self._SPDconfig)  and (oneWorker.getStatus() in ["free", "uninitialized"]):
                self.worker = oneWorker
        if self.worker is None:
            if len(EDPluginSPDCorrectv10.__listOfWorker) < EDPluginSPDCorrectv10.__iNumberOfWorker :
                self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: Initializing %i th worker" % (self.getId(), len(EDPluginSPDCorrectv10.__listOfWorker)))
                self.worker = SPDworker()
                EDPluginSPDCorrectv10.__listOfWorker.append(self.worker)
                self.worker.setExecutable(self.getExecutable())
                self.workerID = EDPluginSPDCorrectv10.__listOfWorker.index(self.worker)
                self.worker.setLogFilename(os.path.join(self.getSPDCommonDirectory(), "worker-%02i.log" % self.workerID))
                self.worker.initialize(self._SPDconfig)
                self.worker.setTimeOut(self.getTimeOut())
        while self.worker is None:
            self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: No workers still to initialize" % self.getId())
            bConfigOK = False
            for idx, oneWorker in enumerate(EDPluginSPDCorrectv10.__listOfWorker) :
#                self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: %s " % (self.getId(), oneWorker.getConfig()))
#                self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: %s " % (self.getId(), self._SPDconfig))
                #bug1 those string must specifically be the same ... change line 248 in spdCake1.5
                if (oneWorker.getConfig() == self._SPDconfig):
                    bConfigOK = True
                    if (oneWorker.getStatus() in ["free", "uninitialized"]):
                        self.worker = oneWorker
                        self.workerID = idx
            if bConfigOK == False:
                for idx, oneWorker in enumerate(EDPluginSPDCorrectv10.__listOfWorker[:]) :
#                    self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: worker %i status %s " % (self.getId(), idx, oneWorker.status))
                    if (oneWorker.getStatus() in ["free", "uninitialized"]):
                        #Bug2 why doest this work ???
#                        self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: Resetting worker %i status %s " % (self.getId(), idx, oneWorker.status))
                        oneWorker.initialize(self._SPDconfig)
                        self.worker = oneWorker
                        self.workerID = idx
                        EDPluginSPDCorrectv10.__listOfWorker[idx] = (self.worker)
            self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s: Left loop worker %s status %s " % (self.getId(), self.workerID, oneWorker))
            time.sleep(0.1)

        if self.workerID is None:
            self.workerID = EDPluginSPDCorrectv10.__listOfWorker.index(self.worker)
        self.DEBUG("EDPluginSPDCorrectv10.chooseWorker %s Release lockWorker=%s" % (self.getId(), EDPluginSPDCorrectv10.__lockWorker._Semaphore__value))
        EDPluginSPDCorrectv10.__lockWorker.release()

    @staticmethod
    def killAllWorkers():
        """
        this methods finishes the process of all workers process underneath
        """
        for oneWorker in EDPluginSPDCorrectv10.__listOfWorker :
            oneWorker.kill(gentle=True)
            oneWorker.closeLogFile()

    @staticmethod
    def cleanDispMat(_path=None):
        """
        This is to ensure that the displacement matrices are removed between 2 tests,
       if _path is given, try to backup file in this directory
       @param  _path: path to backu file to
       @type _path: python string representing a path.
        """
        for onefile in os.listdir(EDPluginSPDCorrectv10.getSPDCommonDirectory()):
            if onefile.endswith(".edf"):
                myFile = os.path.join(EDPluginSPDCorrectv10.getSPDCommonDirectory(), onefile)
                if _path is not None:
                    try:
                        shutil.move(myFile, os.path.join(_path, onefile))
                    except IOError:
                        EDVerbose.WARNING("Problems in moving EDF displacement matrices from %s to %s" % (myFile, _path))
                else:
                    try:
                        os.remove(myFile)
                    except OSError:
                        EDVerbose.WARNING("Problems in removing EDF displacement matrices: %s" % myFile)

    @staticmethod
    def getSPDCommonDirectory():
        """
        Create a temporary directory common for all SPD process / plugins in order to store displacement matrices
        @return: the name of the common directory
        @rtype: string
        """
        if EDPluginSPDCorrectv10.__strSPDDir is None:
            EDPluginSPDCorrectv10.__strSPDDir = tempfile.mkdtemp(suffix='.tmp', prefix='edna-SPD-')
            EDVerbose.screen("The SPD-EDNA logs and matrices will be in " + EDPluginSPDCorrectv10.__strSPDDir)
        return EDPluginSPDCorrectv10.__strSPDDir


    def setSPDConfig(self, strConfig):
        """
        Setter for the configuration of SPD stored as a command line string
        @param strConfig: the configuration of SPD (without the input filename)
        @type strConfig: string
        """
        self._SPDconfig = strConfig


    def getSPDConfig(self):
        """
        Getter for the configuration of SPD stored as a command line string
        @return: the configuration of SPD (without the input filename)
        @rtype strConfig: string
        """
        if self._SPDconfig == None:
            self.generateSPDCommand()
        return self._SPDconfig


    def setExecutable(self, _edStringExecutable):
        """
        Sets the executable
        """
        self.synchronizeOn()
        self._strConfigExecutable = _edStringExecutable
        self.synchronizeOff()


    def getExecutable(self):
        """
        Sets the executable
        """
        return self._strConfigExecutable


    def getListOfCompatibleVersions(self):
        """
        Returns the list of compatible executable versions the plugin supports
        """
        return self._listCompatibleVersions


    def addCompatibleVersion(self, strCompatibleVersion):
        """
        Adds a compatible executable version to the list
        """
        self._listCompatibleVersions.append(strCompatibleVersion)


    def getCompatibleVersionsStringLine(self):
        """
        This Method constructs a string line by concatening the compatible versions this plugin supports
        This is for Log message purpose only.
        """
        strCompatibleVersionsStringLine = ""
        for compatibleVersion in self._listCompatibleVersions:
            strCompatibleVersionsStringLine += compatibleVersion + " ; "
        return strCompatibleVersionsStringLine


    def setStringVersion(self, _edStringVersion):
        """
        Sets the executable version
        """
        self.synchronizeOn()
        self.strCurrentVersion = _edStringVersion
        self.synchronizeOff()


    def getStringVersion(self):
        """
        Returns the executable version
        """
        returnValue = None
        if (self.strCurrentVersion is not None):
            returnValue = self.strCurrentVersion
        return returnValue

    #@property such decorators are not yet available in python2.5 !!!!
    def getFireAndForget(self):
        return self._bFireAndForget

    #@bFireAndForget.setter
    def setFireAndForget(self, _bFireNF):
        self._bFireAndForget = _bFireNF
    bFireAndForget = property(getFireAndForget, setFireAndForget)

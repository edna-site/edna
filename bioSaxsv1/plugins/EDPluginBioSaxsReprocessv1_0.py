# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Jérôme Kieffer
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
ReImplementation of the Reprocess script  ( by ricardo.fernandes@esrf.fr)
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDUtilsBioSaxs     import EDUtilsBioSaxs
from XSDataBioSaxsReprocess import XSDataInputBioSaxsReprocessv1_0
from XSDataBioSaxsReprocess import XSDataResultBioSaxsReprocessv1_0






class EDPluginBioSaxsReprocessv1_0(EDPluginControl):
    """
    Control plugin that does what was in the Reprocess function in the original program 
    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsReprocessv1_0)
        self.__strControlledPluginName = "EDPluginExecTemplate"
        self.xsdInputData = None
        self.__edPluginExecTemplate = None
        self.dictRunFrame = {} #key=run number as string, value: list of frame numbers (as strings again) 
        self.strDetector = None
        self.strOperation = None
        self.strDirectory = None
        self.strRawDir = None
        self.str1dDir = None
        self.str2dDir = None
        self.strMiscDir = None
        self.strPrefix = None
        self.specStatus = None
        self.specVersion = None
        self.specAbort = None
        self.beamCenterX = None
        self.pixelSizeX = None
        self.beamCenterY = None
        self.pixelSizeY = None
        self.firstFrame = 0
        self.lastFrame = sys.maxint - 1
        self.beamStopDiode = None
        self.code = None
        self.comments = None
        self.concentration = None
        self.keepOriginal = True
        self.machineCurrent = None
        self.wavelength = None
        self.runNumber = None
        self.maskFile = None
        self.normalisation = None
        self.bIsOnline = False





    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.xsdInputData = self.dataInput
        self.checkMandatoryParameters(self.xsdInputData.getDetector(), "No detector found !")
        self.checkMandatoryParameters(self.xsdInputData.getOperation(), "No operation mode found !")
        self.checkMandatoryParameters(self.xsdInputData.getDirectory(), "No source directory defined !")
        self.checkMandatoryParameters(self.xsdInputData.beamStopDiode, "No beamStopDiod defined !")
        self.checkMandatoryParameters(self.xsdInputData.wavelength, "No wavelength given !")
#        self.checkMandatoryParameters(self.xsdInputData.getRunNumber(), "No wavelength given !")
        self.checkMandatoryParameters(self.xsdInputData.getKeepOriginal(), "No Keep Original parameter !")
        self.checkMandatoryParameters(self.xsdInputData.getPixelSizeX(), "No beamCenterX defined !")
        self.checkMandatoryParameters(self.xsdInputData.getPixelSizeY(), "No beamCenterY defined !")
        self.checkMandatoryParameters(self.xsdInputData.getBeamCenterX(), "No beamCenterX defined !")
        self.checkMandatoryParameters(self.xsdInputData.getBeamCenterY(), "No beamCenterY defined !")
#        self.checkMandatoryParameters(self.xsdInputData.getFirstFrame(), "No First Frame given !")
#        self.checkMandatoryParameters(self.xsdInputData.getLastFrame(), "No Last Frame given !")
        self.checkMandatoryParameters(self.xsdInputData.maskFile, "No Mask File given !")
        self.checkMandatoryParameters(self.xsdInputData.getCode(), "No Code given !")
        self.checkMandatoryParameters(self.xsdInputData.getComments(), "No comments given !")
        self.checkMandatoryParameters(self.xsdInputData.getConcentration(), "No Concentration given !")
        self.checkMandatoryParameters(self.xsdInputData.machineCurrent, "No Machine Current given !")
        self.checkMandatoryParameters(self.xsdInputData.getNomalisation(), "No Normalisation given !")
        self.checkMandatoryParameters(self.xsdInputData.getPrefix(), "No Prefix given !")
#        self.checkMandatoryParameters(self.xsdInputData.get(), "No  given !")



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.preProcess")
        # Load the execution plugin
        self.__edPluginExecTemplate = self.loadPlugin(self.__strControlledPluginName)

        self.strDetector = self.xsdInputData.getDetector().value
        self.strOperation = self.xsdInputData.getOperation().value
        self.strDirectory = self.xsdInputData.getDirectory().value
        self.beamCenterX = self.xsdInputData.getBeamCenterX().value
        self.pixelSizeX = self.xsdInputData.getPixelSizeX().value
        self.beamCenterY = self.xsdInputData.getBeamCenterY().value
        self.pixelSizeY = self.xsdInputData.getPixelSizeY().value


        self.beamStopDiode = self.xsdInputData.beamStopDiode.value
        self.code = self.xsdInputData.getCode().value
        self.comments = self.xsdInputData.getComments().value
        self.concentration = self.xsdInputData.getConcentration().value
        self.keepOriginal = bool(self.xsdInputData.getKeepOriginal().value)
        self.machineCurrent = self.xsdInputData.machineCurrent.value
        self.wavelength = self.xsdInputData.wavelength.value
        self.strPrefix = self.xsDataInputSPD.getPrefix.value

        self.normalisation = self.xsdInputData.getNomalisation().value
        self.maskFile = self.xsdInputData.maskFile.getPath().value

        if self.xsdInputData.getRunNumber() is not None:
            self.runNumber = self.xsdInputData.getRunNumber().value

        if self.xsdInputData.getSpecVersion() is not None:
            self.specVersion = self.xsdInputData.getSpecVersion().value
        if self.xsdInputData.getSpecVariableAbort() is not None:
            self.specAbort = self.xsdInputData.getSpecVariableAbort().value
        if self.xsdInputData.getSpecVariableStatus() is not None:
            self.specStatus = self.xsdInputData.getSpecVariableStatus().value
        if self.specVersion and  self.specAbort and  self.specStatus:
            EDUtilsBioSaxs.initSpec(self.specVersion, self.specStatus, self.specAbort)

        if not os.path.isfile(self.maskFile):
            self.showMessage(4, "Mask file '%s' not found!" % self.strDirectory)
            self.setFailure()

#        if self.strOperation not in ("-2", "-1", "0", "1", "2", "3"):
        if self.strOperation not in ["normalisation", "reprocess", "average", "complete"]:
            self.showMessage(4, "Invalid operation '%s'!" % self.strOperation)
            self.setFailure()

        self.firstFrame = self.xsdInputData.getFirstFrame().value
        self.lastFrame = self.xsdInputData.getLastFrame().value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.process")

        if not os.path.isdir(self.strDirectory):
            self.showMessage(4, "Directory '%s' not found!" % self.strDirectory)
            self.setFailure()

        self.strRawDir = os.path.join(self.strDirectory, "raw")
        if not os.path.isdir(self.strRawDir):
            self.showMessage(4, "Directory  Raw '%s' not found!" % self.strRawDir)
            self.setFailure()

        self.str1dDir = os.path.join(self.strDirectory, "1d")
        if not os.path.isdir(self.str1dDir):
            try:
                os.mkdir(self.str1dDir)
            except :
                self.showMessage(4, "Could not create directory '1d' in '%s'!" % self.strDirectory)
                self.setFailure()

        self.str2dDir = os.path.join(self.strDirectory, "2d")
        if not os.path.exists(self.str2dDir):
            try:
                os.mkdir(self.str2dDir)
            except Exception:
                self.showMessage(4, "Could not create directory '2d' in '%s'!" % self.strDirectory)
                self.setFailure()

        self.strMiscDir = os.path.join(self.strDirectory, "misc")
        if not os.path.exists(self.strMiscDir):
            try:
                os.mkdir(self.strMiscDir)
            except Exception:
                self.showMessage(4, "Could not create directory 'misc' in '%s'!" % self.strDirectory)
                self.setFailure()



#        runNumberList = []
        iFirstFrame = int(self.firstFrame)
        iLastFrame = int(self.lastFrame)
        if self.runNumber is None:
            for filename in os.listdir(self.strRawDir):
                fullPathFilename = os.path.join(self.strRawDir, filename)
                if os.path.isfile(fullPathFilename):
                    prefix, run, frame, extra, extension = EDUtilsBioSaxs.getFilenameDetails(filename)
                    try:
                        iFrame = int(frame)
                    except ValueError:
                        iFrame = -1
                    if (prefix == self.strPrefix) and (run != "") and\
                            (iFrame >= iFirstFrame) and (iFrame <= iLastFrame) and \
                            ((self.strDetector == "pilatus" and extension == "edf") or \
                            (self.strDetector == "vantec" and extension == "gfrm")):
                        if run not in self.dictRunFrame:
                            self.dictRunFrame[run] = [frame]
                        else:
                            self.dictRunFrame[run].append(frame)
        else:


            if self.bIsOnline: #just treat the last frame of the runs
                for run in self.runNumber.split(","):
                    self.dictRunFrame[run] = ["%02d" % int(self.FrameLast)]
            else:
                listInRunNr = [int(i) for i in self.runNumber.split(",")]
                for filename in os.listdir(self.strRawDir):
                    fullPathFilename = os.path.join(self.strRawDir, filename)
                    if os.path.isfile(fullPathFilename):
                        prefix, run, frame, extra, extension = EDUtilsBioSaxs.getFilenameDetails(filename)
                        try:
                            iRun = int(run)
                        except ValueError:
                            iRun = -1
                        try:
                            iFrame = int(frame)
                        except ValueError:
                            iFrame = -1
                        if (prefix == self.strPrefix) and (iRun in listInRunNr) and \
                                (iFrame >= iFirstFrame) and (iFrame <= iLastFrame)  and \
                                ((self.strDetector == "pilatus" and extension == "edf") or \
                                (self.strDetector == "vantec" and extension == "gfrm")):
                            if run not in self.dictRunFrame:
                                self.dictRunFrame[run] = [frame]
                            else:
                                self.dictRunFrame[run].append(frame)

        if len(self.dictRunFrame) == 0:
            self.showMessage(4, "There are no runs for prefix '%s'!" % self.strPrefix)
            self.setFailure()
        else:
            runNumberList = self.dictRunFrame.keys()
            runNumberList.sort()

#
#        hdfDictionary = HDFDictionary.HDFDictionary()
#
#        dictionaryEDF = "EDF_" + self.strDetector.upper()
#
#        status, dictionary = hdfDictionary.get(os.path.join(sys.path[0], "Reprocess.xml"), dictionaryEDF)
#        if status != 0:
#            self.showMessage(3, "Could not get '%s' dictionary!" % dictionaryEDF)
#
#        #print dictionary

        if not self.keepOriginal:
            directory1D_REP = ""
            directory2D_REP = ""
            directoryMISC_REP = ""
        else:
            i = 0
            while True:
                directory1D_REP = os.path.join(self.str1dDir, "reprocess%i" % i)
                if os.path.isdir(directory1D_REP):
                    i += 1
                else:
                    try:
                        os.mkdir(directory1D_REP)
                    except Exception:
                        self.showMessage(3, "Could not create reprocess directory '%s'!" % directory1D_REP)
                    break

            i = 0
            while True:
                directory2D_REP = os.path.join(self.str2dDir, "reprocess%i" % i)
                if os.path.exists(directory2D_REP):
                    i += 1
                else:
                    try:
                        os.mkdir(directory2D_REP)
                    except Exception:
                        self.showMessage(3, "Could not create reprocess directory '%s'!" % directory2D_REP)
                    break

            i = 0
            while True:
                directoryMISC_REP = os.path.join(self.strMiscDir, "reprocess%i" % i)
                if os.path.exists(directoryMISC_REP):
                    i += 1
                else:
                    try:
                        os.mkdir(directoryMISC_REP)
                    except Exception:
                        self.showMessage(3, "Could not create reprocess directory '%s'!" % directoryMISC_REP)
                    break

        for runNumber in runNumberList:
            doOneRunNumber(runNumber)
        self.showMessage(0, "The data reprocessing is done!")






        self.__edPluginExecTemplate.connectSUCCESS(self.doSuccessExecTemplate)
        self.__edPluginExecTemplate.connectFAILURE(self.doFailureExecTemplate)
        self.__edPluginExecTemplate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsReprocessv1_0()
        self.setDataOutput(xsDataResult)


    def doSuccessExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsReprocessv1_0.doSuccessExecTemplate")


    def doFailureExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsReprocessv1_0.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsReprocessv1_0.doFailureExecTemplate")


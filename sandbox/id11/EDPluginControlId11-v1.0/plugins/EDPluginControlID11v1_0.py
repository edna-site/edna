#
#    Project: ID11
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF
#
#    Principal author:        Regis Perdreau
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

__author__ = "Regis Perdreau"
__license__ = "GPLv3+"
__copyright__ = "Copyright (c) 2011 ESRF"

import os, threading

from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDUtilsTest        import EDUtilsTest
from EDUtilsFile        import EDUtilsFile

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataSPDv1_0")
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataEDFv1_0")

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength


from XSDataWaitFilev1_0 import XSDataInputWaitMultiFile
from XSDataSPDv1_0 import XSDataInputSPDCake
from XSDataEDFv1_0 import XSDataInput1DPowderEDF



from XSDataID11v1_0 import XSDataInputID11
from XSDataID11v1_0 import XSDataResultID11


class EDPluginControlID11v1_0(EDPluginControl):
    """
    Plugin specific to ID11
    """
    __semaphore = threading.Semaphore()
    __dictParamID11XSD = {} #key=filename, value=(dictID11,strXSD


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputID11)
        self.bTimedOut = False
        self.__dictID11 = {}
        self.__strControlledPluginWait = "EDPluginWaitMultiFile"
        self.__edPluginWaitMultipleFile = None
        self.__xsDataInputWaitMultipleFile = XSDataInputWaitMultiFile()
        self.__listProcessedFiles = []
        self.__strControlledPluginSPD = "EDPluginSPDCakev1_5"
        self.__xsDataInputSPDCake = None
        self.__strControlledPluginEDF = "EDPluginExportAsciiPowderv1_0"
        self.bCorrectMask = True


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlID11v1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getParameterFile(), "No parameter file!")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlID11v1_0.preProcess")
        # Read the parameter file
        if self.getDataInput().getCorrectMask() is not None:
            self.bCorrectMask = bool(self.getDataInput().getCorrectMask().getValue())

        strPathToParameterFile = self.getDataInput().getParameterFile().getPath().getValue()

        if os.path.exists(strPathToParameterFile):
            EDPluginControlID11v1_0.__semaphore.acquire()
            if strPathToParameterFile in EDPluginControlID11v1_0.__dictParamID11XSD:
                self.__dictID11, strInputSPDCake = EDPluginControlID11v1_0.__dictParamID11XSD[strPathToParameterFile]
                self.__xsDataInputSPDCake = XSDataInputSPDCake.parseString(strInputSPDCake)
            else:
                self.parseParameterFiles(strPathToParameterFile)
                self.__xsDataInputSPDCake = self.populateXSDataInputSPDCake()
                EDPluginControlID11v1_0.__dictParamID11XSD[strPathToParameterFile] = (self.__dictID11, self.__xsDataInputSPDCake.marshal())
            EDPluginControlID11v1_0.__semaphore.release()
            # Load the execution plugin
            self.synchronizeOn()
            self.__edPluginWaitMultipleFile = self.loadPlugin(self.__strControlledPluginWait)
            self.synchronizeOff()
#            self.__edPluginEDF = self.loadPlugin(self.__strControlledPluginEDF)
            # Paths to the data files
            self.__xsDataInputWaitMultipleFile = XSDataInputWaitMultiFile()
            for xsDataFile in self.getDataInput().getDataFile():
                self.__xsDataInputWaitMultipleFile.addExpectedFile(xsDataFile)
            # we are expecting unsigned int 
            self.__xsDataInputWaitMultipleFile.setExpectedSize(XSDataInteger(512 + 2 * int(self.__dictID11["DIM1_DATA"]) * int(self.__dictID11["DIM2_DATA"])))
            self.__edPluginWaitMultipleFile.setDataInput(self.__xsDataInputWaitMultipleFile)

        else:
            self.ERROR("Path to parameter file does not exist: %s" % strPathToParameterFile)
            self.setFailure()
        xsdOutputDir = self.getDataInput().getOutputdir()
        if xsdOutputDir is not None:
            self.__xsDataInputSPDCake.setOutputDir(xsdOutputDir)
            self.__dictID11["output_dir"] = xsdOutputDir.getPath().getValue()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlID11v1_0.process")
        self.__edPluginWaitMultipleFile.connectSUCCESS(self.doSuccessExecWaitMultipleFile)
        self.__edPluginWaitMultipleFile.connectFAILURE(self.doFailureExecWaitMultipleFile)
        self.__edPluginWaitMultipleFile.executeSynchronous()

        # SPD launch
        if self.bTimedOut:
            self.ERROR("EDPluginControlID11v1_0.process: Wait Multi File ended in Timeout")
            self.setFailure()
            return

        for onefile in self.getDataInput().getDataFile():
            self.synchronizeOn()
            edPluginSPD = self.loadPlugin(self.__strControlledPluginSPD)
            self.__xsDataInputSPDCake.setInputFile(onefile)
            edPluginSPD.setDataInput(self.__xsDataInputSPDCake)
            edPluginSPD.connectSUCCESS(self.doSuccessExecSPDCake)
            edPluginSPD.connectFAILURE(self.doFailureExecSPDCake)
            edPluginSPD.execute()
            self.synchronizeOff()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlID11v1_0.postProcess")
        #Wait for all plugins to finish
        self.synchronizePlugins()
        # Create some output data
        xsDataResult = XSDataResultID11()
        xsDataResult.setOutputFile(self.__listProcessedFiles)
        self.setDataOutput(xsDataResult)


    def populateXSDataInputSPDCake(self, _inputDict=None):
        self.DEBUG("EDPluginControlID11v1_0.populateXSDataInputSPDCake")
        xsDataInputSPDCake = XSDataInputSPDCake()
        if isinstance(_inputDict, dict):
            self.__dictID11 = _inputDict

    # Angle of tilt
        if "ANGLE OF TILT" in self.__dictID11:
            xsDataTilt = XSDataAngle()
            xsDataTilt.setValue(float(self.__dictID11["ANGLE OF TILT"]))
            xsDataTilt.setUnit(XSDataString("deg"))
            xsDataInputSPDCake.setAngleOfTilt(xsDataTilt)

        if "TILT ROTATION" in self.__dictID11:
            xsDataTiltRot = XSDataAngle()
            xsDataTiltRot.setValue(float(self.__dictID11["TILT ROTATION"]))
            xsDataTiltRot.setUnit(XSDataString("deg"))
            xsDataInputSPDCake.setTiltRotation(xsDataTiltRot)

        if "X-PIXEL SIZE" in self.__dictID11:
            xsDataXPixel = XSDataLength()
            xsDataXPixel.setValue(float(self.__dictID11["Y-PIXEL SIZE"]))
            xsDataXPixel.setUnit(XSDataString("micron"))
            xsDataInputSPDCake.setPixelSizeX(xsDataXPixel)

        if "Y-PIXEL SIZE" in self.__dictID11:
            xsDataYPixel = XSDataLength()
            xsDataYPixel.setValue(float(self.__dictID11["Y-PIXEL SIZE"]))
            xsDataYPixel.setUnit(XSDataString("micron"))
            xsDataInputSPDCake.setPixelSizeY(xsDataYPixel)

        if "DISTANCE" in self.__dictID11:
            xsDataDistance = XSDataLength()
            xsDataDistance.setValue(float(self.__dictID11["DISTANCE"]))
            xsDataDistance.setUnit(XSDataString("mm"))
            xsDataInputSPDCake.setSampleToDetectorDistance(xsDataDistance)

        if "WAVELENGTH" in self.__dictID11:
            xsDataWaweLength = XSDataWavelength()
            xsDataWaweLength.setValue(float(self.__dictID11["WAVELENGTH"]))
            xsDataWaweLength.setUnit(XSDataString("A"))
            xsDataInputSPDCake.setWavelength(xsDataWaweLength)

        if "DIM1_DATA" in self.__dictID11:
            xsDataBufferSizeX = XSDataInteger(int(self.__dictID11["DIM1_DATA"]))
            xsDataInputSPDCake.setBufferSizeX(xsDataBufferSizeX)

        if "DIM2_DATA" in self.__dictID11:
            xsDataBufferSizeY = XSDataInteger(int(self.__dictID11["DIM2_DATA"]))
            xsDataInputSPDCake.setBufferSizeY(xsDataBufferSizeY)

    # Dark current
        if ("DARK CURRENT" in self.__dictID11) and (self.__dictID11["DARK CURRENT"] == "YES") :
            if  ("DC FILE" in self.__dictID11) and os.path.isfile(self.__dictID11["DC FILE"]):
                xsDataFile = XSDataFile()
                xsDataFile.setPath(XSDataString(self.__dictID11["DC FILE"]))
                xsDataInputSPDCake.setDarkCurrentImageFile(xsDataFile)
            else:
                self.warning("Asked for DC Current correction but no DC current file")

        if ("FLAT-FIELD" in self.__dictID11) and (self.__dictID11["FLAT-FIELD"] == "YES"):
            if  ("FF FILE" in self.__dictID11) and os.path.isfile(self.__dictID11["FF FILE"]):
                xsDataFile = XSDataFile()
                xsDataFile.setPath(XSDataString(self.__dictID11["FF FILE"]))
                xsDataInputSPDCake.setFlatFieldImageFile(xsDataFile)
            else:
                self.warning("Asked for FLAT-FIELD correction but no FLAT-FIELD file")

        if ("MASK FILE" in self.__dictID11) and (self.__dictID11["USE MASK"] == "YES") :
            if  ("MASK FILE" in self.__dictID11) and os.path.isfile(self.__dictID11["MASK FILE"]):
                xsDataFile = XSDataFile()
                xsDataFile.setPath(XSDataString(self.__dictID11["MASK FILE"]))
                xsDataInputSPDCake.setMaskFile(xsDataFile)
            else:
                self.warning("Asked for DC Current correction but no DC current file")


        if ("FF SCALE" in self.__dictID11) and (self.__dictID11["FF SCALE"] == "YES"):
            if ("FF MULTIPLIER" in self.__dictID11):
                try:
                    value = float(self.__dictID11["FF MULTIPLIER"])
                except Exception:
                    self.warning("Asked for FF SCALE correction but FF MULTIPLIER provided (%s) in not float !" % (self.__dictID11["FF MULTIPLIER"]))
                else:
                     xsDataInputSPDCake.setIntensityScaleFactor(XSDataDouble(1 / value))
            else:
                self.warning("Asked for FF SCALE correction but no FF MULTIPLIER provided")


        if ("SPATIAL DIS." in self.__dictID11) and (self.__dictID11["SPATIAL DIS."] == "YES"):
            if  ("SD FILE" in self.__dictID11) and  os.path.isfile(self.__dictID11["SD FILE"]):
                xsDataFile = XSDataFile()
                xsDataFile.setPath(XSDataString(self.__dictID11["SD FILE"]))
                xsDataInputSPDCake.setSpatialDistortionFile(xsDataFile)
            else :
                self.warning("Asked for SPATIAL DISTORSION correction but no SPATIAL DISTORSION file")

        if "START AZIMUTH" in self.__dictID11:
            xsDataAzimuthStart = XSDataAngle()
            xsDataAzimuthStart.setValue(float(self.__dictID11["START AZIMUTH"]))
            xsDataAzimuthStart.setUnit(XSDataString("deg"))
            xsDataInputSPDCake.setStartAzimuth(xsDataAzimuthStart)

        if "END AZIMUTH" in self.__dictID11:
            xsDataAzimuthStop = XSDataAngle()
            xsDataAzimuthStop.setValue(float(self.__dictID11["END AZIMUTH"]))
            xsDataAzimuthStop.setUnit(XSDataString("deg"))
            xsDataInputSPDCake.setStopAzimuth(xsDataAzimuthStop)

        if "AZIMUTH BINS" in self.__dictID11:
            xsDataAzimuthStep = XSDataAngle()
            xsDataAzimuthStep.setValue((float(self.__dictID11["END AZIMUTH"]) - float(self.__dictID11["START AZIMUTH"])) /
                                       float(self.__dictID11["AZIMUTH BINS"]))
            xsDataAzimuthStep.setUnit(XSDataString("deg"))
            xsDataInputSPDCake.setStepAzimuth(xsDataAzimuthStep)

        if "INNER RADIUS" in self.__dictID11:
            xsDataInnerRadius = XSDataDouble()
            xsDataInnerRadius.setValue(float(self.__dictID11["INNER RADIUS"]))
            xsDataInputSPDCake.setInnerRadius(xsDataInnerRadius)

        if "OUTER RADIUS" in self.__dictID11:
            xsDataOuterRadius = XSDataDouble()
            xsDataOuterRadius.setValue(float(self.__dictID11["OUTER RADIUS"]))
            xsDataInputSPDCake.setOuterRadius(xsDataOuterRadius)

        if "X-BEAM CENTRE" in self.__dictID11:
            xsDataXBeamCentre = XSDataDouble()
            xsDataXBeamCentre.setValue(float(self.__dictID11["X-BEAM CENTRE"]))
            xsDataInputSPDCake.setBeamCentreInPixelsX(xsDataXBeamCentre)

        if "Y-BEAM CENTRE" in self.__dictID11:
            xsDataYBeamCentre = XSDataDouble()
            xsDataYBeamCentre.setValue(float(self.__dictID11["Y-BEAM CENTRE"]))
            xsDataInputSPDCake.setBeamCentreInPixelsY(xsDataYBeamCentre)

#        if "saving_format" in self.__dictID11:
#            xsSaveFormat = XSDataString()
#            if self.__dictID11["saving_format"] == "SPREAD SHEET":
#                xsSaveFormat.setValue("spr")
#            elif self.__dictID11["saving_format"] == "CIF":
#                xsSaveFormat.setValue("cif")
#            elif self.__dictID11["saving_format"] == "CHIPLOT":
#                xsSaveFormat.setValue("chi")
#            else:
#                xsSaveFormat.setValue("edf")
#            xsDataInputSPDCake.setOutputFileType(xsSaveFormat)

        if "output_dir" in self.__dictID11:
            xsOutputDir = XSDataFile()
            xsOutputDir.setPath(XSDataString(self.__dictID11["output_dir"]))
            xsDataInputSPDCake.setOutputDir(xsOutputDir)

        #Default options to SPD
        xsDataInputSPDCake.setOutputFileType(XSDataString("azim"))
        xsDataInputSPDCake.setDeleteCorImg(XSDataBoolean(not self.isVerboseDebug()))
        xsDataInputSPDCake.setCorrectTiltMask(XSDataBoolean(self.bCorrectMask))
        return xsDataInputSPDCake


    def parseParameterFiles(self, _strPath):
        """
        parses Configuration file
        """
        self.DEBUG("EDPluginControlID11v1_0.parseParameterFiles")
        self.__dictID11 = {}
        dictSub = {"${TEST_DATA_IMAGES_HOME}": EDUtilsTest.getTestsDataImagesHome()}
        for linefile in EDUtilsFile.readFileAndParseVariables(_strPath, dictSub).split("\n"):
            strLineData = linefile.strip()
            #discard comment lines 
            if not strLineData.startswith('#') :
                #  discard end line carriage return
                splited = strLineData.split("=", 1)
                if len(splited) == 2:
                    self.__dictID11[splited[0].strip()] = splited[1].strip()
        return self.__dictID11


    def doSuccessExecWaitMultipleFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID11v1_0.doSuccessExecWaitMultipleFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlID11v1_0.doSuccessExecWaitMultipleFile")
        xsDataResult = self.__edPluginWaitMultipleFile.getDataOutput()
        self.bTimedOut = xsDataResult.getTimedOut().getValue()
#        self.screen("got TimeOut=%s Type is %s" % (self.bTimedOut, type(self.bTimedOut)))


    def doFailureExecWaitMultipleFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID11v1_0.doFailureExecWaitMultipleFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlID11v1_0.doFailureExecWaitMultipleFile")
        self.setFailure()


    def doSuccessExecSPDCake(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginControlID11v1_0.doSuccessExecSPDCake")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlID11v1_0.doSuccessExecSPDCake")

        xsdOut = _edPlugin.getDataOutput()

        xsdAzimFile = xsdOut.getCakedFile()
        xsdIn = XSDataInput1DPowderEDF()
        xsdIn.setEdfFile(xsdAzimFile)

        strInputFile = os.path.basename(_edPlugin.getDataInput().getInputFile().getPath().getValue())
        xsdFile = XSDataFile()
        xsdFile.setPath(XSDataString(
               os.path.join(self.__dictID11["output_dir"], os.path.splitext(strInputFile)[0] + "." + self.__dictID11["output_extn"])
                                     ))
        xsdIn.setOutputFile(xsdFile)

        xsdIn.setEdfFile(xsdOut.getCakedFile())

        xsdIn.setOutputFormat(XSDataString(self.__dictID11["output_extn"]))
        xsdIn.setNumberOfBins(XSDataInteger(int(self.__dictID11["RADIAL BINS"])))

        # EDF Launch
        edPluginEDF = self.loadPlugin(self.__strControlledPluginEDF)
        edPluginEDF.setDataInput(xsdIn)
        edPluginEDF.connectSUCCESS(self.doSuccessExec1DPowderEDF)
        edPluginEDF.connectFAILURE(self.doFailureExec1DPowderEDF)
        edPluginEDF.execute()
        self.synchronizeOff()


    def doFailureExecSPDCake(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginControlID11v1_0.doFailureExecSPDCake")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlID11v1_0.doFailureExecSPDCake")
        xsd = _edPlugin.getDataInput()
        if xsd is not None:
            filename = xsd.getInputFile().getPath().getValue()
            self.ERROR("SPD ended in error with file %s" % filename)
        else:
            self.ERROR("SPD ended in error with no input data (!!!!)")
        self.setFailure()
        self.synchronizeOff()


    def doSuccessExec1DPowderEDF(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID11v1_0.doSuccessExec1DPowderEDF")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlID11v1_0.doSuccessExec1DPowderEDF")
        self.synchronizeOn()
        self.__listProcessedFiles.append(_edPlugin.getDataOutput().getOutputFile())
        self.synchronizeOff()


    def doFailureExec1DPowderEDF(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID11v1_0.doFailureExec1DPowderEDF")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlID11v1_0.doFailureExec1DPowderEDF")
        self.setFailure()




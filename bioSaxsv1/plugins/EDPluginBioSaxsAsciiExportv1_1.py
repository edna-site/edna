# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:    Jérôme Kieffer
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
__copyright__ = "ESRF"
__date__ = "20110913"

import os, shutil
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon       import XSDataString, XSDataInteger, XSDataFile
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsAsciiExportv1_0, XSDataResultBioSaxsAsciiExportv1_0, XSDataInputBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile
from XSDataSaxsv1_0     import XSDataInputSaxsCurvesv1_0

class EDPluginBioSaxsAsciiExportv1_1(EDPluginControl):
    """
    Control for Bio Saxs ascii export of integrated data : 
    * Wait for the file to arrive
    * Retrieve metadata from the header
    * export as 3-column ascii file (EDPluginSaxsCurvesv1_0)
    * rewrite metadata    
    """
    TEMP_ASCII_DATA = "temp.dat"

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAsciiExportv1_0)
        self.__strControlledPluginSaxsCurves = "EDPluginExecSaxsCurvesv1_1"
        self.__strControlledPluginWaitFile = "EDPluginWaitFile"
        self.__strControlledPluginSaxsGetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginSaxsCurves = None
        self.__edPluginWaitFile = None
        self.__edPluginSaxsGetMetadata = None

        self.integratedImage = None
        self.integratedCurve = None


        self.detector = None
        self.detectorDistance = None
        self.pixelSize_1 = None
        self.pixelSize_2 = None
        self.beamCenter_1 = None
        self.beamCenter_2 = None
        self.beamStopDiode = None
        self.wavelength = None
        self.maskFile = None
        self.normalizationFactor = None
        self.machineCurrent = None

        self.code = None
        self.comments = None
        self.concentration = None

        self.strProcessLog = ""
        self.xsdResult = XSDataResultBioSaxsAsciiExportv1_0()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.getIntegratedImage(), "Missing integratedImage")
        self.checkMandatoryParameters(self.dataInput.getIntegratedCurve(), "Missing integratedCurve")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.preProcess")
        # Load the execution plugins
        self.__edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)
        self.__edPluginSaxsCurves = self.loadPlugin(self.__strControlledPluginSaxsCurves)

        self.integratedImage = self.dataInput.getIntegratedImage().path.value
        self.integratedCurve = self.dataInput.getIntegratedCurve().path.value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.process")
        xsdiWaitFile = XSDataInputWaitFile()
        xsdiWaitFile.setExpectedFile(self.dataInput.getIntegratedImage())
        xsdiWaitFile.setExpectedSize(XSDataInteger(8196)) #size of the header
        self.__edPluginWaitFile.setDataInput(xsdiWaitFile)
        self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        self.__edPluginWaitFile.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSucessGetMetadata)
            self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
            self.__edPluginSaxsGetMetadata.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsCurves.connectSUCCESS(self.doSuccessSaxsCurves)
            self.__edPluginSaxsCurves.connectFAILURE(self.doFailureSaxsCurves)
            self.__edPluginSaxsCurves.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.postProcess")
        self.synchronizeOn()
        #remove the terminal carriage return
        if self.strProcessLog.endswith("\n"):
            self.strProcessLog = self.strProcessLog[:-1]
        # Create some output data
        self.xsdResult.setProcessLog(XSDataString(self.strProcessLog))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("Comment generated ...\n" + self.strProcessLog)
        self.synchronizeOff()


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAsciiExportv1_1.doSuccessWaitFile")

        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.dataInput.getIntegratedImage())
        if self.dataInput.sample is not None:
            xsdiMetadata.code = self.dataInput.sample.code
            xsdiMetadata.concentration = self.dataInput.sample.concentration
            xsdiMetadata.comments = self.dataInput.sample.comments
        if self.dataInput.experimentSetup is not None:
            xsdiMetadata.detector = self.dataInput.experimentSetup.detector
            xsdiMetadata.detectorDistance = self.dataInput.experimentSetup.detectorDistance
# this is deliberately taken out as pixels size are redefined during integration JK
#            xsdiMetadata.pixelSize_1 = self.dataInput.experimentSetup.pixelSize_1
#            xsdiMetadata.pixelSize_2 = self.dataInput.experimentSetup.pixelSize_2
            xsdiMetadata.beamCenter_1 = self.dataInput.experimentSetup.beamCenter_1
            xsdiMetadata.beamCenter_2 = self.dataInput.experimentSetup.beamCenter_2
            xsdiMetadata.beamStopDiode = self.dataInput.experimentSetup.beamStopDiode
            xsdiMetadata.wavelength = self.dataInput.experimentSetup.wavelength
            xsdiMetadata.machineCurrent = self.dataInput.experimentSetup.machineCurrent
            xsdiMetadata.maskFile = self.dataInput.experimentSetup.maskFile
            xsdiMetadata.normalizationFactor = self.dataInput.experimentSetup.normalizationFactor
        self.__edPluginSaxsGetMetadata.setDataInput(xsdiMetadata)


    def doFailureWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAsciiExportv1_1.doFailureWaitFile")
        self.strProcessLog += "Timeout in waiting for file '%s'\n" % (self.integratedImage)
        self.setFailure()


    def doSucessGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.doSucessGetMetadata")
        if _edPlugin.getDataOutput().getDetector() is not None:
            self.detector = _edPlugin.getDataOutput().getDetector().value
        if _edPlugin.getDataOutput().detectorDistance is not None:
            self.detectorDistance = _edPlugin.getDataOutput().detectorDistance.value
        if _edPlugin.getDataOutput().beamCenter_1 is not None:
            self.beamCenter_1 = _edPlugin.getDataOutput().beamCenter_1.value
        if _edPlugin.getDataOutput().pixelSize_1 is not None:
            self.pixelSize_1 = _edPlugin.getDataOutput().pixelSize_1.value
        if _edPlugin.getDataOutput().beamCenter_2 is not None:
            self.beamCenter_2 = _edPlugin.getDataOutput().beamCenter_2.value
        if _edPlugin.getDataOutput().pixelSize_2 is not None:
            self.pixelSize_2 = _edPlugin.getDataOutput().pixelSize_2.value
        if _edPlugin.getDataOutput().beamStopDiode is not None:
            self.beamStopDiode = _edPlugin.getDataOutput().beamStopDiode.value
        if _edPlugin.getDataOutput().code is not None:
            self.code = _edPlugin.getDataOutput().code.value
        if _edPlugin.getDataOutput().comments is not None:
            self.comments = _edPlugin.getDataOutput().comments.value
        if _edPlugin.getDataOutput().concentration is not None:
            self.concentration = _edPlugin.getDataOutput().getConcentration().value
        else:
            self.WARNING("Conc: %s" % _edPlugin.getDataOutput().marshal())
        if _edPlugin.getDataOutput().machineCurrent is not None:
            self.machineCurrent = _edPlugin.getDataOutput().machineCurrent.value
        if _edPlugin.getDataOutput().wavelength is not None:
            self.wavelength = _edPlugin.getDataOutput().wavelength.value
        if _edPlugin.getDataOutput().normalizationFactor is not None:
            self.normalizationFactor = _edPlugin.getDataOutput().normalizationFactor.value
        if _edPlugin.getDataOutput().maskFile is not None:
            self.maskFile = _edPlugin.getDataOutput().maskFile.path.value
        xsdiSaxsCurves = XSDataInputSaxsCurvesv1_0()
        xsdiSaxsCurves.inputImage = self.dataInput.getIntegratedImage()
        xsdiSaxsCurves.outputDataFile = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.TEMP_ASCII_DATA)))
        xsdiSaxsCurves.setOptions(XSDataString('+pass -scf 2_pi  -spc \"  \" '))
        self.__edPluginSaxsCurves.setDataInput(xsdiSaxsCurves)


    def doFailureGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_0.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_0.doFailureGetMetadata")
        self.strProcessLog += "Failure in GetMetadata retrieval from '%s'\n" % (self.integratedImage)
        self.setFailure()



    def doSuccessSaxsCurves(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.doSuccessSaxsCurves")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAsciiExportv1_1.doSuccessSaxsCurves")
        self.xsdResult.setIntegratedCurve(self.dataInput.getIntegratedCurve())
        self.strProcessLog += "Successful production of an ASCII 3-column spectrum in '%s'\n" % (self.integratedCurve)
        self.rewriteAsciiHeader()

    def doFailureSaxsCurves(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAsciiExportv1_1.doFailureSaxsCurves")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAsciiExportv1_1.doFailureSaxsCurves")
        self.strProcessLog += "Error during the call of saxs_curves for the production of '%s'\n" % (self.integratedCurve)


    def rewriteAsciiHeader(self):
        #if EDVerbose.isVerboseDebug():
        lines = open(os.path.join(self.getWorkingDirectory(), self.TEMP_ASCII_DATA), "rb").readlines()
        headerMarker = None
        headers = []
        firstData = None
        for oneLine in lines:
            stripedLine = oneLine.strip()
            if headerMarker  is None and len(stripedLine) > 0:
                headerMarker = stripedLine[0]
            if len(stripedLine) == 0:
                continue
            elif stripedLine.startswith(headerMarker) :
                headers.append(stripedLine[1:].strip())
            else:
                firstData = lines.index(oneLine)
                break
        outFile = open(self.integratedCurve, "wb")
        outFile.write("# %s \r\n" % self.comments)
        outFile.write("#Sample c= %s mg/ml \r\n# \r\n# Sample environment:\r\n" % self.concentration)


        if  self.detector is not None:
            outFile.write("# Detector = %s \r\n" % self.detector)
#        if self.detectorDistance is not None:
#            outFile.write("# DetectorDistance: %s \r\n" % self.detectorDistance)
        if self.pixelSize_1 is not None:
            outFile.write("# PixelSize_1 = %s \r\n" % self.pixelSize_1)
        if self.pixelSize_2 is not None:
            outFile.write("# PixelSize_2 = %s \r\n" % self.pixelSize_2)
#        if self.beamCenter_1 is not None:
#            outFile.write("# BeamCenter_1 = %s \r\n" % self.beamCenter_1)
#        if self.beamCenter_2  is not None:
#            outFile.write("# BeamCenter_2 = %s \r\n" % self.beamCenter_2)
#        if self.beamStopDiode is not None:
#            outFile.write("# BeamStopDiode: %s \r\n" % self.beamStopDiode)
#        if self.wavelength  is not None:
#            outFile.write("# Wavelength: %s \r\n" % self.wavelength)
#        if self.maskFile is not  None:
#            outFile.write("# MaskFile: %s \r\n" % self.maskFile)
#        if self.normalizationFactor is not  None:
#            outFile.write("# NormalizationFactor: %s \r\n" % self.normalizationFactor)
#        if self.machineCurrent is not  None:
#            outFile.write("# MachineCurrent: %s \r\n" % self.machineCurrent)

        outFile.write("#\r\n")
        for oneLine in headers:
            outFile.write("# %s \r\n" % oneLine.strip())
        outFile.write("# \r\n# Sample Information:\r\n")
        outFile.write("# Concentration: %s\r\n" % self.concentration)
        outFile.write("# Code: %s\r\n" % self.code)
        outFile.write("\r\n".join([i.strip() for i in lines[firstData:]]))
        outFile.close()



# This text should be what the user writes in the comments box of BsxCuBE (limited length)
# Sample c=  6.22 mg/ml
#
# Beamline Parameters
# SampleDistance =  2.430000e+00 
# WaveLength =  9.310000e-11 
# DiodeCurr=0.000129738
# MachCurr=191.655 mA
# Normalisation: 0.0001
# 
# Image Processing Parameters
# Mask: /data/id14eh3/archive/CALIBRATION/MASK/P_25Aug_msk.edf
# Xpix = 172.0 um 
# Xpix = 172.0_um 
# X centre = 866
# Y center = 101
# Dim_1 =  1279 
# Dummy = -2.000000e+00 
# DDummy =  1.100000e+00 
# -ofac = 0.771004078612 
#
# Processing History
# History-1 = saxs_mac +var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 -otit " " -i1dis 2.43 -i1wvl 0.0931_nm -i1pix 172.0_um 172.0_um -i1cen 866 101 -ofac  0.771004078612 /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/raw/Tata_005_10.edf /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/2d/Tata_005_10.edf 
# History-2 = saxs_add -omod n /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/2d/Tata_005_10.edf /data/id14eh3/archive/CALIBRATION/MASK/P_25Aug_msk.edf /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_10.msk 
# History-3 = saxs_angle -omod n -rsys normal -da 360_deg -odim = 1 /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_10.msk /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_10.ang 
# History-4 = saxs_mac -omod n +var -add 10 -ofac 0.1 /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_%%.ang,1,10 /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_ave.ang 
# History-5 = saxs_curves -scf 2_pi -ext .dat -spc "  " /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/misc/Tata_005_ave.ang /data/id14eh3/inhouse/saxs_pilatus/commiss/run4_2010/1d/Tata_005_ave.dat 
# 
# Sample Information
#Concentration: 6.22
#Code: bsa2
##0.0406042  16146.8  16.4415
##0.0453812  7526.6  5.67508
##0.0501582  2310.84  2.63989
##0.0549351  1512.84  1.60361
##0.0597121  1279.3  1.21874

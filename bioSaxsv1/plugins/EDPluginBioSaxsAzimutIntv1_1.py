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

import os
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataString
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsAzimutIntv1_0, XSDataResultBioSaxsAzimutIntv1_0, \
                               XSDataInputBioSaxsAsciiExportv1_0, XSDataInputBioSaxsMetadatav1_0
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataSaxsv1_0")
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataSaxsv1_0         import  XSDataInputSaxsAnglev1_0



class EDPluginBioSaxsAzimutIntv1_1(EDPluginControl):
    """
    Control for Bio Saxs azimuthal integration; suppose the mask is already applied by BioSaxsNormalizev1.1 : 
    * wait for normalized file to arrive  (EDPluginWaitFile) 
    * retrieve and update metadata (EDPluginBioSaxsMetadatav1_0)
    * integrate (EDPluginSaxsAnglev1_0)
    * export as spec-file (EDPluginAsciiExportv1_0)    
    
    TODO: remove the plugins marked with # 
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsAzimutIntv1_0)
        self.__strControlledPluginWaitFile = "EDPluginWaitFile"
        self.__strControlledPluginSaxsAngle = "EDPluginExecSaxsAnglev1_0"
        self.__strControlledPluginAsciiExport = "EDPluginBioSaxsAsciiExportv1_1"
        self.__strControlledPluginSaxsGetMetadata = "EDPluginBioSaxsMetadatav1_1"
        self.__edPluginWaitFile = None
        self.__edPluginSaxsAdd = None
        self.__edPluginSaxsAngle = None
        self.__edPluginAsciiExport = None
        self.__edPluginSaxsGetMetadata = None
        self.__edPluginSaxsSetMetadata = None

        self.xsdMetadata = None

        self.normalizedImage = None
        self.integratedImage = None
        self.integratedCurve = None
        self.normalizationFactor = None

        self.lstProcessLog = []

        self.xsdResult = XSDataResultBioSaxsAzimutIntv1_0()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getNormalizedImage(), "Missing normalizedImage")
        self.checkMandatoryParameters(self.getDataInput().getNormalizedImageSize(), "Missing normalizedImageSize")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedImage(), "Missing integratedImage")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedCurve(), "Missing integratedCurve")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.preProcess")
        # Load the execution plugins
        self.__edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
        self.__edPluginSaxsAngle = self.loadPlugin(self.__strControlledPluginSaxsAngle)
        self.__edPluginAsciiExport = self.loadPlugin(self.__strControlledPluginAsciiExport)
        self.__edPluginSaxsGetMetadata = self.loadPlugin(self.__strControlledPluginSaxsGetMetadata)

        self.normalizedImage = self.getDataInput().getNormalizedImage().getPath().getValue()
        self.integratedImage = self.getDataInput().getIntegratedImage().getPath().getValue()
        self.integratedCurve = self.getDataInput().getIntegratedCurve().getPath().getValue()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.process")
        xsdiWaitFile = XSDataInputWaitFile()
        xsdiWaitFile.setExpectedFile(self.getDataInput().getNormalizedImage())
        xsdiWaitFile.setExpectedSize(self.getDataInput().getNormalizedImageSize())
        self.__edPluginWaitFile.setDataInput(xsdiWaitFile)
        self.__edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
        self.__edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
        self.__edPluginWaitFile.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsGetMetadata.connectSUCCESS(self.doSuccessGetMetadata)
            self.__edPluginSaxsGetMetadata.connectFAILURE(self.doFailureGetMetadata)
            self.__edPluginSaxsGetMetadata.executeSynchronous()
        if not self.isFailure():
            self.__edPluginSaxsAngle.connectSUCCESS(self.doSuccessSaxsAngle)
            self.__edPluginSaxsAngle.connectFAILURE(self.doFailureSaxsAngle)
            self.__edPluginSaxsAngle.executeSynchronous()
        if not self.isFailure():
            self.__edPluginAsciiExport.connectSUCCESS(self.doSuccessAsciiExport)
            self.__edPluginAsciiExport.connectFAILURE(self.doFailureAsciiExport)
            self.__edPluginAsciiExport.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.postProcess")

        # Create some output data
        strLog = os.linesep.join(self.lstProcessLog)
        self.xsdResult.setProcessLog(XSDataString(strLog))
        self.setDataOutput(self.xsdResult)
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.postProces: Comments generated: " + os.linesep + strLog)


    def doSuccessWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doSuccessWaitFile")

        self.lstProcessLog.append("Retrieve metadata from file %s" % (self.normalizedImage))
        xsdiMetadata = XSDataInputBioSaxsMetadatav1_0()
        xsdiMetadata.setInputImage(self.getDataInput().getNormalizedImage())
        xsdiMetadata.setSampleConcentration(self.getDataInput().getSampleConcentration())
        xsdiMetadata.setSampleComments(self.getDataInput().getSampleComments())
        xsdiMetadata.setSampleCode(self.getDataInput().getSampleCode())
        xsdiMetadata.setDetector(self.getDataInput().getDetector())
        xsdiMetadata.setDetectorDistance(self.getDataInput().getDetectorDistance())
        xsdiMetadata.setPixelSize_1(self.getDataInput().getPixelSize_1())
        xsdiMetadata.setPixelSize_2(self.getDataInput().getPixelSize_2())
        xsdiMetadata.setBeamCenter_1(self.getDataInput().getBeamCenter_1())
        xsdiMetadata.setBeamCenter_2(self.getDataInput().getBeamCenter_2())
        xsdiMetadata.setWavelength(self.getDataInput().getWavelength())
        xsdiMetadata.setMachineCurrent(self.getDataInput().getMachineCurrent())
        xsdiMetadata.setMaskFile(self.getDataInput().getMaskFile())
        xsdiMetadata.setNormalizationFactor(self.getDataInput().getNormalizationFactor())
        self.__edPluginSaxsGetMetadata.setDataInput(xsdiMetadata)


    def doFailureWaitFile(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doFailureWaitFile")
        self.lstProcessLog.append("Timeout in waiting for file '%s'" % (self.normalizedImage))
        self.setFailure()


    def doSuccessGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doSuccessGetMetadata")
        if _edPlugin is not None:
            self.xsdMetadata = _edPlugin.getDataOutput()
            self.lstProcessLog.append("Azimuthal integration of Corrected+Masked EDF image '%s'." % (self.normalizedImage))
            xsdiSaxsAngle = XSDataInputSaxsAnglev1_0()
            xsdiSaxsAngle.setInputDataFile(self.getDataInput().getNormalizedImage())
            # XSDataFile(XSDataString(self.normalizedImage)))
            xsdiSaxsAngle.setRegroupedDataFile(self.getDataInput().getIntegratedImage())
            xsdiSaxsAngle.setOptions(XSDataString('+pass -omod n -rsys normal -da 360_deg -odim = 1'))
            self.__edPluginSaxsAngle.setDataInput(xsdiSaxsAngle)


    def doFailureGetMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doFailureGetMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doFailureGetMetadata")
        self.lstProcessLog.append("Failure in GetMetadata retrieval from '%s'" % (self.normalizedImage))
        self.setFailure()


    def doSuccessSaxsAngle(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doSuccessSaxsAngle")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doSuccessSaxsAngle")
        self.xsdResult.setIntegratedImage(self.getDataInput().getIntegratedImage())
        self.lstProcessLog.append("Conversion to spec-like file of '%s'" % (self.integratedImage))
        xsdiAsciiExport = XSDataInputBioSaxsAsciiExportv1_0()
        xsdiAsciiExport.setIntegratedImage(self.getDataInput().getIntegratedImage())
        xsdiAsciiExport.setIntegratedCurve(self.getDataInput().getIntegratedCurve())
        self.__edPluginAsciiExport.setDataInput(xsdiAsciiExport)


    def doFailureSaxsAngle(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doFailureSaxsAngle")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doFailureSaxsAngle")
        self.lstProcessLog.append("Error during integration with saxs_angle on '%s'" % (self.integratedImage))
        self.setFailure()


    def doSuccessAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doSuccessAsciiExport")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doSuccessAsciiExport")
        self.xsdResult.setIntegratedCurve(self.getDataInput().getIntegratedCurve())
        output = _edPlugin.getDataOutput()
        if output is not None:
            self.lstProcessLog.append(output.getProcessLog().getValue())



    def doFailureAsciiExport(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginBioSaxsAzimutIntv1_1.doFailureAsciiExport")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsAzimutIntv1_1.doFailureAsciiExport")
        output = _edPlugin.getDataOutput()
        if output is not None:
            self.lstProcessLog.append(output.getProcessLog().getValue())
        self.setFailure()

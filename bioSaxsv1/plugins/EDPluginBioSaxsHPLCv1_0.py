# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 ESRF
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
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2012 ESRF"
__date__ = "20120918"
__status__ = "development"

import os
from EDPluginControl import EDPluginControl
from EDThreading import Semaphore
from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("XSDataBioSaxsv1_0")
edFactoryPlugin.loadModule("XSDataEdnaSaxs")

from XSDataBioSaxsv1_0 import XSDataInputBioSaxsHPLCv1_0, XSDataResultBioSaxsHPLCv1_0, \
                            XSDataInputBioSaxsProcessOneFilev1_0
from XSDataEdnaSaxs import XSDataInputDatcmp, XSDataInputDataver, XSDataInputDatop, XSDataInputSaxsAnalysis
from XSDataCommon import XSDataFile, XSDataStatus, XSDataString, XSDataInteger, XSDataStatus

class HPLCrun(object):
    def __init__(self, runId, first_curve=None):
        self.id = runId
        self.buffer = None
        self.first_curve = first_curve
        self.frames = []
        self.curves = []
        self.for_buffer = []
        if first_curve:
            self.files.append(first_curve)

class EDPluginBioSaxsHPLCv1_0 (EDPluginControl):
    """
    plugin for processing Saxs data coming from HPLC
    
    runs subsequently:
    *ProcessOneFile, 
    *subtraction of buffer 
    *SaxsAnalysis
    """

    strControlledPluginProcessOneFile = "EDPluginBioSaxsProcessOneFilev1_2"
    strControlledPluginDatop = "EDPluginExecDatopv1_0"
    strControlledPluginSaxsAnalysis = "EDPluginControlSaxsAnalysisv1_0"
    strControlledPluginDatCmp = "EDPluginExecDatcmpv1_0"
    strControlledPluginDatAver = "EDPluginExecDataverv1_0"
    dictHPLC = {} #key=runId, value= HPLCrun instance
    _sem = Semaphore()

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsHPLCv1_0)
        self.__edPluginProcessOneFile = None
        self.__edPluginSubtract = None
        self.__edPluginSaxsAnalysis = None
        self.__edPluginDatCmp = None
        self.xsDataResult = XSDataResultBioSaxsHPLCv1_0()
        self.runId = None
        self.FrameId = None
        self.hplc_run = None
        self.curve = None
        self.subtracted = None
        self.lstExecutiveSummary = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image")
        self.checkMandatoryParameters(self.dataInput.sample, "no Sample parameter")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "No experimental setup parameter")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.preProcess")
        sdi = self.dataInput
        if sdi.runId is not None:
            self.runId = sdi.runId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                self.runId = path[::-1].split("_", 1)[1][::-1]
            else:
                self.runId = path
        with self._sem:
            if self.runId not in self.dictHPLC:
                self.dictHPLC[self.runId] = HPLCrun(self.runId)
        self.hplc_run = self.dictHPLC[self.runId]
        if sdi.frameId is not None:
            self.FrameId = sdi.frameId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                digits = os.path.splitext(os.path.basename(path))[0].split("_")[0]
                try:
                    self.FrameId = int(digits)
                except ValueError:
                    self.WARNING("FrameId is supposed to be an integer, I got %s" % digits)
                    self.FrameId = digits
            else:
                self.warning("using frameID=0 in tests, only")
                self.FrameId = 0
        with self._sem:
            self.hplc_run.frames.append(self.FrameId)

        if sdi.bufferCurve and os.path.exists(sdi.bufferCurve.path.value):
            with self._sem:
                self.hplc_run.buffer = sdi.bufferCurve.path.value

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.process")

        xsdIn = XSDataInputBioSaxsProcessOneFilev1_0(rawImage=self.dataInput.rawImage,
                                                    sample=self.dataInput.sample,
                                                    experimentSetup=self.dataInput.experimentSetup,
                                                    rawImageSize=self.dataInput.rawImageSize,
                                                    normalizedImage=self.dataInput.normalizedImage,
                                                    integratedCurve=self.dataInput.integratedCurve,
                                                    runId=self.dataInput.runId,
                                                    frameId=self.dataInput.frameId)
        self.__edPluginProcessOneFile = self.loadPlugin(self.strControlledPluginProcessOneFile)
        self.__edPluginProcessOneFile.dataInput = xsdIn
        self.__edPluginProcessOneFile.connectSUCCESS(self.doSuccessProcessOneFile)
        self.__edPluginProcessOneFile.connectFAILURE(self.doFailureProcessOneFile)
        self.__edPluginProcessOneFile.executeSynchronous()

        if self.isFailure():
            return

        if self.hplc_run.buffer is None:
            xsdIn = XSDataInputDatcmp(inputCurve=[XSDataFile(XSDataString(self.hplc_run.first_curve)),
                                                  XSDataFile(XSDataString(self.curve))])
            self.__edPluginDatCmp = self.loadPlugin(self.strControlledPluginDatCmp)
            self.__edPluginDatCmp.dataInput = xsdIn
            self.__edPluginDatCmp.connectSUCCESS(self.doSuccessDatCmp)
            self.__edPluginDatCmp.connectFAILURE(self.doFailureDatCmp)
            self.__edPluginDatCmp.executeSynchronous()
        if self.isFailure():
            return

        if self.hplc_run.buffer is None:
            return
#    complex type XSDataInputDatop extends XSDataInput {
#    "datop makes an operation on curves"
#    inputCurve: XSDataFile []
#    outputCurve: XSDataFile
#    operation: XSDataString
#    constant: XSDataDouble optional}
        if self.dataInput.subtractedCurve is not None:
            subtracted = self.dataInput.subtractedCurve.path.value
        else:
            subtracted = os.path.splitext(self.curve)[0] + "_sub.dat"
        xsdIn = XSDataInputDatop(inputCurve=[XSDataFile(XSDataString(self.curve)),
                                              XSDataFile(XSDataString(self.hplc_run.first_curve))],
                                 outputCurve=XSDataFile(XSDataString(subtracted)),
                                 operation=XSDataString("sub"))
        self.__edPluginDatop = self.loadPlugin(self.strControlledPluginDatop)
        self.__edPluginDatop.dataInput = xsdIn
        self.__edPluginDatop.connectSUCCESS(self.doSuccessDatop)
        self.__edPluginDatop.connectFAILURE(self.doFailureDatop)
        self.__edPluginDatop.executeSynchronous()

        if self.subtracted and os.path.exists(self.subtracted):
            xsdIn = XSDataInputSaxsAnalysis(scatterCurve=XSDataFile(XSDataString(self.subtracted)),
                                            gnomFile=XSDataFile(XSDataString(os.path.splitext(self.subtracted)[0] + ".out")))
            self.__edPluginSaxsAnalysis = self.loadPlugin(self.strControlledPluginSaxsAnalysis)
            self.__edPluginSaxsAnalysis.dataInput = xsdIn
            self.__edPluginSaxsAnalysis.connectSUCCESS(self.doSuccessSaxsAnalysis)
            self.__edPluginSaxsAnalysis.connectFAILURE(self.doFailureSaxsAnalysis)
            self.__edPluginSaxsAnalysis.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.postProcess")
        if self.hplc_run.buffer:
            self.xsDataResult.bufferCurve = XSDataFile(XSDataString(self.hplc_run.buffer))
        if self.curve:
            self.xsDataResult.integratedCurve = XSDataFile(XSDataString(self.curve))
        if self.subtracted:
             self.xsDataResult.subtractedCurve = XSDataFile(XSDataString(self.subtracted))

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        executiveSummary = os.linesep.join(self.lstExecutiveSummary)
        self.xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        self.dataOutput = self.xsDataResult

    def average_buffers(self):
        """
        Average out all buffers
        """
        self.lstExecutiveSummary.append("Averaging out buffer files: " + ", ".join(self.hplc_run.for_buffer))
        xsdIn = XSDataInputDataver(inputCurve=[XSDataFile(XSDataString(i)) for i in self.hplc_run.for_buffer])
        if self.dataInput.bufferCurve:
            xsdIn.outputCurve = self.dataInput.bufferCurve
        else:
            xsdIn.outputCurve = XSDataFile(XSDataString(self.hplc_run.first_curve[::-1].split("_", 1)[1][::-1] + "_buffer_aver%02i.dat" % len(self.hplc_run.for_buffer)))
        self.__edPluginDatAver = self.loadPlugin(self.strControlledPluginDatAver)
        self.__edPluginDatAver.dataInput = xsdIn
        self.__edPluginDatAver.connectSUCCESS(self.doSuccessDatAver)
        self.__edPluginDatAver.connectFAILURE(self.doFailureDatAver)
        self.__edPluginDatAver.executeSynchronous()

    def doSuccessProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessProcessOneFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessProcessOneFile")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        output = _edPlugin.dataOutput
        if not output.integratedCurve:
            strErr = "Edna plugin ProcessOneFile did not produce integrated curve"
            self.ERROR(strErr)
            self.lstExecutiveSummary.append(strErr)
            self.setFailure()
            return
        self.curve = output.integratedCurve.path.value
        if not os.path.exists(self.curve):
            strErr = "Edna plugin ProcessOneFile: integrated curve not on disk !!"
            self.ERROR(strErr)
            self.lstExecutiveSummary.append(strErr)
            self.setFailure()
            return
        self.xsDataResult.integratedCurve = output.integratedCurve
        self.xsDataResult.normalizedImage = output.normalizedImage
        with self._sem:
            if not self.hplc_run.first_curve:
                 self.hplc_run.first_curve = self.curve
                 self.hplc_run.for_buffer.append(self.curve)
            self.hplc_run.curves.append(self.curve)


    def doFailureProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureProcessOneFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureProcessOneFile")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin ProcessOneFile failed.")
        self.setFailure()

    def doSuccessDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatop")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatop")
        if _edPlugin and _edPlugin.dataOutput:
            output = _edPlugin.dataOutput
            if output.status and  output.status.executiveSummary:
                self.lstExecutiveSummary.append(output.status.executiveSummary.value)
            if output.outputCurve:
                self.subtracted = output.outputCurve.path.value
                if os.path.exists(self.subtracted):
                    self.xsDataResult.subtractedCurve = output.outputCurve
                else:
                    strErr = "Edna plugin datop did not produce subtracted file %s" % subtracted
                    self.ERROR(strErr)
                    self.lstExecutiveSummary.append(strErr)
                    self.setFailure()

    def doFailureDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatop")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatop")
        strErr = "Edna plugin datop failed."
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append(strErr)
        self.ERROR(strErr)
        self.setFailure()

    def doSuccessSaxsAnalysis(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessSaxsAnalysis")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessSaxsAnalysis")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        self.xsDataResult.gnom = _edPlugin.dataOutput.gnom
        self.xsDataResult.volume = _edPlugin.dataOutput.volume
        self.xsDataResult.autoRg = _edPlugin.dataOutput.autoRg

    def doFailureSaxsAnalysis(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        strErr = "Edna plugin SaxsAnalysis failed."
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin SaxsAnalysis failed.")
        self.setFailure()

    def doSuccessDatCmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatCmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatCmp")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.fidelity:
            fidelity = _edPlugin.dataOutput.fidelity.value
        else:
            strErr = "No fidelity in output of datcmp"
            self.error(strErr)
            self.lstExecutiveSummary.append(strErr)
            self.setFailure()
        if fidelity > 0:
            with self._sem:
                self.hplc_run.for_buffer.append(self.curve)
        else:
            self.average_buffers()
#complex type XSDataResultDatcmp extends XSDataResult {
#    "Higher chi-values indicate dis-similarities in the input.\n
#     Fidelity gives the likelihood of the two data sets being identical.
#    "
#    chi: XSDataDouble 
#    fidelity: XSDataDouble
#}
    def doFailureDatCmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatCmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatCmp")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatCmp failed.")
        self.setFailure()


    def doSuccessDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatAver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.outputCurve:
            buffer = _edPlugin.dataOutput.outputCurve.path.value
            if os.path.exists(buffer):
                with self._sem:
                    self.hplc_run.buffer = buffer
            else:
                strErr = "DatAver claimed buffer is in %s but no such file !!!" % buffer
                self.ERROR(strError)
                self.lstExecutiveSummary.append(strError)
                self.setFailure()

    def doFailureDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatAver failed.")
        self.setFailure()


"""
complex type XSDataResultBioSaxsHPLCv1_0 extends XSDataResultBioSaxsSubtractv1_0{
    "Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"
    integratedCurve: XSDataFile
    bufferCurve: XSDataFile optional
//    subtractedCurve : XSDataFile
//    autorg: XSDataAutoRg
//  gnom: XSDataGnom
//    volume: XSDataDoubleWithUnit
}"""
#complex type XSDataResultBioSaxsProcessOneFilev1_0 extends XSDataResult {
#    normalizedImage: XSDataImage
#    integratedImage: XSDataImage optional
#    integratedCurve: XSDataFile

#complex type XSDataResultBioSaxsHPLCv1_0 extends XSDataResultBioSaxsSubtractv1_0{
#    "Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"
#    integratedCurve: XSDataFile
#    bufferCurve: XSDataFile optional
#//    subtractedCurve : XSDataFile
#//    autorg: XSDataAutoRg
#//  gnom: XSDataGnom
#//    volume: XSDataDoubleWithUnit

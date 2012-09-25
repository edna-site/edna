# coding: utf8
#
#    Project:BioSaxs
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
__date__ = "20120920"
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
from XSDataCommon import XSDataFile, XSDataString, XSDataStatus

from EDUtilsBioSaxs import HPLCframe, HPLCrun




class EDPluginBioSaxsHPLCv1_0(EDPluginControl):
    """
    plugin for processing Saxs data coming from HPLC

    runs subsequently:
    *ProcessOneFile,
    *subtraction of buffer
    *SaxsAnalysis

    todo:
    only store references: Wait for flush to construct HDF5 file and (possibly) web pages with PNG graphs
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
        self.frameId = None
        self.frame = None
        self.hplc_run = None
        self.curve = None
        self.subtracted = None
        self.lstExecutiveSummary = []
        self.isBuffer = False

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
            self.frameId = sdi.frameId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                digits = os.path.splitext(os.path.basename(path))[0].split("_")[-1]
                try:
                    self.frameId = int(digits)
                except ValueError:
                    self.WARNING("frameId is supposed to be an integer, I got %s" % digits)
                    self.frameId = digits
            else:
                self.warning("using frameID=0 in tests, only")
                self.frameId = 0
        with self._sem:
            self.frame = HPLCframe(self.runId, self.frameId)
            self.hplc_run.frames[self.frameId] = self.frame

        if sdi.bufferCurve and os.path.exists(sdi.bufferCurve.path.value):
            with self._sem:
                self.hplc_run.buffer = sdi.bufferCurve.path.value

        if self.hplc_run.hdf5_filename:
            hplc = self.hplc_run.hdf5_filename
        elif sdi.hplcFile:
            hplc = sdi.hplcFile.path.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                hplc = "_".join(os.path.splitext(path)[0].split("_")[:-1]) + ".h5"
            else:
                hplc = os.path.splitext(path)[0] + ".h5"

        if not self.hplc_run.hdf5_filename:
            with self._sem:
                self.hplc_run.init_hdf5(hplc)
#        self.xsDataResult.hplcFile = XSDataFile(XSDataString(hplc))

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


        xsdIn = XSDataInputDatcmp(inputCurve=[XSDataFile(XSDataString(self.hplc_run.first_curve)),
                                              XSDataFile(XSDataString(self.curve))])
        self.__edPluginDatCmp = self.loadPlugin(self.strControlledPluginDatCmp)
        self.__edPluginDatCmp.dataInput = xsdIn
        self.__edPluginDatCmp.connectSUCCESS(self.doSuccessDatCmp)
        self.__edPluginDatCmp.connectFAILURE(self.doFailureDatCmp)
        self.__edPluginDatCmp.executeSynchronous()

        if self.isFailure() or self.isBuffer:
            return

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
        if self.frame:
            self.frame.processing = False

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
        if output.experimentSetup and output.experimentSetup.timeOfFrame:
            startTime = output.experimentSetup.timeOfFrame.value
        else:
            startTime = None
        with self._sem:
            if not self.hplc_run.first_curve:
                self.hplc_run.first_curve = self.curve
                self.hplc_run.start_time = startTime
        self.frame.curve = self.curve
        self.frame.time = startTime


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
                    self.frame.subtracted = self.subtracted
                else:
                    strErr = "Edna plugin datop did not produce subtracted file %s" % self.subtracted
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
        gnom = _edPlugin.dataOutput.gnom
        if gnom:
            if gnom.rgGnom:
                self.frame.gnom = gnom.rgGnom.value
            if gnom.dmax:
                self.frame.Dmax = gnom.dmax.value
            if gnom.total:
                self.frame.total = gnom.total.value
            self.xsDataResult.gnom = gnom

        volume = _edPlugin.dataOutput.volume
        if volume:
            self.frame.volume = volume.value
            self.xsDataResult.volume = volume
        rg = _edPlugin.dataOutput.autoRg
        if rg:
            if rg.rg:
                self.frame.Rg = rg.rg.value
            if rg.rgStdev:
                self.frame.Rg_Stdev = rg.rgStdev.value
            if rg.i0:
                self.frame.I0 = rg.i0.value
            if rg.i0Stdev:
                self.frame.I0_Stdev = rg.i0Stdev.value
            if rg.quality:
                self.frame.quality = rg.quality.value
            self.xsDataResult.autoRg = rg

    def doFailureSaxsAnalysis(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        strErr = "Edna plugin SaxsAnalysis failed."
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
            self.lstExecutiveSummary.append(strErr)
        else:
            self.lstExecutiveSummary.append(strErr)
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
            #self.setFailure()
            fidelity = 0
        if self.hplc_run.buffer is None:
            if fidelity > 0:
                self.isBuffer = True
                if fidelity > 0.1:
                    self.hplc_run.for_buffer.append(self.curve)
            else :
                self.average_buffers()
        elif fidelity > 0:
            self.isBuffer = True

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
            bufferCurve = _edPlugin.dataOutput.outputCurve.path.value
            if os.path.exists(bufferCurve):
                with self._sem:
                    self.hplc_run.buffer = bufferCurve
            else:
                strErr = "DatAver claimed buffer is in %s but no such file !!!" % buffer
                self.ERROR(strErr)
                self.lstExecutiveSummary.append(strErr)
                self.setFailure()

    def doFailureDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatAver failed.")
        self.setFailure()



# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF
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
__copyright__ = "2011 ESRF"
__status__ = "development"
__date__ = "20111107"

import os, shutil
from EDPluginControl import EDPluginControl
from XSDataCommon import XSDataFile, XSDataString, XSDataStatus
from XSDataEdnaSaxs import XSDataInputAutoSub, XSDataInputDataver, \
    XSDataInputDatcmp, XSDataInputAutoRg, XSDataInputDatop
from XSDataEdnaSaxs import XSDataResultAutoSub

def copy(src, dst):
    if os.path.exists(src):
        if os.name == "posix":
            if os.path.islink(dst):
                os.unlink(dst)
            os.symlink(src, dst)
        else:
            if os.path.exists(dst):
                os.unlink(dst)
            shutil.copyfile(src, dst)


class EDPluginAutoSubv1_0(EDPluginControl):
    """
    This is an EDNA plugin that tries to mimic the behavour of autosub:
    - find the best buffer (usually the merged one)
    - subtract data with the best buffer  
    """
    BUFFER_SIMILARITY = 1e-300

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputAutoSub)
        self.__strPluginDatop = "EDPluginExecDatopv1_0"
        self.__strPluginDatcmp = "EDPluginExecDatcmpv1_0"
        self.__strPluginDataver = "EDPluginExecDataverv1_0"
        self.__strPluginAutoRg = "EDPluginExecAutoRgv1_0"
        self.__edPluginDatcmp = None
        self.__edPluginDatop = None
        self.__edPluginDataver = None
        self.__edPluginAutoRg = None
        self.xsDataResult = XSDataResultAutoSub()

        self.buffers = []
        self.sampleCurve = None
        self.subtractedCurve = None
        self.outdir = None
        self.bestBuffer = None
        self.averBuffer = None
        self.actualBestBuffer = None
        self.fidelity = None
        self.lstProcessLog = []
        self.dictRg = {} #key: filename, value = (Rg,I0) 


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginAutoSubv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.sampleCurve, "No sample curve")
        self.checkMandatoryParameters(self.dataInput.buffers, "No buffer curves")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginAutoSubv1_0.preProcess")
        # Load the execution plugin
        self.__edPluginDataver = self.loadPlugin(self.__strPluginDataver)

        if self.dataInput.subtractedCurve is not None:
            self.subtractedCurve = self.dataInput.subtractedCurve.path.value
        self.buffers = [ i.path.value for i in self.dataInput.buffers ]
        self.sampleCurve = self.dataInput.sampleCurve.path.value
        if self.subtractedCurve is None:
            self.outdir = os.path.dirname(self.sampleCurve)
        else:
            self.outdir = os.path.dirname(self.subtractedCurve)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginAutoSubv1_0.process")

        basename = os.path.splitext(os.path.basename(self.sampleCurve))[0]
        self.bestBuffer = os.path.join(self.outdir, "%s_bestbuffer.dat" % basename)
        self.averBuffer = os.path.join(self.outdir, "%s_averbuffer.dat" % basename)
        for idx, name in enumerate(self.buffers):
            copy(name, os.path.join(self.outdir, "%s_buf%i.dat" % (basename, idx)))
        if len(self.buffers) == 1:
            self.actualBestBuffer = self.buffers[0]
        else:
            self.__edPluginDataver.dataInput = XSDataInputDataver(inputCurve=self.dataInput.buffers,
                                                                  outputCurve=XSDataFile(XSDataString(self.averBuffer)))
            self.__edPluginDataver.connectSUCCESS(self.doSuccessExecDataver)
            self.__edPluginDataver.connectFAILURE(self.doFailureExecDataver)
            self.__edPluginDataver.execute()

            if len(self.buffers) == 2:
                edPluginDatcmp = self.loadPlugin(self.__strPluginDatcmp)
                edPluginDatcmp.dataInput = XSDataInputDatcmp(inputCurve=self.dataInput.buffers)
                edPluginDatcmp.connectSUCCESS(self.doSuccessExecDatcmp)
                edPluginDatcmp.connectFAILURE(self.doFailureExecDatcmp)
                edPluginDatcmp.executeSynchronous()
                if self.isFailure() or (self.fidelity is None):
                    return
                if self.fidelity < self.BUFFER_SIMILARITY: #buffer are not the same: keeping the one with lowest Rg/I0
                    edpluginRg = self.loadPlugin(self.__strPluginAutoRg)
                    edpluginRg.dataInput = XSDataInputAutoRg(inputCurve=self.dataInput.buffers)
                    edpluginRg.connectSUCCESS(self.doSuccessExecAutoRg)
                    edpluginRg.connectFAILURE(self.doFailureExecAutoRg)
                    edpluginRg.executeSynchronous()
                    self.actualBestBuffer = self.dictRg.keys()[self.dictRg.values().index(min(self.dictRg.values()))]
                else:
                    self.actualBestBuffer = self.averBuffer
            else:
                self.synchronizePlugins()
                strError = "You should specify exactly 2 buffers for guessing best buffer, I got: " + ", ".join(self.buffers)
                self.WARNING(strError)
                self.lstProcessLog.append(strError)
                self.actualBestBuffer = self.averBuffer

        copy(self.actualBestBuffer, self.bestBuffer)
        self.lstProcessLog.append("Best buffer is %s" % self.actualBestBuffer)
        if self.isFailure() or not os.path.exists(self.bestBuffer) or not os.path.exists(self.sampleCurve):
            return
        edPluginDatop = self.loadPlugin(self.__strPluginDatop)
        edPluginDatop.dataInput = XSDataInputDatop(operation=XSDataString("SUB"),
                               outputCurve=XSDataFile(XSDataString(self.subtractedCurve)),
                               inputCurve=[XSDataFile(XSDataString(self.sampleCurve)), XSDataFile(XSDataString(self.bestBuffer))])
        edPluginDatop.connectSUCCESS(self.doSuccessExecDatop)
        edPluginDatop.connectFAILURE(self.doFailureExecDatop)
        edPluginDatop.executeSynchronous()

        if self.isFailure() or not os.path.exists(self.subtractedCurve):
            return

        edpluginRg = self.loadPlugin(self.__strPluginAutoRg)
        edpluginRg.dataInput = XSDataInputAutoRg(inputCurve=[XSDataFile(XSDataString(self.subtractedCurve))])
        edpluginRg.connectSUCCESS(self.doSuccessExecAutoRg)
        edpluginRg.connectFAILURE(self.doFailureExecAutoRg)
        edpluginRg.executeSynchronous()




    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginAutoSubv1_0.postProcess")
        # Create some output data

        self.xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstProcessLog)))
        self.setDataOutput(self.xsDataResult)


    def doSuccessExecDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doSuccessExecDatop")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginAutoSubv1_0.doSuccessExecDatop")


    def doFailureExecDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doFailureExecDatop")
        self.retrieveFailureMessages(_edPlugin, "EDPluginAutoSubv1_0.doFailureExecDatop")
        self.lstProcessLog.append("Failure in datop (subtraction of the buffer")
        self.setFailure()

    def doSuccessExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doSuccessExecDataver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginAutoSubv1_0.doSuccessExecDataver")


    def doFailureExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doFailureExecDataver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginAutoSubv1_0.doFailureExecDataver")
        self.lstProcessLog.append("Failure in dataver (averaging of buffer")
        self.setFailure()


    def doSuccessExecAutoRg(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doSuccessExecAutoRg")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginAutoSubv1_0.doSuccessExecAutoRg")

        for data in _edPlugin.dataOutput.autoRgOut:
            self.dictRg[data.filename.path.value] = (data.rg.value, data.i0.value)

        if (len(_edPlugin.dataOutput.autoRgOut) == 1) and os.path.exists(self.subtractedCurve): #rewrite Headers
            res = _edPlugin.dataOutput.autoRgOut[0]
            lstRg = []
            if res.rg.value < 1e-6:
                lstRg.append("AutoRg: Rg   =   %.4f +/- %.2f" % (res.rg.value, res.rgStdev.value))
            else:
                lstRg.append("AutoRg: Rg   =   %.4f +/- %.2f ( %.1f%%)" % (res.rg.value, res.rgStdev.value, 100. * res.rgStdev.value / res.rg.value))
            lstRg.append("AutoRg: I(0) =   %.2f +/- %.4f" % (res.i0.value, res.i0Stdev.value))
            lstRg.append("AutoRg: Points   %i to %i ( %i total)" % (res.firstPointUsed.value, res.lastPointUsed.value , 1 + res.lastPointUsed.value - res.firstPointUsed.value))
            lstRg.append("AutoRg: Quality: %.1f%%" % (res.quality.value * 100.0))

            self.rewriteHeader(output=self.subtractedCurve,
                               infile=self.sampleCurve,
                               extraHeaders=["Buffer subtracted file",
                                             "Protein DatFile = %s" % self.sampleCurve,
                                             "Buffer DatFile = %s" % self.actualBestBuffer,
                                             ""] + lstRg,
                               scale=True)
            self.lstProcessLog += lstRg
            self.xsDataResult.autoRg = res



    def doFailureExecAutoRg(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doFailureExecAutoRg")
        self.retrieveFailureMessages(_edPlugin, "EDPluginAutoSubv1_0.doFailureExecAutoRg")
        self.lstProcessLog.append("Failure in AutoRg")
        self.setFailure()


    def doSuccessExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doSuccessExecDatcmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginAutoSubv1_0.doSuccessExecDatcmp")
        self.fidelity = _edPlugin.dataOutput.fidelity.value


    def doFailureExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginAutoSubv1_0.doFailureExecDatcmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginAutoSubv1_0.doFailureExecDatcmp")
        self.lstProcessLog.append("Failure in datcmp (comparison of 2 buffers)")
        self.setFailure()


    def rewriteHeader(self, infile=None, output=None, hdr="#", linesep=os.linesep, extraHeaders=None, scale=False):
        """
        Write the output file with merged data with the good header.
        
        
# BSA sample
#Sample c= 0.0 mg/ml
#
# Merged from: file1
# Merged from: file2
# Merged from: file4
#
# Sample Information:
# Concentration: 0.0
# Code: BSA

        @param infile: path of the original data file where original data are taken from
        @param outfile: path of the destination file
        @param hdr: header marker, often "#"
        @param linesep: line separator, usually "\n" or "\r\n" depending on the Operating System
        @param scale: if True, divide by concentration   
        @return: None
        """
        if extraHeaders is None:
            extraHeaders = []
        Code = Concentration = None
        frameMax = exposureTime = measurementTemperature = storageTemperature = None
        originalFile = infile
        headers = [line.strip() for line in open(originalFile) if line.startswith("#")]
        Comments = headers[0][1:].strip()
        for line in headers:
            if "title =" in  line:
                Comments = line.split("=", 1)[1].strip()
            elif "Comments =" in line:
                Comments = line.split("=", 1)[1].strip()
            elif "Concentration:" in line:
                Concentration = line.split(":", 1)[1].strip()
            elif "Concentration =" in line:
                Concentration = line.split("=", 1)[1].strip()
            elif "Code =" in line:
                Code = line.split("=", 1)[1].strip()
            elif "Code:" in line:
                Code = line.split(":", 1)[1].strip()
            elif "Storage Temperature" in line:
                storageTemperature = line.split(":", 1)[1].strip()
            elif "Measurement Temperature" in line:
                measurementTemperature = line.split(":", 1)[1].strip()
            elif "Time per frame" in line:
                exposureTime = line.split("=", 1)[1].strip()
#            elif "Frame" in line:
#                frameMax = line.split()[-1]
        try:
            c = float(Concentration)
        except:
            c = -1.0
        self.tKey = (Code, Comments, c)
        lstHeader = ["%s %s" % (hdr, Comments), "%s Sample c= %s mg/ml" % (hdr, Concentration), hdr]
#        if frameMax is not None:
#            lstHeader.append(hdr + " Number of frames collected: %s" % frameMax)
        if exposureTime is not None:
            lstHeader.append(hdr + " Exposure time per frame: %s" % exposureTime)

        for i in extraHeaders:
            lstHeader.append(hdr + " " + i)

        lstHeader += [hdr, hdr + " Sample Information:"]
        if storageTemperature is not None:
            lstHeader.append(hdr + " Storage Temperature (degrees C): %s" % storageTemperature)
        if measurementTemperature is not None:
            lstHeader.append(hdr + " Measurement Temperature (degrees C): %s" % measurementTemperature)
        lstHeader += [hdr + " Concentration: %s" % Concentration, "# Code: %s" % Code]
        if scale and c != 0:
            df = [i.split() for i in open(output) if not i.startswith(hdr)]
            data = linesep.join(["%14s %14.6e %14.6e" % (w[0], float(w[1]) / c, float(w[2]) / c) for w in df if len(w) >= 3])
            lstHeader.insert(2, hdr + " Scaled by concentration")
        else:
            data = linesep.join([i.strip() for i in open(output) if not i.startswith(hdr)])
        with open(output, "w") as outfile:
            outfile.write(linesep.join(lstHeader))
            if not data.startswith(linesep):
                outfile.write(linesep)
            outfile.write(data)

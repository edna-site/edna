# coding: utf8
#
#    Project: BioSaxs
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
__date__ = "20120927"
__status__ = "development"

import os, time
from EDPluginControl import EDPluginControl
from EDUtilsParallel import EDUtilsParallel
from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("XSDataBioSaxsv1_0")
edFactoryPlugin.loadModule("XSDataEdnaSaxs")

from XSDataBioSaxsv1_0 import XSDataInputBioSaxsHPLCv1_0, XSDataResultBioSaxsHPLCv1_0#, \
from XSDataEdnaSaxs import XSDataInputDataver
from XSDataCommon import XSDataString, XSDataStatus, XSDataFile
from EDPluginBioSaxsHPLCv1_0 import EDPluginBioSaxsHPLCv1_0


class EDPluginBioSaxsFlushHPLCv1_0 (EDPluginControl):
    """
    plugin that just flushes the HPLC data to disk
    """
    strControlledPluginDatAver = "EDPluginExecDataverv1_0"
    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsHPLCv1_0)
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
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.preProcess")
        sdi = self.dataInput
        if sdi.runId is not None:
            self.runId = sdi.runId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                self.runId = path[::-1].split("_", 1)[1][::-1]
            else:
                self.runId = path

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.process")
        if self.runId in EDPluginBioSaxsHPLCv1_0.dictHPLC:
            res = self.processRun(EDPluginBioSaxsHPLCv1_0.dictHPLC[self.runId])


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.postProcess")
        self.synchronizePlugins()

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        executiveSummary = os.linesep.join(self.lstExecutiveSummary)
        self.xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        self.dataOutput = self.xsDataResult

    def processRun(self, run):
        run.dump_json()
        self.xsDataResult.hplcFile = XSDataFile(XSDataString(run.save_hdf5()))
        self.xsDataResult.hplcImage = XSDataFile(XSDataString(run.make_plot()))
        for group in run.analyse():
            self.lstExecutiveSummary.append("Merging frames from %s to %s" % (group[0], group[-1]))
            xsdFrames = [XSDataFile(XSDataString(run.frames[i].subtracted)) for i in group]
            outname = os.path.splitext(run.frames[group[0]].subtracted)[0] + "_aver_%s.dat" % group[-1]
            edpugin = self.loadPlugin(self.strControlledPluginDatAver)
            edpugin.dataInput = XSDataInputDataver(outputCurve=XSDataFile(XSDataString(outname)), inputCurve=xsdFrames)
            edpugin.connectSUCCESS(self.doSuccessDatAver)
            edpugin.connectFAILURE(self.doFailureDatAver)
            edpugin.execute()


    def doSuccessDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.doSuccessDatAver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsFlushHPLCv1_0.doSuccessDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.outputCurve:
            outCurve = _edPlugin.dataOutput.outputCurve.path.value
            if os.path.exists(outCurve):
                self.xsDataResult.mergedCurves += [_edPlugin.dataOutput.outputCurve]
            else:
                strErr = "DatAver claimed merged curve is in %s but no such file !!!" % outCurve
                self.ERROR(strErr)
                self.lstExecutiveSummary.append(strErr)
                self.setFailure()


    def doFailureDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.doFailureDatAver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsFlushHPLCv1_0.doFailureDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatAver failed.")
        self.setFailure()


# coding: utf8
#
#    Project: EDNA-SAXS
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) EMBL + ESRF + DLS
#
#    Principal author:       Al, Irakli, Alun, Jerome, Olof, Peter and Claudio
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

__author__ = "Al, Irakli, Alun, Jerome, Olof, Peter and Claudio"
__license__ = "GPLv3+"
__copyright__ = "EMBL + ESRF + DLS"

import os
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataEdnaSaxs import XSDataInputAutoRg, XSDataResultAutoRg, \
        XSDataLength, XSDataBoolean, XSDataInteger, XSDataAutoRg, \
        XSDataFile, XSDataDouble, XSDataString

class EDPluginExecAutoRgv1_0(EDPluginExecProcessScript):
    """
    Execution plugin for AutoRg (part of Atsas package)
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputAutoRg)
        self.sample = None
        self.inputCurve = []
        self.minIntervalLength = None
        self.maxSmaxRg = None
        self.maxSminRg = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecProcessScriptAutoRgv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
#        self.checkMandatoryParameters(self.dataInput.sample, "No sample provided")
        self.checkMandatoryParameters(self.dataInput.inputCurve, "No input curve  provided ")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecProcessScriptAutoRgv1_0.preProcess")
        self.sample = self.dataInput.sample

        self.inputCurve = [i.path.value for i in self.dataInput.inputCurve]
        if self.dataInput.maxSmaxRg is not None:
            self.maxSmaxRg = self.dataInput.maxSmaxRg.value
        if self.dataInput.maxSminRg is not None:
            self.maxSminRg = self.dataInput.maxSminRg.value
        if self.dataInput.minIntervalLength is not None:
            self.minIntervalLength = self.dataInput.minIntervalLength.value
#autorg filename file2 file2 ... -f csv/
        self.setScriptCommandline(self.createCommandLine())


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecProcessScriptAutoRgv1_0.postProcess")
        # Create some output data
#        2.83326 0.011646 2.04258e+07 18565.3 47 81 0.783626 1 bioSaxsMerged.dat
        strOutput = self.readProcessLogFile()
        xsDataResult = XSDataResultAutoRg()
        listXSDOut = []
        for line in strOutput.split(os.linesep):
            words = line.split(None, 8)
            if len(words) < 8:
                break
            try:
                xsData = XSDataAutoRg()
                xsData.filename = XSDataFile(XSDataString(words[-1]))
                xsData.rg = XSDataLength(float(words[0]))
                xsData.rgStdev = XSDataLength(float(words[1]))
                xsData.i0 = XSDataDouble(float(words[2]))
                xsData.i0Stdev = XSDataDouble(float(words[3]))
                xsData.firstPointUsed = XSDataInteger(int(words[4]))
                xsData.lastPointUsed = XSDataInteger(int(words[5]))
                xsData.quality = XSDataDouble(float(words[6]))
                xsData.isagregated = XSDataBoolean(bool(int(words[7])))
            except Exception:
                strError = "Error in parsing output:" + line
                self.error(strError)
                self.setFailure()
            listXSDOut.append(xsData)
        xsDataResult.autoRgOut = listXSDOut
        self.setDataOutput(xsDataResult)


    def createCommandLine(self):
        """actually creater the command line and retruns it"""
        lstCommandLine = self.inputCurve
        if self.maxSmaxRg is not None:
            lstCommandLine.append("--smaxrg %s" % self.maxSmaxRg)
        if self.maxSminRg is not None:
            lstCommandLine.append("--sminrg %s" % self.maxSminRg)
        if self.minIntervalLength is not None:
            lstCommandLine.append("--mininterval %s" % self.minIntervalLength)
        lstCommandLine.append("--format ssv")
        return " ".join(lstCommandLine)

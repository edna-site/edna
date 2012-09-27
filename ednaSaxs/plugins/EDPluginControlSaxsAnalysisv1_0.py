# coding: utf8
#
#    Project: Edna Saxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 ESRF
#
#    Principal author: Jerome Kieffer        
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

__authors__ = ["Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "2012-09-17"
__status__ = "Development"

import os
from EDPluginControl import EDPluginControl
from XSDataEdnaSaxs import XSDataInputSaxsAnalysis, XSDataResultSaxsAnalysis, \
                           XSDataInputAutoRg, XSDataInputDatGnom, XSDataInputDatPorod
from XSDataCommon import XSDataString, XSDataLength, XSDataFile, XSDataInteger, XSDataStatus



class EDPluginControlSaxsAnalysisv1_0(EDPluginControl):
    """
    Executes the pipeline:
    * AutoRg -> Extract the Guinier region and measure Rg, I0
    * DatGnom -> transformation from reciprocal to direct space. measure Dmax.
    * DatPorod -> calculates the volume of the protein using the porod formula.
    """
    cpAutoRg = "EDPluginExecAutoRgv1_0"
    cpDatGnom = "EDPluginExecDatGnomv1_0"
    cpDatPorod = "EDPluginExecDatPorodv1_0"

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsAnalysis)
        self.edPluginAutoRg = None
        self.edPluginDatPorod = None
        self.edPluginDatGnom = None
        self.scatterFile = None
        self.gnomFile = None
        self.autoRg = None
        self.gnom = None
        self.xVolume = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.scatterCurve, "No scattering curve provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.preProcess")
        self.scatterFile = self.dataInput.scatterCurve.path.value
        if self.dataInput.gnomFile is not None:
            self.gnomFile = self.dataInput.gnomFile.path.value
        else:
            self.gnomFile = os.path.join(self.getWorkingDirectory(), os.path.basename(self.scatterFile).split(".")[0] + ".out")
        self.autoRg = self.dataInput.autoRg


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.process")
        if self.autoRg is None:
            self.edPluginAutoRg = self.loadPlugin(self.cpAutoRg)
            self.edPluginAutoRg.dataInput = XSDataInputAutoRg(inputCurve=[self.dataInput.scatterCurve])
            self.edPluginAutoRg.connectSUCCESS(self.doSuccessRg)
            self.edPluginAutoRg.connectFAILURE(self.doFailureRg)
            self.edPluginAutoRg.executeSynchronous()

        if self.isFailure():
            return

        self.edPluginDatGnom = self.loadPlugin(self.cpDatGnom)
        self.edPluginDatGnom.dataInput = XSDataInputDatGnom(inputCurve=self.dataInput.scatterCurve,
                                             output=XSDataFile(XSDataString(self.gnomFile)),
                                             rg=self.autoRg.rg,
                                            skip=XSDataInteger(self.autoRg.firstPointUsed.value - 1))
        self.edPluginDatGnom.connectSUCCESS(self.doSuccessGnom)
        self.edPluginDatGnom.connectFAILURE(self.doFailureGnom)
        self.edPluginDatGnom.executeSynchronous()

        if self.gnom is None:
            return

        self.edPluginDatPorod = self.loadPlugin(self.cpDatPorod)
        self.edPluginDatPorod.dataInput = XSDataInputDatPorod(gnomFile=XSDataFile(XSDataString(self.gnomFile)))
        self.edPluginDatPorod.connectSUCCESS(self.doSuccessPorod)
        self.edPluginDatPorod.connectFAILURE(self.doFailurePorod)
        self.edPluginDatPorod.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.postProcess")
        # Create some output data
        strLog = """Rg   =   %f +/- %f 
I(0) =   %e +/- %e
Points   %i to %i 
Quality: %4.2f%%     Aggregated: %s"""%(self.autoRg.rg.value, self.autoRg.rgStdev.value,
                        self.autoRg.i0.value, self.autoRg.i0Stdev.value,
                        self.autoRg.firstPointUsed.value, self.autoRg.lastPointUsed.value,
                        self.autoRg.quality.value * 100., self.autoRg.isagregated.value)
        if self.gnom is None:
            strLog += """
datGnom failed"""
        else:
            strLog += """
Dmax    =    %12f       Total =   %12f     
Guinier =    %12f       Gnom =    %12f"""%(self.gnom.dmax.value, self.gnom.total.value,
                        self.gnom.rgGuinier.value, self.gnom.rgGnom.value)
        if self.xVolume is None:
            strLog += """
datPorod failed"""
        else:
            strLog += """
Volume  =    %12f""" % (self.xVolume.value)

        xsDataResult = XSDataResultSaxsAnalysis(autoRg=self.autoRg,
                                                gnom=self.gnom,
                                                volume=self.xVolume,
                                                status=XSDataStatus(executiveSummary=XSDataString(strLog)))
        self.setDataOutput(xsDataResult)


    def doSuccessRg(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doSuccessRg")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doSuccessRg")
        self.autoRg = _edPlugin.dataOutput.autoRgOut[0]

    def doFailureRg(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doFailureRg")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doFailureRg")
        self.setFailure()

    def doSuccessGnom(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doSuccessGnom")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doSuccessGnom")
        self.gnom = _edPlugin.dataOutput.gnom
        self.gnomFile = self.gnom.gnomFile.path.value

    def doFailureGnom(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doFailureGnom")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doFailureGnom")
        #self.setFailure()

    def doSuccessPorod(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doSuccessPorod")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doSuccessPorod")
        self.xVolume = _edPlugin.dataOutput.volume

    def doFailurePorod(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSaxsAnalysisv1_0.doFailurePorod")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSaxsAnalysisv1_0.doFailurePorod")
        #self.setFailure()

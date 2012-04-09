# coding: utf8
#
#    Project: Solution Scattring pipeline
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:        irakli
#                            Jérôme Kieffer (jerome.Kieffer@esrf.fr)
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

__authors__ = ["irakli", "Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "2011 DLS, 2012 ESRF"
__date__ = "20120214"

import os, operator, itertools, matplotlib, distutils.dir_util
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter
import numpy
from numpy import mean, std, var, arange, resize

from EDVerbose import EDVerbose
from EDSlot import EDSlot
from EDPluginControl import EDPluginControl
from EDActionCluster import EDActionCluster
from EDUtilsFile import EDUtilsFile
from EDConfiguration import EDConfiguration
from EDParallelJobLauncher import EDParallelJobLauncher
from EDUtilsArray import EDUtilsArray
from EDPDBFilter import EDPDBFilter

from XSDataSAS import XSDataInputSolutionScattering, XSDataResultSolutionScattering, XSDataInputGnom, \
                    XSDataInputDammif, XSDataInputSupcomb, XSDataInputDamaver, XSDataInputDamfilt, \
                    XSDataInputDamstart
from XSDataCommon import XSDataDouble, XSDataInteger, XSDataString, XSDataBoolean


def try_float(tmpStr):
    """
    Check in the input string can be converted into float
    """
    try:
        float(tmpStr)
        return True
    except ValueError:
        return False

def rejectDataLine(_tmpLine, _numColumns):
    """
    Check if input string is not list of floats
    """
    _tmpData = _tmpLine.split()
    if  (len(_tmpData) < _numColumns) or (False in [try_float(tmp) for tmp in _tmpData]):
        return True
    else:
        return False

class EDPluginControlSolutionScatteringv0_4(EDPluginControl):
    """
    Solution scattering control plugin for running GNOM->DAMMIF->DAMAVER pipeline
    Step 1: Running GNOM jobs in parallel to idenfity the optimal value for rMax input parameter
    Step 2: Running DAMMIF jobs in parallel to build series of ab-initio models
    Step 3: Run DAMAVER pipeline to calculate an averaged model 
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputSolutionScattering)

        self.__strPluginExecGnom = "EDPluginExecGnomv0_2"
        self.__strPluginExecDammif = "EDPluginExecDammifv0_1"
        self.__strPluginExecSupcomb = "EDPluginExecSupcombv0_1"
        self.__strPluginExecDamaver = "EDPluginExecDamaverv0_1"
        self.__strPluginExecDamfilt = "EDPluginExecDamfiltv0_1"
        self.__strPluginExecDamstart = "EDPluginExecDamstartv0_1"

        self.__pluginConfiguration = None
        self.__strPathToJMol = None
        self.__bUseJMol = None

        self.__xsGnomJobs = None
        self.__xsDammifJobs = None
        self.__xsSupcombJobs = None

        self.__edPluginExecGnom = None
        self.__edPluginExecDammif = None
        self.__edPluginExecDamaver = None
        self.__edPluginExecDamfilt = None
        self.__edPluginExecDamstart = None

        self.__inputType = None
        self.npaExperimentalDataQ = None
        self.npaExperimentalDataI = None
        self.npaExperimentalDataStdDev = None
        self.strExperimentalDataFile = None

        self.__xsDataRMax = None
        self.__xsDataOutput = None

        self.__iNbThreads = None
        self.__iUnit = 1
        self.__strUnit = "ANGSTROM"
        self.__strMode = "Fast"
        self.__strSymmetry = "P1"
        self.__bOnlyGnom = False
        self.__bPlotFit = False

        self.__rMaxStart = 10.0
        self.__rMaxStop = 200.0
        self.__absTol = 1.0
        self.__absErr = self.__absTol * 10
        self.__rMaxDivide = 10

        self.__iNbGnomSeries = None
        self.__iNbDammifJobs = 10

        self.__idxDammifBestNSD = None
        self.__idxDammifBestChiSq = None
        self.__meanNSD = None
        self.__varNSD = None
        self.__dammifRefNSD = {}

        self.__cmDammif = matplotlib.cm.get_cmap('spectral')
        self.__colorsDammif = [self.__cmDammif(1.0 * (ref + 1) / self.__iNbDammifJobs) for ref in range(self.__iNbDammifJobs)]
        self.__colorsDammifRGB = [''.join(['[x', matplotlib.colors.rgb2hex(colorConverter.to_rgb(clr))[1:].upper(), ']']) for clr in self.__colorsDammif]

        self.__xsGnomPlugin = {}
        self.__xsDammifPlugin = {}
        self.__xsSupcombPlugin = {}

        self.__xsDataResultSolutionScattering = XSDataResultSolutionScattering()

        self.__tmpActionCluster = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

        self.checkRMaxSearchParameters()
        self.checkModeParameter()
        self.checkUnitParameter()
        self.checkJMol()

    def checkRMaxSearchParameters(self):
        if self.dataInput.rMaxSearchSettings is not None:
            if self.dataInput.rMaxSearchSettings.rMaxStart is None:
                self.ERROR("EDPluginControlSolutionScatteringv0_4.setRMaxSerachParameters rMaxStart is missing")
                self.setFailure()
            else:
                if self.dataInput.rMaxSearchSettings.rMaxStart.value < self.__rMaxStart:
                    self.WARNING("EDPluginControlSolutionScatteringv0_4.setRMaxSerachParameters rMaxStart is too small. Resetting to the default.")
            if self.dataInput.rMaxSearchSettings.rMaxStop is None:
                self.ERROR("EDPluginControlSolutionScatteringv0_4.setRMaxSerachParameters rMaxStop is missing")
                self.setFailure()
            if self.dataInput.rMaxSearchSettings.getRMaxAbsTol() is None:
                self.ERROR("EDPluginControlSolutionScatteringv0_4.setRMaxSerachParameters rMaxAbsTol is missing")
                self.setFailure()
            if self.dataInput.rMaxSearchSettings.getRMaxIntervals() is None:
                self.ERROR("EDPluginControlSolutionScatteringv0_4.setRMaxSerachParameters rMaxIntervals is missing")
                self.setFailure()

    def checkModeParameter(self):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.checkModeParameter")
        try:
            if self.dataInput.mode.value.lower() in ['fast', 'slow']:
                self.__strMode = self.dataInput.mode.value.lower()
        except:
            self.WARNING("Running Solution Scattering pipeline in fast mode by default")

    def checkUnitParameter(self):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.checkUnitParameter")
        try:
            if self.dataInput.angularUnits.value in [1, 2, 3, 4]:
                self.__iUnit = self.dataInput.angularUnits.value
                if self.__iUnit in [1, 3]:
                    self.__strUnit = "ANGSTROM"
                else:
                    self.__strUnit = "NANOMETER"
        except:
            self.WARNING("Using Angstrom units for q-values by default")

    def checkJMol(self):
        self.__pluginConfiguration = self.getConfiguration()
        self.__strPathToJMol = EDConfiguration.getStringParamValue(self.__pluginConfiguration, 'jMol')
        if os.path.isdir(self.__strPathToJMol):
            distutils.dir_util.copy_tree(self.__strPathToJMol, os.path.join(self.getWorkingDirectory(), "jmol"))
            self.__bUseJMol = True


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.preProcess")

        xsDataInputSolutionScattering = self.dataInput
        if xsDataInputSolutionScattering.experimentalDataQ:
            self.npaExperimentalDataQ = numpy.array([i.value for i in xsDataInputSolutionScattering.experimentalDataQ], dtype="float32")
        elif xsDataInputSolutionScattering.experimentalDataQArray:
            self.npaExperimentalDataQ = EDUtilsArray.xsDataToArray(xsDataInputSolutionScattering.experimentalDataQArray).astype("float32")
        elif xsDataInputSolutionScattering.experimentalDataFile:
            self.strExperimentalDataFile = xsDataInputSolutionScattering.experimentalDataFile.path.value
        else:
            strError = "Missing mandatory parameter: experimentalDataQ or experimentalDataQArray or experimentalDataFile"
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError, strError

        if xsDataInputSolutionScattering.experimentalDataValues:
            self.npaExperimentalDataI = numpy.array([i.value for i in xsDataInputSolutionScattering.experimentalDataValues], dtype="float32")
        elif xsDataInputSolutionScattering.experimentalDataIArray:
            self.npaExperimentalDataI = EDUtilsArray.xsDataToArray(xsDataInputSolutionScattering.experimentalDataIArray).astype("float32")
        elif self.strExperimentalDataFile is None:
            strError = "Missing mandatory parameter: experimentalDataValues or experimentalDataValues or experimentalDataFile"
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError, strError

        if xsDataInputSolutionScattering.experimentalDataStdDev:
            self.npaExperimentalDataStdDev = numpy.array([i.value for i in xsDataInputSolutionScattering.experimentalDataStdDev], dtype="float32")
        elif xsDataInputSolutionScattering.experimentalDataStdArray:
            self.npaExperimentalDataStdDev = EDUtilsArray.xsDataToArray(xsDataInputSolutionScattering.experimentalDataStdArray).astype("float32")

        qMin = qMax = None
        if xsDataInputSolutionScattering.qMin:
            qMin = xsDataInputSolutionScattering.qMin.value
        if xsDataInputSolutionScattering.qMax:
            qMax = xsDataInputSolutionScattering.qMax.value

        if self.strExperimentalDataFile is not None:
            self.readGnomDataColumns(self.strExperimentalDataFile, _fQMin=qMin, _fQMax=qMax)
        else:
            self.cropInputData(qMin, qMax)

        if self.dataInput.symmetry is not None:
            self.__strSymmetry = self.dataInput.symmetry.value

        if self.dataInput.rMaxSearchSettings is not None:
            self.__rMaxStart = max(self.__rMaxStart, self.dataInput.rMaxSearchSettings.rMaxStart.value)
            self.__rMaxStop = self.dataInput.rMaxSearchSettings.rMaxStop.value
            self.__absTol = self.dataInput.rMaxSearchSettings.getRMaxAbsTol().value
            self.__absErr = self.__absTol * 10
            self.__rMaxDivide = self.dataInput.rMaxSearchSettings.getRMaxIntervals().value

        if self.dataInput.getINbThreads() is not None:
            self.__iNbThreads = self.dataInput.getINbThreads().value

        if self.dataInput.getOnlyGnom() is not None:
            self.__bOnlyGnom = self.dataInput.getOnlyGnom().value
        if self.dataInput.getPlotFit() is not None:
            self.__bPlotFit = self.dataInput.getPlotFit().value

    def __checkGnomSeriesResults(self, serInput):
        fitResultDict = dict([((ser, idx), plg.dataOutput.getFitQuality().value) for (ser, idx), plg in self.__xsGnomPlugin.items() if ser == serInput])
        fitResultList = sorted(fitResultDict.iteritems(), key=operator.itemgetter(1), reverse=True)
        ((ser, idx_max), _) = fitResultList[0]

        # Find rMax values bracketing the best rMax result
        self.__rMaxStart = self.__xsGnomPlugin[(ser, max(idx_max - 1, 0))].dataInput.rMax.value
        self.__rMaxStop = self.__xsGnomPlugin[(ser, min(idx_max + 1, len(fitResultList) - 1))].dataInput.rMax.value
        self.__absErr = (fitResultList[0][1] - fitResultList[-1][1])
        return self.__xsGnomPlugin[(ser, idx_max)]


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.process")

        #Make series of GNOM runs narrowing down the optimal value of rMax
        ser = 0
        while self.__absErr > self.__absTol:

            if (not self.__rMaxDivide):
                xsDataRMax = [XSDataDouble(self.__rMaxStart)]
            else:
                xsDataRMax = itertools.imap(lambda idx: XSDataDouble(self.__rMaxStart + idx * (self.__rMaxStop - self.__rMaxStart) / self.__rMaxDivide), range(self.__rMaxDivide + 1))


            dictDataInputGnom = {}
            for idx, rMax in enumerate(xsDataRMax):
                dictDataInputGnom[(ser, idx)] = XSDataInputGnom(experimentalDataQArray=EDUtilsArray.arrayToXSData(self.npaExperimentalDataQ),
                                                                experimentalDataIArray=EDUtilsArray.arrayToXSData(self.npaExperimentalDataI))
                if self.npaExperimentalDataStdDev is not None:
                    dictDataInputGnom[(ser, idx)].experimentalDataStdArray = EDUtilsArray.arrayToXSData(self.npaExperimentalDataStdDev)
                dictDataInputGnom[(ser, idx)].setRMax(rMax)
                dictDataInputGnom[(ser, idx)].setAngularScale(XSDataInteger(self.__iUnit))
                dictDataInputGnom[(ser, idx)].setMode(XSDataString(self.__strMode))
            self.__xsGnomJobs = EDParallelJobLauncher(self, self.__strPluginExecGnom, dictDataInputGnom, self.__iNbThreads)
            ##self.__xsGnomJobs.connectFAILURE(self.doFailureExecGnomActionCluster)
            self.executePluginSynchronous(self.__xsGnomJobs)

            if self.__xsGnomJobs.isFailure():
                self.doFailureExecGnomActionCluster()
                return
            else :
                self.__xsGnomPlugin.update(self.__xsGnomJobs.getPluginJobs())
                edPluginGnomOptimal = self.__checkGnomSeriesResults(ser)
                ser += 1

        self.__iNbGnomSeries = ser

        # Just rerunning GNOM with optimal parameters to fir it into Control plugin pipeline.
        self.__edPluginExecGnom = self.loadPlugin(self.__strPluginExecGnom, self.__strPluginExecGnom + '-optimal')
        self.__edPluginExecGnom.setDataInput(edPluginGnomOptimal.dataInput)
        self.__edPluginExecGnom.connectSUCCESS(self.doSuccessExecGnom)
        self.__edPluginExecGnom.connectFAILURE(self.doFailureExecGnom)
        self.executePluginSynchronous(self.__edPluginExecGnom)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.postProcess")
        self.setDataOutput(self.__xsDataResultSolutionScattering)

    def doSuccessExecGnom(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecGnom")
        self.retrieveSuccessMessages(self.__edPluginExecGnom, "EDPluginControlSolutionScatteringv0_4.doSuccessExecGnom")

        if not self.__bOnlyGnom:
            self.__xsDataOutput = self.__edPluginExecGnom.dataOutput.getOutput()

            xsDataInputDammif = XSDataInputDammif(gnomOutputFile=self.__xsDataOutput,
                                                  unit=XSDataString(self.__strUnit),
                                                  symmetry=XSDataString(self.__strSymmetry),
                                                  mode=XSDataString(self.__strMode))
            dictDataInputDammif = {}
            for idx in range(self.__iNbDammifJobs):
                dictDataInputDammif[idx] = xsDataInputDammif

            self.__xsDammifJobs = EDParallelJobLauncher(self, self.__strPluginExecDammif, dictDataInputDammif, self.__iNbThreads)
            self.__xsDammifJobs.connectSUCCESS(self.doSuccessExecDammif)
            self.__xsDammifJobs.connectFAILURE(self.doFailureExecDammif)
            self.executePluginSynchronous(self.__xsDammifJobs)


    def doFailureExecGnomActionCluster(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecGnom")
        self.retrieveFailureMessages(self.__xsGnomJobs, "EDPluginControlSolutionScatteringv0_4.doFailureExecGnom")


    def doFailureExecGnom(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecGnom")
        self.retrieveFailureMessages(self, "EDPluginControlSolutionScatteringv0_4.doFailureExecGnom")


    def __checkDammifSeriesResults(self):
        """
        Find DAMMIF run with best chi-square value
        """
        fitResultDict = dict([(idx, plg.dataOutput.getChiSqrt().value) for idx, plg in self.__xsDammifPlugin.items()])
        fitResultList = sorted(fitResultDict.iteritems(), key=operator.itemgetter(1))
        (idx_max, _) = fitResultList[0]
        self.__idxDammifBestChiSq = idx_max

        return self.__xsDammifPlugin[idx_max]

    def doSuccessExecDammif(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecDammif")
        self.retrieveSuccessMessages(self.__xsDammifJobs, "EDPluginControlSolutionScatteringv0_4.doSuccessExecDammif")

        self.__xsDammifPlugin.update(self.__xsDammifJobs.getPluginJobs())

        self.__xsDataResultSolutionScattering.lineProfileFitQuality = self.__edPluginExecGnom.dataOutput.getFitQuality()
        self.__xsDataResultSolutionScattering.scatteringFitQ = self.__edPluginExecGnom.dataOutput.scatteringFitQ
        self.__xsDataResultSolutionScattering.scatteringFitValues = self.__edPluginExecGnom.dataOutput.scatteringFitValues
        self.__xsDataResultSolutionScattering.scatteringFitQArray = self.__edPluginExecGnom.dataOutput.scatteringFitQArray
        self.__xsDataResultSolutionScattering.scatteringFitIArray = self.__edPluginExecGnom.dataOutput.scatteringFitIArray

        self.__edPluginExecDammif = self.__checkDammifSeriesResults()
        self.__plotRMaxSearchResults()


        self.__xsDataResultSolutionScattering.setFitFile(self.__edPluginExecDammif.dataOutput.getFitFile())
        self.__xsDataResultSolutionScattering.setLogFile(self.__edPluginExecDammif.dataOutput.getLogFile())
        self.__xsDataResultSolutionScattering.setPdbMoleculeFile(self.__edPluginExecDammif.dataOutput.getPdbMoleculeFile())
        self.__xsDataResultSolutionScattering.setPdbSolventFile(self.__edPluginExecDammif.dataOutput.getPdbSolventFile())

        dictDataInputSupcomb = {}
        for idx in self.__xsDammifPlugin.iterkeys():
            for ser in range(idx):
                dictDataInputSupcomb[(ser, idx)] = XSDataInputSupcomb()
                dictDataInputSupcomb[(ser, idx)].setTemplateFile(self.__xsDammifPlugin[idx].dataOutput.getPdbMoleculeFile())
                dictDataInputSupcomb[(ser, idx)].setSuperimposeFile(self.__xsDammifPlugin[ser].dataOutput.getPdbMoleculeFile())
        self.__xsSupcombJobs = EDParallelJobLauncher(self, self.__strPluginExecSupcomb, dictDataInputSupcomb, self.__iNbThreads)
        self.__xsSupcombJobs.connectSUCCESS(self.doSuccessExecSupcomb)
        self.__xsSupcombJobs.connectFAILURE(self.doFailureExecSupcomb)
        self.executePluginSynchronous(self.__xsSupcombJobs)


    def doFailureExecDammif(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecDammif")
        self.retrieveFailureMessages(self.__xsDammifJobs, "EDPluginControlSolutionScatteringv0_4.doFailureExecDammif")


    def doSuccessExecSupcomb(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecSupcomb")
        self.retrieveSuccessMessages(self.__xsSupcombJobs, "EDPluginControlSolutionScatteringv0_4.doSuccessExecSupcomb")

        self.__xsSupcombPlugin.update(self.__xsSupcombJobs.getPluginJobs())

        self.__idxDammifBestNSD = self.__selectBestNSDModel()

        dictDataInputSupcombBest = {}
        for ser in range(self.__idxDammifBestNSD + 1, self.__iNbDammifJobs):
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)] = XSDataInputSupcomb()
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)].setTemplateFile(self.__xsDammifPlugin[self.__idxDammifBestNSD].dataOutput.getPdbMoleculeFile())
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)].setSuperimposeFile(self.__xsDammifPlugin[ser].dataOutput.getPdbMoleculeFile())
        self.__xsSupcombJobsBest = EDParallelJobLauncher(self, self.__strPluginExecSupcomb, dictDataInputSupcombBest, self.__iNbThreads)
        self.__xsSupcombJobsBest.connectSUCCESS(self.doSuccessExecSupcombAlign)
        self.__xsSupcombJobsBest.connectFAILURE(self.doFailureExecSupcombAlign)
        self.executePluginSynchronous(self.__xsSupcombJobsBest)


    def doFailureExecSupcomb(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecSupcomb")
        self.retrieveFailureMessages(self.__xsSupcombJobs, "EDPluginControlSolutionScatteringv0_4.doFailureExecSupcomb")


    def doSuccessExecSupcombAlign(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecSupcombAlign")
        self.retrieveSuccessMessages(self.__xsSupcombJobsBest, "EDPluginControlSolutionScatteringv0_4.doSuccessExecSupcombAlign")

        self.__xsSupcombPlugin.update(self.__xsSupcombJobsBest.getPluginJobs())
        self.__plotNSDResults()

        xsDataInputDamaver = XSDataInputDamaver()
        tmpOutputPdbFiles = [self.__xsDammifPlugin[self.__idxDammifBestNSD].dataOutput.getPdbMoleculeFile()]

        for (idx, tmpXSDammifPlugin) in self.__xsDammifPlugin.iteritems():
            if idx is not self.__idxDammifBestNSD:
                if abs(self.__dammifRefNSD[idx] - self.__meanNSD) < 2 * self.__varNSD:
                    tmpOutputPdbFiles.append(self.__xsSupcombPlugin[(idx, self.__idxDammifBestNSD)].dataOutput.getOutputFilename())

        xsDataInputDamaver.setPdbInputFiles(tmpOutputPdbFiles)
        xsDataInputDamaver.setAutomatic(XSDataBoolean(False))

        self.__edPluginExecDamaver = self.loadPlugin(self.__strPluginExecDamaver)
        self.__edPluginExecDamaver.setDataInput(xsDataInputDamaver)
        self.__edPluginExecDamaver.connectSUCCESS(self.doSuccessExecDamaver)
        self.__edPluginExecDamaver.connectFAILURE(self.doFailureExecDamaver)
        self.executePluginSynchronous(self.__edPluginExecDamaver)


    def doFailureExecSupcombAlign(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecSupcombAlign")
        self.retrieveFailureMessages(self.__xsSupcombJobsBest, "EDPluginControlSolutionScatteringv0_4.doFailureExecSupcombAlign")


    def doSuccessExecDamaver(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecDamaver")
        self.retrieveSuccessMessages(self.__edPluginExecDamaver, "EDPluginControlSolutionScatteringv0_4.doSuccessExecDamaver")

        xsDataInputDamfilt = XSDataInputDamfilt()
        xsDataInputDamfilt.setInputPdbFile(self.__edPluginExecDamaver.dataOutput.getDamaverPdbFile())

        self.__edPluginExecDamfilt = self.loadPlugin(self.__strPluginExecDamfilt)
        self.__edPluginExecDamfilt.setDataInput(xsDataInputDamfilt)
        self.__edPluginExecDamfilt.connectSUCCESS(self.doSuccessExecDamfilt)
        self.__edPluginExecDamfilt.connectFAILURE(self.doFailureExecDamfilt)
        self.executePluginSynchronous(self.__edPluginExecDamfilt)


    def doFailureExecDamaver(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecDamaver")
        self.retrieveFailureMessages(self.__edPluginExecDamaver, "EDPluginControlSolutionScatteringv0_4.doFailureExecDamaver")


    def doSuccessExecDamfilt(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecDamfilt")
        self.retrieveSuccessMessages(self.__edPluginExecDamfilt, "EDPluginControlSolutionScatteringv0_4.doSuccessExecDamfilt")

        xsDataInputDamstart = XSDataInputDamstart()
        xsDataInputDamstart.setInputPdbFile(self.__edPluginExecDamaver.dataOutput.getDamaverPdbFile())

        self.__edPluginExecDamstart = self.loadPlugin(self.__strPluginExecDamstart)
        self.__edPluginExecDamstart.setDataInput(xsDataInputDamstart)
        self.__edPluginExecDamstart.connectSUCCESS(self.doSuccessExecDamstart)
        self.__edPluginExecDamstart.connectFAILURE(self.doFailureExecDamstart)
        self.executePluginSynchronous(self.__edPluginExecDamstart)


    def doFailureExecDamfilt(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecDamfilt")
        self.retrieveFailureMessages(self.__edPluginExecDamfilt, "EDPluginControlSolutionScatteringv0_4.doFailureExecDamfilt")


    def doSuccessExecDamstart(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doSuccessExecDamstart")
        self.retrieveSuccessMessages(self.__edPluginExecDamstart, "EDPluginControlSolutionScatteringv0_4.doSuccessExecDamstart")




    def doFailureExecDamstart(self, _edPlugin=None):
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.doFailureExecDamstart")
        self.retrieveFailureMessages(self.__edPluginExecDamstart, "EDPluginControlSolutionScatteringv0_4.doFailureExecDamstart")


    def __selectBestNSDModel(self):
        for ref in self.__xsDammifPlugin.iterkeys():
            self.__dammifRefNSD[ref] = mean([self.__xsSupcombPlugin[(min([tmp, ref]), max([tmp, ref]))].dataOutput.getNSD().value \
                           for tmp in self.__xsDammifPlugin.iterkeys() if tmp is not ref])

        self.__meanNSD = mean(self.__dammifRefNSD.values())
        self.__varNSD = std(self.__dammifRefNSD.values())
        self.__xsDataResultSolutionScattering.setMeanNSD(XSDataDouble(self.__meanNSD))
        self.__xsDataResultSolutionScattering.setVariationNSD(XSDataDouble(self.__varNSD))

        resultsNSD = sorted(self.__dammifRefNSD.iteritems(), key=operator.itemgetter(1))

        return resultsNSD[0][0]


    def readGnomNexusDataColumns(self, _fileName, _strNxsQ, _strNxsData, _iNbColumns, _fQMin, _fQMax):
        """
        Initialize pipeline input data structure using Nexus/HDF5 data file.
        """
        tmpExperimentalDataQ = []
        tmpExperimentalDataValues = []
        tmpExperimentalDataStdDev = []

        import h5py
        tmpFile = h5py.File(_fileName, 'r')

        nxsExperimentalQ = tmpFile[_strNxsQ]
        nxsExperimentalValues = tmpFile[_strNxsData]
        nxsShape = nxsExperimentalValues.shape
        if len(nxsShape) > 1:
            _iNbColumns = min(_iNbColumns, nxsShape[-2])
        else:
            _iNbColumns = 1

        nxsExperimentalValues = resize(nxsExperimentalValues, (_iNbColumns, len(nxsExperimentalQ)))

        for (idx, _tmpQ) in enumerate(nxsExperimentalQ[:]):
            if (((_tmpQ > _fQMin) or (_fQMin is None)) and \
                ((_tmpQ < _fQMax) or (_fQMax is None))):

                units = 1
                if self.dataInput.angularUnits is not None:
                    units = self.dataInput.angularUnits.value
                if units in [2, 4]:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ / 10.0))
                else:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ))

                _tmpValue = mean(nxsExperimentalValues[:_iNbColumns, idx])
                tmpExperimentalDataValues.append(XSDataDouble(_tmpValue))
                if (_iNbColumns > 1):
                    _tmpStdDev = std(nxsExperimentalValues[:_iNbColumns, idx])
                    tmpExperimentalDataStdDev.append(XSDataDouble(_tmpStdDev))

        self.dataInput.setExperimentalDataQ(tmpExperimentalDataQ)
        self.dataInput.setExperimentalDataValues(tmpExperimentalDataValues)
        if (_iNbColumns > 1):
            self.dataInput.setExperimentalDataStdDev(tmpExperimentalDataStdDev)


    def readGnomDataColumns(self, fileName, _iNbColumns=1, _fQMin=None, _fQMax=None):
        """
        Initialize pipeline input data structure using ASCII data file.
        Lines with text fields are ignored.
        For every row up to _iNbColums of data will be read.
        """
        if fileName:
            data = None
            if not os.path.isfile(fileName):
                strErrorMessage = "EDPluginControlSolutionScatteringv0_4: experimentalDataFile: %s does not exist" % fileName
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            for i in range(5):
                try:
                    data = numpy.loadtxt(fileName, skiprows=i, dtype="float32")
                except:
                    pass
                else:
                    break
            if data is None:
                strErrorMessage = "EDPluginControlSolutionScatteringv0_4: Unable to parse %s with numpy.loadtxt" % fileName
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            elif (_iNbColumns > 1) and (data.shape[1] > _iNbColumns):
                self.npaExperimentalDataQ = data[:, 0]
                I = data[:, 1:1 + _iNbColumns]
                self.npaExperimentalDataI = I.mean(dtype="float32", axis=1)
                self.npaExperimentalDataStdDev = I.std(dtype="float32", axis=1)
            elif data.shape[1] == 3:
                self.npaExperimentalDataQ, self.npaExperimentalDataI, self.npaExperimentalDataStdDev = data.T
            elif data.shape[1] == 2:
                self.npaQexp, self.npaIexp = data.T
            else:
                strErrorMessage = "EDPluginControlSolutionScatteringv0_4: %s contains an numpy object of shape %s" % (fileName, data.shape)
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            self.cropInputData(_fQMin, _fQMax)

    def cropInputData(self, _fQMin=None, _fQMax=None):
        """
        Retain only the data between qMin and qMax 
        """
        if _fQMin or _fQMax:
            mask = numpy.ones_like(self.npaExperimentalDataQ)
            if _fQMin:
                mask = (self.npaExperimentalDataQ >= _fQMin)
            if _fQMax:
                mask *= (self.npaExperimentalDataQ <= _fQMax)
            self.npaExperimentalDataQ = self.npaExperimentalDataQ[mask]
            self.npaExperimentalDataI = self.npaExperimentalDataI[mask]
            if self.npaExperimentalDataStdDev:
                self.npaExperimentalDataStdDev = self.npaExperimentalDataStdDev[mask]


    def __outputGnomSeriesResults(self):
        self.addExecutiveSummaryLine("Number of GNOM iterations performed before converging : " + str(self.__iNbGnomSeries))
        for itr in range(self.__iNbGnomSeries):
            self.addExecutiveSummarySeparator()
            self.addExecutiveSummaryLine("Iteration # " + str(itr + 1))
            for idx in range(self.__rMaxDivide):
                dirLocation = self.__xsGnomPlugin[(itr, idx)].getWorkingDirectory()
                tmpRMaxInput = "rMax = %3.2f" % self.__xsGnomPlugin[(itr, idx)].dataInput.rMax.value
                tmpFitQuality = "fitQuality = " + str(self.__xsGnomPlugin[(itr, idx)].dataOutput.getFitQuality().value)
                tmpStrLine = "\t".join([tmpRMaxInput, tmpFitQuality, dirLocation])
                self.addExecutiveSummaryLine(tmpStrLine)
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Optimized value of RMax = %3.2f" % self.__edPluginExecGnom.dataInput.rMax.value)
        self.appendExecutiveSummary(self.__edPluginExecGnom)


    def __parceDammifFit(self, _tmpExpQ, _tmpExpValues, _tmpFitQ, _tmpFitValues):
        logFile = EDUtilsFile.readFile(os.path.join(self.__edPluginExecDammif.getWorkingDirectory(), "dammif.fir"))
        logLines = logFile.splitlines()
        for line in logLines:
            if not rejectDataLine(line, 4):
                dataLine = line.split()
                _tmpExpQ.append(float(dataLine[0]))
                _tmpFitQ.append(float(dataLine[0]))
                _tmpExpValues.append(float(dataLine[1]))
                _tmpFitValues.append(float(dataLine[3]))


    def __outputDammifJobResults(self):
        self.addExecutiveSummaryLine("Number of DAMMIF jobs run : " + str(self.__iNbDammifJobs))
        for tmpDammifPlugin in self.__xsDammifPlugin.itervalues():
            dirLocation = tmpDammifPlugin.getWorkingDirectory()
            tmpRFactor = "RFactor = " + str(tmpDammifPlugin.dataOutput.getRfactor().value)
            tmpChiSqrt = "Chi(Sqrt) = " + str(tmpDammifPlugin.dataOutput.getChiSqrt().value)
            tmpStrLine = "\t".join([tmpChiSqrt, tmpRFactor, dirLocation])
            self.addExecutiveSummaryLine(tmpStrLine)
        self.appendExecutiveSummary(self.__edPluginExecDammif)


    def __plotRMaxSearchResults(self):
        """
        Plot results of Rmax optimization procedure and best fit of the experimental data
        """
        cm = matplotlib.cm.get_cmap('cool')

        fig1 = plt.figure(self.__iNbGnomSeries + 1, figsize=(6, 5))
        ax1 = fig1.add_subplot(1, 1, 1)

        for itr in range(self.__iNbGnomSeries):
            rMaxList = []
            fitQualityList = []
            for idx in range(self.__rMaxDivide + 1):
<<<<<<< HEAD
                rMaxList.append(self.__xsGnomPlugin[(itr, idx)].getDataInput().getRMax().getValue())
                fitQualityList.append(self.__xsGnomPlugin[(itr, idx)].getDataOutput().getFitQuality().getValue())
=======
                rMaxList.append(self.__xsGnomPlugin[(itr, idx)].dataInput.rMax.value)
                fitQualityList.append(self.__xsGnomPlugin[(itr, idx)].dataOutput.getFitQuality().value)
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
            ax1.plot(rMaxList, fitQualityList, linestyle='None', marker='o', color=cm(1.0 * (itr + 1) / self.__iNbGnomSeries), markersize=5, label="Iteration # %d" % (itr + 1))
            fign = plt.figure(itr + 1, figsize=(6, 5))
            axn = fign.add_subplot(1, 1, 1)
            axn.plot(rMaxList, fitQualityList, linestyle='-', marker='o', markersize=5, label="Iteration # %d" % (itr + 1))
<<<<<<< HEAD
            axn.set_xlabel(u"Rmax / \u00c5")
=======
            if self.__strUnit == "NANOMETER":
                axn.set_xlabel(u"Rmax / nm")
            else:
                axn.set_xlabel(u"Rmax / \u00c5")
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
            axn.set_ylabel('Fit quality')
            axn.legend(*axn.get_legend_handles_labels(), **{"loc":4})
            fign.savefig(os.path.join(self.getWorkingDirectory(), "rMaxSearchResults-%d.png" % (itr + 1)))
            fign.clf()
            del axn, fign

        ax1.set_xlabel(u"Rmax / \u00c5")
        ax1.set_ylabel('Fit quality')
<<<<<<< HEAD
        fig1.suptitle("Optimized value of RMax : %3.2f   Maximal fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(), self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
=======
        fig1.suptitle("Optimized value of RMax : %3.2f   Maximal fit quality : %1.3f" % (self.__edPluginExecGnom.dataInput.rMax.value, self.__edPluginExecGnom.dataOutput.getFitQuality().value))
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
        ax1.legend(*ax1.get_legend_handles_labels(), **{"loc":4})
        fig1.savefig(os.path.join(self.getWorkingDirectory(), "rMaxSearchResults.png"))
        fig1.clf()
        del ax1, fig1


<<<<<<< HEAD
        _listFitQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.dataOutput.getScatteringFitQ()]
        _listFitValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.dataOutput.getScatteringFitValues()]
        _listExpQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.dataInput.getExperimentalDataQ()]
        _listExpValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.dataInput.getExperimentalDataValues()]
=======
        npaFitQ = EDUtilsArray.xsDataToArray(self.__edPluginExecGnom.dataOutput.scatteringFitQArray)
        npaFitI = EDUtilsArray.xsDataToArray(self.__edPluginExecGnom.dataOutput.scatteringFitIArray)
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
        _listDammifFitQ = []
        _listDammifFitValues = []
        _listDammifExpQ = []
        _listDammifExpValues = []

        self.__parceDammifFit(_listDammifExpQ, _listDammifExpValues, _listDammifFitQ, _listDammifFitValues)
        figFit = plt.figure(figsize=(6, 5))
        axFit = figFit.add_subplot(1, 1, 1)
<<<<<<< HEAD
        axFit.semilogy(_listExpQ, _listExpValues, linestyle='None', marker='o', markersize=5, label="Experimental Data")
        axFit.semilogy(_listFitQ, _listFitValues, label="GNOM fitting curve")
        axFit.semilogy(_listDammifFitQ, _listDammifFitValues, color='y', label="DAMMIF ab-initio model")
        axFit.set_xlabel(u"q / \u00c5$^{-1}$")
        axFit.set_ylabel('I(q)')
        figFit.suptitle("RMax : %3.2f   Fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(), self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
=======
        axFit.semilogy(self.npaExperimentalDataQ, self.npaExperimentalDataI, linestyle='None', marker='o', markersize=5, label="Experimental Data")
        axFit.semilogy(npaFitQ, npaFitI, label="GNOM fitting curve")
        axFit.semilogy(_listDammifFitQ, _listDammifFitValues, color='y', label="DAMMIF ab-initio model")

        if self.__strUnit == "NANOMETER":
            axFit.set_xlabel(u"q / nm$^{-1}$")
        else:
            axFit.set_xlabel(u"q / \u00c5$^{-1}$")
        axFit.set_ylabel('I(q)')
        figFit.suptitle("RMax : %3.2f   Fit quality : %1.3f" % (self.__edPluginExecGnom.dataInput.rMax.value, self.__edPluginExecGnom.dataOutput.getFitQuality().value))
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
        axFit.legend(*axFit.get_legend_handles_labels())
        figFit.savefig(os.path.join(self.getWorkingDirectory(), "gnomFittingResults.png"))
        figFit.clf()
        del axFit, figFit

<<<<<<< HEAD
        _listDistributionR = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionR()]
        _listDistributionPr = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionPr()]
        _listDistributionErr = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionErr()]

        figDist = plt.figure(figsize=(6, 5))
        axDist = figDist.add_subplot(1, 1, 1)
        axDist.errorbar(_listDistributionR, _listDistributionPr, yerr=_listDistributionErr)
        axDist.set_xlabel(u"R / \u00c5")
=======
        npaR = EDUtilsArray.xsDataToArray(self.__edPluginExecGnom.dataOutput.arrayR)
        npaPr = EDUtilsArray.xsDataToArray(self.__edPluginExecGnom.dataOutput.arrayPr)
        npaErr = EDUtilsArray.xsDataToArray(self.__edPluginExecGnom.dataOutput.arrayErr)

        figDist = plt.figure(figsize=(6, 5))
        axDist = figDist.add_subplot(1, 1, 1)
        axDist.errorbar(npaR, npaPr, npaErr)
        if self.__strUnit == "NANOMETER":
            axDist.set_xlabel(u"R / nm")
        else:
            axDist.set_xlabel(u"R / \u00c5")
>>>>>>> d85e03d801b6d92e06c07ce403d72883676d00cd
        axDist.set_ylabel('P(R)')
        figDist.suptitle("Distance distribution function")
        figDist.savefig(os.path.join(self.getWorkingDirectory(), "distributionPR.png"))
        figDist.clf()
        del axDist, figDist

        if self.__bPlotFit:
            for gnomJob in self.__xsGnomPlugin.itervalues():
                gnomJob.plotFittingResults()
            self.__edPluginExecGnom.plotFittingResults()


    def __plotNSDResults(self):
        """
        Plot results of DAMMIF model alignment
        """

        _width = 0.5 / (self.__iNbDammifJobs - 1)
        _ind = [tmp * (1 - _width) + 0.25 for tmp in arange(self.__iNbDammifJobs)]
        _indLabels = []
        fig0 = plt.figure(figsize=(10, 8))
        ax0 = fig0.add_subplot(1, 1, 1)
        fig30 = plt.figure(figsize=(10, 8))
        ax30 = fig30.add_subplot(1, 1, 1)
        for ref in self.__xsDammifPlugin.iterkeys():

            _tmpNSD = []
            _tmpInd = []
            for tmp in self.__xsDammifPlugin.iterkeys():
                if tmp is not ref:
                    _tmpNSD.append(self.__xsSupcombPlugin[(min([tmp, ref]), max([tmp, ref]))].dataOutput.getNSD().value)
                    if tmp < ref:
                        _tmpInd.append(tmp + _width * (ref - tmp - 1))
                    else:
                        _tmpInd.append(tmp + _width * (ref - tmp))

            _tmpColor = self.__colorsDammif[ref]
            _tmpLegendPos = 0.8 - 0.4 * ref / self.__iNbDammifJobs
            _tmpLabel = os.path.relpath(self.__xsDammifPlugin[ref].getWorkingDirectory(), self.getWorkingDirectory())
            _indLabels.append(_tmpLabel)
            ax0.bar(_tmpInd, _tmpNSD, _width, color=_tmpColor, label=_tmpLabel)
            fig0.text(0.75, _tmpLegendPos, _tmpLabel, backgroundcolor=_tmpColor, \
                          color='white', weight='roman', size='medium')#, transform=ax0.transAxes)
            ax30.barh([self.__iNbDammifJobs - ref], self.__dammifRefNSD[ref], 0.8, color=_tmpColor)

        fig0.subplots_adjust(right=0.7, bottom=0.3)
        ax0.set_ylabel('Normalised Spatial Discrepancy (NSD)')
        ax0.set_xlabel('DAMMIF Model')
        ax0.set_title('DAMAVER model alignment results')
        ax0.set_xticks(_ind)
        ax0.set_xticklabels(_indLabels, rotation=65)
        fig0.savefig(os.path.join(self.getWorkingDirectory(), "dammifNSDResults.png"))
        fig0.clf()
        del ax0, fig0
        ax30.axvspan(self.__meanNSD - 2 * self.__varNSD, self.__meanNSD + 2 * self.__varNSD, facecolor='g', alpha=0.3)
#        fig30.subplots_adjust(left=0.3, right=0.8)
        ax30.set_xlabel('Average NSD')
        ax30.set_ylabel('DAMMIF Model')
        ax30.text(self.__meanNSD, self.__iNbDammifJobs + 1.5, "Model acceptance interval", ha="center", va="bottom", \
                   bbox=dict(boxstyle="round", ec='g', fc='g', alpha=0.3))
        ax30.set_ylim(0.5, self.__iNbDammifJobs + 1.2)
        ax30.set_yticks(self.__iNbDammifJobs + 0.4 - arange(self.__iNbDammifJobs))
        ax30.set_yticklabels(_indLabels)
        fig30.savefig(os.path.join(self.getWorkingDirectory(), "dammifAverageNSD.png"))
        fig30.clf()
        del ax30, fig30



    def __outputHTMLSummaryTable(self):
        _pdbFilter = EDPDBFilter()
        pathDamaverFileRaw = self.__edPluginExecDamaver.dataOutput.getDamaverPdbFile().getPath().value
        pathDamaverFile = os.path.join(self.__edPluginExecDamaver.getWorkingDirectory(), "damaver_valid.pdb")
        if os.path.isfile(pathDamaverFileRaw):
            _pdbFilter.filterPDBFile(pathDamaverFileRaw, pathDamaverFile)

        _htmlCode = ['<table border="1"  cellpadding=5>']
        if self.__bUseJMol:
            _htmlCode.extend(['<tr>', '<th><h3>GNOM</h3></th>', \
                              '<th><h3>DAMMIF</h3></th>', '<th><h3>DAMMIF<br />model</h3></th>', \
                              '<th><h3>DAMAVER</h3></th>', '<th><h3>DAMAVER<br />model</h3></th>', '</tr>'])
        else:
            _htmlCode.extend(['<tr>', '<th><h3>GNOM</h3></th>', '<th><h3>DAMMIF</h3></th>', '<th><h3>DAMAVER</h3></th>', '</tr>'])

        _gnomResults = os.linesep.join(["<p>Optimized value of RMax : %3.2f</p>" % self.__edPluginExecGnom.dataInput.rMax.value, \
                                  "<p>Estimated Rg : %3.2f</p>  " % self.__edPluginExecGnom.dataOutput.getRadiusOfGyration().value, \
                                  "<p>Output fit quality : %1.3f</p>" % self.__edPluginExecGnom.dataOutput.getFitQuality().value])
        _dammifResults = os.linesep.join(["<p>RFactor : %1.4f</p>" % self.__edPluginExecDammif.dataOutput.getRfactor().value, \
                                    "<p>Chi(Sqrt) : %3.3f</p>" % self.__edPluginExecDammif.dataOutput.getChiSqrt().value])
        _damaverResults = os.linesep.join(["<p>Mean NSD : %2.3f</p>" % self.dataOutput.getMeanNSD().value, \
                                     "<p>Variation of NSD : %2.3f</p>" % self.dataOutput.getVariationNSD().value])

        if self.__idxDammifBestChiSq is self.__idxDammifBestNSD:
            _dammifModelLink = os.path.join(os.path.relpath(self.__edPluginExecDammif.getWorkingDirectory(), self.getWorkingDirectory()), "dammif-1.pdb")
        else:
            _dammifModelLink = os.path.join(os.path.relpath(self.__xsSupcombPlugin[self.__idxDammifBestChiSq, self.__idxDammifBestNSD].getWorkingDirectory(), self.getWorkingDirectory()), "result.pdb")
        _damaverModelLink = os.path.relpath(pathDamaverFile, self.getWorkingDirectory())
        _dammifModel = os.linesep.join(['<script>jmolInitialize("./jmol", true);', \
                                  'jmolApplet(200, "load %s; isosurface saSurface; color orange; spin on");</script>' % _dammifModelLink])
        _damaverModel = os.linesep.join(['<script>jmolInitialize("./jmol", true);', \
                                  'jmolApplet(200, "load %s; isosurface saSurface; color orange; spin on");</script>' % _damaverModelLink])

        if self.__bUseJMol:
            _htmlCode.extend(['<tr>', '<td>%s</td>' % _gnomResults, \
                              '<td>%s</td>' % _dammifResults, \
                              '<td>%s</td>' % _dammifModel, \
                              '<td>%s</td>' % _damaverResults, \
                              '<td>%s</td>' % _damaverModel, '</tr>'])
        else:
            _htmlCode.extend(['<tr>', '<td>%s</td>' % _gnomResults, \
                              '<td>%s</td>' % _dammifResults, \
                              '<td>%s</td>' % _damaverResults, '</tr>'])

        _htmlCode.append('</table>')
        return _htmlCode


    def __outputHTMLGnomImages(self):
        #_imgRMax = os.path.join(self.getWorkingDirectory(),"rMaxSearchResults.png")
        #_imgFit = os.path.join(self.getWorkingDirectory(),"gnomFittingResults.png")
        _imgRMax = "rMaxSearchResults.png"
        _imgFit = "gnomFittingResults.png"
        _headerLines = ['<th><h3>Rmax search results</h3></th>', \
                        '<th><h3>Experimental data fitting</h3></th>']
        _imageLines = ['<td><img alt="Rmax search results" src="%s"></td>' % _imgRMax, \
                       '<td><img alt="Experimental data fitting" src="%s"></td>' % _imgFit]

        return ['<table>', '<tr>'] + _headerLines + ['</tr>', '<tr>'] + _imageLines + ['</tr>', '</table>']


    def __outputHTMLGnomTables(self):
        _gnomOutputLink = os.path.join(os.path.relpath(self.__edPluginExecGnom.getWorkingDirectory(), self.getWorkingDirectory()), "gnom.out")
        _imgPR = "distributionPR.png"

        _htmlCode = ['<hr />']
        _htmlCode.append("<h2>Results of GNOM run</h2>")
        _htmlCode.append('<hr />')
        _htmlCode.append('<h3>Optimized value of RMax : %3.2f</h3>' % self.__edPluginExecGnom.dataInput.rMax.value)
        _htmlCode.append("<h3>Estimated Rg : %3.2f</h3>" % self.__edPluginExecGnom.dataOutput.getRadiusOfGyration().value)
        _htmlCode.append("<h3>Output fit quality : %1.3f</h3>" % self.__edPluginExecGnom.dataOutput.getFitQuality().value)
        _htmlCode.append('<h4>GNOM output file : <a href="%(link)s">%(link)s</a></h4>' % {'link' : _gnomOutputLink})
        _htmlCode.append('<img alt="Distribution function" src="%s"></td>' % _imgPR)
        _htmlCode.append('<hr />')
        _htmlCode.append('<h3>Number of GNOM iterations performed before converging : %d</h3>' % self.__iNbGnomSeries)
        for itr in range(self.__iNbGnomSeries):
            _htmlCode.append("<div id='iteration_%d' class='toggle_folder'>" % (itr + 1))
            _htmlCode.append("<div id='iteration_%d_open_view' style='display: none;'>" % (itr + 1))
            _htmlCode.append('<span class="control close_control"><a href="javascript://" onclick="toggleElements(\'iteration_%(itr)d_open_view\',\'iteration_%(itr)d_closed_view\');">' % {'itr':(itr + 1)})
            _htmlCode.append('<span class="tool_tip" title="Hide table of iteration results">')
            _htmlCode.append('<h3> - Iteration # %d</h3></span></a></span><div>' % (itr + 1))
            #_tmpImgRMax = os.path.join(self.getWorkingDirectory(),"rMaxSearchResults-%d.png" % (itr+1))
            _tmpImgRMax = "rMaxSearchResults-%d.png" % (itr + 1)
            _htmlCode.append('<table>')
            _htmlCode.append('<tr><td><img alt="Iteration %d search results" src="%s"/></td>' % ((itr + 1), _tmpImgRMax))
            _htmlCode.append('<td><table border="1">')
            _htmlCode.extend(['<tr>', '<th><h3>Rmax</h3></th>', '<th><h3>Fit Quality</h3></th>', '<th><h3>Link</h3></th>', '</tr>'])
            for idx in range(self.__rMaxDivide):
                dirLocation = os.path.relpath(self.__xsGnomPlugin[(itr, idx)].getWorkingDirectory(), self.getWorkingDirectory())
                _htmlCode.extend(['<tr>', '<td>%3.2f</td>' % self.__xsGnomPlugin[(itr, idx)].dataInput.rMax.value, \
                               '<td>%1.3f</td>' % self.__xsGnomPlugin[(itr, idx)].dataOutput.getFitQuality().value, \
                               '<td><a href="%(link)s">%(link)s</a></td>' % {'link' : dirLocation}, '</tr>'])
            _htmlCode.append('</table></td></tr></table></div></div>')
            _htmlCode.append("<div id='iteration_%d_closed_view' style='display: block;'>" % (itr + 1))
            _htmlCode.append("<span class='control open_control'><a href='javascript://' onclick='toggleElements(\"iteration_%(itr)d_open_view\",\"iteration_%(itr)d_closed_view\");'>" % {'itr':(itr + 1)})
            _htmlCode.append("<span class='tool_tip' title='Show all iteration results'>")
            _htmlCode.append(" + Iteration # %d</span></a></span></div></div>" % (itr + 1))

        _htmlCode.append('<hr />')
        return _htmlCode


    def __outputHTMLDammifResults(self):
        _dammifDir = os.path.relpath(self.__edPluginExecDammif.getWorkingDirectory(), self.getWorkingDirectory())

        _htmlCode = ["<h2>Results of the best DAMMIF run</h2>"]
        _htmlCode.append('<hr />')
        _htmlCode.append("<h3>RFactor : %1.4f   Chi(Sqrt) : %3.3f</h3>" % (self.__edPluginExecDammif.dataOutput.getRfactor().value, self.__edPluginExecDammif.dataOutput.getChiSqrt().value))
        _htmlCode.append('<h4>DAMMIF particle model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(_dammifDir, "dammif-1.pdb")})
        _htmlCode.append('<h4>DAMMIF solvent model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(_dammifDir, "dammif-0.pdb")})
        _htmlCode.append('<h4>DAMMIF fit file : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(_dammifDir, "dammif.fit")})
        _htmlCode.append('<h4>DAMMIF log file : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(_dammifDir, "dammif.log")})
        _htmlCode.append('<hr />')
        _htmlCode.append("<h3>Number of DAMMIF jobs run : %d</h3>" % self.__iNbDammifJobs)
        _htmlCode.append('<table border="1">')
        if self.__bUseJMol:
            _htmlCode.extend(['<tr>', '<th><h3>RFactor</h3></th>', '<th><h3>Chi(Sqrt)</h3></th>', '<th><h3>Model</h3></th>', '<th><h3>Link</h3></th>', '</tr>'])
        else:
            _htmlCode.extend(['<tr>', '<th><h3>RFactor</h3></th>', '<th><h3>Chi(Sqrt)</h3></th>', '<th><h3>Link</h3></th>', '</tr>'])
        for (ref, tmpDammifPlugin) in self.__xsDammifPlugin.iteritems():
            if ref is self.__idxDammifBestNSD:
                modelLocation = os.path.relpath(tmpDammifPlugin.getWorkingDirectory(), self.getWorkingDirectory())
                modelFile = os.path.join(modelLocation, "dammif-1.pdb")
            else:
                modelLocation = os.path.relpath(self.__xsSupcombPlugin[ref, self.__idxDammifBestNSD].getWorkingDirectory(), self.getWorkingDirectory())
                modelFile = os.path.join(modelLocation, "result.pdb")

            dirLocation = os.path.relpath(tmpDammifPlugin.getWorkingDirectory(), self.getWorkingDirectory())
            _htmlCode.extend(['<tr>', '<td>%1.4f</td>' % tmpDammifPlugin.dataOutput.getRfactor().value, \
                               '<td>%3.3f</td>' % tmpDammifPlugin.dataOutput.getChiSqrt().value])
            if self.__bUseJMol:
                _htmlCode.append('<td><script>jmolInitialize("./jmol", true);')
                _htmlCode.append('jmolApplet(200, "load %s; isosurface saSurface; color isosurface %s");</script></td>' \
                                  % (modelFile, self.__colorsDammifRGB[ref]))
            _htmlCode.append('<td><a href="%(link)s">%(link)s</a>' % {'link' : dirLocation})
            if abs(self.__dammifRefNSD[ref] - self.__meanNSD) < 2 * self.__varNSD:
                _htmlCode.append('<br /><p>Accepted</p></td></tr>')
            else:
                _htmlCode.append('<br /><b>Rejected</b></td></tr>')

        _htmlCode.append('</table>')
        _htmlCode.append('<hr />')
        return _htmlCode


    def __outputHTMLDamaverResults(self):
        _pdbFilter = EDPDBFilter()
        pathDamfiltFileRaw = self.__edPluginExecDamfilt.dataOutput.getOutputPdbFile().getPath().value
        pathDamstartFileRaw = self.__edPluginExecDamstart.dataOutput.getOutputPdbFile().getPath().value
        pathDamaverFile = os.path.join(self.__edPluginExecDamaver.getWorkingDirectory(), "damaver_valid.pdb")
        pathDamfiltFile = os.path.join(self.__edPluginExecDamfilt.getWorkingDirectory(), "damfilt_valid.pdb")
        pathDamstartFile = os.path.join(self.__edPluginExecDamstart.getWorkingDirectory(), "damstart_valid.pdb")
        if os.path.isfile(pathDamstartFileRaw):
            _pdbFilter.filterPDBFile(pathDamfiltFileRaw, pathDamfiltFile)
        if os.path.isfile(pathDamstartFileRaw):
            _pdbFilter.filterPDBFile(pathDamstartFileRaw, pathDamstartFile)

        _damaverPdbLink = os.path.relpath(pathDamaverFile, self.getWorkingDirectory())
        _damfiltPdbLink = os.path.relpath(pathDamfiltFile, self.getWorkingDirectory())
        _damstartPdbLink = os.path.relpath(pathDamstartFile, self.getWorkingDirectory())
        _imgDamaverRes = "dammifNSDResults.png"
        _imgDamaverAverageNSD = "dammifAverageNSD.png"

        _htmlCode = ["<h2>Results of model averaging using DAMAVER pipeline</h2>"]
        _htmlCode.append('<img alt="Damaver Average NSD" src="%s">' % _imgDamaverAverageNSD)
        _htmlCode.append('<img alt="Damaver results" src="%s">' % _imgDamaverRes)
        if self.__bUseJMol:
            _htmlCode.append('<table border ="1">')
            _htmlCode.append('<tr><td> <h4>DAMAVER output pdb model</h4></td>')
            _htmlCode.append('<td><script>jmolInitialize("./jmol", true);')
            _htmlCode.append('jmolApplet(200, "load %s; isosurface saSurface; color orange");</script></td>' % _damaverPdbLink)
            _htmlCode.append('<td><a href="%(link)s">%(link)s</a></td></tr>' % {'link': _damaverPdbLink})

            _htmlCode.append('<tr><td> <h4>DAMFILT output pdb model</h4></td>')
            _htmlCode.append('<td><script>jmolInitialize("./jmol", true);')
            _htmlCode.append('jmolApplet(200, "load %s; isosurface saSurface; color orange");</script></td>' % _damfiltPdbLink)
            _htmlCode.append('<td><a href="%(link)s">%(link)s</a></td></tr>' % {'link': _damfiltPdbLink})

            _htmlCode.append('<tr><td> <h4>DAMSTART output pdb model</h4></td>')
            _htmlCode.append('<td><script>jmolInitialize("./jmol", true);')
            _htmlCode.append('jmolApplet(200, "load %s; isosurface saSurface; color orange");</script></td>' % _damstartPdbLink)
            _htmlCode.append('<td><a href="%(link)s">%(link)s</a></td></tr>' % {'link': _damstartPdbLink})
            _htmlCode.append('</table>')
        else:
            _htmlCode.append('<hr />')
            _htmlCode.append('<h4>DAMAVER output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': _damaverPdbLink})
            _htmlCode.append('<h4>DAMFILT output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': _damfiltPdbLink})
            _htmlCode.append('<h4>DAMSTART output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': _damstartPdbLink})
            _htmlCode.extend(['<pre>', '<br /> '.join(self.__edPluginExecDamaver.getListExecutiveSummaryLines()[6:]), '</pre>'])
            _htmlCode.append('<hr />')

        return _htmlCode


    def __outputHTMLReferences(self):
        tmpLines = [ '<hr /><h2>References</h2>',
                    """<p><b>ATSAS</b> A program suite for small-angle scattering data analysis from biological macromolecules.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.embl-hamburg.de/biosaxs/software.html'},
                    """<p><b>GNOM</b> Svergun D.I. (1992) Determination of the regularization parameter
                        in indirect-transform methods using perceptual criteria. <em>J. Appl. Cryst.</em>
                        <strong>25</strong>, 495-503</p>""",
                    """<p><b>DAMMIF</b> Franke, D. and Svergun, D.I. (2009) DAMMIF, a program for
                         rapid ab-initio shape determination in small-angle scattering. <em>J. Appl. Cryst.</em> <strong>42</strong>, 342-346.</p>""", \
                    """<p><b>SUPCOMB</b> M.Kozin and D.Svergun (2000) Automated matching of high- and low-resolution
                        structural models <em>J. Appl. Cryst.</em> <strong>34</strong>, 33-41.</p>""",
                    """<p><b>DAMAVER</b> V. V. Volkov and D. I. Svergun (2003). Uniqueness of ab-initio shape
                        determination in small-angle scattering. <em>J. Appl. Cryst.</em> <strong>36</strong>, 860-864.</p>""", \
                    """<p><b>EDNA</b> M.-F. Incardona, G. P. Bourenkov, K. Levik, R. A. Pieritz, A. N. Popov and O. Svensson (2009).
                        EDNA: a framework for plugin-based applications applied to X-ray experiment online data analysis.
                        <em>J. Synchrotron Rad.</em> <strong>16</strong>, 872-879.<a href="%(link)s">%(link)s</a></p>""" % {'link':'http://www.edna-site.org/'}, \
                    """<p><b>Jmol</b> an open-source Java viewer for chemical structures in 3D.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.jmol.org/'},
                    """<p><b>Numpy</b> the package for scientific computing in Python
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://numpy.scipy.org/'},
                    """<p><b>Matplotlib</b> the package for 2D plotting in Python
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://matplotlib.sourceforge.net/'},
                    """<p><b>NeXus</b> a common data format for neutron, x-ray, and muon science.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.nexusformat.org/'},
                    """<p><b>h5py</b> a simple Python interface to HDF5
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://h5py.alfven.org/'}]

        return tmpLines


    def __jsFunctions(self):
        tmpLines = [ \
        '<script>                                                           ',
        '/* EDNA2html.js                                                    ',
        '                                                                   ',
        '   Javascript functions for use in the output of EDNA2html         ',
        '                                                                   ',
        '   CVS_id $Id: EDNA2html.js,v 1.3 2010/04/22 09:19:34 pjb93 Exp $  ',
        ' */                                                                ',
        '                                                                   ',
        '// Toggle the display property of a specific element               ',
        '// Specify the id of an element and its display style              ',
        '// will be flipped from "none" to "block", or "block" to           ',
        '// "none" as appropriate                                           ',
        'function toggleElement(name)                                       ',
        '{                                                                  ',
        '    var obj = document.getElementById(name);                       ',
        '    var state = obj.style.display;                                 ',
        '    var new_state = "";                                            ',
        '    if (state == "none") {                                         ',
        '    new_state = "block";                                           ',
        '    } else {                                                       ',
        '    new_state = "none";                                            ',
        '    }                                                              ',
        '    obj.style.display = new_state;                                 ',
        '}                                                                  ',
        '                                                                   ',
        '// Toggle the display properties of multiple elements              ',
        '// Specify a list of element ids to have their display             ',
        '// style flipped between "none" and "block"                        ',
        'function toggleElements()                                          ',
        '{                                                                  ',
        '    for (var i=0; i < arguments.length; i++) {                     ',
        '    toggleElement(arguments[i]);                                   ',
        '    }                                                              ',
        '}                                                                  ',
        '</script>                                                          ',
        '<script src="./jmol/Jmol.js"></script>']
        return os.linesep.join(tmpLines)


    def __outputHTMLPipelineResults(self):
        """
        Output pipilene results in HTML format
        """

        htmlText = ['<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"', '"http://www.w3.org/TR/html4/strict.dtd"> ', \
                    '<html>', '<head>', '<title>Solution Scattering Pipeline Results</title>', self.__jsFunctions(), '</head>', '<body>']
        htmlText.append('<h1>Summary of Solution Scattering Pipeline Execution</h1>')

        if self.dataInput.getTitle() is not None:
            htmlText.append('<h1>Data file : %s</h1>' % self.dataInput.getTitle().value)

        htmlText.extend(self.__outputHTMLSummaryTable())
        htmlText.extend(self.__outputHTMLGnomImages())
        htmlText.extend(self.__outputHTMLGnomTables())
        if not self.__bOnlyGnom:
            htmlText.extend(self.__outputHTMLDammifResults())
            htmlText.extend(self.__outputHTMLDamaverResults())
        htmlText.extend(self.__outputHTMLReferences())

        htmlText.append('<hr /></body>')
        with open(os.path.join(self.getWorkingDirectory(), "pipelineResults.html"), 'w') as htmlLog:
            htmlLog.write(os.linesep.join(htmlText))


    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginControlSolutionScatteringv0_4.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of Solution Scattering Pipeline Execution:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()
        self.__outputGnomSeriesResults()
        self.addExecutiveSummarySeparator()
        if not self.__bOnlyGnom:
            self.__outputDammifJobResults()
            self.addExecutiveSummarySeparator()
            self.appendExecutiveSummary(self.__edPluginExecDamaver)

        self.verboseScreenExecutiveSummary()

        self.__outputHTMLPipelineResults()

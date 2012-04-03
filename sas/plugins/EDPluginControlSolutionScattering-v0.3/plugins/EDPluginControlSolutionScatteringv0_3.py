#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:        irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os, operator, itertools, matplotlib, distutils.dir_util
matplotlib.use('Agg')

from matplotlib import pylab
from matplotlib.colors import colorConverter

from numpy import mean, std, var, arange, resize

from EDVerbose import EDVerbose
from EDSlot import EDSlot
from EDPluginControl import EDPluginControl
from EDActionCluster import EDActionCluster
from EDUtilsFile import EDUtilsFile
from EDConfiguration import EDConfiguration
from EDParallelJobLauncher import EDParallelJobLauncher

from EDPDBFilter import EDPDBFilter

from XSDataSAS import XSDataInputSolutionScattering
from XSDataSAS import XSDataResultSolutionScattering
from XSDataSAS import XSDataInputGnom
from XSDataSAS import XSDataInputDammif
from XSDataSAS import XSDataInputSupcomb
from XSDataSAS import XSDataInputDamaver
from XSDataSAS import XSDataInputDamfilt
from XSDataSAS import XSDataInputDamstart

from XSDataSAS import XSDataDouble, XSDataInteger, XSDataString, XSDataBoolean


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

class EDPluginControlSolutionScatteringv0_3(EDPluginControl):
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

        self.__strPluginExecGnom = "EDPluginExecGnomv0_1"
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

        self.__xsDataExperimentalDataQ = None
        self.__xsDataExperimentalDataValues = None
        self.__xsDataExperimentalDataStdDev = None
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
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

        self.checkRMaxSearchParameters()
        self.checkModeParameter()
        #self.checkUnitParameter()
        self.checkJMol()

    def checkRMaxSearchParameters(self):
        if self.getDataInput().getRMaxSearchSettings() is not None:
            if self.getDataInput().getRMaxSearchSettings().getRMaxStart() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_3.setRMaxSerachParameters rMaxStart is missing")
                self.setFailure()
            else:
                if self.getDataInput().getRMaxSearchSettings().getRMaxStart().getValue() < self.__rMaxStart:
                    EDVerbose.WARNING("EDPluginControlSolutionScatteringv0_3.setRMaxSerachParameters rMaxStart is too small. Resetting to the default.")
            if self.getDataInput().getRMaxSearchSettings().getRMaxStop() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_3.setRMaxSerachParameters rMaxStop is missing")
                self.setFailure()
            if self.getDataInput().getRMaxSearchSettings().getRMaxAbsTol() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_3.setRMaxSerachParameters rMaxAbsTol is missing")
                self.setFailure()
            if self.getDataInput().getRMaxSearchSettings().getRMaxIntervals() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_3.setRMaxSerachParameters rMaxIntervals is missing")
                self.setFailure()

    def checkModeParameter(self):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.checkModeParameter")
        try:
            if self.getDataInput().getMode().getValue().lower() in ['fast', 'slow']:
                self.__strMode = self.getDataInput().getMode().getValue().lower()
        except:
            EDVerbose.WARNING("Running Solution Scattering pipeline in fast mode by default")

    def checkUnitParameter(self):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.checkUnitParameter")
        try:
            if self.getDataInput().getAngularUnits().getValue() in [1, 2, 3, 4]:
                self.__iUnit = self.getDataInput().getAngularUnits().getValue()
                if self.__iUnit in [1, 3]:
                    self.__strUnit = "ANGSTROM"
                else:
                    self.__strUnit = "NANOMETER"
        except:
            EDVerbose.WARNING("Using Angstrom units for q-values by default")

    def checkJMol(self):
        self.__pluginConfiguration = self.getConfiguration()
        self.__strPathToJMol = EDConfiguration.getStringParamValue(self.__pluginConfiguration, 'jMol')
        if os.path.isdir(self.__strPathToJMol):
            distutils.dir_util.copy_tree(self.__strPathToJMol, os.path.join(self.getWorkingDirectory(), "jmol"))
            self.__bUseJMol = True


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.preProcess")

        xsDataInputSolutionScattering = self.getDataInput()
        self.__xsDataExperimentalDataQ = xsDataInputSolutionScattering.getExperimentalDataQ()
        self.__xsDataExperimentalDataValues = xsDataInputSolutionScattering.getExperimentalDataValues()
        if xsDataInputSolutionScattering.getExperimentalDataStdDev():
            self.__xsDataExperimentalDataStdDev = xsDataInputSolutionScattering.getExperimentalDataStdDev()

        if self.getDataInput().getSymmetry() is not None:
            self.__strSymmetry = self.getDataInput().getSymmetry().getValue()

        if self.getDataInput().getRMaxSearchSettings() is not None:
            self.__rMaxStart = max(self.__rMaxStart, self.getDataInput().getRMaxSearchSettings().getRMaxStart().getValue())
            self.__rMaxStop = self.getDataInput().getRMaxSearchSettings().getRMaxStop().getValue()
            self.__absTol = self.getDataInput().getRMaxSearchSettings().getRMaxAbsTol().getValue()
            self.__absErr = self.__absTol * 10
            self.__rMaxDivide = self.getDataInput().getRMaxSearchSettings().getRMaxIntervals().getValue()

        if self.getDataInput().getINbThreads() is not None:
            self.__iNbThreads = self.getDataInput().getINbThreads().getValue()

        if self.getDataInput().getOnlyGnom() is not None:
            self.__bOnlyGnom = self.getDataInput().getOnlyGnom().getValue()
        if self.getDataInput().getPlotFit() is not None:
            self.__bPlotFit = self.getDataInput().getPlotFit().getValue()

    def __checkGnomSeriesResults(self, serInput):
        fitResultDict = dict([((ser, idx), plg.getDataOutput().getFitQuality().getValue()) for (ser, idx), plg in self.__xsGnomPlugin.items() if ser == serInput])
        fitResultList = sorted(fitResultDict.iteritems(), key=operator.itemgetter(1), reverse=True)
        ((ser, idx_max), _) = fitResultList[0]

        # Find rMax values bracketing the best rMax result
        self.__rMaxStart = self.__xsGnomPlugin[(ser, max(idx_max - 1, 0))].getDataInput().getRMax().getValue()
        self.__rMaxStop = self.__xsGnomPlugin[(ser, min(idx_max + 1, len(fitResultList) - 1))].getDataInput().getRMax().getValue()
        self.__absErr = (fitResultList[0][1] - fitResultList[-1][1])
        return self.__xsGnomPlugin[(ser, idx_max)]


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.process")

        #Make series of GNOM runs narrowing down the optimal value of rMax
        ser = 0
        while self.__absErr > self.__absTol:

            if (not self.__rMaxDivide):
                xsDataRMax = [XSDataDouble(self.__rMaxStart)]
            else:
                xsDataRMax = itertools.imap(lambda idx: XSDataDouble(self.__rMaxStart + idx * (self.__rMaxStop - self.__rMaxStart) / self.__rMaxDivide), range(self.__rMaxDivide + 1))

            dictDataInputGnom = {}
            for idx, rMax in enumerate(xsDataRMax):
                dictDataInputGnom[(ser, idx)] = XSDataInputGnom()
                dictDataInputGnom[(ser, idx)].setExperimentalDataQ(self.__xsDataExperimentalDataQ)
                dictDataInputGnom[(ser, idx)].setExperimentalDataValues(self.__xsDataExperimentalDataValues)
                if self.__xsDataExperimentalDataStdDev:
                    dictDataInputGnom[(ser, idx)].setExperimentalDataStdDev(self.__xsDataExperimentalDataStdDev)
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
        self.__edPluginExecGnom.setDataInput(edPluginGnomOptimal.getDataInput())
        self.__edPluginExecGnom.connectSUCCESS(self.doSuccessExecGnom)
        self.__edPluginExecGnom.connectFAILURE(self.doFailureExecGnom)
        self.executePluginSynchronous(self.__edPluginExecGnom)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.postProcess")


    def doSuccessExecGnom(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecGnom")
        self.retrieveSuccessMessages(self.__edPluginExecGnom, "EDPluginControlSolutionScatteringv0_3.doSuccessExecGnom")

        if not self.__bOnlyGnom:
            self.__xsDataOutput = self.__edPluginExecGnom.getDataOutput().getOutput()

            xsDataInputDammif = XSDataInputDammif()
            xsDataInputDammif.setGnomOutputFile(self.__xsDataOutput)
            xsDataInputDammif.setUnit(XSDataString(self.__strUnit))
            xsDataInputDammif.setSymmetry(XSDataString(self.__strSymmetry))
            xsDataInputDammif.setMode(XSDataString(self.__strMode))

            dictDataInputDammif = {}
            for idx in range(self.__iNbDammifJobs):
                dictDataInputDammif[idx] = xsDataInputDammif

            self.__xsDammifJobs = EDParallelJobLauncher(self, self.__strPluginExecDammif, dictDataInputDammif, self.__iNbThreads)
            self.__xsDammifJobs.connectSUCCESS(self.doSuccessExecDammif)
            self.__xsDammifJobs.connectFAILURE(self.doFailureExecDammif)
            self.executePluginSynchronous(self.__xsDammifJobs)


    def doFailureExecGnomActionCluster(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecGnom")
        self.retrieveFailureMessages(self.__xsGnomJobs, "EDPluginControlSolutionScatteringv0_3.doFailureExecGnom")


    def doFailureExecGnom(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecGnom")
        self.retrieveFailureMessages(self, "EDPluginControlSolutionScatteringv0_3.doFailureExecGnom")


    def __checkDammifSeriesResults(self):
        """
        Find DAMMIF run with best chi-square value
        """
        fitResultDict = dict([(idx, plg.getDataOutput().getChiSqrt().getValue()) for idx, plg in self.__xsDammifPlugin.items()])
        fitResultList = sorted(fitResultDict.iteritems(), key=operator.itemgetter(1))
        (idx_max, _) = fitResultList[0]
        self.__idxDammifBestChiSq = idx_max

        return self.__xsDammifPlugin[idx_max]

    def doSuccessExecDammif(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecDammif")
        self.retrieveSuccessMessages(self.__xsDammifJobs, "EDPluginControlSolutionScatteringv0_3.doSuccessExecDammif")

        self.__xsDammifPlugin.update(self.__xsDammifJobs.getPluginJobs())

        self.__xsDataResultSolutionScattering.setLineProfileFitQuality(self.__edPluginExecGnom.getDataOutput().getFitQuality())
        self.__xsDataResultSolutionScattering.setScatteringFitQ(self.__edPluginExecGnom.getDataOutput().getScatteringFitQ())
        self.__xsDataResultSolutionScattering.setScatteringFitValues(self.__edPluginExecGnom.getDataOutput().getScatteringFitValues())

        self.__edPluginExecDammif = self.__checkDammifSeriesResults()
        self.__plotRMaxSearchResults()


        self.__xsDataResultSolutionScattering.setFitFile(self.__edPluginExecDammif.getDataOutput().getFitFile())
        self.__xsDataResultSolutionScattering.setLogFile(self.__edPluginExecDammif.getDataOutput().getLogFile())
        self.__xsDataResultSolutionScattering.setPdbMoleculeFile(self.__edPluginExecDammif.getDataOutput().getPdbMoleculeFile())
        self.__xsDataResultSolutionScattering.setPdbSolventFile(self.__edPluginExecDammif.getDataOutput().getPdbSolventFile())

        dictDataInputSupcomb = {}
        for idx in self.__xsDammifPlugin.iterkeys():
            for ser in range(idx):
                dictDataInputSupcomb[(ser, idx)] = XSDataInputSupcomb()
                dictDataInputSupcomb[(ser, idx)].setTemplateFile(self.__xsDammifPlugin[idx].getDataOutput().getPdbMoleculeFile())
                dictDataInputSupcomb[(ser, idx)].setSuperimposeFile(self.__xsDammifPlugin[ser].getDataOutput().getPdbMoleculeFile())
        self.__xsSupcombJobs = EDParallelJobLauncher(self, self.__strPluginExecSupcomb, dictDataInputSupcomb, self.__iNbThreads)
        self.__xsSupcombJobs.connectSUCCESS(self.doSuccessExecSupcomb)
        self.__xsSupcombJobs.connectFAILURE(self.doFailureExecSupcomb)
        self.executePluginSynchronous(self.__xsSupcombJobs)


    def doFailureExecDammif(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecDammif")
        self.retrieveFailureMessages(self.__xsDammifJobs, "EDPluginControlSolutionScatteringv0_3.doFailureExecDammif")


    def doSuccessExecSupcomb(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecSupcomb")
        self.retrieveSuccessMessages(self.__xsSupcombJobs, "EDPluginControlSolutionScatteringv0_3.doSuccessExecSupcomb")

        self.__xsSupcombPlugin.update(self.__xsSupcombJobs.getPluginJobs())

        self.__idxDammifBestNSD = self.__selectBestNSDModel()

        dictDataInputSupcombBest = {}
        for ser in range(self.__idxDammifBestNSD + 1, self.__iNbDammifJobs):
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)] = XSDataInputSupcomb()
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)].setTemplateFile(self.__xsDammifPlugin[self.__idxDammifBestNSD].getDataOutput().getPdbMoleculeFile())
            dictDataInputSupcombBest[(ser, self.__idxDammifBestNSD)].setSuperimposeFile(self.__xsDammifPlugin[ser].getDataOutput().getPdbMoleculeFile())
        self.__xsSupcombJobsBest = EDParallelJobLauncher(self, self.__strPluginExecSupcomb, dictDataInputSupcombBest, self.__iNbThreads)
        self.__xsSupcombJobsBest.connectSUCCESS(self.doSuccessExecSupcombAlign)
        self.__xsSupcombJobsBest.connectFAILURE(self.doFailureExecSupcombAlign)
        self.executePluginSynchronous(self.__xsSupcombJobsBest)


    def doFailureExecSupcomb(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecSupcomb")
        self.retrieveFailureMessages(self.__xsSupcombJobs, "EDPluginControlSolutionScatteringv0_3.doFailureExecSupcomb")


    def doSuccessExecSupcombAlign(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecSupcombAlign")
        self.retrieveSuccessMessages(self.__xsSupcombJobsBest, "EDPluginControlSolutionScatteringv0_3.doSuccessExecSupcombAlign")

        self.__xsSupcombPlugin.update(self.__xsSupcombJobsBest.getPluginJobs())
        self.__plotNSDResults()

        xsDataInputDamaver = XSDataInputDamaver()
        tmpOutputPdbFiles = [self.__xsDammifPlugin[self.__idxDammifBestNSD].getDataOutput().getPdbMoleculeFile()]

        for (idx, tmpXSDammifPlugin) in self.__xsDammifPlugin.iteritems():
            if idx is not self.__idxDammifBestNSD:
                if abs(self.__dammifRefNSD[idx] - self.__meanNSD) < 2 * self.__varNSD:
                    tmpOutputPdbFiles.append(self.__xsSupcombPlugin[(idx, self.__idxDammifBestNSD)].getDataOutput().getOutputFilename())

        xsDataInputDamaver.setPdbInputFiles(tmpOutputPdbFiles)
        xsDataInputDamaver.setAutomatic(XSDataBoolean(False))

        self.__edPluginExecDamaver = self.loadPlugin(self.__strPluginExecDamaver)
        self.__edPluginExecDamaver.setDataInput(xsDataInputDamaver)
        self.__edPluginExecDamaver.connectSUCCESS(self.doSuccessExecDamaver)
        self.__edPluginExecDamaver.connectFAILURE(self.doFailureExecDamaver)
        self.executePluginSynchronous(self.__edPluginExecDamaver)


    def doFailureExecSupcombAlign(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecSupcombAlign")
        self.retrieveFailureMessages(self.__xsSupcombJobsBest, "EDPluginControlSolutionScatteringv0_3.doFailureExecSupcombAlign")


    def doSuccessExecDamaver(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecDamaver")
        self.retrieveSuccessMessages(self.__edPluginExecDamaver, "EDPluginControlSolutionScatteringv0_3.doSuccessExecDamaver")

        xsDataInputDamfilt = XSDataInputDamfilt()
        xsDataInputDamfilt.setInputPdbFile(self.__edPluginExecDamaver.getDataOutput().getDamaverPdbFile())

        self.__edPluginExecDamfilt = self.loadPlugin(self.__strPluginExecDamfilt)
        self.__edPluginExecDamfilt.setDataInput(xsDataInputDamfilt)
        self.__edPluginExecDamfilt.connectSUCCESS(self.doSuccessExecDamfilt)
        self.__edPluginExecDamfilt.connectFAILURE(self.doFailureExecDamfilt)
        self.executePluginSynchronous(self.__edPluginExecDamfilt)


    def doFailureExecDamaver(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecDamaver")
        self.retrieveFailureMessages(self.__edPluginExecDamaver, "EDPluginControlSolutionScatteringv0_3.doFailureExecDamaver")


    def doSuccessExecDamfilt(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecDamfilt")
        self.retrieveSuccessMessages(self.__edPluginExecDamfilt, "EDPluginControlSolutionScatteringv0_3.doSuccessExecDamfilt")

        xsDataInputDamstart = XSDataInputDamstart()
        xsDataInputDamstart.setInputPdbFile(self.__edPluginExecDamaver.getDataOutput().getDamaverPdbFile())

        self.__edPluginExecDamstart = self.loadPlugin(self.__strPluginExecDamstart)
        self.__edPluginExecDamstart.setDataInput(xsDataInputDamstart)
        self.__edPluginExecDamstart.connectSUCCESS(self.doSuccessExecDamstart)
        self.__edPluginExecDamstart.connectFAILURE(self.doFailureExecDamstart)
        self.executePluginSynchronous(self.__edPluginExecDamstart)


    def doFailureExecDamfilt(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecDamfilt")
        self.retrieveFailureMessages(self.__edPluginExecDamfilt, "EDPluginControlSolutionScatteringv0_3.doFailureExecDamfilt")


    def doSuccessExecDamstart(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doSuccessExecDamstart")
        self.retrieveSuccessMessages(self.__edPluginExecDamstart, "EDPluginControlSolutionScatteringv0_3.doSuccessExecDamstart")

        self.setDataOutput(self.__xsDataResultSolutionScattering)


    def doFailureExecDamstart(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.doFailureExecDamstart")
        self.retrieveFailureMessages(self.__edPluginExecDamstart, "EDPluginControlSolutionScatteringv0_3.doFailureExecDamstart")


    def __selectBestNSDModel(self):
        for ref in self.__xsDammifPlugin.iterkeys():
            self.__dammifRefNSD[ref] = mean([self.__xsSupcombPlugin[(min([tmp, ref]), max([tmp, ref]))].getDataOutput().getNSD().getValue() \
                           for tmp in self.__xsDammifPlugin.iterkeys() if tmp is not ref])

        self.__meanNSD = mean(self.__dammifRefNSD.values())
        self.__varNSD = std(self.__dammifRefNSD.values())
        self.__xsDataResultSolutionScattering.setMeanNSD(XSDataDouble(self.__meanNSD))
        self.__xsDataResultSolutionScattering.setVariationNSD(XSDataDouble(self.__varNSD))

        resultsNSD = sorted(self.__dammifRefNSD.iteritems(), key=operator.itemgetter(1))

        return resultsNSD[0][0]


    def readGnomNexusDataColumns(self, _fileName, _strNxsQ, _strNxsData, _iNbColumns, _fQMin, _fQMax):
        """
        Initialize pipeline input data structure using Nexus data file.
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
                if self.getDataInput().getAngularUnits() is not None:
                    units = self.getDataInput().getAngularUnits().getValue()
                if units in [2, 4]:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ / 10.0))
                else:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ))

                _tmpValue = mean(nxsExperimentalValues[:_iNbColumns, idx])
                tmpExperimentalDataValues.append(XSDataDouble(_tmpValue))
                if (_iNbColumns > 1):
                    _tmpStdDev = std(nxsExperimentalValues[:_iNbColumns, idx])
                    tmpExperimentalDataStdDev.append(XSDataDouble(_tmpStdDev))

        self.getDataInput().setExperimentalDataQ(tmpExperimentalDataQ)
        self.getDataInput().setExperimentalDataValues(tmpExperimentalDataValues)
        if (_iNbColumns > 1):
            self.getDataInput().setExperimentalDataStdDev(tmpExperimentalDataStdDev)


    def readGnomDataColumns(self, fileName, _iNbColumns, _fQMin, _fQMax):
        """
        Initialize pipeline input data structure using ASCII data file.
        Lines with text fields are ignored.
        For every row up to _iNbColums of data will be read.
        """
        tmpExperimentalDataQ = []
        tmpExperimentalDataValues = []
        tmpExperimentalDataStdDev = []

        dataLines = EDUtilsFile.readFile(fileName).splitlines()

        for line in dataLines:
            if not rejectDataLine(line, 2):
                lineList = line.split()
                _tmpQ = float(lineList[0])

                if (((_tmpQ > _fQMin) or (_fQMin is None)) and \
                    ((_tmpQ < _fQMax) or (_fQMax is None))):

                    units = 1
                    if self.getDataInput().getAngularUnits() is not None:
                        units = self.getDataInput().getAngularUnits().getValue()
                    if units in [2, 4]:
                        tmpExperimentalDataQ.append(XSDataDouble(_tmpQ / 10.0))
                    else:
                        tmpExperimentalDataQ.append(XSDataDouble(_tmpQ))

                    _tmpValue = mean(map(float, lineList[1:_iNbColumns + 1]))
                    tmpExperimentalDataValues.append(XSDataDouble(_tmpValue))
                    if (_iNbColumns > 1):
                        _tmpStdDev = std(map(float, lineList[1:_iNbColumns + 1]))
                        tmpExperimentalDataStdDev.append(XSDataDouble(_tmpStdDev))

        self.getDataInput().setExperimentalDataQ(tmpExperimentalDataQ)
        self.getDataInput().setExperimentalDataValues(tmpExperimentalDataValues)
        if (_iNbColumns > 1):
            self.getDataInput().setExperimentalDataStdDev(tmpExperimentalDataStdDev)


    def __outputGnomSeriesResults(self):
        self.addExecutiveSummaryLine("Number of GNOM iterations performed before converging : " + str(self.__iNbGnomSeries))
        for itr in range(self.__iNbGnomSeries):
            self.addExecutiveSummarySeparator()
            self.addExecutiveSummaryLine("Iteration # " + str(itr + 1))
            for idx in range(self.__rMaxDivide):
                dirLocation = self.__xsGnomPlugin[(itr, idx)].getWorkingDirectory()
                tmpRMaxInput = "rMax = %3.2f" % self.__xsGnomPlugin[(itr, idx)].getDataInput().getRMax().getValue()
                tmpFitQuality = "fitQuality = " + str(self.__xsGnomPlugin[(itr, idx)].getDataOutput().getFitQuality().getValue())
                tmpStrLine = "\t".join([tmpRMaxInput, tmpFitQuality, dirLocation])
                self.addExecutiveSummaryLine(tmpStrLine)
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Optimized value of RMax = %3.2f" % self.__edPluginExecGnom.getDataInput().getRMax().getValue())
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
            tmpRFactor = "RFactor = " + str(tmpDammifPlugin.getDataOutput().getRfactor().getValue())
            tmpChiSqrt = "Chi(Sqrt) = " + str(tmpDammifPlugin.getDataOutput().getChiSqrt().getValue())
            tmpStrLine = "\t".join([tmpChiSqrt, tmpRFactor, dirLocation])
            self.addExecutiveSummaryLine(tmpStrLine)
        self.appendExecutiveSummary(self.__edPluginExecDammif)


    def __plotRMaxSearchResults(self):
        """
        Plot results of Rmax optimization procedure and best fit of the experimental data
        """
        cm = matplotlib.cm.get_cmap('cool')
        #pylab.rcParams['figure.figsize'] = 6, 5
        for itr in range(self.__iNbGnomSeries):
            rMaxList = []
            fitQualityList = []
            for idx in range(self.__rMaxDivide + 1):
                rMaxList.append(self.__xsGnomPlugin[(itr, idx)].getDataInput().getRMax().getValue())
                fitQualityList.append(self.__xsGnomPlugin[(itr, idx)].getDataOutput().getFitQuality().getValue())

            #pylab.plot(fitQualityList, marker='o', color=cm(1.0*itr/(self.__iNbGnomSeries-1)), markersize=5,  label="Iteration # %d" % (itr+1))
            pylab.figure(self.__iNbGnomSeries + 1, figsize=(6, 5))
            pylab.plot(rMaxList, fitQualityList, linestyle='None', marker='o', color=cm(1.0 * (itr + 1) / self.__iNbGnomSeries), markersize=5, label="Iteration # %d" % (itr + 1))
            pylab.figure(itr + 1, figsize=(6, 5))
            pylab.plot(rMaxList, fitQualityList, linestyle='-', marker='o', markersize=5, label="Iteration # %d" % (itr + 1))
            pylab.xlabel(u"Rmax / \u00c5")
            pylab.ylabel('Fit quality')
            pylab.legend(loc=4)
            pylab.savefig(os.path.join(self.getWorkingDirectory(), "rMaxSearchResults-%d.png" % (itr + 1)))

        pylab.figure(self.__iNbGnomSeries + 1, figsize=(6, 5))
        pylab.xlabel(u"Rmax / \u00c5")
        pylab.ylabel('Fit quality')
        pylab.suptitle("Optimized value of RMax : %3.2f   Maximal fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(), self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
        pylab.legend(loc=4)
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "rMaxSearchResults.png"))
        pylab.clf()


        _listFitQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getScatteringFitQ()]
        _listFitValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getScatteringFitValues()]
        _listExpQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataInput().getExperimentalDataQ()]
        _listExpValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataInput().getExperimentalDataValues()]
        _listDammifFitQ = []
        _listDammifFitValues = []
        _listDammifExpQ = []
        _listDammifExpValues = []

        self.__parceDammifFit(_listDammifExpQ, _listDammifExpValues, _listDammifFitQ, _listDammifFitValues)

        pylab.semilogy(_listExpQ, _listExpValues, linestyle='None', marker='o', markersize=5, label="Experimental Data")
        pylab.semilogy(_listFitQ, _listFitValues, label="GNOM fitting curve")
        #pylab.semilogy(_listDammifExpQ, _listDammifExpValues, linestyle='None', marker='x', markersize=5,  label="Dammif experimental Data")
        pylab.semilogy(_listDammifFitQ, _listDammifFitValues, color='y', label="DAMMIF ab-initio model")
        pylab.xlabel(u"q / \u00c5$^{-1}$")
        pylab.ylabel('I(q)')
        pylab.suptitle("RMax : %3.2f   Fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(), self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
        pylab.legend()
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "gnomFittingResults.png"))
        pylab.clf()

        _listDistributionR = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionR()]
        _listDistributionPr = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionPr()]
        _listDistributionErr = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getDistributionErr()]

        pylab.errorbar(_listDistributionR, _listDistributionPr, yerr=_listDistributionErr)
        pylab.xlabel(u"R / \u00c5")
        pylab.ylabel('P(R)')
        pylab.suptitle("Distance distribution function")
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "distributionPR.png"))
        pylab.clf()

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

        pylab.figure(0, figsize=(10, 8))
        pylab.figure(30, figsize=(10, 5))

        for ref in self.__xsDammifPlugin.iterkeys():

            _tmpNSD = []
            _tmpInd = []
            for tmp in self.__xsDammifPlugin.iterkeys():
                if tmp is not ref:
                    _tmpNSD.append(self.__xsSupcombPlugin[(min([tmp, ref]), max([tmp, ref]))].getDataOutput().getNSD().getValue())
                    if tmp < ref:
                        _tmpInd.append(tmp + _width * (ref - tmp - 1))
                    else:
                        _tmpInd.append(tmp + _width * (ref - tmp))

            _tmpColor = self.__colorsDammif[ref]
            _tmpLegendPos = 0.8 - 0.4 * ref / self.__iNbDammifJobs
            _tmpLabel = os.path.relpath(self.__xsDammifPlugin[ref].getWorkingDirectory(), self.getWorkingDirectory())
            _indLabels.append(_tmpLabel)
            pylab.figure(0)
            pylab.bar(_tmpInd, _tmpNSD, _width, color=_tmpColor, label=_tmpLabel)
            pylab.figtext(0.75, _tmpLegendPos, _tmpLabel, backgroundcolor=_tmpColor, \
                          color='white', weight='roman', size='medium')
            pylab.figure(30)
            pylab.barh([self.__iNbDammifJobs - ref], self.__dammifRefNSD[ref], 0.8, color=_tmpColor)

        pylab.figure(0)
        #pylab.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.3)
        pylab.subplots_adjust(right=0.7, bottom=0.3)
        pylab.ylabel('Normalised Spatial Discrepancy (NSD)')
        pylab.xlabel('DAMMIF Model')
        pylab.title('DAMAVER model alignment results')
        pylab.xticks(_ind, _indLabels, rotation=65)
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "dammifNSDResults.png"))
        pylab.clf()
        pylab.figure(30)
        pylab.axvspan(self.__meanNSD - 2 * self.__varNSD, self.__meanNSD + 2 * self.__varNSD, facecolor='g', alpha=0.3)
        pylab.subplots_adjust(left=0.3, right=0.8)
        pylab.xlabel('Average NSD')
        pylab.ylabel('DAMMIF Model')
        pylab.text(self.__meanNSD, self.__iNbDammifJobs + 1.5, "Model acceptance interval", ha="center", va="bottom", \
                   bbox=dict(boxstyle="round", ec='g', fc='g', alpha=0.3))
        pylab.ylim(0.5, self.__iNbDammifJobs + 1.2)
        pylab.yticks(self.__iNbDammifJobs + 0.4 - arange(self.__iNbDammifJobs), _indLabels)
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "dammifAverageNSD.png"))
        pylab.clf()


    def __outputHTMLSummaryTable(self):
        _pdbFilter = EDPDBFilter()
        pathDamaverFileRaw = self.__edPluginExecDamaver.getDataOutput().getDamaverPdbFile().getPath().getValue()
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

        _gnomResults = '\n'.join(["<p>Optimized value of RMax : %3.2f</p>" % self.__edPluginExecGnom.getDataInput().getRMax().getValue(), \
                                  "<p>Estimated Rg : %3.2f</p>  " % self.__edPluginExecGnom.getDataOutput().getRadiusOfGyration().getValue(), \
                                  "<p>Output fit quality : %1.3f</p>" % self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()])
        _dammifResults = '\n'.join(["<p>RFactor : %1.4f</p>" % self.__edPluginExecDammif.getDataOutput().getRfactor().getValue(), \
                                    "<p>Chi(Sqrt) : %3.3f</p>" % self.__edPluginExecDammif.getDataOutput().getChiSqrt().getValue()])
        _damaverResults = '\n'.join(["<p>Mean NSD : %2.3f</p>" % self.getDataOutput().getMeanNSD().getValue(), \
                                     "<p>Variation of NSD : %2.3f</p>" % self.getDataOutput().getVariationNSD().getValue()])

        if self.__idxDammifBestChiSq is self.__idxDammifBestNSD:
            _dammifModelLink = os.path.join(os.path.relpath(self.__edPluginExecDammif.getWorkingDirectory(), self.getWorkingDirectory()), "dammif-1.pdb")
        else:
            _dammifModelLink = os.path.join(os.path.relpath(self.__xsSupcombPlugin[self.__idxDammifBestChiSq, self.__idxDammifBestNSD].getWorkingDirectory(), self.getWorkingDirectory()), "result.pdb")
        _damaverModelLink = os.path.relpath(pathDamaverFile, self.getWorkingDirectory())
        _dammifModel = '\n'.join(['<script>jmolInitialize("./jmol", true);', \
                                  'jmolApplet(200, "load %s; isosurface saSurface; color orange; spin on");</script>' % _dammifModelLink])
        _damaverModel = '\n'.join(['<script>jmolInitialize("./jmol", true);', \
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
        _htmlCode.append('<h3>Optimized value of RMax : %3.2f</h3>' % self.__edPluginExecGnom.getDataInput().getRMax().getValue())
        _htmlCode.append("<h3>Estimated Rg : %3.2f</h3>" % self.__edPluginExecGnom.getDataOutput().getRadiusOfGyration().getValue())
        _htmlCode.append("<h3>Output fit quality : %1.3f</h3>" % self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue())
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
                _htmlCode.extend(['<tr>', '<td>%3.2f</td>' % self.__xsGnomPlugin[(itr, idx)].getDataInput().getRMax().getValue(), \
                               '<td>%1.3f</td>' % self.__xsGnomPlugin[(itr, idx)].getDataOutput().getFitQuality().getValue(), \
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
        _htmlCode.append("<h3>RFactor : %1.4f   Chi(Sqrt) : %3.3f</h3>" % (self.__edPluginExecDammif.getDataOutput().getRfactor().getValue(), self.__edPluginExecDammif.getDataOutput().getChiSqrt().getValue()))
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
            _htmlCode.extend(['<tr>', '<td>%1.4f</td>' % tmpDammifPlugin.getDataOutput().getRfactor().getValue(), \
                               '<td>%3.3f</td>' % tmpDammifPlugin.getDataOutput().getChiSqrt().getValue()])
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
        pathDamfiltFileRaw = self.__edPluginExecDamfilt.getDataOutput().getOutputPdbFile().getPath().getValue()
        pathDamstartFileRaw = self.__edPluginExecDamstart.getDataOutput().getOutputPdbFile().getPath().getValue()
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
        tmpLines = [ '<hr /><h2>References</h2>', \
                    """<p><b>ATSAS</b> A program suite for small-angle scattering data analysis from biological macromolecules.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.embl-hamburg.de/biosaxs/software.html'}, \
                    """<p><b>GNOM</b> Svergun D.I. (1992) Determination of the regularization parameter
                        in indirect-transform methods using perceptual criteria. <em>J. Appl. Cryst.</em>
                        <strong>25</strong>, 495-503</p>""", \
                    """<p><b>DAMMIF</b> Franke, D. and Svergun, D.I. (2009) DAMMIF, a program for
                         rapid ab-initio shape determination in small-angle scattering. <em>J. Appl. Cryst.</em> <strong>42</strong>, 342-346.</p>""", \
                    """<p><b>SUPCOMB</b> M.Kozin and D.Svergun (2000) Automated matching of high- and low-resolution
                        structural models <em>J. Appl. Cryst.</em> <strong>34</strong>, 33-41.</p>""", \
                    """<p><b>DAMAVER</b> V. V. Volkov and D. I. Svergun (2003). Uniqueness of ab-initio shape
                        determination in small-angle scattering. <em>J. Appl. Cryst.</em> <strong>36</strong>, 860-864.</p>""", \
                    """<p><b>EDNA</b> M.-F. Incardona, G. P. Bourenkov, K. Levik, R. A. Pieritz, A. N. Popov and O. Svensson (2009).
                        EDNA: a framework for plugin-based applications applied to X-ray experiment online data analysis.
                        <em>J. Synchrotron Rad.</em> <strong>16</strong>, 872-879.<a href="%(link)s">%(link)s</a></p>""" % {'link':'http://www.edna-site.org/'}, \
                    """<p><b>Jmol</b> an open-source Java viewer for chemical structures in 3D.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.jmol.org/'}, \
                    """<p><b>Numpy</b> the package for scientific computing in Python
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://numpy.scipy.org/'}, \
                    """<p><b>Matplotlib</b> the package for 2D plotting in Python
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://matplotlib.sourceforge.net/'}, \
                    """<p><b>NeXus</b> a common data format for neutron, x-ray, and muon science.
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://www.nexusformat.org/'}, \
                    """<p><b>h5py</b> a simple Python interface to HDF5
                        <a href="%(link)s">%(link)s</a>""" % {'link':'http://h5py.alfven.org/'}]

        return tmpLines


    def __jsFunctions(self):
        tmpLines = [ \
        '<script>                                                           ', \
        '/* EDNA2html.js                                                    ', \
        '                                                                   ', \
        '   Javascript functions for use in the output of EDNA2html         ', \
        '                                                                   ', \
        '   CVS_id $Id: EDNA2html.js,v 1.3 2010/04/22 09:19:34 pjb93 Exp $  ', \
        ' */                                                                ', \
        '                                                                   ', \
        '// Toggle the display property of a specific element               ', \
        '// Specify the id of an element and its display style              ', \
        '// will be flipped from "none" to "block", or "block" to           ', \
        '// "none" as appropriate                                           ', \
        'function toggleElement(name)                                       ', \
        '{                                                                  ', \
        '    var obj = document.getElementById(name);                       ', \
        '    var state = obj.style.display;                                 ', \
        '    var new_state = "";                                            ', \
        '    if (state == "none") {                                         ', \
        '    new_state = "block";                                           ', \
        '    } else {                                                       ', \
        '    new_state = "none";                                            ', \
        '    }                                                              ', \
        '    obj.style.display = new_state;                                 ', \
        '}                                                                  ', \
        '                                                                   ', \
        '// Toggle the display properties of multiple elements              ', \
        '// Specify a list of element ids to have their display             ', \
        '// style flipped between "none" and "block"                        ', \
        'function toggleElements()                                          ', \
        '{                                                                  ', \
        '    for (var i=0; i < arguments.length; i++) {                     ', \
        '    toggleElement(arguments[i]);                                   ', \
        '    }                                                              ', \
        '}                                                                  ', \
        '</script>                                                          ', \
        '<script src="./jmol/Jmol.js"></script>']
        return '\n'.join(tmpLines)


    def __outputHTMLPipelineResults(self):
        """
        Output pipilene results in HTML format
        """

        htmlLog = open(os.path.join(self.getWorkingDirectory(), "pipelineResults.html"), 'w')
        htmlText = ['<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"', '"http://www.w3.org/TR/html4/strict.dtd"> ', \
                    '<html>', '<head>', '<title>Solution Scattering Pipeline Results</title>', self.__jsFunctions(), '</head>', '<body>']
        htmlText.append('<h1>Summary of Solution Scattering Pipeline Execution</h1>')

        if self.getDataInput().getTitle() is not None:
            htmlText.append('<h1>Data file : %s</h1>' % self.getDataInput().getTitle().getValue())

        htmlText.extend(self.__outputHTMLSummaryTable())
        htmlText.extend(self.__outputHTMLGnomImages())
        htmlText.extend(self.__outputHTMLGnomTables())
        if not self.__bOnlyGnom:
            htmlText.extend(self.__outputHTMLDammifResults())
            htmlText.extend(self.__outputHTMLDamaverResults())
        htmlText.extend(self.__outputHTMLReferences())

        htmlText.append('<hr /></body>')
        htmlLog.write('\n'.join(htmlText))
        htmlLog.close()


    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_3.generateExecutiveSummary")
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

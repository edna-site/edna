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

import os, operator, itertools, matplotlib
matplotlib.use('Agg')

from matplotlib import pylab
from numpy import mean, std, resize

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile
from EDParallelJobLauncher import EDParallelJobLauncher

from XSDataSAS import XSDataInputSolutionScattering
from XSDataSAS import XSDataResultSolutionScattering
from XSDataSAS import XSDataInputGnom
from XSDataSAS import XSDataInputDammif
from XSDataSAS import XSDataInputDamaver

from XSDataSAS import XSDataDouble, XSDataInteger, XSDataString


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
    
class EDPluginControlSolutionScatteringv0_2(EDPluginControl):
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
        self.__strPluginExecDamaver = "EDPluginExecDamaverv0_1"
        
        self.__xsGnomJobs = None
        self.__xsDammifJobs = None
        
        self.__edPluginExecGnom = None
        self.__edPluginExecDammif = None
        self.__edPluginExecDamaver = None

        self.__xsDataExperimentalDataQ = None
        self.__xsDataExperimentalDataValues = None
        self.__xsDataExperimentalDataStdDev = None
        self.__xsDataRMax = None
        self.__xsDataOutput = None

        self.__iNbThreads = None
        self.__iUnit = 1
        self.__strUnit = "ANGSTROM"
        self.__strMode = "Fast"
        self.__bOnlyGnom = False
        self.__bPlotFit = False
        
        self.__rMaxStart = 10.0
        self.__rMaxStop = 200.0
        self.__absTol = 0.1
        self.__absErr = self.__absTol * 10
        self.__rMaxDivide = 10
        
        self.__iNbGnomSeries = None 
        self.__iNbDammifJobs = 10

        self.__xsGnomPlugin = {}
        self.__xsDammifPlugin = {}

        self.__xsDataResultSolutionScattering = XSDataResultSolutionScattering()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

        self.checkRMaxSearchParameters()
        #self.checkUnitParameter()
        self.checkModeParameter()

    def checkRMaxSearchParameters(self):
        if self.getDataInput().getRMaxSearchSettings() is not None:
            if self.getDataInput().getRMaxSearchSettings().getRMaxStart() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_2.setRMaxSerachParameters rMaxStart is missing")
                self.setFailure()
            if self.getDataInput().getRMaxSearchSettings().getRMaxStop() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_2.setRMaxSerachParameters rMaxStop is missing")
                self.setFailure()
            if self.getDataInput().getRMaxSearchSettings().getRMaxAbsTol() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_2.setRMaxSerachParameters rMaxAbsTol is missing")
                self.setFailure()
            if self.getDataInput().getRMaxSearchSettings().getRMaxIntervals() is None:
                EDVerbose.ERROR("EDPluginControlSolutionScatteringv0_2.setRMaxSerachParameters rMaxIntervals is missing")
                self.setFailure()

    def checkModeParameter(self):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.checkModeParameter")
        try:
            if self.getDataInput().getMode().getValue().lower() in ['fast', 'slow']:
                self.__strMode = self.getDataInput().getMode().getValue().lower()
        except Exception:
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
        except Exception:
            EDVerbose.WARNING("Using Angstrom units for q-values by default")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.preProcess")

        xsDataInputSolutionScattering = self.getDataInput()
        self.__xsDataExperimentalDataQ = xsDataInputSolutionScattering.getExperimentalDataQ()
        self.__xsDataExperimentalDataValues = xsDataInputSolutionScattering.getExperimentalDataValues()
        if xsDataInputSolutionScattering.getExperimentalDataStdDev():
            self.__xsDataExperimentalDataStdDev = xsDataInputSolutionScattering.getExperimentalDataStdDev()
            

        if self.getDataInput().getRMaxSearchSettings() is not None:
            self.__rMaxStart = self.getDataInput().getRMaxSearchSettings().getRMaxStart().getValue()
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
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.process")

        #Make series of GNOM runs narrowing down the optimal value of rMax
        ser = 0
        while self.__absErr > self.__absTol:
            
            if (not self.__rMaxDivide):
                xsDataRMax = [XSDataDouble(self.__rMaxStart)]
            else:    
                xsDataRMax = itertools.imap(lambda idx: XSDataDouble(self.__rMaxStart + idx * (self.__rMaxStop - self.__rMaxStart) / self.__rMaxDivide), range(self.__rMaxDivide + 1))
                
            dictDataInputGnom = {}
            for idx, rMax in enumerate(xsDataRMax):
                dictDataInputGnom[(ser,idx)] = XSDataInputGnom()
                dictDataInputGnom[(ser,idx)].setExperimentalDataQ(self.__xsDataExperimentalDataQ)
                dictDataInputGnom[(ser,idx)].setExperimentalDataValues(self.__xsDataExperimentalDataValues)
                if self.__xsDataExperimentalDataStdDev:
                    dictDataInputGnom[(ser,idx)].setExperimentalDataStdDev(self.__xsDataExperimentalDataStdDev)
                dictDataInputGnom[(ser,idx)].setRMax(rMax)
                dictDataInputGnom[(ser,idx)].setAngularScale(XSDataInteger(self.__iUnit))
                dictDataInputGnom[(ser,idx)].setMode(XSDataString(self.__strMode))
            self.__xsGnomJobs = EDParallelJobLauncher(self, self.__strPluginExecGnom, dictDataInputGnom, self.__iNbThreads)
            self.executePluginSynchronous(self.__xsGnomJobs)

            self.__xsGnomPlugin.update(self.__xsGnomJobs.getPluginJobs())
            edPluginGnomOptimal = self.__checkGnomSeriesResults(ser)
            ser += 1

        self.__iNbGnomSeries = ser
        
        # Just rerunning GNOM with optimal parameters to fir it into Control plugin pipeline.
        self.__edPluginExecGnom = self.loadPlugin(self.__strPluginExecGnom, self.__strPluginExecGnom + "-optimal")
        self.__edPluginExecGnom.setDataInput(edPluginGnomOptimal.getDataInput())
        self.__edPluginExecGnom.connectSUCCESS(self.doSuccessExecGnom)
        self.__edPluginExecGnom.connectFAILURE(self.doFailureExecGnom)
        self.executePluginSynchronous(self.__edPluginExecGnom)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.postProcess")


    def doSuccessExecGnom(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doSuccessExecGnom")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doSuccessExecGnom")

        self.__plotRMaxSearchResults()
        
        if not self.__bOnlyGnom:
            self.__xsDataOutput = self.__edPluginExecGnom.getDataOutput().getOutput()
    
            xsDataInputDammif = XSDataInputDammif()
            xsDataInputDammif.setGnomOutputFile(self.__xsDataOutput)
            xsDataInputDammif.setUnit(XSDataString(self.__strUnit))
            xsDataInputDammif.setMode(XSDataString(self.__strMode))
    
            dictDataInputDammif = {}
            for idx in range(self.__iNbDammifJobs):
                dictDataInputDammif[(0,idx)] = xsDataInputDammif
                
            self.__xsDammifJobs = EDParallelJobLauncher(self, self.__strPluginExecDammif, dictDataInputDammif,self.__iNbThreads)
            self.__xsDammifJobs.connectSUCCESS(self.doSuccessExecDammif)
            self.__xsDammifJobs.connectFAILURE(self.doFailureExecDammif)
            self.executePluginSynchronous(self.__xsDammifJobs)

    def doFailureExecGnom(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doFailureExecGnom")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doFailureExecGnom")


    def __checkDammifSeriesResults(self, serInput):
        """
        Find DAMMIF run with best chi-square value
        """
        fitResultDict = dict([((ser, idx), plg.getDataOutput().getChiSqrt().getValue()) for (ser, idx), plg in self.__xsDammifPlugin.items() if ser == serInput])
        fitResultList = sorted(fitResultDict.iteritems(), key=operator.itemgetter(1))
        ((ser, idx_max), _) = fitResultList[0]

        return self.__xsDammifPlugin[(ser, idx_max)]

    def doSuccessExecDammif(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doSuccessExecDammif")
        #self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doSuccessExecDammif")

        self.__xsDammifPlugin.update(self.__xsDammifJobs.getPluginJobs())
                    
        self.__xsDataResultSolutionScattering.setLineProfileFitQuality(self.__edPluginExecGnom.getDataOutput().getFitQuality())
        self.__xsDataResultSolutionScattering.setScatteringFitQ(self.__edPluginExecGnom.getDataOutput().getScatteringFitQ())
        self.__xsDataResultSolutionScattering.setScatteringFitValues(self.__edPluginExecGnom.getDataOutput().getScatteringFitValues())

        self.__edPluginExecDammif = self.__checkDammifSeriesResults(0)

        self.__xsDataResultSolutionScattering.setFitFile(self.__edPluginExecDammif.getDataOutput().getFitFile())
        self.__xsDataResultSolutionScattering.setLogFile(self.__edPluginExecDammif.getDataOutput().getLogFile())
        self.__xsDataResultSolutionScattering.setPdbMoleculeFile(self.__edPluginExecDammif.getDataOutput().getPdbMoleculeFile())
        self.__xsDataResultSolutionScattering.setPdbSolventFile(self.__edPluginExecDammif.getDataOutput().getPdbSolventFile())

        xsDataInputDamaver = XSDataInputDamaver()
        tmpOutputPdbFiles = [tmpXSDammifPlugin.getDataOutput().getPdbMoleculeFile() for (_, _), tmpXSDammifPlugin in self.__xsDammifPlugin.items()]
        xsDataInputDamaver.setPdbInputFiles(tmpOutputPdbFiles)

        self.__edPluginExecDamaver = self.loadPlugin(self.__strPluginExecDamaver)
        self.__edPluginExecDamaver.setDataInput(xsDataInputDamaver)
        self.__edPluginExecDamaver.connectSUCCESS(self.doSuccessExecDamaver)
        self.__edPluginExecDamaver.connectFAILURE(self.doFailureExecDamaver)
        self.executePluginSynchronous(self.__edPluginExecDamaver)

    def doFailureExecDammif(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doFailureExecDammif")
        #self.retrieveFailureMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doFailureExecDammif")

    def doSuccessExecDamaver(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doSuccessExecDamaver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doSuccessExecDamaver")

        self.__xsDataResultSolutionScattering.setMeanNSD(self.__edPluginExecDamaver.getDataOutput().getMeanNSD())
        self.__xsDataResultSolutionScattering.setVariationNSD(self.__edPluginExecDamaver.getDataOutput().getVariationNSD())

        self.setDataOutput(self.__xsDataResultSolutionScattering)


    def doFailureExecDamaver(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.doFailureExecDamaver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSolutionScatteringv0_2.doFailureExecDamaver")
        
        
    #def readGnomDataFile(self, fileName):
    #    """
    #    Initialize pipeline input data structure using GNOM ASCII data file 
    #    """
    #    tmpExperimentalDataQ = []
    #    tmpExperimentalDataValues = []
    #    
    #    dataLines = EDUtilsFile.readFile(fileName).splitlines()[1:]
    #    for line in dataLines:
    #        tmpValue = XSDataDouble()
    #        tmpQ = XSDataDouble()
    #        lineList = line.split()
    #        tmpQ.setValue(float(lineList[0]))
    #        tmpValue.setValue(float(lineList[1]))
    #        tmpExperimentalDataQ.append(tmpQ)
    #        tmpExperimentalDataValues.append(tmpValue)
    #    self.getDataInput().setExperimentalDataQ(tmpExperimentalDataQ)
    #    self.getDataInput().setExperimentalDataValues(tmpExperimentalDataValues)
        
    
    def readGnomNexusDataColumns(self, _fileName, _strNxsQ, _strNxsData, _iNbColumns, _fQMin, _fQMax):
        """
        Initialize pipeline input data structure using Nexus data file.
        """
        import h5py
        tmpExperimentalDataQ = []
        tmpExperimentalDataValues = []
        tmpExperimentalDataStdDev = []
        
        tmpFile = h5py.File(_fileName,'r')
        nxsExperimentalQ = tmpFile[_strNxsQ]
        nxsExperimentalValues = tmpFile[_strNxsData]
        nxsShape = nxsExperimentalValues.shape 
        if len(nxsShape) > 1:
            _iNbColumns = min(_iNbColumns, nxsShape[-2])
        else:
            _iNbColumns = 1
            
        nxsExperimentalValues = resize(nxsExperimentalValues, (_iNbColumns,len(nxsExperimentalQ)))
        
        for (idx, _tmpQ) in enumerate(nxsExperimentalQ[:]):
            if (((_tmpQ > _fQMin) or (_fQMin is None)) and \
                ((_tmpQ < _fQMax) or (_fQMax is None))):

                units = 1
                if self.getDataInput().getAngularUnits() is not None:
                    units = self.getDataInput().getAngularUnits().getValue()
                if units in [2,4]:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ/10.0))
                else:
                    tmpExperimentalDataQ.append(XSDataDouble(_tmpQ))
                    
                _tmpValue = mean(nxsExperimentalValues[:_iNbColumns,idx])                  
                tmpExperimentalDataValues.append(XSDataDouble(_tmpValue))
                if (_iNbColumns > 1):
                    _tmpStdDev = std(nxsExperimentalValues[:_iNbColumns,idx])
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
                    if units in [2,4]:
                        tmpExperimentalDataQ.append(XSDataDouble(_tmpQ/10.0))
                    else:
                        tmpExperimentalDataQ.append(XSDataDouble(_tmpQ))
                        
                    _tmpValue = mean(map(float, lineList[1:_iNbColumns+1]))                  
                    tmpExperimentalDataValues.append(XSDataDouble(_tmpValue))
                    if (_iNbColumns > 1):
                        _tmpStdDev = std(map(float, lineList[1:_iNbColumns+1]))
                        tmpExperimentalDataStdDev.append(XSDataDouble(_tmpStdDev))
                        
        self.getDataInput().setExperimentalDataQ(tmpExperimentalDataQ)
        self.getDataInput().setExperimentalDataValues(tmpExperimentalDataValues)
        if (_iNbColumns > 1):
            self.getDataInput().setExperimentalDataStdDev(tmpExperimentalDataStdDev)
        
    def __outputGnomSeriesResults(self):
        self.addExecutiveSummaryLine("Number of GNOM iterations performed before converging : " + str(self.__iNbGnomSeries))
        for itr in range(self.__iNbGnomSeries):
            self.addExecutiveSummarySeparator()
            self.addExecutiveSummaryLine("Iteration # " + str(itr+1))
            for idx in range(self.__rMaxDivide):
                dirLocation = self.__xsGnomPlugin[(itr,idx)].getWorkingDirectory()
                tmpRMaxInput = "rMax = %3.2f" % self.__xsGnomPlugin[(itr,idx)].getDataInput().getRMax().getValue()
                tmpFitQuality = "fitQuality = " + str(self.__xsGnomPlugin[(itr,idx)].getDataOutput().getFitQuality().getValue())
                tmpStrLine = "\t".join([tmpRMaxInput, tmpFitQuality,dirLocation])
                self.addExecutiveSummaryLine(tmpStrLine)
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Optimized value of RMax = %3.2f" % self.__edPluginExecGnom.getDataInput().getRMax().getValue())
        self.appendExecutiveSummary(self.__edPluginExecGnom)
                
    def __outputDammifJobResults(self):
        self.addExecutiveSummaryLine("Number of DAMMIF jobs run : " + str(self.__iNbDammifJobs))
        for itr in range(self.__iNbDammifJobs):
            dirLocation = self.__xsDammifPlugin[(0,itr)].getWorkingDirectory()
            tmpRFactor = "RFactor = " + str(self.__xsDammifPlugin[(0,itr)].getDataOutput().getRfactor().getValue())
            tmpChiSqrt = "Chi(Sqrt) = " + str(self.__xsDammifPlugin[(0,itr)].getDataOutput().getChiSqrt().getValue())
            tmpStrLine = "\t".join([tmpChiSqrt, tmpRFactor,dirLocation])
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
                rMaxList.append(self.__xsGnomPlugin[(itr,idx)].getDataInput().getRMax().getValue())
                fitQualityList.append(self.__xsGnomPlugin[(itr,idx)].getDataOutput().getFitQuality().getValue())
            
            #pylab.plot(fitQualityList, marker='o', color=cm(1.0*itr/(self.__iNbGnomSeries-1)), markersize=5,  label="Iteration # %d" % itr)
            pylab.figure(self.__iNbGnomSeries+1, figsize=(6,5))
            pylab.plot(rMaxList, fitQualityList, linestyle='None', marker='o', color=cm(1.0*(itr+1)/self.__iNbGnomSeries), markersize=5,  label="Iteration # %d" % itr)
            pylab.figure(itr+1, figsize=(6,5))
            pylab.plot(rMaxList, fitQualityList, linestyle='-', marker='o', markersize=5,  label="Iteration # %d" % itr)
            pylab.xlabel(u"Rmax / \u00c5")
            pylab.ylabel('Fit quality')
            pylab.legend(loc=4)
            pylab.savefig(os.path.join(self.getWorkingDirectory(),"rMaxSearchResults-%d.png" % (itr+1)))
            
        pylab.figure(self.__iNbGnomSeries+1, figsize=(6,5))
        pylab.xlabel(u"Rmax / \u00c5")
        pylab.ylabel('Fit quality')
        pylab.suptitle("Optimized value of RMax : %3.2f   Maximal fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(),self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
        pylab.legend(loc=4)
        pylab.savefig(os.path.join(self.getWorkingDirectory(),"rMaxSearchResults.png"))
        pylab.clf()
        
        
        _listFitQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getScatteringFitQ()]
        _listFitValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataOutput().getScatteringFitValues()]
        _listExpQ = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataInput().getExperimentalDataQ()]
        _listExpValues = [tmp.getValue() for tmp in self.__edPluginExecGnom.getDataInput().getExperimentalDataValues()]
         
        pylab.semilogy(_listExpQ, _listExpValues, linestyle='None', marker='o', markersize=5,  label="Experimental Data")
        pylab.semilogy(_listFitQ, _listFitValues, label="Fitting curve")
        pylab.xlabel(u"q / \u00c5$^{-1}$")
        pylab.ylabel('I(q)')
        pylab.suptitle("RMax : %3.2f   Fit quality : %1.3f" % (self.__edPluginExecGnom.getDataInput().getRMax().getValue(),self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()))
        pylab.legend()
        pylab.savefig(os.path.join(self.getWorkingDirectory(),"gnomFittingResults.png"))
        pylab.clf()
        
        if self.__bPlotFit:
            for gnomJob in self.__xsGnomPlugin.itervalues():
                gnomJob.plotFittingResults()  
            self.__edPluginExecGnom.plotFittingResults()
        
    def __outputHTMLSummaryTable(self):
        _htmlCode = ['<table border="1"  cellpadding=5>']
        _htmlCode.extend(['<tr>','<th><h3>GNOM</h3></th>','<th><h3>DAMMIF</h3></th>','<th><h3>DAMAVER</h3></th>','</tr>'])
        
        _gnomResults = '\n'.join(["<p>Optimized value of RMax : %3.2f</p>" % self.__edPluginExecGnom.getDataInput().getRMax().getValue(), \
                                  "<p>Estimated Rg : %3.2f</p>  " % self.__edPluginExecGnom.getDataOutput().getRadiusOfGyration().getValue(), \
                                  "<p>Output fit quality : %1.3f</p>" % self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue()])
        _dammifResults = '\n'.join(["<p>RFactor : %1.4f</p>"  % self.__edPluginExecDammif.getDataOutput().getRfactor().getValue(), \
                                    "<p>Chi(Sqrt) : %3.3f</p>" % self.__edPluginExecDammif.getDataOutput().getChiSqrt().getValue()])         
        _damaverResults = '\n'.join(["<p>Mean NSD : %2.3f</p>"  % self.__edPluginExecDamaver.getDataOutput().getMeanNSD().getValue(), \
                                     "<p>Variation of NSD : %2.3f</p>" % self.__edPluginExecDamaver.getDataOutput().getVariationNSD().getValue()])
                 
        _htmlCode.extend(['<tr>','<td>%s</td>' % _gnomResults, \
                           '<td>%s</td>' % _dammifResults, \
                           '<td>%s</td>' % _damaverResults,'</tr>'])
        _htmlCode.append('</table>')
        return _htmlCode
    
    def __outputHTMLGnomImages(self):
        _imgRMax = os.path.join(self.getWorkingDirectory(),"rMaxSearchResults.png")
        _imgFit = os.path.join(self.getWorkingDirectory(),"gnomFittingResults.png")
        _headerLines = ['<th><h3>Rmax search results</h3></th>','<th><h3>Experimental data fitting</h3></th>']        
        _imageLines = ['<td><img alt="Rmax search results" src="%s"></td>' % _imgRMax, \
                       '<td><img alt="Experimental data fitting" src="%s"></td>' % _imgFit]
        
        return ['<table>','<tr>'] + _headerLines + ['</tr>','<tr>'] + _imageLines + ['</tr>','</table>']
      
    def __outputHTMLGnomTables(self):
        _htmlCode = ['<hr />']
        _htmlCode.append("<h2>Results of GNOM run</h2>")
        _htmlCode.append('<hr />')
        _htmlCode.append('<h3>Optimized value of RMax : %3.2f</h3>' % self.__edPluginExecGnom.getDataInput().getRMax().getValue())
        _htmlCode.append("<h3>Estimated Rg : %3.2f</h3>" % self.__edPluginExecGnom.getDataOutput().getRadiusOfGyration().getValue())
        _htmlCode.append("<h3>Output fit quality : %1.3f</h3>" % self.__edPluginExecGnom.getDataOutput().getFitQuality().getValue())
        _htmlCode.append('<h4>GNOM output file : <a href="%(link)s">%(link)s</a></h4>' % {'link' : os.path.join(self.__edPluginExecGnom.getWorkingDirectory(), "gnom.out")})
        _htmlCode.append('<hr />')
        _htmlCode.append('<h3>Number of GNOM iterations performed before converging : %d</h3>' % self.__iNbGnomSeries)
        for itr in range(self.__iNbGnomSeries):
            _htmlCode.append("<div id='iteration_%d' class='toggle_folder'>" % (itr+1))
            _htmlCode.append("<div id='iteration_%d_open_view' style='display: none;'>" % (itr+1))
            _htmlCode.append('<span class="control close_control"><a href="javascript://" onclick="toggleElements(\'iteration_%(itr)d_open_view\',\'iteration_%(itr)d_closed_view\');">' % {'itr':(itr+1)})
            _htmlCode.append('<span class="tool_tip" title="Hide table of iteration results">')
            _htmlCode.append('<h3> - Iteration # %d</h3></span></a></span><div>' % (itr+1))
            _tmpImgRMax = os.path.join(self.getWorkingDirectory(),"rMaxSearchResults-%d.png" % (itr+1))
            _htmlCode.append('<img alt="Iteration %d search results" src="%s"/>' % ((itr+1), _tmpImgRMax))
            _htmlCode.append('<table border="1">')
            _htmlCode.extend(['<tr>','<th><h3>Rmax</h3></th>','<th><h3>Fit Quality</h3></th>','<th><h3>Link</h3></th>','</tr>'])        
            for idx in range(self.__rMaxDivide):
                dirLocation = self.__xsGnomPlugin[(itr,idx)].getWorkingDirectory()
                _htmlCode.extend(['<tr>','<td>%3.2f</td>' % self.__xsGnomPlugin[(itr,idx)].getDataInput().getRMax().getValue(), \
                               '<td>%1.3f</td>' % self.__xsGnomPlugin[(itr,idx)].getDataOutput().getFitQuality().getValue(), \
                               '<td><a href="%(link)s">%(link)s</a></td>' % {'link' : dirLocation},'</tr>'])
            _htmlCode.append('</table></div></div>')
            _htmlCode.append("<div id='iteration_%d_closed_view' style='display: block;'>" % (itr+1))
            _htmlCode.append("<span class='control open_control'><a href='javascript://' onclick='toggleElements(\"iteration_%(itr)d_open_view\",\"iteration_%(itr)d_closed_view\");'>" % {'itr':(itr+1)})
            _htmlCode.append("<span class='tool_tip' title='Show all iteration results'>")
            _htmlCode.append(" + Iteration # %d</span></a></span></div></div>" % (itr+1))
        
        _htmlCode.append('<hr />')
        return _htmlCode
        
    def __outputHTMLDammifResults(self):
        _htmlCode = ["<h2>Results of the best DAMMIF run</h2>"]
        _htmlCode.append('<hr />')
        _htmlCode.append("<h3>RFactor : %1.4f   Chi(Sqrt) : %3.3f</h3>" % (self.__edPluginExecDammif.getDataOutput().getRfactor().getValue(),self.__edPluginExecDammif.getDataOutput().getChiSqrt().getValue()))
        _htmlCode.append('<h4>DAMMIF particle model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDammif.getWorkingDirectory(), "dammif-1.pdb")})
        _htmlCode.append('<h4>DAMMIF solvent model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDammif.getWorkingDirectory(), "dammif-0.pdb")})
        _htmlCode.append('<h4>DAMMIF fit file : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDammif.getWorkingDirectory(), "dammif.fit")})
        _htmlCode.append('<h4>DAMMIF log file : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDammif.getWorkingDirectory(), "dammif.log")})
        _htmlCode.append('<hr />')
        _htmlCode.append("<h3>Number of DAMMIF jobs run : %d</h3>" % self.__iNbDammifJobs)
        _htmlCode.append('<table border="1">')
        _htmlCode.extend(['<tr>','<th><h3>RFactor</h3></th>','<th><h3>Chi(Sqrt)</h3></th>','<th><h3>Link</h3></th>','</tr>'])        
        for itr in range(self.__iNbDammifJobs):
            dirLocation = self.__xsDammifPlugin[(0,itr)].getWorkingDirectory()
            _htmlCode.extend(['<tr>','<td>%1.4f</td>' % self.__xsDammifPlugin[(0,itr)].getDataOutput().getRfactor().getValue(), \
                               '<td>%3.3f</td>' % self.__xsDammifPlugin[(0,itr)].getDataOutput().getChiSqrt().getValue(), \
                               '<td><a href="%(link)s">%(link)s</a></td>' % {'link' : dirLocation},'</tr>'])
        _htmlCode.append('</table>')
        _htmlCode.append('<hr />')
        
        
        return _htmlCode
        
    def __outputHTMLDamaverResults(self):
        _htmlCode = ["<h2>Results of model averaging using DAMAVER pipeline</h2>"]
        _htmlCode.append('<hr />')
        _htmlCode.append('<h4>DAMAVER output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDamaver.getWorkingDirectory(), "damaver.pdb")})
        _htmlCode.append('<h4>DAMFILT output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDamaver.getWorkingDirectory(), "damfilt.pdb")})
        _htmlCode.append('<h4>DAMSTART output pdb model : <a href="%(link)s">%(link)s</a></h4>' % {'link': os.path.join(self.__edPluginExecDamaver.getWorkingDirectory(), "damstart.pdb")})
        _htmlCode.extend(['<pre>', '<br /> '.join(self.__edPluginExecDamaver.getListExecutiveSummaryLines()[6:]), '</pre>'])
        _htmlCode.append('<hr />')

        return _htmlCode
    
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
        '</script>                                                           ']
        return '\n'.join(tmpLines)
        
    def __outputHTMLPipelineResults(self):
        """
        Output pipilene results in HTML format
        """
        htmlLog = open(os.path.join(self.getWorkingDirectory(), "pipelineResults.html"), 'w')
        htmlText = ['<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"', '"http://www.w3.org/TR/html4/strict.dtd"> ', \
                    '<html>', '<head>', '<title>Solution Scattering Pipeline Results</title>', self.__jsFunctions(), '</head>', '<body>']
        htmlText.append('<h1>Summary of Solution Scattering Pipeline Execution</h1>')
        
        htmlText.extend(self.__outputHTMLSummaryTable())
        htmlText.extend(self.__outputHTMLGnomImages())
        htmlText.extend(self.__outputHTMLGnomTables())
        if not self.__bOnlyGnom:
            htmlText.extend(self.__outputHTMLDammifResults())
            htmlText.extend(self.__outputHTMLDamaverResults())
        
        htmlText.append('</body>')
        htmlLog.write('\n'.join(htmlText))
        htmlLog.close()
            
         
    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlSolutionScatteringv0_2.generateExecutiveSummary")
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
        
        
        


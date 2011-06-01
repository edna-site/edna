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

import os, h5py

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile

from XSDataIfeffit import XSDataInputXAFSDataProcessing
from XSDataIfeffit import XSDataResultXAFSDataProcessing
from XSDataIfeffit import XSDataInputIfeffit

from XSDataIfeffit import XSDataFloat, XSDataString, XSDataFile


class EDPluginControlXAFSDataProcessingv0_1(EDPluginControl):
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
        self.setXSDataInputClass(XSDataInputXAFSDataProcessing)

        self.__strPluginExecIfeffit = "EDPluginExecIfeffitv0_1"
        self.__strIfeffitScriptName = "script.iff"
        self.__strIfeffitDataName = "tmpXAFS.dat"
        
        self.__edPluginExecIfeffit = None

        self.__xsDataExperimentalDataEnergy = None
        self.__xsDataExperimentalDataLnI0It = None
        
        self.__fRbkg = None

        self.__fftfKmin    = None
        self.__fftfKmax    = None
        self.__fftfDk      = None
        self.__fftfKweight = None

        self.__xsDataResultXAFSDataProcessing = XSDataResultXAFSDataProcessing()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.preProcess")

        xsDataInputXAFSDataProcessing = self.getDataInput()
        self.__xsDataExperimentalDataEnergy = xsDataInputXAFSDataProcessing.getExperimentalDataEnergy()
        self.__xsDataExperimentalDataLnI0It = xsDataInputXAFSDataProcessing.getExperimentalDataLnI0It()
        
        if xsDataInputXAFSDataProcessing.getSplineDataInput() is not None:
            self.__fRbkg = xsDataInputXAFSDataProcessing.getSplineDataInput().getRbkg().getValue()
             
        if xsDataInputXAFSDataProcessing.getFftfDataInput() is not None:
            self.__fftfKmin = xsDataInputXAFSDataProcessing.getFftfDataInput().getKmin().getValue() 
            self.__fftfKmax = xsDataInputXAFSDataProcessing.getFftfDataInput().getKmax().getValue() 
            self.__fftfDk = xsDataInputXAFSDataProcessing.getFftfDataInput().getDk().getValue() 
            self.__fftfKweight = xsDataInputXAFSDataProcessing.getFftfDataInput().getKweight().getValue() 
                       

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.process")

        _xsDataInputIfeffit = XSDataInputIfeffit()
        self.__generateIfeffitInputFile()
        tmpScriptFile = XSDataString(self.__generateIfeffitScript())
        _xsDataInputIfeffit.setScriptFile(XSDataFile(tmpScriptFile))
        
        # Running Ifeffit script.
        self.__edPluginExecIfeffit = self.loadPlugin(self.__strPluginExecIfeffit)
        self.__edPluginExecIfeffit.setDataInput(_xsDataInputIfeffit)
        self.__edPluginExecIfeffit.connectSUCCESS(self.doSuccessExecIfeffit)
        self.__edPluginExecIfeffit.connectFAILURE(self.doFailureExecIfeffit)
        self.__edPluginExecIfeffit.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.postProcess")


    def doSuccessExecIfeffit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.doSuccessExecIfeffit")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlXAFSDataProcessingv0_1.doSuccessExecIfeffit")

        self.setDataOutput(self.__xsDataResultXAFSDataProcessing)


    def doFailureExecIfeffit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.doFailureExecIfeffit")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlXAFSDataProcessingv0_1.doFailureExecIfeffit")
        
        
    def readXAFSNexusData(self, _fileName, _strNxsEnergy, _strNxsLnI0It):
        """
        Initialize pipeline input data structure using Nexus data file.
        """
        tmpExperimentalDataEnergy = []
        tmpExperimentalDataLnI0It = []
        
        tmpFile = h5py.File(_fileName,'r')
        nxsExperimentalEnergy = tmpFile[_strNxsEnergy]
        nxsExperimentalLnI0It = tmpFile[_strNxsLnI0It]
        
        
        for (idx, _tmpEnergy) in enumerate(nxsExperimentalEnergy[:]):
            _tmpLnI0It = nxsExperimentalLnI0It[idx]                  
            tmpExperimentalDataEnergy.append(XSDataFloat(_tmpEnergy))
            tmpExperimentalDataLnI0It.append(XSDataFloat(_tmpLnI0It))
             
        self.getDataInput().setExperimentalDataEnergy(tmpExperimentalDataEnergy)
        self.getDataInput().setExperimentalDataLnI0It(tmpExperimentalDataLnI0It)
        
        
    def __generateIfeffitInputFile(self):
        xsExperimentalDataEnergy = self.getDataInput().getExperimentalDataEnergy()
        xsExperimentalDataLnI0It = self.getDataInput().getExperimentalDataLnI0It()

        strLines = '# energy    ln(I0/It)\n'
        for i, dataEnergy in enumerate(xsExperimentalDataEnergy):
            strLines += ' '.join([str(dataEnergy.getValue()), str(xsExperimentalDataLnI0It[i].getValue())]) + '\n'
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), self.__strIfeffitDataName)
        EDUtilsFile.writeFile(tmpInputFileName, strLines)
        return tmpInputFileName
    
    def __generateSplineCommand(self):
        tmpStr = ['edna.energy','edna.lni0it']
        if self.__fRbkg:
            tmpStr.append('rbkg=%2.3f' % self.__fRbkg)
        tmpCommand = 'spline(%s)' % ','.join(tmpStr)
        return tmpCommand
    
    def __generateFFTFCommand(self):
        dictParameters = {'kmin':self.__fftfKmin, \
                         'kmax':self.__fftfKmax, \
                         'dk':self.__fftfDk, \
                         'kweight':self.__fftfKweight}
        
        tmpStr = ','.join(['%(key)s=%(val)2.3f' % {'key':key,'val':var} \
                           for (key, var) in dictParameters.iteritems() if var])
        
        tmpCommand = 'fftf(edna.chi,%s)' % tmpStr
        return tmpCommand
    
    def __generateIfeffitScript(self):
        strLines = ["read_data(file='%s', group = 'edna', label='energy lni0it')" %  os.path.join(self.getWorkingDirectory(), self.__strIfeffitDataName)]
        strLines.append(self.__generateSplineCommand())
        strLines.append(self.__generateFFTFCommand())
        strLines.extend(["write_data(file=norm.dat, edna.energy, edna.lni0it, edna.pre, edna.norm, edna.bkg)", \
                    "write_data(file=chik.dat, edna.k, edna.chi, edna.win)", \
                    "write_data(file=fftf.dat, edna.r, edna.chir_mag, edna.chir_pha, edna.chir_re, edna.chir_im)", \
                    "save(session.sav)"])
        
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), self.__strIfeffitScriptName)
        EDUtilsFile.writeFile(tmpInputFileName, '\n'.join(strLines))
        return tmpInputFileName
        
    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlXAFSDataProcessingv0_1.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of XAFS data processing pipeline execution:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()
        self.appendExecutiveSummary(self.__edPluginExecIfeffit)
        
        self.verboseScreenExecutiveSummary()
        
        


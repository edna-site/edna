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
from EDPluginParallelXNCFJobLauncher import EDPluginParallelXNCFJobLauncher

from XSDataIfeffit import XSDataInputXAFSDataBatchProcessing
#from XSDataIfeffit import XSDataResultXAFSDataBatchProcessing
from XSDataIfeffit import XSDataInputIfeffit
from XSDataIfeffit import XSDataXAFSExperiment

from XSDataIfeffit import XSDataFloat, XSDataString, XSDataFile


class EDPluginControlXAFSDataBatchProcessingv0_1(EDPluginControl):
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
        self.setXSDataInputClass(XSDataInputXAFSDataBatchProcessing)

        self.__strPluginExecIfeffit = "EDPluginExecIfeffitv0_1"
        
        self.__strIfeffitScriptName = ".iff"
        self.__strIfeffitDataName = ".dat"
        self.__strIfeffitSessionName = ".sav"
        self.__strIfeffitResultNormName = "_norm.dat"
        self.__strIfeffitResultChiName = "_chi.dat"
        self.__strIfeffitResultFftfName = "_fftf.dat"
        
        self.__dictXAFSExperimentalData = {}
        
        self.__xsIfeffitPlugin = {}
        self.__iNbThreads = 10
        
        self.__xsDataExperimentalDataEnergy = None
        self.__xsDataExperimentalDataLnI0It = None
        
        self.__normPre1 = None
        self.__normPre2 = None
        self.__normPost1 = None
        self.__normPost2 = None
        
        self.__fE0 = None
        self.__fRbkg = None
        self.__splKmin = None
        self.__splKmax = None
        self.__splKweight = None
        self.__splKwindow = None

        self.__fftfKmin    = None
        self.__fftfKmax    = None
        self.__fftfDk      = None
        self.__fftfDk1      = None
        self.__fftfDk2      = None
        self.__fftfKweight = None
        self.__fftfKwindow = None

        #self.__xsDataResultXAFSDataBatchProcessing = XSDataResultXAFSDataBatchProcessing()

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.preProcess")

        xsDataInputXAFSDataBatchProcessing = self.getDataInput()
        
        if xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput() is not None:
            self.setPreEdgeParameters(xsDataInputXAFSDataBatchProcessing)
            
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput() is not None:
            self.setSplineParameters(xsDataInputXAFSDataBatchProcessing)
             
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput() is not None:
            self.setFftfParameters(xsDataInputXAFSDataBatchProcessing)
                       
        self.__dictXAFSExperimentalData = dict([(dataset.getLabel().getValue(), dataset) for dataset in xsDataInputXAFSDataBatchProcessing.getXafsExperimentData()])    


    def setPreEdgeParameters(self, xsDataInputXAFSDataBatchProcessing):
        if xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getPre1() is not None:
            self.__normPre1 = xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getPre1().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getPre2() is not None:
            self.__normPre2 = xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getPre2().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getNorm1() is not None:
            self.__normPost1 = xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getNorm1().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getNorm2() is not None:
            self.__normPost2 = xsDataInputXAFSDataBatchProcessing.getPreEdgeDataInput().getNorm2().getValue()
         
                
    def setSplineParameters(self, xsDataInputXAFSDataBatchProcessing):
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getE0() is not None:
            self.__fE0 = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getE0().getValue()
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getRbkg() is not None:
            self.__fRbkg = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getRbkg().getValue()
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKminSpl() is not None:
            self.__splKmin = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKminSpl().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKmaxSpl() is not None:
            self.__splKmax = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKmaxSpl().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKweightSpl() is not None:
            self.__splKweight = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKweightSpl().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKwindow() is not None:
            self.__splKwindow = xsDataInputXAFSDataBatchProcessing.getSplineDataInput().getKwindow().getValue()
         
                
    def setFftfParameters(self, xsDataInputXAFSDataBatchProcessing):
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKmin() is not None:
            self.__fftfKmin = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKmin().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKmax() is not None:
            self.__fftfKmax = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKmax().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk() is not None:
            self.__fftfDk = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk1() is not None:
            self.__fftfDk1 = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk1().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk2() is not None:
            self.__fftfDk2 = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getDk2().getValue() 
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKweight() is not None:
            self.__fftfKweight = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKweight().getValue()
        if xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKwindow() is not None:
            self.__fftfKwindow = xsDataInputXAFSDataBatchProcessing.getFftfDataInput().getKwindow().getValue()
         
                
    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.process")

        _dictDataInputIfeffit = {}
        for (label, dataset) in sorted(self.__dictXAFSExperimentalData.iteritems(), key=lambda tmpVal: str.lower(str(tmpVal[0]))):
            self.__generateIfeffitInputFile(dataset)
            tmpScriptFile = XSDataString(self.__generateIfeffitScript(dataset))
            
            _dictDataInputIfeffit[label] = XSDataInputIfeffit()
            _dictDataInputIfeffit[label].setScriptFile(XSDataFile(tmpScriptFile))

        _xsIfeffitJobs = EDPluginParallelXNCFJobLauncher(self, self.__strPluginExecIfeffit, _dictDataInputIfeffit, self.__iNbThreads)
        _xsIfeffitJobs.connectSUCCESS(self.doSuccessExecIfeffit)
        _xsIfeffitJobs.connectFAILURE(self.doFailureExecIfeffit)
        _xsIfeffitJobs.run()
        self.__xsIfeffitPlugin.update(_xsIfeffitJobs.getPluginJobs())


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.postProcess")
        
        #self.parseIfeffitChiFiles()
        #self.parseIfeffitFftfFiles()
        nxsFileName = self.returnResultsFilename()
        f = h5py.File(os.path.join(self.getWorkingDirectory(), nxsFileName), 'w')
        dEntry = f.create_group("entry1")
        dEntry.attrs["NX_class"] = "NXentry"
        
        _normDatasets = {1 : 'lni0it', 2 : 'pre', 3 : 'norm', 4 : 'bkg'}
        self.parseIfeffitFiles(f, self.__strIfeffitResultNormName, _normDatasets, 'norm', 'energy')
        
        _chiDatasets = {1 : 'chi', 2 : 'win'}
        self.parseIfeffitFiles(f, self.__strIfeffitResultChiName, _chiDatasets, 'chi', 'K')
        
        _fftfDatasets = {1 : 'chir_mag', 2 : 'chir_pha', 3 : 'chir_re', 4 : 'chir_im'}
        self.parseIfeffitFiles(f, self.__strIfeffitResultFftfName, _fftfDatasets, 'fftf', 'R')
        f.close()


    def doSuccessExecIfeffit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.doSuccessExecIfeffit")
        #self.retrieveSuccessMessages(_edPlugin, "EDPluginControlXAFSDataBatchProcessingv0_1.doSuccessExecIfeffit")

        #self.setDataOutput(self.__xsDataResultXAFSDataBatchProcessing)


    def doFailureExecIfeffit(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.doFailureExecIfeffit")
        #self.retrieveFailureMessages(_edPlugin, "EDPluginControlXAFSDataBatchProcessingv0_1.doFailureExecIfeffit")
        
        
    def readXAFSNexusFiles(self, _fileNames, _strNxsEnergy, _strNxsLnI0It, _strNxsScanIndex):
        """
        Initialize pipeline input data structure using Nexus data files.
        """
        listDataXAFSExperiment = []
        
        for _fileName in _fileNames:
            xsDataXAFSExperiment = XSDataXAFSExperiment()
            tmpExperimentalDataEnergy = []
            tmpExperimentalDataLnI0It = []
        
            tmpFile = h5py.File(_fileName,'r')
            nxsExperimentalEnergy = tmpFile[_strNxsEnergy]
            nxsExperimentalLnI0It = tmpFile[_strNxsLnI0It]
            nxsScanIndex =  str(tmpFile[_strNxsScanIndex][0])
        
        
            for (idx, _tmpEnergy) in enumerate(nxsExperimentalEnergy[:]):
                _tmpLnI0It = nxsExperimentalLnI0It[idx]                  
                tmpExperimentalDataEnergy.append(XSDataFloat(_tmpEnergy))
                tmpExperimentalDataLnI0It.append(XSDataFloat(_tmpLnI0It))
                
            xsDataXAFSExperiment.setLabel(XSDataString(''.join(os.path.split(_fileName)[1].split('.')[:-1])))
            #xsDataXAFSExperiment.setLabel(XSDataString(nxsScanIndex))
            xsDataXAFSExperiment.setExperimentalDataEnergy(tmpExperimentalDataEnergy)
            xsDataXAFSExperiment.setExperimentalDataLnI0It(tmpExperimentalDataLnI0It)
            listDataXAFSExperiment.append(xsDataXAFSExperiment)
             
        self.getDataInput().setXafsExperimentData(listDataXAFSExperiment)       

        
    def returnResultsFilename(self):
        return ''.join(['results_', str(self.getId()), '.nxs'])

    
    def __generateIfeffitInputFile(self, dataset):
        _xsExperimentalDataEnergy = dataset.getExperimentalDataEnergy()
        _xsExperimentalDataLnI0It = dataset.getExperimentalDataLnI0It()
        _label = dataset.getLabel()

        strLines = '# energy    ln(I0/It)\n'
        for i, dataEnergy in enumerate(_xsExperimentalDataEnergy):
            strLines += ' '.join([str(dataEnergy.getValue()), str(_xsExperimentalDataLnI0It[i].getValue())]) + '\n'
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), _label.getValue()+self.__strIfeffitDataName)
        EDUtilsFile.writeFile(tmpInputFileName, strLines)
        return tmpInputFileName
    
    def __generateSplineCommand(self, _group):
        tmpStr = ['%s.energy' % _group,'%s.lni0it' % _group]
        
        dictParameters = {'pre1':self.__normPre1, \
                          'pre2':self.__normPre2, \
                          'norm1':self.__normPost1, \
                          'norm2':self.__normPost2, \
                          'e0':self.__fE0, \
                          'rbkg':self.__fRbkg, \
                          'kmin':self.__splKmin, \
                          'kmax':self.__splKmax, \
                          'kweight':self.__splKweight}
            
        tmpStr.append(','.join(['%(key)s=%(val)2.3f' % {'key':key,'val':var} \
                           for (key, var) in dictParameters.iteritems() if var is not None]))
        
        if self.__splKwindow is not None:
            tmpStr.append('kwindow=%s' % self.__splKwindow)
        
        tmpCommand = 'spline(%s)' % ','.join(tmpStr)
        return tmpCommand

    
    def __generateFFTFCommand(self, _group):
        tmpStr = ['%s.chi' % _group]
        dictParameters = {'kmin':self.__fftfKmin, \
                          'kmax':self.__fftfKmax, \
                          'dk':self.__fftfDk, \
                          'dk1':self.__fftfDk1, \
                          'dk2':self.__fftfDk2, \
                          'kweight':self.__fftfKweight}
        
        tmpStr.append(','.join(['%(key)s=%(val)2.3f' % {'key':key,'val':var} \
                           for (key, var) in dictParameters.iteritems() if var]))
        
        if self.__fftfKwindow is not None:
            tmpStr.append('kwindow=%s' % self.__fftfKwindow)
        
        tmpCommand = 'fftf(%s)' % ','.join(tmpStr)
        return tmpCommand

    
    def __generateIfeffitScript(self, dataset):
        _label = dataset.getLabel().getValue()
        
        strLines = ["read_data(file='%(file)s', group = '%(group)s', label='energy lni0it')" % \
                    {'file':os.path.join(self.getWorkingDirectory(), _label+self.__strIfeffitDataName), 'group':_label}]
        strLines.append(self.__generateSplineCommand(_label))
        strLines.append(self.__generateFFTFCommand(_label))
        strLines.extend(["write_data(file=%(file)s, %(group)s.energy, %(group)s.lni0it, %(group)s.pre, %(group)s.norm, %(group)s.bkg)" % \
                            {'file':(_label+self.__strIfeffitResultNormName), 'group':_label}, \
                         "write_data(file=%(file)s, %(group)s.k, %(group)s.chi, %(group)s.win)" % \
                            {'file':(_label+self.__strIfeffitResultChiName), 'group':_label}, \
                         "write_data(file=%(file)s, %(group)s.r, %(group)s.chir_mag, %(group)s.chir_pha, %(group)s.chir_re, %(group)s.chir_im)" % \
                            {'file':(_label+self.__strIfeffitResultFftfName), 'group':_label}, \
                         "save(%s)" % (_label+self.__strIfeffitSessionName)])
        
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), _label+self.__strIfeffitScriptName)
        EDUtilsFile.writeFile(tmpInputFileName, '\n'.join(strLines))
        return tmpInputFileName
        
    def parseIfeffitFiles(self, f, strIfeffitResultName, dictDatasets, _groupLabel, _xLabel):
        dataLabels = []
        xResults = []
        yResults = []
        for (idx,label) in enumerate(sorted(self.__xsIfeffitPlugin.iterkeys())):
            dataLabels.append(label)
            yResults.append({})
            logLines = EDUtilsFile.readFile(os.path.join(self.__xsIfeffitPlugin[label].getWorkingDirectory(), \
                                                         label+strIfeffitResultName)).split('\n')[4:]
            xResults.append([float(dataLine.split()[0]) for dataLine in logLines if dataLine])
            for (col, param) in dictDatasets.iteritems():
                yResults[idx][param] = [float(dataLine.split()[col]) for dataLine in logLines if dataLine]
            
        _lenData = min([len(tmp) for tmp in xResults]) 
        dEntry = f['/entry1']
        dProcessing = dEntry.create_group(_groupLabel)
        dProcessing.attrs["NX_class"] = "NXdata"
        dx = dProcessing.create_dataset(_xLabel, (_lenData,), '=f8')
        dx.attrs["target"] = "/".join(['','entry1',_groupLabel,_xLabel])
        dx.attrs["axis"] = 2
        dx.attrs["primary"] = 1
        dx[:] = xResults[0][:_lenData] 
        
        #str_type = h5py.new_vlen(str)
        #dz = dProcessing.create_dataset('dataLabels', (len(dataLabels),), str_type)
        dz = dProcessing.create_dataset('scanID', (len(dataLabels),), "i")
        dz.attrs["target"] = "/".join(['','entry1',_groupLabel,'scanID'])
        dz.attrs["axis"] = 1
        dz.attrs["primary"] = 2
        dz[:] = [int(tmpLabel.split('_')[-1]) for tmpLabel in dataLabels]
        
        for tmpName in dictDatasets.itervalues():
            tmpLines = ['  '.join(['#',_xLabel,''] + dataLabels)]
            for idx in range(_lenData):
                tmpLines.append(str(xResults[0][idx]) + '  ' + '  '.join([str(yResults[idxDataLabel][tmpName][idx]) for idxDataLabel in range(len(dataLabels))]))
                
            EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), ''.join(['results_',tmpName,'.dat'])), '\n'.join(tmpLines))
        
        
            #dTmp = dProcessing.create_dataset(tmpName, (_lenData,len(dataLabels)), '=f8')
            #dTmp.attrs["target"] = "/".join(['','entry1',_groupLabel,tmpName])
            #for idxDataLabel in  range(len(dataLabels)):
            #    dTmp[:,idxDataLabel] = yResults[idxDataLabel][tmpName][:_lenData]
                
            dTmp = dProcessing.create_dataset(tmpName, (len(dataLabels),_lenData), '=f8')
            dTmp.attrs["target"] = "/".join(['','entry1',_groupLabel,tmpName])
            dTmp.attrs["signal"] = 1
            dTmp.attrs["axes"] = ':'.join([_xLabel,"dataLabels"])
            

            for idxDataLabel in  range(len(dataLabels)):
                dTmp[idxDataLabel,:] = yResults[idxDataLabel][tmpName][:_lenData]
        
    #def parseIfeffitChiFiles(self):
    #    chiLabels = []
    #    chiResults = []
    #    for (idx,label) in enumerate(self.__xsIfeffitPlugin.iterkeys()):
    #        logLines = EDUtilsFile.readFile(os.path.join(self.__xsIfeffitPlugin[label].getWorkingDirectory(), \
    #                                                     label+self.__strIfeffitResultChiName)).split('\n')[4:]
    #        if idx == 0:
    #            kResults = [float(dataLine.split()[0]) for dataLine in logLines if dataLine]
    #        tmpChiResults = [float(dataLine.split()[1]) for dataLine in logLines if dataLine]
    #        chiLabels.append(label)
    #        chiResults.append(tmpChiResults)
    #        
    #    tmpLines = ['#  k  ' + '  '.join(chiLabels)]
    #    _lenData = min([len(chiResults[idxLabel]) for idxLabel in range(len(chiLabels))])
    #    for idxK in range(_lenData):
    #        tmpLines.append(str(kResults[idxK]) + '  ' + '  '.join([str(chiResults[idxLabel][idxK]) for idxLabel in range(len(chiLabels))]))
    #        
    #    EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), 'resultsChiK.dat'), '\n'.join(tmpLines))
    #    
    #    f = h5py.File(os.path.join(self.getWorkingDirectory(), 'results.nxs'), 'w')
    #    dEntry = f.create_group("entry1")
    #    dEntry.attrs["NX_class"] = "NXentry"
    #    dProcessing = dEntry.create_group("chi_k")
    #    dProcessing.attrs["NX_class"] = "NXdata"
    #    
    #    dK = dProcessing.create_dataset("K", (_lenData,), '=f8')
    #    dK.attrs["target"] = "/entry1/chi_k/K"
    #    dK.attrs["axis"] = 1
    #    dK[:] = kResults[:_lenData] 
    #    
    #    dChi = dProcessing.create_dataset("Chi", (_lenData,len(chiLabels)), '=f8')
    #    dChi.attrs["target"] = "/entry1/chi_k/Chi"
    #    for idxLabel in  range(len(chiLabels)):
    #        dChi[:,idxLabel] = chiResults[idxLabel][:_lenData]
    #        
    #    #dChiData = []
    #    #for idxLabel in range(len(chiLabels)):
    #    #    _label = chiLabels[idxLabel]
    #    #    dChiData.append(dProcessing.create_dataset(_label, (_lenData,), '=f8'))
    #    #    dChiData[idxLabel].attrs["target"] = "/entry1/process1/Chi" + str(idxLabel)
    #    #    dChiData[idxLabel][:] = chiResults[idxLabel][:_lenData]
    #    f.close()
    #
    #def parseIfeffitFftfFiles(self):
    #    fftfLabels = []
    #    rMagResults = []
    #    rPhaResults = []
    #    rReResults = []
    #    rImResults = []
    #    for (idx,label) in enumerate(self.__xsIfeffitPlugin.iterkeys()):
    #        logLines = EDUtilsFile.readFile(os.path.join(self.__xsIfeffitPlugin[label].getWorkingDirectory(), \
    #                                                     label+self.__strIfeffitResultFftfName)).split('\n')[4:]
    #        if idx == 0:
    #            rResults = [float(dataLine.split()[0]) for dataLine in logLines if dataLine]
    #        tmpRMagResults = [float(dataLine.split()[1]) for dataLine in logLines if dataLine]
    #        tmpRPhaResults = [float(dataLine.split()[2]) for dataLine in logLines if dataLine]
    #        tmpRReResults = [float(dataLine.split()[3]) for dataLine in logLines if dataLine]
    #        tmpRImResults = [float(dataLine.split()[4]) for dataLine in logLines if dataLine]
    #        fftfLabels.append(label)
    #        rMagResults.append(tmpRMagResults)
    #        rPhaResults.append(tmpRPhaResults)
    #        rReResults.append(tmpRReResults)
    #        rImResults.append(tmpRImResults)
    #        
    #    _lenData = len(rResults)
    #    f = h5py.File(os.path.join(self.getWorkingDirectory(), 'results.nxs'), 'r+')
    #    dEntry = f['/entry1']
    #    dProcessing = dEntry.create_group("fftf")
    #    dProcessing.attrs["NX_class"] = "NXdata"
    #    dR = dProcessing.create_dataset("R", (_lenData,), '=f8')
    #    dR.attrs["target"] = "/entry1/fftf/R"
    #    dR.attrs["axis"] = 1
    #    dR[:] = rResults[:] 
    #    
    #    dictDatasets = {'results_rMag.dat' : rMagResults, 'results_rPha.dat' : rPhaResults, 'results_rRe.dat' : rReResults, 'results_rIm.dat' : rImResults}
    #    for (tmpName, tmpResults) in dictDatasets.iteritems():
    #        tmpLines = ['#  R  ' + '  '.join(fftfLabels)]
    #        for idxR in range(_lenData):
    #            tmpLines.append(str(rResults[idxR]) + '  ' + '  '.join([str(tmpResults[idxLabel][idxR]) for idxLabel in range(len(fftfLabels))]))
    #            
    #        EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), tmpName), '\n'.join(tmpLines))
    #    
    #    
    #        dTmp = dProcessing.create_dataset(tmpName, (_lenData,len(fftfLabels)), '=f8')
    #        dTmp.attrs["target"] = "/entry1/fftf/"+tmpName
    #        for idxLabel in  range(len(fftfLabels)):
    #            dTmp[:,idxLabel] = tmpResults[idxLabel][:_lenData]
    #        
    #    f.close()
        
    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlXAFSDataBatchProcessingv0_1.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of XAFS data processing pipeline execution:")
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation failure! Error messages: ")
        self.addExecutiveSummarySeparator()

        for _edPluginExecIfeffit in self.__xsIfeffitPlugin.itervalues():
            self.appendExecutiveSummary(_edPluginExecIfeffit)
        
        self.verboseScreenExecutiveSummary()
        
        


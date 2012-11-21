#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source
#
#    Principal author:        Irakli Sikharulidze
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

__author__="Irakli Sikharulidze"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source"

import operator, copy
from itertools import imap
from math import fabs, exp

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDParallelJobLauncher")
from EDParallelJobLauncher import EDParallelJobLauncher

from XSDataAbsCalc import XSDataInputAbsorption
from XSDataAbsCalc import XSDataResultAbsorption
from XSDataAbsCalc import XSDataInputAbsCalc
from XSDataAbsCalc import XSDataResultAbsCalc

from XSDataAbsCalc import XSDataFloat

class EDPluginControlAbsorptionv0_1( EDPluginControl ):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """
    
    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputAbsorption)
        self.__strPluginExecAbsCalc = "EDPluginExecAbsCalcv0_1"
        
        self.__fracStart = 0.0
        self.__fracStop = 100.0
        self.__absTol = 0.01
        self.__absErr = self.__absTol * 10
        self.__fracDivide = 100
        
        self.__fracScale = None 
        
        self.__refAbsCalc = None
        self.__deltaMuT = None
        
        self.__iNbThreads = 1
                        
        self.__edPluginRefSample = None
        self.__edPluginFinalAbsCalc = None
        self.__xsDataInputAbsorption = None
        
        self.__xsAbsCalcPlugin = {}


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlAbsorptionv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlAbsorptionv0_1.preProcess")
        
        self.__xsDataInputAbsorption = self.getDataInput()
        
        self.__refAbsCalc = self.__xsDataInputAbsorption.getAbsCalcReference()
        self.__deltaMuT = self.__xsDataInputAbsorption.getDeltaMuT().getValue()
        
        self.__fracScale = 1.0/reduce(operator.add, [cmp.getFraction().getValue() for cmp in self.__refAbsCalc.getCompoundList()])
        

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlAbsorptionv0_1.process")
        
        _refSample = copy.deepcopy(self.__refAbsCalc)
        
        for comp in _refSample.getCompoundList():
            _tmpFrac = comp.getFraction().getValue() 
            comp.setFraction(XSDataFloat(100.0 * self.__fracScale * _tmpFrac))
            
        _refSample.getBuffer().setFraction(XSDataFloat(0.0))
        
        _refSample.setTransAfterEdge(XSDataFloat(self.__deltaMuT))
            
        self.__edPluginRefSample = self.loadPlugin(self.__strPluginExecAbsCalc)
        self.__edPluginRefSample.setDataInput(_refSample)
        self.__edPluginRefSample.connectSUCCESS(self.doSuccessRefSample)
        #_edPluginRefSample.connectFAILURE(self.doFailureRefSample)
        self.executePluginSynchronous(self.__edPluginRefSample)
        

    def doSuccessRefSample(self, _edPlugin):
        _xsDataResultRefSample = self.__edPluginRefSample.getDataOutput()
        
        _thicknessRefSample = _xsDataResultRefSample.getThicknessDisk().getValue()
        _thicknessRequired = self.__refAbsCalc.getTransAfterEdge().getValue()
        
        if _thicknessRefSample > _thicknessRequired:
            print "Sample thickness insufficient!"
        else:
            cycles = 0
            
            self.__fracStop = min(exp(self.__deltaMuT) * 100.0 * _thicknessRefSample / _thicknessRequired, 100.0)
            while (self.__absErr > self.__absTol) and (cycles < 5):
                
                if (not self.__fracDivide):
                    xsDataFractions = [XSDataFloat(self.__fracStart)]
                else:    
                    xsDataFractions = imap(lambda idx: XSDataFloat(self.__fracStart + idx * (self.__fracStop - self.__fracStart) / self.__fracDivide), range(self.__fracDivide + 1))
                    
                dictDataInputAbsCalc = {}
                for idx, frac in enumerate(xsDataFractions):
                    dictDataInputAbsCalc[frac] = copy.deepcopy(self.__refAbsCalc)
                    for comp in dictDataInputAbsCalc[frac].getCompoundList():
                        _tmpFrac = comp.getFraction().getValue() 
                        comp.setFraction(XSDataFloat(frac.getValue() * self.__fracScale * _tmpFrac))
                        
                    dictDataInputAbsCalc[frac].getBuffer().setFraction(XSDataFloat(100.0 - frac.getValue()))
        
                self.__xsAbsCalcJobs = EDParallelJobLauncher(self, self.__strPluginExecAbsCalc, dictDataInputAbsCalc, self.__iNbThreads)
                self.executePluginSynchronous(self.__xsAbsCalcJobs)
            
                self.__xsAbsCalcPlugin = self.__xsAbsCalcJobs.getPluginJobs()
                _edPluginAbsCalcSolution = self.__checkAbsCalcSeriesResults()
                cycles += 1
            
            self.__edPluginFinalAbsCalc = self.loadPlugin(self.__strPluginExecAbsCalc, self.__strPluginExecAbsCalc + '-final')
            self.__edPluginFinalAbsCalc.setDataInput(_edPluginAbsCalcSolution.getDataInput())
            self.executePluginSynchronous(self.__edPluginFinalAbsCalc)
    
            
    def __checkAbsCalcSeriesResults(self):
        
        fracResultDict = {}
        for frac, plg in self.__xsAbsCalcPlugin.items():
            tmpTransBeforeEdge = plg.getDataOutput().getTransBeforeEdge().getValue()
            tmpTransAfterEdge = plg.getDataOutput().getTransAfterEdge().getValue()
            
            if (tmpTransAfterEdge - tmpTransBeforeEdge) > 0.1 * self.__deltaMuT :
                fracResultDict[frac] = fabs(tmpTransAfterEdge - tmpTransBeforeEdge - self.__deltaMuT)
            
        fracResultList = sorted(fracResultDict.iteritems(), key=operator.itemgetter(1))     
        
        _fracSolution = fracResultList[0][0]
        _tmpFracStart = min(fracResultList[1][0].getValue(), fracResultList[2][0].getValue()) 
        _tmpFracStop = max(fracResultList[1][0].getValue(), fracResultList[2][0].getValue()) 

        # Find rMax values bracketing the best rMax result
        self.__fracStart = max(self.__fracStart, _tmpFracStart)
        self.__fracStop = min(self.__fracStop, _tmpFracStop)
        self.__absErr = fracResultList[0][1]
        return self.__xsAbsCalcPlugin[_fracSolution]
    
    
    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlAbsorptionv0_1.postProcess")
        # Create some output data
        xsDataResult = XSDataResultAbsorption()
        self.setDataOutput(xsDataResult)
    
        
    def generateExecutiveSummary(self, __edPlugin=None):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlAbsorptionv0_1.generateExecutiveSummary")
        
        self.appendExecutiveSummary(self.__edPluginFinalAbsCalc)
        

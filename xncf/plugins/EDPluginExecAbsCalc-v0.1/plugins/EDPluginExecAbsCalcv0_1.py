#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source
#
#    Principal author:       Irakli Sikharulidze
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

import os.path, shutil

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration
from EDUtilsFile import EDUtilsFile

from XSDataAbsCalc import XSDataInputAbsCalc
from XSDataAbsCalc import XSDataResultAbsCalc
from XSDataAbsCalc import XSDataFloat

class EDPluginExecAbsCalcv0_1(EDPluginExecProcessScript ):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__(self ):
        """
        """
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputAbsCalc)
        self.__xsDataResult     = None        
        
        self.__iNumCompounds    = None;
        self.__lCompounds       = []
        self.__tBuffer          = {}
        self.__strEdge          = None
        self.__fTransAfterEdge  = None
        self.__fDiameterDisk    = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecAbsCalcv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")
        self.checkAbsTable()
        
        self.__iNumCompounds = int(self.getDataInput().getNumCompounds().getValue())
        
        for _itemCompound in self.getDataInput().getCompoundList():
            _tmpCompound = {}
            _tmpCompound['formula'] = _itemCompound.getFormula().getValue() 
            _tmpCompound['fraction'] = _itemCompound.getFraction().getValue() 
            _tmpCompound['density'] = _itemCompound.getDensity().getValue() 
            self.__lCompounds.append(_tmpCompound)
            
        self.__tBuffer['formula'] = self.getDataInput().getBuffer().getFormula().getValue() 
        self.__tBuffer['density'] = self.getDataInput().getBuffer().getDensity().getValue()
        
        self.__strEdge = self.getDataInput().getEdge().getValue() 
        self.__fTransAfterEdge = float(self.getDataInput().getTransAfterEdge().getValue()) 
        self.__fDiameterDisk = float(self.getDataInput().getDiameterDisk().getValue()) 

        
    def checkAbsTable(self):
        _pluginConfiguration = self.getConfiguration()
        _strAbsTable = EDConfiguration.getStringParamValue(_pluginConfiguration, 'absTable')
        if os.path.isfile(_strAbsTable):
            shutil.copy(_strAbsTable, self.getWorkingDirectory())
        else:
            EDVerbose.ERROR("EDPluginExecAbsCalcv0_1.checkAbsTable Couldn't find abstable file")
            self.setFailure()

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecAbsCalcv0_1.preProcess")
        
        self.generateAbsCalcScript()
        
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecAbsCalcv0_1.process")

        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecAbsCalcv0_1.postProcess")
        # Create some output data
        self.__xsDataResult = XSDataResultAbsCalc()
        
        self.parseAbsCalcOutputFile()
        
        self.setDataOutput(self.__xsDataResult)
    
    def generateAbsCalcScript(self):
        EDVerbose.DEBUG("*** EDPluginExecGnomv0_1.generateGnomScript")
        self.setScriptCommandline("")
        
        commandList = ['1', '1', str(self.__iNumCompounds), '1']
        map(commandList.extend, [[tmp['formula'], str(tmp['fraction']), str(tmp['density'])] for tmp in self.__lCompounds])
        commandList.extend([self.__tBuffer['formula'], str(self.__tBuffer['density'])])
        commandList.extend([self.__strEdge, str(self.__fTransAfterEdge), str(self.__fDiameterDisk), '1'])
        
        self.addListCommandExecution('\n'.join(commandList))

    def parseAbsCalcOutputFile(self):
        _weights            = {}
        _tmpDensitySample   = None
        _tmpTransBeforeEdge = None
        _tmpTransAfterEdge  = None
        _tmpDiskThickness   = None
        _tmpDiskRadius      = None

        logFile = EDUtilsFile.readFile(os.path.join(self.getWorkingDirectory(), "abs.out"))
        logLines = logFile.splitlines()
        
        for line in logLines:
            listLine = [tmp for tmp in line.split(' ') if tmp]
            
            if tuple(listLine[0:2]) == ('SAMPLE', 'DENSITY'):
                _tmpDensitySample = float(listLine[-1])
                
            if tuple(listLine[0:2]) == ('WEIGHT', 'OF'):
                _weights[' '.join(listLine[2:-3])] = float(listLine[-1])
                
            if tuple(listLine[0:3]) == ('TRANSMISSION', 'BEFORE', 'EDGE'):
                try:
                    _tmpTransBeforeEdge = float(listLine[-1])
                except Exception:
                    _tmpTransBeforeEdge = -1
                
            if tuple(listLine[0:3]) == ('TRANSMISSION', 'AFTER', 'EDGE'):
                try:
                    _tmpTransAfterEdge = float(listLine[-1])
                except Exception:
                    _tmpTransAfterEdge = -1
            if tuple(listLine[0:2]) == ('DISC', 'THICKNESS'):
                _tmpDiskThickness = float(listLine[-1][1:-1])
                
            if tuple(listLine[0:2]) == ('DISC', 'RADIUS'):
                _tmpDiskRadius = float(listLine[-1])
                
        
        _tmpCompounds = self.getDataInput().getCompoundList()
        for _tmpCompound in _tmpCompounds:
            _tmpCompound.setWeight(XSDataFloat(_weights[str(_tmpCompound.getFormula().getValue()).upper()]))
        self.__xsDataResult.setCompoundList(_tmpCompounds)
            
        _tmpBuffer = self.getDataInput().getBuffer()
        _tmpBuffer.setWeight(XSDataFloat(_weights[_tmpBuffer.getFormula().getValue()]))
        self.__xsDataResult.setBuffer(_tmpBuffer)
        
        self.__xsDataResult.setDensitySample(XSDataFloat(_tmpDensitySample))
        self.__xsDataResult.setWeightSample(XSDataFloat(_weights['SAMPLE']))
        self.__xsDataResult.setTransBeforeEdge(XSDataFloat(_tmpTransBeforeEdge))
        self.__xsDataResult.setTransAfterEdge(XSDataFloat(_tmpTransAfterEdge))
        self.__xsDataResult.setThicknessDisk(XSDataFloat(_tmpDiskThickness))
        self.__xsDataResult.setRadiusDisk(XSDataFloat(_tmpDiskRadius))

                
    def generateExecutiveSummary(self,__edPlugin=None):
        
        abscalcLog = open(os.path.join(self.getWorkingDirectory(), "abs.out"))
        for line in abscalcLog:
            self.addExecutiveSummaryLine(line)

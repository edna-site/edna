#
#    Project: DIMPLE
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source and CCP4
#
#    Principal authors: Graeme Winter (graeme.winter@diamond.ac.uk)
#                       Ronan Keegan (ronan.keegan@stfc.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the Lesser GNU General Public License as published by
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

__author__= ['Graeme Winter', 'Ronan Keegan']
__license__ = 'LGPLv3+'
__copyright__ = '2010 Diamond Light Source, CCP4'

import os

from EDImportLib import EDVerbose

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4DataInputCAD
from XSDataCCP4DIMPLE import CCP4DataResultCAD
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus
from XSDataCCP4DIMPLE import XSDataString

class EDPluginExecDIMPLECADv10(EDPluginExecProcessScript):
    '''A wrapper for the CCP4 program CAD, with primary purpose: adding
    columns from two MTZ files together.'''

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputCAD)

        self._hklin_list = []
        self._labin_list = []
        self._hklout = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** EDPluginExecDIMPLECADv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),
                                      'Data Input is None')

        # check we have a list of hklin files
        # and a list of column label lists
        # and that these two lists are the same length

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getColumnLabels(),
                                      'No column labels specified')
        
        assert(len(data.getHKLIN()) == len(data.getColumnLabels()))       
        
        return

    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLECADv10.preProcess')

        data = self.getDataInput()

        for hklin in data.getHKLIN():
            self._hklin_list.append(hklin.getPath().getValue())

        for labin in data.getColumnLabels():            
            self._labin_list.append([l.getValue() for l in labin.getValues()])
            
        self._hklout = data.getHKLOUT().getPath().getValue()
        

        self.cad_script()

        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLECADv10.process')

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLECADv10.postProcess')

        self.programTermination()

        xsDataResult = CCP4DataResultCAD(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())
        self.setDataOutput(xsDataResult)

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue() 
        
        
        return

    def cad_script(self):
        '''Actually write the script to run cad.'''

        commandline = 'hklout "%s"' % self._hklout

        for j, hklin in enumerate(self._hklin_list):
            commandline += ' hklin%d "%s"' % (j + 1, hklin)
        
        self.setScriptCommandline(commandline)

        for j, labin in enumerate(self._labin_list):
            command = 'labin file %d' % (j + 1)

            if labin:
                for k, l in enumerate(labin):
                    command += ' E%d=%s' % (k + 1, l)
            else:
                command += ' ALL'
        
            self.addListCommandExecution(command)

        return
    
    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLECADv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                    CAD Output Log                    ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                 End CAD Output Log                   ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()

    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLECADv10.programTermination")
        strLog=self.readProcessLogFile()
        cadreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for cadline in cadreadlines:
            if "CAD:   *** Normal Termination of CAD ***" in cadline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of cad" 
        
        return

 



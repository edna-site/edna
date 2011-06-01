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

from XSDataCCP4DIMPLE import CCP4DataInputUNIQUE
from XSDataCCP4DIMPLE import CCP4DataResultUNIQUE

from XSDataCCP4Refinery import CCP4UnitCellTuple
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLEUNIQUEv10(EDPluginExecProcessScript):
    """A plugin to run the CCP4 program UNIQUE, which will calculate
    a list of Miller indices in an MTZ file from a unit cell, space
    group and resolution limit."""

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputUNIQUE)

        self._unit_cell = None
        self._space_group_name = None
        self._resolution_limit = None
        self._hklout = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

        self.checkMandatoryParameters(self.getDataInput().getHKLOUT(),
                                      "No MTZ file specified")
        self.checkMandatoryParameters(self.getDataInput().getSpaceGroup(),
                                      "No space group")
        self.checkMandatoryParameters(self.getDataInput().getUnitCell(),
                                      "No unit cell")
        self.checkMandatoryParameters(self.getDataInput().getResolutionLimit(),
                                      "No resolution limit")

        return
        
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.preProcess")
        
        self._hklout = self.getDataInput().getHKLOUT().getPath(
            ).getValue()
        self._space_group_name = self.getDataInput().getSpaceGroup(
            ).getName().getValue()
        self._unit_cell = CCP4UnitCellTuple(
            self.getDataInput().getUnitCell())
        self._resolution_limit = self.getDataInput().getResolutionLimit(
           ).getResolution().getValue()
        
        self.generate_unique_reflections_script()

        return

    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.process")

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.postProcess")

        self.programTermination()

        # call something to parse out the results

        xsDataResult = CCP4DataResultUNIQUE(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue()     

        return
    
    def generate_unique_reflections_script(self):
        '''Actually perform the processing to give the reflection file.'''

        self.setScriptCommandline('hklout %s' % self._hklout)
        self.addListCommandExecution('cell %f %f %f %f %f %f' %
                                     self._unit_cell)
        self.addListCommandExecution('symmetry "%s"' %
                                     self._space_group_name)
        self.addListCommandExecution('resolution %f' %
                                     self._resolution_limit)
        self.addListCommandExecution('labout F=F_UNIQUE SIGF=SIGF_UNIQUE')
        self.addListCommandExecution('end')

        return
                                     
    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  UNIQUE Output Log                   ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End UNIQUE Output Log                 ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()

    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEUNIQUEv10.programTermination")
        strLog=self.readProcessLogFile()
        uniquereadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for uniqueline in uniquereadlines:
            if "UNIQUE:  Normal Termination" in uniqueline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of unique" 
        
        return
        
 


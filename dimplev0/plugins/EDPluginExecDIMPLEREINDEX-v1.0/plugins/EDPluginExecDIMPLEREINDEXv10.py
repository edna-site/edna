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

from XSDataCCP4DIMPLE import CCP4DataInputREINDEX
from XSDataCCP4DIMPLE import CCP4DataResultREINDEX
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLEREINDEXv10(EDPluginExecProcessScript):
    '''An EDNA plugin for the CCP4 program reindex.'''

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputREINDEX)

        self._hklin = None
        self._hklout = None

        self._space_group_name = None
        self._reindexing_operation = 'h,k,l'

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREINDEXv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),'Data Input is None')

        # first see if we've been configured through the getter / setter 
        # methods

        if self._hklin and self._hklout and self._space_group_name and \
           self._reindexing_operation:
            return

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No MTZ file specified')

        self.checkMandatoryParameters(data.getSpaceGroup(),
                                      'No spacegroup specified')
        self.checkMandatoryParameters(data.getReindexingOperation(),
                                      'No reindexing operation specified')

        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREINDEXv10.preProcess')

        if self._hklin and self._hklout and self._space_group_name and \
           self._reindexing_operation:
            return
        
        data = self.getDataInput()
        print ("SQUARING THE CIRCLE TWO")
        self._hklin = data.getHKLIN().getPath().getValue()
        self._hklout = data.getHKLOUT().getPath().getValue()
        
        self._space_group_name = data.getSpaceGroup().getName().getValue()
        self._reindexing_operation = data.getReindexingOperation().getSymmetryOperation().getValue()
        
        self.reindex_script()
        
        return
        
    def process(self, _edObject = None):        
        EDPluginExecProcessScript.process(self)               
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREINDEXv10.process')
        
        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREINDEXv10.postProcess')

        self.programTermination()

        xsDataResult = CCP4DataResultREINDEX(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue()
        

        return

    # getter / setter methods

    def set_hklin(self, hklin):
        self._hklin = hklin
        return

    def get_hklin(self):
        return self._hklin

    def set_hklout(self, hklout):
        self._hklout = hklout
        return

    def get_hklout(self):
        return self._hklout

    def set_space_group_name(self, space_group_name):
        self._space_group_name = space_group_name
        return

    def get_space_group_name(self):
        return self._space_group_name

    def set_reindexing_operation(self, reindexing_operation):
        self._reindexing_operation = reindexing_operation
        return

    def get_reindexing_operation(self):
        return self._reindexing_operation

    # main meat 'n' two veg
    
    def reindex_script(self):
        '''Actually write the script to run reindex.'''
        
        self.setScriptCommandline('hklin "%s" hklout "%s"' % 
                                  (self._hklin, self._hklout))
        self.addListCommandExecution('symmetry "%s"' % self._space_group_name)
        self.addListCommandExecution('reindex "%s"' %
                                     self._reindexing_operation)

        return

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEREINDEXv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  REINDEX Output Log                  ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End REINDEX Output Log                ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()

    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEREINDEXv10.programTermination")
        strLog=self.readProcessLogFile()
        reindexreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for reindexline in reindexreadlines:
            if "REINDEX:   ** Normal termination" in reindexline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of reindex" 
        
        return




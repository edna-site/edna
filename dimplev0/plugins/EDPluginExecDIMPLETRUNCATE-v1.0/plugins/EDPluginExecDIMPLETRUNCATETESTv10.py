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

from EDPluginExecProcessXIA2CORE import EDPluginExecProcessXIA2CORE

from XSDataCCP4DIMPLE import CCP4DataInputTRUNCATE
from XSDataCCP4DIMPLE import CCP4DataResultTRUNCATE
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLETRUNCATETESTv10(EDPluginExecProcessXIA2CORE):
    '''An EDNA plugin for the CCP4 program truncate.'''

    def __init__(self):
        EDPluginExecProcessXIA2CORE.__init__(self)
        self.setXSDataInputClass(CCP4DataInputTRUNCATE)

        self._hklin = None
        self._hklout = None

        self._nres = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATETESTv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),'Data Input is None')

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No MTZ file specified')

        self.checkMandatoryParameters(data.getSequence(),
                                      'No sequence specified')

        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessXIA2CORE.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATETESTv10.preProcess')

        data = self.getDataInput()

        self._hklin = data.getHKLIN().getPath().getValue()
        self._hklout = data.getHKLOUT().getPath().getValue()

        self._nres = data.getSequence().getNumberOfResidues().getValue()

        self.truncate_script()

        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessXIA2CORE.process(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATETESTv10.process')

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessXIA2CORE.postProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATETESTv10.postProcess')

        self.programTermination()

        xsDataResult = CCP4DataResultTRUNCATE(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue()

        return
    
    def truncate_script(self):
        '''Actually write the script to run truncate.'''
        
        self.setCommandline('hklin "%s" hklout "%s"' % 
                                  (self._hklin, self._hklout))
        self.addListCommandExecution('nres %d' % self._nres)

        return

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLETRUNCATETESTv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  TRUNCATE Output Log                  ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End TRUNCATE Output Log                ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()


    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLETRUNCATETESTv10.programTermination")
        strLog=self.readProcessLogFile()
        truncatereadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for truncateline in truncatereadlines:
            if "TRUNCATE:  Normal termination" in truncateline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of truncate" 
        
        return



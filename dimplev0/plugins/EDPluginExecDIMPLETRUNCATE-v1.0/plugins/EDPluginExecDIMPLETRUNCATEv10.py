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

from XSDataCCP4DIMPLE import CCP4MTZColLabels
from XSDataCCP4DIMPLE import CCP4DataInputTRUNCATE
from XSDataCCP4DIMPLE import CCP4DataResultTRUNCATE
from XSDataCCP4DIMPLE import XSDataString
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLETRUNCATEv10(EDPluginExecProcessScript):
    '''An EDNA plugin for the CCP4 program truncate.'''

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputTRUNCATE)

        self._hklin = None
        self._hklout = None

        self._nres = None

        self._ColLabels = None      
        self._ColLabels_IMEAN = None
        self._ColLabels_SIGIMEAN = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATEv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),'Data Input is None')

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No MTZ file specified')

        self.checkMandatoryParameters(data.getSequence(),
                                      'No sequence specified')

        self.checkMandatoryParameters(data.getColLabels(),
                                      'No column labels specified (input)')

        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATEv10.preProcess')

        data = self.getDataInput()

        self._hklin = data.getHKLIN().getPath().getValue()
        self._hklout = data.getHKLOUT().getPath().getValue()

        self._nres = data.getSequence().getNumberOfResidues().getValue()

        self._ColLabels=data.getColLabels()
        self._ColLabels_IMEAN = data.getColLabels().IMEAN.getValue()
        self._ColLabels_SIGIMEAN = data.getColLabels().SIGIMEAN.getValue()

        self.truncate_script()

        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATEv10.process')

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATEv10.postProcess')

        self.programTermination()

        xsDataResult = CCP4DataResultTRUNCATE(
            HKLOUT = HKL(self._hklout),
            ColLabels=self._ColLabels,
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue()

        return
    
    def truncate_script(self):
        '''Actually write the script to run truncate.'''
        EDVerbose.DEBUG('*** EDPluginExecDIMPLETRUNCATEv10.truncate_script')
        
        self.setScriptCommandline('hklin "%s" hklout "%s"' % 
                                  (self._hklin, self._hklout))
        self.addListCommandExecution(
            'labin IMEAN=%s SIGIMEAN=%s' % (self._ColLabels_IMEAN, self._ColLabels_SIGIMEAN))
        self.addListCommandExecution('labout F=F SIGF=SIGF')
        if self._nres:
            self.addListCommandExecution('nres %d' % self._nres)
      
        self._ColLabels.setF(XSDataString("F"))
        self._ColLabels.setSIGF(XSDataString("SIGF"))
 
        return

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLETRUNCATEv10.generateExecutiveSummary")
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
        EDVerbose.DEBUG("*** EDPluginExecDIMPLETRUNCATEv10.programTermination")
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



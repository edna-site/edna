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

from XSDataCCP4DIMPLE import CCP4DataInputFREERFLAG
from XSDataCCP4DIMPLE import CCP4DataResultFREERFLAG
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLEFREERFLAGv10(EDPluginExecProcessScript):
    """An EDNA plugin to wrap the CCP4 program freerflag, which randomly
    assigns a give fraction (typically 5%) of the unique reflections
    to a free set, for validation."""
    
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputFREERFLAG)

        self._hklin = None
        self._hklout = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),
                                      "No MTZ file specified")
        self.checkMandatoryParameters(self.getDataInput().getHKLOUT(),
                                      "No MTZ file specified")

        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.preProcess")

        self._hklin = self.getDataInput().getHKLIN().getPath(
            ).getValue()
        self._hklout = self.getDataInput().getHKLOUT().getPath(
            ).getValue()
        
        self.freer_flag_script()
        
        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.process")

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.postProcess")

        self.programTermination()

        xsDataResult = CCP4DataResultFREERFLAG(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue()     


        return

    def freer_flag_script(self):
        '''Actually write the script to run freerflag.'''
        
        self.setScriptCommandline('hklin "%s" hklout "%s"' % 
                                  (self._hklin, self._hklout))
        self.addListCommandExecution('end')

        return
                                     
        
    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                FREERFLAG Output Log                  ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###              End FREERFLAG Output Log                ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()

    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEFREERFLAGv10.programTermination")
        strLog=self.readProcessLogFile()
        freeflagreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for freeflagline in freeflagreadlines:
            if "FREERFLAG:  Normal termination" in freeflagline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of freeflag" 
        
        return
        


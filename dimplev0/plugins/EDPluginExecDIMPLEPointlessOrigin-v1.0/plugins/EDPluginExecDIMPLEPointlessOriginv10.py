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

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4DataInputPointlessOrigin
from XSDataCCP4DIMPLE import CCP4DataResultPointlessOrigin
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLEPointlessOriginv10(EDPluginExecProcessScript):
    """An EDNA plugin for the CCP4 program Pointless, to determine the
    correct origin for an input MTZ file with respect to an input PDB file."""

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputPointlessOrigin)

        self._hklin = None
        self._xyzin = None
        self._hklout = None
        
        return

    def checkParameters(self):
        EDVerbose.DEBUG("EDPluginExecDIMPLEPointlessOriginv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

        

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')        
        self.checkMandatoryParameters(data.getXYZIN(),
                                      'No PDB file specified')        
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No PDB file specified')
        
        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPointlessOriginv10.preProcess")
        
        data = self.getDataInput()

        self._hklin = data.getHKLIN().getPath().getValue()
        self._xyzin = data.getXYZIN().getPath().getValue()
        self._hklout = data.getHKLOUT().getPath().getValue()
        

        self.pointless_origin_script()
        
        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPointlessOriginv10.process")
        
        return
        

    def postProcess(self, _edObject = None):        
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPointlessOriginv10.postProcess")
        
        xsDataResult = CCP4DataResultPointlessOrigin(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)

        if not os.path.isfile(self.getDataOutput().getHKLOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getHKLOUT().getPath().getValue() 

        return


    def pointless_origin_script(self):
        '''Actually write the script to run pointless to determine the
        right origin, and reindex accordingly.'''
        #print ("%s ---------------- " % self._xyzin)
        self.setScriptCommandline('hklin "%s" xyzin "%s" hklout "%s"' % 
                                  (self._hklin, self._xyzin, self._hklout))
       
        return


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPointlessOriginv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPointlessOriginv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###               Pointless Output Log                   ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###              End Pointless Output Log                ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()


    

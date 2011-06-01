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
import shutil

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4MTZColLabels
from XSDataCCP4DIMPLE import CCP4DataInputPhaser
from XSDataCCP4DIMPLE import CCP4DataResultPhaser
from XSDataCCP4DIMPLE import XSDataFloat
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus


class EDPluginExecDIMPLEPHASERv10(EDPluginExecProcessScript ):
    """
    An EDNA plugin for the CCP4 program Phaser
    """
    

    def __init__(self ):
        """
        """
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(CCP4DataInputPhaser)

        self._hklin = None
        self._hklout = None
        self._xyzin = None
        self._xyzout = None

        self._ColLabels_F = None
        self._ColLabels_SIGF = None

        return

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDIMPLEPHASERv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified (input)')
        self.checkMandatoryParameters(data.getHKLOUT(),
                                      'No MTZ file specified (output)')
        self.checkMandatoryParameters(data.getXYZIN(),
                                      'No PDB file specified (input)')
        self.checkMandatoryParameters(data.getXYZOUT(),
                                      'No PDB file specified (output)')
        self.checkMandatoryParameters(data.getColLabels(),
                                      'No column labels specified (input)')

        return

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPHASERv10.postProcess")

        data = self.getDataInput()

        self._hklin = data.getHKLIN().getPath().getValue()
        self._hklout = data.getHKLOUT().getPath().getValue()
        self._xyzin = data.getXYZIN().getPath().getValue()
        self._xyzout = data.getXYZOUT().getPath().getValue()

        self._ColLabels_F = data.getColLabels().F.getValue()
        self._ColLabels_SIGF = data.getColLabels().SIGF.getValue()

        self.phaser_script()

        return
        
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPHASERv10.process")

        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLEPHASERv10.postProcess")

        self.programTermination()
        # Create some output data
        xsDataResult = CCP4DataResultPhaser(
            HKLOUT = HKL(self._hklout),
            XYZOUT = XYZ(self._xyzout),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)

        xyzout = None

        for record in self.readProcessLogFile().split('\n'):
            if 'Solution' in record and 'written to PDB file:' in record and ".pdb" in record:
                xyzout = record.split()[-1]

        assert(xyzout)
                
        shutil.copyfile(os.path.join(self.getWorkingDirectory(), xyzout),
                        self._xyzout)

        if  not os.path.isfile(self._xyzout):
            raise RuntimeError, 'File %s does not exist' % self._xyzout

        return

    def phaser_script(self):
        mw=self.calculateMW(self._xyzin)
        self.addListCommandExecution(
            'mode mr_auto')
        self.addListCommandExecution(
            'hklin "%s"' % (self._hklin))
        self.addListCommandExecution(
            'labin F=%s SIGF=%s' % (self._ColLabels_F, self._ColLabels_SIGF))
        self.addListCommandExecution(
            'ensemble model pdb "%s" identity 100' % (self._xyzin))
        self.addListCommandExecution(
            'composition protein mw %d num 1' % mw)
        self.addListCommandExecution(
            'search ensemble model num 1')
        self.addListCommandExecution(
            'root mr')
        self.addListCommandExecution(
            'end')

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPHASERv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPHASERv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###               Phaser Output Log                      ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End Phaser Output Log                 ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()

    def calculateMW(self,filename):
        """
        Calculates the Molecular Weight of the protein approximately
        """
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPHASERv10.calculateMW")
        
        SEQRESFound=False
        count=0
        Chain=''        
        CurrentIndex=int(0)
        NumberOfResidues=int(0)
        f=open(filename,'r')
        pdbreadlines=f.readlines()
        
        for pdbline in pdbreadlines:
            if "SEQRES" in pdbline:                
                SEQRESFound=True
                pdblistofitemsincurrentline=pdbline.split()
                for pdblinecurrentitem in pdblistofitemsincurrentline:
                    if pdblinecurrentitem.upper() in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS']:
                        NumberOfResidues=NumberOfResidues+1
            elif SEQRESFound==False:
                pdblistofitemsincurrentline=pdbline.split()
                if pdblistofitemsincurrentline[0].upper()=="ATOM":
                    if (pdblistofitemsincurrentline[3].upper() in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS'] or 
                        pdblistofitemsincurrentline[2].upper()[-3:] in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS']):
                       if pdblistofitemsincurrentline[3].upper() in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS']:
		               if  Chain=='':
		                   Chain=pdblistofitemsincurrentline[4].upper()
		                   CurrentIndex=pdblistofitemsincurrentline[5]
		               elif pdblistofitemsincurrentline[4].upper()!=Chain:
		                    Chain=pdblistofitemsincurrentline[4].upper()                            
		                    NumberOfResidues=int(NumberOfResidues) + int(CurrentIndex)
		                    CurrentIndex=int(0)
		               elif pdblistofitemsincurrentline[4].upper()==Chain: 
		                    if pdblistofitemsincurrentline[5]!=CurrentIndex:
                                        CurrentIndex=pdblistofitemsincurrentline[5]
                       elif (pdblistofitemsincurrentline[3].upper() not in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS'] and pdblistofitemsincurrentline[2].upper()[-3:] in ['ILE','LEU','LYS','MET','PHE','THR','TRP','VAL','ALA','ASN','ASP','CYS','GLU','GLN','GLY','PRO','SER','TYR','ARG','HIS']):
                               if  Chain=='':
		                   Chain=pdblistofitemsincurrentline[3].upper()
		                   CurrentIndex=pdblistofitemsincurrentline[4]
		               elif pdblistofitemsincurrentline[3].upper()!=Chain:
		                    Chain=pdblistofitemsincurrentline[3].upper()                            
		                    NumberOfResidues=int(NumberOfResidues) + int(CurrentIndex)
		                    CurrentIndex=int(0)
		               elif pdblistofitemsincurrentline[3].upper()==Chain: 
		                    if pdblistofitemsincurrentline[4]!=CurrentIndex:
                                        CurrentIndex=pdblistofitemsincurrentline[4]
                                
                                
            

            count=count+1       
            if len(pdbreadlines)==count and SEQRESFound==False:
                NumberOfResidues=int(NumberOfResidues) + int(CurrentIndex)
                         

        f.close()                

        return NumberOfResidues*110

    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPHASERv10.programTermination")
        strLog=self.readProcessLogFile()
        phaserreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for phaserline in phaserreadlines:
            if "EXIT STATUS: SUCCESS" in phaserline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of phaser" 
        
        return


    

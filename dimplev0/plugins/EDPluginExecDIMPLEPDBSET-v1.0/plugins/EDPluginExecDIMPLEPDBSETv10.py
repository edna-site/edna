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

from XSDataCCP4DIMPLE import CCP4DataInputPDBSET
from XSDataCCP4DIMPLE import CCP4DataResultPDBSET
from XSDataCCP4DIMPLE import CCP4ReturnStatus
from XSDataCCP4DIMPLE import XSDataString
from XSDataCCP4DIMPLE import XSDataInteger

import sys

class EDPluginExecDIMPLEPDBSETv10( EDPluginExecProcessScript ):
    """
    An EDNA plugin for the CCP4 program PDBSET
    """
    

    def __init__( self ):
        """
        """
        EDPluginExecProcessScript.__init__( self )
        self.setXSDataInputClass( CCP4DataInputPDBSET )


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEPDBSETv10.checkParameters")
        self.checkMandatoryParameters( self.getDataInput(),"Data Input is None" )
        self.checkMandatoryParameters( self.getDataInput().getXYZIN(),"No input PDB file" )
        self.checkMandatoryParameters( self.getDataInput().getXYZOUT(),"No output PDB file" )
        #self.checkMandatoryParameters( self.getDataInput().getOutputLogFile(),"No output Log file" )
        self.checkMandatoryParameters( self.getDataInput().getUnitCell(),"No unit cell data" )
        #EDVerbose.DEBUG( `self.getDataInput().getXYZIN().getPath().getValue()`)
        #self.checkMandatoryParameters( self.getDataInput().getUnitCell(),"No unit cell" )

    
    def preProcess( self, _edObject = None ):
        EDPluginExecProcessScript.preProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEPDBSETv10.preProcess")
        self.generatePDBSETCommands()
        if self.getDataInput().getOutputLogFile() != None:
           self.setScriptLogFileName(self.getDataInput().getOutputLogFile().getPath().getValue())
           EDVerbose.DEBUG( "*** EDPluginExecDIMPLEPDBSETv10.preProcess - setting log file to: " \
                            + self.getScriptLogFileName())
        
        
    def postProcess( self, _edObject = None ):
        EDPluginExecProcessScript.postProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEPDBSETv10.postProcess")

        self.programTermination()

        # Create some output data
        # xsDataResult = CCP4DataResultPDBSET()
        # self.setDataOutput( xsDataResult )
        strLog=self.readProcessLogFile()
        ccp4ReturnStatus=self.getPDBSETReturnStatus(strLog)        
     
	ccp4DataResultPDBSET=CCP4DataResultPDBSET()       

        # Set the output PDB file
        ccp4DataResultPDBSET.setXYZOUT(XSDataString(self.getDataInput().getXYZOUT().getPath().getValue()))

        # Set the output log file
        ccp4DataResultPDBSET.setOutputLogFile(XSDataString(self.getScriptLogFileName()))

        # Set the return status
        ccp4DataResultPDBSET.setReturnStatus(ccp4ReturnStatus)

        # Set the data output for the job
        self.setDataOutput(ccp4DataResultPDBSET)
        
        if not os.path.isfile(self.getDataOutput().getXYZOUT().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getXYZOUT().getValue() 


    def generatePDBSETCommands(self):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBSETv10.generatePDBSETCommands")
        self.setScriptCommandline("XYZIN %s XYZOUT %s" % (self.getDataInput().getXYZIN().getPath().getValue(),self.getDataInput().getXYZOUT().getPath().getValue()))           
        uc=self.getDataInput().getUnitCell()
        self.addListCommandExecution("CELL %f %f %f %f %f %f" % (uc.getA().getValue(), uc.getB().getValue(),uc.getC().getValue(),uc.getAlpha().getValue(),uc.getBeta().getValue(),uc.getGamma().getValue()))
        self.addListCommandExecution("END")

    def getPDBSETReturnStatus(self, stringOfCommands):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBSETv10.getPDBSETReturnStatus")
        ccp4ReturnStatus=CCP4ReturnStatus()
        ccp4ReturnStatus.setCode(XSDataInteger(0))
        ccp4ReturnStatus.setMessage(XSDataString("No message"))
        pyListLogLines = stringOfCommands.split("\n")
        for pyStrLine in enumerate(pyListLogLines):
            if " PDBSET:   === Normal completion PDBSET ===" in pyStrLine:
                ccp4ReturnStatus.setCode(XSDataInteger(1))
                ccp4ReturnStatus.setMessage(XSDataString("Normal completion"))
            elif " PDBSET:   "  in pyStrLine:
                ccp4ReturnStatus.setCode(XSDataInteger(0))
                pyStrStatus = pyStrLine.split("=")[3].strip()
                ccp4ReturnStatus.setMessage(XSDataString(pyStrStatus))

        return ccp4ReturnStatus


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  PDBSET Output Log                   ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile()) 
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End PDBSET Output Log                 ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()


    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBSETv10.programTermination")
        strLog=self.readProcessLogFile()
        pdbsetreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for pdbsetline in pdbsetreadlines:
            if "PDBSET:   === Normal completion PDBSET ===" in pdbsetline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of pdbset" 
        
        return








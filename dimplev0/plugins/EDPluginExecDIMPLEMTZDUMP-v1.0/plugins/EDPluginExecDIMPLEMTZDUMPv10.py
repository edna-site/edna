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

from EDImportLib import EDVerbose

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4DataInputMTZDUMP
from XSDataCCP4DIMPLE import CCP4DataResultMTZDUMP

from XSDataCCP4DIMPLE import CCP4SpaceGroup
from XSDataCCP4DIMPLE import CCP4UnitCell
from XSDataCCP4DIMPLE import CCP4ResolutionLimit
from XSDataCCP4DIMPLE import CCP4SymmetryOperation

from XSDataCCP4DIMPLE import XSParamList
from XSDataCCP4DIMPLE import XSDataString
from XSDataCCP4DIMPLE import XSDataInteger
from XSDataCCP4DIMPLE import XSDataFloat
from XSDataCCP4DIMPLE import XSParamItem


class EDPluginExecDIMPLEMTZDUMPv10( EDPluginExecProcessScript ):
    """
    [To be replaced with a description of EDPluginExecProcessScriptTemplatev10]
    """
    

    def __init__( self ):
        """
        """
        EDPluginExecProcessScript.__init__( self )
        self.setXSDataInputClass( CCP4DataInputMTZDUMP )


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEMTZDUMPv10.checkParameters")       
        self.checkMandatoryParameters( self.getDataInput(),"Data Input is None" )        
        self.checkMandatoryParameters( self.getDataInput().getHKLIN(),"No input MTZ file" )

    
    def preProcess( self, _edObject = None ):
        EDPluginExecProcessScript.preProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEMTZDUMPv10.preProcess")
        self.generateDIMPLEMTZDUMPCommands()
        if self.getDataInput().getOutputLogFile() != None:
           self.setScriptLogFileName(self.getDataInput().getOutputLogFile().getPath().getValue())
           EDVerbose.DEBUG( "*** EDPluginExecDIMPLEPDBSETv10.preProcess - setting log file to: " \
                            + self.getScriptLogFileName())
        
    """    
    def process( self, _edObject = None ):
        EDPluginExecProcessScript.process( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEMTZDUMPv10.process")
    """
        

    def postProcess( self, _edObject = None ):
        EDPluginExecProcessScript.postProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEMTZDUMPv10.postProcess")    
        # check to see if the program terminated normally    
        self.programTermination()
        # Create some output data
        strLog=self.readProcessLogFile()
        dataResultFromMTZDUMP=self.parseDIMPLEMTZDUMP(strLog)        
        self.setDataOutput(dataResultFromMTZDUMP)       


    def generateDIMPLEMTZDUMPCommands(self):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEMTZDUMPv10.generateDIMPLEMTZDUMPCommands")
        ccp4DataInputMTZDUMP=self.getDataInput()
        HKLIN=ccp4DataInputMTZDUMP.getHKLIN().getPath().getValue()
        self.setScriptCommandline("HKLIN %s" % HKLIN)
        self.addListCommandExecution("END")

    def parseDIMPLEMTZDUMP(self, stringOfCommands):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEMTZDUMPv10.parseDIMPLEMTZDUMP")        
        pyListLogLines = stringOfCommands.split("\n")
        listOfColumns = XSParamList()

	column_name_list = []
        column_type_list = []

        for j, pyStrLine in enumerate(pyListLogLines):
            if "* Dataset ID, project/crystal/dataset names, cell dimensions, wavelength:" in pyStrLine:
                pyTupleCell = tuple(map(float, pyListLogLines[j + 5].split()))
            if " * Space group = " in pyStrLine:
                pyStrSpaceGroupName = pyStrLine.split("'")[1].strip()
                iSpaceGroupNumber = int(pyStrLine.replace("(", " ").replace(")", " ").split()[-1])
            if "*  Resolution Range" in pyStrLine:
                lowerResolutionLimit = float(((pyListLogLines[j + 2].split("(")[1]).split())[0])
                upperResolutionLimit = float(((pyListLogLines[j + 2].split("(")[1]).split())[2])
            if "* Column Labels" in pyStrLine:
                column_name_list = pyListLogLines[j + 2].split()
            if "* Column Types" in pyStrLine:
                column_type_list = pyListLogLines[j + 2].split()

        for j, column_name in enumerate(column_name_list):
            column_type = column_type_list[j]
            listOfColumns.addXSParamItem(XSParamItem(name = column_name, value = column_type))

        ccp4DataResultMTZDUMP=CCP4DataResultMTZDUMP()

        # Set the unit cell values
        ccp4UnitCell = CCP4UnitCell()     
        ccp4UnitCell.setA(XSDataFloat(pyTupleCell[0]))
        ccp4UnitCell.setB(XSDataFloat(pyTupleCell[1]))
        ccp4UnitCell.setC(XSDataFloat(pyTupleCell[2]))
        ccp4UnitCell.setAlpha(XSDataFloat(pyTupleCell[3]))
        ccp4UnitCell.setBeta(XSDataFloat(pyTupleCell[4]))
        ccp4UnitCell.setGamma(XSDataFloat(pyTupleCell[5]))

        # Set the Spacegroup parameters
        ccp4SpaceGroup = CCP4SpaceGroup()
        ccp4SpaceGroup.setName(XSDataString(pyStrSpaceGroupName))
        ccp4SpaceGroup.setNumber(XSDataInteger(iSpaceGroupNumber))

        ccp4DataResultMTZDUMP.setUnitCell(ccp4UnitCell)
        ccp4DataResultMTZDUMP.setSpaceGroup(ccp4SpaceGroup)

        # changed this to match the API specified in the data model
        
        ccp4DataResultMTZDUMP.setLowerResolutionLimit(
            CCP4ResolutionLimit(resolution = 
                                XSDataFloat(lowerResolutionLimit)))
        ccp4DataResultMTZDUMP.setUpperResolutionLimit(
            CCP4ResolutionLimit(resolution = 
                                XSDataFloat(upperResolutionLimit)))
        
        ccp4DataResultMTZDUMP.addListOfColumns(listOfColumns)

        
        if self.getDataInput().getOutputLogFile():
            ccp4DataResultMTZDUMP.setOutputLogFile(XSDataString(self.getScriptLogFileName()))                
        
        return ccp4DataResultMTZDUMP


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEMTZDUMPv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  MTZDUMP Output Log                  ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End MTZDUMP Output Log                ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()



    def programTermination(self):
        """
        Check if the logfile has correct termination message
        """        
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEMTZDUMPv10.programTermination")
        strLog=self.readProcessLogFile()
        mtzreadlines = strLog.split("\n")

        bProgramTerminatedNormally=False
                
        for mtzline in mtzreadlines:
            if "MTZDUMP:   Normal termination of mtzdump" in mtzline:  
                bProgramTerminatedNormally=True
                break
               

        if bProgramTerminatedNormally==False:
            raise RuntimeError, "Abnormal termination of mtzdump" 
        
        return





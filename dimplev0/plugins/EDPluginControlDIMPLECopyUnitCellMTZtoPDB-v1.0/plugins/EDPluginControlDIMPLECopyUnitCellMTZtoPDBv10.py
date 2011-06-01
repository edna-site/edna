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

from EDPluginControl import EDPluginControl

from XSDataCCP4DIMPLE import CCP4DataInputControlCopyUnitCellMTZtoPDB
from XSDataCCP4DIMPLE import CCP4DataResultControlCopyUnitCellMTZtoPDB

from XSDataCCP4DIMPLE import CCP4DataInputMTZDUMP
from XSDataCCP4DIMPLE import CCP4DataResultMTZDUMP

from XSDataCCP4DIMPLE import CCP4DataInputPDBSET
from XSDataCCP4DIMPLE import CCP4DataResultPDBSET

class EDPluginControlDIMPLECopyUnitCellMTZtoPDBv10( EDPluginControl ):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """
    

    def __init__( self ):
        """
        """
        EDPluginControl.__init__( self )
        self.setXSDataInputClass( CCP4DataInputControlCopyUnitCellMTZtoPDB )
        self.m_edStringControlledPluginName = "EDPluginExecDIMPLEMTZDUMPv10"
        self.m_edPluginExecTemplate = None


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "*** EDPluginControlDIMPLECopyUnitCellMTZtoPDBv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None" )
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(), "No input MTZ file")
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(), "No input PDB file")

############################################################################################################
    
    def preProcess( self, _edObject = None ):
        EDPluginControl.preProcess( self )
        EDVerbose.DEBUG( "*** EDPluginControlDIMPLECopyUnitCellMTZtoPDBv10.preProcess")
        # Load the execution plugin
        #self.m_edPluginExecTemplate = self.loadPlugin( self.m_edStringControlledPluginName ) 
        # Set the input MTZ file for the Control plugin
        self.ccp4DataFile_mtzInputFile = self.getDataInput().getHKLIN()
        # Create an instance of the MTZDUMP exec plugin
        self.ccp4DataInput_MTZDUMP = CCP4DataInputMTZDUMP()
        # Set the input MTZ file for MTZDUMP 
        self.ccp4DataInput_MTZDUMP.setHKLIN(self.getDataInput().getHKLIN())
        # Set the input PDB file for the Control plugin
        self.ccp4DataInput_XYZIN = self.getDataInput().getXYZIN()
        # Set the output PDB file for the Control plugin
        self.ccp4DataInput_XYZOUT = self.getDataInput().getXYZOUT()
  
############################################################################################################

    def process( self, _edObject = None ):
        EDPluginControl.process( self )
        EDVerbose.DEBUG( "*** EDPluginExecDIMPLEMTZDUMPv10.process")

        self.edPluginMTZDUMP = self.loadPlugin('EDPluginExecDIMPLEMTZDUMPv10')
        self.edPluginMTZDUMP.setDataInput(self.ccp4DataInput_MTZDUMP)
        self.edPluginMTZDUMP.connectSUCCESS(self.doSuccess_MTZDUMP)
        self.edPluginMTZDUMP.connectFAILURE(self.doFailure_MTZDUMP)
        self.edPluginMTZDUMP.executeSynchronous()

############################################################################################################
    
    def postProcess( self, _edObject = None ):
        EDPluginControl.postProcess( self )
        EDVerbose.DEBUG( "*** EDPluginControlDIMPLECopyUnitCellMTZtoPDBv10.postProcess")
        # Create some output data
        xsDataResult = CCP4DataResultControlCopyUnitCellMTZtoPDB()
        self.setDataOutput( xsDataResult )

############################################################################################################

    def doSuccess_MTZDUMP(self, _edPlugin=None):
        EDVerbose.DEBUG("*** doSuccess_MTZDUMP")
        self.ccp4DataInput_inputUnitCell = self.edPluginMTZDUMP.getDataOutput().getUnitCell()
        self.ccp4DataInput_PDBSET = CCP4DataInputPDBSET()
        self.ccp4DataInput_PDBSET.setUnitCell(self.ccp4DataInput_inputUnitCell)
        self.ccp4DataInput_PDBSET.setXYZIN(self.ccp4DataInput_XYZIN)
        self.ccp4DataInput_PDBSET.setXYZOUT(self.ccp4DataInput_XYZOUT)

        self.edPluginPDBSET = self.loadPlugin('EDPluginExecDIMPLEPDBSETv10')
        self.edPluginPDBSET.setDataInput(self.ccp4DataInput_PDBSET)
        self.edPluginPDBSET.connectSUCCESS(self.doSuccess_PDBSET)
        self.edPluginPDBSET.connectFAILURE(self.doFailure_PDBSET)
        self.edPluginPDBSET.executeSynchronous()



    def doFailure_MTZDUMP(self, _edPlugin=None):
        EDVerbose.DEBUG("*** doFailure_MTZDUMP")

############################################################################################################

    def doSuccess_PDBSET(self, _edPlugin=None):
        EDVerbose.DEBUG("*** doSuccess_PDBSET")
        ccp4DataResult_CopyUnitCellMTZtoPDB = CCP4DataResultControlCopyUnitCellMTZtoPDB()
        ccp4DataResult_CopyUnitCellMTZtoPDB.setXYZOUT(self.edPluginPDBSET.getDataOutput().getXYZOUT())
        self.setDataOutput(ccp4DataResult_CopyUnitCellMTZtoPDB)

    def doFailure_PDBSET(self, _edPlugin=None):
        EDVerbose.DEBUG("*** doFailure_PDBSET")

############################################################################################################

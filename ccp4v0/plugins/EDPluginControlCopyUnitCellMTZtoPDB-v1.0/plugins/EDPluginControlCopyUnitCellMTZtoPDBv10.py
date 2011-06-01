# -*- coding: UTF8 -*-
#
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4 / ESRF
#
#    Principal author:       Mark
#                        Jérôme Kieffer (Kieffer@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
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

from EDVerbose import EDVerbose

from EDPluginControl import EDPluginControl

from XSDataCCP4v0 import XSDataUnitCell
from XSDataCCP4v0 import XSDataSpaceGroup
from XSDataCCP4v0 import XSDataInputMTZDUMPUnitCellSpaceGroup
from XSDataCCP4v0 import XSDataResultMTZDUMPUnitCellSpaceGroup
from XSDataCCP4v0 import XSDataInputPDBSETUnitCell
from XSDataCCP4v0 import XSDataResultPDBSETUnitCell
from XSDataCCP4v0 import XSDataInputCopyUnitCellMTZtoPDB
from XSDataCCP4v0 import XSDataResultCopyUnitCellMTZtoPDB


class EDPluginControlCopyUnitCellMTZtoPDBv10(EDPluginControl):
    """   
    This is the Edna plugin control that runs subsequently the two execution plugins called MTZDUMPUnitCellSpaceGroupv10 and PDBSETUnitCellv10
    
    -MTZDUMP to extract the Unit Cell parameters and the space group of an MTZ file
    
    -PDBSET to set the unit cell formerly extracted into the given PDB file.    


    @author: Mark Basham, Jérôme Kieffer
    @copyright: CCP4 team, DLS & ESRF collaboration
    @license: GPLv3 or above 
    
    """


    def __init__(self):
        """
        Constructor of the class.
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCopyUnitCellMTZtoPDB)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginExecMTZDUMPUnitCellSpaceGroupv10.checkParameters")
#        print self.getDataInput().marshal()
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputMTZFile(), "No input MTZ file")
        self.checkMandatoryParameters(self.getDataInput().getInputPDBFile(), "No input PDB file")

    def preProcess(self, _edObject=None):
        """Set the input of the first execution plugin, MTZDUMPUnitCellSpaceGroupv10, to be the same as the control plugin
        """
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecMTZDUMPUnitCellSpaceGroupv10.preProcess")
        self.xsDataFile_mtzInputFile = self.getDataInput().getInputMTZFile()
        self.xsDataInput_MTZDUMPUnitCellSpaceGroup = XSDataInputMTZDUMPUnitCellSpaceGroup()
        self.xsDataInput_MTZDUMPUnitCellSpaceGroup.setInputMTZFile(self.xsDataFile_mtzInputFile)
        self.xsDataInput_inputPDBFile = self.getDataInput().getInputPDBFile()

    def process(self, _edObject=None):
        """Runs the first execution plugin, i.e. MTZDUMPUnitCellSpaceGroupv10 and connects the two methods  doSuccess_MTZDUMP and doFailure_MTZDUMP 
        which will be executed afterwards
        """
        EDPluginControl.process(self)
        EDVerbose.DEBUG("*** EDPluginExecMTZDUMPUnitCellSpaceGroupv10.process")
        self.edPluginMTZDUMP = self.loadPlugin('EDPluginExecMTZDUMPUnitCellSpaceGroupv10')
        self.edPluginMTZDUMP.setDataInput(self.xsDataInput_MTZDUMPUnitCellSpaceGroup)
        self.edPluginMTZDUMP.connectSUCCESS(self.doSuccess_MTZDUMP)
        self.edPluginMTZDUMP.connectFAILURE(self.doFailure_MTZDUMP)
        self.edPluginMTZDUMP.executeSynchronous()

    def postProcess(self, _edObject=None):
        """This is the post-processing of the control plugin, it is always executed at the very end of the procedure.
        It can set some results in case they are not dependent of the success/failure of any of its controled plugins
        """
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecMTZDUMPUnitCellSpaceGroupv10.postProcess")

    def doSuccess_MTZDUMP(self, _edPlugin=None):
        """
        This method is called after the MTZDUMPUnitCellSpaceGroup execution plugin has successfully processed, 
        it retrieves the results out of the execution plugin MTZDUMPUnitCellSpaceGroupv10 
        and sets the input for the second execution plugin EDPluginExecPDBSETUnitCellv10
        before running it. The two methods doSuccess_PDBSET and doFailure_PDBSET are also connected here.
        """
        EDVerbose.DEBUG("*** doSuccess_MTZDUMP")
        self.xsDataInput_inputUnitCell = self.edPluginMTZDUMP.getDataOutput().getUnitCell()
        self.xsDataInput_PDBSET = XSDataInputPDBSETUnitCell()
        self.xsDataInput_PDBSET.setUnitCell(self.xsDataInput_inputUnitCell)
        self.xsDataInput_PDBSET.setInputPDBFile(self.xsDataInput_inputPDBFile)

        self.edPluginPDBSET = self.loadPlugin('EDPluginExecPDBSETUnitCellv10')
        self.edPluginPDBSET.setDataInput(self.xsDataInput_PDBSET)
        self.edPluginPDBSET.connectSUCCESS(self.doSuccess_PDBSET)
        self.edPluginPDBSET.connectFAILURE(self.doFailure_PDBSET)
        self.edPluginPDBSET.executeSynchronous()

    def doFailure_MTZDUMP(self, _edPlugin=None):
        """
        Method called after the MTZDUMPUnitCellSpaceGroup execution plugin has failed during it process processed.
        This is the place for doing error handling
        """
        EDVerbose.DEBUG("*** doFailure_MTZDUMP")

    def doSuccess_PDBSET(self, _edPlugin=None):
        """
        Method called when the PDBSETUnitCell execution plugin successfully processed, 
        it sets the output of the control plugin to be the output of control plugin. 
        """
        EDVerbose.DEBUG("*** doSuccess_PDBSET")
        xsDataResult_CopyUnitCellMTZtoPDB = XSDataResultCopyUnitCellMTZtoPDB()
        xsDataResult_CopyUnitCellMTZtoPDB.setOutputPDBFile(self.edPluginPDBSET.getDataOutput().getOutputPDBFile())
        self.setDataOutput(xsDataResult_CopyUnitCellMTZtoPDB)

    def doFailure_PDBSET(self, _edPlugin=None):
        """
        Method called after the PDBSETUnitCell execution plugin has failed during it's process.
        This is the place for doing error handling.
        """
        EDVerbose.DEBUG("*** doFailure_PDBSET")


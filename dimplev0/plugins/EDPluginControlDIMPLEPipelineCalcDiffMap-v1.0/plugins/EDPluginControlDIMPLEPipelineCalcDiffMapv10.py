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

from EDPluginControl import EDPluginControl

from XSDataCCP4DIMPLE import CCP4DataInputControlPipelineCalcDiffMap
from XSDataCCP4DIMPLE import CCP4DataResultControlPipelineCalcDiffMap
from XSDataCCP4DIMPLE import CCP4DataInputControlPrepareMTZFileForRefinement
from XSDataCCP4DIMPLE import CCP4DataResultControlPrepareMTZFileForRefinement
from XSDataCCP4DIMPLE import CCP4DataInputControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4DIMPLE import CCP4DataResultControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4DIMPLE import CCP4DataInputREFMACRigidBody
from XSDataCCP4DIMPLE import CCP4DataResultREFMACRigidBody
from XSDataCCP4DIMPLE import CCP4DataInputREFMACRestrainedRefinement
from XSDataCCP4DIMPLE import CCP4DataResultREFMACRestrainedRefinement
from XSDataCCP4DIMPLE import CCP4DataInputControlCopyUnitCellMTZtoPDB
from XSDataCCP4DIMPLE import CCP4DataResultControlCopyUnitCellMTZtoPDB
from XSDataCCP4DIMPLE import CCP4DataInputControlRefmacRigidBodyPhaser
from XSDataCCP4DIMPLE import CCP4DataInputCheckValidHKL
from XSDataCCP4DIMPLE import CCP4DataInputCheckValidXYZ
from XSDataCCP4DIMPLE import CCP4DataResultCheckValidHKL
from XSDataCCP4DIMPLE import CCP4DataResultCheckValidXYZ
from XSDataCCP4DIMPLE import CCP4DataInputPointlessOrigin
from XSDataCCP4DIMPLE import CCP4DataResultPointlessOrigin
from XSDataCCP4DIMPLE import CCP4MTZColLabels

from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginControlDIMPLEPipelineCalcDiffMapv10(EDPluginControl):
    '''A pipeline to compute a difference map from an intensity data file from
    e.g. fast_dp and a putative correct structure. Aim is for ligand
    identification.'''
    
    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(CCP4DataInputControlPipelineCalcDiffMap)

        # handles for the plugins I will use

        self._prepare_mtz_plugin = None
        self._prepare_pdb_plugin = None
        #self._rigidbody_plugin = None
        self._rigigbody_phaser_plugin = None
        self._restrained_plugin = None
        self._check_for_Validity_of_HKL = None
        self._check_for_Validity_of_XYZ = None
        self._pointless_origin_check = None

        # convenience handles

        self._hklin = None
        self._hklout = None
        self._xyzin = None
        self._xyzout = None

        self._ColLabels = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** PipelineCalcDiffMapv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),
                                      'Data Input is None')
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),
                                      "No input MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getHKLOUT(),
                                      "No output MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(),
                                      "No input PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getXYZOUT(),
                                      "No output PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getColLabels(),
                                      'No column labels specified (input)')

        return
    
    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG('*** PipelineCalcDiffMapv10.preProcess')

        # (1) copy out the information I need from the input files

        self.set_hklin(
            self.getDataInput().getHKLIN().getPath().getValue())
        self.set_hklout(
            self.getDataInput().getHKLOUT().getPath().getValue())
        self.set_xyzin(
            self.getDataInput().getXYZIN().getPath().getValue())
        self.set_xyzout(
            self.getDataInput().getXYZOUT().getPath().getValue())

        self._ColLabels = self.getDataInput().getColLabels()

        # (2) set up the plugins I will be wanting

        self._prepare_pdb_plugin = self.loadPlugin(
            'EDPluginControlDIMPLECopyUnitCellMTZtoPDBv10')

        self._prepare_mtz_plugin = self.loadPlugin(
            'EDPluginControlDIMPLEPrepareMTZFileForRefinementv10')

        #self._rigidbody_plugin = self.loadPlugin(
        #    'EDPluginExecDIMPLEREFMACRigidBodyv10')

        self._rigigbody_phaser_plugin = self.loadPlugin(
            'EDPluginControlDIMPLERefmacRigidBodyPhaserv10')

        self._restrained_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEREFMACRestrainedRefinementv10')

        self._check_for_Validity_of_HKL = self.loadPlugin(
            'EDPluginExecDIMPLECheckValidHKLv10')

        self._check_for_Validity_of_XYZ = self.loadPlugin(
            'EDPluginExecDIMPLECheckValidXYZv10')

        self._pointless_origin_check = self.loadPlugin(
            'EDPluginExecDIMPLEPointlessOriginv10'
        )

        # (3) check that the input file contains no unknown ligands -
        #     this should really move to being a plugin which is called
        #     at the start of the pipeline...

        self._check_input_pdb_monomers()

        return
        
    def process(self, _edObject = None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG('*** PipelineCalcDiffMapv10.process')

        
        #----------------------------------------------------------------------------
        # Verify that the input file self._hklin is actually an mtz file    
        self._check_for_Validity_of_HKL.setDataInput(CCP4DataInputCheckValidHKL(HKLIN=HKL(self._hklin)))
        self._check_for_Validity_of_HKL.connectSUCCESS(self._generic_success)
        self._check_for_Validity_of_HKL.connectFAILURE(self._generic_failure)
        self._check_for_Validity_of_HKL.executeSynchronous()
        returnStatusHKL = self._check_for_Validity_of_HKL.getDataOutput()
        if returnStatusHKL.getReturnStatus().getCode().getValue() == 0:
            raise RuntimeError, returnStatusHKL.getReturnStatus().getMessage().getValue()
            return        
        #----------------------------------------------------------------------------


        #----------------------------------------------------------------------------
        # Verify that the input file self._xyzin is actually a pdb file    
        self._check_for_Validity_of_XYZ.setDataInput(CCP4DataInputCheckValidXYZ(XYZIN=XYZ(self._xyzin)))
        self._check_for_Validity_of_XYZ.connectSUCCESS(self._generic_success)
        self._check_for_Validity_of_XYZ.connectFAILURE(self._generic_failure)
        self._check_for_Validity_of_XYZ.executeSynchronous()
        returnStatusXYZ = self._check_for_Validity_of_XYZ.getDataOutput()
        if returnStatusXYZ.getReturnStatus().getCode().getValue() == 0:
            raise RuntimeError, returnStatusXYZ.getReturnStatus().getMessage().getValue()
            return
        #----------------------------------------------------------------------------
        

        #----------------------------------------------------------------------------
        # Pointless Origin Check

        hklout = os.path.join(self.getWorkingDirectory(),
                              'pointlessOriginCheck.mtz')   

        self._pointless_origin_check.setDataInput(
            CCP4DataInputPointlessOrigin(
            HKLIN=HKL(self._hklin),
            XYZIN=XYZ(self._xyzin),
            HKLOUT=HKL(hklout)))

        self._pointless_origin_check.connectSUCCESS(self._generic_success)
        self._pointless_origin_check.connectFAILURE(self._generic_failure)

        self._pointless_origin_check.executeSynchronous()

        #----------------------------------------------------------------------------


        # first prepare the input reflection file


        hklin = hklout
        hklout = os.path.join(self.getWorkingDirectory(),
                              'prepared.mtz')     
        preparedmtz = hklout
        
        
        self._prepare_mtz_plugin.setDataInput(
            CCP4DataInputControlPrepareMTZFileForRefinement(
                XYZIN = XYZ(self._xyzin),
                HKLIN = HKL(hklin),
                HKLOUT = HKL(hklout),
                ColLabels = self._ColLabels))            

        self._prepare_mtz_plugin.connectSUCCESS(self._generic_success)
        self._prepare_mtz_plugin.connectFAILURE(self._generic_failure)

        self._prepare_mtz_plugin.executeSynchronous()


        # then prepare the input pdb file

        xyzout = os.path.join(self.getWorkingDirectory(),
                              'prepared.pdb')        

        self._prepare_pdb_plugin.setDataInput(
            CCP4DataInputControlCopyUnitCellMTZtoPDB(
            XYZIN = XYZ(self._xyzin),
            HKLIN = HKL(preparedmtz),
            XYZOUT = XYZ(xyzout)))

        self._prepare_pdb_plugin.connectSUCCESS(self._generic_success)
        self._prepare_pdb_plugin.connectFAILURE(self._generic_failure)

        self._prepare_pdb_plugin.executeSynchronous()


        # then run the rigid body refinement

        xyzin = xyzout
        hklin = hklout
        
        xyzout = os.path.join(self.getWorkingDirectory(),
                              'rigidbody.pdb')        

        self._rigigbody_phaser_plugin.setDataInput(
            CCP4DataInputControlRefmacRigidBodyPhaser(
            XYZIN = XYZ(xyzin),
            HKLIN = HKL(hklin),
            XYZOUT = XYZ(xyzout),
            ColLabels = self._prepare_mtz_plugin.getDataInput().getColLabels()))
            
            
        self._rigigbody_phaser_plugin.connectSUCCESS(self._generic_success)
        self._rigigbody_phaser_plugin.connectFAILURE(self._generic_failure)

        self._rigigbody_phaser_plugin.executeSynchronous()

        # and finally run the restrained refinement

        xyzin = xyzout

        self._restrained_plugin.setDataInput(
            CCP4DataInputREFMACRestrainedRefinement(
            XYZIN = XYZ(xyzin),
            HKLIN = HKL(hklin),
            XYZOUT = XYZ(self._xyzout),
            HKLOUT = HKL(self._hklout),            
            ColLabels = self._prepare_mtz_plugin.getDataInput().getColLabels()))
            
        self._restrained_plugin.connectSUCCESS(self._generic_success)
        self._restrained_plugin.connectFAILURE(self._generic_failure)

        self._restrained_plugin.executeSynchronous()

        return
    
    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG('*** PipelineCalcDiffMapv10.postProcess')

        results = self._restrained_plugin.getDataOutput()

        xsDataResult = CCP4DataResultControlPipelineCalcDiffMap(
            HKLOUT = HKL(self._hklout),
            XYZOUT = XYZ(self._xyzout),
            initialR = results.getInitialR(),
            initialRFree = results.getInitialRFree(),
            finalR = results.getFinalR(),
            finalRFree = results.getFinalRFree(),
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)            

        # and also produce a summary file? - first pull out the residuals

        refmac_out = self._restrained_plugin.readProcessLogFile().split('\n')

        residuals = { }
        collect_residuals = False

        for record in refmac_out:
            if '$TABLE: Rfactor analysis, stats vs cycle' in record:
                collect_residuals = True
                continue

            if not collect_residuals:
                continue

            if record.strip()[0] in '0123456789':
                tokens = record.split()
                cycle = int(tokens[0])
                r_rfree_fom = map(float, tokens[1:4])

                residuals[cycle] = r_rfree_fom

            if 'Final results' in record:
                collect_residuals = False

        # now need to write this someplace...

        summary = open(os.path.join(self.getWorkingDirectory(),
                                    'summary.log'), 'w')

        for c in sorted(residuals):
            summary.write('%2d %.4f %.4f %.3f\n' % (c, residuals[c][0],
                                                    residuals[c][1],
                                                    residuals[c][2]))

        summary.close()
        
        # Create a Coot script launcher
        self.createCootLauncher()
        
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

    def set_xyzin(self, xyzin):
        self._xyzin = xyzin
        return
    
    def get_xyzin(self):
        return self._xyzin

    def set_xyzout(self, xyzout):
        self._xyzout = xyzout
        return
    
    def get_xyzout(self):
        return self._xyzout

    # useless joiners

    def _generic_success(self, _edPlugin = None):
        '''Everything is hunky-sory, carry on.'''

        return

    def _generic_failure(self, _edPlugin = None):
        '''Something failed, sorry.'''

        raise RuntimeError, '%s failed' % _edPlugin.getPluginName()

    # useful functions which should be migrated to plugins

    def _check_input_pdb_monomers(self):
        '''Check that all of the monomers listed in the input PDB file
        occur in the CCP4 monomer dictionary.'''

        # first build up the database

        known_monomers = []

        monomer = os.path.join(os.environ['CCP4'], 'lib', 'data', 'monomers')

        for dirpath, dirnames, filenames in os.walk(monomer):
            for filename in filenames:
                known_monomers.append(filename.replace('.cif', ''))

        assert(known_monomers)

        # then check the pdb file

        unknown = []

        for record in open(self._xyzin):

            if 'ATOM  ' in record[:6] or 'HETATM' in record[:6]:
                residue = record[17:20].strip()

                if not residue in known_monomers:
                    unknown.append(residue)

        if unknown:
            unknown_residues = unknown[0]
            for m in unknown_residues[1:]:
                unknown_residues += ' %s' % m
            raise RuntimeError, 'Unknown residues: %s' % unknown_residues

        return
        
        
    def createCootLauncher(self):
        '''Create a launch script for Coot so that it will fire up with the 
        resulting MTZ and PDB from the job.'''
        
        EDVerbose.DEBUG('*** PipelineCalcDiffMapv10.createCootLauncher')

        # open the file
        cootScriptFile = os.path.join(self.getWorkingDirectory(),
                              'cootLauncher.sh')   

        file=open(cootScriptFile, "w") 
        file.write("#!/bin/sh\n")
        file.write("# Coot Launch script\n")
        file.write("#\n")
        file.write("\n")
        file.write("coot --pdb %s --auto %s --no-guano\n" % (self._xyzout, self._hklout))
        file.write("\n")

        file.close()

        # change the file permissions on the script
        os.chmod(cootScriptFile, 0774)

   
        
    
    

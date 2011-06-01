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

from XSDataCCP4DIMPLE import CCP4DataInputControlPrepareMTZFileForRefinement
from XSDataCCP4DIMPLE import CCP4DataResultControlPrepareMTZFileForRefinement
from XSDataCCP4DIMPLE import CCP4DataInputControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4DIMPLE import CCP4DataResultControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4DIMPLE import XSDataListOfStrings
from XSDataCCP4Factory import CCP4SpaceGroup
from XSDataCCP4Factory import CCP4ReindexingOperation
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import CCP4ResolutionLimit
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus

from XSDataCCP4DIMPLE import CCP4DataInputPDBDUMP
from XSDataCCP4DIMPLE import CCP4DataResultPDBDUMP
from XSDataCCP4DIMPLE import CCP4DataInputMTZDUMP
from XSDataCCP4DIMPLE import CCP4DataResultMTZDUMP
from XSDataCCP4DIMPLE import CCP4DataInputFREERFLAG
from XSDataCCP4DIMPLE import CCP4DataResultFREERFLAG
from XSDataCCP4DIMPLE import CCP4DataInputUNIQUE
from XSDataCCP4DIMPLE import CCP4DataResultUNIQUE
from XSDataCCP4DIMPLE import CCP4DataInputCAD
from XSDataCCP4DIMPLE import CCP4DataResultCAD
from XSDataCCP4DIMPLE import CCP4DataInputTRUNCATE
from XSDataCCP4DIMPLE import CCP4DataResultTRUNCATE
from XSDataCCP4DIMPLE import CCP4DataInputREINDEX
from XSDataCCP4DIMPLE import CCP4DataResultREINDEX
from XSDataCCP4DIMPLE import CCP4MTZColLabels

class EDPluginControlDIMPLEPrepareMTZFileForRefinementv10(EDPluginControl):
    '''A plugin to prepare the input reflection file from fast_dp for
    refinement with refmac. This will do the following:

    query pdb, get sequence (nres -> truncate) (spacegroup -> reindex)
    query mtz, get unit cell (+ spacegroup -> unique, freerflag)
    run truncate, copy in free column.'''

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(
            CCP4DataInputControlPrepareMTZFileForRefinement)

        # handles for the plugins

        self._copy_spacegroup_plugin = None
        self._truncate_plugin = None
        self._pdbdump_plugin = None
        self._mtzdump_plugin = None
        self._unique_plugin = None
        self._freerflag_plugin = None
        self._cad_plugin = None

        # then handles for the files

        self._xyzin = None
        self._hklin = None
        self._hklout = None

        self._ColLabels = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** PrepareMTZFileForRefinementv10.checkParameters')

        self.checkMandatoryParameters(self.getDataInput(),
                                      'Data Input is None')
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(),
                                      "No input PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),
                                      "No input MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getHKLOUT(),
                                      "No output MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getColLabels(),
                                      'No column labels specified (input)')
        return
    
    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG('*** PrepareMTZFileForRefinementv10.preProcess')

        # control plugins I will use

        self._copy_spacegroup_plugin = self.loadPlugin(
            'EDPluginControlDIMPLECopySpaceGroupPDBtoMTZv10')

        # read in the column labels
       
        self._ColLabels = self.getDataInput().getColLabels()

        # execute plugins I will use

        self._pdbdump_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEPDBDUMPv10')
        self._mtzdump_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEMTZDUMPv10')
        self._unique_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEUNIQUEv10')
        self._freerflag_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEFREERFLAGv10')
        self._cad_plugin = self.loadPlugin(
            'EDPluginExecDIMPLECADv10')
        self._truncate_plugin = self.loadPlugin(
            'EDPluginExecDIMPLETRUNCATEv10')

        self.set_xyzin(
            self.getDataInput().getXYZIN().getPath().getValue())
        self.set_hklin(
            self.getDataInput().getHKLIN().getPath().getValue())
        self.set_hklout(
            self.getDataInput().getHKLOUT().getPath().getValue())


        return

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG('*** PrepareMTZFileForRefinementv10.process')

        # ok, first query xyzin to get the space group for input to unique

        self._pdbdump_plugin.setDataInput(CCP4DataInputPDBDUMP(
            XYZIN = XYZ(self._xyzin)))

        self._pdbdump_plugin.connectSUCCESS(self._generic_success)
        self._pdbdump_plugin.connectFAILURE(self._generic_failure)

        self._pdbdump_plugin.executeSynchronous()

        dimple_spacegroup = self._pdbdump_plugin.getDataOutput(
            ).getSpaceGroup()
        dimple_sequence = self._pdbdump_plugin.getDataOutput(
            ).getSequence()

        # then query the mtz object for the cell constants &c.
        
        self._mtzdump_plugin.setDataInput(CCP4DataInputMTZDUMP(
            HKLIN = HKL(self._hklin)))

        self._mtzdump_plugin.connectSUCCESS(self._generic_success)
        self._mtzdump_plugin.connectFAILURE(self._generic_failure)

        self._mtzdump_plugin.executeSynchronous()

        mtzdump_results = self._mtzdump_plugin.getDataOutput()

        dimple_unitcell = mtzdump_results.getUnitCell()

        dimple_dmin = mtzdump_results.getUpperResolutionLimit()

        # then run unique with this

        hklout = os.path.join(self.getWorkingDirectory(),
                              'unique.mtz')

        self._unique_plugin.setDataInput(CCP4DataInputUNIQUE(
            HKLOUT = HKL(hklout),
            spaceGroup = dimple_spacegroup,
            unitCell = dimple_unitcell,
            resolutionLimit = dimple_dmin))

        self._unique_plugin.connectSUCCESS(self._generic_success)
        self._unique_plugin.connectFAILURE(self._generic_failure)

        self._unique_plugin.executeSynchronous()

        # and then freerflag on this one

        hklin = hklout
        hklout = os.path.join(self.getWorkingDirectory(),
                              'free.mtz')

        self._freerflag_plugin.setDataInput(CCP4DataInputFREERFLAG(
            HKLIN = HKL(hklin),
            HKLOUT = HKL(hklout)))

        self._freerflag_plugin.connectSUCCESS(self._generic_success)
        self._freerflag_plugin.connectFAILURE(self._generic_failure)

        self._freerflag_plugin.executeSynchronous()

        # then start processing the input reflection file - first copy
        # the spacegroup across, then run truncate, then cad together the
        # twain

        hklout = os.path.join(self.getWorkingDirectory(),
                              'spacegroup.mtz')

        self._copy_spacegroup_plugin.setDataInput(
            CCP4DataInputControlCopySpaceGroupPDBtoMTZ(
            HKLIN = HKL(self._hklin),
            XYZIN = HKL(self._xyzin),
            HKLOUT = HKL(hklout)))

        self._copy_spacegroup_plugin.connectSUCCESS(self._generic_success)
        self._copy_spacegroup_plugin.connectFAILURE(self._generic_failure)

        self._copy_spacegroup_plugin.executeSynchronous()

        # only run truncate if structure factors where not given in the input

        hklin = hklout
        hklout = os.path.join(self.getWorkingDirectory(),
                           'truncate.mtz')

        self._truncate_plugin.setDataInput(CCP4DataInputTRUNCATE(
            HKLIN = HKL(hklin),
            HKLOUT = HKL(hklout),
            sequence = dimple_sequence,
            ColLabels = self._ColLabels))            

        self._truncate_plugin.connectSUCCESS(self._generic_success)
        self._truncate_plugin.connectFAILURE(self._generic_failure)

        self._truncate_plugin.executeSynchronous()

        # cad together free.mtz and truncate.mtz

        hklin1 = os.path.join(self.getWorkingDirectory(),
                              'truncate.mtz')

        hklin2 = os.path.join(self.getWorkingDirectory(),
                              'free.mtz')

        self._cad_plugin.setDataInput(CCP4DataInputCAD(
            HKLIN = [HKL(hklin1),
                            HKL(hklin2)],
            columnLabels = [XSDataListOfStrings(), XSDataListOfStrings()],
            HKLOUT = HKL(self._hklout)))

        self._cad_plugin.connectSUCCESS(self._generic_success)
        self._cad_plugin.connectFAILURE(self._generic_failure)

        self._cad_plugin.executeSynchronous()
        
        # we should be all good by here - clean up perhaps?

        return
    
    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG('*** PrepareMTZFileForRefinementv10.postProcess')

        postProcessColLabels = self._truncate_plugin.getDataOutput().getColLabels()

        xsDataResult = CCP4DataResultControlPrepareMTZFileForRefinement(
            HKLOUT = HKL(self._hklout),
            ColLabels = postProcessColLabels,
            returnStatus = CCP4ReturnStatus())
        self.setDataOutput(xsDataResult)

    # getter / setter methods

    def set_xyzin(self, xyzin):
        self._xyzin = xyzin
        return
    
    def get_xyzin(self):
        return self._xyzin

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

    # useless joiners

    def _generic_success(self, _edPlugin = None):
        '''Everything is hunky-sory, carry on.'''

        return

    def _generic_failure(self, _edPlugin = None):
        '''Something failed, sorry.'''

        raise RuntimeError, '%s failed' % _edPlugin.getPluginName()


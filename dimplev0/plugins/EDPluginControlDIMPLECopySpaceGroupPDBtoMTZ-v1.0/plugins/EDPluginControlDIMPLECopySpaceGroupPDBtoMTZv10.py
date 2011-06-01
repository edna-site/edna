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

from XSDataCCP4DIMPLE import CCP4DataInputControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4DIMPLE import CCP4DataResultControlCopySpaceGroupPDBtoMTZ
from XSDataCCP4Factory import CCP4SpaceGroup
from XSDataCCP4Factory import CCP4ReindexingOperation
from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus

from XSDataCCP4DIMPLE import CCP4DataInputPDBDUMP
from XSDataCCP4DIMPLE import CCP4DataResultPDBDUMP
from XSDataCCP4DIMPLE import CCP4DataInputREINDEX
from XSDataCCP4DIMPLE import CCP4DataResultREINDEX

class EDPluginControlDIMPLECopySpaceGroupPDBtoMTZv10(EDPluginControl):
    '''A plugin to copy the spacegroup name from a PDB file to an MTZ.'''

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(CCP4DataInputControlCopySpaceGroupPDBtoMTZ)

        self._pdbdump_plugin = None
        self._reindex_plugin = None

        # handles for the input and output

        self._xyzin = None
        self._hklin = None
        self._hklout = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG(
            '*** CopySpaceGroupPDBtoMTZv10.checkParameters')

        self.checkMandatoryParameters(self.getDataInput(),
                                      "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(),
                                      "No input PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),
                                      "No input MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getHKLOUT(),
                                      "No output MTZ file given")

        return

    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10.preProcess')

        self._pdbdump_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEPDBDUMPv10')
        self._reindex_plugin = self.loadPlugin(
            'EDPluginExecDIMPLEREINDEXv10')

        self.set_xyzin(
            self.getDataInput().getXYZIN().getPath().getValue())
        self.set_hklin(
            self.getDataInput().getHKLIN().getPath().getValue())
        self.set_hklout(
            self.getDataInput().getHKLOUT().getPath().getValue())
        
        self._pdbdump_plugin.setDataInput(CCP4DataInputPDBDUMP(
            XYZIN = XYZ(self._xyzin)))

        return

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10.process')

        self._pdbdump_plugin.connectSUCCESS(self._success_pdbdump)
        self._pdbdump_plugin.connectFAILURE(self._failure_pdbdump)

        self._pdbdump_plugin.executeSynchronous()

        # copy out information from pdbdump, pack it into input
        # for reindex 

        self._reindex_plugin.connectSUCCESS(self._success_reindex)
        self._reindex_plugin.connectFAILURE(self._failure_reindex)
        
        self._reindex_plugin.executeSynchronous()

        return

    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10.postProcess')

        xsDataResult = CCP4DataResultControlCopySpaceGroupPDBtoMTZ(
            HKLOUT = HKL(self._hklout),
            returnStatus = CCP4ReturnStatus())            
        self.setDataOutput(xsDataResult)

        return

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

    # linker methods
    
    def _success_pdbdump(self,  _edPlugin = None):
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10._success_pdbdump')
        self.retrieveSuccessMessages(
            _edPlugin, 'CopySpaceGroupPDBtoMTZv10._success_pdbdump')

        # self._reindex_plugin.set_space_group_name(
        # self._pdbdump_plugin.get_space_group_name())
        
        reindex_input = CCP4DataInputREINDEX(
            HKLIN = HKL(self._hklin),
            HKLOUT = HKL(self._hklout),
            spaceGroup = self._pdbdump_plugin.getDataOutput().getSpaceGroup(),
            reindexingOperation = CCP4ReindexingOperation('h,k,l'))

        self._reindex_plugin.setDataInput(reindex_input)
        
        return

    def _failure_pdbdump(self,  _edPlugin = None):
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10._failure_pdbdump')
        self.retrieveFailureMessages(
            _edPlugin, 'CopySpaceGroupPDBtoMTZv10._failure_pdbdump')

        raise RuntimeError, 'pdbdump failed'

        return
                        
    def _success_reindex(self,  _edPlugin = None):
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10._success_reindex')
        self.retrieveSuccessMessages(
            _edPlugin, 'CopySpaceGroupPDBtoMTZv10._success_reindex')

        # all good...

        return

    def _failure_reindex(self,  _edPlugin = None):
        EDVerbose.DEBUG('*** CopySpaceGroupPDBtoMTZv10._failure_reindex')
        self.retrieveFailureMessages(
            _edPlugin, 'CopySpaceGroupPDBtoMTZv10._failure_reindex')

        raise RuntimeError, 'reindex failed'

        return
                        

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

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec

from XSDataCCP4DIMPLE import CCP4DataInputRefmacMonomerCheck
from XSDataCCP4DIMPLE import CCP4DataResultRefmacMonomerCheck
from XSDataCCP4Factory import CCP4ReturnStatus

import os

class EDPluginExecDIMPLERefmacMonomerCheckv10(EDPluginExec):
    """A plugin to verify that an input PDB file is fine."""
    

    def __init__(self ):
        EDPluginExec.__init__(self )
        self.setXSDataInputClass(CCP4DataInputRefmacMonomerCheck)

        return

    def checkParameters(self):
        EDVerbose.DEBUG(
            "EDPluginExecDIMPLERefmacMonomerCheckv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getXYZIN(),
                                      'No PDB file specified')
        
        return
    
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLERefmacMonomerCheckv10.postProcess")
        
        data = self.getDataInput()

        self._xyzin = data.getXYZIN().getPath().getValue()

        return
    
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLERefmacMonomerCheckv10.process")

        self._check_xyzin_monomers()

        return

    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLERefmacMonomerCheckv10.postProcess")

        xsDataResult = CCP4DataResultRefmacMonomerCheck(
            returnStatus = CCP4ReturnStatus())
        self.setDataOutput(xsDataResult)
    
        return

    def _check_xyzin_monomers(self):
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
        known = []

        for record in open(self._xyzin):

            if 'ATOM  ' in record[:6] or 'HETATM' in record[:6]:
                residue = record[17:20]

                if not residue in known_monomers:
                    if not residue in unknown:
                        unknown.append(residue)

                else:
                    if not residue in known:
                        known.append(residue)
                        EDVerbose.DEBUG("Known residue: %s" % residue)
                        
        if unknown:
            unknown_residues = unknown[0]
            for m in unknown_residues[1:]:
                unknown_residues += ' %s' % m
            raise RuntimeError, 'Unknown residues: %s' % unknown_residues

        return
        
        
    
        

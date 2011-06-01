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

from EDPluginExec import EDPluginExec

from XSDataCCP4DIMPLE import CCP4DataInputPDBDUMP
from XSDataCCP4DIMPLE import CCP4DataResultPDBDUMP

from XSDataCCP4Factory import CCP4Sequence
from XSDataCCP4Factory import CCP4SpaceGroup
from XSDataCCP4Factory import CCP4UnitCellTuple

class EDPluginExecDIMPLEPDBDUMPv10(EDPluginExec):
    '''An EDNA plugin to dump some metadata from a PDB file to allow
    comparison with metadata in an MTX file. In particular, returns
    information about the unit cell, space group and amino acid sequence.'''
    
    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(CCP4DataInputPDBDUMP)

        # some storage for things which I think will be helpful... accessed
        # via getter and setter methods defined below.
        self._xyzin = None

        # output results
        self._amino_acid_sequence = []
        self._unit_cell_constants = None
        self._space_group_name = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEPDBDUMPv10.checkParameters')

        # may have sent through the plugin overloader
        if self._xyzin:
            return

        self.checkMandatoryParameters(self.getDataInput(),
                                      'Data Input is None')
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(),
                                      'No input PDB file given')

        return
            
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEPDBDUMPv10.preProcess')

        self.set_xyzin(
            self.getDataInput().getXYZIN().getPath().getValue())

        EDVerbose.DEBUG('Obtained PDB file: %s' % self._xyzin)

        return

    def process(self, _edObject = None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEPDBDUMPv10.process')

        self.parse_pdb_get_sequence()
        self.parse_pdb_get_unit_cell_symmetry()
        self.programTermination()

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG( '*** EDPluginExecDIMPLEPDBDUMPv10.postProcess')

        xsDataResult = CCP4DataResultPDBDUMP(
            spaceGroup = self.get_space_group(),
            unitCell = self.get_unit_cell(),
            sequence = self.get_sequence())

        self.setDataOutput(xsDataResult)

        return

    # real working code...

    def set_xyzin(self, xyzin):
        self._xyzin = xyzin
        return

    def get_amino_acid_sequence(self):
        return self._amino_acid_sequence

    def get_unit_cell_constants(self):
        return self._unit_cell_constants

    def get_space_group_name(self):
        return self._space_group_name

    # edna'd versions

    def get_space_group(self):
        return CCP4SpaceGroup(self._space_group_name)

    def get_unit_cell(self):
        return CCP4UnitCellTuple(self._unit_cell_constants)

    def get_sequence(self):
        return CCP4Sequence(self._amino_acid_sequence)

    # real parsing code - based on documentation from the wwPDB:
    # 
    # http://www.wwpdb.org/documentation/format32/sec3.html#SEQRES
    # http://www.wwpdb.org/documentation/format32/sec8.html#CRYST1
    
    def parse_pdb_get_sequence(self):
        '''Actually read in the sequence information from the pdb file.'''

        for record in open(self._xyzin):
            if 'SEQRES' in record[:6]:
                for token in record[19:].split():
                    self._amino_acid_sequence.append(token)

        return

    def parse_pdb_get_unit_cell_symmetry(self):
        '''Actually read in the unit cell and symmetry information from the
        pdb file.'''

        for record in open(self._xyzin):
            if 'CRYST1' in record[:6]:
                self._unit_cell_constants = tuple(map(
                    float, record[6:54].split()))
                self._space_group_name = record[55:66].strip()
                
        return

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBDUMPv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                  PDBDUMP Output Log                  ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("PDB Unit Cell Dimenions:")
        self.addExecutiveSummaryLine("   a    : %.2lf" % self._unit_cell_constants[0])
        self.addExecutiveSummaryLine("   b    : %.2lf" % self._unit_cell_constants[1])
        self.addExecutiveSummaryLine("   c    : %.2lf" % self._unit_cell_constants[2])
        self.addExecutiveSummaryLine("   alpha: %.2lf" % self._unit_cell_constants[3])
        self.addExecutiveSummaryLine("   beta : %.2lf" % self._unit_cell_constants[4])
        self.addExecutiveSummaryLine("   gamma: %.2lf" % self._unit_cell_constants[5])
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("PDB Symmetry Information:")
        self.addExecutiveSummaryLine("   %s" % self._space_group_name)
        self.addExecutiveSummaryLine("")
        #self.addExecutiveSummaryLine("PDB Amino Acid Sequence:")
        #seq=self.get_sequence
        #self.addExecutiveSummaryLine("   %s" % self.get_sequence[0])
        #self.addExecutiveSummaryLine("")        
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End PDBDUMP Output Log                 ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()


    def programTermination(self):
        """
        Have all the data been collected?
        """
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEPDBDUMPv10.programTermination")
        if self._unit_cell_constants[0]==None or self._unit_cell_constants[1]==None or self._unit_cell_constants[2]==None or self._unit_cell_constants[3]==None or self._unit_cell_constants[4]==None or self._unit_cell_constants[5]==None or self._space_group_name==None:
            raise RuntimeError, "unit cell constants or space group name missing"





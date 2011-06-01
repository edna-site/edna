#!/usr/bin/env python
# 
#   Copyright (C) 2010 Diamond Light Source, Graeme Winter
#
#   This code is distributed under the LGPL license, a copy of which is 
#   included in the root directory of this package.
# 
# A factory for the classes shown in XSDataCCP4DIMPLE.py, to make them 
# more easily accessed. N.B. this includes CCTBX functionality to allow
# cleverer things to be done, for example automatic population of
# spacegroup information.

import sys

from cctbx.sgtbx import rt_mx as cctbx_rt_mx
from cctbx.sgtbx import space_group_symbols as cctbx_space_group_symbols
from cctbx.sgtbx import space_group as cctbx_space_group

from XSDataCCP4DIMPLE import XSDataFloat as _XSDataFloat
from XSDataCCP4DIMPLE import XSDataInteger as _XSDataInteger
from XSDataCCP4DIMPLE import XSDataString as _XSDataString
from XSDataCCP4DIMPLE import XSDataListOfStrings as \
     _XSDataListOfStrings

from XSDataCCP4DIMPLE import CCP4UnitCell as _CCP4UnitCell
from XSDataCCP4DIMPLE import CCP4RTMatrix as _CCP4RTMatrix
from XSDataCCP4DIMPLE import CCP4SymmetryOperation as _CCP4SymmetryOperation
from XSDataCCP4DIMPLE import CCP4SpaceGroup as _CCP4SpaceGroup
from XSDataCCP4DIMPLE import CCP4Sequence as _CCP4Sequence
from XSDataCCP4DIMPLE import CCP4ResolutionLimit as _CCP4ResolutionLimit
from XSDataCCP4DIMPLE import HKL as _HKL
from XSDataCCP4DIMPLE import XYZ as _XYZ
from XSDataCCP4DIMPLE import CCP4ReturnStatus as _CCP4ReturnStatus

def CCP4ListOfStrings(list_of_strings):
    '''Create a list of XSDataStrings as a XSDataListOfStrings.'''

    return _XSDataListOfStrings([XSDataString(s) for s in list_of_strings])

def CCP4UnitCellTuple(unit_cell):
    '''Create a CCP4 unit cell object from a list or tuple of 6 floats.'''

    assert(len(unit_cell) == 6)

    a, b, c, alpha, beta, gamma = tuple(unit_cell)
    
    return CCP4UnitCell(a, b, c, alpha, beta, gamma)

def CCP4UnitCell(a, b, c, alpha, beta, gamma):
    '''Usefully create a unit cell object from the Python floats for the
    cell constants. N.B. for reasons unclear this must first pun the floats.'''

    float_type = type(0.0)

    assert(type(a) is float_type)
    assert(type(b) is float_type)
    assert(type(c) is float_type)
    assert(type(alpha) is float_type)
    assert(type(beta) is float_type)
    assert(type(gamma) is float_type)

    _a = _XSDataFloat(a)
    _b = _XSDataFloat(b)
    _c = _XSDataFloat(c)
    _alpha = _XSDataFloat(alpha)
    _beta = _XSDataFloat(beta)
    _gamma = _XSDataFloat(gamma)

    return _CCP4UnitCell(a = _a, b = _b, c = _c,
                         alpha = _alpha, beta = _beta, gamma = _gamma)

def CCP4RTMatrix(e11, e12, e13,
                 e21, e22, e23,
                 e31, e32, e33,
                 e41, e42, e43):
    '''A useful constructor for RT matrices.'''
    
    float_type = type(0.0)

    assert(type(e11) is float_type)
    assert(type(e12) is float_type)
    assert(type(e13) is float_type)
    assert(type(e21) is float_type)
    assert(type(e22) is float_type)
    assert(type(e23) is float_type)
    assert(type(e31) is float_type)
    assert(type(e32) is float_type)
    assert(type(e33) is float_type)
    assert(type(e41) is float_type)
    assert(type(e42) is float_type)
    assert(type(e43) is float_type)

    _e11 = _XSDataFloat(e11)
    _e12 = _XSDataFloat(e12)
    _e13 = _XSDataFloat(e13)
    _e21 = _XSDataFloat(e21)
    _e22 = _XSDataFloat(e22)
    _e23 = _XSDataFloat(e23)
    _e31 = _XSDataFloat(e31)
    _e32 = _XSDataFloat(e32)
    _e33 = _XSDataFloat(e33)
    _e41 = _XSDataFloat(e41)
    _e42 = _XSDataFloat(e42)
    _e43 = _XSDataFloat(e43)

    return _CCP4RTMatrix(e11 = _e11,  e12 = _e12,  e13 = _e13,
                         e21 = _e21,  e22 = _e22,  e23 = _e23,
                         e31 = _e31,  e32 = _e32,  e33 = _e33,
                         e41 = _e41,  e42 = _e42,  e43 = _e43)

def CCP4SymmetryOperation(symmetry_operation):
    '''Construct a full CCP4 symmetry operation object from just the
    symop string, using CCTBX to calculate the corresponding matrix
    elements and assign.'''

    string_type = type(' ')

    assert(type(symmetry_operation) is string_type)

    op = cctbx_rt_mx(symmetry_operation)

    r = op.r().as_double()
    t = op.t().as_double()

    matrix = CCP4RTMatrix(r[0], r[1], r[2],
                          r[3], r[4], r[5],
                          r[6], r[7], r[8],
                          t[0], t[1], t[2])

    symop = _XSDataString(symmetry_operation)

    return _CCP4SymmetryOperation(symmetryOperation = symop,
                                  symmetryMatrix = matrix)

def CCP4ReindexingOperation(symmetry_operation):
    '''Construct a full CCP4 symmetry operation object from just the
    symop string, using CCTBX to calculate the corresponding matrix
    elements and assign. Punned from CCP4SymmetryOperation'''

    return CCP4SymmetryOperation(symmetry_operation)

def CCP4SpaceGroup(space_group_name):
    '''From a space group name, construct and populate a CCP4SpaceGroup
    object. N.B. that this will parse the spacegroup information from CCTBX
    to get the required information.'''

    string_type = type(' ')

    assert(type(space_group_name) is string_type)

    space_group_symbols = cctbx_space_group_symbols(space_group_name)
    space_group_number = space_group_symbols.number()
    space_group_name = space_group_symbols.hermann_mauguin()

    ccp4_space_group = _CCP4SpaceGroup(
        name = _XSDataString(space_group_name),
        number = _XSDataInteger(space_group_number))

    # now unpack and populate the symmetry operations

    space_group = cctbx_space_group(space_group_symbols)

    for ltr in space_group.ltr():
        for smx in space_group.smx():
            symop = smx + ltr
            ccp4_space_group.addSymmetryOperations(
                CCP4SymmetryOperation(symop.as_xyz()))

    return ccp4_space_group

def CCP4Sequence(aa_sequence):
    '''From a list of amino acids as three letter codes construct the
    one-letter code, number of residues and total mass.'''

    list_type = type([])

    assert(type(aa_sequence) is list_type)

    three_to_one = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q',
                    'LYS': 'K', 'ILE': 'I', 'PRO': 'P', 'THR': 'T',
                    'PHE': 'F', 'ALA': 'A', 'GLY': 'G', 'HIS': 'H',
                    'GLU': 'E', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                    'VAL': 'V', 'ASN': 'N', 'TYR': 'Y', 'MET': 'M',
                    'MSE': 'M'}

    three_to_mass = {'CYS': 121, 'ASP': 133, 'SER': 105, 'GLN': 146,
                     'LYS': 146, 'ASN': 132, 'PRO': 115, 'THR': 119,
                     'PHE': 165, 'ALA': 89,  'HIS': 155, 'GLY': 75,
                     'ILE': 131, 'LEU': 131, 'ARG': 174, 'TRP': 204,
                     'VAL': 117, 'GLU': 147, 'TYR': 181, 'MET': 149,
                     'MSE': 149}
    
    sequence = ''
    mass = 0
    number = 0

    for aa in aa_sequence:
        sequence += three_to_one[aa]
        mass += three_to_mass[aa]
        number += 1

    return _CCP4Sequence(oneLetterCode = _XSDataString(sequence),
                         numberOfResidues = _XSDataInteger(number),
                         molecularMass = _XSDataFloat(mass))

def CCP4ResolutionLimit(resolution_limit):
    '''Construct a resolution limit object.'''

    float_type = type(0.0)

    assert(type(resolution_limit) is float_type)

    return _CCP4ResolutionLimit(
        resolution = _XSDataFloat(resolution_limit))

def HKL(mtz_file):
    '''Construct a ccp4 mtz file object.'''

    string_type = type(' ')
    ustring_type = type(u' ')

    assert(type(mtz_file) in [string_type, ustring_type])

    return _HKL(path = _XSDataString(mtz_file))

def XYZ(pdb_file):
    '''Construct a ccp4 pdb file object.'''

    string_type = type(' ')
    ustring_type = type(u' ')

    assert(type(pdb_file) in [string_type, ustring_type])

    return _XYZ(path = _XSDataString(pdb_file))

def CCP4ReturnStatus(code = 0, message = ''):
    '''Generate a ccp4 return status - by default assumes all is well.'''

    integer_type = type(0)
    string_type = type(' ')
    
    assert(type(code) is integer_type)
    assert(type(message) is string_type)

    return _CCP4ReturnStatus(code = _XSDataInteger(code),
                             message = _XSDataString(message))

if __name__ == '__main__':

    ccp4_uc = CCP4UnitCell(10., 20., 30., 90., 90., 90.)
    ccp4_rt = CCP4RTMatrix(1., 2., 3.,
                           4., 5., 6.,
                           7., 8., 9.,
                           10., 11., 12.)
    ccp4_symop = CCP4SymmetryOperation('y,z,x')
    ccp4_space_group = CCP4SpaceGroup('I 23')
    ccp4_sequence = CCP4Sequence(['ALA', 'CYS'])
    ccp4_mtz_file = HKL('/tmp/foo.mtz')
    ccp4_return_status = CCP4ReturnStatus()

    # generate some useful XML input for the DIMPLEUNIQUE plugin - add
    # .export(sys.stdout, level = 0) to report as XML documents

    CCP4UnitCell(78.9, 78.9, 78.9, 90.0, 90.0, 90.0)
    CCP4SpaceGroup('I 21 3')
    CCP4ResolutionLimit(1.5)
    HKL('/tmp/unique.mtz')
    CCP4SpaceGroup('I 2 3')

    CCP4SymmetryOperation('x,y,z')

    CCP4Sequence(['GLY', 'ILE', 'VAL', 'GLU', 'GLN', 'CYS', 'CYS',
                  'THR', 'SER', 'VAL', 'CYS', 'SER', 'LEU', 'TYR',
                  'GLN', 'LEU', 'GLU', 'ASN', 'TYR', 'CYS', 'ASN',
                  'PHE', 'VAL', 'ASN', 'GLN', 'HIS', 'LEU', 'CYS',
                  'GLY', 'SER', 'HIS', 'LEU', 'VAL', 'GLU', 'ALA',
                  'LEU', 'TYR', 'LEU', 'VAL', 'CYS', 'GLY', 'GLU',
                  'ARG', 'GLY', 'PHE', 'PHE', 'TYR', 'THR', 'PRO',
                  'LYS', 'ALA'])


    

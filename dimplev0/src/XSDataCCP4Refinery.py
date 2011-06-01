#!/usr/bin/env python
# 
#   Copyright (C) 2010 Diamond Light Source, Graeme Winter
#
#   This code is distributed under the LGPL license, a copy of which is 
#   included in the root directory of this package.
# 
# A refinery for the classes shown in XSDataCCP4DIMPLE.py, to make them 
# more easily accessed. This is to extract useful information from very big
# EDNA lumps of XML.

def CCP4UnitCellTuple(ccp4_unit_cell):
    '''Take a CCP4 EDNA unit cell object, return a tuple of unit cell
    constants.'''

    a = ccp4_unit_cell.getA().getValue()
    b = ccp4_unit_cell.getB().getValue()
    c = ccp4_unit_cell.getC().getValue()
    alpha = ccp4_unit_cell.getAlpha().getValue()
    beta = ccp4_unit_cell.getBeta().getValue()
    gamma = ccp4_unit_cell.getGamma().getValue()

    float_type = type(0.0)

    assert(type(a) is float_type)
    assert(type(b) is float_type)
    assert(type(c) is float_type)
    assert(type(alpha) is float_type)
    assert(type(beta) is float_type)
    assert(type(gamma) is float_type)
    
    return (a, b, c, alpha, beta, gamma)


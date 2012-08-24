#!/usr/bin/env python
# -*- Coding: UTF8 -*-
#    File: "$Id$"
###########################################################################
# Written 2009-10-14 by Jerome Kieffer 
# Copyright (C) 2009 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Jerome Kieffer  (jerome.kieffer@esrf.fr)
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
#############################################################################



"""CIFfile is a library for manipulating Crystallographic information files and tries to conform to the specification of the IUCR  
"""

import os.path, sys, re, time, os, string, tempfile
SpaceGroups = [None, 'P 1', 'P -1', 'P 2', 'P 21', 'C 2',
'P m', 'P c', 'C m', 'C c', 'P 2/m',
'P 21/m', 'C 2/m', 'P 2/c', 'P 21/c', 'C 2/c',
'P 2 2 2', 'P 2 2 21', 'P 21 21 2', 'P 21 21 21', 'C 2 2 21',
'C 2 2 2', 'F 2 2 2', 'I 2 2 2', 'I 21 21 21', 'P m m 2',
'P m c 21', 'P c c 2', 'P m a 2', 'P c a 21', 'P n c 2',
'P m n 21', 'P b a 2', 'P n a 21', 'P n n 2', 'C m m 2',
'C m c 21', 'C c c 2', 'A m m 2', 'A b m 2', 'A m a 2',
'A b a 2', 'F m m 2', 'F d d 2', 'I m m 2', 'I b a 2',
'I m a 2', 'P m m m', 'P n n n', 'P c c m', 'P b a n',
'P m m a', 'P n n a', 'P m n a', 'P c c a', 'P b a m',
'P c c n', 'P b c m', 'P n n m', 'P m m n', 'P b c n',
'P b c a', 'P n m a', 'C m c m', 'C m c a', 'C m m m',
'C c c m', 'C m m a', 'C c c a', 'F m m m', 'F d d d',
'I m m m', 'I b a m', 'I b c a', 'I m m a', 'P 4',
'P 41', 'P 42', 'P 43', 'I 4', 'I 41',
'P -4', 'I -4', 'P 4/M', 'P 42/M', 'P 4/N',
'P 42/N', 'I 4/M', 'I 41/A', 'P 4 2 2', 'P 4 21 2',
'P 41 2 2', 'P 41 21 2', 'P 42 2 2', 'P 42 21 2', 'P 43 2 2',
'P 43 21 2', 'I 4 2 2', 'I 41 2 2', 'P 4 M M', 'P 4 B M',
'P 42 C M', 'P 42 N M', 'P 4 C C', 'P 4 N C', 'P 42 M C',
'P 42 B C', 'I 4 M M', 'I 4 C M', 'I 41 M D', 'I 41 C D',
'P -4 2 M', 'P -4 2 C', 'P -4 21 M', 'P -4 21 C', 'P -4 M 2',
'P -4 C 2', 'P -4 B 2', 'P -4 N 2', 'I -4 M 2', 'I -4 C 2',
'I -4 2 M', 'I -4 2 D', 'P 4/M M M', 'P 4/M C C', 'P 4/N B M',
'P 4/N N C', 'P 4/M B M', 'P 4/M N C', 'P 4/N M M', 'P 4/N C C',
'P 42/M M C', 'P 42/M C M', 'P 42/N B C', 'P 42/N N M', 'P 42/M B C',
'P 42/M N M', 'P 42/N M C', 'P 42/N C M', 'I 4/M M M', 'I 4/M C M',
'I 41/A M D', 'I 41/A C D', 'P 3', 'P 31', 'P 32',
'R 3', 'P -3', 'R -3', 'P 3 1 2', 'P 3 2 1',
'P 31 1 2', 'P 31 2 1', 'P 32 1 2', 'P 32 2 1', 'R 3 2',
'P 3 M 1', 'P 3 1 M', 'P 3 C 1', 'P 3 1 C', 'R 3 M',
'R 3 C', 'P -3 1 M', 'P -3 1 C', 'P -3 M 1', 'P -3 C 1',
'R -3 M', 'R -3 C', 'P 6', 'P 61', 'P 65',
'P 62', 'P 64', 'P 63', 'P -6', 'P 6/M',
'P 63/M', 'P 6 2 2', 'P 61 2 2', 'P 65 2 2', 'P 62 2 2',
'P 64 2 2', 'P 63 2 2', 'P 6 M M', 'P 6 C C', 'P 63 C M',
'P 63 M C', 'P -6 M 2', 'P -6 C 2', 'P -6 2 M', 'P -6 2 C',
'P 6/M M M', 'P 6/M C C', 'P 63/M C M', 'P 63/M M C', 'P 2 3',
'F 2 3', 'I 2 3', 'P 21 3', 'I 21 3', 'P M -3',
'P N -3', 'F M -3', 'F D -3', 'I M -3', 'P A -3',
'I A -3', 'P 4 3 2', 'P 42 3 2', 'F 4 3 2', 'F 41 3 2',
'I 4 3 2', 'P 43 3 2', 'P 41 3 2', 'I 41 3 2', 'P -4 3 M',
'F -4 3 M', 'I -4 3 M', 'P -4 3 N', 'F -4 3 C', 'I -4 3 D',
'P M -3 M', 'P N -3 N', 'P M -3 N', 'P N -3 M', 'F M -3 M',
'F M -3 C', 'F D -3 M', 'F D -3 C', 'I M -3 M', 'I A -3 D']

Symmetries = {"x,y,z": ['Triclinic', 'P 1'],
    "x,y,z;-x,-y,-z": ['Triclinic', 'P -1'],
    "x,y,z;-x,y+1/2,-z": ['Monoclinic', 'P 21'],
    "x,y,z;-x,y+1/2,-z+1/2;-x,-y,-z;x,-y+1/2,z+1/2": ['Monoclinic', 'P 21/c'],
    "x,y,z;-x,y+1/2,-z+1/2;-x,-y,-z;x,-y-1/2,z-1/2": ['Monoclinic', 'P 21/c'],
    "x,y,z;x,-y+1/2,z+1/2;-x,-y,-z;-x,y-1/2,-z-1/2": ['Monoclinic', 'P 21/c'],
    "x,y,z;-x+1/2,y+1/2,-z;-x,-y,-z;x+1/2,-y+1/2,z":['Monoclinic', 'P 21/a'],
    "x,y,z;-x+1/2,y+1/2,-z+1/2;-x,-y,-z;x-1/2,-y-1/2,z-1/2": ['Monoclinic', 'P 21/n'],
    "x,y,z;x+1/2,-y+1/2,z+1/2;-x,-y,-z;-x-1/2,y-1/2,-z-1/2": ['Monoclinic', 'P 21/n'],
    "x,y,z;-x+1/2,y+1/2,-z+1/2;-x,-y,-z;x+1/2,-y+1/2,z+1/2": ['Monoclinic', 'P 21/n'],
    "x,y,z;-x+1/2,y+1/2,-z;-x,-y,-z;x-1/2,-y-1/2,z": ['Monoclinic', 'P 21/a'],
    "x,y,z;x,-y,z+1/2;x+1/2,y+1/2,z;x+1/2,-y+1/2,z+1/2": ['Monoclinic', 'C c'],
    "x,y,z;-x,y,-z+1/2;x+1/2,y+1/2,z;-x+1/2,y+1/2,-z+1/2;-x,-y,-z;x,-y,z+1/2;-x+1/2,-y+1/2,-z;x+1/2,-y+1/2,z+1/2": ['Monoclinic', 'C 2/c'],
    "x,y,z;-x,y,-z+1/2;x+1/2,y+1/2,z;-x+1/2,y+1/2,-z+1/2;-x,-y,-z;x,-y,z-1/2;-x+1/2,-y+1/2,-z;x+1/2,-y+1/2,z-1/2": ['Monoclinic', 'C 2/c'],
    "x,y,z;-x,y,-z+1/2;-x,-y,-z;x,-y,z+1/2;x+1/2,y+1/2,z;-x+1/2,y+1/2,-z+1/2;-x+1/2,-y+1/2,-z;x+1/2,-y+1/2,z+1/2": ['Monoclinic', 'C 2/c'],
    "x,y,z;-x,y,-z;x+1/2,y+1/2,z;-x+1/2,y+1/2,-z": ['Monoclinic', 'C 2'],
    "x,y,z;x,-y,z+1/2": ['Monoclinic', 'P c'],
    "x,y,z;x+1/2,-y+1/2,z+1/2":['Monoclinic', 'P n'],
    "x,y,z;-x,y,-z;x+1/2,y+1/2,z+1/2;-x+1/2,y+1/2,-z+1/2": ['Monoclinic', 'I 2'],
    "x,y,z;-x,-y,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z": ['Orthorhombic', 'P 21 21 2'],
    "x,y,z;-x,-y,z;x+1/2,-y+1/2,-z;-x+1/2,y+1/2,-z": ['Orthorhombic', 'P 21 21 2'],
    "x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z": ['Orthorhombic', 'P 21 21 21'],
    "x,y,z;-x+1/2,-y,z+1/2;x+1/2,-y+1/2,-z;-x,y+1/2,-z+1/2": ['Orthorhombic', 'P 21 21 21'],
    "x,y,z;x+1/2,-y+1/2,-z;-x,y+1/2,-z+1/2;-x+1/2,-y,z+1/2":['Orthorhombic', 'P 21 21 21'],
    "x,y,z;-x,-y,z+1/2;-x+1/2,y+1/2,z+1/2;x+1/2,-y+1/2,z": ['Orthorhombic', 'P n a 21'],
    "x,y,z;-x,-y,z+1/2;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z+1/2": ['Orthorhombic', 'P n a 21'],
    "x,y,z;-x,-y,z+1/2;x+1/2,-y,z;-x+1/2,y,z+1/2": ['Orthorhombic', 'P c a 21'],
    "x,y,z;x+1/2,-y,-z;x,-y+1/2,z+1/2;x+1/2,y+1/2,-z+1/2": ['Orthorhombic', 'P 21 c n'],
    "x,y,z;x+1/2,-y,-z;x,y+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2": ['Orthorhombic', 'P 21 n b'],
    "x,y,z;x,-y+1/2,-z+1/2;-x+1/2,y+1/2,-z;-x+1/2,-y,z+1/2;-x,-y,-z;-x,y+1/2,z+1/2;x+1/2,-y+1/2,z;x+1/2,y,-z+1/2": ['Orthorhombic', 'P n a a'],
    "x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;-x,-y,-z;x+1/2,y,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y+1/2,z": ['Orthorhombic', 'P b c a'],
    "x,y,z;-x+1/2,-y+1/2,z;x+1/2,-y,-z+1/2;-x,y+1/2,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;-x+1/2,y,z+1/2;x,-y+1/2,z+1/2": ["Orthorhombic", "Pccn"],
    "x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;-x,-y,-z;x-1/2,y,-z-1/2;x,-y-1/2,z-1/2;-x-1/2,y-1/2,z": ['Orthorhombic', 'P b c a'],
    "x,y,z;x+1/2,-y+1/2,-z;-x,y+1/2,-z+1/2;-x+1/2,-y,z+1/2;-x,-y,-z;-x-1/2,y-1/2,z;x,-y-1/2,z-1/2;x-1/2,y,-z-1/2": ['Orthorhombic', 'P b c a'],
    "x,y,z;-x+1/2,-y,z+1/2;x+1/2,-y+1/2,-z;-x,y+1/2,-z+1/2;-x,-y,-z;x+1/2,y,-z+1/2;-x+1/2,y+1/2,z;x,-y+1/2,z+1/2":['Orthorhombic', 'P b c a'],
    "x,y,z;x,-y,-z;x,-y+1/2,z+1/2;x,y+1/2,-z+1/2;x+1/2,y+1/2,z;x+1/2,-y+1/2,-z;x+1/2,-y,z+1/2;x+1/2,y,-z+1/2": ['Orthorhombic', 'C 2 c b'],
    "x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3": ['Trigonal', 'P 31'],
    "x,y,z;-x,-y,z+1/2;-y,x,z+1/4;y,-x,z+3/4": ['Tetragonal', 'P 43'],
    "x,y,z;-x+1/2,-y,z+1/2;-y+3/4,x+1/4,z+1/4;y+3/4,-x+3/4,z+3/4;x+1/2,y+1/2,z+1/2;-x+1,-y+1/2,z+1;-y+5/4,x+3/4,z+3/4;y+5/4,-x+5/4,z+5/4;-x,-y,-z;x-1/2,y,-z-1/2;y-3/4,-x-1/4,-z-1/4;-y-3/4,x-3/4,-z-3/4;-x+1/2,-y+1/2,-z+1/2;x,y+1/2,-z;y-1/4,-x+1/4,-z+1/4;-y-1/4,x-1/4,-z-1/4": ['Tetragonal', 'I 41/a'],
    "x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x+1/3,y+2/3,z+2/3;-y+1/3,x+2/3,z+2/3;-x+1/3,-x+2/3,z+2/3;-x+1/3,-y+2/3,-z+2/3;y+1/3,-x+2/3,-z+2/3;x+1/3,x+2/3,-z+2/3;x+2/3,y+1/3,z+1/3;-y+2/3,x+1/3,z+1/3;-x+2/3,-x+1/3,z+1/3;-x+2/3,-y+1/3,-z+1/3;y+2/3,-x+1/3,-z+1/3;x+2/3,x+1/3,-z+1/3":['Trigonal', 'R -3'],
    "x,y,z;-y,x-y,z;-x+y,-x,z;x+2/3,y+1/3,z+1/3;-y+2/3,x-y+1/3,z+1/3;-x+y+2/3,-x+1/3,z+1/3;x+1/3,y+2/3,z+2/3;-y+1/3,x-y+2/3,z+2/3;-x+y+1/3,-x+2/3,z+2/3;-x,-y,-z;y,-x+y,-z;x-y,x,-z;-x+2/3,-y+1/3,-z+1/3;y+2/3,-x+y+1/3,-z+1/3;x-y+2/3,x+1/3,-z+1/3;-x+1/3,-y+2/3,-z+2/3;y+1/3,-x+y+2/3,-z+2/3;x-y+1/3,x+2/3,-z+2/3":['Trigonal', 'R -3'],

"x,y,z;-x,-y,-z" : [ "Triclinic"  , "P -1" ],
"x,y,z;-x,y,-z" : [ "Monoclinic"  , "P 2" ],
"x,y,z;-x,-y,z" : [ "Monoclinic"  , "P 2" ],
"x,y,z;-x,y+1/2,-z" : [ "Monoclinic"  , "P 21" ],
"x,y,z;-x,-y,z+1/2" : [ "Monoclinic"  , "P 21" ],
"x,y,z;x,-y,z" : [ "Monoclinic"  , "P m" ],
"x,y,z;x,y,-z" : [ "Monoclinic"  , "P m" ],
"x,y,z;x,-y,z+1/2" : [ "Monoclinic"  , "P c" ],
"x,y,z;x+1/2,-y,z+1/2" : [ "Monoclinic"  , "P c" ],
"x,y,z;x+1/2,-y,z" : [ "Monoclinic"  , "P c" ],
"x,y,z;x+1/2,y+1/2,-z" : [ "Monoclinic"  , "P c" ],
"x,y,z;x,y+1/2,-z" : [ "Monoclinic"  , "P c" ],
#"x,y,z;x+1/2,y,-z" : [ "Monoclinic"  , "C c" ],
"x,y,z;x,-y,z+1/2;x+1/2,y+1/2,z;x+1/2,-y+1/2,z+1/2":[ "Monoclinic"  , "C c" ],
"x,y,z;-x,y,-z;-x,-y,-z;x,-y,z" : [ "Monoclinic"  , "P 2/m" ],
"x,y,z;-x,-y,z;-x,-y,-z;x,y,-z" : [ "Monoclinic"  , "P 2/m" ],
"x,y,z;-x,y+1/2,-z;-x,-y,-z;x,-y+1/2,z" : [ "Monoclinic"  , "P 21/m" ],
"x,y,z;-x,-y,z+1/2;-x,-y,-z;x,y,-z+1/2" : [ "Monoclinic"  , "P 21/m" ],
"x,y,z;-x,y,-z+1/2;-x,-y,-z;x,-y,z+1/2" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x+1/2,y,-z+1/2;-x,-y,-z;x+1/2,-y,z+1/2" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x+1/2,y,-z;-x,-y,-z;x+1/2,-y,z" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x+1/2,-y,z;-x,-y,-z;x+1/2,y,-z" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x+1/2,-y+1/2,z;-x,-y,-z;x+1/2,y+1/2,-z" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x,-y+1/2,z;-x,-y,-z;x,y+1/2,-z" : [ "Monoclinic"  , "P 2/c" ],
"x,y,z;-x,y+1/2,-z+1/2;-x,-y,-z;x,-y+1/2,z+1/2" : [ "Monoclinic"  , "P 21/c" ],
"x,y,z;-x+1/2,y+1/2,-z;-x,-y,-z;x+1/2,-y+1/2,z" : [ "Monoclinic"  , "P 21/c" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,-y,-z;x+1/2,y,-z+1/2" : [ "Monoclinic"  , "P 21/c" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-x,-y,-z;x+1/2,y+1/2,-z+1/2" : [ "Monoclinic"  , "P 21/c" ],
"x,y,z;-x,-y+1/2,z+1/2;-x,-y,-z;x,y+1/2,-z+1/2" : [ "Monoclinic"  , "P 21/c" ],
"x,y,z;-x,y,-z;-x,-y,-z;x,-y,z;x+1/2,y+1/2,z;-x+1/2,y+1/2,-z;-x+1/2,-y+1/2,-z;x+1/2,-y+1/2,z":[ "Monoclinic"  , "C 2/m" ],
"x,y,z;x,-y,z;x+1/2,y+1/2,z;x+1/2,-y+1/2,z": [ "Monoclinic"  , "C m" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z" : [ "Orthorhombic"  , "P 2 2 2" ],
"x,y,z;-x,-y,z+1/2;-x,y,-z+1/2;x,-y,-z" : [ "Orthorhombic"  , "P 2 2 21" ],
"x,y,z;-x,-y,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z" : [ "Orthorhombic"  , "P 21 21 2" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z" : [ "Orthorhombic"  , "P 21 21 21" ],
"x,y,z;-x,-y,z;x,-y,z;-x,y,z" : [ "Orthorhombic"  , "P m m 2" ],
"x,y,z;-x,-y,z+1/2;x,-y,z+1/2;-x,y,z" : [ "Orthorhombic"  , "P m c 21" ],
"x,y,z;-x,-y,z;x,-y,z+1/2;-x,y,z+1/2" : [ "Orthorhombic"  , "P c c 2" ],
"x,y,z;-x,-y,z;x+1/2,-y,z;-x+1/2,y,z" : [ "Orthorhombic"  , "P m a 2" ],
"x,y,z;-x,-y,z+1/2;x+1/2,-y,z;-x+1/2,y,z+1/2" : [ "Orthorhombic"  , "P c a 21" ],
"x,y,z;-x,-y,z;x,-y+1/2,z+1/2;-x,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n c 2" ],
"x,y,z;-x+1/2,-y,z+1/2;x+1/2,-y,z+1/2;-x,y,z" : [ "Orthorhombic"  , "P m n 21" ],
"x,y,z;-x,-y,z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z" : [ "Orthorhombic"  , "P b a 2" ],
"x,y,z;-x,-y,z+1/2;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n a 21" ],
"x,y,z;-x,-y,z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n n 2" ],
"x,y,z;-x,-y,z;x,-y+1/2,z;-x,y+1/2,z" : [ "Orthorhombic"  , "A b m 2" ],
"x,y,z;-x,-y,z;x+1/4,-y+1/4,z+1/4;-x+1/4,y+1/4,z+1/4" : [ "Orthorhombic"  , "F d d 2" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;-x,-y,-z;x,y,-z;x,-y,z;-x,y,z" : [ "Orthorhombic"  , "P m m m" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n n n" ],
"x,y,z;-x+1/2,-y+1/2,z;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n n n" ],
"x,y,z;-x,-y,z;-x,y,-z+1/2;x,-y,-z+1/2;-x,-y,-z;x,y,-z;x,-y,z+1/2;-x,y,z+1/2" : [ "Orthorhombic"  , "P c c m" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z" : [ "Orthorhombic"  , "P b a n" ],
"x,y,z;-x+1/2,-y+1/2,z;-x+1/2,y,-z;x,-y+1/2,-z;-x,-y,-z;x+1/2,y+1/2,-z;x+1/2,-y,z;-x,y+1/2,z" : [ "Orthorhombic"  , "P b a n" ],
"x,y,z;-x+1/2,-y,z;-x,y,-z;x+1/2,-y,-z;-x,-y,-z;x+1/2,y,-z;x,-y,z;-x+1/2,y,z" : [ "Orthorhombic"  , "P m m a" ],
"x,y,z;-x+1/2,-y,z;-x+1/2,y+1/2,-z+1/2;x,-y+1/2,-z+1/2;-x,-y,-z;x+1/2,y,-z;x+1/2,-y+1/2,z+1/2;-x,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n n a" ],
"x,y,z;-x+1/2,-y,z+1/2;-x+1/2,y,-z+1/2;x,-y,-z;-x,-y,-z;x+1/2,y,-z+1/2;x+1/2,-y,z+1/2;-x,y,z" : [ "Orthorhombic"  , "P m n a" ],
"x,y,z;-x+1/2,-y,z;-x,y,-z+1/2;x+1/2,-y,-z+1/2;-x,-y,-z;x+1/2,y,-z;x,-y,z+1/2;-x+1/2,y,z+1/2" : [ "Orthorhombic"  , "P c c a" ],
"x,y,z;-x,-y,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;-x,-y,-z;x,y,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z" : [ "Orthorhombic"  , "P b a m" ],
"x,y,z;-x+1/2,-y+1/2,z;-x,y+1/2,-z+1/2;x+1/2,-y,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;x,-y+1/2,z+1/2;-x+1/2,y,z+1/2" : [ "Orthorhombic"  , "P c c n" ],
"x,y,z;-x,-y,z+1/2;-x,y+1/2,-z+1/2;x,-y+1/2,-z;-x,-y,-z;x,y,-z+1/2;x,-y+1/2,z+1/2;-x,y+1/2,z" : [ "Orthorhombic"  , "P b c m" ],
"x,y,z;-x,-y,z;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;-x,-y,-z;x,y,-z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n n m" ],
"x,y,z;-x,-y,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;x,-y,z;-x,y,z" : [ "Orthorhombic"  , "P m m n" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-x,y,-z+1/2;x+1/2,-y+1/2,-z;-x,-y,-z;x+1/2,y+1/2,-z+1/2;x,-y,z+1/2;-x+1/2,y+1/2,z" : [ "Orthorhombic"  , "P b c n" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;-x,-y,-z;x+1/2,y,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y+1/2,z" : [ "Orthorhombic"  , "P b c a" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z;x+1/2,-y+1/2,-z+1/2;-x,-y,-z;x+1/2,y,-z+1/2;x,-y+1/2,z;-x+1/2,y+1/2,z+1/2" : [ "Orthorhombic"  , "P n m a" ],
"x,y,z;-x,-y,z+1/2;-x,y,-z+1/2;x,-y,-z;-x,-y,-z;x,y,-z+1/2;x,-y,z+1/2;-x,y,z" : [ "Orthorhombic"  , "C m c m" ],
"x,y,z;-x,-y+1/2,z+1/2;-x,y+1/2,-z+1/2;x,-y,-z;-x,-y,-z;x,y+1/2,-z+1/2;x,-y+1/2,z+1/2;-x,y,z" : [ "Orthorhombic"  , "C m c a" ],
"x,y,z;-x,-y+1/2,z;-x,y+1/2,-z;x,-y,-z;-x,-y,-z;x,y+1/2,-z;x,-y+1/2,z;-x,y,z" : [ "Orthorhombic"  , "C m m a" ],
"x,y,z;-x+1/2,-y+1/2,z;-x,y,-z;x+1/2,-y+1/2,-z;-x,-y+1/2,-z+1/2;x+1/2,y,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y,z+1/2" : [ "Orthorhombic"  , "C c c a" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;-x+1/4,-y+1/4,-z+1/4;x+1/4,y+1/4,-z+1/4;x+1/4,-y+1/4,z+1/4;-x+1/4,y+1/4,z+1/4" : [ "Orthorhombic"  , "F d d d" ],
"x,y,z;-x+3/4,-y+3/4,z;-x+3/4,y,-z+3/4;x,-y+3/4,-z+3/4;-x,-y,-z;x+1/4,y+1/4,-z;x+1/4,-y,z+1/4;-x,y+1/4,z+1/4" : [ "Orthorhombic"  , "F d d d" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z" : [ "Tetragonal"  , "P 4" ],
"x,y,z;-x,-y,z+1/2;-y,x,z+1/4;y,-x,z+3/4" : [ "Tetragonal"  , "P 41" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2" : [ "Tetragonal"  , "P 42" ],
"x,y,z;-x,-y,z+1/2;-y,x,z+3/4;y,-x,z+1/4" : [ "Tetragonal"  , "P 43" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4" : [ "Tetragonal"  , "I 41" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z" : [ "Tetragonal"  , "P -4" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,-y,-z;x,y,-z;y,-x,-z;-y,x,-z" : [ "Tetragonal"  , "P4/m" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;-x,-y,-z;x,y,-z;y,-x,-z+1/2;-y,x,-z+1/2" : [ "Tetragonal"  , "P4(2)/m" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z;y+1/2,-x+1/2,z;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;y,-x,-z;-y,x,-z" : [ "Tetragonal"  , "P4/n" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z;y,-x+1/2,z;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z;-y,x+1/2,-z" : [ "Tetragonal"  , "P4/n" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y,-x,-z;-y,x,-z" : [ "Tetragonal"  , "P4(2)/n" ],
"x,y,z;-x+1/2,-y+1/2,z;-y,x+1/2,z+1/2;y+1/2,-x,z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;y,-x+1/2,-z+1/2;-y+1/2,x,-z+1/2" : [ "Tetragonal"  , "P4(2)/n" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;-x,-y+1/2,-z+1/4;x+1/2,y,-z+3/4;y,-x,-z;-y+1/2,x+1/2,-z+1/2" : [ "Tetragonal"  , "I4(1)/a" ],
"x,y,z;-x+1/2,-y,z+1/2;-y+3/4,x+1/4,z+1/4;y+3/4,-x+3/4,z+3/4;-x,-y,-z;x+1/2,y,-z+1/2;y+1/4,-x+3/4,-z+3/4;-y+1/4,x+1/4,-z+1/4" : [ "Tetragonal"  , "I4(1)/a" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,y,-z;x,-y,-z;y,x,-z;-y,-x,-z" : [ "Tetragonal"  , "P 4 2 2" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z;y+1/2,-x+1/2,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;y,x,-z;-y,-x,-z" : [ "Tetragonal"  , "P 4 21 2" ],
"x,y,z;-x,-y,z+1/2;-y,x,z+1/4;y,-x,z+3/4;-x,y,-z;x,-y,-z+1/2;y,x,-z+3/4;-y,-x,-z+1/4" : [ "Tetragonal"  , "P 41 2 2" ],
"x,y,z;-x,-y,z+1/2;-y+1/2,x+1/2,z+1/4;y+1/2,-x+1/2,z+3/4;-x+1/2,y+1/2,-z+1/4;x+1/2,-y+1/2,-z+3/4;y,x,-z;-y,-x,-z+1/2" : [ "Tetragonal"  , "P 41 21 2" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;-x,y,-z;x,-y,-z;y,x,-z+1/2;-y,-x,-z+1/2" : [ "Tetragonal"  , "P 42 2 2" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;y,x,-z;-y,-x,-z" : [ "Tetragonal"  , "P 42 21 2" ],
"x,y,z;-x,-y,z+1/2;-y,x,z+3/4;y,-x,z+1/4;-x,y,-z;x,-y,-z+1/2;y,x,-z+1/4;-y,-x,-z+3/4" : [ "Tetragonal"  , "P 43 2 2" ],
"x,y,z;-x,-y,z+1/2;-y+1/2,x+1/2,z+3/4;y+1/2,-x+1/2,z+1/4;-x+1/2,y+1/2,-z+3/4;x+1/2,-y+1/2,-z+1/4;y,x,-z;-y,-x,-z+1/2" : [ "Tetragonal"  , "P 43 21 2" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;-x+1/2,y,-z+3/4;x,-y+1/2,-z+1/4;y+1/2,x+1/2,-z+1/2;-y,-x,-z" : [ "Tetragonal"  , "I 41 2 2" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;x,-y,z;-x,y,z;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4mm" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4bm" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;x,-y,z+1/2;-x,y,z+1/2;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4(2)cm" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4(2)nm" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;x,-y,z+1/2;-x,y,z+1/2;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4cc" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4nc" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;x,-y,z;-x,y,z;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4(2)mc" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4(2)bc" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;x,-y,z;-x+1/2,y+1/2,z+1/2;-y,-x+1/2,z+1/4;y+1/2,x,z+3/4" : [ "Tetragonal"  , "I4(1)md" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;x,-y,z+1/2;-x+1/2,y+1/2,z;-y,-x+1/2,z+3/4;y+1/2,x,z+1/4" : [ "Tetragonal"  , "I4(1)cd" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;-x,y,-z;x,-y,-z;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P-42m" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;-x,y,-z+1/2;x,-y,-z+1/2;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P-42c" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P-42(1)m" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P-42(1)c" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;x,-y,z;-x,y,z;y,x,-z;-y,-x,-z" : [ "Tetragonal"  , "P-4m2" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;x,-y,z+1/2;-x,y,z+1/2;y,x,-z+1/2;-y,-x,-z+1/2" : [ "Tetragonal"  , "P-4c2" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;y+1/2,x+1/2,-z;-y+1/2,-x+1/2,-z" : [ "Tetragonal"  , "P-4b2" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2" : [ "Tetragonal"  , "P-4n2" ],
"x,y,z;-x,-y,z;y,-x,-z;-y,x,-z;-x+1/2,y,-z+3/4;x+1/2,-y,-z+3/4;-y+1/2,-x,z+3/4;y+1/2,x,z+3/4" : [ "Tetragonal"  , "I-42d" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,y,-z;x,-y,-z;y,x,-z;-y,-x,-z;-x,-y,-z;x,y,-z;y,-x,-z;-y,x,-z;x,-y,z;-x,y,z;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4/mmm" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,y,-z+1/2;x,-y,-z+1/2;y,x,-z+1/2;-y,-x,-z+1/2;-x,-y,-z;x,y,-z;y,-x,-z;-y,x,-z;x,-y,z+1/2;-x,y,z+1/2;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4/mcc" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,y,-z;x,-y,-z;y,x,-z;-y,-x,-z;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;y+1/2,-x+1/2,-z;-y+1/2,x+1/2,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4/nbm" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z;y,-x+1/2,z;-x+1/2,y,-z;x,-y+1/2,-z;y,x,-z;-y+1/2,-x+1/2,-z;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z;-y,x+1/2,-z;x+1/2,-y,z;-x,y+1/2,z;-y,-x,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4/nbm" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x,y,-z;x,-y,-z;y,x,-z;-y,-x,-z;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y+1/2,-x+1/2,-z+1/2;-y+1/2,x+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4/nnc" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z;y,-x+1/2,z;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;y,x,-z+1/2;-y+1/2,-x+1/2,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z;-y,x+1/2,-z;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2;-y,-x,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4/nnc" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;y+1/2,x+1/2,-z;-y+1/2,-x+1/2,-z;-x,-y,-z;x,y,-z;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4/mbm" ],
"x,y,z;-x,-y,z;-y,x,z;y,-x,z;-x+1/2,y+1/2,-z+1/2;x+1/2,-x+1/2,-z+1/2;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;-x,-y,-z;x,y,-z;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4/mnc" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z;y+1/2,-x+1/2,z;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;y,x,-z;-y,-x,-z;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;y,-x,-z;-y,x,-z;x,-y,z;-x,y,z;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4/nmm" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z;y,-x+1/2,z;-x,y+1/2,-z;x+1/2,-y,-z;y+1/2,x+1/2,-z;-y,-x,-z;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z;-y,x+1/2,-z;x,-y+1/2,z;-x+1/2,y,z;-y+1/2,-x+1/2,z;y,x,z" : [ "Tetragonal"  , "P4/nmm" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z;y+1/2,-x+1/2,z;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;y,x,-z+1/2;-y,-x,-z+1/2;-x+1/2,-y+1/2,-z;x+1/2,y+1/2,-z;y,-x,-z;-y,x,-z;x,-y,z+1/2;-x,y,z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4/ncc" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z;y,-x+1/2,z;-x,y+1/2,-z+1/2;x+1/2,-y,-z+1/2;y+1/2,x+1/2,-z+1/2;-y,-x,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z;-y,x+1/2,-z;x,-y+1/2,z+1/2;-x+1/2,y,z+1/2;-y+1/2,-x+1/2,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4/ncc" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;-x,y,-z;x,-y,-z;y,x,-z+1/2;-y,-x,-z+1/2;-x,-y,-z;x,y,-z;y,-x,-z+1/2;-y,x,-z+1/2;x,-y,z;-x,y,z;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4(2)/mmc" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;-x,y,-z+1/2;x,-y,-z+1/2;y,x,-z;-y,-x,-z;-x,-y,-z;x,y,-z;y,-x,-z+1/2;-y,x,-z+1/2;x,-y,z+1/2;-x,y,z+1/2;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4(2)/mcm" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x,y,-z+1/2;x,-y,-z+1/2;y+1/2,x+1/2,-z;-y+1/2,-x+1/2,-z;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y,-x,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4(2)/nbc" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z+1/2;y,-x+1/2,z+1/2;-x+1/2,y,-z;x,-y+1/2,-z;y,x,-z+1/2;-y+1/2,-x+1/2,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z+1/2;-y,x+1/2,-z+1/2;x+1/2,-y,z;-x,y+1/2,z;-y,-x,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4(2)/nbc" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x,y,-z;x,-y,-z;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y,-x,-z;-y,x,-z;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4(2)/nnm" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z+1/2;y,-x+1/2,z+1/2;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;y,x,-z;-y+1/2,-x+1/2,-z;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z+1/2;-y,x+1/2,-z+1/2;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2;-y,-x,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4(2)/nnm" ],
"x,y,z;-x,-y,z;-y,x,z+1/2;y,-x,z+1/2;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;-x,-y,-z;x,y,-z;y,-x,-z+1/2;-y,x,-z+1/2;x+1/2,-y+1/2,z;-x+1/2,y+1/2,z;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4(2)/mbc" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;y,x,-z;-y,-x,-z;-x,-y,-z;x,y,-z;y+1/2,-x+1/2,-z+1/2;-y+1/2,x+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-y,-x,z;y,x,z" : [ "Tetragonal"  , "P4(2)/mnm" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,-z+1/2;y,x,-z;-y,-x,-z;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y,-x,-z;-y,x,-z;x,-y,z;-x,y,z;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2" : [ "Tetragonal"  , "P4(2)/nmc" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z+1/2;y,-x+1/2,z+1/2;-x,y+1/2,-z;x+1/2,-y,-z;y+1/2,x+1/2,-z+1/2;-y,-x,-z+1/2;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z+1/2;-y,x+1/2,-z+1/2;x,-y+1/2,z;-x+1/2,y,z;-y+1/2,-x+1/2,z+1/2;y,x,z+1/2" : [ "Tetragonal"  , "P4(2)/nmc" ],
"x,y,z;-x,-y,z;-y+1/2,x+1/2,z+1/2;y+1/2,-x+1/2,z+1/2;-x+1/2,y+1/2,-z;x+1/2,-y+1/2,-z;y,x,-z+1/2;-y,-x,-z+1/2;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;y,-x,-z;-y,x,-z;x,-y,z+1/2;-x,y,z+1/2;-y+1/2,-x+1/2,z;y+1/2,x+1/2,z" : [ "Tetragonal"  , "P4(2)/ncm" ],
"x,y,z;-x+1/2,-y+1/2,z;-y+1/2,x,z+1/2;y,-x+1/2,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y,-z+1/2;y+1/2,x+1/2,-z;-y,-x,-z;-x,-y,-z;x+1/2,y+1/2,-z;y+1/2,-x,-z+1/2;-y,x+1/2,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y,z+1/2;-y+1/2,-x+1/2,z;y,x,z" : [ "Tetragonal"  , "P4(2)/ncm" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;-x+1/2,y,-z+3/4;x,-y+1/2,-z+1/4;y+1/2,x+1/2,-z+1/2;-y,-x,-z;-x,-y+1/2,-z+1/4;x+1/2,y,-z+3/4;y,-x,-z;-y+1/2,x+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x,y,z;-y+1/2,-x,z+3/4;y,x+1/2,z+1/4" : [ "Tetragonal"  , "I4(1)/amd" ],
"x,y,z;-x+1/2,-y,z+1/2;-y+1/4,x+3/4,z+1/4;y+1/4,-x+1/4,z+3/4;-x+1/2,y,-z+1/2;x,-y,-z;y+1/4,x+3/4,-z+1/4;-y+1/4,-x+1/4,-z+3/4;-x,-y,-z;x+1/2,y,-z+1/2;y+3/4,-x+1/4,-z+3/4;-y+3/4,x+3/4,-z+1/4;x+1/2,-y,z+1/2;-x,y,z;-y+3/4,-x+1/4,z+3/4;y+3/4,x+3/4,z+1/4" : [ "Tetragonal"  , "I4(1)/amd" ],
"x,y,z;-x+1/2,-y+1/2,z+1/2;-y,x+1/2,z+1/4;y+1/2,-x,z+3/4;-x+1/2,y,-z+1/4;x,-y+1/2,-z+3/4;y+1/2,x+1/2,-z;-y,-x,-z+1/2;-x,-y+1/2,-z+1/4;x+1/2,y,-z+3/4;y,-x,-z;-y+1/2,x+1/2,-z+1/2;x+1/2,-y+1/2,z;-x,y,z+1/2;-y+1/2,-x,z+1/4;y,x+1/2,z+3/4" : [ "Tetragonal"  , "I4(1)/acd" ],
"x,y,z;-x+1/2,-y,z+1/2;-y+1/4,x+3/4,z+1/4;y+1/4,-x+1/4,z+3/4;-x+1/2,y,-z;x,-y,-z+1/2;y+1/4,x+3/4,-z+3/4;-y+1/4,-x+1/4,-z+1/4;-x,-y,-z;x+1/2,y,-z+1/2;y+3/4,-x+1/4,-z+3/4;-y+3/4,x+3/4,-z+1/4;x+1/2,-y,z;-x,y,z+1/2;-y+3/4,-x+1/4,z+1/4;y+3/4,x+3/4,z+3/4" : [ "Tetragonal"  , "I4(1)/acd" ],
"x,y,z;-y,x-y,z;-x+y,-x,z" : [ "Trigonal"  , "P 3" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3" : [ "Trigonal"  , "P 31" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3" : [ "Trigonal"  , "P 32" ],
"x,y,z;z,x,y;y,z,x" : [ "Trigonal"  , "R 3" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,-z;y,-x+y,-z;x-y,x,-z" : [ "Trigonal"  , "P -3" ],
"x,y,z;z,x,y;y,z,x;-x,-y,-z;-z,-x,-y;-y,-z,-x" : [ "Trigonal"  , "R -3" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-y,-x,-z;-x+y,y,-z;x,x-y,-z" : [ "Trigonal"  , "P 3 1 2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;y,x,-z;x-y,-y,-z;-x,-x+y,-z" : [ "Trigonal"  , "P 3 2 1" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;-y,-x,-z+2/3;-x+y,y,-z+1/3;x,x-y,-z" : [ "Trigonal"  , "P 31 1 2" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;y,x,-z;x-y,-y,-z+2/3;-x,-x+y,-z+1/3" : [ "Trigonal"  , "P 31 2 1" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;-y,-x,-z+1/3;-x+y,y,-z+2/3;x,x-y,-z" : [ "Trigonal"  , "P 32 1 2" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;y,x,-z;x-y,-y,-z+1/3;-x,-x+y,-z+2/3" : [ "Trigonal"  , "P 32 2 1" ],
"x,y,z;z,x,y;y,z,x;-y,-x,-z;-x,-z,-y;-z,-y,-x" : [ "Trigonal"  , "R 3 2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-y,-x,z;-x+y,y,z;x,x-y,z" : [ "Trigonal"  , "P3m1" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Trigonal"  , "P31m" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2" : [ "Trigonal"  , "P3c1" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Trigonal"  , "P31c" ],
"x,y,z;z,x,y;y,z,x;y,x,z;x,z,y;z,y,x" : [ "Trigonal"  , "R3m" ],
"x,y,z;z,x,y;y,z,x;y+1/2,x+1/2,z+1/2;x+1/2,z+1/2,y+1/2;z+1/2,y+1/2,x+1/2" : [ "Trigonal"  , "R3c" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-y,-x,-z;-x+y,y,-z;x,x-y,-z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Trigonal"  , "P-31m" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-y,-x,-z+1/2;-x+y,y,-z+1/2;x,x-y,-z+1/2;-x,-y,-z;y,-x+y,-z;x-y,x,-z;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Trigonal"  , "P-31c" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;y,x,-z;x-y,-y,-z;-x,-x+y,-z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;-y,-x,z;-x+y,y,z;x,x-y,z" : [ "Trigonal"  , "P-3m1" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;y,x,-z+1/2;x-y,-y,-z+1/2;-x,-x+y,-z+1/2;-x,-y,-z;y,-x+y,-z;x-y,x,-z;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2" : [ "Trigonal"  , "P-3c1" ],
"x,y,z;z,x,y;y,z,x;-y,-x,-z;-x,-z,-y;-z,-y,-x;-x,-y,-z;-z,-x,-y;-y,-z,-x;y,x,z;x,z,y;z,y,x" : [ "Trigonal"  , "R-3m" ],
"x,y,z;z,x,y;y,z,x;-y+1/2,-x+1/2,-z+1/2;-x+1/2,-z+1/2,-y+1/2;-z+1/2,-y+1/2,-x+1/2;-x,-y,-z;-z,-x,-y;-y,-z,-x;y+1/2,x+1/2,z+1/2;x+1/2,z+1/2,y+1/2;z+1/2,y+1/2,x+1/2" : [ "Trigonal"  , "R-3c" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z" : [ "Hexagonal"  , "P 6" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;-x,-y,z+1/2;y,-x+y,z+5/6;x-y,x,z+1/6" : [ "Hexagonal"  , "P 61" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;-x,-y,z+1/2;y,-x+y,z+1/6;x-y,x,z+5/6" : [ "Hexagonal"  , "P 65" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;-x,-y,z;y,-x+y,z+2/3;x-y,x,z+1/3" : [ "Hexagonal"  , "P 62" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;-x,-y,z;y,-x+y,z+1/3;x-y,x,z+2/3" : [ "Hexagonal"  , "P 64" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2" : [ "Hexagonal"  , "P 63" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;x,y,-z;-y,x-y,-z;-x+y,-x,-z" : [ "Hexagonal"  , "P -6" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z;-y,x-y,-z;-x+y,-x,-z" : [ "Hexagonal"  , "P6/m" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z+1/2;-y,x-y,-z+1/2;-x+y,-x,-z+1/2" : [ "Hexagonal"  , "P6(3)/m" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;y,x,-z;x-y,-y,-z;-x,-x+y,-z;-y,-x,-z;-x+y,y,-z;x,x-y,-z" : [ "Hexagonal"  , "P 6 2 2" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;-x,-y,z+1/2;y,-x+y,z+5/6;x-y,x,z+1/6;y,x,-z+1/3;x-y,-y,-z;-x,-x+y,-z+2/3;-y,-x,-z+5/6;-x+y,y,-z+1/2;x,x-y,-z+1/6" : [ "Hexagonal"  , "P 61 2 2" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;-x,-y,z+1/2;y,-x+y,z+1/6;x-y,x,z+5/6;y,x,-z+2/3;x-y,-y,-z;-x,-x+y,-z+1/3;-y,-x,-z+1/6;-x+y,y,-z+1/2;x,x-y,-z+5/6" : [ "Hexagonal"  , "P 65 2 2" ],
"x,y,z;-y,x-y,z+2/3;-x+y,-x,z+1/3;-x,-y,z;y,-x+y,z+2/3;x-y,x,z+1/3;y,x,-z+2/3;x-y,-y,-z;-x,-x+y,-z+1/3;-y,-x,-z+2/3;-x+y,y,-z;x,x-y,-z+1/3" : [ "Hexagonal"  , "P 62 2 2" ],
"x,y,z;-y,x-y,z+1/3;-x+y,-x,z+2/3;-x,-y,z;y,-x+y,z+1/3;x-y,x,z+2/3;y,x,-z+1/3;x-y,-y,-z;-x,-x+y,-z+2/3;-y,-x,-z+1/3;-x+y,y,-z;x,x-y,-z+2/3" : [ "Hexagonal"  , "P 64 2 2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;y,x,-z;x-y,-y,-z;-x,-x+y,-z;-y,-x,-z+1/2;-x+y,y,-z+1/2;x,x-y,-z+1/2" : [ "Hexagonal"  , "P 63 2 2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;-y,-x,z;-x+y,y,z;x,x-y,z;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Hexagonal"  , "P6mm" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Hexagonal"  , "P6cc" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Hexagonal"  , "P6(3)cm" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;-y,-x,z;-x+y,y,z;x,x-y,z;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Hexagonal"  , "P6(3)mc" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;x,y,-z;-y,x-y,-z;-x+y,-x,-z;-y,-x,z;-x+y,y,z;x,x-y,z;-y,-x,-z;-x+y,y,-z;x,x-y,-z" : [ "Hexagonal"  , "P-6m2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;x,y,-z+1/2;-y,x-y,-z+1/2;-x+y,-x,-z+1/2;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2;-y,-x,-z;-x+y,y,-z;x,x-y,-z" : [ "Hexagonal"  , "P-6c2" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;x,y,-z;-y,x-y,-z;-x+y,-x,-z;y,x,-z;x-y,-y,-z;-x,-x+y,-z;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Hexagonal"  , "P-62m" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;x,y,-z+1/2;-y,x-y,-z+1/2;-x+y,-x,-z+1/2;y,x,-z;x-y,-y,-z;-x,-x+y,-z;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Hexagonal"  , "P-62c" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;y,x,-z;x-y,-y,-z;-x,-x+y,-z;-y,-x,-z;-x+y,y,-z;x,x-y,-z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z;-y,x-y,-z;-x+y,-x,-z;-y,-x,z;-x+y,y,z;x,x-y,z;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Hexagonal"  , "P6/mmm" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z;y,-x+y,z;x-y,x,z;y,x,-z+1/2;x-y,-y,-z+1/2;-x,-x+y,-z+1/2;-y,-x,-z+1/2;-x+y,y,-z+1/2;x,x-y,-z+1/2;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z;-y,x-y,-z;-x+y,-x,-z;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Hexagonal"  , "P6/mcc" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;y,x,-z+1/2;x-y,-y,-z+1/2;-x,-x+y,-z+1/2;-y,-x,-z;-x+y,y,-z;x,x-y,-z;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z+1/2;-y,x-y,-z+1/2;-x+y,-x,-z+1/2;-y,-x,z+1/2;-x+y,y,z+1/2;x,x-y,z+1/2;y,x,z;x-y,-y,z;-x,-x+y,z" : [ "Hexagonal"  , "P6(3)/mcm" ],
"x,y,z;-y,x-y,z;-x+y,-x,z;-x,-y,z+1/2;y,-x+y,z+1/2;x-y,x,z+1/2;y,x,-z;x-y,-y,-z;-x,-x+y,-z;-y,-x,-z+1/2;-x+y,y,-z+1/2;x,x-y,-z+1/2;-x,-y,-z;y,-x+y,-z;x-y,x,-z;x,y,-z+1/2;-y,x-y,-z+1/2;-x+y,-x,-z+1/2;-y,-x,z;-x+y,y,z;x,x-y,z;y,x,z+1/2;x-y,-y,z+1/2;-x,-x+y,z+1/2" : [ "Hexagonal"  , "P6(3)/mmc" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x" : [ "Cubic"  , "P 2 3" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2" : [ "Cubic"  , "P 21 3" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;-x,-y,-z;x,y,-z;x,-y,z;-x,y,z;-z,-x,-y;-z,x,y;z,x,-y;z,-x,y;-y,-z,-x;y,-z,x;-y,z,x;y,z,-x" : [ "Cubic"  , "Pm-3" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-z+1/2,-x+1/2,-y+1/2;-z+1/2,x+1/2,y+1/2;z+1/2,x+1/2,-y+1/2;z+1/2,-x+1/2,y+1/2;-y+1/2,-z+1/2,-x+1/2;y+1/2,-z+1/2,x+1/2;-y+1/2,z+1/2,x+1/2;y+1/2,z+1/2,-x+1/2" : [ "Cubic"  , "Pn-3" ],
"x,y,z;-x+1/2,-y+1/2,z;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;z,x,y;z,-x+1/2,-y+1/2;-z+1/2,-x+1/2,y;-z+1/2,x,-y+1/2;y,z,x;-y+1/2,z,-x+1/2;y,-z+1/2,-x+1/2;-y+1/2,-z+1/2,x;-x,-y,-z;x+1/2,y+1/2,-z;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2;-z,-x,-y;-z,x+1/2,y+1/2;z+1/2,x+1/2,-y;z+1/2,-x,y+1/2;-y,-z,-x;y+1/2,-z,x+1/2;-y,z+1/2,x+1/2;y+1/2,z+1/2,-x" : [ "Cubic"  , "Pn-3" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;-x+1/4,-y+1/4,-z+1/4;x+1/4,y+1/4,-z+1/4;x+1/4,-y+1/4,z+1/4;-x+1/4,y+1/4,z+1/4;-z+1/4,-x+1/4,-y+1/4;-z+1/4,x+1/4,y+1/4;z+1/4,x+1/4,-y+1/4;z+1/4,-x+1/4,y+1/4;-y+1/4,-z+1/4,-x+1/4;y+1/4,-z+1/4,x+1/4;-y+1/4,z+1/4,x+1/4;y+1/4,z+1/4,-x+1/4" : [ "Cubic"  , "Fd-3" ],
"x,y,z;-x+1/4,-y+1/4,z;-x+1/4,y,-z+1/4;x,-y+1/4,-z+1/4;z,x,y;z,-x+1/4,-y+1/4;-z+1/4,-x+1/4,y;-z+1/4,x,-y+1/4;y,z,x;-y+1/4,z,-x+1/4;y,-z+1/4,-x+1/4;-y+1/4,-z+1/4,x;-x,-y,-z;x+3/4,y+3/4,-z;x+3/4,-y,z+3/4;-x,y+3/4,z+3/4;-z,-x,-y;-z,x+3/4,y+3/4;z+3/4,x+3/4,-y;z+3/4,-x,y+3/4;-y,-z,-x;y+3/4,-z,x+3/4;-y,z+3/4,x+3/4;y+3/4,z+3/4,-x" : [ "Cubic"  , "Fd-3" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2;-x,-y,-z;x+1/2,y,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y+1/2,z;-z,-x,-y;-z+1/2,x+1/2,y;z+1/2,x,-y+1/2;z,-x+1/2,y+1/2;-y,-z,-x;y,-z+1/2,x+1/2;-y+1/2,z+1/2,x;y+1/2,z,-x+1/2" : [ "Cubic"  , "Pa-3" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y,x,-z;-y,-x,-z;y,-x,z;-y,x,z;x,z,-y;-x,z,y;-x,-z,-y;x,-z,y;z,y,-x;z,-y,x;-z,y,x;-z,-y,-x" : [ "Cubic"  , "P 4 3 2" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;y+1/2,-x+1/2,z+1/2;-y+1/2,x+1/2,z+1/2;x+1/2,z+1/2,-y+1/2;-x+1/2,z+1/2,y+1/2;-x+1/2,-z+1/2,-y+1/2;x+1/2,-z+1/2,y+1/2;z+1/2,y+1/2,-x+1/2;z+1/2,-y+1/2,x+1/2;-z+1/2,y+1/2,x+1/2;-z+1/2,-y+1/2,-x+1/2" : [ "Cubic"  , "P 42 3 2" ],
"x,y,z;-x,-y+1/2,z+1/2;-x+1/2,y+1/2,-z;x+1/2,-y,-z+1/2;z,x,y;z+1/2,-x,-y+1/2;-z,-x+1/2,y+1/2;-z+1/2,x+1/2,-y;y,z,x;-y+1/2,z+1/2,-x;y+1/2,-z,-x+1/2;-y,-z+1/2,x+1/2;y+3/4,x+1/4,-z+3/4;-y+1/4,-x+1/4,-z+1/4;y+1/4,-x+3/4,z+3/4;-y+3/4,x+3/4,z+1/4;x+3/4,z+1/4,-y+3/4;-x+3/4,z+3/4,y+1/4;-x+1/4,-z+1/4,-y+1/4;x+1/4,-z+3/4,y+3/4;z+3/4,y+1/4,-x+3/4;z+1/4,-y+3/4,x+3/4;-z+3/4,y+3/4,x+1/4;-z+1/4,-y+1/4,-x+1/4" : [ "Cubic"  , "F 41 3 2" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2;y+1/4,x+3/4,-z+3/4;-y+1/4,-x+1/4,-z+1/4;y+3/4,-x+3/4,z+1/4;-y+3/4,x+1/4,z+3/4;x+1/4,z+3/4,-y+3/4;-x+3/4,z+1/4,y+3/4;-x+1/4,-z+1/4,-y+1/4;x+3/4,-z+3/4,y+1/4;z+1/4,y+3/4,-x+3/4;z+3/4,-y+3/4,x+1/4;-z+3/4,y+1/4,x+3/4;-z+1/4,-y+1/4,-x+1/4" : [ "Cubic"  , "P 43 3 2" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2;y+3/4,x+1/4,-z+1/4;-y+3/4,-x+3/4,-z+3/4;y+1/4,-x+1/4,z+3/4;-y+1/4,x+3/4,z+1/4;x+3/4,z+1/4,-y+1/4;-x+1/4,z+3/4,y+1/4;-x+3/4,-z+3/4,-y+3/4;x+1/4,-z+1/4,y+3/4;z+3/4,y+1/4,-x+1/4;z+1/4,-y+1/4,x+3/4;-z+1/4,y+3/4,x+1/4;-z+3/4,-y+3/4,-x+3/4" : [ "Cubic"  , "P 41 3 2" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y,x,z;-y,-x,z;y,-x,-z;-y,x,-z;x,z,y;-x,z,-y;-x,-z,y;x,-z,-y;z,y,x;z,-y,-x;-z,y,-x;-z,-y,x" : [ "Cubic"  , "P-43m" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y+1/2,x+1/2,z+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,-x+1/2,-z+1/2;-y+1/2,x+1/2,-z+1/2;x+1/2,z+1/2,y+1/2;-x+1/2,z+1/2,-y+1/2;-x+1/2,-z+1/2,y+1/2;x+1/2,-z+1/2,-y+1/2;z+1/2,y+1/2,x+1/2;z+1/2,-y+1/2,-x+1/2;-z+1/2,y+1/2,-x+1/2;-z+1/2,-y+1/2,x+1/2" : [ "Cubic"  , "P-43n" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2;y+1/4,x+1/4,z+1/4;-y+1/4,-x+3/4,z+3/4;y+3/4,-x+1/4,-z+3/4;-y+3/4,x+3/4,-z+1/4;x+1/4,z+1/4,y+1/4;-x+3/4,z+3/4,-y+1/4;-x+1/4,-z+3/4,y+3/4;x+3/4,-z+1/4,-y+3/4;z+1/4,y+1/4,x+1/4;z+3/4,-y+1/4,-x+3/4;-z+3/4,y+3/4,-x+1/4;-z+1/4,-y+3/4,x+3/4" : [ "Cubic"  , "I-43d" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y,x,-z;-y,-x,-z;y,-x,z;-y,x,z;x,z,-y;-x,z,y;-x,-z,-y;x,-z,y;z,y,-x;z,-y,x;-z,y,x;-z,-y,-x;-x,-y,-z;x,y,-z;x,-y,z;-x,y,z;-z,-x,-y;-z,x,y;z,x,-y;z,-x,y;-y,-z,-x;y,-z,x;-y,z,x;y,z,-x;-y,-x,z;y,x,z;-y,x,-z;y,-x,-z;-x,-z,y;x,-z,-y;x,z,y;-x,z,-y;-z,-y,x;-z,y,-x;z,-y,-x;z,y,x" : [ "Cubic"  , "Pm-3m" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y,x,-z;-y,-x,-z;y,-x,z;-y,x,z;x,z,-y;-x,z,y;-x,-z,-y;x,-z,y;z,y,-x;z,-y,x;-z,y,x;-z,-y,-x;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-z+1/2,-x+1/2,-y+1/2;-z+1/2,x+1/2,y+1/2;z+1/2,x+1/2,-y+1/2;z+1/2,-x+1/2,y+1/2;-y+1/2,-z+1/2,-x+1/2;y+1/2,-z+1/2,x+1/2;-y+1/2,z+1/2,x+1/2;y+1/2,z+1/2,-x+1/2;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2;-y+1/2,x+1/2,-z+1/2;y+1/2,-x+1/2,-z+1/2;-x+1/2,-z+1/2,y+1/2;x+1/2,-z+1/2,-y+1/2;x+1/2,z+1/2,y+1/2;-x+1/2,z+1/2,-y+1/2;-z+1/2,-y+1/2,x+1/2;-z+1/2,y+1/2,-x+1/2;z+1/2,-y+1/2,-x+1/2;z+1/2,y+1/2,z+1/2" : [ "Cubic"  , "Pn-3n" ],
"x,y,z;-x+1/2,-y+1/2,z;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;z,x,y;z,-x+1/2,-y+1/2;-z+1/2,-x+1/2,y;-z+1/2,x,-y+1/2;y,z,x;-y+1/2,z,-x+1/2;y,-z+1/2,-x+1/2;-y+1/2,-z+1/2,x;y,x,-z+1/2;-y+1/2,-x+1/2,-z+1/2;y,-x+1/2,z;-y+1/2,x,z;x,z,-y+1/2;-x+1/2,z,y;-x+1/2,-z+1/2,-y+1/2;x,-z+1/2,y;z,y,-x+1/2;z,-y+1/2,x;-z+1/2,y,x;-z+1/2,-y+1/2,-x+1/2;-x,-y,-z;x+1/2,y+1/2,-z;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2;-z,-x,-y;-z,x+1/2,y+1/2;z+1/2,x+1/2,-y;z+1/2,-x,y+1/2;-y,-z,-x;y+1/2,-z,x+1/2;-y,z+1/2,x+1/2;y+1/2,z+1/2,-x;-y,-x,z+1/2;y+1/2,x+1/2,z+1/2;-y,x+1/2,-z;y+1/2,-x,-z;-x,-z,y+1/2;x+1/2,-z,-y;x+1/2,z+1/2,y+1/2;-x,z+1/2,-y;-z,-y,x+1/2;-z,y+1/2,-x;z+1/2,-y,-x;z+1/2,y+1/2,x+1/2" : [ "Cubic"  , "Pn-3n" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;y+1/2,-x+1/2,z+1/2;-y+1/2,x+1/2,z+1/2;x+1/2,z+1/2,-y+1/2;-x+1/2,z+1/2,y+1/2;-x+1/2,-z+1/2,-y+1/2;x+1/2,-z+1/2,y+1/2;z+1/2,y+1/2,-x+1/2;z+1/2,-y+1/2,x+1/2;-z+1/2,y+1/2,x+1/2;-z+1/2,-y+1/2,-x+1/2;-x,-y,-z;x,y,-z;x,-y,z;-x,y,z;-z,-x,-y;-z,x,y;z,x,-y;z,-x,y;-y,-z,-x;y,-z,x;-y,z,x;y,z,-x;-y+1/2,-x+1/2,z+1/2;y+1/2,x+1/2,z+1/2;-y+1/2,x+1/2,-z+1/2;y+1/2,-x+1/2,-z+1/2;-x+1/2,-z+1/2,y+1/2;x+1/2,-z+1/2,-y+1/2;x+1/2,z+1/2,y+1/2;-x+1/2,z+1/2,-y+1/2;-z+1/2,-y+1/2,x+1/2;-z+1/2,y+1/2,-x+1/2;z+1/2,-y+1/2,-x+1/2;z+1/2,y+1/2,x+1/2" : [ "Cubic"  , "Pm-3n" ],
"x,y,z;-x,-y,z;-x,y,-z;x,-y,-z;z,x,y;z,-x,-y;-z,-x,y;-z,x,-y;y,z,x;-y,z,-x;y,-z,-x;-y,-z,x;y+1/2,x+1/2,-z+1/2;-y+1/2,-x+1/2,-z+1/2;y+1/2,-x+1/2,z+1/2;-y+1/2,x+1/2,z+1/2;x+1/2,z+1/2,-y+1/2;-x+1/2,z+1/2,y+1/2;-x+1/2,-z+1/2,-y+1/2;x+1/2,-z+1/2,y+1/2;z+1/2,y+1/2,-x+1/2;z+1/2,-y+1/2,x+1/2;-z+1/2,y+1/2,x+1/2;-z+1/2,-y+1/2,-x+1/2;-x+1/2,-y+1/2,-z+1/2;x+1/2,y+1/2,-z+1/2;x+1/2,-y+1/2,z+1/2;-x+1/2,y+1/2,z+1/2;-z+1/2,-x+1/2,-y+1/2;-z+1/2,x+1/2,y+1/2;z+1/2,x+1/2,-y+1/2;z+1/2,-x+1/2,y+1/2;-y+1/2,-z+1/2,-x+1/2;y+1/2,-z+1/2,x+1/2;-y+1/2,z+1/2,x+1/2;y+1/2,z+1/2,-x+1/2;-y,-x,z;y,x,z;-y,x,-z;y,-x,-z;-x,-z,y;x,-z,-y;x,z,y;-x,z,-y;-z,-y,x;-z,y,-x;z,-y,-x;z,y,x" : [ "Cubic"  , "Pn-3m" ],
"x,y,z;-x+1/2,-y+1/2,z;-x+1/2,y,-z+1/2;x,-y+1/2,-z+1/2;z,x,y;z,-x+1/2,-y+1/2;-z+1/2,-x+1/2,y;-z+1/2,x,-y+1/2;y,z,x;-y+1/2,z,-x+1/2;y,-z+1/2,-x+1/2;-y+1/2,-z+1/2,x;y+1/2,x+1/2,-z;-y,-x,-z;y+1/2,-x,z+1/2;-y,x+1/2,z+1/2;x+1/2,z+1/2,-y;-x,z+1/2,y+1/2;-x,-z,-y;x+1/2,-z,y+1/2;z+1/2,y+1/2,-x;z+1/2,-y,x+1/2;-z,y+1/2,x+1/2;-z,-y,-x;-x,-y,-z;x+1/2,y+1/2,-z;x+1/2,-y,z+1/2;-x,y+1/2,z+1/2;-z,-x,-y;-z,x+1/2,y+1/2;z+1/2,x+1/2,-y;z+1/2,-x,y+1/2;-y,-z,-x;y+1/2,-z,x+1/2;-y,z+1/2,x+1/2;y+1/2,z+1/2,-x;-y+1/2,-x+1/2,z;y,x,z;-y+1/2,x,-z+1/2;y,-x+1/2,-z+1/2;-x+1/2,-z+1/2,y;x,-z+1/2,-y+1/2;x,z,y;-x+1/2,z,-y+1/2;-z+1/2,-y+1/2,x;-z+1/2,y,-x+1/2;z,-y+1/2,-x+1/2;z,y,x" : [ "Cubic"  , "Pn-3m" ],
"x,y,z;-x,-y+1/2,z+1/2;-x+1/2,y+1/2,-z;x+1/2,-y,-z+1/2;z,x,y;z+1/2,-x,-y+1/2;-z,-x+1/2,y+1/2;-z+1/2,x+1/2,-y;y,z,x;-y+1/2,z+1/2,-x;y+1/2,-z,-x+1/2;-y,-z+1/2,x+1/2;y+3/4,x+1/4,-z+3/4;-y+1/4,-x+1/4,-z+1/4;y+1/4,-x+3/4,z+3/4;-y+3/4,x+3/4,z+1/4;x+3/4,z+1/4,-y+3/4;-x+3/4,z+3/4,y+1/4;-x+1/4,-z+1/4,-y+1/4;x+1/4,-z+3/4,y+3/4;z+3/4,y+1/4,-x+3/4;z+1/4,-y+3/4,x+3/4;-z+3/4,y+3/4,x+1/4;-z+1/4,-y+1/4,-x+1/4;-x+1/4,-y+1/4,-z+1/4;x+1/4,y+3/4,-z+3/4;x+3/4,-y+3/4,z+1/4;-x+3/4,y+1/4,z+3/4;-z+1/4,-x+1/4,-y+1/4;-z+3/4,x+1/4,y+3/4;z+1/4,x+3/4,-y+3/4;z+3/4,-x+3/4,y+1/4;-y+1/4,-z+1/4,-x+1/4;y+3/4,-z+3/4,x+1/4;-y+3/4,z+1/4,x+3/4;y+1/4,z+3/4,-x+3/4;-y+1/2,-x,z+1/2;y,x,z;-y,x+1/2,-z+1/2;y+1/2,-x+1/2,-z;-x+1/2,-z,y+1/2;x+1/2,-z+1/2,-y;x,z,y;-x,z+1/2,-y+1/2;-z+1/2,-y,x+1/2;-z,y+1/2,-x+1/2;z+1/2,-y+1/2,-x;z,y,x" : [ "Cubic"  , "Fd-3m" ],
"x,y,z;-x+3/4,-y+1/4,z+1/2;-x+1/4,y+1/2,-z+3/4;x+1/2,-y+3/4,-z+1/4;z,x,y;z+1/2,-x+3/4,-y+1/4;-z+3/4,-x+1/4,y+1/2;-z+1/4,x+1/2,-y+3/4;y,z,x;-y+1/4,z+1/2,-x+3/4;y+1/2,-z+3/4,-x+1/4;-y+3/4,-z+1/4,x+1/2;y+3/4,x+1/4,-z+1/2;-y,-x,-z;y+1/4,-x+1/2,z+3/4;-y+1/2,x+3/4,z+1/4;x+3/4,z+1/4,-y+1/2;-x+1/2,z+3/4,y+1/4;-x,-z,-y;x+1/4,-z+1/2,y+3/4;z+3/4,y+1/4,-x+1/2;z+1/4,-y+1/2,x+3/4;-z+1/2,y+3/4,x+1/4;-z,-y,-x;-x,-y,-z;x+1/4,y+3/4,-z+1/2;x+3/4,-y+1/2,z+1/4;-x+1/2,y+1/4,z+3/4;-z,-x,-y;-z+1/2,x+1/4,y+3/4;z+1/4,x+3/4,-y+1/2;z+3/4,-x+1/2,y+1/4;-y,-z,-x;y+3/4,-z+1/2,x+1/4;-y+1/2,z+1/4,x+3/4;y+1/4,z+3/4,-x+1/2;-y+1/4,-x+3/4,z+1/2;y,x,z;-y+3/4,x+1/2,-z+1/4;y+1/2,-x+1/4,-z+3/4;-x+1/4,-z+3/4,y+1/2;x+1/2,-z+1/4,-y+3/4;x,z,y;-x+3/4,z+1/2,-y+1/4;-z+1/4,-y+3/4,x+1/2;-z+3/4,y+1/2,-x+1/4;z+1/2,-y+1/4,-x+3/4;z,y,x" : [ "Cubic"  , "Fd-3m" ],
"x,y,z;-x,-y+1/2,z+1/2;-x+1/2,y+1/2,-z;x+1/2,-y,-z+1/2;z,x,y;z+1/2,-x,-y+1/2;-z,-x+1/2,y+1/2;-z+1/2,x+1/2,-y;y,z,x;-y+1/2,z+1/2,-x;y+1/2,-z,-x+1/2;-y,-z+1/2,x+1/2;y+3/4,x+1/4,-z+3/4;-y+1/4,-x+1/4,-z+1/4;y+1/4,-x+3/4,z+3/4;-y+3/4,x+3/4,z+1/4;x+3/4,z+1/4,-y+3/4;-x+3/4,z+3/4,y+1/4;-x+1/4,-z+1/4,-y+1/4;x+1/4,-z+1/4,y+3/4;z+3/4,y+1/4,-x+3/4;z+1/4,-y+3/4,x+3/4;-z+3/4,y+3/4,x+1/4;-z+1/4,-y+1/4,-x+1/4;-x+3/4,-y+3/4,-z+3/4;x+3/4,y+1/4,-z+1/4;x+1/4,-y+1/4,z+3/4;-x+1/4,y+3/4,z+1/4;-z+3/4,-x+3/4,-y+3/4;-z+1/4,x+3/4,y+1/4;z+3/4,x+1/4,-y+1/4;z+1/4,-x+1/4,y+3/4;-y+3/4,-z+3/4,-x+3/4;y+1/4,-z+1/4,x+3/4;-y+1/4,z+3/4,x+1/4;y+3/4,z+1/4,-x+1/4;-y,-x+1/2,z;y+1/2,x+1/2,z+1/2;-y+1/2,x,-z;y,-x,-z+1/2;-x,-z+1/2,y;x,-z,-y+1/2;x+1/2,z+1/2,y+1/2;-x+1/2,z,-y;-z,-y+1/2,x;-z+1/2,y,-x;z,-y,-x+1/2;z+1/2,y+1/2,x+1/2" : [ "Cubic"  , "Fd-3c" ],
"x,y,z;-x+1/4,-y+3/4,z+1/2;-x+3/4,y+1/2,-z+1/4;x+1/2,-y+1/4,-z+3/4;z,x,y;z+1/2,-x+1/4,-y+3/4;-z+1/4,-x+3/4,y+1/2;-z+3/4,x+1/2,-y+1/4;y,z,x;-y+3/4,z+1/2,-x+1/4;y+1/2,-z+1/4,-x+3/4;-y+1/4,-z+3/4,x+1/2;y+3/4,x+1/4,-z;-y+1/2,-x+1/2,-z+1/2;y+1/4,-x,z+3/4;-y,x+3/4,z+1/4;x+3/4,z+1/4,-y;-x,z+3/4,y+1/4;-x+1/2,-z+1/2,-y+1/2;x+1/4,-z,y+3/4;z+3/4,y+1/4,-x;z+1/4,-y,x+3/4;-z,y+3/4,x+1/4;-z+1/2,-y+1/2,-x+1/2;-x,-y,-z;x+3/4,y+1/4,-z+1/2;x+1/4,-y+1/2,z+3/4;-x+1/2,y+3/4,z+1/4;-z,-x,-y;-z+1/2,x+3/4,y+1/4;z+3/4,x+1/4,-y+1/2;z+1/4,-x+1/2,y+3/4;-y,-z,-x;y+1/4,-z+1/2,x+3/4;-y+1/2,z+3/4,x+1/4;y+3/4,z+1/4,-x+1/2;-y+1/4,-x+3/4,z;y+1/2,x+1/2,z+1/2;-y+3/4,x,-z+1/4;y,-x+1/4,-z+3/4;-x+1/4,-z+3/4,y;x,-z+1/4,-y+3/4;x+1/2,z+1/2,y+1/2;-x+3/4,z,-y+1/4;-z+1/4,-y+3/4,x;-z+3/4,y,-x+1/4;z,-y+1/4,-x+3/4;z+1/2,y+1/2,x+1/2" : [ "Cubic"  , "Fd-3c" ],
"x,y,z;-x+1/2,-y,z+1/2;-x,y+1/2,-z+1/2;x+1/2,-y+1/2,-z;z,x,y;z+1/2,-x+1/2,-y;-z+1/2,-x,y+1/2;-z,x+1/2,-y+1/2;y,z,x;-y,z+1/2,-x+1/2;y+1/2,-z+1/2,-x;-y+1/2,-z,x+1/2;y+3/4,x+1/4,-z+1/4;-y+3/4,-x+3/4,-z+3/4;y+1/4,-x+1/4,z+3/4;-y+1/4,x+3/4,z+1/4;x+3/4,z+1/4,-y+1/4;-x+1/4,z+3/4,y+1/4;-x+3/4,-z+3/4,-y+3/4;x+1/4,-z+1/4,y+3/4;z+3/4,y+1/4,-x+1/4;z+1/4,-y+1/4,x+3/4;-z+1/4,y+3/4,x+1/4;-z+3/4,-y+3/4,-x+3/4;-x,-y,-z;x+1/2,y,-z+1/2;x,-y+1/2,z+1/2;-x+1/2,y+1/2,z;-z,-x,-y;-z+1/2,x+1/2,y;z+1/2,x,-y+1/2;z,-x+1/2,y+1/2;-y,-z,-x;y,-z+1/2,x+1/2;-y+1/2,z+1/2,x;y+1/2,z,-x+1/2;-y+1/4,-x+3/4,z+3/4;y+1/4,x+1/4,z+1/4;-y+3/4,x+3/4,-z+1/4;y+3/4,-x+1/4,-z+3/4;-x+1/4,-z+3/4,y+3/4;x+3/4,-z+1/4,-y+3/4;x+1/4,z+1/4,y+1/4;-x+3/4,z+3/4,-y+1/4;-z+1/4,-y+3/4,x+3/4;-z+3/4,y+3/4,-x+1/4;z+3/4,-y+1/4,-x+3/4;z+1/4,y+1/4,x+1/4" : [ "Cubic"  , "Ia-3d" ],
        }

SpaceGroupFreq = [None, 0.96627177635927464, 22.797866390567005, 0.019413257405926591, 5.4849385477959016, 0.86712549746472101, 0.0027733224865609417, 0.41230060966872661, 0.047377592478749418, 1.0753557941640051, 0.016639934919365648, 0.56691333829449908, 0.51814908457246922, 0.59187324067354763, 35.094547185771006, 8.0014975941427426, 0.0048533143514816477, 0.011093289946243767, 0.42524278127267767, 8.0213730719630956, 0.18396372494187579, 0.0076266368380425893, 0.0027733224865609417, 0.025191012586261885, 0.0057777551803352943, 0.0023111020721341179, 0.017795485955432708, 0.002079991864920706, 0.002079991864920706, 0.72776604251503374, 0.014559943054444942, 0.074417486722718598, 0.018719926784286356, 1.4275677499572446, 0.031893208595450827, 0.00092444082885364718, 0.15807938173397365, 0.015022163468871766, 0.0036977633154145887, 0.0069333062164023537, 0.01825770636985953, 0.10631069531816942, 0.01039995932460353, 0.34435420874798356, 0.011786620567884001, 0.054310898695151773, 0.011555510360670589, 0.0018488816577072944, 0.0078577470452560003, 0.002079991864920706, 0.0085510776668962368, 0.0071644164236157656, 0.091519642056511072, 0.018026596162646121, 0.044604269992188472, 0.028888775901676475, 0.35637193952308099, 0.11139511987686448, 0.077884139830919769, 0.036284302532505648, 0.89208539984376956, 3.5235062191756761, 1.2570084170337468, 0.10908401780473036, 0.13427503039099226, 0.01548438388329859, 0.01039995932460353, 0.0069333062164023537, 0.0489953639292433, 0.0073955266308291774, 0.090826311434870827, 0.010631069531816943, 0.043448718956121415, 0.025191012586261885, 0.012248840982310825, 0.0050844245586950595, 0.10238182179554142, 0.0097066287029632953, 0.074879707137145424, 0.02842655548724965, 0.02588434320790212, 0.026577673829542355, 0.14721720199494331, 0.0064710858019755299, 0.015946604297725413, 0.099146278894553658, 0.13288836914771177, 0.060550874289913889, 0.3408875556397824, 0.0013866612432804708, 0.0069333062164023537, 0.0073955266308291774, 0.22186579892487532, 0.0011555510360670589, 0.019875477820353413, 0.0046222041442682358, 0.15946604297725414, 0.0073955266308291774, 0.0080888572524694131, 0.0002311102072134118, 0.00069333062164023541, 0.0011555510360670589, 0.0036977633154145887, 0.0025422122793475298, 0.0097066287029632953, 0.00046222041442682359, 0.010168849117390119, 0.0023111020721341179, 0.0039288735226280002, 0.0060088653875487062, 0.035590971910865417, 0.0013866612432804708, 0.004159983729841412, 0.027964335072822828, 0.13774168349919341, 0.00046222041442682359, 0.0030044326937743531, 0.0069333062164023537, 0.02334213092855459, 0.004159983729841412, 0.010862179739030354, 0.022879910514127768, 0.05916421304663342, 0.01039995932460353, 0.012248840982310825, 0.0025422122793475298, 0.024959902379048472, 0.012017730775097412, 0.01039995932460353, 0.024266571757408237, 0.046915372064322593, 0.0025422122793475298, 0.0013866612432804708, 0.0034666531082011768, 0.0062399755947621181, 0.0092444082885364716, 0.021031028856420473, 0.013635502225591295, 0.011093289946243767, 0.014791053261658355, 0.0057777551803352943, 0.019413257405926591, 0.047608702685962831, 0.028195445280036237, 0.084586335840108717, 0.067946400920743069, 0.13427503039099226, 0.1137062219489986, 0.59765099585388293, 0.0013866612432804708, 0.0097066287029632953, 0.0030044326937743531, 0.094061854335858591, 0.0025422122793475298, 0.060319764082700476, 0.040444286262347064, 0.0011555510360670589, 0.0025422122793475298, 0.0090132980813230606, 0.030737657559383767, 0.029813216730530119, 0.10654180552538284, 0.0018488816577072944, 0.033510980045944709, 0.01039995932460353, 0.057546441596139537, 0.039288735226280007, 0.13404392018377884, 0.0036977633154145887, 0.066559739677462593, 0.050844245586950595, 0.0087821878741096478, 0.0048533143514816477, 0.073261935686651541, 0.003235542900987765, 0.0030044326937743531, 0.13080837728279107, 0.00069333062164023541, 0.021493249270847295, 0.017102155333792474, 0.0057777551803352943, 0.0034666531082011768, 0.0085510776668962368, 0.00069333062164023541, 0.0011555510360670589, 0.0034666531082011768, 0.015946604297725413, 0.00069333062164023541, 0.0013866612432804708, 0.0027733224865609417, 0.015022163468871766, 0.0050844245586950595, 0.01039995932460353, 0.0039288735226280002, 0.020568808441993647, 0.0018488816577072944, 0.0071644164236157656, 0.013866612432804707, 0.063324196776474828, 0.0034666531082011768, 0.0023111020721341179, 0.0039288735226280002, 0.0025422122793475298, 0.011324400153457178, 0.010862179739030354, 0.097990727858486601, 0.0097066287029632953, 0.00046222041442682359, 0.0011555510360670589, 0.002079991864920706, 0.002079991864920706, 0.002079991864920706, 0.0046222041442682358, 0.0050844245586950595, 0.003235542900987765, 0.0069333062164023537, 0.0076266368380425893, 0.026115453415115533, 0.014559943054444942, 0.0099377389101767064, 0.023804351342981415, 0.0090132980813230606, 0.0087821878741096478, 0.0034666531082011768, 0.0043910939370548239, 0.031430988181024001, 0.00069333062164023541, 0.014328832847231531, 0.0080888572524694131, 0.014559943054444942, 0.0050844245586950595]

SpaceGroupChiral = [None, True, False, True, True, True, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

#Atomic moleculat weight taken from the MPQC program : http://www.mpqc.org
AtomicWeight = {
'Ac':227.03, 'Ag':107.87, 'Al':26.98, 'Am':243.00, 'Ar':39.96,
'As':74.92, 'At':210.00, 'Au':196.97, 'B':11.01, 'Ba':137.33,
'Be':9.01, 'Bi':208.98, 'Bk':247.00, 'Br':79.90, 'C':12.01,
'Ca':39.96, 'Cd':112.41, 'Ce':140.12, 'Cf':251.00, 'Cl':35.45,
'Cm':247.00, 'Co':58.93, 'Cr':51.94, 'Cs':132.91, 'Cu':63.55,
'Dy':162.50, 'Er':167.26, 'Es':254.00, 'Eu':151.96, 'F':19.00,
'Fe':55.85, 'Fm':257.00, 'Fr':223.00, 'Ga':68.93, 'Gd':157.25,
'Ge':73.92, 'H':1.01, 'Ha':260.00, 'He':4.00, 'Hf':178.49,
'Hg':200.59, 'Ho':164.93, 'I':126.90, 'In':114.82, 'Ir':192.22,
'K':39.10, 'Kr':83.91, 'La':138.91, 'Li':6.94, 'Lr':260.00,
'Lu':174.97, 'Md':258.00, 'Mg':23.99, 'Mn':54.94, 'Mo':95.94,
'N':14.01, 'Na':22.99, 'Nb':92.91, 'Nd':144.24, 'Ne':19.99,
'Ni':58.70, 'No':259.00, 'Np':237.05, 'O':16.00, 'Os':190.20,
'P':30.97, 'Pa':231.04, 'Pb':207.20, 'Pd':106.40, 'Pm':145.00,
'Po':209.00, 'Pr':140.91, 'Pt':195.09, 'Pu':244.00, 'Ra':226.03,
'Rb':85.47, 'Re':186.21, 'Rf':260.00, 'Rh':102.91, 'Rn':222.00,
'Ru':101.07, 'S':32.06, 'Sb':121.75, 'Sc':44.96, 'Se':79.92,
'Si':27.98, 'Sm':150.40, 'Sn':118.69, 'Sr':87.62, 'Ta':180.95,
'Tb':158.93, 'Tc':98.00, 'Te':127.60, 'Th':232.04, 'Ti':47.95,
'Tl':204.37, 'Tm':168.93, 'U':238.03, 'Un':266.00, 'V':50.94,
'W':183.85, 'Xe':131.30, 'Y':88.91, 'Yb':173.04, 'Zn':65.35,
'Zr':91.22
}

#Atomic volumes are taken from Acta Cryst B 57  pp 489-493
AtomicVolume = {
'Ac': 74.0, 'Ag': 35.0, 'Al': 39.6, 'Am': 17.0, 'Ar': 0,
'As': 36.4, 'At': 0, 'Au': 43.0, 'B': 13.24, 'Ba': 66.0,
'Be': 36.0, 'Bi': 60.0, 'Bk': 0, 'Br': 32.7, 'C': 13.87,
'Ca': 45.0, 'Cd': 51.0, 'Ce': 54.0, 'Cf': 0, 'Cl': 25.8,
'Cm': 0, 'Co': 29.4, 'Cr': 28.1, 'Cs': 46.0, 'Cu': 26.9,
'Dy': 50.0, 'Er': 54.0, 'Es': 0, 'Eu': 53.0, 'F': 11.17,
'Fe': 30.4, 'Fm': 0, 'Fr': 0, 'Ga': 37.8, 'Gd': 56.0,
'Ge': 41.6, 'H': 5.08, 'He': 0, 'Hf': 40.0, 'Hg': 38.0,
'Ho': 42.0, 'I': 46.2, 'In': 55.0, 'Ir': 34.3, 'K': 36.0,
'Kr': 0, 'La': 58.0, 'Li': 22.6, 'Lu': 35.0, 'Mg': 36.0,
'Mn': 31.9, 'Mo': 38.0, 'N': 11.8, 'Na': 26.0, 'Nb': 37.0,
'Nd': 50.0, 'Ne': 0, 'Ni': 26.0, 'Np': 45.0, 'O': 11.39,
'Os': 41.9, 'P': 29.5, 'Pa': 60.0, 'Pb': 52.0, 'Pd': 35.0,
'Pm': 0, 'Po': 0, 'Pr': 57.0, 'Pt': 38.0, 'Pu': 0,
'Ra': 0, 'Rb': 42.0, 'Re': 42.7, 'Rh': 31.2, 'Rn': 0,
'Ru': 37.3, 'S': 25.2, 'Sb': 48.0, 'Sc': 42.0, 'Se': 30.3,
'Si': 37.3, 'Sm': 50.0, 'Sn': 52.8, 'Sr': 47.0, 'Ta': 43.0,
'Tb': 45.0, 'Tc': 38.0, 'Te': 46.7, 'Th': 56.0, 'Ti': 27.3,
'Tl': 54.0, 'Tm': 49.0, 'U': 58.0, 'V': 24.0, 'W': 38.8,
'Xe': 45.0, 'Y': 44.0, 'Yb': 59.0, 'Zn': 39.0, 'Zr': 27.0,
}

DefaultAuthor = "J.Kieffer;Grenoble"
Version = [" Generated by CifFile.py: Octobre 2009", " Written by Jerome Kieffer : Jerome.Kieffer@esrf.fr", " On-Line data analysis / software group ", " ESRF Grenoble (France)"]


#check for the existance of Booleans : this is only if your python is too old
try:
        True
except Exception:
    True = (1 == 1)
    False = (1 == 0)


EOL = ["\r", "\n", "\r\n", "\n\r"]
Blank = [" ", "    "] + EOL
StartComment = ["\"", "\'"]

for i in EOL:
    StartComment.append((i + ";"))

EndComment = []
for i in EOL:
    EndComment.append(i + ";")
for i in ["\"", "\'"]:
    for j in Blank:
        EndComment.append(i + j)

class CIFreal():
    """this is an attempt to create a class for storing float values taking into account ESD
    Here is short example:
    a=CIFreal("123.56(18)")
    a.getValue()
     ==> 123.56
    a.getEsd()
     ==> 0.18
    a.set(56,0.1)
     ==> "56.0(1)"            
     """
    def __init__(self, sInput=""):
        """constructor of the class, 
        @type sInput: string
        @param sInput: the string representation of the real as value(esd)
        """
        self.value = None #at the moment not yet defined, using float in a systematic manner would slow down a lot the processing
        self.esd = None #also initialized at nothing for the moment
        self.str = sInput

    def __repr__(self):
        """retuns the standard representation in CIF format of the value(esd)"""
        return self.str

    def getValue(self):
        """return the value of the real as a float number 
        @return: the value of the real(esd)
        @rtype: python float
        """
        if self.value is None:
            self.value = float(self.str.split("(")[0])
        return  self.value

    def getEsd(self):
        """return the estimated standard deviation of the real as a float number 
        @return: the deviation of the real(esd)
        @rtype: python float
        """

        if self.esd is None:
            sValue, sEsd = tuple(self.str.split("(", 1))
            sEsd = sEsd.rstrip(")")
            lEsd = list(sEsd)
            lValue = list(sValue)
            lValue.reverse()
            lEsd.reverse()
            for i in range(len(lValue)):
                if i >= len(lEsd):
                    if lValue[i] == "." :
                        lEsd.append(".")
                    else:
                        lEsd.append("0")
                elif lValue[i] == "." and lEsd[i] != "." :
                    print "we are in a trouble ....", lValue, lEsd

            lEsd.reverse()
            sEsd = ""
            for i in lEsd:
                sEsd += i
            self.esd = float(sEsd)
        return self.esd


    def set(self, value=0.0, esd=0.0):
        """initialize from a couple of floats
        @param value: numerical value of the real
        @type  value: python float
        @param   esd: estimated stadard deviation
        @type    esd: python  float
        """
        self.value = value
        self.esd = esd
        sValue = str(float(self.value))
        sEsd = str(float(self.esd))
        iDotPosValue = sValue.find(".")
        iDotPosEsd = sEsd.find(".")
        if iDotPosValue < iDotPosEsd:
            sValue = "0" * (iDotPosEsd - iDotPosValue) + sValue
        elif iDotPosValue > iDotPosEsd:
            sEsd = "0" * (-iDotPosEsd + iDotPosValue) + sEsd
        if len(sValue) > len(sEsd) :
            sEsd += "0" * (-len(sEsd) + len(sValue))
        elif len(sValue) < len(sEsd) :
            sValue += "0" * (len(sEsd) - len(sValue))
        if sValue[-2:] == ".0" and sEsd[-2:] == ".0":
            sValue = sValue[:-2]
            sEsd = sEsd[:-2]
        self.str = sValue + "(" + sEsd.lstrip(" 0.") + ")"

    def __add__(self, other):
        """addition of two reals, for example 1.5(2) + 2.3(3) = 3.8(5)
        @param other: another CIFreal to be added
        @type other: CIFreal
        @return: the sum of the two reals
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(self.getValue() + other.getValue(), self.getEsd() + other.getEsd())
        return result

    def __sub__(self, other):
        """Substraction of two reals, for example 1.5(2) - 2.3(3) = -0.8(5)
        @param other: another CIFreal to be substracted 
        @type other: CIFreal
        @return: the substraction of the two reals
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(self.getValue() - other.getValue(), abs(self.getEsd()) + abs(other.getEsd()))
        return result
    def __mul__(self, other):
        """Multiplication two reals, for example 1.5(2) * 2.3(3) = 3.45(91)
        @param other: another CIFreal to be muliplied
        @type other: CIFreal
        @return: the multiplication of the two reals
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(self.getValue()*other.getValue(), abs(self.getEsd()*other.getValue()) + abs(other.getEsd()*self.getValue()))
        return result
    def __div__(self, other):
        """Division of two reals, for example 1.5(2) / 2.3(3) = 3.45(91)
        @param other: another CIFreal to be divided by
        @type other: CIFreal
        @return: the division of the two reals
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(self.getValue() / other.getValue(), abs(self.getEsd() / other.getValue()) + abs(other.getEsd()*self.getValue() / other.getValue() / other.getValue()))
        return result

    def __neg__(self):
        """Negation of a real -(1.5(2)) = -1.5(2)
        @return: the negation of the real
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(-self.getValue(), abs(self.getEsd()))
        return result

    def __inv__(self, other):
        """Inversion of a reals, for example 1 / 1.6(2) = 0.625(78)
        @return: the sum of the two reals
        @rtype: CIFreal
        """
        result = CIFreal()
        result.set(1 / self.getValue(), abs(self.getEsd() / self.getValue() / self.getValue()))
        return result



class CIF(dict):
    """This is the CIF class, it represents the CIF dictionnary as a a python dictionnary thus inherits from the dict built in class.
    
    """
    def loadCIF(self, _strFilename):
            """Load the CIF file and returns the CIF dictionnary int the object
            @param _strFilename: the name of the file to open
            @type  _strFilename: string
            @return: the CIF object corresponding to the Xtal structure
            @rtype: dictionnary
            """
            self._parseCIF(self._readCIF(_strFilename))

    def _readCIF(self, _strFilename):
        """-Check if the filename containing the CIF data exists 
        -read the cif file
        -removes the comments 
        @param _strFilename: the name of the CIF file
        @type _strFilename: string
        @return: a string containing the raw data
        @rtype: string"""
        if not os.path.isfile(_strFilename):
            raise("I cannot find the file %s" % _strFilename)
            sys.exit(1)
        lLinesRead = open(_strFilename, "rb").readlines()
        sText = ""
        for sLine in lLinesRead:
            iPos = sLine.find("#")
            if iPos >= 0:
                sText += sLine[:iPos] + "\n"
                if iPos > 80 :
                    print "Warning, this line is too long and could cause problems in PreQuest\n", sLine
            else :
                sText += sLine
                if len(sLine.strip()) > 80 :
                    print "Warning, this line is too long and could cause problems in PreQuest\n", sLine
        return sText

    def _parseCIF(self, sText):
        """ 
        -Parses the text of a CIF file   
        -Cut it in fields
        -Find all the loops and process    
        -Find all the keys and values      
        @param sText: the content of the CIF-file
        @type sText: string
        @return: Nothing, the data are incorporated at the CIF object dictionnary
        @rtype: dictionnary
        """
        loopidx = []
        looplen = []
        loop = []
        #first of all : separate the cif file in fields
        lFields = self._splitCIF(sText.strip())
        #Then : look for loops
        for i in range(len(lFields)):
            if lFields[i].lower() == "loop_":
                loopidx.append(i)
        if len(loopidx) > 0:
            for i in loopidx:
                loopone, length, keys = self._analyseOneLoop(lFields, i)
                loop.append([keys, loopone])
                looplen.append(length)


            for i in range(len(loopidx) - 1, -1, -1):
                f1 = lFields[:loopidx[i]] + lFields[loopidx[i] + looplen[i]:]
                lFields = f1

            self["loop_"] = loop

        for i in range(len(lFields) - 1):
    #        print lFields[i], lFields[i+1]
            if len(lFields[i + 1]) == 0 : lFields[i + 1] = "?"
            if lFields[i][0] == "_" and lFields[i + 1][0] != "_":
                self[lFields[i]] = lFields[i + 1]


    def _splitCIF(self, sText):
        """Separate the text in fields as defined in the CIF
        @param sText: the content of the CIF-file
        @type sText: string
        @return: list of all the fields of the CIF
        @rtype: list
        """
        lFields = []
        while True:
            if len(sText) == 0:
                break
            elif sText[0] == "'":
                idx = 0
                bFinished = False
                while not  bFinished:
                    idx += 1 + sText[idx + 1:].find("'")
            ##########debuging    in case we arrive at the end of the text             
                    if idx >= len(sText) - 1:
            #                    print sText,idx,len(sText)
                        lFields.append(sText[1:-1].strip())
                        sText = ""
                        bFinished = True
                        break

                    if sText[idx + 1] in Blank:
                        lFields.append(sText[1:idx].strip())
                        sText1 = sText[idx + 1:]
                        sText = sText1.strip()
                        bFinished = True

            elif sText[0] == '"':
                idx = 0
                bFinished = False
                while not  bFinished:
                    idx += 1 + sText[idx + 1:].find('"')
            ##########debuging    in case we arrive at the end of the sText             
                    if idx >= len(sText) - 1:
            #                    print sText,idx,len(sText)
                        lFields.append(sText[1:-1].strip())
                        sText = ""
                        bFinished = True
                        break

                    if sText[idx + 1] in Blank:
                        lFields.append(sText[1:idx].strip())
                        sText1 = sText[idx + 1:]
                        sText = sText1.strip()
                        bFinished = True
            elif sText[0] == ';':
                idx = 0
                bFinished = False
                while not  bFinished:
                    idx += 1 + sText[idx + 1:].find(';')
                    if sText[idx - 1] in EOL:
                        lFields.append(sText[1:idx - 1].strip())
                        sText1 = sText[idx + 1:]
                        sText = sText1.strip()
                        bFinished = True
            else:
                f = sText.split(None, 1)[0]
                lFields.append(f)
                sText1 = sText[len(f):].strip()
                sText = sText1

        return lFields

    def _analyseOneLoop(self, lFields, iStart):
        """Processes one loop in the data extraction of the CIF file
        @param lFields: list of all the words contained in the cif file
        @type lFields: list
        @param iStart: the starting index corresponding to the "loop_" key 
        @type iStart: integer
        @return: the list of loop dictionnaries, the length of the data extracted from the lFields and the list of all the keys of the loop.
        @rtype: tupple
        """
        #    in earch loop we first search the length of the loop
        #    print lFields
#        curloop = {}
        loop = []
        keys = []
        i = iStart + 1
        bFinished = False
        while not bFinished:
            if lFields[i][0] == "_":
                keys.append(lFields[i])#.lower())
                i += 1
            else:
                bFinished = True
        data = []
        while True:
            if i >= len(lFields):
                break
            elif len(lFields[i]) == 0:
                break
            elif lFields[i][0] == "_":
                break
            elif lFields[i] in ["loop_", "stop_", "global_", "data_", "save_"]:
                break
            else:
                data.append(lFields[i])
                i += 1
        #print len(keys), len(data)
        k = 0

        if len(data) < len(keys):
            element = {}
            for j in keys:
                if k < len(data):
                    element[j] = data[k]
                else :
                    element[j] = "?"
                k += 1
            #print element
            loop.append(element)

        else:
            #print data
            #print keys 
            for i in range(len(data) / len(keys)):
                element = {}
                for j in keys:
                    element[j] = data[k]
                    k += 1
        #            print element
                loop.append(element)
        #    print loop
        return loop, 1 + len(keys) + len(data), keys






#############################################################################################
########     everything needed to  write a cif file #########################################
#############################################################################################

    def saveCIF(self, _strFilename="test.cif"):
        """Transforms the CIF object in string then write it into the given file
        @param _strFilename: the of the file to be written
        @type param: string
        """
        #TODO We should definitly handle exception here   
        try:
            fFile = open(_strFilename, "wb")
        except Exception:
            print "Error during the opening of file for write : %s" % _strFilename
            return

        fFile.write(self._cif2str(_strFilename))
        try:
            fFile.close()
        except Exception:
            print "Error during the opening of file for write : %s" % _strFilename





    def _cif2str(self, _strFilename):
        """converts a cif dictionnary to a string according to the CIF syntax
        @param _strFilename: the name of the filename to be apppended in the header of the CIF file 
        @type _strFilename: string
        @return : a sting that corresponds to the content of the CIF-file.
        @rtype: string
        """
        sCifText = ""
        for i in Version:
            sCifText += "#" + i + "\n"
        if self.exists("_chemical_name_common"):
            t = self["_chemical_name_common"].split()[0]
        elif _strFilename == "test.cif":
            t = ""
        else:
            t = os.path.splitext(os.path.basename(_strFilename))[0].replace(" ", "_")
        sCifText += "data_%s\n" % t.strip()
        #first of all get all the keys :
        lKeys = self.keys()
        lKeys.sort()
        for sKey in lKeys:
            if sKey == "loop_":continue
            sValue = self[sKey]
            if sValue.find("\n") > -1: #should add value  between ;;
                sLine = "%s \n;\n %s \n;\n" % (sKey, sValue)
            elif len(sValue.split()) > 1: #should add value between ''
                sLine = "%s        '%s' \n" % (sKey, sValue)
                if len(sLine) > 80:
                    sLine = "%s\n '%s' \n" % (sKey, sValue)
            else:
                sLine = "%s        %s \n" % (sKey, sValue)
                if len(sLine) > 80:
                    sLine = "%s\n %s \n" % (sKey, sValue)
            sCifText += sLine
        if self.has_key("loop_"):
            for loop in self["loop_"]:
                sCifText += "loop_ \n"
                lKeys = loop[0]
                llData = loop[1]
                for sKey in lKeys:
                    sCifText += " %s \n" % sKey
                for lData in llData:
                    sLine = ""
                    for key in lKeys:
                        sRawValue = lData[key]
                        if sRawValue.find("\n") > -1: #should add value  between ;;
                            sLine += "\n; %s \n;\n" % (sRawValue)
                            sCifText += sLine
                            sLine = ""
                        else:
                            if len(sRawValue.split()) > 1: #should add value between ''
                                value = "'%s'" % (sRawValue)
                            else:
                                value = sRawValue
                            if len(sLine) + len(value) > 78:
                                sCifText += sLine + " \n"
                                sLine = " " + value
                            else:
                                sLine += " " + value
                    sCifText += sLine + " \n"
                sCifText += "\n"
        #print sCifText
        return sCifText

    def exists(self, sKey):
        """
        Check if the key exists in the CIF and is non empty.
        @param sKey: CIF key
        @type sKey: string
        @param cif: CIF dictionnary
        @return: True if the key exists in the CIF dictionnary and is non empty
        @rtype: boolean
        """
        bExists = False
        if self.has_key(sKey):
            if len(self[sKey]) >= 1:
                if self[sKey][0] not in ["?", "."]: bExists = True
        return bExists

    def existsInLoop(self, sKey):
        """
        Check if the key exists in the CIF dictionnary.
        @param sKey: CIF key
        @type sKey: string
        @param cif: CIF dictionnary
        @return: True if the key exists in the CIF dictionnary and is non empty
        @rtype: boolean
        """
        bExists = False
        if not bExists:
            for i in self["loop_"]:
                for j in i[0]:
                    if j == sKey:
                        bExists = True
        return bExists

def LoopHasKey(loop, key):
    "Returns True if the key (string) existe in the array called loop"""
    try:
        loop.index(key)
        return True
    except Exception:
        return False



if __name__ == '__main__':
    print "This is just a test of the library"
    #print os.getcwd()
    #print os.listdir(".")
    aspirine = CIF()
    aspirine.loadCIF("aspirin.cif")
#    for sKey in aspirine:
#        print sKey, aspirine[sKey]   
    aspirine.saveCIF("test.cif")



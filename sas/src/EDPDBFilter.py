#coding: utf8
#    Project: Solution scattering pipeline
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010 DLS
#                  2012 ESRF
#
#    Principal author:        irakli
#                             Jerome Kieffer
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
from __future__ import with_statement
__authors__ = ["irakli", "Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "2012 DLS; 2012 ESRF"

class EDPDBFilter(object):
    """
    Class for verifying validity of input PDB file
    """
    __lPDBKeywords = [  'HEADER',
                        'TITLE',
                        'COMPND',
                        'SOURCE',
                        'KEYWDS',
                        'EXPDTA',
                        'AUTHOR',
                        'REVDAT',
                        'JRNL',
                        'REMARK',
                        'DBREF',
                        'SEQADV',
                        'SEQRES',
                        'MODRES',
                        'HET',
                        'HETNAM',
                        'FORMUL',
                        'HELIX',
                        'SHEET',
                        'CRYST1',
                        'ORIGX1',
                        'ORIGX2',
                        'ORIGX3',
                        'SCALE1',
                        'SCALE2',
                        'SCALE3',
                        'ATOM',
                        'TER',
                        'HETATM',
                        'CONECT',
                        'MASTER',
                        'END']
    @classmethod
    def filterPDBFile(cls, _inputPDB, _outputPDB):
        """
        Put REMARK keyword in front of the comment lines
        """
        _linesOutput = []
        for line in open(_inputPDB):
            data = line.split()
            if data:
                if data[0] in cls.__lPDBKeywords:
                    _linesOutput.append(line)
                else:
                    _linesOutput.append('REMARK ' + line)
            else:
                _linesOutput.append('REMARK ' + line)
        with open(_outputPDB, "w") as f:
            f.writelines(_linesOutput)


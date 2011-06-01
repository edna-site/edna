#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:        irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

from EDUtilsFile import EDUtilsFile

class EDPDBFilter:
    """
    Class for verifying validity of input PDB file
    """
    
    def __init__(self):
        """
        Initialize keywork list and input pdb file
        @param _inputPDB: Input PDB file
        """
        self.__lPDBKeywords = ['HEADER', \
                                'TITLE', \
                                'COMPND', \
                                'SOURCE', \
                                'KEYWDS', \
                                'EXPDTA', \
                                'AUTHOR', \
                                'REVDAT', \
                                'JRNL', \
                                'REMARK', \
                                'DBREF', \
                                'SEQADV', \
                                'SEQRES', \
                                'MODRES', \
                                'HET', \
                                'HETNAM', \
                                'FORMUL', \
                                'HELIX', \
                                'SHEET', \
                                'CRYST1', \
                                'ORIGX1', \
                                'ORIGX2', \
                                'ORIGX3', \
                                'SCALE1', \
                                'SCALE2', \
                                'SCALE3', \
                                'ATOM', \
                                'TER', \
                                'HETATM', \
                                'CONECT', \
                                'MASTER', \
                                'END']
        
    def filterPDBFile(self, _inputPDB, _outputPDB):
        """
        Put REMARK keyword in front of the comment lines
        """
        _linesOutput = []
        _linesPDB = EDUtilsFile.readFile(_inputPDB).split('\n')
        for line in _linesPDB:
            data = line.split()
            if data:
                if data[0] in self.__lPDBKeywords:
                    _linesOutput.append(line)
                else:
                    _linesOutput.append('REMARK ' + line)
            else:
                _linesOutput.append('REMARK')
                
        EDUtilsFile.writeFile(_outputPDB, '\n'.join(_linesOutput)) 

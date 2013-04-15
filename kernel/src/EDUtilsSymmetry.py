#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


class EDUtilsSymmetry:
    """
    This utility class contains methods useful for handling symmetries.
    """

    @staticmethod
    def getMinimumSymmetrySpaceGroupFromBravaisLattice(_strBravaisLattice):
        """
        This static method returns a string containing the name of the space
        group with minimum symmetry that corresponds to a given two-letter Bravais
        Lattice.
        
        Note that the "hR" Bravais Lattice is translated into the "H3" and not the
        "R3" space group since the "H3" space group is the one used in MX in general
        and in particular for structures deposited in the PDB.
        
        If the Bravais Lattice is not recognised a "None" object is returned.
        """
        strSpaceGroup = None
        strBravaisLattice = _strBravaisLattice
        if strBravaisLattice == "aP":
            strSpaceGroup = "P1"

        elif strBravaisLattice == "mP":
            strSpaceGroup = "P2"

        elif strBravaisLattice == "mC" or \
               strBravaisLattice == "mI":
            strSpaceGroup = "C2"

        elif strBravaisLattice == "oP":
            strSpaceGroup = "P222"

        elif strBravaisLattice == "oA" or \
               strBravaisLattice == "oB" or \
               strBravaisLattice == "oC" or \
               strBravaisLattice == "oS":
            strSpaceGroup = "C222"

        elif strBravaisLattice == "oF":
            strSpaceGroup = "F222"

        elif strBravaisLattice == "oI":
            strSpaceGroup = "I222"

        elif strBravaisLattice == "tP" or \
               strBravaisLattice == "tC":
            strSpaceGroup = "P4"

        elif strBravaisLattice == "tI" or \
               strBravaisLattice == "tF":
            strSpaceGroup = "I4"

        elif strBravaisLattice == "hP":
            strSpaceGroup = "P3"

        elif strBravaisLattice == "hR":
            strSpaceGroup = "H3"

        elif strBravaisLattice == "cP":
            strSpaceGroup = "P23"

        elif strBravaisLattice == "cF":
            strSpaceGroup = "F23"

        elif strBravaisLattice == "cI":
            strSpaceGroup = "I23"

        return strSpaceGroup



    @staticmethod
    def getNumberOfSymmetryOperatorsFromSpaceGroupITNumber(_strSpaceGroupId, _strSymmetryTableFileName):
        """
        """
        return EDUtilsSymmetry.getNumberOfSymmetryOperators(_strSpaceGroupId, 0, _strSymmetryTableFileName)


    @staticmethod
    def getNumberOfSymmetryOperatorsFromSpaceGroupName(_strSpaceGroupName, _strSymmetryTableFileName):
        """
        """
        return EDUtilsSymmetry.getNumberOfSymmetryOperators(_strSpaceGroupName, 3, _strSymmetryTableFileName)



    @staticmethod
    def getNumberOfSymmetryOperators(_strSpaceGroupIdOrName, _iIndex, _strSymmetryTableFileName):
        """
        """
        strNumOperators = None
        symmetryTableFile = open(_strSymmetryTableFileName)
        for strLine in symmetryTableFile.xreadlines():
            listItems = strLine.split(" ")
            if (len(listItems) > 3 and listItems[_iIndex] == _strSpaceGroupIdOrName):
                strNumOperators = listItems[1]
        return strNumOperators

    @staticmethod
    def getITNumberFromSpaceGroupName(_strSpaceGroupName, _strSymmetryTableFileName):
        """
        """
        iITNumber = None
        symmetryTableFile = open(_strSymmetryTableFileName)
        for strLine in symmetryTableFile.xreadlines():
            listItems = strLine.split(" ")
            if len(listItems) > 3:
                if _strSpaceGroupName == listItems[3]:
                    iITNumber = int(listItems[0])
        return iITNumber

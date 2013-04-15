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

import os

from EDTestCase      import EDTestCase
from EDUtilsSymmetry import EDUtilsSymmetry
from EDAssert        import EDAssert


class EDTestCaseEDUtilsSymmetry(EDTestCase):


    def testGetMinimumSymmetrySpaceGroupFromBravaisLattice(self):
        """
        Testing retrieving the lowest symmetry space group from all Bravais Lattices
        """
        listBravaisLattice = [ "aP", "mP", "mC", "mI", "oP", "oA", "oB", "oC", "oS", "oF", "oI", "tP", "tC", "tI", "tF", "hP", "hR", "cP", "cF", "cI" ]
        listSpaceGroup = [ "P1", "P2", "C2", "C2", "P222", "C222", "C222", "C222", "C222", "F222", "I222", "P4", "P4", "I4", "I4", "P3", "H3", "P23", "F23", "I23" ]
        for iIndex in range(len(listBravaisLattice)):
            EDAssert.equal(listSpaceGroup[ iIndex ], EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(listBravaisLattice[ iIndex]))

    def testGetITNumberFromSpaceGroupName(self):
        strSymopFileName = "/opt/pxsoft/ccp4/v6.3.0/linux-x86_64/lib/data/symop.lib"
        if os.path.exists(strSymopFileName):
            EDAssert.equal(1, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P1", strSymopFileName), "ITNumber from space group P1")
            EDAssert.equal(3, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P2", strSymopFileName), "ITNumber from space group P2")
            EDAssert.equal(5, EDUtilsSymmetry.getITNumberFromSpaceGroupName("C2", strSymopFileName), "ITNumber from space group C2")
            EDAssert.equal(16, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P222", strSymopFileName), "ITNumber from space group P222")
            EDAssert.equal(21, EDUtilsSymmetry.getITNumberFromSpaceGroupName("C222", strSymopFileName), "ITNumber from space group C222")
            EDAssert.equal(22, EDUtilsSymmetry.getITNumberFromSpaceGroupName("F222", strSymopFileName), "ITNumber from space group F222")
            EDAssert.equal(75, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P4", strSymopFileName), "ITNumber from space group P4")
            EDAssert.equal(79, EDUtilsSymmetry.getITNumberFromSpaceGroupName("I4", strSymopFileName), "ITNumber from space group I4")
            EDAssert.equal(143, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P3", strSymopFileName), "ITNumber from space group P3")
            EDAssert.equal(146, EDUtilsSymmetry.getITNumberFromSpaceGroupName("H3", strSymopFileName), "ITNumber from space group H3")
            EDAssert.equal(195, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P23", strSymopFileName), "ITNumber from space group P23")
            EDAssert.equal(196, EDUtilsSymmetry.getITNumberFromSpaceGroupName("F23", strSymopFileName), "ITNumber from space group F23")
        


    def process(self):
        self.addTestMethod(self.testGetMinimumSymmetrySpaceGroupFromBravaisLattice)
        self.addTestMethod(self.testGetITNumberFromSpaceGroupName)


if __name__ == '__main__':

    edTestCaseEDUtilsSymmetry = EDTestCaseEDUtilsSymmetry("TestCase EDTestCaseEDUtilsSymmetry")
    edTestCaseEDUtilsSymmetry.execute()

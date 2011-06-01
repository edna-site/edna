#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginUnitControlCharacterisationv1_3(EDTestSuite):
    """
    This is the unit test suite for EDNA plugin Characterisationv1_3 
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitControlCharacterisationv1_3")



if __name__ == '__main__':

    edTestSuitePluginUnitControlCharacterisationv1_3 = EDTestSuitePluginUnitControlCharacterisationv1_3("EDTestSuitePluginUnitControlCharacterisationv1_3")
    edTestSuitePluginUnitControlCharacterisationv1_3.execute()


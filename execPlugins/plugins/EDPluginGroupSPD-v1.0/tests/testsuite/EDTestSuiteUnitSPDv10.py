#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite import EDTestSuite

class EDTestSuiteUnitSPDv10(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginUnitSPDCorrectv10")
        self.addTestCaseFromName("EDTestCasePluginUnitSPDCakev1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitSPDCakev1_1")
        self.addTestCaseFromName("EDTestCasePluginUnitSPDCakev1_5")
        self.addTestCaseFromName("EDTestCasePluginUnitSPDCorrectv10")


##############################################################################
if __name__ == '__main__':

    edTestSuiteUnitSPDv10 = EDTestSuiteUnitSPDv10("EDTestSuiteUnitSPDv10")
    edTestSuiteUnitSPDv10.execute()

##############################################################################

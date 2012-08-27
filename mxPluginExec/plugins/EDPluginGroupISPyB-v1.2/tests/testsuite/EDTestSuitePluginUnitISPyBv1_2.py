#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:  Marie-Francoise Incardona (incardon@esrf.fr)
#                           Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Karl Levik, Marie-Francoise Incardona, Olof Svensson"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"
__date__ = "20120712"
__status__ = "production"

from EDTestSuite                                   import EDTestSuite

class EDTestSuitePluginUnitISPyBv1_2(EDTestSuite):

    def process(self):
        """
        Adds the plugin unit test cases 
        """
        self.addTestCaseFromName("EDTestCasePluginUnitISPyBv1_2")


if __name__ == '__main__':
    edTestSuitePluginUnitISPyBv1_2 = EDTestSuitePluginUnitISPyBv1_2("EDTestSuitePluginUnitISPyBv1_2")
    edTestSuitePluginUnitISPyBv1_2.execute()


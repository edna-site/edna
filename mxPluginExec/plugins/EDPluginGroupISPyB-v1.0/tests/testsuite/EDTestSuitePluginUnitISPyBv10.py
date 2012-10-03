#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 Diamond Light Source
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


from EDTestSuite                                   import EDTestSuite

class EDTestSuitePluginUnitISPyBv10(EDTestSuite):

    def process(self):
        """
        Adds the plugin unit test cases 
        """
        self.addTestCaseFromName("EDTestCasePluginUnitISPyBv10")


if __name__ == '__main__':

    EDTestSuitePluginUnitISPyBv10 = EDTestSuitePluginUnitISPyBv10("EDTestSuitePluginUnitISPyBv10")
    EDTestSuitePluginUnitISPyBv10.execute()


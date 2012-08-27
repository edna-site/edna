#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#                            Sandor Brockhauser (brockhauser@embl-grnoble.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

__authors__ = ["Olof Svensson", "Sandor Brockhauser", "Gleb Bourenkov"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

from EDTestSuite import EDTestSuite

class EDTestSuitePluginUnitXDSv1_1(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitXDSSpotSearchv1_1")


if __name__ == '__main__':

    edTestSuitePluginUnitXDSv1_1 = EDTestSuitePluginUnitXDSv1_1("EDTestSuitePluginUnitXDSv1_1")
    edTestSuitePluginUnitXDSv1_1.execute()

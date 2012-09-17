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
__status__ = "alpha"

import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute




class EDTestCasePluginExecuteXDSSpotSearchv1_1(EDTestCasePluginExecute):

    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginXDSSpotSearchv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSSpotSearch_reference.xml"))


    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteXDSSpotSearchv1_0 = EDTestCasePluginExecuteXDSSpotSearchv1_0("EDTestCasePluginExecuteXDSSpotSearchv1_0")
    edTestCasePluginExecuteXDSSpotSearchv1_0.execute()

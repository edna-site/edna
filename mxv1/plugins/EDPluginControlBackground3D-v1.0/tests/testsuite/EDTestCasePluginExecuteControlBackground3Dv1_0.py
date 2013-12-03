#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlBackground3Dv1_0(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlBackground3Dv1_0")
        self.setRequiredPluginConfiguration("EDPluginBackground3Dv1_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputControlBackground3D_reference.xml"))



    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "mesh2d-x1_1_0001.cbf",
                            "mesh2d-x1_1_0002.cbf",
                            "mesh2d-x1_1_0003.cbf",
                            "mesh2d-x1_1_0004.cbf",
                            "mesh2d-x1_1_0005.cbf",
                             ])


    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)



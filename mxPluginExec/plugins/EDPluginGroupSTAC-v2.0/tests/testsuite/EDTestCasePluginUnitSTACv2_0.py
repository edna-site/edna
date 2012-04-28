#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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


import os

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsPath          import EDUtilsPath


class EDTestCasePluginUnitSTACv2_0(EDTestCasePluginUnit):

    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginSTACv2_0")
        strPluginTestDataHome = self.getPluginTestsDataHome()
        self.strUnitTestDataHome = os.path.join(strPluginTestDataHome, "unitTest")




    def testWriteKappaSettings(self):
        # prepare plugin
        edPluginSTACv2_0 = self.createPlugin()
        edPluginSTACv2_0.setScriptExecutable("cat")
        edPluginSTACv2_0.configure()
        self.cleanUp(edPluginSTACv2_0)


    def process(self):
        self.addTestMethod(self.testWriteKappaSettings)





if __name__ == '__main__':

    edTestCasePluginUnitSTACv2_0 = EDTestCasePluginUnitSTACv2_0("EDTestCasePluginUnitSTACv2_0")
    edTestCasePluginUnitSTACv2_0.execute()

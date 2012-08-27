#coding: utf8
#
#    Project: Solution Scattering
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 DLS
#                  2012 ESRF
#
#    Principal author:       irakli
#                            Jérôme Kieffer (jerome.kieffer@esrf.fr)
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

__authors__ = ["irakli", "Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "2011 DLS; 2012 ESRF"
__date__ = "20120214"

import os

from EDTestCasePluginExecute        import EDTestCasePluginExecute
from XSDataCommon                   import XSDataString


class EDTestCasePluginExecuteControlSolutionScatteringv0_4(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlSolutionScatteringv0_4")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_SolutionScattering.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputSolutionScattering_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultSolutionScattering_reference.xml"))


    def testExecute(self):
        """
        """
        self.getPlugin().readGnomDataColumns(os.path.join(self.getPluginTestsDataHome(), "lyzexp.dat"), 1, None, None)
        self.getPlugin().getDataInput().setTitle(XSDataString('lyzexp.dat'))
        self.run()



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

if __name__ == '__main__':

    edTestCase = EDTestCasePluginExecuteControlSolutionScatteringv0_4("EDTestCasePluginExecuteControlSolutionScatteringv0_4")
    edTestCase.execute()

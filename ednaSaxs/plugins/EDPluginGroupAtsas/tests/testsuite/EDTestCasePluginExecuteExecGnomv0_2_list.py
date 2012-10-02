# coding: utf8
#
#    Project: SolutionScatering
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 DLS
#                  2012 ESRF
#
#    Principal author:       irakli
#                            Jérôme Kieffer
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
__copyright__ = "2011 DLS, 2012 ESRF"

import os

from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDUtilsFile                import EDUtilsFile
from XSDataCommon               import XSDataDouble
from EDDecorator                import timeit
class EDTestCasePluginExecuteExecGnomv0_2_list(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Gnomv0_2
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecGnomv0_2")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputGnom_reference_list.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultGnom_reference.xml"))

    @timeit
    def testExecute(self):
        """
        """
        self.run()



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

    def postProcess(self):
        """
        """
        self.plugin.plotFittingResults()


if __name__ == '__main__':

    testGnomv0_2instance = EDTestCasePluginExecuteExecGnomv0_2("EDTestCasePluginExecuteExecGnomv0_2")
    testGnomv0_2instance.execute()

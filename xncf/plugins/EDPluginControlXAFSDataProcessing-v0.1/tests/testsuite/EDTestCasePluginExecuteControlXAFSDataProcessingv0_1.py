#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:       irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlXAFSDataProcessingv0_1(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlXAFSDataProcessingv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_XAFSDataProcessing.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputXAFSDataProcessing_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultXAFSDataProcessing_reference.xml"))


    def testExecute(self):
        """
        """
        _tmpDataHome = "/dls/b18/data/2010/cm1901-3/Experiment_1/nexus"
        self.getPlugin().readXAFSNexusData(os.path.join(_tmpDataHome, "Ptfoil3_1_532.nxs"), \
                                       '/entry1/counterTimer01/Energy', \
                                       '/entry1/counterTimer01/lnI0It')
        self.run()



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

if __name__ == '__main__':

    edTestCasePluginExecuteControlXAFSDataProcessingv0_1 = EDTestCasePluginExecuteControlXAFSDataProcessingv0_1("EDTestCasePluginExecuteControlXAFSDataProcessingv0_1")
    edTestCasePluginExecuteControlXAFSDataProcessingv0_1.execute()

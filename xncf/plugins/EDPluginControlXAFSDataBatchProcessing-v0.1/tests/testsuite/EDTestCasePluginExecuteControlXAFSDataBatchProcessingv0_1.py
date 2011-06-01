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


class EDTestCasePluginExecuteControlXAFSDataBatchProcessingv0_1(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlXAFSDataBatchProcessingv0_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_XAFSDataBatchProcessing.xml"))
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputXAFSDataBatchProcessing_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultXAFSDataBatchProcessing_reference.xml"))


    def testExecute(self):
        """
        """
        _tmpDataHome = "/dls/b18/data/2010/cm1901-3/Experiment_1/nexus"
        _tmpFileNames = [os.path.join(_tmpDataHome, _fileName) for _fileName in ["Ptfoil3_7_572.nxs", \
                                                                                "Ptfoil3_6_571.nxs", \
                                                                                "Ptfoil3_5_570.nxs", \
                                                                                "Ptfoil3_4_569.nxs", \
                                                                                "Ptfoil3_3_568.nxs", \
                                                                                "Ptfoil3_2_567.nxs", \
                                                                                "Ptfoil3_1_566.nxs"]]
          
        self.getPlugin().readXAFSNexusFiles(_tmpFileNames, '/entry1/counterTimer01/Energy', '/entry1/counterTimer01/lnI0It', '/entry1/entry_identifier')
        self.run()



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

if __name__ == '__main__':

    edTestCasePluginExecuteControlXAFSDataBatchProcessingv0_1 = EDTestCasePluginExecuteControlXAFSDataBatchProcessingv0_1("EDTestCasePluginExecuteControlXAFSDataBatchProcessingv0_1")
    edTestCasePluginExecuteControlXAFSDataBatchProcessingv0_1.execute()

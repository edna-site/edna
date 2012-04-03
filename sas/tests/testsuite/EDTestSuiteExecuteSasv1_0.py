# coding: utf8
#
#    Project: BioSaxs Downstream processing
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Jérôme Kieffer (kieffer@esrf.fr) 
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
__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDTestSuite import EDTestSuite


class EDTestSuiteExecuteSasv1_0(EDTestSuite):


    def process(self):
        """
        """
        # Test as well the execPlugins
        self.addTestCaseFromName("EDTestCasePluginExecuteExecDamaverv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecSupcombv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecDamminv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecDamfiltv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecGnomv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecGnomv0_2")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecDamstartv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecDammifv0_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlSolutionScatteringv0_2")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlSolutionScatteringv0_3")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlSolutionScatteringv0_4")

##############################################################################
if __name__ == '__main__':

    edTestSuite = EDTestSuiteExecuteSasv1_0("EDTestSuiteExecuteSasv1_0")
    edTestSuite.execute()

##############################################################################

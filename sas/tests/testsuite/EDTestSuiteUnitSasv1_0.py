# coding: utf8
#
#    Project: bioSaxs Downstream processing
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuiteUnitBioSaxsv1_0.py 923 2009-10-27 13:35:32Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Jérôme Kieffer (kieffer@esrf.fr) 
#
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

from EDTestSuite           import EDTestSuite


class EDTestSuiteUnitSasv1_0(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitExecDamaverv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecSupcombv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecDamminv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecDamfiltv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecGnomv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecGnomv0_2")
        self.addTestCaseFromName("EDTestCasePluginUnitExecDamstartv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitExecDammifv0_1")
        self.addTestCaseFromName("EDTestCasePluginUnitControlSolutionScatteringv0_2")
        self.addTestCaseFromName("EDTestCasePluginUnitControlSolutionScatteringv0_3")
        self.addTestCaseFromName("EDTestCasePluginUnitControlSolutionScatteringv0_4")


##############################################################################
if __name__ == '__main__':

    edTestSuite = EDTestSuiteUnitSasv1_0("EDTestSuiteUnitSasv1_0")
    edTestSuite.execute()

##############################################################################

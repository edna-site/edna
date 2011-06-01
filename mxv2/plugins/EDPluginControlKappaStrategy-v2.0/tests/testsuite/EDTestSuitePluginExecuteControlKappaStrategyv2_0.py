#
#    Project: EDNA MXv2
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


from EDTestSuite                                   import EDTestSuite

class EDTestSuitePluginExecuteControlKappaStrategyv2_0(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlKappaStrategyv2_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlKappaStrategyv2_0_withDamPar")


if __name__ == '__main__':

    edTestSuitePluginExecuteControlKappaStrategyv2_0 = EDTestSuitePluginExecuteControlKappaStrategyv2_0("EDTestSuitePluginExecuteControlKappaStrategyv2_0")
    edTestSuitePluginExecuteControlKappaStrategyv2_0.execute()


#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Marie-Francoise Incardona (incardon@esrf.fr)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDTestSuite                                  import EDTestSuite

class EDTestSuitePluginExecuteInterfacev1_1(EDTestSuite):


    def process(self):
        #self.addTestCaseFromName( "EDTestCasePluginExecuteCCP4iv1_1" )
        self.addTestCaseFromName("EDTestCasePluginExecuteCCP4iv1_1_withDataSetInput")
        self.addTestCaseFromName("EDTestCasePluginExecuteSubWedgeMergev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlSubWedgeAssemblev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge")


if __name__ == '__main__':

    edTestSuitePluginExecuteInterfacev1_1 = EDTestSuitePluginExecuteInterfacev1_1("EDTestSuitePluginExecuteInterfacev1_1")
    edTestSuitePluginExecuteInterfacev1_1.execute()

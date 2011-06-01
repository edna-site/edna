#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#                            Jerome Kieffer (kieffer@esrf.fr)
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
__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite           import EDTestSuite


class EDTestSuitePluginUnitPhotov1(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitControlDevelopRawv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitCopyExifv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecDcrawv1_0")

if __name__ == '__main__':

    edTestSuitePluginUnitPhotov1 = EDTestSuitePluginUnitPhotov1()
    edTestSuitePluginUnitPhotov1.execute()


#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuiteKernel.py 788 2009-07-16 07:45:55Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:  Olof Svensson (svensson@esrf.fr)
#                        Jerome Kieffer (Jerome.Kieffer@esrf.fr)
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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDTestSuite    import EDTestSuite


class EDTestSuitePluginExecutePhotov1(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlDevelopRawv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteCopyExifv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteExecDcrawv1_0")


if __name__ == '__main__':

    edTestSuitePluginExecutePhotov1 = EDTestSuitePluginExecutePhotov1("EDTestSuitePluginExecutePhotov1")
    edTestSuitePluginExecutePhotov1.execute()


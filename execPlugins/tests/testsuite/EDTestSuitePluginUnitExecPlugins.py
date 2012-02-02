#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginUnitMXPluginExec.py 923 2009-10-27 13:35:32Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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
__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer", "Karl Levik"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite           import EDTestSuite


class EDTestSuitePluginUnitExecPlugins(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginUnitAccumulatorv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitExecCommandLinev10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitFIT2Dv1_0")
        self.addTestSuiteFromName("EDTestSuiteUnitSPDv10")
        self.addTestCaseFromName("EDTestCasePluginUnitExecThumbnailv10")
        self.addTestCaseFromName("EDTestCasePluginUnitExecVideov10")
        self.addTestCaseFromName("EDTestCasePluginUnitExecVideov10")
        self.addTestSuiteFromName("EDTestSuitePluginUnitHDF5")
        self.addTestSuiteFromName("EDTestSuitePluginUnitGroupSaxsv1_0")
        self.addTestCaseFromName("EDTestCasePluginUnitWaitFile")
        self.addTestCaseFromName("EDTestCasePluginUnitWaitMultiFile")
        self.addTestSuiteFromName("EDTestSuitePluginUnitFilterImage")
        #Atsas        
        self.addTestSuiteFromName("EDTestSuiteUnitAtsas")
        # Shift & offset
        self.addTestSuiteFromName("EDTestSuitePluginExecUnitShift")
        #documentation
        self.addTestCaseFromName("EDTestCasePluginUnitExecEpydocv1_0")

##############################################################################
if __name__ == '__main__':

    edTestSuitePluginUnitExecPlugins = EDTestSuitePluginUnitExecPlugins()
    edTestSuitePluginUnitExecPlugins.execute()

##############################################################################

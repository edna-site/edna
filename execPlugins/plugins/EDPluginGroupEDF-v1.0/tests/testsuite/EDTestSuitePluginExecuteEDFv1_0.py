#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       <author>
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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginExecuteEDFv1_0(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginExecuteEDFReadHeaderv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteChiToEDFv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2cif")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2array")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_array2array")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chiNbBins")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2spr")
        self.addTestCaseFromName("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi_mask")


##############################################################################
if __name__ == '__main__':

    edTestSuitePluginExecuteEDF = EDTestSuitePluginExecuteEDF("EDTestSuitePluginExecuteEDFv1_0")
    edTestSuitePluginExecuteEDF.execute()

##############################################################################

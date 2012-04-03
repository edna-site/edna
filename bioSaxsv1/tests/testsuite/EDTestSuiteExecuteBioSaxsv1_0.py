# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteMXPluginExec.py 923 2009-10-27 13:35:32Z svensson $"
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


class EDTestSuiteExecuteBioSaxsv1_0(EDTestSuite):


    def process(self):
        """
        """
        # Test as well the execPlugins
        self.addTestSuiteFromName("EDTestSuiteExecuteBioSaxsAsciiExportv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsAveragev1_0")
        self.addTestSuiteFromName("EDTestSuiteExecuteBioSaxsAzimutIntv1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsMetadatav1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsMetadatav1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsNormalizev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsNormalizev1_1")
        self.addTestSuiteFromName("EDTestSuitePluginBioSaxsSmartMergev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsReduceFileSeriev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsProcessOneFilev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsProcessOneFilev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteBioSaxsToSAS")

##############################################################################
if __name__ == '__main__':

    edTestSuite = EDTestSuiteExecuteBioSaxsv1_0("EDTestSuiteExecuteBioSaxsv1_0")
    edTestSuite.execute()

##############################################################################

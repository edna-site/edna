# coding: utf8
# 
#
#    Project: ExecPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble 2010
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, 2010"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi             import EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi
from XSDataEDFv1_0 import XSDataResult1DPowderEDF


class EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chiNbBins(EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi):
    """
    Those are all execution tests for the EDNA Exec plugin <pluginName>
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chi.__init__(self, "EDPluginExportAsciiPowderv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInput1DPowder_edf2chiNbBins.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResult1DPowder_edf2chiNbBins.xml"))
        self.refOutput = "sample1_6284-2048.chi"




if __name__ == '__main__':

    testinstance = EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chiNbBins("EDTestCasePluginExecuteExportAsciiPowderEDF_edf2chiNbBins")
    testinstance.execute()

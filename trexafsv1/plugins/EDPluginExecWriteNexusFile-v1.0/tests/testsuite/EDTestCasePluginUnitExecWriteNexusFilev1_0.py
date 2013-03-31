# coding: utf8
#
#    Project: Time-Resolved EXAFS
#             http://www.edna-site.org
#
#    Copyright (C)      2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, numpy

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsArray import EDUtilsArray

from XSDataCommon import XSDataDouble

from XSDataWriteNexusFilev1_0 import XSDataInputWriteNexusFile

class EDTestCasePluginUnitExecWriteNexusFilev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Control plugin Dexafsv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecWriteNexusFilev1_0")
              


    def testCheckParameters(self):
        strPath = os.path.join(self.getPluginTestsDataHome(), "XSDataInputWriteNexusFile_reference.xml")
        xsDataInputWriteNexusFile = XSDataInputWriteNexusFile.parseFile(strPath)
        edPluginExecWriteNexusFile = self.createPlugin()
        edPluginExecWriteNexusFile.setDataInput(xsDataInputWriteNexusFile)
        edPluginExecWriteNexusFile.checkParameters()
        
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecWriteNexusFilev1_0 = EDTestCasePluginUnitExecWriteNexusFilev1_0("EDTestCasePluginUnitExecWriteNexusFilev1_0")
    edTestCasePluginUnitExecWriteNexusFilev1_0.execute()

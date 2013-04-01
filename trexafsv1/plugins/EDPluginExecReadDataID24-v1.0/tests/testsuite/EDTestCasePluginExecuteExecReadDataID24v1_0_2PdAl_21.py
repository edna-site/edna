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


import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecReadDataID24v1_0_2PdAl_21(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin <pluginName>
    """
    
    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecReadDataID24v1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputReadDataID24_2PdAl_21.xml"))
                 
    def preProcess(self):
        """
        Download reference file
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["2PdAl_21_xoplog_0_asc0",
                            "2PdAl_21_xoplog_1_asc0",
                            "2PdAl_21_xoplog_2_asc0",
                            "2PdAl_21_xoplog_3_asc0",
                            "2PdAl_21_xoplog_4_asc0",
                            "2PdAl_21_xoplog_5_asc0",
                            "2PdAl_21_xoplog_6_asc0"])
        
    def testExecute(self):
        self.run()
        xsDataResult = self.getPlugin().dataOutput
        xsDataArrayEnergy = xsDataResult.energy
        xsDataArrayEnergy.exportToFile("XSDataArrayEnergy_2PdAl_21.xml")
        xsDataArrayData = xsDataResult.dataArray
        xsDataArrayData.exportToFile("XSDataArrayData_2PdAl_21.xml")        

    def process(self):
        self.addTestMethod(self.testExecute)

        


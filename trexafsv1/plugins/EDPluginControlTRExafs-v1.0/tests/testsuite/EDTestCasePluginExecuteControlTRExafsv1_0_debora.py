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

__author__="<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlTRExafsv1_0_debora(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin <pluginName>
    """
    
    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlTRExafsv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputTRExafs_debora.xml"))
#                                           "XSDataInputTRExafs_debora.xml"))
#        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
#                                                     "XSDataResultJesfv1_0_reference.xml"))
                 
    def preProcess(self):
        """
        Download reference files
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["XSDataArrayEnergy_debora.xml", "XSDataArrayData_debora.xml"])
        
    def testExecute(self):
        """
        """ 
        self.run()
#        plugin = self.getPlugin()
#
#################################################################################
## Compare XSDataResults
#################################################################################
#
#        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        EDVerbose.DEBUG("Checking obtained result...")
#        xsDataResultReference = XSDataResult.parseString(strExpectedOutput)
#        xsDataResultObtained = plugin.getDataOutput()
#        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")
        

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        


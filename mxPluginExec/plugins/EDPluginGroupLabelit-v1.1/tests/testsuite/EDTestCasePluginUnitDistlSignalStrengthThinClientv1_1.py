#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os

from EDAssert import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength
from XSDataLabelitv1_1 import XSDataResultDistlSignalStrength

class EDTestCasePluginUnitDistlSignalStrengthThinClientv1_1(EDTestCasePluginUnit):


    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginDistlSignalStrengthThinClientv1_1")
        self.__strReferenceInputFile1 = os.path.join(self.getPluginTestsDataHome(), "XSDataInputDistlSignalStrength_reference.xml")
        #self.__strReferenceOutputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultLabelitDistl_reference.xml")


    def testParseLabelitDistlOutput(self):
        """
        This method test the parsing of the distl.signal_strength results in the log file.
        """
        edPluginDistlSignalStrengthThinClientv1_1 = self.createPlugin()
        strPathToLabelitLogText = os.path.join(self.getPluginTestsDataHome(), "phenix.distl_thin_client_v17_650.txt")
        strLabelitLogText = self.readAndParseFile(strPathToLabelitLogText)
        xsDataImageQualityIndicators = edPluginDistlSignalStrengthThinClientv1_1.parseLabelitDistlOutput(strLabelitLogText)
        xmlInput1 = self.readAndParseFile(self.__strReferenceInputFile1)
        xsDataInputDistlSignalStrength = XSDataInputDistlSignalStrength.parseString(xmlInput1)
        xsDataImageQualityIndicators.setImage(xsDataInputDistlSignalStrength.getReferenceImage())

        strResultDistlSignalStrengthFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultDistlSignalStrengthThinClient_reference.xml")
        strResultDistlSignalStrength = self.readAndParseFile(strResultDistlSignalStrengthFile)
        xsDataResultDistlSignalStrength = XSDataResultDistlSignalStrength.parseString(strResultDistlSignalStrength)
        xsDataImageQualityIndicatorsReference = xsDataResultDistlSignalStrength.getImageQualityIndicators()
        EDAssert.equal(xsDataImageQualityIndicatorsReference.marshal(), xsDataImageQualityIndicators.marshal())




    def testGenerateExecutiveSummary(self):
        """
        This method tests the generateExecutiveSummary of the Labelit plugin.
        It contains no assert call so the contents of the executive summary is not tested.
        """
        edPluginDistlSignalStrengthThinClientv1_1 = self.createPlugin()
        xmlInput1 = self.readAndParseFile(self.__strReferenceInputFile1)
        edPluginDistlSignalStrengthThinClientv1_1.setDataInput(xmlInput1)

        strResultDistlSignalStrengthFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultDistlSignalStrengthThinClient_reference.xml")
        strResultDistlSignalStrength = self.readAndParseFile(strResultDistlSignalStrengthFile)
        xsDataResultDistlSignalStrength = XSDataResultDistlSignalStrength.parseString(strResultDistlSignalStrength)
        edPluginDistlSignalStrengthThinClientv1_1.setDataOutput(xsDataResultDistlSignalStrength)
        edPluginDistlSignalStrengthThinClientv1_1.generateExecutiveSummary(edPluginDistlSignalStrengthThinClientv1_1)


    def process(self):
        self.addTestMethod(self.testParseLabelitDistlOutput)
        self.addTestMethod(self.testGenerateExecutiveSummary)


if __name__ == '__main__':

    EDTestCasePluginUnitDistlSignalStrengthThinClientv1_1 = EDTestCasePluginUnitDistlSignalStrengthThinClientv1_1("EDTestCasePluginUnitDistlSignalStrengthThinClientv1_1")
    EDTestCasePluginUnitDistlSignalStrengthThinClientv1_1.execute()


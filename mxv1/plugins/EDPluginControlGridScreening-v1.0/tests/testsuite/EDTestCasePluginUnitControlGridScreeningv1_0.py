#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString

from XSDataGridScreeningv1_0 import XSDataInputGridScreening
from XSDataGridScreeningv1_0 import XSDataGridScreeningFileNameParameters

class EDTestCasePluginUnitControlGridScreeningv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlGridScreeningv1_0")
        self.strPathToReferenceInput = os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputGridScreening_reference.xml")


    def testCheckParameters(self):
        strXMLInput = self.readAndParseFile(self.strPathToReferenceInput)
        xsDataInput = XSDataInputGridScreening.parseString(strXMLInput)
        edPluginExecCharacterisation = self.createPlugin()
        edPluginExecCharacterisation.setDataInput(xsDataInput)
        edPluginExecCharacterisation.checkParameters()


    def testGetFileNameParameters(self):
        edPluginExecCharacterisation = self.createPlugin()
        xsDataGridScreeningFileNameParameters = edPluginExecCharacterisation.getFileNameParameters("mesh_0_21.676_-0.051_22_001.mccd")
        xsDataGridScreeningFileNameParameters_reference = XSDataGridScreeningFileNameParameters()
        xsDataGridScreeningFileNameParameters_reference.setScanId1(XSDataString("0"))
        xsDataGridScreeningFileNameParameters_reference.setMotorPosition1(XSDataString("21.676"))
        xsDataGridScreeningFileNameParameters_reference.setMotorPosition2(XSDataString("-0.051"))
        xsDataGridScreeningFileNameParameters_reference.setScanId2(XSDataString("22"))
        EDAssert.equal(xsDataGridScreeningFileNameParameters_reference.marshal(), xsDataGridScreeningFileNameParameters.marshal(), "Test with conforming image name")
        xsDataGridScreeningFileNameParameters2 = edPluginExecCharacterisation.getFileNameParameters("ref-testscale_1_001.img")
        EDAssert.equal(None, xsDataGridScreeningFileNameParameters2, "Test with non-conforming image name")
        xsDataGridScreeningFileNameParameters3 = edPluginExecCharacterisation.getFileNameParameters("AAA060A_TVP_2_10_57_001.mccd")
        xsDataGridScreeningFileNameParameters_reference3 = XSDataGridScreeningFileNameParameters()
        xsDataGridScreeningFileNameParameters_reference3.setScanId1(XSDataString("TVP"))
        xsDataGridScreeningFileNameParameters_reference3.setMotorPosition1(XSDataString("2"))
        xsDataGridScreeningFileNameParameters_reference3.setMotorPosition2(XSDataString("10"))
        xsDataGridScreeningFileNameParameters_reference3.setScanId2(XSDataString("57"))
        EDAssert.equal(xsDataGridScreeningFileNameParameters_reference3.marshal(), xsDataGridScreeningFileNameParameters3.marshal(), "Test with conforming image name")
        xsDataGridScreeningFileNameParameters4 = edPluginExecCharacterisation.getFileNameParameters("semet_nt_7_16_9_001.mccd")
        xsDataGridScreeningFileNameParameters_reference4 = XSDataGridScreeningFileNameParameters()
        xsDataGridScreeningFileNameParameters_reference4.setScanId1(XSDataString("nt"))
        xsDataGridScreeningFileNameParameters_reference4.setMotorPosition1(XSDataString("7"))
        xsDataGridScreeningFileNameParameters_reference4.setMotorPosition2(XSDataString("16"))
        xsDataGridScreeningFileNameParameters_reference4.setScanId2(XSDataString("9"))
        EDAssert.equal(xsDataGridScreeningFileNameParameters_reference4.marshal(), xsDataGridScreeningFileNameParameters4.marshal(), "Test with conforming image name")



    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testGetFileNameParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlGridScreeningv1_0 = EDTestCasePluginUnitControlGridScreeningv1_0("EDTestCasePluginUnitControlGridScreeningv1_0")
    EDTestCasePluginUnitControlGridScreeningv1_0.execute()

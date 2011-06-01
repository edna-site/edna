# coding: utf8
#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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


from EDVerbose             import EDVerbose
from EDTestCasePluginUnit  import EDTestCasePluginUnit
from XSDataDiffractionCTv1 import XSDataInputDiffractionCT
from XSDataDiffractionCTv1 import XSDataImage
from XSDataDiffractionCTv1 import XSDataFile
from XSDataDiffractionCTv1 import XSDataString

class EDTestCasePluginUnitControlDiffractionCTv1_0(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginControlDiffractionCTv1_0", "EDPluginControlDCTPowderIntegration-v1.0", _edStringTestName)


    def testCheckParameters(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitControlDiffractionCTv1_0.testCheckParameters")
        xsDataInput = XSDataInputDiffractionCT()
        xsDataImage = XSDataImage()
        xsDataInput.setImage(xsDataImage)
        xsDataFile = XSDataFile()
        xsDataInput.setDestinationDirectory(xsDataFile)
        xsDataInput.setSinogramFileNamePrefix(XSDataString("FakePrefix"))
        xsDataInput.setPowderDiffractionSubdirectory(XSDataString("Powder"))
        edPluginControlDCTPowderIntegration = self.createPlugin()
        edPluginControlDCTPowderIntegration.setDataInput(xsDataInput)
        edPluginControlDCTPowderIntegration.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitControlDiffractionCTv1_0 = EDTestCasePluginUnitControlDiffractionCTv1_0("EDTestCasePluginUnitControlDiffractionCTv1_0")
    edTestCasePluginUnitControlDiffractionCTv1_0.execute()

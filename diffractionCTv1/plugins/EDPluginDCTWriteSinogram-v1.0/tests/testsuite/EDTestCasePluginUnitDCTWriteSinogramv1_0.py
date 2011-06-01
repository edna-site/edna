#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
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


from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataDiffractionCTv1 import XSDataString
from XSDataDiffractionCTv1 import XSDataFile
from XSDataDiffractionCTv1 import XSDataInputWriteSinogram

class EDTestCasePluginUnitDCTWriteSinogramv1_0(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginDCTWriteSinogramv1_0")


    def testCheckParameters(self):

        xsDataFileIntegratedIntensities = XSDataFile()
        xsDataFileIntegratedIntensities.setPath(XSDataString("/tmp/file.cif"))

        xsDataFileSinogramDirectory = XSDataFile()
        xsDataFileSinogramDirectory.setPath(XSDataString("/tmp"))

        xsDataString = XSDataString("FakeExample")


        xsDataInput = XSDataInputWriteSinogram()
        xsDataInput.setIntegratedIntensities(xsDataFileIntegratedIntensities)
        xsDataInput.setSinogramDirectory(xsDataFileSinogramDirectory)
        xsDataInput.setSinogramFileNamePrefix(xsDataString)



        edPluginExecDCTWriteSinogram = self.createPlugin()
        edPluginExecDCTWriteSinogram.setDataInput(xsDataInput)
        edPluginExecDCTWriteSinogram.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



##############################################################################


if __name__ == '__main__':

    EDTestCasePluginUnitDCTWriteSinogramv1_0 = EDTestCasePluginUnitDCTWriteSinogramv1_0("EDTestCasePluginUnitDCTWriteSinogramv1_0")
    EDTestCasePluginUnitDCTWriteSinogramv1_0.execute()

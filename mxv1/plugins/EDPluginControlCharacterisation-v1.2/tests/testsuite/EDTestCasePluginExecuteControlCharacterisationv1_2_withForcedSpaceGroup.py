#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlCharacterisationv1_1With2Sweep.py 1509 2010-05-11 07:17:48Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr) 
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


__authors__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlCharacterisationv1_2 import EDTestCasePluginExecuteControlCharacterisationv1_2




class EDTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup(EDTestCasePluginExecuteControlCharacterisationv1_2):
    """
    Test of characterisation error messages.
    """

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv1_2.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_withForcedSpaceGroup.xml"))
        self.setNoExpectedWarningMessages(1)
        self.setNoExpectedErrorMessages(0)


    def preProcess(self):
        EDTestCasePluginExecuteControlCharacterisationv1_2.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        EDTestCasePluginExecuteControlCharacterisationv1_2.testExecute(self)

        edPlugin = self.getPlugin()
        xsDataCharacterisation = edPlugin.getDataOutput()
        xsDataResultIndexing = xsDataCharacterisation.getIndexingResult()
        xsDataSelectedSolution = xsDataResultIndexing.getSelectedSolution()
        xsDataCrystal = xsDataSelectedSolution.getCrystal()
        xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
        strSpaceGroupName = xsDataSpaceGroup.getName().getValue()
        EDAssert.equal("P1", strSpaceGroupName, "Selected indexing solution is P1")



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup = EDTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup("EDTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup")
    edTestCasePluginExecuteControlCharacterisationv1_2_withForcedSpaceGroup.execute()

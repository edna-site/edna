#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlCharacterisationv1_1With2Sweep.py 1509 2010-05-11 07:17:48Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlCharacterisationv1_3 import EDTestCasePluginExecuteControlCharacterisationv1_3




class EDTestCasePluginExecuteControlCharacterisationv1_3_indexingError(EDTestCasePluginExecuteControlCharacterisationv1_3):
    """
    Test of characterisation error messages.
    """

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv1_3.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv1_3_indexingError")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_indexingError.xml"))
        self.setNoExpectedWarningMessages(4)
        self.setNoExpectedErrorMessages(1)
        self.setAcceptPluginFailure(True)


    def preProcess(self):
        EDTestCasePluginExecuteControlCharacterisationv1_3.preProcess(self)
        self.loadTestImage([ "indexingError_2_001.img" ])


    def testExecute(self):
        EDTestCasePluginExecuteControlCharacterisationv1_3.testExecute(self)

        edPlugin = self.getPlugin()
        strStatusMessage = None
        if edPlugin.hasDataOutput("statusMessage"):
            strStatusMessage = edPlugin.getDataOutput("statusMessage")[0].getValue()
        EDAssert.equal(True, strStatusMessage.find("Indexing FAILURE") != -1, "Status message contains 'Indexing FAILURE'")
        
        edPlugin.generateExecutiveSummary(edPlugin)
        edPlugin.verboseScreenExecutiveSummary()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv1_3_indexingError = EDTestCasePluginExecuteControlCharacterisationv1_3_indexingError("EDTestCasePluginExecuteControlCharacterisationv1_3_indexingError")
    edTestCasePluginExecuteControlCharacterisationv1_3_indexingError.execute()

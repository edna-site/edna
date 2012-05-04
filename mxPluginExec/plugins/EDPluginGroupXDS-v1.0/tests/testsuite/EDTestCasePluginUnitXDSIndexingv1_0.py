#
#    Project: EDNA mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
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

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"

import os

from EDVerbose      import EDVerbose
from EDUtilsPath      import EDUtilsPath
from EDTestCasePluginUnit     import EDTestCasePluginUnit

from EDAssert         import EDAssert


class EDTestCasePluginUnitXDSIndexingv1_0(EDTestCasePluginUnit):


    def __init__(self, _pyStrTestName="EDPluginXDSIndexingv1_0"):
        EDTestCasePluginUnit.__init__(self, _pyStrTestName)
        self.strReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSIndexing_reference.xml")


    def testSetDataInput(self):
        """
        """
        edPluginXDSIndexingv1_0 = self.createPlugin()
        xsPluginItemGood01 = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "EDPluginXDSIndexingv1_0_configuration_OK_01.xml"))
        edPluginXDSIndexingv1_0.setConfiguration(xsPluginItemGood01)
        edPluginXDSIndexingv1_0.setScriptExecutable("cat")
        edPluginXDSIndexingv1_0.configure()

        from XSDataXDSv1_0 import XSDataInputXDSIndexing
        xmlInput = self.readAndParseFile(self.strReferenceInputFile)
        xsDataXDSIndexingInputReference = XSDataInputXDSIndexing.parseString(xmlInput)
        xsDataXDSIndexingInputReference.exportToFile("XSDataInputXDSIndexing_reference.xml")
        edPluginXDSIndexingv1_0.setDataInput(xmlInput)

        xsDataXDSIndexingInput = edPluginXDSIndexingv1_0.getDataInput()
        xsDataXDSIndexingInput.exportToFile("XSDataInputXDSIndexing.xml")
        EDAssert.equal(xsDataXDSIndexingInputReference.marshal(), xsDataXDSIndexingInput.marshal())

        self.cleanUp(edPluginXDSIndexingv1_0)


    def process(self):
        self.addTestMethod(self.testSetDataInput)


if __name__ == '__main__':

    edTestCasePluginUnitXDSIndexingv1_0 = EDTestCasePluginUnitXDSIndexingv1_0("EDTestCasePluginUnitXDSIndexingv1_0")
    edTestCasePluginUnitXDSIndexingv1_0.execute()

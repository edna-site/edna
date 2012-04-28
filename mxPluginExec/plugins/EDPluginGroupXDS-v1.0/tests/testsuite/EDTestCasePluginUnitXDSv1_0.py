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

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDUtilsPath import EDUtilsPath

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsTest import EDUtilsTest

from XSDataXDSv1_0 import XSDataInputXDS

class EDTestCasePluginUnitXDSv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName="EDPluginXDSv1_0"):
        EDTestCasePluginUnit.__init__(self, _strTestName)
        self.m_strReferenceDataInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSIndexing_reference.xml")


    def testGenerateXDSCommands(self):
        from XSDataXDSv1_0 import XSDataInputXDSIndexing
        xsDataInputXDSIndexing = XSDataInputXDSIndexing.parseFile(self.m_strReferenceDataInputFile)
        edPluginXDSv1_0 = self.createPlugin()
        edPluginXDSv1_0.setXSDataInputClass(XSDataInputXDS)
        edPluginXDSv1_0.setScriptExecutable("cat")
        edPluginXDSv1_0.configure()
        edPluginXDSv1_0.setDataInput(xsDataInputXDSIndexing)
        edPluginXDSv1_0.addJob("INIT")
        edPluginXDSv1_0.generateXDSCommands()
        edPluginXDSv1_0.writeInputXDSFile()


    def testCreateImageLinks(self):
        from XSDataXDSv1_0 import XSDataInputXDSIndexing
        xsDataInputXDSIndexing = XSDataInputXDSIndexing.parseFile(self.m_strReferenceDataInputFile)
        edPluginXDSv1_0 = self.createPlugin()
        edPluginXDSv1_0.setXSDataInputClass(XSDataInputXDS)
        edPluginXDSv1_0.setScriptExecutable("cat")
        edPluginXDSv1_0.configure()
        edPluginXDSv1_0.setDataInput(xsDataInputXDSIndexing)
        edPluginXDSv1_0.createImageLinks()
        strScript = edPluginXDSv1_0.prepareScript()
        edPluginXDSv1_0.writeExecutableScript(strScript)


    def process(self):
        self.addTestMethod(self.testGenerateXDSCommands)
        self.addTestMethod(self.testCreateImageLinks)




if __name__ == '__main__':

    edTestCasePluginUnitXDSv1_0 = EDTestCasePluginUnitXDSv1_0("EDTestCasePluginUnitXDSv1_0")
    edTestCasePluginUnitXDSv1_0.execute()

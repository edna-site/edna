#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France

#    Principal author:       Jerome Kieffer kieffer@esrf.fr
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

__author__ = "Jerome Kieffer kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataExecVideo        import XSDataInputExecVideo

class EDTestCasePluginUnitExecVideov10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Videov10
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecVideov10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputVideo_reference.xml")

    def testCheckParameters(self):
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecVideo = self.createPlugin()
        edPluginExecVideo.setDataInput(pyStrXMLInput)
        edPluginExecVideo.checkParameters()


    def testpreProcess(self):
        self.loadTestImage([ "sample1_%04i.jpg" % i for i in range(50, 101)])
        pyStrXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        edPluginExecVideo = self.createPlugin()
        edPluginExecVideo.setDataInput(pyStrXMLInput)
        edPluginExecVideo.preProcess()
        self.cleanUp(edPluginExecVideo)

    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testpreProcess)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitExecVideov10 = EDTestCasePluginUnitExecVideov10("EDTestCasePluginUnitExecVideov10")
    edTestCasePluginUnitExecVideov10.execute()

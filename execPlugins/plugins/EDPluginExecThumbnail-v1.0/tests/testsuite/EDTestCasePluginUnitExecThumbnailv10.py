#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France

#    Principal author:       Jerome Kieffer (Jerome.Kieffer@esrf.eu)
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

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, tempfile
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataExecThumbnail    import XSDataInputExecThumbnail
from EDFactoryPluginStatic      import EDFactoryPluginStatic


# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")


class EDTestCasePluginUnitExecThumbnailv10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Thumbnailv10
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecThumbnailv10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputThumbnail_reference.xml")

    def testCheckParameters(self):

        strXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
#        xsDataInput = XSDataInputExecThumbnail()
        EDVerbose.DEBUG("strXMLInput = " + strXMLInput)
        edPluginExecThumbnail = self.createPlugin()
        edPluginExecThumbnail.setDataInput(strXMLInput)
        edPluginExecThumbnail.checkParameters()


    def testpreProcess(self):
        self.loadTestImage([ "diff6105.edf" ])
        strXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
#        xsDataInput = XSDataInputExecThumbnail()
        EDVerbose.DEBUG("strXMLInput = " + strXMLInput)
        edPluginExecThumbnail = self.createPlugin()
        edPluginExecThumbnail.setDataInput(strXMLInput)
        edPluginExecThumbnail.preProcess()
        self.cleanUp(edPluginExecThumbnail)

    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testpreProcess)


##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitExecThumbnailv10 = EDTestCasePluginUnitExecThumbnailv10("EDTestCasePluginUnitExecThumbnailv10")
    edTestCasePluginUnitExecThumbnailv10.execute()

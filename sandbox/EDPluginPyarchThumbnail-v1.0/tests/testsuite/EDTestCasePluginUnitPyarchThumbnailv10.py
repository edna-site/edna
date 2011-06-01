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
from EDAssert import EDAssert
from XSDataPyarchThumbnail    import XSDataInputPyarchThumbnail


class EDTestCasePluginUnitPyarchThumbnailv10(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Thumbnailv10
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginPyarchThumbnailv10")
        self.m_pyStrReferenceInputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataInputPyarchThumbnail_reference.xml")

    def testCheckParameters(self):

        strXMLInput = self.readAndParseFile(self.m_pyStrReferenceInputFile)
        EDVerbose.DEBUG("strXMLInput = " + strXMLInput)
        edPluginPyarchThumbnail = self.createPlugin()
        edPluginPyarchThumbnail.setDataInput(strXMLInput)
        edPluginPyarchThumbnail.checkParameters()


    def testCreatePyarchFilePath(self):
        edPluginPyarchThumbnail = self.createPlugin()
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/"))
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/data"))
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/data/visitor"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415", edPluginPyarchThumbnail.createPyarchFilePath("/data/visitor/mx415/id14eh2"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212", edPluginPyarchThumbnail.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1", edPluginPyarchThumbnail.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212/1"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1/2", edPluginPyarchThumbnail.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212/1/2"))
        # Test with inhouse account...
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/"))
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/data"))
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2"))
        EDAssert.equal(None, edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2/inhouse"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232", edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2/inhouse/opid232"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525", edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1", edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525/1"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1/2", edPluginPyarchThumbnail.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525/1/2"))


    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testCreatePyarchFilePath)




if __name__ == '__main__':

    edTestCasePluginUnitPyarchThumbnailv10 = EDTestCasePluginUnitPyarchThumbnailv10("EDTestCasePluginUnitPyarchThumbnailv10")
    edTestCasePluginUnitPyarchThumbnailv10.execute()

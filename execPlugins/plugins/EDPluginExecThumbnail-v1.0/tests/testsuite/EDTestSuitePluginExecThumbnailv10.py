#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
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

from EDTestSuite  import EDTestSuite



class EDTestSuitePluginExecThumbnailv10(EDTestSuite):
    """
    This is the test suite for EDNA plugin Thumbnailv10 
    It will run subsequently all unit tests and execution tests.     
    """

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_minimal")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_resize")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_keepRatio")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_png")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_gamma")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_invert")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_equalize")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_equalize_colorize")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_normalize")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_colorize")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_pilatus2M")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_pilatus6M")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecThumbnailv10_pilatus6M_png")

if __name__ == '__main__':
    edTestSuitePluginExecThumbnailv10 = EDTestSuitePluginExecThumbnailv10()
    edTestSuitePluginExecThumbnailv10.execute()

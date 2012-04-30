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

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDTestCasePluginExecuteExecThumbnailv10             import EDTestCasePluginExecuteExecThumbnailv10
from XSDataExecThumbnail                 import XSDataInputExecThumbnail
from XSDataExecThumbnail                 import XSDataResultExecThumbnail

class EDTestCasePluginExecuteExecThumbnailv10_resize(EDTestCasePluginExecuteExecThumbnailv10):
    """
    Those are all execution tests for the EDNA Exec plugin Thumbnailv10 with resize option without keeping the ratio
    """
    def __init__(self):
        """
        Constructor of the Class Execute Test Plugin Exec fro thumbnails with  resize option without keeping the ratio
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecThumbnailv10")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_Thumbnail.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputThumbnail_reference_resize.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultThumbnail_reference_resize.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0

if __name__ == '__main__':

    testThumbnailv10instance = EDTestCasePluginExecuteExecThumbnailv10_resize()
    testThumbnailv10instance.execute()

#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import tarfile, tempfile

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteExecOutputHTMLv1_0  import EDTestCasePluginExecuteExecOutputHTMLv1_0


class EDTestCasePluginExecuteExecOutputHTMLv1_0_withDnafiles(EDTestCasePluginExecuteExecOutputHTMLv1_0):
    """
    Those are all execution tests for the EDNA Exec plugin OutputHTMLv1_0
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecuteExecOutputHTMLv1_0.__init__(self, "EDPluginExecOutputHTMLv1_0")
        # This plugin is somewhat peculiar - a tgz file as input:


    def preProcess(self, _edObject = None):
        EDTestCasePluginExecuteExecOutputHTMLv1_0.preProcess(self)
        self.strTestDnaFileDirectory = tempfile.mkdtemp(prefix = "EDTestCasePluginExecuteExecOutputHTMLv1_0_withDnafiles_")
        os.environ["EDNA_DNA_FILE_DIRECTORY"] = self.strTestDnaFileDirectory
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataFileDnaWorkingDirectory.xml"), "dnaFileDirectory")
        
    def postProcess(self, _edObject = None):
        EDTestCasePluginExecuteExecOutputHTMLv1_0.postProcess(self)
        os.removedirs(self.strTestDnaFileDirectory)
        


#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
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
import tarfile

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecOutputHTMLv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin OutputHTMLv1_0
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecOutputHTMLv1_0")
        # This plugin is somewhat peculiar - a tgz file as input:
        self.__strPathToTgzFile = os.path.join(self.getPluginTestsDataHome(), \
            "ControlInterfaceToMXCuBEv1_3.tgz")


    def testExecute(self):
        # Untar the tgz file in the plugin working directory
        edPlugin = self.getPlugin()
        edPlugin.configure()
        strWorkingDirectory = edPlugin.getWorkingDirectory()
        tarfileCharacterisation = tarfile.open(self.__strPathToTgzFile)
        tarfileCharacterisation.extractall(path=strWorkingDirectory)
        self.run()
        # Check for "failure report"
        bFailureReport = False
        strPathToEdnaHtml = os.path.join(os.path.dirname(edPlugin.getWorkingDirectory()), "edna.html")
        pyFile = open(strPathToEdnaHtml)
        strHtml = pyFile.read()
        pyFile.close()
        if strHtml.find("failure report") != -1:
                bFailureReport = True
        EDAssert.equal(False, bFailureReport, "HTML file contains failure report")
        


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testOutputHTMLv1_0instance = EDTestCasePluginExecuteControlOutputHTMLv1_0("EDTestCasePluginExecuteExecOutputHTMLv1_0")
    testOutputHTMLv1_0instance.execute()

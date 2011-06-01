#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
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
__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDTestCasePluginExecuteExecVideov10 import EDTestCasePluginExecuteExecVideov10
from XSDataExecVideo                     import XSDataInputExecVideo
from XSDataExecVideo                     import XSDataResultExecVideo



class EDTestCasePluginExecuteExecVideov10_minimal(EDTestCasePluginExecuteExecVideov10):
    """
    Those are all execution tests for the EDNA Exec plugin Videov10 with the minimum imput parameters.
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecVideov10")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_Video.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputVideo_reference_minimal.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultVideo_reference_minimal.xml"))
#        EDVerbose.DEBUG( "PluginName = " + self.getPluginName() )
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    testVideov10instance = EDTestCasePluginExecuteExecVideov10_minimal("EDTestCasePluginExecuteExecVideov10_minimal")
    testVideov10instance.execute()

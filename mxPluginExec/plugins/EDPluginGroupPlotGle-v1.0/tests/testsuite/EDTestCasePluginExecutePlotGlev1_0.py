# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20120712"
__status__ = "production"

import os


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecutePlotGlev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin PlotGle
    """
    
    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecPlotGlev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_PlotGle.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputPlotGle_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultPlotGle_reference.xml"))
                 
        
    def testExecute(self):
        """
        """ 
        self.run()
        

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        

if __name__ == '__main__':

    testPlotGleinstance = EDTestCasePluginExecuteControlPlotGle("EDTestCasePluginExecuteExecPlotGle")
    testPlotGleinstance.execute()

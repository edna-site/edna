# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
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

import os

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsFile import EDUtilsFile

from XSDataPlotGlev1_0 import XSDataInputPlotGle

class EDTestCasePluginUnitPlotGlev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin PlotGle
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecPlotGlev1_0")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputPlotGle()
        edPluginExecPlotGle = self.createPlugin()
        edPluginExecPlotGle.setDataInput(xsDataInput)
        edPluginExecPlotGle.checkParameters()
        
        
    def testReadPlotMtv(self):
        strPathTestFile = os.path.join(self.getPluginTestsDataHome(), \
                                       "best_plots.mtv")
        strXml = EDUtilsFile.readFile(strPathTestFile)
        edPluginExecPlotGle = self.createPlugin()
        xsDataplotSet = edPluginExecPlotGle.readPlotMtv(strXml)
        print xsDataplotSet.marshal()
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testReadPlotMtv)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecPlotGle = EDTestCasePluginUnitExecPlotGle("EDTestCasePluginUnitExecPlotGle")
    edTestCasePluginUnitExecPlotGle.execute()

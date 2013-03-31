#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteExecSimpleHTMLPagev2_0.py 1682 2010-06-24 11:57:23Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute



class EDTestCasePluginExecuteExecSimpleHTMLPagev2_0(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecSimpleHTMLPagev2_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputSimpleHTMLPage_v2_0.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001_pred.jpg", "ref-testscale_1_002_pred.jpg" ])


    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteExecSimpleHTMLPagev2_0 = EDTestCasePluginExecuteExecSimpleHTMLPagev2_0("EDTestCasePluginExecuteExecSimpleHTMLPagev2_0")
    edTestCasePluginExecuteExecSimpleHTMLPagev2_0.execute()

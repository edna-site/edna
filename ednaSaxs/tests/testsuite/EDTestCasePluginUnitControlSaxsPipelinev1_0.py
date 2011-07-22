# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Thomas Boeglin
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

__author__ = "Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataEdnaSaxs import *

class EDTestCasePluginUnitControlSaxsPipelinev1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlSaxsPipelinev1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputSaxsPipeline()
        edPluginExecSaxsPipeline = self.createPlugin()
        edPluginExecSaxsPipeline.setDataInput(xsDataInput)
        edPluginExecSaxsPipeline.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlSaxsPipelinev1_0 = EDTestCasePluginUnitControlSaxsPipelinev1_0("EDTestCasePluginUnitControlSaxsPipelinev1_0")
    EDTestCasePluginUnitControlSaxsPipelinev1_0.execute()

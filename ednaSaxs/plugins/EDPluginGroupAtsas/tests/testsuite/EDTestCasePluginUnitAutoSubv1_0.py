# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:        Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF"
__date__ = "20111108"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataCommon import XSDataFile
from XSDataEdnaSaxs import XSDataInputAutoSub

class EDTestCasePluginUnitAutoSubv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginAutoSubv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputAutoSub(sampleCurve=XSDataFile(), buffers=[XSDataFile()])
        edPluginAutoSubv1_0 = self.createPlugin()
        edPluginAutoSubv1_0.setDataInput(xsDataInput)
        edPluginAutoSubv1_0.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitAutoSub = EDTestCasePluginUnitAutoSubv1_0("EDTestCasePluginUnitAutoSubv1_0")
    EDTestCasePluginUnitAutoSub.execute()

#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2012      European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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
__license__ = "GPLv3+"
__copyright__ = "Copyrigth (c) 2010 ESRF"

import os

from EDAssert import EDAssert
from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from XSDataCommon import XSDataInput

class EDTestCaseEDHandlerESRFPyarchv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDHandlerESRFPyarchv1_0")


    def testCreatePyarchFilePath(self):
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/"))
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data"))
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/visitor"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/visitor/mx415/id14eh2"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212/1"))
        EDAssert.equal("/data/pyarch/id14eh2/mx415/20100212/1/2", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/visitor/mx415/id14eh2/20100212/1/2"))
        # Test with inhouse account...
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/"))
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data"))
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2"))
        EDAssert.equal(None, EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2/inhouse"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2/inhouse/opid232"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525/1"))
        EDAssert.equal("/data/pyarch/id23eh2/opid232/20100525/1/2", EDHandlerESRFPyarchv1_0.createPyarchFilePath("/data/id23eh2/inhouse/opid232/20100525/1/2"))



    def process(self):
        self.addTestMethod(self.testCreatePyarchFilePath)




if __name__ == '__main__':

    EDTestCaseEDHandlerESRFPyarchv1_0 = EDTestCaseEDHandlerESRFPyarchv1_0("EDTestCaseEDHandlerESRFPyarchv1_0")
    EDTestCaseEDHandlerESRFPyarchv1_0.execute()

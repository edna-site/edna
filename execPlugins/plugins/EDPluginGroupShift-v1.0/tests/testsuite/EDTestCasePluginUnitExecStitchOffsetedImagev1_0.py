# coding: utf8
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer
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

__author__="Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataShiftv1_0 import XSDataInputStitchOffsetedImage,OffsetedImage

class EDTestCasePluginUnitExecStitchOffsetedImagev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin StitchOffsetedImagev1_0
    """

    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecStitchOffsetedImagev1_0")
              

    def testCheckParameters(self):
        xsDataInput = XSDataInputStitchOffsetedImage()
        xsDataInput.setInputImages([OffsetedImage()])
        edPluginExecStitchOffsetedImage = self.createPlugin()
        edPluginExecStitchOffsetedImage.setDataInput(xsDataInput)
        edPluginExecStitchOffsetedImage.checkParameters()
        
    
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecStitchOffsetedImagev1_0 = EDTestCasePluginUnitExecStitchOffsetedImagev1_0("EDTestCasePluginUnitExecStitchOffsetedImagev1_0")
    edTestCasePluginUnitExecStitchOffsetedImagev1_0.execute()

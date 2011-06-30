# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF 2010
#
#    Principal author:      Jérôme Kieffer
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
__copyright__ = "ESRF"


from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsAzimutIntv1_0
from XSDataCommon import XSDataFile, XSDataInteger, XSDataDouble, XSDataString, \
    XSDataImage

class EDTestCasePluginUnitBioSaxsAzimutIntv1_1(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBioSaxsAzimutIntv1_1")


    def testCheckParameters(self):
        xsDataInput = XSDataInputBioSaxsAzimutIntv1_0()
        xsDataInput.setNormalizedImage(XSDataImage())
        xsDataInput.setNormalizedImageSize(XSDataInteger())
        xsDataInput.setIntegratedImage(XSDataImage())
        xsDataInput.setIntegratedCurve(XSDataFile())
        xsDataInput.setNormalizationFactor(XSDataDouble())
        xsDataInput.setMaskFile(XSDataImage())
        xsDataInput.setCorrectedImage(XSDataImage())
        xsDataInput.setConcentration(XSDataDouble())
        xsDataInput.setComments(XSDataString())
        xsDataInput.setCode(XSDataString())

        edPluginExec = self.createPlugin()
        edPluginExec.setDataInput(xsDataInput)
        edPluginExec.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    edTestCasePlugin = EDTestCasePluginUnitBioSaxsAzimutIntv1_1 ("EDTestCasePluginUnitBioSaxsAzimutIntv1_1")
    edTestCasePlugin.execute()

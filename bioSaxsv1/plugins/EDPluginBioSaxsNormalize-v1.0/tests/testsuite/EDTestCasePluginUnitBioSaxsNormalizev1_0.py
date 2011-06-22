#
#coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
__copyright__ = "ESRF"

import os, sys
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsNormalizev1_0
from XSDataCommon           import XSDataInteger, XSDataDouble, XSDataImage, XSDataFile, XSDataString
from EDFactoryPluginStatic               import EDFactoryPluginStatic


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")


class EDTestCasePluginUnitBioSaxsNormalizev1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBioSaxsNormalizev1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputBioSaxsNormalizev1_0()
        xsDataInput.setRawImage(XSDataFile())
        xsDataInput.setLogFile(XSDataFile())
        xsDataInput.setNormalizedImage(XSDataFile())
        xsDataInput.setRawImageSize(XSDataDouble())
        xsDataInput.setBeamStopDiode(XSDataDouble())
        xsDataInput.setNormalizationFactor(XSDataDouble())
        xsDataInput.setMachineCurrent(XSDataDouble())
        xsDataInput.setMaskFile(XSDataFile())
        xsDataInput.setDetectorDistance(XSDataDouble())
        xsDataInput.setWavelength(XSDataDouble())
        xsDataInput.setPixelSize_1(XSDataDouble())
        xsDataInput.setPixelSize_2(XSDataDouble())
        xsDataInput.setBeamCenter_1(XSDataDouble())
        xsDataInput.setBeamCenter_2(XSDataDouble())

        edPluginExecBioSaxsNormalize = self.createPlugin()
        edPluginExecBioSaxsNormalize.setDataInput(xsDataInput)
        edPluginExecBioSaxsNormalize.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitBioSaxsNormalizev1_0 = EDTestCasePluginUnitBioSaxsNormalizev1_0("EDTestCasePluginUnitBioSaxsNormalizev1_0")
    EDTestCasePluginUnitBioSaxsNormalizev1_0.execute()

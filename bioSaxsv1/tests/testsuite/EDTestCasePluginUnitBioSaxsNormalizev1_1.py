# coding: utf8
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
__date__ = "2011-02-25"

import os, sys
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsNormalizev1_0, XSDataBioSaxsSample, XSDataBioSaxsExperimentSetup
from XSDataCommon           import XSDataInteger, XSDataDouble, XSDataImage, XSDataFile, XSDataString, \
    XSDataLength, XSDataWavelength
from EDFactoryPluginStatic import EDFactoryPluginStatic
# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")


class EDTestCasePluginUnitBioSaxsNormalizev1_1(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBioSaxsNormalizev1_1")


    def testCheckParameters(self):
        xsDataInput = XSDataInputBioSaxsNormalizev1_0()
        xsDataInput.setRawImage(XSDataImage())
#        xsDataInput.setLogFile(XSDataFile())
        xsDataInput.setNormalizedImage(XSDataImage())
        xsDataInput.setRawImageSize(XSDataInteger())
        xsDataInput.setExperimentSetup(XSDataBioSaxsExperimentSetup())
        xsDataInput.setSample(XSDataBioSaxsSample())
#        xsDataInput.setBeamStopDiode(XSDataDouble())
#        xsDataInput.setNormalizationFactor(XSDataDouble())
#        xsDataInput.setMachineCurrent(XSDataDouble())
#        xsDataInput.setMaskFile(XSDataImage())
#        xsDataInput.setDetectorDistance(XSDataLength())
#        xsDataInput.setWavelength(XSDataWavelength())
#        xsDataInput.setPixelSize_1(XSDataLength())
#        xsDataInput.setPixelSize_2(XSDataLength())
#        xsDataInput.setBeamCenter_1(XSDataDouble())
#        xsDataInput.setBeamCenter_2(XSDataDouble())

        edPluginExecBioSaxsNormalize = self.createPlugin()
        edPluginExecBioSaxsNormalize.setDataInput(xsDataInput)
        edPluginExecBioSaxsNormalize.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitBioSaxsNormalizev1_1 = EDTestCasePluginUnitBioSaxsNormalizev1_1("EDTestCasePluginUnitBioSaxsNormalizev1_1")
    EDTestCasePluginUnitBioSaxsNormalizev1_1.execute()

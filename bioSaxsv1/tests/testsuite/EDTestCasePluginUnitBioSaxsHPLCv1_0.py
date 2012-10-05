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
from XSDataBioSaxsv1_0     import XSDataInputBioSaxsHPLCv1_0, XSDataBioSaxsSample, XSDataBioSaxsExperimentSetup
from XSDataCommon           import XSDataInteger, XSDataDouble, XSDataImage, XSDataFile, XSDataString, XSDataLength, \
    XSDataWavelength
from EDFactoryPluginStatic               import EDFactoryPluginStatic


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")


class EDTestCasePluginUnitBioSaxsHPLCv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBioSaxsHPLCv1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputBioSaxsHPLCv1_0()
        xsDataInput.rawImage = XSDataImage()
        xsDataInput.sample = XSDataBioSaxsSample()
        xsDataInput.experimentSetup = XSDataBioSaxsExperimentSetup()
        xsDataInput.logFile = XSDataFile()
        xsDataInput.normalizedImage = XSDataImage()
        xsDataInput.rawImageSize = XSDataInteger()
        edPluginExecBioSaxsNormalize = self.createPlugin()
        edPluginExecBioSaxsNormalize.setDataInput(xsDataInput)
        edPluginExecBioSaxsNormalize.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    eDTestCase = EDTestCasePluginUnitBioSaxsHPLCv1_0("EDTestCasePluginUnitBioSaxsHPLCv1_0")
    eDTestCase.execute()

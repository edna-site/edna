#
# coding: utf8
#
#    Project: Image Filter
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF
#
#    Principal author:       Jérôme Kieffer
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

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataImageFilter                   import XSDataResultMedianFilterImage
from EDFactoryPluginStatic               import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")

class EDTestCasePluginExecuteControlMedianFilterImagev1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlMedianFilterImagev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MedianFilterImage.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMedianFilterImage_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMedianFilterImage_empty.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "noise2.edf", "noise3.edf", "noise4.edf", "noise5.edf", "noise6.edf"])


    def testExecute(self):
        """
        """
        self.run()
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultMedianFilterImage.parseString(strExpectedOutput)
        xsDataResultObtained = XSDataResultMedianFilterImage.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "Check if XSDataResult are exactly the same")



    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlMedianFilterImagev1_0 = EDTestCasePluginExecuteControlMedianFilterImagev1_0("EDTestCasePluginExecuteControlMedianFilterImagev1_0")
    edTestCasePluginExecuteControlMedianFilterImagev1_0.execute()

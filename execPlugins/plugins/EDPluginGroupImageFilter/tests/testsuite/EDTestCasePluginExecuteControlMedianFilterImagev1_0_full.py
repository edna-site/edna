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
from XSDataCommon                        import XSDataString
from EDAssert                            import EDAssert
from EDTestCasePluginExecuteControlMedianFilterImagev1_0             import EDTestCasePluginExecuteControlMedianFilterImagev1_0
from XSDataImageFilter                   import XSDataResultMedianFilterImage
from EDFactoryPluginStatic               import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")
EDFactoryPluginStatic.loadModule("XSDataAccumulatorv1_0")
from XSDataAccumulatorv1_0               import XSDataQuery, XSDataInputAccumulator

class EDTestCasePluginExecuteControlMedianFilterImagev1_0_full(EDTestCasePluginExecuteControlMedianFilterImagev1_0):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecuteControlMedianFilterImagev1_0.__init__(self, "EDPluginControlMedianFilterImagev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_MedianFilterImage.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMedianFilterImage_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMedianFilterImage_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        """
        EDTestCasePluginExecuteControlMedianFilterImagev1_0.preProcess(self)
        self.loadTestImage([ "noise2.edf", "noise3.edf", "noise4.edf", "noise5.edf", "noise6.edf"])
        acc = EDFactoryPluginStatic.loadPlugin("EDPluginAccumulatorv1_0")
        xsdIn = XSDataInputAccumulator()
        xsdIn.setItem([XSDataString(os.path.join(self.getTestsDataImagesHome(), "noise%i.edf" % i)) for i in [2, 3, 5, 6]])
        acc.setDataInput(xsdIn)
        acc.executeSynchronous()


if __name__ == '__main__':

    edTestCasePluginExecuteControlMedianFilterImagev1_0 = EDTestCasePluginExecuteControlMedianFilterImagev1_0_full("EDTestCasePluginExecuteControlMedianFilterImagev1_0_full")
    edTestCasePluginExecuteControlMedianFilterImagev1_0.execute()

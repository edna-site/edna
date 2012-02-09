#    coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseParallelExecute.py 2128 2010-10-04 16:39:42Z kieffer $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (kieffer@esrf.fr)
# 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = ["Jérôme Kieffer"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDUtilsArray                        import EDUtilsArray
from XSDataCommon                        import XSDataArray
from EDUtilsLibraryInstaller             import EDUtilsLibraryInstaller
from EDFactoryPluginStatic               import EDFactoryPluginStatic
from EDUtilsPlatform                     import EDUtilsPlatform

#EDVerbose.screen("Check Install Numpy")
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", EDUtilsPlatform.architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="__version__")
if numpy is None:
    EDVerbose.WARNING("Numpy is not directly available, I will run all tests without it")

#EDVerbose.screen("Check Install PIL")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
#ImagePath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", EDUtilsPlatform.architecture)
#Image = EDFactoryPluginStatic.preImport("Image", ImagePath, _strMethodVersion="VERSION")
#if Image is None:
#    EDVerbose.WARNING("Image is not directly available, I will run all tests without it")


#EDVerbose.screen("Check Install Fabio")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
#fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", EDUtilsPlatform.architecture)
#fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath, _strMethodVersion="version")
#if fabio is None:
#    EDVerbose.WARNING("FabIO is not directly available, I will run all tests without it")

#EDVerbose.screen("Check Install H5Py")
EDFactoryPluginStatic.loadModule("EDInstallH5Pyv1_3_0")
#h5pyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "H5Py-1.3.0", EDUtilsPlatform.architecture)
#h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.version")
#if h5py is None:
#    EDVerbose.WARNING("H5Py is not directly available, I will run all tests without it")



class EDTestCaseEDUtilsArray(EDTestCase):
    """
    Unit & execution test for the EDUtilsArray static class
    """

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDUtilsArray")
        self.strXSDataArrayNumpy = """<?xml version="1.0" ?>
<XSDataArray>
        <shape>10</shape>
        <shape>10</shape>
        <size>100</size>
        <dtype>uint8</dtype>
        <data>AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiYw==</data>
        <coding><value>base64</value></coding>
        <md5sum><value>7acedd1a84a4cfcb6e7a16003242945e</value></md5sum>
</XSDataArray>"""
        self.xsDataArrayNumpy = XSDataArray.parseString(self.strXSDataArrayNumpy)
        self.strXSDataArrayNoNumpy = """<?xml version="1.0" ?>
<XSDataArray>
        <shape>10</shape>
        <shape>10</shape>
        <size>100</size>
        <dtype>int64</dtype>
        <data>AAAAAAAAAAABAAAAAAAAAAIAAAAAAAAAAwAAAAAAAAAEAAAAAAAAAAUAAAAAAAAABgAAAAAAAAAHAAAAAAAAAAgAAAAAAAAACQAAAAAAAAAKAAAAAAAAAAsAAAAAAAAADAAAAAAAAAANAAAAAAAAAA4AAAAAAAAADwAAAAAAAAAQAAAAAAAAABEAAAAAAAAAEgAAAAAAAAATAAAAAAAAABQAAAAAAAAAFQAAAAAAAAAWAAAAAAAAABcAAAAAAAAAGAAAAAAAAAAZAAAAAAAAABoAAAAAAAAAGwAAAAAAAAAcAAAAAAAAAB0AAAAAAAAAHgAAAAAAAAAfAAAAAAAAACAAAAAAAAAAIQAAAAAAAAAiAAAAAAAAACMAAAAAAAAAJAAAAAAAAAAlAAAAAAAAACYAAAAAAAAAJwAAAAAAAAAoAAAAAAAAACkAAAAAAAAAKgAAAAAAAAArAAAAAAAAACwAAAAAAAAALQAAAAAAAAAuAAAAAAAAAC8AAAAAAAAAMAAAAAAAAAAxAAAAAAAAADIAAAAAAAAAMwAAAAAAAAA0AAAAAAAAADUAAAAAAAAANgAAAAAAAAA3AAAAAAAAADgAAAAAAAAAOQAAAAAAAAA6AAAAAAAAADsAAAAAAAAAPAAAAAAAAAA9AAAAAAAAAD4AAAAAAAAAPwAAAAAAAABAAAAAAAAAAEEAAAAAAAAAQgAAAAAAAABDAAAAAAAAAEQAAAAAAAAARQAAAAAAAABGAAAAAAAAAEcAAAAAAAAASAAAAAAAAABJAAAAAAAAAEoAAAAAAAAASwAAAAAAAABMAAAAAAAAAE0AAAAAAAAATgAAAAAAAABPAAAAAAAAAFAAAAAAAAAAUQAAAAAAAABSAAAAAAAAAFMAAAAAAAAAVAAAAAAAAABVAAAAAAAAAFYAAAAAAAAAVwAAAAAAAABYAAAAAAAAAFkAAAAAAAAAWgAAAAAAAABbAAAAAAAAAFwAAAAAAAAAXQAAAAAAAABeAAAAAAAAAF8AAAAAAAAAYAAAAAAAAABhAAAAAAAAAGIAAAAAAAAAYwAAAAAAAAA=</data>
        <coding><value>base64</value></coding>
        <md5sum><value>13e5d157161f66d98fe0b75ce51c982b</value></md5sum>
</XSDataArray>"""

        self.arrayNoNumpy = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
 [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
 [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
 [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
 [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
 [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]
        if numpy is not None:
            self.arrayNumpy = numpy.arange(100, dtype="uint8").reshape((10, 10))
        else:
            self.arrayNumpy = self.arrayNoNumpy

    def unitTestXsdToArray(self):
        """
        test the execution of xsDataToArray static method
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsArray.unitTestXsdToArray")
        if numpy is not None:
            EDAssert.arraySimilar(self.arrayNumpy,
                                  EDUtilsArray.xsDataToArray(self.xsDataArrayNumpy, _bForceNoNumpy=False),
                                  _strComment="Array are the same (Numpy used)")
        else:
            EDAssert.equal(self.arrayNoNumpy,
                           EDUtilsArray.xsDataToArray(self.xsDataArrayNumpy, _bCheckMd5sum=True, _bForceNoNumpy=False),
                           "Array are the same (no Numpy available)")

    def unitTestXsdToArrayNoNumpy(self):
        """
        test the execution of detectNumberOfCPUs
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsArray.unitTestXsdToArrayNoNumpy")
        EDAssert.equal(self.arrayNoNumpy,
                       EDUtilsArray.xsDataToArray(self.xsDataArrayNumpy, _bForceNoNumpy=True),
                       "Array are the same (forced No Numpy)")


    def unitTestArraytoXsd(self):
        """
        test the execution of xsDataToArray static method
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsArray.unitTestArraytoXsd")
        if numpy is not None:
            EDAssert.strAlmostEqual(XSDataArray.parseString(self.strXSDataArrayNumpy).marshal(),
                                    EDUtilsArray.arrayToXSData(self.arrayNumpy).marshal(),
                                    _strComment="XSDataArray from (numpyArray) are the same")
        else:
            EDAssert.strAlmostEqual(XSDataArray.parseString(self.strXSDataArrayNoNumpy).marshal(),
                                    EDUtilsArray.arrayToXSData(self.arrayNumpy).marshal(),
                                    _strComment="XSDataArray from (Non numpy Array) are the same")


    def unitTestArraytoXsdNoNumpy(self):
        """
        test the execution of detectNumberOfCPUs
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsArray.unitTestArraytoXsdNoNumpy")
        EDAssert.strAlmostEqual(XSDataArray.parseString(self.strXSDataArrayNoNumpy).marshal(),
                                EDUtilsArray.arrayToXSData(self.arrayNumpy, _bForceNoNumpy=True).marshal(),
                                _strComment="XSDataArray from (numpyArray) are the same (forced No Numpy)")
        EDAssert.strAlmostEqual(XSDataArray.parseString(self.strXSDataArrayNoNumpy).marshal(),
                                EDUtilsArray.arrayToXSData(self.arrayNoNumpy, _bForceNoNumpy=True).marshal(),
                                _strComment="XSDataArray from (list of lists) are the same (forced No Numpy)")


    def process(self):
        self.addTestMethod(self.unitTestXsdToArray)
        self.addTestMethod(self.unitTestXsdToArrayNoNumpy)
        self.addTestMethod(self.unitTestArraytoXsd)
        self.addTestMethod(self.unitTestArraytoXsdNoNumpy)



if __name__ == '__main__':

    edTestCaseEDUtils = EDTestCaseEDUtilsArray("EDTestCaseEDUtilsArray")
    edTestCaseEDUtils.execute()

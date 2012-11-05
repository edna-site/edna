# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
__copyright__ = "ESRF"

import os, sys

from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from EDTestCasePluginExecute            import EDTestCasePluginExecute
from XSDataBioSaxsv1_0                  import XSDataResultBioSaxsHPLCv1_0
from EDFactoryPluginStatic              import EDFactoryPluginStatic
from EDUtilsParallel                    import EDUtilsParallel
# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

import numpy
from fabio.openimage import openimage


class EDTestCasePluginExecuteBioSaxsHPLCv1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsHPLCv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_BioSaxsHPLC.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsHPLC_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsHPLC_reference_v1_0.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["bioSaxsRaw.edf", "bioSaxsMask.edf",
                            "bioSaxsCorrected.edf", "bioSaxsProcessNormalized.edf",
                            "bioSaxsProcessIntegrated.edf", "bioSaxsProcessIntegrated1_2.dat"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsHPLCv1_0.parseString(strExpectedOutput)
        self.refNormImg = xsDataResultReference.normalizedImage.path.value
        self.refIntCrv = xsDataResultReference.integratedCurve.path.value
        if not os.path.isdir(os.path.dirname(self.refNormImg)):
            os.makedirs(os.path.dirname(self.refNormImg))
        if os.path.isfile(self.refNormImg):
            os.remove(self.refNormImg)
        if os.path.isfile(self.refIntCrv):
            os.remove(self.refIntCrv)
        EDUtilsParallel.initializeNbThread()

    def testExecute(self):
        """
        """
        plugin = self.getPlugin()
        plugin.__class__.dictHPLC = {}
        self.run()

################################################################################
# Compare XSDataResults
################################################################################

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultBioSaxsHPLCv1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")


################################################################################
# Compare Ascii files
################################################################################
        asciiObt = os.linesep.join([i.strip() for i in  open(xsDataResultObtained.integratedCurve.path.value) if "Raster" not in i])
        asciiRef = os.linesep.join([i.strip() for i in  open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsProcessIntegrated1_2.dat")) if "Raster" not in i])

        EDAssert.strAlmostEqual(asciiRef, asciiObt, _strComment="3 column ascii files are the same", _fRelError=0.1, _strExcluded=os.environ["USER"])
        EDVerbose.screen("Execution time for %s: %.3fs" % (plugin.getClassName(), plugin.getRunTime()))
    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCase = EDTestCasePluginExecuteBioSaxsHPLCv1_0("EDTestCasePluginExecuteBioSaxsHPLCv1_0")
    edTestCase.execute()

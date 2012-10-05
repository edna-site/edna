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
from XSDataBioSaxsv1_0                  import XSDataResultBioSaxsProcessOneFilev1_0
from EDFactoryPluginStatic import EDFactoryPluginStatic
# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

import numpy
from fabio.openimage import openimage


class EDTestCasePluginExecuteBioSaxsProcessOneFilev1_1(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsProcessOneFilev1_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_BioSaxsProcessOneFile.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsProcessOneFile_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsProcessOneFile_reference_v1_1.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["bioSaxsRaw.edf", "bioSaxsMask.edf",
                            "bioSaxsCorrected.edf", "bioSaxsProcessNormalized.edf",
                            "bioSaxsProcessIntegrated.edf", "bioSaxsProcessIntegrated1_1.dat"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsProcessOneFilev1_0.parseString(strExpectedOutput)
        self.refNormImg = xsDataResultReference.normalizedImage.path.value
        self.refIntImg = xsDataResultReference.integratedImage.path.value
        self.refIntCrv = xsDataResultReference.integratedCurve.path.value
        if not os.path.isdir(os.path.dirname(self.refNormImg)):
            os.makedirs(os.path.dirname(self.refNormImg))
        if os.path.isfile(self.refNormImg):
            os.remove(self.refNormImg)
        if os.path.isfile(self.refIntImg):
            os.remove(self.refIntImg)
        if os.path.isfile(self.refIntCrv):
            os.remove(self.refIntCrv)



    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

################################################################################
# Compare XSDataResults
################################################################################

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultBioSaxsProcessOneFilev1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")


################################################################################
# Compare dictionary
################################################################################
        obtFile = xsDataResultObtained.integratedImage.path.value
        refFile = os.path.join(self.getTestsDataImagesHome(), "bioSaxsProcessIntegrated.edf")
        EDVerbose.DEBUG("fileRef=%s fileObt=%s" % (refFile, obtFile))
        edfRef = openimage(refFile)
        edfObt = openimage(obtFile)
        headerRef = edfRef.header
        headerObt = edfObt.header

        keysRef = headerRef.keys()
        keysObt = headerObt.keys()
        keysRef.sort()
        keysObt.sort()
#        EDAssert.equal(keysRef, keysObt, _strComment="Same keys in the header dict")
        for key in keysRef:
            if not (key.startswith("History") or key in [ "Compression", "DDummy", "Dummy", "EDF_HeaderSize", "HeaderID", "Image", "filename", "RasterOrientation"]):
                EDAssert.strAlmostEqual(headerRef[key], headerObt[key], _strComment="header value %s are the same" % key, _strExcluded="bioSaxs")

################################################################################
# Compare images 
################################################################################

        outputData = edfRef.data
        referenceData = edfObt.data
        EDAssert.arraySimilar(numpy.maximum(outputData, 0), numpy.maximum(referenceData, 0) , _fScaledMaxDelta=0.05, _strComment="Images-data are the same")

        outputData = edfRef.next().data
        referenceData = edfObt.next().data
        EDAssert.arraySimilar(numpy.maximum(outputData, 0), numpy.maximum(referenceData, 0) , _fScaledMaxDelta=0.05, _strComment="Images-ESD are the same")

################################################################################
# Compare Ascii files
################################################################################
        asciiObt = os.linesep.join([i.strip() for i in  open(xsDataResultObtained.integratedCurve.path.value) if "Raster" not in i])
        asciiRef = os.linesep.join([i.strip() for i in  open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsProcessIntegrated1_1.dat")) if "Raster" not in i])

        EDAssert.strAlmostEqual(asciiRef, asciiObt, _strComment="3 column ascii files are the same", _fRelError=0.1, _strExcluded=os.environ["USER"])
        EDVerbose.screen("Execution time for %s: %.3fs" % (plugin.getClassName(), plugin.getRunTime()))
    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCase = EDTestCasePluginExecuteBioSaxsProcessOneFilev1_1("EDTestCasePluginExecuteBioSaxsProcessOneFilev1_1")
    edTestCase.execute()

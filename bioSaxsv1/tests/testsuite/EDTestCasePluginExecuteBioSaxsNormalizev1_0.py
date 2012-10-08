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
from XSDataBioSaxsv1_0                  import XSDataResultBioSaxsNormalizev1_0
from EDFactoryPluginStatic               import EDFactoryPluginStatic


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")

import EdfFile


class EDTestCasePluginExecuteBioSaxsNormalizev1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsNormalizev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_BioSaxsNormalize.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsNormalize_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsNormalize_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["bioSaxsRaw.edf", "bioSaxsMask.edf", "bioSaxsNormalized.edf", "bioSaxsNormalized.log"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsNormalizev1_0.parseString(strExpectedOutput)
        self.refOutput = xsDataResultReference.normalizedImage.getPath().value
        EDVerbose.DEBUG("Output file is %s" % self.refOutput)
        if not os.path.isdir(os.path.dirname(self.refOutput)):
            os.makedirs(os.path.dirname(self.refOutput))
        if os.path.isfile(self.refOutput):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % self.refOutput)
            os.remove(self.refOutput)



    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

################################################################################
# Compare XSDataResults
################################################################################

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultBioSaxsNormalizev1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")

################################################################################
# Compare Log Files
################################################################################

        outputData = ""
        for oneLine in open(xsDataResultObtained.getLogFile().getPath().value, "rb").readlines():
            oneline = oneLine.lower()
            if oneline.startswith("first"):outputData += oneLine
            if oneline.startswith("last"):outputData += oneLine
            if oneline.startswith("increment"):outputData += oneLine
            if oneline.startswith("factor"):outputData += oneLine
            if oneline.startswith("constant"):outputData += oneLine

        referenceData = ""
        for oneLine in open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsNormalized.log"), "rb").readlines():
            oneline = oneLine.lower()
            if oneline.startswith("first"):referenceData += oneLine
            elif oneline.startswith("last"):referenceData += oneLine
            elif oneline.startswith("increment"):referenceData += oneLine
            elif oneline.startswith("factor"):referenceData += oneLine
            elif oneline.startswith("constant"):referenceData += oneLine

        EDAssert.strAlmostEqual(referenceData, outputData, _strComment="LogFiles are the same", _fAbsError=0.1)


################################################################################
# Compare dictionary
################################################################################
        edfRef = EdfFile.EdfFile(xsDataResultObtained.normalizedImage.getPath().value)
        edfObt = EdfFile.EdfFile(os.path.join(self.getTestsDataImagesHome(), "bioSaxsNormalized.edf"))

        ########################################################################
        # Deprected plugin => deprected test
        ########################################################################
#        headerRef = edfRef.GetHeader(0)
#        headerObt = edfObt.GetHeader(0)
#        keysRef = headerRef.keys()
#        keysObt = headerObt.keys()
#        keysRef.sort()
#        keysObt.sort()
#        for key in ["HeaderID", "Image", 'EDF_BinarySize', "EDF_DataBlockID", "EDF_HeaderSize", "filename", "RasterOrientation", "time_of_day" ]:
#            if key in keysObt: keysObt.remove(key)
#            if key in keysRef: keysRef.remove(key)
#        EDAssert.equal(keysRef, keysObt, _strComment="Same keys in the header dict")
#        for key in keysRef:
#            if not key.startswith("History"):
#                EDAssert.strAlmostEqual(headerRef[key], headerObt[key], _strComment="header value %s are the same" % key, _strExcluded="bioSaxs")


################################################################################
# Compare images 
################################################################################

        outputData = edfRef.GetData(0)
        referenceData = edfObt.GetData(0)
        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.1, _fScaledMaxDelta=0.05, _strComment="Images-data are the same")

        outputData = edfRef.GetData(1)
        referenceData = edfObt.GetData(1)
        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.1, _fScaledMaxDelta=0.05, _strComment="Images-ESD are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsNormalizev1_0 = EDTestCasePluginExecuteBioSaxsNormalizev1_0("EDTestCasePluginExecuteBioSaxsNormalizev1_0")
    edTestCasePluginExecuteBioSaxsNormalizev1_0.execute()

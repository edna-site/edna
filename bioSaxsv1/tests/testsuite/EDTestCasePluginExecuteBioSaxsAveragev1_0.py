#
#coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, 2010
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
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsAveragev1_0

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDFactoryPluginStatic               import EDFactoryPluginStatic


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")

import EdfFile


class EDTestCasePluginExecuteBioSaxsAveragev1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsAveragev1_0")
        self.setConfigurationFile(self.getConfigurationFile())
        #os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsAveragev1_0_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsAveragev1_0_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        #EDVerbose.DEBUG(str([ "bioSaxsIntegrated%02i.edf" % i for i in range(1, 11) ] + ["bioSaxsAveraged.dat", "bioSaxsAveraged.edf"]))
        self.loadTestImage([ "bioSaxsIntegrated%02i.edf" % i for i in range(1, 11) ] + ["bioSaxsAveraged.dat", "bioSaxsAveraged.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsAveragev1_0.parseString(strExpectedOutput)
        self.averagedCurve = xsDataResultReference.getAveragedCurve().getPath().value
        EDVerbose.DEBUG("Output file is %s" % self.averagedCurve)
        if not os.path.isdir(os.path.dirname(self.averagedCurve)):
            os.makedirs(os.path.dirname(self.averagedCurve))
        if os.path.isfile(self.averagedCurve):
            EDVerbose.DEBUG(" Output Averaged Curve file exists %s, I will remove it" % self.averagedCurve)
            os.remove(self.averagedCurve)

        self.AveragedImage = xsDataResultReference.getAveragedImage().getPath().value
        EDVerbose.DEBUG("Output Integrated Image file is %s" % self.AveragedImage)
        if not os.path.isdir(os.path.dirname(self.AveragedImage)):
            os.makedirs(os.path.dirname(self.AveragedImage))
        if os.path.isfile(self.AveragedImage):
            EDVerbose.DEBUG(" Output Integrated Image file exists %s, I will remove it" % self.AveragedImage)
            os.remove(self.AveragedImage)

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
        xsDataResultReference = XSDataResultBioSaxsAveragev1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")


################################################################################
# Compare spectrum ascii Files
################################################################################

        outputData = open(xsDataResultObtained.getAveragedCurve().getPath().value, "rb").read()
        referenceData = open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsAveraged.dat"), "rb").read()

        EDAssert.strAlmostEqual(referenceData, outputData, _strComment="3-column ascii spectra files spectra are the same", _fRelError=0.1, _fAbsError=0.1, _strExcluded="bioSaxs")

################################################################################
# Compare images 
################################################################################
        edfObt = EdfFile.EdfFile(xsDataResultObtained.getAveragedImage().getPath().value)
        edfRef = EdfFile.EdfFile(os.path.join(self.getTestsDataImagesHome(), "bioSaxsAveraged.edf"))
        outputData = edfObt.GetData(0)
        referenceData = edfRef.GetData(0)
        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.1, _fScaledMaxDelta=0.05, _strComment="Averaged images are the same")

        headerRef = edfRef.GetHeader(0)
        headerObt = edfObt.GetHeader(0)
        keysRef = headerRef.keys()
        keysObt = headerObt.keys()
        keysRef.sort()
        keysObt.sort()
        for key in ["HeaderID", "Image", 'EDF_BinarySize', "EDF_DataBlockID", "EDF_HeaderSize", "filename", "RasterOrientation", "History-1", "History-1~1" ]:
            if key in keysObt: keysObt.remove(key)
            if key in keysRef: keysRef.remove(key)
        EDAssert.equal(keysRef, keysObt, _strComment="Same keys in the header dictionary for Corrected Images")
        for key in keysRef:
            EDAssert.strAlmostEqual(headerRef[key], headerObt[key], _strComment="header value in Averaged %s are the same" % key, _strExcluded="bioSaxs")






    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsAveragev1_0 = EDTestCasePluginExecuteBioSaxsAveragev1_0("EDTestCasePluginExecuteBioSaxsAveragev1_0")
    edTestCasePluginExecuteBioSaxsAveragev1_0.execute()

# coding: utf8
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDFactoryPluginStatic               import EDFactoryPluginStatic
from EDUtilsParallel                     import EDUtilsParallel
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsAzimutIntv1_0


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")


import fabio


class EDTestCasePluginExecuteBioSaxsAzimutIntv1_3(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsAzimutIntv1_3")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsAzimutIntv1_1_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsAzimutIntv1_3_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "bioSaxsMask.edf", "bioSaxsNormalized.edf", "bioSaxsIntegratedv1_3.dat", "bioSaxsCorrected.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsAzimutIntv1_0.parseString(strExpectedOutput)
        self.integratedCurve = xsDataResultReference.getIntegratedCurve().getPath().value
        EDVerbose.DEBUG("Output file is %s" % self.integratedCurve)
        if not os.path.isdir(os.path.dirname(self.integratedCurve)):
            os.makedirs(os.path.dirname(self.integratedCurve))
        if os.path.isfile(self.integratedCurve):
            EDVerbose.DEBUG(" Output Integrated Curve file exists %s, I will remove it" % self.integratedCurve)
            os.remove(self.integratedCurve)

        EDUtilsParallel.initializeNbThread()
#        self.correctedImage = xsDataResultReference.getCorrectedImage().getPath().value
#        EDVerbose.DEBUG("Output Corrected Image file is %s" % self.correctedImage)
#        if not os.path.isdir(os.path.dirname(self.correctedImage)):
#            os.makedirs(os.path.dirname(self.correctedImage))
#        if os.path.isfile(self.correctedImage):
#            EDVerbose.DEBUG(" Output Corrected Image file exists %s, I will remove it" % self.correctedImage)
#            os.remove(self.correctedImage)

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
        xsDataResultReference = XSDataResultBioSaxsAzimutIntv1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")

################################################################################
# Compare spectrum ascii Files
################################################################################

        outputData = open(xsDataResultObtained.getIntegratedCurve().getPath().value, "rb").read()
        referenceData = open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsIntegratedv1_3.dat"), "rb").read()

        EDAssert.strAlmostEqual(referenceData, outputData, _strComment="3column ascii spectra files are the same", _fRelError=0.1, _fAbsError=0.1, _strExcluded="bioSaxs")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsAzimutIntv1_0 = EDTestCasePluginExecuteBioSaxsAzimutIntv1_3("EDTestCasePluginExecuteBioSaxsAzimutIntv1_3")
    edTestCasePluginExecuteBioSaxsAzimutIntv1_0.execute()

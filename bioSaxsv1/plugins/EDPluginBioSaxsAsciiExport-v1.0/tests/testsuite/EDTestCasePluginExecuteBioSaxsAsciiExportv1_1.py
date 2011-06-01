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
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsAsciiExportv1_0

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



class EDTestCasePluginExecuteBioSaxsAsciiExportv1_1(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsAsciiExportv1_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsAsciiExportv1_0_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsAsciiExportv1_0_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([  "bioSaxsAsciiExportv1_1.dat", "bioSaxsIntegrated.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsAsciiExportv1_0.parseString(strExpectedOutput)
        self.integratedSpectrum = xsDataResultReference.getIntegratedSpectrum().getPath().getValue()
        EDVerbose.DEBUG("Output file is %s" % self.integratedSpectrum)
        if not os.path.isdir(os.path.dirname(self.integratedSpectrum)):
            os.makedirs(os.path.dirname(self.integratedSpectrum))
        if os.path.isfile(self.integratedSpectrum):
            EDVerbose.DEBUG(" Output Integrated Spectrum file exists %s, I will remove it" % self.integratedSpectrum)
            os.remove(self.integratedSpectrum)


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
        xsDataResultReference = XSDataResultBioSaxsAsciiExportv1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")

################################################################################
# Compare spectrum ascii Files
################################################################################

        outputData = open(xsDataResultObtained.getIntegratedSpectrum().getPath().getValue(), "rb").read()
        referenceData = open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsAsciiExportv1_1.dat"), "rb").read()

        EDAssert.strAlmostEqual(referenceData, outputData, _strComment="3-column ascii spectra files are the same", _fRelError=0.1, _fAbsError=0.1, _strExcluded="bioSaxs")




    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsAsciiExportv1_0 = EDTestCasePluginExecuteBioSaxsAsciiExportv1_1("EDTestCasePluginExecuteBioSaxsAsciiExportv1_1")
    edTestCasePluginExecuteBioSaxsAsciiExportv1_0.execute()

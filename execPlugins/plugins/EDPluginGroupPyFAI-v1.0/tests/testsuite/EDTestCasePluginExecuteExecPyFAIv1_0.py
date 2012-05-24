# coding: utf8
#
#    Project: Python Fast Azimuthal Integration
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#
#    Principal author:       Jerome Kieffer <jerome.kieffer@esrf.fr>
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

__author__ = "Jerome Kieffer <jerome.kieffer@esrf.fr>"
__license__ = "GPLv3+"
__copyright__ = "2012 European Synchrotron Radiation Facility"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataPyFAIv1_0                     import XSDataResultPyFAI


class EDTestCasePluginExecuteExecPyFAIv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin PyFAIv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecPyFAIv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_PyFAIv1_0.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputPyFAIv1_0_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultPyFAIv1_0_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "AgBe_SAXS.%s" % i for i in ("cbf", "dat")])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultPyFAI.parseString(strExpectedOutput)
        self.refOutput = xsDataResultReference.output.path.value
        EDVerbose.DEBUG(" Output file is %s" % self.refOutput)
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

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultPyFAI.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


#        outputData = openimage(xsDataResultObtained.output.path.value).data
#        referenceData = openimage(os.path.join(self.getTestsDataImagesHome(), "Moke-2th10-tilt0-rot0.azim")).data
#        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.4, _fScaledMaxDelta=0.5, _strComment="Images are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testPyFAIv1_0instance = EDTestCasePluginExecuteExecPyFAIv1_0("EDPluginExecPyFAIv1_0")
    testPyFAIv1_0instance.execute()

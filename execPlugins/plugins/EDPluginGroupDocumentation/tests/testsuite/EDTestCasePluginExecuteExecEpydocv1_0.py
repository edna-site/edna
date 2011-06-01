# coding: utf8
#
#    Project: PROJECT
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
from XSDataDocumentation                 import XSDataInputEpydoc, XSDataResultEpydoc


class EDTestCasePluginExecuteExecEpydocv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Epydocv1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecEpydocv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Epydoc.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputEpydoc_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultEpydoc_reference.xml"))
        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        self.XSDataInput = XSDataInputEpydoc
        self.XSDataResult = XSDataResultEpydoc

    def preProcess(self):
        """
        Cleans up the destination files if they exists.
        """
        EDTestCasePluginExecute.preProcess(self)
        xsDataInput = self.XSDataInput.parseString(self.readAndParseFile(self.getDataInputFile()))
        xsDataResultReference = self.XSDataResult.parseString(self.readAndParseFile (self.getReferenceDataOutputFile()))
        outputFileName = xsDataResultReference.getDocPath().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
#        plugin.synchronize()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = self.XSDataResult.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XML are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testEpydocv1_0instance = EDTestCasePluginExecuteControlEpydocv1_0("EDTestCasePluginExecuteExecEpydocv1_0")
    testEpydocv1_0instance.execute()

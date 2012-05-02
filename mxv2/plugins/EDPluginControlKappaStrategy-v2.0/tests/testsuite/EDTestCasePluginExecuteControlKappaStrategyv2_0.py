#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute



class EDTestCasePluginExecuteControlKappaStrategyv2_0(EDTestCasePluginExecute):

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlKappaStrategyv2_0")

        self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputStrategy_reference_02.xml") , "mxv1InputStrategy")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "mxv2_XSDataCollection_reference.xml") , "mxv2DataCollection")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "mxv1_XSDataIndexingResult_reference.xml") , "mxv1IndexingResult")

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultStrategy_reference.xml"))


    def testExecute(self):
        self.run()

        # Checks that there are no error messages

        #plugin = self.getPlugin()

        # Checks the expected result
        #strExpectedOutput = EDUtilsTest.readAndParseFile (self.getReferenceDataOutputFile())
        #strObtainedOutput = EDUtilsTest.readAndParseFile (self.edObtainedOutputDataFile)
        #EDVerbose.DEBUG("Checking obtained result...")

        #from XSDataMXv1 import XSDataStrategyResult

        #xsDataOutputExpected = XSDataStrategyResult.parseString(strExpectedOutput)
        #xsDataOutputObtained = XSDataStrategyResult.parseString(strObtainedOutput)


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edTestCasePluginExecuteControlKappaStrategyv2_0 = EDTestCasePluginExecuteControlKappaStrategyv2_0("EDTestCasePluginExecuteControlKappaStrategyv2_0")
    edTestCasePluginExecuteControlKappaStrategyv2_0.execute()

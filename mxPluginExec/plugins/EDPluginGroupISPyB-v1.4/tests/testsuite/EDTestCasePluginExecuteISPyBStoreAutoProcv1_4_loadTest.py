#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os.path, time

from EDAssert import EDAssert
from EDTestCasePluginExecute          import EDTestCasePluginExecute
from EDConfiguration import EDConfiguration
from EDUtilsFile import EDUtilsFile

class EDTestCasePluginExecuteISPyBStoreAutoProcv1_4_loadTest(EDTestCasePluginExecute):

    def __init__(self, _edStringTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginISPyBStoreAutoProcv1_4")

#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_ESRF_testDataBase.xml"))
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_ESRF_testDataBaseJboss6.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputStoreAutoProc_test.xml"))


    def testExecute(self):
        """
        Runs the plugin and then compares expected output with obtained output to verify that it executed correctly. 
        """
        for i in range(100):
            # We set up the plugin manually as it has to be executed many times
            edPlugin = self.createPlugin()
            edConfiguration = EDConfiguration(self.getConfigurationFile())
            edConfiguration.load()
            edPlugin.setConfiguration(edConfiguration.getPluginItem("EDPluginISPyBStoreAutoProcv1_4"))
            edPlugin.setDataInput(EDUtilsFile.readFileAndParseVariables(self.getDataInputFile()))
            edPlugin.executeSynchronous()
            # Check that the id extists in the results
            xsDataResult = edPlugin.getDataOutput()
            bAttributeExists = True
            if xsDataResult.getAutoProcId() is None:
                bAttributeExists = False
            EDAssert.equal(True, bAttributeExists, "Attribute AutoProcId %d in the result" % xsDataResult.autoProcId.value)
#            time.sleep(1)


    def process(self):
        """
        Adds the plugin execute test methods
        """
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':
    edTestCasePluginExecuteISPyBStoreAutoProcv1_4_loadTest = EDTestCasePluginExecuteISPyBStoreAutoProcv1_4_loadTest("EDTestCasePluginExecuteISPyBStoreAutoProcv1_4_loadTest")
    edTestCasePluginExecuteISPyBStoreAutoProcv1_4_loadTest.execute()

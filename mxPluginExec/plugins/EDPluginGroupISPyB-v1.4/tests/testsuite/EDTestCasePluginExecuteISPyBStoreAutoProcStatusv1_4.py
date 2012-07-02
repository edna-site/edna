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


import os.path

from EDAssert import EDAssert
from EDTestCasePluginExecute          import EDTestCasePluginExecute


class EDTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4(EDTestCasePluginExecute):

    def __init__(self, _edStringTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginISPyBStoreAutoProcStatusv1_4")

        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_ESRF_testDataBaseJboss6.xml"))
        #self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_ESRF_productionDataBase.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputStoreAutoProcStatus_test.xml"))


    def testExecute(self):
        """
        Runs the plugin and then compares expected output with obtained output to verify that it executed correctly. 
        """
        self.run()
        
        # Check that the id extists in the results
        edPlugin = self.getPlugin()
        xsDataResult = edPlugin.getDataOutput()
        bAttributeExists = True
        if xsDataResult.getAutoProcIntegrationId() is None:
            bAttributeExists = False
        EDAssert.equal(True, bAttributeExists, "Attribute AutoProcIntegrationId in the result")
        if xsDataResult.getAutoProcStatusId() is None:
            bAttributeExists = False
        EDAssert.equal(True, bAttributeExists, "Attribute AutoProcStatusId in the result")


    def process(self):
        """
        Adds the plugin execute test methods
        """
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':
    edTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4 = EDTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4("EDTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4")
    edTestCasePluginExecuteISPyBStoreAutoProcStatusv1_4.execute()

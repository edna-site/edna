#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011      European Synchrotron Radiation Facility
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


class EDTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_3(EDTestCasePluginExecute):

    def __init__(self, _edStringTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginISPyBStoreImageQualityIndicatorsv1_3")

        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration_ESRF_testDataBase.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputStoreImageQualityIndicators_test.xml"))


    def testExecute(self):
        """
        Runs the plugin and then compares expected output with obtained output to verify that it executed correctly. 
        """
        self.run()
        
        # Check that the id extists in the results
        edPlugin = self.getPlugin()
        xsDataResult = edPlugin.getDataOutput()
        bAttributeExists = True
        if xsDataResult.getImageQualityIndicatorsId() is None:
            bAttributeExists = False
        EDAssert.equal(True, bAttributeExists, "Attribute imageQualityIndicatorsId in the result")


    def process(self):
        """
        Adds the plugin execute test methods
        """
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':
    edTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_3 = EDTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_3("EDTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_3")
    edTestCasePluginExecuteISPyBStoreImageQualityIndicatorsv1_3.execute()

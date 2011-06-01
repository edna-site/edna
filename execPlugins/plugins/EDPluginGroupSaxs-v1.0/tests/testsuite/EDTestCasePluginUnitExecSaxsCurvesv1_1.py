#
# coding: utf8 
# 
#    Project: execPlugins / Saxs Group / saxs_mac
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright 2011 (C) ESRF

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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2011 ESRF"

from EDVerbose            import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from XSDataSaxsv1_0 import XSDataInputSaxsCurvesv1_0
from EDFactoryPluginStatic import EDFactoryPluginStatic
# Needed for loading the plugin...
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")


class EDTestCasePluginUnitExecSaxsCurvesv1_1(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin SaxsCurvesv1_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsCurvesv1_1: init")
        EDTestCasePluginUnit.__init__(self, "EDPluginExecSaxsCurvesv1_1")


    def testCheckParameters(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsCurvesv1_1: testCheckParameters")
        xsDataInput = XSDataInputSaxsCurvesv1_0()
        edPluginExecSaxsCurves = self.createPlugin()
        edPluginExecSaxsCurves.setDataInput(xsDataInput)
        edPluginExecSaxsCurves.checkParameters()



    def process(self):
        EDVerbose.DEBUG("EDTestCasePluginUnitExecSaxsCurvesv1_1: process")
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecSaxsCurvesv1_1 = EDTestCasePluginUnitExecSaxsCurvesv1_1("EDTestCasePluginUnitExecSaxsCurvesv1_1")
    edTestCasePluginUnitExecSaxsCurvesv1_1.execute()

#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteMOSFLMIndexingv10.py 1677 2010-06-22 15:41:10Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose import EDVerbose
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDApplication import EDApplication
from XSDataCommon import XSPluginItem

class EDTestCasePluginExecuteMOSFLMv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, _strTestName)
        self.setConfigurationFile(self.getRefConfigFile())
        edPluginMOSFLM = self.createPlugin()
        xsPluginItem = edPluginMOSFLM.getConfiguration()
        if xsPluginItem is None:
            xsPluginItem = EDApplication.getApplicationPluginConfiguration(self.getPluginName())
            if (xsPluginItem is None):
                # No application wide configuration file found! Try to find a project specific config file:
                xsPluginItem = EDApplication.getProjectPluginConfiguration(self.getPluginName())

            if (xsPluginItem is None):
                EDVerbose.DEBUG("EDPlugin.configure: No plugin configuration found for " + self.getPluginName())
                xsPluginItem = XSPluginItem()
            else:
                edPluginMOSFLM.setConfiguration(xsPluginItem)
        #edPluginMOSFLM.configure()
        strMOSFLMVersion = edPluginMOSFLM.getStringConfigurationParameterValue("execProcessScriptVersionString")
        if strMOSFLMVersion.find("7.0.1") != -1:
            strResultDir = "executionTestResult_v701_20070820"
        elif strMOSFLMVersion.find("7.0.5") != -1:
            strResultDir = "executionTestResult_v706_20090812"
        elif strMOSFLMVersion.find("7.0.6") != -1:
            strResultDir = "executionTestResult_v706_20100126"
        else:
            strResultDir = "executionTestResult_v707_20101220"
        strPluginTestDataHome = self.getPluginTestsDataHome()
        self.strExecutionTestDataInputHome = os.path.join(strPluginTestDataHome, "executionTestInput")
        self.strExecutionTestDataResultHome = os.path.join(strPluginTestDataHome, strResultDir)


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


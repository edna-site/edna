#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Karl Levik"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

import os


from EDMessage          import EDMessage
from EDPluginExec       import EDPluginExec
from XSDataCommon       import XSDataString
from XSDataCommon       import XSDataFile

from EDPluginExecProcessScript import EDPluginExecProcessScript

class EDPluginMxv1ParamsToXMLv1_0(EDPluginExecProcessScript):
    """
    Plugin to convert a string of parameters into a proper XSDataInputInterface object 
    """

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataString, "paramString")
        self.setScriptExecutable("/dls_sw/apps/mx-scripts/auto-edna/makeAnEDNAXML-SDA.sh")

    def setScript(self, _strScript):
        self.strScript = strScript

    def configure(self):
        """
        Gets the name (with full path) of the bash script to run 
        """
        EDPluginExecProcessScript.configure(self)
        pluginConfiguration = self.getConfiguration()
        self.setRequireCCP4(True)

        if(pluginConfiguration == None):
            self.DEBUG("*** EDPluginMxv1ParamsToXMLv1_0.configure: pluginConfiguration is None, using default settings")
        else:
            self.DEBUG("*** EDPluginMxv1ParamsToXMLv1_0.configure: pluginConfiguration found, using settings from there")
            strScriptExecutable = self.getScriptExecutable()
            if (strScriptExecutable == None):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginMxv1ParamsToXMLv1_0.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: strScriptExecutable")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        if self.hasDataInput("paramString"):
            strParamString = self.getDataInput("paramString")[0].getValue()
            self.setScriptCommandline(strParamString)
        self.setScriptLogFileName("XSDataInputInterface.xml")

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        strError = self.readProcessErrorLogFile()
        if((strError is not None) and (strError != "")):
            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginMxv1ParamsToXMLv1_0.postProcess', 'EDPluginMxv1ParamsToXMLv1_0', strError)
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage

        # This should work as long as there is a single output, i.e. not a list: 
        strFilePath = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        xsDataFileResult = XSDataFile()
        xsDataFileResult.setPath(XSDataString(strFilePath))
        # Do not specify name of output here:
        self.setDataOutput(xsDataFileResult)

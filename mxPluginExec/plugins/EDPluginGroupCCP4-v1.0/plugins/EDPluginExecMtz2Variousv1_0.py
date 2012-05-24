# coding: utf8
#
#    Project: MX Plugin Exec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile


from XSDataCCP4v1_0 import XSDataInputMtz2Various
from XSDataCCP4v1_0 import XSDataResultMtz2Various

class EDPluginExecMtz2Variousv1_0(EDPluginExecProcessScript ):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__(self ):
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputMtz2Various)
        self.setRequireCCP4(True)
        self.strHklFile = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.preProcess")
        self.generateCommands()

        
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.process")

        
    def finallyProcess(self, _edObject = None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.finallyProcess")
        xsDataResult = XSDataResultMtz2Various()
        xsDataResult.setHklfile(XSDataFile(XSDataString(self.strHklFile)))
        self.setDataOutput(xsDataResult)
    
    def generateCommands(self):
        """
        This method creates a list of commands for mtz2various
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.generateCommands")
        xsDataInputMtz2Various = self.getDataInput()

        if (xsDataInputMtz2Various is not None):
            
            strMtzFile = xsDataInputMtz2Various.getMtzfile().getPath().getValue()
            self.strHklFile = os.path.join(self.getWorkingDirectory(), os.path.splitext(os.path.basename(strMtzFile))[0] + ".hkl")
            self.setScriptCommandline(" hklin " + \
                                      strMtzFile +\
                                      " hklout " +\
                                      self.strHklFile)

            strLabinLine = "LABIN"
            for strLabin in xsDataInputMtz2Various.getLabin():
                strLabinLine += " " + strLabin.getValue()
            self.addListCommandExecution(strLabinLine)
            
            if xsDataInputMtz2Various.getOutput() is not None:
                self.addListCommandExecution("OUTPUT "+xsDataInputMtz2Various.getOutput().getValue())
                
            
        
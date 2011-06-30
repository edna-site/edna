#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Diamond Light Source
#
#    Principal author:       Irakli Sikharulidze
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

__author__="Irakli Sikharulidze"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source"

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataFind import XSDataInputFind
from XSDataFind import XSDataResultFind

class EDPluginExecFindv0_1(EDPluginExecProcessScript ):
    """
    [To be replaced with a description of EDPluginExecProcessScriptTemplatev10]
    """
    

    def __init__(self ):
        """
        """
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputFind)
        
        self.__searchPath = None
        self.__inputString = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecProcessScriptFindv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")
        
        self.__searchPath = self.getDataInput().getSearchPath().getValue() 
        self.__inputString = self.getDataInput().getInputString().getValue() 

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecProcessScriptFindv0_1.preProcess")
        self.generateFindScript()
        
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecProcessScriptFindv0_1.process")

        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecProcessScriptFindv0_1.postProcess")
        # Create some output data
        xsDataResult = XSDataResultFind()
        self.setDataOutput(xsDataResult)
    
    def generateFindScript(self):
        commandString = ' '.join([self.__searchPath,'-name "*" -exec grep',self.__inputString, "{} \;"])
        self.setScriptCommandline('')
        #self.setScriptCommandline(commandString)
        #self.setScriptCommandline('\n'.join([commandString + ' & ','/usr/bin/find ' + commandString + ' & ','/usr/bin/find ' + commandString]))

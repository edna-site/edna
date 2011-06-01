#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:        irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

from EDVerbose import EDVerbose
from EDActionCluster import EDActionCluster


class EDParallelJobLauncher(EDActionCluster):
    """
    Class for starting execution plugin jobs in parallel for every input data object in dictionary   
    """
    
    def __init__(self, _edControlPlugin, _strPluginName, _dictXSDataInput, _iNbThreads):
        """
        Initialaze data structures
        @param _edControlPlugin: Parent control plugin
        @param _strPluginName: Name of the execution plugin to run
        @param _dictXSDataInput: Dictionary of the input objects for execution plugin
        """
        
        EDActionCluster.__init__(self, _iNbThreads)
        
        self.__strPluginName = _strPluginName
        self.__dictXSDataInput = _dictXSDataInput
        self.__edControlPlugin = _edControlPlugin
        
        self.__xsEDPluginExecJobs = {}

        
    def preProcess(self, _edObject=None):
        EDActionCluster.preProcess(self)
        EDVerbose.DEBUG("EDParallelJobLauncher.preProcess")

        for __dictKey in self.__dictXSDataInput.keys():
            self.__xsEDPluginExecJobs[__dictKey] = self.__edControlPlugin.loadPlugin(self.__strPluginName)
            
            if (self.__xsEDPluginExecJobs[__dictKey] is not None):
                
                if (self.__dictXSDataInput[__dictKey] is not None) and (self.__dictXSDataInput[__dictKey] is not "") :
                    self.__xsEDPluginExecJobs[__dictKey].setDataInput(self.__dictXSDataInput[__dictKey])
                    self.addAction(self.__xsEDPluginExecJobs[__dictKey])
                else:
                    EDVerbose.screen("ERROR! Input data not found in " + self.__xsEDPluginExecJobs[__dictKey].getWorkingDirectory())
                    
            else:
                EDVerbose.screen("ERROR! Plugin not found : " + self.__strPluginName)
                
        self.setTimeOut(self.__edControlPlugin.getTimeOut())
        
        
    def getPluginJobs(self):
        """
        Get dictionary of launched plugin jobs
        """
        return self.__xsEDPluginExecJobs 

    
    def getListOfWarningMessages(self):
        _listOfWarningMessages = []
        map(_listOfWarningMessages.extend, [tmpPlugin.getListOfWarningMessages() for tmpPlugin in self.__xsEDPluginExecJobs.values()])
        return _listOfWarningMessages 
    
            
    def getListOfErrorMessages(self):
        _listOfErrorMessages = []
        map(_listOfErrorMessages.extend, [tmpPlugin.getListOfErrorMessages() for tmpPlugin in self.__xsEDPluginExecJobs.values()])
        return _listOfErrorMessages 
    

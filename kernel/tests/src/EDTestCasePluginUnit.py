#coding: utf8
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (kieffer@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"

import os, glob, shutil

from EDVerbose import EDVerbose
from EDConfiguration import EDConfiguration
from EDTestCasePlugin import EDTestCasePlugin
from EDUtilsParallel    import EDUtilsParallel

class EDTestCasePluginUnit(EDTestCasePlugin):
    """
    This is the main class for all Plugin Unit tests
    """

    def __init__(self, _strPluginName, _strPluginDir=None, _strTestName=None):
        """
        Initialize the Plugin Unit test
        """
        EDTestCasePlugin.__init__(self, _strPluginName, _strPluginDir, _strTestName)
        self.__edPlugin = None
#        To track dead locks
        EDUtilsParallel.initializeNbThread(1)


    def preProcess(self):
        """
        Creates the main plugin instance
        """
        self.__edPlugin = self.createPlugin()


    def getPlugin(self):
        """
        Returns the main plugin instance
        """
        return self.__edPlugin


    def getPluginConfiguration(self, _strConfigurationFileName):
        """
        Returns the plugin configuration from a configuration file
        """
        xsPluginItem = None
        edConfiguration = EDConfiguration(_strConfigurationFileName)
        if(edConfiguration != None):
            xsPluginItem = edConfiguration.getXSConfigurationItem(self.getPluginName())
            if(xsPluginItem == None):
                EDVerbose.warning("EDTestCasePluginUnit.getPluginConfiguration: Could not get configuration plugin item for: " + self.getPluginName())
        else:
            EDVerbose.warning("EDTestCasePluginUnit.getPluginConfiguration: Could not load Configuration: " + _strConfigurationFileName)
        return xsPluginItem


    def cleanUp(self, _edPlugin):
        """
        Cleans up some empty directories 
        (mainly working directories that were created automatically, but not filled as Unit tests do not execute the plugin)
        """
        workingDirectory = _edPlugin.getWorkingDirectory()
        if(workingDirectory is not None):
            fileList = glob.glob(os.path.join(workingDirectory, "*"))
            if(len(fileList) == 0):
                EDVerbose.DEBUG("Deleting " + workingDirectory + " ...")
                shutil.rmtree(workingDirectory)
        EDUtilsParallel.semaphoreNbThreadsRelease()



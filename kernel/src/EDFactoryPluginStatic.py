# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDFactoryPlugin.py 1530 2010-05-17 14:11:41Z kieffer $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:    Olof Svensson (svensson@esrf.fr) 
#                          Jérôme Kieffer (kieffer@esrf.fr) 
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
__authors__ = ["Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import threading #, sys, os
from EDFactoryPlugin    import EDFactoryPlugin
from EDUtilsPath        import EDUtilsPath
from EDVerbose          import EDVerbose


class EDFactoryPluginStatic:
    """
    The purpose of this class is to provide a single EDFactoryPlugin instance for a given Python session
    """

    # Static variables
    __semaphore = None
    __edFactoryPlugin = None
    __dictLoadedModules = {}

    @staticmethod
    def getFactoryPlugin():
        EDFactoryPluginStatic.synchronizeOn()
        if (EDFactoryPluginStatic.__edFactoryPlugin is None):
            EDFactoryPluginStatic.__edFactoryPlugin = EDFactoryPlugin()
        EDFactoryPluginStatic.synchronizeOff()
        return EDFactoryPluginStatic.__edFactoryPlugin


    @staticmethod
    def loadPlugin(_strPluginName):
        return EDFactoryPluginStatic.getFactoryPlugin().loadPlugin(_strPluginName)

    @staticmethod
    def getModuleLocation(_strModuleName):
        return EDFactoryPluginStatic.getFactoryPlugin().getModuleLocation(_strModuleName)

    @staticmethod
    def loadModule(_strModuleName):
        EDFactoryPluginStatic.getFactoryPlugin().loadModule(_strModuleName)


    @staticmethod
    def preImport(_strModuleName, _strPath=None, _strForceVersion=None, _strMethodVersion="version"):
        """
        Static method that import locally with a lock and keeps track of already imported module.
        @param _strModuleName: Name of the module to import
        @param _strPath: Path to the module to import
        @param _strForceVersion: version string to enforce to. Should be compatible with the method given !!!
        @param _strMethodVersion: property or method to get the version number (should return a string)
        @return: reference to the module loaded
        """
        return EDFactoryPlugin.preImport(_strModuleName, _strPath, _strForceVersion, _strMethodVersion)


    @staticmethod
    def unImport(_strModuleName):
        """
        Static method that remove a module from the imported modules.
        @param _strModuleName: Name of the module to import
        """
        EDFactoryPlugin.unImport(_strModuleName)


    @staticmethod
    def getConfigurationHome(_strPluginName):
        """
        Returns the configuration directory path for a given test module
        """
        strModuleLocation = EDFactoryPluginStatic.getFactoryPlugin().getModuleLocation(_strPluginName)
        strConfigurationHome = EDUtilsPath.appendListOfPaths(strModuleLocation, [ "..", "..", "..", "conf" ])
        return strConfigurationHome


    @staticmethod
    def getPathToProjectConfigurationFile(_strModuleName):
        return EDFactoryPluginStatic.getFactoryPlugin().getPathToProjectConfigurationFile(_strModuleName)


    @staticmethod
    def synchronizeOn():
        """
        Lock the whole class
        """
        if (EDFactoryPluginStatic.__semaphore is None):
            EDFactoryPluginStatic.__semaphore = threading.Semaphore()
        EDFactoryPluginStatic.__semaphore.acquire()


    @staticmethod
    def synchronizeOff():
        """
        Unlock the whole class
        """
        if (EDFactoryPluginStatic.__semaphore is None):
            EDVerbose.ERROR("Trying to release unintitialized Semaphore in FactoryPluginStatic")
        else:
            EDFactoryPluginStatic.__semaphore.release()




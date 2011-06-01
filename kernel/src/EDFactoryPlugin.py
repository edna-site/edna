# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:    Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author: Marie-Francoise Incardona (incardon@esrf.fr)
#                         Jérôme Kieffer (jerome.kieffer@esrf.fr)
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
__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, threading

from EDObject    import EDObject
from EDVerbose   import EDVerbose
from EDUtilsPath import EDUtilsPath
from EDUtilsFile import EDUtilsFile
from EDModule    import EDModule

from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataKeyValuePair
from XSDataCommon import XSDataString

class EDFactoryPlugin(EDObject):
    """
    This class provides a factory for loading plugins and/or modules. By default all plugins/modules located
    in $EDNA_HOME can be loaded with this class. A plugin or module located elsewhere can be loaded
    provided one of its parent directories is added with the method "addPluginRootDirectory".
    
    All plugins or modules with file name ending with \*.py are located. If the file name starts
    with "EDPlugin" or "XSData" a warning is issued if multiple modules/plugins with the same name are located.
    
    Both the loadPlugin and loadModule methods will automatically add the module location to the
    application python path, if it not already exists on the path. 

    The EDFactoryPlugin also adds the path to a "src" directory if the following scheme for
    locating the plugins is followed:
    
    EDNA project, e.g. mxv1, mxExecPlugins etc::
     |
     |-conf
     |-datamodel
     |-src
     |  |-XSData[project name].py
     |-tests
     |   |-data
     |   |-testsuite
     |   |    |-EDTestSuite[for the project]
     |
     |-plugins
     |   |-EDPlugin[name of plugin]-v1.0
     |   |   |-plugins
     |   |   |   |-EDPlugin[name of plugin]v10.py
     |   |   |   |-EDPlugin[another name of plugin]v10.py
     |   |   |-tests
     |   |   |   |-data
     |   |   |   |-testsuite
     |   |   |   |    |-EDTestCase[for a plugin]
         
    The "src" directory above is used for storing the data bindings for a project common data model,
    e.g. XSDataMXv1.py, or in general for code used by all the plugins. The path to the "src"
    directory is added using a relative path from the plugin location: ../../../src
    The path to the src directory is only added if the src directory exists.
    
    In order to improve speed, a cache of the modules and their location is saved to disk
    the first time a module/plugin is located. The default location of this cache
    file is in $EDNA_HOME, and the default name is ".XSDataDictionaryModule.xml".
     
    If a cache files is present, and if a module/plugin cannot be loaded, the cache is
    updated by searching all plugin root directories again.
    
    If a directory contains the file ".ednaignore" in this directory and sub-directories are ignored.
    """

    # class  variables
    IGNORE_FILE = ".ednaignore"
    __dictLoadedModules = {}
    __semaphoreStatic = threading.Semaphore()

    def __init__(self):
        EDObject.__init__(self)
        strEdnaHome = EDUtilsPath.getEdnaHome()
        # Default plugin root directory: $EDNA_HOME
        self.__listPluginRootDirectory = [ strEdnaHome ]
        self.__dictModuleLocation = None
        self.__strCacheFileName = ".XSDataDictionaryModule.xml"
        self.__strPathToModuleCache = os.path.abspath(os.path.join(EDUtilsPath.getEdnaHome(), self.__strCacheFileName))



    def __initModuleDictionary(self):
        """
        This private method initialises the dictionary with all plugins. If the path to
        the dictionary cache file exists the plugins are loaded, otherwise
        the plugin root directories are searched and the dictionary is
        written to the cache file.
        """
        if (os.path.exists(self.__strPathToModuleCache)):
            self.loadModuleDictionaryFromDisk(self.__strPathToModuleCache)
        else:
            self.__searchRootDirectories()
            self.saveModuleDictionaryToDisk(self.__strPathToModuleCache)



    def saveModuleDictionaryToDisk(self, _strPath):
        """
        This method saves the module dictionary to disk in form of XML.
        This method should be private but is kept public in order to be unit tested.

        @param _strPath: Path to the module dictionary XML file
        @type _strPath: python string
        """
        xsDataDictionaryPlugin = XSDataDictionary()
        strEdnaHome = EDUtilsPath.getEdnaHome()
        for strModule in self.__dictModuleLocation:
            xsDataKeyValuePair = XSDataKeyValuePair()
            xsDataKeyValuePair.setKey(XSDataString(strModule))
            strModuleLocation = self.__dictModuleLocation[ strModule ]
            # Remove the path up to $EDNA_HOME
            strModuleLocationStripped = strModuleLocation.replace(strEdnaHome, "")
            if (strModuleLocationStripped.startswith("/") or  strModuleLocationStripped.startswith("\\")):
                strModuleLocationStripped = strModuleLocationStripped[1:]
            xsDataKeyValuePair.setValue(XSDataString(strModuleLocationStripped))
            xsDataDictionaryPlugin.addKeyValuePair(xsDataKeyValuePair)
        try:
            xsDataDictionaryPlugin.outputFile(_strPath)
        except:
            EDVerbose.warning("The module cache could not be written to disk.")


    def loadModuleDictionaryFromDisk(self, _strPath):
        """
        Loads the cache from disk.

        @param _strPath: Path to the module dictionary XML file
        @type _strPath: python string
        """
        #strPath = None
        strEdnaHome = EDUtilsPath.getEdnaHome()
        self.__dictModuleLocation = {}
        try:
            xsDataDictionaryPlugin = XSDataDictionary.parseFile(_strPath)
            for xsDataKeyValuePair in xsDataDictionaryPlugin.getKeyValuePair():
                strModuleName = xsDataKeyValuePair.getKey().getValue()
                strModuleLocationRelative = xsDataKeyValuePair.getValue().getValue()
                strModuleLocationAbsolute = os.path.abspath(os.path.join(strEdnaHome, strModuleLocationRelative))
                if not os.path.exists(strModuleLocationAbsolute):
                    raise BaseException("Path loaded from disk does not exist: %s" % strModuleLocationAbsolute)
                self.__dictModuleLocation[ strModuleName ] = strModuleLocationAbsolute
        except BaseException, oExcpetionType:
            EDVerbose.warning("Error when reading module cache from disk: %s" % str(oExcpetionType))
            EDVerbose.warning("Forcing reload of module locations.")
            self.__searchRootDirectories()
            self.saveModuleDictionaryToDisk(_strPath)


    def getModuleLocation(self, _strModuleName):
        """
        This method returns the location of a module, e.g. XSDataCommon.

        @param _strModuleName: Name of the module
        @type _strModuleName: python string

        @return: Path to the module location
        @type: python string
        """
        self.synchronizeOn()
        strModuleLocation = None
        if (self.__dictModuleLocation is None):
            self.__initModuleDictionary()
        if (_strModuleName in self.__dictModuleLocation.keys()):
            strModuleLocation = self.__dictModuleLocation[ _strModuleName ]
            strDirectoryIgnored = self.checkDirectoriesForIgnoreFile(strModuleLocation)
            if strDirectoryIgnored:
                EDVerbose.warning("Module location %s ignored because directory %s contains %s" % (strModuleLocation, strDirectoryIgnored, EDFactoryPlugin.IGNORE_FILE))
                self.__searchRootDirectories()
                self.saveModuleDictionaryToDisk(self.__strPathToModuleCache)
                strModuleLocation = None
        else:
            # The module was not found - force reloading of all plugins
            EDVerbose.warning("Module %s not found, forcing reloading of all modules..." % _strModuleName)
            self.__searchRootDirectories()
            # Save the new dictionary in any case - even if the plugin might not be found.
            self.saveModuleDictionaryToDisk(self.__strPathToModuleCache)
            if (_strModuleName in self.__dictModuleLocation.keys()):
                strModuleLocation = self.__dictModuleLocation[ _strModuleName ]
                # Fix for bug #395 - update the saved cache
                EDVerbose.DEBUG("EDFactoryPlugin.loadModule: Updating the module cache file %s" % self.__strPathToModuleCache)
            else:
                EDVerbose.DEBUG("EDFactoryPlugin.loadModule: module %s not found after forced reload of all modules." % _strModuleName)
        self.synchronizeOff()
        return strModuleLocation


    def checkDirectoriesForIgnoreFile(self, _strDirectory):
        # Check that this directory and all directories above till $EDNA_HOME should not be ignored
        strDirectoryIgnored = None
        bContinueSearching = True
        strCurrentDirectory = _strDirectory
        while bContinueSearching:
            if EDFactoryPlugin.IGNORE_FILE in os.listdir(strCurrentDirectory):
                strDirectoryIgnored = strCurrentDirectory
                bContinueSearching = False
            # Move up a directory
            strPreviousDirectory = strCurrentDirectory
            strCurrentDirectory = os.path.abspath(os.path.join(strCurrentDirectory, ".."))
            if strCurrentDirectory == EDUtilsPath.getEdnaHome() or strCurrentDirectory == strPreviousDirectory:
                bContinueSearching = False
        return strDirectoryIgnored



    def isPlugin(self, _strFileName):
        """
        This method returns a True if the file name provided is considered to
        be an EDNA plugin or module, i.e. it starts with either "EDPlugin" or "XSData" 
        and it ends with ".py", otherwise the method returns False.

        @param _strFileName: Name of the file
        @type _strFileName: python string

        @return: True or False
        @type: boolean
        """
        bValue = False
        if ((_strFileName.startswith("EDPlugin") or _strFileName.startswith("XSData")) and \
             _strFileName.endswith(".py")):
            bValue = True
        return bValue


    def __addPluginLocation(self, _strPluginRootDirectory, _strDirectoryVisit, _listDirectory):
        """
        This method is called by the python walk command in the addPluginRootDirectory method.
        
        It checks all the file names in the _listDirectory list if they corresponds to plugins or modules
        using the method "isPlugin". If the file name corresponds to a plugin or module, the location of the
        plugin or module is added to the self.__dictModuleLocation.        

        @param _strPluginRootDirectory: Name of the root directory
        @type _strPluginRootDirectory: python string

        @param _strDirectoryVisit: Name of the directory currently visited
        @type _strDirectoryVisit: python string

        @param _listDirectory: List of directory entries
        @type _listDirectory: python list
        """
        if (self.__dictModuleLocation is None):
            self.__dictModuleLocation = {}
        strDirectoryIgnored = self.checkDirectoriesForIgnoreFile(_strDirectoryVisit)
        if strDirectoryIgnored:
            EDVerbose.DEBUG("Directory %s ignored because directory %s contains %s" % (_strDirectoryVisit, strDirectoryIgnored, EDFactoryPlugin.IGNORE_FILE))
        else:
            for strFileName in _listDirectory:
                if strFileName.endswith(".py"):
                    # Strip off the ".py" exctension
                    strPluginName = strFileName[:-3]
                    if (strPluginName in self.__dictModuleLocation.keys() and self.isPlugin(strFileName)):
                        EDVerbose.error("EDFactoryPlugin: Found multiple plugins/modules with the same name!")
                        EDVerbose.error("EDFactoryPlugin: Plugin/module already loaded:" + strPluginName + ", location: " + self.__dictModuleLocation[ strPluginName ])
                        EDVerbose.error("EDFactoryPlugin: Duplicate plugin/module definition in :" + _strDirectoryVisit)
                        raise RuntimeError
                    else:
                        self.__dictModuleLocation[ strPluginName ] = _strDirectoryVisit


    def addPluginRootDirectory(self, _strPluginRootDirectory):
        """
        This method can be called by an application if plugins or modules are supposed to be loaded
        outside the EDNA_HOME directory.

        @param _strPluginRootDirectory: Name of the root directory
        @type _strPluginRootDirectory: python string
        """
        self.synchronizeOn()
        self.__listPluginRootDirectory.append(_strPluginRootDirectory)
        self.synchronizeOff()


    def __searchRootDirectories(self):
        """
        This method loops through all the root directories and recursively searchs for modules/plugins.
        """
        self.__dictModuleLocation = {}
        for strPluginRootDirectory in self.__listPluginRootDirectory:
            # The following Python call will be deprecated in Python 3.0, see bug #262
            os.path.walk(strPluginRootDirectory, self.__addPluginLocation, strPluginRootDirectory)


    def loadPlugin(self, _strPluginName):
        """
        This method loads a plugin if it's present in the self.__dictModuleLocation.

        @param _strPluginName: Name of the plugin to be loaded
        @type _strPluginName: python string
        """
        edPlugin = None
        strModuleLocation = self.getModuleLocation(_strPluginName)
        if (strModuleLocation is not None):
            self.appendPath(strModuleLocation)
            oModule = EDFactoryPlugin.preImport(_strPluginName, strModuleLocation)
            if oModule:
                edPlugin = oModule.__dict__[ _strPluginName ]()
            else:
                EDVerbose.error("Plugin %s couldn't be loaded from %s" % (_strPluginName, strModuleLocation))
        else:
            EDVerbose.error("Plugin not found: " + _strPluginName)
        return edPlugin


    def loadModule(self, _strModuleName):
        """
        This method loads a module, i.e. it adds the module to the python path.

        @param _strModuleName: Name of the module to be loaded
        @type _strModuleName: python string
        """
        strModuleLocation = self.getModuleLocation(_strModuleName)
        if (strModuleLocation is not None):
            EDFactoryPlugin.preImport(_strModuleName, strModuleLocation)



    def appendPath(self, _strModuleLocation):
        """
        This method appends the plugin "src" directory to the system path, if it's not already present.

        @param _strModuleLocation: Path to the module location
        @type _strModuleLocation: python string
        """
        strSrcDirectory = EDUtilsPath.appendListOfPaths(_strModuleLocation, [ "..", "..", "..", "src" ])
        if (os.path.exists(strSrcDirectory)):
            if (not strSrcDirectory in sys.path):
                sys.path.append(strSrcDirectory)


    def getProjectRootDirectory(self, _strModuleName):
        """
        This method returns the project root directory of a given module name.
        A directory is considered to be a project root if it contains the following
        directories: "conf", "src" and "plugins"

        @param _strModuleName: Name of the module
        @type _strModuleName: python string
        
        @return: The project root directory
        @type: python string
        """
        strModuleLocation = self.getModuleLocation(_strModuleName)
        self.synchronizeOn()
        strProjectRootDirectory = None
        if (strModuleLocation is not None):
            # Now start looking for "conf" and "plugins", max four iterations
            bFoundRootDirectory = False
            iMaxIterations = 4
            strProjectRootDirectory = strModuleLocation
            while ((not bFoundRootDirectory) and (iMaxIterations > 0)):
                strProjectRootDirectory = os.path.abspath(os.path.join(strProjectRootDirectory, ".."))
                edListDirectoryContent = EDUtilsPath.getFileList(strProjectRootDirectory)
                if (("conf" in edListDirectoryContent) and \
                     ("src" in edListDirectoryContent) and \
                     ("plugins" in edListDirectoryContent)):
                    bFoundRootDirectory = True
                iMaxIterations = iMaxIterations - 1
            if (not bFoundRootDirectory):
                strProjectRootDirectory = None
        self.synchronizeOff()
        return strProjectRootDirectory


    def getProjectName(self, _strModuleName):
        """
        This method returns the name of the project by finding the project root directory
        and returning the basename.

        @param _strModuleName: Name of the module
        @type _strModuleName: python string
        
        @return: The project name
        @type: python string
        """
        strProjectName = None
        strProjectRootDirectory = self.getProjectRootDirectory(_strModuleName)
        self.synchronizeOn()
        if (strProjectRootDirectory is not None):
            strProjectName = EDUtilsFile.getBaseName(strProjectRootDirectory)
        self.synchronizeOff()
        return strProjectName


    def getPathToProjectConfigurationFile(self, _strModuleName):
        """
        This method returns the path to the Project configuration file.

        @param _strModuleName: Name of the module
        @type _strModuleName: python string
        
        @return: The path to the project configuration file
        @type: python string
        """
        strPathToProjectConfigurationFile = None
        strCurrentDirectory = self.getModuleLocation(_strModuleName)
        bConfFileFound = False
        self.synchronizeOn()
        while not bConfFileFound:
            strPreviousDirectory = strCurrentDirectory
            strCurrentDirectory = os.path.dirname(strCurrentDirectory)
            strPathToConfigurationDirectory = os.path.abspath(os.path.join(strCurrentDirectory, "conf"))
            strConfigurationFileName = "XSConfiguration_%s.xml" % EDUtilsPath.getEdnaSite()
            strPathToProjectConfigurationFile = os.path.abspath(os.path.join(strPathToConfigurationDirectory, \
                                                                            strConfigurationFileName))
            EDVerbose.DEBUG("Looking for configuration file for %s in %s" %
                            (_strModuleName, strPathToProjectConfigurationFile))
            bConfFileFound = os.path.isfile(strPathToProjectConfigurationFile)
            if strCurrentDirectory in (EDUtilsPath.getEdnaHome(), strPreviousDirectory):
                strPathToProjectConfigurationFile = None
                break
        self.synchronizeOff()
        return strPathToProjectConfigurationFile


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
        oModule = None
        EDVerbose.DEBUG("EDFactoryPlugin.preImport %s %s %s is loaded=%s" % (_strModuleName, _strPath, _strForceVersion, _strModuleName in EDFactoryPlugin.__dictLoadedModules))
        if (_strModuleName not in EDFactoryPlugin.__dictLoadedModules) or \
                (EDFactoryPlugin.__dictLoadedModules[_strModuleName].module is None):
            EDFactoryPlugin.__semaphoreStatic.acquire()
            if _strModuleName not in EDFactoryPlugin.__dictLoadedModules:
                edModule = EDModule(_strModuleName)
                EDFactoryPlugin.__dictLoadedModules[_strModuleName] = edModule
            else:
                edModule = EDFactoryPlugin.__dictLoadedModules[_strModuleName]
            EDFactoryPlugin.__semaphoreStatic.release()
            oModule = edModule.preImport(_strPath, _strMethodVersion)
        elif (_strForceVersion) and \
            (EDFactoryPlugin.__dictLoadedModules[_strModuleName].version < _strForceVersion):
            EDVerbose.WARNING("EDFactoryPlugin.preimport wrong module version: %s is %s not %s" % (_strModuleName, EDFactoryPlugin.__dictLoadedModules[_strModuleName].version, _strForceVersion))
            EDFactoryPlugin.unImport(_strModuleName)
            EDFactoryPlugin.preImport(_strModuleName, _strPath,)
        else:
            oModule = EDFactoryPlugin.__dictLoadedModules[_strModuleName].module
        return oModule



    @staticmethod
    def unImport(_strModuleName):
        """
        Static method that remove a module from the imported modules.
        @param _strModuleName: Name of the module to un-import
        """
        if _strModuleName in  EDFactoryPlugin.__dictLoadedModules:
            EDVerbose.DEBUG("EDFactoryPlugin.unImport: unload module %s." % _strModuleName)
            EDFactoryPlugin.__semaphoreStatic.acquire()
            module = EDFactoryPlugin.__dictLoadedModules.pop(_strModuleName)
            module.unImport()
            EDFactoryPlugin.__semaphoreStatic.release()
        else:
            EDVerbose.WARNING("EDFactoryPlugin.unImport: Module %s is not loaded. " % _strModuleName)



# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr)
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
from __future__ import with_statement

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This class handles the EDNA configuration XML/JSON files.
"""

import os, json
from EDVerbose import EDVerbose
from EDLogging import EDLogging
from EDUtilsFile import EDUtilsFile
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDDecorator import deprecated
from XSDataCommon import XSConfiguration, XSPluginItem, XSParamList, XSParamItem

def bestType(a):
    """
    convert a string to it's typed version
    """
    if a.lower() in ["true", "on"]:
        return True
    if a.lower() in ["false", "off"]:
        return False
    if a.lower() in ["none", "nul", "null"]:
        return None
    try:
        ia = int(a)
    except:
        ia = None
    try:
        fa = float(a)
    except:
        fa = None
    if ia is not None and fa is not None:
        if ia == fa:
            return ia
        else:
            return fa
    else:
        return str(a)


class EDConfiguration(EDLogging):
    """
    This class handles the EDNA configuration XML files. The structure of
    the XML is described in the XSDataCommon data model.

    If environment variable strings like "$XXX" or "${XXX}" is present in the
    configuration file, the strings are replaced with the corresponding
    environment variable content. For example, if "${CCP4} is present in the
    XML string, the string "${CCP4}" is replaced by the environment variable $CCP4
    content.
    """


    def __init__(self, _strFileName=None):
        """"Set  up semaphore for thread safeness and dictionary for config files"""
        EDLogging.__init__(self)
        self._dictConfigurationFiles = {}
        self._dictPluginConfiguration = {}
        if _strFileName is not None:
            self.addConfigurationFile(_strFileName)

    def addConfigurationFile(self, _strFileName, _bReplace=True):
        """Loads an XML/JSON config file into the dictionary if not already loaded"""
        strFileName = os.path.abspath(_strFileName)
        if not os.path.exists(strFileName):
            self.WARNING("Trying to add configuration file but file %s doesn't exist!" % _strFileName)
        else:
            if strFileName in self._dictConfigurationFiles:
                self.DEBUG("EDConfiguration.addConfigurationFile: File %s already parsed, in cache" % strFileName)
            else:
                self.DEBUG("EDConfiguration.addConfigurationFile: Parsing file %s" % strFileName)
                strConfiguration = EDUtilsFile.readFileAndParseVariables(strFileName)
                if strFileName.endswith(".xml"):
                    xsConfiguration = XSConfiguration.parseString(strConfiguration)
                    if xsConfiguration is not None :
                        dictConfig = {"__extend__":[]}
                        for other in xsConfiguration.XSImportConfiguration:
                            if other.directory not in [None, "None"]:
                                dictConfig["__extend__"].append(os.path.join(other.directory, other.name))
                            else:
                                dictConfig["__extend__"].append(other.name)

                        xsPluginList = xsConfiguration.getXSPluginList()
                        if xsPluginList is not None:
                            for pluginItem in xsPluginList.getXSPluginItem():
                                plugin_conf = {}
                                plugin_name = pluginItem.name
                                paramList = pluginItem.getXSParamList()
                                if paramList:
                                    for paramItem in paramList.getXSParamItem():
                                        plugin_conf[paramItem.name] = bestType(paramItem.value)
                                dictConfig[plugin_name] = plugin_conf
                else: #JSON mode
                    dictConfig = json.loads(strConfiguration)
                # Make sure we are thread safe when manipulating the cache
                with self.locked():
                    self._dictConfigurationFiles[strFileName] = dictConfig
                # First look for configuration imports
                for importConfiguration in dictConfig["__extend__"]:
                    if importConfiguration.startswith(os.sep):
                        for ext in ["", ".json", ".xml" ]:
                            if os.path.isfile(importConfiguration + ext):
                                strImportPath = importConfiguration + ext
                                break
                    else:
                        for ext in ["", ".json", ".xml" ]:
                            path = os.path.join(os.path.dirname(strFileName), importConfiguration + ext)
                            if os.path.isfile(path):
                                strImportPath = path
                                break
                    self.DEBUG("Importing configuration file : %s" % strImportPath)
                    self.addConfigurationFile(strImportPath, _bReplace) #Was True, why?

                # Make sure we are thread safe when manipulating the cache
                with self.locked():
                    # Load configurations into the plugin dictionary
                    for strPluginName in dictConfig:
                        if strPluginName == "__extend__":
                            continue
                        if strPluginName in self._dictPluginConfiguration:
                            if _bReplace:
                                self.DEBUG("EDConfiguration.addConfigurationFile: plugin configuration for %s already exists and will be replaced." % strPluginName)
                                self._dictPluginConfiguration[strPluginName] = dictConfig[strPluginName]
                            else:
                                self.DEBUG("EDConfiguration.addConfigurationFile: plugin configuration for %s already exists and will not be replaced." % strPluginName)
                        else:
                            self.DEBUG("EDConfiguration.addConfigurationFile: adding plugin configuration for %s." % strPluginName)
                            self._dictPluginConfiguration[strPluginName] = dictConfig[strPluginName]


    def getPathToProjectConfigurationFile(self, _strPluginName):
        """
        This method returns the path to the Project configuration file.

        @param _strPluginName: Name of the module
        @type _strPluginName: python string

        @return: The path to the project configuration file
        @type: python string
        """
        strPathToProjectConfigurationFile = None
        strCurrentDirectory = EDFactoryPluginStatic.getModuleLocation(_strPluginName)
        if strCurrentDirectory is None:
            self.WARNING("Cannot find path to configuration for plugin %s" % _strPluginName)
        else:
            with self.locked():
                bConfFileFound = False
                strPathToProjectConfigurationFile = None
                strConfigurationFileBaseName = "XSConfiguration_%s" % EDUtilsPath.EDNA_SITE
                while not bConfFileFound:
                    strPreviousDirectory = strCurrentDirectory
                    strCurrentDirectory = os.path.dirname(strCurrentDirectory)
                    if strCurrentDirectory in (EDUtilsPath.EDNA_HOME, strPreviousDirectory):
                        strPathToProjectConfigurationFile = None
                        break
                    strPathToConfigurationDirectory = os.path.abspath(os.path.join(strCurrentDirectory, "conf"))
                    for ext in [".json", ".xml"]:
                        strPathToProjectConfigurationFile = os.path.abspath(os.path.join(strPathToConfigurationDirectory, \
                                                                                    strConfigurationFileBaseName + ext))
                        self.DEBUG("Looking for configuration file for %s in %s" %
                                    (_strPluginName, strPathToProjectConfigurationFile))
                        bConfFileFound = os.path.isfile(strPathToProjectConfigurationFile)
                        if bConfFileFound:
                            break
        return strPathToProjectConfigurationFile


    ############################################################################
    # Dictionary like interface
    ############################################################################

    def get(self, _strPluginName, default=None):
        """
        Returns the configuration for a given plugin as a dictionary. 
        
        If the plugin configuration is not in the cache the methods
        'getPathToProjectConfigurationFile' and 'addConfigurationFile'
        are called for attempting to load the plugin configuration
        from a file (lazy loading).
        
        @param _strPluginName: name of the plugin
        @param default: optional default return value if plugin not loaded (e.g. {})
        @return: configuration as a dict (or default value)
        """
        dictPluginConfiguration = default
        if _strPluginName in self._dictPluginConfiguration:
            dictPluginConfiguration = self._dictPluginConfiguration[_strPluginName]
        else:
            strPathToProjectConfigurationFile = self.getPathToProjectConfigurationFile(_strPluginName)
            if strPathToProjectConfigurationFile is not None:
                self.addConfigurationFile(strPathToProjectConfigurationFile, _bReplace=True)
                if _strPluginName in self._dictPluginConfiguration:
                    dictPluginConfiguration = self._dictPluginConfiguration[_strPluginName]
        return dictPluginConfiguration

    def __contains__(self, key):
        return (key in self._dictPluginConfiguration)

    def __getitem__(self, _strPluginName):
        """
        edConfig["myPlugin"] -> {}
        """
        return self._dictPluginConfiguration.get(_strPluginName, {})

    def __setitem__(self, _strPluginName, plugin_config={}):
        """
        edConfig["myPlugin"]= {"timeout":5}

        @param _strPluginName: name of the plugin as a string
        @param plugin_config: configuration of a whole plugin as a dict
        """
        with self.locked():
            self._dictPluginConfiguration[_strPluginName] = plugin_config

    def __len__(self):
        return len(self._dictPluginConfiguration)

    def getPluginListSize(self):
        """
        Returns the number of plugins configured
        """
        return len(self._dictPluginConfiguration)

################################################################################
# #    Deprecation zone
################################################################################

#    @deprecated
    def getXSConfigurationItem(self, _strPluginName):
        "Method offering compatibility with XML structure: deprecated !!!"
        config = None
        if _strPluginName  in self._dictPluginConfiguration:
            config = self._dictPluginConfiguration[_strPluginName]
        else: # Try to load "project" configuration
            config = self.get(_strPluginName)
        if config is not None:
            return  XSPluginItem(name=_strPluginName,
                             XSParamList=XSParamList([XSParamItem(name=i, value=str(config[i])) for i in config]))


#    @deprecated
    def setXSConfigurationItem(self, _xsPluginItem):
        "Compatibility with XML structure: deprecated"
        if _xsPluginItem is not None:
            if _xsPluginItem.name is not None:
                strPluginName = _xsPluginItem.name
                plugin_conf = {}
                paramList = _xsPluginItem.getXSParamList()
                if paramList:
                    for paramItem in paramList.getXSParamItem():
                        plugin_conf[paramItem.name] = bestType(paramItem.value)
                if strPluginName in self._dictPluginConfiguration.keys():
                    self.DEBUG("Replacing configuration for plugin %s" % strPluginName)
                else:
                    self.DEBUG("Setting configuration for plugin %s" % strPluginName)
                with self.locked():
                    self._dictPluginConfiguration[strPluginName] = plugin_conf


    def getStringValue(self, _strPluginName, _strConfigurationName):
        "Get the configuration for one plugin and one config parameter, as a string"
        config = None
        if _strPluginName in self._dictPluginConfiguration:
            config = self._dictPluginConfiguration[_strPluginName]
        else: # Try to load "project" configuration
            config = self.get(_strPluginName)
        if (config is not None) and (_strConfigurationName in config):
            return str(config[_strConfigurationName])



#    @deprecated
    @staticmethod
    def getParamItem(_xsPluginItem, _pyStrParamName):
        """
        Returns the corresponding 'paramItem' for a given plugin name
        -> Deprecated
        """
        xsParamList = _xsPluginItem.getXSParamList()
        xsParamItemReturn = None

        if (xsParamList != None):
            xsParamItems = xsParamList.getXSParamItem()
            for xsParamItem in xsParamItems:
                if (xsParamItem.getName() == _pyStrParamName):
                    xsParamItemReturn = xsParamItem
                    break
        return xsParamItemReturn

#    @deprecated
    @classmethod
    def getStringParamValue(cls, _xsPluginItem, _pyStrParamName):
        """
        Returns the parameter value in a string format
        -> Deprecated
        """
        strParamValue = None
        xsParamItem = cls.getParamItem(_xsPluginItem, _pyStrParamName)
        if xsParamItem is not None:
            strParamValue = xsParamItem.getValue()
        return strParamValue
    

#    @deprecated
    @classmethod
    def getIntegerParamValue(cls, _xsPluginItem, _pyStrParamName):
        """
        Returns the parameter value in a integer format
        -> Deprecated
        """
        strParamValue = cls.getStringParamValue(_xsPluginItem, _pyStrParamName)
        try:
            return int(strParamValue)
        except TypeError:
            return
        except ValueError:
            EDVerbose.ERROR("invalid literal for int(), got %s" % strParamValue)




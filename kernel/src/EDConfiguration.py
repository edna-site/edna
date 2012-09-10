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


__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This class handles the EDNA configuration XML files.
"""

import os

from EDLogging import EDLogging
from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDThreading            import Semaphore

from XSDataCommon import XSConfiguration

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


    def __init__(self, _strXMLFileName = None):
        """"Set  up semaphore for thread safeness and dictionary for config files"""
        EDLogging.__init__(self)
        self.__semaphore = Semaphore()
        self.__dictXSConfiguration = {}
        if _strXMLFileName is not None:
            self.addConfigurationFile(_strXMLFileName)
            
    
    def addConfigurationFile(self, _strXMLFileName):
        """Loads an XML config file into the dictionary if not already loaded"""
        with self.__semaphore:
            strXMLFileName = os.path.abspath(_strXMLFileName)
            if not strXMLFileName in self.__dictXSConfiguration.keys():
                self.DEBUG("EDConfiguration.addConfigurationFile: Parsing file %s" % strXMLFileName)
                strXMLConfiguration = EDUtilsFile.readFileAndParseVariables(strXMLFileName)
                xsConfiguration = XSConfiguration.parseString(strXMLConfiguration)
                self.__dictXSConfiguration[strXMLFileName] = xsConfiguration
            else:
                self.DEBUG("EDConfiguration.addConfigurationFile: File %s already parsed, in cache" % strXMLFileName)
        
    
    


#    def __init__(self, _strXMLFileName):
#        """
#        The Constructor initializes the files (xsd and xml) objects
#        The Configuration will be fully constructed after the load method
#        """
#        # Configuration File
#        self.__strXmlFileName = os.path.abspath(_strXMLFileName)
#        # XSConfiguration object
#        self.__xsConfiguration = None
#        self.__bLoaded = False


#    def load(self):
#        """
#        Loads a configuration file. Any environment variables present
#        in the XML file are substituted.
#        """
#        EDVerbose.DEBUG("EDConfiguration.load file %s" % self.__strXmlFileName)
#        with EDConfiguration.__semaphore:
#            if not self.__strXmlFileName in EDConfiguration.__dictXSConfiguration.keys():
#                EDVerbose.DEBUG("EDConfiguration.load: importing %s configuration file" % self.__strXmlFileName)
#                strXMLConfiguration = EDUtilsFile.readFileAndParseVariables(self.__strXmlFileName)
#                EDConfiguration.__dictXSConfiguration[self.__strXmlFileName] = strXMLConfiguration
#            else:
#                EDVerbose.DEBUG("EDConfiguration.load: using cached configuration file %s" % self.__strXmlFileName)
#                strXMLConfiguration = EDConfiguration.__dictXSConfiguration[self.__strXmlFileName]
#            self.__xsConfiguration = XSConfiguration.parseString(strXMLConfiguration)
#            self.__bLoaded = True
#
#
#    def isLoaded(self):
#        """
#        Returns true if the configuration file has been loaded
#        """
#        return self.__bLoaded
#
#
#    def getXmlFileName(self):
#        """
#        Returns the absolute path of the XML file
#        """
#        return self.__strXmlFileName
#
#
#    def getXSConfiguration(self):
#        """
#        Gets the auto-generated XSConfiguration module
#        """
#        return self.__xsConfiguration
#
#
#    def getPluginList(self):
#        """
#        Returns an XSPluginList object that encapsulates a list of XSPluginItem
#        """
#        pluginList = self.__xsConfiguration.getXSPluginList()
#        return pluginList
#
#
#    def getPluginItem(self, _edStrPluginName):
#        """
#        Returns a particular XSPluginItem given its name
#        """
#        xsPluginList = self.__xsConfiguration.getXSPluginList()
#        xsPluginItems = xsPluginList.getXSPluginItem()
#        pluginItem = None
#        for xsPluginItem in xsPluginItems:
#            if (xsPluginItem.getName() == _edStrPluginName):
#                pluginItem = xsPluginItem
#        return pluginItem
#
#
#    def getOptionItem(_xsPluginItem, _pyStrOptionName):
#        """
#        Returns a XSOptionItem given an option name
#        """
#        xsOptionList = _xsPluginItem.getXSOptionList()
#        xsOptionItems = xsOptionList.getXSOptionItem()
#        optionItem = None
#        for xsOptionItem in xsOptionItems:
#            if (xsOptionItem.getName() == _pyStrOptionName):
#                optionItem = xsOptionItem
#        return optionItem
#    getOptionItem = staticmethod(getOptionItem)
#
#
#    def getParamItem(_xsPluginItem, _pyStrParamName):
#        """
#        Returns a XSParamItem given a param name
#        """
#        xsParamList = _xsPluginItem.getXSParamList()
#        xsParamItems = xsParamList.getXSParamItem()
#        paramItem = None
#        for xsParamItem in xsParamItems:
#            if (xsParamItem.getName() == _pyStrParamName):
#                paramItem = xsParamItem
#        return paramItem
#    getParamItem = staticmethod(getParamItem)
#
#
#    def getStringParamValue(_xsPluginItem, _pyStrParamName):
#        """
#        Returns the parameter value in a string format
#        """
#        xsParamList = _xsPluginItem.getXSParamList()
#        paramValue = None
#
#        if (xsParamList != None):
#            xsParamItems = xsParamList.getXSParamItem()
#            for xsParamItem in xsParamItems:
#                if (xsParamItem.getName() == _pyStrParamName):
#                    paramValue = xsParamItem.getValue()
#        return paramValue
#    getStringParamValue = staticmethod(getStringParamValue)
#
#
#    def getIntegerParamValue(_xsPluginItem, _pyStrParamName):
#        """
#        Returns the parameter value in a integer format
#        """
#        strParamValue = EDConfiguration.getStringParamValue(_xsPluginItem, _pyStrParamName)
#        intParamValue = None
#        if strParamValue is not None:
#            intParamValue = int(strParamValue)
#        return intParamValue
#    getIntegerParamValue = staticmethod(getIntegerParamValue)
#
#
#    def getPluginListSize(self):
#        """
#        Returns the size of the XSPluginItem list
#        """
#        iSize = len(self.getPluginList().getXSPluginItem())
#        return iSize
#
##    @classmethod
##    def setConfiguration(cls, _edConfiguration):
##        """
##        """
##        EDVerbose.DEBUG("EDConfiguration.setConfiguration")
##        with cls.__semaphore:
##            if (_edConfiguration == None):
##                EDVerbose.warning("EDConfiguration.setConfiguration: Configuration is None!")
##            else:
##                cls.__edConfiguration = _edConfiguration
#
#
#    @classmethod
#    def getApplicationPluginConfiguration(cls, _pluginName):
#        """
#        """
#        EDVerbose.DEBUG("EDConfiguration.getApplicationPluginConfiguration")
#        with cls.__semaphore:
#            pluginConfiguration = None
#            if (cls.__edConfiguration != None):
#                pluginConfiguration = EDConfiguration.__edConfiguration.getPluginItem(_pluginName)
#            if (pluginConfiguration is None):
#                EDVerbose.DEBUG("EDConfiguration.getApplicationPluginConfiguration: No application configuration found for %s " % _pluginName)
#            else:
#                EDVerbose.DEBUG("EDConfiguration.getApplicationPluginConfiguration: Reading %s configuration from %s" % (\
#                                 _pluginName, \
#                                 cls.__edConfiguration.getXmlFileName()))
#        return pluginConfiguration
#
#
#    @classmethod
#    def getProjectPluginConfiguration(cls, _pluginName):
#        """
#        """
#        EDVerbose.DEBUG("EDConfiguration.getProjectPluginConfiguration")
#        pluginConfiguration = None
#        strPathToProjectConfigurationFile = EDFactoryPluginStatic.getPathToProjectConfigurationFile(_pluginName)
#        with cls.__semaphore:
#            if (strPathToProjectConfigurationFile is not None):
#                edConfigurationProject = EDConfiguration(strPathToProjectConfigurationFile)
#                edConfigurationProject.load()
#                if (edConfigurationProject is not None):
#                    pluginConfiguration = edConfigurationProject.getPluginItem(_pluginName)
#            if (pluginConfiguration is None):
#                EDVerbose.DEBUG("EDConfiguration.getProjectPluginConfiguration: No project configuration found for %s " % _pluginName)
#            else:
#                EDVerbose.DEBUG("EDConfiguration.getProjectPluginConfiguration: Reading %s configuration from %s" % (\
#                                 _pluginName, \
#                                 strPathToProjectConfigurationFile))
#        return pluginConfiguration
#
#
#    @classmethod
#    def loadConfiguration(cls):
#        """
#        Loads the configuration file if not already loaded
#        """
#        if((cls.__edConfiguration != None) & (cls.__edConfiguration.isLoaded() == False)):
#            EDVerbose.DEBUG("EDConfiguration.loadConfiguration: Loading Configuration File...")
#            cls.__edConfiguration.load()
#
#
#    @classmethod
#    def getConfigurationHome(cls, _strPluginName):
#        """
#        Returns the configuration directory path for a given test module
#        """
#        strModuleLocation = EDFactoryPluginStatic.getFactoryPlugin().getModuleLocation(_strPluginName)
#        strConfigurationHome = EDUtilsPath.appendListOfPaths(strModuleLocation, [ "..", "..", "..", "conf" ])
#        return strConfigurationHome




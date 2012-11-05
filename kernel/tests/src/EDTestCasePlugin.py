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

"""
Test case for both unit tests and execution tests for EDNA plugins 

It is especially in charge of 
 - downloading large files not contained in the SVN repository for the tests (typically images coming from CCD, 8 or 16 Megabytes each)
 - doing the replacement or variable like ${EDNA_HOME} in the XML strings
"""


__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120131"

import sys, os, threading, urllib2

from EDVerbose             import EDVerbose
from EDUtilsPath           import EDUtilsPath
from EDTestCase            import EDTestCase
from EDUtilsTest           import EDUtilsTest
from EDUtilsFile           import EDUtilsFile
from EDConfigurationStatic import EDConfigurationStatic, EDConfiguration
from EDFactoryPlugin       import EDFactoryPlugin
from EDDecorator           import deprecated

iMAX_DOWNLOAD_TIME = 60


class EDTestCasePlugin(EDTestCase):
    """
    This is the main test class to test a plugin (Unit and Execution)
    """
    URL_EDNA_SITE = "http://www.edna-site.org/data/tests/images"

    def __init__(self, _strPluginName, _strPluginDir=None, _strTestName=None):
        """
        Initialize the test case by determining the paths to the plugin home and plugin test directories.
        """
        EDTestCase.__init__(self, _strTestName)
        self._edPlugin = None
        self._strPluginName = _strPluginName
        self._strPluginHome = EDUtilsTest.getFactoryPluginTest().getModuleLocation(_strPluginName)
        self._strPluginTestsDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        self._listRequiredConfigurationPluginNames = []
        self._strConfigurationFile = None


    def preProcess(self):
        # Check if the plugin to be tested requires configuration
        edPlugin = self.createPlugin()
        if edPlugin is None:
            strErr = "Unable to create plugin %s: Check the corresponding module" % self.getPluginName()
            EDVerbose.ERROR(strErr)
            raise RuntimeError(strErr)
        if edPlugin.isRequiredToHaveConfiguration():
            self._listRequiredConfigurationPluginNames.append(self.getPluginName())
        # Check if the required plugin parameters are available
        for strPluginName in self._listRequiredConfigurationPluginNames:
            if self.getPluginConfig(strPluginName) is None:
                EDVerbose.DEBUG("EDTestCasePlugin.preProcess: plugin configuration NOT found for plugin %s" % strPluginName)
                self.setReasonForNotBeingExectuted("Missing configuration for %s" % strPluginName)
            else:
                EDVerbose.DEBUG("EDTestCasePlugin.preProcess: plugin configuration found for plugin %s" % strPluginName)


    def getPluginConfig(self, _strPluginName=None):
        # Load the configuration file if provided
        dictConfig = None
        if _strPluginName is None:
            strPluginName = self.getPluginName()
        else:
            strPluginName = _strPluginName
        if self._strConfigurationFile is not None:
            edConfig = EDConfiguration(self._strConfigurationFile)
            dictConfig = edConfig.get(strPluginName)
        else:
            dictConfig = EDConfigurationStatic.get(strPluginName)
        return dictConfig

    @deprecated
    def getPluginConfiguration(self, _strPluginName=None):
        # Load the configuration file if provided
        xsConfiguration = None
        if _strPluginName is None:
            strPluginName = self.getPluginName()
        else:
            strPluginName = _strPluginName
        if self._strConfigurationFile is not None:
            edConfig = EDConfiguration(self._strConfigurationFile)
            xsConfiguration = edConfig.getXSConfigurationItem(strPluginName)
        else:
            xsConfiguration = EDConfigurationStatic.getXSConfigurationItem(strPluginName)
        return xsConfiguration




    def setConfigurationFile(self, _strConfigurationFile):
        """
        Sets the configuration file
        """
        self._strConfigurationFile = _strConfigurationFile


    def getConfigurationFile(self):
        """
        Returns the configuration file
        """
        return self._strConfigurationFile



    def setRequiredPluginConfiguration(self, _strPluginName=None):
        if _strPluginName is None:
            self._listRequiredConfigurationPluginNames.append(self._strPluginName)
        else:
            self._listRequiredConfigurationPluginNames.append(_strPluginName)


    def createPlugin(self):
        """
        Creates a plugin instance
        """
        edPlugin = None
        exceptionObject = None
        try:
            edFactoryPlugin = EDFactoryPlugin()
            edPlugin = edFactoryPlugin.loadPlugin(self.getPluginName())
        except ImportError, exceptionObject:
            strWarningMessage = "Could not create the plugin: %s, reason: %s" % (self.getPluginName(), exceptionObject)
            EDVerbose.WARNING(strWarningMessage)
        if edPlugin is None:
            if exceptionObject is None:
                EDVerbose.error("EDTestCasePlugin.createPlugin: Could not create plugin: " + self.getPluginName())
        return edPlugin


    def getPlugin(self):
        """
        Returns the plugin instance
        """
        return self._edPlugin
    plugin = property(getPlugin, doc="read-only only property")


    def getPluginName(self):
        """
        Returns the plugin name
        """
        return self._strPluginName
    pluginName = property(getPluginName, doc="read-only property")


    def getPluginHome(self):
        """
        Returns the plugin home directory
        """
        return self._strPluginHome
    pluginHome = property(getPluginHome, doc="read-only property")


    def getPluginTestsDataHome(self):
        """
        Returns the plugin test data home directory
        """
        return self._strPluginTestsDataHome


    def setPluginTestsDataHome(self, _strPluginTestsDataHome):
        """
        Sets the plugin test data home directory
        """
        self._strPluginTestsDataHome = _strPluginTestsDataHome
    pluginTestDataHome = property(getPluginTestsDataHome, setPluginTestsDataHome, "pluginTestDataHome is the data directory in the plugin's tests")


    def loadTestImage(self, _listImageFileName):
        """
        This method checks the presence of all the images in the list of image file names
        in the $EDNA_HOME/tests/data/images directory. If one image is not present
        this method tries to download it from http://www.edna-site.org/data/tests/images
        """
        if not os.path.isdir(EDUtilsPath.EDNA_TESTIMAGES):
            os.makedirs(EDUtilsPath.EDNA_TESTIMAGES)
        for strImageName in _listImageFileName:
            strImagePath = os.path.join(EDUtilsPath.EDNA_TESTIMAGES, strImageName)
            if(not os.path.exists(strImagePath)):
                EDVerbose.unitTest("Trying to download image %s, timeout set to %d s" % (strImagePath, iMAX_DOWNLOAD_TIME))
                if os.environ.has_key("http_proxy"):
                    dictProxies = {'http': os.environ["http_proxy"]}
                    proxy_handler = urllib2.ProxyHandler(dictProxies)
                    opener = urllib2.build_opener(proxy_handler).open
                else:
                    opener = urllib2.urlopen

# Nota: since python2.6 there is a timeout in the urllib2                    
                timer = threading.Timer(iMAX_DOWNLOAD_TIME + 1, timeoutDuringDownload)
                timer.start()
                if sys.version > (2, 6):
                    data = opener("%s/%s" % (self.URL_EDNA_SITE, strImageName), data=None, timeout=iMAX_DOWNLOAD_TIME).read()
                else:
                    data = opener("%s/%s" % (self.URL_EDNA_SITE, strImageName), data=None).read()
                timer.cancel()

                try:
                    open(strImagePath, "wb").write(data)
                except IOError:
                    raise IOError, "unable to write downloaded data to disk at %s" % strImagePath

                if os.path.exists(strImagePath):
                    EDVerbose.unitTest("Image %s successfully downloaded." % strImagePath)
                else:
                    raise RuntimeError, "Could not automatically download test images %r! \n \
                                         If you are behind a firewall, please set the environment variable http_proxy. \n \
                                         Otherwise please try to download the images manually from \n \
                                         http://www.edna-site.org/data/tests/images" % _listImageFileName

    def getDictReplace(self):
        dictReplace = EDUtilsPath.getDictOfPaths()
        dictReplace["${EDNA_PLUGIN_TESTS_DATA_HOME}"] = self._strPluginTestsDataHome
        if self._edPlugin is not None:
            workDir = self._edPlugin.getWorkingDirectory()
            if workDir is not None:
                dictReplace["${EDNA_WORKING_DIR}"] = workDir
        return dictReplace
    dictReplace = property(getDictReplace, doc="Read-only property")

    def readAndParseFile(self, _strFileName):
        """
        Reads a file and parses potential existing environment variables such as:
         - EDNA_TESTS_DATA_HOME
         - EDNA_PLUGIN_TESTS_DATA_HOME
         - EDNA_HOME
         - USER
         - TMPDIR

        All those key are defined in a class dictionary

        Returns the content of this file as a string
        """
        return  str(EDUtilsFile.readFileAndParseVariables(_strFileName, self.dictReplace))



def timeoutDuringDownload():
    """
    Function called after a timeout in the download part ... just raise an Exception. 
    """
    raise RuntimeError, "Could not automatically download test images ! \n \
                         If you are behind a firewall, please set the environment variable http_proxy. \n \
                         Otherwise please try to download the images manually from \n \
                         http://www.edna-site.org/data/tests/images"

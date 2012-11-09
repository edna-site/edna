#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jerome Kieffer
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
__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, time
from EDThreading            import Semaphore
from EDCommandLine          import EDCommandLine
from EDVerbose              import EDVerbose
from EDConfigurationStatic  import EDConfigurationStatic
from EDMessage              import EDMessage
from EDUtilsPath            import EDUtilsPath
from EDUtilsFile            import EDUtilsFile
from EDFactoryPluginStatic  import EDFactoryPluginStatic


class EDApplication(object):
    """
    This is the main EDNA application class. This class can be sub-classed for any specific application need.
    An EDNA application is able to launch an entry point plugin. It accepts the following parameter:
    --execute    : name of the plugin to be executed 
    --inputFile  : related plugin data (xml input data file name)
    --outputFile : related plugin result (xml output data file name)
    --conf       : configuration file name
    --basedir    : where the application working directory should go 
    --DEBUG or --debug : turns on debugging   
    -v or --version : Displays the application name and version
    --verbose    : Turns on verbose mode
    --no-log     : Turns off logging
    -h or --help : Prints out an usage message
    """

    CONFIGURATION_PARAM_LABEL = "--conf"
    PLUGIN_PARAM_LABEL = "--execute"
    DATASET_PARAM_LABEL = "--inputFile"
    OUTPUT_PARAM_LABEL = "--outputFile"
    DATASET_BASE_DIRECTORY = "--basedir"
    DEBUG_PARAM_LABEL_1 = "--DEBUG"
    DEBUG_PARAM_LABEL_2 = "--debug"
    VERSION_PARAM_LABEL_1 = "-v"
    VERSION_PARAM_LABEL_2 = "--version"
    VERBOSE_MODE_LABEL = "--verbose"
    NO_LOG_LABEL = "--no-log"
    HELP_LABEL_1 = "-h"
    HELP_LABEL_2 = "--help"

    __edConfiguration = None
    __edFactoryPlugin = None
    __semaphore = Semaphore()


    def __init__(self, _strName="EDApplication", \
                  _strVersion="1.0.1", \
                  _strPluginName=None, \
                  _strConfigurationFileName=None, \
                  _strDataInputFilePath=None, \
                  _edLogFile=None, \
                  _strBaseDir=None, \
                  _strWorkingDir=None, \
                  _strDataOutputFilePath=None):
        self.__strName = _strName
        self.__strVersion = _strVersion
        self.__strPluginName = _strPluginName
        self.__strConfigurationFileName = _strConfigurationFileName
        self.__strDataInputFilePath = _strDataInputFilePath
        self.__strDataOutputFilePath = _strDataOutputFilePath
        self.__edLogFile = _edLogFile
        self.__strBaseDir = _strBaseDir
        self.__strWorkingDir = _strWorkingDir
        self.__strFullApplicationWorkingDirectory = None
        self.__strXMLData = None
        self.__listErrorMessages = []
        self.__listWarningMessages = []
        self.__xsDataOutput = None
        self.__edObtainedOutputDataFile = None
        self.__strDataOutputFilePath = None
        self.__edPlugin = None
        self.__edCommandLine = EDCommandLine(sys.argv)
        self.__strApplicationInstanceName = self.__strName + "_" + time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        self.__strLogFileName = self.__strApplicationInstanceName + ".log"
        self.__bIsFailure = False
        self.__strCurrentWorkingDirectory = os.getcwd()
        self.__strConfigurationHome = None
        self.__strPathToLogFile = None


    def execute(self):
        """
        This is the main execute method which executes preProcess, process and postProcess.
        """
        self.preProcess()
        self.process()
        self.postProcess()


    def preProcess(self):
        """
        Creates the application working directory (log dir)
        Initializes the configuration
        retrieves the plugin xml data to be passed to the plugin
        """
        EDVerbose.DEBUG("EDApplication.preProcess")
        self.processCommandline()
        if (not self.__bIsFailure):
            # Check that the plugin can be located
            strPluginLocation = EDFactoryPluginStatic.getFactoryPlugin().getModuleLocation(self.__strPluginName)
            if (strPluginLocation is None):
                EDVerbose.error("Plugin  %s cannot be loaded!" % self.__strPluginName)
                self.__bIsFailure = True
            # Check that the input file can be read
            if (self.getDataInputFilePath() is not None) and (not os.path.exists(self.__strDataInputFilePath)):
                EDVerbose.error("Input XML file not found : %s" % self.__strDataInputFilePath)
                self.__bIsFailure = True
            # Check that the output file can be created
            if (self.__strDataOutputFilePath is not None):
                strOutputDirectory = os.path.dirname(self.__strDataOutputFilePath)
                if (strOutputDirectory is None or strOutputDirectory == ""):
                    strOutputDirectory = os.getcwd()
                    self.__strDataOutputFilePath = os.path.join(strOutputDirectory, self.__strDataOutputFilePath)
                if (not os.access(strOutputDirectory, os.W_OK)):
                    EDVerbose.error("Output directory not writable: %s" % strOutputDirectory)
                    self.__bIsFailure = True
                elif (os.path.exists(self.__strDataOutputFilePath)):
                    if (not os.access(self.__strDataOutputFilePath, os.W_OK)):
                        EDVerbose.error("Output file not writable: %s" % self.__strDataOutputFilePath)
                        self.__bIsFailure = True
        if (not self.__bIsFailure):
            EDVerbose.DEBUG("EDApplication.PLUGIN_PARAM_LABEL: " + EDApplication.PLUGIN_PARAM_LABEL)

            if self.__strConfigurationFileName is not None:
                # Load the configuration file
                if (os.path.exists(self.__strConfigurationFileName)):
                    EDVerbose.screen("Loading Configuration file: %s" % self.__strConfigurationFileName)
                    EDConfigurationStatic.addConfigurationFile(self.__strConfigurationFileName, _bReplace=True)
                else:
                    EDVerbose.warning("Cannot find configuration file: %s" % self.__strConfigurationFileName)
            pyDictionary = {}
            pyDictionary[ "${EDNA_HOME}" ] = EDUtilsPath.getEdnaHome()
            if self.getDataInputFilePath() is not None:
                self.__strXMLData = EDUtilsFile.readFileAndParseVariables(self.getDataInputFilePath(), pyDictionary)
            # Create the application working directory    
            if(self.__strWorkingDir is None):
                self.__strWorkingDir = self.__strApplicationInstanceName
            self.createApplicationWorkingDirectory()


    def process(self):
        """
        Calls the Plugin to be executed
        """
        if (not self.__bIsFailure):
            self.__edPlugin = EDFactoryPluginStatic.loadPlugin(self.__strPluginName)
            if(self.__edPlugin is not None):
                self.__edPlugin.setBaseDirectory(self.__strFullApplicationWorkingDirectory)
                self.__edPlugin.setBaseName(self.__strPluginName)
                self.__edPlugin.setDataInput(self.__strXMLData)
                self.__edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                self.__edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplication.process: Executing " + self.__strPluginName)
                self.__edPlugin.execute()
                self.__edPlugin.synchronize()
            else:
                EDVerbose.error(EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDApplication.process', self.__strPluginName))
                self.__bIsFailure = True




    def processCommandline(self):
        """
        This method is intended to be overridden by applications who
        would like to implement their own command line handling.
        
        This default method implements the following workflow:
            - Check for debug, verbose and log file command line options
        
        """
        EDVerbose.DEBUG("EDApplication.execute")
        EDVerbose.log(self.__edCommandLine.getCommandLine())
        self.processCommandLineDebugVerboseLogFile()
        # Determine the base directory
        if(self.__strBaseDir is None):
            self.processCommandLineBaseDirectory()
        # Set the name of the log file
        self.__strPathToLogFile = os.path.abspath(os.path.join(self.__strBaseDir, self.__strLogFileName))
        EDVerbose.setLogFileName(self.__strPathToLogFile)
        self.processCommandLineHelp()
        if (not self.__bIsFailure):
            self.processCommandLineVersion()
        if (not self.__bIsFailure):
            # Name of the plugin to be executed        
            if (self.__strPluginName is None):
                self.processCommandLinePluginName()
            # Path to the input XML file
            if (self.__strDataInputFilePath is None):
                self.processCommandLineInputFilePath()
            # Path to the output XML file
            if(self.__strDataOutputFilePath is None):
                self.processCommandLineOutputFilePath()
            if (self.__bIsFailure):
                self.usage()
        if (not self.__bIsFailure):
            # If strConfigurationFileName is None, this means that it has not been given to the constructor\
            # It has been given by the command line\
            if(self.__strConfigurationFileName is None):
                self.__strConfigurationFileName = self.getCommandLineArgument(EDApplication.CONFIGURATION_PARAM_LABEL)



    def processCommandLineDebugVerboseLogFile(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineDebugVerboseLogFile")
        EDVerbose.setVerboseOff()
        # Check if no log file
        if (self.__edCommandLine.existCommand(EDApplication.NO_LOG_LABEL)):
            EDVerbose.setLogFileOff()
            EDVerbose.DEBUG("Log file output switched off")
        # Check if debug mode
        if (self.__edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_1) or
            self.__edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_2)):
            EDVerbose.setVerboseDebugOn()
            EDVerbose.DEBUG("Debug Mode [ON]")
        # Check if verbose
        if (self.__edCommandLine.existCommand(EDApplication.VERBOSE_MODE_LABEL)):
            EDVerbose.setVerboseOn()


    def processCommandLineHelp(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineHelp")
        if (self.__edCommandLine.existCommand(EDApplication.HELP_LABEL_1)
            or self.__edCommandLine.existCommand(EDApplication.HELP_LABEL_2)):
            EDVerbose.setVerboseOn()
            self.usage()
            self.__bIsFailure = True


    def processCommandLineVersion(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineVersion")
        if (self.__edCommandLine.existCommand(EDApplication.VERSION_PARAM_LABEL_1) or
            self.__edCommandLine.existCommand(EDApplication.VERSION_PARAM_LABEL_2)):
            EDVerbose.setVerboseOn()
            EDVerbose.screen("%s version %s" % (self.__strName, self.__strVersion))
            self.__bIsFailure = True



    def processCommandLinePluginName(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLinePluginName")
        if (not self.__edCommandLine.existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
            EDVerbose.error("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
            self.__bIsFailure = True
        else:
            self.__strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self.__strPluginName))


    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineInputFilePath")
        if (not self.__edCommandLine.existCommand(EDApplication.DATASET_PARAM_LABEL)):
            EDVerbose.error("No %s command line argument found!" % EDApplication.DATASET_PARAM_LABEL)
            self.__bIsFailure = True
        else:
            self.__strDataInputFilePath = self.getCommandLineArgument(EDApplication.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.initApplication : %s = %s" % (EDApplication.DATASET_PARAM_LABEL, self.__strDataInputFilePath))


    def processCommandLineOutputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineOutputFilePath")
        if (not self.__edCommandLine.existCommand(EDApplication.OUTPUT_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found" % EDApplication.OUTPUT_PARAM_LABEL)
        else:
            self.__strDataOutputFilePath = self.getCommandLineArgument(EDApplication.OUTPUT_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.initApplication : %s = %s" % (EDApplication.OUTPUT_PARAM_LABEL, self.__strDataOutputFilePath))


    def processCommandLineBaseDirectory(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineBaseDirectory")
        self.__strBaseDir = self.getCommandLineArgument(EDApplication.DATASET_BASE_DIRECTORY)
        if(self.__strBaseDir is None):
            self.__strBaseDir = os.getcwd()
            EDVerbose.DEBUG("Base directory set to current working directory = %s" % (self.__strBaseDir))
        else:
            EDVerbose.DEBUG("%s = %s" % (EDApplication.DATASET_BASE_DIRECTORY, self.__strBaseDir))





    def postProcess(self):
        """
        """
        # Restore the current working directory 
        os.chdir(self.__strCurrentWorkingDirectory)


    @classmethod
    def usage(cls):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Name of the plugin to be executed" % (cls.PLUGIN_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Path to the XML input file" % (cls.DATASET_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" Additional options available:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Path to the file wich will contain the XML output" % (cls.OUTPUT_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Base directory, i.e. working directory for the application" % (cls.DATASET_BASE_DIRECTORY))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Verbose mode" % (cls.VERBOSE_MODE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : XSConfiguration file" % (cls.CONFIGURATION_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (cls.VERSION_PARAM_LABEL_1 + " or " + cls.VERSION_PARAM_LABEL_2))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (cls.DEBUG_PARAM_LABEL_1 + " or " + cls.DEBUG_PARAM_LABEL_2))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : No log file" % (cls.NO_LOG_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : This help message" % (cls.HELP_LABEL_1 + " or " + cls.HELP_LABEL_2))
        EDVerbose.screen("")


    @classmethod
    def getFactoryPlugin(cls):
        EDVerbose.WARNING("the use of EDclsetFactoryPlugin is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        return EDFactoryPluginStatic.getFactoryPlugin


    @classmethod
    def loadPlugin(cls, _strPluginName):
        EDVerbose.WARNING("The use of EDApplication.loadPlugin is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        return EDFactoryPluginStatic.loadPlugin(_strPluginName)


    @classmethod
    def loadModule(cls, _strModuleName):
        EDVerbose.WARNING("The use of EDApplication.loadModule is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        EDFactoryPluginStatic.loadModule(_strModuleName)


    def getDataInputFilePath(self):
        return self.__strDataInputFilePath


    def getBaseDir(self):
        """
        Getter for base directory
        @return: path of the base directory
        @rtype: string
        """
        return self.__strBaseDir


    def createApplicationWorkingDirectory(self):
        """
        Created the working directory of the application (<date>-<application name>)
        First tries to retrieve the base dir from --basedir option or related parameter from constructor
        Otherwise tries to retrieve it from EDNA_BASE_DIRECTORY environment variable
        Otherwise put the base dir as the current directory
        """
        EDVerbose.DEBUG("EDApplication.createApplicationWorkingDirectory")
        strBaseDirectory = self.getBaseDir()
        strDateTime = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        self.__strFullApplicationWorkingDirectory = os.path.join(strBaseDirectory, self.__strWorkingDir)
        # Check that a folder / file with the same name already exists
        if(os.path.exists(self.__strFullApplicationWorkingDirectory) or \
            os.path.exists(self.__strFullApplicationWorkingDirectory)):
            # It does exist so we have to modify the name of the working directory
            iIndex = 1
            bContinueFlag = True
            while (bContinueFlag):
                self.__strFullApplicationWorkingDirectory = os.path.join(strBaseDirectory,
                                                                                        "%s_%d" % \
                                                                                        (strDateTime, \
                                                                                          iIndex))
                if(os.path.isdir(self.__strFullApplicationWorkingDirectory) or \
                    os.path.exists(self.__strFullApplicationWorkingDirectory)):
                    iIndex += 1
                else:
                    bContinueFlag = False
        # Make the directory
        os.mkdir(self.__strFullApplicationWorkingDirectory)
        # Change it to be the current working directory
        os.chdir(self.__strFullApplicationWorkingDirectory)


    def getFullApplicationWorkingDirectory(self):
        return self.__strFullApplicationWorkingDirectory

    def getCurrentWorkingDirectory(self):
        return self.__strCurrentWorkingDirectory


    def doSuccessActionPlugin(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin")
        # Print the potential Warnings and Errors
        self.__listWarningMessages = _edPlugin.getListOfWarningMessages()
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin: Plugin %s Successful with : %i Warnings " % (_edPlugin.getPluginName(), len(self.__listWarningMessages)))
        for warningMessage in self.__listWarningMessages:
            EDVerbose.screen(warningMessage)
        self.__listErrorMessages = _edPlugin.getListOfErrorMessages()
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin: Plugin %s Successful with : %i Errors" % (_edPlugin.getPluginName(), len(self.__listErrorMessages)))
        for errorMessage in self.__listErrorMessages:
            EDVerbose.error(errorMessage)
        if (_edPlugin.hasDataOutput()):
            xsDataOutput = _edPlugin.getDataOutput()
            if (xsDataOutput is not None and self.__strDataOutputFilePath is not None):
                xsDataOutput.exportToFile(self.__strDataOutputFilePath)
            if (xsDataOutput is not None and self.__edObtainedOutputDataFile is not None):
                xsDataOutput.exportToFile(self.__edObtainedOutputDataFile)


    def doFailureActionPlugin(self, _edPlugin):
        EDVerbose.DEBUG("EDApplication.doFailureActionPlugin")

        # Print the potential Warnings and Errors
        EDVerbose.DEBUG("EDApplication.doFailureActionPlugin: Plugin %s failed" % _edPlugin.getClassName())
        self.__listWarningMessages = _edPlugin.getListOfWarningMessages()
        for warningMessage in self.__listWarningMessages:
            EDVerbose.screen(warningMessage)

        self.__listErrorMessages = _edPlugin.getListOfErrorMessages()
        for errorMessage in self.__listErrorMessages:
            EDVerbose.screen(errorMessage)
        if (_edPlugin.hasDataOutput()):
            xsDataOutput = _edPlugin.getDataOutput()
            if (xsDataOutput is not None and self.__strDataOutputFilePath is not None):
                xsDataOutput.exportToFile(self.__strDataOutputFilePath)
            if (xsDataOutput is not None and self.__edObtainedOutputDataFile is not None):
                xsDataOutput.exportToFile(self.__edObtainedOutputDataFile)


    def getPlugin(self):
        return self.__edPlugin


    def getPluginOutputData(self):
        return self.__xsDataOutput


    def getWarningMessages(self):
        return self.__listWarningMessages


    def getErrorMessages(self):
        return self.__listErrorMessages


    def getEdCommandLine(self):
        return self.__edCommandLine


    def getCommandLine(self):
        return self.__edCommandLine.getCommandLine()


    def getCommandLineArguments(self):
        with self.__class__.__semaphore:
            edCommandLine = self.__edCommandLine.getCommandLine()
        return edCommandLine

    def getCommandLineArgument(self, _strKey):
        with self.__class__.__semaphore:
            strCommandLineArgument = self.__edCommandLine.getArgument(_strKey)
        return strCommandLineArgument

    @classmethod
    def synchronizeOn(cls):
        """
        Lock the whole class
        """
        cls.__semaphore.acquire()


    @classmethod
    def synchronizeOff(cls):
        """
        Unlock the whole class
        """
        cls.__semaphore.release()


    def getApplicationName(self):
        return self.__strName + "-" + self.__strVersion


    def getWorkingDir(self):
        """
        Getter for working dir
        @rtype: string
        @return working dir 
        """
        return self.__strWorkingDir


    def setWorkingDir(self, _strDir):
        """
        Setter for working dir
        @type _strDir: string
        @param _strDir: working dir 
        """
        self.__strWorkingDir = _strDir


    def isFailure(self):
        return self.__bIsFailure


    def setFailure(self, _bFailure):
        self.__bIsFailure = _bFailure


    def getPluginName(self):
        return self.__strPluginName

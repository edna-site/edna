#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source, Chilton, UK
#
#    Principal author: Graeme Winter (graeme.winter@diamond.ac.uk)
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

__authors__ = [ "Graeme Winter" ]
__contact__ = "graeme.winter@diamond.ac.uk"
__license__ = "LGPLv3+"
__copyright__ = "Diamond Light Source, Chilton, UK"

# I got this far... here's the plan:
# 
# This will encapsulate a Driver from the DriverFactory, so will be a 
# static class. The interface from the current ScriptPlugin will be 
# maintained.

"""
The purpose of this plugin execute class is to be subclassed for
creating plugins that execute external programs through the xia2core.
"""

# standard Python imports
import os
import shlex

# EDNA imports
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile
from EDPluginExec import EDPluginExec
from EDActionExecuteSystemCommand import EDActionExecuteSystemCommand
from EDConfiguration import EDConfiguration

from XSDataCommon import XSPluginItem

# import the DriverFactory - either from edna's xia2core or a separate
# one configured in the environment as XIA2CORE_ROOT.

if "XIA2CORE_ROOT" in os.environ and os.environ['XIA2CORE_ROOT'] != '':
    pathxia2core = os.path.join(os.environ['XIA2CORE_ROOT'], 'Python')
else:
    pathxia2core = EDFactoryPluginStatic.getModuleLocation('XIA2CoreVersion')
    os.environ["XIA2CORE_ROOT"] = os.path.dirname(pathxia2core)

EDVerbose.DEBUG('Found xia2core in %s' % pathxia2core)

EDFactoryPluginStatic.preImport("Driver", pathxia2core)

from Driver.DriverFactory import DriverFactory

class EDPluginExecProcessXIA2CORE(EDPluginExec):

    # static class variables

    CONF_EXEC_PROCESS_EXECUTABLE = "execProcessExecutable"
    CONF_EXEC_PROCESS_XIA2CORE_TYPE = "execProcessXIA2COREType"
    CONF_EXEC_PROCESS_VERSION_STRING = "execProcessXIA2COREVersionString"

    def __init__ (self):
        """
        Initializes process related attributes described above
        """
        EDPluginExec.__init__(self)
        self.__strExecutable = None
        self.__strVersion = None
        self.__listCompatibleVersions = []
        self.__strCommandline = ""
        self.__listCommandPreExecution = []
        self.__listCommandExecution = []
        self.__listCommandPostExecution = []
        self.__strLogFileName = None
        self.__strErrorLogFileName = None
        self.__listStandardOutput = []
        self.__listStandardError = []
        self.__strConfigXIA2COREType = None

        return

    def preProcess(self, _edObject=None):
        """
        Calls the parent preProcess method
        Generates the script
        """
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.preProcess")

        return

    def generateXIA2CORE(self, _edObject=None, executable=None):
        """Factory method to create and configure a xia2core Driver
        instance."""

        if executable is None:
            executable = self.getExecutable()

        if executable is None:
            raise RuntimeError, 'no executable set in factory'

        EDVerbose.DEBUG("Driver created for executable %s" % executable)

        driver = DriverFactory.Driver(self.__strConfigXIA2COREType)
        driver.set_executable(executable)
        driver.set_working_directory(self.getWorkingDirectory())

        return driver

    def process(self, _edObject=None):
        """
        This method starts the execution of the EDNA script using
        EDActionExecuteSystemCommand. In case of failure, an error
        message is added to the list and the plugin fails.
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.process starting")
        self.synchronizeOn()

        # FIXME from here will need to do some real programming

        self.launchProcessWithXIA2CORE()

        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.process finished ")
        self.synchronizeOff()


    def postProcess(self, _edObject=None):
        """
        Calls the parent preProcess method
        Checks that the installed 3rd party software is in the list of
        compatible versions
        """
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.postProcess")

        # Tests the compatibles executable versions
        listCompatibleVersions = self.getListOfCompatibleVersions()

        if(len(listCompatibleVersions) != 0):

            bFound = False
            for compatibleVersion in listCompatibleVersions:
                bFound = self.findStringInLog(compatibleVersion)
                if(bFound == True):
                    break

            if(bFound == False):
                strErrorMessage = "Plugin not compatible with %s, compatible versions are: %s" % \
                                  (self.getStringVersion(),
                                   self.getCompatibleVersionsStringLine())
                EDVerbose.warning(strErrorMessage)
                self.addWarningMessage(strErrorMessage)
                #self.setFailure()
                #if (EDVerbose.isVerboseDebug()):
                #    raise RuntimeError, strErrorMessage


    # why is this configuration not a separate thing? surely it would make
    # more sense to have a class which you pass a dictionary of wanted keys
    # which could do all of the setattr stuff and configuration reading
    # all in one place?

    def configure(self):
        """
        Configures the plugin from the configuration file with the following
        parameters
         - The shell that will execute the script
         - Script executor
         - Script executable to be invoked
         - Path to CCP4 setup file if required
         - The 3rd party executable installed version
        """
        EDPluginExec.configure(self)
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            EDVerbose.warning(
                "EDPluginExecProcessXIA2CORE.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()

        if (self.getExecutable() is None):
            strExecutable = EDConfiguration.getStringParamValue(
                xsPluginItem,
                EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_EXECUTABLE)
            if(strExecutable == None):
                strErrorMessage = "Configuration parameter missing: " + \
                                  EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_EXECUTABLE
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                if (EDVerbose.isVerboseDebug()):
                    raise RuntimeError, strErrorMessage
            else:
                # Check that the executable file exists
                if (os.path.exists(strExecutable) == False):
                    strErrorMessage = "Cannot find configured " + EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_EXECUTABLE + " : " + strExecutable
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                    if (EDVerbose.isVerboseDebug()):
                        raise RuntimeError, strErrorMessage
                else:
                    self.setExecutable(strExecutable)

        if (self.getConfigXIA2COREType() is None):
            strXIA2COREType = EDConfiguration.getStringParamValue(
                xsPluginItem,
                EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_XIA2CORE_TYPE)
            if(strXIA2COREType == None):
                strErrorMessage = "Configuration parameter not set: " + \
                                  EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_XIA2CORE_TYPE
                EDVerbose.DEBUG(strErrorMessage)
            else:
                # FIXME test that this is a legal name
                self.__strConfigXIA2COREType = strXIA2COREType

        strVersion = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_VERSION_STRING)
        if(strVersion == None):
            EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.configure: No configuration parameter found for: " + \
                            EDPluginExecProcessXIA2CORE.CONF_EXEC_PROCESS_VERSION_STRING + ", NO default value!")
        else:
            self.setStringVersion(strVersion)
        if (self.__strLogFileName == None):
            self.setLogFileName(self.getBaseName() + ".log")
        if (self.__strErrorLogFileName == None):
            self.setErrorLogFileName(self.getBaseName() + ".err")

        if self.__strExecutable is None:
            EDVerbose.ERROR("Executable not defined in configuration file")
            # shall we raise an exception?

        self.__strPathToHostNamePidFile = os.path.join(self.getWorkingDirectory(), os.path.basename(self.__strExecutable) + "_hostNamePid.txt")

        return

    def launchProcessWithXIA2CORE(self):
        """
        Launch a process using the xia2 core.
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.launchProcessWithXIA2CORE")

        # launch the preexecution steps
        for strCommandPreExecution in self.__listCommandPreExecution:
            split_command_line = shlex.split(str(strCommandPreExecution))
            executable = split_command_line[0]
            arguments = split_command_line[1:]
            driver = self.generateXIA2CORE(executable)
            for token in arguments:
                driver.add_command_line(token)
            driver.start()
            driver.close_wait()

        driver = self.generateXIA2CORE()
        for token in shlex.split(str(self.__strCommandline)):
            driver.add_command_line(token)
        driver.start()
        for record in self.__listCommandExecution:
            driver.input(record)
        if self.__strLogFileName:
            EDVerbose.DEBUG("Logging to %s in %s" % (self.__strLogFileName, self.getWorkingDirectory()))
            driver.write_log_file(os.path.join(self.getWorkingDirectory(), self.__strLogFileName))
        driver.close_wait()

        self.__listStandardOutput = driver.get_all_output()

        for strCommandPostExecution in self.__listCommandPostExecution:
            split_command_line = shlex.split(str(strCommandPreExecution))
            executable = split_command_line[0]
            arguments = split_command_line[1:]
            driver = self.generateXIA2CORE(executable)
            for token in arguments:
                driver.add_command_line(token)
            driver.start()
            driver.close_wait()

        # FIXME in here I need to check for errors

        return


    def getListOfCompatibleVersions(self):
        """
        Returns the list of compatible executable versions the plugin supports
        """
        return self.__listCompatibleVersions


    def addCompatibleVersion(self, _strCompatibleVersion):
        """
        Adds a compatible executable version to the list
        """
        self.__listCompatibleVersions.append(_strCompatibleVersion)


    def getCompatibleVersionsStringLine(self):
        """
        This Method constructs a string line by concatening the compatible versions this plugin supports
        This is for Log message purpose only.
        """
        strCompatibleVersionsStringLine = ""
        for compatibleVersion in self.getListOfCompatibleVersions():
            strCompatibleVersionsStringLine = strCompatibleVersionsStringLine + compatibleVersion + " ; "

        return strCompatibleVersionsStringLine

    # why are the following not defined in a super class which is standard
    # across the different exec plugins?


    def setListCommandExecution(self, _listCommandExecution):
        """
        Sets the list of execution commands
        """
        self.synchronizeOn()
        if (_listCommandExecution is not None):
            self.__listCommandExecution = list(_listCommandExecution)
        self.synchronizeOff()


    def addListCommandExecution(self, _strCommandExecution):
        """
        Adds an execution command to the list
        """
        self.synchronizeOn()
        if (_strCommandExecution is not None):
            self.__listCommandExecution.append(_strCommandExecution)
        self.synchronizeOff()


    def getListCommandExecution(self):
        """
        Returns the list of execution commands
        """
        self.synchronizeOn()
        edObject = None
        if (self.__listCommandExecution is not None):
            edObject = list(self.__listCommandExecution)
        self.synchronizeOff()
        return edObject


    def setListCommandPreExecution(self, _listCommandPreExecution):
        """
        Sets the list of pre execution commands
        """
        self.synchronizeOn()
        if (_listCommandPreExecution is not None):
            self.__listCommandPreExecution = list(_listCommandPreExecution)
        self.synchronizeOff()


    def addListCommandPreExecution(self, _strCommandPreExecution):
        """
        Adds a pre execution command to the list
        """
        self.synchronizeOn()
        if (_strCommandPreExecution is not None):
            self.__listCommandPreExecution.append(_strCommandPreExecution)
        self.synchronizeOff()


    def getListCommandPreExecution(self):
        """
        Returns the list of pre execution commands
        """
        self.synchronizeOn()
        edObject = None
        if (self.__listCommandPreExecution != None):
            edObject = list(self.__listCommandPreExecution)
        self.synchronizeOff()
        return edObject


    def setListCommandPostExecution(self, _listCommandPostExecution):
        """
        Sets the list of post execution commands
        """
        self.synchronizeOn()
        if (_listCommandPostExecution is not None):
            self.__listCommandPostExecution = list(_listCommandPostExecution)
        self.synchronizeOff()


    def addListCommandPostExecution(self, _strCommandPostExecution):
        """
        Adds a post execution command to the list
        """
        self.synchronizeOn()
        if (_strCommandPostExecution is not None):
            self.__listCommandPostExecution.append(_strCommandPostExecution)
        self.synchronizeOff()


    def getListCommandPostExecution(self):
        """
        Returns the list of post execution commands
        """
        self.synchronizeOn()
        edObject = None
        if (self.__listCommandPostExecution != None):
            edObject = list(self.__listCommandPostExecution)
        self.synchronizeOff()
        return edObject


    def setConfigXIA2COREType(self, _strXIA2COREType):
        """
        Sets the script shell
        """
        self.synchronizeOn()
        self.__strConfigXIA2COREType = _strXIA2COREType
        self.synchronizeOff()


    def getConfigXIA2COREType(self):
        """
        Returns the script shell
        """
        return self.__strConfigXIA2COREType


    def setLogFileName(self, _strLogFileName):
        """
        Sets the standard output log file name
        """
        self.synchronizeOn()
        self.__strLogFileName = _strLogFileName
        self.synchronizeOff()


    def setErrorLogFileName(self, _strErrorLogFileName):
        """
        Sets the error output log file name
        """
        self.synchronizeOn()
        self.__strErrorLogFileName = _strErrorLogFileName
        self.synchronizeOff()


    def getLogFileName(self):
        """
        Returns the standard output log file name
        """
        return self.__strLogFileName


    def getErrorLogFileName(self):
        """
        Returns the error output log file name
        """
        return self.__strErrorLogFileName

    def setExecutable(self, _strExecutable):
        """
        Sets the executable path
        """
        self.synchronizeOn()
        self.__strExecutable = _strExecutable
        self.synchronizeOff()


    def getExecutable(self):
        """
        Returns the executable path
        """
        returnValue = self.__strExecutable
        if (returnValue is not None):
            returnValue = self.__strExecutable
        return returnValue

    def setCommandline(self, _strCommandline):
        """
        Sets the script command line (parameters to executable)
        """
        self.synchronizeOn()
        self.__strCommandline = _strCommandline
        self.synchronizeOff()


    def getCommandline(self):
        """
        Returns the script command line (parameters to executable)
        """
        return self.__strCommandline


    def setStringVersion(self, _strVersion):
        """
        Sets the executable version
        """
        self.synchronizeOn()
        self.__strVersion = _strVersion
        self.synchronizeOff()


    def getStringVersion(self):
        """
        Returns the executable version
        """
        returnValue = None
        if (self.__strVersion is not None):
            returnValue = self.__strVersion
        return returnValue


    def setPathToHostNamePidFile(self, _strPathToHostNamePidFile):
        """
        Sets the executable version
        """
        self.__strPathToHostNamePidFile = _strPathToHostNamePidFile


    def getPathToHostNamePidFile(self):
        """
        Returns the executable version
        """
        return self.__strPathToHostNamePidFile

    def findStringInLog(self, _strInput):
        """
        Returns True if a string exists in the log file
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.findStringInLog")
        for record in self.__listStandardOutput:
            if _strInput in record:
                return True
        return False

    def writeProcessFile(self, _strFileName, _strContent):
        """
        Main method to write a file in the plugin working directory
        Such a file is called process file
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.writeProcessFile")
        strFilePath = os.path.join(self.getWorkingDirectory(), _strFileName)
        EDUtilsFile.writeFile(strFilePath, _strContent)


    def readProcessFile(self, _strFileName):
        """
        Returns the file content of a process file
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.readProcessFile")
        strFilePath = os.path.join(self.getWorkingDirectory(), _strFileName)
        strFileContent = None
        if os.path.exists(strFilePath):
            strFileContent = EDUtilsFile.readFile(strFilePath)
        return strFileContent


    def readProcessLogFile(self):
        """
        Returns the content of the process standard output log file
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.readProcessLogFile")
        return ''.join(self.__listStandardOutput)

    def readProcessErrorLogFile(self):
        """
        Returns the content of the process error output log file
        """
        EDVerbose.DEBUG("EDPluginExecProcessXIA2CORE.readProcessErrorLogFile")
        return ''.join(self.__listStandardError)

    def getScriptBaseName(self):
        return self.getBaseName()
